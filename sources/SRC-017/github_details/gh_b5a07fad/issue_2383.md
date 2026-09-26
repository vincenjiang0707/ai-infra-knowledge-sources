# [Issue #2383] [GIN/GDAKI] A `TRANSPORT_RETRY_EXC_ERR` completion on a GDAKI QP hangs the device forever: the device-side wait loops treat an error CQE as "not yet"

source: https://github.com/NVIDIA/nccl/issues/2383
state: open | updated: 2026-09-14T04:34:09Z
labels: 

## 正文

**NCCL version:** 2.30.7 (nvidia-nccl-cu13 wheel), `NCCL_GIN_ENABLE=1 NCCL_GIN_TYPE=3` (GDAKI), 4 GIN contexts, 1 counter + 84 signals per context
**GPU:** Blackwell sm_120 (110 SMs, 72 GB), driver 580.173.02, CUDA 13.0, 8 GPUs per node, PIX groups of 4
**NIC:** ConnectX-7 400G, **RoCE v2**, fw 40.47.2682, one NIC per 2 GPUs, eth MTU 4200 (`active_mtu` 4096), PFC on priority 5 + ECN/DCQCN enabled
**Env:** `NCCL_IB_HCA=mlx5_1:1,...,mlx5_8:1 NCCL_P2P_LEVEL=PIX NCCL_SHM_DISABLE=1`, IB timeout / retry at defaults (20 / 7), TC/SL defaults

## Summary

A persistent kernel using the NCCL device API (`ncclGin::put` with `ncclGin_SignalAdd` + `ncclGin_CounterInc`, then `waitCounter` / `waitSignal`) wedges about once per 10–50 runs, on all 8 ranks, forever. Reading the GDAKI queues from the host during the wedge shows that on exactly one RC connection the requester QP has completed with **CQE syndrome 0x15 (`TRANSPORT_RETRY_EXC_ERR`, vendor syndrome 0x83)** and moved to the ERR state, the companion QP was flushed (`0x05`), and therefore the local completion counter can never advance. The device-side wait loops (`waitCounter`, `waitSignal`, `flush` → `waitImpl` / `poll_one_cq_at`) only exit on `status == 0`, so an error completion is indistinguishable from "not yet" and the CTA spins until the job is killed. `ncclCommGetAsyncError` on the comm does report `ncclRemoteError` — but only if the application calls it; nothing in NCCL reacts to the QP error on its own.

Two issues, one of them clearly NCCL's:

1. **The device wait paths spin forever on an error CQE.** `doca_gpu_dev_verbs_poll_one_cq_at` returns `-EIO` for `MLX5_CQE_REQ_ERR`, but `nccl::gin::gdaki::waitImpl` / `flushImplMode` loop `while (status != 0 && !testAbort(...))`, and `waitCounter` / `waitSignal` poll a memory word that is never written after the error. 2.31.2's device-side timeouts bound this, but an error completion should terminate the wait immediately and be reportable (e.g. return `ncclRemoteError`, or set the comm's abort flag from the error path), not be waited out.
2. **The transport event itself**: one RC connection stops making progress in both directions for ≥ 7 retries × 2^20·4 µs ≈ 30 s while every other connection on the same two NICs keeps flowing (details below). We are asking whether this is a known GDAKI / firmware issue with bidirectional WRITE + ATOMIC traffic on the same QP pair.

## Usage pattern

- 8 ranks, 4 GIN contexts. Per launch every rank puts to its 4 off-switch peers on every context: `gin.put(team, peer, dstWin, dstOff, srcWin, srcOff, bytes, ncclGin_SignalAdd{slot, delta}, ncclGin_CounterInc{0}, ncclCoopCta(), ncclGin_None{}, thread_scope_thread, thread_scope_system)`, `bytes` ≈ 2–7 MB per put.
- The two ends of every RC connection do this **at the same time** (rank r puts to p while p puts to r on the same context), so each QP pair carries WRITE + ATOMIC_FA in both directions concurrently.
- Independently, a small kernel issues `gin.signal(..., ncclGin_SignalAdd)` on context 0 to every peer (including self).
- Then one CTA per context does `gin.waitCounter(ncclCoopCta(), 0, runningTotal)`; other CTAs `gin.waitSignal(ncclCoopCta(), slot, epoch)`.
- ~250 launches per run; wedge rate ~2–10 % per run. A tight loop of the same kernel without the surrounding model (≈400 k launches at 64 / 1024 / 8192 rows) never wedged **until we added concurrent host-side NCCL traffic on the same NICs** — see the reproducer below.

