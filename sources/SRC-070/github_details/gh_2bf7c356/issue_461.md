# [Issue #461] Some question about the DC QP in nvshmem.

source: https://github.com/deepseek-ai/DeepEP/issues/461
state: closed | updated: 2026-09-18T10:09:11Z
labels: 

## 正文

Hi dear developer,

I've just started learning about DeeEP, and noticed that in the code of origin nvshmem, there are lots of logic about DC, but there is not any such login in nvshmem used by deepep.
There are two questions:
(1) In the native nvshmem, what is the role of DC qp?
(2) Is the DC logic necessary? If so, what should be used instead of simplifying the DC logic?

Thank you!

## 评论 (4)

### seth-howell · 2025-10-22

1. In NVSHMEM, DC is used for large-scale jobs where ranks may be switching between destinations infrequently. It typically involves creating multiple DC QPs per SM or CTA on the GPU. At very large-scale, this can result in memory savings since you don't need to scale QPs by the number of processes. There is an extra half-handshake of latency each time the target of a DC QP changes, so it is not ideal from a latency perspective.
2. DeepEP always uses RC, so the DC logic is not necessary. RC is the default QP strategy in NVSHMEM.
One thing to keep in mind, specifically requesting DC QPs in the [environment](https://docs.nvidia.com/nvshmem/api/gen/env.html#c.NVSHMEM_IBGDA_NUM_DCT) before running DeepEP would result in hangs or segfaults.


### shanleo2024 · 2025-10-27

Hi @seth-howell 
From the nvshmem source code alone, it can be seen that whether DC is necessary mainly depends on whether the GPU supports CUevice-ATTRIBUTE-GPU-DIRECT-RDMA-WRITES-ORDERING.
```
CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_WRITES_ORDERING = 118
    GPUDirect RDMA writes to the device do not need to be flushed for consumers within the scope indicated by the returned attribute
```

From Deepep's perspective, the simplified version of ibgda_device.cuh file does not use DC's QP. Does it depend on NV's GPU supporting this attribute?

Thank you!

### alpha-baby · 2025-10-30

> Hi [@seth-howell](https://github.com/seth-howell) From the nvshmem source code alone, it can be seen that whether DC is necessary mainly depends on whether the GPU supports CUevice-ATTRIBUTE-GPU-DIRECT-RDMA-WRITES-ORDERING.
> 
> ```
> CU_DEVICE_ATTRIBUTE_GPU_DIRECT_RDMA_WRITES_ORDERING = 118
>     GPUDirect RDMA writes to the device do not need to be flushed for consumers within the scope indicated by the returned attribute
> ```
> 
> From Deepep's perspective, the simplified version of ibgda_device.cuh file does not use DC's QP. Does it depend on NV's GPU supporting this attribute?
> 
> Thank you!

<img width="1830" height="1430" alt="Image" src="https://github.com/user-attachments/assets/47d0a881-3ad6-4295-819f-b5ca978208b1" />

I checked the source code of NVSHMEM, and this is the only place where QP is being created.

<img width="2190" height="2218" alt="Image" src="https://github.com/user-attachments/assets/074c52c1-be0c-4bbe-bca7-239674f20a88" />

### seth-howell · 2025-11-04

Hi, sorry for the delay. I was OOO last week.

In upstream NVSHMEM, RC and DC are both supported as the main communication path regardless of the value of this attribute.
You are correct that in the general case (Using the entire set of upstream NVSHMEM APIs), a single DC qpair can be required to enforce consistent GPU memory in certain cases. **This is not applicable to the DeepEP kernels because of the limited set of APIs it uses.**

The reasoning for requiring consistency is as follows. Prior to Hopper, GPUDirect RDMA writes were not flushed to the level of consistency by default. The traditional way to fix this was to create a loopback read operation which flushed all writes which had been performed to your GPU from all peers.

> it can be seen that whether DC is necessary mainly depends on whether the GPU supports CUevice-ATTRIBUTE-GPU-DIRECT-RDMA-WRITES-ORDERING.

Thank you for pointing out this case. There is some nuance to this requirement, and why DeepEP doesn't need it.

consistency is used in two cases:
1. nvshmem_quiet (called directly) or internally through non-blocking RMA operations and some collectives).
    This is only required after a get operation has been issued, or a fetching atomic has been performed (for some transports including IBGDA). This is to guarantee the SHMEM memory model.
2. Called directly from an internal path in the barrier operation. This is to guarantee the visibility of all writes to your own memory.

DeepEP does not use get operations or fetching atomics, and they do not use the barrier function. So it is not required by DeepEP.

IB atomics perform a PCIe read, modifies the value and writes it back. The read in the non-fetching atomic performs the same function on the remote PE as if it did a loopback read to itself, so you get ordering guarantees for the writes before it. This is consistent with the DeepEP model which relies on the put_nbi->atomic_add operation sequence to guarantee ordering.

nvshmem_quiet + nvshmem_sync is used in the notify functions rather than nvshmem_barrier.
quiet + sync is equivalent to barrier, minus the enforce_cst call. enforce_cst can be ignored based on the write->atomic reasoning above.
