"""Export readable time series and mechanics derived from SAVED forward states.

This postprocessing does not change the simulated trajectory. CSV files use
seconds and SI units; anatomical joint angles are also exported in degrees.
Dense muscle-by-coordinate arrays are compressed in NPZ to keep files small.
"""
import json
from pathlib import Path
import numpy as np
import mujoco as mj
from .update_muscle_paths import update_muscle_paths
from .muscle_moment_arms import muscle_moment_arms
from .muscle_joint_moments import muscle_joint_moments
from .muscle_force_length_velocity import muscle_force_length_velocity


def save_table(path, times, values, columns):
    """Write a CSV with explicit column names and a time_s first column."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    matrix = np.asarray(values).reshape(len(times), -1)
    np.savetxt(path, np.column_stack((times, matrix)), delimiter=',',
               header=','.join(['time_s'] + list(columns)), comments='', fmt='%.10g')


def export_biomechanics(result, state, folder):
    """Export input, activation, fiber/tendon, motion, force and moment folders."""
    folder = Path(folder)
    times = result['time']
    muscles = [str(n) for n in result['names']]
    coordinates = [str(n) for n in result['coordinate_names']]
    paths = {
        'excitation': ('Muscle_Excitation/excitation_0_to_1.csv', ''),
        'activation': ('Muscle_Activation/activation_0_to_1.csv', ''),
        'force': ('Muscle_Forces/tendon_tension_N.csv', '_N'),
        'fiber_length': ('Muscle_Tendon_States/fiber_length_m.csv', '_m'),
        'fiber_velocity': ('Muscle_Tendon_States/fiber_velocity_m_s.csv', '_m_s'),
        'mtu_length': ('Muscle_Tendon_States/whole_MTU_length_m.csv', '_m'),
        'tendon_length': ('Muscle_Tendon_States/elastic_tendon_length_m.csv', '_m'),
    }
    for key, (name, unit) in paths.items():
        save_table(folder/name, times, result[key], [m+unit for m in muscles])
    # Evaluate the parallel elastic contribution at each saved fiber length.
    # F0 is already tendon-projected in this model: no extra cos(alpha) factor.
    # This component is included in the fiber/tendon equilibrium during solving;
    # it is NOT an additional external force applied a second time afterwards.
    parameters = state['muscle_params']
    normalized_length = result['fiber_length'] / result['optimal_fiber_length_m']
    passive_force = np.zeros_like(normalized_length)
    for channel in range(len(muscles)):
        for sample in range(len(times)):
            passive_factor = muscle_force_length_velocity(
                normalized_length[sample, channel], 0.0, parameters[channel]
            )[2]
            passive_force[sample, channel] = parameters[channel, 2] * passive_factor
    save_table(folder/'Muscle_Forces/passive_fiber_tendon_component_N.csv',
               times, passive_force, [m+'_N' for m in muscles])
    save_table(folder/'Muscle_Tendon_States/normalized_fiber_length.csv',
               times, normalized_length, muscles)
    passive_audit = {
        'law': 'Prilutsky 2016 Table 10.3 / Rahmati 2025 Table 3, tension-only adaptation',
        'enabled_channels': int(np.count_nonzero(parameters[:, 13] > 0)),
        'total_channels': len(muscles),
        'channels': {name: {
            'enabled': bool(parameters[i, 13] > 0),
            'maximum_normalized_fiber_length': float(normalized_length[:, i].max()),
            'peak_passive_tendon_component_N': float(passive_force[:, i].max()),
        } for i, name in enumerate(muscles)},
    }
    (folder/'passive_fiber_force_summary.json').write_text(json.dumps(passive_audit, indent=2))
    strain = result['tendon_length']/state['slack'] - 1
    save_table(folder/'Muscle_Tendon_States/tendon_strain.csv', times, strain, muscles)
    save_table(folder/'Joint_Kinematics/generalized_positions.csv', times, result['qpos'], coordinates)
    save_table(folder/'Joint_Kinematics/generalized_velocities.csv', times, result['qvel'], coordinates)
    # Finite differences of saved velocities are clearly labelled; they are not
    # presented as exact integration-step accelerations.
    acceleration = np.gradient(result['qvel'], times, axis=0) if len(times)>1 else np.zeros_like(result['qvel'])
    save_table(folder/'Joint_Kinematics/acceleration_from_saved_velocities.csv', times, acceleration, coordinates)
    joint_names = [side+'_'+j for side, joints in [('LH',['hip','knee','ankle','MTP']),('RH',['hip','knee','ankle','MTP']),('LF',['shoulder','elbow','wrist','MCP']),('RF',['shoulder','elbow','wrist','MCP'])] for j in joints]
    anatomical = np.empty_like(result['joint_q'])
    for side in range(4):
        signs = np.array([-1,1,-1,-1]) if side<2 else np.array([1,-1,-1,-1])
        offset = np.array([0,np.pi,np.pi,np.pi]) if side<2 else np.full(4,np.pi)
        anatomical[:,side] = np.rad2deg(offset+signs*result['joint_q'][:,side])
    save_table(folder/'Joint_Kinematics/anatomical_joint_angles_deg.csv',times,anatomical,joint_names)
    save_table(folder/'Ground_Reaction_Forces/raw_paw_forces_N.csv',times,result['grf'],[s+'_'+axis+'_N' for s in ['LH','RH','LF','RF'] for axis in ['Fx','Fy','Fz']])

    # Reconstruct geometry on the completed state workspace. No stepping,
    # contact force recalculation or motor adaptation occurs here.
    model, data = state['model'], state['data']
    arms = np.empty((len(times),model.nu,model.nv))
    moments = np.empty_like(arms)
    paw_positions = np.empty((len(times),4,3))
    body_positions = np.empty((len(times),model.nbody,3))
    for row in range(len(times)):
        data.qpos[:] = result['qpos'][row]
        data.qvel[:] = result['qvel'][row]
        update_muscle_paths(state)
        mj.mj_fwdPosition(model,data)
        arms[row] = muscle_moment_arms(model,data)
        moments[row], _ = muscle_joint_moments(arms[row],result['force'][row])
        paw_positions[row] = data.site_xpos[state['paw_ids']]
        body_positions[row] = data.xipos
    for directory in ['Moment_Arms','Muscle_Joint_Moments','Body_Motion']:
        (folder/directory).mkdir(exist_ok=True)
    np.savez_compressed(folder/'Moment_Arms/signed_transmission_moment_arms.npz',time=times,values=arms,muscle_names=muscles,coordinate_names=coordinates)
    np.savez_compressed(folder/'Muscle_Joint_Moments/individual_contributions.npz',time=times,values=moments,muscle_names=muscles,coordinate_names=coordinates)
    save_table(folder/'Muscle_Joint_Moments/summed_muscle_generalized_forces.csv',times,moments.sum(axis=1),coordinates)
    np.savez_compressed(folder/'Body_Motion/body_and_paw_positions.npz',time=times,paw_positions=paw_positions,body_com_positions=body_positions,body_names=[model.body(i).name for i in range(model.nbody)])
    metadata = {
        'time':'s; absolute simulation clock',
        'muscle_input':'excitation; prescribed in advance; no sensory feedback',
        'force':'positive tensile force, N',
        'passive_fiber_tendon_component':'F0 * fP(l_f/l_opt), N; evaluated at saved fiber state; included inside muscle equilibrium, not added again to tendon tension; zero below stretch threshold even when enabled',
        'generalized_units':'hinges: rad, rad/s, rad/s^2 and N m; sliders: m, m/s, m/s^2 and N',
        'moments':'muscle-only generalized contributions; no claim of inverse-dynamics or reaction moments',
        'axes':'world +x progression, +z upward; anterior–posterior (AP) Fx can be braking (<0) or propulsive (>0)',
        'moment_arm':'-dL_MT/dq from the actual engine transmission; same moving route geometry as simulation',
        'accelerations':'finite differences of saved velocities, not exact step acceleration',
        'reference_scope':'RH measured; LH assumed mirror; forelimbs separate study, EMG pooled',
    }
    (folder/'OUTPUT_DICTIONARY.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
