# [Issue #3236] [Feature] [Help Wanted] `sequential_targets_per_subgraph="auto"`

source: https://github.com/vllm-project/llm-compressor/issues/3236
state: open | updated: 2026-09-27T02:45:44Z
labels: enhancement, good follow-up issue, tracing

## 正文

## Problem Description

The sequential pipeline partitions a model into subgraphs according to `sequential_targets`, then onloads and calibrates one subgraph at a time. The `sequential_targets_per_subgraph` argument controls how many sequential targets are grouped into each subgraph. Larger values mean fewer subgraphs, fewer onload/offload round-trips, fewer cached intermediates, and faster end-to-end compression, at the cost of higher peak VRAM usage.

Currently, users have to choose this value by hand. In practice this means one of two outcomes:
1. Users leave it at the default of `1`, underutilizing their GPU and paying a significant runtime cost, especially on large-VRAM devices (H100/H200/B200) compressing small-to-medium models.
2. Users guess a larger value, hit an OOM partway through calibration (sometimes hours in), and retry with a smaller value.

The right value is almost entirely determined by information we already have at runtime: how much VRAM is available and how much memory each subgraph's weights take up. The goal of this issue is to support `sequential_targets_per_subgraph="auto"`, which chooses the grouping automatically.

```python
oneshot(
    model=model,
    recipe=recipe,
    dataset=dataset,
    sequential_targets_per_subgraph="auto",
)
```

## Considerations

### Subgraphs are not uniform

A single integer applied to every subgraph is not sufficient, because subgraphs can differ significantly in size:

* **Embeddings and LM head.** Depending on the model and tracing, `embed_tokens` and `lm_head` may be folded into the first/last subgraph or split into their own. For models with large vocabularies, these can be larger than an entire decoder layer. Tied embeddings should also only be counted once.
* **Fine-grained MoE targets.** When sequential targets are set to e.g. attention + individual experts, subgraphs alternate between one relatively large attention block and many small expert MLPs. The ideal grouping packs many experts together while keeping attention blocks in smaller groups.
* **Mixed dense/MoE architectures.** Some models (e.g. DeepSeek-style) have several dense layers before switching to MoE layers, so per-layer sizes change partway through the model.

This means "auto" should produce a *variable* grouping (a list of group sizes, or equivalently a list of target boundaries), not a single integer.

### Subgraph grouping likely has to happen occur tracing

The memory footprint of a subgraph is not just the sum of its target modules' parameters. Non-target modules (embeddings, final norms, LM head, rotary embeddings, etc.) get assigned to whichever partition the graph topology places them in, and we only know that assignment after the graph has been traced and partitioned. So the approach is likely:

1. Trace and partition with one target per subgraph (the finest granularity)
2. Measure the weight memory of each fine-grained subgraph
3. Greedily merge *consecutive* subgraphs until the next merge would exceed the budget

Since subgraphs must execute in order, merging is constrained to contiguous runs. With that constraint, a greedy left-to-right pack is optimal for minimizing the number of subgraphs.

Note that tracing is the expensive step; partitioning an already-traced graph is cheap. So the second partitioning pass (with the computed grouping) should reuse the traced graph rather than retracing.

### Memory budget is not just weights

Weight memory is the dominant term but not the only one. The budget should reserve headroom for:

* Calibration activations and cached intermediates for the current batch
* Modifier state, which can be substantial. For example, GPTQ accumulates a Hessian of size `in_features x in_features` (fp32) for every targeted Linear in the subgraph, which for large MLPs can rival the weights themselves
* Allocator fragmentation / general safety margin

A reasonable starting point is to compute `budget = free_vram * fraction` with a conservative default fraction, and optionally let modifiers report an estimate of their per-module state (e.g. `GPTQModifier` can compute Hessian sizes up front from module shapes).

## Suggested Test Cases ##
* Model with decoder targets
* Model with attention + expert targets
* DDP test with two GPUs
* Tests with higher levels of activation batching which restricts the number of targets that can group into a subgraph

## 评论 (1)

### satyamg1620 · 2026-09-27

@kylesayrs Can you please assign this issue to me
