# [Issue #450] HT Kernels with "--test-ll-compatibility" option

source: https://github.com/deepseek-ai/DeepEP/issues/450
state: closed | updated: 2026-09-18T09:51:41Z
labels: 

## 正文

The question is in the context of high throughput kernels with the option `--test-ll-compatibility`.

1. What is this compatibility checking? It seems that the compatibility of the HT kernel buffer is checked with LL kernel buffer. Is it in the context of prefill stage followed by a decode stage (in inference)? I understand that prefill will use HT kernels and decode will use decode kernels. 

2. With this option, how is the NVSHMEM communicator built? For example, with 2 servers (with 8 GPUs each), do we expect to see 8 communicators built (one per NVLink rank)? We're seeing that [this init method in runtime.cu](https://github.com/deepseek-ai/DeepEP/blob/main/csrc/kernels/runtime.cu#L49) gets called by all 16 GPUs. However, all GPUs on the first server have rank 0 (its' rdma_rank) and all GPUs on the second server have rank 1. This is explained in the figure below. This does not seem correct. Kindly clarify.

<img width="400" height="600" alt="Image" src="https://github.com/user-attachments/assets/79b2c9e9-ec21-4135-880c-866af152dcaa" />

## 评论 (1)

### sphish · 2025-10-11

1. `test-ll-compatibility` is for verifying whether a DeepEP Buffer can switch between normal mode and low-latency mode.
2. We have implemented two modes for building NVSHMEM.  
One is the **low-latency mode**, which creates a single NVSHMEM group containing all ranks. This mode supports both normal and low-latency kernels.  This mode is suitable for fully connected networks.
The other is the **non–low-latency mode**, as shown in your diagram, which builds 8 NVSHMEM groups, each containing only the GPUs with the same index. This mode supports only normal kernels and does not support low-latency kernels, but it can operate in multi-plane network configurations.
