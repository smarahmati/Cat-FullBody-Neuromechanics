"""Build navigable folder guides and readable source listings from public files.

Run this from the project root after editing code or documentation:
    python Code/simulation_tools/generate_folder_guides.py
This changes HTML only; it never modifies numerical model inputs or results.
"""
from pathlib import Path
import ast
import html
import os
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
MARKER = '<!-- generated folder guide -->'
PURPOSE = {
    'Code': 'Executable model functions, parameter readers and simulation tools.',
    'neuromechanics': 'Activation, muscle–tendon mechanics, muscle paths, contact and coupled body dynamics.',
    'model_configuration': 'Parameter schema, default settings and configuration readers.',
    'simulation_tools': 'Tools to run, view and export simulations and build scientific documentation.',
    'Data': 'Model inputs, source parameters and experimental references.',
    'Model_Parameters': 'Editable anatomical, mechanical, activation, contact and numerical parameters.',
    'Muscle_Excitation_Input': 'Fixed dimensionless excitation u(t), from 0 to 1. This is the motor input, not computed activation.',
    'Experimental_Reference_Data': 'Experimental and explicitly assumed comparison signals; these never impose motion or force.',
    'Original_Study_Data': 'Original research tables and implementations. Original filenames are retained for source traceability.',
    'Skeletal_Geometry': 'Mechanical topology and geometry. Optional surface meshes affect visualization only.',
    'Recorded_EMG': 'EMG envelope references; provenance identifies the recorded, mirrored and pooled channels.',
    'Inverse_Estimates': 'Inverse-estimated reference signals, distinct from direct measurements.',
    'Ground_Reaction_Forces': 'Paw forces in newtons: Fx anterior–posterior, Fy lateral, Fz vertical.',
    'Joint_Kinematics': 'Joint angles and generalized motion; headers specify radians/degrees and derivative units.',
    'Joint_Moments': 'Reference joint moments from inverse dynamics, not imposed simulation torques.',
    'Muscle_Excitation': 'Prescribed muscle excitation u(t), dimensionless, before activation dynamics.',
    'Muscle_Activation': 'Computed muscle activation a(t), dimensionless, after activation dynamics.',
    'Muscle_Forces': 'Computed muscle–tendon tension and passive-fiber contribution in newtons.',
    'Muscle_Tendon_States': 'Fiber, MTU and tendon lengths (m), fiber velocity (m/s), normalized fiber length and tendon strain.',
    'Moment_Arms': 'Signed muscle moment arms in metres for rotational coordinates.',
    'Muscle_Joint_Moments': 'Muscle generalized forces: N m for rotational and N for translational coordinates.',
    'Body_Motion': 'Predicted body centres and paw positions in world coordinates, metres.',
    'Model_Parameters_Used': 'Exact physical parameters and excitation used for this saved simulation.',
    'Experimental_References_Used': 'Exact reference tables used for comparison with the saved simulation.',
    'Simulation_Code_Used': 'Implementation recorded with this saved numerical calculation.',
    'Documentation': 'Scientific methods, instructions, parameter tables, figures and references.',
    'Code_Reference': 'Line-numbered source listings linked to the scientific flowcharts.',
    'Figures_and_Videos': 'Scientific comparison plots, muscle schematics and walking animation.',
    'References': 'Scientific papers, citations and links to original sources.',
    'Verification': 'Executable equation checks and complete intact-walking reproduction.',
    'Simulation_Results': 'Complete intact-cat simulation and its computed variables.',
    'Intact_Walking': '60-second intact forward simulation, raw states and experimental comparisons.',
    'excitation_cycle.tsv': 'One prescribed cycle: phase plus 104 dimensionless excitation columns.',
    'muscle_input_dictionary.csv': 'Channel identifiers, limb, anatomy, function and source/measurement status.',
    'forward_simulation_timeseries.npz': 'Raw integrated states, excitation, activation, muscle force and paw-contact force arrays.',
    'simulation_summary.json': 'Requested and computed duration, fall outcome, mass and computation time.',
    'simulation_report.html': 'Simulation plots and quantitative comparison with experimental references.',
    'experimental_comparison_metrics.json': 'Joint-angle, force and EMG comparison metrics.',
    'walking_quality_metrics.json': 'Specified walking-quality criteria and their measured values.',
    'OUTPUT_DICTIONARY.json': 'Definitions, units, axes and limitations of every output category.',
    'INPUT_HASHES.json': 'Checksums identifying the exact parameter and reference copies.',
    'PARAMETER_PROVENANCE.json': 'Verified source values, applied values, units and scientific attribution.',
    'TABLE_MANIFEST.json': 'Reference file paths, units, array shapes and phase convention.',
    'INPUT_PROVENANCE.json': 'Experimental origin and assumptions for the reference signals.',
}

