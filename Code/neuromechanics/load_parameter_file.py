"""Read a commented, editable Python dictionary without executing code."""

import ast

from pathlib import Path


def load_parameter_file(path):
    """The file contains comments/docstrings and one PARAMETERS assignment.

    Using literal dictionaries keeps configuration approachable while avoiding
    hidden computations. Every applied number is visible in the file.
    """
    tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == "PARAMETERS"
    ]
    if len(assignments) != 1:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError(f"{path}: expected one PARAMETERS dictionary")
    values = ast.literal_eval(assignments[0].value)
    if not isinstance(values, dict):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("PARAMETERS must be a dictionary")
    # Saved configurations may use the former name for this same force scale.
    # Normalize the name only: retain the value and its existing pennation projection.
    if Path(path).name == "muscle_tendon.py":
        old_name = "max_isometric_tendon_force_N"
        force_name = "max_isometric_muscle_force_along_tendon_N"
        for muscle, parameters in values.items():
            if old_name in parameters:
                # Two names would make it unclear which user-edited value to apply.
                if force_name in parameters:
                    raise ValueError(f"{path}/{muscle}: duplicate isometric force fields")
                parameters[force_name] = parameters.pop(old_name)
    return values
