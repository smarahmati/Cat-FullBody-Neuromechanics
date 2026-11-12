# Read this file independently: executable numbers in PARAMETERS are the values used in this model.
# Source-value comments identify verified source numbers; missing sources are explicitly stated.
"""Editable muscle geometry. Read ATTACHMENT_MAP.html for connections and axes.
All xyz coordinates are METRES in the named BODY frame: 0.001 m = 1 mm.
The number assigned below is the applied value; comments preserve provenance.
Changing xyz moves a point on its existing body; it does not reattach a muscle
to a different bone. Left/right entries are independent. A visible bone mesh
does not automatically wrap a muscle. Unused sites are labelled explicitly.
For moving routing sites edit routing.py; for wrap surfaces edit wrapping.py.
Run run_model.ps1 again to apply edits. Inspect that run's ATTACHMENT_MAP.html.
"""

# Set PARAMETERS.
PARAMETERS = {
    # ===== L_IP =====
    # Branch 1, divisor 1.0: L_IP_origin [L_pelvis_anchor] -> L_IP_wrap0 [L_pelvis_anchor] -> L_IP_insert [L_thigh]
    # ===== L_BFA =====
    # Branch 1, divisor 1.0: L_BFA_origin [L_pelvis_anchor] -> L_BFA_wrap0 [L_pelvis_anchor] -> L_BFA_insert [L_thigh]
    # ===== L_VL =====
    # Branch 1, divisor 1.0: L_VL_origin [L_thigh] -> L_VL_wrap0 [L_thigh] -> L_VL_insert [L_shank]
    # ===== L_VM =====
    # Branch 1, divisor 1.0: L_VM_origin [L_thigh] -> L_VM_wrap0 [L_thigh] -> L_VM_insert [L_shank]
    # ===== L_TA =====
    # Branch 1, divisor 1.0: L_TA_origin [L_shank] -> L_TA_wrap0 [L_shank] -> L_TA_insert [L_foot]
    # ===== L_SO =====
    # Branch 1, divisor 1.0: L_SO_origin [L_shank] -> L_SO_wrap0 [L_shank] -> L_SO_insert [L_foot]
    # ===== L_RF =====
    # Branch 1, divisor 1.0: L_RF_origin [L_pelvis_anchor] -> L_RF_wrap0 [L_pelvis_anchor] -> L_RF_tangent [L_thigh] -> L_RF_wrap1 [L_thigh] -> L_RF_insert [L_shank]
    # VIA POINT for L_RF. Connected body: L_thigh. Computed local coordinates: update_routing.py overwrites them at each step.
    "L_RF_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.005420765027322405,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.010585365853658537,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 2.53073,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.004763827802212448,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.010585365853658537,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.0955,
    },
    # ===== L_BFP =====
    # Branch 1, divisor 1.0: L_BFP_origin [L_pelvis_anchor] -> L_BFP_wrap0 [L_pelvis_anchor] -> L_BFP_tangent [L_thigh] -> L_BFP_wrap1 [L_thigh] -> L_BFP_insert [L_shank]
    # VIA POINT for L_BFP. Connected body: L_thigh. Computed local coordinates: update_routing.py overwrites them at each step.
    "L_BFP_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.008469945355191258,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.03175609756097561,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 2.46091,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.004763827802212448,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.005716593362654938,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.0955,
    },
    # ===== L_SAM =====
    # Branch 1, divisor 1.0: L_SAM_origin [L_pelvis_anchor] -> L_SAM_wrap0 [L_pelvis_anchor] -> L_SAM_tangent [L_thigh] -> L_SAM_wrap1 [L_thigh] -> L_SAM_insert [L_shank]
    # VIA POINT for L_SAM. Connected body: L_thigh. Computed local coordinates: update_routing.py overwrites them at each step.
    "L_SAM_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.013551912568306013,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.010585365853658537,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.004763827802212448,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.005716593362654938,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.0955,
    },
    # ===== L_LG =====
    # Branch 1, divisor 1.0: L_LG_origin [L_thigh] -> L_LG_wrap0 [L_thigh] -> L_LG_tangent [L_shank] -> L_LG_wrap1 [L_shank] -> L_LG_insert [L_foot]
    # VIA POINT for L_LG. Connected body: L_shank. Computed local coordinates: update_routing.py overwrites them at each step.
    "L_LG_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0058890030832476885,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.01555878084179971,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -3.03687,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.0058890030832476885,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.004884810791217741,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.1085,
    },
    # ===== L_MG =====
    # Branch 1, divisor 1.0: L_MG_origin [L_thigh] -> L_MG_wrap0 [L_thigh] -> L_MG_tangent [L_shank] -> L_MG_wrap1 [L_shank] -> L_MG_insert [L_foot]
    # VIA POINT for L_MG. Connected body: L_shank. Computed local coordinates: update_routing.py overwrites them at each step.
    "L_MG_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0058890030832476885,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.01555878084179971,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -3.03687,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.0058890030832476885,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.004884810791217741,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.1085,
    },
    # ===== R_IP =====
    # Branch 1, divisor 1.0: R_IP_origin [R_pelvis_anchor] -> R_IP_wrap0 [R_pelvis_anchor] -> R_IP_insert [R_thigh]
    # ===== R_BFA =====
    # Branch 1, divisor 1.0: R_BFA_origin [R_pelvis_anchor] -> R_BFA_wrap0 [R_pelvis_anchor] -> R_BFA_insert [R_thigh]
    # ===== R_VL =====
    # Branch 1, divisor 1.0: R_VL_origin [R_thigh] -> R_VL_wrap0 [R_thigh] -> R_VL_insert [R_shank]
    # ===== R_VM =====
    # Branch 1, divisor 1.0: R_VM_origin [R_thigh] -> R_VM_wrap0 [R_thigh] -> R_VM_insert [R_shank]
    # ===== R_TA =====
    # Branch 1, divisor 1.0: R_TA_origin [R_shank] -> R_TA_wrap0 [R_shank] -> R_TA_insert [R_foot]
    # ===== R_SO =====
    # Branch 1, divisor 1.0: R_SO_origin [R_shank] -> R_SO_wrap0 [R_shank] -> R_SO_insert [R_foot]
    # ===== R_RF =====
    # Branch 1, divisor 1.0: R_RF_origin [R_pelvis_anchor] -> R_RF_wrap0 [R_pelvis_anchor] -> R_RF_tangent [R_thigh] -> R_RF_wrap1 [R_thigh] -> R_RF_insert [R_shank]
    # VIA POINT for R_RF. Connected body: R_thigh. Computed local coordinates: update_routing.py overwrites them at each step.
    "R_RF_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.005420765027322405,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.010585365853658537,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 2.53073,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.004763827802212448,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.010585365853658537,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.0955,
    },
    # ===== R_BFP =====
    # Branch 1, divisor 1.0: R_BFP_origin [R_pelvis_anchor] -> R_BFP_wrap0 [R_pelvis_anchor] -> R_BFP_tangent [R_thigh] -> R_BFP_wrap1 [R_thigh] -> R_BFP_insert [R_shank]
    # VIA POINT for R_BFP. Connected body: R_thigh. Computed local coordinates: update_routing.py overwrites them at each step.
    "R_BFP_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.008469945355191258,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.03175609756097561,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 2.46091,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.004763827802212448,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.005716593362654938,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.0955,
    },
    # ===== R_SAM =====
    # Branch 1, divisor 1.0: R_SAM_origin [R_pelvis_anchor] -> R_SAM_wrap0 [R_pelvis_anchor] -> R_SAM_tangent [R_thigh] -> R_SAM_wrap1 [R_thigh] -> R_SAM_insert [R_shank]
    # VIA POINT for R_SAM. Connected body: R_thigh. Computed local coordinates: update_routing.py overwrites them at each step.
    "R_SAM_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.013551912568306013,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.010585365853658537,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.004763827802212448,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.005716593362654938,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.0955,
    },
    # ===== R_LG =====
    # Branch 1, divisor 1.0: R_LG_origin [R_thigh] -> R_LG_wrap0 [R_thigh] -> R_LG_tangent [R_shank] -> R_LG_wrap1 [R_shank] -> R_LG_insert [R_foot]
    # VIA POINT for R_LG. Connected body: R_shank. Computed local coordinates: update_routing.py overwrites them at each step.
    "R_LG_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0058890030832476885,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.01555878084179971,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -3.03687,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.0058890030832476885,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.004884810791217741,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.1085,
    },
    # ===== R_MG =====
    # Branch 1, divisor 1.0: R_MG_origin [R_thigh] -> R_MG_wrap0 [R_thigh] -> R_MG_tangent [R_shank] -> R_MG_wrap1 [R_shank] -> R_MG_insert [R_foot]
    # VIA POINT for R_MG. Connected body: R_shank. Computed local coordinates: update_routing.py overwrites them at each step.
    "R_MG_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0058890030832476885,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.01555878084179971,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -3.03687,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.0058890030832476885,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.004884810791217741,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.1085,
    },
    # ===== L_EDL =====
    # Branch 1, divisor 1.0: L_EDL_osim_0 [L_shank] -> L_EDL_osim_1 [L_shank] -> L_EDL_osim_2 [L_foot] -> L_EDL_osim_3 [L_foot] -> L_EDL_osim_4 [L_foot] -> L_EDL_osim_5 [L_foot] -> L_EDL_osim_6 [L_digits]
    # ===== R_EDL =====
    # Branch 1, divisor 1.0: R_EDL_osim_0 [R_shank] -> R_EDL_osim_1 [R_shank] -> R_EDL_osim_2 [R_foot] -> R_EDL_osim_3 [R_foot] -> R_EDL_osim_4 [R_foot] -> R_EDL_osim_5 [R_foot] -> R_EDL_osim_6 [R_digits]
    # ===== L_FDL =====
    # Branch 1, divisor 1.0: L_FDL_osim_0 [L_shank] -> L_FDL_osim_1 [L_shank] -> L_FDL_osim_2 [L_foot] -> L_FDL_osim_3 [L_foot] -> L_FDL_osim_4 [L_digits]
    # ===== R_FDL =====
    # Branch 1, divisor 1.0: R_FDL_osim_0 [R_shank] -> R_FDL_osim_1 [R_shank] -> R_FDL_osim_2 [R_foot] -> R_FDL_osim_3 [R_foot] -> R_FDL_osim_4 [R_digits]
    # ===== L_FHL =====
    # Branch 1, divisor 1.0: L_FHL_attachment0 [L_shank] -> L_FHL_attachment1 [L_shank] -> L_FHL_attachment2 [L_foot] -> L_FHL_attachment3 [L_foot] -> L_FHL_attachment4 [L_digits]
    # ===== R_FHL =====
    # Branch 1, divisor 1.0: R_FHL_attachment0 [R_shank] -> R_FHL_attachment1 [R_shank] -> R_FHL_attachment2 [R_foot] -> R_FHL_attachment3 [R_foot] -> R_FHL_attachment4 [R_digits]
    # ===== FL_ShoulderExtensor =====
    # Branch 1, divisor 1.0: FL_ShoulderExtensor_s0_origin [FL_scapula] -> FL_ShoulderExtensor_s0_pulley0 [FL_scapula] -> FL_ShoulderExtensor_s0_insert [FL_upperarm]
    # WRAP SIDE SELECTOR for FL_ShoulderExtensor. Body: FL_scapula. NOT a path vertex or anatomical attachment.
    "FL_ShoulderExtensor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0564002012493833,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.00794548203380911,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -0.277010006173251,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 2.39160180521177,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00794485115987297,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.05771428571428572,
    },
    # ===== FL_ElbowExtensor =====
    # Branch 1, divisor 1.0: FL_ElbowExtensor_s0_origin [FL_upperarm] -> FL_ElbowExtensor_s0_pulley0 [FL_upperarm] -> FL_ElbowExtensor_s0_insert [FL_forearm]
    # WRAP SIDE SELECTOR for FL_ElbowExtensor. Body: FL_upperarm. NOT a path vertex or anatomical attachment.
    "FL_ElbowExtensor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0600016465411511,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.00558020397995713,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.155275208613396,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -2.69130152425526,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00211767658246807,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # ===== FL_BicepsBrachii =====
    # Branch 1, divisor 1.0: FL_BicepsBrachii_s0_origin [FL_scapula] -> FL_BicepsBrachii_s0_pulley0 [FL_scapula] -> FL_BicepsBrachii_s0_tangent [FL_upperarm] -> FL_BicepsBrachii_s0_pulley1 [FL_upperarm] -> FL_BicepsBrachii_s0_insert [FL_forearm]
    # VIA POINT for FL_BicepsBrachii. Connected body: FL_upperarm. Computed local coordinates: update_routing.py overwrites them at each step.
    "FL_BicepsBrachii_s0_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.012186834291057365,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.011134867494658732,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -1.9686494462266706,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -0.40005001439213644,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.009946928604793973,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.005259145389888545,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # ===== FL_ElbowFlexor =====
    # Branch 1, divisor 1.0: FL_ElbowFlexor_s0_origin [FL_upperarm] -> FL_ElbowFlexor_s0_pulley0 [FL_upperarm] -> FL_ElbowFlexor_s0_insert [FL_forearm]
    # WRAP SIDE SELECTOR for FL_ElbowFlexor. Body: FL_upperarm. NOT a path vertex or anatomical attachment.
    "FL_ElbowFlexor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0715037507591663,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.00740043933035868,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -0.0697366814458689,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.898729071000832,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00320000000000039,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # ===== FL_ElbowFlexorWristFlexor =====
    # Branch 1, divisor 1.0: FL_ElbowFlexorWristFlexor_s0_origin [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_pulley0 [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_insert [FL_forearm]
    # WRAP SIDE SELECTOR for FL_ElbowFlexorWristFlexor. Body: FL_upperarm. NOT a path vertex or anatomical attachment.
    "FL_ElbowFlexorWristFlexor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0114000013042347,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0951000002121869,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.286687371689756,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.0645005602980572,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00536465406611287,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # Branch 2, divisor 1.0: FL_ElbowFlexorWristFlexor_s1_origin [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_pulley0 [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_insert [FL_carpals]
    # WRAP SIDE SELECTOR for FL_ElbowFlexorWristFlexor. Body: FL_forearm. NOT a path vertex or anatomical attachment.
    "FL_ElbowFlexorWristFlexor_s1_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0061346492911567106,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0332999926671867,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -1.530831880600672,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.12583820430839,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00350749590190618,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09465714285714286,
    },
    # ===== FL_WristFlexor =====
    # Branch 1, divisor 1.0: FL_WristFlexor_s0_origin [FL_forearm] -> FL_WristFlexor_s0_insert [FL_forearm]
    # Branch 2, divisor 1.0: FL_WristFlexor_s1_origin [FL_forearm] -> FL_WristFlexor_s1_pulley0 [FL_forearm] -> FL_WristFlexor_s1_insert [FL_carpals]
    # WRAP SIDE SELECTOR for FL_WristFlexor. Body: FL_forearm. NOT a path vertex or anatomical attachment.
    "FL_WristFlexor_s1_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.006009024678845052,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0171115446907036,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -2.3325124139914677,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.114800555463146,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.0024,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09465714285714286,
    },
    # ===== FL_WristExtensor =====
    # Branch 1, divisor 1.0: FL_WristExtensor_s0_origin [FL_forearm] -> FL_WristExtensor_s0_insert [FL_forearm]
    # Branch 2, divisor 1.0: FL_WristExtensor_s1_origin [FL_forearm] -> FL_WristExtensor_s1_pulley0 [FL_forearm] -> FL_WristExtensor_s1_insert [FL_carpals]
    # WRAP SIDE SELECTOR for FL_WristExtensor. Body: FL_forearm. NOT a path vertex or anatomical attachment.
    "FL_WristExtensor_s1_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.00518652885093298,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0288587788186216,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 1.282292184119631,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -0.163175752538083,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00271044296770131,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09465714285714286,
    },
    # ===== FL_ShoulderFlexor =====
    # Branch 1, divisor 1.0: FL_ShoulderFlexor_s0_origin [FL_scapula] -> FL_ShoulderFlexor_s0_pulley0 [FL_scapula] -> FL_ShoulderFlexor_s0_insert [FL_upperarm]
    # WRAP SIDE SELECTOR for FL_ShoulderFlexor. Body: FL_scapula. NOT a path vertex or anatomical attachment.
    "FL_ShoulderFlexor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0507609523493369,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0167000301127897,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.127927581350083,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.594581222632492,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00184271114122135,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.05771428571428572,
    },
    # ===== FL_TricepsBrachiiLong =====
    # Branch 1, divisor 1.0: FL_TricepsBrachiiLong_s0_origin [FL_scapula] -> FL_TricepsBrachiiLong_s0_pulley0 [FL_scapula] -> FL_TricepsBrachiiLong_s0_tangent [FL_upperarm] -> FL_TricepsBrachiiLong_s0_pulley1 [FL_upperarm] -> FL_TricepsBrachiiLong_s0_insert [FL_forearm]
    # VIA POINT for FL_TricepsBrachiiLong. Connected body: FL_upperarm. Computed local coordinates: update_routing.py overwrites them at each step.
    "FL_TricepsBrachiiLong_s0_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.01023654140200321,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.014854093335665784,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -0.04621934250258526,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -2.8324783497454353,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.004419416012604855,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.011883274668532628,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # ===== FR_ShoulderExtensor =====
    # Branch 1, divisor 1.0: FR_ShoulderExtensor_s0_origin [FR_scapula] -> FR_ShoulderExtensor_s0_pulley0 [FR_scapula] -> FR_ShoulderExtensor_s0_insert [FR_upperarm]
    # WRAP SIDE SELECTOR for FR_ShoulderExtensor. Body: FR_scapula. NOT a path vertex or anatomical attachment.
    "FR_ShoulderExtensor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0564002012493833,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.00794548203380911,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -0.277010006173251,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 2.39160180521177,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00794485115987297,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.05771428571428572,
    },
    # ===== FR_ElbowExtensor =====
    # Branch 1, divisor 1.0: FR_ElbowExtensor_s0_origin [FR_upperarm] -> FR_ElbowExtensor_s0_pulley0 [FR_upperarm] -> FR_ElbowExtensor_s0_insert [FR_forearm]
    # WRAP SIDE SELECTOR for FR_ElbowExtensor. Body: FR_upperarm. NOT a path vertex or anatomical attachment.
    "FR_ElbowExtensor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0600016465411511,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.00558020397995713,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.155275208613396,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -2.69130152425526,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00211767658246807,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # ===== FR_BicepsBrachii =====
    # Branch 1, divisor 1.0: FR_BicepsBrachii_s0_origin [FR_scapula] -> FR_BicepsBrachii_s0_pulley0 [FR_scapula] -> FR_BicepsBrachii_s0_tangent [FR_upperarm] -> FR_BicepsBrachii_s0_pulley1 [FR_upperarm] -> FR_BicepsBrachii_s0_insert [FR_forearm]
    # VIA POINT for FR_BicepsBrachii. Connected body: FR_upperarm. Computed local coordinates: update_routing.py overwrites them at each step.
    "FR_BicepsBrachii_s0_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.012186834291057365,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.011134867494658732,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -1.9686494462266706,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -0.40005001439213644,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.009946928604793973,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.005259145389888545,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # ===== FR_ElbowFlexor =====
    # Branch 1, divisor 1.0: FR_ElbowFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexor_s0_insert [FR_forearm]
    # WRAP SIDE SELECTOR for FR_ElbowFlexor. Body: FR_upperarm. NOT a path vertex or anatomical attachment.
    "FR_ElbowFlexor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0715037507591663,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.00740043933035868,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -0.0697366814458689,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.898729071000832,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00320000000000039,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # ===== FR_ElbowFlexorWristFlexor =====
    # Branch 1, divisor 1.0: FR_ElbowFlexorWristFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_insert [FR_forearm]
    # WRAP SIDE SELECTOR for FR_ElbowFlexorWristFlexor. Body: FR_upperarm. NOT a path vertex or anatomical attachment.
    "FR_ElbowFlexorWristFlexor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0114000013042347,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0951000002121869,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.286687371689756,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.0645005602980572,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00536465406611287,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # Branch 2, divisor 1.0: FR_ElbowFlexorWristFlexor_s1_origin [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_pulley0 [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_insert [FR_carpals]
    # WRAP SIDE SELECTOR for FR_ElbowFlexorWristFlexor. Body: FR_forearm. NOT a path vertex or anatomical attachment.
    "FR_ElbowFlexorWristFlexor_s1_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0061346492911567106,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0332999926671867,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -1.530831880600672,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.12583820430839,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00350749590190618,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09465714285714286,
    },
    # ===== FR_WristFlexor =====
    # Branch 1, divisor 1.0: FR_WristFlexor_s0_origin [FR_forearm] -> FR_WristFlexor_s0_insert [FR_forearm]
    # Branch 2, divisor 1.0: FR_WristFlexor_s1_origin [FR_forearm] -> FR_WristFlexor_s1_pulley0 [FR_forearm] -> FR_WristFlexor_s1_insert [FR_carpals]
    # WRAP SIDE SELECTOR for FR_WristFlexor. Body: FR_forearm. NOT a path vertex or anatomical attachment.
    "FR_WristFlexor_s1_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.006009024678845052,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0171115446907036,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -2.3325124139914677,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.114800555463146,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.0024,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09465714285714286,
    },
    # ===== FR_WristExtensor =====
    # Branch 1, divisor 1.0: FR_WristExtensor_s0_origin [FR_forearm] -> FR_WristExtensor_s0_insert [FR_forearm]
    # Branch 2, divisor 1.0: FR_WristExtensor_s1_origin [FR_forearm] -> FR_WristExtensor_s1_pulley0 [FR_forearm] -> FR_WristExtensor_s1_insert [FR_carpals]
    # WRAP SIDE SELECTOR for FR_WristExtensor. Body: FR_forearm. NOT a path vertex or anatomical attachment.
    "FR_WristExtensor_s1_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.00518652885093298,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0288587788186216,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 1.282292184119631,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -0.163175752538083,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00271044296770131,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09465714285714286,
    },
    # ===== FR_ShoulderFlexor =====
    # Branch 1, divisor 1.0: FR_ShoulderFlexor_s0_origin [FR_scapula] -> FR_ShoulderFlexor_s0_pulley0 [FR_scapula] -> FR_ShoulderFlexor_s0_insert [FR_upperarm]
    # WRAP SIDE SELECTOR for FR_ShoulderFlexor. Body: FR_scapula. NOT a path vertex or anatomical attachment.
    "FR_ShoulderFlexor_s0_preferred": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.0507609523493369,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.0167000301127897,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": 0.127927581350083,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": 0.594581222632492,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.00184271114122135,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": 0.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.05771428571428572,
    },
    # ===== FR_TricepsBrachiiLong =====
    # Branch 1, divisor 1.0: FR_TricepsBrachiiLong_s0_origin [FR_scapula] -> FR_TricepsBrachiiLong_s0_pulley0 [FR_scapula] -> FR_TricepsBrachiiLong_s0_tangent [FR_upperarm] -> FR_TricepsBrachiiLong_s0_pulley1 [FR_upperarm] -> FR_TricepsBrachiiLong_s0_insert [FR_forearm]
    # VIA POINT for FR_TricepsBrachiiLong. Connected body: FR_upperarm. Computed local coordinates: update_routing.py overwrites them at each step.
    "FR_TricepsBrachiiLong_s0_tangent": {
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "origin_radius_m": 0.01023654140200321,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "insertion_radius_m": 0.014854093335665784,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "origin_angle_rad": -0.04621934250258526,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: rad.
        # Original raw/source: None; None = not independently established.
        "insertion_angle_rad": -2.8324783497454353,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_radius_m": 0.004419416012604855,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "proximal_joint_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_radius_m": 0.011883274668532628,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_wrap_sign": 1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "distal_joint_sign": -1.0,
        # Analytical moving-via routing parameter; see update_routing.py and route_biarticular.py. Unit: m.
        # Original raw/source: None; None = not independently established.
        "joint_spacing_m": 0.09275714285714286,
    },
    # ===== FL_S_C3 =====
    # Branch 1, divisor 1.0: FL_S_C3_attachment0 [FL_scapula] -> FL_S_C3_attachment1 [cat_root]
    # ===== FR_S_C3 =====
    # Branch 1, divisor 1.0: FR_S_C3_attachment0 [FR_scapula] -> FR_S_C3_attachment1 [cat_root]
    # ===== FL_S_C4 =====
    # Branch 1, divisor 1.0: FL_S_C4_attachment0 [FL_scapula] -> FL_S_C4_attachment1 [cat_root]
    # ===== FR_S_C4 =====
    # Branch 1, divisor 1.0: FR_S_C4_attachment0 [FR_scapula] -> FR_S_C4_attachment1 [cat_root]
    # ===== FL_S_C5 =====
    # Branch 1, divisor 1.0: FL_S_C5_attachment0 [FL_scapula] -> FL_S_C5_attachment1 [cat_root]
    # ===== FR_S_C5 =====
    # Branch 1, divisor 1.0: FR_S_C5_attachment0 [FR_scapula] -> FR_S_C5_attachment1 [cat_root]
    # ===== FL_S_C6 =====
    # Branch 1, divisor 1.0: FL_S_C6_attachment0 [FL_scapula] -> FL_S_C6_attachment1 [cat_root]
    # ===== FR_S_C6 =====
    # Branch 1, divisor 1.0: FR_S_C6_attachment0 [FR_scapula] -> FR_S_C6_attachment1 [cat_root]
    # ===== FL_S_C7 =====
    # Branch 1, divisor 1.0: FL_S_C7_attachment0 [FL_scapula] -> FL_S_C7_attachment1 [cat_root]
    # ===== FR_S_C7 =====
    # Branch 1, divisor 1.0: FR_S_C7_attachment0 [FR_scapula] -> FR_S_C7_attachment1 [cat_root]
    # ===== FL_S_T1 =====
    # Branch 1, divisor 1.0: FL_S_T1_attachment0 [FL_scapula] -> FL_S_T1_attachment1 [cat_root]
    # ===== FR_S_T1 =====
    # Branch 1, divisor 1.0: FR_S_T1_attachment0 [FR_scapula] -> FR_S_T1_attachment1 [cat_root]
    # ===== FL_S_T2 =====
    # Branch 1, divisor 1.0: FL_S_T2_attachment0 [FL_scapula] -> FL_S_T2_attachment1 [cat_root]
    # ===== FR_S_T2 =====
    # Branch 1, divisor 1.0: FR_S_T2_attachment0 [FR_scapula] -> FR_S_T2_attachment1 [cat_root]
    # ===== FL_S_T3 =====
    # Branch 1, divisor 1.0: FL_S_T3_attachment0 [FL_scapula] -> FL_S_T3_attachment1 [cat_root]
    # ===== FR_S_T3 =====
    # Branch 1, divisor 1.0: FR_S_T3_attachment0 [FR_scapula] -> FR_S_T3_attachment1 [cat_root]
    # ===== FL_S_T4 =====
    # Branch 1, divisor 1.0: FL_S_T4_attachment0 [FL_scapula] -> FL_S_T4_attachment1 [cat_root]
    # ===== FR_S_T4 =====
    # Branch 1, divisor 1.0: FR_S_T4_attachment0 [FR_scapula] -> FR_S_T4_attachment1 [cat_root]
    # ===== FL_S_T5 =====
    # Branch 1, divisor 1.0: FL_S_T5_attachment0 [FL_scapula] -> FL_S_T5_attachment1 [cat_root]
    # ===== FR_S_T5 =====
    # Branch 1, divisor 1.0: FR_S_T5_attachment0 [FR_scapula] -> FR_S_T5_attachment1 [cat_root]
    # ===== FL_S_T6 =====
    # Branch 1, divisor 1.0: FL_S_T6_attachment0 [FL_scapula] -> FL_S_T6_attachment1 [cat_root]
    # ===== FR_S_T6 =====
    # Branch 1, divisor 1.0: FR_S_T6_attachment0 [FR_scapula] -> FR_S_T6_attachment1 [cat_root]
    # ===== FL_S_T7 =====
    # Branch 1, divisor 1.0: FL_S_T7_attachment0 [FL_scapula] -> FL_S_T7_attachment1 [cat_root]
    # ===== FR_S_T7 =====
    # Branch 1, divisor 1.0: FR_S_T7_attachment0 [FR_scapula] -> FR_S_T7_attachment1 [cat_root]
    # ===== FL_S_T8 =====
    # Branch 1, divisor 1.0: FL_S_T8_attachment0 [FL_scapula] -> FL_S_T8_attachment1 [cat_root]
    # ===== FR_S_T8 =====
    # Branch 1, divisor 1.0: FR_S_T8_attachment0 [FR_scapula] -> FR_S_T8_attachment1 [cat_root]
    # ===== FL_S_T9 =====
    # Branch 1, divisor 1.0: FL_S_T9_attachment0 [FL_scapula] -> FL_S_T9_attachment1 [cat_root]
    # ===== FR_S_T9 =====
    # Branch 1, divisor 1.0: FR_S_T9_attachment0 [FR_scapula] -> FR_S_T9_attachment1 [cat_root]
    # ===== FL_R_C2 =====
    # Branch 1, divisor 1.0: FL_R_C2_attachment0 [FL_scapula] -> FL_R_C2_attachment1 [cat_root]
    # ===== FR_R_C2 =====
    # Branch 1, divisor 1.0: FR_R_C2_attachment0 [FR_scapula] -> FR_R_C2_attachment1 [cat_root]
    # ===== FL_R_C3-7 =====
    # Branch 1, divisor 1.0: FL_R_C3-7_attachment0 [FL_scapula] -> FL_R_C3-7_attachment1 [cat_root]
    # ===== FR_R_C3-7 =====
    # Branch 1, divisor 1.0: FR_R_C3-7_attachment0 [FR_scapula] -> FR_R_C3-7_attachment1 [cat_root]
    # ===== FL_R_T1 =====
    # Branch 1, divisor 1.0: FL_R_T1_attachment0 [FL_scapula] -> FL_R_T1_attachment1 [cat_root]
    # ===== FR_R_T1 =====
    # Branch 1, divisor 1.0: FR_R_T1_attachment0 [FR_scapula] -> FR_R_T1_attachment1 [cat_root]
    # ===== FL_R_T2 =====
    # Branch 1, divisor 1.0: FL_R_T2_attachment0 [FL_scapula] -> FL_R_T2_attachment1 [cat_root]
    # ===== FR_R_T2 =====
    # Branch 1, divisor 1.0: FR_R_T2_attachment0 [FR_scapula] -> FR_R_T2_attachment1 [cat_root]
    # ===== FL_R_T3 =====
    # Branch 1, divisor 1.0: FL_R_T3_attachment0 [FL_scapula] -> FL_R_T3_attachment1 [cat_root]
    # ===== FR_R_T3 =====
    # Branch 1, divisor 1.0: FR_R_T3_attachment0 [FR_scapula] -> FR_R_T3_attachment1 [cat_root]
    # ===== FL_R_T4 =====
    # Branch 1, divisor 1.0: FL_R_T4_attachment0 [FL_scapula] -> FL_R_T4_attachment1 [cat_root]
    # ===== FR_R_T4 =====
    # Branch 1, divisor 1.0: FR_R_T4_attachment0 [FR_scapula] -> FR_R_T4_attachment1 [cat_root]
    # ===== FL_R_T5 =====
    # Branch 1, divisor 1.0: FL_R_T5_attachment0 [FL_scapula] -> FL_R_T5_attachment1 [cat_root]
    # ===== FR_R_T5 =====
    # Branch 1, divisor 1.0: FR_R_T5_attachment0 [FR_scapula] -> FR_R_T5_attachment1 [cat_root]
    # ===== FL_DigitalExtensors =====
    # Branch 1, divisor 1.0: FL_ElbowFlexorWristFlexor_s0_origin [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_pulley0 [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_insert [FL_forearm]
    # Shared entry 'FL_ElbowFlexorWristFlexor_s0_preferred': already defined above.
    # Branch 2, divisor 1.0: FL_ElbowFlexorWristFlexor_s1_origin [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_pulley0 [FL_forearm] -> FL_DigitalExtensors_attachment0 [FL_carpals] -> FL_DigitalExtensors_attachment1 [FL_digits]
    # Shared entry 'FL_ElbowFlexorWristFlexor_s1_preferred': already defined above.
    # ===== FR_DigitalExtensors =====
    # Branch 1, divisor 1.0: FR_ElbowFlexorWristFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_insert [FR_forearm]
    # Shared entry 'FR_ElbowFlexorWristFlexor_s0_preferred': already defined above.
    # Branch 2, divisor 1.0: FR_ElbowFlexorWristFlexor_s1_origin [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_pulley0 [FR_forearm] -> FR_DigitalExtensors_attachment0 [FR_carpals] -> FR_DigitalExtensors_attachment1 [FR_digits]
    # Shared entry 'FR_ElbowFlexorWristFlexor_s1_preferred': already defined above.
    # ===== FL_DigitalFlexors =====
    # Branch 1, divisor 1.0: FL_WristExtensor_s0_origin [FL_forearm] -> FL_WristExtensor_s0_insert [FL_forearm]
    # Branch 2, divisor 1.0: FL_WristExtensor_s1_origin [FL_forearm] -> FL_WristExtensor_s1_pulley0 [FL_forearm] -> FL_DigitalFlexors_attachment0 [FL_carpals] -> FL_DigitalFlexors_attachment1 [FL_digits]
    # Shared entry 'FL_WristExtensor_s1_preferred': already defined above.
    # ===== FR_DigitalFlexors =====
    # Branch 1, divisor 1.0: FR_WristExtensor_s0_origin [FR_forearm] -> FR_WristExtensor_s0_insert [FR_forearm]
    # Branch 2, divisor 1.0: FR_WristExtensor_s1_origin [FR_forearm] -> FR_WristExtensor_s1_pulley0 [FR_forearm] -> FR_DigitalFlexors_attachment0 [FR_carpals] -> FR_DigitalFlexors_attachment1 [FR_digits]
    # Shared entry 'FR_WristExtensor_s1_preferred': already defined above.
    # ===== FL_TrapeziusCervical =====
    # Branch 1, divisor 1.0: FL_TrapeziusCervical_origin [cat_root] -> FL_TrapeziusCervical_insertion [FL_scapula]
    # ===== FR_TrapeziusCervical =====
    # Branch 1, divisor 1.0: FR_TrapeziusCervical_origin [cat_root] -> FR_TrapeziusCervical_insertion [FR_scapula]
    # ===== FL_TrapeziusThoracic =====
    # Branch 1, divisor 1.0: FL_TrapeziusThoracic_origin [cat_root] -> FL_TrapeziusThoracic_insertion [FL_scapula]
    # ===== FR_TrapeziusThoracic =====
    # Branch 1, divisor 1.0: FR_TrapeziusThoracic_origin [cat_root] -> FR_TrapeziusThoracic_insertion [FR_scapula]
    # ===== FL_LatissimusDorsi =====
    # Branch 1, divisor 1.0: FL_LatissimusDorsi_origin [cat_root] -> FL_LatissimusDorsi_insertion [FL_upperarm]
    # ===== FR_LatissimusDorsi =====
    # Branch 1, divisor 1.0: FR_LatissimusDorsi_origin [cat_root] -> FR_LatissimusDorsi_insertion [FR_upperarm]
    # ===== FL_PectoralisProfundus =====
    # Branch 1, divisor 1.0: FL_PectoralisProfundus_origin [cat_root] -> FL_PectoralisProfundus_insertion [FL_upperarm]
    # ===== FR_PectoralisProfundus =====
    # Branch 1, divisor 1.0: FR_PectoralisProfundus_origin [cat_root] -> FR_PectoralisProfundus_insertion [FR_upperarm]
    # ===== FL_PectoralisSuperficialis =====
    # Branch 1, divisor 1.0: FL_PectoralisSuperficialis_origin [cat_root] -> FL_PectoralisSuperficialis_insertion [FL_upperarm]
    # ===== FR_PectoralisSuperficialis =====
    # Branch 1, divisor 1.0: FR_PectoralisSuperficialis_origin [cat_root] -> FR_PectoralisSuperficialis_insertion [FR_upperarm]
    # ===== FL_Clavobrachialis =====
    # Branch 1, divisor 1.0: FL_Clavobrachialis_origin [cat_root] -> FL_Clavobrachialis_insertion [FL_upperarm]
    # ===== FR_Clavobrachialis =====
    # Branch 1, divisor 1.0: FR_Clavobrachialis_origin [cat_root] -> FR_Clavobrachialis_insertion [FR_upperarm]
}
