# [Issue #2915] [Feature Request][CuTe, SM100] Sparse MLA with native 64-head design

source: https://github.com/Dao-AILab/flash-attention/issues/2915
state: open | updated: 2026-09-25T16:08:07Z
labels: 

## 正文

Kudos to https://github.com/Dao-AILab/flash-attention/pull/2883 that really speeds up 64-head DSA padding a lot! I wonder if there's any plan on a native 64-head implementation?

The reason why I prefer FA4 over FlashMLA + cuDNN is that FA4 is more accurate, because FlashMLA doesn't export `o_lo`.

I let coding agent run for a while and it came up with a implementation. I opened a draft at: https://github.com/Dao-AILab/flash-attention/pull/2914 This is no way reviewable. So I wonder if there's an official plan to support 64-head DSA?

## 评论 (1)

### jayhshah · 2026-09-25

I started an implementation a while ago that has 1CTA design with 64 M tile (so adapted to native 64 head MQA) but need to finish porting sparse topk gather. Branch is jshah/mla-1cta
