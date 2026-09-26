# [Issue #2360] [Bug] Hopper NVLS BF16 results depend on multicast allocation history and differ across H800 hosts with identical software

source: https://github.com/NVIDIA/nccl/issues/2360
state: open | updated: 2026-09-21T01:11:40Z
labels: resolved

## 正文

### How is this issue impacting you?

Lower performance than expected

### Share Your Debug Logs

### Summary

On a single 8× NVIDIA H800 node, the result of a large BF16 NVLS AllReduce on a fixed target process group changes deterministically according to how many other same-rank process groups were previously initialized by a tiny collective.

The target operation has:

- identical per-rank BF16 input values;
- identical target process-group membership and rank order;
- identical NCCL algorithm and protocol (`NVLS + SIMPLE`);
- identical public channel topology;
- explicit CUDA synchronization before the target operation.

Nevertheless, the output hash alternates with the number of live, credit-only peer communicators:

```text
0 tiny peer communicators -> hash A
1 tiny peer communicator  -> hash B
2 tiny peer communicators -> hash A
3 tiny peer communicators -> hash B
```

All ranks receive the same result within each run, and repeated executions of the same scenario are bitwise stable. This is not per-call randomness.

The alternation disappears when either:

```bash
NCCL_RUNTIME_CONNECT=0
```

or:

```bash
NCCL_NVLS_ENABLE=0
```

is set.

Destroying the tiny peer communicator before initializing the target communicator also restores hash A.

The same minimal reproducer was then run on a second physical 8× H800 host
with an identical PyTorch/CUDA/NCCL user-space stack. It exhibits the same
A/B/A/B alternation, but both stable hashes and the number of 0/1 elements are
different from the first host.

Finally, a real 48-block, 10-step inference workload was run on both hosts with
identical code, input, configuration, and checkpoint shards:

```text
NVLS enabled:  cross-host latent results differ significantly
NVLS disabled: complete result .pt files are byte-identical
```

### Why this appears distinct from existing reports

Related issues:

- #1497 reports NVLS non-determinism between calls. In this report, each scenario is stable; the result depends on the number of live, previously initialized communicators.
- #2077 reports multicast-slot exhaustion. This report does not exhaust slots or fail; it observes alternating, valid but numerically different BF16 results.
- #1906 reports incorrect rank order under NVLS. Here rank order and all-gather semantics are correct; only floating-point reduction values differ.

I could not find an existing issue covering deterministic numerical alternation caused by prior multicast-object allocation state.

### Environment

```text
GPU:                    8× NVIDIA H800
Kernel driver:          560.35.03
Loaded libcuda:         /usr/local/cuda-12.8/compat/lib.real/libcuda.so.570.86.10
nvidia-smi CUDA level:  12.8
PyTorch:                2.7.0+cu126
PyTorch CUDA runtime:   12.6.77
NCCL runtime:           2.26.2
NCCL package:           nvidia-nccl-cu12==2.26.2
Topology:               single node, 8 GPUs, NVSwitch/NVLS
CUDA Graph:             disabled
torch.compile:          disabled
```

The issue also reproduces after an explicit `torch.cuda.synchronize()` following every tiny peer collective.

### Minimal reproducer

```python
import hashlib
import os

import torch
import torch.distributed as dist


rank = int(os.environ["OMPI_COMM_WORLD_RANK"])
local_rank = int(os.environ["OMPI_COMM_WORLD_LOCAL_RANK"])
world_size = int(os.environ["OMPI_COMM_WORLD_SIZE"])
torch.cuda.set_device(local_rank)

dist.init_process_group(
    backend="nccl",
    init_method="tcp://127.0.0.1:" + os.environ["PORT"],
    rank=rank,
    world_size=world_size,
)

# Four independent ProcessGroupNCCL instances with identical ranks.
groups = [dist.new_group(range(world_size)) for _ in range(4)]
target_group = groups[0]

# A 1-element float32 AllReduce selects a tiny RING/LL operation. It lazily
# initializes the peer communicator and its NVLS credit multicast object, but
# it does not trigger the large NVLS data-buffer setup.
for peer_group in groups[1 : 1 + int(os.environ["N_TINY"])]:
    tiny = torch.ones(1, device="cuda", dtype=torch.float32)
    dist.all_reduce(tiny, group=peer_group)
    torch.cuda.synchronize()

# Mirror the application path where a permutation-only collective initializes
# the target communicator before its first large BF16 sum.
source = torch.arange(
    world_size * 1024,
    device="cuda",
    dtype=torch.bfloat16,
).reshape(world_size, 1024)
target = torch.empty_like(source)
dist.all_to_all_single(target, source, group=target_group)

# The exact mathematical sum is 1. Different BF16 parenthesizations can yield
# either 0 or 1:
#   (256 + -256) + 1 = 1
#   256 + (-256 + 1) = 0
rank_values = [256.0, -256.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
tensor = torch.full(
    (1_417_216,),
    rank_values[rank],
    device="cuda",
    dtype=torch.bfloat16,
)

dist.all_reduce(tensor, group=target_group)
torch.cuda.synchronize()

digest = hashlib.sha256(
    tensor.cpu().contiguous().view(torch.uint8).numpy().tobytes()
).hexdigest()

gathered_hashes = [None] * world_size
dist.all_gather_object(gathered_hashes, digest)

if rank == 0:
    unique_values, unique_counts = torch.unique(
        tensor.cpu(),
        return_counts=True,
    )
    print(
        "n_tiny=", os.environ["N_TINY"],
        "unique_values=", unique_values.tolist(),
        "unique_counts=", unique_counts.tolist(),
        "hash=", digest,
        "all_ranks_same=", len(set(gathered_hashes)) == 1,
        flush=True,
    )

dist.destroy_process_group()
```

