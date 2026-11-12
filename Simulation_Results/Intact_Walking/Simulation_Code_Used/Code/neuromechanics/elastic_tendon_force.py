"""Dimensionless elastic tendon law; see Documentation/model_methods.html, section 5."""

import numpy as np

from numba import njit

from model_configuration.formulation_constants import TENDON_TOE_CURVATURE

from .elastic_tendon_transition import elastic_tendon_transition


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def elastic_tendon_force(strain, strain_at_maximum_force):
    curvature = TENDON_TOE_CURVATURE
    toe = elastic_tendon_transition(strain_at_maximum_force)
    slope = 0.67 / (strain_at_maximum_force - toe)
    if strain <= 0:
        return 0.0
    if strain <= toe:
        return 0.33 * np.expm1(curvature * strain / toe) / np.expm1(curvature)
    return 0.33 + slope * (strain - toe)
