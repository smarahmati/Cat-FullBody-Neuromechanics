"""Complete-cycle muscle_excitation/EMG pairs, with unchanged source clocks."""

import json

import numpy as np

from model_configuration.paths import ROOT

from .experimental_comparison_targets import experimental_comparison_targets

from .load_reference_tables import load_reference_tables

from .periodic_interpolate import periodic_interpolate


def emg_comparison_cycles(names, settings, samples=2048):
    """Return measured/pooled/assumed channels only; no inferred EMG targets."""
    names = list(names)
    phase = np.arange(samples) / samples
    T = settings["period_s"]
    target = experimental_comparison_targets(
        phase * T,
        T,
        settings.get("reference_table_dir"),
    )["excitation"]
    if settings.get("excitation_table_file"):
        from .read_time_series import read_time_series

        table = read_time_series(ROOT / settings["excitation_table_file"], names)[2]
    elif "excitation_control_points" in settings:
        table = np.asarray(settings["excitation_control_points"])
    elif settings.get("excitation_file"):
        table = np.load(ROOT / settings["excitation_file"])["excitation_table"]
    else:
        folder = (
            ROOT / "Data/Skeletal_Geometry/Model"
            if settings.get("model_variant", "base") == "base"
            else ROOT / "Data/Skeletal_Geometry/Model" / settings["model_variant"]
        )
        table = np.load(folder / "muscle_parameters.npz")["excitation_table"]
    provenance = json.loads((ROOT / "Data/Experimental_Reference_Data/INPUT_PROVENANCE.json").read_text())[
        "channels"
    ]
    pairs = []
    for side, prefix in enumerate(["L", "R", "FL", "FR"]):
        for item in provenance:
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
            column = (
                (
                    (22 if side == 2 else 31)
                    + [c["channel"] for c in provenance[11:]].index(item["channel"])
                )
                if fore
                else (
                    (0 if side == 0 else 11)
                    + [c["channel"] for c in provenance[:11]].index(item["channel"])
                )
            )
            i = names.index(name)
            pred = np.interp(phase, np.linspace(0, 1, len(table)), table[:, i]) / max(
                0.02,
                float(table[:, i].max()),
            )
            ref = target[:, column] / max(1e-12, float(target[:, column].max()))
            pairs.append(
                dict(
                    channel=name,
                    limb=prefix,
                    kind=item["kind"] if side else "assumed_LH_from_recorded_RH",
                    excitation=pred,
                    reference=ref,
                )
            )
    fhl = load_reference_tables(settings.get("reference_table_dir"))[2]
    for side, prefix in enumerate(["L", "R"]):
        name = prefix + "_FHL"
        if name not in names:
            # Skip the remaining work for this item.
            continue
        i = names.index(name)
        pred = np.interp(phase, np.linspace(0, 1, len(table)), table[:, i]) / max(
            0.02,
            float(table[:, i].max()),
        )
        ref = np.array([periodic_interpolate(fhl, p + 0.5 + [0.5, 0][side]) for p in phase])
        ref /= max(1e-12, float(ref.max()))
        pairs.append(
            dict(
                channel=name,
                limb=prefix,
                kind="recorded_RH_EMG" if side else "assumed_LH_from_recorded_RH",
                excitation=pred,
                reference=ref,
            )
        )
    return pairs
