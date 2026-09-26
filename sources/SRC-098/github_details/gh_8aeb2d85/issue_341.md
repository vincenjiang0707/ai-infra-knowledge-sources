# [Issue #341] can alltoall use zero copy (only send without recv) by ncclCommRegister?

source: https://github.com/NVIDIA/nccl-tests/issues/341
state: open | updated: 2026-03-19T09:02:10Z
labels: 

## 正文

// nWarpPerWork = nWarps/nWorks
    int nWarpPerWork = __popc(__ballot_sync(~0u, nWorks*(lane+1) <= nWarps));
    int nRecvWarpPerWork = nWarpPerWork<=4 ? nWarpPerWork/2 : (nWarpPerWork-1)/2;
    int nSendWarpPerWork = nWarpPerWork<=4 ? nRecvWarpPerWork : nRecvWarpPerWork+1;

i found these codes in nccl/src/device/sendrecv.h, which means recv alway use half warps ,  maybe nccl-tests -R param can not use in ALL2ALL?

## 评论 (6)

### AddyLaddy · 2025-09-05

NCCL Send/Recv cannot make use of the Symmetric memory registration.
However, NCCL 2.28 now includes a new Collective API: `ncclAlltoAll`
And there is also a CE based implementation of the AlltoAll collective call. You need to use both Symmetric registration at CTA Policy `NCCL_CTA_POLICY_ZERO` to utilize it on certain platforms.


### alokprasad · 2025-09-24

@AddyLaddy 
1. "You need to use both Symmetric registration at CTA Policy NCCL_CTA_POLICY_ZERO to utilize it on certain platforms."
What do you mean by platform ? 
if i use NCCL_CTA_POLICY_ZERO then with NCCL 2.28/Cuda 13 will nccl-tests alltoall will use CE ?
how can i know amount of SM and CE used ?

### zhenhaohe · 2025-09-25

We have the requirements to use CE specified here: 
https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/bufferreg.html#zero-cta-optimization
AlltoAll API uses CE in NCCL perf tests if the above requirements are met.

### alokprasad · 2025-09-25

@zhenhaohe thanks and how to confirm from nccl logs, 

### zhenhaohe · 2025-09-25

You could add 

- NCCL_DEBUG=INFO
- NCCL_DEBUG_SUBSYS=INIT

And you will see information on CE initialization on the first run of your workload:
https://github.com/NVIDIA/nccl/blob/master/src/ce_coll.cc#L48

### banjiaojuhao · 2026-03-19

Summarize
```bash
NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=TUNING ./build/alltoall_perf -b 1K -e 1G -f 2 -g 4 -d half -w 20 -n 50 -x 2 -R 2
# NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=TUNING: for log to ensure CE is used. (NCCL INFO AlltoAll [Copy Engine]: 134217728 Bytes -> cudaMemcpy)
# [-x,--cta_policy <0/1/2> set CTA policy (NCCL_CTA_POLICY_DEFAULT (0), NCCL_CTA_POLICY_EFFICIENCY (1), NCCL_CTA_POLICY_ZERO (2)) (default: do not set)]
# [-R,--local_register <0/1/2> enable local (1) or symmetric (2) buffer registration on send/recv buffers (default: disable (0))]
```
