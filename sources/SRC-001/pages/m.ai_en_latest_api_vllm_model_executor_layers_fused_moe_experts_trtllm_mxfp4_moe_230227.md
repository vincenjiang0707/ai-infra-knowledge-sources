source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe/
lastmod: 2026-09-24

class TrtLlmMxfp4ExpertsModular(TrtLlmMxfp4ExpertsBase, mk.FusedMoEExpertsModular):
"""Modular version of the MXFP4 TRTLLM kernel (just the experts).
Wraps flashinfer.trtllm_fp4_block_scale_routed_moe().
Moved from trtllm_moe.py.
"""
@staticmethod
def _supports_parallel_config(
moe_parallel_config: FusedMoEParallelConfig,
) -> bool:
return True
@staticmethod
def _supports_routing_method(
routing_method: RoutingMethodType,
weight_key: QuantKey | None,
activation_key: QuantKey | None,
) -> bool:
# Modular kernel handles only the expert computation;
# routing is done externally, so accept any routing method.
return True
def finalize_weight_and_reduce_impl(self) -> mk.TopKWeightAndReduce:
return TopKWeightAndReduceNoOP()
def workspace_shapes(
self,
M: int,
N: int,
K: int,
topk: int,
global_num_experts: int,
local_num_experts: int,
expert_tokens_meta: mk.ExpertTokensMetadata | None,
activation: MoEActivation,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
# The workspaces for this implementation are managed by flashinfer.
workspace1 = (0,)
workspace2 = (0,)
output = (M, self.hidden_dim_unpadded)
return (workspace1, workspace2, output)
def _max_supported_tokens(self, top_k: int, global_num_experts: int) -> int:
"""Max tokens per kernel call before the batched-GEMM grid overflows.
The TRTLLM-Gen batched GEMM launches a static grid whose batch (Y)
dimension is ``getMaxNumCtasInBatchDim(num_tokens, top_k, num_experts,
tileTokensDim)`` and must stay <= 65535. Solving that for num_tokens
with the smallest tile the kernel may pick (tileTokensDim=8, the runner
default) gives a bound that is safe regardless of the tactic selected.
Without it, large batches (e.g. Kimi-K3 top_k=16, EP16 profiling with
131072 gathered tokens) overflow the grid and the GEMM launch fails.
"""
MAX_GRID_Y = 65535
MIN_TILE_TOKENS_DIM = 8
max_tokens = (MAX_GRID_Y - global_num_experts) * MIN_TILE_TOKENS_DIM // top_k
return max(1, min(300000, max_tokens))
def _invoke_kernel(
self,
output: torch.Tensor,
x_quant: torch.Tensor,
x_scale: torch.Tensor | None,
topk_ids: torch.Tensor,
topk_weights: torch.Tensor,
w1: torch.Tensor,
w2: torch.Tensor,
activation: MoEActivation,
global_num_experts: int,
local_num_experts: int,
local_expert_offset: int,
topk: int,
) -> None:
from flashinfer import trtllm_fp4_block_scale_routed_moe
trtllm_fp4_block_scale_routed_moe(
topk_ids=(topk_ids, topk_weights),
routing_bias=None,
hidden_states=x_quant,
hidden_states_scale=x_scale,
gemm1_weights=w1,
gemm1_weights_scale=self.w1_scale,
gemm1_bias=self.w1_bias,
gemm1_alpha=self.gemm1_alpha,
gemm1_beta=self.gemm1_beta,
gemm1_clamp_limit=self.gemm1_clamp_limit,
gemm2_weights=w2,
gemm2_weights_scale=self.w2_scale,
gemm2_bias=self.w2_bias,
output1_scale_scalar=None,
output1_scale_gate_scalar=None,
output2_scale_scalar=None,
num_experts=global_num_experts,
top_k=topk,
n_group=None,
topk_group=None,
intermediate_size=self.intermediate_size_per_partition,
local_expert_offset=local_expert_offset,
local_num_experts=local_num_experts,
routed_scaling_factor=None,
# Modular kernel receives pre-routed tokens, so routing is already
# done. Use Renormalize as a safe default the TRTLLM kernel supports.
routing_method_type=RoutingMethodType.Renormalize,
do_finalize=True,
enable_pdl=True,
activation_type=self._flashinfer_activation_type(activation),
output=output,
tune_max_num_tokens=fi_moe_largest_bucket(self.moe_config),
)
def apply(
self,
output: torch.Tensor,
hidden_states: torch.Tensor,
w1: torch.Tensor,
w2: torch.Tensor,
topk_weights: torch.Tensor,
topk_ids: torch.Tensor,
activation: MoEActivation,
global_num_experts: int,
expert_map: torch.Tensor | None,
a1q_scale: torch.Tensor | None,
a2_scale: torch.Tensor | None,
workspace13: torch.Tensor,
workspace2: torch.Tensor,
expert_tokens_meta: mk.ExpertTokensMetadata | None,
apply_router_weight_on_input: bool,
):
topk_ids = topk_ids.to(dtype=torch.int32)
topk = topk_ids.size(-1)
local_num_experts = w1.size(0)
local_expert_offset = self.moe_config.ep_rank * local_num_experts
if a1q_scale is not None:
x_quant = hidden_states
x_scale = a1q_scale.view(torch.float8_e4m3fn)
else:
assert hidden_states.dtype == torch.bfloat16
x_quant = hidden_states
x_scale = None
assert self.w1_scale is not None
assert self.w2_scale is not None
# Chunk tokens so the batched-GEMM grid stays within CUDA limits.
M = x_quant.size(0)
chunk_size = self._max_supported_tokens(topk, global_num_experts)
for start in range(0, M, chunk_size):
end = min(start + chunk_size, M)
self._invoke_kernel(
output[start:end],
x_quant[start:end],
None if x_scale is None else x_scale[start:end],
topk_ids[start:end],
topk_weights[start:end],
w1,
w2,
activation,
global_num_experts,
local_num_experts,
local_expert_offset,
topk,
)
return output