# These explanations appear beside navigation links, before a reader opens them.
PURPOSE.update({
    'Experimental_Reference_Data': 'Joint angles, paw forces and EMG used to assess the prediction. RH is recorded, LH is an assumed mirror, and forelimb references come from a separate study. These curves do not drive the motion during a forward run.',
    'Muscle_Excitation_Input': 'The excitation waveform supplied to every muscle channel. excitation_cycle.tsv stores one cycle of dimensionless commands between 0 and 1; the simulator repeats this cycle and computes activation from it.',
    'Model_Parameters': 'Editable values for body mass and inertia, joints, muscle attachments, activation, muscle–tendon mechanics, contact and the initial state. Source-to-model tables explain the origin and applied value of each documented parameter.',
    'Skeletal_Geometry': 'The connected body and joint structure and its geometric data. This determines where forces act and how segments move. Optional bone surface meshes change the appearance, not the mechanical calculation.',
    'Original_Study_Data': 'Original numerical tables and MATLAB files from the hindlimb and forelimb studies, retained to trace the scientific sources. The organized parameter and excitation files define the inputs used by run.py.',
    'neuromechanics': 'Functions that calculate excitation, activation, muscle and tendon forces, paw contact, coupled body motion and output comparisons. Each file represents a named part of the calculation.',
    'model_configuration': 'Code that defines parameter names, validates their organization and locates project files. To change physical values for a simulation, edit Data/Model_Parameters.',
    'simulation_tools': 'Commands for running the model, playing its saved movement, exporting figures and preparing documentation. The root run.py is the normal entry point.',
    'additional_muscles': 'Source architecture and grouping information for additional muscle paths, including toe and forelimb channels. These source records support the applied anatomy in Model_Parameters.',
    'forelimb': 'Original forelimb parameter, EMG-processing and muscle-grouping records. Forelimb experimental references are from a separate study, not the same trial as the hindlimb recording.',
    'hindlimb': 'Original hindlimb walking records, muscle parameters, geometry and inverse-estimated activations. Trial labels identify the source data associated with the supplied model.',
    'matched_trial': 'Original muscle, geometry and activation files associated with the selected hindlimb walking trial. They document how the source trial was characterized.',
    'matched_trial_geometry.json': 'Geometry values associated with the selected hindlimb trial; used to identify the source dimensions and muscle-length conventions.',
    'optimized': 'Activation estimates from the original hindlimb inverse analysis, grouped by source animal. These estimates are distinct from measured EMG and the applied forward excitation table.',
    'Brad': 'Original inverse-analysis records for the animal labeled Brad. Numbered filenames identify trials within that dataset.',
    'Ted': 'Original inverse-analysis records for the animal labeled Ted. Numbered filenames identify trials within that dataset.',
    'geometry_M2': 'Source MATLAB geometry and segment tables. The original source label is retained to identify the formulation and data used for anatomical calculations.',
    'geometry_audit': 'Original forelimb MATLAB source used to inspect geometric calculations and coordinate conventions.',
    'Model': 'Mechanical model files that define the connected bodies, joints and muscle transmission paths.',
    'articulated_girdle': 'Body and joint topology with an articulated shoulder girdle, numerical mechanics and muscle data. Applied parameter overrides are stored separately in Model_Parameters.',
    'Recorded_EMG': 'Available measured or pooled EMG envelopes and their provenance. EMG is normalized for shape comparison; it is not a direct measurement of absolute muscle excitation or activation.',
    'Inverse_Estimates': 'Excitation and activation estimated by the source inverse analysis. They are model estimates, not recorded EMG, and are not the complete 104-channel motor input used in this forward model.',
    'Joint_Kinematics': 'Joint-angle and motion tables. Reference tables describe the comparison target; result tables contain predicted motion. Each filename or column specifies whether angles are in radians or degrees.',
    'Ground_Reaction_Forces': 'Paw forces in newtons. Fx is anterior–posterior (negative braking, positive propulsion), Fy is lateral and Fz is vertical. Reference forces are comparison targets; simulated forces are calculated from paw contact.',
    'Joint_Moments': 'Information about joint-moment references. No synchronized four-limb measured moment series is supplied; original hindlimb inverse-analysis records remain in Original_Study_Data.',
    'activation_0_to_1.csv': 'Computed activation a(t) after activation dynamics, dimensionless. It changes with a time lag relative to excitation.',
    'excitation_0_to_1.csv': 'Applied excitation u(t), dimensionless, sampled on the simulation clock. This is the prescribed motor command.',
    'tendon_tension_N.csv': 'Muscle–tendon tensile force in newtons, obtained from elastic tendon and fiber equilibrium.',
    'passive_fiber_tendon_component_N.csv': 'Passive fiber contribution projected along the tendon, in newtons. It is already included in total tension and must not be added to tendon_tension_N again.',
    'raw_paw_forces_N.csv': 'Unfiltered calculated paw forces for every limb, in newtons, on the absolute simulation clock.',
    'anatomical_joint_angles_deg.csv': 'Predicted angles between adjacent anatomical segments, in degrees, using the same convention as the comparison figures.',
    'generalized_positions.csv': 'Predicted model coordinates: metres for translations and radians for rotations. These coordinates are not all anatomical joint angles.',
    'generalized_velocities.csv': 'Predicted coordinate velocities: m/s for translations and rad/s for rotations.',
    'acceleration_from_saved_velocities.csv': 'Accelerations estimated by differentiating the saved velocities; these are not the internal integration-step accelerations.',
    'elastic_tendon_length_m.csv': 'Computed elastic tendon length in metres; compare with tendon slack length to determine stretch.',
    'fiber_length_m.csv': 'Computed muscle-fiber length in metres, distinct from total muscle–tendon path length.',
    'fiber_velocity_m_s.csv': 'Computed fiber shortening or lengthening rate in metres per second.',
    'normalized_fiber_length.csv': 'Fiber length divided by optimal fiber length; a dimensionless ratio used in force–length relationships.',
    'tendon_strain.csv': 'Dimensionless tendon extension relative to slack length, (length − slack length) / slack length.',
    'signed_transmission_moment_arms.npz': 'Signed muscle leverage calculated from the path derivative −dL_MT/dq. Rotational-coordinate moment arms are in metres.',
    'individual_contributions.npz': 'Each muscle’s generalized force contribution from its tendon tension and transmission geometry. Rotational contributions are moments in N m.',
    'summed_muscle_generalized_forces.csv': 'Sum of all muscle contributions at each coordinate. These exclude contact and passive joint contributions, so they are not total inverse-dynamics moments.',
    'body_and_paw_positions.npz': 'Predicted body and paw positions in world coordinates, in metres.',
    'joint_q.tsv': 'Reference joint-coordinate cycles in radians. Use the documented anatomical conversion before comparing them with angle plots in degrees.',
    'grf.tsv': 'Reference force cycles for all four paws, in newtons. Column labels identify limb, axis and whether the reference is recorded or assumed.',
    'hip_x.tsv': 'Reference hip position along the direction of progression, in metres.',
    'hip_z.tsv': 'Reference hip height in metres.',
    'pelvis_angle.tsv': 'Reference pelvis orientation in radians.',
    'pelvis_angular_velocity.tsv': 'Reference pelvis angular velocity in rad/s.',
    'scapula_angle.tsv': 'Reference scapula orientation in radians.',
    'scapula_angle_by_side.tsv': 'Side-specific scapula reference orientations in radians.',
    'shoulder_z.tsv': 'Reference shoulder height in metres.',
    'shoulder_z_by_side.tsv': 'Side-specific reference shoulder heights in metres.',
    'left_joint_correction_rad.tsv': 'Saved left-side assembly correction in radians used with the assumed mirrored hindlimb reference; this is not a measured left-side recording.',
    'excitation.tsv': 'Source inverse-estimated excitation reference, dimensionless; the applied 104-channel input is in Muscle_Excitation_Input/excitation_cycle.tsv.',
    'optimized_activation.tsv': 'Source inverse-estimated activation reference, dimensionless; it is not activation calculated by the current forward run.',
    'phase_aligned_available_EMG.csv': 'Available peak-normalized EMG envelopes on the comparison phase grid. Only channels with available source EMG are represented.',
    'FHL_peak_normalized.tsv': 'Peak-normalized flexor hallucis longus EMG envelope used for shape comparison.',
    'EMG_PROVENANCE.json': 'Identifies the EMG source, channel correspondence and normalization/availability limitations.',
    'hindlimb_flexor_hallucis_longus_emg.npz': 'Numerical flexor hallucis longus EMG reference, with its source sampling information. Used for waveform comparison, not as an imposed activation state.',
    'aligned_forelimb_EMG_individual_cycles.npz': 'Available individual forelimb EMG cycles on the comparison phase grid; the source recordings are from a separate study.',
    'hindlimb_forelimb_reference_cycles.npz': 'Named arrays of the hindlimb and forelimb comparison cycles, including their phase convention and reference signals.',
    'right_hindlimb_walking_reference.npz': 'Right hindlimb walking reference arrays associated with the selected source trial.',
    'hindlimb_pose_initialization.npz': 'Source arrays for constructing the initial hindlimb pose. The applied starting state is recorded in Model_Parameters/initial_state.py.',
    'paw_contact_initialization.npz': 'Stored source arrays associated with preparing paw contact and the starting state; the live run calculates forces from its current mechanics.',
    'model_parameter_values.csv': 'Human-readable table of source values, applied values, units and explanations of parameter differences.',
    'ATTACHMENT_MAP.html': 'Readable map of muscle origins, insertions and intermediate routing points, with their body-local coordinates.',
    'ATTACHMENT_MAP.json': 'Machine-readable muscle attachment and routing coordinates corresponding to the anatomical map.',
    'APPLIED_PARAMETER_READBACK.json': 'Parameter values read back from the assembled mechanical model, for checking what was actually applied.',
    'mechanics_exact.npz': 'Numerical body and joint properties used when assembling the skeletal dynamics.',
    'muscle_parameters.npz': 'Numerical muscle architecture and strength arrays associated with the mechanical model.',
    'cat.xml': 'MuJoCo model topology: connected bodies, joints, geometric objects and muscle paths.',
    'ASSUMPTIONS.json': 'Documented geometric and model-assembly assumptions.',
    'activation.py': 'Activation and deactivation time constants governing how quickly excitation changes muscle activation. Values are in seconds.',
    'muscle_tendon.py': 'Per-channel strength, optimal fiber length, tendon slack length, pennation, damping and force-law settings. Units and source values appear beside the applied entries.',
    'attachments.py': 'Muscle origins, insertions and intermediate attachment coordinates relative to the named bones. Changing a point changes the muscle path, length and moment arms.',
    'bodies.py': 'Body mass, center-of-mass location and inertia used in coupled skeletal dynamics.',
    'joints.py': 'Joint properties, including mechanical limits and passive stiffness or damping where specified.',
    'contact.py': 'Paw-pad geometry, normal stiffness and dissipation, tangential stiffness and friction parameters used to predict GRFs.',
    'environment.py': 'Environmental settings such as gravity and ground properties.',
    'initial_state.py': 'Starting mechanical and internal states applied once when a forward run begins.',
    'simulation_settings.py': 'Run configuration and fixed-excitation timing settings.',
    'numerical_parameters.py': 'Integration and sampling settings, including time steps and numerical tolerances.',
    'formulation_constants.py': 'Shared constants in the implemented activation, muscle–tendon and contact equations.',
    'routing.py': 'Rules defining how muscle paths follow the articulated skeleton.',
    'wrapping.py': 'Geometric wrapping settings where supported by the configured muscle paths.',
    'interactive_experimental_comparison.html': 'Browse any interval of the 60-second trial with a movable time window, limb selection, joint-angle and GRF plots.',
    'data_manifest.json': 'Inventory of supplied data files with their purpose, byte size and checksum for file-integrity checks.',
    'Open_Access_Papers': 'Redistributable scientific article copies. The reference library identifies each paper and its role in the model.',
})


