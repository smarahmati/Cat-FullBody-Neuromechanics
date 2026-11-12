"""Precondition fibers.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np

import mujoco as mj

from .assemble_reference_kinematics import assemble_reference_kinematics

from .update_muscle_paths import update_muscle_paths

from .periodic_interpolate import periodic_interpolate

from .activation_derivative import activation_derivative

from .solve_elastic_muscle_by_bisection import solve_elastic_muscle_by_bisection

from .muscle_excitation import muscle_excitation


def precondition_fibers(s):
    """Before t=0 only: periodic activation/fiber history on reference lengths."""
    m, d = s["model"], s["data"]
    q0 = d.qpos.copy()
    v0 = d.qvel.copy()
    ref = assemble_reference_kinematics(s, 240)
    length = []
    for q in ref["pose"]:
        d.qpos[:] = q
        update_muscle_paths(s)
        mj.mj_forward(m, d)
        length.append(d.actuator_length + s["mtu_length_offset"])
    length = np.vstack([length, length[0]])
    a = np.zeros(m.nu)
    lf = s["fiber_length"].copy()
    dt = 0.001
    T = s["settings"]["period_s"]
    steps = round(3 * T / dt)
    dt = 3 * T / steps
    for t in np.arange(steps) * dt - 3 * T:
        a = np.clip(
            a + dt * activation_derivative(muscle_excitation(s, t), a, s["time_constants"]),
            0,
            1,
        )
        lf, v, f, r, b = solve_elastic_muscle_by_bisection(
            periodic_interpolate(length, (t + dt) / T),
            lf,
            a,
            s["lopt"],
            s["slack"],
            s["muscle_params"],
            s["e0"],
            s["fiber_damping_coefficients"],
            dt,
        )
    d.qpos[:] = q0
    d.qvel[:] = v0
    d.act[:] = a
    update_muscle_paths(s)
    mj.mj_forward(m, d)
    s.update(fiber_length=lf, fiber_velocity=v, force=f, residual=r, fiber_bound=b)
