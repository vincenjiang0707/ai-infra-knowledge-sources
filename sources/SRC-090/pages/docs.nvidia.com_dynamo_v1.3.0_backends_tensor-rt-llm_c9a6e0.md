source: https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm
lastmod: 2026-09-24T19:58:16.636Z

TensorRT-LLM


TensorRT-LLM

TensorRT-LLM engines run in Dynamo’s distributed runtime with disaggregated serving, KV-aware routing, and multinode support.

## Use the Latest Release

We recommend using the [latest stable release](https://github.com/ai-dynamo/dynamo/releases/latest) of Dynamo to avoid breaking changes.

Dynamo TensorRT-LLM integrates [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) engines into Dynamo’s distributed runtime, enabling disaggregated serving, KV-aware routing, multi-node deployments, and request cancellation. It supports LLM inference, multimodal models, video diffusion, and advanced features like speculative decoding and attention data parallelism.

## Feature Support Matrix

### Core Dynamo Features

### Large Scale P/D and WideEP Features

## Prerequisites

for in-place YAML edits. Install with`yq`

`wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/local/bin/yq && chmod +x /usr/local/bin/yq`

or`pip install yq`

(the latter is a different tool with the same name but similar syntax). If neither is available, a`sed`

fallback is shown inline where`yq`

is used.

## Container / driver matrix

Source of truth: [ docs/reference/support-matrix.md](https://docs.nvidia.com/dynamo/v1.3.0/resources/support-matrix#cuda-and-driver-requirements) and

[. If those differ from the values above, the source-of-truth files win.](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts)

`docs/reference/release-artifacts.md`

## Quick Start

**Step 1 (host terminal):** Start infrastructure services:

**Step 2 (host terminal):** Pull and run the prebuilt container:

The `DYNAMO_VERSION`

variable above can be set to any specific available version of the container.
To find the available `tensorrtllm-runtime`

versions for Dynamo, visit the [NVIDIA NGC Catalog for Dynamo TensorRT-LLM Runtime](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/tensorrtllm-runtime).

**Step 3 (inside the container):** Launch an aggregated serving deployment (uses `Qwen/Qwen3-0.6B`

by default):

The launch script will automatically download the model and start the TensorRT-LLM engine. You can override the model by setting `MODEL_PATH`

and `SERVED_MODEL_NAME`

environment variables before running the script.

**Step 4 (host terminal):** Verify the deployment:

## Deploy

Deploy TensorRT-LLM with Dynamo on Kubernetes using a `DynamoGraphDeployment`

. Before `kubectl apply`

, substitute the container image tag in the deployment YAML. The `sed`

fallback is shown inline for environments without `yq`

:

For full Kubernetes deployment instructions, see the [TensorRT-LLM Kubernetes Deployment Guide](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/backends/trtllm/deploy/README.md).

## Next Steps

: Features, configuration, and operational details[Reference Guide](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm/reference-guide): All deployment patterns with launch scripts[Examples](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm/examples): KV cache transfer methods for disaggregated serving[KV Cache Transfer](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/tensor-rt-llm-details/kv-cache-transfer): Metrics and monitoring[Observability](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm/observability): Multi-node deployment with SLURM[Multinode Examples](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/tensor-rt-llm-details/multinode-examples): Kubernetes deployment guide[Deploying TensorRT-LLM with Dynamo on Kubernetes](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/backends/trtllm/deploy/README.md)