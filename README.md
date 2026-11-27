# IHP Standard Cells LEGO Models

This project aims to create LEGO models for all IHP Standard Cells using the LDraw (LDR) format, following the SG13G2 "V3 Gold Standard".

## Project Status

The library consists of 84 standard cells. All 84 cells are physically mapped from CIF+LEF to buildable LDR models with seam-staggered interlocking bases, half-lap cell-to-cell snapping tabs, Trans-Clear dielectric support pillars, and BrickLink-available LEGO elements.

| Metric | Status | Pass Rate |
|--------|--------|-----------|
| **Total Cells** | 84 | - |
| **3D LEGO Buildability (`verify_buildability.py`)** | 84/84 | 100% |
| **Base Layer Coverage (`verify_layers_coverage.py`)** | 84/84 | 100% |
| **Macro Dimensions (`verify_macro_dimensions.py`)** | 84/84 | 100% |
| **Pin Existence (`verify_pin_existence.py`)** | 84/84 | 100% |
| **Spatial Mapping (`verify_spatial_mapping.py`)** | 84/84 | 100% |
| **V3 Gold Standard Compliance (`verify_models_v3.py`)** | 84/84 | 100% |

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

The following diagram illustrates the generation and verification workflow:

![IHP Standard Cells LEGO Generation Workflow](https://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/chatelao/ihp-standard-cells-lego/main/specifications/workflow.puml)

## Gallery
The generated LEGO models can be viewed in the [IHP LEGO Models Gallery](https://chatelao.github.io/ihp-standard-cells-lego/).

## Reference
- [IHP Open PDK](https://github.com/IHP-GmbH/IHP-Open-PDK)
- [LDraw File Format](https://www.ldraw.org/article/218.html)
