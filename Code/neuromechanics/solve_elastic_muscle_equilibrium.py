"""Safeguarded Newton solve of the SAME backward-Euler elastic equation.

This is a numerical acceleration, not a new muscle or tendon law. A bracket
and bisection fallback protect the solve at piecewise-curve transitions.
"""

import numpy as np

from numba import njit

from .muscle_force_curve_derivatives import muscle_force_curve_derivatives

from .elastic_tendon_force import elastic_tendon_force

from model_configuration.formulation_constants import TENDON_TOE_CURVATURE

from model_configuration.numerical_parameters import (
    MINIMUM_FIBER_LENGTH_RATIO,
    MINIMUM_LENGTH_GAP_M,
    MAXIMUM_FIBER_ITERATIONS,
    FIBER_FORCE_TOLERANCE,
    FIBER_LENGTH_TOLERANCE_M,
    NEWTON_FALLBACK_ITERATION,
)

from .elastic_tendon_transition import elastic_tendon_transition


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def solve_elastic_muscle_equilibrium(
    muscle_tendon_length_m,
    previous_fiber_length_m,
    activation,
    optimal_fiber_length_m,
    tendon_slack_length_m,
    muscle_parameters,
    strain_at_maximum_force,
    fiber_damping,
    step_s,
):
    muscle_count = len(muscle_tendon_length_m)
    length = np.empty(muscle_count)
    velocity = np.empty(muscle_count)
    tension = np.empty(muscle_count)
    residual = np.empty(muscle_count)
    bound = np.zeros(muscle_count, np.int64)
    damping = np.asarray(fiber_damping).reshape(-1)
    for i in range(muscle_count):
        coefficient = damping[i] if len(damping) > 1 else damping[0]
        cosine = muscle_parameters[i, 9] if muscle_parameters.shape[1] > 9 else 1.0
        lower = MINIMUM_FIBER_LENGTH_RATIO * optimal_fiber_length_m[i]
        upper = max(lower + MINIMUM_LENGTH_GAP_M, muscle_tendon_length_m[i] / cosine)
        low, high = lower, upper
        maximum_fiber_speed_m_s = optimal_fiber_length_m[i] * muscle_parameters[i, 6]
        fiber_length_m = min(high, max(low, previous_fiber_length_m[i]))
        curvature = TENDON_TOE_CURVATURE
        toe = elastic_tendon_transition(strain_at_maximum_force[i])
        for iteration in range(MAXIMUM_FIBER_ITERATIONS):
            normalized_velocity = (fiber_length_m - previous_fiber_length_m[i]) / (
                step_s
                * maximum_fiber_speed_m_s
            )
            active_length_factor, velocity_factor, passive_length_factor, dfl, dfv, dfp = (
                muscle_force_curve_derivatives(
                    fiber_length_m / optimal_fiber_length_m[i],
                    normalized_velocity,
                    muscle_parameters[i],
                )
            )
            strain = (
                muscle_tendon_length_m[i]
                - fiber_length_m * cosine
            ) / tendon_slack_length_m[i] - 1
            normalized_tendon_force = elastic_tendon_force(
                strain,
                strain_at_maximum_force[i],
            )
            error = (
                normalized_tendon_force
                - activation[i] * active_length_factor * velocity_factor
                - passive_length_factor
                - coefficient * normalized_velocity
            )
            if abs(error) < FIBER_FORCE_TOLERANCE:
                # Leave this loop because the convergence or stopping condition was met.
                break
            if error > 0:
                low = fiber_length_m
            else:
                high = fiber_length_m
            if high - low < FIBER_LENGTH_TOLERANCE_M:
                fiber_length_m = 0.5 * (low + high)
                # Leave this loop because the convergence or stopping condition was met.
                break
            dft = (
                0.0
                if strain <= 0
                else (
                    0.33
                    * curvature
                    / toe
                    * np.exp(curvature * strain / toe)
                    / np.expm1(curvature)
                    if strain <= toe
                    else 0.67 / (strain_at_maximum_force[i] - toe)
                )
            )
            derivative = (
                -dft * cosine / tendon_slack_length_m[i]
                - (activation[i] * dfl * velocity_factor + dfp) / optimal_fiber_length_m[i]
                - (activation[i] * active_length_factor * dfv + coefficient)
                / (step_s * maximum_fiber_speed_m_s)
            )
            candidate = (
                fiber_length_m - error / derivative
                if derivative < 0
                else 0.5 * (low + high)
            )
            if (
                candidate <= low
                or candidate >= high
                or iteration > NEWTON_FALLBACK_ITERATION
            ):
                candidate = 0.5 * (low + high)
            fiber_length_m = candidate
        fiber_velocity_m_s = (fiber_length_m - previous_fiber_length_m[i]) / step_s
        active_length_factor, velocity_factor, passive_length_factor, dfl, dfv, dfp = (
            muscle_force_curve_derivatives(
                fiber_length_m / optimal_fiber_length_m[i],
                fiber_velocity_m_s / maximum_fiber_speed_m_s,
                muscle_parameters[i],
            )
        )
        normalized_tendon_force = elastic_tendon_force(
            (muscle_tendon_length_m[i] - fiber_length_m * cosine) / tendon_slack_length_m[i]
            - 1,
            strain_at_maximum_force[i],
        )
        length[i] = fiber_length_m
        velocity[i] = fiber_velocity_m_s
        tension[i] = muscle_parameters[i, 2] * normalized_tendon_force
        residual[i] = muscle_parameters[i, 2] * (
            normalized_tendon_force
            - activation[i] * active_length_factor * velocity_factor
            - passive_length_factor
            - coefficient * fiber_velocity_m_s / maximum_fiber_speed_m_s
        )
        if (
            fiber_length_m <= 0.200001 * optimal_fiber_length_m[i]
            or muscle_tendon_length_m[i] - fiber_length_m * cosine <= 1e-9
            or muscle_tendon_length_m[i] <= 0.2 * optimal_fiber_length_m[i] * cosine
        ):
            bound[i] = 1
    return length, velocity, tension, residual, bound
