# Roadmap

## Past Steps
- [x] Research IHP PDK and identify standard cell sources
- [x] Create initial `README.md` and project documentation
- [x] Create project directory structure (`specifications/`, `models/`, `images/`)
- [x] Fetch and store IHP SG13G2 standard cell list in `specifications/`
- [x] Convert cell specifications to Markdown for better readability
- [x] Fetch and store IHP SG13G2 LEF specification
- [x] Define LEGO modeling guidelines for semiconductor cells
- [x] Set up GitHub Actions for automated LEGO model rendering
- [x] Fix GitHub Action rendering by updating OpenGL dependencies
- [x] Fix GH Action Workflow failure and trigger render on every push
- [x] Enhance CI/CD to fully synchronize `/images` with models on every push
- [x] Generate detailed markdown for all standard cells and subcomponents
- [x] Separate GitHub Pages deployment into its own workflow and restore video rendering
- [x] Fix rendering errors and improve CI/CD diagnostic logging
- [x] Enhance GitHub Pages gallery with detailed model cards and direct links
- [x] Refine modeling guidelines based on initial model feedback
- [x] Automate the generation of LDR models from LEF coordinates
- [x] Refine automation script for complex pin geometries
- [x] Implement LDR model for 3-input NAND gate (`sg13g2_nand3_1`) (V2 Migration)
- [x] Implement LDR model for 3-input NOR gate (`sg13g2_nor3_1`)
- [x] Implement LDR model for 4-input NAND gate (`sg13g2_nand4_1`)
- [x] Implement LDR model for 4-input NOR gate (`sg13g2_nor4_1`)
- [x] Remove animations from workflows and GitHub Pages

## Next 5 Steps
- [ ] Implement all standard cell LDR models
