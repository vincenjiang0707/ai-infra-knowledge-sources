# [Issue #2364] [Store] RDMA memory leak on MountSegment RPC failure

source: https://github.com/kvcache-ai/Mooncake/issues/2364
state: closed | updated: 2026-09-13T03:14:56Z
labels: stale, auto-closed

## 正文

## Problem

In `Client::MountSegmentAndGetId()` (`client_service.cpp:2692`), when the `MountSegment` RPC fails, the RDMA memory registered at line 2675 via `registerLocalMemory()` is never unregistered, leaking the registration.

## Why a simple fix is insufficient

As @ykwd pointed out in #2345, simply calling `unregisterLocalMemory()` on RPC failure is unsafe: the master may have actually succeeded but the response was lost in transit. In that case, the client would unregister memory that the master still considers valid, leaving the system in an inconsistent state.

## Possible approaches

1. **Idempotent mount with retry** — retry the mount RPC before giving up; if the master already has the registration, it returns success
2. **Client-side reconciliation** — on startup or reconnect, reconcile local RDMA registrations with master state
3. **Lazy cleanup with TTL** — master-side expiration of stale registrations

## Context

- Discovered during #2345 code review
- The `unregisterLocalMemory` cleanup was removed from #2345 per reviewer feedback

## 评论 (2)

### github-actions[bot] · 2026-09-06

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-13

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.
