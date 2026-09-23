source: https://docs.vllm.ai/en/latest/api/vllm/models/dots3_note/nvidia/vision_attention/
lastmod: 2026-09-23

#

`vllm.models.dots3_note.nvidia.vision_attention`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention)

Shared vision attention stack for Dots dense / MoE ViT encoders.

Exports every attention backend (eager, eager_v2, sdpa, flash_attention_2, flash_attention_3), RoPE helpers, and block wiring utilities.

Classes:

-
–[VisionAttention](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.VisionAttention)Eager attention with a dense block-diagonal mask (cu_seqlens boundaries).

-
–[VisionAttentionV2](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.VisionAttentionV2)Eager attention per varlen segment (lower peak memory than :class:

`VisionAttention`

). -
–[VisionRMSNorm](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.VisionRMSNorm)Dots ViT RMSNorm with an fp32 reduction and input-dtype output.

-
–[VisionRotaryEmbedding](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.VisionRotaryEmbedding)2D vision RoPE frequency table.


Functions:

-
–[apply_vision_attention_residual](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.apply_vision_attention_residual)Pre-norm residual attention used by dense / MoE vision blocks.

-
–[build_vision_attention](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.build_vision_attention)Instantiate a vision attention module from

`attn_implementation`

and config. -
–[prepare_rotary_pos_emb_vision](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.prepare_rotary_pos_emb_vision)Materialize vision RoPE cos/sin once for every encoder layer.

-
–[prepare_seqlens_for_attention](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.prepare_seqlens_for_attention)Return per-segment lengths when the resolved backend needs

`seqlens`

. -
–[resolve_attn_implementation](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.resolve_attn_implementation)Apply FA3 → FA2 → eager fallback when backends are missing.


##

`VisionAttention`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.VisionAttention)

Bases: [_VisionAttentionBase](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention._VisionAttentionBase)

Eager attention with a dense block-diagonal mask (cu_seqlens boundaries).

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`VisionAttentionV2`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.VisionAttentionV2)

Bases: [_VisionAttentionBase](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention._VisionAttentionBase)

Eager attention per varlen segment (lower peak memory than :class:`VisionAttention`

).

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`VisionRMSNorm`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.VisionRMSNorm)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Dots ViT RMSNorm with an fp32 reduction and input-dtype output.

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`VisionRotaryEmbedding`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.VisionRotaryEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

2D vision RoPE frequency table.

When `cache_seq_len`

is set, precomputes and reuses frequencies up to that length (MoE default). Otherwise frequencies are computed on each forward (dense default).

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`_VisionAttentionBase`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention._VisionAttentionBase)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

QKV projection, optional Q/K norm, and output projection.

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`apply_vision_attention_residual(attn, norm, hidden_states, cu_seqlens, max_seqlen, rotary_pos_emb, *, seqlens=None, uses_seqlens=False)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.apply_vision_attention_residual)

Pre-norm residual attention used by dense / MoE vision blocks.

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`build_vision_attention(attn_implementation, config, *, dim=None, num_heads=None, bias=None, eager_fallback='eager')`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.build_vision_attention)

Instantiate a vision attention module from `attn_implementation`

and config.

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`prepare_rotary_pos_emb_vision(freqs)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.prepare_rotary_pos_emb_vision)

Materialize vision RoPE cos/sin once for every encoder layer.

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`prepare_seqlens_for_attention(attn_implementation, cu_seqlens, *, eager_fallback='eager')`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.prepare_seqlens_for_attention)

Return per-segment lengths when the resolved backend needs `seqlens`

.

## Source code in `vllm/models/dots3_note/nvidia/vision_attention.py`


##

`resolve_attn_implementation(attn_implementation, *, eager_fallback='eager')`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision_attention.resolve_attn_implementation)

Apply FA3 → FA2 → eager fallback when backends are missing.

`eager_fallback`

selects which eager backend is used when flash-attn is unavailable. MoE historically used per-segment eager (`eager_v2`

); dense uses full-mask `eager`

.