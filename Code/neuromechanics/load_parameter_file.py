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
    return values
