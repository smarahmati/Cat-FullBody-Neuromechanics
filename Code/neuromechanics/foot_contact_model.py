"""Physical paw-contact interface; no experimental force is imposed."""

from .compute_paw_contact_forces import compute_paw_contact_forces


def foot_contact_model(state, time_step_s):
    """Update pad deformation, shear memory, Ground_Reaction_Forces and body contact wrenches.

    The equations are in viscoelastic_paw_pad.py, and pad-to-body moment
    transfer is in sum_paw_contact_forces_and_moments.py. Each pad has its own config values.
    """
    # Calculate all four paw forces from current deformation/slip, advancing shear memory.
    compute_paw_contact_forces(state, time_step_s)
