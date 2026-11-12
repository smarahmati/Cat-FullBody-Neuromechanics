"""Readable equivalent of native MuJoCo activation dynamics (no smoothing)."""

import numpy as np


def activation_dynamics(
    muscle_excitation,
    activation,
    activation_time_s,
    deactivation_time_s,
):
    """Return da/dt in 1/s; this diagnostic does not integrate a second state.

    The production integrator advances MuJoCo's native activation state.
    The same time constants are supplied by activation.py. This expression
    documents and tests the zero-switch-smoothing branch used by this model.
    """
    # Keep the incoming neural command between no excitation (0) and full excitation (1).
    u = np.clip(muscle_excitation, 0.0, 1.0)
    # Keep the current active state within its physical range, from 0 to 1.
    a = np.clip(activation, 0.0, 1.0)
    # Let the response time depend on the present activation, as in the native muscle law.
    factor = 0.5 + 1.5 * a
    # Use activation timing when the command rises and deactivation timing when it falls.
    tau = np.where(u > a, activation_time_s * factor, deactivation_time_s / factor)
    # The difference between command and activation determines how quickly activation changes.
    return (u - a) / tau
