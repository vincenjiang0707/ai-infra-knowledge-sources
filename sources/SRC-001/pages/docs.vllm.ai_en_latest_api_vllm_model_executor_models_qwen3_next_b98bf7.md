source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen3_next/
lastmod: 2026-09-24

class Qwen3NextAttention(nn.Module):
def __init__(
self,
config: Qwen3NextConfig,
model_config: ModelConfig | None = None,
cache_config: CacheConfig | None = None,
quant_config: QuantizationConfig | None = None,
reduce_results: bool = True,
prefix: str = "",
) -> None:
super().__init__()
self.config = config
self.hidden_size = config.hidden_size
tp_size = get_tensor_model_parallel_world_size()
self.total_num_heads = config.num_attention_heads
assert self.total_num_heads % tp_size == 0
self.num_heads = self.total_num_heads // tp_size
self.total_num_kv_heads = config.num_key_value_heads
if self.total_num_kv_heads >= tp_size:
# Number of KV heads is greater than TP size, so we partition
# the KV heads across multiple tensor parallel GPUs.
assert self.total_num_kv_heads % tp_size == 0
else:
# Number of KV heads is less than TP size, so we replicate
# the KV heads across multiple tensor parallel GPUs.
assert tp_size % self.total_num_kv_heads == 0
self.num_kv_heads = max(1, self.total_num_kv_heads // tp_size)
self.head_dim = config.head_dim or (self.hidden_size // self.num_heads)
self.q_size = self.num_heads * self.head_dim
self.kv_size = self.num_kv_heads * self.head_dim
self.scaling = self.head_dim**-0.5
self.dual_chunk_attention_config = getattr(
config, "dual_chunk_attention_config", None
)
self.attn_output_gate = getattr(config, "attn_output_gate", True)
self.qkv_proj = QKVParallelLinear(
config.hidden_size,
self.head_dim,
self.total_num_heads * (1 + self.attn_output_gate),
self.total_num_kv_heads,
bias=getattr(config, "qkv_bias", False),
quant_config=quant_config,
prefix=f"{prefix}.qkv_proj",
)
self.o_proj = RowParallelLinear(
self.total_num_heads * self.head_dim,
config.hidden_size,
bias=False,
reduce_results=reduce_results,
quant_config=quant_config,
prefix=f"{prefix}.o_proj",
)
self.rotary_emb = get_rope(
head_size=self.head_dim,
max_position=config.max_position_embeddings,
rope_parameters=config.rope_parameters,
dual_chunk_attention_config=self.dual_chunk_attention_config,
)
# Late-interaction retrieval models (e.g. ColQwen3.5) run BIDIRECTIONAL
# attention on the full_attention layers; they set config.is_causal=False
# via a VerifyAndUpdateConfig handler. Generation models leave is_causal
# unset (-> causal/DECODER), so this is a no-op for them. Mirrors qwen3.py.
attn_type = (
AttentionType.DECODER
if getattr(config, "is_causal", True)
else AttentionType.ENCODER_ONLY
)
self.attn = Attention(
self.num_heads,
self.head_dim,
self.scaling,
num_kv_heads=self.num_kv_heads,
cache_config=cache_config,
quant_config=quant_config,
prefix=f"{prefix}.attn",
attn_type=attn_type,
**{
"layer_idx": extract_layer_index(prefix),
"dual_chunk_attention_config": self.dual_chunk_attention_config,
}
if self.dual_chunk_attention_config
else {},
)
self.q_norm = Qwen3NextRMSNorm(self.head_dim, eps=config.rms_norm_eps)
self.k_norm = Qwen3NextRMSNorm(self.head_dim, eps=config.rms_norm_eps)
# Fuse the gated split + QK-RMSNorm + (partial) NeoX RoPE + gate copy.
mm_config = model_config.multimodal_config if model_config else None
text_only = mm_config is None or mm_config.language_model_only
mrope_section = getattr(self.rotary_emb, "mrope_section", None)
supports_mrope = bool(
type(self.rotary_emb) is MRotaryEmbedding
and mrope_section
and len(mrope_section) == 3
and sum(mrope_section) == self.rotary_emb.rotary_dim // 2
and getattr(self.rotary_emb, "mrope_interleaved", False)
)
supports_dtype = getattr(self.rotary_emb, "dtype", None) in (
torch.float16,
torch.bfloat16,
)
self.use_fused_qk_norm_rope_gate = (
self.attn_output_gate
and getattr(self.rotary_emb, "is_neox_style", False)
and (current_platform.is_cuda() or current_platform.is_xpu())
and supports_dtype
and (text_only or supports_mrope)
)
def _project_qkv_gate(
self,
qkv: torch.Tensor,
positions: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor | None]:
"""Return post-norm, post-RoPE (q, k, v) and the pre-sigmoid gate.
Dispatches between the fused Triton kernel and the eager
split + QK-RMSNorm + RoPE path. ``gate`` is ``None`` when output
gating is disabled.
"""
if self.use_fused_qk_norm_rope_gate:
q_gate, k, v = qkv.split(
[self.q_size * 2, self.kv_size, self.kv_size], dim=-1
)
if positions.ndim == 2 and not getattr(
self.rotary_emb, "mrope_section", None
):
positions = positions[0]
q, k, gate = fused_qk_rmsnorm_rope_gate(
q_gate,
k,
self.q_norm.weight,
self.k_norm.weight,
self.rotary_emb.cos_sin_cache,
positions,
self.q_norm.variance_epsilon,
self.num_heads,
self.num_kv_heads,
self.head_dim,
self.rotary_emb.rotary_dim,
norm_beta=1.0,
mrope_section=(
getattr(self.rotary_emb, "mrope_section", None)
if positions.ndim == 2
else None
),
)
return q, k, v, gate
if self.attn_output_gate:
q_gate, k, v = qkv.split(
[self.q_size * 2, self.kv_size, self.kv_size], dim=-1
)
orig_shape = q_gate.shape[:-1]
q_gate = q_gate.view(*orig_shape, self.num_heads, -1)
q, gate = torch.chunk(q_gate, 2, dim=-1)
q = q.reshape(*orig_shape, -1)
gate = gate.reshape(*orig_shape, -1)
else:
q, k, v = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1)
gate = None
q = self.q_norm(q.view(-1, self.num_heads, self.head_dim)).view(
-1, self.num_heads * self.head_dim
)
k = self.k_norm(k.view(-1, self.num_kv_heads, self.head_dim)).view(
-1, self.num_kv_heads * self.head_dim
)
q, k = self.rotary_emb(positions, q, k)
return q, k, v, gate
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
) -> torch.Tensor:
qkv, _ = self.qkv_proj(hidden_states)
q, k, v, gate = self._project_qkv_gate(qkv, positions)
attn_output = self.attn(q, k, v)
if gate is not None:
attn_output = attn_output * torch.sigmoid(gate)
output, _ = self.o_proj(attn_output)
return output