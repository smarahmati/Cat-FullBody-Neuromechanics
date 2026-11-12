"""Interpolate saved scalar-coordinate states for display, never for physics."""

import numpy as np


def interpolate_simulation_for_display(result, time_s):
    """Return one display sample between the two surrounding archived samples.

    The present sagittal model has scalar translations/hinges (nq == nv),
    so coordinate interpolation does not involve quaternions. Recorded arrays
    and force peaks are never edited. No smoothing or new dynamics is applied.
    """
    times = result["time"]
    t = float(np.clip(time_s, times[0], times[-1]))
    right = min(len(times) - 1, int(np.searchsorted(times, t, side="right")))
    left = max(0, right - 1)
    weight = 0.0 if right == left else (t - times[left]) / (times[right] - times[left])
    fields = ["qpos", "qvel", "activation", "excitation", "force", "grf", "joint_q"]
    sample = {
        key: (1.0 - weight) * result[key][left] + weight * result[key][right]
        for key in fields
    }
    sample.update(time=t, left_index=left, right_index=right, fraction=float(weight))
    return sample
