"""Compute each muscle's generalized contribution and the sum across muscles.

Tension is positive in newtons. Moment arms are -dL_MT/dq. Hinge outputs
are moments in N m; slider outputs are forces in N. These are muscle
contributions, not inverse-dynamics net joint moments or joint reactions.
"""
import numpy as np


def muscle_joint_moments(moment_arms, tendon_forces):
    """Return individual muscle contributions and their sum, preserving signs."""
    individual = moment_arms * np.asarray(tendon_forces)[:, None]
    return individual, individual.sum(axis=0)
