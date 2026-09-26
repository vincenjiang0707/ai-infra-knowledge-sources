source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.0/blog/flash-indexer
lastmod: 2026-09-23T23:30:39.914Z

Flash Indexer: A Story of Inter-Galactic KV Routing


Flash Indexer: A Story of Inter-Galactic KV Routing

The **Flash Indexer** is a concurrent global index of every cached KV block across every inference worker, sustaining over **100 million operations per second**. It evolved through six iterations—from a Python dictionary to a jump-optimized spatial index—to the point where network latency, tokenization, and hashing are the bottlenecks. We’re shipping it as the default indexer in Dynamo v1.0.0.

For scale intuition: at 100M+ index ops/sec, the system can support approximately concurrent workloads, where is the workload’s sustained index ops/sec (inserts + lookups) under real traffic, including bursty prefill, well beyond current planetary-scale inference demand.

This post walks through those iterations—how each redesign drove a new order-of-magnitude improvement, and the specific data structure or concurrency breakthrough behind it.

## 1. Background

### 1.1 KV Block Identity

Every cached block carries three identifiers:

-
**Local block hash**(`u64`

): Content hash of the tokens within a single block. Position-independent—two blocks with the same tokens produce the same hash. Both the frontend and publisher use the same algorithm. -
**Sequence block hash**(`u64`

): Rolling hash of the entire prefix up to this block. Position-dependent—identical tokens at different positions produce different hashes.

**Worker ID**: Which worker holds the block.

Local hashes are deliberately *chunk hashes* (no prefix context) so frontends can hash query blocks cheaply in parallel. The tradeoff: chunk hashes can’t distinguish position. *“Predict the next token | Learn from the error | Predict the next token.”* produces identical hashes at blocks 0 and 2. This collision problem drives every data structure decision below.

### 1.2 Events and Requests

The indexer handles two kinds of traffic:

**KV Events** (writes): A publisher sitting alongside each engine emits `Store(worker_id, local_hash, seq_hash)`

when a block is cached and `Remove(worker_id, seq_hash)`

when evicted. We need explicit events because engines cache blocks beyond request lifetime and their eviction policies (LRU sweeps, memory pressure, preemption) are opaque—there’s no way to infer cache state from request-response cycles alone. The stream is bursty: prefills produce dozens of stores at once; eviction sweeps produce bursts of removes.

**Requests** (reads): On every inference request, the frontend sends a sequence of chunk hashes `[local_hash_0, ..., local_hash_D]`

. The indexer returns `(worker_id, match_depth)`

scores so the router can pick the worker with the deepest cached prefix.

Both paths are hot. Slow events mean stale routing decisions. Slow queries to the indexer means user-facing latency. The design goal: keep both fast without mutual contention.

## 2. Nested Dictionary → Rust Actor

### 2.1 Python Dictionary

The simplest possible index is a nested dictionary. For each worker, store a mapping from local block hash to the set of external sequence hashes that share that chunk hash. Since local hashes are chunk hashes, the same tokens can appear at different positions in different sequences, and a single local hash can map to multiple sequence hashes on the same worker. To find matches, iterate every worker and walk through the query sequence, checking for hits.

There is a correctness issue with this approach. `local_hash in blocks`

tells us the worker has *some* block with those tokens, but not *which* one—different sequences sharing the same chunk hash are conflated. This collision problem shapes every data structure decision that follows. This is `O(W × D)`

per query (W workers, D query depth).

With hundreds of workers and sequences thousands of blocks long, it’s a non-starter.

### 2.2 Rust Actor

Porting to Rust (`HashMap<WorkerId, HashMap<LocalHash, HashSet<ExternalHash>>>`

) eliminates interpreter overhead. A **single-threaded actor** owns the index exclusively and communicates through channels—correct and lock-free, but serializes all reads behind all writes. The single thread is the throughput ceiling.

## 3. Inverted Index

`worker -> { hash -> ... }`

forces `find_matches`

