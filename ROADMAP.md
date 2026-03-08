# Roadmap

## Past Steps
- [x] Research IHP PDK and identify standard cell sources
- [x] Create initial `README.md` and project documentation
- [x] Create project directory structure (`specifications/`, `models/`, `images/`)
- [x] Fetch and store IHP SG13G2 standard cell list in `specifications/`
- [x] Convert cell specifications to Markdown for better readability
- [x] Fetch and store IHP SG13G2 LEF specification
- [x] Define LEGO modeling guidelines for semiconductor cells
- [x] Create the first LEGO LDR model (`sg13g2_inv_1`)
- [x] Set up GitHub Actions for automated LEGO model rendering
- [x] Implement LDR model for basic NAND gate (`sg13g2_nand2_1`)
- [x] Implement LDR model for basic NOR gate (`sg13g2_nor2_1`)
- [x] Fix GitHub Action rendering by updating OpenGL dependencies
- [x] Fix GH Action Workflow failure and trigger render on every push
- [x] Enhance CI/CD to fully synchronize `/images` with models on every push
- [x] Implement LDR model for D-Flip-Flop (`sg13g2_dfrbp_1`)
- [x] Implement LDR model for AND gate (`sg13g2_and2_1`)
- [x] Implement LDR model for OR gate (`sg13g2_or2_1`)
- [x] Implement LDR model for XOR gate (`sg13g2_xor2_1`)
- [x] Generate detailed markdown for all standard cells and subcomponents
- [x] Separate GitHub Pages deployment into its own workflow and restore video rendering

- [x] Enhance GitHub Pages gallery with detailed model cards and direct links
- [x] Refine modeling guidelines based on initial model feedback
- [x] Implement LDR model for buffer (sg13g2_buf_1)
- [x] Implement LDR model for MUX2 (`sg13g2_mux2_1`)
- [x] Implement LDR model for XNOR gate (`sg13g2_xnor2_1`)

## Next 5 Steps
- [ ] Automate the generation of LDR models from LEF coordinates
- [ ] Implement LDR model for D-Latch (`sg13g2_dlrbp_1`)
- [ ] Implement LDR model for Adder (`sg13g2_fa_1`)
- [ ] Implement LDR model for Decoders (`sg13g2_dec24_1`)
- [ ] Implement LDR model for Clock Buffer (`sg13g2_clkbuf_1`)
