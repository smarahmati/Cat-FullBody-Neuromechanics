"""Toe length giving continuous force AND slope at the tendon-law join."""

import numpy as np

from numba import njit

from model_configuration.formulation_constants import TENDON_TOE_CURVATURE


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def elastic_tendon_transition(strain_at_max_force):
    k = TENDON_TOE_CURVATURE
    if k == 3.0:
        # Preserve the previous operation order at the original coefficient.
        return 99 * strain_at_max_force * np.exp(3.0) / (166 * np.exp(3.0) - 67)
    numerator = 0.33 * k * np.exp(k)
    return strain_at_max_force * numerator / (numerator + 0.67 * np.expm1(k))
