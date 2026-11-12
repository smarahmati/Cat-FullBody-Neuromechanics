"""Advance the common skeleton and native muscle activation by one step."""

import mujoco as mj


def multibody_system_dynamics(state, muscle_excitation):
    """All four limbs share one mass matrix and one root; no imposed motion.

    Native muscle actuators use the elastic tendon forces computed on the
    preceding step. Paw wrenches are physical contact forces. This partitioned
    update is why time-step convergence must be checked.
    """
    model, data = state["model"], state["data"]
    data.ctrl[:] = muscle_excitation
    data.qfrc_applied[:] = 0.0
    data.xfrc_applied[:] = state["contact_wrench"]
    # Integrate the common skeleton and native activation by one mechanical timestep.
    mj.mj_step(model, data)
