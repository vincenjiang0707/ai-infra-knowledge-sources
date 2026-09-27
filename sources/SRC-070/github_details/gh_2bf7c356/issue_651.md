# [Issue #651] ElasticBuffer.barrier doesn't ensure global sync in hybrid mode

source: https://github.com/deepseek-ai/DeepEP/issues/651
state: closed | updated: 2026-07-07T07:58:43Z
labels: 

## 正文

## Problem

We found `test_ep.y` first round dispatch is usually slower than later.
It uses `ElasticBuffer.barrier` by default in `bench_kineto`, and can be walk around by switching to `dist.all_reduce`.

## Reason

in `gpu_barrier` implementation:
https://github.com/deepseek-ai/DeepEP/blob/d4f41e4e93602a15e95f55f6ee8df8f1aaa0e4bb/deep_ep/include/deep_ep/common/comm.cuh#L213
```cpp
        // Do scaleup and scaleout barrier in parallel
        EP_DEVICE_ASSERT(kNumSMs >= 2 and "At least 2 SMs for a hybrid barrier");
        if (sm_idx == 0) {
            // First SM do the scaleup barrier
           ...
        } else {
            // The remaining SMs do the scaleout barrier
            ...
        }
```

It uses 2 SM for rail and LSA domain separately.
If a rank enters barrier quite late, members of its rail and LSA domain will be blocked;
while other ranks won't be blocked, and their dispatch kernel will have long execution time.

```
+------ node0 -------+  +------- node1 ------+
| +--------------+   |  |   +--------------+ |
| | rank0 (----) | <-|--|-- | rank2 (wait) | | ...... rail0
| +--------------+   |  |   +--------------+ |
|        ^           |  |          ^         |
|        |           |  |          |         |
|        |           |  |          |         |
| +--------------+   |  |   +--------------+ |
| | rank1 (wait) | <-|--|-- | rank3 (exit) | | ...... rail1
| +--------------+   |  |   +--------------+ |
+--------------------+  +--------------------+
```
* rank0 hasn't enter barrier
* rank1 and rank2 enter and wait for rank0's signal
* rank3 enters barrier, receives signals from rank1 and rank2, then exits


## Possible Solution

Run rail and LSA domain sequentially



## 评论 (0)
