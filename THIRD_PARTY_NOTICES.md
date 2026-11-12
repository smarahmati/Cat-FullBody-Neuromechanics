# Attribution and redistribution scope

The root MIT license applies to the original Python implementation and original
project documentation. It does not replace the terms of third-party publications,
source files, datasets, meshes, or installed software. A citation is not a license.

| Material | Source and treatment |
|---|---|
| Original Python model and guides | MIT, as selected by the project author. |
| Author-provided numeric/MATLAB research records | `Data/Original_Study_Data` and reference tables retain their source attribution. These records are supplied for scientific reproduction; the code license does not assert ownership of coauthors' or third parties' material. Consult the original study and data authors for other reuse. |
| Rahmati et al. (2025) PDF | CC BY-NC article, with the notice retained in the unmodified PDF; noncommercial restrictions apply to the article, not to original MIT code. DOI 10.1113/JP287448. |
| Paw-shake article (2022) PDF | CC BY, original publisher file with attribution/notice preserved. DOI 10.3389/fnint.2022.810139. |
| Other papers | Complete DOI bibliography and source links are included. Public reading copies are bundled only where permission is identified. Locally retrieved author copies without verified redistribution permission are in ignored `Documentation/References/Local_Papers`. |
| Bone surfaces | Derived from the SimTK cat hindlimb and Fujiwara (2018) supporting anatomy. Separate redistribution terms were not established. Exact local files are retained, but `Data/Skeletal_Geometry/Model/meshes` is excluded from Git. The public model automatically draws schematic bones without changing mechanics. |
| Simulation media | Project-generated visualization, not recorded animal footage. The detailed skeleton is a rendering of the source anatomy above; this does not grant redistribution rights to the original mesh files. |
| Numerical dependencies | Installed separately using pinned requirements; each dependency retains its own license. MuJoCo is the active multibody engine. OpenSim is cited for the force–velocity implementation but is not required or bundled. |

See `Documentation/References/index.html` for each source's specific contribution,
license notice, DOI, and the distinction between a published relation and a
project-specific adaptation. No published paper validates this exact assembled
104-channel model or its percentage thresholds for motor reduction.
