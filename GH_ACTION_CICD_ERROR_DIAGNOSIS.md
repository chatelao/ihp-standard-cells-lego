# GitHub Action CI/CD Error Diagnosis

## Problem Statement
The GitHub Action `render` job in `render_models.yml` is failing during the "Render models and generate videos" step with exit code 254.

## Symptoms
1. **LDView Errors:**
   - Previous runs showed `OSMesa not working!`.
   - After adding `xvfb-run`, logs show:
     ```
     libEGL warning: DRI3 error: Could not get DRI3 device
     libEGL warning: Ensure your X server supports DRI3 to get accelerated rendering
     EGL configCount: 1
     ```
   - This suggests `ldview` is attempting to use hardware acceleration (DRI3) which is not available in the headless GitHub Actions runner environment.

2. **FFmpeg Failures:**
   - `ffmpeg` fails with: `Could find no file with path 'temp_sg13g2_and2_1/frame_%02d.jpg' and index in the range 0-4`.
   - This confirms that the `ldview` commands executed within the loop are not successfully producing the output images, even though they might not be returning a non-zero exit code that stops the script immediately (or the shell's `-e` behavior isn't catching it inside the loop as expected).

3. **Performance/Resource issues:**
   - Running `xvfb-run` inside a loop 36 times per model is extremely inefficient and can lead to resource exhaustion or race conditions with display allocation.

## Root Cause Analysis
- **Missing Software Rendering Path:** The `ldview-osmesa` build or the underlying Mesa library is trying to use DRI3/Hardware acceleration. In a CI environment, software rendering must be forced.
- **Display Server Overhead:** Repeatedly starting and stopping `xvfb` for every single frame is problematic.

## Proposed Fix
1. **Force Software Rendering:** Set `LIBGL_ALWAYS_SOFTWARE=1` environment variable.
2. **Optimize Xvfb usage:** Wrap the entire rendering logic for a model (static image + video frames) in a single `xvfb-run` call or start `xvfb` once for the whole job.
3. **Verify Output:** Add a check to ensure images are actually created before calling `ffmpeg`.

## Planned Action
Update `.github/workflows/render_models.yml` to:
- Export `LIBGL_ALWAYS_SOFTWARE=1` to force software rendering in headless environments.
- Wrap all model rendering in a single `xvfb-run -a -s "-screen 0 800x600x24"` session for efficiency.
- Added `shopt -s nullglob` and `set -e` for better error handling.
- Added verification of generated frames before calling `ffmpeg`.