Run:

```bash
for n in 0 1 2 3; do
  export N_TINY="$n"
  export PORT="$((30100 + n))"

  mpirun -np 8 \
    -x N_TINY \
    -x PORT \
    python3 nvls_multicast_parity_repro.py
done
```

### Actual output

```text
n_tiny=0
unique_values=[0.0, 1.0]
unique_counts=[696960, 720256]
hash=bae037d146a7a72f4e62f94f4bdaca4430ed22ba2531c5a6857c1207de4df29d
all_ranks_same=True

n_tiny=1
unique_values=[0.0, 1.0]
unique_counts=[708736, 708480]
hash=84edacdcfdd4e2ec3104353d3a978e91e8c7795341e89b724694cfde227613c3
all_ranks_same=True

n_tiny=2
unique_values=[0.0, 1.0]
unique_counts=[696960, 720256]
hash=bae037d146a7a72f4e62f94f4bdaca4430ed22ba2531c5a6857c1207de4df29d
all_ranks_same=True

n_tiny=3
unique_values=[0.0, 1.0]
unique_counts=[708736, 708480]
hash=84edacdcfdd4e2ec3104353d3a978e91e8c7795341e89b724694cfde227613c3
all_ranks_same=True
```

### Controls

#### Disable runtime connect

```bash
export NCCL_RUNTIME_CONNECT=0
```

All four scenarios become identical:

```text
n_tiny=0 -> bae037d146a7a72f...
n_tiny=1 -> bae037d146a7a72f...
n_tiny=2 -> bae037d146a7a72f...
n_tiny=3 -> bae037d146a7a72f...
```

#### Disable NVLS

```bash
export NCCL_NVLS_ENABLE=0
```

The result no longer depends on `N_TINY`:

```text
n_tiny=0 -> df3547bb0fd23e71...
n_tiny=1 -> df3547bb0fd23e71...
```

#### Cross-host control

The exact same reproducer and software stack were run on two physical 8× H800 hosts.

Host A:

```text
VBIOS:       96.00.A5.00.03
Board Part:  692-2G520-0280-001

n_tiny=0:
  unique_counts=[696960, 720256]
  hash=bae037d146a7a72f4e62f94f4bdaca4430ed22ba2531c5a6857c1207de4df29d

n_tiny=1:
  unique_counts=[708736, 708480]
  hash=84edacdcfdd4e2ec3104353d3a978e91e8c7795341e89b724694cfde227613c3
```

Host B:

```text
VBIOS:       96.00.CF.00.02
Board Part:  692-2G520-0280-501

n_tiny=0:
  unique_counts=[394624, 1022592]
  hash=b35614b7d3ab40c3f8dc8904e66d26bb1aafdd0874a8ccfb50356a68b59da535

n_tiny=1:
  unique_counts=[388224, 1028992]
  hash=4ba47d5a698b72d92e5c83d1ee43c0675f8b58502305e1c60b71739201e2cdab
```

Both hosts use:

```text
8× H800
kernel driver 560.35.03
CUDA 12.8 compat libcuda 570.86.10
PyTorch 2.7.0+cu126
NCCL 2.26.2
```

Application artifacts were independently verified:

