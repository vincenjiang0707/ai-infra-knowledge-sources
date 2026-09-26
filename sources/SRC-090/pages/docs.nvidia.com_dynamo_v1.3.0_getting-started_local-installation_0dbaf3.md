source: https://docs.nvidia.com/dynamo/v1.3.0/getting-started/local-installation
lastmod: 2026-09-24T19:58:16.636Z

# Local Installation

This guide walks through installing and running Dynamo on a local machine or VM with one or more GPUs. By the end, you’ll have a working OpenAI-compatible endpoint serving a model.

For production multi-node clusters, see the [Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/kubernetes-quickstart). To build from source for development, see [Building from Source](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/building-from-source).

## System Requirements

###### CUDA

###### XPU

TensorRT-LLM does not support Python 3.11.

For the full compatibility matrix including backend framework versions, see the [Support Matrix](https://docs.nvidia.com/dynamo/v1.3.0/resources/support-matrix).

## Install Dynamo

### Option A: Containers (Recommended)

###### CUDA

###### XPU

Containers have all dependencies pre-installed. No setup required.

To run frontend and worker in the same container, either:

- Run processes in background with
`&`

(see Run Dynamo section below), or - Open a second terminal and use
`docker exec -it <container_id> bash`


See [Release Artifacts](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#container-images) for available
versions and backend guides for run instructions: [SGLang](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang) |
[TensorRT-LLM](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm) | [vLLM](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm)

### Option B: Install from PyPI

###### CUDA

###### XPU

Supported for vLLM and SGLang only. Use Option A for TensorRT-LLM.

Install system dependencies and the Dynamo wheel for your chosen backend:

**SGLang**

**vLLM**

## Run Dynamo

### Discovery Backend

Dynamo components discover each other through a shared backend. Two options are available:

This guide uses `--discovery-backend file`

. For etcd setup, see [Service Discovery](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/advanced-platform/service-discovery).

### Verify Installation (Optional)

Verify the CLI is installed and callable:

If you cloned the repository, you can run additional system checks:

### Start the Frontend

To run in a single terminal (useful in containers), append `> logfile.log 2>&1 &`

to run processes in background:

### Start a Worker

In another terminal (or same terminal if using background mode), start a worker for your chosen accelerator and backend:

###### CUDA

###### XPU

**SGLang**

**TensorRT-LLM**

The warning `Cannot connect to ModelExpress server/transport error. Using direct download.`

is expected in this local single-machine setup (no ModelExpress server running) and can
be safely ignored. In a Kubernetes deployment where `MODEL_EXPRESS_URL`

is configured,
this warning — or the related `Failed to resolve local model path after server download`

— indicates that ModelExpress is configured but is not actually serving cached models;
see [Model Caching in Kubernetes](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/model-loading/model-caching#option-2-modelexpress-p2p-distribution)
for the correct configuration.

**vLLM**

## Test Your Deployment

## Troubleshooting

###### CUDA

###### XPU

**CUDA/driver version mismatch**

Run `nvidia-smi`

to check your driver version. Dynamo requires driver 575.51.03+ for CUDA 12 or 580.00.03+ for CUDA 13. B300/GB300 GPUs require CUDA 13. See the [Support Matrix](https://docs.nvidia.com/dynamo/v1.3.0/resources/support-matrix) for full requirements.

**Model doesn’t fit on GPU (OOM)**

The default model `Qwen/Qwen3-0.6B`

requires ~2GB of GPU memory. Larger models need more VRAM:

Start with a small model and scale up based on your hardware.

**TensorRT-LLM**

TensorRT-LLM is not supported via a local PyPI install. Use the
`tensorrtllm-runtime`

container (Option A).

**Container runs but GPU not detected**

Pass `--gpus all`

to `docker run`

. Without this flag, the container won’t have access to NVIDIA GPUs:

**vLLM worker fails to start: FlashInfer sampler JIT and CUDA 13 wheels**

When you run a vLLM worker from a CUDA 13 install, the worker can abort during startup with a FlashInfer JIT error:

The CUDA wheels resolved for a CUDA 13 install can be version-skewed: `torch`

pins the runtime headers to 13.0, while vLLM’s `tilelang`

dependency pulls `nvidia-cuda-nvcc`

13.2. FlashInfer compiles its sampler kernel with `nvcc`

against those headers, and the version mismatch fails the build. This is tracked upstream at [flashinfer#3493](https://github.com/flashinfer-ai/flashinfer/issues/3493).

Set `VLLM_USE_FLASHINFER_SAMPLER=0`

so vLLM falls back to its native sampler:

## Next Steps

[Backend Guides](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang)— Backend-specific configuration and features[Disaggregated Serving](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/disaggregated-serving)— Scale prefill and decode independently[KV Cache Aware Routing](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/kv-cache-aware-routing)— Smart request routing[Kubernetes Deployment](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/kubernetes-quickstart)— Production multi-node deployments