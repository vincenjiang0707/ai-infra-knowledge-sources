source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/diffusion/fastvideo
lastmod: 2026-09-23T23:30:39.914Z

# FastVideo

Deploys FastVideo text-to-video generation on Dynamo through a custom worker that serves the /v1/videos endpoint.

This guide covers deploying [FastVideo](https://github.com/hao-ai-lab/FastVideo) text-to-video generation on Dynamo using a custom worker (`worker.py`

) exposed through the `/v1/videos`

endpoint.

Dynamo also supports diffusion through built-in backends: [SGLang Diffusion](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/diffusion) (LLM diffusion, image, video), [vLLM-Omni](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/v-llm-omni) (text-to-image, text-to-video), and [TRT-LLM Diffusion](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm/diffusion-experimental) (text-to-image, text-to-video). See the [Diffusion Overview](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/diffusion) for the full support matrix.

## Overview

**Default model:**`FastVideo/LTX2-Distilled-Diffusers`

— a distilled variant of the LTX-2 Diffusion Transformer (Lightricks), reducing inference from 50+ steps to just 5.**Two-stage pipeline:**Stage 1 generates video at target resolution; Stage 2 refines with a distilled LoRA for improved fidelity and texture.**Optimized inference:**FP4 quantization and`torch.compile`

are available via`--enable-optimizations`

; attention backend selection is controlled separately via`--attention-backend`

.**Response format:**Returns one complete MP4 payload per request as`data[0].b64_json`

(non-streaming).**Concurrency:**One request at a time per worker (VideoGenerator is not re-entrant). Scale throughput by running multiple workers.

`worker.py`

defaults to `--attention-backend TORCH_SDPA`

for broader compatibility across GPUs, including systems such as H100. For the B200/B300-oriented path, enable FP4/compile with `--enable-optimizations`

and, if desired, opt into flash-attention explicitly with `--attention-backend FLASH_ATTN`

.

## Docker Image Build

The local Docker workflow builds a runtime image from the [ Dockerfile](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/diffusers/Dockerfile):

- Base image:
`nvidia/cuda:13.1.1-devel-ubuntu24.04`

- Installs
[FastVideo](https://github.com/hao-ai-lab/FastVideo)from GitHub - Installs Dynamo from the
`release/1.0.0`

branch (for`/v1/videos`

support) - Compiles a
[flash-attention](https://github.com/RandNMR73/flash-attention)fork from source

The Dockerfile exposes `TORCH_CUDA_ARCH_LIST`

as a build argument (default: `10.0 10.0a`

for Blackwell). Pass `--build-arg`

to target a different architecture:

`MAX_JOBS`

(default: `4`

) controls parallel compilation jobs for flash-attention. Lower it if the build runs out of memory:

When using Docker Compose, set these as environment variables before running `docker compose up --build`

:

The first Docker image build can take **20–40+ minutes** because FastVideo and CUDA-dependent components are compiled during the build. Subsequent builds are much faster if Docker layer cache is preserved. Compiling `flash-attention`

can use significant RAM — low-memory builders may hit out-of-memory failures. If that happens, lower `MAX_JOBS`

in the Dockerfile to reduce parallel compile memory usage. The [flash-attn install notes](https://pypi.org/project/flash-attn/) specifically recommend this on machines with less than 96 GB RAM and many CPU cores.

## Warmup Time

On first start, workers download model weights. When `--enable-optimizations`

is enabled, compile/warmup steps can push the first ready time to roughly **10–20 minutes** (hardware-dependent). After the first successful optimized response, the second request can still take around **35 seconds** while runtime caches finish warming up; steady-state performance is typically reached from the third request onward.

When using Kubernetes, mount a shared Hugging Face cache PVC (see [Kubernetes Deployment](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/diffusion/fastvideo#kubernetes-deployment)) so model weights are downloaded once and reused across pod restarts.

## Local Deployment

### Prerequisites

**For Docker Compose:**

- Docker Engine 26.0+
- Docker Compose v2
- NVIDIA Container Toolkit

**For host-local script:**

- Python environment with Dynamo + FastVideo dependencies installed
- CUDA-compatible GPU runtime available on host

### Option 1: Docker Compose

The Compose file builds from the Dockerfile and exposes the API on `http://localhost:8000`

. See the [Docker Image Build](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/diffusion/fastvideo#docker-image-build) section for build time expectations.

### Option 2: Host-Local Script

Environment variables:

Example:

`--enable-optimizations`

and `--attention-backend`

are `worker.py`

flags, not `dynamo.frontend`

flags, so pass them through `WORKER_EXTRA_ARGS`

when you want a non-default worker configuration.

The script writes logs to:

`.runtime/logs/worker.log`

`.runtime/logs/frontend.log`


## Kubernetes Deployment

### Files

### Prerequisites

- Dynamo Kubernetes Platform installed
- GPU-enabled Kubernetes cluster
- FastVideo runtime image pushed to your registry
- Optional HF token secret (for gated models)

Create a Hugging Face token secret if needed:

### Deploy

For clusters with tainted `user-workload`

nodes and private registry pulls:

- Set your pull secret name and image in
`agg_user_workload.yaml`

. - Apply:

### Update Image Quickly

### Verify and Access

## Test Request

If this is the first request after startup, expect it to take longer while warmup completes. See [Warmup Time](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/diffusion/fastvideo#warmup-time) for details.

Send a request and decode the response:

## Worker Configuration Reference

### CLI Flags

### Request Parameters (`nvext`

)

### Environment Variables

## Troubleshooting

## Source Code

The example source lives at [ examples/diffusers/](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/diffusers) in the Dynamo repository.

## See Also

[vLLM-Omni Text-to-Video](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/v-llm-omni#text-to-video)— vLLM-Omni video generation via`/v1/videos`

[vLLM-Omni Text-to-Image](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/v-llm-omni#text-to-image)— vLLM-Omni image generation[SGLang Video Generation](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/diffusion#video-generation)— SGLang video generation worker[SGLang Image Diffusion](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/diffusion#image-diffusion)— SGLang image diffusion worker[TRT-LLM Diffusion](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm/diffusion-experimental#quick-start)— TensorRT-LLM diffusion quick start[Diffusion Overview](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/diffusion)— Full backend support matrix