"""Recompute the complete 60-second intact walking simulation.

Run: python reproduce.py --gui
Pass any run.py option, such as --seconds or --output, to override the defaults.
"""
from pathlib import Path
import subprocess
import sys


def main():
    """Use the same current parameters and forward integrator as run.py."""
    arguments = list(sys.argv[1:])
    if '--seconds' not in arguments:
        arguments.extend(['--seconds', '60'])
    if '--gui' not in arguments and '--no-gui' not in arguments:
        arguments.append('--no-gui')
    subprocess.run([sys.executable, str(Path(__file__).resolve().parent / 'run.py'), *arguments], check=True)


if __name__ == '__main__':
    main()
