"""Periodic interpolate.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np


def periodic_interpolate(values, phase):
    """Linear interpolation of endpoint-inclusive cycle samples; never extrapolate."""
    values = np.asarray(values)
    x = (phase % 1.0) * (len(values) - 1)
    i = int(x)
    f = x - i
    return values[i] * (1 - f) + values[i + 1] * f
