# [Issue #4061] [RFC]: [TENT] Fault tolerance for the RDMA notification channel

source: https://github.com/kvcache-ai/Mooncake/issues/4061
state: open | updated: 2026-09-23T18:01:16Z
labels: RFC

## 正文

### Changes proposed

## Summary

A TENT notification is one RC SEND on the per-endpoint notify QP. Today a notification that was posted and then lost is gone; a peer whose control plane stopped answering blocks the calling thread for the full RPC timeout on every call; and nothing on the wire lets a receiver recognize a copy, so no resend is possible without producing duplicates.

This RFC proposes a seven-PR series. In stack order:

1. **Keep a retiring notify QP published until its completions are drained** - closes a receive-side loss the sender can never learn about.
2. **Read the notify QP's RTR/RTS attributes from `EndPointParams`** - both QPs of an endpoint on one retry budget.
3. **Fall back to the control plane when the RDMA notification channel is unavailable** - plus a receive drain that covers every transport.
4. **Fail fast on peers whose control plane stopped answering** - an unreachable-peer cache with a prober, and a bounded wait for a send slot.
5. **Return a control-plane failure as it is instead of refetching the segment** - a failed call is not a stale descriptor.
6. **Stamp notifications with a session and sequence number and drop duplicates** - the groundwork a resend needs.
7. **Resend notifications whose path failed on another rail or the control plane.**

The first three apply to `main` on their own. 4 depends on 3; 5 on 3 and 4; 6 on 3; 7 on 6 and 4. Every new wire behaviour is capability-negotiated, peers that do not opt in see byte-identical traffic, and no default timeout changes.

## Motivation

Reproduced by injecting faults into the notify QP or freezing the peer process with `SIGSTOP`, on one host with two BlueField-3 integrated ConnectX-7 VFs over RoCE v2, 2000 transfer-bound plus 2000 standalone notifications per run.

| Scenario | Today | With the series |
|---|---|---|
| Sender's notify channel disabled mid-stream | 500 of 4000 received; the END marker never arrived | 4000/4000, 0 duplicates |
| Receiver's notify QP moved to ERR mid-stream | 3743 of 4000; the ~256 sends in flight are flushed when the endpoint retires | 4000/4000, 0 duplicates |
| Endpoint retired by a thread other than the notify worker | up to 256 notifications per retirement dropped as "unknown QP" after the receiver already had them | 0 dropped |
| Frozen peer, no endpoint yet, `sendNotification` twice | 30.011 s and 30.001 s, one bootstrap timeout per call | 30.009 s once, then 0.000 s |
| Frozen peer, `submitTransfer` | 90.002 s: bootstrap 30 s + notify 30 s + descriptor refetch 30 s | 30.000 s |
| Peer freezes mid-stream while the initiator sends | one `sendNotification` blocked 59.289 s until the peer resumed | 31.000 s once, then 0 s |

Two things make this a coordinated series rather than a one-line fix.

The blocking happens on the thread that polls a batch - `maybeFireSubmitHooks()` runs `sendNotification()` under the batch shard lock - or on a transfer worker in `Workers::getEndpoint()`. One dead peer stalls its poller and its worker for 30 s per attempt, and every retry pays again. The 30 s is the yalantinglibs `coro_rpc` default; a frozen peer's kernel still completes the TCP handshake, so the connect never fails early.

And the loss cannot be fixed by resending alone. Consumers such as vLLM's KV-transfer completion accounting count notifications per request, so a duplicate is a double-counted completion that releases or decodes a block early. A resend therefore needs receiver-side deduplication first, which is why PR 6 precedes PR 7 and why peers that cannot deduplicate are deliberately never resent to.

## Non-goals

- **Changing any timeout default.** 5 s for the bootstrap and notify RPCs was measured and behaves correctly, but the defaults stay at the library's 30 s until bootstrap latency under a large-cluster start has been measured.
- **Receiver-side loss when a QP is moved to RESET.** The mlx5 provider cleans that QP's CQEs on the transition, so sends the NIC already acknowledged are lost with the sender seeing success. Covering it needs an application-level ACK, which does not belong in TENT. The ERR path, which is what real retirement uses, is covered by PR 1.
- **Exactly-once delivery.** The series gives at-least-once with a receiver window, and keeps at-most-once for peers that cannot deduplicate.
- **Restructuring the notify channel onto an SRQ or DC**, and broadcasting local port state to peers. Each is independent and small enough for its own PR.
- **The test-only fault-injection hooks and the two-process probe** used for the measurements are not part of any PR.

