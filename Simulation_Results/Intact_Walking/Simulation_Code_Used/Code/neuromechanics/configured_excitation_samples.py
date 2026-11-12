"""All saved input samples, for one fixed normalization scale per muscle."""

import numpy as np

from model_configuration.paths import ROOT


def configured_excitation_samples(settings, fallback=None):
    if settings.get("excitation_table_file"):
        from .read_time_series import read_time_series

        return read_time_series(ROOT / settings["excitation_table_file"])[2]
    if settings.get("excitation_sequence_file"):
        sequence = np.load(ROOT / settings["excitation_sequence_file"])[
            "excitation_sequence"
        ]
        return sequence.reshape(-1, sequence.shape[-1])
    if "excitation_control_points" in settings:
        return np.asarray(settings["excitation_control_points"])
    if settings.get("excitation_file"):
        return np.load(ROOT / settings["excitation_file"])["excitation_table"]
    if fallback is not None:
        return fallback
    # Stop and explain the invalid model setting or failed calculation.
    raise ValueError("No saved muscle_excitation input is configured")
