# [Issue #5265] [Bug][MP] Stale CUDA IPC mappings block vLLM restart after an abnormal worker exit

source: https://github.com/LMCache/LMCache/issues/5265
state: open | updated: 2026-09-22T03:45:03Z
labels: 

## 正文

## Summary

In multiprocess mode, LMCache currently performs the server-side CUDA IPC KV-cache registration from `register_kv_caches()` before vLLM finishes model warmup and CUDA Graph capture.

This creates a failure window:

1. vLLM allocates its KV cache.
2. LMCache imports the KV cache through CUDA IPC.
3. vLLM is still running warmup or CUDA Graph capture.
4. The vLLM worker crashes before it sends `UNREGISTER_KV_CACHE`.
5. LMCache keeps the imported CUDA IPC mappings.
6. A restarted vLLM worker may fail to start because of retained GPU memory, or may encounter `CUDA error: CUDA-capable device(s) is/are busy or unavailable`.

The current `worker_registration_grace_seconds` default is very large, so LMCache may keep the old CUDA resources for a long time. Restarting the LMCache server is currently the most reliable way to release them.

This issue is related to [PR #2798](https://github.com/LMCache/LMCache/pull/2798), [PR #2943](https://github.com/LMCache/LMCache/pull/2943), [Issue #4014](https://github.com/LMCache/LMCache/issues/4014).

## Background

PR #2798 changed the heartbeat behavior so that the heartbeat starts after KV-cache registration. PR #2943 later changed it again so that the heartbeat starts only when the first `STORE` or `RETRIEVE` request arrives.

The reason for the lazy heartbeat was that vLLM may still be performing warmup and CUDA Graph capture after KV-cache registration, and the heartbeat thread may become blocked or may incorrectly cause health-state transitions during this period.

The maintainer @maobaolong confirmed that this behavior was observed in a real deployment.

However, delaying only the heartbeat does not prevent LMCache from already importing and retaining the vLLM CUDA IPC resources. If the worker crashes between KV-cache registration and the first request, there may be no heartbeat and no unregister request. The server therefore keeps the CUDA resources until the registration grace timeout expires.

## Root cause

The current flow is approximately:

```text
vLLM register_kv_caches()
  -> LMCacheMPConnector.register_kv_caches()
  -> LMCacheMPWorkerAdapter.register_kv_caches()
  -> create_transfer_context()
  -> transfer_ctx.register()
  -> REGISTER_KV_CACHE
  -> LMCache imports the CUDA IPC tensors
```

Once the server has imported the CUDA IPC tensors, the resources remain referenced by the server-side `GPUCacheContext` until one of the following happens:

- the worker sends `UNREGISTER_KV_CACHE`;
- the server reaps the worker after a heartbeat timeout;
- the LMCache server itself is restarted.

The current worker `instance_id` is generated randomly using `uuid.uuid4()`. A restarted worker therefore receives a new ID, so the server cannot reliably determine which old worker it replaces.

Using `model_name`, rank, world size, or CUDA device as a deterministic identity is not generally sufficient, because multiple independent vLLM instances can have identical model and parallel configuration, and may even use the same rank and GPU.

## Proposed solution

The preferred solution is to defer the actual server-side CUDA IPC registration until vLLM has completed warmup and a real transfer operation is needed.

The vLLM connector callback can still be invoked at the existing time, but LMCache would treat it as a pending registration:

```
vLLM register_kv_caches()
  -> save KV-cache tensors and layout metadata locally
  -> do not create the CUDA transfer context
  -> do not send REGISTER_KV_CACHE
  -> return successfully

First real STORE or RETRIEVE operation
  -> ensure registration has completed
  -> create the transfer context
  -> send REGISTER_KV_CACHE
  -> start the heartbeat
  -> continue with the STORE or RETRIEVE operation
```

This would prevent a vLLM crash during warmup or CUDA Graph capture from leaving an imported CUDA IPC context in LMCache, because no CUDA IPC registration would have occurred yet.

## Expected behavior after the fix

The following cases should work:

```
vLLM register_kv_caches() callback
  -> LMCache records pending registration only
vLLM crashes during warmup
  -> LMCache has no imported CUDA IPC mapping
  -> no GPU memory is retained by LMCache
```

## Trade-offs and compatibility considerations

This changes the meaning of the client-side `register_kv_caches()` call: it would acknowledge the KV-cache metadata locally, while the server-side CUDA IPC registration would happen lazily.

Potential trade-offs include:

- The first STORE or RETRIEVE request will pay the registration cost.
- The first request may need to handle registration failure.

An alternative would be to add an explicit vLLM callback after warmup and CUDA Graph capture, but that would require vLLM-side changes.

Another possible mitigation is a manual HTTP endpoint to trigger worker reaping. This would be useful as an operational fallback, but it would not automatically solve the failure.

## Questions

1. Is lazy server-side CUDA IPC registration from the first STORE/RETRIEVE path acceptable for MP mode?
2. Should LMCache also provide a manual HTTP endpoint to trigger worker reaping as an operational fallback?


## 评论 (4)

### Lyra0706 · 2026-09-20

Hi @ertcmm, I'm interested in looking into this and wanted to check if anyone is already working on it.

I took a first pass through the current `dev` code. It looks like KV registration happens in `register_kv_caches()`, while the worker heartbeat doesn't start until the first store/retrieve. One thing I'm not sure about is where the best boundary for deferring the CUDA IPC registration would be — `create_recorded_event()` currently assumes the transfer context is already registered, and `REGISTER_KV_CACHE` also seems to populate layout metadata used by lookup.

Would it make sense to explore a narrow fix that delays the CUDA IPC import without breaking the first lookup/event path? I'd keep the initial scope limited to the vLLM MP + LMCache-driven CUDA path, with tests for both an abort before the first transfer and the normal first-request path.

I haven't reproduced this on a GPU yet, so I wanted to check that this is the right direction before going further.

### ertcmm · 2026-09-21

Thanks for looking into this. @Lyra0706 @maobaolong 

The problem is that vLLM registers its KV cache before warmup and CUDA Graph capture finish. If the worker crashes during this period, LMCache may retain the imported CUDA IPC resources. A restarted worker can then fail to register until the old context is reaped.

I implemented a draft fix in my fork:

[[fix/defer-cuda-ipc-registration-after-vllm-warmup](https://github.com/ertcmm/LMCache/tree/fix/defer-cuda-ipc-registration-after-vllm-warmup)]

The change separates metadata registration from CUDA IPC registration:

- `register_kv_caches()` registers only KV-cache metadata, so lookup can work without importing CUDA IPC handles.
- Full CUDA IPC registration is deferred until the first operation that actually needs it, including `STORE`, `RETRIEVE`, `create_recorded_event()`, and CUDA IPC ring-buffer paths.
- Metadata-only registrations are also covered by unregister, reap, and cleanup logic.

I tested the worker failure window during CUDA Graph capture. After killing and restarting vLLM before the first transfer, the new worker completed initialization successfully, and the first request succeeded without triggering a CUDA-busy error or leaving the old GPU memory allocation behind.

BTW, the following open PRs are also related to my change:

- PR #4732: separates heartbeat liveness from transfer readiness. It is the most relevant overlap. It should be integrated carefully because this change introduces a metadata-only registration state before full CUDA IPC registration.
- PR #4941: improves explicit unregister cleanup across cache owners. Metadata-only registrations should be included in the same cleanup flow.


### maobaolong · 2026-09-21

@ertcmm Thanks for digging into this issue and proposing this approach. One concern is first-request latency. With full CUDA IPC registration deferred until the first STORE/RETRIEVE, that request synchronously waits for REGISTER_KV_CACHE to complete within mq_timeout.
On the server, full registration imports the CUDA IPC mappings, creates the per-worker GPU cache context, allocates the block-ID and staging GPU buffers, initializes CUDA/CuPy streams, and may register the staging buffer with GDS. For large models or GDS configurations, this work could be non-trivial and may increase TTFT or hit mq_timeout.
Could we benchmark the full-registration latency and consider performing it after vLLM warmup but before the worker is marked ready, or initialize it asynchronously while gating readiness on completion?

### ertcmm · 2026-09-22

@maobaolong Thanks for pointing this out. I agree that the first STORE/RETRIEVE request may synchronously pay the full CUDA IPC registration cost.
I will benchmark the client-side registration latency, server-side CUDA IPC registration, and the additional latency of the first STORE and RETRIEVE request, including large-model and GDS configurations.
I will also verify the measured latency against mq_timeout, and consider TTFT. If it is significant, we should consider a post-warmup readiness hook from vLLM, because LMCache alone cannot reliably determine when warmup and CUDA Graph capture have completed.
