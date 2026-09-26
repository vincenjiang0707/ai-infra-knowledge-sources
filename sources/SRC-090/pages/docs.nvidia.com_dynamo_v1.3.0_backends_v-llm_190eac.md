source: https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm
lastmod: 2026-09-24T19:58:16.636Z

# vLLM

vLLM engines run in Dynamo’s distributed runtime with disaggregated serving, NIXL KV transfer, and KV-aware routing.

Dynamo vLLM integrates [vLLM](https://github.com/vllm-project/vllm) engines into Dynamo’s distributed runtime, enabling disaggregated serving, KV-aware routing, and request cancellation while maintaining full compatibility with vLLM’s native engine arguments. Dynamo leverages vLLM’s native KV cache events, NIXL-based transfer mechanisms, and metric reporting to enable KV-aware routing and P/D disaggregation.

## Installation

### Install Latest Release

We recommend using [uv](https://github.com/astral-sh/uv) to install:

This installs Dynamo with the compatible vLLM version.

### Container

We have public images available on [NGC Catalog](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo/artifacts):

###### Build from source


### Development Setup

For development, use the [devcontainer](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/.devcontainer) which has all dependencies pre-installed.

## Feature Support Matrix

## KV Routing Requirements

Starting the frontend with `--router-mode kv`

does not enable KV event
publishing on vLLM workers. For event-driven cache-aware routing, enable
publishing on every aggregated or prefill worker whose cache state the router
should track:

`endpoint`

is the base ZMQ port, and vLLM offsets it by data-parallel rank.
For worker processes that share a host or network namespace, reserve one port
per rank and choose base ports whose resulting ranges do not overlap. If
workers will not publish events, start the frontend with
`--no-router-kv-events`

for approximate cache prediction or `--load-aware`

for
load-only routing.

## Quick Start

Start infrastructure services for local development:

Launch an aggregated serving deployment:


Running launch scripts standalone.The`launch/*.sh`

scripts expect etcd and NATS to be reachable on localhost. Bring them up first (run from the repo root, or use the absolute path shown):Then run the launch script. Without these, workers register but the frontend cannot discover them and requests hang.


### Rust Backend Preview

The Python vLLM backend remains the recommended entry point for production
deployments and examples. The Rust backend is a development preview for
validating the Rust `LLMEngine`

integration with vLLM’s engine-core client.
Use it when working on the Rust backend contract, cancellation, metrics,
or P/D wiring; use `python -m dynamo.vllm`

or
`python -m dynamo.vllm.unified_main`

for the most complete vLLM feature
coverage.

The Rust backend depends on vLLM’s engine-core crates, which are not yet
published to crates.io and are pulled as git dependencies. They are gated
behind the off-by-default `vllm_rs`

cargo feature, so the default workspace
build does not require the git sources and the crate is excluded from the
published Dynamo crates. You must pass `--features vllm_rs`

to build or run it.

To run the Rust backend locally, start the same infrastructure services and frontend, then launch the Rust worker in another terminal:

The Rust worker starts a managed vLLM engine-core process and registers with the Dynamo frontend using the same discovery path as the Python unified backend. The Rust backend is expected to become the default only after it reaches feature and operational parity with the Python vLLM backend.

## Next Steps

: Configuration, arguments, and operational details[Reference Guide](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/reference-guide): All deployment patterns with launch scripts[Examples](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/examples): KVBM, LMCache, and FlexKV integrations[KV Cache Offloading](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/kv-cache-offloading): Metrics and monitoring[Observability](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/observability): Multimodal model serving[vLLM-Omni](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/v-llm-omni): Kubernetes deployment guide[Kubernetes Deployment](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples/backends/vllm/deploy/README.md): Upstream vLLM serve arguments[vLLM Documentation](https://docs.vllm.ai/en/stable/)