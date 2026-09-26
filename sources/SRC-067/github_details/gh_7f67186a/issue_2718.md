# [Issue #2718] Why do we need proxy fence in FA4 BWD postprocess kernel?

source: https://github.com/Dao-AILab/flash-attention/issues/2718
state: open | updated: 2026-07-27T22:46:19Z
labels: 

## 正文

There is a `cute.arch.fence_view_async_shared()`, which translates to `fence.proxy.async.shared::cta;` PTX, follwing G2S, S2R and R2S copies of the BWD postprocess kernel:

https://github.com/Dao-AILab/flash-attention/blame/77aacb68d194ba9af1010eda5eac3e7c0df8e6f6/flash_attn/cute/flash_bwd_postprocess.py#L453

https://github.com/Dao-AILab/flash-attention/blame/77aacb68d194ba9af1010eda5eac3e7c0df8e6f6/flash_attn/cute/flash_bwd_postprocess.py#L468

https://github.com/Dao-AILab/flash-attention/blame/77aacb68d194ba9af1010eda5eac3e7c0df8e6f6/flash_attn/cute/flash_bwd_postprocess.py#L489

If I understand it correctly, all these copies are using `ld` or `st` to access GMEM and SMEM, which should all be in generic proxy, so there's no need for a fence between generic and async proxy.

From ncu it also seems the perf cost is not none:

<img width="1800" height="407" alt="Image" src="https://github.com/user-attachments/assets/62f12515-a721-4672-adee-7d81268b4ef1" />


I'll be glad to put up a PR if we agree they're not needed

## 评论 (2)

### Johnsonms · 2026-07-20

Thanks to @pchen7e2 for raising this issue.
Seems you're right, let me dig it into for the solidate evidence for this soon

### pchen7e2 · 2026-07-27

@Johnsonms The validations seem to have passed on your PR. What's the recommended next step?
