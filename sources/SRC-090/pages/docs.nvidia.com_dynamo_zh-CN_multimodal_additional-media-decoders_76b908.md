source: https://docs.nvidia.com/dynamo/zh-CN/multimodal/additional-media-decoders
lastmod: 2026-09-24T19:58:16.636Z

# Additional Media Decoders

Dynamo’s runtime images ship a deliberately small media stack. The in-tree FFmpeg is built for VP8/VP9 video, and the wider backend decode packages are not pre-installed, which keeps the distributed images small and their input-format surface narrow by default.

Two input classes are already covered without installing anything:

**VP8 and VP9 video**decode through the in-tree FFmpeg.**H.264 and H.265 video**decode on the GPU through NVDEC, which every backend uses by default. NVDEC needs a GPU with a video decode engine and a container granted the`video`

driver capability. See[Video Decode GPU Requirements](https://docs.nvidia.com/dynamo/multimodal/video-decode-gpu-requirements)for the hardware and capability matrix.

Installing an additional decoder package covers what remains:

**AAC and other compressed audio**, which NVDEC does not decode at all.**H.264 and H.265 on hosts where NVDEC is unavailable**— no video decode engine on the GPU, or a container without the`video`

capability.

Each backend decodes such input through a specific Python package whose wheel bundles its own FFmpeg, so the support is added with a plain `pip install`

— no image rebuild. **Nothing installs automatically.** There is no environment switch and no startup hook: an operator runs the install as a deliberate, visible step, so a deployment that broadens the image’s codec surface says so in its Dockerfile, pod spec, or runbook.

**input decoding**only. Generated video

**output**is unaffected and always uses VP9.

## What each backend needs

The lower bound of each spec is the version validated against Dynamo’s multimodal test suite; the upper bound excludes the next major release so an install cannot silently pick up an unvalidated version. PyNvVideoCodec is not in this list because the images already ship it — it is the NVDEC path, not a fallback, so there is nothing to install. torchcodec is left out because no Dynamo decode path imports it.

## Install with pip

The table above is the contract; these commands are its direct translation, and work with the installer of your choice (`pip`

, `uv pip`

, …):

`--no-deps`

keeps the install from changing the image’s pinned dependency stack (for example numpy under PyTorch/vLLM); the carriers only need numpy, which the backend already provides. To pin different versions or install a custom subset, adjust these commands directly — that is the intended customization path.

## Install with the bundled installer

For exactly the tested combinations above, every runtime image also ships an installer as part of the `ai-dynamo`

package. Run it in the worker container (not the frontend) for the backend you deploy:

Compared to the raw pip commands it adds: skip-if-already-importable, a cross-process lock for concurrent runs, a post-install import verification in a fresh interpreter, and a non-zero exit if anything did not land. It deliberately installs only the validated specs — it has no package-selection flags. To see what it would do first:

## Kubernetes

Prefer baking the install into an image layer, so the deployment manifest deploys exactly what was reviewed and scanned:

For a quick evaluation without an image build, run the installer ahead of the worker in the pod command, where it is visible in the manifest:

## Air-gapped and allowlisted networks

The install needs a package index or a local wheelhouse. Point pip at one with `--pip-args`

(use the `=`

form, so a value starting with a dash is not mistaken for an option):

The default pip timeout is 600 seconds (`--timeout-s`

overrides it; `0`

disables it), so a stalled index fails the run rather than hanging it.

## Notes and limits

- For H.264 and H.265, prefer NVDEC. Granting the container the
`video`

driver capability decodes those formats on the GPU with no extra package. Install a software decoder when that is not an option, or when the input is audio. - Installing a decoder package brings in that wheel’s bundled media libraries. The runtime images are scanned for media components at build time; a package installed afterwards is not covered by that scan. Review what your deployment ships — a baked image layer keeps the change visible and reviewable.
- On TensorRT-LLM, the install puts back
`opencv-python-headless`

, which those images deliberately do not ship. H.264 and H.265 already decode there through NVDEC, so install it only for a host where NVDEC is unavailable. - The optional Rust frontend decoder (
`--frontend-decoding`

) links FFmpeg’s compiled-in decoders and always decodes VP8/VP9 regardless of installed Python packages; backend decoding is what an install extends. Re-encoding an input to VP9 (`ffmpeg -i input.mp4 -c:v libvpx-vp9 -an output.webm`

) is an alternative that needs no additional packages.