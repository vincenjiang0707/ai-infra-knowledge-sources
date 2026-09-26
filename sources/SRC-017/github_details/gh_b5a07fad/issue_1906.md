# [Issue #1906] [Issue]: `all_gather` returns tensors in incorrect rank order for certain permutation of `CUDA_VISIBLE_DEVICES` and `NCCL_ALGO=NVLS ` (regression in NCCL 2.26.2; NCCL 2.21.5 OK)

source: https://github.com/NVIDIA/nccl/issues/1906
state: open | updated: 2026-09-21T01:41:09Z
labels: resolved

## 正文

### How is this issue impacting you?

Data corruption

### Share Your Debug Logs

We are seeing silent rank order corruption in `all_gather` in the following 2 scenarios:

**Scenario 1:**
1. Certain permutation of `CUDA_VISIBLE_DEVICES` (e.g., `1,2,3,4,5,6,7,0` or `3,4,5,6,7,0,1,2`)
2. `NCCL_P2P_DISABLE=1`
3. NCCL version is 2.26.2 and PyTorch version is 2.7
4. Using 8 GPUs on a node.

**Scenario 2:**
1. Certain permutation of `CUDA_VISIBLE_DEVICES` (e.g., `1,2,3,4,5,6,7,0` or `3,4,5,6,7,0,1,2`)
2. `NCCL_ALGO=NVLS`
3. NCCL version is 2.26.2 and PyTorch version is 2.7
4. Using 8 GPUs on a node.

I think the underlying reason to cause the issue for both scenarios might be related, and setting `NCCL_P2P_DISABLE=1` just makes the issue more obvious to reproduce at small load.

### Steps to Reproduce the Issue

Below is a minimal repro script `nccl_debug.py`:
```
# Test PyTorch NCCL
import torch
import torch.distributed as dist
import os

# Initialize distributed to get rank
dist.init_process_group(backend='nccl')
rank = dist.get_rank()
world_size = dist.get_world_size()

# Collect information silently
cuda_visible_devices = os.environ.get('CUDA_VISIBLE_DEVICES', 'NOT SET')
nccl_p2p_disable = os.environ.get('NCCL_P2P_DISABLE', 'NOT SET')

# Collect NCCL environment variables
nccl_env_vars = []
for key, value in sorted(os.environ.items()):
    if 'NCCL' in key:
        nccl_env_vars.append(f"{key}: {value}")

# Collect PyTorch and CUDA information
pytorch_version = torch.__version__
cuda_available = torch.cuda.is_available()
device_count = torch.cuda.device_count()
nccl_version = torch.cuda.nccl.version() if cuda_available else "N/A"
device_names = []
if cuda_available:
    for i in range(device_count):
        device_names.append(f"Device {i}: {torch.cuda.get_device_name(i)}")

# Set up device
local_rank = rank % device_count
dev = torch.device("cuda", local_rank)
device_name = torch.cuda.get_device_name(dev)
torch.cuda.set_device(dev)
current_device = torch.cuda.current_device()

# Create tensors and perform all_gather
x = torch.full((4,), float(rank), device=dev)
out = [torch.empty_like(x) for _ in range(world_size)]

dist.barrier()
dist.all_gather(out, x)
dist.barrier()

# Verify results
results = []
all_passed = True
for i, t in enumerate(out):
    expected = float(i)
    actual = t[0].item()
    passed = torch.all(t == float(i))
    results.append(f"  From rank {i}: {t.tolist()} (expected {expected}, got {actual}) - {'✓' if passed else '✗'}")
    if not passed:
        all_passed = False

# Build entire summary as a single string to print atomically
summary_lines = []
summary_lines.append(f"\n{'='*80}")
summary_lines.append(f"[RANK {rank}/{world_size}] NCCL DEBUG SUMMARY")
summary_lines.append(f"{'='*80}")
summary_lines.append(f"[ENVIRONMENT]")
summary_lines.append(f"  CUDA_VISIBLE_DEVICES: {cuda_visible_devices}")
summary_lines.append(f"  NCCL_P2P_DISABLE: {nccl_p2p_disable}")
if nccl_env_vars:
    summary_lines.append(f"  NCCL environment variables:")
    for nccl_var in nccl_env_vars:
        summary_lines.append(f"    {nccl_var}")

summary_lines.append(f"[PYTORCH & CUDA]")
summary_lines.append(f"  PyTorch version: {pytorch_version}")
summary_lines.append(f"  CUDA available: {cuda_available}")
summary_lines.append(f"  CUDA device count: {device_count}")
summary_lines.append(f"  NCCL version: {nccl_version}")
for device_name_line in device_names:
    summary_lines.append(f"  {device_name_line}")

summary_lines.append(f"[DEVICE ASSIGNMENT]")
summary_lines.append(f"  Local rank: {local_rank}")
summary_lines.append(f"  Assigned device: {dev}")
summary_lines.append(f"  Device name: {device_name}")
summary_lines.append(f"  Current device: {current_device}")

summary_lines.append(f"[NCCL ALL_GATHER RESULTS]")
summary_lines.append(f"  Input tensor: {x.tolist()}")
for result_line in results:
    summary_lines.append(result_line)

summary_lines.append(f"[STATUS]")
if all_passed:
    summary_lines.append(f"  ✓✓✓ SUCCESS: All tests passed on rank {rank}")
else:
    summary_lines.append(f"  ✗✗✗ FAILURE: Some tests failed on rank {rank}")
summary_lines.append(f"{'='*80}\n")

# Synchronize before printing
dist.barrier()

# Print entire summary as one atomic operation
print("\n".join(summary_lines))

# Synchronize after printing
dist.barrier()
```
To reproduce the issue, run

