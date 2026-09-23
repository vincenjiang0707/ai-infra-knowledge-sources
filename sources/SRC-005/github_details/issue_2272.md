# [Issue #2272] [Kernel] cuDNN attention backend

source: https://github.com/sgl-project/sglang/issues/2272
state: open | updated: 2026-09-21T22:43:28Z
labels: enhancement, good first issue, help wanted, high priority

## 正文

cuDNN provides very fast attention implementation and it is well maintained by NVIDIA. We would like to add a new attention backend based on cudnn.  

## Steps
1. Learn this cudnn paged attention python api. https://github.com/NVIDIA/cudnn-frontend/blob/v1.8.0/samples/python/52_scaled_dot_product_attention_with_paged_caches.ipynb
2. Add a new attention backend "cudnn" here https://github.com/sgl-project/sglang/tree/main/python/sglang/srt/layers/attention
3. We should be able to use it with `python3 -m sglang.launch_server --model meta-llama/Llama-3.1-8B-Instruct --attention-backend cudnn`

## 评论 (5)

### zhyncs · 2024-12-04

Note: The key is to confirm whether supporting a page size of 1 is possible.

### github-actions[bot] · 2025-02-03

This issue has been automatically closed due to inactivity. Please feel free to reopen it if needed.

### ykdcai · 2025-02-27

Is anybody working on this issue now? We are interested working on in this issue. I will add a new `AttentionBackend` with cuDNN Python API.

### robertlee22 · 2026-04-15

Is this issue resolved yet?

### Oxygen56 · 2026-06-09

Hi @zhyncs @hnyls2002,

I'm interested in picking up the cuDNN attention backend. Before investing time, I'd like to confirm a few things:

1. **Is this feature still desired?** I noticed two previous PRs (#4650 and #5505) were both closed. PR #5505 by @ykcai-daniel got quite far — the int32/int64 correctness issue was resolved, but CUDA Graph integration wasn't completed before the PR was closed.

2. **Are there known technical blockers?** @zhyncs mentioned confirming page_size=1 support — is that still an open question?

3. **Any guidance on scope?** Should a new attempt focus on getting a working backend without CUDA Graph first, then add graph support incrementally?

Happy to align on the approach before starting. Thanks!
