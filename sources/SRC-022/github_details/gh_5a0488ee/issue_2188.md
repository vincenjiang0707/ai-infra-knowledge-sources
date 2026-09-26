# [Issue #2188] hipIpcGetMemHandle fails (invalid argument) at p2p.cc:256 when a second GPU-disjoint process initialises on the same MI350X node

source: https://github.com/ROCm/rccl/issues/2188
state: closed | updated: 2026-08-24T04:48:40Z
labels: 

## 正文

**Title:** `hipIpcGetMemHandle` fails (`invalid argument`) at `p2p.cc:256` when a second GPU-disjoint process initialises on the same MI350X node

---

## Summary

On an 8-GPU MI350X (gfx950) node, a first process using 4 GPUs initialises RCCL
normally and runs fine. A **second** process on the **disjoint** 4 GPUs then
fails during RCCL init:

```
transport/p2p.cc:250  Cuda Alloc Size 6291456 pointer 0x... flags 3
transport/p2p.cc:256  NCCL WARN hipIpcGetMemHandle failed : invalid argument
                      [FATAL ERROR]: HIP failure: 'invalid argument'
```

The 6 MB allocation at `p2p.cc:250` **succeeds**; only the IPC export of that
pointer fails. It fails on every rank of the joining process.

The first process is **never affected** — it keeps serving throughout.

This is intermittent but heavily weighted to failure: **2 successes in 62
bring-up attempts** across two MI350X nodes. We have found no configuration that
predicts the outcome, and we are **not** proposing a mechanism.

## Environment

Two 8-GPU MI350X (gfx950) bare-metal nodes, both reproducing the failure:

```
RCCL      2.27.7-HEAD:29e1567
HIP       7.2.53211-97f5574fe2
ROCm      7.2.4.0-93-97f5574fe2
ROCr      1.18
firmware  44
kernel    6.8.0-136-generic
```

The two nodes differ in one relevant respect: **one boots with `iommu=pt`, the
other has no `iommu=` argument at all.** Both fail (see table below), so this is
recorded as non-predictive rather than as a factor.

Each process runs in its own container, `--network host`, with a disjoint
`ROCR_VISIBLE_DEVICES` set. No GPU is shared between the two processes.

## Reproduction

1. Start process 1 with `ROCR_VISIBLE_DEVICES=0,1,2,3`, 4-rank RCCL comm. Wait
   until it is healthy.
2. Start process 2 with `ROCR_VISIBLE_DEVICES=4,5,6,7`, 4-rank RCCL comm.
3. Process 2 dies at `p2p.cc:256` during init, on all 4 ranks, ~50–60 s in.
4. Process 1 continues normally.

Retrying step 2 eventually succeeds — observed on attempt 17 of one sequence —
and once both processes are up, the pair is stable (one such pair sustained six
full benchmark passes with balanced throughput across the two processes).

## Measured bring-up rates

All attempts start from a verified-clean node: no orphaned SysV IPC segments, no
stale `/dev/kfd` holders, no leftover processes, all 8 GPUs at 0% VRAM.

| node | condition | success |
|---|---|---|
| no `iommu=pt` | GPU memory ~0.90 of device, first process on host IPC ns | **2 / 26** |
| no `iommu=pt` | same, both processes in private IPC ns | 0 / 14 |
| no `iommu=pt` | GPU memory ~0.62 of device | 0 / 14 |
| **`iommu=pt`** | ~0.90, application IPC pool = plain `hipMalloc` | 0 / 5 |
| **`iommu=pt`** | ~0.90, application IPC pool = default caching allocator | 0 / 3 |
| | **pooled** | **2 / 62** |

## What we ruled out — each with a control, not by reasoning

| candidate | result |
|---|---|
| `NCCL_DMABUF_ENABLE=1` | interleaved off/on/on/off/off/on → **0/3 on, 0/3 off**; `p2p.cc:256` present in all six |
| `iommu=pt` | the node **with** it: 0/5 and 0/3. The node **without** it produced both successes. Non-predictive in both directions |
| container IPC namespace | successes seen with host+private and with private+private; failures seen with every shape |
| GPU memory envelope | failures at ~0.62 and ~0.90; the only successes were at ~0.90 |
| driver / library version | identical on both nodes; success and failure minutes apart on one node with nothing changed |
| node-global IPC state | checked before every attempt (see above); always clean |
| our own IPC usage | see next section |

RCCL also reports on every rank, on both nodes:

```
NCCL WARN Missing "iommu=pt" from kernel command line ...
NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
```

We tested both. Neither changes the outcome.

## This is not our own IPC usage

