"""Explicit calibration gates; completing integration alone is not walking."""

import numpy as np

from .compare_simulation_with_experiment import compare_simulation_with_experiment

from .experimental_comparison_targets import experimental_comparison_targets


def walking_acceptance(result, settings):
    """Compare unfiltered signals and sustained contact cycles to fixed targets.

    These tolerances are engineering acceptance targets, not uncertainty
    intervals for the biological recordings. LH and fore EMG data limitations
    remain in compare_simulation_with_experiment(). Contact dwell is only event detection, never force
    smoothing or an alteration of plotted/scored Ground_Reaction_Forces.
    """
    t = result["time"]
    metrics = compare_simulation_with_experiment(result, settings)
    T = settings["period_s"]
    target = experimental_comparison_targets(t, T, settings.get("reference_table_dir"))
    late = t >= max(0.0, float(t[-1]) - 10.0)
    q = np.sqrt(
        np.mean(np.rad2deg(result["joint_q"][late] - target["joint_q"][late]) ** 2, axis=0)
    )
    grf = np.sqrt(np.mean((result["grf"][late] - target["grf"][late]) ** 2, axis=0))
    angle_limit = np.array([8.0, 6.0, 8.0, 8.0])[:, None]
    cycles = []
    dt = float(np.median(np.diff(t)))
    dwell = max(1, round(0.025 / dt))
    for limb in range(4):
        raw = result["grf"][:, limb, 2] > 1.0
        on = bool(raw[0])
        counter = 0
        touch = []
        off = []
        for k, value in enumerate(raw):
            counter = counter + 1 if bool(value) != on else 0
            if counter >= dwell:
                on = bool(value)
                (touch if on else off).append(float(t[k - dwell + 1]))
                counter = 0
        recent = np.array(off)
        recent = recent[recent >= max(0.0, float(t[-1]) - 10.0)]
        periods = np.diff(recent)
        cycles.append(
            dict(
                completed_cycles=max(0, len(off) - 1),
                last_window_median_period_s=(
                    float(np.median(periods))
                    if len(periods)
                    else None
                ),
                period_relative_sd=(
                    float(np.std(periods) / np.mean(periods))
                    if len(periods) > 1
                    else None
                ),
            )
        )
    sufficient = bool(float(t[-1]) >= 59.99 and not str(result["failure"]))
    rhythm = bool(
        sufficient
        and all(
            c["completed_cycles"] >= int(0.8 * float(t[-1]) / T)
            and c["last_window_median_period_s"] is not None
            and abs(c["last_window_median_period_s"] / T - 1) < 0.10
            and c["period_relative_sd"] is not None
            and c["period_relative_sd"] < 0.10
            for c in cycles
        )
    )
    force_signs = []
    for limb in range(4):
        fx = result["grf"][late, limb, 0]
        force_signs.append(bool(fx.min() < -0.5 and fx.max() > 0.5))
    emg_pass = all(
        e["peak_normalized_rmse"] < 0.25 and e["correlation"] > 0.7
        for e in metrics["emg"]
    )
    timing = []
    for item in metrics["emg"]:
        score = item["complete_input_cycle_timing"]
        edges = all(
            score[key]["unmatched_predicted"] == 0
            and score[key]["unmatched_reference"] == 0
            and (
                score[key]["maximum_absolute_error_s"] is None
                or score[key]["maximum_absolute_error_s"]
                <= settings.get("emg_phase_edge_tolerance_s", 0.035)
            )
            for key in ["onset", "offset"]
        )
        timing.append(
            bool(
                score["active_intersection_over_union"]
                >= settings.get("emg_phase_iou_min", 0.8)
                and edges
            )
        )
    tests = dict(
        uninterrupted_60s=sufficient,
        rhythmic_four_paw_contacts=rhythm,
        all_joint_RMSE=bool(np.all(q < angle_limit)),
        all_AP_RMSE=bool(np.all(grf[:, 0] < 0.6)),
        all_vertical_RMSE=bool(np.all(grf[:, 2] < 1.5)),
        braking_and_propulsion_all_paws=all(force_signs),
        available_EMG_shapes=bool(emg_pass),
    )
    tests["available_EMG_active_quiet_timing"] = bool(all(timing))
    if "max_interior_fiber_residual_N" in result:
        tests["interior_elastic_equilibrium"] = bool(
            float(result["max_interior_fiber_residual_N"])
            < 1e-4
        )
        tests["no_geometric_fiber_bounds"] = bool(int(result["fiber_bound_steps"]) == 0)
    else:
        tests["interior_elastic_equilibrium"] = False
        tests["no_geometric_fiber_bounds"] = False
    if settings.get("fore_force_velocity_mode") == "degroote_2016":
        tests["published_fore_force_velocity_domain"] = bool(
            "peak_abs_normalized_fiber_velocity" in result
            and np.max(result["peak_abs_normalized_fiber_velocity"][28:]) <= 1.0 + 1e-6
        )
    if settings.get("hind_force_velocity_mode") == "degroote_2016":
        tests["published_hind_force_velocity_domain"] = bool(
            "peak_abs_normalized_fiber_velocity" in result
            and np.max(result["peak_abs_normalized_fiber_velocity"][:28]) <= 1.0 + 1e-6
        )
    if "degroote_force_velocity_enabled" in result:
        enabled = np.asarray(result["degroote_force_velocity_enabled"], bool)
        if np.any(enabled):
            tests["configured_force_velocity_domain"] = bool(
                np.max(result["peak_abs_normalized_fiber_velocity"][enabled])
                <= 1.0 + 1e-6
            )
    return dict(
        tests=tests,
        primary_calibration_pass=bool(all(tests.values())),
        half_step_and_perturbation_still_required=True,
        late_window_start_s=float(t[late][0]),
        late_joint_RMSE_deg=q.tolist(),
        late_AP_vertical_RMSE_N=grf[:, [0, 2]].tolist(),
        contact_cycles=cycles,
        threshold_provenance="Declared engineering targets comparable to preserved hindlimb fit; not published biological tolerances.",
        independent_four_limb_validation=False,
    )
