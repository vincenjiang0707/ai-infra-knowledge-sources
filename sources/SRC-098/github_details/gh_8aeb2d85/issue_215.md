# [Issue #215] NCCL_ALGO on multi-node and multi-GPU

source: https://github.com/NVIDIA/nccl-tests/issues/215
state: open | updated: 2025-06-27T06:00:05Z
labels: 

## 正文

Hi.

I have been running NCCL_TESTS on a multi-node, multi-GPU environment with NCCL 2.19.3-1 and OpenMPI 4.1.6. Each node has 4 NVIDIA V100 GPUs interconnected with NVLink and PCIe.

1. How is the ``NCCL_ALGO`` chosen by default, and what is the decision logic for choosing the algorithms for inter-node and intra-node communications?

2. If I specify ``NCCL_ALGO=Ring`` and at the same time set the ``OMPI_MCA_coll_tuned_use_dynamic_rules=1`` and set an algorithm for ``coll_tuned_allreduce_algorithm``, how the final algorithm will be chosen? Does it go with the NCCL one or the MCA one? Or maybe one is chosen for inter-node and the other for intra-node?

## 评论 (3)

### sjeaugey · 2024-05-21

1. We have an internal model which compares the performance of the different algorithms and (hopefully) chooses the best one.
2. You're mixing up NCCL and MPI. The OMPI_ setting controls MPI and NCCL does not use MPI (even for inter-node communication). MPI is only used by the NCCL tests to spawn tasks and help with the CPU-CPU synchronization, but it's not required by NCCL, at all.

### alokprasad-mrvl · 2025-01-28

@sjeaugey "NCCL does not use MPI (even for inter-node communication)."
I didnt understand this fully, then how does NCCL exchange info between nodes - if we use MPI it should be OPENMPI ( if there is no other   program socket(overt tcp) etc).

Does it mean we need to individually run nccl-tests on each node if we want to skip OpenMPI

### sjeaugey · 2025-01-28

> how does NCCL exchange info between nodes - if we use MPI it should be MPI ( if there is no other program socket(overt tcp) etc).

NCCL has its own networking layer, with network plugins (using sockets, IB/RoCE, [libfabrics](https://github.com/aws/aws-ofi-nccl), etc). NCCL does not need MPI for inter-node communication.

> Does it mean we need to individually run nccl-tests on each node if we want to skip OpenMPI

Yes, and you'll also need some way to share the NCCL handle between ranks to initialize NCCL, i.e. a CPU-CPU communication mechanism. Which is why MPI is a great companion for NCCL, as a launcher and CPU-CPU communication bootstrap mechanism, but it is not a dependency (for example, PyTorch doesn't use MPI).



