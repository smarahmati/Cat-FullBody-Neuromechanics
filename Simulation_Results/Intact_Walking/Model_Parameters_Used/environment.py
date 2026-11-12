"""Applied model values. Edit the numbers in PARAMETERS, then run run.py.
Comments and PARAMETER_PROVENANCE.json preserve originals; they do not override your edits.
Missing raw originals are stated honestly. SI units unless noted. Experimental agreement and limitations are documented in Documentation/results.html.
"""

# Set PARAMETERS.
PARAMETERS = {
    # Engine integration scheme; original and applied: 3 = implicitfast.
    # Available engine choices: 0 Euler, 1 RK4, 2 implicit, 3 implicitfast.
    # This partitioned muscle/contact scheme was tested with 3; retest any change.
    "integrator": 3,
    # Environment/engine setting: gravity_m_s2.
    "gravity_m_s2": [0.0, 0.0, -9.81],
    # Environment/engine setting: solver_iterations.
    "solver_iterations": 80,
    # Environment/engine setting: solver_tolerance.
    "solver_tolerance": 1e-08,
}