## Current mechanism

- `RdmaEndPoint::construct()` creates one RC notify QP per endpoint plus two host buffers of 256 x 64 KB, one for sends and one for receives, allocated whether or not the endpoint ever sends a notification. The receiver pre-posts all 256 RECVs; the sender flow-controls to 256 sends in flight and waited without bound for a free slot.
- `RdmaTransport::sendNotification()` takes the first enabled local context and the peer's NIC 0, bootstraps the endpoint over the control-plane RPC, and posts one SEND. The wire payload is `[name_len][name][msg_len][msg]`, nothing else.
- A completion error on the notify QP retires the endpoint, and the SENDs still in flight are flushed and dropped. With the notify QP's hard-coded attributes the error took 14.9 s to arrive on this NIC; on the data QPs' attributes it takes 3.6-3.8 s.
- `receiveNotification()` drains only the first transport that supports notifications, so a notification queued by the TCP transport is never handed out.
- The data path has `RailMonitor` and a reroute. Notifications have no health state, no alternate path and no resend.
- Control-plane RPCs have no per-call timeout and no memory of a peer that stopped answering.

## Design

### PR 1 - the receiver keeps a retiring notify QP published

Found while validating PR 7. When an endpoint retired, the receiver removed its notify QP from the QP-number table before the QP went to ERR. Notifications that had already landed but were still unpolled in the notify CQ then came back as "unknown QP" and were dropped - and because the sender's HCA had been acknowledged, its completion was a success and no resend could ever cover them. It happens only when the retirement comes from a thread other than the notify worker: a data-path worker after slice retries, the RPC thread on a peer re-bootstrap, store eviction. Measured with the retirement injected from a detached thread, 208 and 246 of 4000 were lost in two runs; with the fix, none.

The QP now stays in the table until `deconstruct()`, which already unpublishes it under the resource mutex that `handleNotifyRecv()` takes. `finishDestroy()` waits for the notify QP the way it already waited for the data QPs, because destroying a QP takes its unpolled completions with it. Flushes stay quiet because a retiring or disabled notify QP is treated as not ready in the completion classifier.

### PR 2 - notify QP attributes from `EndPointParams`

`path_mtu`, `min_rnr_timer`, `timeout` and `retry_cnt` now come from the same params the data QPs use, so both QPs of an endpoint run on one budget. `rnr_retry` stays pinned at 7: RNR NAKs are ordinary flow control on the endpoint's only SEND/RECV QP and must never retire it together with its data QPs. Dead-path reporting went from 14.9 s to 3.6 s, and the shorter RNR timer took a 2000-notification burst from p50 15.3 ms to 1.6 ms. The defaults themselves are unchanged.

### PR 3 - control-plane fallback

The three "nothing left the host" failures in `sendNotification()` become `DeviceNotFound` / `RdmaError`; the engine tries the next notification transport and then the control-plane `Notify` RPC, about 67 us over loopback when the peer is alive. `receiveNotification()` drains every transport, and an in-process notify callback is registered before the transports install so RPC-delivered notifications are not dropped by an RDMA-only engine. A bootstrap that failed because the RPC itself failed is not retried over RPC, so a dead control plane costs the one timeout the caller already paid. `notification/rpc_fallback` (default true) turns it off. A payload larger than the 64 KB slot now reaches the peer over RPC instead of failing.

### PR 4 - fail fast on dead peers

`CoroRpcAgent::call()` gains per-call timeouts and a flag saying whether a failure was transport level. `PeerHealth` is a process-wide record keyed by the peer's RPC address: a transport-level failure marks it for a cooldown doubling from 5 s to 60 s, during which the four control-plane RPCs fail at once, and any reply clears the mark. A prober re-checks marked peers every second, so a peer that comes back is usable again in about a second - measured 0.705-0.805 s after it resumed. `RdmaEndPoint::sendNotification()` waits at most 1 s for a send slot instead of forever, and the caller then takes PR 3's fallback.

Two consequences are called out in that PR's description: a slice whose bootstrap the peer never answered is no longer charged to the NIC pair, because fail-fast would otherwise trip a healthy pair into a cooldown of minutes; and a refused bootstrap - the peer answered, and said its device is down - is now told apart from a peer that did not answer at all.

