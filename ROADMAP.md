# Roadmap

## Past Milestones
- [x] **Phase 1: Infrastructure & Specifications**
  - Established repository structure and LDraw V2 modeling standards.
  - Processed IHP SG13G2 LEF files and generated detailed component specifications.
- [x] **Phase 2: Automation & Library Generation**
  - Developed `scripts/lef_to_ldr.py` with 2D tiling and grid alignment for accurate LEF-to-LDR conversion.
  - Automated the generation of all 84 standard cell LDR models.
- [x] **Phase 3: Verification & Quality Assurance (V2)**
  - Implemented a V2 verification suite and validated the initial library.
  - Integrated visual regression testing for the project gallery.
- [x] **Phase 4: CI/CD & Deployment**
  - Configured GitHub Actions for automated headless rendering and documentation deployment.
- [x] **Phase 5: Building Instructions**
  - Implemented automated generation of multi-page PDF building instructions.
- [x] **Phase 6: Bidirectional Generation Chain**
  - Implemented `scripts/design_to_ldr.py` to allow manual edits in design documentation to propagate back to LEGO models.
  - Completed the full automation loop: LEF -> LDR -> Design Docs (Golden Standards) -> LDR.
  - Successfully preserved pin metadata and contact stacks during back-propagation.
- [x] **Phase 0: Repository Housekeeping**
  - Cleaned up transient log files and verification results from the root directory.
  - Updated `.gitignore` and centralized verification outputs into `logs/`.
  - Deprecated and removed obsolete V2 scripts.
- [x] **Phase 7: Mapping Review Fixes (Buildability, Fidelity & Purchasability)**
  - [x] **Step 1: Structural Buildability Verifier & Hygiene** — Removed stray `sg13g2_and3_1_from_lef.*` files, fixed `'T'` typo in `handmade/sg13g2_a21o_1.md` and `GOLDEN_STANDARD.md`, and implemented `scripts/verify_buildability.py`.
  - [x] **Step 2: Fix CIF Layer Mapping, Output Pin Semantics & Rasterization** — Switched N-Well from `L14D0` (`pSD`) to `L31D0` (`NWell`), added `L19D0` (`Via1`) and `L10D0` (`Metal2`), read LEF pin directions, fixed box arg order & polygon intersection, and implemented net-aware Metal 1 tiling.
  - [x] **Step 3: Structural Interlocking, Dielectric Supports & Edge Snapping** — Restored `Y=-16` Substrate/N-Well fill, fixed `z==6` contact base logic, implemented seam-staggered base tiling, `Y=-8` half-lap snapping tabs (`Z=1, 13`), and Trans-Clear (`47`) dielectric support pillars.
  - [x] **Step 4: Modern BrickLink-Available Palette & Instruction Sub-Stepping** — Migrated to modern LDraw colors (`72`, `71`, `212`, `3070b.dat`, `47`, `25`) with per-color mold whitelisting, ordered `6141.dat` before `3062b.dat`, and chunked steps (≤28 parts/step).
  - [x] **Step 5: Harmonize Parity, `/handmade` Preservation & Full Library Regeneration** — Preserved all 9 `/handmade` files, unified parity & blob naming in `verify_models_v3.py`, updated `MAPPING_RULEBOOK.md`, and regenerated + verified all 84 cells.

## Next Steps
- [ ] Re-render all 84 `.jpg` images and `.pdf` building instructions in CI via GitHub Actions.
- [ ] Physically test-build a multi-cell row (e.g., `inv_1` + `nand2_1` + `a21o_1`) using the generated BrickLink BOM.
- [ ] Implement advanced modeling for custom macros and analog blocks.
- [ ] Explore 3D printable STL exports for physical chip visualization.
- [ ] Extend the library to include additional IHP SG13G2 families (e.g., IO cells).
