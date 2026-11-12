"""Calculate paw deformation and slip, then apply their contact forces and moments.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np

import mujoco as mj

from .sum_paw_contact_forces_and_moments import sum_paw_contact_forces_and_moments


def compute_paw_contact_forces(state, advance_s=0.0):
    """Actual paw deformation/slip -> forces and body wrenches, all four paws."""
    model, data = state["model"], state["data"]
    pad_indices = state["pad_ids"]
    velocity = np.zeros((4, 6))
    position = np.zeros((4, 3))
    for i, site in enumerate(state["paw_ids"]):
        mj.mj_objectVelocity(model, data, mj.mjtObj.mjOBJ_SITE, int(site), velocity[i], 0)
        position[i] = data.site_xpos[site]
    paw_forces, center_of_pressure, wrench, depth, energy, power = (
        sum_paw_contact_forces_and_moments(
            data.geom_xpos[pad_indices],
            model.geom_size[pad_indices, 0],
            state["pad_side"],
            model.geom_bodyid[pad_indices],
            data.xipos,
            position,
            velocity,
            state["bristle"],
            advance_s,
            state["contact_parameters"],
            True,
        )
    )
    state.update(
        grf=paw_forces,
        center_of_pressure=center_of_pressure,
        contact_wrench=wrench,
        pad_depth=depth,
        pad_energy=energy,
        contact_power=power,
    )
