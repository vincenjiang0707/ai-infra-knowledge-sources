source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/utility/
lastmod: 2026-09-24

#

`vllm.compilation.passes.utility`

[¶](https://docs.vllm.ai#vllm.compilation.passes.utility)

Modules:

-
–[fix_functionalization](https://docs.vllm.ai/fix_functionalization/#vllm.compilation.passes.utility.fix_functionalization) -
–[noop_elimination](https://docs.vllm.ai/noop_elimination/#vllm.compilation.passes.utility.noop_elimination) -
–[post_cleanup](https://docs.vllm.ai/post_cleanup/#vllm.compilation.passes.utility.post_cleanup) -
–[scatter_split_replace](https://docs.vllm.ai/scatter_split_replace/#vllm.compilation.passes.utility.scatter_split_replace)Replace

`slice_scatter`

and`split_with_sizes`

nodes with a single -
–[split_coalescing](https://docs.vllm.ai/split_coalescing/#vllm.compilation.passes.utility.split_coalescing)Coalesce duplicate

`split_with_sizes`

nodes that operate on the same