source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma4_dspark/
lastmod: 2026-09-23

@support_torch_compile
class Gemma4DSparkModel(DFlashQwen3Model):
"""Gemma4 DSpark draft backbone (Gemma4 layers + DSpark Markov head)."""
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
nn.Module.__init__(self)
assert vllm_config.speculative_config is not None
config = vllm_config.speculative_config.draft_model_config.hf_config
self.config = config
self.use_aux_hidden_state = True
self.target_layer_ids = tuple(
getattr(config, "dspark_target_layer_ids", None) or config.target_layer_ids
)
current_vllm_config = get_current_vllm_config()
cache_config = current_vllm_config.cache_config
quant_config = current_vllm_config.quant_config
self.embed_tokens = VocabParallelEmbedding(
config.vocab_size,
config.hidden_size,
prefix=maybe_prefix(prefix, "embed_tokens"),
)
self.register_buffer(
"normalizer",
torch.tensor(config.hidden_size**0.5, dtype=vllm_config.model_config.dtype),
persistent=False,
)
self.fc = ReplicatedLinear(
config.hidden_size * len(self.target_layer_ids),
config.hidden_size,
bias=False,
return_bias=False,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "fc"),
)
self.hidden_norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
self.layers = nn.ModuleList(
Gemma4DSparkDecoderLayer(
config,
cache_config,
quant_config,
prefix=maybe_prefix(prefix, f"layers.{i}"),
)
for i in range(config.num_hidden_layers)
)
self.norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
draft_vocab_size = (
getattr(config, "draft_vocab_size", None) or config.vocab_size
)
self.markov_head = DSparkMarkovHead(
config.vocab_size,
draft_vocab_size,
config.markov_rank,
prefix=maybe_prefix(prefix, "markov_head"),
)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.embed_tokens(input_ids) * self.normalizer
def _build_fused_kv_buffers(self) -> None:
layers_attn = [layer.self_attn for layer in self.layers]
attn0 = layers_attn[0]
assert all(a.use_k_eq_v for a in layers_attn), (
"Gemma4 DSpark fused precompute assumes uniform attention_k_eq_v layers"
)
self._build_context_kv_buffers(layers_attn, attn0.k_proj.bias is not None)
self._rope_head_size = attn0.rotary_emb.head_size
self._rope_cos_sin_cache = attn0.rotary_emb.cos_sin_cache
self._rope_is_neox = attn0.rotary_emb.is_neox_style
self._num_attn_layers = len(layers_attn)
self._kv_size = attn0.kv_size
self._head_dim = attn0.head_dim
self._num_kv_heads = attn0.num_kv_heads
self._rms_norm_eps = attn0.q_norm.variance_epsilon
self._attn_layers = [layer.self_attn.attn for layer in self.layers]
def _build_context_kv_buffers(
self, layers_attn: list[nn.Module], has_bias: bool
) -> None:
self._hidden_norm_weight = self.hidden_norm.weight.data
self._fused_k_weight = torch.cat([a.k_proj.weight for a in layers_attn], dim=0)
self._fused_k_bias: torch.Tensor | None = (
torch.cat([a.k_proj.bias for a in layers_attn], dim=0) if has_bias else None
)
self._k_norm_weights = torch.stack(
[a.k_norm.weight.data for a in layers_attn], dim=0
).contiguous()
# v_norm has no learnable scale; ones matching the K-norm call shape.
self._v_norm_weights = torch.ones(
len(layers_attn),
layers_attn[0].head_dim,
dtype=self._k_norm_weights.dtype,
device=self._k_norm_weights.device,
)
def _project_context_kv(
self,
context_states: torch.Tensor,
num_ctx: int,
num_layers: int,
num_kv_heads: int,
head_dim: int,
) -> tuple[torch.Tensor, torch.Tensor]:
# Project once via k_proj for all layers. K is raw (the inherited path
# applies k_norm + RoPE); V = v_norm(same projection), no RoPE (k_eq_v).
normed = torch.empty_like(context_states)
ops.rms_norm(
normed, context_states, self._hidden_norm_weight, self._rms_norm_eps
)
all_k_flat = F.linear(normed, self._fused_k_weight, self._fused_k_bias)
all_k = (
all_k_flat.view(num_ctx, num_layers, num_kv_heads, head_dim)
.permute(1, 0, 2, 3)
.contiguous()
)
all_v = torch.empty_like(all_k)
ops.rms_norm(all_v, all_k, self._v_norm_weights, self._rms_norm_eps)
return all_k, all_v
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
input_embeds: torch.Tensor | None = None,
) -> torch.Tensor:
hidden_states = (
self.embed_input_ids(input_ids) if input_embeds is None else input_embeds
)
for layer in self.layers:
hidden_states, _ = layer(positions, hidden_states, None)
return self.norm(hidden_states)