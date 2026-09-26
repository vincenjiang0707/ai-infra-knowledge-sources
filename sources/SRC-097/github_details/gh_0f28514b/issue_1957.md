# [Issue #1957] [BUG] POSIX io_uring/aio partial enqueue leaves stale queue entries

source: https://github.com/ai-dynamo/nixl/issues/1957
state: open | updated: 2026-07-28T08:08:37Z
labels: 

## 正文

The POSIX (io_uring/aio) backend does not roll back entries when enqueue() fails partway through a request. Because all requests share one I/O pool and submission queue, another request can later submit the leftover entry.

## Failure sequence

Assume `ios_pool_size=64`.

| Step | Operation | Queue state |
|---|---|---|
| 1 | Request A posts 63 descriptors and remains in progress. | 63 entries belong to A; 1 entry is free. |
| 2 | Request B starts posting 2 descriptors. | |
| 3 | B's first `enqueue()` succeeds. | Its entry is appended to the global `ios_to_submit_`; no entries remain free. |
| 4 | B's second `enqueue()` fails with `NIXL_ERR_NOT_ALLOWED`. | B's first entry remains queued. |
| 5 | `nixlPosixBackendReqH::postXfer()` immediately returns the error. | No rollback removes B's first entry. |
| 6 | The application may release B because posting returned a terminal error. | B's request handle is deleted. |
| 7 | The application polls request A. | io_uring's global `poll()` submits queued entries, including B's leftover entry. |
| 8 | B's I/O completes. | Its callback uses B's deleted request handle as `ctx_`, causing a use-after-free. |

Even if B is not released, one of its I/Os executes despite `postXferReq(B)` reporting failure. Reposting B can then mix the leftover operation with new operations and corrupt completion accounting.

## 评论 (1)

### AlterHoodie · 2026-07-28

@lluki can I work on this if a fix is not in place already?

Proposed approach (under the existing `io_queue_lock_` when sync is enabled):
1. Preflight: before enqueueing, if `free_ios_.size() < num_descriptors`, return immediately.
2. Rollback: if enqueue still fails mid-loop, move this request’s just-queued entries from `ios_to_submit_` back to `free_ios_` before returning the error.