to iterate every worker. But the question is *“which workers have this block?”*—keyed by block, not worker. Instead of iterating workers and checking blocks, build a forward index keyed by LocalHash that maps to the sequence hashes and their worker sets.

Now `find_matches`

traverses the query once. At each position, take the union of worker sets. Workers only *drop out* as you go deeper—each is drained at most once—giving **O(D + W)** instead of O(W × D).

The inverted index is a major win for reads, but every data structure choice is a two-sided tradeoff between query performance and update cost.

On the read side, the collision issue from Section 2.1 resurfaces in a different shape. When we union worker sets across sequence hashes at a given local hash, we conflate workers that cached different sequences sharing the same chunk. The seq hash data is in the index, but `find_matches`

cannot use it without computing the query’s own seq hashes—which reintroduces rolling hash computation on the read path, exactly what chunk hashes were designed to avoid.

On the write side, removes are equally expensive: without a per-worker reverse lookup, removing a block by seq hash requires scanning the entire index. We could add a reverse lookup table, but that’s more bookkeeping on every store.

The radix tree resolves both.

## 4. Radix Tree

Each node has a small children map keyed by `LocalHash`

, plus a worker set. Parent-child relationships scope collision risk: two blocks with the same chunk hash collide only if they share the same parent, which means the same prefix. Different prefixes lead to different parents. This requires one new field in KV events: the **parent hash**, so the tree can link child to parent as events arrive.

Each node also carries a sequence hash. A per-worker **lookup table** (`worker -> { seq_hash -> node }`

) provides O(1) access for event processing: stores attach children via the parent’s seq hash; removes find the node directly. Two keys for two access patterns—local hash for traversal, sequence hash for events.

Both the tree and the lookup table point to the same nodes via `Rc<RefCell<T>>`

(shared ownership with interior mutability, single-threaded). The children maps at each node are small—bounded by branching factor, not total block count.

This approach remains single-threaded behind the actor, with serialized reads and writes.

## 5. Concurrent Radix Tree

Reads don’t conflict with each other. We replace `Rc<RefCell<T>>`

with `Arc<RwLock<T>>`

(atomic reference counting + reader-writer lock). Now `find_matches`

acquires only read locks and executes *inline on the caller’s thread*—no channel, no actor, no queue.

Writes use **sticky routing**: a `ThreadPoolIndexer`

deterministically assigns each `WorkerId`

to one thread. Events for the same worker always land on the same thread, so there’s no write-write contention on any worker’s subtree.

`DashMap`

shards the outer map so reads and writes to different workers don’t touch the same lock. `parking_lot::RwLock`

avoids the OS syscall on uncontended paths (2–3x faster than `std::sync::RwLock`

). `FxHashMap`

replaces SipHash with a single multiply-xor step—safe here because keys are `u64`

hashes, not user input.

`parking_lot::RwLock`

is task-fair by default: it processes waiters in arrival order rather than unconditionally favoring readers or writers. Combined with sticky routing’s guarantee that each worker’s writes are serialized on a single thread, write contention is minimal and neither reads nor writes are starved.

The actor is gone for reads. Multiple `find_matches`

calls proceed concurrently with writes to different workers.

## 6. Positional Indexer with Jump Search

The radix tree traverses node-by-node, following pointers from parent to child—cache-hostile and fundamentally sequential. You can’t check position 128 without visiting 0 through 127.

Replace the tree with a `Vec<DashMap<LocalHash, SeqEntry>>`

indexed by position. `index[position]`

is a concurrent map from local hash to sequence entry. Any position is O(1)—no traversal required.

The `SeqEntry`

enum handles collisions: in the common case a `(position, local_hash)`

slot has exactly one sequence hash, stored inline without a `HashMap`

allocation. Only when multiple prefixes produce the same chunk hash at the same position does it upgrade to `Multi`

.

The `Single`

/`Multi`

split also enables lazy hash computation: when a lookup finds a `Single`

entry, the match is unambiguous without computing the query’s sequence hash. The expensive rolling hash is only needed on the rare `Multi`

entries where chunk hash collisions require disambiguation.

