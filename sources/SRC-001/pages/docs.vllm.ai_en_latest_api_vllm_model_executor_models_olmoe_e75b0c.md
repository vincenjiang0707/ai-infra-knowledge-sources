source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/olmoe/
lastmod: 2026-09-24

class OlmoeMoE(nn.Module):
"""A tensor-parallel MoE implementation for Olmoe that shards each expert
across all ranks.
Each expert's weights are sharded across all ranks and a fused MoE
kernel is used for the forward pass, and finally we reduce the outputs
across ranks.
"""
def __init__(
self,
num_experts: int,
top_k: int,
hidden_size: int,
intermediate_size: int,
params_dtype: torch.dtype | None = None,
quant_config: QuantizationConfig | None = None,
tp_size: int | None = None,
prefix: str = "",
):
super().__init__()
self.hidden_size = hidden_size
# Gate always runs at half / full precision for now.
self.gate = GateLinear(
hidden_size,
num_experts,
prefix=f"{prefix}.gate",
)
self.experts = FusedMoEFactory(
num_experts=num_experts,
top_k=top_k,
hidden_size=hidden_size,
intermediate_size=intermediate_size,
renormalize=False,
quant_config=quant_config,
tp_size=tp_size,
prefix=f"{prefix}.experts",
)
def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
# NOTE: hidden_states can have either 1D or 2D shape.
orig_shape = hidden_states.shape
hidden_dim = hidden_states.shape[-1]
hidden_states = hidden_states.view(-1, hidden_dim)
# router_logits: (num_tokens, n_experts)
router_logits, _ = self.gate(hidden_states)
final_hidden_states = self.experts(
hidden_states=hidden_states, router_logits=router_logits
)
return final_hidden_states.view(orig_shape)