Our application also calls `hipIpcGetMemHandle` for a custom all-reduce, so we
removed that as a variable. We switched the application's IPC pool to a plain
`hipMalloc` allocation — exportable by construction — and verified per rank from
the process log that the new pool was actually in use. `p2p.cc:256` still failed
identically. A control with that change reverted failed the same way (`0/5` vs
`0/3` in the table above).

So the application-side pool choice is **orthogonal** to this failure. Our own
`hipIpcGetMemHandle` failure appears *later* in the log than `p2p.cc:256` and is
downstream of it; it is not what this report is about.

## The observation that most constrains the cause

**The incumbent process is never harmed.** Across ~50 consecutive second-process
failures on two nodes, process 1 never dropped a request, never restarted, and
logged no error.

Whatever makes the export invalid appears scoped to the *joining* process's own
handle export, not to node-global IPC state — otherwise we would expect the
incumbent to degrade as well.

## Attachments

- `rccl_p2p_excerpt.log` — 1893 lines, `NCCL_DEBUG=INFO`,
  `NCCL_DEBUG_SUBSYS=INIT,ALLOC,ENV`: full RCCL init of the failing process from
  version banner through transport selection to the `p2p.cc:256` failure and its
  unwind. Hostnames, IP addresses and application identifiers are redacted;
  library/driver versions, allocation sizes, flags and pointers are intact.
- Per-attempt logs for the 17-attempt retry sequence, and for the rate table
  rows, are available on request.

### Init banner (redacted)

```
[lib] load RCCL version: 2.27.7
node [0] NCCL INFO Kernel version: 6.8.0-136-generic

[2026-08-23 09:56:58] node [0] /app/rccl/build/release/hipify/src/init.cc:213 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
node [0] NCCL INFO Hipruntime version: 70253211, firmware version: 44
node [0] NCCL INFO ROCr version 1.18
node [0] NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
node [0] NCCL INFO Kernel version: 6.8.0-136-generic

[2026-08-23 09:56:58] node [0] /app/rccl/build/release/hipify/src/init.cc:213 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
node [0] NCCL INFO RCCL version : 2.27.7-HEAD:29e1567
HIP version  : 7.2.53211-97f5574fe2
ROCm version : 7.2.4.0-93-97f5574fe2
Hostname     : (redacted)
Librccl path : /usr/local/lib/librccl.so.1
node [0] NCCL INFO /app/rccl/build/release/hipify/src/init.cc:2491 Cuda Host Alloc Size 4 pointer 0x73cba4001000
node [0] NCCL INFO NET/Plugin: Could not find: libnccl-net.so. 
node [0] NCCL INFO NET/IB : No device found.
node [0] NCCL INFO NET/IB : Using [RO]; OOB eth0:165.245.165.177<0>
node [0] NCCL INFO NET/Socket : Using [0]eth0:165.245.165.177<0> [1]eth1:REDACTED-IP<0> [2]eth2:REDACTED-IP<0> [3]eth3:REDACTED-IP<0> [4]eth4:REDACTED-IP<0> [5]eth5:REDACTED-IP<0> [6]eth6:REDACTED-IP<0> [7]eth7:REDACTED-IP<0> [8]eth8:REDACTED-IP<0> [9]eth9:REDACTED-IP<0> [10]tailscale0:REDACTED-IP<0> [11]flannel.1:REDACTED-IP<0> [12]cni0:REDACTED-IP<0>
node [0] NCCL INFO Initialized NET plugin Socket
node [0] NCCL INFO Assigned NET plugin Socket to comm
node [0] NCCL INFO Using network Socket
node [0] NCCL INFO Created side stream 0x27cd19f0 of dev 0 busid a3000
```

### The allocation, then the failed export

```
node [1] NCCL INFO /app/rccl/build/release/hipify/src/channel.cc:45 Cuda Alloc Size 72 pointer 0x75b4f033e000 flags 0
node [1] NCCL INFO ncclCudaCallocDebug: Memory used = 34342400 on device = 1
node [1] NCCL INFO /app/rccl/build/release/hipify/src/channel.cc:56 Cuda Alloc Size 16 pointer 0x75b4f033f000 flags 0
node [1] NCCL INFO Mem Realloc old size 0, new size 8 pointer 0x75b48c0012b0
node [1] NCCL INFO Found side stream 0x370389e0 of dev 1 busid ab000 count 1
node [1] NCCL INFO ncclCudaCallocDebug: Memory used = 40633856 on device = 1
node [1] NCCL INFO /app/rccl/build/release/hipify/src/transport/p2p.cc:250 Cuda Alloc Size 6291456 pointer 0x75b499600000 flags 3

[2026-08-23 09:56:59] node [1] /app/rccl/build/release/hipify/src/transport/p2p.cc:256 NCCL WARN hipIpcGetMemHandle failed : invalid argument
node [1] NCCL INFO ncclCudaFree: Memory used = 34342400 on device = 1
node [1] [FATAL ERROR]: HIP failure: 'invalid argument'
node [1] NCCL INFO /app/rccl/build/release/hipify/src/transport/p2p.cc:709 -> 1
node [1] NCCL INFO /app/rccl/build/release/hipify/src/transport/p2p.cc:510 -> 1
node [1] NCCL INFO /app/rccl/build/release/hipify/src/transport.cc:47 -> 1
node [1] NCCL INFO /app/rccl/build/release/hipify/src/transport.cc:182 -> 1
node [1] NCCL INFO /app/rccl/build/release/hipify/src/transport/generic.cc:25 -> 1
node [3] NCCL INFO /app/rccl/build/release/hipify/src/channel.cc:45 Cuda Alloc Size 72 pointer 0x7404d6738000 flags 0
node [3] NCCL INFO ncclCudaCallocDebug: Memory used = 34334160 on device = 3
```

