"""Editable applied settings. Original values live in source_snapshots.

These are research starting values, not a validated full-body walking fit.
Every calibrated override is saved as JSON in config/ and copied to results.
"""

from .paths import ROOT

SETTINGS = {
    "parameter_bundle_dir": None,  # Optional named, commented absolute physical values. Applied once before initialization; no runtime controller. None preserves historical configs.
    "model_variant": "base",  # Separate anatomy candidates never replace the saved base model.
    "activation_parameter_mode": "legacy",  # legacy preserves historical trials; source synchronizes native activation and offline prediction to saved time_constants (s).
    "muscle_force_scales": {},  # Actuator name -> multiplier on original Fmax; calibrated values must be documented. Original all 1.
    "period_s": 0.6833333333333333,  # Measured RH Stella trial Ted_046.
    "dt_s": 0.000125,  # Resolved hindlimb contact step; test full model at half step.
    "sample_s": 0.005,
    "seconds": 3.0,
    "fore_contact_scale": [1.0, 1.0, 1.0, 1.0],  # k_normal, dissipation, k_shear, c_shear.
    "fore_strength_scale": 1.0,  # Source Fmax unchanged.
    "girdle_strength_scale": 1.0,  # Source shoulder-girdle Fmax unchanged.
    "fore_slack_scale": 1.0,  # Source LT0 unchanged.
    "fore_fiber_damping": 0.10,  # Generic normalized damping, not measured cat value.
    "fore_passive_fiber": False,  # Historical candidate omitted passive fiber force. Optional source-exponential tensile branch; original MATLAB excludes it only in its a==1 maximum-force calculation.
    "fore_damping_mode": "normalized",  # Alternative source_velocity maps bM=0.02 times physical fiber velocity to normalized beta. A separate candidate, never a silent default change.
    "fore_force_velocity_mode": "source",  # Original/source curve remains default. Optional 'degroote_2016' is an explicit general-muscle adaptation, not cat-specific validation.
    "hind_force_velocity_mode": "source",  # Separate exploratory option; the preserved hindlimb release is never modified.
    "fore_mount_offset_m": [0.0, 0.0, 0.0],  # Original registered fore mounts retained.
    "trunk_com_offset_m": [
        0.0,
        0.0,
        0.0,
    ],  # Body-local shift of the lumped trunk COM, not bone geometry. Original zero. Fitted values require a recorded balance audit.
    "fore_pad_radius_offset_m": 0.0,  # Original radii retained; calibrated only offline.
    "passive_joint_overrides": {},  # Optional named stiffness (N m/rad), damping (N m s/rad), springref (rad). Empty preserves source values; every fitted override must be logged.
    "contact_material_scale": [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
    ],  # Shared pad k_normal, normal dissipation, k_shear, c_shear, friction multipliers. Original all 1; no force filtering.
    "initial_height_offset_m": 0.0,
    "initial_pitch_offset_rad": 0.0,
    "initial_root_velocity_offset": [
        0.0,
        0.0,
        0.0,
    ],  # t=0 forward/vertical speed (m/s), pitch speed (rad/s); offline initial-condition fitting only.
    "initial_joint_angle_offsets_rad": {},  # Named hinges, applied once at t=0 and to negative-time muscle prehistory only. Original zero.
    "initial_joint_velocity_offsets_rad_s": {},  # Named hinge rates, applied once at t=0 only. Original zero.
    "excitation_file": None,  # Fixed periodic table. Never a feedback controller.
    "excitation_sequence_file": None,  # Optional frozen per-stride tables, indexed only by time. No online correction; simulation may not exceed their recorded duration.
    "initialization_excitation_file": None,  # Optional separate waveform used only for t<0 fiber/activation initialization; runtime excitation still uses excitation_file.
    "precondition_fibers": False,  # Optional offline reference prehistory at t<0.
    "periodic_muscle_initialization": False,  # Recompute t=0 activation/fiber states from the candidate's own periodic input. No state resetting after t=0.
    "prehistory_samples": 1024,  # Samples per cycle in negative-time initialization only.
    "prehistory_cycles": 4,
    "initialize_contact_memory": False,  # Optional saved periodic bristle strain at t=0 only. No ongoing replay.
    "reference_seed": None,  # Offline reference variant, never runtime pose replay.
    "forward_initial_state_file": None,  # Optional explicitly fitted native state, applied only at t=0. No cycle resets. Original: absent.
    "initialize_from_assembled_reference": True,  # Initial pose only, no ongoing tracking.
    "spine_passive": [0.5, 0.0, 0.04],  # N m/rad, rad, N m s/rad; effective assumptions.
    "scapula_translation_passive": [10.0, 0.3],  # N/m and N s/m; assumed sling centering.
    "joint_limit_overrides": {
        "L_hip": [-2.8, -0.89]
    },  # Original [-2.8,-1.05] excluded the assumed LH reference peak (-.981 rad). New upper bound includes a 5-degree margin; NOT a measured end stop.
    "girdle_length_overrides": {},  # Name -> [LF0,LT0] metres. Originals remain in source snapshot.
    "stop_on_fall": True,
    "fit_angle_scale_deg": 10.0,
    "fit_ap_scale_N": 3.0,
    "fit_vertical_scale_N": 15.0,
    "fit_emg_weight": 2.0,  # Separate per-side, peak-normalized EMG discrepancy.
    "emg_phase_threshold": 0.10,  # New analysis setting: active when above 10% of complete-cycle peak. Not a measured neural threshold.
    "emg_phase_iou_min": 0.80,  # Engineering timing target: overlap / union of active regions. Previously timing was not separately scored.
    "emg_phase_edge_tolerance_s": 0.035,  # Engineering onset/offset tolerance (35 ms); no signal shift is permitted to obtain it.
    "native_fit_cycles": 1,  # Offline shooting horizon only. The phase-priority revision tests 2 uninterrupted input periods per fitting trial.
    "native_closure_weight": 10.0,  # Historical residual multiplier. The balanced phase-priority candidate uses 5; both values are recorded per run.
    "native_stride_residual_weight": 1.0,  # Historical displacement-target penalty. An explicit zero-weight initial-state audit predicts natural stride distance instead of requiring an exact experimental distance.
    "native_parameter_regularization": 0.001,  # Historical numerical parameter penalty; zero is allowed in a separately logged fixed-input initial-state closure audit. No runtime effect.
    "native_fit_emg_blend": False,  # Optional offline mixture toward available source EMG shapes; never an online input. Disabled in existing stability fits.
    "native_emg_blend_min": 0.0,  # 0 retains starting shape; 1 reproduces source shape at the fitted peak, with unchanged timing.
    "native_emg_blend_max": 0.05,  # Small continuation stage, not a physiological parameter. Raise only with a new documented forward fit.
    "native_emg_shape_weight": 0.05,  # Dimensionless residual weights; no motor or mechanical action.
    "native_emg_quiet_weight": 0.5,
    "native_emg_active_weight": 0.5,
    "native_waveform_weight": 0.1,  # Historical native-shooting angle/GRF residual multiplier. Revised candidate: 1.
    "native_balance_residual_families": False,  # Historical: sum all states. Revised candidate: normalize each state family by sqrt(channel count).
    "native_center_emg_blend": False,  # Numerical coordinates only; true means b=(x+1)/2, still b in [0,1]. No change to the physical input family.
    "native_unmeasured_log_gain_scale": 0.1,  # Original +/-0.1 log-amplitude range. Exploratory distal-stability fits use 0.7 ONLY for groups without source EMG. This tunes fixed input amplitudes, not Fmax; measured groups keep 0.1. Actual inputs remain 0..1.
    "native_fit_distal_waveforms": False,  # Offline only: two harmonics for six forelimb groups without source EMG; no clock shift.
    "native_distal_waveform_bound": 0.25,  # Bounds each log-waveform harmonic. Engineering fitting range, not a measured physiological coefficient.
    "native_extra_unmeasured_waveform_groups": [],  # Optional explicitly named additional groups. The fitter rejects any group with source EMG; original default adds none.
    "native_excitation_softcap_width": 0.0,  # Original hard [0,1] clip. Optional C1 upper-cap band; epsilon=.005 reduces raw u=1 by .00125, retains exact quiet zeros, and changes only the offline estimated input.
    "native_robust_direction_file": None,  # Optional diagnosed state direction for three independent OFFLINE trials. No runtime feedback is added.
    "native_robust_angle_deg": 0.1,  # Largest joint-angle error in each plus/minus offline robustness trial.
    "native_robust_target_gain": 0.9,  # Numerical contraction target over one stride, not a biological measurement.
    "native_robust_weight": 0.5,  # Weight on error growth above target; documented per optimization run.
    "native_robust_directions": 1,  # Number of diagnosed initial error directions; one plus/minus trial pair each.
    "native_fit_passive_damping": False,  # Offline calibration of bilateral wrist/MCP damping. Default preserves coefficients.
    "native_robust_measure": "directional_gain",  # Original paired norm-growth penalty. Candidate subspace_spectrum instead targets reduced stride multipliers; full-state/long replay still required.
    "native_robust_leakage_weight": 0.01,  # Numerical penalty for propagation outside a frozen diagnosed subspace. Not a physiological parameter.
    "native_passive_log_bound": 0.6931471805599453,  # +/-log(2): 0.5..2 times candidate baseline; always positive/passive. Not a measured feline uncertainty range.
    "fit_limb_weights": [1.0, 1.0, 1.0, 1.0],  # LH,RH,LF,RF equal aggregate influence.
}
