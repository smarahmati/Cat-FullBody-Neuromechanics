"""Common collapse/contact criterion for optimization trials and validation."""

from model_configuration.formulation_constants import FALL_PELVIS_HEIGHT_M, FALL_ROOT_PITCH_RAD


def detect_body_fall(model, data):
    """A low pelvis, excessive pitch, or head/trunk contact terminates walking.

    These are explicit simulation failure criteria, not clinical thresholds.
    They do not generate support forces or modify the simulated state.
    """
    if data.qpos[1] < FALL_PELVIS_HEIGHT_M or abs(data.qpos[2]) > FALL_ROOT_PITCH_RAD:
        return True
    for contact in data.contact:
        names = [model.geom(int(i)).name for i in [contact.geom1, contact.geom2]]
        if "ground_contact" in names and any("head" in n or "torso" in n for n in names):
            return True
    return False
