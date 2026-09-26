source: https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang
lastmod: 2026-09-24T19:58:16.636Z

# SGLang

SGLang engines run in Dynamo’s distributed runtime with disaggregated serving, KV-aware routing, and request cancellation.

## Use the Latest Release

We recommend using the [latest stable release](https://github.com/ai-dynamo/dynamo/releases/latest) of Dynamo to avoid breaking changes.

Dynamo SGLang integrates [SGLang](https://github.com/sgl-project/sglang) engines into Dynamo’s distributed runtime, enabling disaggregated serving, KV-aware routing, and request cancellation while maintaining full compatibility with SGLang’s native engine arguments. It supports LLM inference, embedding models, multimodal vision models, and diffusion-based generation (LLM, image, video).

## Prerequisites

-
**CUDA toolkit headers**for bare-metal builds (e.g.`nvcc`

,`cuda_runtime.h`

). See[CUDA Requirements](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/local-installation#system-requirements). Not required when running the pre-built`sglang-runtime`

container. -
for gated models. Export it on every node that pulls the model weights, and accept the model license on the Hugging Face model page before launch:`HF_TOKEN`


## Installation

### Install Latest Release

We recommend using [uv](https://github.com/astral-sh/uv) to install:

This installs the latest stable release of Dynamo with the compatible SGLang version.

### Install for Development

###### Development installation in a virtual environment (recommended)


Requires Rust and the CUDA toolkit (`nvcc`

).

[Maturin](https://github.com/PyO3/maturin) is the Rust-Python bindings build tool. The `patchelf`

extra lets maturin patch native extension library paths during the build.

This is the ideal way for agents to develop. You can provide the path to both repos and the virtual environment and have it rerun these commands as it makes changes

### Docker

Two paths are supported. Pick the one that matches how you plan to develop.

#### Pre-built Dynamo SGLang container (recommended)

Pull and launch the published `sglang-runtime`

image from NGC. See [release artifacts](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts) for the current tag and CUDA variants.

Mount the host Hugging Face cache (`-v $HOME/.cache/huggingface:/home/dynamo/.cache/huggingface`

) so each container restart doesn’t re-download model weights. The container runs as user `dynamo`

(UID 1000), which is why the in-container path is `/home/dynamo/.cache/huggingface`

.

#### Build from source inside upstream SGLang container

Pull and launch the upstream SGLang image, then build Dynamo from source inside it:

Install build dependencies and Rust inside the container:

Clone and build Dynamo:

## Feature Support Matrix

## Quick Start

### Python / CLI Deployment

Start infrastructure services for local development:

Launch an aggregated serving deployment:

Verify the deployment:

### Disaggregated Serving

Launch a disaggregated Qwen3-0.6B deployment (smallest model, useful for plumbing validation):


Performance caveat:Qwen3-0.6B is small enough that the disaggregated pathway is dominated by transport overhead and will often look slower than aggregated. Use it for plumbing validation, not benchmarks. Switch to Qwen3-32B-FP8 or larger for realistic disagg numbers.

### Multi-Node TP

SGLang supports multi-node tensor parallelism via the native `--dist-init-addr`

, `--nnodes`

, and `--node-rank`

flags. See [SGLang server arguments](https://docs.sglang.ai/advanced_features/server_arguments.html) for the canonical reference; the same flags work with `python -m dynamo.sglang`

. For a Kubernetes deployment example, see [ disagg-multinode.yaml](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/backends/sglang/deploy/disagg-multinode.yaml).

### Kubernetes Deployment

You can deploy SGLang with Dynamo on Kubernetes using a `DynamoGraphDeployment`

. For more details, see the [SGLang Kubernetes Deployment Guide](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/backends/sglang/deploy).

## Next Steps

: Worker types, architecture, and configuration[Reference Guide](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/reference-guide): All deployment patterns with launch scripts[Examples](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/examples): P/D architecture and KV transfer details[Disaggregation](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/disaggregation): LLM, image, and video diffusion models[Diffusion](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/diffusion): Metrics, tracing, and Grafana dashboards[Observability](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/observability): Kubernetes deployment guide[Deploying SGLang with Dynamo on Kubernetes](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/backends/sglang/deploy)