```text
top-level code commit:
29be9ae5c81048cdcba6cd95b804f233167679ed

kdist commit:
a2d45fec9fb2728fae657492eefcb5ea658ba479

model commit:
473b7d36b16136d27413f3d606b40ddf09f676d8

server.json SHA256:
03a34eb5673b70f37016dd6de4622d609420ec6989216445c7299d18a448ff66
```

All input files passed SHA256 verification. All eight checkpoint shards have
identical byte sizes and identical SHA256 values over 4 MiB samples from their
start, middle, and end.

With `NCCL_NVLS_ENABLE=0`, both hosts produce the same minimal-reproducer hash:

```text
df3547bb0fd23e7156da922fb732c352958552cbc3c783a228344ec3127d7cc3
```

A full model inference using identical code, all input SHA256 values, model
configuration, and sampled hashes from all eight 65.88 GB checkpoint shards was
also tested on both hosts:

```text
NVLS enabled:  outputs differ
NVLS disabled: complete result .pt files are byte-identical
```

The byte-identical NVLS-disabled result:

```text
complete result.pt:
b92b167280706a1f34fafb2eb493dcd5153dd023d4f13a1a34c8577f57fe911b

video latent:
36c6625b68edebc684557fcba41a4cc096feb3fe2c72372c16c79bfc7028eb55

audio latent:
a43a1f1971fca2c2ab2249da74ca13e87efb12c894bec6bc09b9a85c6d7a999f
```

The cross-host result strongly indicates that the visible numerical signature is
determined below the NCCL logical algorithm/channel plan, in the physical
NVSwitch/multicast reduction path.

Their CPU/NIC topology also differs, while GPU-to-GPU connectivity is NV18 on
both systems.

#### Destroy the peer communicator

If the tiny peer communicator is destroyed before the target communicator is used:

```python
dist.all_reduce(tiny, group=peer_group)
torch.cuda.synchronize()
dist.destroy_process_group(peer_group)
```

the target result returns to the `n_tiny=0` hash.

#### Use a large NVLS operation on the peer

If the peer communicator first executes a large BF16 NVLS operation, it allocates both its credit and data multicast objects. The target result also returns to the `n_tiny=0` hash.

### NCCL TRACE observations

For both target signatures:

```text
Algorithm:        NVLS
Protocol:         SIMPLE
NVLS channels:    16
channel range:    0..15
ranks:            0..7
communicator API: ncclCommInitRankConfig
```

No `ncclCommSplit` is involved.

With no tiny peer communicator:

```text
target credit multicast create: ~2 MiB
target data multicast create:   ~512 MiB mapping
target hash:                     A
```

With one live tiny peer communicator:

```text
peer credit multicast create:   ~2 MiB
target credit multicast create: ~2 MiB
target data multicast create:   ~512 MiB mapping
target hash:                     B
```

No successful NVLS user-buffer registration is present in the REG logs. The target uses the regular staging-buffer path in both scenarios.

### Real application impact

The first affected audio/text reduction is numerically close between the two
NVLS signatures:

```text
audio:
  cosine similarity 0.99999222
  relative L2       0.394%

text:
  cosine similarity 0.99999134
  relative L2       0.416%
```

Both signatures are similarly close to an FP32 sum reference, so this does not
look like a missing rank, stale buffer, or an arithmetically invalid reduction.

However, the real model contains 48 blocks and 10 denoising steps, with at
least 960 audio/text attention reductions plus FFN and MoE communication. The
small BF16 perturbation is repeatedly injected and amplified by nonlinear
residual blocks, large distillation steps, and potentially discrete MoE top-k
routing.

Observed full-model cross-host cosine similarity with NVLS enabled:

```text
video latent: approximately 0.62
audio latent: approximately 0.94
```

With NVLS disabled, the same full-model outputs are bitwise identical across
hosts.

On Host B, adding one tiny WORLD-group barrier before the model subgroup is
first used makes the serving path bitwise equal to the direct path:

```text
direct DET0 video:
a6bf910e98e6a5b3a4815d4911d95424b5dd102776c346154ac3086f1638d7af

serving + WORLD barrier DET0 video:
a6bf910e98e6a5b3a4815d4911d95424b5dd102776c346154ac3086f1638d7af

serving without WORLD barrier DET0 video:
122068a80708f8c7adec0371bf342e8cfef6555e9bcfe4ab86c039991425b9e4
```

### Relevant NCCL 2.26.2 source paths

Exact tag:

```text
v2.26.2-1
f44ac759fee12ecb3cc6891e9e739a000f66fd70
```

