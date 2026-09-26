source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/backends/sg-lang/reference-guide
lastmod: 2026-09-23T23:30:39.914Z

# Reference Guide

## Overview

The SGLang backend in Dynamo uses a modular architecture where `main.py`

dispatches to specialized initialization modules based on the worker type. Each worker type has its own init module, request handler, health check, and registration logic.

Dynamo SGLang uses SGLang’s native argument parser — all SGLang engine arguments (e.g., `--model-path`

, `--tp`

, `--trust-remote-code`

) are passed through directly. Dynamo adds its own arguments for worker mode selection, tokenizer control, and disaggregation configuration.

### Worker Types

## Argument Reference

### Dynamo-Specific Arguments

These arguments are added by Dynamo on top of SGLang’s native arguments.

`--disagg-config`

and `--disagg-config-key`

must be provided together. The selected section is written to a temp YAML file and passed to SGLang’s `--config`

flag.

Keep `--dedicated-mm-encoder`

separate from `--enable-multimodal`

. `--enable-multimodal --disaggregation-mode prefill/decode`

is also the native P/D multimodal shape where normal prefill/decode handlers both pass raw media metadata to SGLang: prefill builds the vision context, and decode reprocesses the same metadata to match token layout with the transferred KV cache. `--dedicated-mm-encoder`

is what changes those workers into internal E/P/D components that expect precomputed embeddings from an encode worker and do not provide the public OpenAI surface.

Unlike vLLM, SGLang E/P/D needs `--dedicated-mm-encoder`

on both decode and prefill workers. The encode worker delegates generation to `backend.generate`

, which is the decode worker, and that internal decode worker forwards the precomputed multimodal payload to prefill. Keeping this flag in the encode-worker topology also prevents falling back to native P/D’s duplicate raw-media preprocessing.

The current supported parser names for both flags are documented in [Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/tool-call-parsing-dynamo#supported-tool-call-parsers) and [Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/reasoning-parsing-dynamo#supported-reasoning-parsers).

For reasoning models with required or named tool choice, configure both reasoning parsers on the worker:

The SGLang parser delays grammar enforcement until reasoning ends; the Dynamo
parser populates `reasoning_content`

. Parser names can differ between registries.

## Tokenizer Behavior

By default, Dynamo handles tokenization and detokenization through its Rust-based frontend, passing `input_ids`

to SGLang. This enables all frontend endpoints (`v1/chat/completions`

, `v1/completions`

, `v1/embeddings`

).

For SGLang-native preprocessing (tool calling, reasoning parsing, chat templates), use `--dyn-chat-processor sglang`

on the frontend. See [SGLang Chat Processor](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/frontend-processor-fallback) for architecture and usage.

`--use-sglang-tokenizer`

is deprecated. Use `--dyn-chat-processor sglang`

on the frontend instead, which provides the same SGLang-native processing with KV router support and the completions endpoint.

## Request Cancellation

When a client disconnects, Dynamo automatically cancels the in-flight request across all workers, freeing compute resources. A background cancellation monitor detects disconnection and aborts the SGLang request.

For details on the cancellation architecture, see [Request Cancellation](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-cancellation).

## Graceful Shutdown

SGLang workers use Dynamo’s graceful shutdown mechanism. When a `SIGTERM`

or `SIGINT`

is received:

**Discovery unregister**: The worker is removed from service discovery so no new requests are routed to it**Grace period**: In-flight requests are allowed to complete**Deferred handlers**: SGLang’s internal signal handlers (captured during startup via monkey-patching`loop.add_signal_handler`

) are invoked after the graceful period

This ensures zero dropped requests during rolling updates or scale-down events.

For more details, see [Graceful Shutdown](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/graceful-shutdown).

## Health Checks

Each worker type has a specialized health check payload that validates the full inference pipeline:

Health checks are registered with the Dynamo runtime and called by the frontend or Kubernetes liveness probes. See [Health Checks](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/health-checks) for the broader health check architecture.

## Metrics and KV Events

### Prometheus Metrics

Enable metrics with `--enable-metrics`

on the worker. Set `DYN_SYSTEM_PORT`

to expose the `/metrics`

endpoint:

Both SGLang engine metrics (`sglang:*`

prefix) and Dynamo runtime metrics (`dynamo_*`

prefix) are served from the same endpoint.

For metric details, see [SGLang Observability](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/observability). For visualization setup, see [Prometheus + Grafana](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/prometheus-grafana-setup).

### KV Events

When configured with `--kv-events-config`

, workers publish KV cache events (block creation/deletion) for the [KV-aware router](https://docs.nvidia.com/dynamo/v1.3.0/components/router). Events are published via ZMQ from SGLang’s scheduler and relayed through Dynamo’s event plane.

For DP attention mode (`--enable-dp-attention`

), the publisher handles multiple DP ranks per node, each with its own KV event stream.

## Engine Routes

SGLang workers expose operational endpoints via Dynamo’s system server:

## See Also

: All deployment patterns[Examples](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/examples): P/D architecture and KV transfer[Disaggregation](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/disaggregation): LLM, image, and video diffusion models[Diffusion](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/diffusion): KV-aware routing configuration[Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning)