# [Issue #4181] [RFC]: [Store] The client heartbeat path must share no lock or thread with data-plane operations

source: https://github.com/kvcache-ai/Mooncake/issues/4181
state: open | updated: 2026-09-21T06:26:30Z
labels: 

## 正文

### Changes proposed

**Make the client heartbeat path share no contended resource with data-plane operations.** On `main` a `Ping` waits for `client_mutex_` (held exclusively by every client-state writer), for the calling client's liveness-record mutex (held for the whole lifetime of a serving/retaining guard), and for the one io thread that owns its connection, which also runs data-plane handlers. Any of the three lets a slow control-plane operation stop a live client from being observed, and the master then moves healthy clients to `SUSPECTED` and, after the suspicion TTL, to `OFFLINE`, which offboards their segments and erases the keys on them.

Two changes remove the three dependencies:
- **Lock dimension: #4180.** Its session registry replaces `client_mutex_` and the guards, and leaves `Ping` with only O(1) critical sections (§2.1). Our smaller #4182 did the same on `main`'s structure; it is closed in favour of #4180.
- **Thread dimension: #4183.** A separate single-thread RPC server for `Ping` (§2.2). #4180 does not touch RPC threading.

This RFC states the invariant they establish together, so that future changes cannot silently reintroduce the dependency.

> **Invariant.** The liveness path, from a `Ping` arriving at the master until its observation is recorded, and the monitor deciding a transition, never waits for a resource that a data-plane operation can hold for a data-dependent time.

### 1. Why this needs a structural fix

In production, one store pod restarting on a master holding 13.9M keys made every one of the 12 live clients expire at once and erased the index from 13.9M keys to 0.43M. That build predated #3533. We reproduced the chain on a rig and described it in #3937: the joining client's `ReMountSegment` walked all metadata shards under exclusive `client_mutex_`, no `Ping` could be served, and the monitor expired everyone.

On `main`, #3533 limits that walk to remounts after an HA promotion, and `UnmountSegment` runs its O(keys) `ClearInvalidHandles` sweep synchronously only with HA, snapshot or CXL enabled. So the known triggers now need one of those modes. In those modes they are still on the rollout path (deploy, roll, scale-out, eviction, node reboot), and the invariant itself is still unwritten.

#3936 proposed a circuit breaker for the resulting mass expiry. As @ykwd noted there, that is a mitigation: it withholds the consequence and leaves the cause (#3936 is now closed). #2991 (RFC #2953) made the consequence recoverable, since a heartbeat gap now yields `SUSPECTED` before `OFFLINE`, but the cause is unchanged, and the number of places that can trigger it grew:

| exclusive `client_mutex_` holder on `main` (d9e4dcbc) | note |
| -- | -- |
| `MountSegment` | exclusive since #2991 (previously did not take the lock) |
| `ReMountSegment` | includes the 1024-shard walk when standby-restored memory is kept alive (HA promotion) |
| `ProcessClientOffboardingJob` | new in #2991 |
| `MountLocalDiskSegment` | |
| `RestoreFromStandbyState` | whole restore |
| `ClientMonitorFunc` retirement, `UpdateClientHostId`, `ResetStateAfterFailedRestoreAttempt`, `RebuildClientLivenessAfterSnapshotRestore` | |

and `Ping` now records the heartbeat itself inside that lock (`record->Observe()` under `client_mutex_` shared), where it previously pushed onto a lock-free queue.

How the invariant was lost, in four steps that were each reasonable on their own:
- #501 introduced `ok_client_`, the status lookup in `Ping` and exclusive `client_mutex_` in `ReMountSegment`: HA-only, bounded work.
- #845 removed the HA gate, so every deployment runs this path.
- #2826 put the standby validation and the full shard walk inside that exclusive section.
- #2991 moved heartbeat recording under the lock and added exclusive holders.

Nothing in the code says "`client_mutex_` is on the heartbeat path, so keep its critical sections short", so no review could catch any of these. Narrowing one holder's lock restores that promise once; the invariant removes the need for the promise.

### 2. Design

