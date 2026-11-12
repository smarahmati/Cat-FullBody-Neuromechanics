"""Score every saved stride; never score only the baseline of a varied sequence."""

import numpy as np

from model_configuration.paths import ROOT

from .emg_comparison_cycles import emg_comparison_cycles

from .emg_phase_metrics import emg_phase_metrics


def emg_input_timing_scores(names, settings):
    pairs = emg_comparison_cycles(names, settings)
    T = settings["period_s"]
    threshold = settings.get("emg_phase_threshold", 0.10)
    if not settings.get("excitation_sequence_file"):
        return {
            p["channel"]: emg_phase_metrics(p["excitation"], p["reference"], T, threshold)
            for p in pairs
        }
    sequence = np.load(ROOT / settings["excitation_sequence_file"])["excitation_sequence"]
    names = list(names)
    peaks = np.maximum(0.02, sequence.max(axis=(0, 1)))
    scores = {}
    for pair in pairs:
        index = names.index(pair["channel"])
        phase = np.arange(len(pair["reference"])) / len(pair["reference"])
        rows = [
            emg_phase_metrics(
                np.interp(phase, np.linspace(0, 1, len(table)), table[:, index])
                # Use the intact peak so attenuation is still visible in the score.
                / peaks[index]
,
                pair["reference"],
                T,
                threshold,
            )
            for table in sequence
        ]
        summary = dict(rows[0])
        summary["active_intersection_over_union"] = min(
            r["active_intersection_over_union"]
            for r in rows
        )
        for key in [
            "phase_disagreement_fraction",
            "false_active_fraction_of_cycle",
            "missed_active_fraction_of_cycle",
        ]:
            summary[key] = max(r[key] for r in rows)
        for edge in ["onset", "offset"]:
            summary[edge] = {}
            for key in rows[0][edge]:
                values = [r[edge][key] for r in rows if r[edge][key] is not None]
                summary[edge][key] = max(values) if values else None
        for key in ["active_fraction_predicted", "predicted_burst_count"]:
            if key in rows[0]:
                values = [r[key] for r in rows]
                summary[key + "_range"] = [min(values), max(values)]
                summary[key] = max(values)
        summary.update(
            scope="Worst timing agreement across every saved input stride; fixed whole-sequence peak normalization",
            per_stride=rows,
        )
        scores[pair["channel"]] = summary
    return scores
