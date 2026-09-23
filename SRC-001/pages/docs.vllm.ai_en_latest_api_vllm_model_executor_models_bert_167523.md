source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bert/
lastmod: 2026-09-23

#

`vllm.model_executor.models.bert`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bert)

Classes:

-
–[BertEmbeddingModel](https://docs.vllm.ai#vllm.model_executor.models.bert.BertEmbeddingModel)A model that uses Bert to provide embedding functionalities.

-
–[BertForMaskedLM](https://docs.vllm.ai#vllm.model_executor.models.bert.BertForMaskedLM)Bert with a masked-language-modeling head on top of

`BertModel`

. -
–[BertForSequenceClassification](https://docs.vllm.ai#vllm.model_executor.models.bert.BertForSequenceClassification)A model that uses Bert to provide embedding functionalities.

-
–[BertSpladeSparseEmbeddingModel](https://docs.vllm.ai#vllm.model_executor.models.bert.BertSpladeSparseEmbeddingModel)BertEmbeddingModel + SPLADE sparse embedding.

-
–[SPLADESparsePooler](https://docs.vllm.ai#vllm.model_executor.models.bert.SPLADESparsePooler)SPLADE sparse pooling:


##

`BertEmbeddingModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bert.BertEmbeddingModel)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

A model that uses Bert to provide embedding functionalities.

This class encapsulates the BertModel and provides an interface for embedding operations and customized pooling functions.

Attributes:

-
–`model`

An instance of BertModel used for forward operations.

-
–`_pooler`

An instance of Pooler used for pooling operations.


## Source code in `vllm/model_executor/models/bert.py`


##

`BertForMaskedLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bert.BertForMaskedLM)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Bert with a masked-language-modeling head on top of `BertModel`

.

Produces per-token logits over the vocabulary. In vLLM terms this is a token-level pooling model (`tok_pooling_type="ALL"`

): the encoder output is projected by the MLM head to `vocab_size`

logits for every position, and the token pooler returns one vector per token.

## Source code in `vllm/model_executor/models/bert.py`


|
|

##

`BertForSequenceClassification`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bert.BertForSequenceClassification)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsCrossEncoding](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsCrossEncoding)[SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

A model that uses Bert to provide embedding functionalities.

This class encapsulates the BertModel and provides an interface for embedding operations and customized pooling functions.

Attributes:

-
–`model`

An instance of BertModel used for forward operations.

-
–`_pooler`

An instance of Pooler used for pooling operations.


## Source code in `vllm/model_executor/models/bert.py`


##

`BertSpladeSparseEmbeddingModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bert.BertSpladeSparseEmbeddingModel)

Bases: [BertEmbeddingModel](https://docs.vllm.ai#vllm.model_executor.models.bert.BertEmbeddingModel)

BertEmbeddingModel + SPLADE sparse embedding. - Make logits by self.mlm_head - pooler: SPLADESparsePooler(mlm_head...)

## Source code in `vllm/model_executor/models/bert.py`


|
|

##

`SPLADESparsePooler`

[¶](https://docs.vllm.ai#vllm.model_executor.models.bert.SPLADESparsePooler)

Bases: [Pooler](https://docs.vllm.ai/layers/pooler/#vllm.model_executor.layers.pooler.Pooler)

SPLADE sparse pooling: logits = mlm_head(hidden_states) -> log1p(relu(logits)) -> (max|sum over L) -> [V]

Padding is masked with an attention mask, [CLS]/[SEP] is removed (selected), and then pooled.

## Source code in `vllm/model_executor/models/bert.py`


|
|