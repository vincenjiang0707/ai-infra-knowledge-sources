source: https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/diffusion
lastmod: 2026-09-24T19:58:16.636Z

# Diffusion

Dynamo SGLang supports three types of diffusion-based generation: **LLM diffusion** (text generation via iterative refinement), **image diffusion** (text-to-image), and **video generation** (text-to-video). Each uses a different worker flag and handler, but all integrate with SGLang’s `DiffGenerator`

.

## Overview

If you see a CuDNN version mismatch error on startup (`cuDNN frontend 1.8.1 requires cuDNN lib >= 9.5.0`

), set `SGLANG_DISABLE_CUDNN_CHECK=1`

before launching. This is common when PyTorch ships a CuDNN version older than what SGLang requires for Conv3d operations.

## LLM Diffusion

Diffusion Language Models generate text through iterative refinement rather than autoregressive token-by-token generation. The model starts with masked tokens and progressively replaces them with predictions, refining low-confidence tokens each step.

LLM diffusion is auto-detected: when `--dllm-algorithm`

is set, the worker automatically uses `DiffusionWorkerHandler`

without needing a separate flag. For more details on diffusion algorithms, see the [SGLang Diffusion Language Models documentation](https://github.com/sgl-project/sglang/blob/main/docs/supported_models/text_generation/diffusion_language_models.md).

### Launch

See the [launch script](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/examples/backends/sglang/launch/diffusion_llada.sh) for configuration options.

### Test

## Image Diffusion

Image diffusion workers generate images from text prompts using SGLang’s `DiffGenerator`

. Generated images are returned as either URLs (when using `--media-output-fs-url`

for storage) or base64 data, in an OpenAI-compatible response format.

### Launch

Supports local storage (`--fs-url file:///tmp/images`

) and S3 (`--fs-url s3://bucket`

). Pass `--http-url`

to set the base URL for serving stored images. See the launch script for all configuration options.

### Test

## Video Generation

Video generation workers produce videos from text or image prompts using SGLang’s `DiffGenerator`

with frame-to-video encoding. Supports text-to-video (T2V) and image-to-video (I2V) workflows.

### Launch

Use `--wan-size 1b`

(default, 1 GPU) or `--wan-size 14b`

(2 GPUs). See the launch script for all configuration options.

### Test

## See Also

: Launch scripts for all deployment patterns[Examples](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/examples): Worker types and argument reference[Reference Guide](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/reference-guide): SGLang diffusion documentation[SGLang Diffusion LMs (upstream)](https://github.com/sgl-project/sglang/blob/main/docs/supported_models/text_generation/diffusion_language_models.md)