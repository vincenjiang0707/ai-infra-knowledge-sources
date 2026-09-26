source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/gdn/base/
lastmod: 2026-09-24

Bases: [PluggableLayer](../../../../custom_op/#vllm.model_executor.custom_op.PluggableLayer)

, [MambaBase](../../abstract/#vllm.model_executor.layers.mamba.abstract.MambaBase)


Base class for GatedDeltaNet attention layer.

## Source code in `vllm/model_executor/layers/mamba/gdn/base.py`


| class GatedDeltaNetAttention(PluggableLayer, MambaBase):
"""Base class for GatedDeltaNet attention layer."""
def __init__(
self,
config: PreTrainedConfig,
vllm_config: VllmConfig,
prefix: str = "",
) -> None:
super().__init__()
self.prefix = prefix
self.tp_size = get_tensor_model_parallel_world_size()
self.tp_rank = get_tensor_model_parallel_rank()
self.layer_idx = extract_layer_index(prefix)
self.hidden_size = config.hidden_size
self.activation = config.hidden_act
self.layer_norm_epsilon = config.rms_norm_eps
self.model_config = vllm_config.model_config
self.cache_config = vllm_config.cache_config
self.quant_config = vllm_config.quant_config
self.speculative_config = vllm_config.speculative_config
self.num_spec = (
self.speculative_config.num_speculative_tokens
if self.speculative_config
else 0
)
@property
def mamba_type(self) -> MambaAttentionBackendEnum:
return MambaAttentionBackendEnum.GDN_ATTN
def get_state_dtype(self) -> tuple[torch.dtype, ...]:
return MambaStateDtypeCalculator.gated_delta_net_state_dtype(
self.model_config.dtype,
self.cache_config.mamba_cache_dtype,
self.cache_config.mamba_ssm_cache_dtype,
)
|