"""Package the existing HTML documentation for GitHub Pages.

This script does not run, fit or alter the neuromechanical model. It copies public
documentation and supporting files into a NEW output directory, preserving the
relative paths used by downloaded HTML. Large raw Results arrays stay in GitHub;
links to those arrays are rewritten to their exact repository revision.

Parameters:
  --output: new/empty folder for the website, usually _site in GitHub Actions.
  --repository: GitHub owner/name; defaults to the confirmed publication address.
  --revision: commit or branch used for links to downloadable raw result files.
  --include-untracked: local preview only; honor .gitignore for these files too.

Example (from repository root):
  python Code/simulation_tools/build_documentation_website.py --output _site

Only Python's standard library and Git are needed; no simulation dependencies.
"""

from pathlib import Path, PurePosixPath
from html.parser import HTMLParser
from urllib.parse import quote, unquote, urlsplit
import argparse
import html
import json
import os
import posixpath
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REPOSITORY = 'smarahmati/Cat-FullBody-Neuromechanics'
ROOT_PAGES = {'index.html', 'START_HERE.html', '.nojekyll', 'README.md',
              'LICENSE', 'THIRD_PARTY_NOTICES.md', 'CITATION.cff',
              'run.py', 'view.py', 'reproduce.py', 'requirements.txt',
              'requirements-lock.txt', 'Run Simulation.cmd', 'Setup Windows.cmd'}
RESULT_WEB_TYPES = {'.html', '.png', '.svg', '.jpg', '.jpeg', '.gif', '.json'}
LINK_ATTRIBUTE = re.compile(r'(?P<key>\b(?:href|src|data|poster|xlink:href))\s*=\s*(?P<quote>[\"\x27])(?P<url>.*?)(?P=quote)', re.I)


def forbidden_path(relative):
    """Keep ignored environments, private reading copies and restricted meshes out."""
    parts = PurePosixPath(relative).parts
    return (any(part in {'.git', '.venv', '__pycache__', '.idea', '_site'} for part in parts)
            or relative.startswith('Documentation/References/Local_Papers/')
            or relative.startswith('Data/Skeletal_Geometry/Model/meshes/'))


def public_repository_files(root, include_untracked=False):
    """Use Git's publication inventory, never a recursive copy of the workstation."""
    command = ['git', '-C', str(root), 'ls-files', '--cached', '-z']
    if include_untracked:
        command += ['--others', '--exclude-standard']
    names = subprocess.check_output(command).decode('utf-8').split('\0')
    return {name for name in names if name and not forbidden_path(name)
            and (root / name).is_file() and not (root / name).is_symlink()}


def belongs_in_website(relative):
    """Include reports and assets; leave large raw simulation arrays in GitHub."""
    if forbidden_path(relative):
        return False
    if relative in ROOT_PAGES:
        return True
    if relative.startswith(('Documentation/', 'Code/', 'Data/', 'Verification/')):
        return True
    if relative.startswith('Simulation_Results/'):
        # These snapshots remain reproducibility downloads, not duplicated web pages.
        if any(part in {'Model_Parameters_Used', 'Experimental_References_Used', 'Simulation_Code_Used'}
               for part in PurePosixPath(relative).parts):
            return False
        return PurePosixPath(relative).suffix.lower() in RESULT_WEB_TYPES
    return False


def local_target(page, link):
    """Resolve a relative HTML link using POSIX rules, also on Windows."""
    parsed = urlsplit(html.unescape(link))
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    # Root-relative links break GitHub project-site prefixes: keep links relative.
    if parsed.path.startswith('/'):
        raise ValueError(f'Root-relative link in {page}: {link}')
    target = posixpath.normpath(posixpath.join(posixpath.dirname(page), unquote(parsed.path)))
    if target == '..' or target.startswith('../'):
        raise ValueError(f'Link escapes the project in {page}: {link}')
    return target


def resolve_link(page, link, included, public, repository, revision):
    """Retain local pages and direct omitted public downloads to GitHub."""
    target = local_target(page, link)
    if target is None:
        return link
    parsed = urlsplit(html.unescape(link))
    suffix = ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')
    if target in included:
        return link
    # Directory URLs should resolve to explicit index pages on file:// and HTTP.
    index = target.rstrip('/') + '/index.html'
    if index in included:
        return posixpath.relpath(index, posixpath.dirname(page) or '.') + suffix
    if target in public:
        return f'https://github.com/{repository}/blob/{quote(revision, safe="")}/{quote(target, safe="/")}' + suffix
    if any(p.startswith(target.rstrip('/') + '/') for p in public):
        return f'https://github.com/{repository}/tree/{quote(revision, safe="")}/{quote(target, safe="/")}' + suffix
    raise ValueError(f'Missing or non-public linked file in {page}: {link}')


