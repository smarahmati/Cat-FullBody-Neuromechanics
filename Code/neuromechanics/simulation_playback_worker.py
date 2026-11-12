"""Independent 3D playback loop so Tk plotting cannot dictate frame timing."""

from collections import deque

import json

import threading

import time

import numpy as np

import mujoco as mj

from .interpolate_simulation_for_display import interpolate_simulation_for_display

from .update_saved_visual_state import update_saved_visual_state

from .draw_saved_grf_vectors import draw_saved_grf_vectors


class SavedReplayWorker:
    """Own MuJoCo data/viewer mutations; exchange plain values with the Tk thread."""

    def __init__(self, viewer, state, result, profile_path, profile_seconds=12.0):
        self.viewer, self.state, self.result = viewer, state, result
        self.profile_path, self.profile_seconds = profile_path, profile_seconds
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.controls = dict(
            paused=True,
            speed=0.5,
            fps=60.0,
            forces=True,
            rich=False,
            follow=True,
            seek=None,
        )
        self.current = dict(
            time=0.0,
            update_hz=0.0,
            # Calculate the error in this comparison.
            error=None,
            forces=np.zeros((4, 3)),
            arrows=[],
        )
        self.intervals = []
        self.work_seconds = []
        self.profile_saved = False
        self.thread = threading.Thread(
            target=self._run,
            name="cat-saved-3d-replay",
            daemon=True,
        )

    def start(self):
        self.thread.start()

    def command(self, **values):
        # Keep this file or shared state safely scoped to the following operations.
        with self.lock:
            self.controls.update(values)

    def snapshot(self):
        # Keep this file or shared state safely scoped to the following operations.
        with self.lock:
            return dict(self.current)

    def stop(self):
        self.stop_event.set()
        self.thread.join(timeout=3.0)

    def _run(self):
        # Attempt the operation and report a failure in the exception branch.
        try:
            self._loop()
        # Handle the stated error without hiding its cause.
        except Exception as error:
            import traceback

            traceback.print_exc()
            # Keep this file or shared state safely scoped to the following operations.
            with self.lock:
                self.current["error"] = str(error)

    def _loop(self):
        frame_times = deque(maxlen=180)
        beginning = previous = time.perf_counter()
        simulation_time = 0.0
        pelvis_id = self.state["model"].body("pelvis").id
        # Repeat while not self.stop_event.is_set() and self.viewer.is_running().
        while not self.stop_event.is_set() and self.viewer.is_running():
            started = time.perf_counter()
            elapsed = started - previous
            previous = started
            # Keep this file or shared state safely scoped to the following operations.
            with self.lock:
                control = dict(self.controls)
                self.controls["seek"] = None
            if control["seek"] is not None:
                simulation_time = float(
                    np.clip(control["seek"], 0.0, self.result["time"][-1])
                )
            elif not control["paused"]:
                simulation_time = min(
                    float(self.result["time"][-1]),
                    simulation_time + elapsed * control["speed"],
                )
            sample = interpolate_simulation_for_display(self.result, simulation_time)
            # Keep this file or shared state safely scoped to the following operations.
            with self.viewer.lock():
                update_saved_visual_state(self.state, sample)
                if control["follow"]:
                    self.viewer.cam.lookat[0] = self.state["data"].xpos[pelvis_id, 0] + 0.12
                self.viewer.user_scn.flags[mj.mjtRndFlag.mjRND_SHADOW] = control["rich"]
                self.viewer.user_scn.flags[mj.mjtRndFlag.mjRND_REFLECTION] = control["rich"]
                arrows = draw_saved_grf_vectors(
                    self.viewer,
                    self.state,
                    sample["grf"],
                    control["forces"],
                )
            self.viewer.sync()
            finished = time.perf_counter()
            frame_times.append(finished)
            if len(frame_times) > 1:
                rate = (len(frame_times) - 1) / (frame_times[-1] - frame_times[0])
            else:
                rate = 0.0
            if started - beginning > 2.0 and len(frame_times) > 1:
                self.intervals.append(frame_times[-1] - frame_times[-2])
                self.work_seconds.append(finished - started)
            # Keep this file or shared state safely scoped to the following operations.
            with self.lock:
                self.current.update(
                    time=simulation_time,
                    update_hz=rate,
                    forces=sample["grf"].copy(),
                    arrows=arrows,
                )
                if simulation_time >= self.result["time"][-1]:
                    self.controls["paused"] = True
            if (
                not self.profile_saved
                and started - beginning >= self.profile_seconds
                and self.intervals
            ):
                report = dict(
                    target_update_hz=control["fps"],
                    measured_3d_update_hz=1.0 / float(np.mean(self.intervals)),
                    frame_interval_ms_median=1000 * float(np.median(self.intervals)),
                    frame_interval_ms_p95=1000 * float(np.quantile(self.intervals, 0.95)),
                    frame_work_ms_median=1000 * float(np.median(self.work_seconds)),
                    displayed_arrow_count=len(arrows),
                    mesh_triangles=int(self.state["model"].nmeshface),
                    shadows_and_reflections=control["rich"],
                    rate_scope="Python state + passive-viewer synchronization, not measured monitor/GPU presentation FPS",
                    recording_unchanged=True,
                    interpolation="Linear between saved scalar-coordinate states for display only",
                )
                self.profile_path.parent.mkdir(parents=True, exist_ok=True)
                # Save the computed values or figure for inspection and reproducibility.
                self.profile_path.write_text(json.dumps(report, indent=2))
                print("GUI_PERFORMANCE " + json.dumps(report), flush=True)
                self.profile_saved = True
            # Python 3.12 sleep uses a high-resolution Windows waitable timer.
            # Event.wait rounds short waits to the coarser system tick on this
            # host, which reduced a 60-Hz request to roughly 30 actual updates.
            time.sleep(max(0.0, 1.0 / control["fps"] - (time.perf_counter() - started)))
