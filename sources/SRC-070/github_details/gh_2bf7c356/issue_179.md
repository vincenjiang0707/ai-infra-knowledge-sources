# [Issue #179] Does DeepEP use SMs for its normal and low-latency kernels?

source: https://github.com/deepseek-ai/DeepEP/issues/179
state: closed | updated: 2026-09-18T10:16:27Z
labels: 

## 正文

I saw in a DeepSeek-V3 paper (https://arxiv.org/pdf/2505.09343) that "during training, up to 20 of the SMs on the H800 GPU are allocated for communication-related operations, leaving fewer resources available for actual computation." and I also saw that in the issue (https://github.com/deepseek-ai/DeepEP/issues/61#issuecomment-2709205782) that with `return_recv_hook`, communication kernels does not use any SM, it just issue RDMA requests and just return.
Does that mean DeepSeek training uses normal kernel and the 20 SMs are used because of NVLink forwarding? 
Any help is much appreciated. Thank you!

## 评论 (4)

### LyricZhao · 2025-06-05

> Does that mean DeepSeek training uses normal kernel and the 20 SMs are used because of NVLink forwarding?

Yes. Normal kernels are designed for training and prefill with SM (due to NVLink, managed communication queue for less VRAM). While low-latency kernels allocate the worst-case VRAM and only have RDMA, which is designed for decoding.

### njw1123 · 2025-07-27

> > Does that mean DeepSeek training uses normal kernel and the 20 SMs are used because of NVLink forwarding?
> 
> Yes. Normal kernels are designed for training and prefill with SM (due to NVLink, managed communication queue for less VRAM). While low-latency kernels allocate the worst-case VRAM and only have RDMA, which is designed for decoding.

Does this mean that whether SMs are used is independent of whether IBRC or IBGDA is used — that is, pure IBRC or IBGDA communication does not occupy SMs? Another thing that confuses me is that IBGDA offloads communication control to the GPU — doesn’t that consume some SM resources?
Are the GPU thread resources it uses so minimal that they can be considered negligible? I would greatly appreciate your help!

### LyricZhao · 2025-07-30

> Does this mean that whether SMs are used is independent of whether IBRC or IBGDA is used — that is, pure IBRC or IBGDA communication does not occupy SMs? Another thing that confuses me is that IBGDA offloads communication control to the GPU — doesn’t that consume some SM resources?

No matter you are using IBRC or IBGDA, the SM should issue instructions into CPU (IBRC) or into IB (IBGDA). But for low-latency mode, you can issue lots of instructions and just exit the kernel, the issuing process occupies the SM, but it just costs ~us. The real data sending does not occupy any SM. For normal mode, the communication should be maintained throughout the whole (issuing + sending) process, as we have a communication queue and NVLink forward is involved.

> Are the GPU thread resources it uses so minimal that they can be considered negligible? I would greatly appreciate your help!

For normal kernels, the block (CTA) occupies the whole SM, so it is not negligible. For low-latency kernels, issuing costs all SMs (also not negligible), but the issuing time is negligible (~us to issue, then you can quit the kernel).

### njw1123 · 2025-07-30

> > Does this mean that whether SMs are used is independent of whether IBRC or IBGDA is used — that is, pure IBRC or IBGDA communication does not occupy SMs? Another thing that confuses me is that IBGDA offloads communication control to the GPU — doesn’t that consume some SM resources?
> 
> No matter you are using IBRC or IBGDA, the SM should issue instructions into CPU (IBRC) or into IB (IBGDA). But for low-latency mode, you can issue lots of instructions and just exit the kernel, the issuing process occupies the SM, but it just costs ~us. The real data sending does not occupy any SM. For normal mode, the communication should be maintained throughout the whole (issuing + sending) process, as we have a communication queue and NVLink forward is involved.
> 
> > Are the GPU thread resources it uses so minimal that they can be considered negligible? I would greatly appreciate your help!
> 
> For normal kernels, the block (CTA) occupies the whole SM, so it is not negligible. For low-latency kernels, issuing costs all SMs (also not negligible), but the issuing time is negligible (~us to issue, then you can quit the kernel).

thanks for your reply.
