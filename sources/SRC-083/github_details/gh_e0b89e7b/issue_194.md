# [Issue #194] (Feature request) DirectML support

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/194
state: open | updated: 2026-03-31T16:32:47Z
labels: Windows, Cross Platform

## 正文

I have an AMD GPU, so my way of getting around not having CUDA is by using DirectML. Unfortunately, this depends on CUDA APIs (and is Linux only), so I can't use it.

## 评论 (5)

### RoARene317 · 2023-03-21

Just use Linux, make sure your GPU support ROCm. Case closed.

### github-actions[bot] · 2023-12-20

This issue has been automatically marked as stale because it has not had recent activity. If you think this still needs to be addressed please comment on this thread.



### yoda5477 · 2024-08-20

This would be greatly appeciated now that it is needed for flux nf4. not sure how complexe to solve the current issue link to only cuda compatible


### ethrx · 2025-03-02

Can we re-open this?

It's a valid use-case. 

### matthewdouglas · 2025-03-02

@ethrx I agree, especially for consumer AMD GPUs not otherwise supported in ROCm. I'll reopen this, but we won't be able to get to this right away.
