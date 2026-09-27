# [Issue #5143] [Bug] LMCacheMPConnector ignores kv_transfer_config.kv_role — kv_consumer engines still store KV to the shared MP server

source: https://github.com/LMCache/LMCache/issues/5143
state: closed | updated: 2026-09-17T17:26:14Z
labels: 

## 正文

## Summary

In multiprocess (MP) mode, `LMCacheMPConnector` never reads `KVTransferConfig.kv_role`. An engine launched with `kv_role="kv_consumer"` still generates store metadata for every scheduled request and unconditionally writes its KV into the shared MP server (CPU L1). This contradicts the semantics vLLM documents for `kv_role` ("Whether this vLLM instance produces, consumes KV cache, or both") and also differs from LMCache's own non-MP connector (`LMCacheConnectorV1` / `vllm_v1_adapter.py`), which honors the role via `force_skip_save`.

No correctness impact — the stored content is identical — but a consumer-role engine pays device→host copy cost on every request and consumes shared L1 capacity it is supposed to only read from.

## Environment

- LMCache: `dev` branch, tested at `e5078730` (2026-09-14). Re-checked current `dev` on 2026-09-17: `lmcache/integration/vllm/lmcache_mp_connector.py` still contains zero occurrences of `kv_role` / `kv_consumer` / `kv_producer` / `force_skip_save`.
- vLLM: v1.5.0-based build with the standard KV connector V1 interface (`KVConnectorBase_V1`, SCHEDULER/WORKER roles).
- Topology: one LMCache MP server (shared CPU L1) + two vLLM TP4 engine processes connected to it. Model was Qwen3.8-27B-FP8 (hybrid GDN + full attention, 784-token hybrid KV chunk) — model details are not believed relevant; this is pure connector logic.

## Observed behavior

From an archived instrumented run (both engines' roles are echoed in their APIServer startup args, so the roles were definitely delivered to the connector):

- Engine B launched with `kv_role="kv_both"`, engine A with `kv_role="kv_consumer"`; both connected to the same MP server.
- B received **zero requests** during the measurement window (its engine log is empty between registration and teardown).
- A received exactly **one** cold request with a 32K-token prompt → the MP server log recorded **168 `Stored 784` lines = 42 chunks × 4 TP ranks**, i.e. the entire 32K prefix was stored by the `kv_consumer` engine.
- The only engine that could have produced those stores is A: the store burst coincides exactly with A's single request window, and the line count matches A's prompt geometry exactly.

(We initially mis-attributed some store bursts in single-realm producer-first chains before isolating this cleanly; happy to share the raw logs.)

## Where it happens in code

- `__init__` only reads `lmcache.mp.*` extra-config keys (server_urls / host / port / mq_timeout / heartbeat / eager_prefetch / lazy_offload / transfer_intermediate_tensors); the class docstring's extra-config list has no role field either.
- Scheduler side: `_process_new_requests` and `_process_cached_requests` build `LMCacheMPRequestMetadata.GetStoreMetadata(...)` for every scheduled request with no role gate (only `lazy_offload` changes how/when the store is queued).
- Worker side: `wait_for_save` submits every STORE entry via `batched_submit_store_requests`.
- `request_finished` returns `True` unconditionally in the default mode, telling vLLM "this request is being saved asynchronously, don't free its blocks".

vLLM, by contrast, treats the role as a real contract: `kv_role` is mandatory when `kv_connector` is set (`KVTransferConfig.__post_init__` raises otherwise) and exposes `is_kv_producer` / `is_kv_consumer` helpers specifically for connectors to branch on. The vLLM core itself never enforces the role — that is each connector's responsibility.

LMCache's non-MP connector already does the right thing, e.g. in `lmcache/integration/vllm/vllm_v1_adapter.py`:

```python
force_skip_save = self.kv_role == "kv_consumer" or self.force_skip_save
```

## Impact

- A `kv_consumer` engine wastes D2H bandwidth and MP-server CPU L1 capacity on every request (for our model: a 32K prefix ≈ 8.6 GB across 4 ranks) — capacity that in a shared-cache deployment belongs to the producer's output.
- PD-disaggregated or shared-L1 deployments cannot use `kv_role` to prevent write-back; today the only way to keep a consumer from writing is deployment-topology isolation (separate MP realms), which is what we had to resort to.
- Silent semantic gap: nothing warns the user that MP mode ignores a field vLLM documents as meaningful.

## Minimal reproduction

1. Start an LMCache MP server on port P (CPU L1 backend is fine).
2. Launch vLLM with:

```json
--kv-transfer-config '{"kv_connector":"LMCacheMPConnector","kv_role":"kv_consumer","engine_id":"consumer_a", ...mp server settings...}'
```

3. Send one request with a novel long prompt (cold cache).
4. Expected per `kv_role`: no store. Actual: the MP server logs `Stored N tokens` and `total_object_count` in the health endpoint increases by the prompt's chunk count × TP rank count.

## Workaround

Run all engines as `kv_both` and isolate store domains by topology (a separate MP server per engine group), accepting redundant stores within each group.

## Suggested directions

Either would resolve this for us:

1. Honor the role: in the scheduler-side connector, skip store-metadata generation when `kv_transfer_config.is_kv_consumer` (mirroring `force_skip_save` in the non-MP adapter); or
2. If MP mode is intentionally always-`kv_both`, document that explicitly and (ideally) warn at connector init when `kv_role != "kv_both"` so users aren't misled.

## Related minor note

The `Stored %d tokens` log line is only emitted when `stored_count > 0` (content-addressed dedup skips already-present chunks). A fully-deduped re-store is therefore indistinguishable in the logs from "no store happened"; a `Stored 0 tokens (N/N chunks already present)` line would help debugging. Low priority.


## 评论 (3)

### kezboard233 · 2026-09-16

**Update while preparing a patch proposal:** found the prior report #4665 — same mechanism from the CacheBlend angle (single-process connector honors `kv_role`/`skip_save`, MP connector honors neither). It was closed by its author without maintainer response, and no fix has landed on `dev` (re-checked today: zero occurrences of `kv_role`/`force_skip_save` in `lmcache_mp_connector.py`).

To settle design intent before sending code, we opened a discussion: #5146 — is MP mode intentionally always-`kv_both` (→ we'd propose docs + an init warning), or a contract gap vs vLLM's documented `kv_role` semantics (→ we'd propose a role gate mirroring the single-process `force_skip_save`)? We're happy to contribute either. @zhengfeihe would you mind steering?

### DongDongJu · 2026-09-16

Hello @kezboard233, you are right. mp STORE should check kv_role. Let me check now

### zhengfeihe · 2026-09-17

@kezboard233 

Hi! Thank you for taking time to report this. I’ve checked #5148, and I think it should resolve the issue. If you run into any further problems, don’t hesitate to report or submit a PR. Appreciate your help!
