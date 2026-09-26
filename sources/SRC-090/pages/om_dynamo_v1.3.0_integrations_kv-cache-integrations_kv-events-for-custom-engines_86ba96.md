source: https://docs.nvidia.com/dynamo/v1.3.0/integrations/kv-cache-integrations/kv-events-for-custom-engines
lastmod: 2026-09-24T19:58:16.636Z

# KV Events for Custom Engines

This document explains how to implement KV event publishing for custom inference engines, enabling them to participate in Dynamo’s KV cache-aware routing.

This guide covers lower-level Python workers and custom runtime integrations
that instantiate `KvEventPublisher`

directly. Unified backends should prefer
`LLMEngine.kv_event_sources()`

and let `Worker`

construct publishers; see
[KV event publishing for unified backends](https://docs.nvidia.com/dynamo/v1.3.0/backends/custom-backend/writing-unified-backends#python-kv-event-publishing-optional).

## Overview

The KV Router relies on real-time events from backend workers to track which KV cache blocks are stored on each worker. When your custom engine allocates or evicts KV cache blocks, it should publish these events so the router can make optimal routing decisions.

Events are published over the **Dynamo event plane**, a transport-agnostic pub/sub layer that supports both NATS and ZMQ backends (see [Event Plane](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/communication-planes/event-plane) for details). The `KvEventPublisher`

binding handles all transport concerns — your engine code does not interact with the event plane directly.

`KvEventPublisher`

supports two publishing modes:

**Direct publishing**— Your engine calls`publish_stored()`

/`publish_removed()`

to push events directly over the event plane. Simplest approach for custom engines.**ZMQ relay**— For engines that emit raw KV events over a ZMQ socket (like SGLang and vLLM). The publisher subscribes to the ZMQ endpoint and relays events to the event plane automatically.

## Event Types

The KV cache supports three event types:

### Event Structure

Each event contains:

: Monotonically increasing identifier per worker (managed internally by the publisher)`event_id`

: Data parallel rank (0 if DP not enabled)`dp_rank`

: One of`data`

`Stored`

,`Removed`

, or`Cleared`


For `BlockStored`

events:

: List of token IDs for the stored blocks`token_ids`

: List of`block_hashes`

**sequence block hashes**from the engine’s block manager. These are cumulative hashes that incorporate all tokens from the start of the sequence up to and including the current block (not just the tokens within that block). This enables prefix matching across requests.: Number of tokens per block (should all equal`num_block_tokens`

`kv_block_size`

): Hash of the parent block. Required for all blocks except the first block in a sequence (which has no parent).`parent_hash`

: LoRA adapter name string (omit or`lora_name`

`None`

for base model). When set, the adapter name is incorporated into block hash computation so that blocks for different LoRA adapters (or the base model) are never conflated.

For `BlockRemoved`

events:

: List of sequence block hashes being evicted`block_hashes`


## Direct Publishing (Recommended for Custom Engines)

Call `publish_stored()`

and `publish_removed()`

directly from your engine code. The publisher handles event IDs, serialization, and transport.

**When to use:**

- Building a custom inference engine from scratch
- Your engine doesn’t have a ZMQ-based event system
- You want the simplest integration path

### Basic Setup

### Integration with Your Engine

## ZMQ Relay (For Engines with Raw KV Events)

For engines that already publish raw KV events over a ZMQ socket (like SGLang and vLLM), use the same `KvEventPublisher`

with a `zmq_endpoint`

. The publisher subscribes to the ZMQ socket and relays events to the event plane automatically.

**When to use:**

- Your engine already publishes KV events via ZMQ (like SGLang or vLLM)
- You want to decouple event publishing from your engine’s main loop

### Setup

Pass `zmq_endpoint`

(and optional `zmq_topic`

) to the same `KvEventPublisher`

:

No further calls to `publish_stored()`

/ `publish_removed()`

are needed — the publisher reads events from the ZMQ socket and forwards them automatically.

### ZMQ Wire Format

The ZMQ message format (compatible with SGLang / vLLM):

Each event in the payload is a dictionary with a `type`

field (`BlockStored`

, `BlockRemoved`

, or `AllBlocksCleared`

).

For `BlockStored`

:

For `BlockRemoved`

:

For `AllBlocksCleared`

:

## API Reference

`KvEventPublisher`


`publish_stored()`


Publish a block-stored event. Event IDs are managed internally. When `lora_name`

is provided, the adapter name is mixed into block hash computation so blocks cached under different adapters produce distinct hashes.

`publish_removed()`


Publish a block-removed event. Event IDs are managed internally.

`shutdown()`


Stop background tasks (ZMQ listener, event forwarding).

## Best Practices

-
your engine’s actual block size.`kv_block_size`

must match -
for all blocks except the first in a sequence — it links blocks to enable prefix matching.`parent_hash`

is required -
**Block hashes are signed 64-bit integers**in the Python API. The publisher handles conversion internally. -
**Event ordering is automatic**— the publisher assigns monotonically increasing event IDs. You do not need to track event IDs yourself.

## See Also

: Transport options (NATS, ZMQ) and configuration[Event Plane](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/communication-planes/event-plane): Router flags, tuning, and production setup[Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning): Architecture details and event transport modes[Router Design](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/component-design/router-design)