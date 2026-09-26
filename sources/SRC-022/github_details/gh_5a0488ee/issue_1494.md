# [Issue #1494] Measuring time spent for reduction operation in AllReduce.

source: https://github.com/ROCm/rccl/issues/1494
state: closed | updated: 2025-05-13T06:37:36Z
labels: Under Investigation

## 正文

I am trying to measure time spent in reduction operation of RCCL Allreduce. I found that eventually it calls this part of code in common_kernel.h.      
#pragma unroll Unroll
      for (int u=0; u < Unroll; u++) {
        if (s < PreOpSrcs) tmp[u] = applyPreOp(preFn, tmp[u]);
        acc[u] = applyReduce(redFn, acc[u], tmp[u]);
      }

How can we measure time spent in applyReduce function? tried _clock64, wall_clock64. They are not helpful

## 评论 (4)

### ppanchad-amd · 2025-01-24

Hi @jain-jainendra. Internal ticket has been created to assist with your issue. Thanks!

### huanrwan-amd · 2025-02-03

Hi @jain-jainendra , 
In rccl-test examples (https://github.com/ROCm/rccl-tests), ./all_reduce_perf test could help to benchmark the time spent in reduction operation. 

e.g. https://rocm.docs.amd.com/en/develop/how-to/rocm-for-ai/training/train-a-model.html#running-the-rccl-bandwidth-test 

![Image](https://github.com/user-attachments/assets/83f12941-2d5f-4420-8dd0-bdd33e0d5c12)
It shows the out-of-place and in-place time for reduce operation.

Please let us know for any further help. 

### jain-jainendra · 2025-02-07

I am using RCCL tests only. But this gives complete time for allreduce application which involves communication and computation. I want to measure only time spent in computation i.e. reduction operation.

### huanrwan-amd · 2025-02-10

Hi @jain-jainendra, 
Just on the code level you could add: 
```
         unsigned long long start = clock64();
         acc[u] = applyReduce(redFn, acc[u], tmp[u]); 
         unsigned long long end = clock64();
```
To track the time in applyReduce(). 
As you may be aware in large-scale systems, reduction operations are performed asynchronously and in parallel. As a result, the computation and communication phases are interdependent and are highly optimized in libraries such as RCCL and NCCL.
