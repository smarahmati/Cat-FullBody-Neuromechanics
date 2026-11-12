"""Read the intact muscle excitation table using simulation time.

Input: time in seconds and a table with values between 0 and 1. Output: one
excitation per muscle-tendon path. Joint angles and forces do not alter it.
"""

import numpy as np

from .periodic_interpolate import periodic_interpolate



def muscle_excitation(state, time_s):
    """Calculate every muscle's prescribed excitation at this time."""
    # Fixed finite sequences use their specified time index.
    if "excitation_sequence" in state or "offline_cycle_input" in state:
        from .fixed_sequence_excitation import fixed_sequence_excitation

        original_excitation = fixed_sequence_excitation(state, time_s)
    else:
        # Find how far time has progressed through the input cycle.
        cycle_fraction = time_s / state["settings"]["period_s"]
        # Interpolate neighboring rows of the repeated excitation table.
        original_excitation = periodic_interpolate(
            state["excitation_table"],
            cycle_fraction,
        )
        # Keep excitation inside the defined 0-to-1 range.
        original_excitation = np.clip(original_excitation, 0.0, 1.0)
    # The prescribed input is independent of the resulting motion and forces.
    return original_excitation
