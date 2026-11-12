"""Apply an explicitly saved state once at t=0, then resume native dynamics."""

import numpy as np

import mujoco as mj

from .update_muscle_paths import update_muscle_paths

from .compute_paw_contact_forces import compute_paw_contact_forces

from .muscle_excitation import muscle_excitation

from .initial_elastic_force import initial_elastic_force


def apply_forward_initial_state(state, values):
    """Input keys: qpos, qvel, activation, fiber_length, bristle (SI units).

    Used only by initial setup or by restarting independent offline shooting
    trials. Calling it during a continuing simulation is not supported.
    """
    m, d = state["model"], state["data"]
    if d.time != 0:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Initial state may only be applied at time zero")
    for key, size in [
        ("qpos", m.nq),
        ("qvel", m.nv),
        ("activation", m.na),
        ("fiber_length", m.nu),
    ]:
        if np.asarray(values[key]).shape != (size,) or not np.isfinite(values[key]).all():
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Invalid initial " + key)
    if (
        np.asarray(values["bristle"]).shape != state["bristle"].shape
        or not np.isfinite(values["bristle"]).all()
    ):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Invalid initial contact memory")
    if np.any(np.asarray(values["activation"]) < 0) or np.any(
        np.asarray(values["activation"])
        > 1
    ):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Initial activation must lie in [0,1]")
    if np.any(np.asarray(values["fiber_length"]) < 0.2 * state["lopt"]):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Initial fiber length violates the muscle model lower bound")
    d.qpos[:] = values["qpos"]
    d.qvel[:] = values["qvel"]
    d.act[:] = values["activation"]
    state["fiber_length"] = np.array(values["fiber_length"], copy=True)
    state["bristle"] = np.array(values["bristle"], copy=True)
    update_muscle_paths(state)
    # Recalculate positions and routed muscle lengths at the new pose.
    mj.mj_fwdPosition(m, d)
    # Recalculate velocities at the new pose and generalized speed.
    mj.mj_fwdVelocity(m, d)
    mtu = d.actuator_length + state["mtu_length_offset"]
    force, velocity, residual = initial_elastic_force(
        mtu,
        state["fiber_length"],
        d.act,
        state["lopt"],
        state["slack"],
        state["muscle_params"],
        state["e0"],
        state["fiber_damping_coefficients"],
    )
    if not np.isfinite(force).all() or not np.isfinite(velocity).all():
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Initial muscle equilibrium is nonfinite")
    bounds = (
        (state["fiber_length"] <= 0.200001 * state["lopt"])
        | (mtu - state["fiber_length"] * state["cosine"] <= 1e-9)
    ).astype(np.int64)
    state.update(
        force=force,
        fiber_velocity=velocity,
        residual=residual,
        fiber_bound=bounds,
    )
    m.actuator_biasprm[:, 0] = -force
    d.ctrl[:] = muscle_excitation(state, 0.0)
    d.qfrc_applied[:] = 0.0
    d.xfrc_applied[:] = 0.0
    mj.mj_forward(m, d)
    compute_paw_contact_forces(state)
