"""Translate named initial conditions into the native coupled state."""

import numpy as np

from .load_parameter_file import load_parameter_file

from .apply_forward_initial_state import apply_forward_initial_state


def apply_initial_parameter_file(state, path):
    """Apply this state once at t=0. Never reset it at a stride boundary."""
    p = load_parameter_file(path)
    m = state["model"]
    coordinates = [m.joint(i).name for i in range(m.njnt)]
    if m.nq != m.nv or m.nv != m.njnt:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Named initial state currently supports scalar joints only")
    names = list(state["names"])
    pads = [m.geom(int(i)).name for i in state["pad_ids"]]
    for section, expected in [
        ("coordinates", coordinates),
        ("muscles", names),
        ("contact_memory", pads),
    ]:
        if set(p[section]) != set(expected):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Initial {section} names do not match model")
    q = np.empty(m.nq)
    v = np.empty(m.nv)
    for i, name in enumerate(coordinates):
        q[m.jnt_qposadr[i]] = p["coordinates"][name]["position"]
        v[m.jnt_dofadr[i]] = p["coordinates"][name]["velocity"]
    apply_forward_initial_state(
        state,
        dict(
            qpos=q,
            qvel=v,
            activation=np.array([p["muscles"][n]["activation_0_to_1"] for n in names]),
            fiber_length=np.array([p["muscles"][n]["fiber_length_m"] for n in names]),
            bristle=np.array([p["contact_memory"][n] for n in pads]),
        ),
    )
