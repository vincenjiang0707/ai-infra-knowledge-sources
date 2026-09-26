# [Issue #436] `notify_dispatch` and `cached_notify` in normal mode.

source: https://github.com/deepseek-ai/DeepEP/issues/436
state: closed | updated: 2026-09-18T09:50:33Z
labels: 

## 正文

Hi, I am wondering why compared to low latency mode, normal mode needs additional synchronization primitives, such as `nvshmem_sync_with_same_gpu_idx` and `nvshmemi_ibgda_quiet` for flushing, whereas low latency mode does not have that. 
Can normal mode follow low latency mode in not using these primitives? 

## 评论 (3)

### a1372422617 · 2025-09-28

Because the normal mode needs to ensure that the preceding RDMA operations are written to disk, it uses a barrier to guarantee that all GPUs have reached the synchronization point before clearing the flag to zero

### MaoZiming · 2025-09-29

Thanks for the answer. What do you mean by "written to disk"? I am wondering why low latency mode does not need these primitives

### sphish · 2025-10-10

The low-latency mode uses a double-buffer design specifically to avoid relying on these synchronization primitives. In contrast, the normal kernel does not use double buffering — this is a trade-off between GPU memory usage and latency.
