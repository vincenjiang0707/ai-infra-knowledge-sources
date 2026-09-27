# [Issue #596] `detect_accessible_ranks` returns incorrect NVLink domain size on GB200 NVL72 (MNNVL)

source: https://github.com/deepseek-ai/DeepEP/issues/596
state: closed | updated: 2026-04-16T04:59:22Z
labels: 

## 正文


## Environment

- **GPU:** NVIDIA GB200 NVL72 (4 GPUs per node, 18 NVLinks per GPU, Multi-Node NVLink / MNNVL)
- **DeepEP branch:** `hybrid-ep`
- **CUDA:** 13.0
- **PyTorch:** 2.7 (cu130 nightly)
- **NVSHMEM:** with `NVSHMEM_DISABLE_MNNVL=0` (MNNVL enabled)

## Problem

On GB200 NVL72 systems with MNNVL enabled, `ExtendedMemoryAllocator.detect_accessible_ranks()` over-counts the NVLink domain size because GPU memory on remote nodes is accessible via MNNVL NVLink. This causes `HybridEPBuffer` to set `num_of_ranks_per_node` to the full EP group size (e.g., 8 or 32) instead of the physical node size (4), and `num_of_nodes` to 1.

**Consequence:** The `device_sync_kernel` barrier expects all EP ranks in a single NVLink domain. Since the dispatch/combine kernels are launched with a grid sized for the physical node, the barrier deadlocks waiting for atomic increments that never arrive.

## Root Cause

Two compounding factors:

### 1. NVML reports `FFFFFFFF:FF:FF.0` for all NVLink peers

On GB200 NVL72, all NVLink connections go through an NVSwitch fabric (MNNVL). NVML's `nvmlDeviceGetNvLinkRemotePciInfo` cannot resolve the PCI bus ID of peers behind the switch and returns the sentinel value `FFFFFFFF:FF:FF.0` for every link — both local-node and remote-node peers are indistinguishable:

```
GPU 0 (NVIDIA GB200) PCI=00000008:06:00.0
  NVLink  0: remote=FFFFFFFF:FF:FF.0  state=ACTIVE
  NVLink  1: remote=FFFFFFFF:FF:FF.0  state=ACTIVE
  ...
  NVLink 17: remote=FFFFFFFF:FF:FF.0  state=ACTIVE
```

`topo_detection.cuh` handles this correctly by classifying unknown peers as NVSwitch (`0x068000`). However, this means the XML-based topology detection provides no information about which GPUs are on the same physical node vs. remote nodes.

### 2. IPC accessibility test succeeds across nodes

`detect_accessible_ranks()` in `allocator.cu` uses `cuMemSetAccess` / IPC memory handles to test which ranks can access the current GPU's memory. With MNNVL enabled (`NVSHMEM_DISABLE_MNNVL=0`), GPU memory IS accessible across nodes via NVLink. The test returns `num_accessible_ranks == group_size` instead of `gpus_per_physical_node`.

The resulting misconfiguration:
```
Expected (4-node, 4 GPU/node, TP=2, 8 EP ranks):
  num_of_ranks_per_node = 4   (physical node boundary)
  num_of_nodes = 2

Actual:
  num_of_ranks_per_node = 8   (all EP ranks appear NVLink-accessible)
  num_of_nodes = 1
```

## Reproduction

**Reproducer script** (`probe_detect_ranks.py`):

```python
#!/usr/bin/env python3
"""Launch with: torchrun --nnodes=2 --nproc-per-node=4 probe_detect_ranks.py"""
import os, socket, torch, torch.distributed as dist

def main():
    dist.init_process_group(backend="nccl")
    rank, world_size = dist.get_rank(), dist.get_world_size()
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    torch.cuda.set_device(local_rank)

    try:
        import hybrid_ep_cpp
    except ImportError:
        from deep_ep import hybrid_ep_cpp

    detected = hybrid_ep_cpp.ExtendedMemoryAllocator().detect_accessible_ranks(dist.group.WORLD)
    print(f"[rank {rank}/{world_size} on {socket.gethostname()} GPU {local_rank}] "
          f"detect_accessible_ranks={detected}  →  "
          f"num_of_ranks_per_node={detected}, num_of_nodes={world_size // detected}")

    dist.barrier()
    if rank == 0:
        physical = torch.cuda.device_count()
        print(f"\nPhysical GPUs per node: {physical}")
        if detected != physical:
            print(f"BUG: detected={detected} != physical={physical}. "
                  f"Workaround: export NUM_OF_HYBRID_EP_RANKS_PER_NVLINK_DOMAIN={physical}")
    dist.destroy_process_group()

if __name__ == "__main__":
    main()
```

**Actual output** on GB200 NVL72 (2 nodes, 4 GPUs/node, 8 ranks total, `NVSHMEM_DISABLE_MNNVL=0`):

```
[rank 0/8 on lyris0015 GPU 0] detect_accessible_ranks=8  →  num_of_ranks_per_node=8, num_of_nodes=1
[rank 1/8 on lyris0015 GPU 1] detect_accessible_ranks=8  →  num_of_ranks_per_node=8, num_of_nodes=1
[rank 2/8 on lyris0015 GPU 2] detect_accessible_ranks=8  →  num_of_ranks_per_node=8, num_of_nodes=1
[rank 3/8 on lyris0015 GPU 3] detect_accessible_ranks=8  →  num_of_ranks_per_node=8, num_of_nodes=1
[rank 4/8 on lyris0018 GPU 0] detect_accessible_ranks=8  →  num_of_ranks_per_node=8, num_of_nodes=1
[rank 5/8 on lyris0018 GPU 1] detect_accessible_ranks=8  →  num_of_ranks_per_node=8, num_of_nodes=1
[rank 6/8 on lyris0018 GPU 2] detect_accessible_ranks=8  →  num_of_ranks_per_node=8, num_of_nodes=1
[rank 7/8 on lyris0018 GPU 3] detect_accessible_ranks=8  →  num_of_ranks_per_node=8, num_of_nodes=1

Physical GPUs per node: 4
BUG: detected=8 != physical=4. HybridEP will deadlock on multi-node dispatch.
Workaround: export NUM_OF_HYBRID_EP_RANKS_PER_NVLINK_DOMAIN=4
```

**Expected:** `detect_accessible_ranks=4` (physical GPUs per node).
**Actual:** `detect_accessible_ranks=8` (full group size — cross-node GPUs are IPC-accessible via MNNVL).

The issue does **not** manifest when `num_of_ranks_per_node` happens to equal the group size (e.g., TP=4 DP=4 → 4 EP ranks on 4 GPUs/node). It only manifests when TP < GPUS_PER_NODE, creating multiple EP ranks per node.

## Workaround

The existing env var override works correctly:

```bash
export NUM_OF_HYBRID_EP_RANKS_PER_NVLINK_DOMAIN=4  # physical GPUs per node
```

This bypasses `detect_accessible_ranks()` entirely (`hybrid_ep_buffer.py:64-66`).

## Suggested Fix

`detect_accessible_ranks()` tests memory accessibility, but on MNNVL systems this is not equivalent to being on the same physical node. The detection should additionally check whether peers share the same host (e.g., via `boot_id` or hostname comparison, as `topo_detection.cuh` already does with `getHostHash()`). Ranks that are memory-accessible but on different hosts should not be counted as part of the NVLink domain.

Alternatively, `detect_accessible_ranks` could incorporate the topology information from the XML/topo detection pass (which correctly identifies per-host system IDs via `host_hash`) to bound the domain to same-host ranks only.


## 评论 (0)
