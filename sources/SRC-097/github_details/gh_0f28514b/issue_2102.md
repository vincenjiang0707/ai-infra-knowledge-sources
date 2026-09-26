# [Issue #2102] [UCX] nixlUcxSharedThread::run() arms the worker with no CUDA context -> SIGSEGV in cuEventQuery (same defect class as #1157)

source: https://github.com/ai-dynamo/nixl/issues/2102
state: open | updated: 2026-08-21T07:30:19Z
labels: Network

## 正文

## Summary

`nixlUcxSharedThread::run()` calls `worker->arm()` without ever establishing a CUDA context on that
thread. When the UCX `cuda_copy` transport implements the arm, it calls `cuEventQuery`, which
segfaults in the driver. This is the same defect class as #1157 (libfabric progress thread), in the
backend that issue assumed was already safe.

We hit this **9 times in 43 hours** on a production 8×B200 PD-disaggregated deployment. It is
almost certainly the unexplained root cause behind sgl-project/sglang#23489 and
sgl-project/sglang#23499, both of which were closed without one.

## Stack (identical on all 9 crashes)

```
Fatal Python error: Segmentation fault

  File "<unknown>", line 0, in pthread_kill
  File "<unknown>", line 0, in gsignal
  File "<unknown>", line 0, in cuEventQuery
  File "<unknown>", line 0, in uct_cuda_base_iface_event_fd_arm
  File "<unknown>", line 0, in ucp_worker_arm
  File "<unknown>", line 0, in nixlUcxWorker::arm() const
  File "<unknown>", line 0, in nixlUcxSharedThread::run()
  File "<unknown>", line 0, in __clone
  File "<unknown>", line 0, in 0xffffffffffffffff
```

A corroborating UCX error appears on the same box shortly before some crashes:

```
cuda_copy_ep.c:217  UCX  ERROR failed to get context id of device GPU0 (0)
```

## Environment

- `nixl` / `nixl-cu13` **1.3.2** (UCX bundled in the wheel: `nixl_cu13.libs/libucp-*.so`)
- CUDA 13.0, driver-side B200 (sm_100), x86_64, 8 GPUs per host
- SGLang v0.5.17, `--disaggregation-transfer-backend nixl`, prefill and decode roles co-located on
  one host (prefill TP4/DP4 on GPUs 0-3, decode TP4/DP4 on GPUs 4-7)
- `UCX_TLS=cuda_copy,cuda_ipc,tcp`, `UCX_MEMTYPE_CACHE=n`, `UCX_RCACHE_MAX_UNRELEASED=1024`
- Each role runs with **all 8 GPUs visible** (`CUDA_VISIBLE_DEVICES` covers 0-7, own devices first)
  so that same-host CUDA IPC can map the peer role's KV memory — but each role only creates CUDA
  contexts on its own 4 devices.

## Analysis

`src/plugins/ucx/ucx_backend.cpp`, the shared thread's entire hot loop:

```cpp
// nixlUcxSharedThread::run(), ~line 339
do {
    worker->progressLoop();
} while (worker->arm() == NIXL_IN_PROG);
```

`arm()` → `ucp_worker_arm` → `uct_cuda_base_iface_event_fd_arm` → `cuEventQuery`. That last call
needs a valid CUDA context current on the calling thread. Nothing in the UCX plugin ever sets one.

Grepping the repo for context management returns hits in exactly one plugin:

```console
$ grep -rn "vramApplyCtx\|pthrCudaCtx\|cuCtxSetCurrent\|cuCtxPushCurrent" --include=*.cpp --include=*.h src/
src/plugins/libfabric/libfabric_backend.h:54:    CUcontext pthrCudaCtx_;
src/plugins/libfabric/libfabric_backend.h:356:    vramApplyCtx();
src/plugins/libfabric/libfabric_backend.cpp:302:    result = cuCtxSetCurrent(pthrCudaCtx_);
src/plugins/libfabric/libfabric_backend.cpp:971:                    vramApplyCtx();
src/plugins/libfabric/libfabric_backend.cpp:1023:        vramApplyCtx();
...
```

Zero hits under `src/plugins/ucx/`.

This is exactly the failure described in #1157 — a backend progress thread touching GPU state with
`pthrCudaCtx_` effectively NULL — and the fix there was to apply the context inside the progress
loop rather than once at thread start. Notably, #1157's own text states:

> The UCX backend handles this correctly by restarting the thread when the context changes, but the
> libfabric backend does not.

The current source does not support that claim. There is no context capture, no `cuCtxSetCurrent`,
and no restart-on-context-change anywhere in the UCX plugin.

## Why this configuration reaches it reliably

The thread only exists when the backend receives `num_threads > 0`:

```cpp
// ucx_backend.cpp:763
const size_t num_threads =
    nixl::getBackendParamDefaulted(init_params.customParams, "num_threads", 0u);
if (num_threads > 0) {
    engine = new nixlUcxThreadPoolEngine(init_params, num_threads);
```

SGLang passes `num_threads=8` for the **prefill** role and `0` for **decode**
(`python/sglang/srt/disaggregation/nixl/conn.py`). In our deployment the prefill role has crashed
9 times and the decode role — same host, same image, same UCX env, same traffic — has **never**
crashed. That asymmetry maps exactly onto the presence or absence of `nixlUcxSharedThread`.

