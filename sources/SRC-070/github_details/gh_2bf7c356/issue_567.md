# [Issue #567] question about Hybrid-EP

source: https://github.com/deepseek-ai/DeepEP/issues/567
state: open | updated: 2026-07-30T09:47:13Z
labels: 

## 正文

hello~@Autumn1998  I’d like to ask some questions about Hybrid-EP.

1. i found that there has cudamemcpy from/to user hidden tensor to/from rdma registed buffer in Hybrid-EP. When using the permute version, the cudamemcpy in postprocess can be fused, but the preprocessing still remains. So i wonder if it can use zero copy in Hybrid-EP like [this]( https://github.com/deepseek-ai/DeepEP/pull/79/files).
2. There seem to be redundant stores [here](https://github.com/deepseek-ai/DeepEP/blob/hybrid-ep/csrc/hybrid_ep/extension/permute.cu#L202).
thx~

## 评论 (1)

### Autumn1998 · 2026-01-30

@Thunderbrook Sorry for missing this issue:

1. Theoretically, we could use zero-copy for the input part in the inter-node case. But this would make the op not standalone, that is., we would need to expose a tensor and let the attn side write the results directly into it, which we prefer not to do unless it causes a significant perf regression.

2. What does “redundant store” refer to here? If you mean token per expert, after we apply padding we will recompute token per expert and write it again, and its meaning is different from the previous one.
