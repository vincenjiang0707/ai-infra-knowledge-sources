# [Issue #4155] SIGSEGV of whole cache server on partial-chunk transfers: python_ops_fallback wraps CUDA staging buffers as CPU tensors (plus wrap-shape rank mismatch that silently corrupts MiniMax-M3 MSA-indexer KV)

source: https://github.com/LMCache/LMCache/issues/4155
state: open | updated: 2026-09-18T01:46:49Z
labels: stale

## 正文


Title: `python_ops_fallback.multi_layer_block_kv_transfer` segfaults the whole cache server on partial-chunk (skip_prefix_n_blocks>0) transfers: `_normalize_lmcache_objects` pointer mode wraps CUDA staging buffers as CPU tensors

## Environment
- lmcache 0.5.1, external `lmcache server` (MP mode) + LMCacheMPConnector, chunk_size 256
- vLLM 0.23.1rc1.dev672, MiniMax-M3 TP4, 8x B200; fallback path active because the native kernels
  reject the M3 topology (see companion issue #1)

## Symptom
2-for-2 (on two different hosts): after a successful full retrieve, the next request that triggers a
PARTIAL external load (engine already holds most of the prefix; only a 128-256 token sliver is loaded,
so the transfer runs with `skip_prefix_n_blocks > 0`) SIGSEGVs the server process (exit 139).

- dmesg: `segfault at <buf_ptr>+0x8020 ip <libtorch_cpu> error 4` — multiple "pids" at the same ip
  simultaneously (OMP worker threads of one TensorIterator copy)
- gdb core bt: `at::native::AVX2::direct_copy_kernel` (`c10::Half` path) <- `TensorIteratorBase::serial_for_each` <- OMP
- faulthandler: `python_ops_fallback.py:1744 _transfer_per_layer_hnd` <- `:1312 multi_layer_block_kv_transfer`
  <- `lmcache_driven_transfer.py:559 transfer_kv_per_object_group` <- `:1244 retrieve`

## Root cause (verified by instrumentation)
`transfer_kv_per_object_group` passes `get_temp_kernel_group_buffer(...).data_ptr()` (raw ints) to the
fallback. Those staging buffers are **CUDA tensors** (verified: `dev=cuda:1`, `ptr=0x71b46e000000`;
fault address `0x71b46e008020` = ptr+0x8020). `_normalize_lmcache_objects` pointer mode reconstructs
them with `_tensor_from_ptr(ptr, chunk_shape, dtype, "cpu")` — device hardcoded to CPU (the docstring
even says "always on CPU").

Why full loads don't crash: with `skip_prefix_n_blocks == 0` the slice `obj[:, :, 0:chunk]` is
contiguous, so `.to(cuda)` becomes a single cudaMemcpy — CUDA UVA resolves the "host" pointer as
device memory and the copy silently works (D2D). With a partial load the slice
`obj[:, :, offset:end]` is NON-contiguous, so PyTorch contiguous-ifies on the CPU first
(`direct_copy_kernel`, AVX2) — CPU loads on a device pointer → SIGSEGV. The whole server dies,
taking every registered engine's KV service with it.

Secondary bug, same site: pointer mode infers `torch.Half` for these bf16 buffers (gdb frame shows the
`c10::Half` kernel). Same element size, so it is silent today, but it is wrong.

## Fix that works (tested)
Pass the real tensors instead of `.data_ptr()` ints at the `transfer_kv_per_object_group` callsite —
`_normalize_lmcache_objects` already short-circuits tensor input — the copy then runs on the correct
device with the correct dtype. With this one-line change the previously-crashing partial-load flow
completes (verified end-to-end on MiniMax-M3: partial 128-tok external hit, correct output).
Alternatively `_normalize_lmcache_objects` should take the device from the caller instead of
hardcoding "cpu".

## Two follow-on bugs the tensor-mode fix exposes (fix them together)
1. **Wrap-shape rank mismatch (silent KV corruption for M3):** the real staging buffers can have a
   different (numel-identical) rank than the ptr-mode wrap shapes the transfer functions expect.
   Observed: the M3 MSA-indexer group's real buffer is `(1, 57, 256, 128)` while
   `_transfer_per_layer_mla` expects `(nl, slots, hs)` = `(57, 256, 128)` and slices dim 1 as the
   TOKEN dim. With the raw 4-dim tensor it silently slices the LAYER dim instead — the indexer KV is
   scrambled and MiniMax-M3's sparse attention reads the wrong positions (we reproduced retrieved
   documents whose "beginning" contained end-of-document content, deterministically). Callers must
   reshape staging tensors to the exact wrap shapes ((nl, slots, hs) for MLA-format groups, else
   (2, nl, slots, nh*hs)) — or the transfer functions should normalize rank themselves.
