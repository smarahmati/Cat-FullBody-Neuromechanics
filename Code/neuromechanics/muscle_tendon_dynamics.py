"""Elastic muscle-tendon dynamics; fiber length is an evolving state."""

from .solve_elastic_muscle_equilibrium import solve_elastic_muscle_equilibrium


def muscle_tendon_dynamics(state):
    """Solve fiber/tendon equilibrium with backward-Euler fiber velocity.

    Whole MT path length comes from current bones and attachment sites.
    Fiber length differs from MT length because the tendon can stretch.
    Forces returned here, in N, act on the skeleton on the next time step.
    """
    model, data = state["model"], state["data"]
    # Solve every muscle's fiber length, fiber speed, tension, residual and bound flag.
    length, velocity, force, residual, bound = solve_elastic_muscle_equilibrium(
        # Whole muscle-tendon length: routed path plus its fixed length offset (m).
        data.actuator_length + state["mtu_length_offset"],
        # Fiber length at the preceding time step (m).
        state["fiber_length"],
        # Current muscle activation, between zero and one.
        data.act,
        # Optimal fiber lengths used to normalize fiber extension (m).
        state["lopt"],
        # Unloaded series-tendon lengths (m).
        state["slack"],
        # Muscle strengths, pennation and force-curve parameters from configuration.
        state["muscle_params"],
        # Tendon strain when tension equals maximum isometric muscle force along the tendon direction.
        state["e0"],
        # Dimensionless damping of fiber motion.
        state["fiber_damping_coefficients"],
        # Elapsed mechanical step, in seconds, for backward-Euler fiber velocity.
        model.opt.timestep,
    )
    # Save the newly solved muscle state for output and the next mechanical step.
    state.update(
        fiber_length=length,
        fiber_velocity=velocity,
        force=force,
        # Remaining tendon-minus-muscle force imbalance (N).
        residual=residual,
        # Flag any fiber that reached a numerical/geometric length bound.
        fiber_bound=bound,
    )
    # Native length increases away from the origin; tensile force is negative
    # in this actuator convention. Maximum force is not multiplied twice.
    model.actuator_biasprm[:, 0] = -force
