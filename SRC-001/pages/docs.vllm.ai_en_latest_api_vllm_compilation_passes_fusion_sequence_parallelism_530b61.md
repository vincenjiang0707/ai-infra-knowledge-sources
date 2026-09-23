source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/sequence_parallelism/
lastmod: 2026-09-23

Bases: [VllmPatternMatcherPass](../../vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass)


This pass enables sequence parallelism for models. It identifies patterns where an AllReduce operation is followed by an RMSNorm (or RMSNorm and then Quantization) operation. These patterns are replaced with a ReduceScatter operation, followed by a local RMSNorm/Quantization, and then an AllGather operation.

The general transformation is: Input -> AllReduce -> RMSNorm -> Output becomes Input -> ReduceScatter -> RMSNorm -> AllGather -> Output

While this pass itself does not directly yield performance improvements, it lays the groundwork for subsequent fusion passes, such as GEMM + ReduceScatter and AllGather + GEMM fusions. These fusions can significantly reduce communication overhead and improve overall model performance.

This pass is only supported when compiling the whole graph (fullgraph mode, i.e. using Inductor graph partition or empty splitting_ops). Piecewise compilation is not supported because the residual tensor gets split across TP ranks, causing size mismatches at subgraph boundaries.

This pass splits up the residual tensor across TP ranks and hence divides its size. The pattern matcher starts at the end of the graph (last layer first), so when each replacement inserts a residual slice, the preceding layer has not been replaced yet and the slice is correct. Once the preceding layer IS replaced, its residual output shrinks and the slice becomes semantically incorrect (out-of-bounds indices for rank > 0). The graph is never executed in this intermediate state — NoOpEliminationPass removes these slices based on symbolic shape equality (input shape == output shape) before the graph is compiled.

Methods:

## Source code in `vllm/compilation/passes/fusion/sequence_parallelism.py`


