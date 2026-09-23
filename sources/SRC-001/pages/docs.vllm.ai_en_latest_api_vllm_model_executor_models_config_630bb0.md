source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/config/
lastmod: 2026-09-23

#

`vllm.model_executor.models.config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config)

Classes:

-
–[ColQwen3_5Config](https://docs.vllm.ai#vllm.model_executor.models.config.ColQwen3_5Config)Apply the attention contract declared by a ColQwen3.5 checkpoint.

-
–[DiffusionGemmaModelForBlockDiffusionConfig](https://docs.vllm.ai#vllm.model_executor.models.config.DiffusionGemmaModelForBlockDiffusionConfig) -
–[Gemma4Config](https://docs.vllm.ai#vllm.model_executor.models.config.Gemma4Config) -
–[HybridAttentionMambaModelConfig](https://docs.vllm.ai#vllm.model_executor.models.config.HybridAttentionMambaModelConfig) -
–[JinaEmbeddingsV5ModelConfig](https://docs.vllm.ai#vllm.model_executor.models.config.JinaEmbeddingsV5ModelConfig)Config handler for Jina Embeddings V5 embedding models.

-
–[KimiK3ForConditionalGenerationConfig](https://docs.vllm.ai#vllm.model_executor.models.config.KimiK3ForConditionalGenerationConfig)Route MXFP4-checkpointed Kimi-K3 MoE experts to the MXFP4 interface.

-
–[LlamaNemotronVLConfig](https://docs.vllm.ai#vllm.model_executor.models.config.LlamaNemotronVLConfig)Config handler for LlamaNemotronVL embedding models.

-
–[MambaModelConfig](https://docs.vllm.ai#vllm.model_executor.models.config.MambaModelConfig) -
–[NemotronHForCausalLMConfig](https://docs.vllm.ai#vllm.model_executor.models.config.NemotronHForCausalLMConfig) -
–[Qwen3_5ForConditionalGenerationConfig](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen3_5ForConditionalGenerationConfig) -
–[Qwen4ExpForConditionalGenerationConfig](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen4ExpForConditionalGenerationConfig)Apply the Qwen3.5 hybrid-cache contract to Qwen4Exp.

-
–[Qwen4ExpMTPConfig](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen4ExpMTPConfig)Preserve MRoPE for a VL target and use 1D RoPE for a text target.

-
–[UnlimitedOCRForCausalLMConfig](https://docs.vllm.ai#vllm.model_executor.models.config.UnlimitedOCRForCausalLMConfig)

##

`ColQwen3_5Config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.ColQwen3_5Config)

Bases: [Qwen3_5ForConditionalGenerationConfig](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen3_5ForConditionalGenerationConfig)

Apply the attention contract declared by a ColQwen3.5 checkpoint.

## Source code in `vllm/model_executor/models/config.py`


##

`DiffusionGemmaModelForBlockDiffusionConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.DiffusionGemmaModelForBlockDiffusionConfig)

Bases: `VerifyAndUpdateConfig`


Methods:

-
–[verify_and_update_config](https://docs.vllm.ai#vllm.model_executor.models.config.DiffusionGemmaModelForBlockDiffusionConfig.verify_and_update_config)Set up the diffusion config and defaults for DiffusionGemma.


## Source code in `vllm/model_executor/models/config.py`


###

`verify_and_update_config(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.DiffusionGemmaModelForBlockDiffusionConfig.verify_and_update_config)

Set up the diffusion config and defaults for DiffusionGemma.

Auto-creates DiffusionConfig from the HF config when the user didn't pass `--diffusion-config`

