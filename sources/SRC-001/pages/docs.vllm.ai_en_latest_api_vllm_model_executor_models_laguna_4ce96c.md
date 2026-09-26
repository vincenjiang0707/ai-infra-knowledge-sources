source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/laguna/
lastmod: 2026-09-24

class LagunaAttention(nn.Module):
"""Laguna attention with optional softplus output gating.
Supports per-layer sliding window attention when ``config.layer_types``
is present. Layers whose type is ``"sliding_attention"`` use
``config.sliding_window``; all other layers (typically labelled
``"full_attention"``) use full attention. When ``layer_types`` is
absent every layer defaults to full attention for backwards
compatibility.
"""
def __init__(
self,
config,
hidden_size: int,
num_heads: int,
num_kv_heads: int,
max_position_embeddings: int = 131072,
head_dim: int | None = None,
cache_config: CacheConfig | None = None,
quant_config: QuantizationConfig | None = None,
prefix: str = "",
attention_sink: bool = False,
layer_idx: int | None = None,
attention_prefix: str | None = None,
) -> None:
super().__init__()
if layer_idx is None:
layer_idx = extract_layer_index(prefix)
if attention_prefix is None:
attention_prefix = prefix
self.hidden_size = hidden_size
tp_size = get_tensor_model_parallel_world_size()
self.total_num_heads = num_heads
assert self.total_num_heads % tp_size == 0
self.num_heads = self.total_num_heads // tp_size
self.total_num_kv_heads = num_kv_heads
if self.total_num_kv_heads >= tp_size:
assert self.total_num_kv_heads % tp_size == 0
else:
assert tp_size % self.total_num_kv_heads == 0
self.num_kv_heads = max(1, self.total_num_kv_heads // tp_size)
self.head_dim = head_dim or (hidden_size // self.total_num_heads)
self.q_size = self.num_heads * self.head_dim
self.kv_size = self.num_kv_heads * self.head_dim
self.scaling = self.head_dim**-0.5
self.max_position_embeddings = max_position_embeddings
# Gating flag
self.gating = config.gating
# Per-layer sliding window (follows Gemma2/Cohere2 convention)
layer_types = getattr(config, "layer_types", None)
if layer_types is not None:
is_sliding = layer_types[layer_idx] == "sliding_attention"
self.sliding_window = config.sliding_window if is_sliding else None
else:
self.sliding_window = None
self.qkv_proj = QKVParallelLinear(
self.hidden_size,
self.head_dim,
self.total_num_heads,
self.total_num_kv_heads,
bias=config.attention_bias,
quant_config=quant_config,
prefix=f"{prefix}.qkv_proj",
)
# Output projection
self.o_proj = RowParallelLinear(
self.total_num_heads * self.head_dim,
self.hidden_size,
bias=config.attention_bias,
quant_config=quant_config,
prefix=f"{prefix}.o_proj",
)
# Gating projection (Laguna-specific, optional)
# config.gating may be:
# - True / "per-element": one gate per (head, head_dim) channel
# - "per-head": one gate per head, broadcast across head_dim
self.g_proj: ColumnParallelLinear | None
if self.gating:
# v5 LagunaConfig uses ``gating=True`` for per-head; older configs
# used ``"per-head"``. Accept both. ``"per-element"`` (or legacy
# ``True``) means per-element gating with output size num_heads ×
# head_dim.
gate_per_head = self.gating is True or self.gating == "per-head"
g_out = (
self.total_num_heads
if gate_per_head
else self.total_num_heads * self.head_dim
)
self.g_proj = ColumnParallelLinear(
hidden_size,
g_out,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.g_proj",
)
self.gate_per_head = gate_per_head
else:
self.g_proj = None
self.gate_per_head = False
# Attention sinks (learnable per-head bias for SWA layers)
sinks = None
if attention_sink:
self.sink = torch.nn.Parameter(
torch.empty(self.total_num_heads // tp_size, requires_grad=False)
)
sinks = self.sink
# Resolve rope params per-layer-type. ``config.rope_parameters`` is
# either a flat dict (legacy) or a nested ``{layer_type: rope_dict}``
# (v5 Laguna-XS schema). The v5 form is unhashable as-is and would
# crash `get_rope`'s cache lookup, so always pull out the layer's
# sub-dict before forwarding.
layer_type = (
layer_types[layer_idx] if layer_types is not None else "full_attention"
)
is_sliding = layer_type == "sliding_attention"
top_rope = getattr(config, "rope_parameters", None) or {}
if any(isinstance(v, dict) for v in top_rope.values()):
# Nested per-layer-type form.
base_rope = top_rope.get(layer_type) or top_rope.get("full_attention") or {}
else:
base_rope = top_rope
# Older flat-rope ckpts can carry a separate `swa_rope_parameters`
# for SWA layers. Prefer it when present; otherwise the nested
# rope dict above already supplies the correct sub-config.
swa_rope = getattr(config, "swa_rope_parameters", None)
if (
is_sliding
and swa_rope is None
and not any(isinstance(v, dict) for v in top_rope.values())
):
logger.warning_once(
"Laguna config has sliding_attention layers but neither "
"`swa_rope_parameters` nor a nested per-layer-type "
"`rope_parameters` — SWA layers will reuse the global rope. "
"If the checkpoint was trained with distinct SWA rope "
"(theta / partial_rotary_factor), regenerate its HF config "
"to include either form."
)
rope_params = swa_rope if (is_sliding and swa_rope is not None) else base_rope
# `partial_rotary_factor` may live on the top-level config (main attention)
# or on the per-layer rope dict itself (e.g. SWA can differ). Inject the
# top-level value into `rope_params` if the dict doesn't already set it.
top_partial = getattr(config, "partial_rotary_factor", None)
if top_partial is not None and "partial_rotary_factor" not in rope_params:
rope_params = {**rope_params, "partial_rotary_factor": top_partial}
# Rotary embeddings (YaRN)
self.rotary_emb = get_rope(
head_size=self.head_dim,
max_position=max_position_embeddings,
is_neox_style=True,
rope_parameters=rope_params,
)
self.attn = Attention(
self.num_heads,
self.head_dim,
self.scaling,
num_kv_heads=self.num_kv_heads,
cache_config=cache_config,
quant_config=quant_config,
per_layer_sliding_window=self.sliding_window,
prefix=f"{attention_prefix}.attn",
sinks=sinks,
)
# QK normalization (like Qwen3)
self.q_norm = RMSNorm(self.head_dim, eps=config.rms_norm_eps)
self.k_norm = RMSNorm(self.head_dim, eps=config.rms_norm_eps)
def forward(
self,
positions: torch.Tensor,
hidden_states: torch.Tensor,
) -> torch.Tensor:
qkv, _ = self.qkv_proj(hidden_states)
q, k, v = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1)
q_by_head = q.view(*q.shape[:-1], q.shape[-1] // self.head_dim, self.head_dim)
q_by_head = self.q_norm(q_by_head)
q = q_by_head.view(q.shape)
k_by_head = k.view(*k.shape[:-1], k.shape[-1] // self.head_dim, self.head_dim)
k_by_head = self.k_norm(k_by_head)
k = k_by_head.view(k.shape)
q, k = self.rotary_emb(positions, q, k)
attn_output = self.attn(q, k, v)
# Apply gating if enabled (compute softplus in float32 for precision)
if self.gating and self.g_proj is not None:
gate, _ = self.g_proj(hidden_states)
gate = F.softplus(gate.float()).type_as(attn_output)
if self.gate_per_head:
# gate: [..., num_heads]; broadcast across head_dim
attn_shape = attn_output.shape
attn_output = (
attn_output.view(*attn_shape[:-1], self.num_heads, self.head_dim)
* gate.unsqueeze(-1)
).view(attn_shape)
else:
attn_output = attn_output * gate
output, _ = self.o_proj(attn_output)
return output