# V3.3 controlled mesh/reference experiment (2026-11-01)

G02 remains OPEN. Script issued in project chat: `G02_V33_mesh_reference_investigation.py`, SHA256 `90c5dd967fcdc7c1925b53d68b8714a21d435ae3bd952c67a0d60ca205a8b3fc`. Python syntax and dry-run ZIP verified. **No AEDT results yet.**

## New fact from Ansys and PyAEDT documentation
The actual Q3D Capacitance/Conductance adaptive refinement property is `setup.props['Cap']['PerRefine']` (default 30), not `PercentRefinement`. Ansys: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Q3DExtractor/Subsystems/Q3DExtractor%20Scripting/Content/InsertSetupQ3DExtractor.htm ; PyAEDT: https://aedt.docs.pyansys.com/version/stable/API/SetupTemplatesQ3D.html. V3.2 silently failed to change this property; V3.3 requires this actual key, writes the value and fails loudly if unsupported.

## Scientific design
Keep 4 Cu TSVs G-S-S-G and silicon/oxide dimensions unchanged: D=4 um, pitch=15 um, height=35 um, tox=.3 um, Si margin=25 um, epsSi=11.7, rho 100/10/1 ohm cm (sigma=1/10/100 S/m) with **default threshold 10,000 S/m**.

18 material/mesh attempts: each sigma x `PerRefine=5,10,15,20` with default mesh, plus 35- and 16-um Cu-SIG_A mesh seed at `PerRefine=10`. PerError=0.5%, MinPass=3, MinConvPass=2, MaxPass=12. These are independent mesh *attempts*; progression cannot be established from percent-refinement alone, and no 4k-8k element count is guaranteed. Capture actual mesh counts, C and G matrices, and loss/passivity/solver diagnostics. Student hard limit is 8000 **surface** elements, not reported total mesh elements.

5 physics controls: sigma=0 lossless, sigma=10 lower-threshold silicon left unassigned vs assigned ground (unphysical conductor-limit controls), sigma=10 default-threshold dielectric silicon with a **localized grounded metal contact patch on the far-right silicon bottom margin** (without touching TSV Cu or liner), and duplicate contact case with another mesh growth rate. A contact patch only defines a hypothetical geometric electrical contact, **not proof of ohmic semiconductor boundary physics**. The original 4 TSVs remain unchanged; only reference-case metal patch is added.

Optional deep mode adds six intermediate mesh attempts and contact probes at sigma=1 and 100. A substantive inference about substrate physics requires both contact/no-contact comparison and interpretation of the solver's treatment of dielectric current.

## Command
```bat
py -3.13 "C:\暂时下载\G02_V33_mesh_reference_investigation.py" --mode pilot --student --aedt-version 2025.2
```
Returns `G02_V33_results_bundle.zip` under `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<id>\`.

## Caveats
Do not construe independent mesh count by itself as monotonic refinement or <1% physical accuracy. Script includes automatic C cross-mesh screening, but G and near-zero mutual terms need human review. It does not certify physical backside ohmic contact, independent terminal charge conservation, frequency-dependent C/G or MOS bias. No final DOE/ML labels until these are qualified.
