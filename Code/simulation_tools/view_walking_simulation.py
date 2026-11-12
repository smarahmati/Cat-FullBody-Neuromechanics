"""Inspect an already computed forward run; never solve or alter its motion.

The MuJoCo window displays saved mechanical states. The companion window
shows corresponding saved excitations, activations and raw contact forces.
Changing playback speed, time or plot selection does not change the model.
"""

import argparse

import json

import os

from pathlib import Path

import sys

import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Code"))
# Read the saved bundle before importing numerical helpers. This keeps a viewer
# consistent even if the editable default constants changed after the trial.
_selected_run = "Intact_Walking"
if "--run" in sys.argv:
    _selected_run = sys.argv[sys.argv.index("--run") + 1]
_saved_folder = Path(_selected_run)
if not _saved_folder.is_absolute():
    _saved_folder = ROOT / _saved_folder if (ROOT / _saved_folder).is_dir() else ROOT / "Simulation_Results" / _saved_folder
if (_saved_folder / "settings.json").exists():
    _saved_settings = json.loads((_saved_folder / "settings.json").read_text())
    os.environ["CAT_PARAMETER_FOLDER"] = str(ROOT / _saved_settings.get("parameter_bundle_dir", "Data/Model_Parameters"))
import numpy as np

import mujoco as mj

import mujoco.viewer

import tkinter as tk

from tkinter import ttk

from neuromechanics.initialize_neuromechanical_model import initialize_neuromechanical_model

from neuromechanics.experimental_comparison_targets import experimental_comparison_targets

from neuromechanics.emg_comparison_cycles import emg_comparison_cycles

from neuromechanics.configured_excitation_samples import configured_excitation_samples

from neuromechanics.simulation_comparison_plots import ReplayPlotPanel

