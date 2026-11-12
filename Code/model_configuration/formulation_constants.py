"""Load editable constants from the same parameter bundle as the simulation."""
from pathlib import Path
import os, runpy
from .paths import ROOT
folder = Path(os.environ.get("CAT_PARAMETER_FOLDER", ROOT / "Data/Model_Parameters"))
globals().update({k:v for k,v in runpy.run_path(str(folder / "formulation_constants.py")).items() if k.isupper()})
