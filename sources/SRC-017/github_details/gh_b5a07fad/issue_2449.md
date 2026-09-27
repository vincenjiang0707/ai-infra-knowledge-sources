# [Issue #2449] [Issue]: ncclCommInitRankConfig / ncclCommInitRankScalable / ncclCommInitAll crash on invalid nranks, nId or ndev instead of returning ncclInvalidArgument

source: https://github.com/NVIDIA/nccl/issues/2449
state: open | updated: 2026-09-26T15:30:25Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

_No response_

### Steps to Reproduce the Issue

NCCL master 2.32.3-1 (12df1a11), CUDA 12.9, single node. Small program (full version attached), `comm` is declared the usual way and never initialized:

```c
ncclComm_t comm;          // uninitialized, as in every example
ncclUniqueId id; ncclGetUniqueId(&id);
ncclCommInitRankConfig(&comm, 0, id, 0, NULL);        // nranks = 0 -> SIGSEGV
ncclCommInitRankScalable(&comm, 1, 0, 0, &id, NULL);  // nId = 0    -> SIGSEGV
ncclCommInitRankScalable(&comm, 1, 0, 2, &id, NULL);  // nId > nranks -> SIGSEGV
ncclCommInitRankScalable(&comm, 1, 0, 1, NULL, NULL); // commIds NULL -> SIGSEGV in memcpy
ncclComm_t comms[1]; int dev = 0;
ncclCommInitAll(comms, 0, &dev);                      // ndev = 0 -> SIGSEGV
ncclCommInitRank(&comm, 0, id, 0);                    // same nranks = 0: returns ncclInvalidArgument, fine
```

Whether the first three crash depends on what happens to be in `comm` beforehand; with `comm = (ncclComm_t)0x1` they crash every time, with a stack slot that is zero they return `ncclInvalidArgument`.


`ncclCommInitRankDev()` (src/init.cc) checks `nId` first and returns with a plain `return ncclInvalidArgument;` before it has stored anything in `*newcomm`. Every other error in that function goes through `fail:`, which sets `*newcomm = NULL`. The callers assume that:

```c
fail:
  if (newcomm && *newcomm && !(*newcomm)->config.blocking) (void)ncclCommSetAsyncError(*newcomm, ret);
```

so on the nId path they dereference whatever the user had in the variable. `ncclCommInitRankConfig` hits it with `nranks = 0` because it passes `nId = 1` and the check is `nId > nranks`. `commId` also has no NULL check (`memcpy(job->commId, commId, nId * NCCL_UNIQUE_ID_BYTES)`).

`ncclCommInitAll()` rejects `ndev < 0` but not `ndev == 0`; with zero devices nothing is created and the NVTX payload line reads `comms[0]->commHash` from an array that was never written (default NVTX=1 build, no profiler needed).

Both since 2.23.4 (nId check) / 2.25.1 (NVTX payload in ncclCommInitAll).

### NCCL Version

2.32.3-1 (master 12df1a11)

### Your platform details

Ubuntu 24.04, CUDA 12.9, driver 595.84, RTX 5070 Ti + RTX 2070, single node. Host-side argument checks, nothing platform specific.

### Error Message & Behavior

_No response_

## 评论 (1)

### kodlan · 2026-09-26

Opened #2450 with the fix: the nId check moves after the pointer and rank checks so the fail path sets *newcomm to NULL like every other error, commIds gets a NULL check, and ncclCommInitAll rejects ndev == 0. The seven calls from the report all return ncclInvalidArgument now (verified on the 2-GPU box from the report), nccl-tests still pass.