def describe(path):
    """Explain each item from its scientific role or Python module documentation."""
    if path.name in PURPOSE:
        return PURPOSE[path.name]
    if path.suffix == '.py':
        try:
            return (ast.get_docstring(ast.parse(path.read_text(encoding='utf-8'))) or path.stem.replace('_',' ')).split('\n')[0]
        except (SyntaxError, UnicodeError):
            pass
    if 'Original_Study_Data' in path.parts:
        if path.name.startswith('Activations_'):
            return 'Original inverse-analysis activation estimates for the trial number in the filename; not a measured EMG recording.'
        if path.suffix == '.m':
            return 'Original MATLAB source for the cited study. Open it to inspect its equations, variable names and source parameter conventions.'
        if path.suffix == '.mat':
            return 'Original MATLAB numerical data. Open with MATLAB or scipy.io.loadmat to inspect named variables; source units and conventions follow the associated study code.'
        return 'Original study source record documenting its data or anatomical calculations; retained for scientific traceability.'
    return path.stem.replace('_',' ') + ({'.csv': ' — table with named columns.', '.tsv': ' — tab-separated signal table.', '.npz': ' — named numerical arrays.', '.json': ' — machine-readable data/metadata.', '.png': ' — figure.', '.svg': ' — scalable diagram.', '.mp4': ' — walking animation.'}.get(path.suffix,'.'))


