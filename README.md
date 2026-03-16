# IHP Standard Cells LEGO Models

This project aims to create LEGO models for all IHP Standard Cells using the LDraw (LDR) format, following the SG13G2 "V3 Gold Standard".

## Project Status

The library consists of 84 standard cells. All cells have been physically mapped from LEF to LDR. Migration to the high-fidelity V3 Gold Standard is currently in progress.

| Metric | Status | Pass Rate |
|--------|--------|-----------|
| **Total Cells** | 84 | - |
| **Physical Mapping** | 84/84 | 100% |
| **Geometric Accuracy** | 84/84 | 100% |
| **Pin Existence** | 84/84 | 100% |
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

The following diagram illustrates the generation and verification workflow:

```plantuml
@startuml
skinparam monochrome true
skinparam packageStyle rectangle
skinparam shadowing false

title IHP Standard Cells LEGO Generation Workflow

package "Data Sources" {
    [sg13g2_stdcell.lef] as LEF
    [sg13g2_stdcell.celllist] as List
    [handmade/*.md] as Handmade
}

package "Processing Scripts" {
    [lef_to_ldr.py] as LEF2LDR
    [generate_design_docs.py] as GenDocs
    [design_to_ldr.py] as Design2LDR
    [render_models.sh] as Render
    [generate_gallery.py] as GenGallery
}

package "Intermediate Results" {
    folder "/models/*.ldr" as LDRs
    folder "/design/*.md" as Docs
}

package "Final Outputs" {
    folder "/images/*.jpg" as Images
    folder "/instructions/*.pdf" as PDFs
    [index.html] as Gallery
}

package "Verification" {
    [verify_models_v3.py] as V3
    [verify_spatial_mapping.py] as Spatial
    [verify_macro_dimensions.py] as Dim
    [verify_pin_existence.py] as Pins
    folder "/logs/*.log" as Logs
}

LEF --> LEF2LDR
List --> LEF2LDR
LEF2LDR --> LDRs

LDRs --> GenDocs
Handmade --> GenDocs
GenDocs --> Docs

Docs --> Design2LDR
Design2LDR --> LDRs

LDRs --> Render
Render --> Images
Render --> PDFs

Images --> GenGallery
Gallery <.. GenGallery

LDRs --> V3
LDRs --> Spatial
LDRs --> Dim
LDRs --> Pins

V3 --> Logs
Spatial --> Logs
Dim --> Logs
Pins --> Logs

@enduml
```

## Gallery
The generated LEGO models can be viewed in the [IHP LEGO Models Gallery](https://chatelao.github.io/ihp-standard-cells-lego/).

## Reference
- [IHP Open PDK](https://github.com/IHP-GmbH/IHP-Open-PDK)
- [LDraw File Format](https://www.ldraw.org/article/218.html)