from neuromechanics.simulation_playback_worker import SavedReplayWorker


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", default="Intact_Walking")
    parser.add_argument(
        "--autoplay",
        action="store_true",
        help="Start playback immediately",
    )
    parser.add_argument("--start-time", type=float, default=0.0)
    parser.add_argument("--fps", type=int, choices=[30, 60, 90], default=60)
    parser.add_argument("--profile-seconds", type=float, default=12.0)
    args = parser.parse_args()
    folder = Path(args.run)
    if not folder.is_absolute():
        folder = (ROOT / folder) if (ROOT / folder).is_dir() else (ROOT / "Simulation_Results" / folder)
    result = dict(np.load(folder / "forward_simulation_timeseries.npz"))
    cfg = json.loads((folder / "settings.json").read_text())
    times = result["time"]
    names = list(result["names"])
    print("Loading saved forward model and visual meshes...", flush=True)
    state = initialize_neuromechanical_model(cfg, graphics=True)
    model, data = state["model"], state["data"]
    target = experimental_comparison_targets(
        times,
        cfg["period_s"],
        cfg.get("reference_table_dir"),
    )
    pairs = {p["channel"]: p for p in emg_comparison_cycles(names, cfg)}
    peaks = np.maximum(0.02, configured_excitation_samples(cfg).max(axis=0))
    root = tk.Tk()
    # Identify the four-second plot window and the selected computed trial.
    root.title("Cat forward simulation (4-second window) - " + folder.name)
    root.geometry("920x850+30+60")
    root.minsize(760, 680)
    paused = tk.BooleanVar(value=not args.autoplay)
    speed = tk.StringVar(value="0.5")
    limb = tk.StringVar(value="RH")
    muscle = tk.StringVar(value="R_VL")
    joint = tk.StringVar(value="Ankle")
    norm = tk.BooleanVar(value=True)
    emg = tk.BooleanVar(value=True)
    position = tk.DoubleVar(value=args.start_time)
    fps = tk.StringVar(value=str(args.fps))
    forces = tk.BooleanVar(value=True)
    rich = tk.BooleanVar(value=False)
    follow = tk.BooleanVar(value=True)
    worker = None
    updating_slider = False
    # Do not move the timeline thumb automatically while the user is dragging it.
    dragging_slider = False

    def set_time(value):
        """Pause at any recorded time; this works before or after the trial ends."""
        # Convert text or button input into seconds.
        requested_time = float(value)
        # Reject invalid numbers before they can reach the playback worker.
        if not np.isfinite(requested_time):
            # Explain how to correct an invalid Go-to-time entry.
            raise ValueError("Enter a finite time in seconds.")
        # Keep the requested position within the saved trial.
        requested_time = float(np.clip(requested_time, 0.0, times[-1]))
        # Hold the chosen frame so the user can inspect its curves and pose.
        paused.set(True)
        # Move the full-trial timeline to the same recorded instant.
        position.set(requested_time)
        if worker is not None:
            # Seeking changes playback only; it does not calculate a new trial.
            worker.command(paused=True, seek=requested_time)

    def slider_seek(value):
        if not updating_slider and worker is not None:
            # Pause and inspect the frame selected anywhere on the full timeline.
            set_time(value)

    # Mark the beginning of mouse dragging on the full-trial timeline.
    def start_timeline_drag(event):
        # Update the flag shared with the periodic refresh callback.
        nonlocal dragging_slider
        # Keep automatic playback updates from moving the thumb under the mouse.
        dragging_slider = True
        # Hold motion while browsing the recording.
        paused.set(True)

    # Finish a timeline drag without losing the author's selected time.
    def finish_timeline_drag(event):
        # Update the flag shared with the periodic refresh callback.
        nonlocal dragging_slider
        # Send the final thumb position to the 3D viewer and plots.
        set_time(position.get())
        # Allow subsequent programmatic timeline updates again.
        dragging_slider = False

    def reset_playback():
        """Return to the archived initial state without changing model parameters."""
        paused.set(True)
        if worker is not None:
            worker.command(paused=True, seek=float(times[0]))
        position.set(float(times[0]))

    status = tk.StringVar(
        value="Ready - press Play. Recorded forward result, not live reintegration."
    )
    ttk.Label(
        root,
        text="Forward result | prescribed excitation | elastic muscle–tendon mechanics | raw Ground_Reaction_Forces",
        font=("Segoe UI", 11, "bold"),
    ).pack(padx=10, pady=(10, 3))
    # Read this trial's actual outcome; an altered-input trial may have fallen.
    summary = json.loads((folder / "simulation_summary.json").read_text())
    # Report a detected fall or limit the survival claim to the saved duration.
    outcome = summary.get("failure") or f"No detected fall during {times[-1]:.2f} seconds."
    # Display the outcome beside a short reminder of the model's validation limits.
    ttk.Label(
        root,
        text=outcome + " EMG timing and forepaw fit remain imperfect.",
    ).pack()
    controls = ttk.Frame(root)
    controls.pack(fill="x", padx=10, pady=7)
    ttk.Checkbutton(controls, text="Paused", variable=paused).pack(side="left")
    ttk.Button(
        controls,
        text="Play / Pause",
        command=lambda: paused.set(not paused.get()),
    ).pack(side="left")
    ttk.Label(controls, text="  Speed ").pack(side="left")
    ttk.Combobox(
        controls,
        textvariable=speed,
        values=["0.1", "0.25", "0.5", "1", "2"],
        state="readonly",
        width=5,
    ).pack(side="left")
    ttk.Button(controls, text="Reset", command=reset_playback).pack(side="left", padx=8)
    ttk.Button(
        controls,
        text="Last 4 seconds",
        command=lambda: set_time(max(0.0, float(times[-1]) - 2.0)),
    ).pack(side="left")
    ttk.Label(controls, text="  3D target Hz ").pack(side="left")
    ttk.Combobox(
        controls,
        textvariable=fps,
        values=["30", "60", "90"],
        state="readonly",
        width=4,
    ).pack(side="left")
    selectors = ttk.Frame(root)
    selectors.pack(fill="x", padx=10)
    limb_box = ttk.Combobox(
        selectors,
        textvariable=limb,
        values=["LH", "RH", "LF", "RF"],
        state="readonly",
        width=5,
    )
    limb_box.pack(side="left")
    muscle_box = ttk.Combobox(selectors, textvariable=muscle, state="readonly", width=32)
    muscle_box.pack(side="left", padx=6)
    joint_box = ttk.Combobox(selectors, textvariable=joint, state="readonly", width=12)
    joint_box.pack(side="left")
    prefixes = ["L", "R", "FL", "FR"]

    def select_limb(event=None):
        side = ["LH", "RH", "LF", "RF"].index(limb.get())
        choices = [n for n in names if n.startswith(prefixes[side] + "_")]
        muscle_box["values"] = choices
        if muscle.get() not in choices:
            muscle.set(choices[0])
        joints = (
            ["Hip", "Knee", "Ankle", "MTP"]
            if side < 2
            else ["Shoulder", "Elbow", "Wrist", "MCP"]
        )
        joint_box["values"] = joints
        if joint.get() not in joints:
            joint.set(joints[0])

    limb_box.bind("<<ComboboxSelected>>", select_limb)
    select_limb()
    options = ttk.Frame(root)
    options.pack(fill="x", padx=10, pady=5)
    ttk.Checkbutton(
        options,
        text="Normalize activation/muscle_excitation to fixed input peak",
        variable=norm,
    ).pack(side="left")
    ttk.Checkbutton(options, text="Show available EMG", variable=emg).pack(
        side="left",
        padx=10,
    )
    display = ttk.Frame(root)
    display.pack(fill="x", padx=10)
    ttk.Checkbutton(display, text="Paw GRF vectors", variable=forces).pack(side="left")
    ttk.Checkbutton(display, text="Shadows / reflections (slower)", variable=rich).pack(
        side="left",
        padx=10,
    )
    ttk.Checkbutton(display, text="Follow body", variable=follow).pack(side="left")
    # Put explicit time-navigation controls above the full-trial slider.
    navigation = ttk.Frame(root)
    # Give the navigation row the available window width.
    navigation.pack(fill="x", padx=10, pady=5)
    # Identify the editable time as actual elapsed simulation seconds.
    ttk.Label(navigation, text="Go to time (s): ").pack(side="left")
    # Keep typed text independent of the moving playback thumb.
    requested_time_text = tk.StringVar(value="0.0")
    # Allow the user to type any time within the recorded trial.
    time_entry = ttk.Entry(navigation, textvariable=requested_time_text, width=9)
    # Place the entry beside its label.
    time_entry.pack(side="left")

    # Apply the time typed in the entry box.
    def jump_to_time():
        # Validate text before sending it to the playback worker.
        try:
            # Pause both motion and plots at the requested instant.
            set_time(requested_time_text.get())
        # Report invalid text without closing the simulation viewer.
        except ValueError:
            # Explain the allowed time range in the existing status area.
            status.set(f"Enter a time between 0 and {times[-1]:.2f} seconds.")
            # Draw attention to the entry without opening another dialog.
            root.bell()

    # Apply a typed time either with Enter or with the Go button.
    time_entry.bind("<Return>", lambda event: jump_to_time())
    # Provide an explicit action for the typed time.
    ttk.Button(navigation, text="Go", command=jump_to_time).pack(side="left", padx=5)
    ttk.Button(navigation, text="Start", command=lambda: set_time(0.0)).pack(side="left")
    # Inspect the middle of the complete recording.
    ttk.Button(navigation, text="Middle", command=lambda: set_time(float(times[-1]) / 2.0)).pack(side="left")
    # Inspect the final recorded frame while keeping browsing controls enabled.
    ttk.Button(navigation, text="End", command=lambda: set_time(float(times[-1]))).pack(side="left")
    # Move backward by one visible plot window.
    ttk.Button(navigation, text="-4 s", command=lambda: set_time(position.get() - 4.0)).pack(side="left", padx=(8, 0))
    # Move forward by one visible plot window.
    ttk.Button(navigation, text="+4 s", command=lambda: set_time(position.get() + 4.0)).pack(side="left")
    # Explain that the slider browses the entire saved trial, not just four seconds.
    ttk.Label(root, text=f"Browse full trial: 0 to {times[-1]:.2f} s. Drag the slider; plots show a 4-second window.").pack()
    # Keep the timeline available throughout playback and after reaching the end.
    timeline = ttk.Scale(
        root,
        variable=position,
        command=slider_seek,
        from_=0.0,
        to=float(times[-1]),
    )
    # Stretch the timeline across the control window.
    timeline.pack(fill="x", padx=15)
    # Protect the selected time from refresh updates during mouse dragging.
    timeline.bind("<ButtonPress-1>", start_timeline_drag)
    # Apply the final selected position when the mouse is released.
    timeline.bind("<ButtonRelease-1>", finish_timeline_drag)
    ttk.Label(root, textvariable=status, wraplength=870).pack(padx=10, pady=4)
    force_text = tk.StringVar(value="Paw vectors: LH cyan | RH pink | LF gold | RF purple")
    ttk.Label(root, textvariable=force_text).pack(pady=2)
    panel = ReplayPlotPanel(root, result, target, pairs, peaks, cfg["period_s"])

    # A click on any visible plot can select the matching time and 3D pose.
    def select_plot_time(event):
        # Only a left click within a plotted time axis should seek playback.
        if event.button == 1 and event.inaxes is not None and event.xdata is not None:
            # All plots use actual simulation seconds, so no time conversion is needed.
            set_time(event.xdata)

    # Connect plot clicks to the same time-selection logic as the timeline.
    panel.canvas.mpl_connect("button_press_event", select_plot_time)
    ttk.Label(
        root,
        text="Muscle colors are fixed identifiers: blue = SAM/SRTm; orange = VL; purple = added toe/girdle paths; red = others.",
    ).pack(pady=(4, 0))
    ttk.Label(
        root,
        text="Dashed black: reference. Blue: prediction. RH recorded; LH mirrored; fore references from a separate study.",
    ).pack(pady=(0, 4))
    viewer = mj.viewer.launch_passive(model, data, show_left_ui=False, show_right_ui=False)
    # Keep this file or shared state safely scoped to the following operations.
    with viewer.lock():
        viewer.cam.distance = 0.95
        viewer.cam.azimuth = 90
        viewer.cam.elevation = -18
        viewer.cam.lookat[:] = data.xpos[model.body("pelvis").id]
        viewer.cam.lookat[0] += 0.12
        viewer.cam.lookat[2] *= 0.72
    profile = folder / "gui" / ("PERFORMANCE_" + time.strftime("%Y%m%d_%H%M%S") + ".json")
    worker = SavedReplayWorker(viewer, state, result, profile, args.profile_seconds)
    worker.command(paused=paused.get(), fps=float(fps.get()), seek=args.start_time)
    worker.start()
    last_status = 0.0
    closed = False

    def close():
        # Use the surrounding GUI or module state rather than creating a new local variable.
        nonlocal closed
        closed = True
        worker.stop()
        viewer.close()
        root.destroy()

    def refresh():
        # Use the surrounding GUI or module state rather than creating a new local variable.
        nonlocal last_status, updating_slider
        if closed:
            return
        if not viewer.is_running():
            close()
            return
        started = time.perf_counter()
        snapshot = worker.snapshot()
        current = snapshot["time"]
        if snapshot["error"]:
            paused.set(True)
            status.set("Viewer error: " + snapshot["error"])
            return
        if current >= times[-1]:
            paused.set(True)
        worker.command(
            paused=paused.get(),
            speed=float(speed.get()),
            fps=float(fps.get()),
            forces=forces.get(),
            rich=rich.get(),
            follow=follow.get(),
        )
        side = ["LH", "RH", "LF", "RF"].index(limb.get())
        joints = (
            ["Hip", "Knee", "Ankle", "MTP"]
            if side < 2
            else ["Shoulder", "Elbow", "Wrist", "MCP"]
        )
        panel.update(
            current,
            side,
            muscle.get(),
            joints.index(joint.get()),
            norm.get(),
            emg.get(),
        )
        if started - last_status > 0.2:
            last_status = started
            updating_slider = True
            # Preserve the thumb position while the user drags to another time.
            if not dragging_slider:
                # Keep the timeline synchronized with ordinary playback.
                position.set(current)
            updating_slider = False
            status.set(
                f'{"PAUSED" if paused.get() else "PLAYING"} | {current:.2f} / {times[-1]:.2f} s | {speed.get()}x | 3D updates: {snapshot["update_hz"]:.1f}/s (target {fps.get()}) | plots: {panel.measured_hz:.1f}/s'
            )
            force_text.set(
                "Paw Ground_Reaction_Forces | "
                + "   ".join(
                    f"{label}: Fx {force[0]:+.1f}, Fz {force[2]:.1f} N"
                    for label, force in zip(
                        ["LH cyan", "RH pink", "LF gold", "RF purple"],
                        snapshot["forces"],
                    )
                )
            )
        # Compensate for plot-update work instead of adding a fixed delay to it.
        # 20 plot updates/s are sufficient for the traces and leave more CPU
        # time for the independent 60-Hz 3D visualization and window rendering.
        root.after(
            max(1, int(1000 * (1 / 20.0 - (time.perf_counter() - started)))),
            refresh,
        )

    root.protocol("WM_DELETE_WINDOW", close)
    root.after(100, refresh)
    print(
        "GUI_READY: independent 60-Hz-target playback, paw-force arrows and blitted comparison plots open",
        flush=True,
    )
    root.mainloop()


if __name__ == "__main__":
    main()
