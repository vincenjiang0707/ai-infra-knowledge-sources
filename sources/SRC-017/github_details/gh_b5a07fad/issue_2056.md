# [Issue #2056] [Issue]: Incorrect nChannels usage of P2P profiler

source: https://github.com/NVIDIA/nccl/issues/2056
state: closed | updated: 2026-08-17T02:20:54Z
labels: 

## 正文

### How is this issue impacting you?

Data corruption

### Share Your Debug Logs

We are tracking p2p operation in our edited inspector. However, in a user reported case we see a resource leakage of p2p operation.

This issue is caused by incorrect nChannels number passing into profiler plugin. If using the same logic of collectives, an operation is done when `(collInfo->nKernelChCompleted == collInfo->nKernelChStarted) && (collInfo->nKernelChCompleted == collInfo->nChannels)`. 

In `src/enqueue.cc`, `nChannels` is assigned as `p2pTasks[dir]->nChannels = nChannels[dir];`. Say it is 4, so inspector would think that it should close the operation when 4 channels are completed.

However, not all channel will be launched in p2p operation. If one proxy op has `nsteps == 0`, then it will be ignored. 
```
      if (proxyOps[dir].nsteps != 0) {
        // Calculate the opCount after adding batch since then the batch count will
        // equal one plus the batch index this p2p settled in.
        proxyOps[dir].channelId = channelId;
        proxyOps[dir].opCount = uint64_t(comm->planner.wipPlan.channels[channelId].nWorkBatchesP2p)<<1 | 1;
        proxyOps[dir].nChannels = nChannels[dir];
        proxyOps[dir].nPeers = concurrentTasks[dir];
        NCCLCHECKGOTO(ncclAddProxyOpIfNeeded(comm, plan, &proxyOps[dir]), ret, cleanup);
        NCCLCHECKGOTO(addProfilerProxyOpIfNeeded(comm, plan, &proxyOps[dir]), ret, cleanup);
      }
```

But inspector cannot know this situation, it will still wait for this ignored channel (since `nKernelChCompleted == 3 != 4 == nChannels`), causing resource leakage.

This issue will happen under specific message size, so we didn't notice this when testing with regular nccltest.



 

### Steps to Reproduce the Issue

We are testing this issue on 8x H20，with this nccltest command:
```
mpirun -np 8 -H localhost:8 -v --allow-run-as-root --bind-to none --map-by slot [some internal parameters] -x NCCL_P2P_NVL_CHUNKSIZE=8192 -x NCCL_P2P_LL_THRESHOLD=0  /path/to/nccl-tests/build/sendrecv_perf -b 8K -e 8K -f 2 -g 1
```

In this situation, nChannel will be 4, and actual launched proxy ops are less than 4.

Different platform may have different configuration, this parameter is calculated by LLM.

### NCCL Version

2.28.7

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (2)

### RicoloveFeng · 2026-04-20

In recent release 2.30.3, this issue may cause memory leakage.

### RicoloveFeng · 2026-08-17

I think this issue has been fixed in the profiler refactor of 2.31. Thank you! @armratner 

```cpp
  for (int part = 0; part < nChannelsMax; part++) {
    int channelId = ncclP2pChannelForPart(comm->p2pnChannels, base, part);
    plan->channelMask |= uint64_t(1) << channelId;
    // Each direction uses its first nChannels[dir] parts; track per-direction
    // channels so the profiler emits KernelCh per direction (see profiler.cc).
    for (int i = 0; i < 2; i++)
      if (part < nChannels[i]) p2pDirChannelMask[i] |= uint64_t(1) << channelId;
    ...
    if (proxyOps[dir].nsteps != 0) {
      ...
      NCCLCHECKGOTO(ncclAddProxyOpIfNeeded(comm, plan, &proxyOps[dir]), ret, cleanup);
    }
    ...
  }
  for (int i = 0; i < 2; i++) {
    if (p2pTasks[i]) p2pTasks[i]->channelMask = p2pDirChannelMask[i];
  }

```

```cpp
      uint8_t profNChannels = pt->nChannels;
      if (pt->eActivationMask & ncclProfileKernelCh) profNChannels = (uint8_t)countOneBits(pt->channelMask);
      if (enable) {
        ...
        eDescr.p2p.nChannels = profNChannels;
        ...
```
