"""Source fiber curves; see Documentation/model_methods.html and SOURCE_AND_FIT_REVISION.html."""

import numpy as np

from numba import njit

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
def muscle_force_length_velocity(normalized_length, normalized_velocity, muscle_parameters):
    if len(muscle_parameters) > 9:
        # Algebraic form of the original MATLAB equations with shortening Vmax<0.
        # c=aV/Fmax=0.00915*SO-0.00467; e=0.8/(aV+1).
        active_length_factor = np.exp(
            -abs(
                (max(normalized_length, 0.0) ** ACTIVE_LENGTH_POWER - 1)
                / ACTIVE_LENGTH_WIDTH
            )
            ** muscle_parameters[10]
        )
        c = muscle_parameters[11]
        e = muscle_parameters[12]
        velocity_factor = (
            max(0.0, c * (1 + normalized_velocity) / (c - normalized_velocity))
            if normalized_velocity < 0
            else (e + (1.8 + 0.8 * e) * normalized_velocity) / (e + normalized_velocity)
        )
        if len(muscle_parameters) > 14 and muscle_parameters[14] > 0:
            velocity_factor = muscle_force_velocity_degroote(normalized_velocity)[0]
        # Parallel elastic fiber force: Prilutsky et al. (2016), Table 10.3,
        # DOI 10.1007/978-1-4939-3267-2_10; Rahmati et al. (2025), Table 3,
        # DOI 10.1113/JP287448. Published coefficients: 0.0075 and 11.6.
        # The released configuration enables this term in ALL 104 channels.
        # Our tension-only adaptation sets force to zero at length <= l_opt;
        # the exponential cap is a numerical overflow guard. Neither choice
        # is a separately measured passive curve for each added muscle.
        # Archived MATLAB copies zeroed FPE; we follow the published law here.
        passive_length_factor = (
            (PASSIVE_LENGTH_SCALE / PASSIVE_LENGTH_EXPONENT)
            * np.expm1(
                min(PASSIVE_EXPONENT_CAP, PASSIVE_LENGTH_EXPONENT * (normalized_length - 1))
            )
            if len(muscle_parameters) > 13
            and muscle_parameters[13] > 0
            and normalized_length > 1
            else 0.0
        )
        return active_length_factor, velocity_factor, passive_length_factor
    low, high = muscle_parameters[4], muscle_parameters[5]
    a = (low + 1) / 2
    b = (1 + high) / 2
    if normalized_length < low or normalized_length > high:
        active_length_factor = 0.0
    elif normalized_length <= a:
        active_length_factor = 0.5 * ((normalized_length - low) / (a - low)) ** 2
    elif normalized_length <= 1:
        active_length_factor = 1 - 0.5 * ((1 - normalized_length) / (1 - a)) ** 2
    elif normalized_length <= b:
        active_length_factor = 1 - 0.5 * ((normalized_length - 1) / (b - 1)) ** 2
    else:
        active_length_factor = 0.5 * ((high - normalized_length) / (high - b)) ** 2
    if normalized_velocity <= -1:
        velocity_factor = 0.0
    elif normalized_velocity <= 0:
        velocity_factor = (normalized_velocity + 1) ** 2
    elif normalized_velocity <= muscle_parameters[8] - 1:
        velocity_factor = muscle_parameters[8] - (
            muscle_parameters[8]
            - 1
            - normalized_velocity
        ) ** 2 / (muscle_parameters[8] - 1)
    else:
        velocity_factor = muscle_parameters[8]
    if normalized_length <= 1:
        passive_length_factor = 0.0
    elif normalized_length <= b:
        passive_length_factor = (
            0.5
            * muscle_parameters[7]
            * ((normalized_length - 1) / (b - 1)) ** 2
        )
    else:
        passive_length_factor = muscle_parameters[7] * (
            0.5
            + (normalized_length - b) / (b - 1)
        )
    return active_length_factor, velocity_factor, passive_length_factor