## Evidence: host-side snapshot of the GDAKI queues during the wedge

Read with plain D2H copies of `ncclGinGdakiGPUContext` → `doca_gpu_dev_verbs_qp` (main and companion), the CQE rings, and the counter tables; `sq_pi` = `sq_wqe_pi`, `nic_done` = highest `wqe_counter` with a completion in the ring.

**Catch A (epoch 370, ranks 6 → 2, context 3):**

```
rank 6  ncclCommGetAsyncError = ncclRemoteError
rank 6  ctx3 peer2 main  rsvd=988 ready=988 pi=988 nic_done=987 [ERR#1 synd=0x15 vend=0x83 at wqe 987]  ops=WRITE,FA,WRITE,FA
rank 6  ctx3 peer2 COMP  rsvd=988 ready=988 pi=988 nic_done=987 [ERR#2 synd=0x05 vend=0xf9 at wqe 987]  ops=WAIT,FA,WAIT,FA  wait(max_index=987)
rank 2  ncclCommGetAsyncError = ncclSuccess   (all 64 of its QPs healthy)
rank 2  ctx3 peer6 main  rsvd=990 ready=990 pi=990 nic_done=987 [NIC<pi]   ops=WRITE,FA,WRITE,FA
rank 2  ctx3 peer6 COMP  rsvd=990 ready=990 pi=990 nic_done=987 [NIC<pi]   ops=WAIT,FA,WAIT,FA  wait(max_index=989)
every other queue on every rank: rsvd == ready == pi, nic_done == pi-1
```

**Catch B (epoch 424, ranks 7 → 0, context 1):** identical shape — rank 7's main QP to peer 0 `ERR synd=0x15 vend=0x83 at wqe 1131` (its last WQE, the signal atomic), companion flushed; rank 0's QP to peer 7 `nic_done=1127 pi=1132`, no error; `ncclCommGetAsyncError` = `ncclRemoteError` on rank 7 only.

What the snapshots say:

- The error is always on the **8-byte signal `ATOMIC_FA` immediately following a multi-MB `RDMA_WRITE` that was acknowledged** (`nic_done` = the WRITE's index).
- The **receiver did apply the atomic** — its `waitSignal` for that epoch on that context had already passed — so the request reached the responder; the **atomic response never came back**, through all retries.
- The responder's own put in the reverse direction on the same QP pair is unacknowledged (`NIC<pi`) while all its other QPs are healthy: the RC connection is dead **in both directions**.
- Other ranks on the *same two NICs* completed their puts to each other in the same epoch; the port-level PFC pause and ECN/CNP counters did not change at all across the wedge. The stall is per connection, not per link.
- With the error CQE sitting in the ring, all 8 ranks spin: the erroring rank in `waitCounter`, everyone else in `waitSignal` waiting on it. Six dumps over 12 minutes are byte-identical.

## Reproducer (~90 s) and knob bisect

The missing ingredient turned out to be **ordinary host-driven NCCL traffic sharing the NICs**. A stand-alone torchrun script that replays the same launch sequence (8192-row puts of 2–7 MB with `SignalAdd` + `CounterInc`, then `waitCounter` / `waitSignal`) and, once per "layer", does a 256 MB `all_gather_into_tensor` on torch's own (host-proxy) NCCL communicator wedges in **~80–90 s, every time**. Without the all_gather the same script runs ~400 k launches clean.

We then ran that reproducer for 240 s per arm (600 s for the last one), everything else identical:

| arm | result |
|---|---|
| GDAKI baseline (`NCCL_GIN_TYPE=3`) | **wedge** at ~80 s, same `0x15` signature |
| `NCCL_IB_TIMEOUT=22` | **wedge**; the QP is already in ERR within ~20 s of the stall ⇒ the retransmits are being NAK'd, not timing out |
| no counters / no companion QP (`flush` instead of `waitCounter`) | **wedge** — the companion/WAIT-WQE chain is a bystander |
| `NCCL_GIN_GDAKI_MAX_QP_RD_ATOMIC=1` + `MAX_DEST_RD_ATOMIC=1` | **wedge** |
| `NCCL_GDAKI_USE_RELIABLE_DB=1` and `=2` (log confirms the no-dbrec modes on all QP groups) | **wedge** |
| **`NCCL_GIN_TYPE=2` (CPU proxy backend)** | **clean**: 58 696 launches over 600 s + 240 s, vs one wedge per ~4 700 launches on GDAKI |

So with the same NICs, the same WRITE + ATOMIC_FA pattern, the same interfering host-NCCL traffic and the same application code, only the **GPU-driven QP path** (DevX QP, WQ/CQ in GPU memory, GPU doorbell) loses a connection; a host-ibverbs-driven QP never does. That points at the GDAKI / DOCA GPUNetIO QP path or the firmware's handling of it rather than at the fabric or the application.

We are shipping on `NCCL_GIN_TYPE=2` for now (end-to-end it is at parity for this workload), but the GPU-driven path is the reason to use the device API.

## Asks

1. Make the device wait paths **exit on an error completion** (`MLX5_CQE_REQ_ERR`) instead of spinning — return an error / set the abort flag, so that `waitCounter`, `waitSignal` and `flush` cannot hang on a dead QP. (2.31.2's optional timeouts are a workaround, not a fix: an error is known immediately.)
2. Have GDAKI's error detection (2.31.2 event-based CQ error reporting) **act** — abort the comm or at least log a `WARN` — rather than only answering `ncclCommGetAsyncError` when asked; a device-API application has no natural place to poll it.
3. Is a **retry-exceeded on the signal atomic with a healthy responder** a known behaviour for bidirectional WRITE + ATOMIC_FA traffic on one GDAKI QP pair (ConnectX-7 RoCE v2, fw 40.47.2682) while host-driven QPs on the same NIC carry bulk traffic? Given the bisect above (only the GPU-driven QP path fails; `RELIABLE_DB`, `rd_atomic`, timeout make no difference), is there a firmware version, a DOCA GPUNetIO setting, or a GDAKI QP attribute we should try? We can rerun the reproducer with any diagnostic build within the hour.

The host-side queue snapshot tool and the torchrun reproducer are ours and can be shared.

## 评论 (3)

### kgioioso · 2026-09-04

Hi @kiwi3shark thanks for the report. I'll address the 2 issues separately.

## Error handling

Indeed, the Device API does not have error reporting or error handling. We are aware. For now, the recommend path is to query errors on the host via `GetAsyncError`. We actively maintain and improve the `GetAsyncError` path (for example, we recently improved the GDAKI perf of this path by switching to event-based error reporting). 

It's up to the user to call this function and decide how to act. We do not and should not make the decision to abort on behalf of users.

> a device-API application has no natural place to poll it.

I'm not sure I understand this claim. The application created a comm and a DevComm on the host. Why can't it query for errors?

## Error CQE with GDAKI with competing host traffic

This part is very interesting.

Do you have any value set in `/sys/class/infiniband/<device_name>/tc/<port_number>/traffic_class`? We recently discovered that the proxy path reads this value but the GDAKI path does not.

Out of curiosity, are you using the host RMA API for the host traffic? Is the host traffic related to the kernels running at the same time? I ask because we are increasingly seeing feature requests for host-initiated traffic and it's helpful to understand the use case more.

### kiwi3shark · 2026-09-05

Thanks @kgioioso , I'm not quite familiar with the network-related items so I let Fable-5.1 do the following experiments:

-- the traffic-class hint was the right one. Data from the box (16x GPU, 8x ConnectX-7 400G RoCE v2, fw 40.47.2682, NCCL 2.30.7):

## Traffic class

Every RDMA NIC on the box has the mlx5 global override set:

```
$ cat /sys/class/infiniband/mlx5_{1..8}/tc/1/traffic_class
Global tclass=236          # DSCP 59
$ mlnx_qos -i eth1
Priority trust state: dscp
dscp2prio mapping:  prio:0 dscp:07,...,00   prio:5 dscp:59
PFC configuration:  enabled 0 0 0 0 0 1 0 0
```

So on this fabric only DSCP 59 -> priority 5 is lossless (PFC + ECN/DCQCN); everything else is priority 0, lossy, no PFC. The kernel applies the global tclass to every QP that goes through `modify_qp`, so the host proxy QPs (and torch's own NCCL comm) run on DSCP 59 without anyone asking for it. The GDAKI QPs are DevX QPs built by DOCA verbs (`DEVX_SET(qpc, primary_address_path.dscp, traffic_class >> 2)`), the kernel override never touches them, and `gin_host_gdaki.cc` falls back to `NCCL_IB_TC_DEFAULT = 0` when no `NCCL_GIN_IB_TC` / `NCCL_IB_TC` is set. Net effect: the GPU-driven puts and the signal atomics were the only RoCE traffic on the box riding priority 0. Under bulk host-NCCL traffic on the same port they get dropped, the responder NAKs the PSN gap, seven immediate retries burn out, and the QP goes to ERR with `TRANSPORT_RETRY_EXC_ERR` -- which is exactly the syndrome we reported (the retries were NAK'd, not timed out).

## Experiment (same 90-second reproducer, GDAKI, 8 ranks, 256 MB host all_gather per layer)

| arm | env | result |
|---|---|---|
| A control | `NCCL_GIN_TYPE=3` (tclass 0) | **wedge at ~40 s** (progress stopped at layer 282 / ~2.3k launches, no completion after 330 s, killed) |
| B | `NCCL_GIN_TYPE=3 NCCL_GIN_IB_TC=236` | **600 s clean**: 5 247 layers, 41 976 launches, `ncclCommGetAsyncError` = ok on all 8 ranks |
| B2 | same, 1500 s | **1500 s clean**: 13 118 layers, 104 944 launches, async error = ok on all 8 ranks (B + B2 together: 146 920 launches, zero events; the untreated rate was ~1 per 2-5k launches) |

Per-priority port counters (ethtool, summed over the 8 NICs) during the arms: arm A moved **3.4 TB on priority 0** (and 1.3 TB on priority 5 from the host collectives) before it stalled; arm B moved **0.0 GB on priority 0** and 62.5 TB on priority 5, with ~5.0 M PFC pause frames received and zero discards on either priority. NIC-side `rx_prio0_discards` stayed 0 in arm A, so the loss is in the switch queue of the lossy class, as expected without PFC.

So the retry-exceeded is not a GDAKI/firmware defect: the GPU-driven QPs were simply the only RoCE traffic on the box outside the lossless class, and `NCCL_GIN_IB_TC=236` puts them where the kernel already puts every other QP. With that set the reproducer has not wedged.

Suggestions from our side: (a) have the GDAKI path pick up the device's `tc/<port>/traffic_class` when no `NCCL_IB_TC` is given, so DevX QPs inherit whatever the fabric enforces on kernel QPs; (b) at least print a WARN at GIN context creation when the sysfs global tclass is set and the GDAKI tclass differs from it -- this misconfiguration is silent and only shows up as a rare retry-exceeded.

## Your other questions

* Host traffic: plain `torch.distributed` collectives (all_gather / reduce_scatter / all_to_all) on torch's own NCCL communicator, i.e. the model's sequence-parallel and tensor-parallel traffic. We do not use the host RMA API. The device-API kernel is a persistent MoE expert-parallel dispatch/combine that overlaps with those collectives on the same NICs; the two use different communicators.
* On polling `ncclCommGetAsyncError`: fair point, we can poll it from the host thread that owns the comm. What made it awkward is that a device wait that will never complete owns all SMs, so a host poll has to abort the comm and the process rather than recover anything -- fine as a bounded failure, but a device-side exit on an error CQE would still be the better contract.


### kgioioso · 2026-09-05

Great! We're working on GDAKI TC management and should have a fix in the next few weeks.