2. **Lost implicit ordering:** the ptr-mode fake-CPU copies were host-blocking, which accidentally
   serialized against the non-synchronizing staging copies (`lmcache_memcpy_async_*`, own stream) and
   the per-batch reuse of staging slots. Pure tensor-mode copies are fully async, so explicit stream
   ordering/synchronization is required around (a) H2D staging -> kernel-group reads, (b) kernel-group
   writes -> D2H staging, and (c) D2H staging -> next batch's slot reuse.

## Additional robustness finding (same MP stack)
A request that arrives during the server-recovery window (server restarted, KV re-registration in
flight) can park in vLLM's WAITING_FOR_REMOTE_KVS **forever** — engine /health stays 200, later
requests are fine, the parked request never resolves (observed >12 min with
`lmcache.mp.mq_timeout=300`; `kv_load_failure_policy=recompute` does not cover a lookup that never
completes). Bouncing the server frees it. Also: while the server is down, per-request lookup blocking
degrades even trivial requests by 60-160s until the adapter declares the server unhealthy — a
lookup-side fail-fast would keep the engine near-baseline.

## Blast radius notes (why this is severe)
- One bad partial load kills the server for ALL engines; in-flight requests fail
  (`kv_load_failure_policy=fail` default), and in vLLM a late xfer-finished for the failed request
  then kills the ENGINE via `assert req_id in self.requests` (scheduler.py — filing separately
  against vLLM).
- Store path is exposed too: partial-chunk stores take the same wrap; we observed GPF-in-libc
  crashes during store experiments on another host.


Related: #4154 (why the fallback path is active for MiniMax-M3 at all).


## 评论 (2)

### gshubham55 · 2026-07-19

## Operational follow-up: MP server serializes GPU transfers on 1 thread by default, and the worker forward hangs (not the connector) under concurrency

Two findings from load-testing the MP server + `LMCacheMPConnector` on MiniMax-M3 (TP4, 8×B200), where the pure-torch fallback is forced because the native kernels are unusable on this model (#4154):

1. **`lmcache server --max-workers` defaults to 1**, so the GPU affinity pool (STORE/RETRIEVE) has a single thread and all transfers across all TP ranks serialize through it. `affinity_key = hash(zmq identity)` is per-rank, so `--max-gpu-workers N` (N ≥ #ranks) gives each rank its own thread on its own GPU with no same-GPU concurrency (race-safe). This is a large throughput win and should probably default to ≥ the TP size, or be documented prominently for multi-rank serving.

2. **Even with per-rank threads, sustained high concurrency (≈44 in-flight requests, each loading ~22k tokens of shared-prefix KV) hangs the vLLM worker**, which dies with `TimeoutError: RPC call to sample_tokens timed out` after `VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS` (300s). The hang is in the worker forward, not the connector submit (async futures) nor the scheduler — so connector-side mitigations (larger pool, an in-flight backpressure cap that sheds to recompute) do not prevent it. It appears the worker blocks on the cross-process CUDA-IPC transfer-completion event while the server's many small fallback kernels contend on the same GPUs. A watchdog that fails a retrieve/store whose IPC event hasn't completed within a bound (→ `error_block_ids` → recompute) would let the engine degrade gracefully instead of dying. The health path can't catch this because heartbeat pings run on the CPU pool and stay responsive while the GPU pool is saturated.

Net: with the native kernels working (#4154), transfers would be few and fast and this wouldn't arise; with the fallback, the server needs (a) multi-worker default and (b) a worker-side transfer-completion watchdog to be safe under load.


### github-actions[bot] · 2026-09-18

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
