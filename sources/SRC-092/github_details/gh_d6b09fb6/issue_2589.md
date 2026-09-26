# [Issue #2589] [Bug]:  KV Cache Memory Registration and Transfer Fails with RDMA Transport in SGLang PD Split Mode When MACA Compile Option Is Enabled

source: https://github.com/kvcache-ai/Mooncake/issues/2589
state: open | updated: 2026-09-23T03:15:38Z
labels: bug, stale

## 正文

### Bug Report

## Background

During development and deployment on Muxi GPUs, the `-DMACA` compile macro must be enabled to implement GPU-NIC affinity binding.

In SGLang 0.5.7 with PD split architecture enabled, cross-host KV Cache transfer fails immediately. Since the MACA transport backend does not yet support cross-node transmission, we switched to the RDMA transport for data transfer, and the memory registration issue can be reliably reproduced.

## Root Cause

1. MACA software stack behavior: For unpinned/pagable host memory, the pointer attribute query API returns success, but reports the memory type as `unregistered`.
2. The existing Mooncake logic does not handle this `unregistered` memory type, and incorrectly falls through to the GPU device memory registration branch.
3. The memory region registered by SGLang to Mooncake contains a block of unpinned host memory. Attempting to perform device memory registration on this region results in an immediate failure.

## Proposed Fix

We have drafted a fix with the following logic:

1. Add a new conditional branch after fetching the memory type via `cuPointerGetAttribute` to handle the `unregistered` memory type returned by the MACA stack.
2. For unpinned host memory marked as `unregistered`, register it as regular host memory and skip the GPU device memory registration flow.
3. Only apply device memory registration to actual GPU device memory, eliminating invalid registration operations and resolving the crash during KV Cache transfer.

## Steps to reproduce: 

1. Steps to reproduce: 1. Build Mooncake 0.3.11 with the `-DUSE_MACA` compile flag enabled, with RDMA transport support compiled in. 
2. Configure the transport backend to use RDMA transport at runtime (MACA transport does not support cross-node transmission yet). 
3. Call the memory registration API of the RDMA transport with regular CPU pageable (unpinned) host memory as the input buffer and call the transfer API .
4. The memory registration flow incorrectly falls into the GPU device memory registration branch and fails to get rkey/lkey, output the error logs.
5. In the end, transfer failed with segmentation fault and the process core dump.

```bash
E0624 11:00:23.523427 74552 rdma_context.cpp:393] Address 0x562d8af8d700 lkey not found for mlx5_1
E0624 11:00:23.523429 74552 rdma_context.cpp:384] Address 0x562d8af8d700 rkey not found for mlx5_1
E0624 11:00:23.523433 74552 rdma_context.cpp:393] Address 0x562d8af8d700 lkey not found for mlx5_0
E0624 11:00:23.523438 74552 rdma_context.cpp:384] Address 0x562d8af8d700 rkey not found for mlx5_0
.......
E0624 11:00:23.673532 74622 worker_pool.cpp:307] Worker: Process failed for slice (opcode: 1, source_addr: 0x562d8af8eb00, length: 1024, dest_addr: 0x55e665a32540, local_nic: mlx5_1, peer_nic: 10.107.204.141:16388@mlx5_0, dest_rkey: 0, retry_cnt: 1): local protection error
E0624 11:00:23.675357 74622 worker_pool.cpp:307] Worker: Process failed for slice (opcode: 1, source_addr: 0x562d8af8f300, length: 1024, dest_addr: 0x55e665a32d40, local_nic: mlx5_1, peer_nic: 10.107.204.141:16388@mlx5_0, dest_rkey: 0, retry_cnt: 0): local protection error
I0624 11:00:23.679181 74622 topology.cpp:639] ========== Resolved Topology Matrix ==========
I0624 11:00:23.679185 74622 topology.cpp:640] HCA List:
I0624 11:00:23.679188 74622 topology.cpp:643]   HCA[0]: mlx5_1
I0624 11:00:23.679191 74622 topology.cpp:643]   HCA[1]: mlx5_0
I0624 11:00:23.679194 74622 topology.cpp:646] Device to HCA mapping:
I0624 11:00:23.679198 74622 topology.cpp:670]   cpu:0 -> Preferred: [mlx5_0(1) mlx5_1(0) ] Available: [ ]
I0624 11:00:23.679201 74622 topology.cpp:670]   cpu:1 -> Preferred: [ ] Available: [mlx5_0(1) mlx5_1(0) ]
I0624 11:00:23.679204 74622 topology.cpp:670]   maca:7 -> Preferred: [mlx5_1(0) ] Available: [mlx5_0(1) ]
I0624 11:00:23.679208 74622 topology.cpp:670]   maca:1 -> Preferred: [mlx5_0(1) ] Available: [mlx5_1(0) ]
I0624 11:00:23.679211 74622 topology.cpp:670]   maca:2 -> Preferred: [mlx5_0(1) ] Available: [mlx5_1(0) ]
I0624 11:00:23.679214 74622 topology.cpp:670]   maca:3 -> Preferred: [mlx5_0(1) ] Available: [mlx5_1(0) ]
I0624 11:00:23.679216 74622 topology.cpp:670]   maca:4 -> Preferred: [mlx5_1(0) ] Available: [mlx5_0(1) ]
I0624 11:00:23.679220 74622 topology.cpp:670]   maca:5 -> Preferred: [mlx5_1(0) ] Available: [mlx5_0(1) ]
I0624 11:00:23.679224 74622 topology.cpp:670]   maca:6 -> Preferred: [mlx5_1(0) ] Available: [mlx5_0(1) ]
I0624 11:00:23.679229 74622 topology.cpp:670]   maca:0 -> Preferred: [mlx5_0(1) ] Available: [mlx5_1(0) ]
I0624 11:00:23.679231 74622 topology.cpp:670]   * -> Preferred: [mlx5_1(0) mlx5_0(1) ] Available: [ ]
I0624 11:00:23.679939 74622 rdma_endpoint.cpp:265] Connection has been established
E0624 11:00:23.687029 74625 worker_pool.cpp:307] Worker: Process failed for slice (opcode: 1, source_addr: 0x562d8af8f700, length: 1024, dest_addr: 0x55e665a33140, local_nic: mlx5_0, peer_nic: 10.107.204.141:16388@mlx5_1, dest_rkey: 0, retry_cnt: 0): local protection error
E0624 11:00:23.687186 74625 worker_pool.cpp:307] Worker: Process failed for slice (opcode: 1, source_addr: 0x562d8af8d700, length: 1024, dest_addr: 0x55e665a31140, local_nic: mlx5_0, peer_nic: 10.107.204.141:16388@mlx5_1, dest_rkey: 0, retry_cnt: 0): local protection error
W0624 11:00:23.687192 74625 worker_pool.cpp:320] Too many errors found in local RNIC 10.107.204.141:15882@mlx5_0, mark it inactive
I0624 11:00:23.687202 74552 rdma_transport.cpp:573] [MC_TRANSFER_INFO] GPU=cpu:1, HCA=mlx5_1
E0624 11:00:23.687209 74552 rdma_transport.cpp:555] Device 1 is not active
client.sh: line 40: 74552 Segmentation fault      (core dumped) python client.py
```

