"""Assemble reference kinematics.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np

import mujoco as mj

from model_configuration.paths import ROOT

from .experimental_comparison_targets import experimental_comparison_targets

from .periodic_interpolate import periodic_interpolate


def assemble_reference_kinematics(state, count=240):
    """Offline scoring/initialization trajectory; never called by advance_partitioned_timestep.

    Each limb retains its source angle convention and a fixed assembly phase.
    The hind fitted initial offset is applied to the root, not to measurements.
    This assembles separate studies; it is not a recorded four-limb gait.
    """
    m = state["model"]
    T = state["settings"]["period_s"]
    time = np.arange(count) * T / count
    if state["settings"].get("reference_seed"):
        seed = np.load(ROOT / state["settings"]["reference_seed"])
        out = {}
        for key in [
            "pose",
            "velocity",
            "acceleration",
            "joint_q",
            "grf",
            "excitation",
            "scapula",
        ] + (["cop"] if "cop" in seed else []):
            value = seed[key]
            grid = np.arange(len(value)) / len(value)
            flat = value.reshape(len(value), -1).copy()
            if key == "pose":
                stride = (
                    float(seed["stride_m"])
                    if "stride_m" in seed
                    else float(
                        np.load(ROOT / "Data/Experimental_Reference_Data/right_hindlimb_walking_reference.npz")["stride_m"]
                    )
                )
                flat[:, 0] -= stride * grid
            new = np.column_stack(
                [np.interp(time / T, np.r_[grid, 1.0], np.r_[v, v[0]]) for v in flat.T]
            )
            if key == "pose":
                new[:, 0] += stride * time / T
            out[key] = new.reshape((count,) + value.shape[1:])
        return dict(time=time, **out)
    ref = dict(np.load(ROOT / "Data/Experimental_Reference_Data/right_hindlimb_walking_reference.npz"))
    raw = ref["pose"]
    phase_grid = np.arange(len(raw)) / len(raw)
    pose = np.tile(state["qpos"], (count, 1))
    target = experimental_comparison_targets(time, T)
    interp = lambda x: np.interp(
        np.arange(count) / count,
        np.r_[phase_grid, 1.0],
        np.r_[x, x[0]],
    )
    stride = float(ref["stride_m"])
    detrend = raw[:, 0] - stride * phase_grid
    pose[:, 0] = interp(detrend) + stride * time / T
    pose[:, 1] = interp(raw[:, 2]) + (state["qpos"][1] - raw[0, 2])
    base = raw[0, 3:7]
    inverse = base * np.array([1, -1, -1, -1])
    angles = []
    for q in raw[:, 3:7]:
        rel = np.zeros(4)
        mj.mju_mulQuat(rel, q, inverse)
        angles.append(2 * np.arctan2(rel[2], rel[0]))
    pose[:, 2] = interp(np.unwrap(angles)) + state["qpos"][2]
    for k in range(4):
        pose[:, state["joint_indices"][k]] = target["joint_q"][:, k]
    # The separate fore study supplies shoulder heights and scapular angles.
    # Infer one common trunk pitch offline. This is an assembly assumption;
    # runtime lumbosacral motion is free and only a passive spring acts there.
    z = np.load(ROOT / "Data/Experimental_Reference_Data/hindlimb_forelimb_reference_cycles.npz")
    scratch = mj.MjData(m)
    spine = m.joint("lumbosacral_pitch").qposadr[0]
    for k, t in enumerate(time):
        wanted = np.mean(
            [
                periodic_interpolate(
                    z["shoulder_z_by_side"][:, i],
                    t / T + 0.5 + [0.25, 0.75][i],
                )
                for i in range(2)
            ]
        )
        theta = 0.0
        for iteration in range(4):
            pose[k, spine] = theta - pose[k, 2]
            for i, side in enumerate(["FL", "FR"]):
                pose[k, m.joint(side + "_scapulothoracic").qposadr[0]] = (
                    target["scapula"][k, i]
                    + theta
                )
            scratch.qpos[:] = pose[k]
            # Recalculate positions and routed muscle lengths at the new pose.
            mj.mj_fwdPosition(m, scratch)
            actual = np.mean(
                [scratch.xpos[m.body(side + "_upperarm").id, 2] for side in ["FL", "FR"]]
            )
            theta += np.clip((actual - wanted) / 0.2294, -0.10, 0.10)
        pose[k, spine] = theta - pose[k, 2]
        for i, side in enumerate(["FL", "FR"]):
            pose[k, m.joint(side + "_scapulothoracic").qposadr[0]] = (
                target["scapula"][k, i]
                + theta
            )
        # Match each source shoulder height with the passive sling translation.
        # This is OFFLINE reference assembly; during simulation the shoulder
        # translation is determined by inertia, muscle forces and contacts.
        scratch.qpos[:] = pose[k]
        # Recalculate positions and routed muscle lengths at the new pose.
        mj.mj_fwdPosition(m, scratch)
        for i, side in enumerate(["FL", "FR"]):
            wanted_i = periodic_interpolate(
                z["shoulder_z_by_side"][:, i],
                t / T + 0.5 + [0.25, 0.75][i],
            )
            actual_i = scratch.xpos[m.body(side + "_upperarm").id, 2]
            pose[k, m.joint(side + "_scapula_z").qposadr[0]] = (
                wanted_i
                - actual_i
            ) / np.cos(theta)
    from .periodic_kinematic_seed import periodic_kinematic_seed

    pose, velocity, acceleration = periodic_kinematic_seed(pose, T, stride, 8)
    return dict(
        time=time,
        pose=pose,
        velocity=velocity,
        acceleration=acceleration,
        **target
    )
