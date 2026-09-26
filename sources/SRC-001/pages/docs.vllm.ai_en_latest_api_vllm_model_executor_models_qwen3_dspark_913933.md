source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen3_dspark/
lastmod: 2026-09-24

#

`vllm.model_executor.models.qwen3_dspark`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark)

Qwen3 DSpark draft model for semi-autoregressive drafting.

DSpark drafts a whole block in one parallel pass (DFlash-style: context-KV precompute + a non-causal query-block forward) and then injects intra-block dependency with a lightweight sequential Markov head.

The parallel backbone is a standard Qwen3 decoder stack reused from the DFlash Qwen3 draft (see qwen3_dflash.py). DSpark adds: * `markov_head`

: low-rank V x r / r x V transition bias added to the base logits, sampled left-to-right by the speculator (the sequential stage). * `confidence_head`

: per-position acceptance-probability estimate.

DSparkMarkovHead and DSparkConfidenceHead are shared with the DSV4-style DSpark model.

Classes:

-
–[DSparkConfidenceHead](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkConfidenceHead)DSpark acceptance-confidence head.

-
–[DSparkMarkovHead](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkMarkovHead)Sequential transition-bias head (low-rank V x r, r x V).

-
–[Qwen3DSparkForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.Qwen3DSparkForCausalLM) -
–[Qwen3DSparkModel](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.Qwen3DSparkModel)DFlash Qwen3 backbone + DSpark Markov / confidence heads.


##

`DSparkConfidenceHead`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkConfidenceHead)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

DSpark acceptance-confidence head.

## Source code in `vllm/model_executor/models/qwen3_dspark.py`


##

`DSparkMarkovHead`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkMarkovHead)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Sequential transition-bias head (low-rank V x r, r x V).

`markov_w1[token]`

embeds the previously sampled token (target vocab, `vocab_size`

); `markov_w2`

projects it to a draft-vocab bias (`draft_vocab_size`

) added to the base draft logits. The two sizes coincide for full-vocab drafts.

Both weights are replicated because the head runs sequentially for every draft position. Sharding them would add an all-reduce and a full-vocab gather to each position.

Methods:

-
–[apply_bias_gathered](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkMarkovHead.apply_bias_gathered)Apply the Markov bias only to selected rows of

`logits`

. -
–[bias](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkMarkovHead.bias)Vocab-size transition bias from a Markov embedding ([B, r] -> [B, V]).

-
–[embed](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkMarkovHead.embed)r-dim Markov embedding of

`token_ids`

([B] -> [B, r]).

## Source code in `vllm/model_executor/models/qwen3_dspark.py`


|
|

###

`apply_bias_gathered(markov_embed, logits, values, index, scale=1.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkMarkovHead.apply_bias_gathered)

Apply the Markov bias only to selected rows of `logits`

.

The caller initializes `logits`

to `-inf`

once for all draft positions. This method scatters the corrected candidate values into that dense buffer so the normal sampler sees the truncated proposal.

## Source code in `vllm/model_executor/models/qwen3_dspark.py`


###

`bias(markov_embed, logits_processor)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.DSparkMarkovHead.bias)

Vocab-size transition bias from a Markov embedding ([B, r] -> [B, V]).

## Source code in `vllm/model_executor/models/qwen3_dspark.py`


##

`Qwen3DSparkForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.Qwen3DSparkForCausalLM)

Bases: [DFlashQwen3ForCausalLM](https://docs.vllm.ai/qwen3_dflash/#vllm.model_executor.models.qwen3_dflash.DFlashQwen3ForCausalLM)

Methods:

-
–[compute_confidence](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.Qwen3DSparkForCausalLM.compute_confidence)Per-position acceptance probability for each drafted token.


## Source code in `vllm/model_executor/models/qwen3_dspark.py`


|
|

###

`compute_confidence(head_hidden, markov_embed)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.Qwen3DSparkForCausalLM.compute_confidence)

Per-position acceptance probability for each drafted token.

## Source code in `vllm/model_executor/models/qwen3_dspark.py`


##

`Qwen3DSparkModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dspark.Qwen3DSparkModel)

Bases: [DFlashQwen3Model](https://docs.vllm.ai/qwen3_dflash/#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Model)

DFlash Qwen3 backbone + DSpark Markov / confidence heads.