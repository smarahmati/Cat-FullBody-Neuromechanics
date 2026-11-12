"""Score all four limbs separately against unchanged source time series."""

import json

import numpy as np

from model_configuration.paths import ROOT

from .experimental_comparison_targets import experimental_comparison_targets

from .load_reference_tables import load_reference_tables

from .periodic_interpolate import periodic_interpolate

from .emg_comparison_cycles import emg_comparison_cycles

from .emg_phase_metrics import emg_phase_metrics

from .configured_excitation_samples import configured_excitation_samples

from .emg_input_timing_scores import emg_input_timing_scores


def compare_simulation_with_experiment(result, settings):
    t = result["time"]
    target = experimental_comparison_targets(
        t,
        settings["period_s"],
        settings.get("reference_table_dir"),
    )
    u = result["excitation"]
    names = list(result["names"])
    full_target = experimental_comparison_targets(
        np.linspace(0, settings["period_s"], 801),
        settings["period_s"],
        settings.get("reference_table_dir"),
    )["excitation"]
    full_input = configured_excitation_samples(settings, u)
    joint = np.sqrt(np.mean(np.rad2deg(result["joint_q"] - target["joint_q"]) ** 2, axis=0))
    force = np.sqrt(np.mean((result["grf"] - target["grf"]) ** 2, axis=0))
    provenance = json.loads((ROOT / "Data/Experimental_Reference_Data/INPUT_PROVENANCE.json").read_text())
    emg = []
    for side, prefix in enumerate(["L", "R", "FL", "FR"]):
        for item in provenance["channels"]:
            if "EMG" not in item["kind"]:
                # Skip the remaining work for this item.
                continue
            fore = item["kind"].startswith("pooled_fore")
            if fore != (side >= 2):
                # Skip the remaining work for this item.
                continue
            name = prefix + "_" + item["channel"]
            if name not in names:
                # Skip the remaining work for this item.
                continue
            i = names.index(name)
            source_index = (
                (22 if side == 2 else 31)
                + [c["channel"] for c in provenance["channels"][11:]].index(item["channel"])
                if fore
                else (0 if side == 0 else 11)
                + [c["channel"] for c in provenance["channels"][:11]].index(item["channel"])
            )
            ref = target["excitation"][:, source_index]
            shape = ref / max(1e-12, float(full_target[:, source_index].max()))
            pred = u[:, i] / max(0.02, float(full_input[:, i].max()))
            corr = (
                float(np.corrcoef(pred, shape)[0, 1])
                if np.std(pred) > 1e-9 and np.std(shape) > 1e-9
                else 0.0
            )
            emg.append(
                dict(
                    channel=name,
                    kind=item["kind"] if side != 0 else "assumed_LH_from_recorded_RH",
                    peak_normalized_rmse=float(np.sqrt(np.mean((pred - shape) ** 2))),
                    correlation=corr,
                )
            )
    extra = load_reference_tables(settings.get("reference_table_dir"))[2]
    for side, prefix in enumerate(["L", "R"]):
        i = names.index(prefix + "_FHL")
        shape = np.array(
            [
                periodic_interpolate(
                    extra,
                    time / settings["period_s"] + 0.5 + [0.5, 0][side],
                )
                for time in t
            ]
        )
        pred = u[:, i] / max(0.02, float(full_input[:, i].max()))
        emg.append(
            dict(
                channel=prefix + "_FHL",
                kind="recorded_RH_EMG" if side else "assumed_LH_from_recorded_RH",
                peak_normalized_rmse=float(np.sqrt(np.mean((pred - shape) ** 2))),
                correlation=(
                    float(np.corrcoef(pred, shape)[0, 1])
                    if np.std(pred) > 1e-9
                    else 0.0
                ),
            )
        )
    scope = [
        "LH: assumed mirror",
        "RH: measured Ted_046",
        "LF: separate-study mean; pooled EMG",
        "RF: separate-study mean; pooled EMG",
    ]
    phase_scores = emg_input_timing_scores(names, settings)
    for item in emg:
        item["complete_input_cycle_timing"] = phase_scores[item["channel"]]
    return dict(
        duration_s=float(t[-1]),
        failure=str(result["failure"]),
        limbs=[
            dict(
                limb=label,
                joint_rmse_deg=joint[i].tolist(),
                ap_grf_rmse_N=float(force[i, 0]),
                vertical_grf_rmse_N=float(force[i, 2]),
            )
            for i, label in enumerate(scope)
        ],
        emg=emg,
        completed_60s_without_detected_fall=bool(
            t[-1] >= 59.99
            and not str(result["failure"])
        ),
        walking_acceptance_requires_separate_gates=True,
        calibration_to_assembled_source_references=True,
        EMG_peak_normalization=(
            "Complete configured input sequence, one fixed peak per muscle"
            if settings.get("excitation_sequence_file")
            else "Complete configured input cycle, not the displayed interval"
        ),
        EMG_timing_scope="Prescribed full-cycle intact input, normalized to intact input peaks; not a claim that the trial completed that cycle. Whole-trial shape RMSE uses the actual saved excitation.",
        independent_four_limb_validation=False,
    )