. Diffusion sampling params are read straight from generation_config.json at sampler-build time (see DiffusionGemma's custom_sampler), not injected here.

## Source code in `vllm/model_executor/models/config.py`


##

`Gemma4Config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.Gemma4Config)

Bases: `VerifyAndUpdateConfig`


Methods:

-
–[verify_and_update_config](https://docs.vllm.ai#vllm.model_executor.models.config.Gemma4Config.verify_and_update_config)Configure attention for heterogeneous head dimensions.


## Source code in `vllm/model_executor/models/config.py`


###

`verify_and_update_config(vllm_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.Gemma4Config.verify_and_update_config)

Configure attention for heterogeneous head dimensions.

Gemma4 uses different head dimensions for sliding window vs full attention layers. The default FA3 on Hopper cannot handle head_dim > 256, which causes mixed backend selection and numerical divergence.

When FA4 is available we force it for ALL layers, giving a uniform kernel path and avoiding the mixed FA3+FA4 penalty. When FA4 is not available we fall back to Triton.

## Source code in `vllm/model_executor/models/config.py`


##

`HybridAttentionMambaModelConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.HybridAttentionMambaModelConfig)

Bases: `VerifyAndUpdateConfig`


Methods:

-
–[verify_and_update_config](https://docs.vllm.ai#vllm.model_executor.models.config.HybridAttentionMambaModelConfig.verify_and_update_config)Perform early validation and setup for hybrid attention/mamba models.


## Source code in `vllm/model_executor/models/config.py`


###

`verify_and_update_config(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.HybridAttentionMambaModelConfig.verify_and_update_config)

Perform early validation and setup for hybrid attention/mamba models.

Block size alignment with mamba page sizes is handled later by Platform.update_block_size_for_backend(), which runs after model layers are constructed and the attention backend is known.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.HybridAttentionMambaModelConfig.verify_and_update_config(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)vLLM Config


## Source code in `vllm/model_executor/models/config.py`


##

`JinaEmbeddingsV5ModelConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.JinaEmbeddingsV5ModelConfig)

Bases: `VerifyAndUpdateConfig`


Config handler for Jina Embeddings V5 embedding models.

Methods:

-
–[verify_and_update_model_config](https://docs.vllm.ai#vllm.model_executor.models.config.JinaEmbeddingsV5ModelConfig.verify_and_update_model_config)Enable the bidirectional encoder backbone for -nano checkpoints.


## Source code in `vllm/model_executor/models/config.py`


###

`verify_and_update_model_config(model_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.JinaEmbeddingsV5ModelConfig.verify_and_update_model_config)

Enable the bidirectional encoder backbone for -nano checkpoints.

The V5 family ships more than one backbone under a single `architectures`

entry: the `-small`

variants are Qwen3 decoders, while `-nano`

is a bidirectional EuroBERT encoder. Upstream ships a separate `configuration_*.py`

per repository, so the config carries no backbone field and the encoder variants are only identifiable by `is_decoder=False`

. For encoder checkpoints, set `is_causal=False`

so the Llama backbone uses EncoderOnlyAttention; `JinaEmbeddingsV5Model`

then dispatches to its encoder implementation.

## Source code in `vllm/model_executor/models/config.py`


##

`KimiK3ForConditionalGenerationConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.KimiK3ForConditionalGenerationConfig)

Bases: `VerifyAndUpdateConfig`


Route MXFP4-checkpointed Kimi-K3 MoE experts to the MXFP4 interface.

Kimi-K3 ships its routed experts as compressed-tensors `mxfp4-pack-quantized`

(`quant_method="compressed-tensors"`

), which lands them on `CompressedTensorsW4A4Mxfp4MoEMethod`

and its narrow kernel selection. Rewriting `quant_method`

to `"mxfp4"`

selects `Mxfp4Config`

(hence `Mxfp4MoEMethod`

) with its full backend set, while any non-MXFP4 checkpoint is left untouched. Covers both the main model and the MTP draft.

`model_arch_config.quantization_config`

is a separate dict, snapshotted in `ModelConfig.__init__`

before this hook runs, and it is what `_verify_quantization`

reads when resolving the quant method. Patch it alongside the hf configs so the rewrite lands before resolution; otherwise the main model still resolves to compressed-tensors.

## Source code in `vllm/model_executor/models/config.py`


##

`LlamaNemotronVLConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.LlamaNemotronVLConfig)

Bases: `VerifyAndUpdateConfig`


Config handler for LlamaNemotronVL embedding models.

## Source code in `vllm/model_executor/models/config.py`


##

`MambaModelConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.MambaModelConfig)

Bases: `VerifyAndUpdateConfig`


Methods:

-
–[verify_and_update_config](https://docs.vllm.ai#vllm.model_executor.models.config.MambaModelConfig.verify_and_update_config)Enable FULL_AND_PIECEWISE cuda graph mode by default (required


## Source code in `vllm/model_executor/models/config.py`


###

`verify_and_update_config(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.MambaModelConfig.verify_and_update_config)

Enable FULL_AND_PIECEWISE cuda graph mode by default (required to get good performance for mamba layers in V1).

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.MambaModelConfig.verify_and_update_config(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)vLLM Config


## Source code in `vllm/model_executor/models/config.py`


##

`NemotronHForCausalLMConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.NemotronHForCausalLMConfig)

Bases: `VerifyAndUpdateConfig`


Methods:

-
–[update_mamba_ssm_cache_dtype](https://docs.vllm.ai#vllm.model_executor.models.config.NemotronHForCausalLMConfig.update_mamba_ssm_cache_dtype)Update mamba_ssm_cache_dtype for NemotronH models when set to 'auto'


Attributes:

-
([DEFAULT_MAMBA_SSM_CACHE_DTYPE](https://docs.vllm.ai#vllm.model_executor.models.config.NemotronHForCausalLMConfig.DEFAULT_MAMBA_SSM_CACHE_DTYPE)`MambaDType`

) –Only

`float32`

is known to have no accuracy issues by default.

## Source code in `vllm/model_executor/models/config.py`


###

`DEFAULT_MAMBA_SSM_CACHE_DTYPE = 'float32'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.NemotronHForCausalLMConfig.DEFAULT_MAMBA_SSM_CACHE_DTYPE)

Only `float32`

is known to have no accuracy issues by default.

###

`update_mamba_ssm_cache_dtype(*, cache_config, hf_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.NemotronHForCausalLMConfig.update_mamba_ssm_cache_dtype)

Update mamba_ssm_cache_dtype for NemotronH models when set to 'auto' (or not explicitly set), to the value specified in the HF config, or to `float32`

if not specified.

## Source code in `vllm/model_executor/models/config.py`


##

`Qwen3_5ForConditionalGenerationConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen3_5ForConditionalGenerationConfig)

Bases: `VerifyAndUpdateConfig`


Methods:

-
–[verify_and_update_config](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen3_5ForConditionalGenerationConfig.verify_and_update_config)Update mamba_ssm_cache_dtype for Qwen3.5 models when set to 'auto'


## Source code in `vllm/model_executor/models/config.py`


###

`verify_and_update_config(vllm_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen3_5ForConditionalGenerationConfig.verify_and_update_config)

Update mamba_ssm_cache_dtype for Qwen3.5 models when set to 'auto' (or not explicitly set), to the value specified in the HF config's mamba_ssm_dtype field. Warn if the user explicitly overrides it to a different value.

## Source code in `vllm/model_executor/models/config.py`


##

`Qwen4ExpForConditionalGenerationConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen4ExpForConditionalGenerationConfig)

Bases: [Qwen3_5ForConditionalGenerationConfig](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen3_5ForConditionalGenerationConfig)

Apply the Qwen3.5 hybrid-cache contract to Qwen4Exp.

## Source code in `vllm/model_executor/models/config.py`


##

`Qwen4ExpMTPConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen4ExpMTPConfig)

Bases: [Qwen4ExpForConditionalGenerationConfig](https://docs.vllm.ai#vllm.model_executor.models.config.Qwen4ExpForConditionalGenerationConfig)

Preserve MRoPE for a VL target and use 1D RoPE for a text target.

## Source code in `vllm/model_executor/models/config.py`


##

`UnlimitedOCRForCausalLMConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.UnlimitedOCRForCausalLMConfig)

Bases: `VerifyAndUpdateConfig`


Methods:

-
–[verify_and_update_config](https://docs.vllm.ai#vllm.model_executor.models.config.UnlimitedOCRForCausalLMConfig.verify_and_update_config)Configure Unlimited-OCR attention backends for R-SWA and vision.


## Source code in `vllm/model_executor/models/config.py`


|
|

###

`verify_and_update_config(vllm_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.config.UnlimitedOCRForCausalLMConfig.verify_and_update_config)

Configure Unlimited-OCR attention backends for R-SWA and vision.

Backend selection — controlled by the standard `--attention-config`

CLI argument (priority order):

-
`--attention-config '{"backend": "FLASH_ATTN"}'`

→ FA4 + rswa_mask_mod. Exact token-level R-SWA.`flash_attn_version`

is forced to 4 if not already set (R-SWA mask_mod requires FA4; FA3 cannot express it). Raises if FA4 is not available on this device. -
`--attention-config '{"backend": "FLEX_ATTENTION"}'`

→ FlexAttention R-SWA via Triton block mask. -
`--attention-config '{"backend": "TRITON_ATTN"}'`

→ Triton unified attention with an R-SWA decode mask. -
`--attention-config '{"backend": "auto"}'`

(or omitted) → Auto-detect: FA4 if available (H20/H100 SM90), else TritonAttention.

Regardless of backend, prefix caching is disabled for this model: R-SWA decode-phase KV is not a pure causal function of the prefix (so decode blocks are not reusable), and single-turn image-led OCR prompts rarely hit the prefix cache.

Example — force FlexAttention even on a machine with FA4::

```
vllm serve baidu/Unlimited-OCR \
--attention-config '{"backend": "FLEX_ATTENTION"}'
```


## Source code in `vllm/model_executor/models/config.py`


|
|