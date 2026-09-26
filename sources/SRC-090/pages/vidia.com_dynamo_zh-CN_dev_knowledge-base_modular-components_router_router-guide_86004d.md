source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/modular-components/router/router-guide
lastmod: 2026-09-23T23:30:39.914Z

# Router Guide

Choose where routing runs and how worker-set configuration takes effect.

Use this guide to choose a router deployment topology. It does not replace the local or Kubernetes setup guides, which own the commands and manifests for each request path.

## Choose a Deployment Topology

The Frontend and EPP use the same worker selection behavior. Do not configure the Frontend to make another selection after an EPP has selected a worker.

## Choose a Routing Mode

Use `kv`

mode when cache reuse should affect placement. Workers publish KV lifecycle events so the router can measure per-worker prefix overlap. Without worker events, `kv`

mode uses load-only scoring; set `--no-router-kv-events`

to predict cache state from routing decisions instead.

Use `round-robin`

, `random`

, `power-of-two`

, `least-loaded`

, or `device-aware-weighted`

when cache state is not part of the decision. Use `direct`

when an upstream component has already selected a worker. See [Routing Concepts](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/routing-concepts#basic-routing) for policy behavior and [Configuration and Tuning](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning#kv-event-transport) for event transport.

With `DYN_LORA_ENABLED`

, use KV, random, or round-robin routing. Direct, power-of-two, least-loaded, and device-aware-weighted modes are not LoRA-aware and fail startup. Session affinity with LoRA is supported only in KV mode; random and round-robin plus affinity are rejected.

## Configure Worker Sets Consistently

The Frontend’s `--router-mode`

sets the default routing configuration. A worker set can advertise its own router configuration, which replaces the Frontend configuration for requests routed to that set.

A worker set contains replicas with the same namespace, component, endpoint, model, and worker type. The first valid model deployment card observed by a Frontend reserves the set’s configuration. Replicas with a different MDC checksum receive no traffic and cannot disrupt the incumbent, including during construction or retries. Once all incumbent workers disappear, the oldest remaining configuration becomes eligible for a fresh pipeline. See [Worker-Set Admission and Succession](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning#worker-set-admission-and-succession) for checksum compatibility, rolling updates, and readiness behavior.

Worker-set configuration replaces rather than merges with the Frontend configuration. When a worker advertises `--router-mode kv`

, restate every non-default router setting that it needs; omitting a setting selects that setting’s default instead of inheriting the Frontend value. See [Configuration Scope and Precedence](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning#configuration-scope-and-precedence) for examples and environment-variable implications.

## Choose Distributed Features Deliberately

Use [Disaggregated Serving](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/disaggregated-serving) for separate prefill and decode pools. Add [Topology-Aware KV Transfer](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/topology-aware-kv-transfer) when decode selection must honor transfer locality, and use the [Offloading Support Matrix](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/offloading-support-matrix) when lower cache tiers should influence routing.

For replicas, event recovery, and remote indexers, see [Router Operations](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-operations). For APIs that separate index, selection, or load tracking from the router process, see [Standalone Services](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/standalone-indexer).