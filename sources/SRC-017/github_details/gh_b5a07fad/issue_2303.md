# [Issue #2303] [Issue]: OW_LATENCY dispatch/combine receives time out on GB200/GB300 NVL72

source: https://github.com/NVIDIA/nccl/issues/2303
state: closed | updated: 2026-08-08T10:02:27Z
labels: 

## 正文


## NCCL EP LOW_LATENCY dispatch times out on GB200/GB300 NVL72 (HIGH_THROUGHPUT and classic-NVLink LL both pass)

**Setup:** GB200/GB300 NVL72, 4 GPUs/tray (also reproduces world=8 across two trays), one rank/GPU. DeepSeek-V3-like workload: 256 routed experts, top-k 8, hidden 7168, BF16.

```python
import nccl.core, nccl.ep
comm = nccl.core.Communicator.init(nranks, rank, unique_id)
cfg = nccl.ep.GroupConfig(algorithm=nccl.ep.Algorithm.LOW_LATENCY, num_experts=256,
    max_dispatch_tokens_per_rank=256, max_recv_tokens_per_rank=256 * nranks,
    max_token_bytes=7168 * 2, alloc=alloc_cfg)
grp = nccl.ep.Group.create(comm, cfg)     # succeeds; windows register fine
h = grp.create_handle(layout=nccl.ep.Layout.EXPERT_MAJOR, topk_idx=idx, stream=s)
h.dispatch(DispatchInputs(x), DispatchOutputs(...), stream=s)  # receives time out
s.synchronize()                                                # raises 719
```

`NCCL_CUMEM_ENABLE=1`; fails with `NCCL_MNNVL_ENABLE=1` and `=0` alike (verified value reaches ranks via `os.environ`, since baked container env vars can silently override job-level exports).

**Control experiments:** Swapping to `algorithm=HIGH_THROUGHPUT` (+ `Layout.FLAT`, unweighted combine) passes on identical world/fabric/payload (world=8 and 16 over MNNVL). The identical LL sequence passes on H100/H200/B200/B300 (world=8, classic intra-node NVLink, x86_64).

| Setup | P2P transport | HT | LL |
|---|---|---|---|
| H100/H200/B200/B300, world=8, 1 node, x86_64 | classic intra-node NVLink | ✅ | ✅ |
| GB200/GB300, world=8, 2 trays, `MNNVL_ENABLE=1` | P2P/MNNVL | ✅ | ❌ timeout |
| GB200, world=4, 1 tray, `MNNVL_ENABLE=1` | P2P/MNNVL | ✅ | ❌ timeout |
| GB200, world=4, 1 tray, `MNNVL_ENABLE=0` | P2P/CUMEM | — | ❌ timeout |

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

Captured with `NCCL_DEBUG=INFO`, `NCCL_DEBUG_SUBSYS=INIT,P2P,ENV,ALLOC,NET,REG`, `NCCL_EP_DEBUG=1` on the minimal reproducer (GB200, world=4, one tray, one process per GPU, 2026-07-23). Two runs shown: **A** = `NCCL_MNNVL_ENABLE=1`, **B** = `NCCL_MNNVL_ENABLE=0`. Excerpts below; full per-rank logs available on request.

**Run A** — version banners and init; MNNVL engages even at `nNodes 1`:

```
NCCL EP version 0.1.0+cuda13.3

watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO cudaDriverVersion 13000
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO NCCL version 2.30.7+cuda13.3
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO GIN/Plugin: Assigned plugin GIN_IB_GDAKI type 3 to comm
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO Using network IB
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO NCCL_CUMEM_ENABLE set by environment to 1.
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO MNNVL busId 0x801000 fabric UUID a44167d15423d758.7d6b24c07d32e7b3 cliqueId 0x2786 state 3 healthMask 0xaa
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO NCCL_MNNVL_ENABLE set by environment to 1.
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO MNNVL 1 cliqueId 2786 cliqueSize 4 cliqueRank 0 nvlDomainSize 4
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO comm 0x9a39870 rank 0 nRanks 4 nNodes 1 localRanks 4 localRank 0 MNNVL 1
```

