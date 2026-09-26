source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/components/router/kv-event-replay-dynamo-vs-v-llm
lastmod: 2026-09-23T23:30:39.914Z

KV Event Replay — Dynamo vs vLLM


KV Event Replay — Dynamo vs vLLM

## Overview

Both Dynamo and vLLM publish KV cache events (block stored, block removed, etc.) over a fire-and-forget transport (ZMQ PUB/SUB). Because PUB/SUB is lossy, both systems need a mechanism for consumers to detect missed messages and recover. This document compares the two approaches.

## The Problem

A KV event consumer (router, cache coordinator) subscribes to a live stream of block events from workers. Events carry monotonically increasing sequence numbers. When the consumer detects a gap in the sequence (e.g., received seq 42 then seq 45), it needs to recover the missed events or it will have a stale, incorrect view of the worker’s KV cache state.

## Architecture Comparison

## How Each System Works

### vLLM: Buffer-Only Replay

vLLM’s `ZmqEventPublisher`

(in `vllm/distributed/kv_events.py`

) runs two ZMQ sockets in a background thread:

**PUB socket**(default`tcp://*:5557`

): Streams`KVEventBatch`

messages tagged with a monotonic sequence number.**ROUTER socket**(optional, e.g.,`tcp://*:5558`

): Handles replay requests from consumers.

The publisher keeps a `deque`

of the last `buffer_steps`

(default 10,000) serialized batches. When a consumer detects a gap, it sends the missing start sequence number to the ROUTER socket. The publisher linearly scans the buffer and streams back all batches from that sequence onward, ending with a sentinel (`seq=-1, payload=empty`

).

**Trade-offs:**

- Lightweight — no additional state beyond the buffer itself; easy to reason about and deploy.
- If the gap is older than the buffer window, the consumer must rebuild state through other means (e.g., restart and re-discover).
- No built-in initial state sync — a consumer that connects after events have already been published starts with an empty view.
- Linear scan on every replay request (no indexing into the buffer).
- Consumer handles dedup by checking
`replay_seq > last_seq`

.

### Dynamo: Buffer + Indexer with Tree Dump Fallback

Dynamo’s `LocalKvIndexer`

(in `lib/kv-router/src/indexer/local.rs`

) wraps a `KvIndexer`

(backed by a `RadixTree`

) with a circular event buffer:

When the router queries a worker for events via `get_events_in_id_range(start_id, end_id)`

, the local indexer returns one of three responses:

The tree dump fallback means that when the buffer can’t satisfy the request, the indexer falls back to dumping the entire tree state. This makes “buffer too old” a recoverable condition at the cost of additional complexity and memory for maintaining the tree.

## Gap Detection

Both systems detect gaps the same way: the consumer tracks the last sequence/event ID it processed and compares it against the next one received.

**vLLM** (from `examples/online_serving/kv_events_subscriber.py`

):

**Dynamo** (from `lib/llm/src/kv_router/worker_query.rs`

):
The router tracks `last_recovered_event_id`

per worker and requests `recover_from_worker(worker_id, dp_rank, start_event_id, end_event_id)`

when it detects a gap or on initial discovery. The local indexer handles the complexity of deciding whether to replay from buffer or dump the tree.

## When to Use Which

**vLLM’s built-in replay** is a good fit when:

- You are running vLLM standalone and want basic gap recovery without additional infrastructure.
- Your consumer is long-lived and rarely disconnects — transient gaps are the main concern.
- You are building a custom external router or cache coordinator and want to consume KV events directly from vLLM without wrapping it in another framework.

**Dynamo’s local indexer** is a good fit when:

- You need robust recovery, including initial state sync for newly joined routers or consumers that were offline for extended periods.
- You are running multiple router replicas that may start at different times and need to converge on a consistent view of cache state.
- You want dedup and recovery handled by the infrastructure rather than implementing it in each consumer.

The two approaches share the same core idea — a FIFO ring buffer for catching up on small, transient gaps. Dynamo adds a RadixTree underneath as authoritative state, which enables the tree dump fallback for full state recovery at the cost of additional memory and complexity. vLLM keeps it simple with just the buffer, which is sufficient when consumers are stable and gaps are short-lived.

For deployments using Dynamo’s KV-aware routing, the local indexer is used automatically. For standalone vLLM deployments where you want to build your own event consumer, vLLM’s replay buffer provides a lightweight starting point.

## See Also

:[KV Router Index Data Structures](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/lib/kv-router/src/indexer/README.md)`RadixTree`

,`ConcurrentRadixTree`

, and`PositionalIndexer`

internals: Deployment modes and quick start for KV-aware routing[Router Guide](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/kv-cache-aware-routing): Router flags and tuning details[Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.2.1/components/router/configuration-and-tuning): Architecture details and event transport modes[Router Design](https://docs.nvidia.com/dynamo/v1.2.1/design-docs/component-design/router-design)