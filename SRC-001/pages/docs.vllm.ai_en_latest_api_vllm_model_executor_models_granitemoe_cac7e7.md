source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/granitemoe/
lastmod: 2026-09-23

class GraniteMoeMoE(nn.Module):
"""A tensor-parallel MoE implementation for GraniteMoe that shards each
expert across all ranks.
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
is_sequence_parallel=False,
prefix: str = "",
):
super().__init__()
self.hidden_size = hidden_size
self.is_sequence_parallel = is_sequence_parallel
# Gate always runs at half / full precision for now.
self.gate = ReplicatedLinear(
hidden_size,
num_experts,
bias=False,
params_dtype=params_dtype,
quant_config=None,
prefix=f"{prefix}.gate",
)
self.experts = FusedMoEFactory(
num_experts=num_experts,
top_k=top_k,
hidden_size=hidden_size,
intermediate_size=intermediate_size,
params_dtype=params_dtype,
renormalize=True,
quant_config=quant_config,
tp_size=tp_size,
prefix=f"{prefix}.experts",
is_sequence_parallel=self.is_sequence_parallel,
)
def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
# NOTE: hidden_states can have either 1D or 2D shape.
orig_shape = hidden_states.shape
hidden_states = hidden_states.view(-1, self.hidden_size)
if self.is_sequence_parallel:
hidden_states = sequence_parallel_chunk(hidden_states)
# router_logits: (num_tokens, n_experts)
router_logits, _ = self.gate(hidden_states)
final_hidden_states = self.experts(hidden_states, router_logits)
if self.is_sequence_parallel:
final_hidden_states = tensor_model_parallel_all_gather(
final_hidden_states, 0
)
num_tokens = orig_shape[0]
final_hidden_states = final_hidden_states[:num_tokens]
return final_hidden_states.view(orig_shape)