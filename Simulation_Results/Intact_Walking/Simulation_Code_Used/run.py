"""Compute a NEW fully forward trial, optionally opening the result viewer.

Edit the defaults below, then press Run in your IDE. Command-line options win:
    python run.py --seconds 6 --gui
    python run.py --seconds 60 --no-gui
The GUI displays the computed intact walking, muscle states and contact forces.
"""
from pathlib import Path
import os
import sys
import json

# These limits prevent many competing CPU threads; they do not change equations.
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
# Duration is simulation time, not the wall time needed to calculate it.
SIMULATION_SECONDS = 6.0
# True opens animation and plots AFTER calculation; False only saves results.
SHOW_GUI = True
# The current model has one clearly named parameter folder.
PARAMETER_FOLDER = Path(__file__).resolve().parent / "Data" / "Model_Parameters"

sys.path.insert(0, str(Path(__file__).resolve().parent / "Code"))
# Select the constants before importing the numerical kernels.
chosen = PARAMETER_FOLDER
if "--parameters" in sys.argv:
    chosen = (Path(__file__).resolve().parent / sys.argv[sys.argv.index("--parameters") + 1]).resolve()
elif "--config" in sys.argv:
    # Replaying a saved configuration must also reuse its formulation constants.
    saved = json.loads((Path(__file__).resolve().parent / sys.argv[sys.argv.index("--config") + 1]).read_text())
    chosen = Path(__file__).resolve().parent / saved.get("parameter_bundle_dir", "Data/Model_Parameters")
os.environ["CAT_PARAMETER_FOLDER"] = str(chosen)
from simulation_tools.run_forward_simulation import main

if __name__ == "__main__":
    if "--parameters" not in sys.argv and "--config" not in sys.argv:
        sys.argv.extend(["--parameters", str(PARAMETER_FOLDER)])
    main(default_seconds=SIMULATION_SECONDS, default_gui=SHOW_GUI)
