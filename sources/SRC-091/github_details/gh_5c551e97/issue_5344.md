# [Issue #5344] Batched L1 allocate failure commits a torn TP prefix; retrieve then silently returns corrupt KV

source: https://github.com/LMCache/LMCache/issues/5344
state: open | updated: 2026-09-27T03:45:03Z
labels: 

## 正文

## Bug Description

When a multi-rank (tensor-parallel) store cannot allocate L1 memory for every rank, LMCache commits a torn prefix and a later retrieve silently returns corrupt KV. There is no error on the retrieve path. The engine treats the tokens as a cache hit and decodes garbage (mixed-script salad, including U+FFFD).

This is not a bit flip, a GPU compute error, or a transport checksum failure. The bytes that were stored on the ranks that succeeded are fine. The corruption is that the logical chunk is published even though at least one TP shard was never written.

Related but different from #4247 (FlashInfer rank-4 layout). That bug is a view/shape mismatch. This one is an allocation failure that still commits the key.

## What happened

Setup: vLLM 0.28.0, LMCache 0.5.4rc5, `LMCacheMPConnector` `kv_both`, hybrid Mamba/GDN model, TP=4, `--chunk-size 1600`, L1 32 GiB, eviction watermark 0.72, eviction ratio 0.12. One chunk object is 56524800 bytes (53.9 MiB).

L1 usage was only 64-72% (about 10 GiB free). A single `batched_allocate` still failed because the reserve is all-or-nothing and larger than the headroom:

- watermark 0.72 leaves 9 GiB
- eviction runs once a second, only after the watermark, and only frees 12% (3.8 GiB)
- allocate does not wait for eviction or retry
- a 200-284 block reserve wants 10-15 GiB in one shot, so it fails while the usage log still says "not full"

`MemoryAllocator.batched_allocate` raises `RuntimeError` and does not touch the free list. `store()` is fail-closed **per rank**: the rank that loses the race skips the whole store and commits nothing. The ranks that already reserved memory log `Stored N tokens` and commit.

Observed in one millisecond window (4 ranks):

```
Stored 113600 tokens
Failed to batched allocate 71 memory blocks of size 56524800 (short by 12 blocks)
Stored 113600 tokens
Failed to batched allocate 71 memory blocks of size 56524800 (short by 12 blocks)
```

113600 = 71 chunks * 1600. Two ranks committed 71 chunks. Two ranks wrote nothing. Token bindings are published by worker 0 only (`MP_TOKENS`, "one report covers every rank's keys"). So the index says the prefix is present.

Nine minutes later a new request GPU-missed that prefix and retrieved it:

```
Prefetch request completed (L1+L2): 60/64 retained keys (60 L1, 0 L2)
Retrieved 24000 tokens
```

vLLM counted `cached_tokens=24000` (88.7% hit). All 4 ranks logged `Retrieved`. Decode collapsed (~29 tok/s, speculative acceptance ~0) and the output was byte salad, including U+FFFD, on the first generated token. Requests that stayed on the live GPU prefix (no retrieve) were unaffected. A later turn of the poisoned session kept salading with `external_prefix_cache_hits` delta 0, because the bad retrieve had been installed into that prefix's GPU blocks.

`retrieve()` does check `len(window_objs) != len(in_window_keys)` and logs `Some keys not found during retrieve!`. That check is per rank, against that rank's own storage. The rank that stored the shard finds its keys. The rank that skipped the store should miss, but the connector still reported a full token hit and every rank printed `Retrieved 24000 tokens`. The missing shard is therefore being treated as a successful load (empty, stale, or zero-filled), not as a miss that forces recompute.

## Expected behavior

If any rank cannot allocate a chunk, that chunk must be discarded on **every** rank. Do not publish the token binding. A later retrieve should miss those tokens and the engine should recompute them.

Silently committing a prefix that is missing a TP shard is a correctness bug, not a capacity miss. A capacity miss is safe (recompute). A torn commit is not.

Concretely:

1. Cross-rank agreement before commit. Worker 0 must not publish `MP_TOKENS` for a chunk unless every rank finished `finish_write` for that chunk.
2. On `batched_allocate` failure, drop the reserved objects on the ranks that succeeded (same fail-closed rule, but across ranks, not inside one process).
3. Optional: evict-and-retry inside allocate, or refuse a reserve larger than the watermark headroom up front. That avoids the failure. It is not a substitute for (1). The dangerous part is the torn commit, not the allocation failure itself.

## Why the headroom is too small