### Code Changes To Solve This Bug

```
// Mooncake/mooncake-transfer-engine/src/transport/rdma_transport/rdma_context.cpp
   CUresult result = cuPointerGetAttribute(
        &memType, CU_POINTER_ATTRIBUTE_MEMORY_TYPE, (CUdeviceptr)addr);

    // Register memory depending on whether memory is on host or GPU.
    if (result != CUDA_SUCCESS || memType == CU_MEMORYTYPE_HOST) {
        mrMeta.addr = addr;
        mrMeta.mr = ibv_reg_mr(pd_, addr, length, access);
+#if defined(USE_MACA)
+    } else if (memType == CU_MEMORYTYPE_UNREGISTERED) {
+        mrMeta.addr = addr;
+        mrMeta.mr = ibv_reg_mr(pd_, addr, length, access);
+#endif
#if defined(USE_CUDA)
    } else if (memType == CU_MEMORYTYPE_DEVICE &&
               Environ::Get().GetWithNvidiaPeermem()) {
        // WITH_NVIDIA_PEERMEM env var is set: use ibv_reg_mr() directly for
        // GPU memory (requires the nvidia-peermem kernel module to be loaded).
        mrMeta.addr = addr;
        mrMeta.mr = ibv_reg_mr(pd_, addr, length, access);
#endif
```

```
// Mooncake/mooncake-transfer-engine/include/gpu_vendor/maca.h
+#define CU_MEMORYTYPE_UNREGISTERED mcMemoryTypeUnregistered
#define CU_MEMORYTYPE_HOST mcMemoryTypeHost
#define CU_MEMORYTYPE_DEVICE mcMemoryTypeDevice
```

## Expected Behavior

After the fix, Mooncake will correctly recognize `unregistered` host memory from the MACA stack, automatically skip the device memory registration path, and no longer throw memory registration failure errors.

## Environment

- Hardware: Muxi GPU
- Mooncake version: 0.3.11and version what suports maca with rdma transport
- Compile flag: `-DMACA` enabled
- Transport backend: RDMA transport (MACA transport does not support cross-host transmission currently)
- Upper framework: SGLang 0.5.7, PD split mode
- Module: Mooncake distributed KV Cache transport engine

## Additional Notes

It is not confirmed whether GPUs from other vendors (including NVIDIA) have the same behavior. Maintainers please help verify this.

### Before submitting...

- [ ] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### github-actions[bot] · 2026-06-24

Thanks for opening this issue, @XiangGuiXiao!

| Field | Value |
|-------|-------|
| **Issue** | #2589 |
| **GitHub user ID** | `184745144` |
| **Reporter** | @XiangGuiXiao |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### github-actions[bot] · 2026-09-23

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.
