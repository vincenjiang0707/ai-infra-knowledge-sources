source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_tying/
lastmod: 2026-09-24

#

`vllm.model_executor.model_loader.weight_tying`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_tying)

Reconcile word embedding tying with what the checkpoint actually contains.

Functions:

-
–[maybe_retie_word_embeddings](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_tying.maybe_retie_word_embeddings)Re-tie word embeddings that


##

`_get_untied_lm_head(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_tying._get_untied_lm_head)

Locate an `lm_head`

that could be tied to the input embeddings.

Returns `None`

unless the model has exactly one of each, so that models with several heads (such as MTP) or with already tied weights are left alone. Both are found by type rather than by name, because `get_input_embeddings`

takes different arguments on multimodal models and the `lm_head`

of a multimodal model is nested inside its language model.

A quantized `lm_head`

is also left alone. Its weights may be packed under another name, and online quantization creates them after loading, so neither their contents nor whether they were loaded can be established here. Note that this is a property of the layer, not of the model: most quantized models leave the `lm_head`

and the input embeddings unquantized.

## Source code in `vllm/model_executor/model_loader/weight_tying.py`


##

`maybe_retie_word_embeddings(model, model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_tying.maybe_retie_word_embeddings)

Re-tie word embeddings that [ModelConfig.maybe_untie_word_embeddings](https://docs.vllm.ai/config/#vllm.config.ModelConfig.maybe_untie_word_embeddings) untied, if the loaded `lm_head`

turned out to be identical to the input embeddings after all.

Checkpoints produced by quantization or fine-tuning tooling often keep a redundant copy of the tied `lm_head`

. Sharing the storage again reclaims the memory it would otherwise cost.