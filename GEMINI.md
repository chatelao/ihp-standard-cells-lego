# Project Goal
- Create for all IHP Standard Cells a LEGO model with LDR (https://www.ldraw.org/article/218.html)

# Planning & Progress tracking
- Keep an up to date file "ROADMAP.md" with the next 5 steps and all past steps having checkboxes.
- If necessary split steps into 2-5 additional substeps if the complexity of the task is high.
- For each problem draft first three different solutions and then choose the best one, track the
  reason to discard in "DISCARDED.md" in the most relevant directory.
- Before publishing a pull request to GitHub, pull main from the  origin and resolve all merge conflicts.

# Project structure
- / - Keep only GEMINI.md, README.md and ROADMAP.md in the root directory
- /specifications - Download and store the original standard cell definitions from the IHP PDK here
- /specifications - Convert "non .md" files for caching and readability purpose to Markdown here
- /specifications/MODELING_GUIDELINES.md - Instructions about how to draw the LEGO models from specifications
- /models - The LEGO LDR models of the cells, the lego have to be arranged in a way "snapping" into each others
- /images - The rendered LEGO models
- /instructions - The automated instructions how to build the LEGO model as PDF (not committed to repo, only deployed to GitHub Pages)
- /design - Layer-by-layer ASCII art design documentation for cells
- /.github/workflows - For every push on every branch, re-render all models to images and instructions
- README.md - Update overview of the product

# Design Documentation Rules
- For each standard cell, maintain a Markdown file in `/design` with layer-by-layer ASCII art.
- The ASCII art should follow the character mapping defined in `specifications/MODELING_GUIDELINES.md`.
