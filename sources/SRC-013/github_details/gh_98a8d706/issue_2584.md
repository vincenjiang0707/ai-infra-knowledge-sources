# [Issue #2584] [Feature]: Agent-Aware KV Cache Affinity Scheduling and Cache Management

source: https://github.com/llm-d/llm-d/issues/2584
state: open | updated: 2026-09-26T06:34:13Z
labels: enhancement

## 正文

### Feature Area

KV Cache / Prefix Caching

### Problem Statement

As agent workloads become the dominant traffic pattern in production inference services, the llm-d distributed KV cache fabric—built to unify cache management across vLLM, SGLang and other inference engines—faces fundamental structural gaps in adapting to agent-native traffic patterns. The current KV event standard and llm-d’s caching logic were designed for generic one-shot inference requests, and lack semantic abstraction for agent task properties, leading to systemic inefficiencies across the cache stack:

1. **Absence of agent semantic dimensions in the KV event standard**
The current de facto KV cache event schema only defines block-level physical attributes (block hashes, token IDs, storage tier, etc.) and basic business fields (LoRA ID, session ID, cache salt). There is no standardized way to carry agent identity, task priority, program type, or context semantics in events. As a cross-engine cache fabric, llm-d cannot implement differentiated cache governance per agent task, and can only apply a one-size-fits-all LRU eviction policy. This causes high-priority production agent workloads to have their core prefix cache evicted by low-priority background tasks, resulting in repeated prefills and SLA violations.
2. **Lack of program-level cache affinity in distributed routing**
Today llm-d routes requests primarily based on real-time worker load and generic prefix matching. Requests from the same agent program—which share identical system prompts, tool definitions and role instructions that can span thousands of tokens—are often dispatched to different inference nodes. Each node maintains a separate copy of the same prefix cache, causing severe VRAM redundancy and low global cache reuse rates. Cross-node cache sharing cannot be fully utilized, and identical prefills are repeated across nodes for the same agent program.
3. **Cache lifetime misalignment with agent task execution cycles**
Agent workloads alternate between inference generation and external tool calls / system interactions, with idle windows ranging from hundreds of milliseconds to tens of seconds. Under llm-d’s default LRU eviction policy, session cache for waiting agents is eligible for eviction when no new requests arrive during the idle window. When the agent resumes after a tool call, the full context must be re-computed from scratch, increasing end-to-end latency by 2–5x and wasting compute resources on redundant prefill computation.
4. **Context-agnostic eviction wastes high-value cache entries**
Current eviction logic treats all KV blocks equally, ranking them only by recency and frequency of access. In agent scenarios, however, cache value varies drastically by context type: system prompts and tool definitions are reused across the entire session and have the highest value; conversation history accumulates incrementally with moderate value; intermediate reasoning states are single-use and have the lowest value. Without semantic differentiation, high-value permanent prefixes are frequently evicted to make room for low-value temporary context, degrading overall cache efficiency.
5. **No intent-driven mechanism for proactive prefill coordination**
Prefill operations today are triggered passively by incoming user requests. For multi-turn agent conversations, the next turn’s prefix (conversation history + latest assistant reply) is highly predictable, but there is no standardized signal channel for agent intent. llm-d cannot orchestrate proactive pre-warming of cache across inference nodes, so every turn of an agent conversation incurs full cold-start prefill overhead, leaving first-token latency suboptimal for interactive agent use cases.

### Proposed Solution

This RFC proposes standardizing agent semantic fields in the KV cache event schema and defining a set of agent-aware cache management capabilities for the llm-d fabric. All changes follow strict backward compatibility: new fields are optional, and existing consumers and engines continue to work without modification. The solution is structured around five core alignments:

1. **Standardized optional agent semantic fields in KV events**
Append a set of optional agent-related fields to the tail of the standard `BlockStored` and `BlockRemoved` event structures, with unified naming and semantics across inference engines:
   - `priority`: integer task priority level, used for tiered eviction
   - `program_id`: string identifier for the agent program, used for affinity scheduling
   - `context_type`: enumerated semantic type of the context (`system_prompt`, `tool_def`, `conversation`, `reasoning`)
   - `agent_id`: optional unique agent instance identifier
   - `speculative_prefill`: boolean flag indicating whether proactive prefill is allowed for the session

All fields are optional and positioned at the end of the event struct. Legacy decoders will silently ignore unknown fields, and engines not supporting agent semantics can omit them entirely.

2. **Program-level cache affinity scheduling in the llm-d routing layer**
Extend the llm-d router with a `ProgramAffinity` module that maintains a `program_id -> worker` mapping with sliding TTL. When a request carries a `program_id`, the router prioritizes dispatching it to a worker that already has the corresponding prefix cache cached. The router falls back to standard load-balancing only when the target worker’s load exceeds a configurable threshold. This maximizes cross-request cache reuse for the same agent program and eliminates redundant prefix prefills across nodes.
3. **Session-aware cache lifetime management**
Add session-level cache pinning and TTL control to llm-d, aligned with agent task lifecycle signals:
   - Agent harnesses can send lightweight session control commands (`open`, `heartbeat`, `close`) to llm-d
   - On `open`, the session’s KV blocks are pinned with an initial TTL and protected from eviction
   - `heartbeat` commands extend the TTL during long-running operations like tool calls
   - `close` immediately releases the session’s cache resources
   - Sessions without a heartbeat for the TTL duration are automatically unpinned and returned to the general eviction pool

This synchronizes cache lifetime with agent task execution, eliminating unnecessary cache eviction during idle wait periods.

4. **Context-aware tiered eviction policy**
Implement a weighted eviction strategy in llm-d that assigns different eviction weights based on `context_type`:
   - `system_prompt`: lowest weight (highest retention priority)
   - `tool_def`: very low weight
   - `conversation`: baseline weight
   - `reasoning`: elevated weight (lowest retention priority)

Effective eviction priority is calculated as a combination of task `priority` and context weight. This ensures high-value, reusable prefixes are preserved even under memory pressure, while low-value temporary reasoning blocks are evicted first.

5. **Intent-driven speculative prefill orchestration**
Leverage the `speculative_prefill` flag to enable proactive cache pre-warming in llm-d:
   - When a request enables speculative prefill, llm-d coordinates with the target worker to automatically precompute the next turn’s prefix cache immediately after the current reply finishes generation
   - The prefilled cache entry has a short TTL and is released automatically if not used
   - When the next real request arrives, it hits the pre-warmed cache directly, skipping prefix prefill

This reduces first-token latency for multi-turn agent conversations by proactively leveraging idle compute capacity.

### Alternatives Considered

_No response_

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context

_No response_

## 评论 (1)

### Joyjeet045 · 2026-09-26

I’d like to take up this issue and work toward a PR for it. Please feel free to have a look at my profile for some background on my experience and technical interests.

Is this issue open for contribution?

Looking forward to contributing!
@daisyEliot 
