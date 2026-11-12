"""Resolve one editable parameter folder into the settings used by run.py."""

from pathlib import Path

from model_configuration.paths import ROOT

from .load_parameter_file import load_parameter_file

from .read_time_series import read_time_series


def load_model_configuration(folder):
    """Read all named physical parameter files once, before t=0.

    Excitation is read afresh on every run. An edited table therefore changes
    actual motor input, not just its plotted label. References remain scoring
    data and do not prescribe the motion.
    """
    folder = (ROOT / Path(folder)).resolve()
    cfg = load_parameter_file(folder / "simulation_settings.py")
    # Physical overrides belong in the named files. Accepting a legacy
    # multiplier here would be misleading because absolute values win later.
    allowed = {
        "model_variant",
        "period_s",
        "dt_s",
        "sample_s",
        "seconds",
        "stop_on_fall",
        "activation_parameter_mode",
        "initialize_from_assembled_reference",
        "forward_step_implementation",
        "reference_table_dir",
        "fit_angle_scale_deg",
        "fit_ap_scale_N",
        "fit_vertical_scale_N",
        "emg_phase_threshold",
        "emg_phase_iou_min",
        "emg_phase_edge_tolerance_s",
    }
    if set(cfg) - allowed:
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Unknown run settings: " + str(sorted(set(cfg) - allowed)))
    if any(cfg[key] <= 0 for key in ["dt_s", "sample_s", "period_s", "seconds"]):
        # Stop and explain the invalid model setting or failed calculation.
        raise ValueError("Times and period must be positive")
    cfg["parameter_bundle_dir"] = str(folder)
    cfg["initial_parameter_file"] = str(folder / "initial_state.py")
    cfg["excitation_table_file"] = str((folder / "excitation_cycle.tsv") if (folder / "excitation_cycle.tsv").exists() else (ROOT / "Data/Muscle_Excitation_Input/excitation_cycle.tsv"))
    # Keep the exact phase samples; interpolation is performed at runtime.
    # Validation against muscle names is done after loading the model.
    read_time_series(cfg["excitation_table_file"])
    return cfg
