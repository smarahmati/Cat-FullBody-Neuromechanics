"""Clipped acos.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import math

from numba import njit


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=True)
def clipped_acos(x):
    """Roundoff-safe acos; x is dimensionless."""
    return math.acos(max(-1.0, min(1.0, x)))
