# [Issue #2814] [RFC]: Agent-Aware KV Cache Affinity Scheduling and Lifecycle Management

source: https://github.com/vllm-project/aibrix/issues/2814
state: open | updated: 2026-09-26T02:59:17Z
labels: area/gateway, kind/feature, area/testing, area/runtime, area/kv-cache, area/batch

## 正文

### Summary

AIBrix has established a production-grade distributed KV cache architecture with L1 DRAM offloading, L2 shared cache clusters, prefix-aware routing, and P&D (Prefill/Decode) disaggregation, delivering significant efficiency gains for general inference workloads. As agent-based traffic becomes dominant in production clusters, the current cache stack lacks semantic awareness of agent task properties, leading to suboptimal cache reuse, avoidable eviction of high-value prefixes, and misalignment between cache lifetime and agent execution cycles.

This RFC proposes extending the AIBrix stack with agent-native cache management capabilities built on top of standard `agent_hints` fields. The changes span the API gateway routing layer, KV cache runtime, event synchronization protocol, and P&D scheduler — all while preserving full backward compatibility with existing engines, cache backends, and routing policies. The proposal introduces program-level cache affinity, context-weighted eviction, session-aligned cache pinning, and intent-driven speculative prefill, optimized specifically for AIBrix's layered cache and disaggregated architecture.

### Motivation

Agent workloads now account for 40%–60% of production inference traffic in AIBrix deployments, and exhibit fundamentally different cache behavior compared to one-shot requests. The current AIBrix cache stack was designed for generic prompt-based traffic and faces four structural gaps when handling agent workloads:

### 1. Prefix routing lacks program-level semantic affinity

AIBrix's existing `prefix-cache` routing plugin matches requests purely by recursive token block hashes, with no awareness of agent program identity. Requests from different sessions of the same agent program — which share identical system prompts, tool definitions, and role instructions that can span thousands of tokens — are treated as unrelated prefixes. This results in:

- Redundant prefills of the same program prefix across multiple Serving Units
- Wasted L2 cache capacity from duplicate copies of identical program-level prefix blocks
- No ability to intentionally colocate same-program workloads for maximum cache sharing

In multi-tenant agent clusters, this limits global prefix cache reuse rate to roughly 30%, even when most workloads share common agent program templates.

### 2. Cache eviction is blind to context value and task priority

AIBrix's current scan-resistant eviction policy ranks KV blocks only by access frequency and recency, uniformly across all block types. In agent scenarios, cache value varies by orders of magnitude:

- `system_prompt` and `tool_def` blocks are reused across the entire session and have the highest durable value
- `conversation` history blocks accumulate incrementally and have moderate value
- `reasoning` intermediate blocks are single-use and have near-zero reuse value

Without semantic differentiation, high-value permanent prefixes are frequently evicted to make room for low-value temporary reasoning state. Additionally, there is no priority differentiation between production-critical agent tasks and background batch workloads, so low-priority traffic can evict high-priority session cache and cause SLA violations.

### 3. Cache lifetime is decoupled from agent task execution cycles

Agent workloads alternate between inference generation and external tool/API calls, with idle windows ranging from hundreds of milliseconds to tens of seconds. Under AIBrix's default LRU-based eviction, session cache becomes eligible for eviction during tool call idle periods. When the agent resumes execution:

- The full context must be re-prefilled, increasing end-to-end latency by 2–5x
- GPU cycles are wasted recomputing previously computed cache
- In P&D disaggregation mode, the session must be re-mapped to a Prefill GPU, adding scheduling overhead

The existing `session-affinity` routing only maintains pod stickiness but does not protect cache from eviction during idle periods.

### 4. KV event protocol carries no agent semantic metadata

The AIBrix KVCache v1 Connector and event synchronization protocol only transmits block-level physical attributes (block hashes, token IDs, size, medium) to the L2 cache cluster and gateway. Without agent semantic fields in events:

- The L2 cache cannot implement tiered storage policies based on priority or context type
- The gateway cannot make routing decisions informed by agent program identity
- Observability stacks cannot break down cache metrics by agent program or priority tier

### 5. No proactive prefill orchestration for multi-turn agent conversations

