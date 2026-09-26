# [Issue #3937] [RFC]: Master client-expiry circuit breaker — a master stall must not erase the whole cluster's cache index

source: https://github.com/kvcache-ai/Mooncake/issues/3937
state: closed | updated: 2026-09-21T04:33:15Z
labels: 

## 正文

**TL;DR.** Today a stall in `mooncake_master` longer than `client_ttl` (10 s by default) makes the master expire *every* client and erase the entire cluster's cache index — irreversibly — and the stall that does it is triggered by the most routine operation there is: starting a store. This RFC proposes a circuit breaker in `ClientMonitorFunc` that defers an expiry the master cannot rule out as its own stall, bounded by a grace, and judges on the **cause** (an exclusive `client_mutex_` hold) rather than the symptom (how many clients expired). Implementation: #3936.

## 1. The problem: a transient control-plane stall becomes permanent, cluster-wide data loss

`ClientMonitorFunc` expires a client whose heartbeat deadline has passed. It decides this from the **absence** of heartbeats, and absence looks exactly the same whether the clients died or the master stopped serving `Ping`. Expiry is irreversible: the client's segments are unmounted and every key they held is erased from the index; nothing in the master undoes it.

The master does stall. `Ping`'s body is a shared-lock read of `ok_client_` plus a push onto a lock-free queue, so an **exclusive `client_mutex_` holder is the one thing that stops the handler running at all** — and because coro_rpc runs a non-coroutine handler inline on the io thread, io threads blocked on that lock stop reading pings off their connections entirely. We measured `master_ping_requests_total` completely flat for nine consecutive seconds during one such hold.

### Why this must be fixed, not tolerated

- **The trigger is the rollout path.** `ReMountSegment` is the only way into `ok_client_`, so every store start goes through it — a deploy, a rolling update, a scale-out, an eviction, a node reboot. The operations run most often are the ones that can wipe the cache.
- **One node joining freezes the master for every node.** The blast radius is the whole cluster, not the node being rolled.
- **The penalty is charged in the currency operators are trying to save.** Re-warming a cache costs far more than the pod boot that preceded it, so a fleet roll turns into a roll followed by a long cold period. The rational response is to stop restarting store pods — which is the opposite of fast, frequent deploys, and it blocks ordinary scale in/out.
- **It is not a corner case at scale.** Measured on our rig, the metadata scan in `ReMountSegment` took 0.72 s at 1M keys, 9.76 s at 14M, 13.2 s at 18M — against a 10 s `client_ttl`, a threshold near 14.2M keys. One of our production deployments lost its whole cache index to a single store restart at 13.9M keys — under the rig's threshold, because a production master contends for CPU the rig does not — and holds 14.6M in steady state today.
- **#3533 helped but the exposure is structural.** It removed the largest scan on that path. Any exclusive `client_mutex_` hold that outlasts `client_ttl` — present or future — reproduces the same irreversible outcome. The defaults are also inconsistent: the master gives up on a client after 10 s, while the client waits 30 s for the master (coro_rpc's default `request_timeout_duration`, unless `MC_RPC_TIMEOUT_MS` is set) and retries three times before reconnecting.

## 2. Proposal: defer an expiry the master cannot rule out as its own stall

A circuit breaker in `ClientMonitorFunc`. When a tick's expiry candidates cannot be distinguished from the master's own stall, hold them back — a true no-op: no unmount prepared, no sweep started, `client_ttl` untouched — bounded by `client_mass_expiry_grace_sec` (default 60). Recovery needs no machinery: the next queue drain refreshes the deadlines and the episode closes itself.

The judgement is a pure function, `EvaluateClientMassExpiry`, over one tick's readings. Two conditions:

1. **Primary — the cause.** An exclusive `client_mutex_` hold overlapped `[last_ping_batch_at, now]`, the stretch over which this master has no heartbeat of its own to show. Each exclusive site (`ReMountSegment`, `UpdateClientHostId`, `ResetStateAfterFailedRestoreAttempt`) records its hold window into relaxed atomics via an RAII guard; the monitor's own expiry branch deliberately does not, so a previous tick's expiry cannot come back as evidence of a stall.
2. **Secondary — silence.** No heartbeat was popped after the newest candidate went overdue (`last_ping_batch_at < newest_expired_deadline`), counted only with **≥ 2 tracked clients**: with exactly one, hearing nothing says only that that client stopped, which must be acted on at once.

**Why the window opens at `last_ping_batch_at`.** It has to get two cases right at the same time:

