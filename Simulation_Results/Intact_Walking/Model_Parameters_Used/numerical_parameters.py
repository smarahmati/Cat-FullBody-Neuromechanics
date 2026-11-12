"""Elastic-solver settings; these numerical values are not tissue properties.

Original values are shown above each setting. A new run reads any changes.
"""

# Minimum fiber length / optimal fiber length; original 0.2.
MINIMUM_FIBER_LENGTH_RATIO = 0.2
# Positive fiber bracket gap in metres; original 1e-9.
MINIMUM_LENGTH_GAP_M = 1e-9
# Maximum Newton iterations per muscle per step; original 48.
MAXIMUM_FIBER_ITERATIONS = 48
# Dimensionless force-equilibrium tolerance; original 1e-10.
FIBER_FORCE_TOLERANCE = 1e-10
# Fiber bracket-width tolerance in metres; original 1e-12.
FIBER_LENGTH_TOLERANCE_M = 1e-12
# Switch to bisection after this Newton iteration; original 20.
NEWTON_FALLBACK_ITERATION = 20
# Iterations in the historical bisection solver; original 38.
BISECTION_ITERATIONS = 38
# Maximum generalized speed before declaring instability; original 500.
MAXIMUM_GENERALIZED_SPEED = 500.0