Communicator initialization allocates the NVLS credit multicast object:

```text
src/transport/nvls.cc
ncclNvlsSetup()
  -> nvlsAllocateMem(creditSize)
  -> cuMulticastCreate()
```

The first selected NVLS algorithm lazily allocates the data multicast object:

```text
src/group.cc
  -> ncclNvlsBufferSetup()

src/transport/nvls.cc
ncclNvlsBufferSetup()
  -> nvlsAllocateMem(nvlsTotalSize)
  -> cuMulticastCreate()
```

The BF16 arithmetic uses NVSwitch hardware reduction:

```text
src/device/reduce_kernel.h
multimem.ld_reduce.relaxed.sys.global.add.bf16x2
```

### Expected behavior

Given the Hopper CUDA 12.8 determinism statement in #1497, we expected the same
process-group membership, rank-to-device mapping, per-rank input tensor,
algorithm/protocol/channel plan, and non-overlapping launch order to produce a
stable result independent of unrelated live communicators and physical H800
board revision.

If bitwise equality across independent NVLS multicast objects is not guaranteed by design, please clarify the expected numerical contract after the Hopper CUDA 12.8 determinism fix.

### Questions

1. Is this expected after the Hopper NVLS determinism fix in CUDA 12.8?
2. Can CUDA/NVSwitch multicast-object allocation order select different SHARP reduction groupings or parenthesization?
3. Is `NCCL_RUNTIME_CONNECT=0` an intended workaround for applications requiring stable BF16 results across different communicator initialization histories?
4. Is the behavior expected to change in a newer NCCL release or a full native R570+ driver stack?
5. Which additional CUDA driver, Fabric Manager, NVSwitch, or RAS logs would help identify the multicast context used by each `cuMulticastCreate` call?
6. Is cross-host bitwise equality expected for Hopper NVLS after the determinism
   fix, or is determinism only scoped to repeated calls on the same multicast
   object?

### Additional notes

The loaded CUDA stack uses a CUDA 12.8 forward-compat user-mode driver:

```text
/usr/local/cuda-12.8/compat/lib.real/libcuda.so.570.86.10
```

on top of kernel driver `560.35.03`. PyTorch itself uses CUDA runtime `12.6.77`.

It would be useful to know whether the CUDA 12.8 NVLS determinism guarantee requires a native R570 kernel driver, rather than the forward-compat configuration above.



### Steps to Reproduce the Issue

_No response_

### NCCL Version

2.26.2+ cu12.6

### Your platform details

H200
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.03              Driver Version: 560.35.03      CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H800                    On  |   00000000:18:00.0 Off |                    0 |
| N/A   38C    P0            121W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H800                    On  |   00000000:29:00.0 Off |                    0 |
| N/A   45C    P0            129W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H800                    On  |   00000000:3A:00.0 Off |                    0 |
| N/A   37C    P0            124W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H800                    On  |   00000000:4B:00.0 Off |                    0 |
| N/A   45C    P0            130W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H800                    On  |   00000000:9A:00.0 Off |                    0 |
| N/A   38C    P0            125W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H800                    On  |   00000000:AA:00.0 Off |                    0 |
| N/A   45C    P0            128W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H800                    On  |   00000000:BA:00.0 Off |                    0 |
| N/A   40C    P0            127W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H800                    On  |   00000000:CA:00.0 Off |                    0 |
| N/A   45C    P0            127W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

### Error Message & Behavior

this may cause bitwise diff

## 评论 (7)

### xiaofanl-nvidia · 2026-08-23

++ @KaimingOuyang to take a look at this 

### KaimingOuyang · 2026-08-24

@wqshr12345 Can you try to run NCCL 2.27+ version? We improve the NVLS precision after 2.26

### NolenLiang · 2026-09-01

We tried to reproduce this on GB200 (single node, 4 GPUs, NVL72 racks) with NCCL 2.29.7 (PyTorch 2.13.0+cu130, `NCCL_ALGO=NVLS`, 16 MiB fp32 messages) and could not reproduce either symptom:

- **Allocation history**: creating *and exercising* 1-4 additional sub-communicators (pairwise `new_group` + an allreduce on each) before re-running the WORLD allreduce did not change the result -- bitwise-identical hashes across all history states. Run-to-run over 200 iterations on the same communicator was also stable (single hash).
- **Cross-host**: the same seeded input produced bitwise-identical results on three different nodes (different NVL72 racks).

