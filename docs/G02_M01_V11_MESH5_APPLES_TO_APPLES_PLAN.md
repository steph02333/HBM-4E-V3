# M01 v1.1 Maxwell five-level mesh and Q3D matching

2026-11-02. G02 OPEN.

User runner: `G02_M01_mesh5_gated_comparison_v11.py`; source placed in user download. Compiled and CLI help checked; Windows AEDT 2025.2 SV runtime NOT verified.

Input is saved M01 v0.6 AC Conduction model, copied once per slider 1..5. Native `MeshSetup.AssignTrueSurfOp` on same 9 solids (four Cu, four oxide, Si), same mesher and setup. Slider resolution 1,2,3,4,5, not guaranteed five specific element counts or nested meshes. 64k Student volume cap; each run has original SHA integrity audit, native 4 voltage face+value checks, matrix presence gate, blocking Analyze, best-effort export, per-level artifacts, and diagnostics ZIP. Do not claim an API success means numerical convergence.

Matched Q3D reference from raw user V4.0 bundle `cases/DOM10_M25_R18/result.json`: GSSG D4 P15 H35 tox0.3 sigma10 margin25 1000MHz; 2x2 C in fF: [[35.48171237,-11.61826068],[-11.61826068,35.48442813]]; G in mS: [[0.0615920860,-0.0164182208],[-0.0164182208,0.0615990180]]. Important: exported header says 1kHz despite requested 1000MHz; prior independent GUI evidence resolves frequency for one different case, **not definitively this one**. Flag until confirmed. Physical outer boundary, Si body and ground definitions must be examined, not just D/P/H matching.

Stage 3: First compare nominal matrix once Maxwell export and frequency verified; then conditional representative cases tox0.5 and sigma1, only if nominal accuracy and mesh adequacy support them. v1.1 does NOT silently modify geometries/materials to generate those extra cases. It preserves intact Maxwell originals and explicitly records Stage3 pending. If no feasible converged mesh under Student 64k, use full NUS academic license rather than claiming success.

Run: `py -3.13 "C:\暂时下载\G02_M01_mesh5_gated_comparison_v11.py" --student --aedt-version 2025.2`.

Relevant Ansys 2025R2: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Maxwell/Content/Mesh/ModifyingSurfaceApproximationSettings.htm ; native AssignTrueSurfOp in scripting guide.