### PR 5 - a failed control-plane call is not a stale descriptor

Three call sites turned a failed control-plane call into `NeedsRefreshCache`, which drops the thread's cached segment descriptor and fetches it again. Under the peer registry the segment name *is* the peer's address, so the refetch went to the peer that had just failed to answer: a second timeout, a thread left without a descriptor, and the refetch's error handed to the caller instead of its own. They now return the failure as it is and keep the descriptor. A central registry, which can legitimately hand out a new address, still refetches once and repeats the call only if the address changed.

### PR 6 - typed frame, capability, dedup

The notify QP gains a typed frame whose layout is byte for byte the classic engine's `CtrlFrame` v1, carrying a `(session, seq)` stamp, with the raw encoding as its payload. `BootstrapDesc::notify_proto` negotiates it, defaulting to 0 for peers that predate the field, and a typed frame goes only to a peer that advertised support. The receiver keeps a per-sender-session anti-replay window - a high-water mark plus 4096 bits - and drops a `(session, seq)` it has delivered before, whichever transport carried the copy. Unstamped notifications pass through. Nothing is resent by this PR, so it produces no duplicate on its own.

### PR 7 - resend on another path

Every posted notification that carries a stamp, to a peer that can deduplicate, stays in a per-endpoint pending table until its completion. When the notify QP is disabled or the endpoint retires, the whole table is handed to a dedicated resend thread, which walks the `(local NIC, remote NIC)` pairs - primary first - skipping pairs a per-peer health table has paused, for up to three attempts, and then offers the notification to the other transports and the control-plane RPC. The health table applies `RailMonitor`'s rules through the same configuration keys; it needs its own locked copy because `RailMonitor` is a worker thread's private lock-free state. The synchronous send path is unchanged apart from one atomic load and one hash-map insert.

The trade-off: while the primary pair is paused, *new* notifications to that peer go over another transport or the RPC rather than another NIC pair. Only notifications already in flight are rerouted.

### Configuration added

| Key | Default | PR | Meaning |
|---|---|---|---|
| `notification/rpc_fallback` | true | 3 | try other transports and the control-plane RPC when the RDMA channel is unavailable |
| `rpc/{request,bootstrap,notify,connect}_timeout_ms` | -1 (library default) | 4 | per-call timeouts |
| `rpc/probe_timeout_ms` | 2000 | 4 | the prober's own timeout |
| `peer_health/{enable,cooldown_ms,max_cooldown_ms,probe_interval_ms,max_age_ms}` | true, 5000, 60000, 1000, 600000 | 4 | unreachable-peer cache |
| `notification/proto` | 1 | 6 | 0 = raw frames and no stamping, exactly the old behaviour |
| `transports/rdma/rail_*` | existing values | 7 | reused by the notification path health table |

## Validation

Rebased onto current `main`; 69 of 69 tent tests green with the series, 63 of 63 on unpatched `main`. Every commit is formatted with clang-format 20 through `scripts/code_format.sh`, the CI format check passes, and `typos` at the pinned version is clean.

Hardware measurements come from a two-process probe on one host with two BlueField-3 integrated ConnectX-7 VFs over RoCE v2, `USE_CUDA=OFF`, 2000 transfer-bound plus 2000 standalone notifications per run followed by an END marker. The probe counts received notifications per `(session, seq)`, so duplicates are counted rather than guessed. The two arms were run alternately per scenario; the Motivation table above is that matrix. Rows that kill a notify QP need the initiator to stay alive about ten seconds after its last send, because the retry budget, the hand-back and the resend all happen after it.

Each PR carries its own unit tests and, for five of the seven, a negative control: one line weakened, the named test confirmed red, then restored. PR 7 went through two adversarial review passes, which moved the multi-pair scan off the caller's thread, added the peer to the health key, excluded raw frames from the pending table, and stopped a dead control plane from falling through to a second RPC wait.

## Open questions

**1. Should notifications ride the data QP as `WRITE_WITH_IMM` instead of a separate SEND channel?** This is the "most elegant" option we discussed on 1 September. I have not implemented it, but I did measure it with a small verbs program on the same host:

