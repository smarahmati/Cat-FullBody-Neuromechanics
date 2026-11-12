"""Timing agreement between input muscle_excitation and EMG on the original clock."""

import numpy as np

from scipy.optimize import linear_sum_assignment


def emg_phase_metrics(muscle_excitation, reference, period, threshold=0.10):
    """Score one complete cycle; both arrays are already peak-normalized.

    The detection threshold is an analysis choice. No signal is phase-shifted,
    filtered, baseline-subtracted or modified. Edge matching is circular, so
    a burst crossing the end of the cycle is handled as one burst.
    """
    u = np.asarray(muscle_excitation, float)
    r = np.asarray(reference, float)
    if u.shape != r.shape or u.ndim != 1:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Use equally sampled one-dimensional cycles")
    predicted = u > threshold
    expected = r > threshold

    def edges(mask):
        return np.flatnonzero(mask & ~np.roll(mask, 1)), np.flatnonzero(
            ~mask
            & np.roll(mask, 1)
        )

    on, off = edges(predicted)
    ron, roff = edges(expected)
    n = len(u)

    def match(got, wanted):
        if not len(got) or not len(wanted):
            return dict(
                mean_absolute_error_s=None,
                maximum_absolute_error_s=None,
                unmatched_predicted=len(got),
                unmatched_reference=len(wanted),
            )
        difference = ((got[:, None] - wanted[None, :] + n / 2) % n - n / 2) * period / n
        rows, cols = linear_sum_assignment(abs(difference))
        # Calculate the error in this comparison.
        error = abs(difference[rows, cols])
        return dict(
            mean_absolute_error_s=float(error.mean()),
            maximum_absolute_error_s=float(error.max()),
            unmatched_predicted=int(len(got) - len(rows)),
            unmatched_reference=int(len(wanted) - len(cols)),
        )

    union = np.count_nonzero(predicted | expected)
    return dict(
        threshold_fraction_of_peak=threshold,
        active_intersection_over_union=(
            float(np.count_nonzero(predicted & expected) / union)
            if union
            else 1.0
        ),
        phase_disagreement_fraction=float(np.mean(predicted != expected)),
        active_fraction_predicted=float(predicted.mean()),
        active_fraction_reference=float(expected.mean()),
        false_active_fraction_of_cycle=float(np.mean(predicted & ~expected)),
        missed_active_fraction_of_cycle=float(np.mean(~predicted & expected)),
        onset=match(on, ron),
        offset=match(off, roff),
        predicted_burst_count=int(len(on)),
        reference_burst_count=int(len(ron)),
    )
