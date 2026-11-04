# V6.4 four-solve smoke test — HISTORICAL; campaign STOPPED

**The remaining Batch A solves are not authorized under the superseded 76-point remediation plan.** See [corrected ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md).

Four extra independent solutions: DOE0380 and DOE0240 under M_A (PerRefine=7) and M_B (oxide surface length multiplier 0.8). Historical final-solution observations:

| DOE/term | Old R3/R5 C difference | R5 total | M_A total | M_B total | R5/M_A C difference | R5/M_B C difference |
|---|---:|---:|---:|---:|---:|---:|
| DOE0380 CAA | 6.2131% | 3944 | 4248 | 5468 | 0.1463% | 0.1295% |
| DOE0240 abs(CAB) | 7.8223% | 10354 | 14074 | 10354 | 0.8560% | 0.0005% |

DOE0240 M_B matched R5 total elements with near-identical C; this does not independently establish a finer mesh. All comparisons shown are final outputs of *independent* solves, not the within-run successive adaptive pass Cself/Cmutual analysis. Requested 1 GHz versus export 1 kHz frequency issue remains OPEN.

**Preserve these four results, but do not launch the remaining batch based on the retired screen.** Inspect native Solution Data > Matrix > Pass first.
