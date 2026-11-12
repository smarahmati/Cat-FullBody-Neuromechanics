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
    # ORIGIN for L_IP. Connected body: L_pelvis_anchor.
    "L_IP_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0465, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_IP. Connected body: L_thigh.
    "L_IP_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.012366906474820145, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_BFA =====
    # Branch 1, divisor 1.0: L_BFA_origin [L_pelvis_anchor] -> L_BFA_wrap0 [L_pelvis_anchor] -> L_BFA_insert [L_thigh]
    # ORIGIN for L_BFA. Connected body: L_pelvis_anchor.
    "L_BFA_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.006582361197662642, 0.005330337267324761, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_BFA. Connected body: L_thigh.
    "L_BFA_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.049075025693730734, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_VL =====
    # Branch 1, divisor 1.0: L_VL_origin [L_thigh] -> L_VL_wrap0 [L_thigh] -> L_VL_insert [L_shank]
    # ORIGIN for L_VL. Connected body: L_thigh.
    "L_VL_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 1.1695376931857223e-17, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_VL. Connected body: L_shank.
    "L_VL_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.008671039771033588, 0.006071494012593104, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_VM =====
    # Branch 1, divisor 1.0: L_VM_origin [L_thigh] -> L_VM_wrap0 [L_thigh] -> L_VM_insert [L_shank]
    # ORIGIN for L_VM. Connected body: L_thigh.
    "L_VM_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 1.1695376931857223e-17, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_VM. Connected body: L_shank.
    "L_VM_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.008671039771033588, 0.006071494012593104, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_TA =====
    # Branch 1, divisor 1.0: L_TA_origin [L_shank] -> L_TA_wrap0 [L_shank] -> L_TA_insert [L_foot]
    # ORIGIN for L_TA. Connected body: L_shank.
    "L_TA_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0926219512195122, 1.9445001615729926e-18, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_TA. Connected body: L_foot.
    "L_TA_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.014586357039187228, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_SO =====
    # Branch 1, divisor 1.0: L_SO_origin [L_shank] -> L_SO_wrap0 [L_shank] -> L_SO_insert [L_foot]
    # ORIGIN for L_SO. Connected body: L_shank.
    "L_SO_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0037048780487804744, 1.2833701066381752e-17, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_SO. Connected body: L_foot.
    "L_SO_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.015473543498456494, -0.0016263803013220528, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_RF =====
    # Branch 1, divisor 1.0: L_RF_origin [L_pelvis_anchor] -> L_RF_wrap0 [L_pelvis_anchor] -> L_RF_tangent [L_thigh] -> L_RF_wrap1 [L_thigh] -> L_RF_insert [L_shank]
    # ORIGIN for L_RF. Connected body: L_pelvis_anchor.
    "L_RF_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.005420765027322405, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_RF. Connected body: L_shank.
    "L_RF_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.008671039771033588, 0.006071494012593104, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_BFP =====
    # Branch 1, divisor 1.0: L_BFP_origin [L_pelvis_anchor] -> L_BFP_wrap0 [L_pelvis_anchor] -> L_BFP_tangent [L_thigh] -> L_BFP_wrap1 [L_thigh] -> L_BFP_insert [L_shank]
    # ORIGIN for L_BFP. Connected body: L_pelvis_anchor.
    "L_BFP_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.006582361197662642, 0.005330337267324761, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_BFP. Connected body: L_shank.
    "L_BFP_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03175609756097561, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_SAM =====
    # Branch 1, divisor 1.0: L_SAM_origin [L_pelvis_anchor] -> L_SAM_wrap0 [L_pelvis_anchor] -> L_SAM_tangent [L_thigh] -> L_SAM_wrap1 [L_thigh] -> L_SAM_insert [L_shank]
    # ORIGIN for L_SAM. Connected body: L_pelvis_anchor.
    "L_SAM_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.013551912568306013, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_SAM. Connected body: L_shank.
    "L_SAM_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.010585365853658537, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_LG =====
    # Branch 1, divisor 1.0: L_LG_origin [L_thigh] -> L_LG_wrap0 [L_thigh] -> L_LG_tangent [L_shank] -> L_LG_wrap1 [L_shank] -> L_LG_insert [L_foot]
    # ORIGIN for L_LG. Connected body: L_thigh.
    "L_LG_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.08961099691675231, 7.211948776068176e-19, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_LG. Connected body: L_foot.
    "L_LG_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.015473543498456494, -0.0016263803013220528, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_MG =====
    # Branch 1, divisor 1.0: L_MG_origin [L_thigh] -> L_MG_wrap0 [L_thigh] -> L_MG_tangent [L_shank] -> L_MG_wrap1 [L_shank] -> L_MG_insert [L_foot]
    # ORIGIN for L_MG. Connected body: L_thigh.
    "L_MG_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.08961099691675231, 7.211948776068176e-19, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_MG. Connected body: L_foot.
    "L_MG_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.015473543498456494, -0.0016263803013220528, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_IP =====
    # Branch 1, divisor 1.0: R_IP_origin [R_pelvis_anchor] -> R_IP_wrap0 [R_pelvis_anchor] -> R_IP_insert [R_thigh]
    # ORIGIN for R_IP. Connected body: R_pelvis_anchor.
    "R_IP_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0465, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_IP. Connected body: R_thigh.
    "R_IP_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.012366906474820145, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_BFA =====
    # Branch 1, divisor 1.0: R_BFA_origin [R_pelvis_anchor] -> R_BFA_wrap0 [R_pelvis_anchor] -> R_BFA_insert [R_thigh]
    # ORIGIN for R_BFA. Connected body: R_pelvis_anchor.
    "R_BFA_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.006582361197662642, 0.005330337267324761, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_BFA. Connected body: R_thigh.
    "R_BFA_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.049075025693730734, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_VL =====
    # Branch 1, divisor 1.0: R_VL_origin [R_thigh] -> R_VL_wrap0 [R_thigh] -> R_VL_insert [R_shank]
    # ORIGIN for R_VL. Connected body: R_thigh.
    "R_VL_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 1.1695376931857223e-17, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_VL. Connected body: R_shank.
    "R_VL_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.008671039771033588, 0.006071494012593104, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_VM =====
    # Branch 1, divisor 1.0: R_VM_origin [R_thigh] -> R_VM_wrap0 [R_thigh] -> R_VM_insert [R_shank]
    # ORIGIN for R_VM. Connected body: R_thigh.
    "R_VM_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 1.1695376931857223e-17, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_VM. Connected body: R_shank.
    "R_VM_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.008671039771033588, 0.006071494012593104, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_TA =====
    # Branch 1, divisor 1.0: R_TA_origin [R_shank] -> R_TA_wrap0 [R_shank] -> R_TA_insert [R_foot]
    # ORIGIN for R_TA. Connected body: R_shank.
    "R_TA_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0926219512195122, 1.9445001615729926e-18, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_TA. Connected body: R_foot.
    "R_TA_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.014586357039187228, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_SO =====
    # Branch 1, divisor 1.0: R_SO_origin [R_shank] -> R_SO_wrap0 [R_shank] -> R_SO_insert [R_foot]
    # ORIGIN for R_SO. Connected body: R_shank.
    "R_SO_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0037048780487804744, 1.2833701066381752e-17, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_SO. Connected body: R_foot.
    "R_SO_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.015473543498456494, -0.0016263803013220528, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_RF =====
    # Branch 1, divisor 1.0: R_RF_origin [R_pelvis_anchor] -> R_RF_wrap0 [R_pelvis_anchor] -> R_RF_tangent [R_thigh] -> R_RF_wrap1 [R_thigh] -> R_RF_insert [R_shank]
    # ORIGIN for R_RF. Connected body: R_pelvis_anchor.
    "R_RF_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.005420765027322405, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_RF. Connected body: R_shank.
    "R_RF_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.008671039771033588, 0.006071494012593104, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_BFP =====
    # Branch 1, divisor 1.0: R_BFP_origin [R_pelvis_anchor] -> R_BFP_wrap0 [R_pelvis_anchor] -> R_BFP_tangent [R_thigh] -> R_BFP_wrap1 [R_thigh] -> R_BFP_insert [R_shank]
    # ORIGIN for R_BFP. Connected body: R_pelvis_anchor.
    "R_BFP_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.006582361197662642, 0.005330337267324761, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_BFP. Connected body: R_shank.
    "R_BFP_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03175609756097561, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_SAM =====
    # Branch 1, divisor 1.0: R_SAM_origin [R_pelvis_anchor] -> R_SAM_wrap0 [R_pelvis_anchor] -> R_SAM_tangent [R_thigh] -> R_SAM_wrap1 [R_thigh] -> R_SAM_insert [R_shank]
    # ORIGIN for R_SAM. Connected body: R_pelvis_anchor.
    "R_SAM_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.013551912568306013, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_SAM. Connected body: R_shank.
    "R_SAM_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.010585365853658537, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_LG =====
    # Branch 1, divisor 1.0: R_LG_origin [R_thigh] -> R_LG_wrap0 [R_thigh] -> R_LG_tangent [R_shank] -> R_LG_wrap1 [R_shank] -> R_LG_insert [R_foot]
    # ORIGIN for R_LG. Connected body: R_thigh.
    "R_LG_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.08961099691675231, 7.211948776068176e-19, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_LG. Connected body: R_foot.
    "R_LG_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.015473543498456494, -0.0016263803013220528, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_MG =====
    # Branch 1, divisor 1.0: R_MG_origin [R_thigh] -> R_MG_wrap0 [R_thigh] -> R_MG_tangent [R_shank] -> R_MG_wrap1 [R_shank] -> R_MG_insert [R_foot]
    # ORIGIN for R_MG. Connected body: R_thigh.
    "R_MG_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.08961099691675231, 7.211948776068176e-19, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_MG. Connected body: R_foot.
    "R_MG_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.015473543498456494, -0.0016263803013220528, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_EDL =====
    # Branch 1, divisor 1.0: L_EDL_osim_0 [L_shank] -> L_EDL_osim_1 [L_shank] -> L_EDL_osim_2 [L_foot] -> L_EDL_osim_3 [L_foot] -> L_EDL_osim_4 [L_foot] -> L_EDL_osim_5 [L_foot] -> L_EDL_osim_6 [L_digits]
    # ORIGIN for L_EDL. Connected body: L_shank.
    "L_EDL_osim_0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.007115781224220425.
            0.007115781224220425,
            # Run 0.00946437036584518.
            0.00946437036584518,
            # Run -0.004137299386552081.
            -0.004137299386552081,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_EDL. Connected body: L_shank.
    "L_EDL_osim_1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.015395149315294506.
            0.015395149315294506,
            # Run 0.012786301686307396.
            0.012786301686307396,
            # Run -0.004362979134113302.
            -0.004362979134113302,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_EDL. Connected body: L_foot.
    "L_EDL_osim_2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.01331995221027479.
            0.01331995221027479,
            # Run -0.00016017214357696066.
            -0.00016017214357696066,
            # Run -0.0016603620779240757.
            -0.0016603620779240757,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_EDL. Connected body: L_foot.
    "L_EDL_osim_3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.02643178016726403.
            0.02643178016726403,
            # Run 0.0011372222193964286.
            0.0011372222193964286,
            # Run -0.0012548039085772762.
            -0.0012548039085772762,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_EDL. Connected body: L_foot.
    "L_EDL_osim_4": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.04063225806451612.
            0.04063225806451612,
            # Run 0.0069514710312401345.
            0.0069514710312401345,
            # Run -0.002887930700403582.
            -0.002887930700403582,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_EDL. Connected body: L_foot.
    "L_EDL_osim_5": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.06258136200716845.
            0.06258136200716845,
            # Run 0.009113794969529111.
            0.009113794969529111,
            # Run -0.005317565813834683.
            -0.005317565813834683,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_EDL. Connected body: L_digits.
    "L_EDL_osim_6": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.008725689404934686.
            0.008725689404934686,
            # Run 0.004232220609579099.
            0.004232220609579099,
            # Run -0.009600435403769187.
            -0.009600435403769187,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_EDL =====
    # Branch 1, divisor 1.0: R_EDL_osim_0 [R_shank] -> R_EDL_osim_1 [R_shank] -> R_EDL_osim_2 [R_foot] -> R_EDL_osim_3 [R_foot] -> R_EDL_osim_4 [R_foot] -> R_EDL_osim_5 [R_foot] -> R_EDL_osim_6 [R_digits]
    # ORIGIN for R_EDL. Connected body: R_shank.
    "R_EDL_osim_0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.007115781224220425.
            0.007115781224220425,
            # Run 0.00946437036584518.
            0.00946437036584518,
            # Run 0.004137299386552081.
            0.004137299386552081,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_EDL. Connected body: R_shank.
    "R_EDL_osim_1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.015395149315294506.
            0.015395149315294506,
            # Run 0.012786301686307396.
            0.012786301686307396,
            # Run 0.004362979134113302.
            0.004362979134113302,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_EDL. Connected body: R_foot.
    "R_EDL_osim_2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.01331995221027479.
            0.01331995221027479,
            # Run -0.00016017214357696066.
            -0.00016017214357696066,
            # Run 0.0016603620779240757.
            0.0016603620779240757,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_EDL. Connected body: R_foot.
    "R_EDL_osim_3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.02643178016726403.
            0.02643178016726403,
            # Run 0.0011372222193964286.
            0.0011372222193964286,
            # Run 0.0012548039085772762.
            0.0012548039085772762,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_EDL. Connected body: R_foot.
    "R_EDL_osim_4": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.04063225806451612.
            0.04063225806451612,
            # Run 0.0069514710312401345.
            0.0069514710312401345,
            # Run 0.002887930700403582.
            0.002887930700403582,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_EDL. Connected body: R_foot.
    "R_EDL_osim_5": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.06258136200716845.
            0.06258136200716845,
            # Run 0.009113794969529111.
            0.009113794969529111,
            # Run 0.005317565813834683.
            0.005317565813834683,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_EDL. Connected body: R_digits.
    "R_EDL_osim_6": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.008725689404934686.
            0.008725689404934686,
            # Run 0.004232220609579099.
            0.004232220609579099,
            # Run 0.009600435403769187.
            0.009600435403769187,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_FDL =====
    # Branch 1, divisor 1.0: L_FDL_osim_0 [L_shank] -> L_FDL_osim_1 [L_shank] -> L_FDL_osim_2 [L_foot] -> L_FDL_osim_3 [L_foot] -> L_FDL_osim_4 [L_digits]
    # ORIGIN for L_FDL. Connected body: L_shank.
    "L_FDL_osim_0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.03338599241049331.
            0.03338599241049331,
            # Run 7.163194222020615e-05.
            7.163194222020615e-05,
            # Run -0.0048533751261112005.
            -0.0048533751261112005,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_FDL. Connected body: L_shank.
    "L_FDL_osim_1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.10562683550569212.
            0.10562683550569212,
            # Run -0.0013968228732940935.
            -0.0013968228732940935,
            # Run -0.009780025009899034.
            -0.009780025009899034,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_FDL. Connected body: L_foot.
    "L_FDL_osim_2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.012183273596176821.
            0.012183273596176821,
            # Run -0.008393020323432785.
            -0.008393020323432785,
            # Run -0.009984951070462588.
            -0.009984951070462588,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_FDL. Connected body: L_foot.
    "L_FDL_osim_3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.026896057347670248.
            0.026896057347670248,
            # Run -0.008409037537790478.
            -0.008409037537790478,
            # Run -0.009529874199119843.
            -0.009529874199119843,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_FDL. Connected body: L_digits.
    "L_FDL_osim_4": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0030827285921625532.
            -0.0030827285921625532,
            # Run -0.0038664731494920165.
            -0.0038664731494920165,
            # Run -0.013714907719670266.
            -0.013714907719670266,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_FDL =====
    # Branch 1, divisor 1.0: R_FDL_osim_0 [R_shank] -> R_FDL_osim_1 [R_shank] -> R_FDL_osim_2 [R_foot] -> R_FDL_osim_3 [R_foot] -> R_FDL_osim_4 [R_digits]
    # ORIGIN for R_FDL. Connected body: R_shank.
    "R_FDL_osim_0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.03338599241049331.
            0.03338599241049331,
            # Run 7.163194222020615e-05.
            7.163194222020615e-05,
            # Run 0.0048533751261112005.
            0.0048533751261112005,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_FDL. Connected body: R_shank.
    "R_FDL_osim_1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.10562683550569212.
            0.10562683550569212,
            # Run -0.0013968228732940935.
            -0.0013968228732940935,
            # Run 0.009780025009899034.
            0.009780025009899034,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_FDL. Connected body: R_foot.
    "R_FDL_osim_2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.012183273596176821.
            0.012183273596176821,
            # Run -0.008393020323432785.
            -0.008393020323432785,
            # Run 0.009984951070462588.
            0.009984951070462588,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_FDL. Connected body: R_foot.
    "R_FDL_osim_3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.026896057347670248.
            0.026896057347670248,
            # Run -0.008409037537790478.
            -0.008409037537790478,
            # Run 0.009529874199119843.
            0.009529874199119843,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_FDL. Connected body: R_digits.
    "R_FDL_osim_4": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0030827285921625532.
            -0.0030827285921625532,
            # Run -0.0038664731494920165.
            -0.0038664731494920165,
            # Run 0.013714907719670266.
            0.013714907719670266,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== L_FHL =====
    # Branch 1, divisor 1.0: L_FHL_attachment0 [L_shank] -> L_FHL_attachment1 [L_shank] -> L_FHL_attachment2 [L_foot] -> L_FHL_attachment3 [L_foot] -> L_FHL_attachment4 [L_digits]
    # ORIGIN for L_FHL. Connected body: L_shank.
    "L_FHL_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.03343969641973272.
            0.03343969641973272,
            # Run 7.163194222020616e-05.
            7.163194222020616e-05,
            # Run -0.0028831705983929467.
            -0.0028831705983929467,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_FHL. Connected body: L_shank.
    "L_FHL_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.10655770499917504.
            0.10655770499917504,
            # Run -0.0031338974721341725.
            -0.0031338974721341725,
            # Run -0.00980539873286808.
            -0.00980539873286808,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_FHL. Connected body: L_foot.
    "L_FHL_attachment2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.011526881720430107.
            0.011526881720430107,
            # Run -0.009193881041317593.
            -0.009193881041317593,
            # Run -0.010005253738280926.
            -0.010005253738280926,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for L_FHL. Connected body: L_foot.
    "L_FHL_attachment3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.028464994026284343.
            0.028464994026284343,
            # Run -0.009722449115121563.
            -0.009722449115121563,
            # Run -0.00844516703189864.
            -0.00844516703189864,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for L_FHL. Connected body: L_digits.
    "L_FHL_attachment4": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0030827285921625532.
            -0.0030827285921625532,
            # Run -0.0038664731494920165.
            -0.0038664731494920165,
            # Run -0.0027429815439340534.
            -0.0027429815439340534,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== R_FHL =====
    # Branch 1, divisor 1.0: R_FHL_attachment0 [R_shank] -> R_FHL_attachment1 [R_shank] -> R_FHL_attachment2 [R_foot] -> R_FHL_attachment3 [R_foot] -> R_FHL_attachment4 [R_digits]
    # ORIGIN for R_FHL. Connected body: R_shank.
    "R_FHL_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.03343969641973272.
            0.03343969641973272,
            # Run 7.163194222020616e-05.
            7.163194222020616e-05,
            # Run 0.0028831705983929467.
            0.0028831705983929467,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_FHL. Connected body: R_shank.
    "R_FHL_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.10655770499917504.
            0.10655770499917504,
            # Run -0.0031338974721341725.
            -0.0031338974721341725,
            # Run 0.00980539873286808.
            0.00980539873286808,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_FHL. Connected body: R_foot.
    "R_FHL_attachment2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.011526881720430107.
            0.011526881720430107,
            # Run -0.009193881041317593.
            -0.009193881041317593,
            # Run 0.010005253738280926.
            0.010005253738280926,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # VIA POINT for R_FHL. Connected body: R_foot.
    "R_FHL_attachment3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.028464994026284343.
            0.028464994026284343,
            # Run -0.009722449115121563.
            -0.009722449115121563,
            # Run 0.00844516703189864.
            0.00844516703189864,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for R_FHL. Connected body: R_digits.
    "R_FHL_attachment4": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0030827285921625532.
            -0.0030827285921625532,
            # Run -0.0038664731494920165.
            -0.0038664731494920165,
            # Run 0.0027429815439340534.
            0.0027429815439340534,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_ShoulderExtensor =====
    # Branch 1, divisor 1.0: FL_ShoulderExtensor_s0_origin [FL_scapula] -> FL_ShoulderExtensor_s0_pulley0 [FL_scapula] -> FL_ShoulderExtensor_s0_insert [FL_upperarm]
    # ORIGIN for FL_ShoulderExtensor. Connected body: FL_scapula.
    "FL_ShoulderExtensor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0034642043621170918, 0.015424375976162651, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_ShoulderExtensor. Connected body: FL_upperarm.
    "FL_ShoulderExtensor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.005813670326445113, 0.0054158953170269945, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_ElbowExtensor =====
    # Branch 1, divisor 1.0: FL_ElbowExtensor_s0_origin [FL_upperarm] -> FL_ElbowExtensor_s0_pulley0 [FL_upperarm] -> FL_ElbowExtensor_s0_insert [FL_forearm]
    # ORIGIN for FL_ElbowExtensor. Connected body: FL_upperarm.
    "FL_ElbowExtensor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03347737572796786, -0.009279374804372012, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_ElbowExtensor. Connected body: FL_forearm.
    "FL_ElbowExtensor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.005023971663288653, -0.0024286591330201198, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_BicepsBrachii =====
    # Branch 1, divisor 1.0: FL_BicepsBrachii_s0_origin [FL_scapula] -> FL_BicepsBrachii_s0_pulley0 [FL_scapula] -> FL_BicepsBrachii_s0_tangent [FL_upperarm] -> FL_BicepsBrachii_s0_pulley1 [FL_upperarm] -> FL_BicepsBrachii_s0_insert [FL_forearm]
    # ORIGIN for FL_BicepsBrachii. Connected body: FL_scapula.
    "FL_BicepsBrachii_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.06243595326053015, 0.01123498044593019, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_BicepsBrachii. Connected body: FL_forearm.
    "FL_BicepsBrachii_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.010255675241405497, -0.004336634578383328, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_ElbowFlexor =====
    # Branch 1, divisor 1.0: FL_ElbowFlexor_s0_origin [FL_upperarm] -> FL_ElbowFlexor_s0_pulley0 [FL_upperarm] -> FL_ElbowFlexor_s0_insert [FL_forearm]
    # ORIGIN for FL_ElbowFlexor. Connected body: FL_upperarm.
    "FL_ElbowFlexor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.021427190335922205, 0.004982393596393559, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_ElbowFlexor. Connected body: FL_forearm.
    "FL_ElbowFlexor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.004607550668827849, 0.0057911120794285845, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_ElbowFlexorWristFlexor =====
    # Branch 1, divisor 1.0: FL_ElbowFlexorWristFlexor_s0_origin [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_pulley0 [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_insert [FL_forearm]
    # ORIGIN for FL_ElbowFlexorWristFlexor. Connected body: FL_upperarm.
    "FL_ElbowFlexorWristFlexor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.08182242269299914, -0.0032236508291720372, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INTERNAL BRANCH END for FL_ElbowFlexorWristFlexor. Connected body: FL_forearm.
    "FL_ElbowFlexorWristFlexor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09490224546194542, 0.006129750944256109, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Branch 2, divisor 1.0: FL_ElbowFlexorWristFlexor_s1_origin [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_pulley0 [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_insert [FL_carpals]
    # INTERNAL BRANCH START for FL_ElbowFlexorWristFlexor. Connected body: FL_forearm.
    "FL_ElbowFlexorWristFlexor_s1_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09441204025234055, 0.006129750944256109, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_ElbowFlexorWristFlexor. Connected body: FL_carpals.
    "FL_ElbowFlexorWristFlexor_s1_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03303668349099529, 0.004179360662887023, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_WristFlexor =====
    # Branch 1, divisor 1.0: FL_WristFlexor_s0_origin [FL_forearm] -> FL_WristFlexor_s0_insert [FL_forearm]
    # ORIGIN for FL_WristFlexor. Connected body: FL_forearm.
    "FL_WristFlexor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.009341816153249752, -0.005995037194119982, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INTERNAL BRANCH END for FL_WristFlexor. Connected body: FL_forearm.
    "FL_WristFlexor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09880435723966653, 0.004348446901636839, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Branch 2, divisor 1.0: FL_WristFlexor_s1_origin [FL_forearm] -> FL_WristFlexor_s1_pulley0 [FL_forearm] -> FL_WristFlexor_s1_insert [FL_carpals]
    # INTERNAL BRANCH START for FL_WristFlexor. Connected body: FL_forearm.
    "FL_WristFlexor_s1_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09880435723966685, 0.00434844690163684, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_WristFlexor. Connected body: FL_carpals.
    "FL_WristFlexor_s1_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.016998910517186643, 0.0019601027857303775, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_WristExtensor =====
    # Branch 1, divisor 1.0: FL_WristExtensor_s0_origin [FL_forearm] -> FL_WristExtensor_s0_insert [FL_forearm]
    # ORIGIN for FL_WristExtensor. Connected body: FL_forearm.
    "FL_WristExtensor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.006369213062286766, -0.00029685234663381487, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INTERNAL BRANCH END for FL_WristExtensor. Connected body: FL_forearm.
    "FL_WristExtensor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09613280631579318, -0.004972172450585192, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Branch 2, divisor 1.0: FL_WristExtensor_s1_origin [FL_forearm] -> FL_WristExtensor_s1_pulley0 [FL_forearm] -> FL_WristExtensor_s1_insert [FL_carpals]
    # INTERNAL BRANCH START for FL_WristExtensor. Connected body: FL_forearm.
    "FL_WristExtensor_s1_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0931814793984905, -0.004972172450585193, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_WristExtensor. Connected body: FL_carpals.
    "FL_WristExtensor_s1_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.02847542892267019, -0.004688183291220659, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_ShoulderFlexor =====
    # Branch 1, divisor 1.0: FL_ShoulderFlexor_s0_origin [FL_scapula] -> FL_ShoulderFlexor_s0_pulley0 [FL_scapula] -> FL_ShoulderFlexor_s0_insert [FL_upperarm]
    # ORIGIN for FL_ShoulderFlexor. Connected body: FL_scapula.
    "FL_ShoulderFlexor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.007368130527692307, -0.006476028207096081, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_ShoulderFlexor. Connected body: FL_upperarm.
    "FL_ShoulderFlexor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.013834023626670015, 0.00935472052307382, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_TricepsBrachiiLong =====
    # Branch 1, divisor 1.0: FL_TricepsBrachiiLong_s0_origin [FL_scapula] -> FL_TricepsBrachiiLong_s0_pulley0 [FL_scapula] -> FL_TricepsBrachiiLong_s0_tangent [FL_upperarm] -> FL_TricepsBrachiiLong_s0_pulley1 [FL_upperarm] -> FL_TricepsBrachiiLong_s0_insert [FL_forearm]
    # ORIGIN for FL_TricepsBrachiiLong. Connected body: FL_scapula.
    "FL_TricepsBrachiiLong_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.047488676157244, 0.0004729577802118338, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_TricepsBrachiiLong. Connected body: FL_forearm.
    "FL_TricepsBrachiiLong_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.014150059601265615, -0.004518838579248152, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_ShoulderExtensor =====
    # Branch 1, divisor 1.0: FR_ShoulderExtensor_s0_origin [FR_scapula] -> FR_ShoulderExtensor_s0_pulley0 [FR_scapula] -> FR_ShoulderExtensor_s0_insert [FR_upperarm]
    # ORIGIN for FR_ShoulderExtensor. Connected body: FR_scapula.
    "FR_ShoulderExtensor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0034642043621170918, 0.015424375976162651, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_ShoulderExtensor. Connected body: FR_upperarm.
    "FR_ShoulderExtensor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.005813670326445113, 0.0054158953170269945, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_ElbowExtensor =====
    # Branch 1, divisor 1.0: FR_ElbowExtensor_s0_origin [FR_upperarm] -> FR_ElbowExtensor_s0_pulley0 [FR_upperarm] -> FR_ElbowExtensor_s0_insert [FR_forearm]
    # ORIGIN for FR_ElbowExtensor. Connected body: FR_upperarm.
    "FR_ElbowExtensor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03347737572796786, -0.009279374804372012, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_ElbowExtensor. Connected body: FR_forearm.
    "FR_ElbowExtensor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.005023971663288653, -0.0024286591330201198, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_BicepsBrachii =====
    # Branch 1, divisor 1.0: FR_BicepsBrachii_s0_origin [FR_scapula] -> FR_BicepsBrachii_s0_pulley0 [FR_scapula] -> FR_BicepsBrachii_s0_tangent [FR_upperarm] -> FR_BicepsBrachii_s0_pulley1 [FR_upperarm] -> FR_BicepsBrachii_s0_insert [FR_forearm]
    # ORIGIN for FR_BicepsBrachii. Connected body: FR_scapula.
    "FR_BicepsBrachii_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.06243595326053015, 0.01123498044593019, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_BicepsBrachii. Connected body: FR_forearm.
    "FR_BicepsBrachii_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.010255675241405497, -0.004336634578383328, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_ElbowFlexor =====
    # Branch 1, divisor 1.0: FR_ElbowFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexor_s0_insert [FR_forearm]
    # ORIGIN for FR_ElbowFlexor. Connected body: FR_upperarm.
    "FR_ElbowFlexor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.021427190335922205, 0.004982393596393559, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_ElbowFlexor. Connected body: FR_forearm.
    "FR_ElbowFlexor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.004607550668827849, 0.0057911120794285845, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_ElbowFlexorWristFlexor =====
    # Branch 1, divisor 1.0: FR_ElbowFlexorWristFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_insert [FR_forearm]
    # ORIGIN for FR_ElbowFlexorWristFlexor. Connected body: FR_upperarm.
    "FR_ElbowFlexorWristFlexor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.08182242269299914, -0.0032236508291720372, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INTERNAL BRANCH END for FR_ElbowFlexorWristFlexor. Connected body: FR_forearm.
    "FR_ElbowFlexorWristFlexor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09490224546194542, 0.006129750944256109, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Branch 2, divisor 1.0: FR_ElbowFlexorWristFlexor_s1_origin [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_pulley0 [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_insert [FR_carpals]
    # INTERNAL BRANCH START for FR_ElbowFlexorWristFlexor. Connected body: FR_forearm.
    "FR_ElbowFlexorWristFlexor_s1_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09441204025234055, 0.006129750944256109, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_ElbowFlexorWristFlexor. Connected body: FR_carpals.
    "FR_ElbowFlexorWristFlexor_s1_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03303668349099529, 0.004179360662887023, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_WristFlexor =====
    # Branch 1, divisor 1.0: FR_WristFlexor_s0_origin [FR_forearm] -> FR_WristFlexor_s0_insert [FR_forearm]
    # ORIGIN for FR_WristFlexor. Connected body: FR_forearm.
    "FR_WristFlexor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.009341816153249752, -0.005995037194119982, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INTERNAL BRANCH END for FR_WristFlexor. Connected body: FR_forearm.
    "FR_WristFlexor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09880435723966653, 0.004348446901636839, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Branch 2, divisor 1.0: FR_WristFlexor_s1_origin [FR_forearm] -> FR_WristFlexor_s1_pulley0 [FR_forearm] -> FR_WristFlexor_s1_insert [FR_carpals]
    # INTERNAL BRANCH START for FR_WristFlexor. Connected body: FR_forearm.
    "FR_WristFlexor_s1_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09880435723966685, 0.00434844690163684, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_WristFlexor. Connected body: FR_carpals.
    "FR_WristFlexor_s1_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.016998910517186643, 0.0019601027857303775, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_WristExtensor =====
    # Branch 1, divisor 1.0: FR_WristExtensor_s0_origin [FR_forearm] -> FR_WristExtensor_s0_insert [FR_forearm]
    # ORIGIN for FR_WristExtensor. Connected body: FR_forearm.
    "FR_WristExtensor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.006369213062286766, -0.00029685234663381487, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INTERNAL BRANCH END for FR_WristExtensor. Connected body: FR_forearm.
    "FR_WristExtensor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.09613280631579318, -0.004972172450585192, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # Branch 2, divisor 1.0: FR_WristExtensor_s1_origin [FR_forearm] -> FR_WristExtensor_s1_pulley0 [FR_forearm] -> FR_WristExtensor_s1_insert [FR_carpals]
    # INTERNAL BRANCH START for FR_WristExtensor. Connected body: FR_forearm.
    "FR_WristExtensor_s1_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0931814793984905, -0.004972172450585193, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_WristExtensor. Connected body: FR_carpals.
    "FR_WristExtensor_s1_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.02847542892267019, -0.004688183291220659, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_ShoulderFlexor =====
    # Branch 1, divisor 1.0: FR_ShoulderFlexor_s0_origin [FR_scapula] -> FR_ShoulderFlexor_s0_pulley0 [FR_scapula] -> FR_ShoulderFlexor_s0_insert [FR_upperarm]
    # ORIGIN for FR_ShoulderFlexor. Connected body: FR_scapula.
    "FR_ShoulderFlexor_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.007368130527692307, -0.006476028207096081, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_ShoulderFlexor. Connected body: FR_upperarm.
    "FR_ShoulderFlexor_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.013834023626670015, 0.00935472052307382, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_TricepsBrachiiLong =====
    # Branch 1, divisor 1.0: FR_TricepsBrachiiLong_s0_origin [FR_scapula] -> FR_TricepsBrachiiLong_s0_pulley0 [FR_scapula] -> FR_TricepsBrachiiLong_s0_tangent [FR_upperarm] -> FR_TricepsBrachiiLong_s0_pulley1 [FR_upperarm] -> FR_TricepsBrachiiLong_s0_insert [FR_forearm]
    # ORIGIN for FR_TricepsBrachiiLong. Connected body: FR_scapula.
    "FR_TricepsBrachiiLong_s0_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.047488676157244, 0.0004729577802118338, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_TricepsBrachiiLong. Connected body: FR_forearm.
    "FR_TricepsBrachiiLong_s0_insert": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.014150059601265615, -0.004518838579248152, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_C3 =====
    # Branch 1, divisor 1.0: FL_S_C3_attachment0 [FL_scapula] -> FL_S_C3_attachment1 [cat_root]
    # ORIGIN for FL_S_C3. Connected body: FL_scapula.
    "FL_S_C3_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.004795451228317586.
            0.004795451228317586,
            # Run 0.008940083297137217.
            0.008940083297137217,
            # Run 0.00891576258883919.
            0.00891576258883919,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_C3. Connected body: cat_root.
    "FL_S_C3_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2847207381051635.
            0.2847207381051635,
            # Run 0.006759958290251934.
            0.006759958290251934,
            # Run 0.19874225417772787.
            0.19874225417772787,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_C3 =====
    # Branch 1, divisor 1.0: FR_S_C3_attachment0 [FR_scapula] -> FR_S_C3_attachment1 [cat_root]
    # ORIGIN for FR_S_C3. Connected body: FR_scapula.
    "FR_S_C3_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.004795451228317586.
            0.004795451228317586,
            # Run 0.008940083297137217.
            0.008940083297137217,
            # Run -0.00891576258883919.
            -0.00891576258883919,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_C3. Connected body: cat_root.
    "FR_S_C3_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2847207381051635.
            0.2847207381051635,
            # Run -0.006759958290251934.
            -0.006759958290251934,
            # Run 0.19874225417772787.
            0.19874225417772787,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_C4 =====
    # Branch 1, divisor 1.0: FL_S_C4_attachment0 [FL_scapula] -> FL_S_C4_attachment1 [cat_root]
    # ORIGIN for FL_S_C4. Connected body: FL_scapula.
    "FL_S_C4_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.004430780978705402.
            0.004430780978705402,
            # Run 0.006459493101114089.
            0.006459493101114089,
            # Run 0.008070203391403533.
            0.008070203391403533,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_C4. Connected body: cat_root.
    "FL_S_C4_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.27545665548534215.
            0.27545665548534215,
            # Run 0.008685811254932936.
            0.008685811254932936,
            # Run 0.1939673764530556.
            0.1939673764530556,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_C4 =====
    # Branch 1, divisor 1.0: FR_S_C4_attachment0 [FR_scapula] -> FR_S_C4_attachment1 [cat_root]
    # ORIGIN for FR_S_C4. Connected body: FR_scapula.
    "FR_S_C4_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.004430780978705402.
            0.004430780978705402,
            # Run 0.006459493101114089.
            0.006459493101114089,
            # Run -0.008070203391403533.
            -0.008070203391403533,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_C4. Connected body: cat_root.
    "FR_S_C4_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.27545665548534215.
            0.27545665548534215,
            # Run -0.008685811254932936.
            -0.008685811254932936,
            # Run 0.1939673764530556.
            0.1939673764530556,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_C5 =====
    # Branch 1, divisor 1.0: FL_S_C5_attachment0 [FL_scapula] -> FL_S_C5_attachment1 [cat_root]
    # ORIGIN for FL_S_C5. Connected body: FL_scapula.
    "FL_S_C5_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0012534713890847554.
            0.0012534713890847554,
            # Run 0.0013103817769002965.
            0.0013103817769002965,
            # Run 0.007253322123857315.
            0.007253322123857315,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_C5. Connected body: cat_root.
    "FL_S_C5_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2666196940652776.
            0.2666196940652776,
            # Run 0.009954254428764001.
            0.009954254428764001,
            # Run 0.18976545825552768.
            0.18976545825552768,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_C5 =====
    # Branch 1, divisor 1.0: FR_S_C5_attachment0 [FR_scapula] -> FR_S_C5_attachment1 [cat_root]
    # ORIGIN for FR_S_C5. Connected body: FR_scapula.
    "FR_S_C5_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0012534713890847554.
            0.0012534713890847554,
            # Run 0.0013103817769002965.
            0.0013103817769002965,
            # Run -0.007253322123857315.
            -0.007253322123857315,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_C5. Connected body: cat_root.
    "FR_S_C5_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2666196940652776.
            0.2666196940652776,
            # Run -0.009954254428764001.
            -0.009954254428764001,
            # Run 0.18976545825552768.
            0.18976545825552768,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_C6 =====
    # Branch 1, divisor 1.0: FL_S_C6_attachment0 [FL_scapula] -> FL_S_C6_attachment1 [cat_root]
    # ORIGIN for FL_S_C6. Connected body: FL_scapula.
    "FL_S_C6_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.00047624768861937665.
            0.00047624768861937665,
            # Run -0.0030523202735862364.
            -0.0030523202735862364,
            # Run 0.0060980449102903895.
            0.0060980449102903895,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_C6. Connected body: cat_root.
    "FL_S_C6_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.25851201325910744.
            0.25851201325910744,
            # Run 0.009302980858926268.
            0.009302980858926268,
            # Run 0.18611022500003707.
            0.18611022500003707,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_C6 =====
    # Branch 1, divisor 1.0: FR_S_C6_attachment0 [FR_scapula] -> FR_S_C6_attachment1 [cat_root]
    # ORIGIN for FR_S_C6. Connected body: FR_scapula.
    "FR_S_C6_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.00047624768861937665.
            0.00047624768861937665,
            # Run -0.0030523202735862364.
            -0.0030523202735862364,
            # Run -0.0060980449102903895.
            -0.0060980449102903895,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_C6. Connected body: cat_root.
    "FR_S_C6_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.25851201325910744.
            0.25851201325910744,
            # Run -0.009302980858926268.
            -0.009302980858926268,
            # Run 0.18611022500003707.
            0.18611022500003707,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_C7 =====
    # Branch 1, divisor 1.0: FL_S_C7_attachment0 [FL_scapula] -> FL_S_C7_attachment1 [cat_root]
    # ORIGIN for FL_S_C7. Connected body: FL_scapula.
    "FL_S_C7_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 8.232119588210429e-05.
            8.232119588210429e-05,
            # Run -0.006288899528980398.
            -0.006288899528980398,
            # Run 0.005687478138496707.
            0.005687478138496707,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_C7. Connected body: cat_root.
    "FL_S_C7_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2506826114466066.
            0.2506826114466066,
            # Run 0.009253037772594105.
            0.009253037772594105,
            # Run 0.18543644695178288.
            0.18543644695178288,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_C7 =====
    # Branch 1, divisor 1.0: FR_S_C7_attachment0 [FR_scapula] -> FR_S_C7_attachment1 [cat_root]
    # ORIGIN for FR_S_C7. Connected body: FR_scapula.
    "FR_S_C7_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 8.232119588210429e-05.
            8.232119588210429e-05,
            # Run -0.006288899528980398.
            -0.006288899528980398,
            # Run -0.005687478138496707.
            -0.005687478138496707,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_C7. Connected body: cat_root.
    "FR_S_C7_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2506826114466066.
            0.2506826114466066,
            # Run -0.009253037772594105.
            -0.009253037772594105,
            # Run 0.18543644695178288.
            0.18543644695178288,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T1 =====
    # Branch 1, divisor 1.0: FL_S_T1_attachment0 [FL_scapula] -> FL_S_T1_attachment1 [cat_root]
    # ORIGIN for FL_S_T1. Connected body: FL_scapula.
    "FL_S_T1_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0016490221999717954.
            0.0016490221999717954,
            # Run -0.007589861855873643.
            -0.007589861855873643,
            # Run 0.004588559449176619.
            0.004588559449176619,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T1. Connected body: cat_root.
    "FL_S_T1_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2341128215559215.
            0.2341128215559215,
            # Run 0.010799375055515469.
            0.010799375055515469,
            # Run 0.17395637111215734.
            0.17395637111215734,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T1 =====
    # Branch 1, divisor 1.0: FR_S_T1_attachment0 [FR_scapula] -> FR_S_T1_attachment1 [cat_root]
    # ORIGIN for FR_S_T1. Connected body: FR_scapula.
    "FR_S_T1_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0016490221999717954.
            0.0016490221999717954,
            # Run -0.007589861855873643.
            -0.007589861855873643,
            # Run -0.004588559449176619.
            -0.004588559449176619,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T1. Connected body: cat_root.
    "FR_S_T1_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2341128215559215.
            0.2341128215559215,
            # Run -0.010799375055515469.
            -0.010799375055515469,
            # Run 0.17395637111215734.
            0.17395637111215734,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T2 =====
    # Branch 1, divisor 1.0: FL_S_T2_attachment0 [FL_scapula] -> FL_S_T2_attachment1 [cat_root]
    # ORIGIN for FL_S_T2. Connected body: FL_scapula.
    "FL_S_T2_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0015174427443237913.
            0.0015174427443237913,
            # Run -0.00839971492314201.
            -0.00839971492314201,
            # Run 0.004254624312990124.
            0.004254624312990124,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T2. Connected body: cat_root.
    "FL_S_T2_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.22443769174090697.
            0.22443769174090697,
            # Run 0.0116762793895411.
            0.0116762793895411,
            # Run 0.17077170276780373.
            0.17077170276780373,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T2 =====
    # Branch 1, divisor 1.0: FR_S_T2_attachment0 [FR_scapula] -> FR_S_T2_attachment1 [cat_root]
    # ORIGIN for FR_S_T2. Connected body: FR_scapula.
    "FR_S_T2_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0015174427443237913.
            0.0015174427443237913,
            # Run -0.00839971492314201.
            -0.00839971492314201,
            # Run -0.004254624312990124.
            -0.004254624312990124,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T2. Connected body: cat_root.
    "FR_S_T2_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.22443769174090697.
            0.22443769174090697,
            # Run -0.0116762793895411.
            -0.0116762793895411,
            # Run 0.17077170276780373.
            0.17077170276780373,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T3 =====
    # Branch 1, divisor 1.0: FL_S_T3_attachment0 [FL_scapula] -> FL_S_T3_attachment1 [cat_root]
    # ORIGIN for FL_S_T3. Connected body: FL_scapula.
    "FL_S_T3_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0013627636158510797.
            0.0013627636158510797,
            # Run -0.009351782713298548.
            -0.009351782713298548,
            # Run 0.003862063980893065.
            0.003862063980893065,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T3. Connected body: cat_root.
    "FL_S_T3_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.21243192515979034.
            0.21243192515979034,
            # Run 0.015409441199223543.
            0.015409441199223543,
            # Run 0.1736126370395923.
            0.1736126370395923,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T3 =====
    # Branch 1, divisor 1.0: FR_S_T3_attachment0 [FR_scapula] -> FR_S_T3_attachment1 [cat_root]
    # ORIGIN for FR_S_T3. Connected body: FR_scapula.
    "FR_S_T3_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0013627636158510797.
            0.0013627636158510797,
            # Run -0.009351782713298548.
            -0.009351782713298548,
            # Run -0.003862063980893065.
            -0.003862063980893065,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T3. Connected body: cat_root.
    "FR_S_T3_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.21243192515979034.
            0.21243192515979034,
            # Run -0.015409441199223543.
            -0.015409441199223543,
            # Run 0.1736126370395923.
            0.1736126370395923,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T4 =====
    # Branch 1, divisor 1.0: FL_S_T4_attachment0 [FL_scapula] -> FL_S_T4_attachment1 [cat_root]
    # ORIGIN for FL_S_T4. Connected body: FL_scapula.
    "FL_S_T4_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0011449220984346348.
            0.0011449220984346348,
            # Run -0.010278000143844309.
            -0.010278000143844309,
            # Run 0.0034667836427995377.
            0.0034667836427995377,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T4. Connected body: cat_root.
    "FL_S_T4_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.20008094614982327.
            0.20008094614982327,
            # Run 0.01908662916786026.
            0.01908662916786026,
            # Run 0.1768401064874861.
            0.1768401064874861,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T4 =====
    # Branch 1, divisor 1.0: FR_S_T4_attachment0 [FR_scapula] -> FR_S_T4_attachment1 [cat_root]
    # ORIGIN for FR_S_T4. Connected body: FR_scapula.
    "FR_S_T4_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0011449220984346348.
            0.0011449220984346348,
            # Run -0.010278000143844309.
            -0.010278000143844309,
            # Run -0.0034667836427995377.
            -0.0034667836427995377,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T4. Connected body: cat_root.
    "FR_S_T4_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.20008094614982327.
            0.20008094614982327,
            # Run -0.01908662916786026.
            -0.01908662916786026,
            # Run 0.1768401064874861.
            0.1768401064874861,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T5 =====
    # Branch 1, divisor 1.0: FL_S_T5_attachment0 [FL_scapula] -> FL_S_T5_attachment1 [cat_root]
    # ORIGIN for FL_S_T5. Connected body: FL_scapula.
    "FL_S_T5_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0009797837512339586.
            0.0009797837512339586,
            # Run -0.010980160234099564.
            -0.010980160234099564,
            # Run 0.003167120582168551.
            0.003167120582168551,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T5. Connected body: cat_root.
    "FL_S_T5_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.1865681853887686.
            0.1865681853887686,
            # Run 0.023674556976697736.
            0.023674556976697736,
            # Run 0.18106018790692197.
            0.18106018790692197,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T5 =====
    # Branch 1, divisor 1.0: FR_S_T5_attachment0 [FR_scapula] -> FR_S_T5_attachment1 [cat_root]
    # ORIGIN for FR_S_T5. Connected body: FR_scapula.
    "FR_S_T5_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0009797837512339586.
            0.0009797837512339586,
            # Run -0.010980160234099564.
            -0.010980160234099564,
            # Run -0.003167120582168551.
            -0.003167120582168551,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T5. Connected body: cat_root.
    "FR_S_T5_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.1865681853887686.
            0.1865681853887686,
            # Run -0.023674556976697736.
            -0.023674556976697736,
            # Run 0.18106018790692197.
            0.18106018790692197,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T6 =====
    # Branch 1, divisor 1.0: FL_S_T6_attachment0 [FL_scapula] -> FL_S_T6_attachment1 [cat_root]
    # ORIGIN for FL_S_T6. Connected body: FL_scapula.
    "FL_S_T6_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0005560560626145822.
            0.0005560560626145822,
            # Run -0.011881557103370471.
            -0.011881557103370471,
            # Run 0.002839532126640481.
            0.002839532126640481,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T6. Connected body: cat_root.
    "FL_S_T6_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.1760642709531284.
            0.1760642709531284,
            # Run 0.026372768409908903.
            0.026372768409908903,
            # Run 0.18791095712776157.
            0.18791095712776157,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T6 =====
    # Branch 1, divisor 1.0: FR_S_T6_attachment0 [FR_scapula] -> FR_S_T6_attachment1 [cat_root]
    # ORIGIN for FR_S_T6. Connected body: FR_scapula.
    "FR_S_T6_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0005560560626145822.
            0.0005560560626145822,
            # Run -0.011881557103370471.
            -0.011881557103370471,
            # Run -0.002839532126640481.
            -0.002839532126640481,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T6. Connected body: cat_root.
    "FR_S_T6_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.1760642709531284.
            0.1760642709531284,
            # Run -0.026372768409908903.
            -0.026372768409908903,
            # Run 0.18791095712776157.
            0.18791095712776157,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T7 =====
    # Branch 1, divisor 1.0: FL_S_T7_attachment0 [FL_scapula] -> FL_S_T7_attachment1 [cat_root]
    # ORIGIN for FL_S_T7. Connected body: FL_scapula.
    "FL_S_T7_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0004800993907770405.
            0.0004800993907770405,
            # Run -0.012594984013538289.
            -0.012594984013538289,
            # Run 0.002528771441543901.
            0.002528771441543901,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T7. Connected body: cat_root.
    "FL_S_T7_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.16942761000070294.
            0.16942761000070294,
            # Run 0.028487338934251247.
            0.028487338934251247,
            # Run 0.19759941397938688.
            0.19759941397938688,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T7 =====
    # Branch 1, divisor 1.0: FR_S_T7_attachment0 [FR_scapula] -> FR_S_T7_attachment1 [cat_root]
    # ORIGIN for FR_S_T7. Connected body: FR_scapula.
    "FR_S_T7_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0004800993907770405.
            0.0004800993907770405,
            # Run -0.012594984013538289.
            -0.012594984013538289,
            # Run -0.002528771441543901.
            -0.002528771441543901,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T7. Connected body: cat_root.
    "FR_S_T7_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.16942761000070294.
            0.16942761000070294,
            # Run -0.028487338934251247.
            -0.028487338934251247,
            # Run 0.19759941397938688.
            0.19759941397938688,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T8 =====
    # Branch 1, divisor 1.0: FL_S_T8_attachment0 [FL_scapula] -> FL_S_T8_attachment1 [cat_root]
    # ORIGIN for FL_S_T8. Connected body: FL_scapula.
    "FL_S_T8_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0005598619010012685.
            0.0005598619010012685,
            # Run -0.013343888402199973.
            -0.013343888402199973,
            # Run 0.0021708911859018216.
            0.0021708911859018216,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T8. Connected body: cat_root.
    "FL_S_T8_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.16425303594599805.
            0.16425303594599805,
            # Run 0.030136812669404343.
            0.030136812669404343,
            # Run 0.20779362339091326.
            0.20779362339091326,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T8 =====
    # Branch 1, divisor 1.0: FR_S_T8_attachment0 [FR_scapula] -> FR_S_T8_attachment1 [cat_root]
    # ORIGIN for FR_S_T8. Connected body: FR_scapula.
    "FR_S_T8_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0005598619010012685.
            0.0005598619010012685,
            # Run -0.013343888402199973.
            -0.013343888402199973,
            # Run -0.0021708911859018216.
            -0.0021708911859018216,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T8. Connected body: cat_root.
    "FR_S_T8_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.16425303594599805.
            0.16425303594599805,
            # Run -0.030136812669404343.
            -0.030136812669404343,
            # Run 0.20779362339091326.
            0.20779362339091326,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_S_T9 =====
    # Branch 1, divisor 1.0: FL_S_T9_attachment0 [FL_scapula] -> FL_S_T9_attachment1 [cat_root]
    # ORIGIN for FL_S_T9. Connected body: FL_scapula.
    "FL_S_T9_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0006439999858976172.
            0.0006439999858976172,
            # Run -0.014133865079678464.
            -0.014133865079678464,
            # Run 0.0017933996870252023.
            0.0017933996870252023,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_S_T9. Connected body: cat_root.
    "FL_S_T9_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.16700598894960766.
            0.16700598894960766,
            # Run 0.029647353165227562.
            0.029647353165227562,
            # Run 0.2236733320845026.
            0.2236733320845026,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_S_T9 =====
    # Branch 1, divisor 1.0: FR_S_T9_attachment0 [FR_scapula] -> FR_S_T9_attachment1 [cat_root]
    # ORIGIN for FR_S_T9. Connected body: FR_scapula.
    "FR_S_T9_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0006439999858976172.
            0.0006439999858976172,
            # Run -0.014133865079678464.
            -0.014133865079678464,
            # Run -0.0017933996870252023.
            -0.0017933996870252023,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_S_T9. Connected body: cat_root.
    "FR_S_T9_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.16700598894960766.
            0.16700598894960766,
            # Run -0.029647353165227562.
            -0.029647353165227562,
            # Run 0.2236733320845026.
            0.2236733320845026,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_R_C2 =====
    # Branch 1, divisor 1.0: FL_R_C2_attachment0 [FL_scapula] -> FL_R_C2_attachment1 [cat_root]
    # ORIGIN for FL_R_C2. Connected body: FL_scapula.
    "FL_R_C2_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.00421427805669158.
            0.00421427805669158,
            # Run 0.009956284591736005.
            0.009956284591736005,
            # Run 0.009561283478607862.
            0.009561283478607862,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_R_C2. Connected body: cat_root.
    "FL_R_C2_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.27142848686875415.
            0.27142848686875415,
            # Run -0.002657827428674583.
            -0.002657827428674583,
            # Run 0.20982805239781785.
            0.20982805239781785,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_R_C2 =====
    # Branch 1, divisor 1.0: FR_R_C2_attachment0 [FR_scapula] -> FR_R_C2_attachment1 [cat_root]
    # ORIGIN for FR_R_C2. Connected body: FR_scapula.
    "FR_R_C2_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.00421427805669158.
            0.00421427805669158,
            # Run 0.009956284591736005.
            0.009956284591736005,
            # Run -0.009561283478607862.
            -0.009561283478607862,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_R_C2. Connected body: cat_root.
    "FR_R_C2_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.27142848686875415.
            0.27142848686875415,
            # Run 0.002657827428674583.
            0.002657827428674583,
            # Run 0.20982805239781785.
            0.20982805239781785,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_R_C3-7 =====
    # Branch 1, divisor 1.0: FL_R_C3-7_attachment0 [FL_scapula] -> FL_R_C3-7_attachment1 [cat_root]
    # ORIGIN for FL_R_C3-7. Connected body: FL_scapula.
    "FL_R_C3-7_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.00310279235650825.
            0.00310279235650825,
            # Run 0.00868995824284304.
            0.00868995824284304,
            # Run 0.00941303408511365.
            0.00941303408511365,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_R_C3-7. Connected body: cat_root.
    "FL_R_C3-7_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.25213523786591224.
            0.25213523786591224,
            # Run -0.003459217892868749.
            -0.003459217892868749,
            # Run 0.20632892041154333.
            0.20632892041154333,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_R_C3-7 =====
    # Branch 1, divisor 1.0: FR_R_C3-7_attachment0 [FR_scapula] -> FR_R_C3-7_attachment1 [cat_root]
    # ORIGIN for FR_R_C3-7. Connected body: FR_scapula.
    "FR_R_C3-7_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.00310279235650825.
            0.00310279235650825,
            # Run 0.00868995824284304.
            0.00868995824284304,
            # Run -0.00941303408511365.
            -0.00941303408511365,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_R_C3-7. Connected body: cat_root.
    "FR_R_C3-7_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.25213523786591224.
            0.25213523786591224,
            # Run 0.003459217892868749.
            0.003459217892868749,
            # Run 0.20632892041154333.
            0.20632892041154333,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_R_T1 =====
    # Branch 1, divisor 1.0: FL_R_T1_attachment0 [FL_scapula] -> FL_R_T1_attachment1 [cat_root]
    # ORIGIN for FL_R_T1. Connected body: FL_scapula.
    "FL_R_T1_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0001555545282752785.
            0.0001555545282752785,
            # Run 0.0008402433704696094.
            0.0008402433704696094,
            # Run 0.007459435111583078.
            0.007459435111583078,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_R_T1. Connected body: cat_root.
    "FL_R_T1_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.24740381604366046.
            0.24740381604366046,
            # Run -0.003279158157541815.
            -0.003279158157541815,
            # Run 0.21504426254830583.
            0.21504426254830583,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_R_T1 =====
    # Branch 1, divisor 1.0: FR_R_T1_attachment0 [FR_scapula] -> FR_R_T1_attachment1 [cat_root]
    # ORIGIN for FR_R_T1. Connected body: FR_scapula.
    "FR_R_T1_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0001555545282752785.
            0.0001555545282752785,
            # Run 0.0008402433704696094.
            0.0008402433704696094,
            # Run -0.007459435111583078.
            -0.007459435111583078,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_R_T1. Connected body: cat_root.
    "FR_R_T1_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.24740381604366046.
            0.24740381604366046,
            # Run 0.003279158157541815.
            0.003279158157541815,
            # Run 0.21504426254830583.
            0.21504426254830583,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_R_T2 =====
    # Branch 1, divisor 1.0: FL_R_T2_attachment0 [FL_scapula] -> FL_R_T2_attachment1 [cat_root]
    # ORIGIN for FL_R_T2. Connected body: FL_scapula.
    "FL_R_T2_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0015068049132703429.
            -0.0015068049132703429,
            # Run -0.006988896045691723.
            -0.006988896045691723,
            # Run 0.005639624166332163.
            0.005639624166332163,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_R_T2. Connected body: cat_root.
    "FL_R_T2_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.24287721252994796.
            0.24287721252994796,
            # Run -0.0025754774251217057.
            -0.0025754774251217057,
            # Run 0.21834020826460573.
            0.21834020826460573,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_R_T2 =====
    # Branch 1, divisor 1.0: FR_R_T2_attachment0 [FR_scapula] -> FR_R_T2_attachment1 [cat_root]
    # ORIGIN for FR_R_T2. Connected body: FR_scapula.
    "FR_R_T2_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0015068049132703429.
            -0.0015068049132703429,
            # Run -0.006988896045691723.
            -0.006988896045691723,
            # Run -0.005639624166332163.
            -0.005639624166332163,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_R_T2. Connected body: cat_root.
    "FR_R_T2_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.24287721252994796.
            0.24287721252994796,
            # Run 0.0025754774251217057.
            0.0025754774251217057,
            # Run 0.21834020826460573.
            0.21834020826460573,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_R_T3 =====
    # Branch 1, divisor 1.0: FL_R_T3_attachment0 [FL_scapula] -> FL_R_T3_attachment1 [cat_root]
    # ORIGIN for FL_R_T3. Connected body: FL_scapula.
    "FL_R_T3_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0013836213763926102.
            -0.0013836213763926102,
            # Run -0.01516450377661825.
            -0.01516450377661825,
            # Run 0.0018174717400939522.
            0.0018174717400939522,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_R_T3. Connected body: cat_root.
    "FL_R_T3_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2354091170102223.
            0.2354091170102223,
            # Run -0.002630032265058354.
            -0.002630032265058354,
            # Run 0.22304183715388265.
            0.22304183715388265,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_R_T3 =====
    # Branch 1, divisor 1.0: FR_R_T3_attachment0 [FR_scapula] -> FR_R_T3_attachment1 [cat_root]
    # ORIGIN for FR_R_T3. Connected body: FR_scapula.
    "FR_R_T3_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0013836213763926102.
            -0.0013836213763926102,
            # Run -0.01516450377661825.
            -0.01516450377661825,
            # Run -0.0018174717400939522.
            -0.0018174717400939522,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_R_T3. Connected body: cat_root.
    "FR_R_T3_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.2354091170102223.
            0.2354091170102223,
            # Run 0.002630032265058354.
            0.002630032265058354,
            # Run 0.22304183715388265.
            0.22304183715388265,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_R_T4 =====
    # Branch 1, divisor 1.0: FL_R_T4_attachment0 [FL_scapula] -> FL_R_T4_attachment1 [cat_root]
    # ORIGIN for FL_R_T4. Connected body: FL_scapula.
    "FL_R_T4_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0006171901903821737.
            -0.0006171901903821737,
            # Run -0.01637267571851643.
            -0.01637267571851643,
            # Run 0.001136500105504634.
            0.001136500105504634,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_R_T4. Connected body: cat_root.
    "FL_R_T4_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.22545924781618565.
            0.22545924781618565,
            # Run -0.0014434405268229265.
            -0.0014434405268229265,
            # Run 0.22740217128596596.
            0.22740217128596596,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_R_T4 =====
    # Branch 1, divisor 1.0: FR_R_T4_attachment0 [FR_scapula] -> FR_R_T4_attachment1 [cat_root]
    # ORIGIN for FR_R_T4. Connected body: FR_scapula.
    "FR_R_T4_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run -0.0006171901903821737.
            -0.0006171901903821737,
            # Run -0.01637267571851643.
            -0.01637267571851643,
            # Run -0.001136500105504634.
            -0.001136500105504634,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_R_T4. Connected body: cat_root.
    "FR_R_T4_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.22545924781618565.
            0.22545924781618565,
            # Run 0.0014434405268229265.
            0.0014434405268229265,
            # Run 0.22740217128596596.
            0.22740217128596596,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_R_T5 =====
    # Branch 1, divisor 1.0: FL_R_T5_attachment0 [FL_scapula] -> FL_R_T5_attachment1 [cat_root]
    # ORIGIN for FL_R_T5. Connected body: FL_scapula.
    "FL_R_T5_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0002485759413340849.
            0.0002485759413340849,
            # Run -0.016748131645748135.
            -0.016748131645748135,
            # Run 0.0008106705871876146.
            0.0008106705871876146,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_R_T5. Connected body: cat_root.
    "FL_R_T5_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.21767136227520273.
            0.21767136227520273,
            # Run -0.0016274216908904737.
            -0.0016274216908904737,
            # Run 0.23101155292283962.
            0.23101155292283962,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_R_T5 =====
    # Branch 1, divisor 1.0: FR_R_T5_attachment0 [FR_scapula] -> FR_R_T5_attachment1 [cat_root]
    # ORIGIN for FR_R_T5. Connected body: FR_scapula.
    "FR_R_T5_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.0002485759413340849.
            0.0002485759413340849,
            # Run -0.016748131645748135.
            -0.016748131645748135,
            # Run -0.0008106705871876146.
            -0.0008106705871876146,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_R_T5. Connected body: cat_root.
    "FR_R_T5_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [
            # Run 0.21767136227520273.
            0.21767136227520273,
            # Run 0.0016274216908904737.
            0.0016274216908904737,
            # Run 0.23101155292283962.
            0.23101155292283962,
        ],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_DigitalExtensors =====
    # Branch 1, divisor 1.0: FL_ElbowFlexorWristFlexor_s0_origin [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_pulley0 [FL_upperarm] -> FL_ElbowFlexorWristFlexor_s0_insert [FL_forearm]
    # Shared entry 'FL_ElbowFlexorWristFlexor_s0_origin': already defined above.
    # Shared entry 'FL_ElbowFlexorWristFlexor_s0_insert': already defined above.
    # Branch 2, divisor 1.0: FL_ElbowFlexorWristFlexor_s1_origin [FL_forearm] -> FL_ElbowFlexorWristFlexor_s1_pulley0 [FL_forearm] -> FL_DigitalExtensors_attachment0 [FL_carpals] -> FL_DigitalExtensors_attachment1 [FL_digits]
    # Shared entry 'FL_ElbowFlexorWristFlexor_s1_origin': already defined above.
    # VIA POINT for FL_DigitalExtensors. Connected body: FL_carpals.
    "FL_DigitalExtensors_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.0005687001860839453, 0.005971577177090113, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_DigitalExtensors. Connected body: FL_digits.
    "FL_DigitalExtensors_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.004866957206077467, 0.0022584706445033056, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_DigitalExtensors =====
    # Branch 1, divisor 1.0: FR_ElbowFlexorWristFlexor_s0_origin [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_pulley0 [FR_upperarm] -> FR_ElbowFlexorWristFlexor_s0_insert [FR_forearm]
    # Shared entry 'FR_ElbowFlexorWristFlexor_s0_origin': already defined above.
    # Shared entry 'FR_ElbowFlexorWristFlexor_s0_insert': already defined above.
    # Branch 2, divisor 1.0: FR_ElbowFlexorWristFlexor_s1_origin [FR_forearm] -> FR_ElbowFlexorWristFlexor_s1_pulley0 [FR_forearm] -> FR_DigitalExtensors_attachment0 [FR_carpals] -> FR_DigitalExtensors_attachment1 [FR_digits]
    # Shared entry 'FR_ElbowFlexorWristFlexor_s1_origin': already defined above.
    # VIA POINT for FR_DigitalExtensors. Connected body: FR_carpals.
    "FR_DigitalExtensors_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [-0.0005687001860839453, 0.005971577177090113, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_DigitalExtensors. Connected body: FR_digits.
    "FR_DigitalExtensors_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.004866957206077467, 0.0022584706445033056, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_DigitalFlexors =====
    # Branch 1, divisor 1.0: FL_WristExtensor_s0_origin [FL_forearm] -> FL_WristExtensor_s0_insert [FL_forearm]
    # Shared entry 'FL_WristExtensor_s0_origin': already defined above.
    # Shared entry 'FL_WristExtensor_s0_insert': already defined above.
    # Branch 2, divisor 1.0: FL_WristExtensor_s1_origin [FL_forearm] -> FL_WristExtensor_s1_pulley0 [FL_forearm] -> FL_DigitalFlexors_attachment0 [FL_carpals] -> FL_DigitalFlexors_attachment1 [FL_digits]
    # Shared entry 'FL_WristExtensor_s1_origin': already defined above.
    # VIA POINT for FL_DigitalFlexors. Connected body: FL_carpals.
    "FL_DigitalFlexors_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0005376851212354235, -0.0054544472004418275, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_DigitalFlexors. Connected body: FL_digits.
    "FL_DigitalFlexors_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0011753936623770337, -0.006021532171048234, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_DigitalFlexors =====
    # Branch 1, divisor 1.0: FR_WristExtensor_s0_origin [FR_forearm] -> FR_WristExtensor_s0_insert [FR_forearm]
    # Shared entry 'FR_WristExtensor_s0_origin': already defined above.
    # Shared entry 'FR_WristExtensor_s0_insert': already defined above.
    # Branch 2, divisor 1.0: FR_WristExtensor_s1_origin [FR_forearm] -> FR_WristExtensor_s1_pulley0 [FR_forearm] -> FR_DigitalFlexors_attachment0 [FR_carpals] -> FR_DigitalFlexors_attachment1 [FR_digits]
    # Shared entry 'FR_WristExtensor_s1_origin': already defined above.
    # VIA POINT for FR_DigitalFlexors. Connected body: FR_carpals.
    "FR_DigitalFlexors_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0005376851212354235, -0.0054544472004418275, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_DigitalFlexors. Connected body: FR_digits.
    "FR_DigitalFlexors_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0011753936623770337, -0.006021532171048234, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_TrapeziusCervical =====
    # Branch 1, divisor 1.0: FL_TrapeziusCervical_origin [cat_root] -> FL_TrapeziusCervical_insertion [FL_scapula]
    # ORIGIN for FL_TrapeziusCervical. Connected body: cat_root.
    "FL_TrapeziusCervical_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.285, -0.0, 0.222],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_TrapeziusCervical. Connected body: FL_scapula.
    "FL_TrapeziusCervical_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03, 0.002, 0.006],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_TrapeziusCervical =====
    # Branch 1, divisor 1.0: FR_TrapeziusCervical_origin [cat_root] -> FR_TrapeziusCervical_insertion [FR_scapula]
    # ORIGIN for FR_TrapeziusCervical. Connected body: cat_root.
    "FR_TrapeziusCervical_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.285, 0.0, 0.222],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_TrapeziusCervical. Connected body: FR_scapula.
    "FR_TrapeziusCervical_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03, 0.002, -0.006],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_TrapeziusThoracic =====
    # Branch 1, divisor 1.0: FL_TrapeziusThoracic_origin [cat_root] -> FL_TrapeziusThoracic_insertion [FL_scapula]
    # ORIGIN for FL_TrapeziusThoracic. Connected body: cat_root.
    "FL_TrapeziusThoracic_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.185, -0.0, 0.238],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_TrapeziusThoracic. Connected body: FL_scapula.
    "FL_TrapeziusThoracic_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.018, -0.006, 0.006],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_TrapeziusThoracic =====
    # Branch 1, divisor 1.0: FR_TrapeziusThoracic_origin [cat_root] -> FR_TrapeziusThoracic_insertion [FR_scapula]
    # ORIGIN for FR_TrapeziusThoracic. Connected body: cat_root.
    "FR_TrapeziusThoracic_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.185, 0.0, 0.238],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_TrapeziusThoracic. Connected body: FR_scapula.
    "FR_TrapeziusThoracic_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.018, -0.006, -0.006],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_LatissimusDorsi =====
    # Branch 1, divisor 1.0: FL_LatissimusDorsi_origin [cat_root] -> FL_LatissimusDorsi_insertion [FL_upperarm]
    # ORIGIN for FL_LatissimusDorsi. Connected body: cat_root.
    "FL_LatissimusDorsi_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.12, 0.012, 0.227],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_LatissimusDorsi. Connected body: FL_upperarm.
    "FL_LatissimusDorsi_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.013834, 0.00935472, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_LatissimusDorsi =====
    # Branch 1, divisor 1.0: FR_LatissimusDorsi_origin [cat_root] -> FR_LatissimusDorsi_insertion [FR_upperarm]
    # ORIGIN for FR_LatissimusDorsi. Connected body: cat_root.
    "FR_LatissimusDorsi_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.12, -0.012, 0.227],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_LatissimusDorsi. Connected body: FR_upperarm.
    "FR_LatissimusDorsi_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.013834, 0.00935472, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_PectoralisProfundus =====
    # Branch 1, divisor 1.0: FL_PectoralisProfundus_origin [cat_root] -> FL_PectoralisProfundus_insertion [FL_upperarm]
    # ORIGIN for FL_PectoralisProfundus. Connected body: cat_root.
    "FL_PectoralisProfundus_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.185, 0.005, 0.155],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_PectoralisProfundus. Connected body: FL_upperarm.
    "FL_PectoralisProfundus_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.012, 0.01, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_PectoralisProfundus =====
    # Branch 1, divisor 1.0: FR_PectoralisProfundus_origin [cat_root] -> FR_PectoralisProfundus_insertion [FR_upperarm]
    # ORIGIN for FR_PectoralisProfundus. Connected body: cat_root.
    "FR_PectoralisProfundus_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.185, -0.005, 0.155],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_PectoralisProfundus. Connected body: FR_upperarm.
    "FR_PectoralisProfundus_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.012, 0.01, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_PectoralisSuperficialis =====
    # Branch 1, divisor 1.0: FL_PectoralisSuperficialis_origin [cat_root] -> FL_PectoralisSuperficialis_insertion [FL_upperarm]
    # ORIGIN for FL_PectoralisSuperficialis. Connected body: cat_root.
    "FL_PectoralisSuperficialis_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.245, 0.004, 0.157],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_PectoralisSuperficialis. Connected body: FL_upperarm.
    "FL_PectoralisSuperficialis_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03, 0.005, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_PectoralisSuperficialis =====
    # Branch 1, divisor 1.0: FR_PectoralisSuperficialis_origin [cat_root] -> FR_PectoralisSuperficialis_insertion [FR_upperarm]
    # ORIGIN for FR_PectoralisSuperficialis. Connected body: cat_root.
    "FR_PectoralisSuperficialis_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.245, -0.004, 0.157],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_PectoralisSuperficialis. Connected body: FR_upperarm.
    "FR_PectoralisSuperficialis_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.03, 0.005, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FL_Clavobrachialis =====
    # Branch 1, divisor 1.0: FL_Clavobrachialis_origin [cat_root] -> FL_Clavobrachialis_insertion [FL_upperarm]
    # ORIGIN for FL_Clavobrachialis. Connected body: cat_root.
    "FL_Clavobrachialis_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.3, 0.012, 0.19],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FL_Clavobrachialis. Connected body: FL_upperarm.
    "FL_Clavobrachialis_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.025, 0.003, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # ===== FR_Clavobrachialis =====
    # Branch 1, divisor 1.0: FR_Clavobrachialis_origin [cat_root] -> FR_Clavobrachialis_insertion [FR_upperarm]
    # ORIGIN for FR_Clavobrachialis. Connected body: cat_root.
    "FR_Clavobrachialis_origin": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.3, -0.012, 0.19],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # INSERTION for FR_Clavobrachialis. Connected body: FR_upperarm.
    "FR_Clavobrachialis_insertion": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.025, 0.003, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_pelvis_anchor. Editing this site does not change MT lengths.
    "L_IP_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, -0.005028361385832787, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_pelvis_anchor. Editing this site does not change MT lengths.
    "L_BFA_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.005028361385832787, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_pelvis_anchor. Editing this site does not change MT lengths.
    "L_RF_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, -0.005240210582433694, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_pelvis_anchor. Editing this site does not change MT lengths.
    "L_BFP_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.005240210582433694, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_pelvis_anchor. Editing this site does not change MT lengths.
    "L_SAM_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, -0.005240210582433694, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_thigh. Editing this site does not change MT lengths.
    "L_VL_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.011643902439024393, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_thigh. Editing this site does not change MT lengths.
    "L_VM_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.011643902439024393, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_thigh. Editing this site does not change MT lengths.
    "L_RF_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.011643902439024393, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_thigh. Editing this site does not change MT lengths.
    "L_BFP_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, -0.006288252698920432, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_thigh. Editing this site does not change MT lengths.
    "L_SAM_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, -0.006288252698920432, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_thigh. Editing this site does not change MT lengths.
    "L_LG_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, -0.006477903391572458, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_thigh. Editing this site does not change MT lengths.
    "L_MG_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, -0.006477903391572458, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_shank. Editing this site does not change MT lengths.
    "L_TA_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.005585141066940424, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_shank. Editing this site does not change MT lengths.
    "L_SO_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, -0.005585141066940424, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_shank. Editing this site does not change MT lengths.
    "L_LG_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, -0.005373291870339516, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_shank. Editing this site does not change MT lengths.
    "L_MG_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, -0.005373291870339516, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_shank. Editing this site does not change MT lengths.
    "L_EDL_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.07361713995943205, -0.0, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_shank. Editing this site does not change MT lengths.
    "L_EDL_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0033012170385395534, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_shank. Editing this site does not change MT lengths.
    "L_FDL_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.08495131845841784, -0.0, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_shank. Editing this site does not change MT lengths.
    "L_FDL_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, -0.0033012170385395534, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_foot. Editing this site does not change MT lengths.
    "L_EDL_attachment2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.067, 0.001694772344013491, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_foot. Editing this site does not change MT lengths.
    "L_FDL_attachment2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.067, -0.001694772344013491, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_digits. Editing this site does not change MT lengths.
    "L_paw": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.027058823529411764, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_digits. Editing this site does not change MT lengths.
    "L_EDL_attachment3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0119952, -0.0, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: L_digits. Editing this site does not change MT lengths.
    "L_FDL_attachment3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0119952, -0.0, -0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_pelvis_anchor. Editing this site does not change MT lengths.
    "R_IP_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, -0.005028361385832787, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_pelvis_anchor. Editing this site does not change MT lengths.
    "R_BFA_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.005028361385832787, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_pelvis_anchor. Editing this site does not change MT lengths.
    "R_RF_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, -0.005240210582433694, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_pelvis_anchor. Editing this site does not change MT lengths.
    "R_BFP_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, 0.005240210582433694, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_pelvis_anchor. Editing this site does not change MT lengths.
    "R_SAM_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0, -0.005240210582433694, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_thigh. Editing this site does not change MT lengths.
    "R_VL_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.011643902439024393, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_thigh. Editing this site does not change MT lengths.
    "R_VM_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.011643902439024393, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_thigh. Editing this site does not change MT lengths.
    "R_RF_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, 0.011643902439024393, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_thigh. Editing this site does not change MT lengths.
    "R_BFP_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, -0.006288252698920432, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_thigh. Editing this site does not change MT lengths.
    "R_SAM_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, -0.006288252698920432, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_thigh. Editing this site does not change MT lengths.
    "R_LG_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, -0.006477903391572458, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_thigh. Editing this site does not change MT lengths.
    "R_MG_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0955, -0.006477903391572458, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_shank. Editing this site does not change MT lengths.
    "R_TA_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.005585141066940424, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_shank. Editing this site does not change MT lengths.
    "R_SO_side0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, -0.005585141066940424, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_shank. Editing this site does not change MT lengths.
    "R_LG_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, -0.005373291870339516, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_shank. Editing this site does not change MT lengths.
    "R_MG_side1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, -0.005373291870339516, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_shank. Editing this site does not change MT lengths.
    "R_EDL_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.07361713995943205, -0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_shank. Editing this site does not change MT lengths.
    "R_EDL_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, 0.0033012170385395534, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_shank. Editing this site does not change MT lengths.
    "R_FDL_attachment0": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.08495131845841784, -0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_shank. Editing this site does not change MT lengths.
    "R_FDL_attachment1": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.1085, -0.0033012170385395534, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_foot. Editing this site does not change MT lengths.
    "R_EDL_attachment2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.067, 0.001694772344013491, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_foot. Editing this site does not change MT lengths.
    "R_FDL_attachment2": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.067, -0.001694772344013491, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_digits. Editing this site does not change MT lengths.
    "R_paw": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.027058823529411764, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_digits. Editing this site does not change MT lengths.
    "R_EDL_attachment3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0119952, -0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: R_digits. Editing this site does not change MT lengths.
    "R_FDL_attachment3": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.0119952, -0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: FL_digits. Editing this site does not change MT lengths.
    "FL_paw": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.017, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
    # AUXILIARY SITE; not referenced by any muscle tendon in this configuration. Body: FR_digits. Editing this site does not change MT lengths.
    "FR_paw": {
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: m.
        # Original raw/source: None; None = not independently established.
        "position_in_body_m": [0.017, 0.0, 0.0],
        # A point-site orientation does not move its centre; it does not change MT path length.
        # Fixed site in owning body frame; dynamic routing sites are configured separately. Unit: 1.
        # Original raw/source: None; None = not independently established.
        "orientation_in_body_wxyz": [1.0, 0.0, 0.0, 0.0],
    },
}
