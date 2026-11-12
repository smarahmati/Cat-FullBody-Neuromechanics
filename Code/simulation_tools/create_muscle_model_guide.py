"""Build the illustrated muscle guide from the current editable configuration.

Run this file after changing muscle parameters to refresh the documentation.
It reads dictionaries and existing equation documentation; it does not run or
alter the forward model. Outputs are Documentation/muscle_model.html and its
parameter snapshot. The editable SVG schematic is in Documentation/Figures_and_Videos.
"""
from pathlib import Path
import html
import json
import re
import runpy

ROOT = Path(__file__).resolve().parents[2]
PARAM = ROOT / 'Data/Model_Parameters'
DOC = ROOT / 'Documentation'


def read_dictionary(filename):
    """Read the same PARAMETERS dictionary a fresh simulation will use."""
    return runpy.run_path(str(PARAM / filename))['PARAMETERS']


def main():
    """Create an offline-readable figure, parameter selector and equation guide."""
    muscles = read_dictionary('muscle_tendon.py')
    activation = read_dictionary('activation.py')
    initial = read_dictionary('initial_state.py')['muscles']
    shared = runpy.run_path(str(PARAM / 'formulation_constants.py'))
    numerical = runpy.run_path(str(PARAM / 'numerical_parameters.py'))
    records = json.loads((PARAM / 'PARAMETER_PROVENANCE.json').read_text(encoding='utf-8'))['parameters']
    descriptions = {}
    for row in records:
        if row['category'] in ['muscle_tendon', 'activation']:
            descriptions[row['field']] = {'unit': row['unit'], 'meaning': row['meaning']}
    payload = {'muscles': muscles, 'activation': activation, 'initial': initial,
               'descriptions': descriptions, 'source': 'Current editable Data/Model_Parameters dictionaries'}
    (DOC / 'muscle_model_parameters.json').write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')

    # Use the same rendered equations and immediate definitions as the methods.
    # This avoids maintaining a second, potentially inconsistent constitutive law.
    methods = (DOC / 'model_methods.html').read_text(encoding='utf-8')
    equations = []
    for number in range(2, 14):
        match = re.search(r'<h3>' + str(number) + r'\. (.*?)(?=<h[23]>|</main>)', methods, re.S)
        if not match:
            raise ValueError(f'Equation {number} was not found in the methods guide.')
        heading, body = match.group(1).split('</h3>', 1)
        equations.append('<details' + (' open' if number == 3 else '') + '><summary>' +
                         html.escape(str(number)) + '. ' + heading + '</summary>' + body + '</details>')

    constant_meanings = {
        'ACTIVE_LENGTH_POWER': ('1', 'Power p in the active force–length curve; current source shape p = 1.55.'),
        'ACTIVE_LENGTH_WIDTH': ('1', 'Width w in the active force–length curve; current source shape w = 0.55.'),
        'PASSIVE_LENGTH_SCALE': ('1', 'Scale cP = 0.0075 in the tension-only passive exponential.'),
        'PASSIVE_LENGTH_EXPONENT': ('1', 'Exponent kP = 11.6 controlling passive force rise beyond optimal length.'),
        'PASSIVE_EXPONENT_CAP': ('1', 'Numerical overflow safeguard, not a measured tissue property.'),
        'FV_D1': ('1', 'De Groote force–velocity coefficient d1.'),
        'FV_D2': ('1', 'De Groote force–velocity coefficient d2.'),
        'FV_D3': ('1', 'De Groote force–velocity coefficient d3.'),
        'FV_D4': ('1', 'De Groote force–velocity coefficient d4.'),
        'TENDON_TOE_CURVATURE': ('1', 'ktoe: exponential toe-region curvature. Toe-to-linear transition is derived for force and slope continuity.'),
    }
    rows = ''
    for key, (unit, meaning) in constant_meanings.items():
        rows += '<tr>' + ''.join('<td>' + html.escape(str(x)) + '</td>' for x in [key, unit, shared[key], meaning]) + '</tr>'
    numeric_rows = ''
    for key, value in numerical.items():
        if key.startswith(('MINIMUM_FIBER', 'MINIMUM_LENGTH', 'MAXIMUM_FIBER', 'FIBER_', 'NEWTON_')):
            numeric_rows += '<tr><td>' + html.escape(key) + '</td><td>' + html.escape(str(value)) + '</td></tr>'
    options = ''.join('<option value="' + html.escape(name) + '"' + (' selected' if name == 'FR_BicepsBrachii' else '') + '>' + html.escape(name) + '</option>' for name in muscles)
    page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Excitation to muscle force · Illustrated Hill-type model</title><link rel="stylesheet" href="style.css">
