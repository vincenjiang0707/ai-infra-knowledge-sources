source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mixtral/
lastmod: 2026-09-23

class MixtralMoE(nn.Module):
"""A tensor-parallel MoE implementation for Mixtral that shards each expert
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
dp_size: int | None = None,
prefix: str = "",
enable_eplb: bool = False,
):
super().__init__()
self.hidden_size = hidden_size
self.ep_group = get_ep_group().device_group
self.ep_size = self.ep_group.size()
# Expert Parallelism Load balancing settings.
vllm_config = get_current_vllm_config()
parallel_config = vllm_config.parallel_config
self.enable_eplb = enable_eplb
self.n_routed_experts = num_experts
self.n_logical_experts = num_experts
self.n_redundant_experts = parallel_config.eplb_config.num_redundant_experts
self.n_physical_experts = self.n_logical_experts + self.n_redundant_experts
self.n_local_physical_experts = self.n_physical_experts // self.ep_size
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
dp_size=dp_size,
prefix=f"{prefix}.experts",
enable_eplb=self.enable_eplb,
num_redundant_experts=self.n_redundant_experts,
ckpt_names=("w1", "w2", "w3"),
)
def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
# NOTE: hidden_states can have either 1D or 2D shape.
orig_shape = hidden_states.shape
hidden_states = hidden_states.view(-1, self.hidden_size)
# router_logits: (num_tokens, n_experts)
router_logits, _ = self.gate(hidden_states)
final_hidden_states = self.experts(hidden_states, router_logits)
return final_hidden_states.view(orig_shape)