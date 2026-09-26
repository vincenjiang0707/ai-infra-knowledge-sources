source: https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/v-llm-omni
lastmod: 2026-09-24T19:58:16.636Z

vLLM-Omni


vLLM-Omni

vLLM-Omni serves text-to-image, text-to-video, image-to-video, and text-to-speech models through OpenAI-compatible endpoints.

Dynamo supports multimodal generation through the [vLLM-Omni](https://github.com/vllm-project/vllm-omni) backend. This integration exposes text-to-image, text-to-video, image-to-video, and text-to-audio (TTS) capabilities via OpenAI-compatible API endpoints.

## Prerequisites

This guide assumes familiarity with deploying Dynamo with vLLM as described in the [vLLM backend guide](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm).

### Installation

Dynamo container images include vLLM-Omni pre-installed. If you are using `pip install ai-dynamo[vllm]`

, vLLM-Omni is **not** included automatically because the matching release is not yet available on PyPI. Install it separately from source, pinning the vLLM-Omni release that matches your installed vLLM version (see the [vLLM-Omni releases](https://github.com/vllm-project/vllm-omni/releases) page):


ARM64 not supported:vLLM-Omni is currently only installed on`amd64`

builds. On`arm64`

, the container build skips the install and vLLM-Omni features are unavailable.

## Supported Modalities

The `--output-modalities`

flag determines which endpoint(s) the worker registers. When set to `image`

, both `/v1/chat/completions`

(returns inline base64 images) and `/v1/images/generations`

are available. When set to `video`

, the worker serves `/v1/videos`

. When set to `audio`

, the worker serves `/v1/audio/speech`

.

## Tested Models

To run a non-default model, pass `--model`

to any launch script:

## Text-to-Image

Launch using the provided script with `Qwen/Qwen-Image`

:

### Via `/v1/chat/completions`


The response includes base64-encoded images inline:

### Via `/v1/images/generations`


## Text-to-Video

Launch using the provided script with `Wan-AI/Wan2.1-T2V-1.3B-Diffusers`

:

Generate a video via `/v1/videos`

:

The response returns a video URL or base64 data depending on `response_format`

:

The `/v1/videos`

endpoint also accepts NVIDIA extensions via the `nvext`

field for fine-grained control:

## Image-to-Video

Image-to-video (I2V) uses the same `/v1/videos`

endpoint as text-to-video, with an additional `input_reference`

field that provides the source image. The image can be an HTTP URL, a base64 data URI, or a local file path.

Launch with the provided script using `Wan-AI/Wan2.2-TI2V-5B-Diffusers`

:

Generate a video from an image:

The `input_reference`

field accepts:

**HTTP/HTTPS URL**:`"https://example.com/image.png"`

**Base64 data URI**:`"data:image/png;base64,iVBORw0KGgo..."`

**Local file path**:`"/path/to/image.png"`

or`"file:///path/to/image.png"`


The I2V-specific `nvext`

fields (`boundary_ratio`

, `guidance_scale_2`

) control the dual-expert MoE denoising schedule in Wan2.x models. See [Wan2.2-I2V model card](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B-Diffusers) for details.

## Text-to-Audio (TTS)

Launch using the provided script with `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice`

:

### CustomVoice (predefined speakers)

### CustomVoice with style instructions

### VoiceDesign (describe a voice)

### Parameters

The `/v1/audio/speech`

endpoint follows the [vLLM-Omni](https://docs.vllm.ai/projects/vllm-omni/en/latest/) API format. All TTS-specific parameters are top-level fields:

Available voices and languages are loaded dynamically from the model’s `config.json`

at startup. Non-Qwen3-TTS audio models (e.g., MiMo-Audio) use a generic text prompt and ignore TTS-specific parameters.

## CLI Reference

The omni backend uses a dedicated entrypoint: `python -m dynamo.vllm.omni`

.

## Storage Configuration

Generated images, videos, and audio files are stored via [fsspec](https://filesystem-spec.readthedocs.io/), which supports local filesystems, S3, GCS, and Azure Blob.

By default, media is written to the local filesystem at `file:///tmp/dynamo_media`

. To use cloud storage:

When `--media-output-http-url`

is set, response URLs are rewritten as `{base-url}/{storage-path}`

(e.g., `https://cdn.example.com/media/videos/req-id.mp4`

). When unset, the raw filesystem path is returned.

For S3 credential configuration, set the standard AWS environment variables (`AWS_ACCESS_KEY_ID`

, `AWS_SECRET_ACCESS_KEY`

) or use IAM roles. See the [fsspec S3 docs](https://s3fs.readthedocs.io/en/latest/#credentials) for details.

## Stage Configuration

Omni pipelines are configured via YAML stage configs. By default vLLM-Omni ships built-in stage configs for supported models, so no `--stage-configs-path`

is needed unless you want to override the defaults. For full documentation on stage config format and multi-stage pipelines, refer to the [vLLM-Omni Stage Configs documentation](https://docs.vllm.ai/projects/vllm-omni/en/latest/configuration/stage_configs/).

## Disaggregated Multi-Stage Serving

For models with multiple pipeline stages (e.g., AR + Diffusion), Dynamo supports disaggregated serving where each stage runs as an independent process on its own GPU. This enables independent scaling, GPU isolation, and multi-worker replicas per stage.

### Architecture

Each stage runs as an independent process on its own GPU. A lightweight router coordinates them, acting as a **pure message broker** — it never inspects or transforms inter-stage data.

**How it works:**

- The router sends the initial request to Stage 0 and receives back a lightweight connector reference (pointer to the output in shared memory).
- The router forwards that reference — unchanged — to Stage 1. It never reads the bulk data.
- Each stage fetches its inputs from the connector, runs any model-specific processor (e.g.,
`ar2diffusion`

,`thinker2talker`

), then runs its engine. - The final stage’s result goes back to the router for formatting and response.
- Connector references accumulate as the pipeline progresses, so any stage can access outputs from all previous stages.

### Data Flow

### Quick Start: GLM-Image (2-Stage, 2 GPUs)

GLM-Image is a 2-stage text-to-image model with an AR stage (generates prior token IDs) and a DiT stage (diffusion denoising + VAE decode). The built-in vLLM-Omni stage config already assigns each stage to a separate GPU.


Experimental:GLM-Image support is experimental; generation may fail or produce incorrect/garbled outputs for some prompts and sizes.

Test:

### Scaling Stage Replicas

Each stage registers independently with Dynamo’s service discovery. To scale a bottleneck stage, launch additional workers with the same `--stage-id`

on different GPUs — the router automatically load-balances across all replicas for that stage. Other stages are unaffected.

### Tested Models

### CLI Flags (Disaggregated Mode)

## Current Limitations

- Image input is supported only for I2V via
`input_reference`

in`/v1/videos`

. Other endpoints accept text prompts only. - KV cache events are not published for omni workers.
- Each worker supports a single output modality at a time.
- Audio: streaming (
`stream: true`

) is not yet supported. - Audio: Base task (voice cloning) is not yet supported.
- Disaggregated mode:
`async_chunk=true`

(streaming between stages) is not yet supported.