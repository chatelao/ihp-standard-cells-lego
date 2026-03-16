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

## Current Focus
- [ ] **Phase 6: V3 Gold Standard Migration & Validation**
  - [x] Define V3 Gold Standard specifications (stacking, parity, dimensions).
  - [ ] Achieve 100% compliance with the V3 verification suite (Current: 12/84).
  - [ ] Fix VSS/VDD rail contact parity issues (standardizing on ODD studs for VSS).
  - [ ] Correct NMOS and PMOS active contact alignment across all 84 cells.
  - [ ] Resolve symmetric parity for input pins in "Big" models (> 7 studs).

## Future Work
- [ ] Implement advanced modeling for custom macros and analog blocks.
- [ ] Explore 3D printable STL exports for physical chip visualization.
- [ ] Extend the library to include additional IHP SG13G2 families (e.g., IO cells).
