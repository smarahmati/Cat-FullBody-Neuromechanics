"""Named physical parameters, their storage locations, units and meanings.

The editable numeric values live in Data/Model_Parameters. This schema links
those readable names to the exact arrays used by the forward model.
"""

MUSCLE_FIELDS = {
    "max_isometric_muscle_force_along_tendon_N": (
        "muscle_params",
        2,
        "N",
        "Maximum isometric muscle force (F0). The pennation projection is already included. This is not tendon failure strength or a force ceiling; do not multiply by cos(alpha) again.",
    ),
    "optimal_fiber_length_m": (
        "lopt",
        None,
        "m",
        "Optimal fascicle/fiber length, not whole muscle-tendon length.",
    ),
    "tendon_slack_length_m": ("slack", None, "m", "Unloaded series tendon length."),
    "pennation_cosine": (
        "cosine",
        None,
        "1",
        "Cosine of the constant fiber-to-tendon pennation angle.",
    ),
    "tendon_strain_at_max_force": (
        "e0",
        None,
        "1",
        "Tendon strain when tension equals F0, the maximum isometric muscle force.",
    ),
    "max_fiber_speed_optimal_lengths_per_s": (
        "muscle_params",
        6,
        "1/s",
        "Positive maximum-shortening speed magnitude, measured in optimal fiber lengths per second.",
    ),
    "normalized_fiber_damping": (
        "fiber_damping_coefficients",
        None,
        "1",
        "Coefficient of normalized fiber velocity in the normalized tendon-direction force balance.",
    ),
    "MT_path_length_offset_m": (
        "mtu_length_offset",
        None,
        "m",
        "Constant offset added to the routed path to define muscle-tendon length.",
    ),
    "active_force_length_exponent": (
        "muscle_params",
        10,
        "1",
        "Exponent rho in the source active force-length curve.",
    ),
    "source_shortening_curvature": (
        "muscle_params",
        11,
        "1",
        "Source shortening-curve coefficient; inactive when De Groote force-velocity mode is selected.",
    ),
    "source_lengthening_curvature": (
        "muscle_params",
        12,
        "1",
        "Source lengthening-curve coefficient; inactive when De Groote force-velocity mode is selected.",
    ),
    "passive_fiber_enabled": (
        "muscle_params",
        13,
        "0/1",
        "Include the tension-only passive fiber branch.",
    ),
    "degroote_force_velocity_enabled": (
        "muscle_params",
        14,
        "0/1",
        "1 uses the documented De Groote/OpenSim velocity curve; 0 uses the source curve.",
    ),
}
BODY_FIELDS = {
    "mass_kg": ("body_mass", "kg", "Mass of this rigid body, not total cat mass."),
    "principal_inertia_kg_m2": (
        "body_inertia",
        "kg m^2",
        "Three principal moments about the body center of mass.",
    ),
    "COM_position_in_body_m": (
        "body_ipos",
        "m",
        "Center of mass in this body local frame.",
    ),
    "inertia_frame_quaternion_wxyz": (
        "body_iquat",
        "1",
        "Orientation of principal inertia axes in the body frame.",
    ),
    "body_position_in_parent_m": (
        "body_pos",
        "m",
        "Local placement relative to the parent; these offsets encode skeletal segment dimensions.",
    ),
    "body_orientation_in_parent_wxyz": (
        "body_quat",
        "1",
        "Body orientation relative to its parent, scalar-first quaternion.",
    ),
}
JOINT_FIELDS = {
    "position_in_body_m": ("jnt_pos", "m", "Joint center in its owning body frame."),
    "axis_in_body": (
        "jnt_axis",
        "1",
        "Unit direction of rotation or translation in the body frame.",
    ),
    "range": (
        "jnt_range",
        "rad or m",
        "Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately.",
    ),
    "passive_stiffness": (
        "jnt_stiffness",
        "N m/rad or N/m",
        "Passive linear stiffness, with spring reference given separately.",
    ),
    "passive_damping": (
        "dof_damping",
        "N m s/rad or N s/m",
        "Nonnegative passive viscous coefficient.",
    ),
    "armature": (
        "dof_armature",
        "kg m^2 or kg",
        "Additional generalized inertia; an engine/model parameter.",
    ),
    "spring_reference": (
        "qpos_spring",
        "rad or m",
        "Native coordinate at zero passive spring force.",
    ),
    "limit_solver_reference": (
        "jnt_solref",
        "engine units",
        "Soft joint-limit solver reference parameters; not paw-contact material coefficients.",
    ),
    "limit_solver_impedance": (
        "jnt_solimp",
        "engine units",
        "Soft joint-limit solver impedance parameters.",
    ),
}
CONTACT_FIELDS = {
    "normal_stiffness_N_m32": (
        0,
        "N/m^(3/2)",
        "Hunt-Crossley normal stiffness coefficient.",
    ),
    "normal_dissipation_s_m": (1, "s/m", "Velocity multiplier in the normal contact law."),
    "shear_stiffness_N_m": (2, "N/m", "Elastic tangential/shear stiffness."),
    "shear_damping_Ns_m": (
        3,
        "N s/m",
        "Tangential dashpot coefficient, reduced at shallow contact.",
    ),
    "friction_coefficient": (4, "1", "Coulomb limiting shear/normal force ratio."),
    "progressive_stiffening_depth_m": (
        5,
        "m",
        "Optional finite-depth stiffening scale; zero disables the extension.",
    ),
}
