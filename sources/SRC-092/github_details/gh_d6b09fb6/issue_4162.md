# [Issue #4162] [RFC]: Shared Low-Overhead RDMA Congestion Control for TE and TENT

source: https://github.com/kvcache-ai/Mooncake/issues/4162
state: open | updated: 2026-09-16T14:23:15Z
labels: RFC

## 正文

### Changes proposed

## Proposal

Introduce a default-off software congestion controller shared by the classic Transfer Engine (TE) and TENT. After the transport resolves the actual RDMA path and immediately before posting a WR, the controller applies byte-window admission to both the device and route domains. Existing modules continue to own batch submission, QoS ordering, endpoint lifecycles, and final transfer completion status.

The goals are to reduce avoidable network pressure and repeated use of unhealthy paths while keeping the additional fast-path cost measurable and removable. Failure classification determines recovery scope. It must not turn one slow transfer or a temporary quarantine into a claim that a peer has permanently failed.

## Relationship to Existing Work

[PR #2489](https://github.com/kvcache-ai/Mooncake/pull/2489) proposes per-device AIMD in a TENT runtime plugin, and its discussion calls for coordination between congestion control and QoS. This proposal moves byte reservation to the resolved RDMA post boundary, adds route-scoped failure handling, and shares one policy core between classic TE and TENT. It is an integration alternative, not a second controller that should be enabled independently beside that plugin.

[RFC #2866](https://github.com/kvcache-ai/Mooncake/issues/2866) discusses hierarchical QoS budgets and work-conserving scheduling. The proposed composition is: QoS determines which tasks may run and in what order; the transport performs the final byte reservation on the selected device and route. When admission is denied, work remains with its existing queue owner. TENT continues to derive delivery rate from its existing posted/completed telemetry. A permit represents only a temporary admission reservation, not a second scheduling policy.

Before landing, the CC and QoS maintainers must agree on the hook location and a single policy authority. The current code and tests do not establish that this controller can be safely stacked with another unmerged controller.

## Controller and Transport Responsibilities

- The shared core owns AIMD windows, hysteresis, health states, generation fencing, admission permits, and normalized failure classification.
- Classic TE creates one device domain per worker context and one route domain per local context and remote-NIC path. A local-NIC handoff rebinds the route.
- TENT retains device selection, priorities, quotas, and endpoint rebuilds. Its adapter consumes existing device telemetry and route completion feedback.
- A permit reserves the complete slice byte count in both the device and route domains. A failed second reservation rolls back the first, and a terminal path releases each reservation exactly once. A partial post returns only the unposted reservation; posted attempts follow the transport's existing completion and reclamation lifecycle.
- The monitor updates policy. The data path does not query an HCA, read sysfs, capture packets, or emit per-request diagnostic logs.

This is software admission control. It neither implements DCQCN nor configures ECN or PFC. NIC-level congestion control remains independent.

## Failure Model, State Machine, and Recovery

Failure handling must answer two separate questions: whether the current RDMA object remains reusable, and whether the corresponding route is temporarily pressured, suspected of failure, or persistently unavailable. A QP error may require immediate retirement of that QP, but it does not by itself prove that an entire NIC or remote node has permanently failed.

### Failure Scope

| Evidence source | Minimum handling scope | Must not automatically expand to |
| --- | --- | --- |
| operation/WR/WC | Current operation and, when required, the current QP | Entire rail, device, or peer |
| QP/WQ/SRQ | Current QP and the current generation of dependent objects | Other independent QPs on the same GID or port |
| CQ | The CQ and all QPs associated with it | QPs that do not use that CQ |
| route/path | Current local-NIC to remote-NIC path | Other routes on the same device |
| port | QPs, GIDs, and routes on that port | Other ports or devices |
| device | Current local RDMA device | Remote peer or other local devices |

`FailureScope` limits how far the controller may isolate a failure. It does not take ownership of destroying or rebuilding existing QPs, CQs, or endpoints. Peer membership, leases, and global node removal remain responsibilities of metadata, the endpoint manager, and the upper control plane.

### Path State Machine

```text
HEALTHY --sustained pressure with success--> CONGESTED --healthy epochs--> HEALTHY
   |                                             |
   +--a few timeouts or hard errors------------> SUSPECT
                                                    |
                                                    +--success----> HEALTHY/CONGESTED
                                                    +--threshold--> QUARANTINED
                                                                         |
                                                                  cooldown expires
                                                                         v
                                                                     PROBING
                                                                    /       \
                                                               success      failure
                                                                  v            v
                                                               HEALTHY   QUARANTINED
```

- `HEALTHY`: normal admission; consecutive low-pressure successful epochs additively increase the window.
- `CONGESTED`: transfers still succeed, but drain time, backlog, or receiver pressure remains high; multiplicatively reduce the window without triggering failover.
- `SUSPECT`: route timeouts or QP/route hard errors have occurred but have not reached the threshold; stop growing the window and preserve existing recovery opportunities without declaring long-term unavailability.
- `QUARANTINED`: hard errors or timeouts reach the threshold, a CQ/port/device fatal event is observed, or a probe fails; reject new posts in the affected scope.
- `PROBING`: after cooldown, permit only a bounded probe on a new generation; success recovers from the minimum window, while failure returns to quarantine and starts a new cooldown.

Late feedback from an old generation, an old endpoint, or a replaced QP may only settle the old accounting record. It cannot change the replacement path's state. Software timeouts observed while the poller is stalled are suppressed for that control epoch so CPU scheduling or an unconsumed CQ is not mistaken for a network failure.

### Completion/WC Handling Matrix

| WC status | Normalized class/scope | Current-object handling | Controller and recovery action |
| --- | --- | --- | --- |
| `IBV_WC_SUCCESS` | `Success / operation` | Complete normally and release the permit | Record success and completed bytes; low-pressure epochs may grow the window; resolve prior blocking evidence for the task |
| Success while drain time/backlog keeps rising | `Congestion / route or device` | Continue using the QP | Expose `CONGESTED`; shrink only the window, without quarantine or rail replacement |
| `IBV_WC_RNR_RETRY_EXC_ERR` | `ReceiverPressure / QP` | Reconnect or rebuild the current QP through the existing lifecycle | Increase pressure only on the receiving route and back off; do not affect other receivers sharing the source NIC and do not declare the rail failed |
| `IBV_WC_RETRY_EXC_ERR`, `IBV_WC_RESP_TIMEOUT_ERR` | `RouteTimeout / QP` | The current QP is no longer safe to reuse; rebuild it through the existing lifecycle | One error or a count below the threshold enters `SUSPECT`; only threshold exhaustion or failure of a new-generation probe enters `QUARANTINED` |
| `IBV_WC_LOC_LEN_ERR`, `LOC_PROT_ERR`, `MW_BIND_ERR`, `LOC_ACCESS_ERR` | `LocalConfiguration / operation` | Fail the operation and fix the local length, MR, PD, access, or binding | Do not shrink the window or count a path failure; without other CC evidence, the task state is `UNKNOWN` |
| `IBV_WC_LOC_QP_OP_ERR`, `LOC_EEC_OP_ERR`, `LOC_RDD_VIOL_ERR`, `INV_EECN_ERR`, `INV_EEC_STATE_ERR` | `LocalConfiguration / QP` | Stop reusing and rebuild the incorrect local communication object | Do not interpret a local programming or configuration error as congestion or remote failure |
| `IBV_WC_BAD_RESP_ERR`, `REM_INV_REQ_ERR`, `REM_ACCESS_ERR`, `REM_OP_ERR`, `REM_INV_RD_REQ_ERR`, `REM_ABORT_ERR` | `RemoteMetadata / operation` | Refresh the address, rkey, permissions, metadata, and endpoint generation before the existing retry path runs | Window reduction cannot repair the error, and one event does not directly replace the rail; escalate only if the refreshed generation still times out or fails its probe |
| `IBV_WC_WR_FLUSH_ERR` | `DerivedFlush / QP`, not a root failure | Complete teardown/cancellation cleanup and release the permit once | Inherit the root cause that put the QP into ERR or destroyed it; a flush burst must not increment the failure count repeatedly |
| `IBV_WC_FATAL_ERR`, `GENERAL_ERR`, `TM_ERR`, `TM_RNDV_INCOMPLETE` | `Fatal / QP` | Immediately stop reusing the object and retain `vendor_err` | First count a QP/route hard error; quarantine after threshold exhaustion or probe failure without expanding directly to permanent peer failure |
| Unknown WC status | `Fatal / QP` | Fail closed, stop reusing the object, and retain the raw status and `vendor_err` | Handle at the minimum QP/route scope; require an async event or probe before expanding the scope |

`vendor_err` is retained only as diagnostic evidence. A nonzero value does not automatically expand failure scope. `LocalConfiguration`, `RemoteMetadata`, and `DerivedFlush` do not enter the AIMD hard-error counters; their existing request, metadata, or teardown owners handle them.

### Async Event Handling Matrix

| Async event | Normalized scope | Handling |
| --- | --- | --- |
| `IBV_EVENT_QP_FATAL`, `QP_REQ_ERR`, `QP_ACCESS_ERR` | QP | Isolate and rebuild the corresponding QP; count one route hard error without affecting other QPs on the same GID |
| `IBV_EVENT_WQ_FATAL`, `SRQ_ERR` | QP/dependent objects | Stop the affected WQ/SRQ and dependent QPs, and report at QP scope |
| `IBV_EVENT_CQ_ERR` | CQ | The CQ is unusable; isolate all associated QPs and treat it as immediately fatal evidence for the route |
| `IBV_EVENT_PATH_MIG_ERR` | route | Stop using the failed migration path and count one route hard error; remain `SUSPECT` below the threshold and let the existing rail/failover owner select another path |
| `IBV_EVENT_PORT_ERR` | port | Isolate device and route use through that port; wait for a recovery event, state query, and data-plane probe |
| `IBV_EVENT_DEVICE_FATAL` | device | Immediately isolate the entire local device without expanding the conclusion to remote-peer failure |
| `IBV_EVENT_PORT_ACTIVE`, `GID_CHANGE`, `LID_CHANGE`, `PKEY_CHANGE`, successful path migration, and other non-failure events | No direct failure | Let the existing topology/endpoint lifecycle refresh affected objects; require a new-generation probe before declaring recovery |
| Other unknown async event | None | Do not change congestion state; preserve handling and diagnostics in the existing event owner |

### Non-WC and Control-Plane Handling Matrix

| Signal or failure point | Handling | State/caller semantics |
| --- | --- | --- |
| `tryAcquire = kDefer` | Do not post; leave the slice in its existing transport queue; if the second domain rejects admission, roll back the first reservation | Record `BYTE_WINDOW`; task state is `CONGESTED` |
| `tryAcquire = kAvoid` on a quarantined path | Do not post; use the existing alternate rail or transport; do not count the avoidance again as a new hardware failure | Record `PATH_QUARANTINED`; task state is `LONG_UNAVAILABLE` |
| Generation changes after acquisition | Roll back both device and route reservations and resolve the current endpoint/path again | The old attempt cannot affect the new generation; without quarantine evidence, state is `UNKNOWN` |
| Synchronous rejection from `ibv_post_send` or an equivalent API when the WR was not handed to hardware | Release the unposted permit immediately; route the returned error through the existing endpoint/QP owner | Do not fabricate a WC; only normalized route/fatal evidence enters the controller |
| Software completion deadline while the CQ poller is making progress | Normalize as `RouteTimeout`; rebuild the current QP/endpoint through the existing lifecycle | `SUSPECT` and task `CONGESTED` below the threshold; long unavailability only after threshold exhaustion or probe failure |
| Deadline observed together with poller stall | Retain diagnostics but do not count a route timeout in that epoch | `UNKNOWN`; avoid blaming the network for CPU scheduling delay |
| Read-only `GetSegmentDesc` RPC service failure | Discard the failed connection and retry at most once; return the existing metadata error after the second failure | Do not change the congestion window; a later data-plane probe on the new generation determines route usability |
| Mutating notification/control RPC failure | Preserve single-attempt behavior; this proposal does not replay the operation | Return the existing control-plane error and avoid duplicate side effects |
| Stale metadata, rkey, address, or permission | Refresh metadata and endpoint generation, then use the existing retry logic | One event is `REMOTE_METADATA`/`UNKNOWN`; escalate only if the refreshed generation still times out |
| Explicit cancellation, QP teardown, or old-endpoint reclamation | Settle and release every in-flight permit once; classify later flushes as `DerivedFlush` | Do not create a new root failure; without other evidence, task state is `UNKNOWN` |
| All RDMA rails unavailable | Delegate to existing transport failover; the controller does not replace final completion status | `LONG_UNAVAILABLE` with explicit quarantine/no-path evidence; otherwise `UNKNOWN` |
| `RDMA_CM_EVENT_DISCONNECTED`, `UNREACHABLE` | Only when the transport already uses librdmacm, let the existing CM owner isolate and reconnect the connection | Route-scoped connection evidence; do not add an RDMA CM dependency solely for classification |
| `RDMA_CM_EVENT_DEVICE_REMOVAL` | Let the existing CM owner destroy the corresponding `rdma_cm_id` and isolate the local device | Device is persistently unavailable, but the remote peer is not proven permanently failed |

Mooncake does not add a second verbs event loop for this classifier. The completion path reuses existing `ibv_poll_cq` calls; the background path reuses existing `ibv_get_async_event` and `ibv_ack_async_event` handling. `ibv_query_qp` and `ibv_query_port` are allowed only on slow recovery paths for diagnostics, event handling, or pre-probe checks, never per request.

A QP in RTS proves only local QP state. An ACTIVE port does not prove that the remote endpoint, GID, route, and rkey are consistent. NIC counters such as `PortXmitWait`, ECN/CNP/PFC, and retransmissions are low-frequency supporting evidence only. A successful bounded data-plane probe on a new generation is the basis for declaring route recovery.

### Recovery Escalation

```text
operation error
  -> settle the operation/permit according to the WC class
  -> QP hard error: retire the QP and mark the route SUSPECT
  -> refresh metadata/rkey and create a new endpoint generation
  -> run a bounded data-plane probe
       success -> HEALTHY/CONGESTED, recover from a small window
       failure -> QUARANTINED, select another rail
  -> no usable route on the device: isolate the corresponding port/device
  -> every transport/route to the peer failed: notify endpoint/control plane
```

The congestion controller owns admission, quarantine, and recovery only at route/device scope. It neither turns a local RDMA failure into cluster membership removal nor bypasses existing transport failover.

## Caller Observability

The controller's five internal states do not map one-to-one to the four caller-visible states. `HEALTHY` normally projects to `NORMAL`. Byte-window deferral, receiver pressure, congestion feedback, and a route timeout that has not caused quarantine project to `CONGESTED`. `QUARANTINED`, no usable path, or a failed probe project to `LONG_UNAVAILABLE`. Local configuration, remote metadata, derived flush, a terminal failure without usable path evidence, controller-off mode, and unsupported transports project to `UNKNOWN`. `SUSPECT` and `PROBING` change task state only when the task actually observes blocking or quarantine evidence; callers must not infer task state from a background state alone.

| Task evidence | Minimal state | Caller guidance |
| --- | --- | --- |
| Successful completion with no unresolved anomaly | `NORMAL` | Handle normally |
| `BYTE_WINDOW`, `RECEIVER_PRESSURE`, `CONGESTION_FEEDBACK`, or `ROUTE_TIMEOUT` before quarantine | `CONGESTED` | Keep the task or retry with upper-layer backoff; do not mark the peer down |
| `PATH_QUARANTINED`, `PROBE_FAILED`, `NO_USABLE_PATH` | `LONG_UNAVAILABLE` | Try another rail or transport; let the control plane decide node status only after all paths fail |
| `LOCAL_CONFIGURATION`, `REMOTE_METADATA`, `DERIVED_FLUSH`, or `FATAL` without attributable current-path evidence | `UNKNOWN` | Inspect details and use existing error handling; do not automatically treat it as congestion or permanent failure |

The admission boundary does not split a slice. An empty domain may admit one valid complete slice larger than the current window, including while probing. The full byte count is reserved and blocks further over-window admission until it drains. Therefore the adaptive bound is `max(window, one indivisible slice)`, not an absolute 64 KiB probe limit. Existing transport static limits still apply.

The controller retains bounded anomaly evidence on the batch-owned logical task. Callers may query it read-only during the `(batch_id, task_id)` lifetime:

- The minimal query returns `NORMAL`, `CONGESTED`, `LONG_UNAVAILABLE`, or `UNKNOWN`. `LONG_UNAVAILABLE` means the current path remained unavailable through quarantine or recovery evidence; it does not prove permanent HCA or peer damage.
- The detailed query returns the same classification plus the most recent relevant reason, failure scope, affected path, observation time, resolution flag, attempt/generation, and any window, in-flight byte, and cooldown values available when the anomaly was observed. Unobserved fields remain explicitly unobserved.
- For a multi-slice task, the most severe unresolved state wins: long unavailability, then congestion, then normal. Path recovery or a new attempt clears the old active blocking classification. Late feedback from an older generation cannot overwrite the replacement attempt.
- A query never polls a CQ, posts a WR, advances transfer progress, actively probes a path, or reads verbs/NIC control state. The caller queries before freeing the batch. A whole batch rejected before task creation continues to use the existing submission error because no task ID exists.

Classic TE and TENT expose identical semantics through C++ and C, and the existing TENT Python binding provides both minimal and detailed queries. The interface is transport-neutral, but the first implementation records congestion evidence for RDMA only. Unsupported transports, controller-off mode, or insufficient evidence return `UNKNOWN`. Existing `getTransferStatus` and `tent_task_status` layouts remain unchanged; this proposal does not add a combined `*StatusEx` API.

A later Mooncake-pro PUT integration may wait for completion, query a failed task before `free_batch`, and carry the classification in its error path. Upper-layer product integration is not part of this RFC's first implementation.

## Configuration, Compatibility, and Rollback

The controller is compiled only with `MOONCAKE_ENABLE_ADAPTIVE_CC=ON`; the default is `OFF`. A worker reads `MC_ADAPTIVE_CC_MODE=off|observe|enforce` at construction:

- `off`: bypass policy and admission state.
- `observe`: record signals and compute policy without deferring or avoiding work.
- `enforce`: apply byte admission and path quarantine.

All state-machine parameters are adjustable before startup:

| Parameter | Meaning |
| --- | --- |
| `MC_ADAPTIVE_CC_MIN_WINDOW_BYTES` / `MAX_WINDOW_BYTES` | Minimum and maximum byte windows |
| `MC_ADAPTIVE_CC_TARGET_DRAIN_US` | Target drain time |
| `MC_ADAPTIVE_CC_HIGH_PRESSURE_EPOCHS` / `LOW_PRESSURE_EPOCHS` | Consecutive control epochs required to enter congestion or resume window growth |
| `MC_ADAPTIVE_CC_HARD_ERROR_THRESHOLD` | Accumulated route timeout/hard-error threshold before quarantine |
| `MC_ADAPTIVE_CC_COOLDOWN_MS` | Quarantine cooldown |
| `MC_ADAPTIVE_CC_PROBE_WINDOW_BYTES` | Bounded admission window in `PROBING` |

Every numeric value must be positive. The minimum window must not exceed the maximum, and an explicitly configured probe window must not exceed the minimum window. An invalid setting fails worker initialization and leaves the controller off rather than continuing with a partially defaulted configuration.

Rollback currently means draining requests and restarting with mode `off`; changing process environment variables does not hot-switch existing workers. Compile-time `OFF` removes controller fields and code. Consumers and libraries that exchange transport types must use matching public C++ layouts. CMake dependencies must propagate the CC compile definition; manually compiled ON/OFF objects must not be mixed.

The TENT Python extension ships in the existing Mooncake wheel rather than a separate version chain. A TENT build places the extension and runtime dependencies in the `mooncake` package and retains compatibility with top-level `import tent`. Installation acceptance must run from a fresh environment using the repaired wheel, not a build-directory `PYTHONPATH`.

## Performance Acceptance

Proposed gates are at most 1% regression when the controller is compiled in but runtime mode is `off`, and at most 3% large-transfer throughput regression for healthy `enforce`. These are acceptance targets, not conclusions established by a single observation.

Comparisons among compile-out, runtime off, observe, and enforce must fix the HCA, peer, firmware, CPU/NUMA placement, message sizes, workload, and measurement interval. Each arm starts from independent process, queue, and connection state, or applies an identical documented warm-up. Record source and binary identities, CPU cost, throughput, latency tails, queue peaks, actual controller state, and payload correctness. Report small-message costs separately. In addition to healthy bulk transfer, test incast, route recovery, and multi-NIC failure.

The CPU microbenchmark measures the controller, not end-to-end request p99. Soft-RoCE can verify software paths but cannot qualify physical-HCA performance or fabric behavior.

### Before submitting a new issue...

- [ ] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (1)

### github-actions[bot] · 2026-09-16

Thanks for opening this issue, @Bo-Vincent!

| Field | Value |
|-------|-------|
| **Issue** | #4162 |
| **GitHub user ID** | `205891898` |
| **Reporter** | @Bo-Vincent |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
