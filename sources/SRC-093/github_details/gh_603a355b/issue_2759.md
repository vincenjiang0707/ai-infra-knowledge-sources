# [Issue #2759] [Feature] Panic recovery for the gateway plugin gRPC server

source: https://github.com/vllm-project/aibrix/issues/2759
state: closed | updated: 2026-09-23T14:38:23Z
labels: area/gateway, kind/feature

## 正文

### 🚀 Feature Description and Motivation

The gateway plugin has no panic recovery, so any panic on the ExtProc request path kills the whole `aibrix-gateway-plugins` pod and every request in flight on it. `grpc.NewServer` in `cmd/plugins/main.go` is created with OpenTelemetry stats and a max message size, nothing else, and ExtProc handling runs in that server's stream handler, including pod selection and SLO queue ranking. One request-path defect ends the process instead of the single request.

This isn't hypothetical. While working on the routing path I hit one such crash: `ModelGPUProfile.GetSignature` panics with index out of range on a malformed profile, and the root-cause fix for it is underway in #2756. There are earlier cases on the same path: #1284 (`panic: runtime error: index out of range [-1] in gateway queue`) and #2049 (gateway-plugins pod restart under high concurrency). The blast radius is always the same: one defect takes down all in-flight traffic on that pod until it restarts.

Motivation: turn "any panic = full gateway outage" into "the affected request fails, everything else keeps serving", with a stack trace and a counter for diagnosis. This limits blast radius. It doesn't replace fixing root causes.

### Use Case

A shared gateway serving many tenants. Today one malformed artifact, say a bad `aibrix:profile_*` cache entry, can crash the shared gateway pod: all in-flight requests fail and clients see errors until the pod comes back. With a recovery layer, only the affected request fails, other requests continue, and operators get a stack trace plus a counter instead of a restart.

### Proposed Solution

Add a recovery layer at the gRPC server boundary. If you're open to it, this is the scope I'd implement:

- a stream interceptor wired into `grpc.NewServer` in `cmd/plugins/main.go`, next to the existing OTel stats handler, with a `defer`/`recover` at the top of `Process` as the fallback;
- on panic: log the stack trace, increment a counter metric, and fail only that stream with `codes.Internal`, no silent swallowing;
- a unit test with a panicking handler;
- no new dependency, and no change when nothing panics.

There's already precedent for this in `SlowStartBatch` (controller utils), so recovering panics isn't a new pattern for the project. It covers ordinary panics (index out of range, nil dereference, failed type assertion); it can't catch runtime-fatal conditions such as concurrent map writes or OOM, and no recovery layer can.

Before I write anything, two questions. Is a stream interceptor the right home, or would you prefer recovery inside `Process`? Also, any constraints to follow, such as metric naming or error mapping? Happy to be assigned and implement it if the direction looks right. Asking first because it changes runtime behavior on the request path.

### Area

Gateway

## 评论 (3)

### github-actions[bot] · 2026-09-20

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### bolubo · 2026-09-22

Implemented in #2776: a stream interceptor on the plugin gRPC server plus a `Process`-level fallback, a `gateway_request_panic_total` counter, and a server-level test that a panicking stream fails alone.


### bolubo · 2026-09-23

Status: both paths in the issue body now recover on main.

- #2776 (merged 2026-09-22) landed the recovery layer: a stream interceptor on the plugin gRPC server, a `Process`-level fallback for callers that bypass the transport, `gateway_request_panic_total`, and a server-level test where a panicking stream ends with `codes.Internal` and the next stream still runs.
- #2781 (merged 2026-09-23) extended the same treatment to the queue router serve loop behind the SLO queue: peek, route and dequeue each run under a recover, the request behind a recovered panic fails alone, and the drain loop continues; it stops deliberately only when a panic inside `Dequeue` leaves the queue position unknown. The panic is logged with its stack and counted under the same metric.
- The `ModelGPUProfile.GetSignature` crash this issue cites has its root-cause fix merged in #2756.

Fatal conditions a recover cannot catch (concurrent map writes, OOM) stay out of scope by design, same note as in #2776.

Nothing in the issue body's proposed scope looks uncovered, so closing this as implemented.
