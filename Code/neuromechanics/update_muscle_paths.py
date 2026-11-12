"""Update muscle paths.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

from .calculate_muscle_route_points import calculate_muscle_route_points


def update_muscle_paths(state):
    """Update source pulley tangent sites from current joint positions."""
    meta = state["routing_meta"]
    state["model"].site_pos[meta[:, 5], :2] = calculate_muscle_route_points(
        state["data"].qpos,
        meta,
        state["routing_geom"],
    )