Having 8 visible devices with contexts on only 4 appears to make the bad path much easier to hit,
which fits the `failed to get context id of device GPU0 (0)` error above.

## Reproduction rate

Nine crashes in ~43 hours of steady production traffic (~one per 4.8h), spread evenly across the
clock — not correlated with peak load, deploys, or any particular request shape. Each one kills the
role's scheduler process; peers then fail with gloo/NCCL "Connection reset by peer", and in 3 of 9
cases the survivors wedged for ~5 minutes before aborting with **Xid 43**. GPUs are healthy (zero
uncorrected ECC), no OOM.

## Workaround

Force the UCX backend to zero threads, which removes `nixlUcxSharedThread` entirely:

```python
create_backend("UCX", {"num_threads": "0"})
```

Under SGLang: `SGLANG_DISAGGREGATION_NIXL_BACKEND_PARAMS={"num_threads":"0"}`.

Cost is losing the dedicated progress thread, so progress falls to the caller's threads.

## Suggested fix

Mirror #1157 in the UCX plugin: capture the CUDA context at memory-registration time (or first
VRAM descriptor seen), store it on the engine, and apply it inside `nixlUcxSharedThread::run()`
before progressing/arming — on every iteration, not once at thread start, since the context can
change after the thread has already been created. The dedicated-thread path needs the same
treatment.

Happy to put up a PR if the maintainers agree on the shape.

## Related

- #1157 — CUDA context crash in libfabric backend progress thread (same defect class, fixed there)
- sgl-project/sglang#23489 — identical stack, closed same day as "Resolved via rebase"
- sgl-project/sglang#23499 — identical stack, closed with no linked fix; re-reported 2026-07-07 on
  a different GPU/CUDA/SGLang combination and unanswered since


## 评论 (4)

### skeptrunedev · 2026-08-17

Correcting my own report: **the `num_threads` framing above is wrong, and so is the workaround.**
The defect and the stack are unchanged; the explanation of when the progress thread exists is not.

`nixlUcxEngine::create()` (`ucx_backend.cpp:778`):

```cpp
if (num_threads > 0) {
    engine = new nixlUcxThreadPoolEngine(init_params, num_threads);
} else if (init_params.enableProgTh) {
    engine = new nixlUcxThreadEngine(init_params);      // <-- still has a shared progress thread
} else {
    engine = new nixlUcxEngine(init_params);
}
```

and `nixlUcxThreadEngine`'s constructor creates `nixlUcxSharedThread` for every shared worker as
long as `enableProgTh` is set — `num_threads` never enters that decision:

```cpp
if (!init_params.enableProgTh) return;
const size_t shared_count = getSharedWorkers().size();
thread_ = std::make_unique<nixlUcxSharedThread>(this, shared_count, init_params.pthrDelay);
```

`enableProgTh` comes from the agent config (`nixl_agent.cpp:347`,
`init_params.enableProgTh = data->config_.useProgThread`), which is passed through on explicitly
created backends too, and defaults to true. So:

- **`{"num_threads": "0"}` does not remove `nixlUcxSharedThread`.** It only drops the dedicated
  thread pool. Please disregard the workaround section in the original post.
- It is likely to make things *worse*: with the thread pool gone, transfers fall back to
  `nixlUcxEngine::sendXferRange()` on the shared workers, so the CUDA activity moves onto exactly
  the worker the shared thread arms.
- `num_threads` is therefore **not** what distinguishes an affected deployment from an unaffected
  one. The better explanation for why we only see this on the initiator side is that the initiator
  is what drives `cuda_copy` activity through its worker; the target's worker is largely passive,
  so its arm path has no pending CUDA event to query.

That widens the blast radius: any NIXL UCX agent with the default `enable_prog_thread=True` and
`cuda_copy` in `UCX_TLS` is exposed, not just ones that opt into a thread pool.

The only configuration that actually removes the thread is `enable_prog_thread=False` at agent
construction, which most callers (SGLang included) never set and which gives up asynchronous
progress entirely. So the fix in the CUDA-context handling looks like the only real remedy — I have
a patch along the lines suggested above and can open a PR.

Apologies for the noise; I would rather correct it here than have someone try the workaround.


### iyastreb · 2026-08-19

What's the current state?
Should we close the PR and issue?

### tomerg-nvidia · 2026-08-20

I am trying to reproduce this crash. From what I can tell cuEventQuery won't crash due to missing context but will cause a crash if the argument it gets is invalid. In UCX 1.22 there was this PR https://github.com/openucx/ucx/pull/11499 which fixed a potential uninitialised argument to cuEventQuery, but I could not reproduce this flow yet without destroying workers which I don't think is normal NIXL use. @skeptrunedev The fix is present in NIXL 1.4, is it possible for you to try it?

### tomerg-nvidia · 2026-08-21

The error log is not a result of not having a context, the context is pushed a few lines above that call in the code. It is an error with getting its ID with a call to `cuCtxGetId`. This log points to an application issue; something is causing a cuda error.

I also managed to reproduce the crash by externally destroying the cuda context before/during the arm call, and confirmed that with NIXL 1.4 it doesn't crash. @skeptrunedev Try NIXL 1.4, it should fix the issue.
