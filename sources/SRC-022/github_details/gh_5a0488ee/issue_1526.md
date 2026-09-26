# [Issue #1526] How to Customize All-to-all kernels in RCCL

source: https://github.com/ROCm/rccl/issues/1526
state: closed | updated: 2025-02-20T21:01:33Z
labels: question, Under Investigation

## 正文

Hi, 

I currently am looking into optimizing all-to-all communication kernels across 256 MI250 GPUs under our cluster topology. What are the files should I get started looking into? 

Thanks! 

## 评论 (6)

### ppanchad-amd · 2025-02-04

Hi @zixianwang2022. Internal ticket has been created to assist with your issue. Thanks!

### huanrwan-amd · 2025-02-04

Hi @zixianwang2022 , 
Thanks for posting questions. Here are some introduction docs you can review first: 

- https://rocm.docs.amd.com/projects/rccl/en/develop/what-is-rccl.html
- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html

"optimizing all-to-all communication kernels across 256 MI250 GPUs under our cluster topology" is a broad topic. Can you elaborate more on what is the optimization goal and on what level to optimize?

### zixianwang2022 · 2025-02-04

Hello @huanrwan-amd , 

Thanks for the quick response! I have 64 nodes, and each neighboring node is connected with 2x infinibands with 400Gb/s. The objective is to optimize for all-to-all communication. Here's what we have been thinking of: node_{i} will send data to node_{i+1} and receive data from node_{i-1} through IBs. Before the data arrives from previous node (slower IB bandwidth), I will do 1 intra-node all-to-all communication (faster intra-node infinity fabrics). Is it possible to implement such algorithm? 

### huanrwan-amd · 2025-02-06

Hi @zixianwang2022 , 
Because of intellectual property, I can not comment on whether your proposed algorithm can be implemented or not. I can help you to understand the existing code base related to your questions.

Your request is to setup a specific topology. The docs and code around communicator could help. 

1. General docs: https://rocm.docs.amd.com/projects/rccl/en/latest/how-to/using-nccl.html#operation-overview https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/communicators.html. 
3. Related code entrance for topo detection, graph search/optimize/connect: https://github.com/ROCm/rccl/blob/develop/src/init.cc -> initTransportsRank() , it calls the graph routine in https://github.com/ROCm/rccl/tree/develop/src/graph
```
  // Topo detection / System graph creation
  NCCLCHECKGOTO(ncclTopoGetSystem(comm, &comm->topo), ret, fail);
  // save nRanks to ncclTopoSystem as indicator of multi-node
  comm->topo->nRanks = comm->nRanks;
  // init netGdrLevel
  comm->topo->netGdrLevel = -2;
  // init Pivot A2A related fields
  comm->topo->pivotA2AEnabled = false;
  comm->topo->pivotA2ANumBiRings = 0;
  // LL128
  comm->topo->ll128Enabled = false;
  // Topology hint for MSCCL internal scheduler about whether to enable MSCCL
  comm->topo->mscclEnabled = false;
  // Topology hint if tree has been defined by model or User
  comm->topo->treeDefined = false;
  // Compute paths between GPUs and NICs
  NCCLCHECKGOTO(ncclTopoComputePaths(comm->topo, comm), ret, fail);
  // Remove inaccessible GPUs and unused NICs
  NCCLCHECKGOTO(ncclTopoTrimSystem(comm->topo, comm), ret, fail);
  // Recompute paths after trimming
  NCCLCHECKGOTO(ncclTopoComputePaths(comm->topo, comm), ret, fail);
  // Init search
  NCCLCHECKGOTO(ncclTopoSearchInit(comm->topo), ret, fail);
  // Decide on comm's CPU architecture.
  NCCLCHECKGOTO(ncclTopoComputeCommCPU(comm), ret, fail);
  // Print final topology
  NCCLCHECKGOTO(ncclTopoPrint(comm->topo), ret, fail);
```


It is also noticed that msccl is Intergrated and tuned https://github.com/ROCm/rccl/tree/develop/tools/msccl-algorithms .



### zixianwang2022 · 2025-02-06

Hi @huanrwan-amd , 

Thanks for the information! These links will be very helpful. 

### huanrwan-amd · 2025-02-06

@zixianwang2022 Not a problem, if you have any further questions. Let us know. 
