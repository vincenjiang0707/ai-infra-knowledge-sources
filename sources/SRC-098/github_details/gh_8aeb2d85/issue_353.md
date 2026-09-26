# [Issue #353] Poor dual-node performance when NCCL selects topologically-close NICs (H100/CX6)

source: https://github.com/NVIDIA/nccl-tests/issues/353
state: closed | updated: 2025-10-24T17:08:20Z
labels: 

## 正文

Environment

NCCL Version: 2.27.6
nccl-tests Version: 2.16.4
NVIDIA Driver: 580.95.05
CUDA Version: 13.0, V13.0.88

Hardware:

Nodes: 2 x Cray XD670 H100 (cl4-gpu03, cl4-gpu04)
GPUs per Node: 8 x H100
NICs per Node: 4 x ConnectX-6/8 (e.g., mlx5_0, mlx5_2, mlx5_4, mlx5_6)

Problem Description
In a *dual-node* setup , nccl-tests (e.g., all_reduce_perf) with the hardware above, we are observing significantly degraded performance. The test seems to cap at approximately 31 Gbps x 2 (~62 Gbps) aggregate bandwidth.

Our hardware and links are healthy. A simple ib_write_bw --use_cuda test between nodes over a single link consistently achieves ~95 Gbps, so we are expecting much higher performance from NCCL.

Root Cause Analysis
The performance issue appears to be directly related to GPU and NIC selection.

Based on our system topology (see attached diagram), when nccl-tests are run, NCCL appears to correctly identify and use NICs that are "topologically close" to the acting GPU. However, this path is paradoxically the slowest.

Example from our topology (cl4-gpu03, CPU_0):

<img width="1427" height="908" alt="Image" src="https://github.com/user-attachments/assets/e3081616-c763-411e-8983-910e0e2d6b7e" />

GPU 0 (on PCIe 0000:18:00.0) or GPU1
NIC mlx5_0 / mlx5_1 (on PCIe 0000:18:00.0)
These devices share the same parent PCIe switch (0000:16:00.0 ( one level up )). When NCCL uses this "local" path, we get the bad performance (~31 Gbps per NIC). Note - its a baremetal, not a VM. 

We have found that if we manually force NCCL to use topologically distant NICs, the performance doubles (2x).
 If we manually pin GPU 2-3( any of them)  using `-x CUDA_VISIBLE_DEVICES=`  or even on a different NUMA node (e.g.,GPU4-7), we get significantly better performance ( 2x ).



## 评论 (1)

### AddyLaddy · 2025-10-24

This is the nccl-test repo. NCCL issues should be reported against the NCCL GitHub project or via support channels with Cray/HPE or Nvidia.

