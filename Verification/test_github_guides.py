"""Verify navigation and scientific equations in the GitHub-readable guides.

Run with: python -m unittest discover -s Verification -p test_github_guides.py -v
Only the Python standard library is needed; no simulation is performed.
"""

from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


def markdown_files():
    """Include published and newly written guides; ignore local private files."""
    names = subprocess.check_output([
        'git', '-C', str(ROOT), 'ls-files', '--cached', '--others',
        '--exclude-standard', '-z',
    ]).decode('utf-8').split('\0')
    return sorted({ROOT / name for name in names
                   if name.endswith('.md') and (ROOT / name).is_file()})


class GitHubGuideVerification(unittest.TestCase):
    def test_relative_links_reach_files(self):
        """Catch missing pages, wrongly cased filenames and broken figure paths."""
        errors = []
        count = 0
        for page in markdown_files():
            text = re.sub(r'```.*?```', '', page.read_text(encoding='utf-8'), flags=re.S)
            for address in re.findall(r'\]\(([^\n)]+)\)', text):
                address = address.strip('<>')
                url = urlsplit(address)
                if url.scheme or url.netloc:
                    continue
                target = (page.parent / unquote(url.path)).resolve() if url.path else page
                count += 1
                if not target.exists():
                    errors.append(f'{page.relative_to(ROOT)}: {address}')
                    continue
                # Windows tolerates incorrect case; Linux and GitHub do not.
                if target.is_relative_to(ROOT):
                    current = ROOT
                    for part in target.relative_to(ROOT).parts:
                        if part not in {entry.name for entry in current.iterdir()}:
                            errors.append(f'Incorrect filename case: {address}')
                            break
                        current = current / part
        self.assertGreater(count, 500)
        self.assertEqual(errors, [])

    def test_numbered_equations_retain_the_scientific_source(self):
        equations = json.loads((ROOT / 'Documentation/equations.json').read_text(encoding='utf-8'))
        methods = (ROOT / 'Documentation/model_methods.md').read_text(encoding='utf-8')
        for equation in equations:
            latex = equation['latex'].replace(r'\!', '')
            self.assertIn(latex + r'\tag{' + str(equation['number']) + '}', methods)

    def test_guides_fit_github_and_avoid_unpublished_website_links(self):
        for page in markdown_files():
            text = page.read_text(encoding='utf-8')
            self.assertLess(page.stat().st_size, 450000, str(page))
            self.assertNotIn('https://smarahmati.github.io/Cat-FullBody-Neuromechanics/', text, str(page))
            self.assertNotIn('The website is available after its first successful deployment.', text, str(page))
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertNotIn(r'\!', readme)


if __name__ == '__main__':
    unittest.main()
