# [Issue #1698] Inference quality regression

source: https://github.com/AI-Hypercomputer/maxtext/issues/1698
state: closed | updated: 2026-05-11T03:16:10Z
labels: 

## 正文

We're trying to track down a regression in decoding results, where on several evals on a gemma2-like model we get >10% worse results than expected.  Our branch is around a month old, but we isolated the issue to these lines, where if we comment them out we get much better eval results (25% -- same as VLLM, which is our control) than if we leave them in (15%).

https://github.com/AI-Hypercomputer/maxtext/blob/6247f4439fd48c58550fca8a2a6877e77ba0fcd2/MaxText/layers/attentions.py#L925-L928

I don't really understand how sharding could have that big of an effect, but it reliably does.  I also don't understand the purpose of `is_partition_in_decode` -- we're not trying to use context parallelism, but since it defaults to 1, this function returns true.

https://github.com/AI-Hypercomputer/maxtext/blob/6247f4439fd48c58550fca8a2a6877e77ba0fcd2/MaxText/layers/attentions.py#L866-L867

Have you seen issues like this?

## 评论 (1)

### RissyRan · 2025-05-28

Hi @suexu1025 and @mailvijayasingh I think this is a similar issue we met before and we have set out the fix? Could you help confirm?
