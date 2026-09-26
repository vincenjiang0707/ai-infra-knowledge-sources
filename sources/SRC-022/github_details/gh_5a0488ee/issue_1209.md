# [Issue #1209] Can RCCL support PXN if the GPUs are connected with XGMI?

source: https://github.com/ROCm/rccl/issues/1209
state: closed | updated: 2024-07-08T21:22:56Z
labels: 

## 正文

Hi Dear developer,

I notice in the RCCL code, the PXN is set to disabled by default:
`NCCL_PARAM(PxnDisable, "PXN_DISABLE", 1);`

I want to know if the PXN support when all of the GPUs are connected by XGMI and devices similar to NVSwitch if I set NCCL_PXN_DISABLE to 1?
As I have no XGMI and devices similar to NVSwitch, I just want to study the PXN and figure out if the RCCL can support PXN or not.

Thank you.


## 评论 (5)

### gilbertlee-amd · 2024-07-02

Hi @shanleo1986 ,

Yes - RCCL supports PXN, however we decided to disable it by default, as it made less performance improvements on the all-to-all point-to-point XGMI topology AMD hardware uses,  versus what it gets with the switch-based NVSwitch.  

By setting NCCL_PXN_DISABLE to 0 (not 1), you would enable the PXN functionality.  

### shanleo2024 · 2024-07-03

Hi @gilbertlee-amd 

> as it made less performance improvements on the all-to-all point-to-point XGMI topology AMD hardware uses

Did you mean if we enable PXN on XGMI topology AMD hardware, will peformance worse than PXN disabled?
Can you give some more explanation why?
Thank you.

### gilbertlee-amd · 2024-07-03

It depends a little on the use case, but performance could potentially be worse with PXN disabled.

With an NVSwitch, you can get full bandwidth between any two GPUs, assuming no other GPUs are communicating due to how the links are banded together.  However, with point-to-point XGMI, you can only get the bandwidth from the single XGMI link.  

In other words, with XGMI there isn't as much potential benefit by moving data from a GPU to a intermediate GPU prior to the network transfer, especially if there was already other traffic between those two GPUs.

### shanleo2024 · 2024-07-04

Hi @gilbertlee-amd 
Suppose we have one GPU and one NET which located on two CPU socket when running alltoall, do you mean for this case, the GPU send packets to the NET accross the CPU directlly performace better than the GPU send date to the intermediate GPU closed to the NET through XGMI firstly, and then send to the NET?
I don't catch the meaning totally, wish for your response, thank you.


### gilbertlee-amd · 2024-07-08

Hi @shanleo1986 ,

It will depend on the configuration, but yes, you could potentially see better performance going across the socket rather than through XGMI based on how much that XGMI link is being used by other transfers in the all-to-all.

For the all to all, you already have a transfer between GPU A and GPU B, and it would have to share bandwidth with the intermediate transfer from GPU A -> GPU B -> (Net) -> GPU C.    

Our single GPU to GPU maximum bandwidth is limited to what only a single XGMI link can provide, which is less flexible than the NVSwitch based hardware implementation.




