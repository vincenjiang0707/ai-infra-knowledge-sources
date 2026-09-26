source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/muse_glimmer/
lastmod: 2026-09-24

#

`vllm.model_executor.models.muse_glimmer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer)

Inference-only MuseGlimmer multimodal model for vLLM.

Native port of the MuseGlimmer text decoder (`MuseGlimmerForCausalLM`

). The text stack is a Gemma2 derivative with the following MuseGlimmer-specific deltas, each of which is handled explicitly here:

- SiLU-gated MLP (
`hidden_activation="silu"`

), not Gemma's gelu-tanh. - Scaleless RMSNorm on the token embeddings (no sqrt(hidden) scaling).
- Per-layer sandwich RMSNorms with a baked
`+1`

weight offset (`x * (1 + w)`

), matching Gemma, but with distinct eps for the pre/post norms (`rms_norm_eps`

vs`post_norm_eps`

). - QK-norm (weightless, fp32) applied
*before*RoPE, followed by a query pre-scale of`qk_scale_factor / sqrt(head_dim)`

. - A per-head sigmoid attention output gate.
- iRoPE layout: NoPE layers use full attention, RoPE layers use sliding window attention. RoPE is applied NEOX-style (
`is_neox_style=True`

): the HF converter (`convert_muse_glimmer_weights_to_hf.py`

, 20260806+) permutes q/k into the half-split (NEOX) layout via`_permute_for_rope`

so they pair with`rotate_half`

— matching the reference's interleaved rotation on the*native*(unpermuted) weights. Serving the permuted HF weights with`is_neox_style=False`

scrambles q/k and causes token-repetition collapse. - Final logits are pre-scaled by
`output_multiplier`

and then tanh soft-capped at`final_logit_softcapping`

. - Untied lm_head.

The vision path supports variable-resolution images and temporally patched videos. It mirrors the checkpoint's native vision encoder, including sparse block attention, 2-D RoPE, pixel-shuffle downsampling, and the two-layer adapter/projection stack.

Classes:

-
–[MuseGlimmerForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerForCausalLM) -
–[MuseGlimmerImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerImagePixelInputs)Batched variable-resolution image inputs.

-
–[MuseGlimmerRMSNorm](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerRMSNorm)RMSNorm mirroring HF MuseGlimmer exactly (fp32 compute, cast at the end).

-
–[MuseGlimmerVideoPixelInputs](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerVideoPixelInputs)Batched variable-length, variable-resolution video inputs.


##

`MuseGlimmerForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)[SupportsEagle3](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle3)

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerForCausalLM.get_mm_mapping)Get the module prefix in multimodal models


## Source code in `vllm/model_executor/models/muse_glimmer.py`


|
|

###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerForCausalLM.get_mm_mapping)

Get the module prefix in multimodal models

## Source code in `vllm/model_executor/models/muse_glimmer.py`


##

`MuseGlimmerImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Batched variable-resolution image inputs.

## Source code in `vllm/model_executor/models/muse_glimmer.py`


##

`MuseGlimmerRMSNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerRMSNorm)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

RMSNorm mirroring HF MuseGlimmer exactly (fp32 compute, cast at the end).

`normed = _norm(x.float()) * (w.float() + weight_offset)`

cast back to the input dtype. When `with_scale`

is False the layer is weightless (used for QK-norm and the token-embedding norm).

## Source code in `vllm/model_executor/models/muse_glimmer.py`


##

`MuseGlimmerVideoPixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer.MuseGlimmerVideoPixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Batched variable-length, variable-resolution video inputs.

## Source code in `vllm/model_executor/models/muse_glimmer.py`


##

`_muse_glimmer_query_prescale(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer._muse_glimmer_query_prescale)

Post-QK-norm query pre-scale (`scale_query_by`

), normalized across the two config schemas so the net query scaling matches the native reference.

HF native modeling computes `scale_query_by = qk_scale_factor / sqrt(head_dim)`

where the NATIVE `qk_scale_factor`

is the raw `params.json`

value (~43.784). The modular HF `text_config`

PRE-FOLDS the `1/sqrt(head_dim)`

factor and ships `qk_scale_factor = 43.784 / sqrt(128) = 3.87`

already, expecting it applied directly. Both must yield the SAME `scale_query_by`

(~3.87), then softmax uses `scaling = head_dim**-0.5`

.

## Precedence

- explicit
`scale_query_by`

(already the final factor) -> use as-is. - else derive from
`qk_scale_factor`

: - if it is already the folded value (
`~= qk_scale_factor/sqrt(hd)`

is NOT what we want; detect the native form and divide) — we decide by magnitude: the native raw value is`folded * sqrt(head_dim)`

. If`qk_scale_factor`

is close to`folded_expected * sqrt(hd)`

we treat it as native and divide; otherwise it is already folded, use directly.

## Source code in `vllm/model_executor/models/muse_glimmer.py`


##

`_muse_glimmer_use_attn_output_gate(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer._muse_glimmer_use_attn_output_gate)

Whether the per-head sigmoid attention output gate is applied. MuseGlimmer ALWAYS applies it; the modular HF `text_config`

omits `use_attn_output_gate`

(reads as `None`

). Missing/None -> True; only explicit `False`

disables.

## Source code in `vllm/model_executor/models/muse_glimmer.py`


##

`_muse_glimmer_use_qk_norm(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer._muse_glimmer_use_qk_norm)

Whether QK-norm is applied. MuseGlimmer ALWAYS applies QK-norm; the modular HF `text_config`

schema simply omits `use_qk_norm`

(reads as `None`

). Treat a missing/None flag as True — only an explicit `False`

disables it.

## Source code in `vllm/model_executor/models/muse_glimmer.py`


##

`_text_config(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.muse_glimmer._text_config)

MuseGlimmer checkpoints may nest the text config under `text_config`

(multimodal `MuseGlimmerConfig`

) or expose it directly (`MuseGlimmerTextConfig`

).