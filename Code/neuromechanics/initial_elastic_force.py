"""Tendon tension and compatible fiber velocity at a specified initial state."""

import numpy as np

from numba import njit

from .elastic_tendon_force import elastic_tendon_force

from .muscle_force_length_velocity import muscle_force_length_velocity


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def initial_elastic_force(mtu, fiber, activation, lopt, slack, parameters, e0, beta):
    """Evaluate tension, then invert the monotone fiber force/velocity law.

    This initializes a state once. It is never an added motor command. The
    wide velocity bracket permits diagnostics to expose out-of-domain seeds;
    independent validation still checks the published force-velocity domain.
    """
    n = len(mtu)
    force = np.empty(n)
    velocity = np.empty(n)
    residual = np.empty(n)
    for i in range(n):
        ft = elastic_tendon_force(
            (mtu[i] - fiber[i] * parameters[i, 9]) / slack[i] - 1,
            e0[i],
        )
        low = -20.0
        high = 20.0
        x = 0.0
        for _ in range(60):
            x = (low + high) / 2
            fl, fv, fp = muscle_force_length_velocity(fiber[i] / lopt[i], x, parameters[i])
            error = ft - activation[i] * fl * fv - fp - beta[i] * x
            if abs(error) < 1e-12:
                # Leave this loop because the convergence or stopping condition was met.
                break
            if error > 0:
                low = x
            else:
                high = x
        force[i] = ft * parameters[i, 2]
        velocity[i] = x * lopt[i] * parameters[i, 6]
        residual[i] = parameters[i, 2] * error
    return force, velocity, residual
