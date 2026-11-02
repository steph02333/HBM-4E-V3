# G02 V4.3: height and topology pilot (2026-11-03)

## Runner
`G02_V43_height_topology_validation.py` generated from user-uploaded `G02_V39_mesh_contact_qualification.py`. Python compilation, --help, and seven-case dry-run completed. **No actual AEDT solves have been run by assistant.**

Seven configurations:
1 GSSG H25
2 GSSG H35
3 GSSG H50
4 GSG H35
5 GSGSG H35
6 GSGSG H25
7 GSGSG H50.

Fixed: Cu diameter D4 um, adjacent pitch P15 um, liner 0.3um, Si epsilon 11.7, conductivity 10 S/m, no explicit substrate contact, Si margin 25um, Q3D Higher/Iterative, 1GHz, adaptive PerRefine 16, max passes 22. All generated geometry uses centered 1D arrangements. GSG coordinates x=-15,0,+15 um and exactly one SIG_A net; GSSG x=-22.5,-7.5,+7.5,+22.5 um; GSGSG x=-30,-15,0,+15,+30 um. Ground names GROUND_L/M/R as applicable. GSGSG signal separation 30um vs GSSG 15um, so shielding and separation are confounded; do not attribute difference only to a ground shield.

Outputs include full original reduced signal-only C/G matrices, raw solver/mesh outputs and model limitations, with single-signal GSG mutual marked undefined rather than zero. Per-topology mesh remains **not independently qualified**; seven solves are first physical sensitivity pilots, not final DOE gate pass.

Run Windows:
`py -3.13 "C:\暂时下载\G02_V43_height_topology_validation.py" --student --aedt-version 2025.2`

Upload `G02_V43_height_topology_results_bundle.zip` from the newest `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<timestamp>_<id>\` folder. Check all 7 case results, full C/G, actual distinct mesh status, Student resource errors, expected height trends, topology comparison, geometry/net classification, frequency provenance. A dry-run is not a solver run. Charge conservation is archived as NOT INDEPENDENTLY VERIFIED; sigma1 local oxide mesh 1.5% remains provisional by user-approved engineering tradeoff.
