"""Render a video of the cat from saved forward-dynamics states.

This script does not drive or solve the model. The visible movement and paw
forces come from forward_simulation_timeseries.npz. Arguments select the saved time interval,
output frame rate, and playback speed. Time is in seconds; force is in newtons.
"""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Code"))
import numpy as np
import mujoco as mj
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
from neuromechanics.initialize_neuromechanical_model import initialize_neuromechanical_model
from neuromechanics.interpolate_simulation_for_display import (
    interpolate_simulation_for_display,
)
from neuromechanics.update_saved_visual_state import update_saved_visual_state


def render_walking_video(
    run_folder, output, start_s=56.0, end_s=59.9, frames_per_second=40, playback_speed=0.5
):
    """Turn saved states into frames; interpolate only for visual smoothness."""
    folder = ROOT / run_folder
    result = dict(np.load(folder / "forward_simulation_timeseries.npz"))
    settings = json.loads((folder / "settings.json").read_text())
    state = initialize_neuromechanical_model(settings, graphics=True)
    model, data = state["model"], state["data"]
    width, height = 1100, 720
    model.vis.global_.offwidth = width
    model.vis.global_.offheight = height
    renderer = mj.Renderer(model, height=height, width=width)
    camera = mj.MjvCamera()
    camera.distance = 0.95
    camera.azimuth = 90
    camera.elevation = -17
    camera.lookat[:] = [0.15, 0.0, 0.22]
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        imageio_ffmpeg.get_ffmpeg_exe(),
        "-y",
        "-f",
        "rawvideo",
        "-vcodec",
        "rawvideo",
        "-s",
        f"{width}x{height}",
        "-pix_fmt",
        "rgb24",
        "-r",
        str(frames_per_second),
        "-i",
        "-",
        "-an",
        "-c:v",
        "libx264",
        "-crf",
        "20",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        str(output),
    ]
    encoder = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    start_s = max(float(result["time"][0]), start_s)
    end_s = min(float(result["time"][-1]), end_s)
    frame_count = int((end_s - start_s) / playback_speed * frames_per_second)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 22)
    except OSError:
        font = ImageFont.load_default(size=22)
    colors = [(30, 215, 235), (255, 45, 165), (250, 190, 40), (180, 110, 255)]
    for frame in range(frame_count):
        current_s = start_s + frame * playback_speed / frames_per_second
        sample = interpolate_simulation_for_display(result, current_s)
        update_saved_visual_state(state, sample)
        camera.lookat[0] = data.xpos[model.body("pelvis").id, 0] + 0.12
        renderer.update_scene(data, camera=camera)
        renderer.scene.flags[mj.mjtRndFlag.mjRND_SHADOW] = False
        renderer.scene.flags[mj.mjtRndFlag.mjRND_REFLECTION] = False
        for paw, force in enumerate(sample["grf"]):
            magnitude = float(np.linalg.norm(force))
            if magnitude < 0.05:
                # Skip the remaining work for this item.
                continue
            arrow = renderer.scene.geoms[renderer.scene.ngeom]
            origin = data.site_xpos[state["paw_ids"][paw]].copy()
            origin[2] = 0.002
            rgba = np.r_[np.asarray(colors[paw]) / 255.0, 1.0]
            mj.mjv_initGeom(
                arrow,
                mj.mjtGeom.mjGEOM_ARROW,
                np.zeros(3),
                np.zeros(3),
                np.eye(3).ravel(),
                rgba,
            )
            mj.mjv_connector(
                arrow, mj.mjtGeom.mjGEOM_ARROW, 0.0035, origin, origin + 0.006 * force
            )
            renderer.scene.ngeom += 1
        pixels = Image.fromarray(renderer.render())
        text = ImageDraw.Draw(pixels)
        text.rectangle((0, 0, width, 90), fill=(16, 30, 42))
        text.text(
            (20, 12),
            f"CAT | forward dynamics | t = {current_s:.2f} s | playback {playback_speed:g}x",
            font=font,
            fill="white",
        )
        text.text(
            (20, 48),
            "Elastic tendons; prescribed excitation; calculated paw-contact forces",
            font=font,
            fill="white",
        )
        for paw, label in enumerate(["LH", "RH", "LF", "RF"]):
            text.text(
                (20 + paw * 270, height - 38),
                f'{label}: Fx {sample["grf"][paw,0]:+.1f}, Fz {sample["grf"][paw,2]:.1f} N',
                font=font,
                fill=colors[paw],
            )
        encoder.stdin.write(np.asarray(pixels).tobytes())
        if frame == 0:
            pixels.save(output.with_suffix(".png"))
    encoder.stdin.close()
    error_text = encoder.stderr.read().decode(errors="replace")
    if encoder.wait() != 0:
        # Stop and explain the invalid model setting or failed calculation.
        raise RuntimeError(error_text)
    renderer.close()
    metadata = dict(
        source=str(folder / "forward_simulation_timeseries.npz"),
        start_s=start_s,
        end_s=end_s,
        frame_count=frame_count,
        frames_per_second=frames_per_second,
        playback_speed=playback_speed,
        species="cat",
        arrows="saved Ground_Reaction_Forces at projected paw sites; archived center of pressure unavailable",
    )
    # Save the computed values or figure for inspection and reproducibility.
    output.with_suffix(".json").write_text(json.dumps(metadata, indent=2))
    print("VIDEO_SAVED " + str(output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", default="Simulation_Results/Intact_Walking")
    parser.add_argument(
        "--output", default=str(ROOT / "Documentation/Figures_and_Videos/walking_simulation.mp4")
    )
    arguments = parser.parse_args()
    render_walking_video(arguments.run, arguments.output)
