# G02 Section 13 — one-shot four-candidate independent Q3D evidence audit (2026-11-05)

**Source evidence:** uploaded `SECTION13_ALL_FOUR_EVIDENCE_20261105_132314.zip`, nine outer ZIP items including summary, four per-candidate nested evidence ZIPs, and launcher logs. Original evidence ZIP is held in the active conversation sandbox; this markdown and summary CSV are GitHub copies of parsed findings, **not a substitute for binary raw evidence**. [Exact numeric comparison CSV](G02_SECTION13_ALL_FOUR_Q3D_COMPONENT_COMPARISON_20261105.csv).

## What actually happened
- **Four preregistered candidates attempted; eight R3/R5 cases total. Six solver cases completed, two failed before design initialization.**
- OPT03671 (GSG rho=10): previously solved R3/R5 skipped by one-shot resume; both source results present, native C 1×1.
- OPT01697 (GSSG rho=10): R3/R5 completed and exported native signed 2×2 Maxwell C matrices.
- OPT02901 (GSGSG rho=10): R3/R5 completed and exported native signed 2×2 Maxwell C matrices.
- **OPT00662 (GSGSG rho=100): R3 and R5 FAILED BEFORE Q3D SOLVE**, in PyAEDT/Q3D design initialization. Exception in `ansys.aedt.core.desktop.Desktop.active_design`: `AttributeError: 'NoneType' object has no attribute 'GetName'`, triggered while attempting `active_design.GetName()`. There are **no Q3D C values** for OPT00662. This is an **automation/environment initialization failure**, not proof that physical coupling is near zero or nonzero. Retain failed logs and do not substitute a different design.

## Frozen ML versus fresh Q3D native R5, fF
The frozen ML values are printed Section 12B values (six decimals), NOT exact full-precision predictions from the missing original manifest. Absolute relative errors use abs(ML-Q3D)/abs(Q3D).

| Candidate | Coefficient | ML | Q3D R5 | Abs error fF | Relative error |
|---|---|---:|---:|---:|---:|
| OPT03671 | CAA | 16.281986 | 15.5283125724 | 0.753673 | 4.85% |
| OPT01697 | CAA | 14.726529 | 16.8220532905 | 2.095524 | 12.46% |
| OPT01697 | CBB | 14.814701 | 16.8232850928 | 2.008584 | 11.94% |
| OPT01697 | CAB | -5.909626 | -5.3610150960 | 0.548611 | 10.23% |
| OPT02901 | CAA | 19.070661 | 21.4346026635 | 2.363942 | 11.03% |
| OPT02901 | CBB | 18.571125 | 21.4075226572 | 2.836398 | 13.25% |
| OPT02901 | CAB | -2.979704 | -3.9611983853 | 0.981494 | **24.78%** |

This is a **negative result for high-accuracy optimizer-selected prediction**, especially GSGSG CAB. It does not negate the previously reported independent held-out 68-design interpolation scores, but it prevents treating those scores as proof of optimization reliability.

## Native Q3D R3/R5 evidence, in fF
| ID | R3 CAA | R5 CAA | R3 CBB | R5 CBB | R3 CAB | R5 CAB |
|---|---:|---:|---:|---:|---:|---:|
| OPT03671 | 15.5314544921 | 15.5283125724 | NA | NA | NA | NA |
| OPT01697 | 16.8287489802 | 16.8220532905 | 16.8294227078 | 16.8232850928 | -5.3535032673 | -5.3610150960 |
| OPT02901 | 21.4423606123 | 21.4346026635 | 21.4137550843 | 21.4075226572 | -3.9493273603 | -3.9611983853 |

R3–R5 per-coefficient relative differences, normalized by |R5|, range **0.020–0.300%**, less than 1% in these six run results. All six completed solves report three CG adaptive passes, target 0.5%, last-pass CG delta less than target, no CG nonconvergence warning. A strict native consecutive-adaptive-pass coefficient-level <1% audit has **NOT** been reconstructed from consecutive pass matrices. R3–R5 agreement supports numerical repeatability under different mesh refinement policies; does not prove physical accuracy.

## Interpreting OPT00662 correctly
Its pre-registered frozen CAB prediction -0.003095 fF was suspicious because 4/9 nearby model perturbations predicted *positive* CAB, violating expected Maxwell sign in this model, and 82 GSGSG rho100 Sobol predictions failed matrix-validity screening. However, this new Q3D attempt **did not produce a physical matrix**; two design-initialization errors are inconclusive. **Do not label OPT00662 as 'Q3D disproved surrogate' or 'Q3D confirmed near zero'.** Recovery must target initialization without changing geometry, candidate ID, rho, solver physics or predicted values. Preserve the initial failed runs in the audit.

## Other unresolved quality gates
- The native text matrix header says **Frequency: 1kHz** in all six completed runs though Q3D setup requests 1000 MHz. The exported C matrix is stable under multiple selector attempts, but frequency/header mismatch remains unexplained. Do not assert independently verified 1 GHz physical output.
- Some PyAEDT logs note an unsuccessful export attempt, **but a valid native signed C matrix was obtained via the successful selector**. Distinguish intermediate export-selector error from final matrix availability.
- Solver run status `SOLVED_UNVERIFIED_PHYSICS` is intentional. It denotes that a model solved, NOT a universal accuracy, device physics or numerical-quality certification.
- No controlled same-topology/ρ **baseline Q3D comparison** or actual optimality proof is yet established. Three verification points do not support a statistical estimate of optimization-stage generalization.

## Decision / next action
**Archive evidence unchanged.** The top research finding is that the evaluated optimizer-selected designs had larger surrogate prediction errors (GSGSG CAB 24.78%) despite small paired-mesh numerical differences. Next: recover OPT00662 Q3D application initialization for an independent physical test **without changing its frozen geometry**. There is no need for further hyperparameter tuning. Once successful, add Q3D coefficients, component-level errors and baseline-relative engineering comparisons.

Related [OPT03671 first evidence](G02_SECTION13_OPT03671_FRESH_Q3D_FIRST_EVIDENCE_20261105.md), [Section 12B preregistration](G02_SECTION12B_VERIFICATION_PROTOCOL_20261105.md), [Section 12A flaws](G02_SECTION12A_PARETO_AUDIT_20261105.md).
