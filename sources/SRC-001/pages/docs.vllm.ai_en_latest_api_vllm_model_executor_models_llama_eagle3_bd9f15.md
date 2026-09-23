source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/llama_eagle3/
lastmod: 2026-09-23

class LlamaDecoderLayer(_Eagle3LlamaDecoderLayerBase):
def __init__(
self,
vllm_config: VllmConfig,
prefix: str = "",
config: LlamaConfig | None = None,
layer_idx: int = 0,
) -> None:
super().__init__(vllm_config, prefix=prefix, config=config)
config = config or vllm_config.model_config.hf_config
quant_config = self.get_quant_config(vllm_config)
# First layer uses 2*hidden_size (embeds + hidden_states concatenated)
# Subsequent layers use hidden_size (only hidden_states, no embeds)
qkv_input_size = 2 * self.hidden_size if layer_idx == 0 else self.hidden_size
# Parallel drafting checkpoints may have attention bias enabled
qkv_bias = getattr(config, "attention_bias", False)
# Override qkv_proj with correct input size and bias setting
self.self_attn.qkv_proj = QKVParallelLinear(
qkv_input_size,
self.self_attn.head_dim,
self.self_attn.total_num_heads,
self.self_attn.total_num_kv_heads,
bias=qkv_bias,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "self_attn.qkv_proj"),
)
self.hidden_norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
self.layer_idx = layer_idx
if getattr(config, "norm_before_residual", False):
self._residual_norm = self._norm_before_residual
else:
self._residual_norm = self._norm_after_residual
def get_quant_config(self, vllm_config: VllmConfig) -> QuantizationConfig | None:
"""Use drafter's quantization config instead of verifier's."""
return get_draft_quant_config(vllm_config)
def _norm_before_residual(
self, hidden_states: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
hidden_states = self.hidden_norm(hidden_states)
residual = hidden_states
return hidden_states, residual
def _norm_after_residual(
self, hidden_states: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
residual = hidden_states
hidden_states = self.hidden_norm(hidden_states)
return hidden_states, residual
def forward(
self,
positions: torch.Tensor,
embeds: torch.Tensor,
hidden_states: torch.Tensor,
residual: torch.Tensor | None,
) -> tuple[torch.Tensor, torch.Tensor]:
if self.layer_idx == 0:
# First layer: concatenate embeds with hidden_states
embeds = self.input_layernorm(embeds)
hidden_states, residual = self._residual_norm(hidden_states=hidden_states)
hidden_states = torch.cat([embeds, hidden_states], dim=-1)
else:
# Subsequent layers: process hidden_states and residuals only
hidden_states, residual = self.input_layernorm(hidden_states, residual)
# Self Attention
hidden_states = self.self_attn(
positions=positions,
hidden_states=hidden_states,
)
hidden_states, residual = self.post_attention_layernorm(hidden_states, residual)
# Fully Connected
hidden_states = self.mlp(hidden_states)
return hidden_states, residual