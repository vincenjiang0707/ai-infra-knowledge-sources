# [Issue #1527] [RFC]: Kv Events API Standardization

source: https://github.com/kvcache-ai/Mooncake/issues/1527
state: closed | updated: 2026-09-23T03:15:53Z
labels: stale, auto-closed

## 正文

@doujiang24 @yejj710 related to #1403 

# KV Cache Events API Specification

## Overview

This document specifies the wire format for KV cache events exchanged between
inference engine workers and KV cache indexers (routers). Events communicate
which sequence blocks are stored or removed on each worker so the router can
make cache-aware scheduling decisions.

### Design Principles

- **Engine-agnostic**: any engine that can emit conforming events is supported.
- **Indexer-agnostic**: the event format does not assume a specific indexer
  implementation (radix tree, nested hashmap, etc.).
- **Consecutive blocks**: all blocks within a single event are consecutive in
  sequence depth, each block being the parent of the next.
- **Ordered event streams**: events must be processed in consecutive `event_id` order
  within each `(model_name, block_size, additional_salt, lora_name, tenant_id, backend_id, medium, dp_rank)` stream.

---

## Hashing Standard

The recommended block hashing standard is **XXH3-64 with seed `1337`**, which
is currently used by Dynamo for local block hashing.

| Concept | Computation |
|---|---|
| **Local block hash** | `XXH3(token_bytes_le, 1337)` where token bytes are the little-endian `u32` token IDs in the block concatenated. |
| **Rolling sequence hash** | First block: `seq_hash[0] = local_block_hash[0]`. Subsequent: `seq_hash[i] = XXH3(seq_hash[i-1]_le \|\| local_block_hash[i]_le, 1337)` where `_le` denotes 8-byte little-endian encoding. |

All `seq_hashes` in events are rolling sequence hashes. Because each sequence
hash folds in its parent's sequence hash, a single `seq_hash` value uniquely
identifies the entire prefix of blocks up to that depth. Two sequences that
share a common prefix will have identical `seq_hash` values at every shared
depth, and diverge at the first differing block.

---

## Event Envelope

Every event shares a common envelope:

```json
{
  "event_id": 42,
  "timestamp": 1739145600000,
  "event_type": "stored",
  "model_name": null,
  "block_size": null,
  "additional_salt": null,
  "lora_name": null,
  "tenant_id": "default",
  "backend_id": "worker-0",
  "medium": null,
  "dp_rank": null
}
```

| Field | Type | Description |
|---|---|---|
| `event_id` | `u64` | Monotonically increasing sequence number, scoped per identifier dimensions. This is the authoritative ordering within a stream. |
| `timestamp` | `u64 \| null` | Unix epoch milliseconds (UTC). Informational only — used for debugging and latency tracking, **not** for ordering. |
| `event_type` | `string` | One of `"stored"`, `"removed"`, `"cleared"`. |
| `model_name` | `string \| null` | Model name or identifier. Different models produce incompatible KV cache tensors; this field distinguishes workers serving different models when a single indexer hosts multiple model configurations. |
| `block_size` | `u32 \| null` | Number of tokens per block. Different block sizes change the token-to-block mapping and produce incompatible cache structures. |
| `additional_salt` | `string \| null` | Opaque engine-defined salt string. Engines can use this to communicate any extra dimension that should affect block hash disambiguation (e.g., quantization config, model revision) without requiring new envelope fields. The indexer may fold this into its hash namespace or treat it as a separate dimension. |
| `lora_name` | `string \| null` | LoRA adapter name. `null` for base model. Applies to all blocks in this event. |
| `tenant_id` | `string` | Consumer-facing tenant or customer identity. Primarily used for memory isolation between tenants — preventing one tenant's cache activity from being visible to or interfering with another's index. |
| `backend_id` | `string` | Worker-facing backend instance identity. Identifies the downstream worker that produced or holds these KV cache blocks. |
| `medium` | `string \| null` | Memory tier where these blocks reside: `"gpu"`, `"cpu"`, `"disk"`, etc. Applies to all blocks in this event. Each medium is treated as an independent cache namespace. |
| `dp_rank` | `u32 \| null` | Data-parallel rank of the worker. |

### Identifier Dimensions and Indexer Aggregation

The event envelope exposes eight identifier dimensions:
`(model_name, block_size, additional_salt, lora_name, tenant_id, backend_id, medium, dp_rank)`. The event
format is intentionally agnostic to how the indexer uses these dimensions — it
is up to the indexer implementation to decide how to aggregate, salt, or
separate them.

Possible strategies include:

