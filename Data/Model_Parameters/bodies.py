# Read this file independently: executable numbers in PARAMETERS are the values used in this model.
# Source-value comments identify verified source numbers; missing sources are explicitly stated.
"""Applied model values. Edit the numbers in PARAMETERS, then run run.py.
Comments and PARAMETER_PROVENANCE.json preserve originals; they do not override your edits.
Missing raw originals are stated honestly. SI units unless noted. Experimental agreement and limitations are documented in Documentation/results.html.
"""

# Set PARAMETERS.
PARAMETERS = {
    # Specify pelvis.
    "pelvis": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.3246
        "mass_kg": 0.07396697902721999,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 2.7737617135207495e-05.
            2.7737617135207495e-05,
            # Run 2.7737617135207495e-05.
            2.7737617135207495e-05,
            # Run 2.7737617135207495e-05.
            2.7737617135207495e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.0, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.0, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [
            # Run 0.6915933133185649.
            0.6915933133185649,
            # Run 0.6915933133185649.
            0.6915933133185649,
            # Run -0.14730474864392273.
            -0.14730474864392273,
            # Run 0.14730474864392273.
            0.14730474864392273,
        ],
    },
    # Specify L pelvis anchor.
    "L_pelvis_anchor": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.0,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [0.0, 0.0, 0.0],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.0, 0.0, -0.0204087361216],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.0, 0.0, -0.0204087361216],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify L thigh.
    "L_thigh": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.1495
        "mass_kg": 0.13822579205711735,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 1.2950046229361893e-05.
            1.2950046229361893e-05,
            # Run 0.00012475339735377054.
            0.00012475339735377054,
            # Run 0.00012475339735377054.
            0.00012475339735377054,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.04230267214799589, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.0, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify L shank.
    "L_shank": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.0635
        "mass_kg": 0.05871128960285587,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 5.473648906738064e-06.
            5.473648906738064e-06,
            # Run 6.133221971906929e-05.
            6.133221971906929e-05,
            # Run 6.133221971906929e-05.
            6.133221971906929e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.045940487804878055, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.0955, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify L foot.
    "L_foot": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.0217
        "mass_kg": 0.020063543061133424,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 8.457199464524766e-07.
            8.457199464524766e-07,
            # Run 7.997195910071741e-06.
            7.997195910071741e-06,
            # Run 7.997195910071741e-06.
            7.997195910071741e-06,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.032576197387518144, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.1085, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify L digits.
    "L_digits": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.0078
        "mass_kg": 0.0072117804551539485,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 5.65847389558233e-08.
            5.65847389558233e-08,
            # Run 7.831797779352706e-07.
            7.831797779352706e-07,
            # Run 7.831797779352706e-07.
            7.831797779352706e-07,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.018, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.067, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify R pelvis anchor.
    "R_pelvis_anchor": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.0,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [0.0, 0.0, 0.0],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.0, 0.0, 0.0204087361216],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.0, 0.0, 0.0204087361216],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify R thigh.
    "R_thigh": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.1495
        "mass_kg": 0.13822579205711735,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 1.2950046229361893e-05.
            1.2950046229361893e-05,
            # Run 0.00012475339735377054.
            0.00012475339735377054,
            # Run 0.00012475339735377054.
            0.00012475339735377054,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.04230267214799589, 0.0, -0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.0, 0.0, -0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify R shank.
    "R_shank": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.0635
        "mass_kg": 0.05871128960285587,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 5.473648906738064e-06.
            5.473648906738064e-06,
            # Run 6.133221971906929e-05.
            6.133221971906929e-05,
            # Run 6.133221971906929e-05.
            6.133221971906929e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.045940487804878055, 0.0, -0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.0955, 0.0, -0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify R foot.
    "R_foot": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.0217
        "mass_kg": 0.020063543061133424,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 8.457199464524766e-07.
            8.457199464524766e-07,
            # Run 7.997195910071741e-06.
            7.997195910071741e-06,
            # Run 7.997195910071741e-06.
            7.997195910071741e-06,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.032576197387518144, 0.0, -0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.1085, 0.0, -0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify R digits.
    "R_digits": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Original work: 0.0078
        "mass_kg": 0.0072117804551539485,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 5.65847389558233e-08.
            5.65847389558233e-08,
            # Run 7.831797779352706e-07.
            7.831797779352706e-07,
            # Run 7.831797779352706e-07.
            7.831797779352706e-07,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.018, 0.0, -0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.067, 0.0, -0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify cat root.
    "cat_root": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 1.691717804280232,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 0.00164908651561237.
            0.00164908651561237,
            # Run 0.009685084429504328.
            0.009685084429504328,
            # Run 0.009287192401937618.
            0.009287192401937618,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.07917885382672582, 0.0, 0.22],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [-0.09261350342858944, -0.1997167342633804, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [
            # Run 0.6905076763443475.
            0.6905076763443475,
            # Run -0.6905076763443476.
            -0.6905076763443476,
            # Run 0.15231266825031237.
            0.15231266825031237,
            # Run -0.1523126682503124.
            -0.1523126682503124,
        ],
    },
    # Specify FL scapula.
    "FL_scapula": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.05837711735832217,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 3.236421733154842e-06.
            3.236421733154842e-06,
            # Run 3.236421733154841e-05.
            3.236421733154841e-05,
            # Run 3.236421733154841e-05.
            3.236421733154841e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.02748354285714286, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [
            # Run 0.2148799182938485.
            0.2148799182938485,
            # Run 0.02499999999999998.
            0.02499999999999998,
            # Run 0.20477734483331916.
            0.20477734483331916,
        ],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [
            # Run 0.5910014263518294.
            0.5910014263518294,
            # Run 0.5910014263518292.
            0.5910014263518292,
            # Run 0.38822327860408246.
            0.38822327860408246,
            # Run -0.3882232786040824.
            -0.3882232786040824,
        ],
    },
    # Specify FL upperarm.
    "FL_upperarm": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.07485162805890228,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 5.525364373047746e-06.
            5.525364373047746e-06,
            # Run 5.5253643730477466e-05.
            5.5253643730477466e-05,
            # Run 5.5253643730477466e-05.
            5.5253643730477466e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.04528403714285715, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.05771428571428572, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify FL forearm.
    "FL_forearm": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.038469274788041054,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 3.2719639232485494e-06.
            3.2719639232485494e-06,
            # Run 3.271963923248549e-05.
            3.271963923248549e-05,
            # Run 3.271963923248549e-05.
            3.271963923248549e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.04300274, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.09275714285714286, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify FL carpals.
    "FL_carpals": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.006950392246318608,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 5.424105824185633e-08.
            5.424105824185633e-08,
            # Run 5.424105824185633e-07.
            5.424105824185633e-07,
            # Run 5.424105824185633e-07.
            5.424105824185633e-07,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.013664871428571429, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.09465714285714286, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify FL digits.
    "FL_digits": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.004708790718429273,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 2.5373014476651885e-08.
            2.5373014476651885e-08,
            # Run 2.5373014476651884e-07.
            2.5373014476651884e-07,
            # Run 2.5373014476651884e-07.
            2.5373014476651884e-07,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.012714285714285714, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.026142857142857138, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify FR scapula.
    "FR_scapula": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.05837711735832217,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 3.236421733154842e-06.
            3.236421733154842e-06,
            # Run 3.236421733154841e-05.
            3.236421733154841e-05,
            # Run 3.236421733154841e-05.
            3.236421733154841e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.02748354285714286, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [
            # Run 0.2148799182938485.
            0.2148799182938485,
            # Run -0.024999999999999998.
            -0.024999999999999998,
            # Run 0.20477734483331916.
            0.20477734483331916,
        ],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [
            # Run 0.5910014263518294.
            0.5910014263518294,
            # Run 0.5910014263518292.
            0.5910014263518292,
            # Run 0.38822327860408246.
            0.38822327860408246,
            # Run -0.3882232786040824.
            -0.3882232786040824,
        ],
    },
    # Specify FR upperarm.
    "FR_upperarm": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.07485162805890228,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 5.525364373047746e-06.
            5.525364373047746e-06,
            # Run 5.5253643730477466e-05.
            5.5253643730477466e-05,
            # Run 5.5253643730477466e-05.
            5.5253643730477466e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.04528403714285715, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.05771428571428572, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify FR forearm.
    "FR_forearm": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.038469274788041054,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 3.2719639232485494e-06.
            3.2719639232485494e-06,
            # Run 3.271963923248549e-05.
            3.271963923248549e-05,
            # Run 3.271963923248549e-05.
            3.271963923248549e-05,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.04300274, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.09275714285714286, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify FR carpals.
    "FR_carpals": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.006950392246318608,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 5.424105824185633e-08.
            5.424105824185633e-08,
            # Run 5.424105824185633e-07.
            5.424105824185633e-07,
            # Run 5.424105824185633e-07.
            5.424105824185633e-07,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.013664871428571429, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.09465714285714286, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify FR digits.
    "FR_digits": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.004708790718429273,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [
            # Run 2.5373014476651885e-08.
            2.5373014476651885e-08,
            # Run 2.5373014476651884e-07.
            2.5373014476651884e-07,
            # Run 2.5373014476651884e-07.
            2.5373014476651884e-07,
        ],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.012714285714285714, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.026142857142857138, 0.0, 0.0],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Specify head neck mass.
    "head_neck_mass": {
        # Mass of this rigid body, not total cat mass. Unit: kg.
        # Source value (original work or literature): not independently established for this entry.
        "mass_kg": 0.379176,
        # Three principal moments about the body center of mass. Unit: kg m^2.
        # Source value (original work or literature): not independently established for this entry.
        "principal_inertia_kg_m2": [0.00021423444000000003, 0.0003507378, 0.0003222996],
        # Center of mass in this body local frame. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "COM_position_in_body_m": [0.0, 0.0, 0.0],
        # Orientation of principal inertia axes in the body frame. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "inertia_frame_quaternion_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Local placement relative to the parent; these offsets encode skeletal segment dimensions. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "body_position_in_parent_m": [0.325, 0.0, 0.255],
        # Body orientation relative to its parent, scalar-first quaternion. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "body_orientation_in_parent_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
}
