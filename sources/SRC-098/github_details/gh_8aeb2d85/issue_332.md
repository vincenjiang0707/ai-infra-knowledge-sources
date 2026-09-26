# [Issue #332] What hardware factors affect AllToAll performance?

source: https://github.com/NVIDIA/nccl-tests/issues/332
state: closed | updated: 2025-11-17T08:54:32Z
labels: 

## 正文

Hi team,

I'm trying to understand what hardware factors affect AllToAll performance.

I have three servers, each equipped with 8× RTX 5090 GPUs, but their intra NCCL AllToAll performance differs significantly:

`alltoall_perf -b 8 -e 1g -f 2 -g 8`
Server A: Dual Intel Xeon 6530 — AllToAll: 22 GB/s
Server B: Dual AMD EPYC 9554 — AllToAll: 25 GB/s
Server C: Dual AMD EPYC 9355 — AllToAll: 33 GB/s

I originally thought AllToAll performance was mainly dependent on the GPU, but these results suggest that the CPU platform has a major impact.

I understand that UPI (Intel) and xGMI (AMD) bandwidths can affect inter-socket communication, but could that really explain this much variation?
Both the 9355 and 9554 systems support 3 xGMI links, with a theoretical 192 GB/s unidirectional bandwidth.
The 6530 system has 3× 20 GT/s UPI links, with a theoretical 120 GB/s unidirectional bandwidth.

So why is there such a large performance gap, especially between 9355 and 9554, which seem to have the same xGMI bandwidth?

Any insights on which hardware factors (e.g., NUMA distance, PCIe topology, I/O die design, or CPU memory latency/bandwidth) might be causing this would be greatly appreciated.

Thanks!

## 评论 (3)

### PaggyZhang · 2025-07-25

alltoall_perf -b 8 -e 1g -f 2 -g 8
Server A: Dual Intel Xeon 6530 — AllToAll: 22 GB/s
Server B: Dual AMD EPYC 9554 — AllToAll: 25 GB/s
Server C: Dual AMD EPYC 9355 — AllToAll: 33 GB/s           


Why is my test result showing 0, and how should I configure the AMD platform for optimal performance?   

### PaggyZhang · 2025-07-25

![Image](https://github.com/user-attachments/assets/700f67ba-b0bb-4b32-93f2-a05ce47bf3b7)Could you help me ?

### changzhi1990 · 2025-08-18

try to enable p2p order write in the BIOS.
