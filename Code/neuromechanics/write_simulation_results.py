"""Write simulation results.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import json, html, os

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from .experimental_comparison_targets import experimental_comparison_targets

from .compare_simulation_with_experiment import compare_simulation_with_experiment

from .plot_emg_comparison import plot_emg_comparison

from model_configuration.paths import ROOT


def write_simulation_results(result, settings, folder):
    """Compare raw predictions on the source clock, with readable time windows."""
    metrics = compare_simulation_with_experiment(result, settings)
    # Save the computed values or figure for inspection and reproducibility.
    (folder / "experimental_comparison_metrics.json").write_text(json.dumps(metrics, indent=2))
    target = experimental_comparison_targets(
        result["time"],
        settings["period_s"],
        settings.get("reference_table_dir"),
    )
    # Plot a short interval for waveform detail; metrics still use the full trial.
    window_end = float(result["time"][-1])
    window_start = max(float(result["time"][0]), window_end - 4.0)
    names = [["Hip", "Knee", "Ankle", "MTP"]] * 2 + [
        ["Shoulder", "Elbow", "Wrist", "MCP"]
    ] * 2
    limbs = ["LH (assumed)", "RH (measured)", "LF (separate study)", "RF (separate study)"]
    fig, ax = plt.subplots(4, 4, figsize=(15, 10), sharex=True)
    for side in range(4):
        signs = np.array([-1, 1, -1, -1]) if side < 2 else np.array([1, -1, -1, -1])
        offset = np.array([0, np.pi, np.pi, np.pi]) if side < 2 else np.full(4, np.pi)
        for j in range(4):
            a = ax[side, j]
            a.plot(
                result["time"],
                np.rad2deg(offset[j] + signs[j] * target["joint_q"][:, side, j]),
                "k--",
                label="Source reference",
            )
            a.plot(
                result["time"],
                np.rad2deg(offset[j] + signs[j] * result["joint_q"][:, side, j]),
                color="#087f9c",
                label="Forward result",
            )
            a.set_title(
                f'{limbs[side]} {names[side][j]}\nRMSE {metrics["limbs"][side]["joint_rmse_deg"][j]:.1f}°',
                fontsize=10,
            )
            a.grid(alpha=0.2)
            a.set_xlim(window_start, window_end)
        ax[side, 0].set_ylabel("Anatomical angle (deg)")
    ax[0, 0].legend(fontsize=8)
    [a.set_xlabel("Time (s)") for a in ax[-1]]
    fig.suptitle(f"Joint angles · {window_start:.2f}–{window_end:.2f} s\nRMSE labels use the complete trial; explore any interval in the interactive comparison", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, .94))
    # Save the computed values or figure for inspection and reproducibility.
    fig.savefig(folder / "all_joint_angles.png", dpi=140)
    plt.close(fig)
    fig, ax = plt.subplots(4, 2, figsize=(12, 10), sharex=True)
    for side in range(4):
        for col, index in enumerate([0, 2]):
            a = ax[side, col]
            a.plot(
                result["time"],
                target["grf"][:, side, index],
                "k--",
                label="Source reference",
            )
            a.plot(
                result["time"],
                result["grf"][:, side, index],
                color="#087f9c",
                label="Raw contact prediction",
            )
            a.set_title(limbs[side] + (" anterior–posterior (AP)" if col == 0 else " vertical"))
            a.set_ylabel("Force (N)")
            a.grid(alpha=0.2)
            a.set_xlim(window_start, window_end)
    ax[0, 0].legend(fontsize=8)
    [a.set_xlabel("Time (s)") for a in ax[-1]]
    fig.suptitle(f"Raw paw contact forces · {window_start:.2f}–{window_end:.2f} s", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, .95))
    # Save the computed values or figure for inspection and reproducibility.
    fig.savefig(folder / "all_grfs.png", dpi=140)
    plt.close(fig)
    rows = "".join(
        "<tr><td>"
        + html.escape(m["limb"])
        + "</td><td>"
        + ", ".join(f"{x:.2f}" for x in m["joint_rmse_deg"])
        + f'</td><td>{m["ap_grf_rmse_N"]:.2f}</td><td>{m["vertical_grf_rmse_N"]:.2f}</td></tr>'
        for m in metrics["limbs"]
    )
    content = f"""<!doctype html><meta charset="utf-8"><title>Four-limb forward fit</title><style>body{{max-width:1200px;margin:35px auto;font:17px/1.5 Arial;color:#19313e}}img{{width:100%}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #bbc;padding:8px}}.status{{background:#fff2d7;padding:15px}}</style><h1>Four-limb forward model: current trial</h1><p class="status">Duration: {metrics['duration_s']:.3f} s. Failure: {html.escape(metrics['failure'] or 'none detected within this run')}. This trial does not establish the requested 60-second fit unless the separate validation tests pass.</p><p>The four limbs are mechanically coupled. Excitation drives activation, elastic muscle–tendon forces and native articulated dynamics. Ground_Reaction_Forces come from physical paw contact. Raw reference curves and raw forward outputs use the same clock.</p><table><tr><th>Limb and data basis</th><th>Joint RMSE (degrees, proximal to distal)</th><th>AP GRF RMSE (N)</th><th>Vertical GRF RMSE (N)</th></tr>{rows}</table><p>LH is assumed from RH. Forelimb recordings are from a separate study; EMGs are pooled across sides. These are fitting targets, not simultaneous four-limb validation.</p><img src="all_joint_angles.png"><img src="all_grfs.png"><p><a href="experimental_comparison_metrics.json">All metrics, including each EMG channel</a> · <a href="settings.json">Applied parameters</a> · <a href="../../Documentation/model_methods.html">Equations, sources and assumptions</a></p>"""
    emg_files = plot_emg_comparison(result, settings, folder)
    # Browser navigation exposes the complete recording without crowding 60 s.
    from .write_interactive_comparison import write_interactive_comparison
    write_interactive_comparison(result, settings, folder)
    content = content.replace("Ground_Reaction_Forces", "GRFs")
    content = content.replace("Four-limb forward model: current trial", "Intact-cat forward simulation")
    content = content.replace("This trial does not establish the requested 60-second fit unless the separate validation tests pass.", "Duration alone does not establish complete experimental agreement or stability beyond the simulated interval.")
    content = content.replace("<table>", '<p style="padding:16px;background:#e6f5f3"><a href="interactive_experimental_comparison.html"><b>Explore all time points: movable four-second window, joint angles and GRFs</b></a></p><p>Static figures show the final four seconds. The table and plot-title RMSE values use the complete saved trial, without phase shifting.</p><table>', 1)
    if settings.get("excitation_sequence_file"):
        note = '<p class="status"><b>Finite, frozen muscle_excitation sequence.</b> Amplitudes were optimized offline across successive strides. The replay uses elapsed time only, with one initial state and no runtime corrections. This is not a demonstration of an autonomously stable periodic gait, and no repetition beyond the saved sequence is assumed.</p>'
        content = content.replace("<table>", note + "<table>", 1)
    gallery = "<h2>Excitation shapes compared with available EMG</h2>" + "".join(
        f'<img src="{name}" alt="Separate limb muscle_excitation and EMG comparison">'
        for name in emg_files
    )
    content = content.replace(
        '<p><a href="experimental_comparison_metrics.json">',
        gallery + '<p><a href="experimental_comparison_metrics.json">',
    )
    doc_link = os.path.relpath(ROOT / "Documentation/model_methods.html", folder).replace(os.sep, "/")
    content = content.replace("../../Documentation/model_methods.html", doc_link)
    if (folder / "APPLIED_PARAMETERS.html").exists():
        content += '<p><a href="APPLIED_PARAMETERS.html">Actual applied parameter table</a> · <a href="APPLIED_PARAMETERS.json">Machine-readable values</a> · <a href="INPUT_HASHES.json">Frozen config/reference hashes</a> · <a href="walking_quality_metrics.json">Walking acceptance checks</a></p>'
    if (folder / "ATTACHMENT_MAP.html").exists():
        content += '<p><a href="ATTACHMENT_MAP.html">Actual muscle origins, insertions, via points and wrapping</a> · <a href="ATTACHMENT_MAP.json">Connection and coordinate data</a></p>'
    # Save the computed values or figure for inspection and reproducibility.
    (folder / "simulation_report.html").write_text(content, encoding="utf-8")
    return metrics
