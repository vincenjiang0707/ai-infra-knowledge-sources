# [Issue #5168] [MP] [Bug] Isolated IPC: KV re-registration after a server restart fails with CUDA_ERROR_INVALID_CONTEXT

source: https://github.com/LMCache/LMCache/issues/5168
state: open | updated: 2026-09-22T11:27:28Z
labels: 

## 正文

**Summary**
With isolated IPC enabled (`lmcache server --isolated-ipc` + `lmcache.mp.isolated_ipc: true` on the vLLM connector), a vLLM worker cannot **re-register** its KV caches after the LMCache server restarts. The heartbeat recovers, calls `_reregister_kv_caches_callback`, and fails identically on every heartbeat until the vLLM process is restarted, because `RawCudaIPCWrapper` calls the CUDA driver API from a thread that has no current CUDA context.

**Details**
Environment: LMCache 0.5.5 (`lmcache/vllm-openai:v0.5.5`), vLLM 0.29.0, torch 2.13.0+cu130; MP mode on Kubernetes with the LMCache server and vLLM in separate pods, A100 40GB. The stand-alone reproduction below also reproduces on an RTX PRO 6000.

Every re-registration attempt fails with:

```
  File ".../lmcache/integration/vllm/vllm_multi_process_adapter.py", line 1548, in _reregister_kv_caches_callback
  File ".../lmcache/integration/vllm/vllm_multi_process_adapter.py", line 1473, in _send_register_kv_caches_request
  File ".../lmcache/v1/multiprocess/transfer_context/worker_transfer.py", line 460, in register
  File ".../lmcache/v1/platform/kv_wrap.py", line 71, in wrap_kv_caches
  File ".../lmcache/v1/platform/kv_wrap.py", line 35, in wrap_one_kv_cache
  File ".../lmcache/v1/platform/cuda/ipc_wrapper.py", line 275, in wrap
  File ".../lmcache/v1/platform/cuda/ipc_wrapper.py", line 301, in __init__
RuntimeError: cuMemGetAddressRange failed: <CUresult.CUDA_ERROR_INVALID_CONTEXT: 201> (ptr=0x7f5466000000).
CUDA IPC memory handles only support cudaMalloc-style allocations. Memory created through the CUDA VMM API cannot be shared ...
```

The **first** registration of the same tensors succeeds, so the allocation is ordinary `cudaMalloc` memory and the hint about VMM allocations is misleading.

Root cause: `RawCudaIPCWrapper.__init__` calls the CUDA **driver** API (`cuMemGetAddressRange`) directly. The initial `register_kv_caches` runs on the worker's main thread, which has a current CUDA context. The re-registration runs on the connector's `HeartbeatThread`, which has never touched CUDA; the driver API does not bind the primary context implicitly the way the runtime API does, so the call returns `CUDA_ERROR_INVALID_CONTEXT`. The legacy path (`isolated_ipc: false`, hostIPC + shared /dev/shm, `CudaIPCWrapper`) re-registers correctly on the same setup and versions.

Confirmed with a stand-alone script on LMCache 0.5.5: `RawCudaIPCWrapper(view)` succeeds on the main thread and fails with `CUDA_ERROR_INVALID_CONTEXT` from a fresh `threading.Thread`. Wrapping the call in `with torch.cuda.device(...)` (the pattern `VmmCudaIPCWrapper` uses) does **not** help: on a fresh thread torch skips the runtime call when the target equals its cached current device (0). Binding the context explicitly (`cudaSetDevice`, or `cuDevicePrimaryCtxRetain` + `cuCtxSetCurrent`) makes the same call succeed.

**Steps / Reproduction (if applicable)**
1. Start `lmcache server --isolated-ipc ...` and a vLLM with `LMCacheMPConnector` + `lmcache.mp.isolated_ipc: true`; send a request so the KV caches register.
2. Restart the LMCache server (pod restart, or kill and relaunch).
3. Watch the vLLM log: `LMCache server is healthy again, triggering recovery callback`, then `Unexpected error during KV cache re-registration; will retry on next heartbeat` with the traceback above, every heartbeat (10 s), indefinitely.

Minimal stand-alone form: allocate a CUDA tensor on the main thread, then construct `RawCudaIPCWrapper(tensor)` from a new `threading.Thread`.

**Expected Outcome / Goal**
After the server is back, the worker re-registers its KV caches on the first recovery callback, as it does on the legacy (non-isolated) IPC path.

**Actual Outcome (if applicable)**
With isolated IPC on, no worker re-registers for as long as the vLLM process lives (observed for well over 5 minutes); the worker serves in degraded mode with no external cache until it is restarted. With isolated IPC off, the same restart recovers on the next heartbeat.

**Additional Context**
Proposed fix: make the device's primary context current on the calling thread when it has none, before the driver call in `RawCudaIPCWrapper.__init__` (`cuCtxGetCurrent` → `cuDevicePrimaryCtxRetain` + `cuCtxSetCurrent` + `cuDevicePrimaryCtxRelease`), plus a regression test that constructs the wrapper from a fresh thread.

`VmmCudaIPCWrapper` wraps its own driver calls in `with torch.cuda.device(...)` and is exposed to the same gap on a fresh thread.

Workaround: `lmcache.mp.isolated_ipc: false` on the connector and omit `--isolated-ipc` on the server (falls back to the hostIPC + shared /dev/shm path).


## 评论 (1)

### daitran-tensormesh · 2026-09-22

Two updates since filing.

**The code has moved.** The implementation now lives at `lmcache/v1/platform/devices/cuda/ipc_wrapper.py`; the legacy `lmcache/v1/platform/cuda/` re-export package was removed in #5282. The traceback above is from the 0.5.5 release and still reflects what users hit on that version. The bug is unchanged on current `dev` at the new path.

**Scope is both wrappers, not one.** `VmmCudaIPCWrapper.__init__` wraps its driver calls in `with torch.cuda.device(...)`, which is precisely the pattern proven not to bind a context on a fresh thread, so it has the same defect at the same entry point. #5169 now fixes both.
