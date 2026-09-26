source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/utility/split_coalescing/
lastmod: 2026-09-24

#

`vllm.compilation.passes.utility.split_coalescing`

[¶](https://docs.vllm.ai#vllm.compilation.passes.utility.split_coalescing)

Coalesce duplicate `split_with_sizes`

nodes that operate on the same input tensor with the same split sizes.

On certain hardware/dtype combinations (e.g. B200 + FP8) the Inductor graph may contain multiple `split_with_sizes`

calls on the same tensor that CSE fails to merge. This pass detects and replaces the duplicates so that downstream pattern-matching passes (e.g. QK-Norm+RoPE fusion) see a single split node with all users attached.

## See Also

- vLLM #33295 (original issue)
- PyTorch #174472 (upstream CSE gap)

Classes:

-
–[SplitCoalescingPass](https://docs.vllm.ai#vllm.compilation.passes.utility.split_coalescing.SplitCoalescingPass)Replace duplicate

`split_with_sizes`

nodes with a single canonical

##

`SplitCoalescingPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.utility.split_coalescing.SplitCoalescingPass)

Bases: [VllmInductorPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass)

Replace duplicate `split_with_sizes`

nodes with a single canonical node when they share the same input tensor and split sizes.