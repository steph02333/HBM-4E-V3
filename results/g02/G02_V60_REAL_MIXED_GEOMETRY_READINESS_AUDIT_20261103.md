# G02 V6.0 real mixed-geometry readiness audit — 2026-11-03

**Source**: Researcher-uploaded `G02_V60_H0_mesh_readiness_results_bundle.zip`, independently parsed 18 `cases/*/result.json`, native Q3D C matrix and AEDT messages. Evaluated with `G02_V60_mesh_readiness_audit.py`. This audit does NOT certify a full DOE or physical fidelity.

## Results
- **18/18 attempted; 17 solved with C/G matrices; 1 failed**: GSSG sigma=1 S/m (rho=100 Ω·cm) MIX_B L6 R7 official AEDT Student **8,364 surface elements >8,000 limit**. Other R3/R5 solved; do not describe as a mesh-convergence PASS.
- **0/6 new V6.0 policy groups PASS** the stricter screen (3 distinct true meshes, fine/coarse element ratio >=1.10, both adjacent errors <1% for all C coefficients, finest-three span <1%). Five groups have 3 solved levels; GSSG sigma1 MIX_B has 2.
- **Merged V5.7–V6.0**: 43 individual case records, 15 exact policy groups, **1/15 strict PASS**, namely GSSG sigma=1 S/m, rho=100 Ω·cm, WEAK D3/P20/H25/tox0.5 BOTH-signal-oxide L6. Previous V5.x "PASS" labels used looser checks; retain their evidence while avoiding overclaiming.
- All 17 solved V60 cases recorded native Si classified dielectric, expected signal nets, symmetric positive eigenvalues and no `CG_adaptive_nonconvergence_warning`. Matrix-export frequency matches requested frequency flag **False** in all 17: known header/provenance discrepancy; not necessarily wrong native solve frequency, but do not assert exported 1GHz was independently verified.

### V6.0 6 group details

| Structure (sigma S/m; rho Ω·cm) | V52 geometry | policy | 3-level total mesh elements | max of last 2 adjacent component deltas | fine-three max span | strict screen |
|---|---|---|---|---:|---:|---|
| GSGSG sigma10, rho10 | STRONG D6/P10/H50/tox.1 | L10 R3/5/7 | 7648/7856/8208 | 1.469% | 2.812% | weak separation + C drift; FAIL |
| GSGSG sigma10, rho10 | MIX_B D5.73730/P19.35262/H28.07983/tox.48678 | L8 R3/5/7 | 4460/4596/4716 | 0.393% | 0.689% | element ratio 1.057, too small; NOT certified |
| GSGSG sigma100, rho1 | MIX_B D5.78997/P11.01708/H25.06478/tox.45429 | L8 R3/5/7 | 4468/5360/5572 | 4.043% | 4.029% | FAIL |
| GSSG sigma100, rho1 | MIX_B D5.47370/P10.31033/H42.20443/tox.48569 | L8 R3/5/7 | 7648/10792/11662 | 3.791% | 3.806% | FAIL |
| GSSG sigma1, rho100 | MIX_B D4.15415/P10.47958/H49.91236/tox.46725 | L6 R3/5/7 | 14052/14900/FAILED | 0.273% R3→R5 | n/a | insufficient; R7 surface 8364 fails |
| GSGSG sigma1, rho100 | MIX_A D5.61292/P19.41860/H49.02443/tox.15027 | L8 R3/5/7 | 7806/12092/14496 | 4.243% | 4.901% | FAIL |

**Formula** for each C term (AA, BB, |AB|): absolute difference divided by later/finer actual mesh-level term; fine-span is range across three values divided by highest-element-count term. Only within identical geometry/policy group, not cross-policy.

### Important method discovery: ineffective L10 knob
For GSGSG sigma10 STRONG, L10 R3 total mesh 7648, |CAB|=7.1974249fF and L10 R5 7856, 7.3047549fF. Historical **L8** R3 has 7648, 7.1974015fF and L8 R5 has 7856, 7.3038788fF. L10 is near the same meshes/numerical values as L8 and retains ongoing monotone mutual drift (L10 R7 7.4056824fF). Merely loosening oxide seed L8→L10 is not an effective independent mesh-policy alternative here. **Do not run extra L10 R values blindly.**

### Specific C behavior / scientific caution
- GSGSG sigma100 MIX_B: |CAB| 6.425904→6.176177→6.197585 fF; R3→R5 4.043% while R5→R7 0.345%. Last two finer levels close does not erase large first jump.
- GSSG sigma100 MIX_B: |CAB| 12.691366→13.191396→13.193516 fF; first pair 3.791%. Avoid claiming convergence on R5→R7 alone.
- GSGSG sigma1 MIX_A: |CAB| 1.128516→1.082586→1.075794 fF; first pair 4.243%, fine span 4.901%. Highest CG final triangles 7888 (this is *not* the same as licensed surface-element counter); low headroom.
- GSGSG sigma10 MIX_B: C small change yet total meshes 4460→4716 only 5.7% span; needs independent alternate allocation, not extra PerRefine that hardly changes the mesh.
- Cross-policy invariance, charge closure, true substrate/BVP validation, external-domain checks, HBM4 die physics and export header issue remain unresolved.
- Each `SOLVED_UNVERIFIED_PHYSICS` remains only a numerical solve.

## Next research gate / action
1. **Do not start production DOE or blindly run V6.0 coverage 12.**
2. Prioritize risk-adaptive *cross-policy tests* on representative MIX_B: GSGSG sigma100, GSSG sigma100, GSGSG sigma1, and GSGSG sigma10 strong. Change local assignment/mesh budget to obtain genuinely different mesh allocation rather than just another R at nearly identical mesh. Compare independent C coefficients and whole-sequence drift.
3. For the GSSG sigma1 MIX_B failure, test a reduced-cost oxide/local policy under 8000 official surface elements rather than R>5 with L6.
4. Add resource/headroom and mesh-diversity diagnostics to automatic gate. Consider DOE feasibility gate separately from strict research representative mesh validation: validation sample + real-time solve QA + staged fallback instead of claiming proof for every future parameter combination.
5. Keep DOE independently space-filling across all six professor inputs, and reserve V6.0 coverage phase until prior high-risk failures have an actionable mesh strategy.

GitHub document is an interpreted audit of real results; full raw ZIP is retained by researcher (not committed). No new AEDT simulations were run during this review.
