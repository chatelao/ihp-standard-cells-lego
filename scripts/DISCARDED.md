# Discarded Design Options (Mapping Review Fixes)

This document records the 3-option design evaluations performed while fixing the physical LEGO buildability, semiconductor mapping, and purchasability flaws identified in the mapping review, in accordance with `GEMINI.md`.

## 1. Supporting Elevated Metal 1 (`Y=-56`) Plates & Cantilevers
- **Option A — Greedy Metal 1 Tiling Only (Status Quo):**
  - *Discarded:* Leaves `1,074` Metal 1 plates with zero contact pillars underneath and `774` single-stud spinners (`262` cantilevers of area ≥ 4). Physically unbuildable.
- **Option B — Full Solid Trans-Clear (`47`) Interlayer Dielectric (ILD) Fill at `Y=-32..-48`:**
  - *Discarded:* Increases piece count by ~3× (~60,000+ pieces across 84 cells) and obscures internal Polysilicon (`Y=-24`) and Diffusion (`Y=-16`) layers in perspective and side-angled renders.
- **Option C — Net-Aware Metal 1 Tiling + Trans-Clear (`47`) Dielectric Support Pillars (Chosen):**
  - Every multi-stud Metal 1 plate (`area >= 2`) is guaranteed ≥2 support pillars (using real White `15` contact stacks where present, and Trans-Clear `47` `3062b.dat` + `6141.dat` dielectric support pillars under uncontacted sub-plates, corners, and cantilevers > 2 studs). Keeps internal layers clearly visible while achieving 0 floating parts and 0 spinners.

## 2. Base Foundation Seam-Staggering & Cell-to-Cell Snapping
- **Option A — Flush Greedy Tiling from `(0, 0)` (Status Quo):**
  - *Discarded:* `83/84` cells split into disconnected base chunks (`Z=13..14` detached VDD strip in `43` cells, vertical `X` guillotine seams in `25` cells), and `0/84` cells snap together horizontally.
- **Option B — Embedded Technic Bricks (`3700.dat`) & Pins on East/West Edges:**
  - *Discarded:* Standard Technic bricks are 3 plates (`24` LDU) tall, protruding into or colliding with the `Y=-16` Active layer (`16` LDU above `Y=0`).
- **Option C — Seam-Staggered ("Bricklaying") Tiling + Half-Lap `Y=-8` Edge Snapping Tabs (Chosen):**
  - `Y=0` uses `Z`-split `8+7` (straddling `Z=7..8` and `Z=13..14`) and `X`-offset staggering relative to `Y=-8` and `Y=-16` so no seam aligns across adjacent layers.
  - At `Y=-8` on isolation rows `Z=1` and `Z=13`, West edge `X=0` is recessed 1 stud and East edge `X=W` projects +1 stud as a half-lap snapping tab, allowing adjacent cells in a standard-cell row to physically lock together without protruding into `VDD`/`VSS` rails or `Y=-16` Active.

## 3. Canonical CIF+LEF Hybrid Generation vs. Separate Pipelines
- **Option A — Keep `cif_to_ldr.py` + `lef_to_ldr.py` Separate:**
  - *Discarded:* `generate_all_models.py` bypassed `lef_to_ldr.py`, losing LEF pin directions (`31` miscolored outputs) and `Y=-16` fill (`80/84` cells), while `lef_to_ldr.py` had stale fallback heuristics.
- **Option B — Pure LEF-Only Generation:**
  - *Discarded:* LEF lacks `NWell` (`L31D0`), `Activ` (`L1D0`), `GatPoly` (`L5D0`), and `Cont` (`L6D0`) geometries.
- **Option C — Unified CIF Geometry + LEF Port Semantics + Net-Aware Tiling (Chosen):**
  - CIF provides exact physical layers (`L31D0` NWell, `L1D0` Activ, `L5D0` GatPoly, `L6D0` Cont, `L8D0` Metal1, `L19D0` Via1, `L10D0` Metal2); LEF provides authoritative pin names and directions (`INPUT`, `OUTPUT`, `TRISTATE`, `INOUT`, `POWER`/`GROUND`).

## 4. Real-World LEGO Color & Mold Availability
- **Option A — Legacy Pre-2004 LDraw Colors (`7`, `8`, `9`, `3070.dat`) (Status Quo):**
  - *Discarded:* Colors `7`/`8` were retired in 2004 and never existed in `91405.dat`, `92438.dat`, or `60479.dat`; vintage `9` (Light Blue) lacks large plates.
- **Option B — Custom 3D-Printed / Non-Standard Parts:**
  - *Discarded:* Defeats the goal of building models from real LEGO bricks.
- **Option C — Modern BrickLink-Available Palette + Per-Color Mold Whitelist (Chosen):**
  - Migrate `8` → `72` (Dark Bluish Gray), `7` → `71` (Light Bluish Gray), `9` → `212` (Bright Light Blue), `3070.dat` → `3070b.dat`, and decompose plates unavailable in `38` (Dark Orange), `288` (Dark Green), `212`, or `272` (Dark Blue) into widely available `2xN`/`1xN` plates.

## 5. Contact Parity Rule Harmonization
- **Option A — Keep `X=8` Symmetric Parity Flip (`ODD` if `X<8`, `EVEN` if `X>=8`):**
  - *Discarded:* Conflicts with uniform CMOS gate/diffusion pitch across wide cells, causing `39/84` V3 failures and `84/84` LEF contact failures.
- **Option B — Enforce Strict `ODD`-Only Internal Contacts Everywhere:**
  - *Discarded:* Fails wide multi-finger cells where diffusion/gate pitch drifts by 1 stud.
- **Option C — Uniform Rail Parity + CIF-Driven Active/Gate Contact Placement (Chosen):**
  - `VDD` (`Z=14`) and `VSS` (`Z=0`) rails place contacts on `EVEN` `X`-studs (`0, 2, 4, ...`). Internal contacts follow physical CIF `L6D0` locations snapped to the nearest valid silicon stud (`Poly` or `Active`) without artificial `X=8` phase flips.
