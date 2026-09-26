source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache/
lastmod: 2026-09-24

#

`vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache)

EmbeddingCache — named-entry block cache with FIFO eviction.

Manages a fixed pool of block IDs keyed by content identity (mm_hash). Entries transition through: not-ready → ready (evictable) → pinned. Eviction targets ready + unpinned entries in FIFO order.

All public methods are thread-safe.

Classes:

-
–[CacheEntry](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.CacheEntry)A single cache entry. Read

`.block_ids`

and`.ready`

freely; -
–[EmbeddingCache](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache)Fixed-size block cache with FIFO eviction.


##

`CacheEntry`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.CacheEntry)

A single cache entry. Read `.block_ids`

and `.ready`

freely; mutations only through EmbeddingCache methods.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


##

`EmbeddingCache`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache)

Fixed-size block cache with FIFO eviction.

Entries are keyed by content identity (e.g. mm_hash). Blocks are allocated from a free-set; when space is needed, ready + unpinned entries are evicted oldest-first.

The caller is responsible for deciding *when* to call `mark_ready`

(e.g. after enough engine steps have elapsed for the worker to have completed the write).

Methods:

-
–[alloc](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.alloc)Allocate

*n_blocks*for*key*, evicting as needed. -
–[discard](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.discard)Remove a not-ready in-flight entry, returning its blocks to the pool.

-
–[get](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.get)Return the entry for

*key*, or None if not present. -
–[has_held_entries](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.has_held_entries)True if any entry is not-ready or pinned (an in-flight transfer).

-
–[mark_ready](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.mark_ready)Mark an entry as ready (data is CPU-visible).

-
–[pin](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.pin)Pin an entry (prevent eviction).

-
–[pin_if_ready](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.pin_if_ready)Atomically pin

*key*if present and ready; return its entry. -
–[unpin](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.unpin)Unpin an entry. Asserts currently pinned.


## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


|
|

###

`_evict_until(n_blocks)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache._evict_until)

Evict ready+unpinned entries FIFO until enough space. Lock held.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


###

`alloc(key, n_blocks)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.alloc)

Allocate *n_blocks* for *key*, evicting as needed.

The entry starts not-ready. Returns None if there is not enough space even after evicting all evictable entries.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


###

`discard(key)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.discard)

Remove a not-ready in-flight entry, returning its blocks to the pool.

Used when an in-flight fill (e.g. a NIXL READ) fails before the entry is marked ready. Asserts the entry is present and not ready — ready or pinned entries are reclaimed through eviction/unpin, not discard.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


###

`get(key)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.get)

Return the entry for *key*, or None if not present.

###

`has_held_entries()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.has_held_entries)

True if any entry is not-ready or pinned (an in-flight transfer).

Held entries are exactly those absent from the eviction free list, so they represent saves awaiting mark_ready or loads awaiting unpin.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


###

`mark_ready(key)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.mark_ready)

Mark an entry as ready (data is CPU-visible).

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


###

`pin(key)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.pin)

Pin an entry (prevent eviction).

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


###

`pin_if_ready(key)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.pin_if_ready)

Atomically pin *key* if present and ready; return its entry.

Returns None when the key is absent. An entry returned with `ready`

False was not pinned: its save is still in flight, which the producer reports differently from a miss because such a read can be retried.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/scheduler/embedding_cache.py`


###

`unpin(key)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler.embedding_cache.EmbeddingCache.unpin)

Unpin an entry. Asserts currently pinned.