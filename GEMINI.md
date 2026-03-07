# Project Goal
- Create for all IHP Standard Cells a LEGO model with LDR (https://www.ldraw.org/article/218.html)

# Planning & Progress tracking
- Keep an up to date file "ROADMAP.md" with the next 5 steps and all past steps having checkboxes.

# Project structure
- / - Keep only GEMINI.md, README.md and ROADMAP.md in the root directory
- /specifications - Download and store the original standard cell definitions from the IHP PDK here
- /specifications - Convert "non .md" files for caching and readability purpose to Markdown here
- /models - The LEGO LDR models of the cells
- /images - The rendered LEGO models
- /.github/workflows - For every push on every branch, re-rendender all models to images
- README.md - Update overview of the product
