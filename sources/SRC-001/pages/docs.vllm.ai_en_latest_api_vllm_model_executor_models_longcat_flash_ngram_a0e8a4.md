source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/longcat_flash_ngram/
lastmod: 2026-09-24

#

`vllm.model_executor.models.longcat_flash_ngram`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram)

Inference-only LongCat-Flash-Lite (n-gram embedding) model.

`LongcatFlashNgramForCausalLM`

is LongCat-Flash (MLA dual-attention + zero-expert MoE + YaRN) plus an n-gram embedding input layer: each position's embedding fuses the token embedding with hashed embeddings of the preceding `n`

tokens. That per-request token history is isolated in a Model-Runner-V2 :class:`LongcatNgramModelState`

(mirroring `DiffusionGemmaModelState`

), so `get_model_state_cls`

makes the model MRV2-only.

Classes:

-
–[FlashNgramModel](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.FlashNgramModel)FlashModel whose input embedding is an :class:

`NgramEmbedding`

. -
–[LongcatFlashNgramForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.LongcatFlashNgramForCausalLM)LongCat-Flash-Lite for causal LM (MRV2-only, n-gram embedding).

-
–[LongcatNgramModelState](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.LongcatNgramModelState) -
–[NgramEmbedding](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.NgramEmbedding)Token embedding fused with hashed n-gram embeddings.


##

`FlashNgramModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.FlashNgramModel)

Bases: [FlashModel](https://docs.vllm.ai/longcat_flash/#vllm.model_executor.models.longcat_flash.FlashModel)

FlashModel whose input embedding is an :class:`NgramEmbedding`

.

## Source code in `vllm/model_executor/models/longcat_flash_ngram.py`


##

`LongcatFlashNgramForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.LongcatFlashNgramForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)[SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

LongCat-Flash-Lite for causal LM (MRV2-only, n-gram embedding).

## Source code in `vllm/model_executor/models/longcat_flash_ngram.py`


##

`LongcatNgramModelState`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.LongcatNgramModelState)

Bases: [DefaultModelState](https://docs.vllm.ai/v1/worker/gpu/model_states/default/#vllm.v1.worker.gpu.model_states.default.DefaultModelState)

Attributes:

-
–[supports_prompt_embeds](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.LongcatNgramModelState.supports_prompt_embeds)Per-request n-gram token history for LongCat-Flash-Lite.


## Source code in `vllm/model_executor/models/longcat_flash_ngram.py`


|
|

###

`supports_prompt_embeds = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.LongcatNgramModelState.supports_prompt_embeds)

Per-request n-gram token history for LongCat-Flash-Lite.

Maintains a small CPU-side per-slot context (last `n-1`

processed tokens) and a persistent `inputs_embeds`

buffer. `prepare_inputs`

computes the fused n-gram embedding per request into the buffer, handed to the model forward as `inputs_embeds`

.

###

`_compute_oe_ids(input_batch)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.LongcatNgramModelState._compute_oe_ids)

Batched global n-gram ids `[num_tokens, num_embedders]`

.

Assembles an ephemeral per-request token table (`[n-1] context ++ current tokens`

, EOS-negated) and runs the `ngram_compute_n_gram_ids`

CUDA kernel for the whole batch, then rolls each slot's context forward.

## Source code in `vllm/model_executor/models/longcat_flash_ngram.py`


##

`NgramEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.NgramEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Token embedding fused with hashed n-gram embeddings.

TP-sharded: the `k*(n-1)`

per-embedder tables are concatenated into one :class:`VocabParallelEmbedding`

(`oe_embedder`

) with per-embedder offsets, and the projections are stacked into one `oe_projection`

applied with a single `bmm`

. Hashing math is ported from the HF reference.

Methods:

-
–[embed_batched](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.NgramEmbedding.embed_batched)Fused n-gram embedding for a flat batch given precomputed ids.

-
–[load_weight](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.NgramEmbedding.load_weight)Split a per-embedder checkpoint weight into the sharded layout.


## Source code in `vllm/model_executor/models/longcat_flash_ngram.py`


|
|

###

`embed_batched(input_ids, oe_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.NgramEmbedding.embed_batched)

Fused n-gram embedding for a flat batch given precomputed ids.

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.NgramEmbedding.embed_batched(input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[num_tokens]`

current token per position. -

(`oe_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.NgramEmbedding.embed_batched(oe_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[num_tokens, num_embedders]`

global (offset) n-gram ids, as produced by the`ngram_compute_n_gram_ids`

kernel.

Returns: `[num_tokens, hidden]`

.

## Source code in `vllm/model_executor/models/longcat_flash_ngram.py`


###

`load_weight(weight_name, loaded_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.longcat_flash_ngram.NgramEmbedding.load_weight)

Split a per-embedder checkpoint weight into the sharded layout.

Returns the destination parameter's qualified name (relative to the enclosing model) so the caller can mark it loaded for completeness checks.