def prepare_html(page, source, included, public, repository, revision):
    """Rewrite attributes inside real tags, leaving JavaScript and source listings intact."""
    class Rewrite(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.output = []

        def start_tag(self, tag):
            raw = self.get_starttag_text()
            def replace(match):
                old = match['url']
                new = resolve_link(page, old, included, public, repository, revision)
                return match['key'] + '=' + match['quote'] + html.escape(html.unescape(new), quote=True) + match['quote']
            self.output.append(LINK_ATTRIBUTE.sub(replace, raw))

        handle_starttag = lambda self, tag, attrs: self.start_tag(tag)
        handle_startendtag = lambda self, tag, attrs: self.start_tag(tag)
        handle_endtag = lambda self, tag: self.output.append('</' + tag + '>')
        handle_data = lambda self, data: self.output.append(data)
        handle_entityref = lambda self, name: self.output.append('&' + name + ';')
        handle_charref = lambda self, name: self.output.append('&#' + name + ';')
        handle_comment = lambda self, data: self.output.append('<!--' + data + '-->')
        handle_decl = lambda self, decl: self.output.append('<!' + decl + '>')
        handle_pi = lambda self, data: self.output.append('<?' + data + '>')

    parser = Rewrite()
    parser.feed(source)
    parser.close()
    return ''.join(parser.output)


def validate_website(output):
    """Fail the build if an HTML/SVG link, image, video or stylesheet is missing."""
    checked = 0
    for path in sorted(output.rglob('*')):
        if path.suffix.lower() not in {'.html', '.svg'}:
            continue
        page = path.relative_to(output).as_posix()
        class Collect(HTMLParser):
            def handle_starttag(self, tag, attrs):
                nonlocal checked
                for key, link in attrs:
                    if key not in {'href', 'src', 'data', 'poster', 'xlink:href'} or not link:
                        continue
                    target = local_target(page, link)
                    if target is not None:
                        checked += 1
                        if not (output / target).is_file():
                            raise ValueError(f'Broken website link: {page} -> {link}')
        parser = Collect()
        parser.feed(path.read_text(encoding='utf-8'))
    return checked


def build_website(output, repository, revision, include_untracked=False):
    """Create a new static artifact; leave original files and simulation data intact."""
    output = Path(output).resolve()
    if output == ROOT or output in ROOT.parents:
        raise ValueError('The output must be a new folder, not the project or its parent.')
    if output.exists() and any(output.iterdir()):
        raise FileExistsError('Choose a new/empty output folder; existing output is not deleted.')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Repository must be owner/name.')
    public = public_repository_files(ROOT, include_untracked)
    included = {name for name in public if belongs_in_website(name)}
    if not {'index.html', 'START_HERE.html'} <= included:
        raise ValueError('Missing entry pages. Commit the project first, or use --include-untracked for local preview.')
    output.mkdir(parents=True, exist_ok=True)
    for name in sorted(included):
        src, dst = ROOT / name, output / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() in {'.html', '.svg'}:
            text = prepare_html(name, src.read_text(encoding='utf-8'), included, public, repository, revision)
            dst.write_text(text, encoding='utf-8')
        else:
            shutil.copyfile(src, dst)
    count = validate_website(output)
    size = sum((output / name).stat().st_size for name in included)
    if size > 900 * 1024 * 1024:
        raise ValueError('Website exceeds the 900 MiB packaging budget; keep large arrays in the repository.')
    audit = {'repository': repository, 'revision': revision, 'files': len(included),
             'bytes': size, 'checked_local_links': count, 'broken_links': [],
             'model_recomputed': False, 'raw_result_arrays_on_website': False,
             'private_papers_or_restricted_meshes_included': False}
    (output / 'WEBSITE_BUILD.json').write_text(json.dumps(audit, indent=2), encoding='utf-8')
    print(json.dumps(audit, indent=2))
    return audit


def main():
    """Read publishing options; GitHub supplies repository and commit automatically."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / '_site')
    parser.add_argument('--repository', default=os.environ.get('WEBSITE_REPOSITORY', DEFAULT_REPOSITORY))
    parser.add_argument('--revision', default=os.environ.get('WEBSITE_REVISION', 'main'))
    parser.add_argument('--include-untracked', action='store_true')
    args = parser.parse_args()
    build_website(args.output, args.repository, args.revision, args.include_untracked)


if __name__ == '__main__':
    main()
