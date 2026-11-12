"""Read back the actual physical values used by the engine and elastic model."""

import numpy as np

import mujoco as mj

from model_configuration.parameter_schema import MUSCLE_FIELDS, BODY_FIELDS, JOINT_FIELDS, CONTACT_FIELDS


def read_applied_model_parameters(state):
    """Return ordinary dictionaries for config export and per-run auditing."""
    s = state
    m = s["model"]
    d = s["data"]
    value = lambda x: np.asarray(x).tolist()
    muscles = {}
    for i, name in enumerate(s["names"]):
        muscles[str(name)] = {
            field: value(
                s[array][i]
                if col is None
                else s[array][i, col] if col < s[array].shape[1] else 0.0
            )
            for field, (array, col, unit, text) in MUSCLE_FIELDS.items()
        }
    activation = {
        str(n): dict(
            activation_time_constant_s=float(m.actuator_dynprm[i, 0]),
            deactivation_time_constant_s=float(m.actuator_dynprm[i, 1]),
            switch_smoothing_width=float(m.actuator_dynprm[i, 2]),
        )
        for i, n in enumerate(s["names"])
    }
    bodies = {
        m.body(i).name: {f: value(getattr(m, a)[i]) for f, (a, u, t) in BODY_FIELDS.items()}
        for i in range(1, m.nbody)
    }
    joints = {}
    for i in range(m.njnt):
        joints[m.joint(i).name] = {
            f: value(
                getattr(m, a)[
                    (
                        int(m.jnt_dofadr[i])
                        if a.startswith("dof_")
                        else int(m.jnt_qposadr[i]) if a == "qpos_spring" else i
                    )
                ]
            )
            for f, (a, u, t) in JOINT_FIELDS.items()
        }
    contact = {}
    for row, i in enumerate(s["pad_ids"]):
        contact[m.geom(int(i)).name] = dict(
            radius_m=float(m.geom_size[i, 0]),
            position_in_body_m=value(m.geom_pos[i]),
            **{
                f: float(s["contact_parameters"][row, c])
                for f, (c, u, t) in CONTACT_FIELDS.items()
            }
        )
    dynamic_sites = {int(row[5]) for row in s["routing_meta"]}
    attachments = {
        m.site(i).name: dict(
            position_in_body_m=value(m.site_pos[i]),
            orientation_in_body_wxyz=value(m.site_quat[i]),
        )
        for i in range(m.nsite)
        if i not in dynamic_sites
    }
    route_fields = [
        "origin_radius_m",
        "insertion_radius_m",
        "origin_angle_rad",
        "insertion_angle_rad",
        "proximal_wrap_radius_m",
        "proximal_wrap_sign",
        "proximal_joint_sign",
        "distal_wrap_radius_m",
        "distal_wrap_sign",
        "distal_joint_sign",
        "joint_spacing_m",
    ]
    routing = {
        m.site(int(meta[5])).name: dict(zip(route_fields, value(s["routing_geom"][row])))
        for row, meta in enumerate(s["routing_meta"])
    }
    wrap_ids = sorted(
        {
            int(m.wrap_objid[k])
            for k in range(m.nwrap)
            if int(m.wrap_type[k])
            in (int(mj.mjtWrap.mjWRAP_CYLINDER), int(mj.mjtWrap.mjWRAP_SPHERE))
        }
    )
    wrapping = {
        m.geom(i).name: dict(
            position_in_body_m=value(m.geom_pos[i]),
            orientation_in_body_wxyz=value(m.geom_quat[i]),
            radius_m=float(m.geom_size[i, 0]),
        )
        for i in wrap_ids
    }
    initial = dict(
        coordinates={
            m.joint(i).name: dict(
                position=float(d.qpos[m.jnt_qposadr[i]]),
                velocity=float(d.qvel[m.jnt_dofadr[i]]),
            )
            for i in range(m.njnt)
        },
        muscles={
            str(n): dict(
                activation_0_to_1=float(d.act[i]),
                fiber_length_m=float(s["fiber_length"][i]),
            )
            for i, n in enumerate(s["names"])
        },
        contact_memory={
            m.geom(int(i)).name: value(s["bristle"][row])
            for row, i in enumerate(s["pad_ids"])
        },
    )
    environment = dict(
        gravity_m_s2=value(m.opt.gravity),
        solver_iterations=int(m.opt.iterations),
        solver_tolerance=float(m.opt.tolerance),
        # Read back the actual integration scheme used by the engine.
        integrator=int(m.opt.integrator),
    )
    return dict(
        muscle_tendon=muscles,
        activation=activation,
        bodies=bodies,
        joints=joints,
        contact=contact,
        attachments=attachments,
        routing=routing,
        wrapping=wrapping,
        environment=environment,
        initial_state=initial,
    )
