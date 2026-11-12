"""Read signed muscle moment arms from MuJoCo's current transmission Jacobian.

Input: the model and data after muscle paths and positions have been updated.
Output: an (muscle, generalized-coordinate) array equal to -dL_MT/dq.
Rotational columns are metres; translational columns are dimensionless.
Positive tension times this array gives the applied generalized muscle force.
"""
import numpy as np


def muscle_moment_arms(model, data):
    """Convert the engine's sparse transmission representation to a named matrix."""
    jacobian = np.zeros((model.nu, model.nv))
    if data.actuator_moment.ndim == 2:
        jacobian[:] = data.actuator_moment
    else:
        for muscle in range(model.nu):
            first = int(data.moment_rowadr[muscle])
            last = first + int(data.moment_rownnz[muscle])
            columns = data.moment_colind[first:last]
            jacobian[muscle, columns] = data.actuator_moment[first:last]
    # A tensile actuator pulls towards decreasing muscle-tendon length.
    return -jacobian
