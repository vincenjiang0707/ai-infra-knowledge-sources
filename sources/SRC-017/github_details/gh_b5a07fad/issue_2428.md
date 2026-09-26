# [Issue #2428] [Question] NCCL_IGNORE_NET_MISMATCH turns a heterogeneous-HCA misconfiguration into a silent hang

source: https://github.com/NVIDIA/nccl/issues/2428
state: open | updated: 2026-09-22T14:55:46Z
labels: 

## 正文

### Summary

When two ranks expose different RDMA HCA sets, `NCCL_IGNORE_NET_MISMATCH=1` suppresses the mismatch guard and NCCL proceeds — then hangs indefinitely with no error, because the channels created on one rank's extra HCA have no peer.

### Setup

- 2 nodes × 8× NVIDIA H20, RoCE over eRDMA, NCCL 2.30.7
- Node A exposes `erdma_0` + `erdma_1`, both usable
- Node B has `erdma_1` present in the container but not openable (`ibv_open_device(erdma_1)` fails — the device plugin / device cgroup admits only one uverbs device)
- `NCCL_IGNORE_NET_MISMATCH=1` was set to silence the mismatch warning

### Observed

Rank 0 builds channels across both HCAs:

```
Channel 00 -> NET/IB/0/GDRDMA     Channel 01 -> NET/IB/1
Channel 02 -> NET/IB/0/GDRDMA     Channel 03 -> NET/IB/1
...
```

Rank 1 builds every channel on `NET/IB/0/GDRDMA` only, with:

```
NCCL WARN NET/IB : Unable to open device erdma_1
```

Net effect: the channels rank 0 placed on `erdma_1` each wait on a peer that never appears. Initialization completes; the job then spins forever.

### Evidence that this is idle-wait, not work

- GPU SM utilization 100%, but memory throughput 0%, power ~118 W against a ~400 W cap, die temperature 34–37 °C
- `perf` on the workers shows `libnccl.so.2 recvProxyProgress`, `_raw_spin_lock`, `sched_yield`, `clock_gettime` — busy-wait polling, not compute

### Ask

Is there a path to fail fast here — or at minimum to log this prominently — rather than hang indefinitely?

We understand `NCCL_IGNORE_NET_MISMATCH` is an intentional escape hatch for asymmetric-but-usable topologies, so we are not asking for it to be removed. The ask is narrower: the mismatch guard exists precisely to prevent this configuration, and suppressing it currently converts a detectable configuration error into an unbounded hang.

Reverting to a single HCA (`NCCL_IB_HCA=erdma_0`) resolves it, which is the mitigation we applied.


## 评论 (7)

### abhiMishra98 · 2026-09-21

I'd like to take this up.

I'm thinking of a WARN rather than failing init, since some setups legitimately have different NIC counts per node. Rough plan:

1. **`src/transport/net_ib/init.cc`** (`ncclIbInitDevices`): each rank records the HCAs that fail `ibv_open_device`, unless the user excluded them via `NCCL_IB_HCA`.
2. **`src/init.cc`** (`initTransportsRank`, AllGather3): each rank shares that list and its hostname alongside `localNetDeviceCount`.
3. **`src/init.cc`** (Net device count mismatch check): rank 0 already compares NIC counts there. For each rank below the max that reported failed HCAs, it prints a WARN naming the rank, host and HCA, even with `NCCL_IGNORE_NET_MISMATCH=1`.

**Test setup:** 2 nodes × 1 L40S, RoCE (ConnectX-6Lx, mlx5), NCCL 2.30.7. Each node has only one active port, so I'll emulate the case with test-only injection: a duplicated HCA on one rank, and a simulated `ibv_open_device` failure on the other.

I am open to any suggestions/adjustments if required to this approach.


### luoyuctl · 2026-09-21

Thanks @abhiMishra98 — a WARN-only approach sounds right to me, and your reading of the two cases matches what we hit.

In our case the device names were identical on both nodes (`erdma_0`, `erdma_1`), so this was not a naming or index mismatch: `erdma_1` existed on node B but `ibv_open_device` failed there because the device plugin / device cgroup only admitted one uverbs device. Rank 0 therefore spread channels across both HCAs while rank 1 could only build them on `erdma_0`. A name-based comparison would miss that; a per-rank "attempted and failed to open" signal is the right one.

A few notes on the plan:

