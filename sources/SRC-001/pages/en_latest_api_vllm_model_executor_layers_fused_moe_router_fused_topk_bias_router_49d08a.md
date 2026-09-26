source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router/
lastmod: 2026-09-24

class FusedTopKBiasRouter(BaseRouter):
"""Router using fused top-k with e_score_correction_bias."""
def __init__(
self,
top_k: int,
global_num_experts: int,
e_score_correction_bias: torch.Tensor | None = None,
renormalize: bool = True,
routed_scaling_factor: float = 1.0,
eplb_state: EplbLayerState | None = None,
*,
scoring_func: str = "sigmoid",
hash_indices_table: torch.Tensor | None = None,
num_fused_shared_experts: int = 0,
shared_expert_weight: float = 1.0,
bias_vl: torch.Tensor | None = None,
image_sentinel_lo: int = 0,
):
super().__init__(
top_k=top_k,
global_num_experts=global_num_experts,
eplb_state=eplb_state,
)
self.e_score_correction_bias = e_score_correction_bias
self.renormalize = renormalize
self.scoring_func = scoring_func
self.routed_scaling_factor = routed_scaling_factor
self.scoring_func = scoring_func
self._hash_indices_table = hash_indices_table
# Vision bias: image sentinel tokens (five consecutive in-vocab ids
# starting at image_sentinel_lo) select experts with bias_vl instead
# of e_score_correction_bias / the hash table.
self.bias_vl = bias_vl
self.image_sentinel_lo = image_sentinel_lo
# Fused shared experts: append constant slots (ids immediately after
# the routed experts, [global, global+n)) routed to by every token at
# ``shared_expert_weight``, AFTER the routed top-k is renormalized.
self.num_fused_shared_experts = num_fused_shared_experts
self.shared_expert_weight = shared_expert_weight
@property
def routing_method_type(self) -> RoutingMethodType:
return get_routing_method_type(
scoring_func=self.scoring_func,
top_k=self.top_k,
renormalize=self.renormalize,
num_expert_group=None,
has_e_score_bias=True,
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
"""Compute routing using fused top-k with bias."""
topk_weights, topk_ids = fused_topk_bias(
hidden_states=hidden_states,
gating_output=router_logits,
scoring_func=self.scoring_func,
e_score_correction_bias=self.e_score_correction_bias.data
if self.e_score_correction_bias is not None
else None,
topk=self.top_k,
renormalize=self.renormalize,
indices_type=indices_type,
input_tokens=input_ids,
hash_indices_table=self._hash_indices_table,
routed_scaling_factor=self.routed_scaling_factor,
bias_vl=self.bias_vl.data if self.bias_vl is not None else None,
image_sentinel_lo=self.image_sentinel_lo,
)
if self.num_fused_shared_experts > 0:
m = topk_ids.shape[0]
n = self.num_fused_shared_experts
# global_num_experts counts only the routed experts; the fused
# shared experts occupy the slots immediately after them, i.e. ids
# [global_num_experts, global_num_experts + n).
base = self.global_num_experts
shared_ids = torch.arange(
base, base + n, dtype=topk_ids.dtype, device=topk_ids.device
).expand(m, n)
shared_w = torch.full(
(m, n),
self.shared_expert_weight,
dtype=topk_weights.dtype,
device=topk_weights.device,
)
topk_ids = torch.cat([topk_ids, shared_ids], dim=-1)
topk_weights = torch.cat([topk_weights, shared_w], dim=-1)
return topk_weights, topk_ids