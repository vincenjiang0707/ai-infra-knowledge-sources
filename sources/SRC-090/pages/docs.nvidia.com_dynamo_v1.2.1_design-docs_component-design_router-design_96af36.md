source: https://docs.nvidia.com/dynamo/v1.2.1/design-docs/component-design/router-design
lastmod: 2026-09-24T19:58:16.636Z

# Router Design

This document describes the internal architecture of the Dynamo KV Router, including block tracking mechanisms, the KV cache optimization system, event handling, and transport modes.

## KV Router Architecture

The KV Router tracks two key metrics for each worker:

-
**Potential Active Blocks**: The number of blocks that would be used for decoding if a request is routed to a worker. This includes both existing active blocks and new blocks from the incoming request. -
**Potential New Prefill Blocks**: The number of tokens that need to be computed from scratch on a worker, calculated as:- New prefill tokens = Total input tokens - (Overlap blocks × Block size)
- Potential prefill blocks = New prefill tokens / Block size


### Block Tracking Mechanisms

The router maintains block information through two complementary systems:

-
**Active Decoding Blocks**: Tracked locally by the router throughout the request lifecycle:- Incremented when adding a new request
- Updated during token generation
- Decremented upon request completion

-
**Cached Blocks**: Maintained globally by the KvIndexer using a prefix tree built from worker-reported KV events. This provides accurate overlap information for routing decisions.

## KV Cache Router

