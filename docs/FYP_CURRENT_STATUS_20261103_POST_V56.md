# FYP current handoff — after V5.6 mesh diagnostics (2026-11-03)

## What changed today
The researcher completed real V5.3–V5.6 targeted Q3D runs. Primary scientific evidence is [the full V5.3–V5.6 audit](../results/g02/G02_V53_V56_LOCAL_MESH_POLICY_AND_FOURLEVEL_AUDIT_20261103.md) and [case-level machine-readable C matrix table](../results/g02/G02_V53_V56_compiled_nominal_cases_20261103.csv). This page is the current handoff; older `docs/FYP_CURRENT_STATUS_20261103_POST_V46.md`, `docs/VALIDATION_GATE.md`, and some early scripts/README text reflect older stages and must not override this result.

- V5.2 primary: 52 solved /54 attempted; many 3-level GSGSG and GSSG failures. Already audited in `results/g02/G02_V52_MULTILEVEL_REPRESENTATIVE_MESH_AUDIT_20261103.md`.
- V5.3: 6 aggressive local-mesh attempts hit official 8000-surface-element Student cap.
- V5.4 Cu: 6 failures at cap; oxide second stage: 2/6 solved, L6 and L8 were identical true meshes (not independent verification).
- V5.5: 6/6 solved. Same nominal geometry, both-oxide L6 R5/R8: GSSG rho100 maximum C pair difference 0.553%; GSGSG rho1 1.339%. Single oxide assignment diverged ≈2.5% in GSSG, so not a general lower-cost substitute.
- V5.6: 4/4 solved; combined with V5.5 for R5/R6/R8/R10. **GSSG rho100**: all 3 adjacent pairs max 0.449%,0.227%,0.206% => PASS limited to nominal + both-signal-oxide L6 policy. **GSGSG rho1**: adjacent max 0.420%,1.339%,0.653% => NOT full PASS, although late pair promising.
- Status of severe historical anomalies: GSSG rho100 local-oxide V41 1.5% mismatch remains a cross-strategy limitation, despite newly strong within-policy evidence; GSGSG rho1 nominal V49 5.893% cross-strategy mismatch also unresolved. These two different kinds of evidence must not be conflated.

## Research decision
**Do not run V52 Reserve 54 or production DOE yet.** Prioritize a targeted V5.7 with (1) transferred dual-oxide L6 policy on previously problematic GSSG rho100 strong/weak corners, 3+ meaningful distinct mesh results within student cap; (2) GSGSG rho1 one resource-bounded orthogonal mesh policy test using R8/R10 baselines, not blind global refinement; (3) test whether mesh assignment scope can be tightened to reduce costs while keeping both Cself and Cmutual stable. Keep failures and alternative meshes rather than deleting them. Avoid introducing multiple changes at once when possible.

All experiments and planned DOE are on reduced H0 no-contact homogeneous conductive-Si TSV reference model, not a complete HBM4 die. Outputs: for GSG only CAA, for two-signal layouts CAA,CBB,CAB. Select final DOE independently space-filling, never intentionally near representatives. Numerical validation remains conditional; professor's charge-conservation, matched solver, domain/bias limitations remain open.

## Source datasets / local assets
- Uploaded `G02_V53_H0_local_mesh_diagnostics_bundle.zip`
- Uploaded `G02_V54_H0_mesh_budget_results_bundle.zip` (oxide-mode later archive; older Cu-mode had the SAME basename)
- Uploaded `G02_V55_H0_mesh_policy_results_bundle.zip`
- Uploaded `G02_V56_H0_fourlevel_mesh_results_bundle.zip`
- Executable source filenames retained by researcher from earlier project chats, **not necessarily in GitHub**: `G02_V53_H0_targeted_local_mesh_diagnostics.py`, `G02_V54_H0_mesh_budget_calibration.py`, `G02_V55_H0_mesh_policy_diagnostics.py`, `G02_V56_H0_fourlevel_oxide_mesh.py`, `G02_V56_merge_mesh_audit.py`.
- Normal Windows command style: `py -3.13 "C:\暂时下载\SCRIPT.py" --student --aedt-version 2025.2`; actual exact flags from script CLI help. Stdout ZIP outputs, native AEDT project files remain on researcher's PC.
- GitHub target: `steph02333/HBM-4E-V3`, branch main. Avoid claiming archived raw ZIPs and executable runners are in repo unless committed separately.

## QA and claim policy
Four-level in-policy agreement is a mesh consistency screen, not strict independent refinement-to-continuum proof; PerRefine may reorder actual mesh counts. Need high-risk corner transfer evidence before production ML; every label must pass solver + matrix QA, selective independent mesh audit. Record all C coefficients and Student surface license counter separately from total elements / CG triangles.
