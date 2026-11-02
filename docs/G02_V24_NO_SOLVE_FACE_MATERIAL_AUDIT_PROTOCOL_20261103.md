# G02 v24: no-solve Cu face / material inventory

Following G02 v23 dual excitation native E-flux PASS (16/16, max signal C/G deviation 0.6076%, reciprocity cross-term <0.05%), the remaining question is **whether a globally valid D displacement flux can be defined**. Multiplying every Cu surface E integral by epsilon0*3.9 does not demonstrate this: endcaps can border another dielectric or reference region, curved faces have no single normal, the source-facing field is ambiguous, and infinity-reference flux is not independently observed.

## v24 workflow

Offline script supplied to researcher in chat: `G02_Q3D_geometry_material_face_inventory_v24.py` (currently not stored as a GitHub script). Run with Python 3.13, PyAEDT and AEDT 2025.2 Student. This script copies **only** `DOM10_M25_R18.aedt` to a timestamped subfolder, opens the copy, uses read-only 3D Modeler calls (`GetObjectsInGroup`, `GetPropertyValue`, `GetObjectBoundingBox`, `GetFaceIDs`, `GetFaceArea`, `GetFaceCenter`), and exports objects/faces JSON and CSV plus status. There is NO Analyze, Save, or geometry operation, and no .aedtresults copy. A successful run is an inventory, not proof of adjacency or charge conservation. API references: Q3D Extractor Scripting Guide 2025 R2, and PyAEDT Modeler documentation.

Command: `py -3.13 "C:\暂时下载\G02_Q3D_geometry_material_face_inventory_v24.py" --student --aedt-version 2025.2`

Upload only `G02_Q3D_GEOM24_diagnostic.zip`. Interpret target Cu face areas and bboxes to identify **candidate** sidewalls/endcaps; explicitly mark unknown curved-face centers and unresolved dielectric contact. Compare against Si, oxide, and any other material objects and geometry. Do not infer Gauss closure from a face inventory. If geometry/material audit identifies a physically justified closed surface where `D=epsilon E` can be evaluated region by region, design a controlled independent check; otherwise document G02 charge conservation as OPEN / not independently demonstrated and move to other validation gates.

## Stop rule

No further identical E flux probes. Do not count Cu-sum as a conservation residual, even if near zero. No final DOE label freeze until remaining physical-model/domain/convergence gates are resolved or explicitly bounded.
