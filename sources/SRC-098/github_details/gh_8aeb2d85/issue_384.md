# [Issue #384] Why are different buffers used for each iteration when `-n` > 1 in nccl-tests?

source: https://github.com/NVIDIA/nccl-tests/issues/384
state: open | updated: 2026-05-29T07:37:36Z
labels: 

## 正文

Hi everyone,
```
testResult_t BenchTime(struct threadArgs* args, ncclDataType_t type, ncclRedOp_t op, int root, int in_place) {
  size_t count = args->nbytes / wordSize(type);
  if (datacheck) {
    // Initialize sendbuffs, recvbuffs and expected
    TESTCHECK(args->collTest->initData(args, type, op, root, 99, in_place));
  }

  // Sync
  TESTCHECK(startColl(args, type, op, root, in_place, 0));
  TESTCHECK(completeColl(args));

  Barrier(args);

#if CUDART_VERSION >= 11030
  cudaGraph_t graphs[args->nGpus];
  cudaGraphExec_t graphExec[args->nGpus];
  if (cudaGraphLaunches >= 1) {
    // Begin cuda graph capture
    for (int i=0; i<args->nGpus; i++) {
      // Thread local mdoe is needed for:
      // - Multi-thread mode: where graph capture and instantiation can happen concurrently across threads
      // - P2P pre-connect: when there is no warm-up, P2P pre-connect is done during graph capture.
      //   Since pre-connect calls cudaMalloc, we cannot use global capture mode
      CUDACHECK(cudaStreamBeginCapture(args->streams[i], cudaStreamCaptureModeThreadLocal));
    }
  }
#endif

  // Performance Benchmark
  timer tim;
  for (int iter = 0; iter < iters; iter++) {
    if (agg_iters>1) NCCLCHECK(ncclGroupStart());
    for (int aiter = 0; aiter < agg_iters; aiter++) {
      TESTCHECK(startColl(args, type, op, root, in_place, iter*agg_iters+aiter));
    }
    if (agg_iters>1) NCCLCHECK(ncclGroupEnd());
  }
```
I noticed that when I set `-n 10` (10 iterations), the test uses 10 different buffers instead of reusing the same buffer across iterations. I initially expected the same buffer to be reused, but that's not what happens.

And look at the code here，
```
// Sync
  TESTCHECK(startColl(args, type, op, root, in_place, 0));
  TESTCHECK(completeColl(args));
```
I think  this is actually a warm up for the first buffer,  the left 9 buffer will not  warm up.

I'd like to understand the design considerations behind this behavior.  Any considerations?



## 评论 (1)

### sjeaugey · 2026-05-29

A major flaw in communication benchmarks is to keep using the same buffers in a loop. This allows for some hardware mechanisms to kick in and report numbers that are higher than theoretically possible for real communication.

To illustrate what I mean, one such example is CPU-to-CPU communication using user buffers directly. If you keep using the same send buffer without the source writing it on each iteration, the send buffer will stay in the receiver CPU cache and the receiver CPU will do a local cache->cache copy in a loop, reporting the L3 cache bandwidth, which will be much higher than the actual CPU-CPU bandwidth. This makes the bandwidth go very high, then go down once the size is larger than the cache size. But it doesn't make any sense for a real application, since a sender would never send the same data twice without touching it in between. Re-initializing the source takes time and would make it hard to benchmark the communication time, so the best solution to that problem is to always use a sliding window, with that window being larger than all HW data caches.

Arguably, this mechanism could also break some HW cache effects which could actually be usable in real applications, but in our experience it never caused much trouble, and instead provided clean S curves. Testing-wise, it also helps as it swipes across different offsets instead of always using offset 0 of the buffers.

Now, if that was really problematic, I think it would be fairly easy to add an option to disable the sliding window and always run at offset 0.
