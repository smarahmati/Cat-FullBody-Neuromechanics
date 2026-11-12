"""Periodic kinematic seed.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np


def periodic_kinematic_seed(pose, period, stride, harmonics=8):
    """Smooth OFFLINE pose prior and differentiate it analytically.

    Raw measurements have a small cycle-end mismatch and linear-interpolation
    corners. Differentiating those corners creates false accelerations. This
    band-limited prior is used ONLY for inverse seeding, never for scoring or
    smoothing a forward result. The retained harmonics are documented.
    """
    n = len(pose)
    phase = np.arange(n) / n
    values = pose.copy()
    values[:, 0] -= stride * phase
    coefficients = np.fft.rfft(values, axis=0)
    coefficients[harmonics + 1 :] = 0.0
    omega = (2j * np.pi * np.arange(len(coefficients)) / period)[:, None]
    q = np.fft.irfft(coefficients, n=n, axis=0)
    v = np.fft.irfft(coefficients * omega, n=n, axis=0)
    a = np.fft.irfft(coefficients * omega**2, n=n, axis=0)
    q[:, 0] += stride * phase
    v[:, 0] += stride / period
    return q, v, a
