source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/gemma4_rope/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.rotary_embedding.gemma4_rope`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.gemma4_rope)

Gemma4-specific Rotary Positional Embeddings (proportional scaling).

Gemma4 uses "proportional" RoPE which computes inv_freq frequencies scaled by head_dim (not rotary_dim), and zero-pads for non-rotated dimensions when partial_rotary_factor < 1. The actual rotation uses standard neox-style rotate_half, matching HF transformers' apply_rotary_pos_emb.

Classes:

-
–[Gemma4RotaryEmbedding](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.gemma4_rope.Gemma4RotaryEmbedding)Gemma4 proportional RoPE.


##

`Gemma4RotaryEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.gemma4_rope.Gemma4RotaryEmbedding)

Bases: [RotaryEmbedding](https://docs.vllm.ai/base/#vllm.model_executor.layers.rotary_embedding.base.RotaryEmbedding)

Gemma4 proportional RoPE.

Extends RotaryEmbedding (which provides standard neox-style rotation via ops.rotary_embedding CUDA kernel) but overrides the inv_freq computation to match HF's _compute_proportional_rope_parameters: - Frequency exponents use head_dim (not rotary_dim) as denominator - Non-rotated dims are zero-padded (cos=1, sin=0 = identity rotation)

When partial_rotary_factor=1.0 (the default for some variants), ALL dims are rotated and this is equivalent to standard RotaryEmbedding with head_dim-scaled frequencies.

## Source code in `vllm/model_executor/layers/rotary_embedding/gemma4_rope.py`


###

`_compute_inv_freq(base)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.gemma4_rope.Gemma4RotaryEmbedding._compute_inv_freq)

Compute frequencies matching HF proportional RoPE.

Key difference from base: exponent denominator is head_size (not rotary_dim), and non-rotated dims are zero-padded.