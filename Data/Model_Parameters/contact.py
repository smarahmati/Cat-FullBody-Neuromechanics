# Read this file independently: executable numbers in PARAMETERS are the values used in this model.
# Source-value comments identify verified source numbers; missing sources are explicitly stated.
"""Applied model values. Edit the numbers in PARAMETERS, then run run.py.
Comments and PARAMETER_PROVENANCE.json preserve originals; they do not override your edits.
Missing raw originals are stated honestly. SI units unless noted. Experimental agreement and limitations are documented in Documentation/results.html.
"""

# Set PARAMETERS.
PARAMETERS = {
    # Specify L paw pad0.
    "L_paw_pad0": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006944518048175291,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.006928842727548444, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify L paw pad1.
    "L_paw_pad1": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006944518048175291,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.006928842727548444, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify L paw pad2.
    "L_paw_pad2": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.0071395132113181055,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.019298430645675463, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify L paw pad3.
    "L_paw_pad3": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.0071395132113181055,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.019298430645675463, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify L paw pad4.
    "L_paw_pad4": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.007699999604278971,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.03137865992484085, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify L paw pad5.
    "L_paw_pad5": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.007699999604278971,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.03137865992484085, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify R paw pad0.
    "R_paw_pad0": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006944518048175291,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.006928842727548444, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify R paw pad1.
    "R_paw_pad1": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006944518048175291,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.006928842727548444, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify R paw pad2.
    "R_paw_pad2": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.0071395132113181055,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.019298430645675463, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify R paw pad3.
    "R_paw_pad3": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.0071395132113181055,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.019298430645675463, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify R paw pad4.
    "R_paw_pad4": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.007699999604278971,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.03137865992484085, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify R paw pad5.
    "R_paw_pad5": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.007699999604278971,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.03137865992484085, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.524247296978,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.12305001401446,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.3286671878786615,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FL contactpad0.
    "FL_contactpad0": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.004, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FL contactpad1.
    "FL_contactpad1": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.004, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FL contactpad2.
    "FL_contactpad2": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.013, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FL contactpad3.
    "FL_contactpad3": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.013, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FL contactpad4.
    "FL_contactpad4": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.022, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FL contactpad5.
    "FL_contactpad5": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.022, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FR contactpad0.
    "FR_contactpad0": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.004, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FR contactpad1.
    "FR_contactpad1": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.004, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FR contactpad2.
    "FR_contactpad2": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.013, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FR contactpad3.
    "FR_contactpad3": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.013, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FR contactpad4.
    "FR_contactpad4": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.022, 0.0, -0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
    # Specify FR contactpad5.
    "FR_contactpad5": {
        # radius m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "radius_m": 0.006,
        # position in body m Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "position_in_body_m": [0.022, 0.0, 0.005],
        # Hunt-Crossley normal stiffness coefficient. Unit: N/m^(3/2).
        # Source value (original work or literature): not independently established for this entry.
        "normal_stiffness_N_m32": 11296.50835492188,
        # Velocity multiplier in the normal contact law. Unit: s/m.
        # Source value (original work or literature): not independently established for this entry.
        "normal_dissipation_s_m": 1.1713310597178772,
        # Elastic tangential/shear stiffness. Unit: N/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_stiffness_N_m": 2412.5242472969776,
        # Tangential dashpot coefficient, reduced at shallow contact. Unit: N s/m.
        # Source value (original work or literature): not independently established for this entry.
        "shear_damping_Ns_m": 16.123050014014463,
        # Coulomb limiting shear/normal force ratio. Unit: 1.
        # Source value (original work or literature): not independently established for this entry.
        "friction_coefficient": 0.32866718787866145,
        # Optional finite-depth stiffening scale; zero disables the extension. Unit: m.
        # Source value (original work or literature): not independently established for this entry.
        "progressive_stiffening_depth_m": 0.0,
    },
}