One chunk is 53.9 MiB. A long-prefix store/prefetch reserves every chunk in one `batched_allocate`. At watermark 0.72 a 32 GiB pool has 9 GiB free, and one eviction tick frees 3.8 GiB. A 284-block reserve needs ~15 GiB. So a long prefix store fails even though L1 is not full, and it fails independently per rank, which is what creates the tear.

## Environment

- LMCache 0.5.4rc5 (`lmcache_driven_transfer.py` store/retrieve, `memory_management.py` `batched_allocate`)
- vLLM 0.28.0, hybrid Mamba/GDN, TP=4, chunk 1600, `kv_both`
- L1 32 GiB, watermark 0.72, eviction ratio 0.12
- Failure signature: `Failed to batched allocate N memory blocks of size 56524800 because no enough memory is available (short by M blocks)` on a subset of ranks, followed by `Stored` on the others, then a later `Retrieved` of a block-aligned token count with no exception and corrupt output


## 评论 (4)

### Pilgrim132333333 · 2026-09-25

I would like work on this issue

### neevmodh · 2026-09-26

This is a precise and well-instrumented report — the headroom math (9 GiB free vs. ~15 GiB needed for a 284-block reserve at your chunk size) makes the failure mode very believable, and the distinction you draw between "the torn commit is the danger" vs. "the allocation failure is just what triggers it" is the right framing.

I looked at `_publish_token_bindings` (`lmcache_driven_transfer.py:1029`) to sanity-check the "independent per-rank" claim — the docstring itself confirms the store-submission and write-finished events are per-worker, with no cross-rank barrier visible in that path, which is consistent with what you're seeing (one rank publishing `MP_TOKENS` while a sibling rank's `batched_allocate` for the same chunk fails).

That said, a real fix for (1) — cross-rank agreement before a worker publishes `MP_TOKENS` — means introducing a barrier or two-phase-commit across TP ranks that doesn't exist today, and I don't have a TP=4 hybrid Mamba/GDN setup to validate a fix against without risking shipping something that looks right in isolation but doesn't actually close the tear under load (or introduces a new stall if a rank never reports back). Given this is a correctness bug in the cross-rank commit protocol rather than a single-process logic error, I think this one specifically needs a maintainer who owns the MP transfer path to weigh in on where the barrier belongs before anyone sends a PR - happy to help implement or review once that's scoped, and (3) (refuse a reserve above watermark headroom) looks like a safe, independent mitigation that could land on its own in the meantime if that's of interest.


### Pilgrim132333333 · 2026-09-27

@neevmodh Hi, I have submitted a PR #5349. This PR has not address cross_rank agreement, but it makes each TP rank fail closed by detecting L1 allocation failures and rolling back locally staged objects instead of publishing a partial per-rank store. Can I get a review on it? Also, I'd also be happy to discuss and contribute to the follow-up work

### neevmodh · 2026-09-27

Reviewed #5349's diff. What it does: `reserve_write_with_status` now returns each key's `L1Error` instead of collapsing to just the successful keys, so the multiprocess store path can tell OOM apart from an intentionally-skipped key. In `lmcache_driven_transfer.store()`, if any key in a later object group hits `OUT_OF_MEMORY`, it raises, and the existing except path now calls the new `abort_write` on everything staged so far in `all_dict` — so a rank that partially reserved earlier groups before a later group OOMs no longer leaves those staged objects dangling or eligible to leak into a commit.

That's a real, correctly-scoped fix for the *local* half of the bug — a single rank no longer ends up in an inconsistent staged state after a partial OOM. But to be clear about what it doesn't touch, since scope matters here: the actual torn-commit path in the report is two ranks succeeding and two failing on the *same* chunk, and worker 0 still publishing `MP_TOKENS` regardless of sibling rank outcomes — this PR doesn't add any cross-rank check before that publish, which matches what @Pilgrim132333333 already said in the PR description. So after #5349 merges, the specific repro in this issue (some ranks store, worker 0 publishes anyway, retrieve returns torn KV) is still open — item 1 (cross-rank agreement before `MP_TOKENS` publish) remains the real fix and still needs a maintainer to scope where that barrier belongs.

Tests look right for what's being claimed (`test_abort_write_discards_staging_object`, `test_store_aborts_prior_reservations_after_later_group_oom`) — they verify local rollback, not cross-rank behavior, which is consistent with the PR's stated scope.

Net: looks safe to merge as an incremental, honestly-scoped improvement, but it should probably say explicitly in the PR/issue that it does not close this issue on its own.
