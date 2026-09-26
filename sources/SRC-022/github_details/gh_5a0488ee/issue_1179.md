# [Issue #1179] One of the NODE will hang when NCCL_NET_GDR_READ=1

source: https://github.com/ROCm/rccl/issues/1179
state: closed | updated: 2024-06-26T09:06:29Z
labels: 

## 正文

Hi, deer developer,
We have no any NVlinks, the GPU and NIC are connected with a PCIe switch and connect to the CPU.
With two nodes, we run the NCCL_test with NCCL_NET_GDR_READ=1 , that means we enable GDR both on send and recv side.
One of the NODE will hang when the total data about 64KB, with the error logs as follows:
![GDR error](https://github.com/ROCm/rccl/assets/145751038/dae6a47a-46dc-4d6b-b0dd-ed3f42a53ce0)

But if we enable the GDR only on side, the issue will gone.

The TOPO is as follows:
![GDR error TOPO](https://github.com/ROCm/rccl/assets/145751038/613f57c2-f500-45c9-b898-9fa9d58c5640)

Can you give me some hint how to debug this issue?
Thank you very much.

## 评论 (2)

### shanleo2024 · 2024-05-17

Hi Dear developer,
Can you tell me if the RCCL can support GDR on both side? As we just run GDR only on one side, send side or receive side.
Any hint is a great gratitude, thank you again.

### shanleo2024 · 2024-06-26

As it is the hardware issue, no relateded with RCCL, close it now.
