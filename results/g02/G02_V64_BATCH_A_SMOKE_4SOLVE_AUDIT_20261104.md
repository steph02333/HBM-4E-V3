# V6.4 Batch A — Four-solve smoke-test actual-evidence audit (2026-11-04)

Real researcher-submitted `G02_V64_BATCH_A_evidence.zip`, SHA256 `1c761dcf1a5fc59d3ff3dcb7d633a26a2ca7be1e5d47b270089687e3cc5e9260`. 48-case frozen manifest, **4 SOLVED_UNVERIFIED_PHYSICS, 44 MISSING**; smoke tested DOE0380 and DOE0240, M_A and M_B each. No solver failures in the four completed cases. Preserve local raw ZIP and original runs, which are not stored in this GitHub report.

**Policy definitions:** M_A changes PerRefine 5→7; M_B changes target oxide surface MaxLength 1.0→0.8 times original, keeping PerRefine=5. Native setup frequency is 1000MHz, yet all four CG exported frequency headers read `1kHz` (alternate numeric frequency selectors return `1Hz` while unchanged C matrices; this mismatch remains unresolved). Therefore no 1GHz-provenance claim.

| DOE | Term | Original R3/R5 delta | R5 vs M_A | R5 vs M_B | R5 total mesh | M_A total mesh | M_B total mesh |
|---|---|---:|---:|---:|---:|---:|---:|
| DOE0380, GSG rho1 | CAA | 6.2131% | 0.1463% | 0.1295% | 3944 | 4248 | 5468 |
| DOE0240, GSGSG rho100 | |CAB| | 7.8223% | 0.8560% | 0.0005% | 10354 | 14074 | 10354 |

For DOE0240, **all applicable R5-vs-M_A coefficient differences are under 1%** (CAA ≈0.725%, CBB ≈0.964%, |CAB| ≈0.856%). A third, separately realized more resolved mesh supports treating original R3 as suspicious, but proof of asymptotic convergence and physics accuracy still requires caution. For DOE0380, M_A vs M_B CAA differs ≈0.276%, suggesting cross-policy robustness while original R3 is the clear outlier.

**Crucial experimental-design defect:** DOE0240's **M_B total-element count equals original R5 exactly (10354 vs 10354)**, and all C terms are almost identical (≤0.0005% for mutual). Changing the requested seed did **not** achieve a demonstrably independent mesh for this DOE. An apparently outstanding 0.0005% agreement is **NOT** meaningful new independent validation. In contrast, DOE0380 M_B adds ~38.6% total elements and is plausibly an independent mesh.

**Recommendation / decision:** Smoke shows technical execution success and promising M_A numerical stability. Do NOT automatically run 44 remaining cases and claim all M_B meaningful. Extend checkpoint diagnostics so each finished case compares realized mesh stats to original R5 and flags unchanged or effectively duplicated output. Consider limiting M_B to strata where actual targeted mesh responds or making M_B a stronger, controlled mesh-allocation intervention; retain arms/IDs and policy names with distinct versioned policy identifiers if changing policy definitions. Repeat at least a second GSGSG stratum smoke probe to verify M_B behavior before committing full 23-point dual-arm campaign. A lack of M_B effect should not be counted as a data fix. DOE0447 CAP_A_R3/R5 remains unrun (two cases).

The existing report is based strictly on uploaded JSONs and reference V6.3 signed-C CSVs. Note `mesh_stats.txt` counts are exported **total mesh elements**, NOT the Student 8000 3D-surface license counter. Unchanged total count alone cannot prove identical mesh topology; near-identical C plus equal count is sufficient reason to flag the need for independent-mesh evidence, not absolute proof of byte-identical meshes.
