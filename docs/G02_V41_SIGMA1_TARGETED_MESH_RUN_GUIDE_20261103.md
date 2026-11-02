# G02 V4.1 targeted sigma1 local-oxide mesh qualification — 2026-11-03

## Inputs and derivation
Researcher supplied `G02_V39_mesh_contact_qualification.zip` with the original 33,325-byte `G02_V39_mesh_contact_qualification.py` and previously supplied `G02_V39_results_bundle.zip` with original solves. The uploaded source SHA-256 was embedded in the generated V4.1 script. The V39 mesh assignment uses `app.mesh.assign_length_mesh(assignment=[mesh_target], inside_selection=False, maximum_length=um(mesh_seed_um), maximum_elements=None, name='TARGET_SURFACE_SEED')`; setup is iterative solver, Higher-order, cap maxpass22, PerError0.5, adjustable PerRefine, nominal 1GHz, no substrate-contact change. Because the base/oxide cross-mesh differences exceeded 1%, only one conductivity regime is studied.

## Implemented targeted runner
`G02_V41_sigma1_targeted_mesh_qualification.py` delivered in current conversation as downloadable file (not checked into the repository yet). It preserves original source geometry construction, matrix extraction, mesh reports, status and diagnostic ZIP code. Only case generator and version/output name changed. Seven runs:
- `BASE_s1_r18` (control);
- `LOCAL_s1_OX_1_L12`, `L8`, `L5`;
- `LOCAL_s1_OX_2_L12`, `L8`, `L5`.

All use sigma=1 S/m, rho=100 ohm-cm, GSSG D4/P15/H35/tox0.3/Si margin25um, no substrate contact, Higher/Iterative CG 1GHz. L5 is a NEW mesh request and does not guarantee a distinct actual mesh. Model limitations remain unchanged.

Python compilation PASS; `--help` PASS; 7/7 dry-run construction/packaging PASS. **Actual Windows AEDT solves NOT RUN, mesh convergence NOT YET VERIFIED.**

Command: `py -3.13 "C:\暂时下载\G02_V41_sigma1_targeted_mesh_qualification.py" --student --aedt-version 2025.2`

Look for `G02_V41_sigma1_mesh_results_bundle.zip` under `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<timestamp>_<id>\`. Upload that ZIP. Evaluate actual distinct mesh counts, full signed C/G, Student surface 8000 cap, solver warnings; <1% differences for C self/mutual among **different actual meshes** must be established rather than inferred from requested seed lengths. If unchanged meshes or resource ceiling, mark INCONCLUSIVE, not PASS.

Original V39 σ1 R16/R18 worst C difference 0.027%, but local oxide L8 differs by ~1.49% mutual C from BASE R18. Baseline is comparison, not guaranteed ground truth. Charge conservation remains archived as NOT INDEPENDENTLY VERIFIED; separate from this mesh gate.
