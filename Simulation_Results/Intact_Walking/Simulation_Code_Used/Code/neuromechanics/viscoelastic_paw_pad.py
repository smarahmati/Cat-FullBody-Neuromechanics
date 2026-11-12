"""Compliant normal contact plus a passive viscoelastic friction slider."""

import numpy as np

from numba import njit

from model_configuration.formulation_constants import SHEAR_DAMPING_DEPTH_M


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def viscoelastic_paw_pad(depth, velocity, bristle, dt, parameters):
    """Kelvin--Voigt shear element in series with a Coulomb slider.

    The dashpot responds to elastic shear rate, not to the total sliding rate.
    This distinction makes the backward-Euler return map dissipative even
    during rapid slip. The same Hunt--Crossley normal law is retained.
    This is an explicit constitutive modeling choice, not measured cat tissue.
    """
    k, c, kt, bt, mu = parameters[:5]
    if depth <= 0:
        return np.zeros(3), np.zeros(2), 0.0
    elastic = k * depth**1.5
    normal_energy = k * depth**2.5 / 2.5
    # Optional finite-thickness-inspired progressive stiffness. This smooth,
    # conservative elastic term becomes important near the assumed depth.
    # Its exact coefficient is a modeling choice, not a cat tissue measurement.
    if len(parameters) > 5 and parameters[5] > 0.0:
        scale = parameters[5]
        elastic *= 1.0 + (depth / scale) ** 4
        normal_energy += k * depth**6.5 / (6.5 * scale**4)
    normal = elastic * max(0.0, 1.0 - c * velocity[2])
    if normal <= 0:
        return np.zeros(3), np.zeros(2), normal_energy
    damping = bt * min(1.0, depth / SHEAR_DAMPING_DEPTH_M)
    displacement = bristle + dt * velocity[:2]
    trial_stress = kt * displacement + damping * velocity[:2]
    magnitude = np.linalg.norm(trial_stress)
    # Optional smooth Stribeck-like sliding envelope. This is an engineering
    # friction assumption, NOT an identified cat-paw coefficient or an exact
    # reproduction of the Dupont et al. (2002) elastoplastic state equation.
    # The nonnegative return-map slip rate still dissipates stored shear energy.
    if len(parameters) > 7:
        dynamic_mu = parameters[6]
        vscale = parameters[7]
        speed2 = np.dot(velocity[:2], velocity[:2])
        mu = dynamic_mu + (mu - dynamic_mu) * np.exp(-speed2 / (vscale * vscale))
    limit = mu * normal
    stress = trial_stress.copy()
    if magnitude > limit:
        direction = trial_stress / magnitude
        stress = limit * direction
        if dt > 0:
            # Plastic slip rate gamma is nonnegative. The implicit spring and
            # dashpot share the elastic rate (v - gamma*direction).
            gamma = (magnitude - limit) / (kt * dt + damping)
            displacement -= dt * gamma * direction
        # With dt=0 this is a force evaluation only; stored strain is unchanged.
    force = np.empty(3)
    force[:2] = -stress
    force[2] = normal
    return (
        force,
        displacement,
        normal_energy + 0.5 * kt * np.dot(displacement, displacement),
    )
