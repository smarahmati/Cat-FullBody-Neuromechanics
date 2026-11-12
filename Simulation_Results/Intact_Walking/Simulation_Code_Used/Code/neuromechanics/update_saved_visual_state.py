"""Update only the geometry needed to draw an archived forward state."""

import mujoco as mj

from .update_muscle_paths import update_muscle_paths


def update_saved_visual_state(state, sample):
    """Avoid collision/constraint/muscle solves during a visualization replay.

    This is not a replacement for advance_partitioned_timestep. The archived forward dynamics
    already computed the motion and Ground_Reaction_Forces. These calls place bones, sites and
    wrapped tendon paths at the saved/interpolated pose for rendering only.
    """
    m, d = state["model"], state["data"]
    if m.nq != m.nv:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("This display interpolator requires scalar joint coordinates")
    d.qpos[:] = sample["qpos"]
    d.qvel[:] = sample["qvel"]
    d.act[:] = sample["activation"]
    d.ctrl[:] = sample["excitation"]
    d.time = sample["time"]
    update_muscle_paths(state)
    mj.mj_kinematics(m, d)
    mj.mj_comPos(m, d)
    mj.mj_tendon(m, d)
