"""Load anatomy, apply the editable parameters, and set the initial mechanical state once.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import numpy as np

import mujoco as mj

from model_configuration.settings import SETTINGS, ROOT

from .load_skeletal_anatomy import load_skeletal_anatomy

from .update_muscle_paths import update_muscle_paths

from .compute_paw_contact_forces import compute_paw_contact_forces

from .muscle_excitation import muscle_excitation

from .solve_elastic_muscle_by_bisection import solve_elastic_muscle_by_bisection


def initialize_neuromechanical_model(overrides=None, graphics=False):
    """Set initial state once. Subsequent stepping never prescribes motion."""
    settings = dict(SETTINGS)
    settings.update(overrides or {})
    directory = (
        ROOT / "Data/Skeletal_Geometry/Model"
        if settings["model_variant"] == "base"
        else ROOT / "Data/Skeletal_Geometry/Model" / settings["model_variant"]
    )
    state = dict(np.load(directory / "muscle_parameters.npz"))
    model = load_skeletal_anatomy(graphics, settings["model_variant"])
    model.opt.timestep = settings["dt_s"]
    data = mj.MjData(model)
    state.update(model=model, data=data, settings=settings)
    if settings["activation_parameter_mode"] == "source":
        model.actuator_dynprm[:, :2] = state["time_constants"]
    elif settings["activation_parameter_mode"] != "legacy":
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Unknown activation parameter mode")
    if settings["excitation_file"]:
        state["excitation_table"] = np.load(ROOT / settings["excitation_file"])[
            "excitation_table"
        ]
    if settings["excitation_sequence_file"]:
        state["excitation_sequence"] = np.load(ROOT / settings["excitation_sequence_file"])[
            "excitation_sequence"
        ]
        seq = state["excitation_sequence"]
        if (
            seq.ndim != 3
            or seq.shape[2] != model.nu
            or not np.isfinite(seq).all()
            or np.any(seq < 0)
            or np.any(seq > 1)
        ):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Invalid frozen muscle_excitation sequence")
        if len(seq) > 1 and not np.allclose(seq[:-1, -1], seq[1:, 0], atol=1e-12):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Frozen sequence has discontinuous stride boundaries")
    if "excitation_control_points" in settings:
        state["excitation_table"] = np.asarray(settings["excitation_control_points"], float)
    if settings.get("excitation_table_file"):
        from .read_time_series import read_time_series

        phase, channels, table = read_time_series(
            ROOT / settings["excitation_table_file"],
            state["names"],
        )
        if np.any(table < 0) or np.any(table > 1):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Excitation table must stay within [0,1]")
        if not np.allclose(phase, np.linspace(0, 1, len(phase)), atol=1e-12, rtol=0):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Excitation phase grid must be uniform")
        state["excitation_table"] = table
    if state["excitation_table"].shape[1] != model.nu:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Excitation channel count mismatch")
    if not np.allclose(state["excitation_table"][0], state["excitation_table"][-1]):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Nonperiodic muscle_excitation endpoints")
    state["muscle_params"][28:, 2] *= settings["fore_strength_scale"]
    state["slack"][28:] *= settings["fore_slack_scale"]
    state["muscle_params"][46:88, 2] *= settings["girdle_strength_scale"]
    for name, scale in settings["muscle_force_scales"].items():
        if scale <= 0:
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Muscle force scale must be positive")
        state["muscle_params"][list(state["names"]).index(name), 2] *= scale
    state["fiber_damping_coefficients"][28:] = settings["fore_fiber_damping"]
    for name, values in settings["girdle_length_overrides"].items():
        i = list(state["names"]).index(name)
        state["lopt"][i], state["slack"][i] = values
    if settings["fore_passive_fiber"]:
        state["muscle_params"][28:, 13] = 1.0
    modes = [settings["hind_force_velocity_mode"], settings["fore_force_velocity_mode"]]
    if any(mode not in ("source", "degroote_2016") for mode in modes):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Unknown muscle force-velocity model")
    if "degroote_2016" in modes:
        state["muscle_params"] = np.pad(state["muscle_params"], ((0, 0), (0, 1)))
        if modes[0] == "degroote_2016":
            state["muscle_params"][:28, 14] = 1.0
        if modes[1] == "degroote_2016":
            state["muscle_params"][28:, 14] = 1.0
    if settings["fore_damping_mode"] == "source_velocity":
        state["fiber_damping_coefficients"][28:] = (
            0.02
            * state["lopt"][28:]
            * state["muscle_params"][28:, 6]
        )
    elif settings["fore_damping_mode"] != "normalized":
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Unknown fore fiber damping mode")
    for name, limits in settings["joint_limit_overrides"].items():
        model.jnt_range[model.joint(name).id] = limits
    for side in ["FL", "FR"]:
        model.body_pos[model.body(side + "_scapula").id] += settings["fore_mount_offset_m"]
    model.body_ipos[model.body("cat_root").id] += settings["trunk_com_offset_m"]
    j = mj.mj_name2id(model, mj.mjtObj.mjOBJ_JOINT, "lumbosacral_pitch")
    if j >= 0:
        k, rest, damping = settings["spine_passive"]
        model.jnt_stiffness[j] = k
        model.qpos_spring[model.jnt_qposadr[j]] = rest
        model.dof_damping[model.jnt_dofadr[j]] = damping
    for side in ["FL", "FR"]:
        for axis in ["x", "z"]:
            j = mj.mj_name2id(model, mj.mjtObj.mjOBJ_JOINT, side + "_scapula_" + axis)
            if j >= 0:
                model.jnt_stiffness[j] = settings["scapula_translation_passive"][0]
                model.dof_damping[model.jnt_dofadr[j]] = settings[
                    "scapula_translation_passive"
                ][1]
    for name, values in settings["passive_joint_overrides"].items():
        j = model.joint(name).id
        if any(key not in ("stiffness", "damping", "springref") for key in values):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Unknown passive joint parameter")
        if any(not np.isfinite(value) for value in values.values()):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Nonfinite passive joint parameter")
        if any(values.get(key, 0) < 0 for key in ["stiffness", "damping"]):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("Passive stiffness and damping must be nonnegative")
        if "stiffness" in values:
            model.jnt_stiffness[j] = values["stiffness"]
        if "damping" in values:
            model.dof_damping[model.jnt_dofadr[j]] = values["damping"]
        if "springref" in values:
            model.qpos_spring[model.jnt_qposadr[j]] = values["springref"]
    state["joint_indices"] = np.array(
        [
            [
                model.joint(side + "_" + j).qposadr[0]
                for j in (
                    ["hip", "knee", "ankle", "mtp"]
                    if side in ["L", "R"]
                    else ["shoulder", "elbow", "wrist", "mcp"]
                )
            ]
            for side in ["L", "R", "FL", "FR"]
        ]
    )
    state["paw_ids"] = np.array(
        [model.site(side + "_paw").id for side in ["L", "R", "FL", "FR"]]
    )
    state["pad_ids"] = np.array(
        [
            i
            for i in range(model.ngeom)
            if "_paw_pad" in model.geom(i).name or "_contactpad" in model.geom(i).name
        ]
    )
    state["pad_side"] = np.array(
        [
            ["L", "R", "FL", "FR"].index(model.geom(i).name.split("_")[0])
            for i in state["pad_ids"]
        ]
    )
    model.geom_contype[state["pad_ids"]] = 0
    model.geom_conaffinity[state["pad_ids"]] = 0
    model.geom_size[state["pad_ids"][state["pad_side"] >= 2], 0] += settings[
        "fore_pad_radius_offset_m"
    ]
    if np.any(model.geom_size[state["pad_ids"], 0] <= 0):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Nonpositive paw pad radius")
    state["bristle"] = np.zeros((len(state["pad_ids"]), 2))
    state["bristle"][: len(state["hind_bristle"])] = state["hind_bristle"]
    if settings["initialize_contact_memory"] and settings["reference_seed"]:
        saved_seed = np.load(ROOT / settings["reference_seed"])
        if "initial_bristle" not in saved_seed:
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError("The selected reference has no saved contact memory")
        state["bristle"][:] = saved_seed["initial_bristle"]
    # Fore contact initially inherits the resolved hind pad material law.
    # This is an explicit cross-paw assumption; four fitted multipliers above.
    state["contact_parameters"] = np.tile(
        np.mean(state["hind_contact_parameters"], axis=0),
        (len(state["pad_ids"]), 1),
    )
    n = len(state["hind_contact_parameters"])
    state["contact_parameters"][:n] = state["hind_contact_parameters"]
    state["contact_parameters"][n:, :4] *= settings["fore_contact_scale"]
    material_scale = np.asarray(settings["contact_material_scale"], float)
    if (
        material_scale.shape != (5,)
        or not np.isfinite(material_scale).all()
        or np.any(material_scale <= 0)
    ):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Contact material multipliers must be five finite positive values")
    state["contact_parameters"][:, :5] *= material_scale
    if settings.get("parameter_bundle_dir"):
        from .apply_neuromechanical_parameters import apply_neuromechanical_parameters

        apply_neuromechanical_parameters(state, settings["parameter_bundle_dir"])
    mj.mj_setConst(model, data)
    data.qpos[:] = state["qpos"]
    data.qvel[:] = state["qvel"]
    data.act[:] = state["activation"]
    data.ctrl[:] = muscle_excitation(state, 0.0)
    if settings["initialize_from_assembled_reference"]:
        from .assemble_reference_kinematics import assemble_reference_kinematics

        ref = assemble_reference_kinematics(state)
        data.qpos[:] = ref["pose"][0]
        data.qvel[:] = ref["velocity"][0]
    data.qpos[1] += settings["initial_height_offset_m"]
    data.qpos[2] += settings["initial_pitch_offset_rad"]
    data.qvel[:3] += settings["initial_root_velocity_offset"]
    for name, value in settings["initial_joint_angle_offsets_rad"].items():
        data.qpos[model.joint(name).qposadr[0]] += value
    for name, value in settings["initial_joint_velocity_offsets_rad_s"].items():
        data.qvel[model.joint(name).dofadr[0]] += value
    update_muscle_paths(state)
    mj.mj_forward(model, data)
    if settings.get("initial_parameter_file"):
        from .apply_initial_parameter_file import apply_initial_parameter_file

        apply_initial_parameter_file(state, ROOT / settings["initial_parameter_file"])
    elif settings.get("forward_initial_state_file"):
        # An explicit fitted state already supplies activation, fibers and
        # contact memory. Computing a negative-time history and immediately
        # discarding it would not change this state, only initialization cost.
        from .apply_forward_initial_state import apply_forward_initial_state

        apply_forward_initial_state(
            state,
            dict(np.load(ROOT / settings["forward_initial_state_file"])),
        )
    elif settings["periodic_muscle_initialization"]:
        from .precondition_periodic_muscles import precondition_periodic_muscles

        precondition_periodic_muscles(state)
    elif settings["precondition_fibers"]:
        from .precondition_fibers import precondition_fibers

        runtime_table = state["excitation_table"]
        if settings["initialization_excitation_file"]:
            state["excitation_table"] = np.load(
                ROOT
                / settings["initialization_excitation_file"]
            )["excitation_table"]
        precondition_fibers(state)
        state["excitation_table"] = runtime_table
        data.ctrl[:] = muscle_excitation(state, 0.0)
    else:
        # Use preserved hind initial fibers; solve fore static equilibrium only.
        mt = data.actuator_length + state["mtu_length_offset"]
        lf, v, f, r, b = solve_elastic_muscle_by_bisection(
            mt,
            state["fiber_length"],
            data.act,
            state["lopt"],
            state["slack"],
            state["muscle_params"],
            state["e0"],
            state["fiber_damping_coefficients"],
            1e6,
        )
        state["fiber_length"][28:] = lf[28:]
        state["force"][28:] = f[28:]
    model.actuator_biasprm[:, 0] = -state["force"]
    mj.mj_forward(model, data)
    compute_paw_contact_forces(state)
    # Check that the model still satisfies the required numerical assumption.
    assert model.neq == 0 and model.nv in [21, 25, 26] and model.nu == len(state["names"])
    return state
