# Roadmap

## Past Milestones
- [x] **Phase 1: Infrastructure & Specifications**
  - Established repository structure and LDraw V2 modeling standards.
  - Processed IHP SG13G2 LEF files and generated detailed component specifications.
- [x] **Phase 2: Automation & Library Generation**
  - Developed `scripts/lef_to_ldr.py` with 2D tiling and grid alignment for accurate LEF-to-LDR conversion.
  - Automated the generation of all 84 standard cell LDR models.
- [x] **Phase 3: Verification & Quality Assurance**
  - Implemented a V2 verification suite (`scripts/verify_models_v2.py`) and validated the entire library.
  - Fixed spatial mapping verification to correctly isolate pin components from obstructions.
  - Integrated visual regression testing for the project gallery and updated `index.html`.
- [x] **Phase 4: CI/CD & Deployment**
  - Configured GitHub Actions for automated headless rendering and documentation deployment.

## Future Work
- [ ] Implement advanced modeling for custom macros and analog blocks.
- [ ] Explore 3D printable STL exports for physical chip visualization.
- [ ] Extend the library to include additional IHP SG13G2 families (e.g., IO cells).
