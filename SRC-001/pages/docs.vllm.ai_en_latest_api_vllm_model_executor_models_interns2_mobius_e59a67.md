source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interns2_mobius/
lastmod: 2026-09-23

class InternS2MobiusMetaMoeBlock(nn.Module):
"""A routed MoE bank shared by multiple decoder layers."""
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
config = vllm_config.model_config.hf_text_config
parallel_config = vllm_config.parallel_config
self.tp_size = get_tensor_model_parallel_world_size()
self.ep_group = get_ep_group().device_group
self.ep_rank = get_ep_group().rank_in_group
self.ep_size = self.ep_group.size()
self.n_routed_experts = config.num_experts
self.is_sequence_parallel = parallel_config.use_sequence_parallel_moe
if self.tp_size > self.n_routed_experts:
raise ValueError(
f"Tensor parallel size {self.tp_size} is greater than "
f"the number of experts {self.n_routed_experts}."
)
eplb_config = parallel_config.eplb_config
self.enable_eplb = parallel_config.enable_eplb
self.n_logical_experts = self.n_routed_experts
self.n_redundant_experts = eplb_config.num_redundant_experts
self.n_physical_experts = self.n_logical_experts + self.n_redundant_experts
self.n_local_physical_experts = self.n_physical_experts // self.ep_size
self.gate = ReplicatedLinear(
config.hidden_size,
config.num_experts,
bias=False,
quant_config=None,
prefix=f"{prefix}.gate",
)
self.experts = FusedMoEFactory(
gate=self.gate,
num_experts=config.num_experts,
top_k=config.num_experts_per_tok,
hidden_size=config.hidden_size,
intermediate_size=config.moe_intermediate_size,
renormalize=getattr(config, "norm_topk_prob", True),
quant_config=vllm_config.quant_config,
prefix=f"{prefix}.experts",
enable_eplb=self.enable_eplb,
num_redundant_experts=self.n_redundant_experts,
is_sequence_parallel=self.is_sequence_parallel,
activation=config.hidden_act,
)
def forward(
self,
hidden_states: torch.Tensor,
already_sequence_parallel: bool = False,
) -> torch.Tensor:
orig_shape = hidden_states.shape
num_tokens, hidden_dim = hidden_states.shape
hidden_states = hidden_states.view(-1, hidden_dim)
if self.is_sequence_parallel and not already_sequence_parallel:
hidden_states = sequence_parallel_chunk(hidden_states)
final_hidden_states = self.experts(
hidden_states=hidden_states,
router_logits=hidden_states,
)
if self.is_sequence_parallel and not already_sequence_parallel:
final_hidden_states = tensor_model_parallel_all_gather(
final_hidden_states, 0
)
final_hidden_states = final_hidden_states[:num_tokens]
return final_hidden_states.view(orig_shape)