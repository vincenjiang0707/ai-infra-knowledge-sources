# [Issue #5350] L1 eviction races async L2 store: chunks discarded before offload are never stored (persistent re-prefill under L1 pressure)

source: https://github.com/LMCache/LMCache/issues/5350
state: open | updated: 2026-09-26T16:08:32Z
labels: 

## 正文

**Label**
Bug

**Describe the bug**
In LMCache v0.5.5 (MP mode), under L1 (CPU) memory pressure, freshly-computed KV chunks can be evicted from L1 before the asynchronous store controller offloads them to L2, so they are silently dropped and never written to L2 — even when L2 is large enough to hold the entire working set and has no eviction configured.

The result: with a shared-prefix (prefix-caching-style) workload, ~19% of requests permanently retrieve only the shared prefix (first half of the prompt) and re-prefill the unique tail on every recurrence, indefinitely. The half-hits persist through the whole run, not just warmup.

Root cause (confirmed in v0.5.5 source):

L1 eviction destination defaults to EvictionDestination.DISCARD — L1 eviction does not offload to L2 (lru.py, eviction_controller.py:193).
The StoreController offloads L1→L2 by reserve_read-ing keys received from an L1_WRITE_FINISHED notification. If a key was already discard-evicted in the meantime, reserve_read returns KEY_NOT_EXIST, the key is silently skipped from the store (only surfaced as an L1_READ_FAILED / lmcache_mp.l1_read_failure "not_found" anomaly), and it never reaches L2 (lmcache/v1/distributed/storage_controllers/store_controller.py:600-627).
So there is a race between L1 DISCARD eviction and the async L2 offload; the loser is silently never stored.

**To Reproduce**
Environment: LMCache v0.5.5, MP mode, L1 + L2 where L2 is sized to hold the full working set and has no L2 eviction, and L1 is smaller than the shared-prefix working set.

Start the LMCache MP server with a small L1 and one large L2 adapter (e.g. S3/filesystem), no L2 eviction:
lmcache server --host 0.0.0.0 --port 6555 --chunk-size 256 \
  --l1-size-gb 60 --eviction-policy LRU \
  --l2-adapter '{"type":"s3", ... ,"max_capacity_gb":500}'

Start vLLM with LMCacheMPConnector (kv_role: kv_both), --no-enable-prefix-caching --enforce-eager.
Run a shared-prefix benchmark whose prefix pool exceeds L1. With aiperf/genai-perf
--prefix-prompt-length 4096 --num-prefix-prompts 150 \
--isl 4096 --osl 100 --num-dataset-entries 200 \
--concurrency 10 --random-seed 42 --benchmark-duration 1200

Here 150 prefixes × 4096 tokens ≈ 75 GB of prefix KV > 60 GB L1. Each request = 8192 tokens (4096 shared prefix + 4096 unique tail).

Grep the server log for Retrieved N tokens.

Observed — persistent prefix-only half-hits throughout the run (not just warmup)
Half-hits occur at ~20–32/min even in steady state, long after every one of the 200 fixed prompts has been served many times. Since retrieval is a contiguous match from token 0, Retrieved 4096 means "prefix found, tail missing → prefill." (Optionally, lmcache_mp.l1_read_failure / L1_READ_FAILED "not_found" events fire in the same window.)

Control: setting --num-prefix-prompts 10 (prefix pool now fits in L1) eliminates the half-hits — all requests become full 8192-token hits. So the trigger is specifically L1 < shared-prefix pool.

**Expected behavior**
Once a chunk is computed and admitted to L1, it should reliably be offloaded to L2 and remain retrievable regardless of L1 pressure. A chunk should not be silently dropped from the L2 store just because it was evicted from L1 before the async offload read it. Subsequent requests for the same prompt should be full L2 hits, not re-prefills, when L2 has capacity and no eviction.

**Screenshots**
N/A (server-side KV-cache behavior; log evidence included above).

