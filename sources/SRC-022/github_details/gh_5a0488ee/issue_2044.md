# [Issue #2044] rcclNetP2pPolicy returns ncclInvalidArgument when not using infiniband

source: https://github.com/ROCm/rccl/issues/2044
state: closed | updated: 2025-12-03T15:25:22Z
labels: status: triage

## 正文

### Problem Description

The following change in RCCL breaks aws-ofi-nccl.  rcclNetP2pPolicy returns ncclInvalidArgument.  My guess is there is no ncclIbHandle when not using IB.  The change prior to this one works.

https://github.com/ROCm/rccl/commit/45991fadadefe44d31ff8fd8278be981d57a3129

### Operating System

SUSE Linux Enterprise Server 15 SP6

### CPU

AMD EPYC 7A53 64-Core Processor

### GPU

MI250X

### ROCm Version

top of tree devel

### ROCm Component

_No response_

### Steps to Reproduce

Run multi-node rccl-tests all_reduce_perf with this change on Slingshot with aws-ofi-nccl plugin.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### ryanhankins · 2025-11-11

@AbandiGa 
