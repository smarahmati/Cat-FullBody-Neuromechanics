"""Run choices. All physical values are in the neighboring named files."""

# Set PARAMETERS.
PARAMETERS = {
    # Selects anatomical topology. Changing it requires a matching complete parameter set.
    "model_variant": "articulated_girdle",
    # Input period (s). Original RH Ted_046: 0.6833333333333333; fore source: 0.687857483228707. No per-channel phase retiming.
    "period_s": 0.6833333333333333,
    # Applied integration step (s). Reference integration step: 0.00012499237851350527. Smaller steps need independent stability tests.
    "dt_s": 0.00012499237851350527,
    # Saved output interval (s), not integration timestep. Original 0.005.
    "sample_s": 0.005,
    # Fallback duration: run.py SIMULATION_SECONDS and CLI --seconds take precedence.
    # Reference simulation duration: 60 s. Use None in run.py to use this value.
    "seconds": 60.0,
    # Run/analysis option; original defaults are documented in Code/model_configuration/settings.py.
    "stop_on_fall": True,
    # Run/analysis option; original defaults are documented in Code/model_configuration/settings.py.
    "activation_parameter_mode": "source",
    # Run/analysis option; original defaults are documented in Code/model_configuration/settings.py.
    "initialize_from_assembled_reference": False,
    # Named physical subsystem functions with Newton elastic-fiber solve; partitioned integration with elastic equilibrium at each step.
    "forward_step_implementation": "readable",
    # Editable source comparison tables, read again each run. They score the result; they never drive the bones or impose Ground_Reaction_Forces.
    "reference_table_dir": "Data/Experimental_Reference_Data",
    # Run/analysis option; original defaults are documented in Code/model_configuration/settings.py.
    "fit_angle_scale_deg": 10.0,
    # Run/analysis option; original defaults are documented in Code/model_configuration/settings.py.
    "fit_ap_scale_N": 3.0,
    # Run/analysis option; original defaults are documented in Code/model_configuration/settings.py.
    "fit_vertical_scale_N": 15.0,
    # Run/analysis option; original defaults are documented in Code/model_configuration/settings.py.
    "emg_phase_threshold": 0.1,
}
