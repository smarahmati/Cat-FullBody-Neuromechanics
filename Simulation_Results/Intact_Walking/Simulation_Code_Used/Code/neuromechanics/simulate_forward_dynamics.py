"""Advance the coupled cat model and save motion, muscle states and raw paw forces.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import time

import numpy as np

from .initialize_neuromechanical_model import initialize_neuromechanical_model

from .advance_partitioned_timestep import advance_partitioned_timestep

from .detect_body_fall import detect_body_fall


def simulate_forward_dynamics(overrides=None, graphics=False, state=None):
    """One uninterrupted forward trial, saved without time warping/filtering."""
    state = (
        initialize_neuromechanical_model(overrides, graphics)
        if state is None
        else state
    )
    if state is not None:
        state["settings"] = dict(state["settings"], **(overrides or {}))
    model, data = state["model"], state["data"]
    settings = state["settings"]
    stepper = advance_partitioned_timestep
    if settings.get("forward_step_implementation") == "readable":
        from .advance_neuromechanical_timestep import advance_neuromechanical_timestep

        stepper = advance_neuromechanical_timestep
    history = {
        key: []
        for key in [
            "time",
            "qpos",
            "qvel",
            "joint_q",
            "grf",
            "activation",
            "excitation",
            "force",
            "fiber_length",
            "fiber_velocity",
            "mtu_length",
            "tendon_length",
            "pad_depth",
        ]
    }
    start = time.perf_counter()
    interval = max(1, round(settings["sample_s"] / model.opt.timestep))
    failure = None
    fall_time = np.nan
    peak_contact = np.abs(state["grf"]).copy()
    impulse = np.zeros((4, 3))
    max_fiber_residual = 0.0
    fiber_bound_steps = 0
    max_interior_residual = 0.0
    bound_channels = np.zeros(model.nu, dtype=int)
    peak_normalized_fiber_velocity = abs(
        state["fiber_velocity"]
        / (state["lopt"] * state["muscle_params"][:, 6])
    ).copy()
    for step in range(round(settings["seconds"] / model.opt.timestep) + 1):
        if step % interval == 0:
            mtu = data.actuator_length + state["mtu_length_offset"]
            tendon = mtu - state["fiber_length"] * state["cosine"]
            for key, value in dict(
                time=data.time,
                qpos=data.qpos,
                qvel=data.qvel,
                joint_q=data.qpos[state["joint_indices"]],
                grf=state["grf"],
                activation=data.act,
                excitation=data.ctrl,
                force=state["force"],
                fiber_length=state["fiber_length"],
                fiber_velocity=state["fiber_velocity"],
                mtu_length=mtu,
                tendon_length=tendon,
                pad_depth=state["pad_depth"],
            ).items():
                history[key].append(np.array(value, copy=True))
        if data.time >= settings["seconds"] - model.opt.timestep / 2:
            # Leave this loop because the convergence or stopping condition was met.
            break
        if not stepper(state):
            failure = "numerical instability"
            # Leave this loop because the convergence or stopping condition was met.
            break
        peak_contact = np.maximum(peak_contact, np.abs(state["grf"]))
        impulse += state["grf"] * model.opt.timestep
        peak_normalized_fiber_velocity = np.maximum(
            peak_normalized_fiber_velocity,
            abs(state["fiber_velocity"] / (state["lopt"] * state["muscle_params"][:, 6])),
        )
        max_fiber_residual = max(max_fiber_residual, float(np.max(abs(state["residual"]))))
        fiber_bound_steps += int(np.any(state["fiber_bound"]))
        interior = state["fiber_bound"] == 0
        if np.any(interior):
            max_interior_residual = max(
                max_interior_residual,
                float(np.max(abs(state["residual"][interior]))),
            )
        bound_channels += state["fiber_bound"].astype(int)
        # Pelvic collapse or a head/trunk collision. Never reset a fallen run.
        fall = detect_body_fall(model, data)
        if fall:
            if not np.isfinite(fall_time):
                fall_time = data.time
            failure = "body fall"
            if settings["stop_on_fall"]:
                # Leave this loop because the convergence or stopping condition was met.
                break
    result = {k: np.array(v) for k, v in history.items()}
    result["names"] = state["names"]
    result["failure"] = np.array(failure or "")
    result["first_fall_time_s"] = np.array(fall_time)
    result["contact_peak_abs_N"] = peak_contact
    result["contact_impulse_Ns"] = impulse
    result["max_fiber_equilibrium_residual_N"] = np.array(max_fiber_residual)
    result["fiber_bound_steps"] = np.array(fiber_bound_steps)
    result["max_interior_fiber_residual_N"] = np.array(max_interior_residual)
    result["fiber_bound_steps_by_channel"] = bound_channels
    result["optimal_fiber_length_m"] = state["lopt"]
    result["tendon_slack_length_m"] = state["slack"]
    result["coordinate_names"] = np.array(
        [model.joint(model.dof_jntid[i]).name for i in range(model.nv)]
    )
    result["peak_abs_normalized_fiber_velocity"] = peak_normalized_fiber_velocity
    result["wall_seconds"] = np.array(time.perf_counter() - start)
    return result, state
