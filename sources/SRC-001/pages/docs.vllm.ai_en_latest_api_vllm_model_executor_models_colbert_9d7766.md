source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colbert/
lastmod: 2026-09-24

#

`vllm.model_executor.models.colbert`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert)

ColBERT late interaction model for retrieval and reranking.

ColBERT uses per-token embeddings and late interaction (MaxSim) scoring instead of single-vector representations or cross-encoder concatenation.

This module provides:

- :class:
`ColBERTMixin`

— mixin that adds ColBERT late-interaction support to any embedding model. - :class:
`ColBERTModel`

— ColBERT with BERT backbone (original architecture). - :class:
`ColBERTModernBertModel`

— ColBERT with ModernBERT backbone. - :class:
`ColBERTJinaRobertaModel`

— ColBERT with Jina XLM-RoBERTa backbone.

Reference: https://arxiv.org/abs/2004.12832

Classes:

-
–[ColBERTJinaRobertaModel](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTJinaRobertaModel)ColBERT late interaction model with Jina XLM-RoBERTa backbone.

-
–[ColBERTLfm2Model](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTLfm2Model)ColBERT late interaction model with LFM2 backbone.

-
–[ColBERTMixin](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin)Mixin that adds ColBERT late interaction support to any embedding model.

-
–[ColBERTModel](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTModel)ColBERT late interaction model with BERT backbone.

-
–[ColBERTModernBertModel](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTModernBertModel)ColBERT late interaction model with ModernBERT backbone.


##

`ColBERTJinaRobertaModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTJinaRobertaModel)

Bases:

, [ColBERTMixin](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin)[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

ColBERT late interaction model with Jina XLM-RoBERTa backbone.

For `jinaai/jina-colbert-v2`

and similar models.

## Source code in `vllm/model_executor/models/colbert.py`


##

`ColBERTLfm2Model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTLfm2Model)

Bases:

, [ColBERTMixin](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin)

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [HasInnerState](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.HasInnerState)[IsHybrid](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.IsHybrid)

ColBERT late interaction model with LFM2 backbone.

For `LiquidAI/LFM2-ColBERT-350M`

and similar models.

The projection is auto-loaded from sentence-transformers `1_Dense/`

when not present in the main checkpoint.

## Source code in `vllm/model_executor/models/colbert.py`


|
|

##

`ColBERTMixin`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[SupportsLateInteraction](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLateInteraction)

Mixin that adds ColBERT late interaction support to any embedding model.

ColBERT (Contextualized Late Interaction over BERT) uses per-token embeddings with a linear projection layer. This mixin provides:

- ColBERT linear projection initialisation / lazy creation
- Weight loading helpers for the projection layer
- A builder for the token-embedding pooler

**Integration:**

- Inherit from both
`ColBERTMixin`

and`nn.Module`

. - In
`__init__`

: call`super().__init__()`

, then :meth:`_init_colbert_components`

, then create`self.model`

(the backbone) and`self.pooler`

via :meth:`_build_colbert_pooler`

. - In
`load_weights`

: use :meth:`_load_colbert_weights`

to separate the ColBERT projection weight, then delegate the rest to the backbone.

Methods:

-
–[get_colbert_dim_from_config](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin.get_colbert_dim_from_config)Extract ColBERT dimension from a HuggingFace config.


## Source code in `vllm/model_executor/models/colbert.py`


|
|

###

`_build_colbert_linear()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._build_colbert_linear)

Build the ColBERT linear projection layer.

## Source code in `vllm/model_executor/models/colbert.py`


###

`_build_colbert_pooler(pooler_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._build_colbert_pooler)

Build pooler for ColBERT token embeddings.

When `colbert_linear`

is set, it is used as the projector. Otherwise `pooler_for_token_embed`

falls back to auto-loading sentence-transformers Dense layers (`1_Dense/`

etc.).

## Source code in `vllm/model_executor/models/colbert.py`


###

`_init_colbert_components(hidden_size, colbert_dim, head_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._init_colbert_components)

Initialise ColBERT projection layer.

Parameters:

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._init_colbert_components(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Hidden dimension of the encoder backbone.

-

(`colbert_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._init_colbert_components(colbert_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneOutput dimension for ColBERT embeddings. If

`None`

, will be inferred from weights during loading (or auto-loaded from sentence-transformers Dense layers). -

(`head_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._init_colbert_components(head_dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Data type for the projection layer.


## Source code in `vllm/model_executor/models/colbert.py`


###

`_load_colbert_weights(weights, colbert_weight_names=('linear.weight', 'colbert_linear.weight'))`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._load_colbert_weights)

Separate and load ColBERT projection weights.

Scans *weights* for entries whose name ends with one of *colbert_weight_names*. The matching weight is loaded into `self.colbert_linear`

(creating it first if `colbert_dim`

was not known at init time).

Parameters:

-

(`weights`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._load_colbert_weights(weights))

) –[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Iterable of

`(name, tensor)`

weight pairs. -

(`colbert_weight_names`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin._load_colbert_weights(colbert_weight_names))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), ...]`('linear.weight', 'colbert_linear.weight')`

) –Suffixes that identify the ColBERT linear weight.


Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]`(remaining_weights, loaded_names)`

— the weights that were -

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]**not**consumed and the set of names that were loaded.

## Source code in `vllm/model_executor/models/colbert.py`


###

`get_colbert_dim_from_config(hf_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin.get_colbert_dim_from_config)

Extract ColBERT dimension from a HuggingFace config.

Checks `colbert_dim`

, `dim`

and `projection_dim`

in that order.

## Source code in `vllm/model_executor/models/colbert.py`


##

`ColBERTModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTModel)

Bases:

, [ColBERTMixin](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin)[BertEmbeddingModel](https://docs.vllm.ai/bert/#vllm.model_executor.models.bert.BertEmbeddingModel)

ColBERT late interaction model with BERT backbone.

Supports the `token_embed`

task (per-token embeddings for late interaction). MaxSim scoring is computed externally.

## Source code in `vllm/model_executor/models/colbert.py`


##

`ColBERTModernBertModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTModernBertModel)

Bases:

, [ColBERTMixin](https://docs.vllm.ai#vllm.model_executor.models.colbert.ColBERTMixin)[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

ColBERT late interaction model with ModernBERT backbone.

For `lightonai/GTE-ModernColBERT-v1`

and similar models. The projection is auto-loaded from sentence-transformers `1_Dense/`

when not present in the main checkpoint.