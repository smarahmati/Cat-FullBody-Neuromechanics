"""Experimental comparison targets.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np

from model_configuration.paths import ROOT

from .periodic_interpolate import periodic_interpolate


def experimental_comparison_targets(times, period_s=0.6833333333333333, reference_dir=None):
    """Side-specific reference clock; only RH is a simultaneous measured trial.

    LH mirrors RH with the saved geometric consistency adjustment. Forelimb
    angles/Ground_Reaction_Forces have separate Left/Right source curves, but EMGs are pooled.
    These arrays score a run; they never enter the forward mechanical step.
    """
    from .load_reference_tables import load_reference_tables

    z, correction, _ = load_reference_tables(reference_dir)
    q = []
    f = []
    u = []
    scap = []
    for t in times:
        phase = t / period_s + 0.5 + np.array([0.5, 0.0, 0.25, 0.75])
        angles = np.array(
            [periodic_interpolate(z["joint_q"][:, s], phase[s]) for s in range(4)]
        )
        angles[0] += periodic_interpolate(correction, t / period_s)
        q.append(angles)
        f.append([periodic_interpolate(z["grf"][:, s], phase[s]) for s in range(4)])
        u.append(
            np.r_[
                periodic_interpolate(z["excitation"][:, :11], phase[0]),
                periodic_interpolate(z["excitation"][:, 11:22], phase[1]),
                periodic_interpolate(z["excitation"][:, 22:31], phase[2]),
                periodic_interpolate(z["excitation"][:, 31:40], phase[3]),
            ]
        )
        scap.append(
            [
                periodic_interpolate(z["scapula_angle_by_side"][:, s], phase[s + 2])
                - np.mean(z["scapula_angle"])
                for s in range(2)
            ]
        )
    return dict(
        joint_q=np.array(q),
        grf=np.array(f),
        excitation=np.array(u),
        scapula=np.array(scap),
    )
