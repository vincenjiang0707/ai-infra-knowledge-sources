# [Issue #1206] [Issue]: RCCL collective call Alltoall is performing way worse than normal MPI Alltoall on Frontier.

source: https://github.com/ROCm/rccl/issues/1206
state: closed | updated: 2025-05-12T15:30:41Z
labels: Under Investigation

## 正文

### Problem Description

I ran my code on Frontier for scaling on AMD GPUS. It scaled fine with MPI . But as soon as i replace the MPI_Alltoall call with nccl_Alltoall, it is behaving way worse than MPI. why??

### Operating System

SLES (Frontier)

### CPU

AMD EPYC 7763 64-Core Processor

### GPU

AMD Instinct MI250X

### ROCm Version

ROCm 5.7.1

### ROCm Component

rccl

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (5)

### edgargabriel · 2024-07-03

@manver-iitk  a couple of questions: 
- how many nodes did you use ( 1 node vs. more than 1 node) ? 
- if the answer is more than 1 node, how did you configure RCCL on Frontier? Did you use the RCCL libfabric plugin for the inter-node communication?  If not, RCCL will end up using tcp sockets as far as I know (since Frontier does not support verbs API), which might explain why RCCL is so much slower than MPI Alltoall.

### corey-derochie-amd · 2024-09-19

Hello, @manver-iitk .
Has this issue been resolved for you?

### manver-iitk · 2024-10-07

Hello , @corey-derochie-amd my issue still persists.

@edgargabriel i have installed the aws_ofi_rccl driver also for inter node communication. But still timmings is almost 2x to 3x of normal MPI. I'm using 4 to 8 nodes 


### thananon · 2024-10-29

Hi, for alltoall, RCCL uses fan-out algorithm which is very crude (everyone send and recv from everyone). Whereas MPI is doing this in a more algorithmic way. This is the area where we acknowledge NCCL/RCCL lacks. Unfortunately optimizing alltoall for multi-node is not high on our priority list.

### ppanchad-amd · 2025-05-12

We are not expecting to match Alltoall performance of MPI. Closing ticket.
