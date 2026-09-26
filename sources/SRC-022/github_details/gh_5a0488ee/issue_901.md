# [Issue #901] Incorrect bandwidth values in the topology tree at rccl debug info 

source: https://github.com/ROCm/rccl/issues/901
state: closed | updated: 2023-10-31T18:49:20Z
labels: 

## 正文

Hi
I have server with 8 mi100 and two AMD 7003 CPU. All GPUs inserted into PCIe 4.0 bus. GPUs are grouped into 2 hives. There is xGMI connection between GPUs in each hive. I use pytorch 2.0 with ROCm 5.4.2 and have wrote test code to make all-reduce operation. After run code with env variable NCCL_DEBUG=TRACE I've got following topology in output:

```
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO === System : maxWidth 12.5 totalWidth 72.0 ===
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO CPU/0 (1/2/4)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO + SYS[5000.0] - CPU/1
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO + PCI[24.0] - PCI/31000 (1000c01010000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - PCI/45000 (100214a000000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + PCI[24.0] - GPU/47000 (0)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/4C000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/51000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/54000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - NIC/35000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + NET[12.5] - NET/0 (64300003fd7010/1/12.500000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + NET[12.5] - NET/1 (64300003fd7010/2/12.500000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - PCI/4A000 (100214a000000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + PCI[24.0] - GPU/4C000 (1)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/47000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/51000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/54000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - PCI/4F000 (100214a000000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + PCI[24.0] - GPU/51000 (2)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/47000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/4C000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/54000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - PCI/52000 (100214a000000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + PCI[24.0] - GPU/54000 (3)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/47000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/4C000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/51000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO CPU/1 (1/2/4)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO + SYS[5000.0] - CPU/0
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO + PCI[24.0] - PCI/B1000 (1000c01010000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - PCI/C5000 (100214a000000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + PCI[24.0] - GPU/C7000 (4)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/CC000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/D1000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/D4000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - NIC/B5000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + NET[12.5] - NET/2 (205b300003fd7010/1/12.500000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + NET[12.5] - NET/3 (205b300003fd7010/2/12.500000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - PCI/CA000 (100214a000000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + PCI[24.0] - GPU/CC000 (5)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/C7000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/D1000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/D4000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - PCI/CF000 (100214a000000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + PCI[24.0] - GPU/D1000 (6)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/C7000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/CC000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/D4000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO               + PCI[24.0] - PCI/D2000 (100214a000000000)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                             + PCI[24.0] - GPU/D4000 (7)
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/C7000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/CC000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO                                           + XGMI[24.0] - GPU/D1000
rdma-allreduce-test-master-0:26:76 [0] NCCL INFO ==========================================

``` 
As can see in the sample above XGMI/PCIe bandwidth (in square brackets after words XGMI and PCIe) is 24GB/s. It does not look as correct value. In the official doc XGMI and PCIe 4.0 unidirectional bandwidth speeds are 23 GT/s = 46GB/s and 32GB/s respectively. I do not understand why we have such different data transfer rate?


## 评论 (1)

### gilbertlee-amd · 2023-10-31

Hi @LukaOo ,
Sorry for the late response.  These values are actually hard-coded - not measured, so nothing to be concerned about.
They are only used as part of the topology search algorithm when no pre-existing configurations are detected, and have been selected to facilitate the search.
