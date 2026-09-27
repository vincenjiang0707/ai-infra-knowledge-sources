# [Issue #4137] Resident CPU-tier prefix cache entry spuriously measures as a full miss under concurrent write load (not explained by capacity or same-key contention)

source: https://github.com/LMCache/LMCache/issues/4137
state: open | updated: 2026-09-17T01:47:54Z
labels: 

## 正文

## Summary

With `LMCacheConnectorV1` (local CPU backend) serving concurrent requests, a prefix that is confirmed resident (freshly warmed immediately before measurement) still frequently returns full-recompute-level TTFT if any other request is concurrently writing a different prefix to the CPU tier, even with generous capacity headroom and no contention on the same key.

## Environment

- lmcache==0.3.12, vllm==0.13.0
- `vllm serve <model> --enable-prefix-caching --kv-transfer-config '{"kv_connector": "LMCacheConnectorV1", "kv_role": "kv_both"}'`
- `LMCACHE_LOCAL_CPU=True`, `LMCACHE_MAX_LOCAL_CPU_SIZE=20` (GiB), `LMCACHE_CHUNK_SIZE=256`
- Single RTX 4090, single vLLM server process, `ThreadPoolExecutor`-dispatched HTTP client (4 workers)
- Prefix length: 28,000 real tokens (Qwen2.5-0.5B-Instruct)

## Reproduction

1. Maintain a small pool of 2 "resident" prefixes, each re-warmed with a `max_tokens=2` request immediately before I measure it.
2. Interleave concurrent "miss" requests: brand-new, globally-unique 28K-token prefixes, never reused.
3. Dispatch both kinds concurrently (Poisson arrivals, 4 worker threads, hit_ratio≈0.5) against the same server.
4. Measure TTFT for each "hit"-kind request (the one just re-warmed) and compare against the known hit/miss TTFT distributions from isolated, sequential measurement on the same hardware/model (clean, non-overlapping: hit max 95.9ms, miss min 395.7ms).

## Result

At n=150 (66 realized "hit" draws), 80.3% of hit-kind requests measured miss-level TTFT (>150ms; observed range 850-2400ms). I tested and ruled out three candidate causes:

- **Capacity**: raising `LMCACHE_MAX_LOCAL_CPU_SIZE` from 6 to 20 GiB didn't reduce the failure rate. Each request's KV footprint at this prefix length is ~343MB (12,288 bytes/token × ~27,890 real tokens); even 4 concurrent workers plus both resident identities live at once, doubled for margin, is only ~4.1GB, well under the 20GiB cap.
- **Same-key contention**: I instrumented whether another request was concurrently warming/measuring the same resident identity (`same_identity_concurrent`). No significant relationship with failure (Mann-Whitney U, p=0.072), and the trend runs the wrong direction for a same-key-race explanation (failed rows: mean 0.34 concurrent same-key accessors; ok rows: mean 0.62).
- **Sequential timing race**: repeating the exact warm-then-measure pattern 30 times fully sequentially (zero concurrency, zero other traffic) produced 0/30 failures, ruling out an intrinsic async-write-vs-read race independent of concurrency.

What does predict failure: whether any miss request (to an unrelated key) is concurrently in flight during the hit's own measurement window (`concurrent_miss_count`):

| | ok | failed | failure rate |
|---|---:|---:|---:|
| `concurrent_miss_count == 0` | 12 | 8 | 40.0% |
| `concurrent_miss_count >= 1` | 1 | 45 | 97.8% |

Fisher's exact test: odds ratio 67.5, p = 2.9e-7.

The residual 40% failure rate at `concurrent_miss_count == 0` is plausibly a measurement-granularity artifact: the counter is sampled once, immediately before the hit's final request is issued, so a miss that begins microseconds later isn't captured. I haven't confirmed this.

## Root cause

I believe this is a request-scoping bug, not a dict-corruption or capacity issue. In `lmcache/v1/storage_backend/local_cpu_backend.py` (v0.3.12), `LocalCPUBackend` keeps a single, instance-level list of looked-up keys, and its own comment documents an assumption this violates under concurrency:

```python
# to help maintain suffix -> prefix order in the dict
# assumption: only one request is looked up at a time
# (only one worker per cache engine)
self.keys_in_request: List[CacheEngineKey] = []

def contains(self, key, pin=False):
    with self.cpu_lock:
        if key not in self.hot_cache:
            return False
        if pin:
            self.hot_cache[key].pin()
            self.keys_in_request.append(key)   # shared across ALL requests
        return True

def touch_cache(self):
    with self.cpu_lock:
        for key in reversed(self.keys_in_request):
            self.cache_policy.update_on_hit(key, self.hot_cache)
        self.keys_in_request = []              # clears the WHOLE shared list
```

The same pattern recurs in `batched_async_contains` (same file, ~line 211-228), which is on the actual request-serving hot path.

`self.cpu_lock` correctly serializes raw `hot_cache` dict access, so `contains()`/`get_blocking()` should still find a resident key's entry. The corruption is in the eviction bookkeeping: one request's `touch_cache()` can clear another request's just-appended keys before that second request records its own `cache_policy.update_on_hit()` call, silently dropping the "this key was just touched" signal for an unrelated, already-resident key. That makes the key look stale to the eviction policy regardless of how much raw capacity is available, which matches what I saw in the Capacity test above: the failure rate didn't move because the cause was never capacity.

Tracing the caller in `storage_manager.py`: `StorageManager` runs a single dedicated background thread with its own asyncio event loop, and `async_lookup_and_prefetch()` (which awaits `batched_async_contains()`) runs on that loop. So all concurrent requests' lookups execute as interleaved coroutines on a single OS thread, not on separate threads. A `threading.local()` fix wouldn't be enough here since every request shares one thread; a correct fix likely needs per-task scoping (`contextvars.ContextVar`) or explicit per-request key-list threading through the call chain, spanning at least `local_cpu_backend.py` and `storage_manager.py`. `touch_cache()` is also called from `cache_engine.py`, which I haven't inspected yet.

This file has no async device-copy code (no `.to(device, non_blocking=True)`, no CUDA streams/events), so as far as I can tell this is a pure Python scoping bug in LMCache's own request handling, not an upstream PyTorch/CUDA issue.

Happy to share the instrumented repro script if useful.

## 评论 (3)

### vedjaw · 2026-07-17

Taking a look at this — planning to scope `keys_in_request` per asyncio task / request via `contextvars.ContextVar` in `LocalCPUBackend` and `LocalDiskBackend`, and ensure the async lookup path also calls `touch_cache()` when `pin=True` so concurrent lookups can't wipe each other's LRU hit updates.

### github-actions[bot] · 2026-09-16

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### PushpakAg · 2026-09-16

It sounds like the issue might be related to how concurrent writes are affecting the cache's behavior, even with sufficient capacity and no same-key contention. Have you considered whether the cache eviction policy or locking mechanism during concurrent writes could be influencing the results?

