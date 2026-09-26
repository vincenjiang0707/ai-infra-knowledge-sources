source: https://docs.vllm.ai/en/latest/models/pooling_models/token_embed/
lastmod: 2026-09-24

# Token Embedding Usages[¶](https://docs.vllm.ai#token-embedding-usages)

## Summary[¶](https://docs.vllm.ai#summary)

- Model Usage: Token classification models
- Pooling Tasks:
`token_embed`

- Offline APIs:
`LLM.encode(..., pooling_task="token_embed")`


- Online APIs:
- Pooling API (
`/pooling`

)

- Pooling API (

The difference between the (sequence) embedding task and the token embedding task is that (sequence) embedding outputs one embedding for each sequence, while token embedding outputs an embedding for each token.

Many embedding models support both (sequence) embedding and token embedding. For further details on (sequence) embedding, please refer to [this page](https://docs.vllm.ai/embed/).

Note

Pooling multitask support has been removed since v0.21. When the default pooling task (embed) is not what you want, you need to manually specify it via `PoolerConfig(task="token_embed")`

offline or `--pooler-config.task token_embed`

online.

## Typical Use Cases[¶](https://docs.vllm.ai#typical-use-cases)

### Multi-Vector Retrieval[¶](https://docs.vllm.ai#multi-vector-retrieval)

For implementation examples, see:

Offline: [ examples/pooling/token_embed/multi_vector_retrieval_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_embed/multi_vector_retrieval_offline.py)

Online: [ examples/pooling/token_embed/multi_vector_retrieval_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_embed/multi_vector_retrieval_online.py)

### Late interaction[¶](https://docs.vllm.ai#late-interaction)

Similarity scores can be computed using late interaction between two input prompts via the score API. For more information, see [Score API](https://docs.vllm.ai/scoring/).

### Extract last hidden states[¶](https://docs.vllm.ai#extract-last-hidden-states)

Models of any architecture can be converted into embedding models using `--convert embed`

. Token embedding can then be used to extract the last hidden states from these models.

## Supported Models[¶](https://docs.vllm.ai#supported-models)

### Text-only Models[¶](https://docs.vllm.ai#text-only-models)

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`ColBERTLfm2Model`

`LiquidAI/LFM2-ColBERT-350M`

`ColBERTModernBertModel`

`lightonai/GTE-ModernColBERT-v1`

`ColBERTJinaRobertaModel`

`jinaai/jina-colbert-v2`

`HF_ColBERT`

`answerdotai/answerai-colbert-small-v1`

, `colbert-ir/colbertv2.0`

`*Model`

C,`*ForCausalLM`

C, etc.### Multimodal Models[¶](https://docs.vllm.ai#multimodal-models)

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/supported_models/#list-of-multimodal-language-models).

| Architecture | Models | Inputs | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`ColModernVBertForRetrieval`

`ModernVBERT/colmodernvbert-merged`

`ColPaliForRetrieval`

`vidore/colpali-v1.3-hf`

`ColQwen3`

`TomoroAI/tomoro-colqwen3-embed-4b`

, `TomoroAI/tomoro-colqwen3-embed-8b`

`ColQwen3_5`

`athrael-soju/colqwen3.5-4.5B-v3`

, `vultr/VultronRetrieverPrime-Qwen3.5-8B`

`OpsColQwen3Model`

`OpenSearch-AI/Ops-Colqwen3-4B`

, `OpenSearch-AI/Ops-Colqwen3-8B`

`Qwen3VLNemotronEmbedModel`

`nvidia/nemotron-colembed-vl-4b-v2`

, `nvidia/nemotron-colembed-vl-8b-v2`

`*ForConditionalGeneration`

C,`*ForCausalLM`

C, etc.C Automatically converted into an embedding model via `--convert embed`

. ([details](https://docs.vllm.ai/#model-conversion))

* Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as_embedding_model](https://docs.vllm.ai/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_embedding_model).

### Special models[¶](https://docs.vllm.ai#special-models)

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`JinaForRanking`

`jinaai/jina-reranker-v3`

jina-reranker-v3 is a listwise document reranker model with a novel `last but not late interaction`

architecture. More information can be found at: [ examples/pooling/token_embed/jina_reranker_v3_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_embed/jina_reranker_v3_offline.py)

## Offline Inference[¶](https://docs.vllm.ai#offline-inference)

### Pooling Parameters[¶](https://docs.vllm.ai#pooling-parameters)

The following [pooling parameters](https://docs.vllm.ai/api/vllm/#vllm.PoolingParams) are supported.

`LLM.encode`

[¶](https://docs.vllm.ai#llmencode)

The [encode](https://docs.vllm.ai/api/vllm/entrypoints/pooling/offline/#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode) method is available to all pooling models in vLLM.

Set `pooling_task="token_embed"`

when using `LLM.encode`

for token embedding Models:

from vllm import LLM
llm = LLM(model="answerdotai/answerai-colbert-small-v1", runner="pooling")
(output,) = llm.encode("Hello, my name is", pooling_task="token_embed")
data = output.outputs.data
print(f"Data: {data!r}")


`LLM.score`

[¶](https://docs.vllm.ai#llmscore)

The [score](https://docs.vllm.ai/api/vllm/entrypoints/pooling/offline/#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score) method outputs similarity scores between sentence pairs.

All models that support token embedding task also support using the score API to compute similarity scores by calculating the late interaction of two input prompts.

from vllm import LLM
llm = LLM(model="answerdotai/answerai-colbert-small-v1", runner="pooling")
(output,) = llm.score(
"What is the capital of France?",
"The capital of Brazil is Brasilia.",
)
score = output.outputs.score
print(f"Score: {score}")


## Online Serving[¶](https://docs.vllm.ai#online-serving)

Please refer to the [Pooling API](https://docs.vllm.ai/#pooling-api) and use `"task":"token_embed"`

.

## More examples[¶](https://docs.vllm.ai#more-examples)

More examples can be found here: [ examples/pooling/token_embed](https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_embed)

## Supported Features[¶](https://docs.vllm.ai#supported-features)

Token embedding features should be consistent with (sequence) embedding. For more information, see [this page](https://docs.vllm.ai/embed/#supported-features).