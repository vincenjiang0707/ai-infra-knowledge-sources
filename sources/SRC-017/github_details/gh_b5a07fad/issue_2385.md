# [Issue #2385] [Bug]: Deadlock in bootstrap when ranks are unevenly distributed across nodes (7+8), contiguousRanksPerHost falls back to INT_MAX

source: https://github.com/NVIDIA/nccl/issues/2385
state: closed | updated: 2026-09-22T08:01:26Z
labels: 

## 正文

# [Bug]: Deadlock in bootstrap when ranks are unevenly distributed across nodes (7+8), `contiguousRanksPerHost` falls back to INT_MAX

## Summary

A communicator built with an **unequal number of ranks per node** (7 on one node, 8 on the other) deadlocks during `ncclCommInitRank` and never reaches the collective. The same job with an **equal** number of ranks per node works fine, both at full size (8+8) and reduced size (7+7), so the trigger is the per-node *mismatch*, not the rank count and not the launch mechanism.

Reproduced **3/3 attempts** with an identical signature. Notably, rank 0 on the 7-rank node
froze at 553,578 / 553,578 / 553,582 lines of debug output across the three runs —
i.e. the ranks deadlock at essentially the same point every time, not at a
timing-dependent one. Full `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=ALL` logs for all 15 ranks
were captured while hung and are available.

Full `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=ALL` log excerpts (300-line tails from three
representative ranks, showing the three distinct stall stages):
https://gist.github.com/bhaveshdavda/bca392f83f99ca402156264fcc9ba913

## Environment

| | |
|---|---|
| NCCL | 2.31.2+cuda13.3 (`NCCL version 2.31.2+cuda13.3`) |
| nccl-tests | 2.18.3 (`nccl-headers=23102 nccl-library=23102`) |
| GPUs | 8× H100 80GB HBM3 per node, 2 nodes |
| NICs | 8× mlx5 per node, one per GPU (rail-aligned), RoCE |
| Net plugin | `NCCL RDMA Plugin v11` (HPC-X `libnccl-net.so`) |
| GDR | GPUDirect RDMA enabled (both `nvidia-peermem` and DMABUF reported) |
| MPI | HPC-X Open MPI, launched via Kubeflow MPIJob (`orted` bootstrapped through `kubectl exec`) |
| OS/container | Ubuntu 22.04 container image |

## Steps to reproduce

Launch `alltoall_perf` with a hostfile that gives one node fewer slots than the other:

```
# hostfile
node-0 slots=7
node-1 slots=8
```

```bash
mpirun -np 15 --hostfile /tmp/hostfile -bind-to none -x LD_LIBRARY_PATH \
  -x NCCL_DEBUG=INFO \
  -x NCCL_DEBUG_SUBSYS=ALL \
  -x NCCL_DEBUG_FILE=/dev/shm/nccl-debug-rank%h-%p.log \
  /opt/nccl_tests/build/alltoall_perf -b 1K -e 1G -f 2 -g 1 -w 2 -n 100
```

Rank/device placement comes out as intended — node-0 contributes ranks 0–6 on devices 0–6 (device 7 left idle), node-1 contributes ranks 7–14 on devices 0–7:

```
#  Rank  0 Group  0 Pid     59 on node-0 device  0 [0000:1b:00] NVIDIA H100 80GB HBM3
...
#  Rank  6 Group  0 Pid     65 on node-0 device  6 [0001:45:00] NVIDIA H100 80GB HBM3
#  Rank  7 Group  0 Pid     59 on node-1 device  0 [0000:1b:00] NVIDIA H100 80GB HBM3
...
#  Rank 14 Group  0 Pid     68 on node-1 device  7 [0001:4e:00] NVIDIA H100 80GB HBM3
```

## Expected behavior

The communicator initializes and `alltoall_perf` runs, as it does for 8+8 and 7+7.

## Actual behavior

All 15 ranks start and print the device table, then hang permanently in comm init:

1. **GPU utilization stays at 0%** on every device on both nodes — the timing loop is never entered.
2. **Debug log growth stops entirely.** On the first run, one rank's log froze at 553,578 lines and was byte-identical across a re-check seconds later. This is a true stall, not slow progress.
3. Stalled ranks' last line is:
   ```
   NCCL INFO bootstrap.cc:1016 (unexpectedEnqueue) Host Calloc Size 112 pointer 0x...
   ```
4. Ranks stall at **different** stages — some mid-`devCommSetup`, some in proxy `Setup` / `proxyProgressAsync ... operation=Setup res=0` — consistent with a circular wait rather than all ranks blocking on one barrier.
5. Strong log-volume asymmetry between the two nodes: the 7-rank node's processes emitted ~78 MB each (~721 MB total in `/dev/shm`), while the 8-rank node's emitted ~3 MB each.

No errors or warnings are logged other than the benign `wrap_ibv_query_port_speed ... Protocol not supported errno 93` messages.

## Suspected cause

Ranks on the 8-rank node log:

```
NCCL INFO symmetricSupport 0, cuMemEnable 0, globalGinSupport 1, cuMemGdrSupport 1, contiguousRanksPerHost 2147483647, crossNicSupport 1
```

`contiguousRanksPerHost = 2147483647` (INT_MAX) appears to be a sentinel indicating NCCL detected that ranks are not uniformly/contiguously distributed per host and fell back off its normal assumption.

In every working configuration this field reports the true per-node rank count; it degrades to INT_MAX only in the deadlocking one:

| Ranks per node | `contiguousRanksPerHost` | Result |
|---|---|---|
| 8 + 8 | `8` | ✅ |
| 7 + 7 | `7` | ✅ |
| 1 + 1 (`sendrecv_perf`) | `1` | ✅ |
| **7 + 8** | **`2147483647`** | ❌ deadlock |

The deadlock looks like it occurs in ring/channel construction or the bootstrap exchange downstream of that fallback.

## Control experiments (isolating the trigger)

Same image, same manifest, same custom-hostfile launch mechanism — only the slot counts differ:

| Ranks per node | `-np` | Result |
|---|---|---|
| 8 + 8 | 16 | ✅ Completes. `Out of bounds values : 0 OK` |
| 7 + 7 | 14 | ✅ Completes. `Out of bounds values : 0 OK`, 33.68 GB/s avg busbw |
| **7 + 8** | **15** | ❌ **Deadlocks in comm init (2/2 attempts)** |

Because 7+7 works, the cause is not the reduced rank count, not the odd/even total, and not the custom hostfile itself — it is specifically the per-node imbalance.

## Why this configuration

I was investigating the behavior described in https://github.com/NVIDIA/nccl/issues/2193#issuecomment-4661668627 — namely that PXN cannot relay when the rail-aligned GPU on the sending node is not part of the communicator. The natural way to construct that case is a communicator where one node contributes a GPU whose rail-peer is absent on the other node, which requires unequal ranks per node. That construction can't be tested on this stack because it deadlocks before the collective runs.

(The underlying PXN question was ultimately answered with a 2-rank `sendrecv_perf` between GPU0 on node A and GPU7 on node B, which confirmed no PXN relay is used — 0 connections carrying the `netDev(relayRank)` annotation — matching the explanation in that comment.)

## Additional notes

- Is an unequal ranks-per-node communicator expected to be supported? If it is unsupported by design, an explicit error at init would be far preferable to a silent hang.
- If it is meant to be supported, the `contiguousRanksPerHost` INT_MAX fallback path looks like the place to start.


## 评论 (12)

### bhaveshdavda · 2026-09-03

Small clarification on the PXN observation mentioned at the end of the report, now that I've checked it against the source rather than inferring it from log patterns.

In `src/transport/net.cc` (v2.31.2-1, `sendSetup`), the `via NET/...` line has two variants selected by whether the send is proxied through another rank:

