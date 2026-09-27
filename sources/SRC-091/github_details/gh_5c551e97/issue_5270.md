# [Issue #5270] MP client: unanswered STORE/RETRIEVE RPCs cause unbounded client-side memory leak after GPU context loss

source: https://github.com/LMCache/LMCache/issues/5270
state: open | updated: 2026-09-21T01:35:09Z
labels: 

## 正文

## Summary

In a 3P1D deployment using vLLM + LMCacheMPConnector + per-node LMCache sidecars, a sidecar can lose a worker GPU context while the client remains active. Subsequent STORE and RETRIEVE blocking handlers raise a missing-GPU-context ValueError. The server logs the exception but does not return a response to the DEALER client.

The primary impact is an unbounded client-side memory leak, not only a server-side error. A MessageQueueClient pending future is removed only after a response arrives. When the response is omitted, the future permanently retains its request payload, including token IDs. The vLLM worker adapter also waits for that future to complete before removing per-request store/retrieve futures and CUDA IPC events. Every later failed request therefore leaks future, request-key/token payload, and event state; memory grows linearly with request rate until the worker container approaches its memory limit.

## Observed evidence

Three sidecar logs were inspected. p1 and p2 show the same persistent fault; p3 does not.

| Sidecar log | Blocking-handler errors | Missing instance GPU context | Missing model GPU context during lookup |
| --- | ---: | ---: | ---: |
| p1 | 5,932 | 11,864 | 17,260 |
| p2 | 5,976 | 11,952 | 17,625 |
| p3 | 0 | 0 | 0 |

Representative p1 sequence:

1. 2026-09-18 08:25:39.639: lookup reports no GPU context for the model/world-size pair.
2. 2026-09-18 08:25:39.749: mq.py _notify_response logs Error in blocking handler.
3. The handler ends with ValueError: No GPU context registered for instance ID.
4. The failures repeat continuously; Session not found, skipping touch warnings also appear.

The logs show that the sidecar runs a 30-second worker reaper. They prove the missing-context and silent-RPC-failure pattern, but do not by themselves prove the exact reaper decision that removed a particular context.

## Expected behavior

A failed blocking RPC must always resolve its client future with an explicit failure. Independently, clients need bounded cleanup for every unanswered request. A failed async retrieve must surface its failed block IDs so the serving engine recomputes rather than consuming unloaded KV.

## Proposed direction

1. Add TTL-based cleanup for unanswered MessageQueueClient pending requests; expire them with a dedicated exception and remove pending state.
2. Make device-aware futures propagate the expiry without attempting CUDA event import.
3. Make the vLLM worker adapter treat expiry as a completed failed STORE/RETRIEVE, remove per-request futures/events, and report failed retrieve block IDs.
4. Follow up with server-side error responses and worker re-registration or health signaling so this failure is immediate rather than TTL-delayed.

## Reproduction outline

1. Start an MP sidecar and a vLLM worker.
2. Cause the server to lose or reap the worker GPU context while the client stays alive.
3. Submit STORE or RETRIEVE for the stale instance ID.
4. Observe repeated missing-context errors on the server and unanswered client RPCs; inspect client pending future and worker per-request collections for growth.

## 评论 (2)

### wuwanxu · 2026-09-20

## Additional log evidence

The following details come directly from the collected sidecar logs. They strengthen the failure chain, but do not establish the exact condition that caused a specific GPU context to be reaped.

### Log volume and error counts

| Log | Total lines | `Error in blocking handler` | `No GPU context registered for instance ID` | `No GPU context found ... during lookup` | `Session ... not found, skipping touch` |
| --- | ---: | ---: | ---: | ---: | ---: |
| `lmcache_p1.log` | 138,509 | 5,932 | 11,864 | 17,260 | 26,174 |
| `lmcache_p2.log` | 139,549 | 5,976 | 11,952 | 17,625 | 26,145 |
| `lmcache_p3.log` | 202,174 | 0 | 0 | 0 | 317 |

P1/P2 have persistent missing-context failures; P3 has no such failures despite having a larger log. This makes the P1/P2 issue unlikely to be a generic logging artifact.

### Representative P1 failure chain

- The first observed missing model GPU-context message is at `2026-09-18 07:50:25.405`.
- At `2026-09-18 08:25:39.639`, lookup reports that no GPU context is available for the relevant model/world-size pair.
- At `2026-09-18 08:25:39.749`, `mq.py` logs `Error in blocking handler`; the handler terminates with `ValueError: No GPU context registered for instance ID ...`.
- This sequence then repeats at high volume in P1/P2.

The sidecar logs also show a worker reaper with a 30-second interval. The evidence establishes: missing context -> blocking handler exception -> no successful RPC completion. It does **not** establish from logs alone why the reaper removed a particular context.

### Why these server logs imply a client leak

For each failed request above, the server exception path does not send a reply to the DEALER client. Thus the client has no response-driven path to remove its `MessageQueueClient.pending_futures` entry. The client-side future continues to retain its request payload (including token IDs); the vLLM adapter keeps corresponding `store_futures` / `retrieve_futures` and CUDA IPC events until that same future completes. Under sustained traffic, the number of retained objects grows with the number of unanswered RPCs.

### Lipenghee · 2026-09-21

I would like to take the bounded client-cleanup part of this issue.

The current failure path is reproducible without a GPU by submitting a blocking request whose server handler raises or never replies: the DEALER future remains in `MessageQueueClient.pending_futures`, and the vLLM adapter continues retaining its per-request future/event state. I plan to add deterministic fault-injection regressions for that path, introduce an explicit request deadline that expires and removes pending entries with a dedicated exception, and make STORE/RETRIEVE completion consume that terminal failure so failed retrieve block IDs are returned for recomputation and all adapter state is released.

I will keep worker-context re-registration and the underlying GPU-context-loss cause out of scope. I will also avoid inventing a server error protocol in the same patch unless the existing response schema supports it cleanly; the first acceptance target is bounded cleanup and safe recomputation when a reply never arrives.
