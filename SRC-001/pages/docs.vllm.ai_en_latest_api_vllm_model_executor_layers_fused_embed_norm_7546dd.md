source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_embed_norm/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_embed_norm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm)

Replicated input embedding + its fused gather/norm kernels.

Groups the `VLLM_REPLICATE_EMBED`

path in one place: the embedding factory, the predicate that says whether the fusions apply, and the two Triton fusions the full on-rank table unlocks --

`fused_embed_norm`

: gather + a chained RMSNorm (e.g. the first decoder layer's`input_layernorm`

), and`fused_embed_eh_norm`

: gather + pos-0 zeroing + enorm/hnorm + cat, the embed/previous-hidden input norm for a speculative (MTP/eagle) depth layer (the replicated-table analogue of the model-local`fused_eh_norm`

, which takes precomputed embeds).

Self-contained (no model-local imports) so it can live under `layers/`

.

Functions:

-
–[fused_embed_eh_norm](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm.fused_embed_eh_norm)Fused

`cat([enorm(masked embed_table[ids]), hnorm(prev_hidden)])`

-> [N, 2H]. -
–[fused_embed_norm](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm.fused_embed_norm)Fused embedding row gather (

`embed_table[input_ids]`

). -
–[has_full_vocab_on_rank](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm.has_full_vocab_on_rank)Whether

`embedding.weight`

is the whole vocab as a plain [V, H] table. -
–[make_input_embedding](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm.make_input_embedding)Input token embedding with an optional replicated escape hatch.


##

`_fused_embed_eh_norm_kernel(pos_ptr, ids_ptr, table_ptr, table_stride, prev_ptr, prev_stride, enorm_w_ptr, hnorm_w_ptr, eps, out_ptr, out_stride, H, BLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm._fused_embed_eh_norm_kernel)

MTP input fusion with a folded embedding gather: gather `table[ids]`

, zero it at position 0, RMSNorm(embed) with enorm and RMSNorm(prev_hidden) with hnorm, written side-by-side into `out`

([N, 2H]) ready for the eh_proj GEMM. Replaces embedding lookup + where + 2x RMSNorm + cat. Requires the full table on-rank (replicated embedding).

## Source code in `vllm/model_executor/layers/fused_embed_norm.py`


##

`fused_embed_eh_norm(positions, input_ids, embed_table, previous_hidden, enorm_w, hnorm_w, eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm.fused_embed_eh_norm)

Fused `cat([enorm(masked embed_table[ids]), hnorm(prev_hidden)])`

-> [N, 2H].

Folds the embedding row gather into the MTP eh-norm launch; requires the full table on-rank (replicated embedding). Bit-exact vs gathering `embed_table[ input_ids]`

and passing it to the model-local `fused_eh_norm`

.

## Source code in `vllm/model_executor/layers/fused_embed_norm.py`


##

`fused_embed_norm(input_ids, embed_table, chain_weight=None, eps=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm.fused_embed_norm)

Fused embedding row gather (`embed_table[input_ids]`

).

Requires the full vocab on-rank (replicated embedding). When `chain_weight`

is given, also emits `rmsnorm(gathered, chain_weight)`

(the first decoder layer's `input_layernorm`

) as a second output in the same launch, so the returned pair is `(residual, normed_input)`

. Bit-exact vs a plain gather followed by an `RMSNorm`

.

## Source code in `vllm/model_executor/layers/fused_embed_norm.py`


##

`has_full_vocab_on_rank(embedding)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm.has_full_vocab_on_rank)

Whether `embedding.weight`

is the whole vocab as a plain [V, H] table.

The fused gather kernels index the table directly, so they need every row on-rank (`disable_tp`

, or any TP=1 run) and an unquantized weight.

## Source code in `vllm/model_executor/layers/fused_embed_norm.py`


##

`make_input_embedding(num_embeddings, embedding_dim, *, params_dtype=None, quant_config=None, prefix='', tie_word_embeddings=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_embed_norm.make_input_embedding)

Input token embedding with an optional replicated escape hatch.

`VLLM_REPLICATE_EMBED=1`

builds the embedding with `disable_tp`

: the full table lives on every rank and the lookup is a local gather with no mask and no all-reduce, which unlocks the fused gather+norm path. The cost is a full table per rank at TP>1 (no extra memory at TP=1, where vocab-parallel is already unsharded). A replicated, unsharded table cannot be tied to a vocab-parallel `ParallelLMHead`

, so tied word embeddings are rejected at TP>1 (at TP=1 `disable_tp`

is a no-op and tying still works).