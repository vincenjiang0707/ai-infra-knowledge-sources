source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/dynamic_ntk_scaling_rope/
lastmod: 2026-09-23

Bases: [RotaryEmbedding](../base/#vllm.model_executor.layers.rotary_embedding.base.RotaryEmbedding)


RotaryEmbedding extended with Dynamic NTK scaling.

Credits to the Reddit users /u/bloc97 and /u/emozilla

## Source code in `vllm/model_executor/layers/rotary_embedding/dynamic_ntk_scaling_rope.py`


| class DynamicNTKScalingRotaryEmbedding(RotaryEmbedding):
"""RotaryEmbedding extended with Dynamic NTK scaling.
Credits to the Reddit users /u/bloc97 and /u/emozilla
"""
def __init__(
self,
head_size: int,
rotary_dim: int,
max_position_embeddings: int,
max_trained_positions: int,
base: float,
is_neox_style: bool,
scaling_factor: float,
dtype: torch.dtype,
) -> None:
self.scaling_factor = scaling_factor
self.max_trained_positions = max_trained_positions
super().__init__(
head_size, rotary_dim, max_position_embeddings, base, is_neox_style, dtype
)
def _compute_cos_sin_cache(self) -> torch.Tensor:
# NOTE(woosuk): self.max_position_embeddings is the original
# maximum length before applying the rope scaling.
# Thus, the maximum length after applying the rope scaling is
# self.max_position_embeddings * self.scaling_factor.
base = self.base * (
(
self.scaling_factor
* self.max_position_embeddings
/ self.max_trained_positions
)
- (self.scaling_factor - 1)
) ** (self.rotary_dim / (self.rotary_dim - 2))
inv_freq = self._compute_inv_freq(base)
t = torch.arange(self.max_position_embeddings, dtype=torch.float)
freqs = torch.einsum("i,j -> ij", t, inv_freq)
cos = freqs.cos()
sin = freqs.sin()
cache = torch.cat((cos, sin), dim=-1)
return cache
|