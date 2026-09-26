# [Issue #1220] Compatibility and Setup of RCCL with NCCL for Mixed GPU HPC MLOps Cluster

source: https://github.com/ROCm/rccl/issues/1220
state: closed | updated: 2024-12-23T06:51:05Z
labels: 

## 正文

## Description

Hello,

I am currently working on configuring an HPC MLOps cluster that integrates both AMD and NVIDIA GPUs. I came across information suggesting that RCCL can be compatible with certain NCCL versions as mentioned in the [RCCL changelog](https://github.com/ROCm/rccl/blob/develop/CHANGELOG.md). I am trying to understand if it is possible to run a collective communication job leveraging both RCCL and NCCL.

## Setup Details

- **Instances:** AWS g4ad (gfx1011 with ROCm 6.1.2,  rocBLAS build from source, and RCCL 2.18.6 build from source ) and g4dn (AMD with CUDA 12.1 and NCCL 2.18.6 build from source)
- **PyTorch Example:** [Distributed Data Parallel (DDP) example](https://github.com/pytorch/examples/blob/main/distributed/ddp-tutorial-series/multinode.py)
- **Error Encountered:**
    ```bash
    NCCL WARN NET/Socket: message truncated: receiving X bytes instead of Y.
    ```
    The expected and received byte values vary with different combinations of NCCL and RCCL versions. (I tried the unreleased RCCL 2.20.5 with NCCL 2.20.5)
    
## Questions

1. Can a collective communication job be run leveraging both RCCL and NCCL?
2. Could you give me some insight on whether this approach heads a good direction and or if leveraging UCX and UCC would be more effective for such a heterogeneous setup?
3. Any guidance or resources on configuring and troubleshooting this setup would be immensely helpful.

Thank you very much for your time and assistance.



## 评论 (2)

### gilbertlee-amd · 2024-07-02

Hi @RafalSiwek,

Sorry - even though RCCL is a port of NCCL, there's a lot of under-the-hood changes that prevent heterogenous usage of RCCL and NCCL across a cluster.

1) No.  This would not be supported.
2) UCX might work if you have different nodes with different hardware, but I'm not sure if anyone has tested this.  You'd likely get a better response from the UCX team about this use case.
3) Not applicable, due to lack of support.

### etoilestar · 2024-12-23

Could you please clarify what changes were made under the hood in RCCL compared to NCCL?

