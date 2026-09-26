source: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/all_reduce_utils/
lastmod: 2026-09-24

#

`vllm.distributed.device_communicators.all_reduce_utils`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all_reduce_utils)

Functions:

-
–[gpu_p2p_access_check](https://docs.vllm.ai#vllm.distributed.device_communicators.all_reduce_utils.gpu_p2p_access_check)Check if GPU src can access GPU tgt.


##

`can_actually_p2p(batch_src, batch_tgt)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all_reduce_utils.can_actually_p2p)

Usually, checking if P2P access is enabled can be done by `torch.cuda.can_device_access_peer(src, tgt)`

. However, sometimes the driver might be broken, and `torch.cuda.can_device_access_peer(src, tgt)`

returns `True`

even if P2P access is not actually possible. See https://github.com/vllm-project/vllm/issues/2728 and https://forums.developer.nvidia.com/t/direct-gpu-gpu-communication-does-not-seem-to-work-properly/283264/10 Therefore, we have to perform a real P2P access to check if it is actually possible.

Note on p2p and cuda IPC: Usually, one process uses one GPU: GPU src --> cuda context src --> tensor src --> process src

We need to combine p2p and cuda IPC, so that: GPU src --> cuda context src --> tensor src --> process src |shared| GPU tgt --> cuda context tgt --> tensor tgt --> process tgt That is to say, process src creates a tensor in GPU src, passes IPC handle to process tgt, and process tgt accesses the tensor in GPU tgt. Any operation on the tensor in process tgt will be reflected in the tensor in process src, because they are the same memory segment. It is important to note that process tgt accesses the tensor in GPU tgt, not GPU src. That's why we need p2p access.

The most time-consuming part is the process creation. To avoid creating processes for every pair of GPUs, we use batched testing. We create two processes for testing all pairs of GPUs in batch. The trick is to reset the device after each test (which is not available in PyTorch).

## Source code in `vllm/distributed/device_communicators/all_reduce_utils.py`


|
|

##

`gpu_p2p_access_check(src, tgt)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all_reduce_utils.gpu_p2p_access_check)

Check if GPU src can access GPU tgt.

## Source code in `vllm/distributed/device_communicators/all_reduce_utils.py`


|
|

##

`should_nccl_symm_mem_ag_rs()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all_reduce_utils.should_nccl_symm_mem_ag_rs)

Check whether NCCL symmetric memory should be used for AllGather / ReduceScatter collectives.

## Source code in `vllm/distributed/device_communicators/all_reduce_utils.py`


##

`should_nccl_symm_mem_allreduce(world_size, input_tensor)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all_reduce_utils.should_nccl_symm_mem_allreduce)

Determine if NCCL symmetric memory allreduce should be used.

Based on H100 and GB200 benchmarks, NCCL symm_mem is preferred for: - Small tensors (≤16K): Lower latency than custom_AR - Large tensors (≥128K for 8 GPUs, ≥512K for 4 GPUs): Better bandwidth

Custom_AR is preferred for mid-range sizes where its P2P approach has lower overhead than the symm_mem copy-in/copy-out pattern.