- As a one-hop notification, `WRITE_WITH_IMM` is indistinguishable from a 64 B SEND: 5.61-5.72 us against 5.69-5.73 us one way. The hop is not where the difference is.
- Per transfer of k x 64 KB over two lanes, a trailing 0 B immediate on each lane delivers the notification **one RTT earlier** than waiting for the data completions and then sending on the notify QP: 15.3 vs 25.4 us at k=4, 31.8 vs 42.1 us at k=16, and closed-loop throughput at k=16 rises 28%. Keeping the software fence and only moving the notification onto a data QP buys nothing: what costs the RTT is the fence, not the primitive.
- The cost is on the receiver, which must keep RECVs posted on every data QP. At a receive depth of 8 a 64 KB stream runs at 115 Gb/s and at 32 at 258 Gb/s, against 315-365 Gb/s at 128 and above.
- Open: the immediate carries 4 bytes, so a payload needs a convention in the data buffer or a side channel; ordering holds only within one QP, so a transfer striped over L lanes needs one immediate per lane and a receiver-side count, and the sender must emit one on every lane it used; and polling the data QPs' receive CQs is new engineering. A separate channel and a resend layer would still be needed for standalone notifications that have no transfer to ride on.

**2. Endpoint retirement semantics.** On the receive side the answer to "should the receiver keep the old QP mapped until its receive CQ is drained" turned out to be yes, and is PR 1. The sender side is still open: is the transport's resend thread the right owner of the pending table, or should ownership stay with the endpoint store until the replacement endpoint is up?

**3. Notification payload upper bound.** The slot is 64 KB and each endpoint pre-allocates 32 MiB whether or not it ever sends a notification. PR 3 already routes anything larger over RPC, and a 4-byte immediate carries no payload at all. What size should the API promise, and should the pre-allocation shrink or become lazy?

**4. GPUDirect visibility.** An immediate completion says the WRITE landed in the NIC's view; it does not guarantee the data is visible to a GPU kernel without a flush. If notifications move onto the data QP, does the flush live in the transport, or stay the consumer's responsibility as it is today?

## AI Assistance Disclosure

- [ ] No AI tools were used
- [x] AI tools were used (specify below)

The code, tests and measurements in this series were produced with Claude Code as a coding assistant. The author reviewed every change and checked every measurement against the logs.


### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (2)

### github-actions[bot] · 2026-09-12

Thanks for opening this issue, @xiaodouzi666!

| Field | Value |
|-------|-------|
| **Issue** | #4061 |
| **GitHub user ID** | `77219630` |
| **Reporter** | @xiaodouzi666 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### SongOf · 2026-09-23

One gap adjacent to PR 1 of this series, in case you want to fold it in.

#4062 made `finishDestroy()` wait for the notify QP through `notify_inflight_`, a real count of posted-and-not-yet-polled work requests. The data QPs are still gated on `wr_depth_list_`, which is the quota, not the hardware occupancy: `acknowledge()` calls `cancelQuota()` when it resolves slices that are still on the wire — the timeout sweep, the failure sweep, `resetInflightSlices()` — so after a software timeout the depth reads zero while the queue pair's work requests have not been flushed yet. `resetConnection()` moves the QP to ERR, and the next 1 Hz reclaim tick calls `finishDestroy()`, which sees zero depth and destroys the QP before the FLUSH_ERR completions come back. The 30 s backstop only covers a failed ERR transition, not a successful one still draining.

On mlx5/mlx4 nothing observable breaks, because the provider purges the QP's CQEs at destroy. But that is the only thing holding it up: #4092's orphan reaper frees a slice on "endpoint gone" precisely for this case, and a provider that still delivers those CQEs after destroy would hand a freed slice back to `handleCompletion()`; a provider that refuses to destroy a QP with outstanding WRs would leave the endpoint in `waiting_list_` forever. With Hygon, SHCA, AINIC and MACA arriving, neither behaviour has been checked. It also looks like the mechanism behind the "hung WRs wedge QPs silently" half of #3523.

The fix is the mirror of yours: a per-QP count incremented in `submitSlices()` under the QP lock next to `completions_owed` and paid in `handleCompletion()`'s exit guard, with `finishDestroy()` waiting on it instead of the quota. The #4263 stand-in device can drive the test without an RNIC.

Is this something you would rather take into the series, since it is the same function and you are already there? If not, I am happy to open it against current `main` in a few days. Either way I would keep it separate from #4092, which is merged.

