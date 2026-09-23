source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/llama/
lastmod: 2026-09-23

class LlamaDecoderLayer(nn.Module):
def __init__(
self,
vllm_config: VllmConfig,
prefix: str = "",
config: LlamaConfig | None = None,
attn_layer_type: type[nn.Module] = LlamaAttention,
) -> None:
super().__init__()
config = config or vllm_config.model_config.hf_config
cache_config = vllm_config.cache_config
quant_config = self.get_quant_config(vllm_config)
self.hidden_size = config.hidden_size
max_position_embeddings = getattr(config, "max_position_embeddings", 8192)
# Support abacusai/Smaug-72B-v0.1 with attention_bias
attention_bias = getattr(config, "attention_bias", False) or getattr(
config, "bias", False
)
bias_o_proj = attention_bias
# support internlm/internlm3-8b with qkv_bias
if hasattr(config, "qkv_bias"):
attention_bias = config.qkv_bias
# By default, Llama uses causal attention as it is a decoder-only model.
# You can override the HF config with `is_causal=False` to enable
# bidirectional attention, which is used in some embedding models
# (e.g. nvidia/llama-nemotron-embed-1b-v2)
if getattr(config, "is_causal", True):
attn_type = AttentionType.DECODER
else:
attn_type = AttentionType.ENCODER_ONLY
self.self_attn = attn_layer_type(
config=config,
hidden_size=self.hidden_size,
num_heads=config.num_attention_heads,
num_kv_heads=getattr(
config, "num_key_value_heads", config.num_attention_heads
),
max_position_embeddings=max_position_embeddings,
quant_config=quant_config,
bias=attention_bias,
bias_o_proj=bias_o_proj,
cache_config=cache_config,
prefix=f"{prefix}.self_attn",
attn_type=attn_type,
)
self.mlp = LlamaMLP(
hidden_size=self.hidden_size,
intermediate_size=config.intermediate_size,
hidden_act=config.hidden_act,
quant_config=quant_config,
bias=getattr(config, "mlp_bias", False),
prefix=f"{prefix}.mlp",
)
self.input_layernorm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
self.post_attention_layernorm = RMSNorm(
config.hidden_size, eps=config.rms_norm_eps
)
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
residual: torch.Tensor | None,
) -> tuple[torch.Tensor, torch.Tensor]:
# Self Attention
if residual is None:
residual = hidden_states
hidden_states = self.input_layernorm(hidden_states)
else:
hidden_states, residual = self.input_layernorm(hidden_states, residual)
hidden_states = self.self_attn(positions=positions, hidden_states=hidden_states)
# Fully Connected
hidden_states, residual = self.post_attention_layernorm(hidden_states, residual)
hidden_states = self.mlp(hidden_states)
return hidden_states, residual
def get_quant_config(self, vllm_config: VllmConfig) -> QuantizationConfig | None:
"""Get quantization config for this layer. Override in subclasses."""
return vllm_config.quant_config