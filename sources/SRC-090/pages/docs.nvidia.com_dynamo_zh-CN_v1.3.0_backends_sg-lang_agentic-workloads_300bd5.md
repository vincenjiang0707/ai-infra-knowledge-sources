source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/backends/sg-lang/agentic-workloads
lastmod: 2026-09-23T23:30:39.914Z

# SGLang for Agentic Workloads

This guide covers SGLang-specific configuration for agentic serving with Dynamo. It explains which SGLang engine flags to enable, how Dynamo’s [agent hints](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/nvidia-request-extensions-nvext#agent-hints) map to SGLang behavior, and how session headers interact with SGLang 0.5.15.

## Overview

Agentic workloads (tool-calling loops, multi-turn reasoning, code generation pipelines) have different performance characteristics than batch inference:

**Prefix-heavy**: Successive turns share a growing conversation prefix. KV cache reuse is critical for low TTFT.**Priority-sensitive**: Some requests (user-facing agent turns) matter more than background tasks.**Long-lived**: Conversations span minutes to hours. Cache eviction under memory pressure can destroy accumulated KV state.

Dynamo’s agent hints give the router per-request metadata. SGLang’s engine flags control how that metadata affects scheduling and eviction on the worker. For the cross-layer Dynamo priority semantics, see [Priority Scheduling](https://docs.nvidia.com/dynamo/v1.3.0/components/router/priority-scheduling).

## SGLang Engine Flags

### Priority Scheduling

Enable priority-based scheduling so the engine respects the `priority`

value from `nvext.agent_hints.priority`

:

When priority scheduling is enabled, the engine uses the `priority`

field from `nvext.agent_hints`

to order requests in its internal queue. Requests with higher effective priority are scheduled before lower-priority ones. Ties are broken by arrival time.

Router queue priority is configured separately on the frontend with
`--router-queue-threshold`

; see
[Router Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning#routing-behavior).

### Priority-Based KV Cache Eviction

By default, SGLang evicts radix tree nodes using LRU. You can switch to priority-based eviction so that low-priority cache entries are evicted before high-priority ones:

This does **not** require HiCache. It controls GPU-only radix tree eviction. When the GPU KV cache is full:

: Evicts the least recently used leaf nodes first.`lru`

: Evicts lowest-priority leaf nodes first. Nodes with equal priority fall back to LRU ordering.`priority`


#### Interaction with HiCache

When both `--radix-eviction-policy priority`

and `--enable-hierarchical-cache`

are enabled, priority affects eviction at both tiers:

The practical impact depends on your write policy. With `write_through`

, GPU eviction is just a demotion — the real deletion happens at host eviction, which is where priority ordering matters most.

## How Agent Hints Map to SGLang

Dynamo’s `nvext.agent_hints`

fields are consumed by the router and forwarded to SGLang workers. Here is how each hint interacts with the SGLang engine:

### Example: Agentic Request with Hints

## Session Identity

Dynamo normalizes agent headers such as `X-Dynamo-Session-ID`

for request tracing and router affinity. SGLang 0.5.15 supports passive session-aware radix ownership through a top-level `session_id`

request field, but the Dynamo worker does not attach this ID to SGLang generate requests yet.

SGLang’s `session_params`

belongs to its explicit session lifecycle and requires a session created through `open_session`

. It is not a passive KV ownership tag. Passive session ownership also requires SGLang’s `--enable-session-radix-cache`

flag.

The `--radix-eviction-policy priority`

flag controls priority-based KV eviction only; it does not tag radix entries by session. `X-Dynamo-Session-Final: true`

is normalized into an internal KV eviction hint, but the SGLang backend does not act on that hint in this release.

## Quickstart

The `agg_agent.sh`

launcher starts an aggregated SGLang worker and Dynamo frontend for agent workloads:

Agent providers send session headers directly for tracing and router affinity; no body-level lifecycle object is needed.

## See Also

: Full[NVIDIA Request Extensions (nvext)](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/nvidia-request-extensions-nvext)`nvext`

field reference including agent hints: Router configuration and CLI arguments[Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning): Enabling hierarchical KV cache[SGLang HiCache](https://docs.nvidia.com/dynamo/v1.3.0/integrations/kv-cache-integrations/hi-cache)