But the positional indexer’s biggest advantage isn’t the data layout – it’s what **random access makes possible.**

Random access enables **jump search**:

- Initialize the active worker set from position 0.
- Jump ahead by
`jump_size`

positions (e.g., 64) to the next checkpoint. - At the checkpoint, count how many active workers still match (cardinality check—no set cloning needed).
- If all match: the entire skipped range is confirmed. Continue jumping.
- If fewer match: some workers drained in the skipped range. Scan forward through positions
`[previous_checkpoint + 1 .. current_checkpoint]`

to find each lost worker’s exact drain point. - Resume jumping from the current checkpoint.

Best case: `D / J`

lookups instead of `D`

.

Worst case (workers drop at every jump): degrades to a linear scan with jump overhead.

The positional indexer wins on long sequences with high prefix sharing; the radix tree wins on short or highly-divergent sequences.

The `Vec`

layout also improves cache locality: early positions (shared system prompts, common preambles) are the hot path, cluster at the front of the array, and stay warm in cache.

With jump size *J* (= `jump_size`

, defaulting to 64), amortized cost drops to **O(D/J + W)**. Since *J* is a tunable constant, the complexity remains linear in *D*; the practical benefit is skipping the vast majority of positions when prefix sharing is high.

## 7. Benchmarks

All benchmarks run on a 24-core Arrow Lake (285K) desktop, replaying publicly-available [Mooncake production traces](https://github.com/kvcache-ai/Mooncake/tree/main/FAST25-release/arxiv-trace) through a mock engine with 16,384 GPU blocks and prefix caching enabled. The harness tests all five backends with 24 concurrent event-processing threads.

**Ops throughput** is the combined rate of KV events and `find_matches`

requests per second. We sweep offered load by compressing the same trace into shorter durations and compare achieved vs. offered throughput. The **threshold throughput** is where achieved throughput stops tracking offered—the indexer’s saturation point.

## 8. Future Directions

With the Flash Indexer shipping in Dynamo v1.0.0, the next round of optimizations targets the remaining constant factors:

**Binary search within jumps.**Replace the linear scan-back after a failed jump with binary search:`O(log J)`

instead of`O(J)`

per failed jump.**Hierarchical routing.**A sparse top-level indexer for coarse-grained prefix coverage across deployment groups, with full indexers at the leaves.**Inline bitsets for worker sets.**Replace`HashSet`

with fixed-width bitsets stored inline in each node, turning membership tests into single bit operations and eliminating pointer chases.

## 9. Conclusion

The journey from a Python dictionary to the Flash Indexer spans six iterations, each motivated by a concrete bottleneck in the previous design:

**Naive Nested Dict**— simple but O(W × D) per query.**Rust + Actor Pattern**— fast language, correct concurrency, but single-threaded bottleneck.**Inverted Index**— O(D + W) per query by flipping the key structure; secondary`seq_hash`

layer for chunk-hash collision safety.**Radix Tree**— tree structure replaces giant flat map; per-node children maps stay small; dual-key design (local hash for traversal, seq hash for event processing);`Rc<RefCell<>>`

for single-threaded shared ownership.**Concurrent Radix Tree**—`Arc<parking_lot::RwLock<>>`

replaces`Rc<RefCell<>>`

;`DashMap`

with per-worker inner`RwLock`

for the lookup table (shard-level locking for rare mutations, cheap shared reads on the hot path); reads bypass the actor entirely; sticky routing serializes writes per worker with zero contention.**Concurrent Positional Indexer via Jump Search (Flash Indexer)**— an alternative to the radix tree for long-sequence workloads;`Vec<DashMap<>>`

indexed by position replaces pointer chasing with O(1) random access, enabling jump search that skips most of the depth;`DashMap`

with per-worker inner`RwLock`

for the reverse lookup; hot prefix positions cluster at the front of the`Vec`

and stay warm in cache.

The result: a sustained ops throughput of **170 million operations per second**—events and requests combined—with achieved throughput tracking offered throughput all the way to the limit.