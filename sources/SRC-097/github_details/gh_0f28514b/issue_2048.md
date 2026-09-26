# [Issue #2048] PLUGINS/UCX: drain timeout on handle release leaves registered memory unsafe to deregister

source: https://github.com/ai-dynamo/nixl/issues/2048
state: closed | updated: 2026-08-27T12:29:23Z
labels: Network, Customer

## 正文

## Summary

`nixlUcxBackendReqH::release()` and `nixlUcxCompositeBackendReqH::release()` bound how long they will wait for in-flight UCX requests to reach a terminal state. When that deadline expires the request may still genuinely be in flight, and nothing in the current design prevents the caller from deregistering the memory backing the transfer. `ucp_mem_unmap()` then frees the memory handle while a zcopy completion is still pending, and that completion later dereferences the freed handle on a progress thread.

Closing this properly requires deferring deregistration until terminal completion, which changes the memory-registration lifetime contract. This issue tracks that work.

## Background

`release()` historically called `ucp_request_cancel()` and then freed the request immediately, with a `TODO` noting that cancelling may not be enough. It isn't: `ucp_request_cancel()` does not complete RMA/zcopy operations, and `ucp_request_free()` does not synchronously complete internal requests. A request could therefore still be in flight after `release()` returned, so a caller that deregistered its memory next freed the memory handle out from under a pending zcopy completion — a use-after-free that surfaces as a SIGSEGV inside `ucp_memh_put()`.

- #2044 addresses this for the non-composite path by progressing the worker in `drainRequest()` until the request reaches a terminal state.
- #2045 addresses the composite-chunk path by waiting in `waitForPendingChunks()` for `nixlUcxBackendSharedState::pendingReqs` to drain.

Both drains are bounded by `NIXL_UCX_REQUEST_DRAIN_TIMEOUT` (default 10s). The bound is deliberate: an unbounded wait means `release()` never returns when a transfer is wedged on an endpoint that is still alive and simply not progressing. UCX reports no error in that state and the request stays `NIXL_IN_PROG` indefinitely, so an unbounded drain converts a use-after-free into an unkillable teardown path. That failure mode has been observed in production.

## The remaining gap

The deadline makes teardown terminate, but it does not make the timeout path safe. On expiry:

- #2044 logs an error and deliberately leaks the UCX request object rather than freeing it, because freeing a request UCX may still complete is the very use-after-free being avoided.
- #2045 logs an error and proceeds to reset the shared state.

In both cases `release()` returns `void`, so the caller cannot observe the failure, and the log line is the only signal that the memory is not safe to deregister.

**Leaking the request object does not help with the memory handle.** It keeps UCX from writing into a freed *request*, but it does not retain the *memory registration* and does not block a subsequent deregistration. The pending completion still holds a reference to the memh, so if the caller deregisters, the original use-after-free is reachable again on exactly this path.

So the timeout path is a known-unsafe escape hatch, chosen over an unkillable teardown. It is strictly better than the prior behaviour — which freed in-flight requests unconditionally, with no wait and no diagnostic — but it is not a complete fix.

## Why the bounded wait is usually enough in practice

Worth stating so the severity is not overread. For the composite path, `release()` stores a failed status into the shared state *before* waiting; `nixlUcxChunkBackendReqH::status()` returns that status ahead of consulting UCX, and the dedicated thread's loop then calls `complete()` on each queued chunk, decrementing `pendingReqs`. The wait therefore drains within a single dedicated-thread pass unless a chunk is genuinely stuck inside UCX. The timeout only bites in the case where the alternative is hanging forever.

## Affected code paths

All in `src/plugins/ucx/ucx_backend.cpp`:

- `nixlUcxBackendReqH::release()` and `nixlUcxBackendReqH::drainRequest()` (as added by #2044) — the leak-on-expiry path.
- `nixlUcxCompositeBackendReqH::release()` and `nixlUcxCompositeBackendReqH::waitForPendingChunks()` (as added by #2045) — the reset-on-expiry path.
- `NIXL_UCX_REQUEST_DRAIN_TIMEOUT`, which bounds both.

The memory-registration side is the other half: whatever the plugin does on expiry has to interact with `deregisterMem` / `ucp_mem_unmap()` for the descriptors involved in the transfer.

## What a fix would need to change

The plugin needs an ownership record that outlives `release()` and defers `ucp_mem_unmap()` for the affected registrations until the outstanding requests reach a terminal state. Concretely that means:

1. On drain-timeout, record the still-in-flight requests together with the memory registrations they reference, instead of only leaking the request.
2. Make `deregisterMem` for a registration named in such a record defer rather than unmap immediately, and complete the unmap once the last referencing request terminates.
3. Decide how that reclamation is driven — a progress-thread sweep, or reclamation at engine teardown.
4. Decide the contract change this implies for callers: today `deregisterMem` is effectively synchronous, and a caller may reasonably assume the memory is free to reuse or unpin when it returns.

Point 4 is the reason this is not a drive-by change: it alters the memory-registration lifetime contract of the backend, and possibly of `nixlAgent::deregisterMem`, so it needs a maintainer decision on the intended semantics before implementation.

An alternative that avoids the contract change is to make the drain timeout configurable as "wait forever" (for example, treating a non-positive value as unbounded) and let deployments that prefer a hang to a use-after-free opt in. That is a smaller change but does not close the hole for the default configuration.

## Notes

- This is not a regression introduced by #2044 or #2045. Both PRs narrow the window that exists on `main` today; this issue tracks the part they explicitly do not close.
- The gap was raised by CodeRabbit during review of #2044, which agreed that a deferred-deregistration ownership model is the correct fix and is outside the scope of that PR.

Refs #2044, #2045.


## 评论 (3)

### iyastreb · 2026-08-10

Few points:
1) We need to understand the root cause of requests remaining forever in progress, this is clearly an error case, and normally shouldn't happen.
2) UCX already has timeouts and retry counts, normally that should be enough.
3) IMO adding timeout can mask the real issue, making it harder to find out. On the other hand it does not truly solve the problem, just delays it
4) Probably this requires proper request **invalidation**, that is implemented in UCX, but not supported by NIXL yet. If NIXL supports request cancellation, only in this case we can consider timeout approach

### iyastreb · 2026-08-25

As we see from the logs, the root cause of the hang is that:
- after network congestion we see a massive disconnect of EPs, followed by new connections
- some of the new connections remain in wireup mode forever and never promoted
- requests of these wireup EPs remain queued forever

So far I have identified 2 reasons why UCP EP remains in wireup mode:
1) UD connections use dest_id as an identifier, which is just a slot in the array, which is very likely being reused after connection is destroyed on linger timeout. So we have a situation ABA, when connection A is re-established and gets messages from stale B connection.
This is fixed by adding a generation id: https://github.com/openucx/ucx/pull/11800

2) Private UD EPs remain forever in the UNEXP queue, and being selected despite newer match exists.
On first UCP wireup request:
A private endpoint is created internally on CREQ, has no UCP endpoint above it => so keepalive never checks it => and UD never signals a closed remote endpoint.
When remote peer connection dies => private UD connection stays forever pointing at a dead ep_id

On UCP wireup reconnect request => uct_ep_create() matches that stale endpoint by addr+conn_sn => reuses it as is => wireup reply goes to the dead ep_id => connection never completes
The fix is in review: https://github.com/openucx/ucx/pull/11822

### linear-code[bot] · 2026-08-27

from mikhailb:
> Should be fixed by two UCX PRs mentioned by Ilia