- **Single aggregated indexer**: all dimensions are tracked as node attributes
  within a shared data structure (e.g., a radix tree with per-node metadata).
  This minimizes memory overhead but requires careful bookkeeping. Note that
  `block_size` fundamentally changes the token-to-block mapping and generally
  cannot be treated as a simple node attribute — it typically requires a
  separate index.
- **Independent index per dimension**: the indexer maintains a fully
  independent data structure (tree, hashmap, etc.) for each unique value or
  combination of values of one or more dimensions. This provides strong
  isolation at the cost of higher memory usage.
- **Salt hashing**: content-altering dimensions (e.g., `lora_name`,
  `model_name`) can be folded into the block hash computation as a salt, so
  blocks with different content-altering properties naturally produce different
  hashes even for the same token sequence.

The primary motivation for separation is **memory isolation between tenants or
customers** — both for security (preventing one tenant's cache activity from
being visible to or interfering with another's data structure), performance
(preventing one tenant from bloating the indexer and degrading routing quality
for others), and contention (depending on implementation, a shared data
structure may require locking or serialization across tenants, which separate
indices avoid).

---

## Event Types

### `stored`

Published when one or more consecutive blocks are committed to the KV cache.

```json
{
  "event_id": 42,
  "timestamp": 1739145600000,
  "event_type": "stored",
  "model_name": "llama-3.1-8b",
  "block_size": 64,
  "additional_salt": null,
  "lora_name": null,
  "tenant_id": "default",
  "backend_id": "worker-0",
  "medium": "gpu",
  "dp_rank": 0,

  "seq_hashes": [1234567890, 9876543210, 1122334455],
  "base_block_idx": 5,
  "parent_hash": 9999999999,
  "token_ids": null
}
```

| Field | Type | Description |
|---|---|---|
| `seq_hashes` | `u64[]` | Rolling sequence hashes of the stored blocks. Blocks are consecutive in sequence depth. |
| `base_block_idx` | `u32 \| null` | Depth index (0-based) of the first block in this event. Block `i` in the array sits at sequence depth `base_block_idx + i`. |
| `parent_hash` | `u64 \| null` | Rolling sequence hash of the parent block (the block at depth `base_block_idx - 1`). `null` when the first block is at the root of the sequence. |
| `token_ids` | `u32[] \| null` | Token IDs across all blocks in this event. When provided, the consumer can recompute local block hashes from these tokens. |

**Field requirements:**

- At least one of `base_block_idx` or `parent_hash` must be provided so the
  consumer can determine where these blocks sit in the sequence. Both may be
  provided. Some indexer implementations (e.g., radix tree) require
  `parent_hash` to locate the insertion point; others (e.g., nested hashmap
  based) need `base_block_idx` for depth tracking.
- `token_ids` is required when the engine does not follow the standardized
  hashing (XXH3-64, seed 1337), so the consumer can recompute local block
  hashes. It may be omitted when the engine provides conforming `seq_hashes`.

### `removed`

Published when one or more blocks are evicted from the KV cache.

```json
{
  "event_id": 43,
  "timestamp": 1739145601000,
  "event_type": "removed",
  "model_name": "llama-3.1-8b",
  "block_size": 64,
  "additional_salt": null,
  "lora_name": null,
  "tenant_id": "default",
  "backend_id": "worker-0",
  "medium": "gpu",
  "dp_rank": 0,

  "seq_hashes": [1122334455],
  "base_block_idx": 7
}
```

| Field | Type | Description |
|---|---|---|
| `seq_hashes` | `u64[]` | Rolling sequence hashes of the removed blocks. |
| `base_block_idx` | `u32 \| null` | Depth index of the first removed block. When used with `seq_hashes`, the array length determines the count. |

**Field requirements:**

- `seq_hashes` is required.
- `base_block_idx` is optional. Both may be provided.

### `cleared`

Published when all blocks for this identifier dimensions stream are purged.

```json
{
  "event_id": 44,
  "timestamp": 1739145602000,
  "event_type": "cleared",
  "model_name": "llama-3.1-8b",
  "block_size": 64,
  "additional_salt": null,
  "lora_name": null,
  "tenant_id": "default",
  "backend_id": "worker-0",
  "medium": "gpu",
  "dp_rank": 0
}
```

No additional payload fields.

## Open for Discussion

### Content-altering dimensions (LoRA, multimodal, etc.)

Dimensions that change the actual KV cache content — such as LoRA adapters or
multimodal objects — must produce different block hashes so that blocks with
identical tokens but different cached values are not falsely matched. Dimensions
that only affect ownership or location (e.g., `tenant_id`, `backend_id`,
`dp_rank`, `medium`) do not alter block content and are tracked as metadata by
the indexer.

There are two approaches for handling content-altering dimensions:

**Option A: Fold into block hashes on the engine side (salt hashing)**

The engine incorporates content-altering metadata into the block hash
computation before publishing events. For example, the Dynamo `tokens` crate
supports a `SaltHash` — a hash of arbitrary metadata (model architecture, LoRA
adapter, etc.) used as the XXH3 seed instead of the fixed `1337`:

```
salt_hash      = XXH3(salt_bytes, 0)
local_block_hash = XXH3(token_bytes_le, salt_hash)
seq_hash[i]      = XXH3(seq_hash[i-1]_le || local_block_hash[i]_le, salt_hash)
```

Similarly, multimodal content hashes can be appended to the token bytes before
hashing. Under this approach, `seq_hashes` in events already reflect these
dimensions, and no additional event fields are needed. However, this requires
the engine to implement a standardized salt hashing scheme, which may be too
much to ask for cross-engine standardization.

**Option B: Include as explicit fields in events**

The engine publishes raw metadata (e.g., `lora_name`, per-block `mm_hash`) as
additional fields in the event, and the consumer's indexer incorporates them
into its data structure (e.g., separate tree branches, separate hash
namespaces). This keeps the event format self-describing and doesn't require
the engine to implement a specific hashing scheme, but adds protocol complexity
and pushes the disambiguation logic to the consumer. Note that even under this
approach, some form of salt hashing may still be needed for multi-tenant
deployments — to enforce memory isolation between tenants so that one tenant's
cache activity (e.g., bloating the indexer) cannot affect another's.

Open for discussion on which approach (or combination) is preferable.

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (21)

### yejj710 · 2026-02-11

@PeaBrane   I have a few questions:
1. Is `work_id` a unique identifier for a LLM service instance?  
2. `Scoped per (worker_id, dp_rank, lora_name, medium)`. Should separate indexers be maintained for each different medium, or should the medium be included as a property within the indexer? I’m more in favor of including the medium as a internal property, as that would be more extensible.  
3. With the introduction of a storage backend, such as `Mooncake`, the current plan is to add a kv-event publisher. In the future, this could be used to support more granular extensions (e.g., precise awareness of cache node locations, distinction between local store and pooling store, etc.). What are your thoughts on this?

### PeaBrane · 2026-02-11

@yejj710 Thanks for your questions

1. Yea. I think this would just be `tenant_id` in the KvIndexer API, I should rename to that.
2. My idea was to only have a single indexer aggregating across `(worker_id, dp_rank, lora_name, medium)`. Is this aligned with what you have in mind?
3. Yea, I think I'm aligned with this, could also have an additional `extra_fields` for the publisher to publish any extra block identification data.

### doujiang24 · 2026-02-11

@PeaBrane Great, mostly lgtm with a few questions:

1. Seems `block_size` is missing?
2. Where does `worker_id` come from? sglang & vllm do not have such a field yet.

### PeaBrane · 2026-02-11

@doujiang24 

1. Hmm I'm not 100% sure if block size is needed in the kv events themselves. I was thinking this is static and would just be agreed on and kept by the publishers and indexers. What do you think?

2. That's a good question and I'm not super sure. Currently in dynamo, we wrap each vllm / sglang worker with a worker_id / tenant_id / lease_id, so when we relay the raw engine kv events with our publisher we can tag that field on. So I guess for a standalone KV indexer service, it would need to depend how the discovery is set up.

Actually thinking more about the second point. The indexer itself just needs a unique identifier per worker, can be even a simple uuid kept by each worker. The whole discovery / routing bits would be orchestrated by an external router the indexer can be agnostic to. 

These are impl details and out of scope here, but at minimal the kv events would need this worker id somehow tagged before ingestion by the indexer

### yejj710 · 2026-02-11

> 1. My idea was to only have a single indexer aggregating across `(worker_id, dp_rank, lora_name, medium)`

@PeaBrane  agree.  I'm thinking about whether to treat medium as an attribute inside the indexer, or as one of the key components that differentiates between different indexers.

one more thing: I think `lora_name` seems not enough, we will need `model_name` & `lora_name`  together to uniquely identify an inference model service. what's your opinion?

### PeaBrane · 2026-02-11

@yejj710 @doujiang24 

My idea was to have the KV events only communicating (pub sub) within a homogenously configed model deployment group. So only one KvIndexer logical struct would be receiving them (but we can have replicas of it listening on the same events)

If we are to do pub sub across model groups, then yes I think model name and block size would be necessary, to know which indexer service to target among the multiple.

What setup do you guys have in mind? Now looking back at the KvIndexer API definition, it does look like the indexer service assumes multiple indexers for multiple models (and potentially of different block sizes), which I think make sense. So I'm happy to also include model_name and block_size in this case.

(Tangential discussion would be here to also include block_size in the query API if we query by block hashes)

### doujiang24 · 2026-02-12

@PeaBrane 
Yes, One KvIndexer service serving multiple model groups is required in our use case.

Router and KvIndexer are the same, multiple model groups share the same Router/KvIndexer service.

### PeaBrane · 2026-02-12

@doujiang24 got it. I'll update the RFC to include model name and block size in this case

### PeaBrane · 2026-02-12

@yejj710 @doujiang24 

Actually, thinking about everything a bit more. I do think we need a clear delineation / definitions of `tenant_id` and `instance_id`. For me, it looks like `tenant_id` is used to distinguish between external users of the indexer (e.g. customer / router / deployment identifiers), while `instance_id` is used to distinguish between which worker / engine owns the blocks, especially if they are still in GPU memory? So if we imagine indexer to sit bewteen the routers and engines, `tenant_id` is an upstream identifier and `instance_id` is a downstream identifier.

What do you guys think on your end? Now looking more at it, I think `instance_id` would actually be the `api_server_unique_name` in the KvIndexer RFC.

### doujiang24 · 2026-02-14

@PeaBrane 

Yea, agreed. `instance_id` could be better. Maybe `string` could be better instead of `int`, thoughts?


### vladnosiv · 2026-02-17

Thanks for putting this together! We're using both MoonCake Store and Dynamo, so we're very interested in seeing a standardized KV cache events API.

The current RFC appears to assume that KV cache is stored on the inference workers themselves. This creates an implicit coupling between inference execution and cache storage.
However, architectures like MoonCake support a fully decoupled model where cache storage is independent of inference workers. 
For example, in our setup:
* Inference workers don't contribute any additional memory to the shared cache pool
* A DaemonSet deploys one cache storage worker per node, pooling available host memory into a shared distributed cache
* This means cache survives inference worker restarts - no cold start, no warmup needed

This decoupling enables interesting routing strategies based on cache locality rather than cache ownership - routing a request to an inference worker on the same node as the cached blocks (with lower latency) vs. a worker on a different node.

Can you consider whether the spec could accommodate decoupled architectures too?

### PeaBrane · 2026-02-17

@vladnosiv 

Thanks for the feedback, we believe the current spec already handles this via `backend_id`.

`backend_id` doesn't have to be an inference worker — it identifies **whatever entity holds the KV cache blocks**. In your DaemonSet setup, it would be the cache storage daemon:

```json
{
  "backend_id": "node-3-cache-daemon",
  "medium": "cpu"
}
```

The router knows blocks are on node-3 in CPU memory and can route to co-located inference workers for lower latency. Since the daemon publishes events (not the inference workers), cache survives worker restarts with no cold start.

Does this address your concern, or do you see cases where a separate location field would be needed on top of `backend_id`?


### vladnosiv · 2026-02-18

@PeaBrane 

Yes, I really didn't fully realize the universality of backend_id, thank you! Special thanks for tenant_id - a very useful feature

### yejj710 · 2026-02-24

@PeaBrane 
> I do think we need a clear delineation / definitions of `tenant_id` and `instance_id`. For me, it looks like `tenant_id` is used to distinguish between external users of the indexer (e.g. customer / router / deployment identifiers), while `instance_id` is used to distinguish between which worker / engine owns the blocks

Totally agree. Using `tenant_id` to distinguish different users and `instance_id` to distinguish different workers/engines makes this definition very clear.

> What do you guys think on your end? Now looking more at it, I think `instance_id` would actually be the `api_server_unique_name` in the KvIndexer RFC.

Yes. Also, to maintain consistency in naming on both sides, I will use `instance_id` instead of `api_server_unique_name` .
BTW, currently we use `backend_id` to mark different instances in KV Events api, right?

### PeaBrane · 2026-02-24

@yejj710 Yea, I was thinking of either backend_id or instance_id.

backend_id may be more general if the kv block ownerships are decoupled from engine instances as @vladnosiv said

What do you guys think?

### yejj710 · 2026-02-24

@PeaBrane 
I prefer `backend_id`, because it has better scalability.
In addition, for the KVindexer, since requests can only be dispatched to specific engine instances, the `instance_id` is already sufficient, right?

### PeaBrane · 2026-02-24

@yejj710 yes makes sense to me

### github-actions[bot] · 2026-06-09

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-06-16

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.

### github-actions[bot] · 2026-09-16

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-23

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.
