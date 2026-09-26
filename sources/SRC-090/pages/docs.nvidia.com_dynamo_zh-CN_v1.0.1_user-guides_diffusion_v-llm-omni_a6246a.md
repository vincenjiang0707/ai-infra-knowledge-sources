source: https://docs.nvidia.com/dynamo/zh-CN/v1.0.1/user-guides/diffusion/v-llm-omni
lastmod: 2026-09-23T23:30:39.914Z

vLLM-Omni


vLLM-Omni

Dynamo supports multimodal generation through the [vLLM-Omni](https://github.com/vllm-project/vllm-omni) backend. This integration exposes text-to-text, text-to-image, and text-to-video capabilities via OpenAI-compatible API endpoints.

## Prerequisites

This guide assumes familiarity with deploying Dynamo with vLLM as described in the [vLLM backend guide](https://docs.nvidia.com/dynamo/v1.0.1/backends/v-llm).

### Installation

Dynamo container images include vLLM-Omni pre-installed. If you are using `pip install ai-dynamo[vllm]`

, vLLM-Omni is **not** included automatically because the matching release is not yet available on PyPI. Install it separately from source:

## Supported Modalities

The `--output-modalities`

flag determines which endpoint(s) the worker registers. When set to `image`

, both `/v1/chat/completions`

(returns inline base64 images) and `/v1/images/generations`

are available. When set to `video`

, the worker serves `/v1/videos`

.

## Tested Models

To run a non-default model, pass `--model`

to any launch script:

## Text-to-Text

Launch an aggregated deployment (frontend + omni worker):

This starts `Qwen/Qwen2.5-Omni-7B`

with a single-stage thinker config on one GPU.

Verify the deployment:

This script uses a custom stage config (`stage_configs/single_stage_llm.yaml`

) that configures the thinker stage for text generation. See [Stage Configuration](https://docs.nvidia.com/dynamo/v1.0.1/user-guides/diffusion/v-llm-omni#stage-configuration) for details.

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

## CLI Reference

For the full list of Omni-related flags (including `--omni`

, `--output-modalities`

, `--stage-configs-path`

, `--media-output-fs-url`

, `--media-output-http-url`

, and the `--omni-*`

diffusion flags), run:

See also the [Argument Reference](https://docs.nvidia.com/dynamo/v1.0.1/additional-resources/v-llm-details/reference-guide#argument-reference) in the Reference Guide.

## Storage Configuration

Generated images and videos are stored via [fsspec](https://filesystem-spec.readthedocs.io/), which supports local filesystems, S3, GCS, and Azure Blob.

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

Omni pipelines are configured via YAML stage configs. See [ examples/backends/vllm/launch/stage_configs/single_stage_llm.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.0.1/examples/backends/vllm/launch/stage_configs/single_stage_llm.yaml) for an example. For full documentation on stage config format and multi-stage pipelines, refer to the

[vLLM-Omni Stage Configs documentation](https://docs.vllm.ai/projects/vllm-omni/en/latest/configuration/stage_configs/).

## Current Limitations

- Image input is supported only for I2V via
`input_reference`

in`/v1/videos`

. Other endpoints accept text prompts only. - KV cache events are not published for omni workers.
- Each worker supports a single output modality at a time.