```c
if (proxyRank != myInfo->rank && connIndex == 0) comm->useNetPXN = true;
...
if (proxyRank == myInfo->rank) {
  INFO(..., "... [send] via NET/%s/%d%s%s%s", ..., req.netDev, ...);
} else {
  INFO(..., "... [send] via NET/%s/%d(%d)%s%s%s", ..., req.netDev, proxyRank, ...);
}
```

So the parenthetical is `proxyRank`, printed exactly when `proxyRank != myInfo->rank` — the same predicate that sets `comm->useNetPXN`. That makes "line has a parenthetical" a direct, unambiguous indicator that a given connection is PXN-relayed, which is a cleaner signal than the topology-graph `PXN`/`PHB` path typing I had been using.

Re-measuring my runs on that basis (counting `[send] via NET` lines with a parenthetical):

| Configuration | PXN-relayed connections | Total `via NET` lines |
|---|---|---|
| 8+8, PXN default | 640 | 1600 |
| 8+8, `NCCL_PXN_DISABLE=1` | 0 | 1600 |
| 7+7, PXN default | 632 | 1680 |
| 1+1, rail-aligned (GPU0 ↔ GPU0) | 0 | 32 |
| 1+1, rail-misaligned (GPU0 ↔ GPU7) | 0 | 32 |

The two 1+1 rows are the point relevant to https://github.com/NVIDIA/nccl/issues/2193#issuecomment-4661668627: with a single rank per node, `ncclTopoGetNetDev` can only return `proxyRank == myInfo->rank`, so `comm->useNetPXN` is never set and no relay occurs — including in the misaligned case, where the sending GPU's rail-matched peer exists physically on the node but holds no rank in the communicator. That matches @sjeaugey's explanation exactly, and it's why I was trying to build the 7+8 communicator in the first place.

One incidental note in case it helps anyone else parsing these logs: on a 1:1 GPU:NIC topology the parenthetical always happens to equal the `netDev` index (rank *N* owns NIC *N*), so `netDev(N)` looks like a doubled field. That's a coincidence of the topology, not the format — the reliable test is the presence of the parenthetical, not the two values matching.


### sjeaugey · 2026-09-03

PXN and `contiguousRanksPerNode` are totally unrelated, so this bug description can be a bit confusing.

Let's just start with the facts: alltoall_perf hangs when run on 7+8 GPUs. That's simple to work on and try to reproduce.

I'm not even sure this is PXN related. Does the hang also happen when PXN is disabled?

### bhaveshdavda · 2026-09-03

Good call, and you're right — I agree the description conflated two things. `contiguousRanksPerHost` falling back to INT_MAX is just something I noticed nearby in the logs, not something I'd verified was causal.

Tested it directly: same 7+8 `alltoall_perf` config, with `NCCL_PXN_DISABLE=1` added.

**It still hangs**, identically:

- `NCCL_PXN_DISABLE set by environment to 1.` confirmed on every rank
- Same stall call: `bootstrap.cc:1016 (unexpectedEnqueue)`
- Same sentinel: `contiguousRanksPerHost 2147483647`
- Same symptom: 0% GPU utilization, debug log output frozen

One rank got slightly further this time before stalling — into NVLS multicast group creation (`NVLS Creating Multicast group nranks 7 size 2097152 on rank 0` / `NVLS Created Multicast group ... nranks 7 ...`) — but landed at the identical `unexpectedEnqueue` call regardless.

So: not PXN-related. It's a plain `alltoall_perf` on 7+8 GPUs hang, independent of the PXN setting. I'll treat `contiguousRanksPerHost` as an observation rather than a proposed cause going forward — happy to focus on whatever repro shape is most useful from here (smaller GPU counts, a different collective, `NCCL_DEBUG_SUBSYS` narrowed to something specific, etc.) if that helps narrow it down.


### bhaveshdavda · 2026-09-03

You're right, and I'm sorry that's Claude AI slop trying to impress you that I understand the code enough to be able to find the bug leading to the hang :-) Since I was using Claude Code for these experiments, which were basically to validate your explanation in https://github.com/NVIDIA/nccl/issues/2193#issuecomment-4661668627 I'll shepherd it to run a PXN disabled 7+8 experiment and post its results. Which it looks like Claude beat me to while I was typing my human response :)

