"""Read a named, editable tab-delimited numerical time-series table."""

from pathlib import Path

import numpy as np


def read_time_series(path, expected_channels=None):
    """First column is phase (0..1); remaining headers are channel names.

    A complete cycle includes both endpoints. No silent clipping, column
    reordering, phase shift, filtering or extrapolation occurs here.
    """
    path = Path(path)
    headers = path.read_text(encoding="utf-8").splitlines()[0].split("\t")
    values = np.loadtxt(path, delimiter="\t", skiprows=1, ndmin=2)
    if headers[0] != "phase_0_to_1" or len(headers) != values.shape[1]:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError(f"{path}: invalid column headers")
    if len(set(headers)) != len(headers) or not np.isfinite(values).all():
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError(f"{path}: duplicate names or nonfinite values")
    phase = values[:, 0]
    if len(phase) < 2 or phase[0] != 0 or phase[-1] != 1 or np.any(np.diff(phase) <= 0):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError(f"{path}: phase must increase strictly from 0 to 1")
    if expected_channels is not None and headers[1:] != list(expected_channels):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError(f"{path}: channel names/order differ from the model")
    return phase, headers[1:], values[:, 1:]
