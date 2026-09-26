# [Issue #334] 5090 alltoall  bandwith is 0

source: https://github.com/NVIDIA/nccl-tests/issues/334
state: open | updated: 2025-08-05T01:26:59Z
labels: 

## 正文

![Image](https://github.com/user-attachments/assets/98d89a92-1c07-4f3d-a3ed-f8cfdfbd5041)

## 评论 (5)

### PaggyZhang · 2025-07-25

Can I get some help if the settings ? Thanks!

### sjeaugey · 2025-07-25

Geforce cards don't support CUDA P2P, so everything has to go back to the CPU. Your performance is therefore fully dependent on your CPU memory performance, and the more flows you add to it, the lower performance will be (with 8 GPUs it's going to be 8 flows).

One typical problem we see is AMD CPUs being configured as one Numa domain Per Socket (NPS). Setting NPS to 2 or 4 can help a lot. Besides that though, there isn't much we can help with, as the speed of your CPU and memory is outside our control.

### PaggyZhang · 2025-07-25

Are there any other settings that need attention?

### changzhi1990 · 2025-08-04

which kind of CPU?

### PaggyZhang · 2025-08-05

5090D
