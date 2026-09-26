source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/moonep_experts/
lastmod: 2026-09-24

class MoonEPExperts(mk.FusedMoEExpertsModular):
"""Grouped-GEMM experts over MoonEP's ``[NvS, H]`` layout (BF16)."""
def __init__(
self,
moe_config: FusedMoEConfig,
quant_config: FusedMoEQuantConfig,
max_num_tokens: int | None = None,
num_dispatchers: int | None = None,
):
super().__init__(moe_config, quant_config, max_num_tokens, num_dispatchers)
assert quant_config.quant_dtype is None, (
"MoonEPExperts supports unquantized BF16 only"
)
if (
quant_config.gemm1_alpha is not None
or quant_config.gemm1_beta is not None
or quant_config.gemm1_clamp_limit is not None
):
raise NotImplementedError(
"MoonEPExperts implements plain silu(gate) * up only; SwiGLU "
"variants with alpha/beta/clamp parameters are not supported"
)
self._weight_layout = None
def process_weights_after_loading(self, layer: torch.nn.Module) -> None:
# The [E+B] gate/up/down layout built by
# convert_to_unquantized_kernel_format; MoonEPPrepareAndFinalize
# reads it from here (post_init_setup) for weight prefetch.
layout = getattr(layer, "_moonep_weight_layout", None)
assert layout is not None, (
"MoonEPExperts requires the layer to carry _moonep_weight_layout "
"(set by convert_to_unquantized_kernel_format)"
)
self._weight_layout = layout
@property
def weight_layout(self):
return self._weight_layout
@staticmethod
def activation_format() -> mk.FusedMoEActivationFormat:
return mk.FusedMoEActivationFormat.Standard
@staticmethod
def _supports_current_device() -> bool:
return current_platform.is_cuda()
@staticmethod
def _supports_no_act_and_mul() -> bool:
return False
@staticmethod
def _supports_activation(activation: MoEActivation) -> bool:
return activation == MoEActivation.SILU
@staticmethod
def _supports_parallel_config(moe_parallel_config: FusedMoEParallelConfig) -> bool:
# EPLB rearranges the named expert parameters as local_num_experts
# rows, which does not understand the replicated [E+B] layout.
return (
moe_parallel_config.use_moonep_kernels
and not moe_parallel_config.enable_eplb
)
@staticmethod
def _supports_quant_scheme(
weight_key: QuantKey | None,
activation_key: QuantKey | None,
) -> bool:
return weight_key is None and activation_key is None
def supports_chunking(self) -> bool:
# NvS is static and segments must stay whole.
return False
def supports_expert_map(self) -> bool:
# MoonEP addresses global expert rows directly.
return False
def finalize_weight_and_reduce_impl(self) -> mk.TopKWeightAndReduce:
return TopKWeightAndReduceNoOP()
def moe_problem_size(
self,
a1: torch.Tensor,
w1: torch.Tensor,
w2: torch.Tensor,
topk_ids: torch.Tensor,
) -> tuple[int, int, int, int, int]:
# a1 is [NvS, H] in segment order, not token-major, so the base
# implementation's topk_ids/a1 row-count check does not apply.
assert a1.dim() == 2 and w1.dim() == 3 and w2.dim() == 3
num_rows, intermediate, hidden = w1.shape # [E+B, I, H]
assert a1.size(1) == hidden
return num_rows, a1.size(0), intermediate, hidden, topk_ids.size(1)
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
# M is NvS. torch._grouped_mm allocates its own outputs, so no
# workspaces are needed.
return ((0,), (0,), (M, K))
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
) -> None:
# expert_map is ignored: MoonEP dispatches on global expert ids and
# the weights are addressed by global [E+B] row, on every rank.
assert activation == MoEActivation.SILU
assert self._weight_layout is not None, (
"process_weights_after_loading() not called"
)
assert expert_tokens_meta is not None
# MoonEPPrepareAndFinalize returns route weights in NvS order as the
# dispatched topk_weights, and per-row segment lengths as
# expert_tokens_meta.
route_weights_nvs = topk_weights
assert route_weights_nvs.dim() == 1
cu_seqlens = torch.cumsum(
expert_tokens_meta.expert_num_tokens, dim=0, dtype=torch.int32
)
assert cu_seqlens.numel() == w1.size(0)
gate = moonep_grouped_gemm(hidden_states, w1, cu_seqlens)
up = moonep_grouped_gemm(
hidden_states, self._weight_layout.full_up_weight, cu_seqlens
)
act = torch.nn.functional.silu(gate)
act.mul_(up)
if not apply_router_weight_on_input:
# Input-weighted routing (top-1, e.g. Llama 4) was already
# applied to the activations by prepare(), before dispatch.
act.mul_(route_weights_nvs.to(act.dtype).unsqueeze(-1))
# Padding rows past the last segment come out zero-filled.
output.copy_(moonep_grouped_gemm(act, w2, cu_seqlens))