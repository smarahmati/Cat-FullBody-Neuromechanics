"""Recompute 60 seconds of intact walking and compare all saved state arrays.

Run: python Verification/verify_intact_walking.py
Output: a new local Simulation_Results/Verification_Runs folder, or --output.
This checks numerical reproducibility from the supplied fixed input and model
parameters. It neither fits parameters nor claims biological validation.
"""
from pathlib import Path
from datetime import datetime
import argparse
import hashlib
import json
import os
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ['CAT_PARAMETER_FOLDER'] = str(ROOT / 'Data/Model_Parameters')
sys.path.insert(0, str(ROOT / 'Code'))
import numpy as np
from neuromechanics.load_model_configuration import load_model_configuration
from neuromechanics.simulate_forward_dynamics import simulate_forward_dynamics


def main():
    """Run the complete intact trial; exit with an error if comparison fails."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New folder for the recomputed arrays and comparison')
    args = parser.parse_args()
    output = args.output or ROOT / 'Simulation_Results/Verification_Runs' / datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    output.mkdir(parents=True, exist_ok=False)
    cfg = load_model_configuration(ROOT / 'Data/Model_Parameters')
    cfg['seconds'] = 60.0
    print('Computing 60 seconds of intact walking...', flush=True)
    result, state = simulate_forward_dynamics(cfg)
    source = ROOT / 'Simulation_Results/Intact_Walking/forward_simulation_timeseries.npz'
    relative_tolerance, absolute_tolerance = 1e-7, 1e-8
    comparisons = {}
    with np.load(source, allow_pickle=False) as reference:
        for key in ['time', 'qpos', 'qvel', 'joint_q', 'grf', 'excitation', 'activation',
                    'force', 'fiber_length', 'fiber_velocity', 'mtu_length', 'tendon_length', 'pad_depth']:
            actual, expected = np.asarray(result[key]), reference[key]
            same_shape = actual.shape == expected.shape
            comparisons[key] = {
                'shape_matches': same_shape,
                'maximum_absolute_difference': float(np.max(np.abs(actual - expected))) if same_shape else None,
                'within_tolerance': bool(same_shape and np.allclose(actual, expected,
                    rtol=relative_tolerance, atol=absolute_tolerance, equal_nan=True)),
            }
        outcome_matches = str(result['failure']) == str(reference['failure'])
    passed = outcome_matches and all(c['within_tolerance'] for c in comparisons.values())
    report = {'passed': passed, 'requested_duration_s': 60.0,
        'final_saved_time_s': float(result['time'][-1]), 'failure': str(result['failure']),
        'relative_tolerance': relative_tolerance, 'absolute_tolerance_in_native_units': absolute_tolerance,
        'comparisons': comparisons, 'python': platform.python_version(), 'numpy': np.__version__,
        'platform': platform.platform(), 'reference_sha256': hashlib.sha256(source.read_bytes()).hexdigest()}
    np.savez_compressed(output / 'recomputed_forward_timeseries.npz', **result)
    (output / 'numerical_reproduction_comparison.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(('PASS' if passed else 'FAIL') + ': ' + str(output), flush=True)
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
