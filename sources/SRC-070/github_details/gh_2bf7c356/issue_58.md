# [Issue #58] output tokens in intranode::dispatch for each expert isn't packed?

source: https://github.com/deepseek-ai/DeepEP/issues/58
state: closed | updated: 2026-09-18T10:05:09Z
labels: 

## 正文

The output token in the intranode::dispatch kernel offsets is channel_offset + rank_offsets + recv_token_idx;
The tokens for each expert isn't contiguous?

If yes, do you have plan to optimize these?

Thanks.

## 评论 (1)

### LyricZhao · 2025-03-10

> The tokens for each expert isn't contiguous?

Yes, and it is by design. Some MoE models will make one token averagely select more than one expert in a GPU rank. So if we automatically expand/copy these tokens into different experts, the GPU memory consumption will be $\times$ expert-per-rank-per-token-selected, and make training OOM.

So if you want to do grouped GEMM later, you have to expand the tokens and control the GPU memory precisely by yourself. We currently don't have plans to refactor this design.
