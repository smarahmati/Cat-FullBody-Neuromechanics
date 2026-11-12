"""One complete forward step, with named physical subsystems."""

import numpy as np

from model_configuration.numerical_parameters import MAXIMUM_GENERALIZED_SPEED

import mujoco as mj

from .muscle_excitation import muscle_excitation

from .multibody_system_dynamics import multibody_system_dynamics

from .update_muscle_paths import update_muscle_paths

from .muscle_tendon_dynamics import muscle_tendon_dynamics

from .foot_contact_model import foot_contact_model


def advance_neuromechanical_timestep(state):
    """Fixed muscle_excitation -> activation/motion -> elastic force/contact update.

    This is the same partitioned numerical scheme as the optimized research
    step. References are absent from this loop. There is no feedback command,
    target-angle enforcement, external balance support or stride reset.
    """
    # Get the common skeleton and its current positions, velocities and activation.
    model, data = state["model"], state["data"]
    # Read this instant's fixed motor inputs, from the prescribed intact input table.
    motor_input = muscle_excitation(state, data.time)
    # Advance activation and motion using the muscle/contact forces already computed.
    multibody_system_dynamics(state, motor_input)
    # Move the analytical via points with the updated bones and joint angles.
    update_muscle_paths(state)
    # Recalculate positions and routed muscle lengths at the new pose.
    mj.mj_fwdPosition(model, data)
    # Recalculate velocities at the new pose and generalized speed.
    mj.mj_fwdVelocity(model, data)
    # Solve the new elastic tendon-fiber force balance at the updated MT lengths.
    muscle_tendon_dynamics(state)
    # Update pad compression, shear memory, Ground_Reaction_Forces and their moments on the skeleton.
    foot_contact_model(state, model.opt.timestep)
    # Tell the outer simulation loop whether this step remains numerically usable.
    return bool(
        # Every coordinate must be a finite number.
        np.isfinite(data.qpos).all()
        # Every tendon force must be a finite number.
        and np.isfinite(state["force"]).all()
        # Reject an extreme speed indicating numerical divergence.
        and np.max(abs(data.qvel)) < MAXIMUM_GENERALIZED_SPEED
    )
