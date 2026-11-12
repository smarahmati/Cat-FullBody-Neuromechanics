"""Apply one explicit, versioned physical parameter set before initialization."""

from pathlib import Path

import numpy as np

from model_configuration.paths import ROOT

from model_configuration.parameter_schema import MUSCLE_FIELDS, BODY_FIELDS, JOINT_FIELDS, CONTACT_FIELDS

from .load_parameter_file import load_parameter_file


def apply_neuromechanical_parameters(state, folder):
    """All assignments happen before forward integration, never during walking.

    Values are absolute applied values, not multipliers applied repeatedly.
    Existing settings without a bundle preserve the historical model exactly.
    Names and topology must match the selected anatomical model.
    """
    folder = ROOT / Path(folder)
    s = state
    m = s["model"]
    names = list(s["names"])

    # Reject misspelled/unknown entries rather than silently ignore an edit.
    def checked(filename, fields=None, record_names=None):
        values = load_parameter_file(folder / filename)
        if record_names is not None and set(values) != set(record_names):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"{filename}: model record names differ")
        for name, record in values.items():
            if fields is not None and set(record) != set(fields):
                # Stop and explain the invalid model setting or failed calculation.
                raise ValueError(f"{filename}/{name}: unknown or missing field")
            numbers = list(record.values()) if isinstance(record, dict) else [record]
            if any(not np.isfinite(np.asarray(v, float)).all() for v in numbers):
                # Stop and explain the invalid model setting or failed calculation.
                raise ValueError(f"{filename}/{name}: nonfinite value")
        return values

    muscles = checked("muscle_tendon.py", MUSCLE_FIELDS, names)
    if set(muscles) != set(names):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Muscle configuration does not match model channels")
    if s["muscle_params"].shape[1] < 15:
        s["muscle_params"] = np.pad(
            s["muscle_params"],
            ((0, 0), (0, 15 - s["muscle_params"].shape[1])),
        )
    for name, values in muscles.items():
        i = names.index(name)
        for field, (array, column, unit, meaning) in MUSCLE_FIELDS.items():
            value = float(values[field])
            if not np.isfinite(value):
                # Stop and explain the invalid model setting or failed calculation.
                raise ValueError(f"Nonfinite {name}.{field}")
            if column is None:
                s[array][i] = value
            else:
                s[array][i, column] = value
        if (
            min(
                s["lopt"][i],
                s["slack"][i],
                s["e0"][i],
                s["muscle_params"][i, 2],
                s["muscle_params"][i, 6],
            )
            <= 0
        ):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Nonpositive muscle scale: {name}")
        if not 0 < s["cosine"][i] <= 1 or s["fiber_damping_coefficients"][i] < 0:
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Invalid pennation or damping: {name}")
        if (
            values["active_force_length_exponent"] < 1
            or min(
                values["source_shortening_curvature"],
                values["source_lengthening_curvature"],
            )
            <= 0
        ):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Invalid fiber curve coefficients: {name}")
        if any(
            values[key] not in (0, 1)
            for key in ["passive_fiber_enabled", "degroote_force_velocity_enabled"]
        ):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Muscle switches must be 0 or 1: {name}")
        s["muscle_params"][i, 9] = s["cosine"][i]
    for name, values in checked(
        "activation.py",
        [
            "activation_time_constant_s",
            "deactivation_time_constant_s",
            "switch_smoothing_width",
        ],
        names,
    ).items():
        i = names.index(name)
        tau = [values["activation_time_constant_s"], values["deactivation_time_constant_s"]]
        if min(tau) <= 0 or values["switch_smoothing_width"] < 0:
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Invalid activation time constants/smoothing")
        s["time_constants"][i] = tau
        m.actuator_dynprm[i, :3] = tau + [values["switch_smoothing_width"]]
    for name, values in checked(
        "bodies.py",
        BODY_FIELDS,
        [m.body(i).name for i in range(1, m.nbody)],
    ).items():
        i = m.body(name).id
        for field, (array, unit, meaning) in BODY_FIELDS.items():
            getattr(m, array)[i] = values[field]
        if m.body_mass[i] < 0 or np.any(m.body_inertia[i] < 0):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Negative mass or inertia: {name}")
        if np.max(m.body_inertia[i]) > np.sum(m.body_inertia[i]) / 2 + 1e-12:
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Inertia triangle inequality: {name}")
        for quat in [m.body_iquat[i], m.body_quat[i]]:
            if not np.isclose(np.linalg.norm(quat), 1.0, atol=1e-7):
                # Stop and explain the invalid model setting or failed calculation.
                raise ValueError(f"Quaternion must be unit length: {name}")
    for name, values in checked(
        "joints.py",
        JOINT_FIELDS,
        [m.joint(i).name for i in range(m.njnt)],
    ).items():
        i = m.joint(name).id
        for field, (array, unit, meaning) in JOINT_FIELDS.items():
            index = (
                int(m.jnt_dofadr[i])
                if array.startswith("dof_")
                else int(m.jnt_qposadr[i]) if array == "qpos_spring" else i
            )
            getattr(m, array)[index] = values[field]
        if values["passive_stiffness"] < 0 or values["passive_damping"] < 0:
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Passive coefficients must be nonnegative")
        if not np.isclose(np.linalg.norm(m.jnt_axis[i]), 1.0, atol=1e-7):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Joint axis must be unit length: {name}")
        if values["armature"] < 0 or values["range"][0] > values["range"][1]:
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Invalid armature/limits: {name}")
    pads = checked(
        "contact.py",
        list(CONTACT_FIELDS) + ["radius_m", "position_in_body_m"],
        [m.geom(int(i)).name for i in s["pad_ids"]],
    )
    for row, geom in enumerate(s["pad_ids"]):
        values = pads[m.geom(int(geom)).name]
        m.geom_size[geom, 0] = values["radius_m"]
        m.geom_pos[geom] = values["position_in_body_m"]
        for field, (column, unit, meaning) in CONTACT_FIELDS.items():
            s["contact_parameters"][row, column] = values[field]
        if (
            m.geom_size[geom, 0] <= 0
            or np.any(s["contact_parameters"][row] < 0)
            or min(s["contact_parameters"][row, [0, 2]]) <= 0
        ):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Invalid pad geometry/material value")
    dynamic = {int(meta[5]) for meta in s["routing_meta"]}
    for name, values in checked(
        "attachments.py",
        ["position_in_body_m", "orientation_in_body_wxyz"],
        [m.site(i).name for i in range(m.nsite) if i not in dynamic],
    ).items():
        if np.shape(values["position_in_body_m"]) != (3,) or np.shape(
            values["orientation_in_body_wxyz"]
        ) != (4,):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"attachments.py/{name}: expected xyz and wxyz vectors")
        i = m.site(name).id
        if not np.array_equal(
            m.site_pos[i],
            values["position_in_body_m"],
        ) or not np.array_equal(m.site_quat[i], values["orientation_in_body_wxyz"]):
            # The compiled XML can mark a site as coincident with its body.
            # After an edit, that shortcut would ignore the new coordinates.
            m.site_sameframe[i] = 0
        m.site_pos[i] = values["position_in_body_m"]
        m.site_quat[i] = values["orientation_in_body_wxyz"]
        if not np.isclose(np.linalg.norm(m.site_quat[i]), 1.0, atol=1e-7):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Invalid site quaternion: {name}")
    from .apply_wrapping_parameters import apply_wrapping_parameters

    apply_wrapping_parameters(s, folder / "wrapping.py")
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
    routes = checked(
        "routing.py",
        route_fields,
        [m.site(int(meta[5])).name for meta in s["routing_meta"]],
    )
    for row, meta in enumerate(s["routing_meta"]):
        name = m.site(int(meta[5])).name
        values = routes[name]
        s["routing_geom"][row] = [
            values[key]
            for key in [
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
        ]
    environment = checked("environment.py")
    if set(environment) - {
        "gravity_m_s2",
        "solver_iterations",
        "solver_tolerance",
        "integrator",
    }:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Unknown environment parameter")
    m.opt.gravity[:] = environment["gravity_m_s2"]
    m.opt.iterations = int(environment["solver_iterations"])
    m.opt.tolerance = float(environment["solver_tolerance"])
    # Read the configured native integration scheme; old parameter snapshots may omit it.
    integrator = environment.get("integrator", int(m.opt.integrator))
    # Accept only the four named engine schemes listed in environment.py.
    if integrator not in (0, 1, 2, 3):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Invalid MuJoCo integration scheme")
    # Apply the choice before any dynamics steps are calculated.
    m.opt.integrator = int(integrator)
    if m.opt.iterations < 1 or m.opt.tolerance < 0:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Invalid dynamics solver parameters")
    # MuJoCo recomputes all derived inertial constants immediately after this
    # function returns. Initial states and negative-time preparation follow.
    s["parameter_bundle_applied"] = str(folder)