All 256 P2P connect lines in run A are MNNVL (zero `via P2P/direct`):

```
watchtower-navy-cn13:2619530:2619530 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[1] via P2P/MNNVL
```

EP buffer imports and window registration succeed (rank 2 shown):

```
watchtower-navy-cn13:2619532:2619532 [2] NCCL INFO transport/p2p.cc:321 (ncclP2pImportShareableBuffer) Imported shareable buffer device 2 size 10485760 ptr 0xe8e2cd200000
watchtower-navy-cn13:2619532:2619532 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
watchtower-navy-cn13:2619532:2619532 [2] NCCL INFO register comm 0x56e33070 buffer 0xbee0000000 size 1968048128
watchtower-navy-cn13:2619532:2619532 [2] NCCL INFO [2] Segment 0, Type : 1, numSegments : 1, Segment size : 1969225728, memHandle : 1969225728
watchtower-navy-cn13:2619532:2619532 [2] NCCL INFO Inserted window 0xbe6000d000 into address map, ret=0
```

Then the first LL dispatch: every receive waits out the full EP timeout (94 warnings in run A, spanning every (rank, src_rank) pair — including direct NVLink neighbors like rank 2 ← rank 0):

```
NCCL EP: using timeout=96993ms (env=unset, config.timeout_ns=0, source=compile-time default)
Warning: NCCL EP timeout for dispatch receive, rank 2, local_expert_idx 37, src_rank 0
Warning: NCCL EP timeout for dispatch receive, rank 2, local_expert_idx 39, src_rank 0
Warning: NCCL EP timeout for combine receive, rank 0, local_expert_idx 28, src_rank 1
Warning: NCCL EP timeout for combine receive, rank 0, local_expert_idx 30, src_rank 1
...
```

**Run B** — identical setup, `NCCL_MNNVL_ENABLE=0` verified in the rank env; the transport genuinely changes to `P2P/CUMEM`, and LL fails identically (176 timeout warnings):

```
watchtower-navy-cn13:2630772:2630772 [0] NCCL INFO NCCL_CUMEM_ENABLE set by environment to 1.
watchtower-navy-cn13:2630772:2630772 [0] NCCL INFO MNNVL busId 0x801000 fabric UUID a44167d15423d758.7d6b24c07d32e7b3 cliqueId 0x2786 state 3 healthMask 0xaa
watchtower-navy-cn13:2630772:2630772 [0] NCCL INFO NCCL_MNNVL_ENABLE set by environment to 0.
watchtower-navy-cn13:2630772:2630772 [0] NCCL INFO comm 0x440e92d0 rank 0 nRanks 4 nNodes 1 localRanks 4 localRank 0 MNNVL 0

watchtower-navy-cn13:2630772:2630772 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[1] via P2P/CUMEM (all 256 connect lines are P2P/CUMEM)

NCCL EP: using timeout=96993ms (env=unset, config.timeout_ns=0, source=compile-time default)
Warning: NCCL EP timeout for dispatch receive, rank 2, local_expert_idx 7, src_rank 3
Warning: NCCL EP timeout for dispatch receive, rank 2, local_expert_idx 5, src_rank 3
...
```

Both runs then fail at the next stream synchronization with the device-side trap:

```
  File ".../bench/ep_harness.py", line 248, in sample
    torch.cuda.synchronize()
  File "/usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py", line 1162, in synchronize
    return torch._C._cuda_synchronize()
torch.AcceleratorError: CUDA error: unspecified launch failure
```

followed by teardown fallout from the poisoned context (not the cause):

