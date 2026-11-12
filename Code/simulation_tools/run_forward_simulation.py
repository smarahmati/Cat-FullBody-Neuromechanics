"""Run the coupled forward model from editable files.

Examples, from the project directory:
    python run.py --output my_trial
    python run.py --parameters Data/Model_Parameters --seconds 5 --output five_seconds
    python run.py --config Simulation_Results/Intact_Walking/settings.json --seconds 3
    python run.py --output trial_with_viewer --gui

Without --config/--parameters, Data/Model_Parameters is used. Nothing is fitted
automatically: each run reads the requested physical parameters and fixed
muscle excitation table, integrates forward once, and compares with source references.
"""

import os, json, argparse, hashlib, shutil, sys

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from datetime import datetime

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

from model_configuration.paths import ROOT

from neuromechanics.simulate_forward_dynamics import simulate_forward_dynamics

from neuromechanics.initialize_neuromechanical_model import initialize_neuromechanical_model

from neuromechanics.load_model_configuration import load_model_configuration

from neuromechanics.read_applied_model_parameters import read_applied_model_parameters


def main(default_seconds=None, default_gui=False):
    """Read settings, calculate motion, and save results and comparison plots.

    default_seconds: duration chosen in run.py; None uses the parameter file.
    default_gui: whether run.py asks to open the viewer after calculation.
    Explicit --seconds, --gui, or --no-gui arguments take precedence.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--parameters", help="Folder of commented physical parameter files")
    group.add_argument("--config", help="Saved trial settings JSON")
    parser.add_argument(
        "--seconds",
        type=float,
        default=default_seconds,
        help="Run duration in seconds; overrides run.py and simulation_settings.py",
    )
    parser.add_argument(
        "--output",
        default="User_Simulations/walking_" + datetime.now().strftime("%Y%m%d_%H%M%S"),
    )
    parser.add_argument(
        "--replace-results", action="store_true",
        help="Recalculate and overwrite generated files in the named Results folder",
    )
    gui_options = parser.add_mutually_exclusive_group()
    gui_options.add_argument(
        "--gui",
        # Use the editable run.py choice when neither GUI flag is supplied.
        default=default_gui,
        action="store_true",
        help="After simulation, open the intact walking animation and plots",
    )
    gui_options.add_argument(
        "--no-gui",
        action="store_true",
        help="Calculate and save results without opening windows",
    )
    args = parser.parse_args()
    out = (ROOT / "Simulation_Results" / args.output).resolve()
    if not out.is_relative_to((ROOT / "Simulation_Results").resolve()):
        raise ValueError("Output must be within this project's Results folder")
    # Replacing an existing release is explicit; ordinary runs remain separate.
    out.mkdir(parents=True, exist_ok=args.replace_results)
    # Preserve the implementations and global curve constants as well as the
    # values. A parameter record alone cannot identify a changed physical law.
    for source_dir in ["Code/neuromechanics", "Code/model_configuration"]:
        target = out / "Simulation_Code_Used" / source_dir
        target.mkdir(parents=True, exist_ok=args.replace_results)
        for path in (ROOT / source_dir).glob("*.py"):
            shutil.copy2(path, target / path.name)
    shutil.copy2(ROOT / "run.py", out / "Simulation_Code_Used" / "run.py")
    shutil.copy2(
        ROOT / "Code/simulation_tools/run_forward_simulation.py",
        out / "Simulation_Code_Used" / "run_forward_simulation.py",
    )
    if args.config:
        cfg = json.loads((ROOT / args.config).read_text())
        # Save the computed values or figure for inspection and reproducibility.
        (out / "original_settings.json").write_text(json.dumps(cfg, indent=2))
    else:
        original = (ROOT / (args.parameters or "Data/Model_Parameters")).resolve()
        copied = out / "Model_Parameters_Used"
        shutil.copytree(original, copied, dirs_exist_ok=args.replace_results)
        if not (copied / "excitation_cycle.tsv").exists():
            shutil.copy2(ROOT / "Data/Muscle_Excitation_Input/excitation_cycle.tsv", copied / "excitation_cycle.tsv")
        cfg = load_model_configuration(copied)
        source_refs = (ROOT / cfg["reference_table_dir"]).resolve()
        shutil.copytree(source_refs, out / "Experimental_References_Used", dirs_exist_ok=args.replace_results)
        cfg["reference_table_dir"] = str(out / "Experimental_References_Used")
        files = list(copied.rglob("*")) + list((out / "Experimental_References_Used").rglob("*"))
        hashes = {
            str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in files
            if p.is_file()
        }
        # Save the computed values or figure for inspection and reproducibility.
        (out / "INPUT_HASHES.json").write_text(
            json.dumps(
                dict(original_parameter_folder=str(original), files=hashes),
                indent=2,
            )
        )
    if args.seconds is not None:
        cfg["seconds"] = args.seconds
    if cfg.get("seconds", 0) <= 0:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Run duration must be positive")
    state = initialize_neuromechanical_model(cfg)
    applied = read_applied_model_parameters(state)
    from neuromechanics.write_attachment_map import write_attachment_map

    write_attachment_map(state, out)
    # Save the computed values or figure for inspection and reproducibility.
    (out / "APPLIED_PARAMETERS.json").write_text(json.dumps(applied, indent=2))
    if not args.config:
        from neuromechanics.write_parameter_tables import write_parameter_tables

        write_parameter_tables(
            applied,
            json.loads((copied / "PARAMETER_PROVENANCE.json").read_text()),
            out / "APPLIED_PARAMETERS.html",
        )
    # Save the computed values or figure for inspection and reproducibility.
    portable_settings = dict(state["settings"])
    for key in ["parameter_bundle_dir", "initial_parameter_file", "excitation_table_file", "reference_table_dir"]:
        if portable_settings.get(key):
            portable_settings[key] = Path(portable_settings[key]).relative_to(ROOT).as_posix()
    (out / "settings.json").write_text(json.dumps(portable_settings, indent=2))
    print("Applied parameters saved: " + str(out / "APPLIED_PARAMETERS.json"), flush=True)
    result, state = simulate_forward_dynamics(state=state)
    result["degroote_force_velocity_enabled"] = (
        state["muscle_params"][:, 14].astype(bool)
        if state["muscle_params"].shape[1] > 14
        else np.zeros(len(state["names"]), bool)
    )
    # Record constitutive choices with the trajectory, not only in the config.
    result["passive_fiber_enabled"] = state["muscle_params"][:, 13] > 0
    # Save the computed values or figure for inspection and reproducibility.
    np.savez_compressed(out / "forward_simulation_timeseries.npz", **result)
    summary = dict(
        duration_s=float(result["time"][-1]),
        requested_s=state["settings"]["seconds"],
        failure=str(result["failure"]),
        mass_kg=float(state["model"].body_mass.sum()),
        wall_s=float(result["wall_seconds"]),
    )
    # Save the computed values or figure for inspection and reproducibility.
    (out / "simulation_summary.json").write_text(json.dumps(summary, indent=2))
    from neuromechanics.write_simulation_results import write_simulation_results

    write_simulation_results(result, state["settings"], out)
    from neuromechanics.walking_acceptance import walking_acceptance

    # Save the computed values or figure for inspection and reproducibility.
    (out / "walking_quality_metrics.json").write_text(
        json.dumps(walking_acceptance(result, state["settings"]), indent=2)
    )
    from neuromechanics.export_biomechanics import export_biomechanics
    export_biomechanics(result, state, out)
    print(json.dumps(summary, indent=2))
    print("Report: " + str(out / "simulation_report.html"))
    # An explicit --no-gui always overrides SHOW_GUI = True in run.py.
    if args.gui and not args.no_gui:
        import subprocess, sys

        subprocess.run(
            [
                sys.executable,
                str(ROOT / "Code/simulation_tools/view_walking_simulation.py"),
                "--run",
                str(out),
            ],
            check=True,
        )


if __name__ == "__main__":
    main()
