# [Issue #393] `blocking_coll==3` synchronizes each iteration

source: https://github.com/NVIDIA/nccl-tests/issues/393
state: closed | updated: 2026-08-06T16:47:43Z
labels: 

## 正文

When `blocking_coll=3`, each inner iteration also synchronizes. Is it the expected behaviour, since README says "wait and barrier after each outer iteration" (implicitly I guess, meaning not wait nor barrier for inner iterations) ?

https://github.com/NVIDIA/nccl-tests/blob/a0b82b2260cf5152b9f8c061bbf7eaf0ba096432/src/common.cu#L620-L624

## 评论 (3)

### AddyLaddy · 2026-08-03

Good catch. This is not the intended mode-3 behavior. Mode 3 should synchronize only after the outer iteration. The synchronization in `startColl()` should apply only to modes 1 and 2; mode 3 already has its post `ncclGroupEnd()` synchronization in `BenchTime()`. We also need to preserve synchronization for the priming, warmup, and correctness paths through `completeColl()`.
I'll get a fix ready, thanks for the report.


### AddyLaddy · 2026-08-05

Have you had a chance to verify my fix?


### Eren121 · 2026-08-06

Yeah, it looks good now, I did the same changes.
Thanks.
