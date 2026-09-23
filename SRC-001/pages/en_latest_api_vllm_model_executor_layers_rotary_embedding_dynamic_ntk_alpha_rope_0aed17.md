source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/dynamic_ntk_alpha_rope/
lastmod: 2026-09-23

Bases: [RotaryEmbedding](../base/#vllm.model_executor.layers.rotary_embedding.base.RotaryEmbedding)


RotaryEmbedding extended with Dynamic NTK alpha.

Based on the original RotaryEmbedding implementation.

## Source code in `vllm/model_executor/layers/rotary_embedding/dynamic_ntk_alpha_rope.py`


| class DynamicNTKAlphaRotaryEmbedding(RotaryEmbedding):
"""RotaryEmbedding extended with Dynamic NTK alpha.
Based on the original RotaryEmbedding implementation.
"""
def __init__(
self,
head_size: int,
rotary_dim: int,
max_position_embeddings: int,
base: float,
is_neox_style: bool,
scaling_alpha: float,
dtype: torch.dtype,
) -> None:
self.scaling_alpha = scaling_alpha
super().__init__(
head_size, rotary_dim, max_position_embeddings, base, is_neox_style, dtype
)
def _compute_cos_sin_cache(self) -> torch.Tensor:
# For Hunyuan DynamicNTKAlphaRotaryEmbedding
max_len = self.max_position_embeddings
base = self.base * self.scaling_alpha ** (
self.rotary_dim / (self.rotary_dim - 2)
)
inv_freq = self._compute_inv_freq(base)
t = torch.arange(max_len, dtype=torch.float)
freqs = torch.einsum("i,j -> ij", t, inv_freq)
cos = freqs.cos()
sin = freqs.sin()
cache = torch.cat((cos, sin), dim=-1)
return cache
|