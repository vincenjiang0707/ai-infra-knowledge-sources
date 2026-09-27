# [Issue #3957] [Bug] lmcache_mp_connector_0201.py (vLLM 0.20.1) out of sync with refactored adapter API — ParallelStrategy/SchedulerAdapter signature mismatch

source: https://github.com/LMCache/LMCache/issues/3957
state: closed | updated: 2026-09-21T07:57:42Z
labels: 

## 正文

/kind bug

## Summary

On **vLLM 0.20.1 + LMCache 0.5.0**, `LMCacheMPConnector` cannot initialize because **`lmcache/integration/vllm/lmcache_mp_connector_0201.py` is out of sync with the refactored adapter API**. It constructs `ParallelStrategy` and `LMCacheMPSchedulerAdapter`/`LMCacheMPWorkerAdapter` with the *old* (pre-multi-server) signatures.

The generic `lmcache_mp_connector.py` *does* match the current adapter API (`server_urls`, the new `ParallelStrategy` fields), but it imports `KVCacheSpecKind` from `vllm.v1.kv_cache_interface`, which only exists in **vLLM 0.23.0+**, so it cannot be imported on 0.20.1.

Net result: **there is no working `LMCacheMPConnector` path on vLLM 0.20.1** — the version-specific `_0201` connector is stale, and the generic one requires a newer vLLM.

## Environment

- **vLLM:** v0.20.1
- **LMCache:** 0.5.0 (PyPI wheel; `c_ops` rebuilt from sdist against the image's CUDA 13 torch — note: the prebuilt cp312 wheel's `c_ops` links `libcudart.so.12` and falls back to the python backend on a CUDA 13 torch image)
- **Python:** 3.12
- **Model:** `deepseek-ai/DeepSeek-V4-Flash`, FP8 KV, DP=4 + EP, `--block-size 256`
- **Hardware:** NVIDIA B300
- Connector selected via `--kv-transfer-config '{"kv_connector":"LMCacheMPConnector","kv_connector_module_path":"lmcache.integration.vllm.lmcache_mp_connector_0201","kv_role":"kv_both","kv_connector_extra_config":{"lmcache.mp.host":"tcp://...","lmcache.mp.port":18009}}'`

## Errors (two cascading)

**(1)** `lmcache_mp_connector_0201.py:156` (`create_worker_adapter`) / `:123` (`create_scheduler_adapter`):

```
TypeError: ParallelStrategy.__init__() takes 7 positional arguments but 8 were given
```

`_0201` passes `(use_mla, world_size, kv_rank, vllm_world_size, vllm_rank, tp_size, pp_size)`, but the current `ParallelStrategy` dataclass (in `vllm_multi_process_adapter.py`) is `(use_mla, vllm_world_size, vllm_worker_id, tp_size, pp_size, n_servers)`.

**(2)** After locally patching the `ParallelStrategy` call to the new fields (`n_servers=1`), the next mismatch appears at `lmcache_mp_connector_0201.py:136`:

```
TypeError: LMCacheMPSchedulerAdapter.__init__() got an unexpected keyword argument 'server_url'
```

The current `LMCacheMPSchedulerAdapter.__init__` takes `server_urls: list[str]` (plural) + `extra_config`, etc. The `_0201` connector still passes singular `server_url=`.

## Root cause

`lmcache_mp_connector_0201.py` is a version-pinned **copy** that drifts from the actively-maintained generic connector (cf. #3798, which fixes a different drift in the same `_0201` copy). The multi-server refactor (`server_urls`, new `ParallelStrategy`) updated the generic connector and the adapters, but not the `_0201` copy.

## Why it matters

vLLM 0.20.1 is pinned in some production deployments: e.g. **DeepSeek-V4 on B300** — vLLM 0.23.0's V4 native implementation (`sm100_tf32_hc_prenorm_gemm`) fails to launch on B300 SXM6 (`invalid argument` under both CUDA 12.9 and 13.0), so the model is kept on the 0.20.1 implementation. For those users there is currently no usable `LMCacheMPConnector`, even though **0.5.0 already fixes the V4 KV-layout (`storage_offset != 0`) registration path** that blocks 0.4.x (validated: the contiguity error is gone on 0.5.0 before the connector-signature errors above).

## Request

Either keep `lmcache_mp_connector_0201.py` in sync with the refactored adapter API (port the `server_urls` / `ParallelStrategy(n_servers=...)` changes into the `_0201` copy), or document the minimum LMCache version per supported vLLM version so 0.20.1 users know the expected path.

## Related

- #3931 — V4-Flash MPConnector error on vLLM 0.23.0 (contiguity; different root cause)
- #3821 / #3853 — `storage_offset != 0` contiguity fix (the layer *after* this one)
- #3798 — another drift fix in the `_0201` copy
- #3156 — DeepSeek V4 support (feature request)


## 评论 (3)

### github-actions[bot] · 2026-08-30

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### d3nb · 2026-08-30

Still relevant — and the last two months have produced a fairly clean demonstration of the underlying problem, so I'd rather this not age out silently.

The original report was that `lmcache_mp_connector_0201.py` had drifted from the refactored adapter API, while the generic `lmcache_mp_connector.py` (which does match) can't be used on vLLM 0.20.1 because it imports `KVCacheSpecKind`, added in 0.23.0. That leaves 0.20.1 users with no working path.

What's new is that the drift is now observable in real time rather than just asserted:

- **#4781** (merged 2026-08-27) backported the vLLM #47505 guard into `lmcache_mp_connector.py` — the live connector only.
- **#4028** (open since 2026-07-07) carries *the same guard* into `lmcache_mp_connector_0180.py` and `_0201.py`.
- **#3798** does the same thing for a different fix (`free_lookup_locks` missing `cache_salt` in the `_0201` copy), and has just been marked stale as well.

So as of today the version snapshots are demonstrably behind the connector they were copied from, and the gap is being introduced one fix at a time — which is the failure mode this issue was opened about. Each fix has to be remembered twice, and when the second half stalls, the snapshots quietly rot.

Two ways to resolve it, either of which would close this out from my side:

1. Merge #4028 (and #3798) to resync, and treat "does the snapshot need this too?" as part of the review checklist for anything touching the connector.
2. Or state explicitly that the version snapshots are best-effort/frozen, so users on older vLLM know they're on their own rather than discovering it at connector-init time.

What would not be great is the silent third option, which is where this is currently headed.


### d3nb · 2026-09-21

Closing as resolved by #4135 (merged 2026-07-20), which was filed against #4134, a duplicate of this report — so it didn't link here automatically, and I only noticed now.

Verified against `dev` today, the signature drift reported here is gone from `lmcache_mp_connector_0201.py`:

- `ParallelStrategy` is constructed with keyword arguments, including `n_servers`, matching the current definition.
- The scheduler adapter is created with `server_urls=[server_url]`, matching `LMCacheMPSchedulerAdapter(server_urls: list[str])`.
- The worker adapter's `server_url=` is correct as-is: `LMCacheMPWorkerAdapter` still takes a single `server_url: str`.

The separate question of keeping the version snapshots in step with the live connector — specifically the non-chosen-connector guard from #4781 — is tracked in #4028, not here.