One observation that may be relevant to the ordering question: we ran cancellation probes -- placing `1e8, 1.0, -1e8, 1.0` across the 4 ranks in six different permutations (fp32). Under NVLS **every permutation returned the exact sum (2.0)**, which no fp32 pairwise reduction order can produce for all placements. This suggests the in-switch reduction accumulates at higher-than-input precision on this stack, making the combine order invisible at these operand counts/magnitudes. Ring/Tree on the same nodes return order-dependent (and chunk-position-dependent) results, as expected.

Happy to share the probe script if useful. It would be interesting to know whether the Hopper behavior persists on 2.29.x -- i.e. whether this was fixed in NCCL or is architectural.

### xiaofanl-nvidia · 2026-09-04

++ @justus-nv 

### rybruscoe · 2026-09-07

A reading of the A/B/A/B pattern that also explains why the GB200 run didn't reproduce it, plus a test that tells "different but both valid" apart from "wrong".

With NVLS the reduction happens in the switch, and the layout of that reduction (which multicast object, how the message gets chunked, the order partial sums meet in) is fixed at communicator setup based on whatever multicast state exists at that moment. Your credit-only peers change that state. So the target communicator ends up with one tree at 0 live peers, another at 1, and back to the first at 2, which is the alternation you see. Each tree is deterministic, hence every scenario being bitwise stable. They give different bits because the data is BF16: each partial sum gets rounded to 8 mantissa bits, so change the order the partials meet and the result moves. Hash A and hash B are both correct answers to "sum these BF16 values in some order". Neither is the exact sum.

That also covers the rest. `NCCL_NVLS_ENABLE=0` drops to ring, which has a fixed order, so the allocation state stops mattering. Your second host has a different multicast layout, so its A and B are different values again. And the "improved NVLS precision after 2.26" change is most likely wider accumulation inside the switch. That shrinks the per-hop error but can't remove the order dependence of the final BF16 rounding. So a 16 MiB fp32 run on GB200 with 2.29 looking stable is what I'd expect, and it doesn't say much about BF16 on 2.26.

Test that decides it: build an order-independent reference sum of the same BF16 inputs (accumulate exactly, fp64 with Kahan or integer, round once at the end), then check whether A and B are each within one BF16 ulp per element of that reference. If both are, this is order dependence and the fix is a fixed reduction order, not more precision. If one of them is further off than that, there's a real reduction bug and it deserves the escalation. The "differ significantly" on the 48-block run is what order-dependent rounding turns into after 48 nonlinear layers. Under BF16 collectives that's expected, and not by itself evidence of a bug.

We ran into the same thing in RL training, where accumulation order alone flipped reward verdicts, and put the experiments here: https://github.com/anomly-labs/rl-reproducibility. The exact-reduction reference from that work (same bits whatever the tree, slower) lives in https://github.com/anomly-labs/computation-receipts if you want it as the oracle above. Neither is an NCCL patch.

Disclosure: I work on rl-reproducibility and computation-receipts.


### justus-nv · 2026-09-10

> @wqshr12345 Can you try to run NCCL 2.27+ version? We improve the NVLS precision after 2.26

@wqshr12345 Were you able to test @KaimingOuyang suggestion? NCCL 2.27+ may address your issue.

### justus-nv · 2026-09-16

@wqshr12345 Sorry for the long delay with a proper response to your questions.

I tested your repro and verified the failure a Hopper system on my end. I also tested it against a newer version of NCCL (v2.27) and your repro did not exhibit the non-determinism you observed. The newer version of NCCL accumulates the reduction in fp32, which is why the repro passes. This is not a fix for the underlying issue, but it does help mitigate it in many cases. It depends on your specific numerical ranges, so you will need to test with your own data to determine whether this approach fits your needs.

This issue is specific to Hopper. If a newer version of NCCL does not resolve your issue, the next step is to update your kernel driver and Fabric Manager to 550.144.03 or later or 570+. The 560.35.03 kernel driver you reported does not include the fix; the 560 branch never received it.

The fix is in the kernel driver and Fabric Manager. The CUDA user-space library (`libcuda.so`) version does not affect it.

> (2) Can multicast-object allocation order select different reduction groupings or parenthesization?

On Hopper systems with the unfixed driver and Fabric Manager, yes. 

> (3) Is `NCCL_RUNTIME_CONNECT=0` an intended workaround for applications requiring stable BF16 results across different communicator initialization histories?

No, this is not intended to be a determinism control. It only changes the multicast object allocation from lazy to init time. This happens to make allocation of internal multicast objects more repeatable, but any other multicast allocation before communicator init will change the order of operations again.

