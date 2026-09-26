source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/user-guides/diffusion/trt-llm-diffusion
lastmod: 2026-09-23T23:30:39.914Z

Video Diffusion Support (Experimental)


Video Diffusion Support (Experimental)

For general TensorRT-LLM features and configuration, see the [Reference Guide](https://docs.nvidia.com/dynamo/v1.1.1/backends/tensor-rt-llm/reference-guide).

Dynamo supports video generation using diffusion models through the `--modality video_diffusion`

flag and
image generation through `--modality image_diffusion`

flag.

## Requirements

**TensorRT-LLM with visual_gen**: The`visual_gen`

module is part of TensorRT-LLM (`tensorrt_llm._torch.visual_gen`

). Install TensorRT-LLM following the[official instructions](https://github.com/NVIDIA/TensorRT-LLM#installation).**dynamo-runtime with multimodal API**: The Dynamo runtime must include`ModelType.Videos`

or`ModelType.Images`

support. Ensure you’re using a compatible version.**VIDEO diffusion: imageio with ffmpeg**: Required for encoding generated frames to MP4 video:

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