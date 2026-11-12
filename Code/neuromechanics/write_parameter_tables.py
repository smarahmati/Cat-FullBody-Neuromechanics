"""Explain source and model values without requiring project history.

Inputs: parameters is the engine read-back; provenance supplies verified source
values and descriptions; output is the HTML report path. The main table compares
source values with values used in this model. This function changes no model parameter.
"""

import json, html, math

from pathlib import Path


def same_parameter_value(first, second):
    """Compare values without counting negligible round-off as a change."""
    if isinstance(first, (float, int)) and isinstance(second, (float, int)):
        return math.isclose(first, second, rel_tol=1e-10, abs_tol=1e-12)
    return first == second


def explain_parameter_change(row, actual):
    """Explain documented choices; explicitly identify missing rationale."""
    original = row['original']
    if not same_parameter_value(actual, row['applied']):
        return 'Changed in this run relative to the supplied release. The reason for this user-selected value is not recorded here.'
    if original is not None and same_parameter_value(original, actual):
        return 'Retained the verified source value; no numerical change from that source.'
    # Lack of a source value must not be mistaken for a measured parameter.
    status = ('No verified source value is available for direct comparison. ' if original is None
              else 'Different from the verified source value. ')
    if isinstance(original, (float, int)) and isinstance(actual, (float, int)) and original != 0:
        status += f'Change relative to source: {100 * (actual - original) / abs(original):+.3g}%. '
    field = row['field']
    name = row['name']
    # These are explanations of calibration/model choices, not new measurements.
    if field == 'max_isometric_muscle_force_along_tendon_N':
        reason = 'Force capacity was calibrated with motor inputs to improve mechanical agreement; the fit does not uniquely identify it.'
    elif field in ['optimal_fiber_length_m', 'max_fiber_speed_optimal_lengths_per_s'] and name.startswith(('FL_', 'FR_')):
        reason = ('Fiber length and shortening speed were calibrated to set the force-length and force-velocity operating ranges. '
                  'Physical maximum fiber speed is optimal_fiber_length_m multiplied by max_fiber_speed_optimal_lengths_per_s. '
                  'The source and applied numbers are given in this row; these are not new tissue measurements.')
    elif field == 'degroote_force_velocity_enabled':
        reason = 'Model-law choice: 1 enables the smooth De Groote force-velocity relation; 0 selects the alternative implemented law.'
    elif field == 'passive_fiber_enabled':
        reason = ('The published passive force-length law is included in every muscle channel. '
                  'Its coefficients are from Prilutsky et al. (2016), Table 10.3, and Rahmati et al. (2025), Table 3. '
                  'Applying the same normalized law to added muscle channels is a modeling assumption.')
    elif field == 'normalized_fiber_damping':
        reason = 'Effective muscle force-balance coefficient; source-law conversion and calibration are described in the methods.'
    elif field == 'tendon_strain_at_max_force':
        reason = 'Assumed elastic-tendon compliance; not a measured tendon strain for this animal.'
    elif field in ['normal_stiffness_N_m32', 'normal_dissipation_s_m', 'shear_stiffness_N_m', 'shear_damping_Ns_m', 'friction_coefficient']:
        reason = 'Effective paw-contact parameter from model calibration; not an independently measured paw-material constant.'
    elif field == 'COM_position_in_body_m' and name == 'cat_root':
        reason = 'Trunk center of mass was calibrated to adjust body balance and limb loading.'
    elif field == 'body_position_in_parent_m' and name in ['FL_scapula', 'FR_scapula']:
        reason = 'Forelimb mounting position was calibrated to improve whole-body geometry and loading.'
    elif field == 'passive_damping' and name in ['FL_wrist', 'FR_wrist', 'FL_mcp', 'FR_mcp']:
        reason = 'Distal forelimb passive damping was calibrated to improve mechanical behavior.'
    else:
        reason = 'The available record does not establish an individual source-to-model adjustment rationale; no more specific reason is claimed.'
    return status + reason


def parameter_source_description(row):
    """Return the scientific source statement supplied with a parameter."""
    return row.get('source', 'No verified source is established for this value.')


