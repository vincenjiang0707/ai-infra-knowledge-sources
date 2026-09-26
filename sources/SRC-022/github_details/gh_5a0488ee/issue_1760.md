# [Issue #1760] [Issue]RCCL 2.22.3-v1 alltoall with PXN will not do the message aggregation

source: https://github.com/ROCm/rccl/issues/1760
state: closed | updated: 2026-01-22T02:06:22Z
labels: 

## 正文

Hi dear developer,

We tested the RCCL 2.22.3-v1, alltoall with PXN open can not do the message aggregation. While NCCL 2.22.3 in A100, alltoall with PXN open can do the message aggregation, can you give me some comments why RCCL don't do the message aggregation?
Thank you.

## 评论 (8)

### nileshnegi · 2025-06-24

just clarifying, in RCCL, PXN is disabled by default... so are you using `NCCL_PXN_DISABLE=0` to use PXN with RCCL?
also, can you shed some light on how you are measuring/checking for message aggregation?

### shanleo2024 · 2025-07-14

> just clarifying, in RCCL, PXN is disabled by default... so are you using `NCCL_PXN_DISABLE=0` to use PXN with RCCL? also, can you shed some light on how you are measuring/checking for message aggregation?
Hi @nileshnegi 
In deed I set 'NCCL_PXN_DISABLE=0' to enable PXN manually, by checking the code: recvProxyProgress
args->nsubs is always 1, so there is no multi recv for PXN.
I has set those two variables already:
NCCL_NET_SHARED_BUFFERS=1
NCCL_NET_SHARED_COMMS=1

If I have some misunderstanding, please correct me, thank you.


### shanleo2024 · 2025-07-22

Hi @nileshnegi
I noticed NCCL_MAX_DEV_WORK_P2P_PER_BATCH is set to 1 in RCCL, while 8 in NCCL
What considerations led to setting this value to 1？
and this one:
NCCL:
```
#define NCCL_MAX_DEV_WORK_BATCH_BYTES 1024
#define NCCL_MAX_DEV_WORK_BATCH_COLLS (NCCL_MAX_DEV_WORK_BATCH_BYTES/sizeof(ncclDevWorkColl))
#define NCCL_MAX_DEV_WORK_P2P_PER_BATCH 8
```

RCCL:
```
#define NCCL_MAX_DEV_WORK_BATCH_BYTES 128
#define NCCL_MAX_DEV_WORK_BATCH_COLLS (NCCL_MAX_DEV_WORK_BATCH_BYTES/sizeof(ncclDevWorkColl))
#define NCCL_MAX_DEV_WORK_P2P_PER_BATCH 1
```
As NCCL_MAX_DEV_WORK_P2P_PER_BATCH  is set to 1, the alltoall PXN will not do the message aggregation indeed.
Wish for receiving your response, thank you.

### shanleo2024 · 2025-08-05

Hi, is there any update for this issue?
Wonder is there some enhancement if the message aggregation  supported by PXN?

Thank you.

### nileshnegi · 2025-10-01

@shanleo2024 we recently added support for batching P2P operations in multi-node runs: https://github.com/ROCm/rccl/commit/c1e1f2faeb4fad73679603e3c200560d653849a2

This can be enabled with `RCCL_P2P_BATCH_ENABLE=1`

### shanleo2024 · 2025-10-11

@nileshnegi Hi, thank you for your effort!
I have read the commit, the NCCL_MAX_DEV_WORK_P2P_PER_BATCH is set to 2 mainly, and gain some performance benefits.
Furthermore, can this macro be set to 8? We have tested it but failed, as the total threads of one block is 256 and whole threads per warp is 64, NCCL_MAX_DEV_WORK_P2P_PER_BATCH=8 requires a total of 1024 threads.
And there is another question, will this change also affect other operators such as Allreduce and AllGather?

Thank you!


### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2783

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
