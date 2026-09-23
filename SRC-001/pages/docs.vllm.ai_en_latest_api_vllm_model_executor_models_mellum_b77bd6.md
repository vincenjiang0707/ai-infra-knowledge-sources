source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mellum/
lastmod: 2026-09-23

class MellumAttention(Qwen3MoeAttention):
"""Differences from `Qwen3MoeAttention`:
- Supports `per_layer_sliding_window` for `Attention`.
"""
def __init__(
self,
hidden_size: int,
num_heads: int,
num_kv_heads: int,
rope_parameters: dict[str, Any],
max_position_embeddings: int = 8192,
head_dim: int | None = None,
rms_norm_eps: float = 1e-06,
qkv_bias: bool = False,
cache_config: Any | None = None,
quant_config: Any | None = None,
prefix: str = "",
dual_chunk_attention_config: dict[str, Any] | None = None,
per_layer_sliding_window: int | None = None,
) -> None:
nn.Module.__init__(self)
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
self.dual_chunk_attention_config = dual_chunk_attention_config
self.qkv_proj = QKVParallelLinear(
hidden_size,
self.head_dim,
self.total_num_heads,
self.total_num_kv_heads,
bias=qkv_bias,
quant_config=quant_config,
prefix=f"{prefix}.qkv_proj",
)
self.o_proj = RowParallelLinear(
self.total_num_heads * self.head_dim,
hidden_size,
bias=False,
quant_config=quant_config,
prefix=f"{prefix}.o_proj",
)
self.rotary_emb = get_rope(
self.head_dim,
max_position=max_position_embeddings,
rope_parameters=rope_parameters,
dual_chunk_attention_config=dual_chunk_attention_config,
)
if dual_chunk_attention_config:
self.attn = Attention(
self.num_heads,
self.head_dim,
self.scaling,
num_kv_heads=self.num_kv_heads,
cache_config=cache_config,
quant_config=quant_config,
per_layer_sliding_window=per_layer_sliding_window,
prefix=f"{prefix}.attn",
layer_idx=extract_layer_index(prefix),
dual_chunk_attention_config=dual_chunk_attention_config,
)
else:
self.attn = Attention(
self.num_heads,
self.head_dim,
self.scaling,
num_kv_heads=self.num_kv_heads,
cache_config=cache_config,
quant_config=quant_config,
per_layer_sliding_window=per_layer_sliding_window,
prefix=f"{prefix}.attn",
)
self.q_norm = RMSNorm(self.head_dim, eps=rms_norm_eps)
self.k_norm = RMSNorm(self.head_dim, eps=rms_norm_eps)