```
[2026-07-23 04:16:01] watchtower-navy-cn13:2619531:2620804 [1] misc/strongstream.cc:424 (ncclStrongStreamSynchronize) NCCL WARN Cuda failure 'unspecified launch failure'
[2026-07-23 04:16:01] watchtower-navy-cn13:2619531:2620804 [1] init.cc:2745 (commDestroySync) NCCL WARN commDestroySync: comm 0x3a0f7f50 rank 1 sync deviceStream error 1
[2026-07-23 04:16:01] watchtower-navy-cn13:2619531:2620804 [1] allocator.cc:132 (ncclMemFree) NCCL WARN Cuda failure 'unspecified launch failure'
[2026-07-23 04:16:01] watchtower-navy-cn13:2619531:2620804 [1] init.cc:2869 (commReclaim) NCCL WARN commReclaim: cleanup comm 0x3a0f7f50 rank 1 failed in destroy/abort, error 1
```

### Steps to Reproduce the Issue

On a GB200 (or GB300) NVL72 system, 4 GPUs on one tray (also reproduces at world=8 across two trays), one rank per GPU. Workload shape is DeepSeek-V3-like: 256 routed experts, top-k 8, hidden 7168, BF16.

```python
import nccl.core, nccl.ep

# bootstrap: broadcast unique_id over any rendezvous (we use a torch gloo PG)
comm = nccl.core.Communicator.init(nranks, rank, unique_id)

cfg = nccl.ep.GroupConfig(
    algorithm=nccl.ep.Algorithm.LOW_LATENCY,
    num_experts=256,
    max_dispatch_tokens_per_rank=256,
    max_recv_tokens_per_rank=256 * nranks,
    max_token_bytes=7168 * 2,             # bf16
    alloc=alloc_cfg,
)
grp = nccl.ep.Group.create(comm, cfg)     # succeeds; windows register fine
h = grp.create_handle(layout=nccl.ep.Layout.EXPERT_MAJOR, topk_idx=idx, stream=s)
h.dispatch(DispatchInputs(x), DispatchOutputs(...), stream=s)  # <- receives time out
s.synchronize()                                                # <- raises 719
```

Environment: `NCCL_CUMEM_ENABLE=1`; fails with both `NCCL_MNNVL_ENABLE=1` and `=0` (verify the value actually reaches the ranks — container images that bake NCCL env
vars can silently override job-level exports; we set it via `os.environ` in-process).

Control experiments:

- Swapping `algorithm=HIGH_THROUGHPUT` (+ `Layout.FLAT`, unweighted combine): the identical world/fabric/payload **passes** (world=8 and world=16 over MNNVL).
- The identical LL sequence **passes** on H100/H200/B200/B300 (world=8, classic intra-node NVLink, `x86_64`).

### NCCL Version

2.30.7+cuda13.3

### Your platform details

- **GB200 NVL72** (4× GB200 per tray, Grace-Blackwell `aarch64`, NVLink domain of 72):
  fails at world=4 (single tray, `nvlDomainSize 4` clique in the logs) and world=8 (two trays)
- **GB300 NVL72** (4× GB300 per tray, `aarch64`): fails at world=8 (two trays)
- CUDA driver 13.0 (`cudaDriverVersion 13000`), CUDA 13.0 container (`linux/arm64`), Slurm + enroot, one process per GPU
- Node NICs (present but not in play at these world sizes — all peers are LSA/NVLink):
  4× IB 400G NDR `mlx5_0/1/3/4` on GB200; the `GIN_IB_GDAKI` plugin is assigned to the
  comm but all EP peers are within one NVL72 clique

### Error Message & Behavior

In `Algorithm.LOW_LATENCY` mode on GB200/GB300 NVL72 systems, `dispatch`/`combine` never complete their cross-rank receives: every receive waits out the full ~97 s EP timeout, the kernel traps, and the CUDA context is poisoned (`cudaErrorLaunchFailure`, 719). 

## 评论 (3)

### xiaofanl-nvidia · 2026-07-27

@artpol84 could you take a quick look? 
@Oseltamivir it might be better to open this in nccl-extensions repo as per https://github.com/NVIDIA/nccl/issues/2308, unless you believe this issue is actually caused by the core NCCL. 