def write_parameter_tables(parameters, provenance, output):
    """Compare the verified scientific source directly with actual simulator values."""
    escape = lambda x: html.escape(
        json.dumps(x, ensure_ascii=False)
        if isinstance(x, (list, dict))
        else (f"{x:.8g}" if isinstance(x, float) else str(x))
    )
    groups = {}
    for row in provenance["parameters"]:
        # Accept recorded configurations with the former force-field name.
        # This changes table terminology only; the archived input stays untouched.
        row = dict(row)
        old_force_name = "max_isometric_tendon_force_N"
        force_name = "max_isometric_muscle_force_along_tendon_N"
        if row["category"] == "muscle_tendon" and row["field"] == old_force_name:
            row["field"] = force_name
            row["meaning"] = (
                "Maximum isometric muscle force (F0). "
                "The pennation projection is already included; do not apply it twice."
            )
        category = row["category"]
        name = row["name"]
        field = row["field"]
        if category == "initial_state":
            # Skip the remaining work for this item.
            continue
        actual = (
            parameters[category][name]
            if category == "environment"
            else parameters[category][name][
                old_force_name
                if field == force_name and force_name not in parameters[category][name]
                else field
            ]
        )
        cells = [
            name,
            field,
            row["unit"],
            row["meaning"],
            row["original"] if row["original"] is not None else "Not established",
            actual,
            explain_parameter_change(row, actual),
            parameter_source_description(row),
        ]
        groups.setdefault(category, []).append(
            "<tr>"
            + "".join("<td>" + escape(v) + "</td>" for v in cells)
            + "</tr>"
        )
    parts = [
        '<!doctype html><meta charset="utf-8"><title>Actual model parameter tables</title><style>body{margin:30px;font:16px/1.5 Arial;color:#19313e}table{border-collapse:collapse;font-size:13px;width:100%}th,td{border:1px solid #ccd5dc;padding:7px;text-align:left;overflow-wrap:anywhere}th{background:#e9f1f5;position:sticky;top:0}td{max-width:330px}th:nth-child(3),td:nth-child(3){min-width:52px}summary{font-size:20px;margin:25px 0;cursor:pointer}.note{background:#fff1d6;padding:16px}input{padding:9px;width:450px}</style>',
        '<h1>Source values and values used in this model</h1><p class="note"><strong>Source value:</strong> a verified value from the author’s original work or cited literature, in the listed units. '
        '<strong>Value used in this model:</strong> the actual value read back from the assembled simulation. '
        '<strong>What changed and why:</strong> the source-to-model difference and documented rationale. '
        '“Not established” means no verified numerical source value is available; the model value is an assumption, estimate or fitted value. '
        'Successful fitting does not prove that a fitted value is the animal’s true parameter.</p>',
        '<p>Positions use their specified local body frame. Initial conditions appear separately below. '
        'Displayed scalars use up to eight significant digits; saved JSON/CSV values retain full precision. '
        'Editing a parameter requires a new simulation and does not automatically retune excitation.</p>'
        '<input id="search" placeholder="Filter: e.g. R_VL, mass_kg, tendon, damping" oninput="filterRows(this.value)">',
    ]
    for category, rows in groups.items():
        parts.append(
            "<details "
            + ("open" if category == "muscle_tendon" else "")
            + "><summary>"
            + escape(category)
            + " ("
            + str(len(rows))
            + " entries)</summary><table><thead><tr>"
            + "".join(
                "<th>" + x + "</th>"
                for x in [
                    "Object",
                    "Parameter",
                    "Unit",
                    "Meaning",
                    "Source value",
                    "Value used in this model",
                    "What changed and why",
                    "Source / evidence",
                ]
            )
            + "</tr></thead><tbody>"
            + "".join(rows)
            + "</tbody></table></details>"
        )
    parts.append(
        "<h2>Initial conditions (only at t = 0)</h2><p>These are fitted simulation states, not a claim of measured fiber lengths or contact shear. They are never restored each cycle.</p>"
    )
    for kind, rows in parameters["initial_state"].items():
        parts.append(
            "<details><summary>"
            + escape(kind)
            + "</summary><table><tr><th>Object</th><th>Applied initial value</th></tr>"
            + "".join(
                "<tr><td>" + escape(k) + "</td><td>" + escape(v) + "</td></tr>"
                for k, v in rows.items()
            )
            + "</table></details>"
        )
    parts.append('<script>function filterRows(q){q=q.toLowerCase();document.querySelectorAll("tbody tr").forEach(r=>r.hidden=!r.textContent.toLowerCase().includes(q));'
                 'if(q)document.querySelectorAll("details:not([data-history])").forEach(d=>d.open=true)}</script>')
    # Save the computed values or figure for inspection and reproducibility.
    Path(output).write_text("".join(parts), encoding="utf-8")
