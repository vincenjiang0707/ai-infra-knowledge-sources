# [Issue #235] [Question] Contiguous Grouped Gemm for CUDA Graph

source: https://github.com/deepseek-ai/DeepGEMM/issues/235
state: open | updated: 2025-12-08T11:51:44Z
labels: 

## 正文

Hi DeepSeek team,

I noticed that DeepEP provides an optional `num_worst_tokens` argument for CUDA Graph usage. Based on that, I assume contiguous Grouped GEMM is also intended to support CUDA Graph. However, it seems there is no input parameter to supply a valid m for the actual workload. While we can set `m_indices` to -1 for padded tokens, performance degrades significantly because `is_computation_valid` only skips the compute blocks, whereas the TMA loads are still issued for those padded regions.

Did I misunderstand something here, or is there a plan to address this limitation?

Thanks!

## 评论 (2)

### LyricZhao · 2025-12-05

`num_worst_tokens` is supported by the community (maybe with their own GEMM kernels). In DeepSeek, we never use `num_worst_tokens` (prefill without CUDA graph).

We are releasing EPv2 soon, normal/low-latency layout will be merged into a single contiguous layout then. DeepGEMM will also provide the masked/non-masked API.

### yuhyao · 2025-12-08

> `num_worst_tokens` is supported by the community (maybe with their own GEMM kernels). In DeepSeek, we never use `num_worst_tokens` (prefill without CUDA graph).
> 
> We are releasing EPv2 soon, normal/low-latency layout will be merged into a single contiguous layout then. DeepGEMM will also provide the masked/non-masked API.

Thanks for the reply. It’s exciting to hear that DeepEP v2 is coming soon!
Please allow me to double-check my understanding: the low-latency mode in DeepEP v2 will also use contiguous layout, so that the input and output buffers for grouped GEMM consumes less memory compared to the current low-latency layout when number of experts per rank is larger than `num_experts_per_tok`?