**2.1 Lock dimension (#4180).** As of 4da335ab, `Ping` goes through `ClientSessionRegistry::Ping`: a lookup under the registry's own mutex (shared), `ClientLivenessRecord::Observe` under the record's `transition_mutex_`, and a readiness check under the registry mutex (shared) again. `client_mutex_`, `ServingGuard` and `RetainingGuard` no longer exist. Registrations and remounts take a per-client operation lock exclusively, and admitted operations take it shared; `Ping` never takes it. #4182 reached the same property on `main`'s structure with an immutable client view and a try-lock heartbeat; equivalents of its two tests that fail on `main` pass against #4180's registry.

**2.2 Thread dimension (#4183).** coro_rpc gives each io thread its own `io_context`, binds an accepted connection to one of them for its lifetime, and runs non-coroutine handlers inline on the thread that read the request. A `Ping` is therefore read only by the io thread that owns its connection, and if that thread is inside a long handler the `Ping` waits for it, even when every other io thread is idle. New connections are accepted on io thread 0.

`--heartbeat_rpc_port` (default 0, non-HA) starts a second `coro_rpc_server` with one io thread that serves only `Ping` and `ServiceReady`, advertised through a new `GetHeartbeatRpcPort` RPC. `MasterClient::Connect` discovers it and sends `Ping` there once it answers, from a connection pool of its own. The main server keeps serving `Ping`, so an old client, an old master, or an unreachable heartbeat server all fall back to today's behaviour with no coordination. This is the design of #3541 on the P2P branch, applied to `main`'s `Ping`, with the port discovered rather than configured on every client.

**#4183 depends on the lock dimension.** With a single heartbeat thread, any lock wait inside `Ping` stalls every heartbeat at once; without the lock half, one healthy client went `OFFLINE` in S1 (§4). It should not be enabled on a master without #4180.

### 3. Proof that the invariant holds (#4180 at 4da335ab + #4183, non-HA, `--heartbeat_rpc_port` set)

A test can only show that a failure did not occur; it cannot show that it cannot. So the claim is argued from the code, and each step is pinned by a test.

**3.1 Locks on the heartbeat path.** Every acquisition reachable from `WrappedMasterService::Ping`:

| # | acquisition | can a data-plane operation make it wait? |
| -- | -- | -- |
| 1 | registry `mutex_`, shared (twice) | only for O(1) exclusive sections: publishing a new slot, committing a remount, erasing a slot; O(clients) when a restore commits or the registry is reset |
| 2 | `ClientLivenessRecord::transition_mutex_` | no: its only holders (`Observe`, `Evaluate`, `SetTransitionObserver`, `StopObserving`) do O(1) work |
| 3 | on recovery only: the event dispatcher's mutex | no: one queue push; listeners run outside it |
| 4 | per-client operation lock, admission gate, `lifecycle_mutex_`, `snapshot_mutex_`, metadata shard locks, segment manager lock | not taken |
| 5 | `MasterMetricManager::inc_ping_requests` and liveness gauges | no lock: ylt `counter_t`/`gauge_t` are per-thread atomics |
| 6 | glog, only when a line is written (`VLOG(1)` per Ping at `-v>=1`) | only through blocking log I/O, which stalls every thread in the process and is outside this invariant |

`view_version_` is immutable after construction.

**3.2 Threads.**

| server | io threads | handlers registered |
| -- | -- | -- |
| main `coro_rpc_server` | `rpc_thread_num` (its own `io_context_pool`) | every master RPC, including `Ping` for clients that do not use the heartbeat server |
| heartbeat `coro_rpc_server` (`--heartbeat_rpc_port`) | 1 (its own `io_context_pool`) | `Ping`, `ServiceReady` only |

Each `coro_rpc_server` constructs its own `io_context_pool` from its `thread_num`, and `io_context_pool::run()` starts one `std::thread` per `io_context`, so the two servers share no io thread. A `Ping` on the heartbeat server is read and executed by a thread that never runs a data-plane handler, and by 3.1 it never waits for one either. `ServiceReady` returns a constant string.

**3.3 The monitor.** #4180's expiry pass captures `now` before it starts and evaluates each record under that client's operation lock. A wait inside the pass only delays a decision taken against the earlier `now`, so a transition still requires that no heartbeat was recorded for the client within the TTL before `now`. By 3.1 and 3.2, recording a received heartbeat never waits for the data plane. The remaining causes are outside the master's data plane: the client, the network, CPU starvation of the whole process, and blocking log I/O.

### 4. Measurement

Measured before #4180 existed, with #4182 as the lock half ("PR-A") and #4183 as the thread half ("PR-B"). #4180 alone is expected to behave like the PR-A rows; that is not measured yet.

Rig: one master (8 RPC threads, 7-CPU / 40 GiB cgroup), 18M keys, 12 clients pinging every second on their own threads, 16 load threads running `BatchExistKey`, default TTLs (active 10 s, suspicion 20 s). The same benchmark binary is used for every variant; against a master that does not advertise a heartbeat server it behaves as an unmodified client. Numbers are for the 12 clients that were healthy throughout ("originals"), during the load phase. Each cell is a single run.

- **S1: join storm.** 12 store clients join at once. Every remount runs the post-promotion shard walk: a rig-only environment variable forces the `any_standby_kept_alive` branch so this HA path can be exercised without a failover (not part of either PR). Since #4183 is non-HA only, S1 measures the code path, not a configuration that can be deployed today.
- **S2: unmount storm.** 12 clients unmount at once on a non-HA master with `--enable_snapshot`, so `UnmountSegment` runs `ClearInvalidHandles` synchronously on the RPC thread. This is a deployable configuration for #4183.
- **S3: a client really dies** (both PRs). Checks that detection is unchanged.

| scenario | variant | worst heartbeat gap (originals) | originals → SUSPECTED | originals → OFFLINE | keys at end |
| -- | -- | -- | -- | -- | -- |
| S2 unmount storm | main | 19.8 s | 6 | 0 | 18M |
| | PR-A only | 29.1 s | 12 | 0 | 18M |
| | PR-B only | 1.0 s | 0 | 0 | 18M |
| | PR-A + PR-B | 1.0 s | 0 | 0 | 18M |
| S1 join storm | main | 213.6 s | 30 | 0 | 18M |
| | PR-A only | 91.0 s | 28 | 0 | 18M |
| | PR-B only | 196.7 s | 14 | **1** | **16.5M** |
| | PR-A + PR-B | 1.0 s ¹ | 0 | 0 | 18M |
| S3 dead client | PR-A + PR-B | | the dead client only, 9.9 s after its last ping | the dead client only, 30.0 s after | its keys only |

¹ Excluding a 7.5 s gap at t=432 s while gdb was attached to the benchmark process to sample its stacks; every `Ping` sent in that window returned within 7 ms. Two earlier attempts of this cell ended with the benchmark pod out of memory, a benchmark-side leak unrelated to the heartbeat path.

What the table shows:
- **S2 involves no lock at all.** On `main`, every `Ping` that took longer than 2 s completed within 8 ms of an `UnmountSegment` returning: each stall was an io thread working through its queue of unmounts, not lock contention. PR-A does not act here; the 19.8 s vs 29.1 s spread most likely comes from which io thread a heartbeat's connection happened to share with the deepest unmount queue. Only the separate heartbeat thread removed it.
- **Neither dimension is sufficient alone.** The lock half alone shortened the worst S1 gap from 213.6 s to 91.0 s but still left 28 suspicions, because the heartbeats were then waiting for threads. The thread half alone fixed S2 but not S1, where its single heartbeat thread waits for `client_mutex_` behind each remount; one healthy client went `OFFLINE` and 1.5M keys were erased. Together they removed every false transition.
- **#2991's recovery is doing real work on `main`**, which is why S1 on `main` shows dozens of `SUSPECTED` transitions but no data loss in this run. Each of those transitions still removes a healthy client from every serving path while it is suspected, and the margin to `OFFLINE` is only the suspicion TTL (S1 with PR-B only crossed it).
- Detection of a client that really died is unchanged (S3).

### 5. Alternatives considered
- **Narrow the longest exclusive section.** Fixes today's worst holder, but nothing stops the next one (§1).
- **Raise `rpc_thread_num`.** A `Ping` is read only by the io thread that owns its connection, so k long handlers still stall roughly k/N of the connections, each for the handler's full duration, and new connections still depend on io thread 0.
- **Run every non-`Ping` handler on a worker pool.** A generic wrapper at registration needs no list of long handlers, and HA would get it through the same registration. The costs are a thread hop per RPC and more concurrency per connection, a much larger behavioural change than a heartbeat-only server. Returning a coroutine alone does not help: coro_rpc starts it inline on the io thread.
- **Circuit breaker (#3936, closed).** Withholds the consequence of a stall the master cannot rule out as its own; the cause remains.
- **Only the lock half (#4180 or #4182).** A heartbeat that no free thread reads cannot be recorded; S2 is unchanged and S1 still suspects healthy clients (§4).
- **Only the thread half (#4183).** The heartbeat thread still waits for data-plane locks; S1 shows a healthy client going `OFFLINE` and its keys erased (§4).

### 6. Out of scope / follow-ups
- HA mode for `--heartbeat_rpc_port` (the supervisor's server lifecycle). HA is where the remount walk runs, so this is the most valuable follow-up.
- Clients need no configuration: the heartbeat port is discovered on `Connect`.

### 7. Questions for maintainers
1. For the thread half, which direction do you prefer: #4183 as is (a dedicated heartbeat server, extended to HA through the supervisor), a generic wrapper that runs every non-`Ping` handler on a worker pool (§5), or folding it into the #4180 series?
2. Should the heartbeat server be on by default in a later release, once HA support lands?

### AI assistance disclosure
Claude (Anthropic) helped analyze the code paths, write the PRs and their tests, drive the rig measurements and draft this RFC. The submitter reviewed every changed line and the measurement data.

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)


## 评论 (4)

### github-actions[bot] · 2026-09-17

Thanks for opening this issue, @Juhyun-Kim-Memphis!

| Field | Value |
|-------|-------|
| **Issue** | #4181 |
| **GitHub user ID** | `32131411` |
| **Reporter** | @Juhyun-Kim-Memphis |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### Aionw · 2026-09-18

Hello @Juhyun-Kim-Memphis , I've addressed this issue in https://github.com/kvcache-ai/Mooncake/pull/4180, would mind take a look?

### Juhyun-Kim-Memphis · 2026-09-21

@Aionw Thanks for pointing me to #4180. I went through it at 4da335ab.

**Lock side: covered.** `Ping` no longer waits for anything a data-plane operation can hold for long. `client_mutex_` and the guards are gone, the registry lock's exclusive sections are O(1) (O(clients) only when a restore commits), and the record's `transition_mutex_` is only held for O(1) work. I ported the two tests from #4182 that fail on `main` onto the registry: `Ping` while its own remount scope, the restore barrier or another client's registration is held, and while a serving or retaining `SessionGuard` is held. All pass, and a control that holds the registry lock exclusively does block `Ping`, so the tests can tell. I've closed #4182 in favour of #4180 and updated this RFC to point at it for the lock side.

**Thread side: not covered.** #4180 leaves `rpc_service.cpp` untouched, so `Ping` still shares the main server's io threads with every data-plane handler. In coro_rpc each io thread runs its own `io_context`, an accepted connection stays on one of them for its lifetime, and non-coroutine handlers run inline on the thread that read the request. A `Ping` is therefore read only by the io thread that owns its connection: if that one thread is inside a long handler, the `Ping` waits for it, even when every other io thread is idle. Removing locks from `Ping` cannot help there, because nothing is waiting on a lock. In our unmount-storm run (18M keys, non-HA with `--enable_snapshot`, so `UnmountSegment` runs `ClearInvalidHandles` inline), every `Ping` that took longer than 2 s completed within 8 ms of an `UnmountSegment` returning, and healthy clients were marked `SUSPECTED`. #4180 does not shorten those handlers either: the unmount sweep is still synchronous in these modes, and `ReMountSegment` still holds `snapshot_mutex_` exclusively for the standby walk.

#4183 addresses this with a separate single-thread server for `Ping`, and it relies on #4180 for the lock side: with one heartbeat thread, any lock wait inside `Ping` would stall every heartbeat at once. It is non-HA only for now, while the long remount walk runs only in HA. Before I extend it, which direction would you prefer?

1. #4183 as is, a dedicated heartbeat server with a discovered port, extended to HA through the supervisor.
2. A generic wrapper in `RegisterRpcService` that runs every non-`Ping` handler on a worker pool, so the io threads only do I/O. It needs no list of long handlers and HA would get it through the same registration, at the cost of a thread hop per RPC.
3. You fold it into the #4180 series.


### Aionw · 2026-09-21

#4183 would be a grate direction right now. Can you also helping review #4180,  so that we can make sure that we actually solve your issues here.
