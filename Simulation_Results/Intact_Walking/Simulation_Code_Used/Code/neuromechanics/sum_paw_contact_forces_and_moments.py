"""Numerical kernel of the same physical pad law, compiled for fitting speed."""

import numpy as np

from numba import njit

from .pad_force_law import pad_force_law

from .viscoelastic_paw_pad import viscoelastic_paw_pad


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def sum_paw_contact_forces_and_moments(
    position,
    radius,
    side,
    body,
    body_com,
    paw_position,
    paw_velocity,
    bristle,
    dt,
    parameters,
    viscoelastic_slider=False,
):
    force_sum = np.zeros((4, 3))
    cop = np.zeros((4, 3))
    weight = np.zeros(4)
    applied = np.zeros((len(body_com), 6))
    depth_max = 0.0
    energy = 0.0
    power = 0.0
    for n in range(len(position)):
        s = side[n]
        b = body[n]
        depth = max(0.0, radius[n] - position[n, 2])
        point = position[n].copy()
        point[2] = 0.0
        velocity = paw_velocity[s, 3:] + np.cross(
            paw_velocity[s, :3],
            point - paw_position[s],
        )
        p = parameters[n] if parameters.ndim == 2 else parameters
        if viscoelastic_slider:
            f, displacement, stored = viscoelastic_paw_pad(
                depth,
                velocity,
                bristle[n],
                dt,
                p,
            )
        else:
            f, displacement, stored = pad_force_law(depth, velocity, bristle[n], dt, p)
        bristle[n] = displacement
        applied[b, :3] += f
        applied[b, 3:] += np.cross(point - body_com[b], f)
        force_sum[s] += f
        cop[s] += f[2] * point
        weight[s] += f[2]
        depth_max = max(depth_max, depth)
        energy += stored
        power += np.dot(f, velocity)
    for s in range(4):
        cop[s] = cop[s] / weight[s] if weight[s] > 1e-12 else paw_position[s]
    return force_sum, cop, applied, depth_max, energy, power
