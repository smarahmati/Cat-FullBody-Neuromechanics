"""Install editable muscle wrap geometry before forward integration."""

import numpy as np

import mujoco as mj

from .load_parameter_file import load_parameter_file


def apply_wrapping_parameters(state, path):
    """Only tendon wrap objects may be edited here; bones/contact are separate.

    Historical bundles without this file retain their original wrap geometry.
    Topology and body ownership are deliberately kept in the anatomical model.
    """
    if not path.exists():
        return
    m = state["model"]
    ids = sorted(
        {
            int(m.wrap_objid[k])
            for k in range(m.nwrap)
            if int(m.wrap_type[k])
            in (int(mj.mjtWrap.mjWRAP_CYLINDER), int(mj.mjtWrap.mjWRAP_SPHERE))
        }
    )
    entries = load_parameter_file(path)
    if set(entries) != {m.geom(i).name for i in ids}:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("wrapping.py: wrap object names differ from the model")
    for i in ids:
        name = m.geom(i).name
        row = entries[name]
        if set(row) != {"position_in_body_m", "orientation_in_body_wxyz", "radius_m"}:
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"wrapping.py/{name}: unknown or missing field")
        position = np.asarray(row["position_in_body_m"], float)
        quaternion = np.asarray(row["orientation_in_body_wxyz"], float)
        radius = float(row["radius_m"])
        if (
            position.shape != (3,)
            or quaternion.shape != (4,)
            or not np.isfinite(position).all()
            or not np.isfinite(quaternion).all()
        ):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"wrapping.py/{name}: expected finite xyz and wxyz vectors")
        if (
            not np.isfinite(radius)
            or radius <= 0
            or not np.isclose(np.linalg.norm(quaternion), 1.0, atol=1e-7)
        ):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(
                f"wrapping.py/{name}: radius must be positive and quaternion unit length"
            )
        if not np.array_equal(m.geom_pos[i], position) or not np.array_equal(
            m.geom_quat[i],
            quaternion,
        ):
            m.geom_sameframe[i] = 0  # Invalidate the compiled coincident-frame shortcut.
        m.geom_pos[i] = position
        m.geom_quat[i] = quaternion
        m.geom_size[i, 0] = radius
