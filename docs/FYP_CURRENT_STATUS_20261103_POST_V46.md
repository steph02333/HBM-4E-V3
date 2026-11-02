# FYP status ledger — 2026-11-03 (after G02 V4.6)

This is the current handoff index, not a claim that all validation gates passed. Source: project GitHub logs plus researcher-uploaded diagnostic ZIPs and audited results discussed in the project on 2026-11-03.

## Verified research history
- **G01 analytical benchmark:** nine simplified ideal coaxial cases, 3.14–4.02% relative differences; completed as a limited analytical benchmark. Original README "G01 OPEN" is stale.
- **G02 V39:** 65/66 Q3D cases solved, nominal sigma10 S/m strongest mesh evidence. Sigma1 oxide mesh difference ~1.5% remains accepted as a declared limitation; sigma100 conductance cross-strategy deviations up to 12.62%.
- **G02 M01 / Maxwell independent cross-solver investigation ALREADY PERFORMED** (do not restart): nominal Q3D CAA 35.481712 fF, CAB -11.618261 fF, GAA 0.061592086 mS, GAB -0.016418221 mS; Maxwell pass8 CAA 36.474 fF, CAB -12.183 fF, GAA 0.069444 mS, GAB -0.020013 mS. Relative magnitude differences +2.80%, +4.86%, +12.75%, +21.90%. Native geometry, material, 1 GHz frequency and excitation reviewed. Maxwell default Neumann exterior and Q3D infinity reference not established as matching; loss error 2.0011% >1% target. Cross-solver numerical comparison DONE; identical-BVP independent validation OPEN. See docs/G02_M01_V21_BOUNDARY_REFERENCE_FORMULATION_20261102.md and docs/G02_M01_EXACT_NATIVE_REFERENCE_DIFF_20261102.md.
- **G02 V23–25:** 16 complex flux integrals and signal comparisons verified; global independent charge conservation NOT VERIFIED and user chose to archive this as a limitation.
- **G02 V41:** all seven solves complete; sigma1 L8 and L5 generated identical meshes; ~1.5% local-vs-baseline mutual C variation; no strict <1% global mesh PASS.
- **G02 V43–44:** seven total height/topology pilot cases complete (V43 3 GSSG, V44 4 repaired GSG/GSGSG). GSSG CAB magnitudes at H25/35/50: 8.211700/11.648644/16.812051 fF. GSGSG: 4.614627/6.446437/9.202295 fF. H35 GSGSG coupling 44.7% below GSSG, confounded by different signal separations. Per-topology independent meshes pending.
- **G02 V45 completed (previously NOT uploaded to GitHub):** three H0 no-contact sigma10 margin cases solved. M25/50/100 um CAA = 35.485989/35.857985/36.102512 fF; abs CAB = 11.648644/11.728142/11.653208 fF; abs GAB = .016263714/.015138240/.013587715 mS. M25->M100 CAA +1.74%, abs CAB +0.04%, abs GAB -16.45%. Finite silicon body and mesh both change: NOT pure infinity boundary convergence. Source researcher ZIP G02_V45_H0_silicon_extent_results_bundle.zip.
- **G02 V46 completed (previously NOT uploaded to GitHub):** seven H0 sigma10 GSSG geometry trend solves. (case: CAA fF, abs CAB fF): D3 28.083/9.068, nominal D4 35.486/11.649, D6 50.220/16.955, P10 37.142/12.197, P20 34.250/11.194, tox0.1 67.876/24.683, tox0.5 23.865/7.660. Expected D↑C↑, P↑coupling↓, tox↑C↓ all observed; symmetry/passivity yes, no recorded adaptive nonconvergence warning. Single-mesh trend verification only. Source researcher ZIP G02_V46_H0_geometry_trend_results_bundle.zip.

## Current modeling decision
Work with H0 (GSSG/GSG/GSGSG as appropriately defined; no explicit Si ohmic contact), nominal sigma10 S/m, 1 GHz Higher, Q3D C-only ML as FIRST stage, with explicit limitations. H0 not certified real HBM DRAM substrate connectivity. Do not silently include G as validated ML target. Keep Si margin25 um and explicit metadata.

## Next work; DO NOT redo completed experiments
1. Review professor email demands and completed G01/G02/M01 evidence before planning further Maxwell work. The gap is **matched boundary/reference BVP**, not absence of Maxwell runs. Do one narrowly scoped experiment only if it can actually resolve a clear comparison; otherwise declare limitation.
2. Representative legal high-risk geometry corner mesh checks, including topology differences and thin liner.
3. Final DOE design: admissibility filter P>D+2tox, full signed C matrix definitions, topology-aware labels (GSG has no AB), design-space/holdout strategy, failure/QA quarantine, provenance and source code/version.
4. Optional physically sourced substrate ties, MOS bias/Sentaurus pilot as separate physical fidelity extensions; do not claim them validated.

## GitHub synchronization notes
This ledger adds V45/V46 numerical *summary* to GitHub. Raw ZIPs and complete Windows AEDT simulation projects remain outside GitHub and must be retained locally. Runner scripts V41/V43/V44/V45/V46 were supplied in chat, but are **not all committed as scripts/**. Prior M01 work was already documented under docs/. The README and other older date-stamped plans might still be stale; use this ledger as newest handoff source.
