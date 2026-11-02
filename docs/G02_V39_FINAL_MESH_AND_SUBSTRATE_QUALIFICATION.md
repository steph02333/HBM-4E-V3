# V3.8 evidence and V3.9 qualification protocol — 2026-11-02

G02 OPEN. V3.9 script syntax tested, 66-case dry run ZIP verified; actual Ansys run pending.

GUI confirmed AEDT 1GHz solution and native matrix matches same V3.7 Python C/G numeric entries. Default PyAEDT export's 1kHz header is demonstrably misleading for that case, not evidence of incorrect C/G matrix numbers. Other frequency cases need audit.

V3.8 Higher 100 S/m R14/R16 total 6632/6716 elements, worst C/G observed difference 0.141%, but oxide-seeded cases disagree; no global convergence PASS. 1 S/m R12/R14 apparently stable; 10 S/m R12/R14 worst C 1.482%, G 6.669%. Two close mesh outputs alone do not certify accuracy.

Physical substrate: edge contact, corner contact, no contact produce materially different conductance. Cu metal patch grounding and dielectric touch do not prove semiconductor ohmic electrical contact. Never choose edge simply because it converges best. Ansys lossy medium G matrices, ground-to-infinity, net grounding and complete Y=G+jwC interpretation must be documented. Independent charge-current flux is still missing.

V3.9 66 cases preserve GSSG, Cu D4, pitch15, H35, SiO2 liner0.3 um, Si margin25 um, Higher order, 1GHz nominal. Three sigma 1,10,100 S/m x six refinements 8/10/12/14/16/18 = 18; three sigma x four local meshed objects Cu SIG A/B OX_1/OX_2 x two lengths 12/8 = 24; no-contact/edge/corner x 4 refinements = 12; edge with 0.05/0.5/2 um deliberate gap x 2 refinements = 6; 1/100/1000MHz setup x two refinements = 6.

Every mesh case records separate material, geometry, reference, contact gap, frequency, solution order, C/G matrix, convergence profile, mesh metadata and AEDT logs. Independent meshes and physical comparability required. Student 8000 surface limit differs from reported total object mesh elements.

Gap control discriminates grounded patch proximity/shielding from directly touching patch geometry, but cannot prove true semiconductor ohmic continuity. Charge conservation, physical substrate extent, full GSG/GSSG/GSGSG, external solver G03 and MOS bias remain open.

Windows run: py -3.13 C:\暂时下载\G02_V39_mesh_contact_qualification.py --mode pilot --student --aedt-version 2025.2 . Upload generated G02_V39_results_bundle.zip; [CASE i/66] counts included. Never run GUI against active Python AEDT session.