### teojgo · 2026-09-04

@bhaveshdavda can you try running with `NCCL_NVLS_ENABLE=0`?

### bhaveshdavda · 2026-09-04

*Note: this comment was produced by an AI coding assistant (Claude) at my direction, running the test on our cluster.*

@teojgo Confirmed — `NCCL_NVLS_ENABLE=0` fixes it. Same 7+8 config (worker with slots=7 excluding rail 7, worker with slots=8 including it), same `alltoall_perf -b 1K -e 1G -f 2 -g 1 -w 2 -n 100`, only the added env var changed:

- Completes cleanly: full 21-size sweep, `Out of bounds values : 0 OK`, avg bus bandwidth 27.58 GB/s
- GPUs 0–6 hit 100% utilization on the reduced-slot node (rail 7 correctly idle)

This points at NVLS multicast group setup as the actual hang, not `contiguousRanksPerHost` — in one of the earlier hung attempts (before this fix), the furthest-progressed rank had gotten to `NVLS Creating Multicast group nranks 7 size 2097152 on rank 0` before stalling at the same `bootstrap.cc:1016 (unexpectedEnqueue)` call. Consistent with a 7-vs-8 mismatch breaking multicast group formation specifically, rather than anything PXN- or bootstrap-ordering-related in general.

With the job actually completing, I could finally test the original PXN question directly instead of via the 2-rank substitute. Sends from the 7-rank node's ranks, split by whether the destination's rail-matching relay rank exists in the communicator:

| Destination | Relayed via PXN |
|---|---|
| Rank on the excluded rail (rail 7, absent on the 7-rank side) | 0 / 28 |
| All other cross-rail destinations (rail present on both sides) | 172 / 196 |

Same senders, same run — the only variable is whether a local rank owning the destination's rail exists. Matches @sjeaugey's explanation on #2193 exactly: no relay when the rail-matched GPU holds no rank in the communicator, falls back to the sender's own NIC, no failure otherwise.


### teojgo · 2026-09-07

@bhaveshdavda are you setting `NCCL_RUNTIME_CONNECT=0`? If so, can you try with the default value?

### bhaveshdavda · 2026-09-07

@teojgo  No, NCCL_RUNTIME_CONNECT was never set — it was left at default in every run in this thread.

### xiaofanl-nvidia · 2026-09-21

@teojgo can you confirm this was fixed and ready to close? 

> Fixes PAT connection-setup deadlocks when runtime connection is disabled and nodes have uneven local-rank counts. (https://github.com/NVIDIA/nccl/issues/2385)

### teojgo · 2026-09-21

@bhaveshdavda this [commit](https://github.com/NVIDIA/nccl/commit/7f8b14e6461ab6d9b30b96fb08457fa16ce15cf2) which is included in the latest v2.32.3-1 release fixes the issue. Can you please confirm?

### bhaveshdavda · 2026-09-21

*Note: this comment was produced by an AI coding assistant (Claude) at my direction, running the tests on our cluster.*

@teojgo Confirmed. Re-ran the identical 7+8 asymmetric config (worker with slots=7, worker with slots=8, `alltoall_perf -b 1K -e 1G -f 2 -g 1 -w 2 -n 100`) with default settings — no `NCCL_NVLS_ENABLE=0` workaround this time. Debug logs report `NCCL version 2.32.3+cuda13.3`:

- Completes cleanly: full 21-size sweep, `Out of bounds values : 0 OK`, avg bus bandwidth 27.45 GB/s (matches the 27.58 GB/s we saw with the NVLS-disabled workaround)
- Debug logs show `NVLS Creating Multicast group nranks 7 size 86973087744 on rank 0` completing — that's the exact call the old hang stalled at, so this confirms the fix addresses the root cause and not just an NVLS-avoidance side effect

Thanks for tracking this down.


### teojgo · 2026-09-22

Closing since this is fixed.
