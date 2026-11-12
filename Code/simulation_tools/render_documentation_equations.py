"""Prepare self-contained equation figures for the GitHub documentation.

Scientific LaTeX remains editable in Documentation/equations.json. Other formulas
are transcribed from the HTML MathML or the README. Figures use outlined glyphs,
so viewing the guides needs neither JavaScript nor an installed mathematical font.
MathJax is needed only to build a new or changed figure; existing figures are reused.
"""

from pathlib import Path
import hashlib
import json
import re
import subprocess


ROOT = Path(__file__).resolve().parents[2]
FIGURES = ROOT / 'Documentation/Figures_and_Videos/Equations'
RENDERER = Path(__file__).with_name('equation_renderer') / 'render_equations.cjs'


class EquationFigures:
    """Collect equations, preserve their sources and render only changed figures."""

    def __init__(self):
        self.entries = {}
        self.previous = {}
        manifest = FIGURES / 'equation_sources.json'
        if manifest.exists():
            self.previous = json.loads(manifest.read_text(encoding='utf-8'))

    def register(self, latex, label, key, number=None, inline=False):
        """Return a stable figure path without changing the scientific equation."""
        key = re.sub(r'[^a-z0-9_]+', '_', key.lower()).strip('_')
        formula = latex.replace(r'\!', '')
        # Put long groups on separate lines without changing their expressions.
        rendered = formula
        if (len(formula) > 180 or str(number) == '20') and re.search(r'\\q(?:q)?uad\b', formula):
            parts = re.split(r'\\(?:qquad|quad)\b', formula)
            rendered = r'\begin{gathered}' + r' \\ '.join(parts) + r'\end{gathered}'
        if key == 'calibration_summary_01':
            # This long sum needs two lines at ordinary document width.
            marker = r'+30'
            rendered = rendered.replace(marker, r' \\ {}+30', 1)
            rendered = r'\begin{gathered}' + rendered + r'\end{gathered}'
        entry = dict(latex=latex, rendered_latex=rendered, label=label,
                     number=number, inline=inline, file=key + '.svg')
        digest = json.dumps(entry, sort_keys=True).encode() + RENDERER.read_bytes()
        entry['render_hash'] = hashlib.sha256(digest).hexdigest()
        self.entries[key] = entry
        return (FIGURES / entry['file']).relative_to(ROOT).as_posix()

    def preserve_readme_figures(self, text):
        """Keep sources for hand-maintained README figures across regeneration."""
        for key, entry in self.previous.items():
            if key.startswith('readme_') and entry['file'] in text:
                self.register(entry['latex'], entry['label'], key,
                              entry['number'], entry['inline'])

    def write(self):
        """Render a batch with MathJax, then save a complete editable source index."""
        FIGURES.mkdir(parents=True, exist_ok=True)
        changed = [entry for key, entry in self.entries.items()
                   if self.previous.get(key, {}).get('render_hash') != entry['render_hash']
                   or not (FIGURES / entry['file']).exists()]
        if changed:
            subprocess.run(['node', str(RENDERER), str(FIGURES)],
                           input=json.dumps(changed), encoding='utf-8', check=True)
        (FIGURES / 'equation_sources.json').write_text(
            json.dumps(self.entries, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        (FIGURES / 'README.md').write_text(
            '# Equation figures\n\n'
            'Scalable equation figures used by the GitHub guides. Symbols are stored '
            'as vector outlines; no browser math extension is needed.\n\n'
            '- [Methods and symbol definitions](../../model_methods.md)\n'
            '- [Numbered scientific equation sources](../../equations.json)\n'
            '- [Complete figure sources](equation_sources.json)\n'
            '- [Documentation build instructions](../../publishing.md)\n', encoding='utf-8')
        print(f'Equation figures: {len(self.entries)}; rendered {len(changed)}.')

