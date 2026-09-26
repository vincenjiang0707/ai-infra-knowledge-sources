# [Issue #2051] [Question]: ce_alltoall(CUDA 13.1 + NVLS): H2D memcpy launch is blocked by previous H2D completion

source: https://github.com/NVIDIA/nccl/issues/2051
state: closed | updated: 2026-07-24T07:26:14Z
labels: question

## 正文

### Question

We are observing a behavior difference between CUDA 13.1 and CUDA 12.8 when running NCCL with NVLS enabled (default).

On CUDA 13.1, H2D memcpy launch appears to be serialized by the previous round's H2D copy completion:
- the CPU thread tries to launch the next H2D memcpy
- but the launch is blocked
- the next H2D memcpy does not get launched immediately
- it only gets launched after the previous round's H2D memcpy has finished executing

On CUDA 13.1, the issue is not just a longer synchronization time: the launch of the H2D memcpy used for synchronization is itself blocked while the previous round's H2D copy is still executing. The next synchronization H2D is only launched after the previous H2D completes, which causes a long CPU-side stall.

<img width="2578" height="910" alt="Image" src="https://github.com/user-attachments/assets/30c8fcdd-0dcb-4b56-a1c3-d159be2a047d" />

On CUDA 12.8, under the same workload and with NVLS enabled, we do not observe this launch-side blocking. 

<img width="2594" height="926" alt="Image" src="https://github.com/user-attachments/assets/b0770751-07f9-4fff-999d-27ebbae02c79" />

## 评论 (4)

### pkuleo · 2026-03-13

nccl2.29.2

### zhenhaohe · 2026-03-18

Hi,

What is this ce_alltoall implementation? Is it the NCCL alltoall with Zero_CTA enabled or it is a customized implementation? I do not understand where does the H2D (Host-to-Device) copy come from.

### pkuleo · 2026-03-20

It is the NCCL alltoall with Zero_CTA enabled (ncclCeAlltoAll). 
H2D: https://github.com/NVIDIA/nccl/blob/361915904b456d397e6e1578f8f65ea1a45bdd28/src/ce_coll.cc#L141

### xiaofanl-nvidia · 2026-04-12

@pkuleo we recently fixed a related issue on v2.30 branch. Could you give it a try to confirm it solves this issue? Thanks! 
