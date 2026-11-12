"""De Groote et al. (2016) smooth normalized fiber force-velocity curve.

Primary implementation: OpenSim DeGrooteFregly2016Muscle.h, with its corrected
constants that pass through (-1,0) and (0,1). Original rounded paper values
were d1=-0.318 and d4=0.886; applied values are recorded below. This optional
limb-selectable adaptation is NOT the force-velocity law in Rahmati's MATLAB model.
Normalized velocity is positive for lengthening. Published domain [-1,1].
Outside that domain we retain the algebraic curve but prevent negative active
tension; excursions must be reported, not interpreted as validated behavior.
"""

import numpy as np

from numba import njit

from model_configuration.formulation_constants import FV_D1, FV_D2, FV_D3, FV_D4


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def muscle_force_velocity_degroote(velocity):
    x = FV_D2 * velocity + FV_D3
    raw = FV_D1 * np.arcsinh(x) + FV_D4
    value = max(0.0, raw)
    derivative = FV_D1 * FV_D2 / np.sqrt(1 + x * x) if raw > 0 else 0.0
    return value, derivative