**Desktop (please complete the following information):**
OS: Linux
LMCache: v0.5.5
vLLM: 0.26.0
PyTorch: 2.11.0+cu130
Python: 3.12.3
GPU: NVIDIA L40S
Mode: MP (LMCacheMPConnector, kv_role: kv_both), --chunk-size 256, --l1-size-gb 60, L2 sized to hold full working set with no L2 eviction

**Smartphone (please complete the following information):**
N/A (not a mobile/browser issue)

**Additional context**
Add any other context about the problem here.


## 评论 (4)

### neevmodh · 2026-09-26

Traced this down to confirm the exact mechanism — the analysis in the issue is right, and I can pin down precisely where the race window is.

`L1Manager.is_key_evictable` (`l1_manager.py:894`) treats a key as evictable whenever it has "a resident object that is not read-locked." The store controller's L2 offload protects a key from eviction *only once* its `reserve_read` call actually succeeds and takes the read lock. But there's a real gap between "L1 write finished, key is resident" (when the key becomes evictable) and "store controller gets around to calling `reserve_read` for it" (when it becomes protected) — and nothing marks a key as "queued for L2 offload but not yet reserved" during that gap. A DISCARD eviction that lands in that window removes the key before it's ever locked, so `reserve_read` later returns `KEY_NOT_EXIST` exactly as you found in `store_controller.py:600-627`.

So the fix shape I'd propose: extend `is_key_evictable`'s eligibility check with a lightweight "pending L2 offload" marker — set synchronously the moment a key is handed to the store controller for offload (before eviction can observe it as unlocked-and-evictable), cleared on `reserve_read` success (the read lock takes over as the real protection) *or* on definitive offload failure/give-up (so a key that will never be offloaded doesn't become permanently unevictable).

I traced this far with static analysis and I'm confident in the diagnosis, but I don't want to ship a fix for a live data-loss race in the L1/L2 admission path without exercising it under the actual MP + real L2 adapter timing this needs — a marker that's set/cleared at the wrong point could just move the race rather than close it, or introduce a new stuck-key leak on the failure path. If a maintainer can confirm this fix shape (or point at the intended synchronization primitive for this class of "in-flight but not yet locked" state), I'm glad to implement and validate it against the repro in this issue.


### malikoyv · 2026-09-26

Thanks @neevmodh for the diagnosis - it matches what I see. I have a deterministic reproduction on current dev (write keys, evict via is_key_evictable + delete before the store loop runs and keys never reach L2) and a fix along the lines you proposed: the write-back mark is taken inside finish_write's critical section, so there is no window. It's a separate TTL lock checked only by is_key_evictable, so explicit delete() and post-store L1 deletions are unchanged, and a leaked mark expires with the read TTL. Opened a PR with the fix

### neevmodh · 2026-09-26

Glad it lines up — taking the hold inside `finish_write`'s critical section is cleaner than what I sketched, since it closes the gap at the source instead of patching around it. I can pull #5369 and run it against the shared-prefix repro from this issue (L1 < prefix pool) to confirm the half-hits go away, if that's useful before merge.

### neevmodh · 2026-09-26

Verified locally against #5369 (CPU-only, no GPU/vLLM needed):

- On `dev` (unpatched), copying the PR's new `test_l1_write_back_hold.py` in and running it fails exactly as expected: `test_key_evicted_before_store_loop_runs_still_reaches_l2` throws `AssertionError: keys evicted before the store loop ran never reached L2` — this reproduces the race directly (key evicted via `is_key_evictable` + `delete()` before the store loop runs, chunk never reaches L2).
- On #5369's branch, the full `test_l1_write_back_hold.py` suite passes 7/7, including that regression test and the leak-on-stop / explicit-delete cases.

So the write-back hold closes the window cleanly without regressing explicit deletes or leaking holds on stop. Looks good to merge from my side.
