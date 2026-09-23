source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colqwen3_5/
lastmod: 2026-09-23

#

`vllm.model_executor.models.colqwen3_5`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5)

ColQwen3.5 late interaction model for multi-modal retrieval and reranking.

ColQwen3.5 extends Qwen3.5 with a ColBERT-style late interaction head, producing per-token embeddings for both text and image inputs. It uses MaxSim scoring for retrieval/reranking tasks.

This model supports the "token_embed" pooling task and is designed for multi-vector retrieval of documents containing both text and images.

Reference: https://arxiv.org/abs/2407.01449 (ColPali) Based on: Qwen3.5 backbone with custom text projection

Target models: - athrael-soju/colqwen3.5-4.5B-v3 - vultr/VultronRetrieverPrime-Qwen3.5-8B

Classes:

-
–[ColQwen3_5Model](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5Model)ColQwen3.5 late interaction model for multi-modal retrieval/reranking.

-
–[ColQwen3_5ProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5ProcessingInfo)Processing info for ColQwen3.5 models.


##

`ColQwen3_5Model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5Model)

Bases:

, [Qwen3_5ForConditionalGeneration](https://docs.vllm.ai/qwen3_5/#vllm.model_executor.models.qwen3_5.Qwen3_5ForConditionalGeneration)[SupportsLateInteraction](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLateInteraction)

ColQwen3.5 late interaction model for multi-modal retrieval/reranking.

This model extends Qwen3_5ForConditionalGeneration with a ColBERT-style linear projection layer for per-token embeddings. It supports: - "token_embed" task: Per-token embeddings for late interaction scoring

The model produces L2-normalized per-token embeddings by: 1. Running the Qwen3.5 backbone (vision + language) to get hidden states 2. Projection and L2-normalization via the pooler (TokenEmbeddingPoolerHead)

Attributes:

-
–`custom_text_proj`

Linear projection from hidden_size to embed_dim. This is passed to the pooler as pooler.head.projector.


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5Model.forward)Run forward pass returning hidden states for pooler.

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5Model.load_weights)Load weights with special handling for projection layer.


## Source code in `vllm/model_executor/models/colqwen3_5.py`


|
|

###

`_is_proj_weight(name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5Model._is_proj_weight)

Check if a weight name belongs to the projection layer.

###

`forward(input_ids, positions, intermediate_tensors=None, inputs_embeds=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5Model.forward)

Run forward pass returning hidden states for pooler.

## Source code in `vllm/model_executor/models/colqwen3_5.py`


###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5Model.load_weights)

Load weights with special handling for projection layer.

## Source code in `vllm/model_executor/models/colqwen3_5.py`


##

`ColQwen3_5ProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5ProcessingInfo)

Bases: `Qwen3_5ProcessingInfo`


Processing info for ColQwen3.5 models.

ColQwen3.5 models use custom HuggingFace processors (e.g. ColQwen3_5Processor) that are incompatible with vLLM's Qwen3VLMultiModalProcessor. We override get_hf_config() and get_hf_processor() to skip the strict type check and force the standard Qwen3VLProcessor.

## Source code in `vllm/model_executor/models/colqwen3_5.py`


###

`_supports_video`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.colqwen3_5.ColQwen3_5ProcessingInfo._supports_video)

Check if the HF processor supports video inputs.