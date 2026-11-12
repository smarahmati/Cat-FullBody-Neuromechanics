"""Write an inspectable, per-muscle map from actual engine geometry."""

import html

import json

import re

from pathlib import Path

import numpy as np

from .describe_muscle_paths import describe_muscle_paths

from .attachment_equations import EQUATIONS


def write_attachment_map(state, output):
    """Save connections/frames at the current pose; does not alter the model.

    Coordinates are in metres in the named body frame. The world-coordinate
    columns and frame axes are only a snapshot, not fixed points in space.
    """
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    m = state["model"]
    d = state["data"]
    paths = describe_muscle_paths(state)
    frames = []
    for i in range(1, m.nbody):
        frames.append(
            dict(
                body=m.body(i).name,
                parent=m.body(int(m.body_parentid[i])).name,
                origin_in_parent_m=m.body_pos[i].tolist(),
                quaternion_in_parent_wxyz=m.body_quat[i].tolist(),
                world_origin_m=d.xpos[i].tolist(),
                local_axes_in_world_columns=d.xmat[i].reshape(3, 3).tolist(),
            )
        )
    record = dict(
        configuration=state["settings"].get("parameter_bundle_dir", "legacy settings"),
        time_s=float(d.time),
        units="metres; xyz in each named body frame",
        scope="Actual model connections, not an independent anatomical validation. Model-space registration and some attachment regions are estimated.",
        muscles=paths,
        body_frames=frames,
    )
    # Save the computed values or figure for inspection and reproducibility.
    (out / "ATTACHMENT_MAP.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    esc = lambda x: html.escape(str(x))
    vec = lambda x: "[" + ", ".join(f"{v:.8g}" for v in x) + "]"
    rows = []
    for muscle in paths:
        body_rows = []
        order = 0
        for bindex, branch in enumerate(muscle["branches"]):
            for e in branch["elements"]:
                order += 1
                if e["kind"] == "site":
                    description = e["role"] + (
                        " — computed moving point"
                        if e["moving"]
                        else " — body-fixed"
                    )
                    local = vec(e["local_position_m"])
                    world = vec(e["world_position_m"])
                else:
                    description = (
                        e["shape"]
                        + " wrap, radius "
                        + f"{e['radius_m']*1000:.5g}"
                        + " mm"
                    )
                    local = vec(e["local_position_m"])
                    world = "wrap surface, not an attachment"
                vals = [
                    order,
                    bindex + 1,
                    e["name"],
                    description,
                    e["body"],
                    local,
                    world,
                    e["editable_file"],
                ]
                body_rows.append(
                    "<tr>"
                    + "".join("<td>" + esc(v) + "</td>" for v in vals)
                    + "</tr>"
                )
                if e["kind"] == "wrap" and e["side_site"]:
                    side = e["side_site"]
                    role = "side selector (NOT a point the path passes through)"
                    if side["moving"]:
                        role += "; computed"
                    vals = [
                        "—",
                        bindex + 1,
                        side["name"],
                        role,
                        side["body"],
                        vec(side["local_position_m"]),
                        "—",
                        side["editable_file"],
                    ]
                    body_rows.append(
                        '<tr class="side">'
                        + "".join("<td>" + esc(v) + "</td>" for v in vals)
                        + "</tr>"
                    )
        rows.append(
            '<details class="muscle"><summary>'
            + esc(muscle["muscle"])
            + "</summary><p>Native path = "
            + f"{muscle['path_length_m']*1000:.6f}"
            + " mm; constant offset = "
            + f"{muscle['length_offset_m']*1000:.6f}"
            + " mm; MT length = "
            + f"{muscle['MT_length_m']*1000:.6f}"
            + " mm. Branch divisors: "
            + esc([b["divisor"] for b in muscle["branches"]])
            + ".</p><table><thead><tr>"
            + "".join(
                "<th>" + h + "</th>"
                for h in [
                    "Order",
                    "Branch",
                    "Point / object",
                    "Role",
                    "Connected body",
                    "Local xyz (m)",
                    "World xyz at this pose (m)",
                    "Editable file",
                ]
            )
            + "</tr></thead><tbody>"
            + "".join(body_rows)
            + "</tbody></table></details>"
        )
    frames_html = "".join(
        "<tr>"
        + "".join(
            "<td>" + esc(v) + "</td>"
            for v in [
                f["body"],
                f["parent"],
                vec(f["origin_in_parent_m"]),
                vec(f["quaternion_in_parent_wxyz"]),
                "; ".join(
                    "xyz"[k] + ": " + vec(np.array(f["local_axes_in_world_columns"])[:, k])
                    for k in range(3)
                ),
            ]
        )
        + "</tr>"
        for f in frames
    )
    document = (
        """<!doctype html><html lang="en"><meta charset="utf-8"><title>Muscle attachments and wrapping</title>
<style>body{margin:35px auto;max-width:1450px;padding:0 24px;font:17px/1.6 Arial;color:#18333d}h1{font-size:32px}table{border-collapse:collapse;width:100%;font-size:13px}td,th{border:1px solid #c1cdd2;padding:8px;text-align:left}th{background:#e9f1f4}summary{font-size:20px;cursor:pointer;padding:8px;background:#edf4f6}details{margin:14px 0;overflow:auto}.note{background:#fff2db;padding:18px}input{width:95%;padding:12px;font:16px Arial}code,pre{font:14px Consolas,monospace}pre{background:#edf4f6;padding:16px;white-space:pre-wrap}.equation{text-align:center;font:22px/2 Georgia;margin:22px 0}.side{color:#5b6670}a{color:#007b90}li{margin-bottom:7px}@media print{details{display:block}input{display:none}body{font-size:11pt}tr{break-inside:avoid}}</style>
<h1>Origins, insertions, via points and wrapping</h1>
<p class="note">This is a map of the geometry actually used in the forward simulation. It distinguishes fixed bone/body attachments, moving routing points and wrap surfaces. The visible bone mesh does not automatically determine a muscle path. Some coordinates are registered or estimated model geometry, not measured feline attachment coordinates.</p>
<h2>Which file do I edit?</h2><ul>
<li><code>attachments.py</code>: body-fixed origin/insertion/via coordinates. The named body and role appear immediately above each entry. Metres: <b>0.001 m = 1 mm</b>. Changing a point site's orientation alone does not move its centre or alter MT length.</li>
<li><code>routing.py</code>: geometry parameters of computed moving via points and preferred wrap-side selectors. Their positions are recalculated from joint angles at each step; a static site-coordinate edit would be overwritten.</li>
<li><code>wrapping.py</code>: centres, orientations and radii of the actual sphere/cylinder wrap objects. These are separate from the visible bone surfaces.</li>
<li><code>muscle_tendon.py</code>: constant MT path offset, optimal fibre length and slack tendon length. Changing an attachment does not automatically change these parameters.</li></ul>
<p>Run <code>.\\run_model.ps1 --parameters config/user_model --seconds 3 --output my_attachment_trial</code> from the project folder. A new run rereads the files, applies the values before time zero, and writes an <code>ATTACHMENT_MAP.html</code> and <code>APPLIED_PARAMETERS.json</code>. Edits are not silently refitted. Use a new output name for each trial.</p>
<h2>Where are these coordinates?</h2>
<p>A local coordinate belongs to the named rigid body, not the world and not the bone mesh file. In a hindlimb thigh frame, zero is the hip centre and +x runs along the segment towards the knee. In shank and foot frames, zero is their proximal joint and +x points along that segment. Forelimb upper-arm and forearm frames follow the same proximal-to-distal construction. Pelvis, scapula and trunk have their own assembly frames; consult the frame table below. Local y is an in-plane transverse direction and local z is normal to the limb plane for the limb segment frames. They are <em>not</em> universally world-up or world-left.</p>
<div class="equation">p<sub>W,k</sub>(q) = x<sub>B</sub>(q) + R<sub>B</sub>(q) p<sub>B,k</sub> &nbsp; (1)</div>
<p><b>Terms:</b> p<sub>B,k</sub> is the configured xyz coordinate of point k in body B (m); p<sub>W,k</sub> is its world coordinate (m); x<sub>B</sub> is the world position of that body's origin (m); R<sub>B</sub> is its dimensionless 3×3 rotation matrix; q is the current generalized configuration (translations in m, rotations in rad). The point is constant in its body frame, while x<sub>B</sub> and R<sub>B</sub> change during motion. The axes table gives the actual initial orientation for every body.</p>
<h2>How does a coordinate edit change MT length?</h2>
<div class="equation">L<sub>MT,i</sub>(q) = c<sub>i</sub> + ∑<sub>b</sub> L<sub>path,ib</sub>(q) / d<sub>ib</sub> &nbsp; (2)</div>
<p><b>Terms:</b> L<sub>MT,i</sub> is whole muscle–tendon length for muscle path i (m); c<sub>i</sub> is its configured constant <code>MT_path_length_offset_m</code> (m); b indexes an engine path branch; L<sub>path,ib</sub> is that branch's routed length (m), including straight spans and any surface wrap arcs; d<sub>ib</sub> is the dimensionless branch divisor. All current muscle tendon gears are one. A branch seam is a computational construction, not necessarily a separate biological attachment.</p>
<div class="equation">L<sub>straight</sub> = ∑<sub>k</sub> ‖p<sub>W,k+1</sub> − p<sub>W,k</sub>‖ &nbsp; (3)</div>
<p><b>Terms:</b> L<sub>straight</sub> is the length (m) of a branch with only straight spans; k indexes successive ordered points and ‖·‖ is Euclidean distance. This formula alone is insufficient when the path wraps: the engine also includes tangent spans and cylinder/sphere surface arcs. A side selector chooses the wrap side and is not included as a mandatory path vertex. Moving it can change the selected path discontinuously.</p>
<div class="equation">ΔL ≈ [(p<sub>O</sub> − p<sub>I</sub>)/‖p<sub>O</sub> − p<sub>I</sub>‖] · R<sub>B</sub> Δp<sub>B,O</sub> &nbsp; (4)</div>
<p><b>Terms:</b> ΔL is the first-order length change (m) for a single straight origin-to-insertion span with insertion held fixed; p<sub>O</sub> and p<sub>I</sub> are its world origin and insertion (m); Δp<sub>B,O</sub> is the local origin edit (m). Moving directly away from the next path point lengthens a straight span; moving towards it shortens it. A 1 mm edit perpendicular to the span may barely change its length. For a wrapped path or via point use the numerical inspection tool; there is no universal rule that increasing x increases length.</p>
<div class="equation">L<sub>T</sub> = L<sub>MT</sub> − L<sub>F</sub> cos α, &nbsp; ε<sub>T</sub> = (L<sub>T</sub> − L<sub>T0</sub>)/L<sub>T0</sub> &nbsp; (5)</div>
<p><b>Terms:</b> L<sub>T</sub> is elastic tendon length (m); L<sub>F</sub> is fibre length (m); α is the fixed pennation angle (rad); L<sub>T0</sub> is slack tendon length (m); ε<sub>T</sub> is dimensionless tendon strain. MT length is <b>not</b> fibre length. At the same initial fibre state, a longer MT path stretches the tendon more; subsequent fibre motion and tendon force are solved by the elastic mechanics. The code does not automatically rescale fibre or slack lengths to hide your edit.</p>
<p>Changing the path can also change its angle-dependent length and force moment arms. The native force transmission uses the engine path Jacobian. With computed moving via points, verify it against a finite difference that updates the routing at both perturbed joint positions; geometry edits can spoil virtual-work consistency. A successful coordinate edit is not anatomical or gait validation.</p>
<h2>Important editing distinctions</h2><ul><li><b>Body ownership:</b> editing xyz moves a point within its current body. Attaching it to another bone requires changing model topology, not just its coordinates.</li><li><b>Paired seams:</b> some forelimb groups contain multiple computational branches. Keep coincident internal branch endpoints consistent when changing their geometry.</li><li><b>Routed muscles:</b> changing an endpoint does not automatically update polar radii/angles in <code>routing.py</code> or wrap surfaces in <code>wrapping.py</code>. Review all three when changing the anatomical routing construction; otherwise you have deliberately created a different approximation.</li><li><b>Left/right:</b> configuration entries are independent. Editing R_VL does not silently mirror the change to L_VL. Local-frame signs are not universally the same as world left/right signs.</li><li><b>Origins and insertions:</b> names below identify endpoints in the current computational path. Simplified group endpoints are not claims of anatomically exact broad attachment surfaces.</li></ul>
<h2>All muscle paths</h2><p>Search by muscle, body or point name. L/R = left/right hindlimb; FL/FR = left/right forelimb. SAM is the existing medial sartorius/SRTm model-channel label. Coordinates shown here are read back from the engine at the listed pose.</p>
<input id="search" placeholder="e.g. R_VL, SRTm (use SAM), thigh, DigitalFlexors" oninput="filterPaths(this.value)">
"""
        + "".join(rows)
        + """<h2>Body coordinate frames at this pose</h2><p>Parent-frame xyz and wxyz are the base assembly transforms before joint motion. The final column lists each local unit axis expressed in world coordinates at the inspected pose. For a new pose, use the updated world rotation; do not reuse this snapshot as a constant transform.</p><table><thead><tr><th>Body</th><th>Parent</th><th>Origin in parent (m)</th><th>Base orientation wxyz</th><th>Local x/y/z directions in world</th></tr></thead><tbody>"""
        + frames_html
        + """</tbody></table>
<h2>Provenance and implementation</h2><p>Original verified values and imported prepared values remain in the configuration comments and <code>PARAMETER_PROVENANCE.json</code>. “Not independently established” means no exact raw literature coordinate has been verified. The 11 original hindlimb groups use the project's Model 3 routing construction; the forelimb group model, added digit paths and registered shoulder/trunk paths have separate source histories. Some added extrinsic anchors are estimated anatomical-region coordinates. Neither this inspection map nor its colours upgrades them to measured anatomy.</p>
<p>The path, wrapping and branch definitions follow the <a href="https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial">MuJoCo spatial-tendon reference</a>. The body's local transform is evaluated by the dynamics engine. Inspect <code>describe_muscle_paths.py</code>, <code>apply_neuromechanical_parameters.py</code>, <code>apply_wrapping_parameters.py</code>, <code>update_muscle_paths.py</code>, and <code>calculate_muscle_route_points.py</code> for the implemented mapping. Data: <a href="ATTACHMENT_MAP.json">complete machine-readable connection and frame table</a>.</p>
<h2>Symbol table</h2><table><tr><th>Symbol</th><th>Meaning</th><th>Units</th></tr>"""
        + "".join(
            "<tr><td>" + a + "</td><td>" + b + "</td><td>" + c + "</td></tr>"
            for a, b, c in [
                ("i, k, b", "Muscle-path, point and branch indices", "1"),
                ("q", "Generalized configuration", "m or rad"),
                ("pB, pW", "Point in body/world coordinates", "m"),
                ("xB, RB", "Body origin and body-to-world rotation", "m; 1"),
                (
                    "LMT, Lpath, Lstraight",
                    "MT, routed-branch and straight-span lengths",
                    "m",
                ),
                ("ci, dib", "Constant path offset; branch divisor", "m; 1"),
                ("Δp, ΔL", "Coordinate edit and resulting length change", "m"),
                ("LF, LT, LT0", "Fibre, elastic tendon and slack tendon lengths", "m"),
                ("α, εT", "Fixed pennation and tendon strain", "rad; 1"),
            ]
        )
        + """</table>
<script>function filterPaths(q){q=q.toLowerCase().replaceAll('srtm','sam');document.querySelectorAll('details.muscle').forEach(d=>{d.hidden=!d.textContent.toLowerCase().includes(q);d.open=!!q&&!d.hidden;});}</script></html>"""
    )
    equation_index = iter(enumerate(EQUATIONS, 1))

    def typeset(match):
        index, math = next(equation_index)
        return '<div class="equation">' + math + " &nbsp; (" + str(index) + ")</div>"

    document = re.sub(r'<div class="equation">.*?</div>', typeset, document)
    # Save the computed values or figure for inspection and reproducibility.
    (out / "ATTACHMENT_MAP.html").write_text(document, encoding="utf-8")
    return record
