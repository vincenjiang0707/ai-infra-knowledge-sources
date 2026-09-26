source: https://docs.nvidia.com/dynamo/v1.0.0/user-guides/diffusion/trt-llm-diffusion
lastmod: 2026-09-24T19:58:16.636Z

Video Diffusion Support (Experimental)


Video Diffusion Support (Experimental)

For general TensorRT-LLM features and configuration, see the [Reference Guide](https://docs.nvidia.com/dynamo/v1.0.0/backends/tensor-rt-llm/reference-guide).

Dynamo supports video generation using diffusion models through the `--modality video_diffusion`

flag.

## Requirements

**TensorRT-LLM with visual_gen**: The`visual_gen`

module is part of TensorRT-LLM (`tensorrt_llm._torch.visual_gen`

). Install TensorRT-LLM following the[official instructions](https://github.com/NVIDIA/TensorRT-LLM#installation).**imageio with ffmpeg**: Required for encoding generated frames to MP4 video:**dynamo-runtime with video API**: The Dynamo runtime must include`ModelType.Videos`

support. Ensure you’re using a compatible version.

## Supported Models

The pipeline type is **auto-detected** from the model’s `model_index.json`

— no `--model-type`

flag is needed.

## Quick Start

## API Endpoint

Video generation uses the `/v1/videos`

endpoint:

## Configuration Options

## Limitations

- Video diffusion is experimental and not recommended for production use
- Only text-to-video is supported in this release (image-to-video planned)
- Requires GPU with sufficient VRAM for the diffusion model