AIBrix's P&D disaggregation architecture separates compute-heavy prefills from decode-heavy generation, but prefill operations are still triggered only by incoming requests. For multi-turn agent dialogues, the next turn's prefix (conversation history + latest assistant reply) is highly predictable. Without an intent-driven prefill mechanism, every agent turn incurs full cold-start prefill latency, leaving first-token latency suboptimal for interactive agent use cases.

### Proposed Change

All proposed changes are additive and backward-compatible. Existing workloads without `agent_hints` continue to behave exactly as today. The proposal is structured around five targeted extensions to the AIBrix stack:

### 1. Standardized `agent_hints` Field and End-to-End Propagation

Define a standard set of agent semantic fields propagated from the API gateway through to the KV cache runtime and event protocol:

- `program_id`: string identifier for the agent program, used for affinity scheduling
- `priority`: integer task priority level, used for tiered eviction and storage
- `context_type`: enumerated value (`system_prompt`, `tool_def`, `conversation`, `reasoning`)
- `speculative_prefill`: boolean flag enabling proactive next-turn prefill
- `session_ttl_hint`: suggested cache lifetime for the session

**Integration points in AIBrix**:

- The Envoy-based API Gateway parses `agent_hints` from request headers/metadata and injects them into the request context
- The AI Runtime sidecar passes the fields to the KVCache Connector inside the Serving Unit
- The KV Event protocol appends these as optional trailing fields in `BlockStored` and `BlockRemoved` events, compatible with existing msgpack decoding

### 2. Program-Affinity Routing Extension for Request Router

Extend the gateway's routing plugin suite with a `program-affinity` mode that complements the existing `prefix-cache` and `session-affinity` policies:

- Maintain a `program_id -> Serving Unit` mapping table with sliding TTL in the router
- When a request carries a `program_id`, the router first checks which pods already have cached prefix blocks for that program (via KV event state tracking)
- Route to the warmest pod first; fall back to load-balanced routing only when target pod load exceeds a configurable threshold
- For P&D disaggregation deployments, extend the Prefill scheduler with program-level affinity, so prefills for the same agent program are colocated on the same Prefill GPU

This maximizes cross-session prefix reuse for the same agent program and eliminates redundant prefill computation across the cluster.

### 3. Context-Aware Weighted Eviction in KV Cache Runtime

Enhance both L1 and L2 cache eviction policies with semantic weighting:

- **L1 cache (engine-side connector)**: Replace uniform scan-resistant eviction with a weighted eviction score:
`eviction_score = access_score * context_weight / priority`
  - `context_weight` defaults: `system_prompt=0.1`, `tool_def=0.2`, `conversation=1.0`, `reasoning=2.0`
  - Higher priority and lower context weight make blocks less likely to be evicted
- **L2 cache cluster**: Implement priority-tiered storage. High-priority blocks are persisted in L2; low-priority blocks may be stored only in L1 to save L2 capacity

### 4. Session-Aligned Cache Pinning with Lifecycle Signals

Add session-level cache pinning integrated with agent task lifecycle:

- Define lightweight session control signals (`open`, `heartbeat`, `close`) that agent harnesses can send to AIBrix
- On `open` with a `session_id`, pin the session's KV blocks in L1 cache with an initial TTL derived from `session_ttl_hint`
- `heartbeat` signals extend the TTL during long-running operations like tool calls
- `close` signals immediately release pinned cache resources
- Sessions without a heartbeat for the TTL duration are automatically unpinned and returned to the general eviction pool

This synchronizes cache lifetime with agent execution cycles and prevents unnecessary eviction during tool call idle windows.

### 5. Speculative Prefill Orchestration for P&D Architecture

Leverage AIBrix's P&D disaggregation to implement intent-driven proactive prefill:

- When a decode request carries `speculative_prefill=true`, the scheduler registers a pending prefill task immediately after decode completes
- The Prefill GPU automatically precomputes the next turn's prefix (history + generated reply) and stores the result in L2 cache
- Prefilled entries have a short default TTL (5s) and are evicted automatically if not consumed
- When the next real request arrives, the router detects the pre-warmed L2 cache and routes accordingly, skipping prefill entirely

This reduces first-token latency for multi-turn agent conversations by proactively utilizing idle Prefill GPU capacity.

### Alternatives Considered

_No response_

### Area

Not sure

## 评论 (1)

### googs1025 · 2026-09-26

/cc