1. Agree on keeping the `NCCL_IB_HCA` distinction — only report devices that were attempted and failed, not the ones a user deliberately excluded. Warning on an intentional exclusion would be noise that trains people to ignore the message.
2. Include the reason (`errno` / `strerror`) in the WARN. In practice the causes here are permissions (device cgroup / uverbs) versus driver or device-plugin visibility, and "unable to open" alone doesn't let a user tell those apart.
3. Print the consequence, not just the fact — e.g. "channels placed on this HCA have no peer; init can still complete and the job may then hang with no error". That part was the expensive one for us: init finished, then the ranks spun in `recvProxyProgress` at ~118 W against a ~400 W cap with no memory throughput, which reads like stuck compute rather than a missing peer.
4. Worth deciding explicitly whether `NCCL_IGNORE_NET_MISMATCH=1` should still suppress this. A device that fails to open feels like a different class from a topology that is merely asymmetric, so arguably the warn should fire regardless of that variable. No strong opinion on where you draw the line — just flagging it.
5. For the test, make sure the injection actually triggers the `ibv_open_device` failure path. Merely lowering `localNetDeviceCount` on one rank would already be caught by the existing mismatch check and wouldn't exercise the new signal.

On validation: we originally hit this on 2×8 H20 over Alibaba eRDMA, but that fleet can't run `internode_ll` at all (no mlx5 / IBGDA), so the mlx5 setup you described is the more useful one. Happy to compare notes or share the full init logs and `ibv_devinfo` output from our case if that helps.

### abhiMishra98 · 2026-09-21

Thanks @luoyuctl, the feedback is really helpful and I have taken the points into consideration as follows - 

1. **`NCCL_IB_HCA`:** only devices the user allowed are reported; excluded ones stay silent.
2. **Reason:** the WARN includes `strerror` and the errno, e.g. `could not open mlx5_1 (Permission denied, errno 13)`.
3. **Consequence:** A second WARN says the extra devices on other ranks have no peer and the job may hang without an error.
4. **`NCCL_IGNORE_NET_MISMATCH`:** I agree that a device failing to open is a different case from an intentionally asymmetric topology, so the WARN naming the device fires whatever the variable is set to. That WARN includes the rank, host, device, `strerror` text and errno, e.g. `Rank 1 on node-b could not open erdma_1 (Permission denied, errno 13)`.
   - `=1` (default): NCCL keeps running as before, but prints the device WARN plus the consequence WARN (the job may hang), so the problem is visible instead of silent.
   - `=0`: NCCL prints the device WARN, then fails init with the existing mismatch error. Here the consequence line is skipped, since the job stops right away and can't hang.
5. **Test:** besides a simulated failure, I validated it with a real `ibv_open_device` failure (the uverbs device made inaccessible), so the actual failure path and errno are exercised.

On validation: the change only touches NCCL init in the standard IB verbs transport. A plain nccl-tests run (e.g. `all_reduce_perf`) on your 2×8 H20 eRDMA setup, with `erdma_1` blocked on node B as before, would exercise it exactly as in your original case. I'll link the PR here once it's up.

### nitbhat · 2026-09-21

@luoyuctl, thanks for reporting the issue and @abhiMishra98 for providing a fix. I'll review this issue and your fix. 

### luoyuctl · 2026-09-22

Independent validation of #2429 on the fleet where we originally hit this (2×8 H20 / Alibaba eRDMA). Everything below is from a real 2-node NCCL job, not a simulation of the log path.

**Setup**

- Patched NCCL built from the #2429 head (`libnccl.so.2` 2.32.3), swapped in over the PyTorch-bundled 2.29.7 on both ranks. Note `torch.cuda.nccl.version()` reads a compile-time constant in PyTorch, so I confirmed the loaded build via the PR's own format strings plus `NCCL version 2.32.3` in the error path instead.
- 2 nodes × 1 GPU, ranks 0/1, launched with `torchrun` (static rendezvous, no MPI/SSH).
- Fault injection: an initContainer recreates the device nodes in an emptyDir and gives only `uverbs1` a foreign owner plus mode `600`; the main container runs as root with `DAC_OVERRIDE` dropped. The host `/dev` is untouched and `erdma_0` stays on the real node, so the rank genuinely fails `ibv_open_device("erdma_1")` while the rest of the device set is normal.

**Results — the matrix matches the PR description**

