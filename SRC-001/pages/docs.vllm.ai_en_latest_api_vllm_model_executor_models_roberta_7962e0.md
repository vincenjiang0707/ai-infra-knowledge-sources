source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/roberta/
lastmod: 2026-09-23

#

`vllm.model_executor.models.roberta`

[¶](https://docs.vllm.ai#vllm.model_executor.models.roberta)

Classes:

-
–[BgeM3EmbeddingModel](https://docs.vllm.ai#vllm.model_executor.models.roberta.BgeM3EmbeddingModel)A model that extends RobertaEmbeddingModel with sparse embeddings.

-
–[RobertaClassificationHead](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaClassificationHead)Head for sentence-level classification tasks.

-
–[RobertaEmbeddingModel](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaEmbeddingModel)A model that uses Roberta to provide embedding functionalities.

-
–[RobertaForSequenceClassification](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaForSequenceClassification)A model that uses Roberta to provide embedding functionalities.

-
–[RobertaForTokenClassification](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaForTokenClassification)A model that uses Roberta to provide token classification.


##

`BgeM3EmbeddingModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.roberta.BgeM3EmbeddingModel)

Bases: [RobertaEmbeddingModel](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaEmbeddingModel)

A model that extends RobertaEmbeddingModel with sparse embeddings.

This class supports loading an additional sparse_linear.pt file to create sparse embeddings as described in https://arxiv.org/abs/2402.03216

## Source code in `vllm/model_executor/models/roberta.py`


|
|

##

`RobertaClassificationHead`

[¶](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaClassificationHead)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Head for sentence-level classification tasks.

## Source code in `vllm/model_executor/models/roberta.py`


##

`RobertaEmbeddingModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaEmbeddingModel)

Bases: [BertEmbeddingModel](https://docs.vllm.ai/bert/#vllm.model_executor.models.bert.BertEmbeddingModel)

A model that uses Roberta to provide embedding functionalities.

## Source code in `vllm/model_executor/models/roberta.py`


##

`RobertaForSequenceClassification`

[¶](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaForSequenceClassification)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[SupportsCrossEncoding](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsCrossEncoding)

A model that uses Roberta to provide embedding functionalities.

This class encapsulates the BertModel and provides an interface for embedding operations and customized pooling functions.

Attributes:

-
–`roberta`

An instance of BertModel used for forward operations.

-
–`_pooler`

An instance of Pooler used for pooling operations.


## Source code in `vllm/model_executor/models/roberta.py`


##

`RobertaForTokenClassification`

[¶](https://docs.vllm.ai#vllm.model_executor.models.roberta.RobertaForTokenClassification)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

A model that uses Roberta to provide token classification.

Mirrors BertForTokenClassification, swapping in RobertaEmbedding for the RoBERTa/XLM-RoBERTa position-embedding offset and weight layout.

Also registered as XLMRobertaForTokenClassification since XLM-RoBERTa checkpoints share RoBERTa's architecture and `roberta.*`

weight prefix.