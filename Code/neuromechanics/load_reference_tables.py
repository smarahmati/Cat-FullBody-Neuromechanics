"""Read the inspectable source-reference tables, without fitting or filtering."""

import json

from pathlib import Path

import numpy as np

from model_configuration.paths import ROOT

from .read_time_series import read_time_series


def load_reference_tables(folder=None):
    """Return source cycles, LH assembly correction and the separate FHL EMG.

    Optional text tables are exactly the numeric source arrays, not polynomial
    fits. Each file has its own original sampling grid. The caller applies the
    documented fixed limb phase offsets. No reference is used as a force.
    """
    if folder is None:
        return (
            dict(np.load(ROOT / "Data/Experimental_Reference_Data/hindlimb_forelimb_reference_cycles.npz")),
            np.load(ROOT / "Data/Experimental_Reference_Data/hindlimb_pose_initialization.npz")[
                "left_joint_correction_rad"
            ],
            np.load(ROOT / "Data/Experimental_Reference_Data/hindlimb_flexor_hallucis_longus_emg.npz")["FHL_peak_normalized"],
        )
    folder = ROOT / Path(folder)
    manifest = json.loads((folder / "TABLE_MANIFEST.json").read_text())
    out = {}
    for name, item in manifest["tables"].items():
        phase, channels, values = read_time_series(folder / item["file"], item["columns"])
        if not np.allclose(phase, np.linspace(0, 1, len(phase)), atol=1e-12, rtol=0):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(f"Reference {name} needs a uniform phase grid")
        out[name] = values.reshape((len(phase),) + tuple(item["shape_after_time"]))
    correction = out.pop("left_joint_correction_rad")
    fhl = out.pop("FHL_peak_normalized")
    return out, correction, fhl
