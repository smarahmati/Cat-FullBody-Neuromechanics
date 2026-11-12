"""Plot available EMG envelopes separately for every limb, with provenance."""

import json

import numpy as np

import matplotlib.pyplot as plt

from model_configuration.paths import ROOT

from .experimental_comparison_targets import experimental_comparison_targets

from .load_reference_tables import load_reference_tables

from .periodic_interpolate import periodic_interpolate

from .configured_excitation_samples import configured_excitation_samples


def plot_emg_comparison(result, settings, folder):
    t = result["time"]
    T = settings["period_s"]
    target = experimental_comparison_targets(t, T, settings.get("reference_table_dir"))
    full = experimental_comparison_targets(
        np.linspace(0, T, 801),
        T,
        settings.get("reference_table_dir"),
    )["excitation"]
    provenance = json.loads((ROOT / "Data/Experimental_Reference_Data/INPUT_PROVENANCE.json").read_text())[
        "channels"
    ]
    names = list(result["names"])
    u = result["excitation"]
    table = configured_excitation_samples(settings, u)
    interval = "sequence" if settings.get("excitation_sequence_file") else "cycle"
    fhl = load_reference_tables(settings.get("reference_table_dir"))[2]
    files = []
    for side, prefix in enumerate(["L", "R", "FL", "FR"]):
        curves = []
        for index, item in enumerate(provenance):
            if "EMG" not in item["kind"] or item["kind"].startswith("pooled_fore") != (
                side
                >= 2
            ):
                # Skip the remaining work for this item.
                continue
            name = prefix + "_" + item["channel"]
            if name not in names:
                # Skip the remaining work for this item.
                continue
            column = (
                (22 if side == 2 else 31) + index - 11
                if side >= 2
                else (0 if side == 0 else 11) + index
            )
            curves.append(
                (
                    name,
                    target["excitation"][:, column]
                    / max(1e-12, float(full[:, column].max())),
                )
            )
        if side < 2:
            curves.append(
                (
                    prefix + "_FHL",
                    np.array(
                        [periodic_interpolate(fhl, x / T + 0.5 + [0.5, 0][side]) for x in t]
                    ),
                )
            )
        fig, axes = plt.subplots(2, 4, figsize=(13, 6), sharex=True, sharey=True)
        for ax, (name, ref) in zip(axes.ravel(), curves):
            i = names.index(name)
            peak = max(0.02, float(table[:, i].max()))
            ax.plot(t, ref, "k--", label="EMG shape reference")
            ax.plot(
                t,
                u[:, i] / peak,
                color="#087f9c",
                label="Excitation / " + interval + " peak",
            )
            ax.set_title(f"{name}\nexcitation peak {peak:.3f}", fontsize=10)
            ax.grid(alpha=0.2)
            ax.set_ylim(-0.05, 1.1)
        for ax in axes[-1]:
            ax.set_xlabel("Time (s)")
        for ax in axes[:, 0]:
            ax.set_ylabel("Normalized envelope")
        axes[0, 0].legend(fontsize=8)
        label = [
            "LH: assumed mirror of RH EMG",
            "RH: measured EMG envelopes",
            "LF: pooled forelimb EMGs",
            "RF: pooled forelimb EMGs",
        ][side]
        fig.suptitle(
            label
            + "; fixed input clock, no phase shift to improve the fit\nNormalization uses the complete input "
            + interval
            + "; EMG does not identify absolute muscle_excitation amplitude.",
            fontsize=11,
        )
        fig.tight_layout()
        filename = f"emg_{prefix}.png"
        # Save the computed values or figure for inspection and reproducibility.
        fig.savefig(folder / filename, dpi=140)
        plt.close(fig)
        files.append(filename)
    return files
