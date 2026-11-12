"""Four reusable comparison plots, with fast marker/curve updates by blitting."""

import time

from collections import deque

import numpy as np

from matplotlib.figure import Figure

# Choose readable absolute-time tick intervals for both long and short recordings.
from matplotlib.ticker import MaxNLocator

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ReplayPlotPanel:
    """Keep axes and artists alive; redraw static labels only after selection/resize.

    A four-second window follows playback, with actual simulation-time labels.
    Its bounds stay between zero and the last saved sample. Seeking backward
    moves the window backward too, including after playback has finished.
    """

    def __init__(self, parent, result, target, pairs, peaks, period_s):
        self.result, self.target, self.pairs = result, target, pairs
        self.peaks, self.period = peaks, period_s
        self.names = list(result["names"])
        self.times = result["time"]
        # Number of seconds visible at once; short trials use their whole duration.
        self.window_seconds = 4.0
        # About four labeled time intervals fit comfortably within each small plot.
        self.time_tick_locator = MaxNLocator(nbins=4)
        self.figure = Figure(figsize=(9, 6), dpi=90)
        self.axes = self.figure.subplots(2, 2)
        self.figure.subplots_adjust(
            left=0.09,
            right=0.98,
            top=0.93,
            bottom=0.09,
            hspace=0.48,
            wspace=0.28,
        )
        self.canvas = FigureCanvasTkAgg(self.figure, master=parent)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.background = None
        self.key = None
        self.artists = []
        self.curves = []
        self.markers = []
        self.frame_times = deque(maxlen=120)
        self.emg_cache = {}
        self.last_time = None
        self.needs_redraw = True
        self.canvas.mpl_connect("draw_event", self._capture_background)

    def _capture_background(self, event):
        self.background = self.canvas.copy_from_bbox(self.figure.bbox)
        self.needs_redraw = True

    def _setup(self, side, name, joint_index, normalized, show_emg):
        # Discard the previous selection's lines and moving indicators.
        self.curves = []
        # Store one moving dot for every simulated or reference trace.
        self.markers = []
        # Redraw only these changing objects during normal playback.
        self.artists = []
        # Store a current-time vertical line for each of the four plots.
        self.cursors = []
        # Cache movable time labels and vertical grid lines instead of rebuilding axes.
        self.time_ticks = []
        for ax in self.axes.ravel():
            ax.clear()
            ax.grid(alpha=0.2)
            # Start with the first four seconds, or the whole trial if it is shorter.
            ax.set_xlim(0.0, max(min(self.window_seconds, float(self.times[-1])), 0.001))
            # Standard x ticks would require a costly full canvas redraw while scrolling.
            ax.set_xticks([])
            # Reserve enough labels for the small set returned by the time tick locator.
            for tick_number in range(7):
                # Move this vertical grid line to a labeled absolute time during update().
                grid_line = ax.axvline(0.0, color="gray", alpha=0.2, lw=0.8, animated=True)
                # Draw the corresponding time just below the horizontal axis.
                tick_label = ax.text(0.0, -0.045, "", transform=ax.get_xaxis_transform(),
                                     ha="center", va="top", fontsize=10, animated=True)
                # Keep the grid line and its label together with their assigned tick number.
                self.time_ticks.append((tick_number, grid_line, tick_label))
                # These lightweight objects can move without redrawing titles and legends.
                self.artists.extend([grid_line, tick_label])
            # Create the moving current-time line; its initial position is zero.
            cursor = ax.axvline(0.0, color="#aa7b27", lw=1.0, animated=True)
            # Remember the line so update() can move it without rebuilding the axes.
            self.cursors.append(cursor)
            # Include the cursor among the objects redrawn at each playback frame.
            self.artists.append(cursor)
            # Label the horizontal coordinate as actual elapsed simulation time.
            ax.set_xlabel("Simulation time (s)")
            # Leave room for the movable numeric labels above the axis caption.
            ax.xaxis.set_label_coords(0.5, -0.15)
        channel = self.names.index(name)
        scale = self.peaks[channel] if normalized else 1.0
        traces = [
            [
                (
                    self.result["excitation"][:, channel] / scale,
                    "#087f9c",
                    "-",
                    "Excitation",
                ),
                (
                    self.result["activation"][:, channel] / scale,
                    "#aa3484",
                    "-",
                    "Activation",
                ),
            ]
        ]
        if show_emg and name in self.pairs:
            if name not in self.emg_cache:
                ref = self.pairs[name]["reference"]
                phase = np.arange(len(ref)) / len(ref)
                self.emg_cache[name] = np.interp(
                    (self.times / self.period) % 1,
                    np.r_[phase, 1.0],
                    np.r_[ref, ref[0]],
                )
            traces[0].append((self.emg_cache[name], "black", "--", "EMG (peak normalized)"))
        sign = ([-1, 1, -1, -1] if side < 2 else [1, -1, -1, -1])[joint_index]
        offset = ([0, np.pi, np.pi, np.pi] if side < 2 else [np.pi] * 4)[joint_index]
        traces.append(
            [
                (
                    np.rad2deg(
                        offset
                        + sign * self.target["joint_q"][:, side, joint_index]
                    ),
                    "black",
                    "--",
                    "Reference",
                ),
                (
                    np.rad2deg(
                        offset
                        + sign * self.result["joint_q"][:, side, joint_index]
                    ),
                    "#087f9c",
                    "-",
                    "Forward",
                ),
            ]
        )
        for component in [2, 0]:
            traces.append(
                [
                    (self.target["grf"][:, side, component], "black", "--", "Reference"),
                    (
                        self.result["grf"][:, side, component],
                        "#087f9c",
                        "-",
                        "Raw paw force",
                    ),
                ]
            )
        limb = ["LH", "RH", "LF", "RF"][side]
        joint = (
            ["Hip", "Knee", "Ankle", "MTP"]
            if side < 2
            else ["Shoulder", "Elbow", "Wrist", "MCP"]
        )[joint_index]
        titles = [
            name + (" / fixed peak" if normalized else " / absolute input"),
            limb + " " + joint,
            limb + " vertical GRF",
            limb + " anterior–posterior (AP) GRF",
        ]
        for panel, (ax, items) in enumerate(zip(self.axes.ravel(), traces)):
            ax.set_title(titles[panel], fontsize=11)
            ax.set_ylabel(
                ["Input / activation", "Anatomical angle (deg)", "Force (N)", "Force (N)"][
                    panel
                ]
            )
            lower = min(float(v[0].min()) for v in items)
            upper = max(float(v[0].max()) for v in items)
            if panel != 1:
                lower = min(0.0, lower)
            margin = max(0.05, (upper - lower) * 0.08)
            ax.set_ylim(lower - margin, upper + margin)
            for values, color, style, label in items:
                (line,) = ax.plot(
                    # update() supplies the saved samples inside the current time window.
                    [],
                    # Data remain unchanged; only the visible interval is selected.
                    [],
                    color=color,
                    linestyle=style,
                    label=label,
                    lw=1.3,
                    # Redraw the visible curve when the four-second window moves.
                    animated=True,
                )
                (marker,) = ax.plot([], [], "o", color=color, ms=4, animated=True)
                self.curves.append((line, values))
                self.markers.append((marker, values))
                # Reuse both the curve and its current-time dot during scrolling.
                self.artists.extend([line, marker])
            ax.legend(fontsize=7, loc="upper right")
        self.canvas.draw()

    def update(self, time_s, side, name, joint_index, normalized=True, show_emg=True):
        # Keep the displayed cursor inside the recorded interval, including at Reset.
        time_s = float(np.clip(time_s, 0.0, self.times[-1]))
        key = (side, name, joint_index, normalized, show_emg)
        if key != self.key:
            self.key = key
            self._setup(*key)
        elif time_s == self.last_time and not self.needs_redraw:
            return
        # Keep a four-second view centered on the current time where possible.
        trial_end = max(float(self.times[-1]), 0.001)
        # Short recordings need a shorter window so no time outside the trial appears.
        window_width = min(self.window_seconds, trial_end)
        # Clamp the moving window to the first and last available times.
        window_start = min(max(time_s - window_width / 2.0, 0.0), trial_end - window_width)
        # All four plots use exactly the same interval.
        window_end = window_start + window_width
        # Change the time transform without rebuilding static titles, legends, and borders.
        if self.axes[0, 0].get_xlim() != (window_start, window_end):
            # Move every plot together so excitation, angles, and forces stay aligned.
            for axis in self.axes.ravel():
                # These are actual simulation seconds, never time relative to a cursor.
                axis.set_xlim(window_start, window_end)
        # Choose readable absolute times for grid lines inside the visible window.
        tick_times = self.time_tick_locator.tick_values(window_start, window_end)
        # Keep labels within the actual recorded time range.
        tick_times = tick_times[(tick_times >= window_start) & (tick_times <= window_end)]
        # Move cached labels and grid lines using the same absolute-time transform.
        for tick_number, grid_line, tick_label in self.time_ticks:
            # Unused label slots must disappear rather than showing old time values.
            visible = tick_number < len(tick_times)
            # Show only the grid lines needed in this window.
            grid_line.set_visible(visible)
            # Give the matching label the same visibility.
            tick_label.set_visible(visible)
            # Update coordinates only for the label slots in use.
            if visible:
                # Read this grid line's actual simulation time.
                tick_time = float(tick_times[tick_number])
                # Position the grid line at that time.
                grid_line.set_xdata([tick_time, tick_time])
                # Align its numeric label just below the same time coordinate.
                tick_label.set_position((tick_time, -0.045))
                # Avoid long floating-point strings in the small plot panels.
                tick_label.set_text(f"{tick_time:.4g}")
        # Include one neighboring sample on either side for continuous boundary segments.
        first_sample = max(0, np.searchsorted(self.times, window_start) - 1)
        # Keep the next sample as well, without exceeding the saved array.
        last_sample = min(len(self.times), np.searchsorted(self.times, window_end, side="right") + 1)
        # Draw raw saved samples within the moving window; do not filter the waveforms.
        for line, values in self.curves:
            # Every visible point retains its absolute simulation time and original value.
            line.set_data(self.times[first_sample:last_sample], values[first_sample:last_sample])
        # Move all vertical lines to the current absolute simulation time.
        for cursor in self.cursors:
            # Two equal x coordinates make a vertical line at this time.
            cursor.set_xdata([time_s, time_s])
        for marker, values in self.markers:
            # Move each dot to this time and its interpolated signal value.
            marker.set_data([time_s], [np.interp(time_s, self.times, values)])
        if self.background is None:
            self.canvas.draw()
        self.canvas.restore_region(self.background)
        for artist in self.artists:
            artist.axes.draw_artist(artist)
        self.canvas.blit(self.figure.bbox)
        self.last_time = time_s
        self.needs_redraw = False
        self.frame_times.append(time.perf_counter())

    # Apply this function/property behavior.
    @property
    def measured_hz(self):
        if len(self.frame_times) < 2:
            return 0.0
        return (len(self.frame_times) - 1) / (self.frame_times[-1] - self.frame_times[0])