<style>.muscle-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px}.muscle-grid article{background:white;border:1px solid #cbdde4;border-radius:12px;padding:18px}.inactive{color:#637683;background:#f0f2f3}button{font:inherit;padding:10px 15px;margin:4px;border:1px solid #087f8a;border-radius:7px;background:white;color:#086878;cursor:pointer}select{font:inherit;padding:10px;max-width:100%}figure{margin:20px 0}figcaption{font-size:14px;color:#476674}#muscle-parameters code{font-size:12px}#muscle-parameters th{position:sticky;top:0}.parameter-note{background:#e6f5f3;padding:16px}</style></head><body>
<header><div class="tag">Cat · Full-body neuromechanics</div><h1>How excitation produces muscle force</h1><p>The Hill-type muscle and elastic tendon implemented in this release.</p>
<nav><a href="../START_HERE.html">Start here</a><a href="model_methods.html">All equations</a><a href="parameter_tables.html">Source-to-model parameters</a><a href="References/index.html">References</a></nav></header><main>
<p class="note"><strong>Excitation is a command; activation is a dynamic state; tendon force is a mechanical result.</strong>
Force depends on activation, fiber length and velocity, tendon stretch, pennation and muscle parameters. The same excitation need not produce the same force when the limb is in a different mechanical state.</p>
<h2>The elements actually used in this analysis</h2>
<p><strong>Passive fiber force is included in all 104 channels: 76 forelimb and 28 hindlimb.</strong> Elastic tendons and fiber damping are included in both. The figures show the applied equations, not an optional menu of elements.</p>
<p><a href="passive_fiber_mechanics.html">Passive force–length relationship and verification</a></p>
<p id="diagram-status" class="parameter-note">All four limbs: passive fiber branch included.</p>
<figure><img id="muscle-schematic" src="Figures_and_Videos/hill_muscle_model.svg" alt="Excitation activates a Hill-type muscle: active contractile element, passive fiber tissue included in all limbs, and damping in parallel, in series with an elastic tendon; constant pennation partitions fiber and tendon length.">
<figcaption>Project-specific schematic, not an anatomical scale drawing or a figure copied from a paper. Fiber contributions are written in the implemented tendon-force normalization. <a id="full-figure-link" href="Figures_and_Videos/hill_muscle_model.svg">Open the scalable figure</a> · <a id="detail-figure-link" href="Figures_and_Videos/hill_muscle_pennation_detail.svg">Enlarge the main panel with pennation angle α</a>.</figcaption></figure>
<div class="muscle-grid">
<article><h3>1. Motor command</h3><p>u(t), from 0 to 1, is read from the fixed excitation table. The same prescribed cycle is repeated throughout the forward calculation.</p></article>
<article><h3>2. Activation dynamics</h3><p>Activation a(t) rises and falls with finite activation/deactivation time constants. It does not instantaneously become equal to excitation.</p></article>
<article><h3>3. Mechanical equilibrium</h3><p>The elastic solver finds fiber length such that tendon tension balances active, passive and damping contributions. Tendon length changes as the total path and fiber length change.</p></article>
<article><h3>4. Coupled movement</h3><p>The resulting tendon force acts along the muscle path. Its moment arms convert it to joint loading. All four limbs, the trunk and paw contacts participate in the coupled forward dynamics.</p></article></div>
<h2>What is each element?</h2>
<table><tr><th>Element</th><th>Meaning</th><th>Parameters / states</th></tr>
<tr><td>CE: active contractile element</td><td>Activation-dependent force multiplied by force–length and force–velocity factors.</td><td>a, F0, lopt, vmax, active exponent ρ; shared curve constants p, w and d1–d4.</td></tr>
<tr><td>PE: parallel elastic element</td><td>Included for all 104 channels in the current analysis. It produces tensile force when fiber length exceeds optimal length. It is distinct from tendon elasticity.</td><td>Passive switch sP; scale cP; exponent kP; normalized fiber length λ.</td></tr>
<tr><td>D: viscous fiber damping</td><td>Velocity-dependent contribution βν to normalized equilibrium. Its sign follows fiber velocity; it is not a separate neural input.</td><td>β, ν; ν is positive when the fiber lengthens.</td></tr>
<tr><td>SE: series elastic tendon</td><td>No tensile force at or below slack length; nonlinear exponential toe region followed by a linear region. Tendon stretch is a computed outcome.</td><td>ls, ε0, ktoe and F0. ε0 is tendon strain when force equals F0.</td></tr>
<tr><td>Pennation and geometry</td><td>The fiber makes a constant angle α with the tendon axis. LMT = lf cos α + lT. Whole MT length comes from origin/insertion, via/wrap paths and a fixed length offset.</td><td>cos α, ΔL and attachment/routing geometry; q is the current skeletal configuration.</td></tr>
<tr><td>Initial state and integration</td><td>a(0) and lf(0) initialize the muscle once. A backward-Euler fiber-velocity estimate and safeguarded force-equilibrium solve update fiber length.</td><td>Initial activation, fiber length, mechanical time step and numerical tolerances.</td></tr></table>
<p class="parameter-note"><strong>Two implementation details:</strong> Passive fiber force is ON in all channels. It can nevertheless be zero when a fiber is shorter than its passive stretch threshold. The tendon is elastic in all channels. Also, F0 is already a tendon-projected maximum isometric force; applying an additional cos α factor to the force would double-project it. The implementation uses α in the length partition and holds it constant.</p>
<h2>Passive fiber force and its sources</h2>
<p>The current model uses the passive exponential in Prilutsky et al. (2016), Table 10.3, and Rahmati et al. (2025), Table 3, with coefficients 0.0075 and 11.6. It is enabled in all limb channels, inside the elastic force-equilibrium solve. This constitutive law is part of the muscle equilibrium equations for every limb.</p>
<p>Zeroing compressive values and limiting the exponent for overflow protection are explicit adaptations. Extending one normalized law to added channels is an assumption, not muscle-specific passive calibration. The passive curve coefficients are taken from the cited publications; they are not fitted to this walking trial. <a href="passive_fiber_mechanics.html">Passive-force equation and stretch verification</a>.</p>
<h2>Inspect every parameter for one muscle</h2>
<p>Select a muscle below. These values come from the editable configuration when this guide was generated. They do not change the running model. Edit the linked Python files and start a new simulation to apply changes.</p>
<label for="muscle-choice"><strong>Muscle:</strong></label> <select id="muscle-choice">OPTIONS</select>
<p id="muscle-state" class="parameter-note"></p>
<table id="muscle-parameters"><thead><tr><th>Configuration parameter</th><th>Value</th><th>Unit</th><th>Meaning and current use</th><th>File</th></tr></thead><tbody></tbody></table>
<p><a href="../Data/Model_Parameters/ATTACHMENT_MAP.html">Origins, insertions, via points and wrapping</a> · <a href="muscle_model_parameters.json">Exact parameter snapshot</a> · <a href="parameter_tables.html">Source values and calibration explanations</a>.</p>
<h2>Shared curve constants</h2>
<p>These constants are shared by muscle channels. The selected muscle’s exponent, strength, lengths, speed and switches still differ by channel. Edit <a href="../Data/Model_Parameters/formulation_constants.py">formulation_constants.py</a> and start a new process to apply a change.</p>
<table><tr><th>Parameter</th><th>Unit</th><th>Value</th><th>Meaning</th></tr>CONSTANT_ROWS</table>
<p>The tendon’s normalized force at the toe-region endpoint is fixed at 0.33; the remaining rise to normalized force 1 is 0.67. These constants are in <a href="../Code/neuromechanics/elastic_tendon_force.py">elastic_tendon_force.py</a> and <a href="../Code/neuromechanics/elastic_tendon_transition.py">elastic_tendon_transition.py</a>, not separate configuration entries. The transition strain is derived from ε0 and ktoe to keep force and stiffness continuous. The exact piecewise equation is below.</p>
<h2>Implemented equations, with every symbol defined</h2>
<p>Open each equation to inspect its formulation, definitions and corresponding code. These are the same equations as the full methods guide. The alternative source force–velocity curve is documented but inactive when the De Groote switch is 1.</p>
EQUATIONS
<details><summary>Numerical solver settings (not tissue properties)</summary>
<p>These settings control solution accuracy and geometric safeguards. Read <a href="../Data/Model_Parameters/numerical_parameters.py">numerical_parameters.py</a> for units and comments. The mechanical time step is in <a href="../Data/Model_Parameters/environment.py">environment.py</a>; the default integration step is approximately 0.000125 s.</p>
<table><tr><th>Setting</th><th>Value</th></tr>NUMERIC_ROWS</table></details>
<h2>If excitation becomes zero, does force vanish immediately?</h2>
<p>No. Activation first decays according to its time constant. Stretched tendon can retain tension, and passive fiber force can remain. The evolving muscle–tendon and skeletal states determine how force changes. The model therefore distinguishes zero excitation, zero activation and zero tendon force.</p>
<h2>Scientific sources and project choices</h2>
<p>The source muscle geometry/curves are documented with the author’s MATLAB hindlimb Model 3 dataset (bundled under Data/Original_Study_Data/hindlimb), <a href="References/index.html#Rahmati2025">Rahmati et al.</a> and the <a href="References/index.html">Prilutsky chapter and supporting literature</a>. The applied force–velocity adaptation is described in <a href="../Code/neuromechanics/muscle_force_velocity_degroote.py">muscle_force_velocity_degroote.py</a> and the methods guide’s De Groote/OpenSim references. Elastic tendon, the constant-pennation formulation, passive-force switches, fitted values and numerical safeguards are disclosed implementation choices; this assembled model is not an exact reproduction of a single paper.</p>
<p>To refresh this page after parameter edits, run <code>python Code/simulation_tools/create_muscle_model_guide.py</code> from the repository root. The reusable SVG is in <code>Documentation/Figures_and_Videos/hill_muscle_model.svg</code>.</p>
</main><footer>Hill-type muscle guide · all files work locally without an internet connection · model values are editable separately.</footer>
<script id="muscle-data" type="application/json">PAYLOAD</script>
<script>
const data = JSON.parse(document.getElementById('muscle-data').textContent);
const selector = document.getElementById('muscle-choice');
function number(x) { return typeof x === 'number' ? Number(x.toPrecision(8)).toString() : JSON.stringify(x); }
function addRow(body, name, value, unit, meaning, file, inactive=false) {
  const row=document.createElement('tr'); if(inactive) row.className='inactive';
  for(const content of [name, number(value), unit, meaning]) { const cell=document.createElement('td'); cell.textContent=content; row.appendChild(cell); }
  const cell=document.createElement('td'), link=document.createElement('a'); link.href='../Data/Model_Parameters/'+file; link.textContent=file; cell.appendChild(link); row.appendChild(cell); body.appendChild(row);
}
function updateMuscle() {
  const name=selector.value, muscle=data.muscles[name], act=data.activation[name], body=document.querySelector('#muscle-parameters tbody'); body.replaceChildren();
  const isFore=name.startsWith('FL_') || name.startsWith('FR_');
  const schematic=document.getElementById('muscle-schematic');
  const full='hill_muscle_model.svg';
  const detail='hill_muscle_pennation_detail.svg';
  schematic.src='Figures_and_Videos/'+full;
  schematic.alt='Applied muscle model with active force, passive fiber branch, damping, elastic tendon and pennation.';
  document.getElementById('full-figure-link').href='Figures_and_Videos/'+full;
  document.getElementById('detail-figure-link').href='Figures_and_Videos/'+detail;
  document.getElementById('diagram-status').textContent=name+' — passive fiber force INCLUDED; elastic tendon and fiber damping included.';
  const alpha=Math.acos(Math.max(-1,Math.min(1,muscle.pennation_cosine)))*180/Math.PI;
  document.getElementById('muscle-state').textContent=name+' | Pennation α = '+alpha.toFixed(3)+'° (derived from cos α) | Passive fiber force '+(muscle.passive_fiber_enabled ? 'ON' : 'OFF')+' | Elastic tendon ON | Force–velocity: '+(muscle.degroote_force_velocity_enabled ? 'De Groote' : 'source law');
  for(const [key,value] of Object.entries(act)) { const info=data.descriptions[key]||{}; addRow(body,key,value,info.unit||'',info.meaning||'Activation-dynamics setting','activation.py'); }
  for(const [key,value] of Object.entries(muscle)) {
    const info=data.descriptions[key]||{}, inactive=!!muscle.degroote_force_velocity_enabled && ['source_shortening_curvature','source_lengthening_curvature'].includes(key);
    addRow(body,key,value,info.unit||'',(info.meaning||'Muscle parameter')+(inactive?' Inactive in this run because De Groote force–velocity is enabled.':''),'muscle_tendon.py',inactive);
  }
  for(const [key,value] of Object.entries(data.initial[name]||{})) { addRow(body,key,value,key.includes('length')?'m':'1','Initial muscle state; used once at t = 0.','initial_state.py'); }
}
function chooseDiagram(name) { selector.value=name; updateMuscle(); }
selector.addEventListener('change',updateMuscle);updateMuscle();
</script></body></html>'''
    page = (page.replace('OPTIONS', options).replace('CONSTANT_ROWS', rows)
            .replace('NUMERIC_ROWS', numeric_rows).replace('EQUATIONS', ''.join(equations))
            .replace('PAYLOAD', json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c')))
    (DOC / 'muscle_model.html').write_text(page, encoding='utf-8')
    print(f'Wrote illustrated guide and {len(muscles)} muscle parameter records.')


if __name__ == '__main__':
    main()
