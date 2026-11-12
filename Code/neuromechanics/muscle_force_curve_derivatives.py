"""The existing fiber law and its derivatives, for the elastic root solver."""

import numpy as np

from numba import njit

from .muscle_force_length_velocity import muscle_force_length_velocity

from .muscle_force_velocity_degroote import muscle_force_velocity_degroote

from model_configuration.formulation_constants import (
    ACTIVE_LENGTH_POWER,
    ACTIVE_LENGTH_WIDTH,
    PASSIVE_LENGTH_SCALE,
    PASSIVE_LENGTH_EXPONENT,
    PASSIVE_EXPONENT_CAP,
)


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def muscle_force_curve_derivatives(l, v, p):
    fl, fv, fp = muscle_force_length_velocity(l, v, p)
    if len(p) > 9:
        x = (max(l, 0.0) ** ACTIVE_LENGTH_POWER - 1) / ACTIVE_LENGTH_WIDTH
        dfl = (
            -fl
            * p[10]
            * abs(x) ** (p[10] - 1)
            * np.sign(x)
            * ACTIVE_LENGTH_POWER
            * max(l, 0.0) ** (ACTIVE_LENGTH_POWER - 1)
            / ACTIVE_LENGTH_WIDTH
        )
        c, e = p[11], p[12]
        if v < 0:
            dfv = c * (c + 1) / (c - v) ** 2 if fv > 0 else 0.0
        else:
            dfv = e * (0.8 + 0.8 * e) / (e + v) ** 2
        if len(p) > 14 and p[14] > 0:
            dfv = muscle_force_velocity_degroote(v)[1]
        dfp = (
            PASSIVE_LENGTH_SCALE * np.exp(PASSIVE_LENGTH_EXPONENT * (l - 1))
            if len(p) > 13
            and p[13] > 0
            and 1 < l < 1 + PASSIVE_EXPONENT_CAP / PASSIVE_LENGTH_EXPONENT
            else 0.0
        )
    else:
        low, high = p[4], p[5]
        a = (low + 1) / 2
        b = (1 + high) / 2
        if l < low or l > high:
            dfl = 0.0
        elif l <= a:
            dfl = (l - low) / (a - low) ** 2
        elif l <= 1:
            dfl = (1 - l) / (1 - a) ** 2
        elif l <= b:
            dfl = -(l - 1) / (b - 1) ** 2
        else:
            dfl = -(high - l) / (high - b) ** 2
        if v <= -1:
            dfv = 0.0
        elif v <= 0:
            dfv = 2 * (v + 1)
        elif v <= p[8] - 1:
            dfv = 2 * (p[8] - 1 - v) / (p[8] - 1)
        else:
            dfv = 0.0
        if l <= 1:
            dfp = 0.0
        elif l <= b:
            dfp = p[7] * (l - 1) / (b - 1) ** 2
        else:
            dfp = p[7] / (b - 1)
    return fl, fv, fp, dfl, dfv, dfp
