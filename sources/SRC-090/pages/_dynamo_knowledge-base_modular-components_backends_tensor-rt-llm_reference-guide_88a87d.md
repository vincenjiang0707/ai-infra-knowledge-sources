source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/reference-guide
lastmod: 2026-09-24T19:58:16.636Z

# Reference Guide

Features, configuration, and operational details for the TensorRT-LLM backend

## Argument Reference

The TensorRT-LLM backend accepts Dynamo-specific arguments (model loading, parallelism, batch limits, KV cache, disaggregation, and the experimental diffusion pipeline) plus the cross-cutting Dynamo runtime flags. For the complete field-by-field reference of every flag, default, and environment variable, see:

[TensorRT-LLM Configuration](https://docs.nvidia.com/dynamo/reference/backends/tensor-rt-llm-configuration)— the`DYN_TRTLLM_*`

backend flags.[Runtime Configuration](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration)— the`DYN_*`

flags shared by every backend.

## Default Thinking Mode

To set the thinking mode used when a request omits an explicit control, pass
`--dyn-default-thinking-mode enabled|disabled`

to the TensorRT-LLM worker or
set `DYN_DEFAULT_THINKING_MODE`

. Request-level thinking controls, including
adaptive thinking, take precedence. See
[Deployment-Level Thinking Default](https://docs.nvidia.com/dynamo/parsing/reasoning-parsing#deployment-level-thinking-default).

## Building a Custom Container

The Dynamo TensorRT-LLM image layers Dynamo on top of the upstream `nvcr.io/nvidia/tensorrt-llm/release`

container — it does not build TensorRT-LLM from source. To rebuild it locally, pin a different upstream TRT-LLM tag, or plug in a TRT-LLM image you built from source, see the [Building a Custom Container](https://docs.nvidia.com/dynamo/additional-resources/tensor-rt-llm-details/building-a-custom-container) guide.

## KV Cache Transfer

Dynamo with TensorRT-LLM supports three methods for transferring KV cache in disaggregated serving:

- NIXL with UCX (default)
- NIXL with Libfabric
- using UCX directly

For detailed information and configuration instructions for each method, see the [KV Cache Transfer Guide](https://docs.nvidia.com/dynamo/additional-resources/tensor-rt-llm-details/kv-cache-transfer).

## Request Migration

Dynamo supports [request migration](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration) to handle worker failures gracefully. When enabled, requests can be automatically migrated to healthy workers if a worker fails mid-generation. See the [Request Migration Architecture](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration) documentation for configuration details.

## Request Cancellation

When a user cancels a request (e.g., by disconnecting from the frontend), the request is automatically cancelled across all workers, freeing compute resources for other requests.

### Cancellation Support Matrix

For more details, see the [Request Cancellation Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-cancellation-architecture) documentation.

## Multiple Choices (`n`

)

Dynamo forwards OpenAI-compatible multiple-choice requests to TensorRT-LLM using `n`

. For an `n > 1`

request on TensorRT-LLM’s default deterministic decoding path, set `TLLM_ALLOW_N_GREEDY_DECODING=1`

in the TensorRT-LLM worker environment. Without it, TensorRT-LLM rejects the request before generation.

If a test or deployment intentionally validates `n > 1`

for that path, set:

Scope this environment variable to the specific TensorRT-LLM worker or test configuration that needs `n > 1`

. For Dynamo E2E tests, set it on the relevant `EngineConfig.env`

rather than globally, and keep the client request OpenAI-shaped with `n`

instead of adding `best_of`

.

TensorRT-LLM documents `n`

/`best_of`

behavior and validates this guard as greedy decoding in [ tensorrt_llm/sampling_params.py](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/sampling_params.py).

## Multimodal Support

Dynamo with the TensorRT-LLM backend supports multimodal models, enabling you to process both text and images (or pre-computed embeddings) in a single request. For detailed setup instructions, example requests, and best practices, see the [TensorRT-LLM Multimodal Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/tensorrt-llm-multimodal).

## Diffusion Support (Experimental)

Dynamo supports video and image generation using diffusion models through TensorRT-LLM. For requirements, supported models, API usage, and configuration options, see the [Text-to-Image](https://docs.nvidia.com/dynamo/diffusion/text-to-image#tensorrt-llm) and [Text-to-Video](https://docs.nvidia.com/dynamo/diffusion/text-to-video#tensorrt-llm) guides.

## Logits Processing

Logits processors let you modify the next-token logits at every decoding step. Dynamo provides a backend-agnostic interface and an adapter for TensorRT-LLM. For the API, examples, and how to bring your own processor, see the [Logits Processing Guide](https://docs.nvidia.com/dynamo/additional-resources/tensor-rt-llm-details/logits-processing).

## DP Rank Routing (Attention Data Parallelism)

TensorRT-LLM supports attention data parallelism for models like DeepSeek, enabling KV-cache-aware routing to specific DP ranks. For configuration and usage details, see the [DP Rank Routing Guide](https://docs.nvidia.com/dynamo/additional-resources/tensor-rt-llm-details/dp-rank-routing).

## KVBM Integration

Dynamo with TensorRT-LLM currently supports integration with the Dynamo KV Block Manager. This integration can significantly reduce time-to-first-token (TTFT) latency, particularly in usage patterns such as multi-turn conversations and repeated long-context requests.

See the instructions here: [Running KVBM in TensorRT-LLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/kvbm-guide#run-kvbm-in-dynamo-with-tensorrt-llm).

## Observability

TensorRT-LLM exposes Prometheus metrics for monitoring inference performance. For detailed metrics reference, collection setup, and Grafana integration, see the [Observability Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/observability).

## Disabling Python Cyclic GC for high concurrency benchmarks

Dynamo with TensorRT-LLM exposes `DYN_TRTLLM_SERVER_DISABLE_GC`

to match the behavior of `TRTLLM_SERVER_DISABLE_GC`

in `trtllm-serve`

. When set, the TensorRT-LLM worker disables Python’s cyclic garbage collector at startup so that generational GC pauses do not land on the request hot path. Reference-counted deallocation still runs normally — only the cycle collector is turned off.

This is most useful for high-concurrency benchmarks, where it boosts throughput and stabilizes TTFT/ITL measurements by removing GC-induced tail-latency spikes.

## Known Issues and Mitigations

For known issues, workarounds, and mitigations, see the [Known Issues and Mitigations](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/known-issues) page.