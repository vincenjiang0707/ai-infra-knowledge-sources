# [Issue #1958] [BUG] agent::releaseXferReq() cannot support asynchronous request cleanup

source: https://github.com/ai-dynamo/nixl/issues/1958
state: open | updated: 2026-09-11T14:52:13Z
labels: cancellation

## 正文

`nixlAgent::releaseXferReq()` assumes that `releaseReqH()` either completes the release synchronously or fails. A backend cannot report that cancellation has started but still needs polling, because `NIXL_IN_PROG` is treated like successful release rather than as a distinct result.

Problematic code: [`nixlAgent::releaseXferReq()` lines 1314-1330](https://github.com/ai-dynamo/nixl/blob/a7f2232318903bb37ea8428f25e620c07e25461e/src/core/nixl_agent.cpp#L1314-L1330).

## Current control flow

Assume a transfer is active and the backend needs several progress calls to cancel its work and drain its resources:

1. `releaseXferReq()` sees `req_hndl->status == NIXL_IN_PROG` and calls   `checkXfer()` once.
2. If `checkXfer()` still returns `NIXL_IN_PROG`, `releaseXferReq()` calls the   backend's `releaseReqH()`.
3. The result is tested only with `status < 0`. Every non-negative result,   including `NIXL_IN_PROG`, follows the success path: `backendHandle` is set to   `nullptr`, the outer request is deleted, and `releaseXferReq()` returns   `NIXL_SUCCESS`.

## What the backend can do today

If `releaseReqH()` returns `NIXL_SUCCESS`, the request is destroyed immediately.This is correct only when the backend has already stopped all work and released every resource synchronously. Returning success merely after *starting* asynchronous cancellation loses the request and backend handle, so the caller cannot poll the cleanup to completion.

If `releaseReqH()` returns a negative error, `releaseXferReq()` returns `NIXL_ERR_REPOST_ACTIVE` without deleting the request. However, the negative backend result is stored in `req_hndl->status`; `getXferStatus()` only calls `checkXfer()` while that status is `NIXL_IN_PROG`, so subsequent status checks do not progress cleanup. An error can therefore report that release failed, but cannot represent cleanup that is proceeding normally and needs another poll.

If `releaseReqH()` returns `NIXL_IN_PROG`, the current `< 0` check treats it as success. `releaseXferReq()` clears `backendHandle`, deletes the request, and returns `NIXL_SUCCESS`, even though the backend explicitly reported that the release is unfinished. This is the missing state needed for asynchronous cleanup.

## Suggested fix

Special-case `NIXL_IN_PROG` immediately after `releaseReqH()`: keep both the request and `backendHandle`, leave `req_hndl->status` as `NIXL_IN_PROG`, and report that the request has not yet been released. The caller can then continue calling `getXferStatus()` or retry `releaseXferReq()` until backend cleanup returns a terminal result. Only `NIXL_SUCCESS` should clear `backendHandle` and destroy the request; negative statuses should continue to represent genuine release failures.

## 评论 (4)

### lluki · 2026-07-16

Ok, this is more complicated than the suggested fix: Rust calls this method on `drop` and python `__del__`. Furthermore do these wrappers do not propagate any error code. I think, the better approach is that the backends **must** cleanup and must do so synchronously. If this is not possible, it has to be hidden by the backend (ie, move the context to an list of outstanding contexts that will capture and discard future cleanup requests.)

But this approach is problematic too, that means that for example a `read` request could complete after the releaseXferReq. Thus, the buffer ownership has not been correctly transferred: The caller is not able to use the buffer after the release.

### lluki · 2026-07-17

[nvidia internal design doc link](https://nvidia.sharepoint.com/:w:/r/sites/NBU-Adv-Dev-Professionals/Shared%20Documents/General/Projects/NIXL/Design/2026-08-04%20Request%20Cancellation.docx?d=w8fe0f28b9926467ea29197b5a5c76d81&csf=1&web=1&e=XxUTlr)


### xiaodouzi666 · 2026-09-03

Another data point from a backend that landed the deferred-release side of this.

The Mooncake TENT backend in #2082 does what #2077 settled on: releaseReqH() accepts the release, a batch that has not reached a terminal status is parked on an engine-side list, a sweep on later engine calls frees it once the status reads terminal, and engine teardown reclaims whatever is left.

We tried the synchronous alternative first, because it is the one that keeps buffer ownership honest, and on RDMA it is not viable. With a bounded drain inside releaseReqH() the release call had a p99 of 3.70 s, because cancellation only lands after the fabric has exhausted its retries. Parking instead, the same release path returns in at most 7 us across 320 releases issued while transfers were still in flight, measured from the same binary in the same session. So for at least one more backend, asking backends to clean up synchronously costs seconds on the caller's thread rather than milliseconds.

The buffer-ownership consequence is real for us too, and we assumed exactly the contract in #2077's semantics note: a deferred release returns success while the transfer may still be writing, and a caller that needs the data settled polls to completion first. Since there is discussion on that PR about dropping the public API comment, it would help to have that rule land on releaseXferReq() somewhere rather than only in the PR that introduced it.

### lluki · 2026-09-04

Hi @xiaodouzi666 

Thanks for your report, this is very valuable. I'm currently working on a async cancellation draft PR. Could you explain me in which case you would need this behavior:

> a deferred release returns success while the transfer may still be writing, and a caller that needs the data settled polls to completion first

The only use-case for this that i could find, is on `shutdown` that is, if the process is going down anyway. Do you have any other use case for that behavior?  In non-`shutdown` cases i could think of it would be better to simply keep the request handle alive.


