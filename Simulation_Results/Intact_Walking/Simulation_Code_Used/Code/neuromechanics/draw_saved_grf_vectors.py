"""Draw the saved four-paw force vectors in the passive MuJoCo viewer."""

import mujoco as mj

import numpy as np


def draw_saved_grf_vectors(viewer, state, forces, enabled=True, metres_per_newton=0.006):
    """Use actual saved Ground_Reaction_Forces; arrow tails are ground projections of paw sites.

    The archive has no centre-of-pressure trace. A projected paw site is an
    explicit visualization anchor, not a measured or reconstructed COP.
    Forces below 0.05 N are hidden only as arrows; time series remain unchanged.
    Call with the viewer lock held. This viewer reserves user_scn for arrows.
    """
    scene = viewer.user_scn
    scene.ngeom = 0
    if not enabled:
        return []
    colors = [
        [0.05, 0.82, 1.0, 1.0],
        [1.0, 0.15, 0.58, 1.0],
        [1.0, 0.72, 0.05, 1.0],
        [0.68, 0.35, 1.0, 1.0],
    ]
    labels = ["LH", "RH", "LF", "RF"]
    records = []
    m, d = state["model"], state["data"]
    planes = np.flatnonzero(m.geom_type == int(mj.mjtGeom.mjGEOM_PLANE))
    ground_z = float(m.geom_pos[planes[0], 2]) if len(planes) else 0.0
    for side, force in enumerate(forces):
        magnitude = float(np.linalg.norm(force))
        if magnitude < 0.05:
            # Skip the remaining work for this item.
            continue
        origin = d.site_xpos[state["paw_ids"][side]].copy()
        origin[2] = ground_z + 0.002
        tip = origin + metres_per_newton * force
        geom = scene.geoms[scene.ngeom]
        mj.mjv_initGeom(
            geom,
            mj.mjtGeom.mjGEOM_ARROW,
            np.zeros(3),
            origin,
            np.eye(3).ravel(),
            np.asarray(colors[side], dtype=np.float32),
        )
        mj.mjv_connector(geom, mj.mjtGeom.mjGEOM_ARROW, 0.0035, origin, tip)
        geom.label = f"{labels[side]} {magnitude:.1f} N"
        scene.ngeom += 1
        records.append(
            dict(
                limb=labels[side],
                force_N=force.tolist(),
                origin_m=origin.tolist(),
                tip_m=tip.tolist(),
            )
        )
    return records
