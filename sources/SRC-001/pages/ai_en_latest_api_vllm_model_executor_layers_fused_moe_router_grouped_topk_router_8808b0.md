source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/grouped_topk_router/
lastmod: 2026-09-23

class GroupedTopKRouter(BaseRouter):
"""Router using grouped top-k routing (e.g., DeepSeekV2/V3)."""
def __init__(
self,
top_k: int,
global_num_experts: int,
num_expert_group: int,
topk_group: int,
renormalize: bool = True,
scoring_func: str = "softmax",
routed_scaling_factor: float = 1.0,
e_score_correction_bias: torch.Tensor | None = None,
num_fused_shared_experts: int = 0,
eplb_state: EplbLayerState | None = None,
skip_padding: bool = False,
):
super().__init__(
top_k=top_k,
global_num_experts=global_num_experts,
eplb_state=eplb_state,
)
self.num_expert_group = num_expert_group
self.topk_group = topk_group
self.renormalize = renormalize
self.scoring_func = scoring_func
self.routed_scaling_factor = routed_scaling_factor
self.e_score_correction_bias = e_score_correction_bias
self.num_fused_shared_experts = num_fused_shared_experts
self.skip_padding = skip_padding
@property
def routing_method_type(self) -> RoutingMethodType:
return get_routing_method_type(
scoring_func=self.scoring_func,
top_k=self.top_k,
renormalize=self.renormalize,
num_expert_group=self.num_expert_group,
has_e_score_bias=self.e_score_correction_bias is not None,
routed_scaling_factor=self.routed_scaling_factor,
)
def _compute_routing(
self,
hidden_states: torch.Tensor,
router_logits: torch.Tensor,
indices_type: torch.dtype | None,
*,
input_ids: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Compute routing using grouped top-k."""
def valid_grouping() -> bool:
# Check if num_experts is greater than num_expert_group
# and is divisible by num_expert_group
num_experts = router_logits.shape[-1]
if num_experts <= self.num_expert_group:
return False
return num_experts % self.num_expert_group == 0
if not valid_grouping():
if self.e_score_correction_bias is not None:
topk_weights, topk_ids = fused_topk_bias(
hidden_states=hidden_states,
gating_output=router_logits,
scoring_func=self.scoring_func,
e_score_correction_bias=self.e_score_correction_bias.data,
topk=self.top_k,
renormalize=self.renormalize,
)
if self.routed_scaling_factor != 1.0:
topk_weights *= self.routed_scaling_factor
else:
topk_weights, topk_ids, token_expert_indices = fused_topk(
hidden_states=hidden_states,
gating_output=router_logits,
topk=self.top_k,
renormalize=self.renormalize,
indices_type=indices_type,
)
return topk_weights, topk_ids
# Select grouped_topk implementation
if rocm_aiter_ops.is_fused_moe_enabled():
if not rocm_aiter_ops.is_fusion_moe_shared_experts_enabled():
assert self.num_fused_shared_experts == 0
grouped_topk_impl = partial(
rocm_aiter_grouped_topk,
num_fused_shared_experts=self.num_fused_shared_experts,
)
else:
grouped_topk_impl = grouped_topk
topk_weights, topk_ids = grouped_topk_impl(
hidden_states=hidden_states,
gating_output=router_logits,
topk=self.top_k,
renormalize=self.renormalize,
num_expert_group=self.num_expert_group,
topk_group=self.topk_group,
scoring_func=self.scoring_func,
routed_scaling_factor=self.routed_scaling_factor,
e_score_correction_bias=self.e_score_correction_bias,
)
if (
self.skip_padding
and envs.VLLM_MOE_SKIP_PADDING
and is_forward_context_available()
):
is_padding = get_forward_context().is_padding
if is_padding is not None:
is_padding = is_padding[: topk_ids.shape[0]].unsqueeze(1)
topk_weights = topk_weights.masked_fill(is_padding, 0)
topk_ids = topk_ids.masked_fill(is_padding, -1)
return topk_weights, topk_ids