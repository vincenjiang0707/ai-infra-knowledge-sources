# [Issue #657] [DeepEP V2] tma_copy data race

source: https://github.com/deepseek-ai/DeepEP/issues/657
state: closed | updated: 2026-07-08T04:30:28Z
labels: 

## 正文

https://github.com/deepseek-ai/DeepEP/blob/d4f41e4e93602a15e95f55f6ee8df8f1aaa0e4bb/deep_ep/include/deep_ep/impls/pp_send_recv.cuh#L88-L106

In the `tma_copy` function, the prefetch stage uses `tma_store_wait<kNumStages - 1>()` before reissuing a TMA load into the same shared memory buffer. With `kNumStages = 2`, this translates to `cp.async.bulk.wait_group 1`, which only waits until the number of pending store groups drops to ≤ 1 — meaning the current stage's store may still be in-flight when the next load overwrites the same smem buffer.

The pipeline executes as follows (with kNumStages = 2):

`iter 0, stage 0`: Load from global → stage0_smem. Wait mbarrier. Issue TMA store from stage0_smem → global; commit → group[A]. `Prefetch`: call tma_store_wait<1>().

At this point, group[A] (which reads from stage0_smem) is the only pending group, so wait_group 1 returns immediately without waiting for group[A] to complete.
A new tma_load_1d is then immediately issued into stage0_smem for the next iteration(iter=0+2=2).
Race: tma_store (group[A]) is still reading from stage0_smem while tma_load is writing new data into stage0_smem — this is a read-after-write hazard on the shared memory buffer, resulting in potential data corruption.

## 评论 (2)

### sphish · 2026-06-10

Thank you for pointing out this issue. Have you encountered any data errors caused by this problem in any environment?

### sphish · 2026-07-07

Fixed in https://github.com/deepseek-ai/DeepEP/pull/674. Thank you!
