"""Elastic fiber step in SI units; see Documentation/model_methods.html, section 5."""

import numpy as np

# Read the permitted number of fiber-force balancing steps from the config.
from model_configuration.numerical_parameters import BISECTION_ITERATIONS

from numba import njit

from .muscle_force_length_velocity import muscle_force_length_velocity

from .elastic_tendon_force import elastic_tendon_force


# This compiled function calls muscle_force_length_velocity/elastic_tendon_force from other modules.
# Numba disk caches do not reliably invalidate when imported callees change.
# Compile once per process so edits to those physical laws always take effect.
@njit(cache=False)
def solve_elastic_muscle_by_bisection(
    mt,
    previous,
    activation,
    lopt,
    slack,
    params,
    e0,
    beta,
    dt,
):
    """Backward-Euler fiber step with native MTU geometry held at its new value."""
    n = len(mt)
    length = np.empty(n)
    velocity = np.empty(n)
    tension = np.empty(n)
    residual = np.empty(n)
    bound = np.zeros(n, np.int64)
    damping = np.asarray(beta).reshape(-1)
    for i in range(n):
        coefficient = damping[i] if len(damping) > 1 else damping[0]
        cosine = params[i, 9] if params.shape[1] > 9 else 1.0
        low = 0.2 * lopt[i]
        high = max(low + 1e-9, mt[i] / cosine)
        vscale = lopt[i] * params[i, 6]
        # Repeatedly narrow the fiber-length interval until the forces balance.
        for _ in range(BISECTION_ITERATIONS):
            lf = 0.5 * (low + high)
            v = (lf - previous[i]) / (dt * vscale)
            fl, fv, fp = muscle_force_length_velocity(lf / lopt[i], v, params[i])
            ft = elastic_tendon_force((mt[i] - lf * cosine) / slack[i] - 1, e0[i])
            error = ft - activation[i] * fl * fv - fp - coefficient * v
            if error > 0:
                low = lf
            else:
                high = lf
        lf = 0.5 * (low + high)
        vf = (lf - previous[i]) / dt
        fl, fv, fp = muscle_force_length_velocity(lf / lopt[i], vf / vscale, params[i])
        ft = elastic_tendon_force((mt[i] - lf * cosine) / slack[i] - 1, e0[i])
        length[i] = lf
        velocity[i] = vf
        tension[i] = params[i, 2] * ft
        residual[i] = params[i, 2] * (
            ft
            - activation[i] * fl * fv
            - fp
            - coefficient * vf / vscale
        )
        if (
            lf <= 0.200001 * lopt[i]
            or mt[i] - lf * cosine <= 1e-9
            or mt[i] <= 0.2 * lopt[i] * cosine
        ):
            bound[i] = 1
    return length, velocity, tension, residual, bound
