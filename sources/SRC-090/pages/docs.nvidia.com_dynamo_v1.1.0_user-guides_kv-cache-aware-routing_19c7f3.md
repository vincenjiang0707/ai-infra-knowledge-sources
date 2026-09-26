source: https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-aware-routing
lastmod: 2026-09-24T19:58:16.636Z

# Router Guide

## Overview

The Dynamo KV Router intelligently routes requests by evaluating their computational costs across different workers. It considers both decoding costs (from active blocks) and prefill costs (from newly computed blocks), using KV cache overlap to minimize redundant computation. Optimizing the KV Router is critical for achieving maximum throughput and minimum latency in distributed inference setups. This guide helps you get started with using the Dynamo router and points to the pages that cover routing concepts, configuration, disaggregated serving, and operations in more detail.

## Quick Start

The router can be deployed using [Python / CLI](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-aware-routing#python--cli-deployment), [Kubernetes](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-aware-routing#kubernetes-deployment), or as a [standalone component](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/kv-cache-aware-routing#standalone-router).

### Python / CLI Deployment

To launch the Dynamo frontend with the KV Router:

This command:

- Launches the Dynamo frontend service with KV routing enabled
- Exposes the service on port 8000 (configurable)
- Automatically handles all backend workers registered to the Dynamo endpoint

Backend workers register themselves using the `register_model`

API, after which the KV Router automatically tracks worker state and makes routing decisions based on KV cache overlap.

#### CLI Arguments

For all available options: `python -m dynamo.frontend --help`


For detailed configuration options and tuning parameters, see [Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.1.0/components/router/configuration-and-tuning).

#### AIC Prefill Load Model

The KV router can use AIC to estimate the expected duration of the selected worker’s prompt-side prefill work. When enabled, the router:

- computes
`prefix = overlap_blocks * block_size`

for the chosen worker - computes
`effective_isl = input_tokens - prefix`

- stores one prompt-load hint for the admitted request
- decays only the
**oldest**active prefill request on each worker over time

This affects router-side prompt load accounting only. It does not change backend execution or decode-side accounting.

Enable it on the frontend like this:

The standalone router uses the same AIC flags:

Required when `--router-prefill-load-model=aic`

is enabled:

`--router-mode kv`

on the frontend`--router-track-prefill-tokens`

`--aic-backend`

`--aic-system`

`--aic-model-path`


Optional AIC knobs:

`--aic-backend-version`

: pinned AIC database version; if omitted, Dynamo uses a backend-specific default`--aic-tp-size`

: tensor-parallel size for the modeled backend; defaults to`1`


### Kubernetes Deployment

To enable the KV Router in Kubernetes, add the `DYN_ROUTER_MODE`

environment variable to your frontend service:

**Key Points:**

- Set
`DYN_ROUTER_MODE=kv`

on the**Frontend**service only - Workers automatically report KV cache events to the router
- No worker-side configuration changes needed

#### Environment Variables

All CLI arguments can be configured via environment variables using the `DYN_`

prefix:

For complete K8s examples and advanced configuration, see [K8s Examples](https://docs.nvidia.com/dynamo/v1.1.0/components/router/router-examples#k8s-examples) and [Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.1.0/components/router/configuration-and-tuning).
For A/B testing and advanced K8s setup, see the [KV Router A/B Benchmarking Guide](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/kv-router-a-b-testing).

### Standalone Router

You can also run the KV router as a standalone service (without the Dynamo frontend) for disaggregated serving (e.g., routing to prefill workers), multi-tier architectures, or any scenario requiring intelligent KV cache-aware routing decisions. See the [Standalone Router component](https://github.com/ai-dynamo/dynamo/tree/v1.1.0/components/src/dynamo/router/) for more details.

#### Frontend-Embedded vs. Standalone Router

The standalone router does not include the HTTP frontend (no `/v1/chat/completions`

endpoint). It exposes only the `RouterRequestMetrics`

via the system status server. See the [Standalone Router README](https://github.com/ai-dynamo/dynamo/blob/v1.1.0/components/src/dynamo/router/README.md).

## Deployment Modes

The Dynamo router can be deployed in several configurations. The table below shows every combination and when to use it:

### Routing Modes (`--router-mode`

)

### Device-Aware Weighted Routing

`device-aware-weighted`

is designed for heterogeneous fleets where workers of different compute capability, for example CPU embedding encoders alongside GPU embedding encoders, share the same endpoint.

Workers are split into CPU and non-CPU groups. The router compares a capability-normalized load across the two groups:

The throughput weight is `1`

for CPU workers and `DYN_ENCODER_CUDA_TO_CPU_RATIO`

for non-CPU workers. The next request is routed to the group with the lower normalized load, then to the least-loaded worker inside that group.

Use `DYN_ENCODER_CUDA_TO_CPU_RATIO`

to approximate the throughput ratio of a non-CPU worker relative to one CPU worker. The default is `8`

.

When only one device class is present, the policy degenerates to standard least-loaded routing.

### KV Event Transport Modes (within `--router-mode kv`

)

When using KV routing, the router needs to know what each worker has cached. There are four ways to get this information:

### Aggregated vs. Disaggregated Topology

Disaggregated mode is activated automatically when prefill workers register alongside decode workers. See [Disaggregated Serving](https://docs.nvidia.com/dynamo/v1.1.0/components/router/disaggregated-serving) for details.

## More Router Docs

: Cost model, worker selection, and routing primitives[Routing Concepts](https://docs.nvidia.com/dynamo/v1.1.0/components/router/routing-concepts): Router flags, transport modes, load tracking, and metrics[Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.1.0/components/router/configuration-and-tuning): Prefill and decode routing setups[Disaggregated Serving](https://docs.nvidia.com/dynamo/v1.1.0/components/router/disaggregated-serving): Replicas, remote indexers, persistence, and recovery[Router Operations](https://docs.nvidia.com/dynamo/v1.1.0/components/router/router-operations): Python API usage, K8s examples, and custom routing patterns[Router Examples](https://docs.nvidia.com/dynamo/v1.1.0/components/router/router-examples): Recommended test layers for non-trivial router changes[Router Testing](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/router-testing.md): Run the KV indexer as a separate service[Standalone Indexer](https://docs.nvidia.com/dynamo/v1.1.0/components/router/standalone-indexer): Gap detection and replay behavior[KV Event Replay — Dynamo vs vLLM](https://docs.nvidia.com/dynamo/v1.1.0/components/router/kv-event-replay-dynamo-vs-v-llm)