### artpol84 · 2026-07-28

@Oseltamivir for the sanity check - can you try reproducing with  NCCL EP's `ep_bench`?
One thing that seems wrong is the config:
```
cfg = nccl.ep.GroupConfig(
    algorithm=nccl.ep.Algorithm.LOW_LATENCY,  
    num_experts=256,
    max_dispatch_tokens_per_rank=256,
    max_recv_tokens_per_rank=256 * nranks,       <---- LL does not support this configuration
    max_token_bytes=7168 * 2,             # bf16
    alloc=alloc_cfg,
)
```

As I mentioned above, LL doesn't support max_recv_tokens_per_rank and for Expert-major layout requires `nranks x nLocalExperts x max_dispatch_tokens_per_rank` (or equivalently `num_experts x max_dispatch_tokens_per_rank`) slots to be allocated.
If you have more than 1 expert per GPU the amount of `nranks x 256` is insufficient and may lead to a hang I believe.

IF you want to use rank-major layout that allows providing `nranks x 256` you need to specify the right layout at handle creation and do permutation yourself

### Oseltamivir · 2026-07-29

Update: `ep_bench` does **not** reproduce this, and pretty useful:

**Real trigger: more than one LL handle on the same group.** `handle->ll.buffer_idx` (the double-buffer parity selector, flipped at `nccl_ep.cc:2540` and `:3087`) is per-handle, but `handle->ll.layout`'s offsets point into the per-group `rdma_buffer`. Two handles with the same config get identical offsets, so they alias the same parity-0/1 count and flag slots while advancing parity independently — one handle's "safe to clean" buffer is another's "in flight". Counts and flags share an offset, so both are hit.

Stock `nccl4py[cu13]==0.3.1`, GB200, 4 ranks, same workload, changing only the number of handles the caller creates:

| LL handles on the group | result |
|---|---|
| 1 | `rc=0`, zero receive timeouts, correctness passing |
| 2 | 64 dispatch + 6 combine receive timeouts → 719 |

Our benchmark creates one handle per token count and interleaves them, so it fails almost immediately. `ep_bench` creates one handle, so it stays green, 8 configurations up to 20 000 iterations, including the per-iteration `MPI_Barrier` removed, an injected 500 ms stall on one rank, and dispatch-only and combine-only loops. So rank stagger and loop shape are ruled out.

also, the mechanism I gave (a rank lapping a parity cycle) is wrong: the stale values come from a sibling handle. And LL does *not* work on x86 as I claimed: the same benchmark wedges there too, 5/5 across H100 ×2, B300 ×2, B200 ×1. This is not GB200/GB300- or MNNVL-specific. Sorry for the detour.

On `max_recv_tokens_per_rank`: not the cause. For LL the docs give `NCCL_EP_AUTO → nRanks * max_dispatch_tokens_per_rank`, which is exactly the value we passed, and `LowLatencyLayout` never takes the field. Our expert-major output is the documented `[num_local_experts, num_ranks * max_dispatch_tokens_per_rank, hidden]` = `[64, 1024, 7168]`; my original snippet elided `DispatchOutputs(...)`, which made it look smaller.

Possible fix: Generation-tagging the signal values (#2306) makes stale and foreign values inert and clears the failure (full T=1…256 ladders at world=4 and world=8), but given the corrected cause that is a symptom fix — the structural one is per-handle signal regions, or one group-level parity counter all handles advance. Happy to reshape it and re-file against nccl-extensions; I hadn't seen #2308, and the code there still has the untagged sends (`ll_ep.cuh` L462, L1379) and bare `== 0` polls (L509, L1418).

Main question: is interleaving multiple LL handles on one group meant to be supported? If not, could the second `ncclEpInitHandle` fail loudly instead of costing a ~97 s timeout and a `trap()`?

If not intentions to change, I'll close

