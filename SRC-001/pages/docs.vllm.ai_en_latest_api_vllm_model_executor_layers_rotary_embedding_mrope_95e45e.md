source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/mrope/
lastmod: 2026-09-23

class MRotaryEmbedding(RotaryEmbeddingBase):
"""Rotary Embedding with Multimodal Sections."""
def __init__(
self,
head_size: int,
rotary_dim: int,
max_position_embeddings: int,
base: float,
is_neox_style: bool,
dtype: torch.dtype,
mrope_section: list[int] | None = None,
mrope_interleaved: bool = False,
# YaRN parameters.
*,
scaling_factor: float | None = None,
beta_fast: int = 32,
beta_slow: int = 1,
mscale: float | None = None,
mscale_all_dim: float | None = None,
attention_factor: float | None = None,
truncate: bool = True,
) -> None:
self.scaling_factor = scaling_factor
self.beta_fast = beta_fast
self.beta_slow = beta_slow
self.truncate = truncate
if self.scaling_factor is not None:
# Get n-d magnitude scaling corrected for interpolation
if attention_factor is not None:
self.mscale = float(attention_factor)
elif mscale and mscale_all_dim:
self.mscale = float(
yarn_get_mscale(self.scaling_factor, mscale)
/ yarn_get_mscale(self.scaling_factor, mscale_all_dim)
)
else:
self.mscale = float(yarn_get_mscale(self.scaling_factor))
else:
self.mscale = 1.0
# In Qwen2.5-VL, the maximum index value is related to the duration of
# the input video. We enlarge max_position_embeddings to 4 times to get
# a larger the cos and sin cache.
self.cache_max_position_num = max_position_embeddings * 4
super().__init__(
head_size,
rotary_dim,
self.cache_max_position_num,
base,
is_neox_style,
dtype,
)
self.mrope_section = mrope_section
self.mrope_interleaved = mrope_interleaved
if self.mrope_section:
assert sum(self.mrope_section) == rotary_dim // 2
def _compute_inv_freq(self, base: float) -> torch.Tensor:
if self.scaling_factor is None:
return super()._compute_inv_freq(base)
return YaRNScalingRotaryEmbedding._compute_inv_freq(self, base)
def _compute_cos_sin_cache(self) -> torch.Tensor:
if self.scaling_factor is None:
return super()._compute_cos_sin_cache()
return YaRNScalingRotaryEmbedding._compute_cos_sin_cache(self)
def forward_native(
self,
positions: torch.Tensor,
query: torch.Tensor,
key: torch.Tensor | None = None,
offsets: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor | None]:
"""PyTorch-native implementation equivalent to forward().
Args:
positions:
[num_tokens,] (text only) or
[3, num_tokens] (T/H/W positions with multimodal inputs)
query: [num_tokens, num_heads * head_size]
key: [num_tokens, num_kv_heads * head_size]
offsets: Optional per-token position offsets added to positions.
"""
assert positions.ndim == 1 or positions.ndim == 2
assert key is not None
cos_sin_cache = self._match_cos_sin_cache_dtype(query)
num_tokens = positions.shape[-1]
cos_sin = cos_sin_cache[positions]
cos, sin = cos_sin.chunk(2, dim=-1)
if positions.ndim == 2:
assert self.mrope_section
if self.mrope_interleaved:
cos = apply_interleaved_rope(cos, self.mrope_section)
sin = apply_interleaved_rope(sin, self.mrope_section)
else:
cos = torch.cat(
[m[i] for i, m in enumerate(cos.split(self.mrope_section, dim=-1))],
dim=-1,
)
sin = torch.cat(
[m[i] for i, m in enumerate(sin.split(self.mrope_section, dim=-1))],
dim=-1,
)
query_shape = query.shape
query = query.view(num_tokens, -1, self.head_size)
query_rot = query[..., : self.rotary_dim]
query_pass = query[..., self.rotary_dim :]
query_rot = self.apply_rotary_emb.forward_native(
query_rot,
cos,
sin,
)
query = torch.cat((query_rot, query_pass), dim=-1).reshape(query_shape)
key_shape = key.shape
key = key.view(num_tokens, -1, self.head_size)
key_rot = key[..., : self.rotary_dim]
key_pass = key[..., self.rotary_dim :]
key_rot = self.apply_rotary_emb.forward_native(
key_rot,
cos,
sin,
)
key = torch.cat((key_rot, key_pass), dim=-1).reshape(key_shape)
return query, key
def forward_cuda(
self,
positions: torch.Tensor,
query: torch.Tensor,
key: torch.Tensor | None = None,
offsets: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor | None]:
assert positions.ndim == 1 or positions.ndim == 2
assert key is not None
cos_sin_cache = self._match_cos_sin_cache_dtype(query)
num_tokens = positions.shape[-1]
cos_sin = cos_sin_cache[positions]
cos, sin = cos_sin.chunk(2, dim=-1)
query_shape = query.shape
key_shape = key.shape
if positions.ndim == 2:
assert self.mrope_section
q, k = triton_mrope(
query,
key,
cos,
sin,
self.mrope_section,
self.head_size,
self.rotary_dim,
self.mrope_interleaved,
self.is_neox_style,
)
return q.reshape(query_shape), k.reshape(key_shape)
query = query.view(num_tokens, -1, self.head_size)
query_rot = query[..., : self.rotary_dim]
query_pass = query[..., self.rotary_dim :]
query_rot = self.apply_rotary_emb(
query_rot,
cos,
sin,
)
query = torch.cat((query_rot, query_pass), dim=-1).reshape(query_shape)
key = key.view(num_tokens, -1, self.head_size)
key_rot = key[..., : self.rotary_dim]
key_pass = key[..., self.rotary_dim :]
key_rot = self.apply_rotary_emb(
key_rot,
cos,
sin,
)
key = torch.cat((key_rot, key_pass), dim=-1).reshape(key_shape)
return query, key
def forward_cpu(
self,
positions: torch.Tensor,
query: torch.Tensor,
key: torch.Tensor | None = None,
offsets: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor | None]:
return self.forward_native(positions, query, key, offsets)
def forward_xpu(
self,
positions: torch.Tensor,
query: torch.Tensor,
key: torch.Tensor | None = None,
offsets: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor | None]:
return self.forward_cuda(positions, query, key, offsets)
@staticmethod
def get_next_input_positions(
mrope_position_delta: int,
context_len: int,
seq_len: int,
) -> list[list[int]]:
return [
list(
range(
context_len + mrope_position_delta, seq_len + mrope_position_delta
)
)
for _ in range(3)
]
@staticmethod
def get_next_input_positions_tensor(
out: np.ndarray,
out_offset: int,
mrope_position_delta: int,
context_len: int,
num_new_tokens: int,
):
values = np.arange(
mrope_position_delta + context_len,
mrope_position_delta + context_len + num_new_tokens,
dtype=out.dtype,
)
out[:, out_offset : out_offset + num_new_tokens] = values