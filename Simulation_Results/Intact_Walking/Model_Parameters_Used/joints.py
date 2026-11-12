# Read this file independently: executable numbers in PARAMETERS are the values used in this model.
# Source-value comments identify verified source numbers; missing sources are explicitly stated.
"""Applied model values. Edit the numbers in PARAMETERS, then run run.py.
Comments and PARAMETER_PROVENANCE.json preserve originals; they do not override your edits.
Missing raw originals are stated honestly. SI units unless noted. Experimental agreement and limitations are documented in Documentation/results.html.
"""

# Set PARAMETERS.
PARAMETERS = {
    # Specify pelvis x.
    "pelvis_x": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.9132052441078028, -0.4074999167288356, 0.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [0.0, 0.0],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.0,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 0.0,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.02, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.9, 0.95, 0.001, 0.5, 2.0],
    },
    # Specify pelvis z.
    "pelvis_z": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.4074999167288356, 0.9132052441078028, 0.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [0.0, 0.0],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.0,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 0.0,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.02, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.9, 0.95, 0.001, 0.5, 2.0],
    },
    # Specify pelvis pitch.
    "pelvis_pitch": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, -0.9999999999999999],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [0.0, 0.0],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.0,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 0.0,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.02, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.9, 0.95, 0.001, 0.5, 2.0],
    },
    # Specify L hip.
    "L_hip": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-2.8, -0.89],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify L knee.
    "L_knee": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-2.3, -0.55],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify L ankle.
    "L_ankle": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [0.2, 1.95],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify L mtp.
    "L_mtp": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-0.498392, 1.8],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.01,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.0005,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify R hip.
    "R_hip": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-2.8, -1.05],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify R knee.
    "R_knee": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-2.3, -0.55],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify R ankle.
    "R_ankle": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [0.2, 1.95],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify R mtp.
    "R_mtp": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-0.498392, 1.8],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.01,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.0005,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FL scapulothoracic.
    "FL_scapulothoracic": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [
            # Run 0.006041293692496915.
            0.006041293692496915,
            # Run 0.0057710941954443335.
            0.0057710941954443335,
            # Run -4.16527781698493e-18.
            -4.16527781698493e-18,
        ],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [-3.16261890488892e-16, 1.9589193577125763e-16, 0.9999999999999993],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-0.8, 0.8],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 1.32546377,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.02683806,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.11642999,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FL shoulder.
    "FL_shoulder": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-1.8766967294087722, -0.7214530320239354],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FL elbow.
    "FL_elbow": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [0.34375538143410944, 2.020734489790133],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FL wrist.
    "FL_wrist": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-1.1689410980761448, 0.5241615878217658],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.004948599962227295,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FL mcp.
    "FL_mcp": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-0.5902191353889319, 1.3791475675996363],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.12982562,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.010005756726886875,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": -0.01970531,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FR scapulothoracic.
    "FR_scapulothoracic": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [
            # Run 0.006041293692496915.
            0.006041293692496915,
            # Run 0.0057710941954443335.
            0.0057710941954443335,
            # Run -4.16527781698493e-18.
            -4.16527781698493e-18,
        ],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [-3.16261890488892e-16, 1.9589193577125763e-16, 0.9999999999999993],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-0.8, 0.8],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 1.32546377,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.02683806,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.11642999,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FR shoulder.
    "FR_shoulder": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-1.8766967294087722, -0.7214530320239354],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FR elbow.
    "FR_elbow": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [0.34375538143410944, 2.020734489790133],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.001,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FR wrist.
    "FR_wrist": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-1.1689410980761448, 0.5241615878217658],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.0,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.004948599962227295,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": 0.0,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
    # Specify FR mcp.
    "FR_mcp": {
        # Joint center in its owning body frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Unit direction of rotation or translation in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "axis_in_body": [0.0, 0.0, 1.0],
        # Lower and upper limit in native coordinates; anatomical plotting conventions are documented separately. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "range": [-0.5902191353889319, 1.3791475675996363],
        # Passive linear stiffness, with spring reference given separately. Unit: N m/rad or N/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_stiffness": 0.12982562,
        # Nonnegative passive viscous coefficient. Unit: N m s/rad or N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "passive_damping": 0.010005756726886875,
        # Additional generalized inertia; an engine/model parameter. Unit: kg m^2 or kg.
        # Source value (original work or literature): not independently established for this entry.
        "armature": 2e-06,
        # Native coordinate at zero passive spring force. Unit: rad or m.
        # Source value (original work or literature): not independently established for this entry.
        "spring_reference": -0.01970531,
        # Soft joint-limit solver reference parameters; not paw-contact material coefficients. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_reference": [0.003, 1.0],
        # Soft joint-limit solver impedance parameters. Unit: engine units.
        # Source value (original work or literature): not independently established for this entry.
        "limit_solver_impedance": [0.99, 0.999, 0.001, 0.5, 2.0],
    },
}
