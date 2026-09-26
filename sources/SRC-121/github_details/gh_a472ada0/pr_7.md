# [PR #7] dynamic-vs-static-shared-memo [Not for merge]

source: https://github.com/gpu-mode/lectures/pull/7
state: closed | updated: 2024-02-17T01:06:49Z
labels: 

## 正文

This is to investigate the execution time difference between the dynamic vs static shared memory.
If we use the **linear index for shared memory** (instead of the 2d index), the execution time is indeed the **same**.

Just made a few changes from the original dynamic shared memory implementation and obtained a "copy" of the same implementation with static shared memory (linear index form).

Three forms are benchmarked in the T4 GPU below.  Dynamic shared mem has the same runtime as the static shared memo with linear index.

![image](https://github.com/cuda-mode/lectures/assets/7495155/3f603490-f325-409d-8311-698e53d96b8a)

The full notebook can be previewed in this PR or [from Kaggle notebook](https://www.kaggle.com/code/lancerts/cuda-mode-session-5)

cc @jph00 


## 评论 (1)

### jph00 · 2024-02-17

Thanks for sharing @lancerts -- check out the posted YouTube video, in which I actually figured out the source of the slow-down and managed to fix it! (The fix is at the end of the notebook in the repo)
