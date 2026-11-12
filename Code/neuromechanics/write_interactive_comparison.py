"""Export a browser-based time-window comparison of joint angles and paw GRFs.

This function reads saved output only. It neither reruns nor filters the model.
The HTML embeds the complete sampled series and works without an internet
connection. Display values are rounded to six decimals; raw NPZ/CSV stay intact.
"""
import json
import os
from pathlib import Path
import numpy as np
from model_configuration.paths import ROOT
from .experimental_comparison_targets import experimental_comparison_targets


def write_interactive_comparison(result, settings, folder):
    """Write selectable 1/2/4/8-second or full-trial views with a time slider."""
    folder = Path(folder)
    target = experimental_comparison_targets(result['time'], settings['period_s'], settings.get('reference_table_dir'))
    labels = ['LH — assumed mirror', 'RH — recorded', 'LF — separate study', 'RF — separate study']
    payload = {'time': np.round(result['time'], 6).tolist(), 'kinematics': [], 'forces': []}
    for side in range(4):
        joints = ['Hip', 'Knee', 'Ankle', 'MTP'] if side < 2 else ['Shoulder', 'Elbow', 'Wrist', 'MCP']
        signs = [-1, 1, -1, -1] if side < 2 else [1, -1, -1, -1]
        offsets = [0, np.pi, np.pi, np.pi] if side < 2 else [np.pi] * 4
        for joint, name in enumerate(joints):
            payload['kinematics'].append({'title': labels[side] + ' · ' + name, 'limb': side, 'unit': 'deg',
                'prediction': np.round(np.rad2deg(offsets[joint] + signs[joint] * result['joint_q'][:, side, joint]), 6).tolist(),
                'reference': np.round(np.rad2deg(offsets[joint] + signs[joint] * target['joint_q'][:, side, joint]), 6).tolist()})
        for component, name in [(0, 'Anterior–posterior GRF'), (2, 'Vertical GRF')]:
            payload['forces'].append({'title': labels[side] + ' · ' + name, 'limb': side, 'unit': 'N',
                'prediction': np.round(result['grf'][:, side, component], 6).tolist(),
                'reference': np.round(target['grf'][:, side, component], 6).tolist()})
    relative = lambda path: os.path.relpath(ROOT / path, folder).replace(os.sep, '/')
    page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Intact walking · interactive experimental comparison</title><link rel="stylesheet" href="STYLE"><style>main{max-width:1600px}.controls{position:sticky;top:0;background:#f5fafc;z-index:2;border:1px solid #b8d1dc;padding:14px;border-radius:10px;box-shadow:0 3px 10px #1232}.controls label,.controls button{display:inline-block;margin:4px}button,input,select{font:inherit;padding:5px}#timeline{width:100%;padding:0}#plots{display:grid;grid-template-columns:repeat(4,minmax(260px,1fr));gap:12px;margin-top:20px}#plots.forces{grid-template-columns:repeat(2,minmax(300px,1fr))}.chart{background:white;border:1px solid #ccdde4;border-radius:10px;padding:8px}.chart canvas{display:block;width:100%;height:245px}.chart h3{font-size:14px;margin:5px 8px}.chart p{font-size:12px;margin:3px 8px;color:#426075}.legend{margin:8px 0;font-size:14px}.prediction{color:#087f9c;font-weight:bold}@media(max-width:1150px){#plots{grid-template-columns:repeat(2,minmax(260px,1fr))}}@media(max-width:650px){#plots,#plots.forces{grid-template-columns:1fr}}</style></head><body><header><div class="tag">Cat · Full-body neuromechanics</div><h1>Explore the complete walking simulation</h1><p>Readable time windows across the full saved trial</p><nav><a href="HOME">Start here</a> · <a href="simulation_report.html">Static figures and full-trial metrics</a></nav></header><main><div class="controls"><label>Signals <select id="mode"><option value="kinematics">Joint angles</option><option value="forces">Paw GRFs</option></select></label><label>Limb <select id="limb"><option value="all">All four limbs</option><option value="0">Left hindlimb</option><option value="1">Right hindlimb</option><option value="2">Left forelimb</option><option value="3">Right forelimb</option></select></label><label>Window <select id="width"><option value="1">1 s</option><option value="2">2 s</option><option value="4" selected>4 s</option><option value="8">8 s</option><option value="all">Full trial overview</option></select></label><label>Start time (s) <input id="start" type="number" min="0" step="0.1" value="0" style="width:90px"></label><button id="first">Start</button><button id="middle">Middle</button><button id="last">End</button><button id="back">−4 s</button><button id="next">+4 s</button><button id="play">Play window</button><input id="timeline" aria-label="Window start time" type="range" min="0" step="0.01" value="0"><div id="interval" aria-live="polite"></div></div><p class="legend"><span class="prediction">Blue solid: forward prediction</span> · Black dashed: experimental/assumed reference. Hover over a plot to read corresponding values. RMSE below each plot uses only the displayed window.</p><div id="plots"></div><p>All saved samples in the selected interval are shown without filtering, time warping or phase shifts. Excitation remains prescribed. RH is measured; LH is mirrored; forelimb references are from a separate study with pooled EMG. The full-trial and final-window comparisons use their separately stated scoring intervals.</p></main><script id="comparison-data" type="application/json">PAYLOAD</script><script src="SCRIPT"></script></body></html>'''
    page = page.replace('STYLE', relative('Documentation/style.css')).replace('HOME', relative('START_HERE.html'))
    page = page.replace('SCRIPT', relative('Code/simulation_tools/interactive_comparison.js'))
    page = page.replace('PAYLOAD', json.dumps(payload, separators=(',', ':'), allow_nan=False))
    (folder / 'interactive_experimental_comparison.html').write_text(page, encoding='utf-8')
