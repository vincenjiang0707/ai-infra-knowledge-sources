# [Issue #2049] CORE: per-request nixlXferReqH state is mutated under a shared (and by default no-op) agent lock

source: https://github.com/ai-dynamo/nixl/issues/2049
state: closed | updated: 2026-08-10T14:20:46Z
labels: 

## 正文

## Summary

Mutable per-request state on `nixlXferReqH` — `status`, `backendHandle`, and the `postTime_` field added by #2047 — is written by `nixlAgent::postXferReq`, `nixlAgent::getXferStatus` and `nixlAgent::releaseXferReq` while those functions hold only a *shared* acquisition of the agent-wide `data->lock`. Nothing serialises two of those calls against each other for the same handle.

This is pre-existing behaviour on `main`, not a regression. Filing it so the intended concurrency contract for a request handle can be stated explicitly, and enforced if that is the desired semantics.

## Detail

The three lifecycle entry points all take a shared lock and then write per-handle fields (line numbers against `main`, `src/core/nixl_agent.cpp`):

| Function | Lock | Writes to per-handle state |
| --- | --- | --- |
| `postXferReq` | `std::shared_lock<nixlLock>` (1138) | `status` at 1149 and 1198 |
| `getXferStatus` | `std::shared_lock<nixlLock>` (1238) | `status` at 1249 |
| `releaseXferReq` | `NIXL_SHARED_LOCK_GUARD` (1308) | `status`, then `backendHandle = nullptr` |

`data->lock` protects agent-level state such as `remoteSections_` and `backendHandles_`. Taking it in shared mode is correct for that purpose and is deliberate: it lets operations on *different* request handles proceed concurrently. It is simply not a per-handle lock, so it does not order two writers to the same `nixlXferReqH`.

Two further points make this worth stating rather than assuming:

- `NIXL_SHARED_LOCK_GUARD` expands to `std::shared_lock<nixlLock>` (`src/core/sync.h:97`), so `releaseXferReq` is a reader too, not a writer.
- `nixlLock` is mode-driven (`src/core/sync.h:24`), and under `nixl_thread_sync_t::NIXL_THREAD_SYNC_NONE` every lock and unlock callback is a no-op. Since `nixlAgentConfig::kDefaultSyncMode` is `NIXL_THREAD_SYNC_DEFAULT`, which aliases `NIXL_THREAD_SYNC_NONE`, the default configuration performs no locking at all. Even in `NIXL_THREAD_SYNC_RW` mode, a shared acquisition does not exclude another shared acquisition.

Concretely, a caller that polls a handle from one thread while posting or releasing the same handle from another gets unsynchronised access to `status`. That matters because `status` drives control flow on the release path: `releaseXferReq` reads it to decide whether to call `checkXfer` and `releaseReqH`, and clears `backendHandle` to stop the destructor releasing the backend handle a second time.

## Is this actually supported today?

Probably not, but it is not written down anywhere. The evidence that a request handle is intended to be single-threaded:

- `nixlXferReqH` is explicitly non-copyable and non-movable (`src/core/transfer_request.h`).
- It is caller-owned, with a lifetime running from `createXferReq` to `releaseXferReq`.
- All of its state is `private` with `friend class nixlAgent`, so the agent is the only mutator.

What is missing is an explicit statement in the public API documentation, and there is no assertion or debug check that would catch a caller violating it.

## Options

1. **Document the contract.** State in the `nixlAgent` API docs that a single `nixlXferReqH` must not be used concurrently from multiple threads, and that `data->lock` does not provide that guarantee. Lowest cost, and arguably sufficient.
2. **Enforce it.** Add per-request synchronisation covering `status`, `backendHandle`, `postTime_` and the telemetry fields, used consistently across post, poll, release and the destructor.

Option 2 is not a one-line change and needs a design decision first: `checkXfer`, `postXfer` and `releaseReqH` all enter backend code that takes its own internal locks, so holding a per-request lock across those calls raises a lock-ordering question against `data->lock` and against backend-internal locks. Partial coverage would be worse than none, because it would imply a guarantee the surrounding code does not provide.

If option 1 is preferred, this issue can be closed by a documentation change.

## Notes

- Not a regression from #2047. That PR adds `postTime_`, written in `postXferReq` and read in `getXferStatus`, which follows exactly the existing access pattern for `status` and introduces no new race class. If anything it is less consequential than the pre-existing one on `status`, since `postTime_` only feeds a stall-deadline comparison and does not drive the release or cancel paths.
- Raised during review of #2047 and withdrawn there as out of scope for a stall-timeout change; tracked here on its own.

Refs #2047.


## 评论 (1)

### iyastreb · 2026-08-10

Race condition was fixed recently: https://github.com/ai-dynamo/nixl/pull/1811