The leading Large Language Models (LLMs) today are auto-regressive and based off of the [transformer architecture](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf). One key inference optimization technique is to cache the already computed keys and values and to reuse them for the future tokens. This is called the [KV Cache](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/#key-value_caching).

### KV Cache Routing and Load Balancing

The router uses a cost function that considers both the prefill cost (influenced by cached blocks) and the decode load to make optimal routing decisions.

#### Cost Calculation

-
**Prefill blocks**: Calculated from active prompt-side token load plus the incoming request’s input tokens, divided by the block size. The system updates active prompt load when the first output token signals prefill completion. -
**Decode blocks**: Estimated from the request’s input tokens and each worker’s active sequences. The count updates when requests complete and their blocks are freed. -
**Cost formula**:- Lower costs indicate better routing choices
`overlap_score_credit`

is the device-local prefix-overlap credit multiplier, from 0.0 to 1.0`prefill_load_scale`

controls adjusted prompt-side load relative to decode blocks- Higher overlap credits favor cache reuse (improving TTFT), while lower credits prioritize even load distribution (improving ITL)


#### Worker Selection

The router selects the worker with the lowest cost. When `router_temperature`

is set to a non-zero value, the router uses softmax sampling on the normalized cost logits to introduce randomness in the selection, which can help with load distribution.

Example calculation with `overlap_score_credit = 1.0`

:

- Worker 1: raw prefill 10 blocks, device overlap 2 blocks, decode 10 blocks => cost = 8 + 10 = 18
**Worker 2: raw prefill 10 blocks, device overlap 5 blocks, decode 5 blocks => cost = 5 + 5 = 10**(selected - lowest cost)- Worker 3: raw prefill 10 blocks, device overlap 8 blocks, decode 9 blocks => cost = 2 + 9 = 11

### KV Cache Optimizations

Every inference framework will have a KV Cache for each worker. A popular inference framework library is [vLLM](https://github.com/vllm-project/vllm) where a key contribution was [PagedAttention](https://arxiv.org/abs/2309.06180), which allowed them to manage KV Cache in an efficient way by chunking requests into blocks.

Another popular inference framework, [SGLang](https://github.com/sgl-project/sglang), contributed [RadixAttention](https://arxiv.org/abs/2312.07104) which introduced a prefix tree which allows for efficient matching, inserting and eviction of KV Cache blocks. The prefix tree structure popularized KV Cache reuse.

In Dynamo, we introduce a KVPublisher which emits KV Cache events that occur at each worker and a KVIndexer which keeps track of these events globally.

### KV Block Management Flow

To get a feel for how KV Cache management works on a single worker with KV Cache reuse turned on and where the KVPublisher gets plugged in, we can walk through the KV Block management flow:

**Request tokenization**: The incoming prompt is converted into tokens**Block partitioning**: The token sequence is divided into fixed-size blocks (e.g., 16 or 64 tokens per block)**Block hashing**: Each block of tokens is hashed to create a unique identifier. When a LoRA adapter is active, the adapter name is incorporated into the hash so that blocks cached under different adapters produce distinct identifiers.**Cache lookup**:- For each block, the system checks if a matching block already exists in the KV cache
- If a match is found, the existing KV cache block is reused
- If no match is found, the system proceeds to the next step

**Resource allocation**:- For blocks without matches, the system attempts to allocate new memory space
- If sufficient memory is available, allocate memory space and proceed to step 7
- If memory is constrained, proceed to step 6

**Cache eviction**(when necessary):- The system applies an eviction policy (e.g., LRU, LFU) to identify blocks for removal
- Selected blocks are evicted from the cache
**KVPublisher emits a KV removed event notifying KVIndexer about the removed block.**- Alternatively, some systems may offload less-frequently used blocks to CPU memory.

**KV computation**:- For new blocks, the model computes key and value tensors
- These tensors are stored in the newly allocated cache blocks
**KVPublisher emits a kv stored event notifying KVIndexer about newly stored blocks**.


Further details can be found for: [SGLang](https://lmsys.org/blog/2024-01-17-sglang/), [TRT-LLM](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/) and [vLLM](https://docs.vllm.ai/en/latest/design/automatic_prefix_caching.html#design-automatic-prefix-caching).

## Events

### KVPublisher

The KVPublisher can be initialized and then called in the inference framework where blocks are allocated and removed.

The two types of events are:

- KV stored event
- KV removed event

The publisher can be initialized and used through Python bindings.

### Deterministic Event IDs

Engines do not need to emit deterministic block identifiers in KV events, as the router uses local block hashes (computed from token content) for tracking and matching blocks across workers. However, it is strongly preferred that engines do emit deterministic block identifiers, as this keeps the KvIndexer’s internal lookup table smaller and more efficient. To ensure deterministic behavior, all workers should use identical engine versions/configuration. If your engine relies on Python’s built-in `hash()`

for any event IDs, set `PYTHONHASHSEED=0`

; otherwise this setting has no effect.

### KVIndexer

The KVIndexer builds and maintains a global view of cached blocks in a prefix tree. We modify the original prefix tree by also storing the worker id on each node. This is so we can return the number of matched blocks for each worker.

The KVIndexer has a method `find_matches_for_request`

, which takes in tokens and returns a dictionary with keys of worker id and values of the number of matched KV Blocks.

The KVIndexer supports two backend implementations, selected via `--router-event-threads`

:

-
**Single-threaded RadixTree**(`--router-event-threads 1`

): Events are processed in a dedicated single-threaded tokio runtime via channel-based dispatch. Also supports TTL-based expiration for`--no-router-kv-events`

approximate mode. -
**ConcurrentRadixTree**(default,`--router-event-threads N`

where N > 1): A thread-safe radix tree with a pool of N worker threads for event processing and approximate routing-decision writes (default: 4). Uses sticky worker routing (events or synthetic approximate writes for the same worker always go to the same thread) to ensure per-worker serialization. Read operations (`find_matches`

) execute concurrently with writes.

### Inter-Router Communication

In distributed deployments with multiple routers, each router maintains visibility over only a portion of the total requests. To ensure consistent routing decisions, routers synchronize their states through three event types:

-
**AddRequest**: Notifies other routers when a request is assigned to a worker. Includes request ID, worker ID, token sequence blocks, and overlap score to track block usage across the system. -
**MarkPrefillCompleted**: Signals when a request moves from prefill to decode phase, allowing routers to update their worker load calculations by excluding completed prefill tokens. -
**Free**: Indicates request completion and resource release, enabling accurate block reference counting across all routers.

Each event carries a unique router ID to prevent self-event processing. This asynchronous communication system ensures optimal routing decisions by maintaining consistent KV cache state across all routers, even as they handle different request streams.

## Event Transport Modes

The router supports two event transport modes for KV cache state synchronization:

-
**NATS Core / Event Plane with Local Indexer (default)**: Fire-and-forget pub/sub where workers maintain local radix trees (enabled by default). Router rebuilds state by querying workers on startup. Lower latency, simpler setup. Works with both NATS Core and ZMQ event planes. -
**JetStream**(`--durable-kv-events`

on**both**frontend**and**workers): Persistent event stream with durable consumers. State persists across router restarts via snapshots in NATS object store. Best for production with multi-replica consistency.**Important:**Both the frontend and all workers must specify`--durable-kv-events`

for JetStream mode to work correctly.

### JetStream Mode (Opt-in)

KV events are sent to a persistent NATS JetStream. Each KV router/indexer replica acts as a durable consumer, pulling messages from this shared stream. This architecture ensures consistency across router replicas and persistence across restarts.

**Best for**: Production deployments requiring durability and multi-replica router consistency**Tradeoffs**: Requires JetStream setup; slightly higher latency due to persistence guarantees**Enable with**:`--durable-kv-events`

flag on**both**the frontend**and**all workers

**Both frontend and workers must specify --durable-kv-events** for JetStream mode to work correctly. The frontend uses this flag to consume from JetStream, while workers use it to publish to JetStream instead of the local indexer.

### NATS Core / Event Plane with Local Indexer (Default)

By default, workers have local indexer enabled. Each worker maintains its own local radix tree (local indexer) and publishes events over the generic event plane (NATS Core or ZMQ, depending on `--event-plane`

). Each worker assigns monotonically increasing event IDs to its events. The router detects gaps in event sequences and recovers missed events by querying the worker’s local indexer directly.

**Best for**: Lower-latency setups; simpler deployments without JetStream; single-router scenarios; deployments without NATS (using ZMQ event plane)**Tradeoffs**: State persists on workers (not centralized); recovery depends on workers being available**Switch to JetStream**: Use`--durable-kv-events`

flag on**both**workers (SGLang, TRT-LLM, vLLM, mocker)**and**frontend

**How gap detection works:**

- Each worker assigns monotonically increasing event IDs starting from 0
- The router tracks the last received event ID per worker
- If an event arrives with
`event_id > last_id + 1`

, the router detects a gap - The router queries the worker’s local indexer for the missing event range
`[last_id+1, event_id-1]`

- On worker discovery (Added event), the router dumps the worker’s entire local indexer state

**Startup behavior:**

- When a worker is discovered, the router queries and ingests its full local indexer state
- When a worker is removed, the router removes all its blocks from the global radix tree

By default, all workers have `enable_local_indexer=true`

, so the router uses NATS Core / Event Plane mode with local indexer. To use JetStream mode instead, specify `--durable-kv-events`

on **both** the frontend and all workers.

### Local Active Block Management with Replica Sync

In addition to cached blocks, each router replica needs to track active blocks (blocks being used for ongoing generation) as load metrics. Since this information is highly time-sensitive, it should be predicted immediately when:

- The router receives and routes a request
- The first token is generated (prefill complete)
- The response ends (request freed)

This is managed locally in each router via a “slot manager”. To maintain consistency across the system, router replicas synchronize these local predictions with each other through NATS core messaging.

This dual-layer approach—persistent global KV cache state via JetStream and ephemeral active block synchronization via router replicas—enables the system to make optimal routing decisions that balance cache reuse with load distribution.

## See Also

: Quick start guide for the KV Router[Router README](https://docs.nvidia.com/dynamo/v1.2.1/components/router): Router flags, tuning, and production setup[Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.2.1/components/router/configuration-and-tuning): Python API usage and custom routing patterns[Router Examples](https://docs.nvidia.com/dynamo/v1.2.1/components/router/router-examples): Integrate custom inference engines with KV-aware routing[KV Event Publishing for Custom Engines](https://docs.nvidia.com/dynamo/v1.2.1/integrations/kv-cache-integrations/kv-events-for-custom-engines)