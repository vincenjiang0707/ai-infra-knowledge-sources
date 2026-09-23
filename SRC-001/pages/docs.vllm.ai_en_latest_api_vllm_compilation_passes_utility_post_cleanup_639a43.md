source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/utility/post_cleanup/
lastmod: 2026-09-23

#

`vllm.compilation.passes.utility.post_cleanup`

[¶](https://docs.vllm.ai#vllm.compilation.passes.utility.post_cleanup)

Classes:

-
–[PostCleanupPass](https://docs.vllm.ai#vllm.compilation.passes.utility.post_cleanup.PostCleanupPass)This pass performs cleanup after custom passes.


##

`PostCleanupPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.utility.post_cleanup.PostCleanupPass)

Bases: [VllmInductorPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass)

This pass performs cleanup after custom passes. It topologically sorts the graph and removes unused nodes. This is needed because the pattern matcher does not guarantee producing a topologically sorted graph, and there may be unused nodes left around.