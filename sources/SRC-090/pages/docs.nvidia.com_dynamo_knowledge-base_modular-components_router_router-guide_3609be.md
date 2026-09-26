source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide
lastmod: 2026-09-24T19:58:16.636Z

# Router Guide

## Overview

The Dynamo KV Router intelligently routes requests by evaluating their computational costs across different workers. It considers both decoding costs (from active blocks) and prefill costs (from newly computed blocks), using KV cache overlap to minimize redundant computation. Optimizing the KV Router is critical for achieving maximum throughput and minimum latency in distributed inference setups. This guide helps you get started with using the Dynamo router and points to the pages that cover routing concepts, configuration, disaggregated serving, and operations in more detail.

## Quick Start

The router can be deployed using [Python / CLI](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide#python--cli-deployment), [Kubernetes](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide#kubernetes-deployment), or as a [standalone component](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide#standalone-router).

### Python / CLI Deployment

To launch the Dynamo frontend with the KV Router:

This command:

- Launches the Dynamo frontend service with KV routing enabled
- Exposes the service on port 8000 (configurable)
- Automatically handles all backend workers registered to the Dynamo endpoint

Backend workers register themselves using the `register_model`

API. For accurate prefix-cache state, workers must also publish KV cache events with the backend-specific event flags; otherwise the router can run in approximate mode with `--no-router-kv-events`

.

The [Frontend Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#router) is the
canonical list of embedded-router CLI arguments, environment variables, defaults,
and boolean forms. Use [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning) for
workload-specific guidance, [Router Filtering](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-filtering) for candidate
eligibility, and [Routing Concepts](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/routing-concepts#active-load-modeling) for the
prefill and decode cost model.

### Kubernetes Deployment

To enable the KV Router in Kubernetes, add the `DYN_ROUTER_MODE`

environment variable to your frontend service:

**Key Points:**

- Set
`DYN_ROUTER_MODE=kv`

on the**Frontend**service only - Configure worker-side KV event publishing when you want event-driven prefix-cache state
- Use
`--no-router-kv-events`

for approximate cache-state prediction when workers are not publishing events

For exact environment-variable mappings, see the
[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#router). For complete
Kubernetes examples and tuning guidance, see
[Kubernetes Examples](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-examples#k8s-examples) and
[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning).
For A/B testing and advanced K8s setup, see the [KV Router A/B Benchmarking Guide](https://docs.nvidia.com/dynamo/recipes/benchmarks/kv-router-ab-testing).

### Standalone Router

You can also run the KV router as a standalone service without the Dynamo frontend for disaggregated serving, multi-tier architectures, or custom routing pipelines. See [Standalone Router](https://docs.nvidia.com/dynamo/cli/kv-aware-routing/standalone-router) for the Fern guide.

#### Frontend-Embedded vs. Standalone Router

The standalone router does not include the HTTP frontend and does not expose `/v1/chat/completions`

. It exposes routing endpoints through the Dynamo runtime and, when configured, router metrics through the system status server.

## Deployment Modes

The Dynamo router can be deployed in several configurations. The table below shows common combinations and when to use them:

With `DYN_LORA_ENABLED`

, use KV, random, or round-robin routing. Direct,
power-of-two, least-loaded, and device-aware-weighted modes are not LoRA-aware
and fail startup. Session affinity with LoRA is supported only in KV mode;
random and round-robin plus affinity are rejected.

### Routing Modes (`--router-mode`

)

### Device-Aware Weighted Routing

`device-aware-weighted`

is designed for heterogeneous fleets where workers of different compute capability, for example CPU embedding encoders alongside GPU embedding encoders, share the same endpoint.

Workers are split into CPU and non-CPU groups. The router compares a capability-normalized load across the two groups:

The throughput weight is `1`

for CPU workers and `DYN_ENCODER_CUDA_TO_CPU_RATIO`

for non-CPU workers. The next request is routed to the group with the lower normalized load, then to the least-loaded worker inside that group.

For multimodal requests, a full embedding-cache hit on one or more workers bypasses the CPU-to-non-CPU ratio. The router selects the least-loaded worker among those that hold every distinct embedding-cache key in the request. Partial hits continue through the normal weighted group selection. See [Embedding Cache](https://docs.nvidia.com/dynamo/multimodal/embedding-cache#configuration).

Use `DYN_ENCODER_CUDA_TO_CPU_RATIO`

to approximate the throughput ratio of a non-CPU worker relative to one CPU worker. The default is `8`

.

When only one device class is present, the policy degenerates to standard least-loaded routing.

### KV Event Transport Modes (within `--router-mode kv`

)

When using KV routing, the router needs to know what each worker has cached. There are three ways to get this information:

### Aggregated vs. Disaggregated Topology

Disaggregated mode is activated automatically when prefill workers register alongside decode workers. See [Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving) for details.

## More Router Docs

: Cost model, worker selection, and routing primitives[Routing Concepts](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/routing-concepts): Canonical router flags, environment variables, defaults, and boolean forms[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#router): Router behavior, transport modes, load tracking, and tuning guidance[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning): Prefill and decode routing setups[Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving): Runtime metadata and decode routing constraints for topology-aware prefill/decode handoff[Topology-Aware KV Transfer](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/topology-aware-kv-transfer): Replicas, remote indexers, persistence, and recovery[Router Operations](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-operations): Python API usage, K8s examples, and custom routing patterns[Router Examples](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-examples): Recommended test layers for non-trivial router changes[Router Testing](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-testing): Cross-datacenter KV routing and the DC Relay[Multi-DC KV Routing](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/multi-dc-kv-routing): Run the KV indexer as a separate service[Standalone Indexer](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-indexer): Select workers and account for reservations without forwarding requests[Standalone Selection Service](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-selection): Run active-request accounting as a separate service[Standalone Slot Tracker](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-slot-tracker): Gap detection and replay behavior[KV Event Replay — Dynamo vs vLLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/kv-event-replay-comparison)