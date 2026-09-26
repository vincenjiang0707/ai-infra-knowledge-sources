# [Issue #1234] [Issue]: Unexpected Behavior LL Protocol

source: https://github.com/ROCm/rccl/issues/1234
state: closed | updated: 2025-05-12T15:41:00Z
labels: Under Investigation

## 正文

### Problem Description

Hi Everyone,

I have found a very strange behavior in rccl-rocm-6.1.2 that I cannot understand based on my limited knowledge of LL implementation. The behavior is for AllGather - RING - LL test.
 
In the LL implementation, each channel has 256 threads.
Each thread in each trip, sends/receives 8B data.
So each trip of any primitive of LL transfers 256 threads x 8B = 2KB data.
I found that if the data size is not divisible by 128B (16 threads), the latency is very high.
 
In the following experiment, I increase the data by 16B in each step, meaning that 2 more threads will transfer data.
Every 8 steps (x 2 threads = 16 threads or 1/4 of warp size), the latency is low.
Otherwise, latency is huge (~150us difference).
Can anyone understand why this is happening?

![3MI300X](https://github.com/ROCm/rccl/assets/10295464/82b71d95-a5c8-445e-b7a6-e24e8d8a8d58)

Sincerely,
- Alireza



### Operating System

Ubuntu 22.04.3 LTS (Jammy Jellyfish)

### CPU

Intel(R) Xeon(R) Platinum 8480C

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

Using 3 fully-connected GPUs:

RCCL_MSCCL_ENABLE=0 NCCL_PROTO=LL NCCL_ALGO=RING NCCL_MIN_NRINGS=16 NCCL_MAX_NRINGS=16  LD_LIBRARY_PATH=rccl-rocm-6.1.2/build/release/:$LD_LIBRARY_PATH ./build/all_gather_perf -g 3 -b 50331648 -e 50334720 -i 48 -s 1

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### gilbertlee-amd · 2024-07-03

Hi @arkhadem,

Thanks for reporting this - I've created an internal ticket to look into this and will update this ticket when we have some information about it.



### rahulvaidya20 · 2025-02-03

Hi @arkhadem,

I'm unable to reproduce this behavior with the latest ROCm release (6.3) and rccl-develop branch. Could you please try it out and let me know if you still see this issue?

### ppanchad-amd · 2025-05-12

@arkhadem. Closing ticket due to lack of response.  Please feel free to re-open issue if you still see the issue with the latest ROCm. Thanks!
