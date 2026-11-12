"""Advance legacy timestep.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np

from model_configuration.numerical_parameters import MAXIMUM_GENERALIZED_SPEED

import mujoco as mj

from .muscle_excitation import muscle_excitation

from .update_muscle_paths import update_muscle_paths

from .compute_paw_contact_forces import compute_paw_contact_forces

from .solve_elastic_muscle_by_bisection import solve_elastic_muscle_by_bisection


def advance_partitioned_timestep(s, offline_motor_command=None):
    """Excitation -> activation -> elastic force -> motion -> physical contact.

    No reference angles, force templates, support controller, inverse dynamics,
    body-position reset, or externally commanded trunk wrench is used here.
    """
    m, d = s["model"], s["data"]
    d.ctrl[:] = (
        muscle_excitation(s, d.time)
        if offline_motor_command is None
        else offline_motor_command
    )
    d.qfrc_applied[:] = 0.0
    d.xfrc_applied[:] = s["contact_wrench"]
    # Integrate the common skeleton and native activation by one mechanical timestep.
    mj.mj_step(m, d)
    update_muscle_paths(s)
    mj.mj_forward(m, d)
    lf, v, f, r, b = solve_elastic_muscle_by_bisection(
        d.actuator_length + s["mtu_length_offset"],
        s["fiber_length"],
        d.act,
        s["lopt"],
        s["slack"],
        s["muscle_params"],
        s["e0"],
        s["fiber_damping_coefficients"],
        m.opt.timestep,
    )
    s.update(fiber_length=lf, fiber_velocity=v, force=f, residual=r, fiber_bound=b)
    m.actuator_biasprm[:, 0] = -f
    compute_paw_contact_forces(s, m.opt.timestep)
    mj.mj_forward(m, d)
    return bool(
        np.isfinite(d.qpos).all()
        and np.isfinite(f).all()
        and np.max(abs(d.qvel)) < MAXIMUM_GENERALIZED_SPEED
    )