| Case | Expected | Observed |
|---|---|---|
| `NCCL_IGNORE_NET_MISMATCH=1`, rank 1 fails to open `erdma_1` | both WARNs | both present |
| `NCCL_IGNORE_NET_MISMATCH=0`, same failure | device WARN, no consequence WARN, then the existing error | exactly that |
| `NCCL_IB_HCA=erdma_0` (failing device excluded) | no new WARN | 0 lines |
| device counts match, no open failure | no new WARN | 0 lines |

Rank 0 output for the first case (`init.cc:1591` / `init.cc:1594`):

```
NCCL WARN Rank 1 on h20-cherry could not open erdma_1 (No such file or directory, errno 2). Fix device access or restrict NCCL_IB_HCA.
NCCL WARN Rank 1: channels on the extra devices of other ranks have no peer here, so the job may hang without an error.
```

With `=0`, the device WARN is followed directly by the pre-existing `Detected mixed local Net device counts across ranks (min 1, max 2). Set NCCL_IGNORE_NET_MISMATCH=1 to continue.`, and no consequence line — matching the intended split.

**One finding worth fixing: the reported errno is not the underlying cause.**

In the failing process, a plain `open("/dev/infiniband/uverbs1", O_RDWR)` returns **EACCES (13, Permission denied)**, but the WARN reported **ENOENT (2, No such file or directory)**. By the time `ncclIbInitDevices` formats the message, `errno` has already been clobbered by libibverbs / provider internals. For an operator that is actively misleading — the message points at a missing device when the real problem is permissions. Capturing `errno` at the `ibv_open_device` failure site, or wording the message so the errno is clearly "as returned by ibv_open_device" rather than the root cause, would avoid that.

**Not covered: the "`=1` keeps running" half of the claim.** I could not exercise it here — on this fleet the eRDMA data plane does not come up for a plain NCCL job at all (`ibv_query_gid` returns nothing, then `ibv_modify_qp` fails with EINVAL on both ranks). For reference, the production deployment on this same cluster runs with `NCCL_IB_DISABLE=1`. That is unrelated to this change, which only adds init-time logging, so the mlx5 setup in the PR's own test matrix remains the right place for that case.

Happy to re-run against a rebased head if the errno capture changes.

### abhiMishra98 · 2026-09-22

Thank you @nitbhat for being able to review my changes and @luoyuctl for the testing done on my patch. I will look into the error string issue you reported and post my findings/patch as required.

### abhiMishra98 · 2026-09-22

The `ENOENT` is set inside libibverbs before `ibv_open_device` returns ([`ibv_open_device`](https://github.com/linux-rdma/rdma-core/blob/00357df3a344b3515a9a4d345cf0b8c8efb7f116/libibverbs/device.c#L363) - [`verbs_open_device`](https://github.com/linux-rdma/rdma-core/blob/00357df3a344b3515a9a4d345cf0b8c8efb7f116/libibverbs/device.c#L323-L338) - [`open_cdev()`](https://github.com/linux-rdma/rdma-core/blob/00357df3a344b3515a9a4d345cf0b8c8efb7f116/util/open_cdev.c#L134-L146)):

1. `open_cdev()` first opens `/dev/infiniband/uverbs1`, which fails with `EACCES`.
2. It then [falls back](https://github.com/linux-rdma/rdma-core/blob/00357df3a344b3515a9a4d345cf0b8c8efb7f116/util/open_cdev.c#L143-L144) to [`open_cdev_robust()`](https://github.com/linux-rdma/rdma-core/blob/00357df3a344b3515a9a4d345cf0b8c8efb7f116/util/open_cdev.c#L87-L95), which uses `/dev/char/<major>:<minor>`. Your recreated `/dev` in the emptyDir most likely has no `/dev/char/`, so the fallback fails with `ENOENT`, which overwrites the original errno.

I ran the same kind of test on bare metal, blocking `uverbs1` on the second node with `chmod 600`. There `/dev/char/<major>:<minor>` exists and is a symlink to the same `uverbs1` node, so the fallback also failed with `EACCES` and the WARN showed the right errno. That's why my test passed and yours didn't.

Since `ibv_open_device` only reports failure through errno, NCCL can't easily recover the original value. We could work around it in NCCL, but I think the fix belongs in libibverbs rather than here: ideally `open_cdev()` would keep the first `open()` error when the fallback also fails. For this PR, I'd suggest labeling the value as what `ibv_open_device` reported, e.g. `could not open erdma_1 (ibv_open_device: No such file or directory, errno 2)`, so it isn't read as the root cause. Happy to hear if you see it differently.
