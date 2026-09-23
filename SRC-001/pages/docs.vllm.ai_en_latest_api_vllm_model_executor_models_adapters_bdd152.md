source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/
lastmod: 2026-09-23

#

`vllm.model_executor.models.adapters`

[¶](https://docs.vllm.ai#vllm.model_executor.models.adapters)

Functions:

-
–[as_embedding_model](https://docs.vllm.ai#vllm.model_executor.models.adapters.as_embedding_model)Subclass an existing vLLM model to support embeddings.

-
–[as_seq_cls_model](https://docs.vllm.ai#vllm.model_executor.models.adapters.as_seq_cls_model)Subclass an existing vLLM model to support classify and score tasks.


##

`_disable_seq_cls_loading_on_inner_model(language_model, is_vlm)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.adapters._disable_seq_cls_loading_on_inner_model)

Context manager to temporarily disable sequence classification loading on inner VLM models to prevent recursive seq_cls_model_loader calls.

## Source code in `vllm/model_executor/models/adapters.py`


##

`_get_language_model_for_seq_cls(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.adapters._get_language_model_for_seq_cls)

Get the language model component for sequence classification conversion. For VLMs, returns the inner language model. For standard LLMs, returns model itself.

## Source code in `vllm/model_executor/models/adapters.py`


##

`_load_dense_weights(linear, folder, model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.adapters._load_dense_weights)

Load weights using vLLM's weight_loader pattern.

## Source code in `vllm/model_executor/models/adapters.py`


##

`_load_st_projector(model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.adapters._load_st_projector)

Load Sentence-Transformers Dense projection layers.

## Source code in `vllm/model_executor/models/adapters.py`


##

`_resolve_num_labels(hf_config, text_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.adapters._resolve_num_labels)

Resolve the label count for a sequence classification head.

`PretrainedConfig.num_labels`

is derived from `id2label`

, which always carries a default of two entries. Composite configs (such as multimodal checkpoints) declare their label space on the top-level config, so reading `num_labels`

from `get_text_config()`

silently returns that default and builds a score head of the wrong size.

Prefer the top-level config whenever it declares a label space of its own, mirroring the `classifier_from_token`

/ `method`

lookups in `as_seq_cls_model`

.

## Source code in `vllm/model_executor/models/adapters.py`


##

`as_embedding_model(cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.adapters.as_embedding_model)

Subclass an existing vLLM model to support embeddings.

By default, the embeddings of the whole prompt are extracted from the normalized hidden state corresponding to the last token.

## Note

We assume that no extra layers are added to the original model; please implement your own model if this is not the case.

## Source code in `vllm/model_executor/models/adapters.py`


##

`as_seq_cls_model(cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.adapters.as_seq_cls_model)

Subclass an existing vLLM model to support classify and score tasks.

By default, the class probabilities are extracted from the softmaxed hidden state corresponding to the last token.

## Note

We assume that the classification head is a single linear layer stored as the attribute `score`

of the top-level model; please implement your own model if this is not the case.

## Source code in `vllm/model_executor/models/adapters.py`


|
|