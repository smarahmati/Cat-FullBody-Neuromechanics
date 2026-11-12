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
    # CYLINDER WRAP for L_IP. Connected body: L_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "L_IP_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004571237622484351,
    },
    # ===== L_BFA =====
    # Branch 1, divisor 1.0: L_BFA_origin [L_pelvis_anchor] -> L_BFA_wrap0 [L_pelvis_anchor] -> L_BFA_insert [L_thigh]
    # CYLINDER WRAP for L_BFA. Connected body: L_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "L_BFA_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004571237622484351,
    },
    # ===== L_VL =====
    # Branch 1, divisor 1.0: L_VL_origin [L_thigh] -> L_VL_wrap0 [L_thigh] -> L_VL_insert [L_shank]
    # CYLINDER WRAP for L_VL. Connected body: L_thigh. Geometry of a routing surface, not a bone attachment.
    "L_VL_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.010585365852658537,
    },
    # ===== L_VM =====
    # Branch 1, divisor 1.0: L_VM_origin [L_thigh] -> L_VM_wrap0 [L_thigh] -> L_VM_insert [L_shank]
    # CYLINDER WRAP for L_VM. Connected body: L_thigh. Geometry of a routing surface, not a bone attachment.
    "L_VM_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.010585365852658537,
    },
    # ===== L_TA =====
    # Branch 1, divisor 1.0: L_TA_origin [L_shank] -> L_TA_wrap0 [L_shank] -> L_TA_insert [L_foot]
    # CYLINDER WRAP for L_TA. Connected body: L_shank. Geometry of a routing surface, not a bone attachment.
    "L_TA_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005077400968945839,
    },
    # ===== L_SO =====
    # Branch 1, divisor 1.0: L_SO_origin [L_shank] -> L_SO_wrap0 [L_shank] -> L_SO_insert [L_foot]
    # CYLINDER WRAP for L_SO. Connected body: L_shank. Geometry of a routing surface, not a bone attachment.
    "L_SO_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005077400968945839,
    },
    # ===== L_RF =====
    # Branch 1, divisor 1.0: L_RF_origin [L_pelvis_anchor] -> L_RF_wrap0 [L_pelvis_anchor] -> L_RF_tangent [L_thigh] -> L_RF_wrap1 [L_thigh] -> L_RF_insert [L_shank]
    # CYLINDER WRAP for L_RF. Connected body: L_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "L_RF_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004763827801212448,
    },
    # CYLINDER WRAP for L_RF. Connected body: L_thigh. Geometry of a routing surface, not a bone attachment.
    "L_RF_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.010585365852658537,
    },
    # ===== L_BFP =====
    # Branch 1, divisor 1.0: L_BFP_origin [L_pelvis_anchor] -> L_BFP_wrap0 [L_pelvis_anchor] -> L_BFP_tangent [L_thigh] -> L_BFP_wrap1 [L_thigh] -> L_BFP_insert [L_shank]
    # CYLINDER WRAP for L_BFP. Connected body: L_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "L_BFP_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004763827801212448,
    },
    # CYLINDER WRAP for L_BFP. Connected body: L_thigh. Geometry of a routing surface, not a bone attachment.
    "L_BFP_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005716593361654938,
    },
    # ===== L_SAM =====
    # Branch 1, divisor 1.0: L_SAM_origin [L_pelvis_anchor] -> L_SAM_wrap0 [L_pelvis_anchor] -> L_SAM_tangent [L_thigh] -> L_SAM_wrap1 [L_thigh] -> L_SAM_insert [L_shank]
    # CYLINDER WRAP for L_SAM. Connected body: L_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "L_SAM_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004763827801212448,
    },
    # CYLINDER WRAP for L_SAM. Connected body: L_thigh. Geometry of a routing surface, not a bone attachment.
    "L_SAM_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005716593361654938,
    },
    # ===== L_LG =====
    # Branch 1, divisor 1.0: L_LG_origin [L_thigh] -> L_LG_wrap0 [L_thigh] -> L_LG_tangent [L_shank] -> L_LG_wrap1 [L_shank] -> L_LG_insert [L_foot]
    # CYLINDER WRAP for L_LG. Connected body: L_thigh. Geometry of a routing surface, not a bone attachment.
    "L_LG_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005889003082247688,
    },
    # CYLINDER WRAP for L_LG. Connected body: L_shank. Geometry of a routing surface, not a bone attachment.
    "L_LG_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004884810790217741,
    },
    # ===== L_MG =====
    # Branch 1, divisor 1.0: L_MG_origin [L_thigh] -> L_MG_wrap0 [L_thigh] -> L_MG_tangent [L_shank] -> L_MG_wrap1 [L_shank] -> L_MG_insert [L_foot]
    # CYLINDER WRAP for L_MG. Connected body: L_thigh. Geometry of a routing surface, not a bone attachment.
    "L_MG_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005889003082247688,
    },
    # CYLINDER WRAP for L_MG. Connected body: L_shank. Geometry of a routing surface, not a bone attachment.
    "L_MG_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004884810790217741,
    },
    # ===== R_IP =====
    # Branch 1, divisor 1.0: R_IP_origin [R_pelvis_anchor] -> R_IP_wrap0 [R_pelvis_anchor] -> R_IP_insert [R_thigh]
    # CYLINDER WRAP for R_IP. Connected body: R_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "R_IP_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004571237622484351,
    },
    # ===== R_BFA =====
    # Branch 1, divisor 1.0: R_BFA_origin [R_pelvis_anchor] -> R_BFA_wrap0 [R_pelvis_anchor] -> R_BFA_insert [R_thigh]
    # CYLINDER WRAP for R_BFA. Connected body: R_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "R_BFA_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004571237622484351,
    },
    # ===== R_VL =====
    # Branch 1, divisor 1.0: R_VL_origin [R_thigh] -> R_VL_wrap0 [R_thigh] -> R_VL_insert [R_shank]
    # CYLINDER WRAP for R_VL. Connected body: R_thigh. Geometry of a routing surface, not a bone attachment.
    "R_VL_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.010585365852658537,
    },
    # ===== R_VM =====
    # Branch 1, divisor 1.0: R_VM_origin [R_thigh] -> R_VM_wrap0 [R_thigh] -> R_VM_insert [R_shank]
    # CYLINDER WRAP for R_VM. Connected body: R_thigh. Geometry of a routing surface, not a bone attachment.
    "R_VM_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.010585365852658537,
    },
    # ===== R_TA =====
    # Branch 1, divisor 1.0: R_TA_origin [R_shank] -> R_TA_wrap0 [R_shank] -> R_TA_insert [R_foot]
    # CYLINDER WRAP for R_TA. Connected body: R_shank. Geometry of a routing surface, not a bone attachment.
    "R_TA_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005077400968945839,
    },
    # ===== R_SO =====
    # Branch 1, divisor 1.0: R_SO_origin [R_shank] -> R_SO_wrap0 [R_shank] -> R_SO_insert [R_foot]
    # CYLINDER WRAP for R_SO. Connected body: R_shank. Geometry of a routing surface, not a bone attachment.
    "R_SO_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005077400968945839,
    },
    # ===== R_RF =====
    # Branch 1, divisor 1.0: R_RF_origin [R_pelvis_anchor] -> R_RF_wrap0 [R_pelvis_anchor] -> R_RF_tangent [R_thigh] -> R_RF_wrap1 [R_thigh] -> R_RF_insert [R_shank]
    # CYLINDER WRAP for R_RF. Connected body: R_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "R_RF_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004763827801212448,
    },
    # CYLINDER WRAP for R_RF. Connected body: R_thigh. Geometry of a routing surface, not a bone attachment.
    "R_RF_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.010585365852658537,
    },
    # ===== R_BFP =====
    # Branch 1, divisor 1.0: R_BFP_origin [R_pelvis_anchor] -> R_BFP_wrap0 [R_pelvis_anchor] -> R_BFP_tangent [R_thigh] -> R_BFP_wrap1 [R_thigh] -> R_BFP_insert [R_shank]
    # CYLINDER WRAP for R_BFP. Connected body: R_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "R_BFP_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004763827801212448,
    },
    # CYLINDER WRAP for R_BFP. Connected body: R_thigh. Geometry of a routing surface, not a bone attachment.
    "R_BFP_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005716593361654938,
    },
    # ===== R_SAM =====
    # Branch 1, divisor 1.0: R_SAM_origin [R_pelvis_anchor] -> R_SAM_wrap0 [R_pelvis_anchor] -> R_SAM_tangent [R_thigh] -> R_SAM_wrap1 [R_thigh] -> R_SAM_insert [R_shank]
    # CYLINDER WRAP for R_SAM. Connected body: R_pelvis_anchor. Geometry of a routing surface, not a bone attachment.
    "R_SAM_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004763827801212448,
    },
    # CYLINDER WRAP for R_SAM. Connected body: R_thigh. Geometry of a routing surface, not a bone attachment.
    "R_SAM_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005716593361654938,
    },
    # ===== R_LG =====
    # Branch 1, divisor 1.0: R_LG_origin [R_thigh] -> R_LG_wrap0 [R_thigh] -> R_LG_tangent [R_shank] -> R_LG_wrap1 [R_shank] -> R_LG_insert [R_foot]
    # CYLINDER WRAP for R_LG. Connected body: R_thigh. Geometry of a routing surface, not a bone attachment.
    "R_LG_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005889003082247688,
    },
    # CYLINDER WRAP for R_LG. Connected body: R_shank. Geometry of a routing surface, not a bone attachment.
    "R_LG_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004884810790217741,
    },
    # ===== R_MG =====
    # Branch 1, divisor 1.0: R_MG_origin [R_thigh] -> R_MG_wrap0 [R_thigh] -> R_MG_tangent [R_shank] -> R_MG_wrap1 [R_shank] -> R_MG_insert [R_foot]
    # CYLINDER WRAP for R_MG. Connected body: R_thigh. Geometry of a routing surface, not a bone attachment.
    "R_MG_wrap0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005889003082247688,
    },
    # CYLINDER WRAP for R_MG. Connected body: R_shank. Geometry of a routing surface, not a bone attachment.
    "R_MG_wrap1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004884810790217741,
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
    # CYLINDER WRAP for FL_ShoulderExtensor. Connected body: FL_scapula. Geometry of a routing surface, not a bone attachment.
    "FL_ShoulderExtensor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.05771428571428572, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00794485115887297,
    },
    # ===== FL_ElbowExtensor =====
    # Branch 1, divisor 1.0: FL_ElbowExtensor_s0_origin [FL_upperarm] -> FL_ElbowExtensor_s0_pulley0 [FL_upperarm] -> FL_ElbowExtensor_s0_insert [FL_forearm]
    # CYLINDER WRAP for FL_ElbowExtensor. Connected body: FL_upperarm. Geometry of a routing surface, not a bone attachment.
    "FL_ElbowExtensor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00211767658146807,
    },
    # ===== FL_BicepsBrachii =====
    # Branch 1, divisor 1.0: FL_BicepsBrachii_s0_origin [FL_scapula] -> FL_BicepsBrachii_s0_pulley0 [FL_scapula] -> FL_BicepsBrachii_s0_tangent [FL_upperarm] -> FL_BicepsBrachii_s0_pulley1 [FL_upperarm] -> FL_BicepsBrachii_s0_insert [FL_forearm]
    # CYLINDER WRAP for FL_BicepsBrachii. Connected body: FL_scapula. Geometry of a routing surface, not a bone attachment.
    "FL_BicepsBrachii_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.05771428571428572, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.009946928603793972,
    },
    # CYLINDER WRAP for FL_BicepsBrachii. Connected body: FL_upperarm. Geometry of a routing surface, not a bone attachment.
    "FL_BicepsBrachii_s0_pulley1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005259145388888544,
    },
    # ===== FL_ElbowFlexor =====
    # Branch 1, divisor 1.0: FL_ElbowFlexor_s0_origin [FL_upperarm] -> FL_ElbowFlexor_s0_pulley0 [FL_upperarm] -> FL_ElbowFlexor_s0_insert [FL_forearm]
    # CYLINDER WRAP for FL_ElbowFlexor. Connected body: FL_upperarm. Geometry of a routing surface, not a bone attachment.
    "FL_ElbowFlexor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00319999999900039,
    },
    # ===== FL_ElbowFlexorWristFlexor =====
    # Branch 1, divisor 1.0: FL_ElbowFlexorWristFlexor_s0_origin [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_pulley0 [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_insert [FL_forearm]
    # CYLINDER WRAP for FL_ElbowFlexorWristFlexor. Connected body: FL_upperarm. Geometry of a routing surface, not a bone attachment.
    "FL_ElbowFlexorWristFlexor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00536465406511287,
    },
    # Branch 2, divisor 1.0: FL_ElbowFlexorWristFlexor_s1_origin [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_pulley0 [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_insert [FL_carpals]
    # CYLINDER WRAP for FL_ElbowFlexorWristFlexor. Connected body: FL_forearm. Geometry of a routing surface, not a bone attachment.
    "FL_ElbowFlexorWristFlexor_s1_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09465714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00350749590090618,
    },
    # ===== FL_WristFlexor =====
    # Branch 1, divisor 1.0: FL_WristFlexor_s0_origin [FL_forearm] -> FL_WristFlexor_s0_insert [FL_forearm]
    # Branch 2, divisor 1.0: FL_WristFlexor_s1_origin [FL_forearm] -> FL_WristFlexor_s1_pulley0 [FL_forearm] -> FL_WristFlexor_s1_insert [FL_carpals]
    # CYLINDER WRAP for FL_WristFlexor. Connected body: FL_forearm. Geometry of a routing surface, not a bone attachment.
    "FL_WristFlexor_s1_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09465714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.002399999999,
    },
    # ===== FL_WristExtensor =====
    # Branch 1, divisor 1.0: FL_WristExtensor_s0_origin [FL_forearm] -> FL_WristExtensor_s0_insert [FL_forearm]
    # Branch 2, divisor 1.0: FL_WristExtensor_s1_origin [FL_forearm] -> FL_WristExtensor_s1_pulley0 [FL_forearm] -> FL_WristExtensor_s1_insert [FL_carpals]
    # CYLINDER WRAP for FL_WristExtensor. Connected body: FL_forearm. Geometry of a routing surface, not a bone attachment.
    "FL_WristExtensor_s1_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09465714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00271044296670131,
    },
    # ===== FL_ShoulderFlexor =====
    # Branch 1, divisor 1.0: FL_ShoulderFlexor_s0_origin [FL_scapula] -> FL_ShoulderFlexor_s0_pulley0 [FL_scapula] -> FL_ShoulderFlexor_s0_insert [FL_upperarm]
    # CYLINDER WRAP for FL_ShoulderFlexor. Connected body: FL_scapula. Geometry of a routing surface, not a bone attachment.
    "FL_ShoulderFlexor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.05771428571428572, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00184271114022135,
    },
    # ===== FL_TricepsBrachiiLong =====
    # Branch 1, divisor 1.0: FL_TricepsBrachiiLong_s0_origin [FL_scapula] -> FL_TricepsBrachiiLong_s0_pulley0 [FL_scapula] -> FL_TricepsBrachiiLong_s0_tangent [FL_upperarm] -> FL_TricepsBrachiiLong_s0_pulley1 [FL_upperarm] -> FL_TricepsBrachiiLong_s0_insert [FL_forearm]
    # CYLINDER WRAP for FL_TricepsBrachiiLong. Connected body: FL_scapula. Geometry of a routing surface, not a bone attachment.
    "FL_TricepsBrachiiLong_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.05771428571428572, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004419416011604855,
    },
    # CYLINDER WRAP for FL_TricepsBrachiiLong. Connected body: FL_upperarm. Geometry of a routing surface, not a bone attachment.
    "FL_TricepsBrachiiLong_s0_pulley1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.011883274667532627,
    },
    # ===== FR_ShoulderExtensor =====
    # Branch 1, divisor 1.0: FR_ShoulderExtensor_s0_origin [FR_scapula] -> FR_ShoulderExtensor_s0_pulley0 [FR_scapula] -> FR_ShoulderExtensor_s0_insert [FR_upperarm]
    # CYLINDER WRAP for FR_ShoulderExtensor. Connected body: FR_scapula. Geometry of a routing surface, not a bone attachment.
    "FR_ShoulderExtensor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.05771428571428572, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00794485115887297,
    },
    # ===== FR_ElbowExtensor =====
    # Branch 1, divisor 1.0: FR_ElbowExtensor_s0_origin [FR_upperarm] -> FR_ElbowExtensor_s0_pulley0 [FR_upperarm] -> FR_ElbowExtensor_s0_insert [FR_forearm]
    # CYLINDER WRAP for FR_ElbowExtensor. Connected body: FR_upperarm. Geometry of a routing surface, not a bone attachment.
    "FR_ElbowExtensor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00211767658146807,
    },
    # ===== FR_BicepsBrachii =====
    # Branch 1, divisor 1.0: FR_BicepsBrachii_s0_origin [FR_scapula] -> FR_BicepsBrachii_s0_pulley0 [FR_scapula] -> FR_BicepsBrachii_s0_tangent [FR_upperarm] -> FR_BicepsBrachii_s0_pulley1 [FR_upperarm] -> FR_BicepsBrachii_s0_insert [FR_forearm]
    # CYLINDER WRAP for FR_BicepsBrachii. Connected body: FR_scapula. Geometry of a routing surface, not a bone attachment.
    "FR_BicepsBrachii_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.05771428571428572, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.009946928603793972,
    },
    # CYLINDER WRAP for FR_BicepsBrachii. Connected body: FR_upperarm. Geometry of a routing surface, not a bone attachment.
    "FR_BicepsBrachii_s0_pulley1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.005259145388888544,
    },
    # ===== FR_ElbowFlexor =====
    # Branch 1, divisor 1.0: FR_ElbowFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexor_s0_insert [FR_forearm]
    # CYLINDER WRAP for FR_ElbowFlexor. Connected body: FR_upperarm. Geometry of a routing surface, not a bone attachment.
    "FR_ElbowFlexor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00319999999900039,
    },
    # ===== FR_ElbowFlexorWristFlexor =====
    # Branch 1, divisor 1.0: FR_ElbowFlexorWristFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_insert [FR_forearm]
    # CYLINDER WRAP for FR_ElbowFlexorWristFlexor. Connected body: FR_upperarm. Geometry of a routing surface, not a bone attachment.
    "FR_ElbowFlexorWristFlexor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00536465406511287,
    },
    # Branch 2, divisor 1.0: FR_ElbowFlexorWristFlexor_s1_origin [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_pulley0 [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_insert [FR_carpals]
    # CYLINDER WRAP for FR_ElbowFlexorWristFlexor. Connected body: FR_forearm. Geometry of a routing surface, not a bone attachment.
    "FR_ElbowFlexorWristFlexor_s1_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09465714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00350749590090618,
    },
    # ===== FR_WristFlexor =====
    # Branch 1, divisor 1.0: FR_WristFlexor_s0_origin [FR_forearm] -> FR_WristFlexor_s0_insert [FR_forearm]
    # Branch 2, divisor 1.0: FR_WristFlexor_s1_origin [FR_forearm] -> FR_WristFlexor_s1_pulley0 [FR_forearm] -> FR_WristFlexor_s1_insert [FR_carpals]
    # CYLINDER WRAP for FR_WristFlexor. Connected body: FR_forearm. Geometry of a routing surface, not a bone attachment.
    "FR_WristFlexor_s1_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09465714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.002399999999,
    },
    # ===== FR_WristExtensor =====
    # Branch 1, divisor 1.0: FR_WristExtensor_s0_origin [FR_forearm] -> FR_WristExtensor_s0_insert [FR_forearm]
    # Branch 2, divisor 1.0: FR_WristExtensor_s1_origin [FR_forearm] -> FR_WristExtensor_s1_pulley0 [FR_forearm] -> FR_WristExtensor_s1_insert [FR_carpals]
    # CYLINDER WRAP for FR_WristExtensor. Connected body: FR_forearm. Geometry of a routing surface, not a bone attachment.
    "FR_WristExtensor_s1_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09465714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00271044296670131,
    },
    # ===== FR_ShoulderFlexor =====
    # Branch 1, divisor 1.0: FR_ShoulderFlexor_s0_origin [FR_scapula] -> FR_ShoulderFlexor_s0_pulley0 [FR_scapula] -> FR_ShoulderFlexor_s0_insert [FR_upperarm]
    # CYLINDER WRAP for FR_ShoulderFlexor. Connected body: FR_scapula. Geometry of a routing surface, not a bone attachment.
    "FR_ShoulderFlexor_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.05771428571428572, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.00184271114022135,
    },
    # ===== FR_TricepsBrachiiLong =====
    # Branch 1, divisor 1.0: FR_TricepsBrachiiLong_s0_origin [FR_scapula] -> FR_TricepsBrachiiLong_s0_pulley0 [FR_scapula] -> FR_TricepsBrachiiLong_s0_tangent [FR_upperarm] -> FR_TricepsBrachiiLong_s0_pulley1 [FR_upperarm] -> FR_TricepsBrachiiLong_s0_insert [FR_forearm]
    # CYLINDER WRAP for FR_TricepsBrachiiLong. Connected body: FR_scapula. Geometry of a routing surface, not a bone attachment.
    "FR_TricepsBrachiiLong_s0_pulley0": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.05771428571428572, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.004419416011604855,
    },
    # CYLINDER WRAP for FR_TricepsBrachiiLong. Connected body: FR_upperarm. Geometry of a routing surface, not a bone attachment.
    "FR_TricepsBrachiiLong_s0_pulley1": {
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09275714285714286, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
        # Muscle wrap surface geometry in its owning body frame; not a visual bone or paw contact. Unit: m.
        # Original raw/source: None; None = not independently established.
        "radius_m": 0.011883274667532627,
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
    # Shared entry 'FL_ElbowFlexorWristFlexor_s0_pulley0': already defined above.
    # Branch 2, divisor 1.0: FL_ElbowFlexorWristFlexor_s1_origin [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_pulley0 [FL_forearm] -> FL_DigitalExtensors_attachment0 [FL_carpals] -> FL_DigitalExtensors_attachment1 [FL_digits]
    # Shared entry 'FL_ElbowFlexorWristFlexor_s1_pulley0': already defined above.
    # ===== FR_DigitalExtensors =====
    # Branch 1, divisor 1.0: FR_ElbowFlexorWristFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_insert [FR_forearm]
    # Shared entry 'FR_ElbowFlexorWristFlexor_s0_pulley0': already defined above.
    # Branch 2, divisor 1.0: FR_ElbowFlexorWristFlexor_s1_origin [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_pulley0 [FR_forearm] -> FR_DigitalExtensors_attachment0 [FR_carpals] -> FR_DigitalExtensors_attachment1 [FR_digits]
    # Shared entry 'FR_ElbowFlexorWristFlexor_s1_pulley0': already defined above.
    # ===== FL_DigitalFlexors =====
    # Branch 1, divisor 1.0: FL_WristExtensor_s0_origin [FL_forearm] -> FL_WristExtensor_s0_insert [FL_forearm]
    # Branch 2, divisor 1.0: FL_WristExtensor_s1_origin [FL_forearm] -> FL_WristExtensor_s1_pulley0 [FL_forearm] -> FL_DigitalFlexors_attachment0 [FL_carpals] -> FL_DigitalFlexors_attachment1 [FL_digits]
    # Shared entry 'FL_WristExtensor_s1_pulley0': already defined above.
    # ===== FR_DigitalFlexors =====
    # Branch 1, divisor 1.0: FR_WristExtensor_s0_origin [FR_forearm] -> FR_WristExtensor_s0_insert [FR_forearm]
    # Branch 2, divisor 1.0: FR_WristExtensor_s1_origin [FR_forearm] -> FR_WristExtensor_s1_pulley0 [FR_forearm] -> FR_DigitalFlexors_attachment0 [FR_carpals] -> FR_DigitalFlexors_attachment1 [FR_digits]
    # Shared entry 'FR_WristExtensor_s1_pulley0': already defined above.
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
