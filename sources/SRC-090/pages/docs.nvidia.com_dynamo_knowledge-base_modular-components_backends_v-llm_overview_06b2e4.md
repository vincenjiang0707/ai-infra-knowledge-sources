source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/overview
lastmod: 2026-09-24T19:58:16.636Z

# vLLM

Dynamo vLLM integrates [vLLM](https://github.com/vllm-project/vllm) engines into Dynamo’s distributed runtime, enabling disaggregated serving, KV-aware routing, and request cancellation while maintaining full compatibility with vLLM’s native engine arguments. Dynamo leverages vLLM’s native KV cache events, NIXL-based transfer mechanisms, and metric reporting to enable KV-aware routing and P/D disaggregation.

## Experimental Sidecar

The experimental sidecar path runs the Dynamo worker outside vLLM and connects
through vLLM’s native gRPC API. It keeps vLLM’s native server and argument
surface while separating Dynamo and engine dependencies. See
[vLLM Sidecar](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/sidecar) for current readiness and launch examples.

## Installation

### Install Latest Release

We recommend using [uv](https://github.com/astral-sh/uv) to install:

This installs Dynamo with the compatible vLLM version.

### Container

We have public images available on [NGC Catalog](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo/artifacts):

###### Build from source


### Development Setup

For development, use the [devcontainer](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/.devcontainer) which has all dependencies pre-installed.

## Feature Support Matrix

## Feature Interactions

vLLM offers the broadest feature coverage in Dynamo, with full support for disaggregated serving, KV-aware routing, KV block management, LoRA adapters, and multimodal inference including video and audio. The matrix below shows which feature pairs are validated to work together.

**Legend:** ✅ Supported | 🚧 Work in Progress / Experimental / Limited


Notes:

Multimodal + KV-Aware Routing: Image-aware KV routing is supported in the documented vLLM paths. The default Rust frontend path supports model families handled by`llm-multimodal`

; the Python chat-processor path delegates to vLLM’s multimodal processor. ([Source])KV-Aware LoRA Routing: vLLM supports routing requests based on LoRA adapter affinity.Audio Support: vLLM supports audio models like Qwen2-Audio (experimental). ([Source])Video Support: vLLM supports video input with frame sampling. ([Source])Speculative Decoding: Eagle3 support documented. ([Source])

## Quick Start

Start infrastructure services for local development:

Launch an aggregated serving deployment:


Running launch scripts standalone.The`launch/*.sh`

scripts expect etcd and NATS to be reachable on localhost. Bring them up first (run from the repo root, or use the absolute path shown):Then run the launch script. Without these, workers register but the frontend cannot discover them and requests hang.


## Next Steps

: Configuration, arguments, and operational details[Reference Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/reference-guide): Local deployment launch scripts[Examples](https://docs.nvidia.com/dynamo/recipes/cli-templates/v-llm): KVBM, LMCache, and FlexKV integrations[KV Cache Offloading](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/kv-cache-offloading): Metrics and monitoring[Observability](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/observability): Multimodal model serving[vLLM-Omni](https://docs.nvidia.com/dynamo/diffusion/overview): Kubernetes deployment guide[Kubernetes Deployment](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/examples/backends/vllm/deploy/README.md): Upstream vLLM serve arguments[vLLM Documentation](https://docs.vllm.ai/en/stable/)