## What we are asking

1. Is `hipIpcGetMemHandle` expected to be reliable for RCCL's P2P setup when a
   second, GPU-disjoint process initialises on the same node? If there is a
   documented constraint we are violating, we would rather fix our side.
2. Is there a supported way to make this deterministic — a transport selection,
   an environment variable, or a required host configuration we have missed?
3. If this is a genuine bug: the allocation at `p2p.cc:250` succeeds and only the
   export fails, on a pointer RCCL itself just allocated with `flags 3`. Is that
   combination expected to always be exportable?

We are not claiming a mechanism. Every mechanism we hypothesised was falsified by
one of the controls above, and we would rather report the negative result
accurately than guess.


## 评论 (2)

### ThomasNing · 2026-08-24

**Update: reproduced with a second, completely independent application — the failure is not application-level.**

The original report came from one inference framework. I have now reproduced it on the **same node, same RCCL build**, using an entirely different framework: different container image, different Python stack, different distributed-init code path, no shared application code with the first.

The failure is **byte-identical**:

```
node [0] NCCL INFO .../rccl/src/transport/p2p.cc:250 Cuda Alloc Size 6291456 pointer 0x7dcfd6600000 flags 3
[2026-08-24 01:02:12] node [0] .../rccl/src/transport/p2p.cc:256 NCCL WARN hipIpcGetMemHandle failed : invalid argument
node [1] NCCL INFO .../rccl/src/transport/p2p.cc:250 Cuda Alloc Size 6291456 pointer 0x7ee8f8a00000 flags 3
[2026-08-24 01:02:12] node [1] .../rccl/src/transport/p2p.cc:256 NCCL WARN hipIpcGetMemHandle failed : invalid argument
node [2] NCCL INFO .../rccl/src/transport/p2p.cc:250 Cuda Alloc Size 6291456 pointer 0x779b70600000 flags 3
[2026-08-24 01:02:12] node [2] .../rccl/src/transport/p2p.cc:256 NCCL WARN hipIpcGetMemHandle failed : invalid argument
node [3] NCCL INFO .../rccl/src/transport/p2p.cc:250 Cuda Alloc Size 6291456 pointer 0x727991400000 flags 3
[2026-08-24 01:02:12] node [3] .../rccl/src/transport/p2p.cc:256 NCCL WARN hipIpcGetMemHandle failed : invalid argument
```

Same allocation size (`6291456`), same `flags 3`, same `p2p.cc:250` success followed by `p2p.cc:256` export failure, on all 4 ranks of the joining process. The incumbent process again continued serving unaffected.

Second framework's bring-up on this node: **0 / 6** attempts.

**Why this matters for triage:** two applications that share nothing above RCCL fail at the same allocation with the same flags on the same line. That removes application-level IPC usage, allocator behaviour, and framework-specific init ordering from consideration. Whatever invalidates the export is inside RCCL's P2P setup or below it.

**One methodological note for anyone reproducing this**, because it cost me a wrong conclusion: the second framework runs its ranks as child processes whose stderr does not reach the container log, so `NCCL_DEBUG=WARN` produced **zero** NCCL lines and the `p2p.cc` warning appeared to be absent. It is not absent — it only becomes visible with:

```
NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ALLOC,ENV NCCL_DEBUG_FILE=/some/dir/rccl.%h.%p.log
```

`NCCL_DEBUG_FILE` bypasses the swallowed stderr and writes one log per rank. Without it, this failure is easily misattributed to the application layer — which is exactly what happened to me twice before filing.

### ThomasNing · 2026-08-24

Recreated in ROCm/rocm-systems as https://github.com/ROCm/rocm-systems/issues/10609 because GitHub did not permit a native cross-repository transfer with the current account permissions. The original report and follow-up comment were preserved there. Closing this copy as migrated.
