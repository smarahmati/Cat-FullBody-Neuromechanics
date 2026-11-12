"""Polar point.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import math, numpy as np

from numba import njit


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=True)
def polar_point(radius, angle):
    """Cartesian planar point (m), angle (rad)."""
    return np.array([radius * math.cos(angle), radius * math.sin(angle)])
