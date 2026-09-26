source: https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm
lastmod: 2026-09-24T19:58:16.636Z

# vLLM

Dynamo vLLM integrates [vLLM](https://github.com/vllm-project/vllm) engines into Dynamo’s distributed runtime, enabling disaggregated serving, KV-aware routing, and request cancellation while maintaining full compatibility with vLLM’s native engine arguments. Dynamo leverages vLLM’s native KV cache events, NIXL-based transfer mechanisms, and metric reporting to enable KV-aware routing and P/D disaggregation.

## Installation

### Install Latest Release

We recommend using [uv](https://github.com/astral-sh/uv) to install:

This installs Dynamo with the compatible vLLM version.

### Container

We have public images available on [NGC Catalog](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo/artifacts):

###### Build from source


### Development Setup

For development, use the [devcontainer](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/.devcontainer) which has all dependencies pre-installed.

## Feature Support Matrix

## Quick Start

Start infrastructure services for local development:

Launch an aggregated serving deployment:


Running launch scripts standalone.The`launch/*.sh`

scripts expect etcd and NATS to be reachable on localhost. Bring them up first (run from the repo root, or use the absolute path shown):Then run the launch script. Without these, workers register but the frontend cannot discover them and requests hang.


## Next Steps

: Configuration, arguments, and operational details[Reference Guide](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/reference-guide): All deployment patterns with launch scripts[Examples](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/examples): KVBM, LMCache, and FlexKV integrations[KV Cache Offloading](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/kv-cache-offloading): Metrics and monitoring[Observability](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/observability): Multimodal model serving[vLLM-Omni](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/v-llm-omni): Kubernetes deployment guide[Kubernetes Deployment](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/examples/backends/vllm/deploy/README.md): Upstream vLLM serve arguments[vLLM Documentation](https://docs.vllm.ai/en/stable/)