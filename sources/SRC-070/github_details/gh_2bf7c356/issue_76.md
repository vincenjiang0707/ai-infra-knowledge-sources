# [Issue #76] Could normal kernel and ll kernel be executed in same process?

source: https://github.com/deepseek-ai/DeepEP/issues/76
state: closed | updated: 2026-09-18T10:16:22Z
labels: 

## 正文

Hi, we just tried to integrate DeepEp in our engine. As we supposed, without PD disaggregated mode, we do prefilling with normal mode kernels while do decoding with ll kernels. 
But we got crash when we try to initiate two Buffers with different modes, like this:

`       self._buffer = get_buffer_normal(group, hidden_size * WEIGHT_DTYPE_SIZE)`
`       self._low_latency_buffer = get_buffer_low_latency(group, MAX_DISPATCH_TOKENS_PER_RANK, hidden_size, num_local_experts)`

Some error messages would be given out like below:

![Image](https://github.com/user-attachments/assets/9fcbdc70-2585-4484-a72c-548cba0b5789)

or if we change the statement order, we'll get assertion on this line:

![Image](https://github.com/user-attachments/assets/4dee66b2-e6c5-4f85-9482-c9ab8645bfaf)

So is it by-design that the two mode could not work together in same process? Or is there any advise for our use case? Thx!

## 评论 (6)

### LyricZhao · 2025-03-17

How many nodes and GPUs are you using? And the rank layout? Or can you ensure that every `[8k, 8k + 8)` GPUs are in the same NVLink domain? This error means the NVLink IPC handle is not accessible (e.g. giving a NVLink handle to a rank not in the same node).

### lowintelligence · 2025-03-24

> How many nodes and GPUs are you using? And the rank layout? Or can you ensure that every `[8k, 8k + 8)` GPUs are in the same NVLink domain? This error means the NVLink IPC handle is not accessible (e.g. giving a NVLink handle to a rank not in the same node).
Well, I'm using 2nodes * 8 H20 cards, and exactly rank 0-7 in node0 and rank 8-15 in node1...

### LyricZhao · 2025-03-25

> But we got crash when we try to initiate two Buffers with different modes, like this

Oh, sorry. NVSHMEM can not be initialized twice. If you have an engine to do both P and D, you can create **one** buffer with `max(normal_nvl_bytes, low_latency_nvl_bytes)` and `max(normal_rdma_bytes, low_latency_rdma_bytes)` with `low_latency_mode=True` and `num_qps_per_rank` set for the low-latency mode.

Then if you want to switch from P to D, call `clean_low_latency_buffer`. And switching D to P requires nothing.

### lowintelligence · 2025-03-26

> > But we got crash when we try to initiate two Buffers with different modes, like this
> 
> Oh, sorry. NVSHMEM can not be initialized twice. If you have an engine to do both P and D, you can create **one** buffer with `max(normal_nvl_bytes, low_latency_nvl_bytes)` and `max(normal_rdma_bytes, low_latency_rdma_bytes)` with `low_latency_mode=True` and `num_qps_per_rank` set for the low-latency mode.
> 
> Then if you want to switch from P to D, call `clean_low_latency_buffer`. And switching D to P requires nothing.

Thanks a lot for giving the suggestion. I also have another question: I noticed that when doing Buffer __init__ in python when low_latency_mode is true, the environ 'NVSHMEM_IB_ENABLE_IBGDA' would be set as '1'. But if I ran normal kernel with 'NVSHMEM_IB_ENABLE_IBGDA=1', the program would fail in my platform (H20*8 2nodes). So is it possible run normal kernel with 'NVSHMEM_IB_ENABLE_IBGDA' enabled or run low latency kernel with 'NVSHMEM_IB_ENABLE_IBGDA' disabled? 

### LyricZhao · 2025-03-26

Yes, it is possible, and you don't have to do anything, it is fully automatic.

`NVSHMEM_IB_ENABLE_IBGDA` only initialize the IBGDA configs at setup.

But it has no effect for normal kernels, see https://github.com/deepseek-ai/DeepEP/blob/main/csrc/kernels/runtime.cu#L67. The IBGDA flag will always be disabled for official NVSHMEM APIs. When normal kernels called NVSHMEM APIs, they will first judge the flag and switch IBRC/IBGDA code path, so even it is initialized, the NVSHMEM calls will fallback to IBRC.

But for the low-latency kernels, they will call our modified IBGDA APIs (not flag judge, no switch), always using IBGDA, as IBGDA is initialized by setting `NVSHMEM_IB_ENABLE_IBGDA=1`.

### lowintelligence · 2025-03-26

> Yes, it is possible, and you don't have to do anything, it is fully automatic.
> 
> `NVSHMEM_IB_ENABLE_IBGDA` only initialize the IBGDA configs at setup.
> 
> But it has no effect for normal kernels, see https://github.com/deepseek-ai/DeepEP/blob/main/csrc/kernels/runtime.cu#L67. The IBGDA flag will always be disabled for official NVSHMEM APIs. When normal kernels called NVSHMEM APIs, they will first judge the flag and switch IBRC/IBGDA code path, so even it is initialized, the NVSHMEM calls will fallback to IBRC.
> 
> But for the low-latency kernels, they will call our modified IBGDA APIs (not flag judge, no switch), always using IBGDA, as IBGDA is initialized by setting `NVSHMEM_IB_ENABLE_IBGDA=1`.

Thanks a lot for detail interpretation, I'll try more experiments later. <hugging legs>
