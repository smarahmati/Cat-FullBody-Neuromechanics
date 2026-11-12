"""Open an already computed trial without recalculating it.
Example: python view.py --run Simulation_Results/Intact_Walking
"""
from pathlib import Path
import runpy, sys
root = Path(__file__).resolve().parent
sys.path.insert(0, str(root / "Code"))
if __name__ == "__main__":
    runpy.run_path(str(root / "Code/simulation_tools/view_walking_simulation.py"), run_name="__main__")
