source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/dbrx/
lastmod: 2026-09-24

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)


A tensor-parallel MoE implementation for DBRX.

Each expert's weights are sharded across all ranks and a fused MoE kernel is used for the forward pass, and finally we reduce the outputs across ranks.

## Source code in `vllm/model_executor/models/dbrx.py`


| class DbrxMoE(nn.Module):
"""A tensor-parallel MoE implementation for DBRX.
Each expert's weights are sharded across all ranks and a fused MoE
kernel is used for the forward pass, and finally we reduce the outputs
across ranks.
"""
def __init__(
self,
config: DbrxConfig,
quant_config: QuantizationConfig | None = None,
params_dtype: torch.dtype | None = None,
prefix: str = "",
):
super().__init__()
self.d_model = config.d_model
if params_dtype is None:
params_dtype = torch.get_default_dtype()
self.params_dtype = params_dtype
self.router = DbrxRouter(config, self.params_dtype)
self.experts = FusedMoEFactory(
num_experts=config.ffn_config.moe_num_experts,
top_k=config.ffn_config.moe_top_k,
hidden_size=config.d_model,
intermediate_size=config.ffn_config.ffn_hidden_size,
params_dtype=self.params_dtype,
renormalize=True,
quant_config=quant_config,
tp_size=get_tensor_model_parallel_world_size(),
prefix=prefix,
routed_experts_cls=DbrxExperts,
routed_experts_args={"config": config},
)
def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
orig_shape = hidden_states.shape
hidden_states = hidden_states.view(-1, self.d_model)
# router_logits: (num_tokens, n_experts)
router_logits = self.router(hidden_states)
final_hidden_states = self.experts(hidden_states, router_logits)
return final_hidden_states.view(orig_shape)
|