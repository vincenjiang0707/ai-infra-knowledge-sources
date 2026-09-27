# [Issue #5339] MP mode: remaining unbounded request-state retention in vLLM client and sidecar prefetch bookkeeping

source: https://github.com/LMCache/LMCache/issues/5339
state: open | updated: 2026-09-26T10:57:55Z
labels: 

## 正文

## Deployment

We run a production **3P1D** deployment with vLLM and `LMCacheMPConnector`. Each serving node has a per-node LMCache sidecar; LMCache uses `fs_native` as the L2 adapter backed by local SSD. P2P, CacheBlend, and engine-driven transfer are not enabled.

The previous client-side MQ no-response leak is tracked separately in #5270. During a follow-up audit of upstream `dev` (checked at `05fc77a`, 2026-09-24), we found the two request-state retention paths below. This issue only reports the observed behavior and asks maintainers to determine the intended lifecycle and remediation.

## 1. vLLM client: `_returned_finished` grows for the worker lifetime

`LMCacheMPWorkerAdapter` creates:

```python
self._returned_finished: set[str] = set()
```

`_process_finished_stores()` uses this set to prevent a request ID from being reported repeatedly through `finished_sending`, then records returned IDs with:

```python
self._returned_finished.update(ret_stores)
```

We could not find a `discard`, `clear`, TTL, or capacity-based removal path. Therefore every request ID once returned as `finished_sending` remains resident until the vLLM worker exits. This path is exercised by normal successful requests as well as failure paths.

The set appears to be needed for async-scheduling deduplication after neighboring tracking sets are drained, but it also produces monotonic process-lifetime growth. With UUID-like Python request IDs, the retained footprint is roughly 150-200 bytes per request before allocator overhead; at sustained high QPS this can become material in a long-lived worker.

Relevant code:
- `lmcache/integration/vllm/vllm_multi_process_adapter.py` (`_returned_finished`, `_process_finished_stores`)

### Questions for maintainers

1. Is process-lifetime retention of every completed `finished_sending` request ID required by the vLLM connector contract?
2. What lifecycle or retention semantics should this deduplication state have in a long-running worker?

## 2. sidecar: abandoned prefetch jobs and completion Bitmaps are never reclaimed

`LookupModule` registers every lookup in:

```python
self._prefetch_jobs: dict[str, _PrefetchJob] = {}
```

The job is removed when `QUERY_PREFETCH_STATUS` or `WAIT_PREFETCH_STATUS` obtains a non-`None` completion result. If a client aborts or disconnects after LOOKUP, or stops polling after an RPC timeout/unhealthy transition, the job is not consumed by that path.

The corresponding `PrefetchController` completion state has the same consumer-driven ownership:

```python
self._completed_lookups: dict[PrefetchRequestId, int] = {}
self._completed_results: dict[PrefetchRequestId, Bitmap] = {}
```

`query_prefetch_result()` pops both the Bitmap and the lookup result. The source comment notes that failing to consume the prefetch result leaks memory. `Bitmap` is native/C++ memory, so its growth may not be visible in Python GC or tracemalloc. `END_SESSION` removes the session and touches L1 keys but does not remove the prefetch job or controller completion state.

In production we also see frequent `Session ... not found, skipping touch` warnings (roughly 378-953 over two hours), consistent with request-lifecycle skew and making normal client polling an unreliable sole ownership mechanism.

Relevant code:
- `lmcache/v1/multiprocess/modules/lookup.py` (`_prefetch_jobs`, `query_prefetch_status`, `end_session`)
- `lmcache/v1/distributed/storage_controllers/prefetch_controller.py` (`_completed_lookups`, `_completed_results`, `query_prefetch_result`)

### Questions for maintainers

1. What is the intended owner of a prefetch job and its completion result after the original client has abandoned the request?
2. Is there an existing cancellation or reclamation lifecycle that this MP path should use?
3. What cleanup ordering is required for an in-flight prefetch so that late completion cannot expose invalid L1 data or retain completion state?

## Expected behavior

For healthy-sidecar and abort/error paths alike, client and server request bookkeeping should have a defined bounded lifecycle. Abandoned request state should be reclaimable without requiring a vLLM worker or sidecar restart, while preserving correctness for normal in-flight requests.

## Reproduction direction

1. Run vLLM + `LMCacheMPConnector` + sidecar with an SSD-backed `fs_native` L2.
2. Send sustained requests and observe the vLLM worker: `_returned_finished` grows monotonically.
3. Submit LOOKUPs, then abort/disconnect before prefetch polling completes, or induce a prefetch-status timeout.
4. Observe `lmcache_mp.active_prefetch_jobs` and `PrefetchController.report_status()["completed_results_count"]`; entries can remain after the client has abandoned the request.

## 评论 (2)

### neevmodh · 2026-09-26

Read through both paths in `upstream/dev` to check the analysis — can confirm both observations.

**Part 1 (`_returned_finished`):** Confirmed there's no eviction path on this set anywhere in `vllm_multi_process_adapter.py`. Looking at `_process_finished_stores`, the set's only real job is to stop the same `req_id` from being re-added to `ret_stores` if `finished_req_ids_from_engine` reports it again in a later call — but once vLLM's own engine stops mentioning a `req_id` (i.e. it's fully retired from the engine's tracking), `_returned_finished`'s entry for it can never be hit again by the loop that checks it, so it's dead weight from that point on. A conservative fix that doesn't touch the dedup semantics: at the end of `_process_finished_stores`, intersect `_returned_finished` with the union of `self.finished_stores` / `self.store_futures` / `finished_req_ids_from_engine`, so an ID is only retained while it's still reachable through one of the sets that could re-report it. Happy to send that as a small PR if a maintainer confirms there's no other call site relying on longer retention.

**Part 2 (prefetch jobs):** Confirmed `end_session` (`lookup.py:514`) is already the natural per-request teardown hook — it's called on `MP_REQUEST_END` and already knows the `request_id`. Adding `self._prefetch_jobs.pop(request_id, None)` there looks safe on the `LookupModule` side. The harder part is `PrefetchController`'s `_completed_lookups`/`_completed_results` (a *different* class, presumably reachable through session/controller wiring I didn't fully trace) — and your question #3 is the real blocker here: popping a `Bitmap` out from under a prefetch that completes *after* the client has already been torn down risks exactly the late-completion/invalid-L1-data race you flagged, since it's native memory. I don't think this half should be fixed without a maintainer confirming the intended ownership handoff at session end — happy to implement once that's settled, but I'd rather not guess at a fix that touches native memory lifecycle across processes.

### neevmodh · 2026-09-26

Following up on my earlier analysis: opened #5363 for part 1 (the `_returned_finished` set). Rather than guess at exact removal timing (which depends on the vLLM engine-contract question I couldn't answer myself), it bounds the set with a small LRU cap instead — converts unbounded growth into bounded memory without needing that question resolved first. Part 2 (sidecar prefetch/completion state) is intentionally left alone, per my earlier comment on the native-memory ordering risk.