- A hold that released *before* the last heartbeat was popped is refuted by that heartbeat — the master demonstrably served `Ping` afterwards — so an ordinary single-client death expires after one TTL, not after the grace.
- A hold that released while the master *stays* starved (no heartbeat popped since) remains evidence. After a release the master can stay starved for many more ticks — we observed 8.5–9.6 s of post-release starvation from the `UnmountSegment` → `ClearInvalidHandles` sweep at 14M keys — so a wall-clock "holds within the last tick or two" window would age out mid-stall and erase the cache.

Surface: flags `--client_mass_expiry_guard` (default `true`) and `--client_mass_expiry_grace_sec` (default `60`, clamped to 0 with `action=config_clamped` if negative, including via config file); metrics `master_client_expiry_deferred_total` and `master_client_expiry_deferred_clients`; logs `action=client_mass_expiry_deferred` (WARNING on the episode's first tick, INFO after) and `action=client_mass_expiry_grace_exceeded` (ERROR — the master is about to do the unrecoverable thing).

## 3. Alternatives considered

| alternative | why not |
| -- | -- |
| **Symptom-based threshold** ("N or x% of clients expired in one tick") | Defeated by tick-splitting. A deadline is stamped by the tick that popped that client's heartbeat, so a stall's expiries spread across consecutive ticks and each tick's share falls under any threshold. Tried twice before the cause-based rule. |
| **Wall-clock recency window** for completed holds | Unsafe: ages out during post-release starvation (§2, second case) and erases the cache. |
| **Raise `client_ttl` alone** | Moves the threshold (60 s → ~46–60M keys) without removing the irreversibility. Worth doing for default consistency, but orthogonal. |
| **Snapshot / standby recovery** | Recovery, not prevention, and unavailable to non-HA deployments. |
| **Make the master non-blocking** (async handlers, dedicated threads for shard walks) | The right long-term direction and a much larger change. The breaker is orthogonal to it and makes that path safe to keep optimizing: a regression becomes a bounded deferral instead of a cluster-wide loss. |

## 4. Behaviour change a reviewer should weigh

A **genuine simultaneous death of every client is deferred up to the grace bound** before expiry. This is inherent, not an oversight: a vanished fleet and a totally stalled master produce identical heartbeat streams — none — so no rule can separate them. The cost is bounded (60 s), observable (metrics + `LOG(ERROR)`), and buys the difference between a bounded delay and an unrecoverable wipe. `--client_mass_expiry_guard=false` restores the previous behaviour exactly.

Two gaps stay open and are stated in the code: a **single-client** deployment starved by something other than a `client_mutex_` hold records no hold, and one tracked client is not silence evidence, so its keys still go (closing it needs a liveness signal off the data path); and the whole-fleet case above.

## 5. Verification (details in #3936)

Reproduced and gated on a 13-client deployment, master under production limits (8 CPU, 60 GiB).

- **The stall, 18M keys:** a joining client's remount held the lock 13.8 s vs a 10 s TTL. With the breaker: zero expiries, key count held at 18,000,000, the episode closed itself 3 ticks after the hold released. Without it: all 13 expire in one tick and the sweep erases the keys.
- **No false positive:** one client killed while others keep pinging expires after one TTL (10.66 s), zero deferral ticks.
- **Single-client, both directions:** a lone death expires 1.4 s after `SIGKILL`; a genuine stall defers on hold evidence alone and keeps its keys.
- Unit tests on `8715bb7c`: `master_service_test` 80/80, config 9/9, breaker cases 11/11 (7 wall-clock, 4 pure), `master_service_group_test` 13/13. Mutation-checked: deleting the primary condition fails only the stall and tick-split cases; pinning the window's left edge fails only the ordinary-death case.

## 6. Questions for maintainers

1. Default **on** (proposed) or off?
2. Is 60 s the right default grace? It is the client's 30 s RPC wait plus retries plus margin.
3. Should hold recording be folded into a lock wrapper type so a future exclusive `client_mutex_` site cannot forget the guard? Today it is three RAII placements with no compile-time enforcement.
4. Should the `client_ttl` (10 s) vs client RPC timeout (30 s) default inconsistency be fixed in a follow-up?


## 评论 (2)

### github-actions[bot] · 2026-09-08

Thanks for opening this issue, @Juhyun-Kim-Memphis!

| Field | Value |
|-------|-------|
| **Issue** | #3937 |
| **GitHub user ID** | `32131411` |
| **Reporter** | @Juhyun-Kim-Memphis |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### Juhyun-Kim-Memphis · 2026-09-21

Closing together with #3936, which this RFC proposed. The cause of the mass expiry is now addressed directly under RFC #4181: #4180 takes `Ping` off the data-plane locks, and #4183 takes it off the data-plane threads.