def link(page, target):
    """Return a portable relative link for downloaded HTML and GitHub Pages."""
    return os.path.relpath(target,page.parent).replace('\\','/')


def explain_navigation_lists(page):
    """Add meaning beside bare local-file bullets without changing detailed prose."""
    original = page.read_text(encoding='utf-8')

    def explain(match):
        address = html.unescape(match.group(1))
        parsed = urlsplit(address)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)
        target = (page.parent / unquote(parsed.path)).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            return match.group(0)
        item = target.parent if target.name == 'index.html' else target
        # Folder labels follow their current descriptive names; source file names stay exact.
        label = item.name.replace('_', ' ') if item.is_dir() else item.name
        return f'<li><a href="{html.escape(address, quote=True)}">{html.escape(label)}</a> — {html.escape(describe(item))}</li>'

    updated = re.sub(r'<li>\s*<a href="([^"]+)">[^<]+</a>(?:\s*—[^<]*)?\s*</li>', explain, original)
    # Scientific result guides describe their contents, not the packaging workflow.
    updated = updated.replace('Fresh forward result with passive fiber force in all 104 channels; no fine-tuning.', 'Computed intact-cat forward results. The columns and named arrays below describe the simulated quantities.')
    if updated != original:
        page.write_text(updated, encoding='utf-8')


