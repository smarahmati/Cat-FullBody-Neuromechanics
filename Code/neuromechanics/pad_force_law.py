"""Local compliant-pad law; force on paw, SI units, no signal filtering."""

import numpy as np

from numba import njit


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=True)
def pad_force_law(depth, velocity, bristle, dt, parameters):
    """Hunt--Crossley normal force and elastic Coulomb return mapping.

    depth: positive compression [m]; velocity: surface velocity [m/s].
    bristle: tangential elastic displacement [m]. dt advances that state.
    k: N/m^(3/2), dissipation: s/m, tangential stiffness: N/m,
    tangential damping: N*s/m. All parameters are explicitly calibrated,
    not claimed as measurements of this animal's pads.
    """
    k, c, kt, bt, mu = parameters
    if depth <= 0:
        return np.zeros(3), np.zeros(2), 0.0
    normal = k * depth**1.5 * max(0.0, 1.0 - c * velocity[2])
    if normal <= 0:
        return np.zeros(3), np.zeros(2), k * depth**2.5 / 2.5
    displacement = bristle + dt * velocity[:2]
    # The dashpot fades with compression; forces approach zero at contact onset.
    damping = bt * min(1.0, depth / 0.001)
    tangent = -kt * displacement - damping * velocity[:2]
    magnitude = np.linalg.norm(tangent)
    limit = mu * normal
    if magnitude > limit:
        tangent *= limit / max(magnitude, 1.0e-30)
        displacement = -(tangent + damping * velocity[:2]) / kt
    force = np.empty(3)
    force[:2] = tangent
    force[2] = normal
    return (
        force,
        displacement,
        (k * depth**2.5 / 2.5 + 0.5 * kt * np.dot(displacement, displacement)),
    )
