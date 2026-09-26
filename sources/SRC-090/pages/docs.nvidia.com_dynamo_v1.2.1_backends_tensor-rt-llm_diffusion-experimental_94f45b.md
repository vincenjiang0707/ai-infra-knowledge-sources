source: https://docs.nvidia.com/dynamo/v1.2.1/backends/tensor-rt-llm/diffusion-experimental
lastmod: 2026-09-24T19:58:16.636Z

Video Diffusion Support (Experimental)


Video Diffusion Support (Experimental)

For general TensorRT-LLM features and configuration, see the [Reference Guide](https://docs.nvidia.com/dynamo/v1.2.1/backends/tensor-rt-llm/reference-guide).

Dynamo supports video generation using diffusion models through the `--modality video_diffusion`

flag and
image generation through `--modality image_diffusion`

flag.

## Requirements

**TensorRT-LLM with visual_gen**: The`visual_gen`

module is part of TensorRT-LLM (`tensorrt_llm._torch.visual_gen`

). Install TensorRT-LLM following the[official instructions](https://github.com/NVIDIA/TensorRT-LLM#installation).**dynamo-runtime with multimodal API**: The Dynamo runtime must include`ModelType.Videos`

or`ModelType.Images`

support. Ensure you’re using a compatible version.**VIDEO diffusion: imageio with ffmpeg**: Required for encoding generated frames to MP4 video. The Dynamo TRT-LLM runtime container ships an LGPL-only ffmpeg CLI built with the NVIDIA NVENC H.264 encoder (`h264_nvenc`

) and`libvpx_vp9`

for WebM, and points`imageio`

at it via`IMAGEIO_FFMPEG_EXE=/usr/local/bin/ffmpeg`

— the GPL-encumbered ffmpeg binary normally shipped inside the`imageio-ffmpeg`

PyPI wheel is**not**installed. If you’re running outside the container, install the Python wrapper without the bundled binary and point it at your own ffmpeg:MP4 output requires an NVIDIA GPU at runtime (NVENC is a hardware encoder).

## Supported Models

The pipeline type is **auto-detected** from the model’s `model_index.json`

— no `--model-type`

flag is needed.

## Quick Start

### Video Diffusion

#### Launch worker

#### API Endpoint

Video generation uses the `/v1/videos`

endpoint:

### Image Diffusion

#### Launch worker

#### API Endpoint

Image generation uses the `/v1/images/generations`

endpoint:

## Configuration Options

## Limitations

- Diffusion is experimental and not recommended for production use
- Only text-to-video and text-to-image is supported in this release (image-to-video planned)
- Requires GPU with sufficient VRAM for the diffusion model