| class SequenceParallelismPass(VllmPatternMatcherPass):
"""This pass enables sequence parallelism for models.
It identifies patterns where an AllReduce operation is followed by
an RMSNorm (or RMSNorm and then Quantization) operation.
These patterns are replaced with a ReduceScatter operation, followed by
a local RMSNorm/Quantization, and then an AllGather operation.
The general transformation is:
Input -> AllReduce -> RMSNorm -> Output
becomes
Input -> ReduceScatter -> RMSNorm -> AllGather -> Output
While this pass itself does not directly yield performance improvements,
it lays the groundwork for subsequent fusion passes, such as
GEMM + ReduceScatter and AllGather + GEMM fusions. These fusions can
significantly reduce communication overhead and improve overall model
performance.
This pass is only supported when compiling the whole graph (fullgraph
mode, i.e. using Inductor graph partition or empty splitting_ops).
Piecewise compilation is not supported because the residual tensor
gets split across TP ranks, causing size mismatches at subgraph
boundaries.
This pass splits up the residual tensor across TP ranks and hence divides
its size. The pattern matcher starts at the end of the graph (last layer
first), so when each replacement inserts a residual slice, the preceding
layer has not been replaced yet and the slice is correct. Once the
preceding layer IS replaced, its residual output shrinks and the slice
becomes semantically incorrect (out-of-bounds indices for rank > 0).
The graph is never executed in this intermediate state —
NoOpEliminationPass removes these slices based on symbolic shape equality
(input shape == output shape) before the graph is compiled.
"""
@enable_fake_mode
def __init__(self, config: VllmConfig) -> None:
super().__init__(config)
# Get min_token_num threshold
# Read min_token_num from config (calculated during config init)
self.min_token_num = None
if config.model_config is not None:
pass_config = config.compilation_config.pass_config
self.min_token_num = pass_config.sp_min_token_num
if self.min_token_num is not None:
# Take the min to avoid exceeding max_num_batched_tokens
max_batched = config.scheduler_config.max_num_batched_tokens
if max_batched is not None:
self.min_token_num = min(self.min_token_num, max_batched)
logger.debug_once(
f"Sequence parallelism min token threshold: {self.min_token_num}",
scope="global",
)
# Used to clean up redundant views created temporarily
# to circumvent residual shape change issues
self.noop_cleanup = NoOpEliminationPass(config)
self.noop_cleanup.pass_name = f"{self.pass_name}.{self.noop_cleanup.pass_name}"
self.patterns: PatternMatcherPass = PatternMatcherPass(
pass_name="sequence_parallelism_pass"
)
for epsilon in [1e-5, 1e-6]:
# RMSNorm + Static FP8 quantization patterns
FirstAllReduceRMSNormStaticFP8Pattern(
epsilon, self.model_dtype, self.device
).register(self.patterns)
MiddleAllReduceRMSNormStaticFP8Pattern(
epsilon, self.model_dtype, self.device
).register(self.patterns)
if "SCALED_FP4_QUANT_OUT_OVERLOAD" in globals():
FirstAllReduceRMSNormStaticNVFP4Pattern(
epsilon, self.model_dtype, self.device
).register(self.patterns)
MiddleAllReduceRMSNormStaticNVFP4Pattern(
epsilon, self.model_dtype, self.device
).register(self.patterns)
# Normal RMSNorm patterns
FirstAllReduceRMSNormPattern(
epsilon, self.model_dtype, self.device
).register(self.patterns)
MiddleAllReduceRMSNormPattern(
epsilon, self.model_dtype, self.device
).register(self.patterns)
self.dump_patterns(config, self.patterns)
def is_applicable_for_range(self, compile_range: Range) -> bool:
"""Determines if sequence parallelism should be applied for the given
compile range.
SP is only beneficial for larger batch sizes where the communication
overhead is amortized. For small batches, the overhead of splitting
and gathering tensors across TP ranks outweighs the benefits.
Returns False (SP disabled) when:
- min_token_num is None (SP disabled for this device/config)
- The compile range starts below the minimum token threshold
"""
assert (
self.compilation_config.use_inductor_graph_partition
or not self.compilation_config.splitting_ops
), "SequenceParallelismPass requires full-graph compilation"
# min_token_num is None when SP is disabled for this device/config
# (e.g., non-CUDA platform, unsupported GPU, or small hidden_size)
if self.min_token_num is None:
return False
# Only apply SP when batch size meets the minimum threshold
return compile_range.start >= self.min_token_num
@VllmInductorPass.time_and_log
def __call__(self, graph: fx.Graph) -> None:
self.matched_count = self.patterns.apply(graph)
logger.debug("Replaced %s patterns", self.matched_count)
# Clean up reshape nodes
self.noop_cleanup(graph)
|

###

`is_applicable_for_range(compile_range)`


Determines if sequence parallelism should be applied for the given compile range.

SP is only beneficial for larger batch sizes where the communication overhead is amortized. For small batches, the overhead of splitting and gathering tensors across TP ranks outweighs the benefits.

Returns False (SP disabled) when: - min_token_num is None (SP disabled for this device/config) - The compile range starts below the minimum token threshold

## Source code in `vllm/compilation/passes/fusion/sequence_parallelism.py`


| def is_applicable_for_range(self, compile_range: Range) -> bool:
"""Determines if sequence parallelism should be applied for the given
compile range.
SP is only beneficial for larger batch sizes where the communication
overhead is amortized. For small batches, the overhead of splitting
and gathering tensors across TP ranks outweighs the benefits.
Returns False (SP disabled) when:
- min_token_num is None (SP disabled for this device/config)
- The compile range starts below the minimum token threshold
"""
assert (
self.compilation_config.use_inductor_graph_partition
or not self.compilation_config.splitting_ops
), "SequenceParallelismPass requires full-graph compilation"
# min_token_num is None when SP is disabled for this device/config
# (e.g., non-CUDA platform, unsupported GPU, or small hidden_size)
if self.min_token_num is None:
return False
# Only apply SP when batch size meets the minimum threshold
return compile_range.start >= self.min_token_num
|