def write_page(page,title,body):
    """Use the common documentation style without an external web dependency."""
    page.parent.mkdir(parents=True,exist_ok=True)
    page.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><link rel="stylesheet" href="{link(page,ROOT/"Documentation/style.css")}"></head><body>{MARKER}<header><div class="tag">Cat · Full-body neuromechanics</div><h1>{html.escape(title)}</h1><nav><a href="{link(page,ROOT/"START_HERE.html")}">Start here</a> · <a href="{link(page,ROOT/"Documentation/project_structure.html")}">Find a file</a></nav></header><main>{body}</main></body></html>',encoding='utf-8')


def main():
    """Generate only from Git's public inventory; ignored local data stays private."""
    output=subprocess.check_output(['git','-C',str(ROOT),'ls-files','--cached','--others','--exclude-standard','-z']).decode('utf-8')
    files=sorted({ROOT/p for p in output.split('\0') if p and (ROOT/p).is_file()})
    folders={q for p in files for q in p.parents if q.is_relative_to(ROOT)}
    for page in files:
        if page.suffix == '.html' and 'Code_Reference' not in page.parts:
            explain_navigation_lists(page)
    for folder in sorted(folders):
        if folder==ROOT or any(x.startswith('.') for x in folder.relative_to(ROOT).parts):continue
        page=folder/'index.html'
        if page.exists() and MARKER not in page.read_text(encoding='utf-8'):continue
        children=sorted({p if p.parent==folder else folder/p.relative_to(folder).parts[0] for p in files if p.is_relative_to(folder) and p!=page},key=lambda p:(not p.is_dir(),p.name.lower()))
        rows=''.join(f'<tr><td><a href="{html.escape(link(page,p/"index.html" if p.is_dir() else p))}">{html.escape(p.name)}</a></td><td>{html.escape(describe(p))}</td></tr>' for p in children)
        write_page(page,folder.name.replace('_',' '),f'<p>{html.escape(describe(folder))}</p><p><code>{folder.relative_to(ROOT).as_posix()}</code></p><table><tr><th>File or folder</th><th>Purpose and units</th></tr>{rows}</table>')
    guide=ROOT/'Documentation/project_structure.html'
    paths=['run.py','view.py','reproduce.py','Code/neuromechanics','Code/model_configuration','Code/simulation_tools','Data/Model_Parameters','Data/Muscle_Excitation_Input','Data/Experimental_Reference_Data','Data/Original_Study_Data','Data/Skeletal_Geometry','Simulation_Results/Intact_Walking','Verification','Documentation/References','Documentation/Figures_and_Videos']
    rows=''.join(f'<tr><td><a href="{link(guide,ROOT/p/"index.html" if (ROOT/p).is_dir() else ROOT/p)}"><code>{p}</code></a></td><td>{html.escape(describe(ROOT/p))}</td></tr>' for p in paths)
    write_page(guide,'Project folders and files','<p>Start with run.py. Model parameters, prescribed excitation, experimental references and computed results have separate, descriptive folders. Each folder has a navigation guide.</p><table><tr><th>Path from project root</th><th>Purpose</th></tr>'+rows+'<h2>Names and scientific identifiers</h2><p>Scientific muscle channel identifiers are defined in the <a href="muscle_dictionary.html">muscle dictionary</a>. Original research filenames remain unchanged for traceability. README.md, index.html and __init__.py follow standard GitHub, website and Python conventions.</p>')
    count=0
    for source in files:
        if source.suffix!='.py' or 'Simulation_Results' in source.parts:continue
        relative=source.relative_to(ROOT).as_posix()
        target=ROOT/'Documentation/Code_Reference'/(relative.replace('/','__')+'.html')
        lines=''.join(f'<span id="L{i}">{i:4}</span> {html.escape(line)}\n' for i,line in enumerate(source.read_text(encoding='utf-8').splitlines(),1))
        write_page(target,describe(source),f'<p><a href="{link(target,source)}">{relative}</a></p><pre style="overflow:auto;white-space:pre">{lines}</pre>')
        count+=1
    print(f'Generated folder guides and {count} source-code pages.')


if __name__=='__main__':
    main()
