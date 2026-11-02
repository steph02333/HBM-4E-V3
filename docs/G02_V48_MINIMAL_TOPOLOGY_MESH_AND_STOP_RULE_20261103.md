# G02 V4.8 minimal topology mesh pilot — 2026-11-03

## Duplicate-work audit
Existing investigations:
1. Maxwell M01: nominal Q3D vs Maxwell comparison already performed; C mismatch +2.8%/+4.86%, G mismatch +12.75%/+21.90%. Q3D infinity reference versus Maxwell default Neumann external boundary not established equivalent; native Maxwell loss error ~2%. Stop repeating adaptive/terminal scope without a genuinely matched BVP plan.
2. Q3D independent global charge conservation: tested through V25 with actual E flux integrals, correct signal flux agreement ~0.608%, but entire signal/ground/substrate/exterior balance unverified; user explicitly accepted this limitation. No further unbounded face API experiments.
3. Finite domain: V2.7 27 attempted 22 solved 5 Student surface-mesh failures; finite Si body stability not established, with changing physical Si body confounded with moving outer boundary. V4.5 sigma10 no-contact margin25/50/100 shows CAA +1.74%, abs CAB approx +0.04% endpoints, abs GAB -16.45% endpoints. Preserve as limitation; do not repeat blind sweep.
4. Cross-topology/material mesh: V39 sigma 1/10/100 nominal meshes and V4.1 sigma1 oxide attempted; sigma1 local C ~1.5% discrepancy accepted limitation. V4.7 four sigma10 GSSG extreme corners have distinct R12/R18 meshes and worst C change 0.412%. But GSG and GSGSG V4.4 are single-mesh pilots. This is remaining low-cost gap.

## V4.8 targeted run
Runner generated from successful V4.7 source, called `G02_V48_H0_topology_mesh_qualification.py`, located in this chat for download (not yet committed to scripts). 4 new solves: GSG H35 R12/R18 and GSGSG H35 R12/R18. D4µm, P15µm, H35µm, tox0.3µm, Si margin25µm, sigma10 S/m, 1GHz Higher iterative, no explicit substrate contact, PerRefine12/18, PerError0.5 max passes22. Combine with existing V4.4 H35 nominal R16 results as additional *historical* reference; verify geometry/material/reference equality before using across runs. Real mesh counts must differ; check CAA and GSGSG CBB,CAB; GSG has no signal-to-signal mutual term.

Python compilation/CLI/dry-run 4/4 passed; **AEDT solve pending**. Windows command: `py -3.13 "C:\暂时下载\G02_V48_H0_topology_mesh_qualification.py" --student --aedt-version 2025.2`.
Upload `G02_V48_H0_topology_mesh_results_bundle.zip` from latest `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<timestamp>_<id>\`.
On completion inspect raw C/G, actual mesh, warnings, surface license cap, and no >1% pair discrepancy; if PASS, start provisional sigma10 H0 C-only DOE pilot with QA and limitations. This is not full professor validation signoff, especially matched Maxwell BVP and charge closure.
