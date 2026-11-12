"""Activation derivative.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np


def activation_derivative(muscle_excitation, activation, time_constants):
    """MuJoCo muscle activation law; tau=[activation,deactivation] in seconds."""
    u = np.clip(muscle_excitation, 0, 1)
    a = np.clip(activation, 0, 1)
    factor = 0.5 + 1.5 * a
    tau = np.where(u > a, time_constants[:, 0] * factor, time_constants[:, 1] / factor)
    return (u - a) / tau