**Scenario 1:**
```
export CUDA_VISIBLE_DEVICES="1,2,3,4,5,6,7,0"
export NCCL_P2P_DISABLE=1
torchrun --nproc-per-node 8 --standalone nccl_debug.py
```
**Scenario 2:**
```
export CUDA_VISIBLE_DEVICES="1,2,3,4,5,6,7,0"
export NCCL_ALGO=NVLS
torchrun --nproc-per-node 8 --standalone nccl_debug.py
```

### NCCL Version

2.26.2

### Your platform details

NVIDIA-SMI 550.163.01             Driver Version: 550.163.01     CUDA Version: 12.4

### Error Message & Behavior

Here are the results from the repro script:

**NCCL 2.26.2 and PyTorch 2.7 Result**
```
W1109 22:17:45.166000 46353 torch/distributed/run.py:766] 
W1109 22:17:45.166000 46353 torch/distributed/run.py:766] *****************************************
W1109 22:17:45.166000 46353 torch/distributed/run.py:766] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. 
W1109 22:17:45.166000 46353 torch/distributed/run.py:766] *****************************************
[rank3]:[W1109 22:17:55.859904220 ProcessGroupNCCL.cpp:4715] [PG ID 0 PG GUID 0 Rank 3]  using GPU 3 as device used by this process is currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. You can pecify device_id in init_process_group() to force use of a particular device.
[rank7]:[W1109 22:17:55.369605334 ProcessGroupNCCL.cpp:4715] [PG ID 0 PG GUID 0 Rank 7]  using GPU 7 as device used by this process is currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. You can pecify device_id in init_process_group() to force use of a particular device.
[rank6]:[W1109 22:17:56.583847830 ProcessGroupNCCL.cpp:4715] [PG ID 0 PG GUID 0 Rank 6]  using GPU 6 as device used by this process is currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. You can pecify device_id in init_process_group() to force use of a particular device.
[rank0]:[W1109 22:17:56.647513632 ProcessGroupNCCL.cpp:4715] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 as device used by this process is currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. You can pecify device_id in init_process_group() to force use of a particular device.
[rank5]:[W1109 22:17:56.647638104 ProcessGroupNCCL.cpp:4715] [PG ID 0 PG GUID 0 Rank 5]  using GPU 5 as device used by this process is currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. You can pecify device_id in init_process_group() to force use of a particular device.
[rank1]:[W1109 22:17:56.750041798 ProcessGroupNCCL.cpp:4715] [PG ID 0 PG GUID 0 Rank 1]  using GPU 1 as device used by this process is currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. You can pecify device_id in init_process_group() to force use of a particular device.
[rank4]:[W1109 22:17:56.803963466 ProcessGroupNCCL.cpp:4715] [PG ID 0 PG GUID 0 Rank 4]  using GPU 4 as device used by this process is currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. You can pecify device_id in init_process_group() to force use of a particular device.
[rank2]:[W1109 22:17:56.825434231 ProcessGroupNCCL.cpp:4715] [PG ID 0 PG GUID 0 Rank 2]  using GPU 2 as device used by this process is currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. You can pecify device_id in init_process_group() to force use of a particular device.

================================================================================
[RANK 1/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.7.0+cu126
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 26, 2)
[DEVICE ASSIGNMENT]
  Local rank: 1
  Assigned device: cuda:1
  Current device: 1
[NCCL ALL_GATHER RESULTS]
  Input tensor: [1.0, 1.0, 1.0, 1.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [7.0, 7.0, 7.0, 7.0] (expected 1.0, got 7.0) - ✗
  From rank 2: [1.0, 1.0, 1.0, 1.0] (expected 2.0, got 1.0) - ✗
  From rank 3: [2.0, 2.0, 2.0, 2.0] (expected 3.0, got 2.0) - ✗
  From rank 4: [3.0, 3.0, 3.0, 3.0] (expected 4.0, got 3.0) - ✗
  From rank 5: [4.0, 4.0, 4.0, 4.0] (expected 5.0, got 4.0) - ✗
  From rank 6: [5.0, 5.0, 5.0, 5.0] (expected 6.0, got 5.0) - ✗
  From rank 7: [6.0, 6.0, 6.0, 6.0] (expected 7.0, got 6.0) - ✗
[STATUS]
  ✗✗✗ FAILURE: Some tests failed on rank 1
================================================================================

================================================================================
[RANK 0/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.7.0+cu126
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 26, 2)
[DEVICE ASSIGNMENT]
  Local rank: 0
  Assigned device: cuda:0
  Current device: 0
[NCCL ALL_GATHER RESULTS]
  Input tensor: [0.0, 0.0, 0.0, 0.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [7.0, 7.0, 7.0, 7.0] (expected 1.0, got 7.0) - ✗
  From rank 2: [1.0, 1.0, 1.0, 1.0] (expected 2.0, got 1.0) - ✗
  From rank 3: [2.0, 2.0, 2.0, 2.0] (expected 3.0, got 2.0) - ✗
  From rank 4: [3.0, 3.0, 3.0, 3.0] (expected 4.0, got 3.0) - ✗
  From rank 5: [4.0, 4.0, 4.0, 4.0] (expected 5.0, got 4.0) - ✗
  From rank 6: [5.0, 5.0, 5.0, 5.0] (expected 6.0, got 5.0) - ✗
  From rank 7: [6.0, 6.0, 6.0, 6.0] (expected 7.0, got 6.0) - ✗
[STATUS]
  ✗✗✗ FAILURE: Some tests failed on rank 0
================================================================================

================================================================================
[RANK 5/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.7.0+cu126
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 26, 2)
[DEVICE ASSIGNMENT]
  Local rank: 5
  Assigned device: cuda:5
  Current device: 5
[NCCL ALL_GATHER RESULTS]
  Input tensor: [5.0, 5.0, 5.0, 5.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [7.0, 7.0, 7.0, 7.0] (expected 1.0, got 7.0) - ✗
  From rank 2: [1.0, 1.0, 1.0, 1.0] (expected 2.0, got 1.0) - ✗
  From rank 3: [2.0, 2.0, 2.0, 2.0] (expected 3.0, got 2.0) - ✗
  From rank 4: [3.0, 3.0, 3.0, 3.0] (expected 4.0, got 3.0) - ✗
  From rank 5: [4.0, 4.0, 4.0, 4.0] (expected 5.0, got 4.0) - ✗
  From rank 6: [5.0, 5.0, 5.0, 5.0] (expected 6.0, got 5.0) - ✗
  From rank 7: [6.0, 6.0, 6.0, 6.0] (expected 7.0, got 6.0) - ✗
[STATUS]
  ✗✗✗ FAILURE: Some tests failed on rank 5
================================================================================

================================================================================
[RANK 7/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.7.0+cu126
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 26, 2)
[DEVICE ASSIGNMENT]
  Local rank: 7
  Assigned device: cuda:7
  Current device: 7
[NCCL ALL_GATHER RESULTS]
  Input tensor: [7.0, 7.0, 7.0, 7.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [7.0, 7.0, 7.0, 7.0] (expected 1.0, got 7.0) - ✗
  From rank 2: [1.0, 1.0, 1.0, 1.0] (expected 2.0, got 1.0) - ✗
  From rank 3: [2.0, 2.0, 2.0, 2.0] (expected 3.0, got 2.0) - ✗
  From rank 4: [3.0, 3.0, 3.0, 3.0] (expected 4.0, got 3.0) - ✗
  From rank 5: [4.0, 4.0, 4.0, 4.0] (expected 5.0, got 4.0) - ✗
  From rank 6: [5.0, 5.0, 5.0, 5.0] (expected 6.0, got 5.0) - ✗
  From rank 7: [6.0, 6.0, 6.0, 6.0] (expected 7.0, got 6.0) - ✗
[STATUS]
  ✗✗✗ FAILURE: Some tests failed on rank 7
================================================================================

================================================================================
[RANK 4/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.7.0+cu126
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 26, 2)
[DEVICE ASSIGNMENT]
  Local rank: 4
  Assigned device: cuda:4
  Current device: 4
[NCCL ALL_GATHER RESULTS]
  Input tensor: [4.0, 4.0, 4.0, 4.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [7.0, 7.0, 7.0, 7.0] (expected 1.0, got 7.0) - ✗
  From rank 2: [1.0, 1.0, 1.0, 1.0] (expected 2.0, got 1.0) - ✗
  From rank 3: [2.0, 2.0, 2.0, 2.0] (expected 3.0, got 2.0) - ✗
  From rank 4: [3.0, 3.0, 3.0, 3.0] (expected 4.0, got 3.0) - ✗
  From rank 5: [4.0, 4.0, 4.0, 4.0] (expected 5.0, got 4.0) - ✗
  From rank 6: [5.0, 5.0, 5.0, 5.0] (expected 6.0, got 5.0) - ✗
  From rank 7: [6.0, 6.0, 6.0, 6.0] (expected 7.0, got 6.0) - ✗
[STATUS]
  ✗✗✗ FAILURE: Some tests failed on rank 4
================================================================================

================================================================================
[RANK 3/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.7.0+cu126
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 26, 2)
[DEVICE ASSIGNMENT]
  Local rank: 3
  Assigned device: cuda:3
  Current device: 3
[NCCL ALL_GATHER RESULTS]
  Input tensor: [3.0, 3.0, 3.0, 3.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [7.0, 7.0, 7.0, 7.0] (expected 1.0, got 7.0) - ✗
  From rank 2: [1.0, 1.0, 1.0, 1.0] (expected 2.0, got 1.0) - ✗
  From rank 3: [2.0, 2.0, 2.0, 2.0] (expected 3.0, got 2.0) - ✗
  From rank 4: [3.0, 3.0, 3.0, 3.0] (expected 4.0, got 3.0) - ✗
  From rank 5: [4.0, 4.0, 4.0, 4.0] (expected 5.0, got 4.0) - ✗
  From rank 6: [5.0, 5.0, 5.0, 5.0] (expected 6.0, got 5.0) - ✗
  From rank 7: [6.0, 6.0, 6.0, 6.0] (expected 7.0, got 6.0) - ✗
[STATUS]
  ✗✗✗ FAILURE: Some tests failed on rank 3
================================================================================

================================================================================
[RANK 2/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.7.0+cu126
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 26, 2)
[DEVICE ASSIGNMENT]
  Local rank: 2
  Assigned device: cuda:2
  Current device: 2
[NCCL ALL_GATHER RESULTS]
  Input tensor: [2.0, 2.0, 2.0, 2.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [7.0, 7.0, 7.0, 7.0] (expected 1.0, got 7.0) - ✗
  From rank 2: [1.0, 1.0, 1.0, 1.0] (expected 2.0, got 1.0) - ✗
  From rank 3: [2.0, 2.0, 2.0, 2.0] (expected 3.0, got 2.0) - ✗
  From rank 4: [3.0, 3.0, 3.0, 3.0] (expected 4.0, got 3.0) - ✗
  From rank 5: [4.0, 4.0, 4.0, 4.0] (expected 5.0, got 4.0) - ✗
  From rank 6: [5.0, 5.0, 5.0, 5.0] (expected 6.0, got 5.0) - ✗
  From rank 7: [6.0, 6.0, 6.0, 6.0] (expected 7.0, got 6.0) - ✗
[STATUS]
  ✗✗✗ FAILURE: Some tests failed on rank 2
================================================================================

================================================================================
[RANK 6/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.7.0+cu126
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 26, 2)
[DEVICE ASSIGNMENT]
  Local rank: 6
  Assigned device: cuda:6
  Current device: 6
[NCCL ALL_GATHER RESULTS]
  Input tensor: [6.0, 6.0, 6.0, 6.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [7.0, 7.0, 7.0, 7.0] (expected 1.0, got 7.0) - ✗
  From rank 2: [1.0, 1.0, 1.0, 1.0] (expected 2.0, got 1.0) - ✗
  From rank 3: [2.0, 2.0, 2.0, 2.0] (expected 3.0, got 2.0) - ✗
  From rank 4: [3.0, 3.0, 3.0, 3.0] (expected 4.0, got 3.0) - ✗
  From rank 5: [4.0, 4.0, 4.0, 4.0] (expected 5.0, got 4.0) - ✗
  From rank 6: [5.0, 5.0, 5.0, 5.0] (expected 6.0, got 5.0) - ✗
  From rank 7: [6.0, 6.0, 6.0, 6.0] (expected 7.0, got 6.0) - ✗
[STATUS]
  ✗✗✗ FAILURE: Some tests failed on rank 6
================================================================================
```
**NCCL 2.21.5 and PyTorch 2.6 Result**
```
W1109 22:19:14.214000 4815 torch/distributed/run.py:792] *****************************************
W1109 22:19:14.214000 4815 torch/distributed/run.py:792] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. 
W1109 22:19:14.214000 4815 torch/distributed/run.py:792] *****************************************
[rank6]:[W1109 22:19:24.164824990 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 6]  using GPU 6 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a particular device, or call init_process_group() with a device_id.
[rank7]:[W1109 22:19:25.700106572 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 7]  using GPU 7 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a particular device, or call init_process_group() with a device_id.
[rank1]:[W1109 22:19:25.821279724 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 1]  using GPU 1 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a particular device, or call init_process_group() with a device_id.
[rank3]:[W1109 22:19:25.849538390 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 3]  using GPU 3 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a particular device, or call init_process_group() with a device_id.
[rank0]:[W1109 22:19:25.944557362 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 0]  using GPU 0 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a particular device, or call init_process_group() with a device_id.
[rank5]:[W1109 22:19:25.960418667 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 5]  using GPU 5 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a particular device, or call init_process_group() with a device_id.
[rank4]:[W1109 22:19:25.015737744 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 4]  using GPU 4 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a particular device, or call init_process_group() with a device_id.
[rank2]:[W1109 22:19:25.026558830 ProcessGroupNCCL.cpp:4561] [PG ID 0 PG GUID 0 Rank 2]  using GPU 2 to perform barrier as devices used by this process are currently unknown. This can potentially cause a hang if this rank to GPU mapping is incorrect. Specify device_ids in barrier() to force use of a particular device, or call init_process_group() with a device_id.

================================================================================
[RANK 3/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.6.0+cu124
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 21, 5)
[DEVICE ASSIGNMENT]
  Local rank: 3
  Assigned device: cuda:3
  Current device: 3
[NCCL ALL_GATHER RESULTS]
  Input tensor: [3.0, 3.0, 3.0, 3.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [1.0, 1.0, 1.0, 1.0] (expected 1.0, got 1.0) - ✓
  From rank 2: [2.0, 2.0, 2.0, 2.0] (expected 2.0, got 2.0) - ✓
  From rank 3: [3.0, 3.0, 3.0, 3.0] (expected 3.0, got 3.0) - ✓
  From rank 4: [4.0, 4.0, 4.0, 4.0] (expected 4.0, got 4.0) - ✓
  From rank 5: [5.0, 5.0, 5.0, 5.0] (expected 5.0, got 5.0) - ✓
  From rank 6: [6.0, 6.0, 6.0, 6.0] (expected 6.0, got 6.0) - ✓
  From rank 7: [7.0, 7.0, 7.0, 7.0] (expected 7.0, got 7.0) - ✓
[STATUS]
  ✓✓✓ SUCCESS: All tests passed on rank 3
================================================================================

================================================================================
[RANK 2/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.6.0+cu124
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 21, 5)
[DEVICE ASSIGNMENT]
  Local rank: 2
  Assigned device: cuda:2
  Current device: 2
[NCCL ALL_GATHER RESULTS]
  Input tensor: [2.0, 2.0, 2.0, 2.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [1.0, 1.0, 1.0, 1.0] (expected 1.0, got 1.0) - ✓
  From rank 2: [2.0, 2.0, 2.0, 2.0] (expected 2.0, got 2.0) - ✓
  From rank 3: [3.0, 3.0, 3.0, 3.0] (expected 3.0, got 3.0) - ✓
  From rank 4: [4.0, 4.0, 4.0, 4.0] (expected 4.0, got 4.0) - ✓
  From rank 5: [5.0, 5.0, 5.0, 5.0] (expected 5.0, got 5.0) - ✓
  From rank 6: [6.0, 6.0, 6.0, 6.0] (expected 6.0, got 6.0) - ✓
  From rank 7: [7.0, 7.0, 7.0, 7.0] (expected 7.0, got 7.0) - ✓
[STATUS]
  ✓✓✓ SUCCESS: All tests passed on rank 2
================================================================================

================================================================================
[RANK 5/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.6.0+cu124
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 21, 5)
[DEVICE ASSIGNMENT]
  Local rank: 5
  Assigned device: cuda:5
  Current device: 5
[NCCL ALL_GATHER RESULTS]
  Input tensor: [5.0, 5.0, 5.0, 5.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [1.0, 1.0, 1.0, 1.0] (expected 1.0, got 1.0) - ✓
  From rank 2: [2.0, 2.0, 2.0, 2.0] (expected 2.0, got 2.0) - ✓
  From rank 3: [3.0, 3.0, 3.0, 3.0] (expected 3.0, got 3.0) - ✓
  From rank 4: [4.0, 4.0, 4.0, 4.0] (expected 4.0, got 4.0) - ✓
  From rank 5: [5.0, 5.0, 5.0, 5.0] (expected 5.0, got 5.0) - ✓
  From rank 6: [6.0, 6.0, 6.0, 6.0] (expected 6.0, got 6.0) - ✓
  From rank 7: [7.0, 7.0, 7.0, 7.0] (expected 7.0, got 7.0) - ✓
[STATUS]
  ✓✓✓ SUCCESS: All tests passed on rank 5
================================================================================

================================================================================
[RANK 6/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.6.0+cu124
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 21, 5)
[DEVICE ASSIGNMENT]
  Local rank: 6
  Assigned device: cuda:6
  Current device: 6
[NCCL ALL_GATHER RESULTS]
  Input tensor: [6.0, 6.0, 6.0, 6.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [1.0, 1.0, 1.0, 1.0] (expected 1.0, got 1.0) - ✓
  From rank 2: [2.0, 2.0, 2.0, 2.0] (expected 2.0, got 2.0) - ✓
  From rank 3: [3.0, 3.0, 3.0, 3.0] (expected 3.0, got 3.0) - ✓
  From rank 4: [4.0, 4.0, 4.0, 4.0] (expected 4.0, got 4.0) - ✓
  From rank 5: [5.0, 5.0, 5.0, 5.0] (expected 5.0, got 5.0) - ✓
  From rank 6: [6.0, 6.0, 6.0, 6.0] (expected 6.0, got 6.0) - ✓
  From rank 7: [7.0, 7.0, 7.0, 7.0] (expected 7.0, got 7.0) - ✓
[STATUS]
  ✓✓✓ SUCCESS: All tests passed on rank 6
================================================================================

================================================================================
[RANK 0/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.6.0+cu124
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 21, 5)
[DEVICE ASSIGNMENT]
  Local rank: 0
  Assigned device: cuda:0
  Current device: 0
[NCCL ALL_GATHER RESULTS]
  Input tensor: [0.0, 0.0, 0.0, 0.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [1.0, 1.0, 1.0, 1.0] (expected 1.0, got 1.0) - ✓
  From rank 2: [2.0, 2.0, 2.0, 2.0] (expected 2.0, got 2.0) - ✓
  From rank 3: [3.0, 3.0, 3.0, 3.0] (expected 3.0, got 3.0) - ✓
  From rank 4: [4.0, 4.0, 4.0, 4.0] (expected 4.0, got 4.0) - ✓
  From rank 5: [5.0, 5.0, 5.0, 5.0] (expected 5.0, got 5.0) - ✓
  From rank 6: [6.0, 6.0, 6.0, 6.0] (expected 6.0, got 6.0) - ✓
  From rank 7: [7.0, 7.0, 7.0, 7.0] (expected 7.0, got 7.0) - ✓
[STATUS]
  ✓✓✓ SUCCESS: All tests passed on rank 0
================================================================================

================================================================================
[RANK 1/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.6.0+cu124
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 21, 5)
[DEVICE ASSIGNMENT]
  Local rank: 1
  Assigned device: cuda:1
  Current device: 1
[NCCL ALL_GATHER RESULTS]
  Input tensor: [1.0, 1.0, 1.0, 1.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [1.0, 1.0, 1.0, 1.0] (expected 1.0, got 1.0) - ✓
  From rank 2: [2.0, 2.0, 2.0, 2.0] (expected 2.0, got 2.0) - ✓
  From rank 3: [3.0, 3.0, 3.0, 3.0] (expected 3.0, got 3.0) - ✓
  From rank 4: [4.0, 4.0, 4.0, 4.0] (expected 4.0, got 4.0) - ✓
  From rank 5: [5.0, 5.0, 5.0, 5.0] (expected 5.0, got 5.0) - ✓
  From rank 6: [6.0, 6.0, 6.0, 6.0] (expected 6.0, got 6.0) - ✓
  From rank 7: [7.0, 7.0, 7.0, 7.0] (expected 7.0, got 7.0) - ✓
[STATUS]
  ✓✓✓ SUCCESS: All tests passed on rank 1
================================================================================

================================================================================
[RANK 7/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.6.0+cu124
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 21, 5)
[DEVICE ASSIGNMENT]
  Local rank: 7
  Assigned device: cuda:7
  Current device: 7
[NCCL ALL_GATHER RESULTS]
  Input tensor: [7.0, 7.0, 7.0, 7.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [1.0, 1.0, 1.0, 1.0] (expected 1.0, got 1.0) - ✓
  From rank 2: [2.0, 2.0, 2.0, 2.0] (expected 2.0, got 2.0) - ✓
  From rank 3: [3.0, 3.0, 3.0, 3.0] (expected 3.0, got 3.0) - ✓
  From rank 4: [4.0, 4.0, 4.0, 4.0] (expected 4.0, got 4.0) - ✓
  From rank 5: [5.0, 5.0, 5.0, 5.0] (expected 5.0, got 5.0) - ✓
  From rank 6: [6.0, 6.0, 6.0, 6.0] (expected 6.0, got 6.0) - ✓
  From rank 7: [7.0, 7.0, 7.0, 7.0] (expected 7.0, got 7.0) - ✓
[STATUS]
  ✓✓✓ SUCCESS: All tests passed on rank 7
================================================================================

================================================================================
[RANK 4/8] NCCL DEBUG SUMMARY
================================================================================
[ENVIRONMENT]
  CUDA_VISIBLE_DEVICES: 1,2,3,4,5,6,7,0
  NCCL_P2P_DISABLE: 1
  NCCL environment variables:
    NCCL_P2P_DISABLE: 1
    NCCL_VERSION: 2.17.1-1
    NV_LIBNCCL_DEV_PACKAGE: libnccl-dev=2.17.1-1+cuda12.1
    NV_LIBNCCL_DEV_PACKAGE_NAME: libnccl-dev
    NV_LIBNCCL_DEV_PACKAGE_VERSION: 2.17.1-1
    NV_LIBNCCL_PACKAGE: libnccl2=2.17.1-1+cuda12.1
    NV_LIBNCCL_PACKAGE_NAME: libnccl2
    NV_LIBNCCL_PACKAGE_VERSION: 2.17.1-1
    TORCH_NCCL_ASYNC_ERROR_HANDLING: 1
[PYTORCH & CUDA]
  PyTorch version: 2.6.0+cu124
  CUDA available: True
  CUDA device count: 8
  NCCL version: (2, 21, 5)
[DEVICE ASSIGNMENT]
  Local rank: 4
  Assigned device: cuda:4
  Current device: 4
[NCCL ALL_GATHER RESULTS]
  Input tensor: [4.0, 4.0, 4.0, 4.0]
  From rank 0: [0.0, 0.0, 0.0, 0.0] (expected 0.0, got 0.0) - ✓
  From rank 1: [1.0, 1.0, 1.0, 1.0] (expected 1.0, got 1.0) - ✓
  From rank 2: [2.0, 2.0, 2.0, 2.0] (expected 2.0, got 2.0) - ✓
  From rank 3: [3.0, 3.0, 3.0, 3.0] (expected 3.0, got 3.0) - ✓
  From rank 4: [4.0, 4.0, 4.0, 4.0] (expected 4.0, got 4.0) - ✓
  From rank 5: [5.0, 5.0, 5.0, 5.0] (expected 5.0, got 5.0) - ✓
  From rank 6: [6.0, 6.0, 6.0, 6.0] (expected 6.0, got 6.0) - ✓
  From rank 7: [7.0, 7.0, 7.0, 7.0] (expected 7.0, got 7.0) - ✓
[STATUS]
  ✓✓✓ SUCCESS: All tests passed on rank 4
================================================================================
```

