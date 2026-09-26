source: https://docs.nvidia.com/dynamo/zh-CN/knowledge-base/modular-components/backends/sg-lang/agents-on-sg-lang
lastmod: 2026-09-23T23:30:39.914Z

# SGLang for Agentic Workloads

Priority scheduling and session control for multi-turn agentic serving

This guide covers SGLang-specific configuration for agentic serving with Dynamo. It explains which SGLang engine flags to enable, how Dynamo’s [agent hints](https://docs.nvidia.com/dynamo/additional-resources/nvidia-request-extensions-nvext#agent-hints) map to SGLang behavior, and how to use session control to manage KV cache for multi-turn agent conversations.

## Overview

Agentic workloads (tool-calling loops, multi-turn reasoning, code generation pipelines) have different performance characteristics than batch inference:

**Prefix-heavy**: Successive turns share a growing conversation prefix. KV cache reuse is critical for low TTFT.**Priority-sensitive**: Some requests (user-facing agent turns) matter more than background tasks.**Long-lived**: Conversations span minutes to hours. Cache eviction under memory pressure can destroy accumulated KV state.

Dynamo’s agent hints give the router per-request metadata. SGLang’s engine flags control how that metadata affects scheduling and eviction on the worker. For the cross-layer Dynamo priority semantics, see [Priority Scheduling](https://docs.nvidia.com/dynamo/agents/priority-scheduling).

## SGLang Engine Flags

### Priority Scheduling

Enable priority-based scheduling so the engine respects the `priority`

value from `nvext.agent_hints.priority`

. Add the flag to the SGLang worker’s `args:`

in your DGD:

When priority scheduling is enabled, the engine uses the `priority`

field from `nvext.agent_hints`

to order requests in its internal queue. Requests with higher effective priority are scheduled before lower-priority ones. Ties are broken by arrival time.

Router queue priority is configured separately on the frontend with
`--router-queue-threshold`

; see
[Router Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning#routing-behavior).

### Priority-Based KV Cache Eviction

By default, SGLang evicts radix tree nodes using LRU. You can switch to priority-based eviction so that low-priority cache entries are evicted before high-priority ones. Add the flag to the worker `args:`

:

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

Port-forward the Frontend Service (`kubectl port-forward svc/<deployment-name>-frontend 8000:8000 -n ${NAMESPACE}`

), then send a request carrying `nvext.agent_hints`

:

## Session Control for Subagent KV Isolation (Experimental)

Agentic orchestrators often spawn short-lived subagents (research, code execution, planning) that accumulate KV cache, use it for a few turns, then die. Under normal radix cache behavior, this ephemeral KV pollutes the tree and competes with the lead agent’s long-lived prefix for eviction.

Session control solves this by holding subagent KV in dedicated **streaming session slots** outside the radix tree. Session KV is invisible to eviction, has no L2 backup overhead, and is freed deterministically on close or timeout.

### How It Works

Key behaviors:

**Turn 1**goes through the normal radix tree, so the subagent shares the lead agent’s cached system prompt prefix.**Turns 2+**skip the radix tree entirely. KV is restored from the`SessionSlot`

in O(1).**Session KV is invisible to eviction**. It cannot be evicted — only freed by explicit close or inactivity timeout.**Deterministic cleanup**: On close, session KV is freed immediately.**Router-side affinity**: The`StickySessionRouter`

maintains a`session_id -> (worker_id, dp_rank)`

mapping with sliding-window TTL. Clients can use`action: "bind"`

for router-only sticky routing, or`action: "open"`

for SGLang streaming-session KV isolation; both route later turns to the pinned worker/rank.

### Enabling Session Control

Session control is request-driven. The `StickySessionRouter`

activates automatically when a request carries `nvext.session_control`

— no additional frontend flags are needed beyond `--router-mode kv`

. Use `action: "bind"`

for router-only sticky routing without calling SGLang. On the worker side, streaming sessions must be explicitly enabled only for `action: "open"`

/ `action: "close"`

lifecycle RPCs and session KV isolation.

Session control is currently supported only on the SGLang backend. vLLM and TensorRT-LLM do not yet expose the streaming session API.

Streaming sessions require SGLang `0.5.11`

or later, which includes changes from [sgl-project/sglang#21875](https://github.com/sgl-project/sglang/pull/21875) (session-aware cache, race condition fixes, session metrics).

**SGLang worker** — add `--enable-streaming-session`

to the worker `args:`

:

**Router** — set KV routing mode on the Frontend `args:`

:

### Request Format

#### Opening a session

Include `session_control`

with `action: "open"`

on the first request:

#### Subsequent turns

Include `session_control`

with just `session_id`

(no action). The router resolves affinity automatically:

#### Closing a session

Include `action: "close"`

. The close RPC fires after generation completes:

### Limitations

**Streaming sessions only**: Sessions are opened with`streaming=True`

, which means only sequential append operations are supported. Branching (`replace`

), token-level rewind (`offset`

), and`drop_previous_output`

are not supported.**Timeout is idle-based**: The timeout refreshes on every request. If a subagent pauses for a long tool call that exceeds the timeout, the session is reaped and KV is freed. The subagent must re-open the session and re-prefill.**Session metrics**: Active session count (`sglang:num_streaming_sessions`

) and held KV tokens (`sglang:streaming_session_held_tokens`

) are exported as Prometheus gauges on the worker’s metrics endpoint.

## Quickstart

### Launch Script

The `agg_agent.sh`

script launches a single aggregated worker with session control, sticky routing, and KV events:

The frontend listens on port 8000 (override with `DYN_HTTP_PORT`

). Worker metrics are on port 8081.

This script is a local convenience for development. On Kubernetes, assemble the same setup in a DGD: a `--router-mode kv`

Frontend plus an SGLang worker carrying `--enable-streaming-session`

(and any priority/eviction flags from the sections above), then `kubectl port-forward`

the Frontend Service.

### Testing with OpenCode

[OpenCode](https://github.com/opencode-ai/opencode) is an open-source AI coding agent with built-in support for subagents, tool calling, and OpenAI-compatible endpoints. The [Dynamo provider fork](https://github.com/ishandhanani/opencode/tree/idhanani/dynamo-provider) injects `nvext.session_control`

on subagent requests, giving each spawned agent its own Dynamo streaming session with sticky routing and KV isolation.

When OpenCode spawns a subagent (via the `task`

tool), the provider automatically:

- Sends
`session_control.action = "open"`

on the subagent’s first turn - Routes subsequent turns to the same worker via
`session_id`

- Sends
`session_control.action = "close"`

when the subagent completes, freeing KV

The primary agent runs without session control — only subagent sessions are pinned. This keeps lead-agent requests load-balanced while subagent multi-turn conversations stay on a single worker with warm KV cache.

#### Configuration

Model and endpoint are configured in `.opencode/opencode.jsonc`

:

## See Also

: Full[NVIDIA Request Extensions (nvext)](https://docs.nvidia.com/dynamo/additional-resources/nvidia-request-extensions-nvext)`nvext`

field reference including agent hints: Router configuration and CLI arguments[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning): Enabling hierarchical KV cache[SGLang HiCache](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/hi-cache)