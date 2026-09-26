# [Issue #502] RCCL plugin uses UCX

source: https://github.com/ROCm/rccl/issues/502
state: closed | updated: 2022-03-31T16:47:35Z
labels: 

## 正文

When RCCL plugin uses UCX, PCI creation fails. Refer to the previous issues. What is the specific reason?
https://github.com/ROCmSoftwarePlatform/rccl/issues/480
```
j17r2n14:15524:15581 [0] NCCL INFO Connected all rings comm 0x2aaf44000c00 nRanks 08 busId 4000
j17r2n13:31976:32049 [0] NCCL INFO Connected all rings comm 0x2b6520000c00 nRanks 08 busId 4000
j17r2n14:15524:15581 [0] NCCL INFO Channel 00 : 0[4000] -> 4[4000] [receive] via NET/UCX/0/GDRDMA comm 0x2aaf44000c00 nRanks 08
j17r2n13:31976:32049 [0] NCCL INFO Channel 00 : 4[4000] -> 0[4000] [receive] via NET/UCX/0/GDRDMA comm 0x2b6520000c00 nRanks 08
j17r2n14:15524:15581 [0] NCCL INFO Channel 01 : 0[4000] -> 4[4000] [receive] via NET/UCX/0/GDRDMA comm 0x2aaf44000c00 nRanks 08
j17r2n13:31976:32049 [0] NCCL INFO Channel 01 : 4[4000] -> 0[4000] [receive] via NET/UCX/0/GDRDMA comm 0x2b6520000c00 nRanks 08
j17r2n14:15524:15581 [0] NCCL INFO Channel 00 : 4[4000] -> 0[4000] [send] via NET/UCX/0 comm 0x2aaf44000c00 nRanks 08
j17r2n13:31976:32049 [0] NCCL INFO Channel 00 : 0[4000] -> 4[4000] [send] via NET/UCX/0 comm 0x2b6520000c00 nRanks 08
j17r2n14:15524:15581 [0] NCCL INFO Channel 01 : 4[4000] -> 0[4000] [send] via NET/UCX/0 comm 0x2aaf44000c00 nRanks 08
j17r2n13:31976:32049 [0] NCCL INFO Channel 01 : 0[4000] -> 4[4000] [send] via NET/UCX/0 comm 0x2b6520000c00 nRanks 08
===ipc/rocm_ipc_md.c 71 error info: status:4097 base_ptr:0x2b651b200000 size:6422528 key->ipc:0x2b6520b4a260===
[1645148934.092347] [j17r2n13:31976:0]     rocm_ipc_md.c:72   UCX  ERROR Failed to create ipc for 0x2b651b200000/620000
===ipc/rocm_ipc_md.c 71 error info: status:4097 base_ptr:0x2aaf3f000000 size:6422528 key->ipc:0x2aaf4477f820===
[1645148934.092526] [j17r2n14:15524:0]     rocm_ipc_md.c:72   UCX  ERROR Failed to create ipc for 0x2aaf3f000000/620000
===ipc/rocm_ipc_md.c 71 error info: status:4097 base_ptr:0x2b653a000000 size:6422528 key->ipc:0x2b652069df90===
[1645148934.093308] [j17r2n13:31976:0]     rocm_ipc_md.c:72   UCX  ERROR Failed to create ipc for 0x2b653a000000/620000
===ipc/rocm_ipc_md.c 71 error info: status:4097 base_ptr:0x2aaf62800000 size:6422528 key->ipc:0x2aaf4477f5f0===
[1645148934.093589] [j17r2n14:15524:0]     rocm_ipc_md.c:72   UCX  ERROR Failed to create ipc for 0x2aaf62800000/620000
===ipc/rocm_ipc_md.c 75 success info: status:0 base_ptr:0x2b651a800000 size:8388608 key->ipc:0x2b6520b4ad80===
===ipc/rocm_ipc_md.c 75 success info: status:0 base_ptr:0x2aaf3e600000 size:8388608 key->ipc:0x2aaf44ba8b30===
===ipc/rocm_ipc_md.c 75 success info: status:0 base_ptr:0x2b6539600000 size:8388608 key->ipc:0x2b6520b9d650===
===ipc/rocm_ipc_md.c 75 success info: status:0 base_ptr:0x2aaf61e00000 size:8388608 key->ipc:0x2aaf44b9df90===
```

## 评论 (1)

### gilbertlee-amd · 2022-03-31

There were some bugs that were recently fixed in UCX with regards to ROCm support.  Please try a newer version (1.12.x).