## 评论 (10)

### xiangxl-a · 2025-11-11

The issue seems to not be reproducible after `export NCCL_ALGO="^NVLS"` for any permutation of `CUDA_VISIBLE_DEVICES`. Is there any change for NVLS from NCCL 2.21.5 to NCCL 2.26.2?

### sjeaugey · 2025-11-12

The NVLS algorithm should not be enabled by default for allgather operations. Were you forcing that algorithm when you saw data corruption?

Also, as I understand, the bug seemed to be in 2.26, but disappeared in 2.27. [For 2.21, I'm not sure whether allgather/NVLS was even implemented]. @KaimingOuyang does that ring a bell?

### xiangxl-a · 2025-11-12

Thanks @sjeaugey for the response. 

> The NVLS algorithm should not be enabled by default for allgather operations. Were you forcing that algorithm when you saw data corruption?

That's good to know, but we don't force NVLS in the actual LLM inference application, and we saw this issue when NCCL_ALGO is not set (which NCCL will chose the algo to use) in a more subtle way. I enabled it here just for debugging purpose which will make this issue much easier to reproduce with a min repro script. In the actual LLM inference application (with NCCL_ALGO not set), we saw incorrect token probabilities generated at relatively high load with TP=8 and certain permutation of CUDA_VISIBLE_DEVICES (not following PCI BUS ID order). When we set NCCL_ALGO=^NVLS, we no longer saw such issue in the LLM inference application under the same condition with all other parameters unchanged. 

> the bug seemed to be in 2.26, but disappeared in 2.27. 

From my testing, I still can reproduce the issue in 2.27.3 & PyTorch 2.8

> For 2.21, I'm not sure whether allgather/NVLS was even implemented

At least in 2.21.5 doc https://docs.nvidia.com/deeplearning/nccl/archives/nccl_2215/user-guide/docs/env.html, I can see NVLS as a possible value for NCCL_ALGO, which says it is available since 2.17+

### sjeaugey · 2025-11-13

Ok thanks for the confirmation. We're looking into it.


### xiangxl-a · 2025-11-18

Hello Team, is there an update?

### sjeaugey · 2025-11-19

The single node NVLS allgather algorithms seems to be missing the user rank table which ensures proper data ordering. Fixing it requires some work.

Now, we're also not sure why that algorithm was even selected. In theory we should not be using it as it's supposed to be always slower than the ring algorithm. Would you be able to share the log with `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ENV,TUNING`?

### xiangxl-a · 2025-11-23

Thanks @sjeaugey for looking into this issue! 

> Now, we're also not sure why that algorithm was even selected. In theory we should not be using it as it's supposed to be always slower than the ring algorithm. 

Good to know. Would you recommend to set NCCL ALGO explicitly to Ring as a mitigation? If NVLS is always slower than Ring, what's the benefit of NVLS (assuming it must be better than Ring in some other perspectives)?

> Would you be able to share the log with NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ENV,TUNING?

After setting the above env variables, I can see both 
```
 NCCL INFO AllGather: 579600 Bytes -> Algo NVLS proto SIMPLE channel{Lo..Hi}={0..15}
```
and 
```
NCCL INFO AllGather: 515200 Bytes -> Algo RING proto LL channel{Lo..Hi}={0..23}
```
Is there any specific log pattern you are looking for? I can share those specific logs as well. The issue can be reproduced in vLLM application as well if you want to test it. 


### sjeaugey · 2025-11-24

I would not suggest to set NCCL_ALGO in general, aside from disabling a very specific algorithm for a specific operation, as a temporary workaround.

So setting `NCCL_ALGO=allgather:^NVLS` would be my recommendation until this is resolved.

> If NVLS is always slower than Ring, what's the benefit of NVLS (assuming it must be better than Ring in some other perspectives)?

NVLS uses a lot less SMs, especially when operating on registered buffers. So, if low SM usage is more important than peak bandwidth, NVLS may help with overall performance.

### EylonKrause · 2026-06-24

Traced this against current `master` — sharing in case it's useful, with the upfront caveat that I **can't validate it on hardware** (single-GPU dev box, no NVSwitch), so the below is static analysis and should be treated as a hypothesis to confirm.

## Description

Single-node NVLS `AllGather` writes each head's gathered slice at its **dense head index** instead of the head's **user rank**, so output chunks are mis-ordered whenever `CUDA_VISIBLE_DEVICES` permutes ranks out of NVLS/PCI discovery order (slot 0 happens to land correctly, slots 1..n-1 are rotated).

The single-node, non-registered gather (`src/device/all_gather.h`, `work->oneNode`) issues `prims.gather(offset, nvls->nHeads*count, nelem, count, -1, 0)`, which resolves in `ScatterGatherOp` (`src/device/prims_simple.h`, Recv branch) to `pOffset = i * peerOffset; dst0 = dsts[0] + pOffset`. The peer index `i` is the dense head index (`nvls->up[h] = nRanks+1+h`), not the user rank. The three sibling paths remap via `rank = collNetDenseToUserRank[node*nRails+rail]` (multi-node NVLS `all_gather.h:230`, CollNetDirect `:459`, ReduceScatter `reduce_scatter.h:194/405`). This matches @sjeaugey's diagnosis that the single-node path "is missing the user rank table." The single-node ReduceScatter (`reduce_scatter.h:248`) is the symmetric mirror with the same gap.

One subtlety that makes the fix non-trivial: `collNetDenseToUserRank` is built only in collnet/SHARP setup and is **null on the device** for pure single-node NVLS, so this path cannot simply index it — a dense→user table must first be made available (natural source: `comm->nvlsHeads[h]`).

## Changes & Impact

- Add a dedicated `nvlsDenseToUserRank` table (host `comm.h` + device `ncclKernelComm`), filled `= nvlsHeads[h]`, copied to device in `init.cc` like the collnet one (null-guarded); kept separate so collnet paths are untouched.
- Add opt-in `gatherRemap`/`scatterRemap` wrappers in `prims_simple.h` (`pOffset = (remap ? remap[i] : i) * peerOffset`); existing `gather()`/`scatter()` unchanged, so `AllReduce`/reg-sync are unaffected.
- Point the two single-node sites at the remapped wrappers.

Identity-preserving (unpermuted: `nvlsHeads[i]==i` → byte-identical). **Open item:** the host table must be populated *before* `if (comm->nNodes == 1) return ncclSuccess;` in `connectNvls` (`connect.cc:270`); the `nHeads == nRanks` assumption should be guarded for partial-NVLS domains.

## Performance Impact

None — one extra table lookup per gathered chunk on the NVLS path.

### Testing

- Statically traced end-to-end against current `master` and cross-checked against the three correct sibling paths; an adversarial review confirmed the remap semantics + identity-preservation and surfaced the `connectNvls` placement constraint above.
- **Not runtime-validated** — the repro needs an NVSwitch multi-GPU box; my dev machine is a single GPU. On NVLS hardware, validation should assert output `slot i == float(i)` across several non-identity `CUDA_VISIBLE_DEVICES` permutations, plus an unpermuted run and a ring (non-NVLS) regression (`all_gather_perf`, `#wrong=0`).

Happy to put up a draft PR if this direction looks right — and is a separate `nvlsDenseToUserRank` table the approach you'd prefer over reusing the collnet table?


### EylonKrause · 2026-08-27

I came back to this and put up a fix: #2377.

Turns out the plumbing is mostly there already on current master — `denseToUserRank` now gets built and copied to the device for pure single-node NVLS too (`ncclTransportInitRankMap` at `init.cc:1573`, gated only on `nvlsSupport`, with the device copy in `devCommSetup`). What was still missing was the device-side consumption: the `oneNode`/`!regUsed` gather in `all_gather.h` writes head `i`'s slice to output slot `i` (the dense head index) instead of `denseToUserRank[i]`, so the output is permuted exactly when the ranks aren't in dense-head order. `ReduceScatter` has the symmetric mirror on the scatter side. Every other path (multi-node NVLS, CollNetDirect, PAT) already remaps through `denseToUserRank`, so I made the single-node paths do the same.

I kept it device-only and opt-in: `ScatterGatherOp` gets a template `Remap` flag (defaulting off, so every existing caller — AllReduce, multi-node, CollNet, reg-sync — is byte-identical), plus `scatterRemap`/`gatherRemap` wrappers, and the two `oneNode` sites pass `comm->denseToUserRank`. AllReduce is left alone since its scatter+gather round-trip is order-invariant.

Fair warning: I don't have an NVSwitch box, so I couldn't run it on real hardware — I verified the remap direction against the multi-node/CollNet/PAT paths and checked the C++ mechanics compile and permute correctly in a standalone harness, but it needs a real run before merging. `all_gather_perf`/`reduce_scatter_perf` with `NCCL_ALGO=NVLS` and a few non-identity `CUDA_VISIBLE_DEVICES` permutations (plus a non-NVLS regression) should confirm it. Would appreciate a look when you get a chance, @sjeaugey.

