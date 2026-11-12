"""Interpolate a prerecorded muscle_excitation sequence using time only."""

import numpy as np


def fixed_sequence_excitation(state, time):
    dt = state["model"].opt.timestep
    period = state["settings"]["period_s"]
    steps = round(period / dt)
    tick = round(time / dt)
    if abs(steps * dt - period) > 1e-10:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError(
            "Frozen sequence requires an integer number of integration steps per stride"
        )
    if "offline_cycle_input" in state:
        start, table = state["offline_cycle_input"]
        phase = np.clip((tick - start) / steps, 0.0, 1.0)
    else:
        sequence = state["excitation_sequence"]
        cycle, within = divmod(tick, steps)
        if cycle == len(sequence) and within == 0:
            return sequence[-1, -1].copy()
        if cycle >= len(sequence):
            # Stop and explain the invalid model setting or failed calculation.
            raise ValueError(
                "Frozen muscle_excitation sequence exhausted; no untested repetition is allowed"
            )
        table = sequence[cycle]
        phase = within / steps
    position = phase * (len(table) - 1)
    lo = min(int(position), len(table) - 2)
    weight = position - lo
    return np.clip((1 - weight) * table[lo] + weight * table[lo + 1], 0.0, 1.0)
