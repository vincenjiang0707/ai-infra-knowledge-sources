# [Issue #357] Does the GinAlltoAllKernel have send/receive conflicts in in-place mode?

source: https://github.com/NVIDIA/nccl-tests/issues/357
state: open | updated: 2025-10-30T14:23:56Z
labels: 

## 正文

Consider an in-place all-to-all operation where send and receive buffers are the same memory region, and there is no intermediate buffering. Is there a risk that a process receives data into a buffer location before it has finished sending the original data from that same location, thereby corrupting the outgoing message?

<img width="1696" height="976" alt="Image" src="https://github.com/user-attachments/assets/25f4f3e5-b6df-4d1d-9721-2780458e7e62" />

## 评论 (1)

### shanedsnyder · 2025-10-30

> Is there a risk that a process receives data into a buffer location before it has finished sending the original data from that same location, thereby corrupting the outgoing message?

Yes. I believe this behavior is not necessarily unique to the GIN kernel, though -- there's not really a guarantee in any case that a rank's send buffer hasn't already been written into by remote ranks when doing in-place alltoall. 

In fact, we disable data validation checking for in-place alltoall for this reason in all cases (GIN or not): https://github.com/NVIDIA/nccl-tests/blob/da0b547b1b9c6e3b1d4c15578087874522ae3761/src/alltoall.cu#L42
