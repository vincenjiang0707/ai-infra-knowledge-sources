# [Issue #2981] [Performance] Speed up subgraph tracing for large models

source: https://github.com/vllm-project/llm-compressor/issues/2981
state: closed | updated: 2026-09-09T16:00:47Z
labels: enhancement, good first issue, tracing

## 正文

## Background ##
LLM Compressor uses [Sequential Onloading](https://docs.vllm.ai/projects/llm-compressor/en/latest/guides/big_models_and_distributed/sequential_onloading/#implementation) to avoid loading the entire model into GPU memory. This relies on [`trace_subgraphs`](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/pipelines/sequential/helpers.py#L84) which performs a virtual pass through the model to create a graph which is later partitioned into subgraphs

This process can take upwards of 10min for very large models like `moonshotai/Kimi-K3`

## Proposed Changes ##
Because of the complexity of the tracing and partitioning logic within LLM Compressor, this issue only focuses on small diff + high impact changes which can reduce this runtime.

A few places I've noticed already are:
1. Changing [`partitions`](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/pipelines/sequential/helpers.py#L339C36-L339C46) into a set, not a list for O(1) lookup
2. Changing [this code](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/pipelines/sequential/transformers_helpers.py#L1356-L1368) to cache an inverse dict of params and buffers, rather than iterating through params and buffers each time, leading to O(N^2) runtime for parameter proxy making

**PRs which fundamentally refactor subgraph/ tracing logic will not be accepted**. Only well thought-out improvements from DSA principles will be accepted (thank you!).

Please include a benchmark script on a dummy model, see [`test_models`](https://github.com/vllm-project/llm-compressor/blob/main/tests/llmcompressor/transformers/tracing/test_models.py) for regression testing.

Ping @kylesayrs for any follow up questions

## 评论 (4)

### wanadzhar913 · 2026-07-30

Hi @kylesayrs, would love to help with this. Can I take No. 1?

For benchmarking scripts, what metrics would you be keen to look at? I presume Sequential Onloading wall time is the most important metric?

### kylesayrs · 2026-07-30

@wanadzhar913 Sounds good! I'll assign this ticket to you, while leaving 2 (and extras) open.

W.r.t. benchmarking, the goal is to see runtime improvements on a trace_subgraphs task with around the magnitude of 100K matched sequential targets.

This is relevant to the Kimi-K3 model, but you can create a dummy model to trace and put the benchmark results in the benchmarks folder.

### YingqiDuan · 2026-07-30

Hi @kylesayrs, I'd like to work on No. 2. 

I also notice an extra [trace_consumed_names](https://github.com/vllm-project/llm-compressor/blob/8cec0acc1931de6f8f73257151ab7007c14dbf4e/src/llmcompressor/pipelines/sequential/helpers.py#L398-L414). My plan is to make a single reverse pass, using a set to track the names already seen.

### kylesayrs · 2026-07-30

@YingqiDuan That would be great, thanks!
