# [Issue #2077] NCCL 2.29.7: NVLS multicast slot exhaustion causes fatal error instead of graceful fallback

source: https://github.com/NVIDIA/nccl/issues/2077
state: open | updated: 2026-08-14T22:30:55Z
labels: Community Discussion

## 正文

## Summary

NCCL 2.29.7 exhausts all 128 NVSwitch multicast slots when creating NVLS transport for multiple sub-communicators (e.g., FSDP 2-rank sub-communicators), then crashes with a fatal `ncclUnhandledCudaError` instead of falling back to non-NVLS transport. NCCL 2.28.9 handled this gracefully.

## Environment

- **Hardware:** 8x NVIDIA H200 (NV18 NVLink interconnect, 4x NVSwitch)
- **NCCL:** 2.29.7+cuda12.8
- **CUDA:** 13.0
- **Driver:** 580.65.06
- **Fabric Manager:** 580.65.06 (running, State: Completed, Status: Success)
- **OS:** RHEL 10 (kernel 6.12.0)
- **PyTorch:** upstream main (commit 5bfd4be)

## Error

```
torch.distributed.DistBackendError: NCCL error in: /pytorch/torch/csrc/distributed/c10d/NCCLUtils.cpp:93, unhandled cuda error, NCCL version 2.29.7
ncclUnhandledCudaError: Call to CUDA function failed.
Failed to bind NVLink SHARP (NVLS) Multicast memory of size 2097152 : CUDA error 2 'out of memory'.
This is usually caused by a system or configuration error in the Fabric Manager or NVSwitches.
Disable NVLS (NCCL_NVLS_ENABLE=0) if you wish to avoid this error in the future.
```

## Root Cause Analysis

We traced this through the Fabric Manager logs and confirmed:

1. NVSwitch hardware has a **hard limit of 128 multicast slots**
2. NCCL 2.29.7 creates NVLS multicast groups for every sub-communicator (including 2-rank FSDP sub-communicators)
3. Each rank creates ~10 multicast groups per sub-communicator
4. With 8 GPUs and multiple FSDP sub-communicators, this exhausts all 128 slots
5. **None of the groups are freed** during the test — they are only released when communicators are destroyed
6. When slot 128 is requested, `cuMulticastBindMem` fails with `CUDA error 2 (out of memory)`
7. NCCL 2.29.7 treats this as a **fatal error** and crashes

### Fabric Manager log evidence:

```
[INFO] multicast group 126 is allocated.
[INFO] multicast group 127 is allocated.
[ERROR] all the NVSwitch multicast resources/slot ids are used for partition id -1.
[ERROR] failed to allocated resource to the multicast team setup request id ...
```

- **128 groups allocated** (0–127) before failure
- **0 groups freed** during active test
- **Peak concurrent active groups: 127**

## Regression from NCCL 2.28.9

NCCL 2.28.9 either:
- Created fewer multicast groups (did not create per-pair 2-rank NVLS groups for sub-communicators), or
- Handled the allocation failure gracefully by falling back to non-NVLS transport

NCCL 2.29.7 appears to have introduced more aggressive NVLS usage for sub-communicators and removed the graceful fallback path.

## Reproducer

Run the following PyTorch FSDP distributed test on an 8x H200 system with NCCL 2.29.7:

```bash
# Fails — NVLS enabled (default)
python test/distributed/_composable/fsdp/test_fully_shard_training.py \
  TestFullyShard1DTrainingCore.test_train_parity_multi_group

# Passes — NVLS disabled
NCCL_NVLS_ENABLE=0 python test/distributed/_composable/fsdp/test_fully_shard_training.py \
  TestFullyShard1DTrainingCore.test_train_parity_multi_group
```

The test is from upstream PyTorch (`test/distributed/_composable/fsdp/test_fully_shard_training.py`).

## NCCL env vars tested (none resolve the issue)

| Configuration | Result |
|---|---|
| `NCCL_NVLS_TREE_ENABLE=0` | FAILED — still exhausts 128 slots |
| `NCCL_NVLS_NCHANNELS=1` | FAILED — still exhausts slots |
| `NCCL_NVLS_TREE_ENABLE=0` + `NCCL_NVLS_NCHANNELS=1` + `NCCL_MAX_NCHANNELS=2` | FAILED |
| `NCCL_NVLS_ENABLE=0` | PASSED (only workaround) |

## Expected Behavior

When NVSwitch multicast slots are exhausted, NCCL should **fall back gracefully** to non-NVLS transport (NVLink P2P, ring, tree) instead of crashing with a fatal error. This is what NCCL 2.28.9 did.

## Suggested Improvements

1. **Graceful fallback:** When `cuMulticastBindMem` fails with `CUDA error 2`, fall back to non-NVLS transport for that communicator instead of returning `ncclUnhandledCudaError`
2. **Resource-aware NVLS:** Avoid creating NVLS multicast groups for small (2-rank) sub-communicators where the performance benefit over NVLink P2P is minimal
3. **Configurable limit:** Provide an env var (e.g., `NCCL_NVLS_MAX_GROUPS`) to cap total multicast group allocation across all communicators

## 评论 (2)

### xiaofanl-nvidia · 2026-04-04

Falling back gracefully to hide lower level issues with NVLS caused a hang at large scale training job (not all ranks get the same error that NVLS cannot work, so some of them think NVLS is good while others silently fell back to disable NVLS), which we spent a lot of time debugging, so we decided to not hide the issue from lower level stack and require users to either explicitly disable NVLS for their use case, or get a hard error when NVLS is enable but doesn't work. 

@subinz1 please let us know if this makes sense to you. We are open to discussing ways to make your life easier. But we are hesitant to add complexity to NCCL that hides lower level SW/system config issues because it will end up costing a lot more than convenience - e.g. debugging at thousand GPU scale for months. 

### xiaofanl-nvidia · 2026-08-14

Quick update on this: 

We recently added a new toggle in commConfig to allow users to selectively disable host APIs from using NVLS resources on some communicators. Device API is not impacted and still controlled with devCommCreate. We hope this can be helpful in this issue. See more https://github.com/NVIDIA/nccl/commit/b194d662b5d05e78e15008b295a86cb9fada6c88. 

We are continuing to optimize the usage of NVLS slot in NCCL and plan to release some of these optimizations as part of 2.32. 
