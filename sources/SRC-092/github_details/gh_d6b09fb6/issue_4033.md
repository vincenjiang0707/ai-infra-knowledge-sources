# [Issue #4033] [Bug]: NoF master keeps allocating space despite client-to-target network partitions

source: https://github.com/kvcache-ai/Mooncake/issues/4033
state: open | updated: 2026-09-12T04:43:25Z
labels: bug

## 正文

### Bug Report

## Description

NoF heartbeats are initiated by the master. If the master can reach a NoF target while a client cannot, the master may continue allocating space on that target even though the client cannot complete the actual I/O.

## Scenario

```text
Client ←── Metadata RPC: healthy ──→ Master
                                       │
                                       │ NoF heartbeat: healthy
                                       ↓
Client ←──── Network partition ────→ NoF Target
```

In this scenario, the client can successfully issue `PutStart`, and the master's NoF probes continue to succeed, leaving the segment available for allocation. However, after receiving the allocation, the client cannot access the target. The write consequently fails or waits for the underlying transport to report an error.

Because the master's probes continue to succeed, this condition may persist throughout the partition rather than being limited to the heartbeat detection window.

## Current code behavior

Based on the `USE_NOF` / SPDK path at commit `cafc5078`:

- **Heartbeats verify the master-to-target path.** `ProbeNofSegment()` reads LBA 0 of the target namespace through the master's own SPDK connection. This does not establish reachability from a client. See the [probe implementation](https://github.com/kvcache-ai/Mooncake/blob/cafc5078/mooncake-store/src/spdk/spdk_wrapper.cpp#L423).
- **NoF allocation does not filter targets by client reachability.** The master allocates space from mounted NoF allocators without excluding targets that are unreachable from the requesting client. See the [allocation logic](https://github.com/kvcache-ai/Mooncake/blob/cafc5078/mooncake-store/src/master_service.cpp#L4123).
- **A client-side I/O failure does not update reachability information for subsequent allocations.** The write path calls `PutEnd` or `PutRevoke` according to transfer results. `PutRevoke` handles replicas of the current object; it does not mark the target as unreachable from that client. Subsequent requests may therefore receive allocations on the same target. See the [client write path](https://github.com/kvcache-ai/Mooncake/blob/cafc5078/mooncake-store/src/client_service.cpp#L1881) and [PutRevoke implementation](https://github.com/kvcache-ai/Mooncake/blob/cafc5078/mooncake-store/src/master_service.cpp#L4776).

### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### github-actions[bot] · 2026-09-11

Thanks for opening this issue, @CageChen!

| Field | Value |
|-------|-------|
| **Issue** | #4033 |
| **GitHub user ID** | `22573449` |
| **Reporter** | @CageChen |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-09-12

Verified the three mechanism claims against current main; they all hold.

1. `ProbeNofSegment` (spdk_wrapper.cpp) proves only the master-to-target path: it initializes the master's own SPDK env, opens the segment through that connection, and submits an LBA-0 read. Nothing about it exercises any client's reachability.
2. The NoF allocation in `MasterService` (`allocation_strategy_->Allocate(...)` around master_service.cpp:4782) sees only the mounted allocator set plus the client's `preferred_nof_segments`; the exclusion set is a hardcoded empty set, so no per-client reachability signal can influence it.
3. `PutRevoke` handles only the revoked object's replicas (mark-removed, quota settle, oplog finalize). It writes nothing back to segment or allocator state, so a client that fails its I/O cannot lower the target's allocation odds for the next request, even though the master's own probes keep succeeding. The partition therefore persists for exactly as long as the master-to-target path stays healthy, as the report says.

On direction, the least invasive seam looks like the allocation side rather than the probe side: a client that gives up on a target (PutRevoke after transport failure, or an explicit client-reported probe failure) could add the segment to a short-TTL per-client exclusion that `Allocate` already accepts as a parameter, instead of inventing a new global health channel. That keeps the master's global view untouched (other clients may still reach the target fine) and avoids flapping a shared state on one client's partition. The open design question is whether the exclusion belongs in the client config surface (like `preferred_nof_segments`) or in a master-side per-(client, segment) table with its own expiry, and the latter needs the heartbeats to stay strictly master-scoped so the two signals never fight.

(Tagging @CageChen in case the reporter wants to shape the RFC around one of those seams.)

