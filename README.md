# IHP Standard Cells LEGO Models

This project aims to create LEGO models for all IHP Standard Cells using the LDraw (LDR) format, following the SG13G2 "V3 Gold Standard".

## Project Status

The library consists of 84 standard cells. All cells have been physically mapped from LEF to LDR. Migration to the high-fidelity V3 Gold Standard is currently in progress.

| Metric | Status | Pass Rate |
|--------|--------|-----------|
| **Total Cells** | 84 | - |
| **Macro Dimensions** | 84/84 | 100% |
| **Pin Existence** | 84/84 | 100% |
| **Spatial Mapping** | 84/84 | 100% |
| **V3 Gold Standard Compliance** | 45/84 | 53% |

## Goal
To provide a physical, LEGO-based representation of semiconductor standard cells from the IHP PDK, specifically targeting the SG13G2 process.

## Structure
- `/specifications`: Original and converted (Markdown) standard cell definitions from the IHP PDK.
- `/models`: LEGO LDR models of the cells.
- `/images`: Rendered images of the LEGO models.
- `/design`: Detailed layer-by-layer ASCII art documentation.
- `/handmade`: Manually verified "Gold Standard" reference designs.
- `.github/workflows`: Automated rendering and verification on every push.

## Workflow

The project utilizes a CIF-driven generation flow, orchestrated by `scripts/generate_all_models.py`. The workflow follows these steps:

1.  **Initial Generation**: `scripts/cif_to_ldr.py` converts physical layout data (CIF) into base LDraw (LDR) models.
2.  **Documentation Update**: `scripts/generate_design_docs.py` creates or updates Markdown documentation in `/design`, preserving `GOLDEN STANDARD` sections from `/handmade`.
3.  **Model Refinement**: `scripts/design_to_ldr.py` propagates the refined physical mapping from documentation back into the LDR models.
4.  **Specialty Imaging**:
    *   `scripts/generate_construction_images.py` generates layer-by-layer assembly views.
    *   `scripts/generate_top_images.py` (via `scripts/render_ldr_top.py`) produces orthographic top-down PNG renders.
5.  **Final Rendering**: `scripts/render_models.sh` uses `LDView` to generate perspective JPGs and PDF instructions.
6.  **Gallery Update**: `scripts/generate_gallery.py` refreshes the web-based gallery.

The following diagram illustrates the generation and verification workflow:

![IHP Standard Cells LEGO Generation Workflow](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/chatelao/ihp-standard-cells-lego/main/specifications/workflow.puml)

## Gallery
The generated LEGO models can be viewed in the [IHP LEGO Models Gallery](https://chatelao.github.io/ihp-standard-cells-lego/).

## Reference
- [IHP Open PDK](https://github.com/IHP-GmbH/IHP-Open-PDK)
- [LDraw File Format](https://www.ldraw.org/article/218.html)
