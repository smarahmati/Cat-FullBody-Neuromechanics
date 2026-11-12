"""Read the real tendon transmission, including branches and wrap objects.

This is an inspection function. It never substitutes a straight line for the
engine path and never changes anatomy. Names come from the loaded model.
"""

import numpy as np

import mujoco as mj


def describe_muscle_paths(state):
    """Return SI coordinates, connected bodies and ordered path elements.

    A MuJoCo spatial tendon can contain multiple branches. A branch endpoint
    is not necessarily a separate anatomical origin/insertion. Side sites
    choose the side of a wrapping object; the tendon does not pass through
    those sites. The distinction matters when interpreting an attachment edit.
    """
    s = state
    m = s["model"]
    d = s["data"]
    moving = {int(meta[5]): row for row, meta in enumerate(s["routing_meta"])}
    result = []
    for i, name in enumerate(s["names"]):
        tendon_id = int(m.actuator_trnid[i, 0])
        if int(m.actuator_trntype[i]) != int(mj.mjtTrn.mjTRN_TENDON):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"{name}: inspection expects a tendon transmission")
        start = int(m.tendon_adr[tendon_id])
        branches = [dict(divisor=1.0, elements=[])]
        for k in range(start, start + int(m.tendon_num[tendon_id])):
            kind = int(m.wrap_type[k])
            object_id = int(m.wrap_objid[k])
            if kind == int(mj.mjtWrap.mjWRAP_PULLEY):
                branches.append(dict(divisor=float(m.wrap_prm[k]), elements=[]))
                # Skip the remaining work for this item.
                continue
            if kind == int(mj.mjtWrap.mjWRAP_SITE):
                body = int(m.site_bodyid[object_id])
                entry = dict(
                    kind="site",
                    name=m.site(object_id).name,
                    body=m.body(body).name,
                    local_position_m=m.site_pos[object_id].tolist(),
                    world_position_m=d.site_xpos[object_id].tolist(),
                    moving=object_id in moving,
                    editable_file="routing.py" if object_id in moving else "attachments.py",
                )
            elif kind in (int(mj.mjtWrap.mjWRAP_CYLINDER), int(mj.mjtWrap.mjWRAP_SPHERE)):
                body = int(m.geom_bodyid[object_id])
                side = int(m.wrap_prm[k])
                entry = dict(
                    kind="wrap",
                    name=m.geom(object_id).name,
                    shape=(
                        "cylinder"
                        if kind == int(mj.mjtWrap.mjWRAP_CYLINDER)
                        else "sphere"
                    ),
                    body=m.body(body).name,
                    local_position_m=m.geom_pos[object_id].tolist(),
                    radius_m=float(m.geom_size[object_id, 0]),
                    editable_file="wrapping.py",
                    side_site=(
                        None
                        if side < 0
                        else dict(
                            name=m.site(side).name,
                            body=m.body(int(m.site_bodyid[side])).name,
                            local_position_m=m.site_pos[side].tolist(),
                            moving=side in moving,
                            editable_file=(
                                "routing.py"
                                if side in moving
                                else "attachments.py"
                            ),
                        )
                    ),
                )
            else:
                # Stop and explain the invalid model setting or failed calculation.
                raise ValueError(f"{name}: unsupported wrap type {kind}")
            branches[-1]["elements"].append(entry)
        branches = [b for b in branches if b["elements"]]
        for branch_index, branch in enumerate(branches):
            sites = [e for e in branch["elements"] if e["kind"] == "site"]
            for index, point in enumerate(sites):
                point["role"] = (
                    ("origin" if branch_index == 0 else "internal branch start")
                    if index == 0
                    else (
                        (
                            "insertion"
                            if branch_index == len(branches) - 1
                            else "internal branch end"
                        )
                        if index == len(sites) - 1
                        else "via point"
                    )
                )
        result.append(
            dict(
                muscle=str(name),
                tendon=m.tendon(tendon_id).name,
                branches=branches,
                path_length_m=float(d.actuator_length[i]),
                length_offset_m=float(s["mtu_length_offset"][i]),
                MT_length_m=float(d.actuator_length[i] + s["mtu_length_offset"][i]),
                tendon_gear=float(m.actuator_gear[i, 0]),
            )
        )
    return result
