"""Make t=0 muscle states consistent with each candidate's own waveform."""

import numpy as np

import mujoco as mj

from .assemble_reference_kinematics import assemble_reference_kinematics

from .update_muscle_paths import update_muscle_paths

from .periodic_muscle_history_kernel import periodic_muscle_history_kernel


def precondition_periodic_muscles(s):
    """Reference kinematics apply only to the negative-time muscle prehistory.

    No joint pose, velocity or contact state is reset after t=0. The cached
    reference lengths depend on fixed geometry/reference, never on muscle_excitation.
    In contrast, activation and fiber states are recomputed for every input.
    """
    m, d = s["model"], s["data"]
    q = d.qpos.copy()
    v0 = d.qvel.copy()
    cfg = s["settings"]
    n = cfg["prehistory_samples"]
    offsets = cfg.get("initial_joint_angle_offsets_rad", {})
    cache_key = tuple(sorted(offsets.items()))
    if "prehistory_mtu" not in s or s.get("prehistory_geometry_key", ()) != cache_key:
        reference = assemble_reference_kinematics(s, n)
        length = []
        for row in reference["pose"]:
            d.qpos[:] = row
            for name, value in offsets.items():
                d.qpos[m.joint(name).qposadr[0]] += value
            update_muscle_paths(s)
            # Recalculate positions and routed muscle lengths at the new pose.
            mj.mj_fwdPosition(m, d)
            length.append(d.actuator_length + s["mtu_length_offset"])
        s["prehistory_mtu"] = np.asarray(length)
        s["prehistory_geometry_key"] = cache_key
    a, lf, v, f, r, b, da, dl = periodic_muscle_history_kernel(
        s["prehistory_mtu"],
        s["excitation_table"],
        s["lopt"],
        s["slack"],
        s["muscle_params"],
        s["e0"],
        s["fiber_damping_coefficients"],
        s["time_constants"],
        cfg["period_s"],
        cfg["prehistory_cycles"],
    )
    d.qpos[:] = q
    d.qvel[:] = v0
    d.act[:] = a
    s.update(
        fiber_length=lf,
        fiber_velocity=v,
        force=f,
        residual=r,
        fiber_bound=b,
        prehistory_activation_repeat_error=da,
        prehistory_fiber_repeat_error=dl,
    )
    m.actuator_biasprm[:, 0] = -f
    update_muscle_paths(s)
    mj.mj_forward(m, d)
