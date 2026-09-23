source: https://docs.vllm.ai/en/latest/models/pooling_models/scoring/
lastmod: 2026-09-23

# Scoring Usages[¶](https://docs.vllm.ai#scoring-usages)

The score models is designed to compute similarity scores between two input prompts. It supports three model types (aka `score_type`

): `cross-encoder`

, `late-interaction`

, and `bi-encoder`

.

Note

vLLM handles only the model inference component of RAG pipelines (such as embedding generation and reranking). For higher-level RAG orchestration, you should leverage integration frameworks like [LangChain](https://github.com/langchain-ai/langchain).

## Summary[¶](https://docs.vllm.ai#summary)

- Model Usage: Scoring
- Pooling Task:

| Score Types | Pooling Tasks | scoring function |
|---|---|---|
`cross-encoder` | `classify` (see note) | linear classifier |
`late-interaction` | `token_embed` | late interaction(MaxSim) |
`bi-encoder` | `embed` | cosine similarity |

- Offline APIs:
`LLM.score`


- Online APIs:
[Score API](https://docs.vllm.ai/#score-api)(`/score`

,`/v1/score`

)[Cohere Rerank API](https://docs.vllm.ai/#cohere-rerank-api)(`/rerank`

,`/v1/rerank`

,`/v2/rerank`

)


Note

Only when a classification model outputs num_labels equal to 1 can it be used as a scoring model and have its scoring API enabled.

### Score Types[¶](https://docs.vllm.ai#score-types)

The three supported scoring functions are as illustrated in the figure below.

## Supported Models[¶](https://docs.vllm.ai#supported-models)

### Cross-encoder models[¶](https://docs.vllm.ai#cross-encoder-models)

[Cross-encoder](https://www.sbert.net/examples/applications/cross-encoder/README.html) (aka reranker) models are a subset of classification models that accept two prompts as input and output num_labels equal to 1.

#### Text-only Models[¶](https://docs.vllm.ai#text-only-models)

| Architecture | Models | Example HF Models | Score template (see note) |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`BertForSequenceClassification`

`cross-encoder/ms-marco-MiniLM-L-6-v2`

, etc.`GemmaForSequenceClassification`

`BAAI/bge-reranker-v2-gemma`

(see note), etc.[bge-reranker-v2-gemma.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/bge-reranker-v2-gemma.jinja)`GteNewForSequenceClassification`

`Alibaba-NLP/gte-multilingual-reranker-base`

, etc.`LlamaBidirectionalForSequenceClassification`

C`nvidia/llama-nemotron-rerank-1b-v2`

, etc.[nemotron-rerank.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/nemotron-rerank.jinja)`ModernBertForSequenceClassification`

`Alibaba-NLP/gte-reranker-modernbert-base`

, etc.`Qwen2ForSequenceClassification`

C`mixedbread-ai/mxbai-rerank-base-v2`

(see note), etc.[mxbai_rerank_v2.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/mxbai_rerank_v2.jinja)`Qwen3ForSequenceClassification`

C`tomaarsen/Qwen3-Reranker-0.6B-seq-cls`

, `Qwen/Qwen3-Reranker-0.6B`

(see note), etc.[qwen3_reranker.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/qwen3_reranker.jinja)`RobertaForSequenceClassification`

`cross-encoder/quora-roberta-base`

, etc.`XLMRobertaForSequenceClassification`

`BAAI/bge-reranker-v2-m3`

, etc.`*Model`

C,`*ForCausalLM`

C, etc.C Automatically converted into a classification model via `--convert classify`

. ([details](https://docs.vllm.ai/#model-conversion))

* Feature support is the same as that of the original model.

Note

Some models require a specific prompt format to work correctly.

You can find Example HF Models's corresponding score template in [ examples/pooling/score/template/](https://github.com/vllm-project/vllm/tree/main/examples/pooling/score/template)

Examples : [ examples/pooling/score/using_template_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/using_template_offline.py) [ examples/pooling/score/using_template_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/using_template_online.py)

Note

Load the official original `BAAI/bge-reranker-v2-gemma`

by using the following command.

Note

The second-generation GTE model (mGTE-TRM) is named `NewForSequenceClassification`

. The name `NewForSequenceClassification`

is too generic, you should set `--hf-overrides '{"architectures": ["GteNewForSequenceClassification"]}'`

to specify the use of the `GteNewForSequenceClassification`

architecture.

Note

Load the official original `mxbai-rerank-v2`

by using the following command.

Note

Load the official original `Qwen3 Reranker`

by using the following command. More information can be found at: [ examples/pooling/score/qwen3_reranker_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/qwen3_reranker_offline.py) [ examples/pooling/score/qwen3_reranker_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/qwen3_reranker_online.py).

#### Multimodal Models[¶](https://docs.vllm.ai#multimodal-models)

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/supported_models/#list-of-multimodal-language-models).

| Architecture | Models | Inputs | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`JinaVLForSequenceClassification`

E+`jinaai/jina-reranker-m0`

, etc.`LlamaNemotronVLForSequenceClassification`

E+`nvidia/llama-nemotron-rerank-vl-1b-v2`

`Qwen3VLForSequenceClassification`

E++ VE+`Qwen/Qwen3-VL-Reranker-2B`

(see note), etc.C Automatically converted into a classification model via `--convert classify`

. ([details](https://docs.vllm.ai/#model-conversion))

* Feature support is the same as that of the original model.

Note

Similar to Qwen3-Reranker, you need to use the following `--hf_overrides`

to load the official original `Qwen3-VL-Reranker`

. `Qwen3-VL`

officially uses `qwen_vl_utils`

for image preprocessing, while vLLM uses `transformers`

' `video_processing_qwen3_vl`

, which leads to slightly different results compared to the official Hugging Face repository examples.

### Late-interaction models[¶](https://docs.vllm.ai#late-interaction-models)

All models that support token embedding task also support using the score API to compute similarity scores by calculating the late interaction of two input prompts. See [this page](https://docs.vllm.ai/token_embed/) for more information about token embedding models.

### Text-only Models[¶](https://docs.vllm.ai#text-only-models_1)

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

C, etc.### Multimodal Models[¶](https://docs.vllm.ai#multimodal-models_1)

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

### Bi-encoder[¶](https://docs.vllm.ai#bi-encoder)

All models that support embedding task also support using the score API to compute similarity scores by calculating the cosine similarity of two input prompt's embeddings. See [this page](https://docs.vllm.ai/embed/) for more information about embedding models.

### Text-only Models[¶](https://docs.vllm.ai#text-only-models_2)

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`BertModel`

`BAAI/bge-base-en-v1.5`

, `Snowflake/snowflake-arctic-embed-xs`

, etc.`BertSpladeSparseEmbeddingModel`

`naver/splade-v3`

`BgeM3EmbeddingModel`

`BAAI/bge-m3`

`Gemma2Model`

C`BAAI/bge-multilingual-gemma2`

, etc.`Gemma3TextModel`

C`google/embeddinggemma-300m`

, etc.`GteModel`

`Snowflake/snowflake-arctic-embed-m-v2.0`

.`GteNewModel`

`Alibaba-NLP/gte-multilingual-base`

, etc.`JinaEmbeddingsV5Model`

C`jinaai/jina-embeddings-v5-text-small`

, `jinaai/jina-embeddings-v5-text-nano`

(see note)`LlamaBidirectionalModel`

C`nvidia/llama-nemotron-embed-1b-v2`

, etc.`LlamaModel`

C,`LlamaForCausalLM`

C,`MistralModel`

C, etc.`intfloat/e5-mistral-7b-instruct`

, etc.`ModernBertModel`

`Alibaba-NLP/gte-modernbert-base`

, etc.`NomicBertModel`

`nomic-ai/nomic-embed-text-v1`

, `nomic-ai/nomic-embed-text-v2-moe`

, `Snowflake/snowflake-arctic-embed-m-long`

, etc.`Qwen2Model`

C,`Qwen2ForCausalLM`

C`ssmits/Qwen2-7B-Instruct-embed-base`

(see note), `Alibaba-NLP/gte-Qwen2-7B-instruct`

(see note), etc.`Qwen3Model`

C,`Qwen3ForCausalLM`

C`Qwen/Qwen3-Embedding-0.6B`

, etc.`RobertaModel`

, `RobertaForMaskedLM`

`sentence-transformers/all-roberta-large-v1`

, etc.`VoyageQwen3BidirectionalEmbedModel`

C`voyageai/voyage-4-nano`

, etc.`XLMRobertaModel`

`BAAI/bge-m3`

(see note), `intfloat/multilingual-e5-base`

, `jinaai/jina-embeddings-v3`

(see note), etc.`*Model`

C,`*ForCausalLM`

C, etc.Note

The second-generation GTE model (mGTE-TRM) is named `NewModel`

. The name `NewModel`

is too generic, you should set `--hf-overrides '{"architectures": ["GteNewModel"]}'`

to specify the use of the `GteNewModel`

architecture.

Note

`ssmits/Qwen2-7B-Instruct-embed-base`

has an improperly defined Sentence Transformers config. You need to manually set mean pooling by passing `--pooler-config '{"pooling_type": "MEAN"}'`

.

Note

For `Alibaba-NLP/gte-Qwen2-*`

, you need to enable `--trust-remote-code`

for the correct tokenizer to be loaded. See [ relevant issue on HF Transformers](https://github.com/huggingface/transformers/issues/34882).

Note

The `BAAI/bge-m3`

model comes with extra weights for sparse and colbert embeddings, See [this page](https://docs.vllm.ai/specific_models/#baaibge-m3) for more information.

Note

`jinaai/jina-embeddings-v3`

supports multiple tasks through LoRA, while vllm temporarily only supports text-matching tasks by merging LoRA weights.

Note

`jinaai/jina-embeddings-v5-text-small`

(Qwen3 decoder) and `jinaai/jina-embeddings-v5-text-nano`

(bidirectional EuroBERT encoder, `is_decoder=false`

) ship with four task-specific LoRA adapters (`retrieval`

, `text-matching`

, `classification`

, `clustering`

). vLLM merges the selected adapter into the base weights at load time. Choose the task with `--hf-overrides '{"jina_task": "<task>"}'`

; the default is `retrieval`

.

### Multimodal Models[¶](https://docs.vllm.ai#multimodal-models_2)

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/supported_models/#list-of-multimodal-language-models).

| Architecture | Models | Inputs | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`CLIPModel`

`openai/clip-vit-base-patch32`

, `openai/clip-vit-large-patch14`

, etc.`LlamaNemotronVLModel`

`nvidia/llama-nemotron-embed-vl-1b-v2`

`LlavaNextForConditionalGeneration`

C`royokong/e5-v`

`Phi3VForCausalLM`

C`TIGER-Lab/VLM2Vec-Full`

`Qwen3VLForConditionalGeneration`

C(see note)`Qwen/Qwen3-VL-Embedding-2B`

, etc.`SiglipModel`

`google/siglip-base-patch16-224`

, `google/siglip2-base-patch16-224`

`*ForConditionalGeneration`

C,`*ForCausalLM`

C, etc.C Automatically converted into an embedding model via `--convert embed`

. ([details](https://docs.vllm.ai/#model-conversion))

* Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as_embedding_model](https://docs.vllm.ai/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_embedding_model). By default, the embeddings of the whole prompt are extracted from the normalized hidden state corresponding to the last token.

Note

`Qwen3-VL-Embedding`

officially uses `qwen_vl_utils`

for image preprocessing, while vLLM uses `transformers`

' `video_processing_qwen3_vl`

, which leads to slightly different results compared to the official Hugging Face repository examples. Example code for offline inference using `qwen_vl_utils`

can be found in the [ vision_embedding_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/vision_embedding_offline.py) example.

Note

Although vLLM supports automatically converting models of any architecture into embedding models via --convert embed, to get the best results, you should use pooling models that are specifically trained as such.

## Offline Inference[¶](https://docs.vllm.ai#offline-inference)

### Pooling Parameters[¶](https://docs.vllm.ai#pooling-parameters)

The following [pooling parameters](https://docs.vllm.ai/api/vllm/#vllm.PoolingParams) are only supported by cross-encoder models and do not work for late-interaction and bi-encoder models.

`LLM.score`

[¶](https://docs.vllm.ai#llmscore)

The [score](https://docs.vllm.ai/api/vllm/entrypoints/pooling/offline/#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.score) method outputs similarity scores between sentence pairs.

from vllm import LLM
llm = LLM(model="BAAI/bge-reranker-v2-m3", runner="pooling")
(output,) = llm.score(
"What is the capital of France?",
"The capital of Brazil is Brasilia.",
)
score = output.outputs.score
print(f"Score: {score}")


A code example can be found here: [ examples/basic/offline_inference/score.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/offline_inference/score.py)

## Online Serving[¶](https://docs.vllm.ai#online-serving)

### Score API[¶](https://docs.vllm.ai#score-api)

Our Score API (`/score`

, `/v1/score`

) is similar to `LLM.score`

, compute similarity scores between two input prompts.

#### Parameters[¶](https://docs.vllm.ai#parameters)

The following Score API parameters are supported:

model: str | None = None
user: str | None = None
truncate_prompt_tokens: Annotated[int, Field(ge=-1)] | None = None
padding: Literal["max_length", "do_not_pad"] | None = Field(
default=None,
description=(
"Whether to pad the prompt, using the same names as the "
"Transformers tokenizer. 'max_length' pads to the maximum input "
"length, 'do_not_pad' leaves the prompt as is. Models trained "
"with a fixed sequence length and no attention mask, such as "
"SigLIP, need 'max_length' to match training, otherwise their "
"embeddings are not comparable."
),
)
truncation_side: Literal["left", "right"] | None = Field(
default=None,
description=(
"Which side to truncate from when truncate_prompt_tokens is active. "
"'right' keeps the first N tokens. "
"'left' keeps the last N tokens."
),
)
request_id: str = Field(
default_factory=random_uuid,
description=(
"The request_id related to this request. If the caller does "
"not set it, a random_uuid will be generated. This id is used "
"through out the inference process and return in response."
),
)
priority: int = Field(
default=0,
ge=-(2**63),
le=2**63 - 1,
description=(
"The priority of the request (lower means earlier handling; "
"default: 0). Any priority other than 0 will raise an error "
"if the served model does not use priority scheduling."
),
)
mm_processor_kwargs: dict[str, Any] | None = Field(
default=None,
description="Additional kwargs to pass to the HF processor.",
)
cache_salt: str | None = Field(
default=None,
min_length=1,
max_length=1024,
description=(
"If specified, the prefix cache will be salted with the provided "
"string to prevent an attacker to guess prompts in multi-user "
"environments. The salt should be random, protected from "
"access by 3rd parties, and long enough to be "
"unpredictable (e.g., 43 characters base64-encoded, corresponding "
"to 256 bit)."
),
)
use_activation: bool | None = Field(
default=None,
description="Whether to use activation for the pooler outputs. "
"`None` uses the pooler's default, which is `True` in most cases.",
)
max_tokens_per_query: int = Field(
default=0,
description=(
"Maximum number of tokens per query. Queries longer than "
"this will be truncated to this length. 0 means no "
"query-level truncation is applied."
),
)
max_tokens_per_doc: int = Field(
default=0,
description=(
"Maximum number of tokens per document. Documents longer than "
"this will be truncated to this length. 0 means no "
"document-level truncation is applied (only truncate_prompt_tokens "
"applies to the combined query+document)."
),
)
instruction: str | None = Field(
default=None,
description=(
"Task instruction prepended to each scored pair via the chat "
"template. Equivalent to passing "
"chat_template_kwargs={'instruction': ...}."
),
)
chat_template_kwargs: dict[str, Any] | None = Field(
default=None,
description=(
"Additional keyword args to pass to the chat template renderer. "
"Will be accessible by the score/rerank chat template."
),
)
queries: ScoreInput | list[ScoreInput]
documents: ScoreInput | list[ScoreInput]


#### Examples[¶](https://docs.vllm.ai#examples)

##### Single inference[¶](https://docs.vllm.ai#single-inference)

You can pass a string to both `queries`

and `documents`

, forming a single sentence pair.

curl -X 'POST' \
'http://127.0.0.1:8000/score' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"model": "BAAI/bge-reranker-v2-m3",
"encoding_format": "float",
"queries": "What is the capital of France?",
"documents": "The capital of France is Paris."
}'


## Response

##### Batch inference[¶](https://docs.vllm.ai#batch-inference)

You can pass a string to `queries`

and a list to `documents`

, forming multiple sentence pairs where each pair is built from `queries`

and a string in `documents`

. The total number of pairs is `len(documents)`

.

## Request

## Response

You can pass a list to both `queries`

and `documents`

, forming multiple sentence pairs where each pair is built from a string in `queries`

and the corresponding string in `documents`

(similar to `zip()`

). The total number of pairs is `len(documents)`

.

## Request

curl -X 'POST' \
'http://127.0.0.1:8000/score' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"model": "BAAI/bge-reranker-v2-m3",
"encoding_format": "float",
"queries": [
"What is the capital of Brazil?",
"What is the capital of France?"
],
"documents": [
"The capital of Brazil is Brasilia.",
"The capital of France is Paris."
]
}'


## Response

##### Multi-modal inputs[¶](https://docs.vllm.ai#multi-modal-inputs)

You can pass multi-modal inputs to scoring models by passing `content`

including a list of multi-modal input (image, etc.) in the request. Refer to the examples below for illustration.

To serve the model:

Since the request schema is not defined by OpenAI client, we post a request to the server using the lower-level `requests`

library:

## Code

import requests
response = requests.post(
"http://localhost:8000/v1/score",
json={
"model": "jinaai/jina-reranker-m0",
"queries": "slm markdown",
"documents": [
{
"content": [
{
"type": "image_url",
"image_url": {
"url": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/handelsblatt-preview.png"
},
}
],
},
{
"content": [
{
"type": "image_url",
"image_url": {
"url": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/handelsblatt-preview.png"
},
}
]
},
],
},
)
response.raise_for_status()
response_json = response.json()
print("Scoring output:", response_json["data"][0]["score"])
print("Scoring output:", response_json["data"][1]["score"])


Full example:

[examples/pooling/score/vision_score_api_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_score_api_online.py)[examples/pooling/score/vision_rerank_api_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_rerank_api_online.py)

### Cohere Rerank API[¶](https://docs.vllm.ai#cohere-rerank-api)

`/rerank`

, `/v1/rerank`

, and `/v2/rerank`

APIs are compatible with both [Jina AI's rerank API interface](https://jina.ai/reranker/) and [Cohere's rerank API interface](https://docs.cohere.com/v2/reference/rerank) to ensure compatibility with popular open-source tools.

Code example: [ examples/pooling/score/rerank_api_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/rerank_api_online.py)

#### Parameters[¶](https://docs.vllm.ai#parameters_1)

The following rerank api parameters are supported:

model: str | None = None
user: str | None = None
truncate_prompt_tokens: Annotated[int, Field(ge=-1)] | None = None
padding: Literal["max_length", "do_not_pad"] | None = Field(
default=None,
description=(
"Whether to pad the prompt, using the same names as the "
"Transformers tokenizer. 'max_length' pads to the maximum input "
"length, 'do_not_pad' leaves the prompt as is. Models trained "
"with a fixed sequence length and no attention mask, such as "
"SigLIP, need 'max_length' to match training, otherwise their "
"embeddings are not comparable."
),
)
truncation_side: Literal["left", "right"] | None = Field(
default=None,
description=(
"Which side to truncate from when truncate_prompt_tokens is active. "
"'right' keeps the first N tokens. "
"'left' keeps the last N tokens."
),
)
request_id: str = Field(
default_factory=random_uuid,
description=(
"The request_id related to this request. If the caller does "
"not set it, a random_uuid will be generated. This id is used "
"through out the inference process and return in response."
),
)
priority: int = Field(
default=0,
ge=-(2**63),
le=2**63 - 1,
description=(
"The priority of the request (lower means earlier handling; "
"default: 0). Any priority other than 0 will raise an error "
"if the served model does not use priority scheduling."
),
)
mm_processor_kwargs: dict[str, Any] | None = Field(
default=None,
description="Additional kwargs to pass to the HF processor.",
)
cache_salt: str | None = Field(
default=None,
min_length=1,
max_length=1024,
description=(
"If specified, the prefix cache will be salted with the provided "
"string to prevent an attacker to guess prompts in multi-user "
"environments. The salt should be random, protected from "
"access by 3rd parties, and long enough to be "
"unpredictable (e.g., 43 characters base64-encoded, corresponding "
"to 256 bit)."
),
)
use_activation: bool | None = Field(
default=None,
description="Whether to use activation for the pooler outputs. "
"`None` uses the pooler's default, which is `True` in most cases.",
)
max_tokens_per_query: int = Field(
default=0,
description=(
"Maximum number of tokens per query. Queries longer than "
"this will be truncated to this length. 0 means no "
"query-level truncation is applied."
),
)
max_tokens_per_doc: int = Field(
default=0,
description=(
"Maximum number of tokens per document. Documents longer than "
"this will be truncated to this length. 0 means no "
"document-level truncation is applied (only truncate_prompt_tokens "
"applies to the combined query+document)."
),
)
instruction: str | None = Field(
default=None,
description=(
"Task instruction prepended to each scored pair via the chat "
"template. Equivalent to passing "
"chat_template_kwargs={'instruction': ...}."
),
)
chat_template_kwargs: dict[str, Any] | None = Field(
default=None,
description=(
"Additional keyword args to pass to the chat template renderer. "
"Will be accessible by the score/rerank chat template."
),
)
query: ScoreInput
documents: ScoreInput | list[ScoreInput]
top_n: int = Field(default=0, ge=0)


#### Examples[¶](https://docs.vllm.ai#examples_1)

Note that the `top_n`

request parameter is optional and will default to the length of the `documents`

field. Result documents will be sorted by relevance, and the `index`

property can be used to determine original order.

## Request

curl -X 'POST' \
'http://127.0.0.1:8000/v1/rerank' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"model": "BAAI/bge-reranker-base",
"query": "What is the capital of France?",
"documents": [
"The capital of Brazil is Brasilia.",
"The capital of France is Paris.",
"Horses and cows are both animals"
]
}'


## Response

{
"id": "rerank-fae51b2b664d4ed38f5969b612edff77",
"model": "BAAI/bge-reranker-base",
"usage": {
"total_tokens": 56
},
"results": [
{
"index": 1,
"document": {
"text": "The capital of France is Paris."
},
"relevance_score": 0.99853515625
},
{
"index": 0,
"document": {
"text": "The capital of Brazil is Brasilia."
},
"relevance_score": 0.0005860328674316406
}
]
}


## More examples[¶](https://docs.vllm.ai#more-examples)

More examples can be found here: [ examples/pooling/score](https://github.com/vllm-project/vllm/tree/main/examples/pooling/score)

## Supported Features[¶](https://docs.vllm.ai#supported-features)

As cross-encoder models are a subset of classification models that accept two prompts as input and output num_labels equal to 1, cross-encoder features should be consistent with (sequence) classification. For more information, see [this page](https://docs.vllm.ai/classify/#supported-features).

### Score Template[¶](https://docs.vllm.ai#score-template)

Score templates are supported for **cross-encoder** models only. If you are using an **embedding** model for scoring, vLLM does not apply a score template.

Some scoring models require a specific prompt format to work correctly. You can specify a custom score template using the `--chat-template`

parameter (see [Chat Template](https://docs.vllm.ai/serving/online_serving/#chat-template)).

Like chat templates, the score template receives a `messages`

list. For scoring, each message has a `role`

attribute—either `"query"`

or `"document"`

. For the usual kind of point-wise cross-encoder, you can expect exactly two messages: one query and one document. To access the query and document content, use Jinja's `selectattr`

filter:

**Query**:`{{ (messages | selectattr("role", "eq", "query") | first).content }}`

**Document**:`{{ (messages | selectattr("role", "eq", "document") | first).content }}`


This approach is more robust than index-based access (`messages[0]`

, `messages[1]`

) because it selects messages by their semantic role. It also avoids assumptions about message ordering if additional message types are added to `messages`

in the future.

Example template file: [ examples/pooling/score/template/nemotron-rerank.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/nemotron-rerank.jinja)

### Enable/disable activation[¶](https://docs.vllm.ai#enabledisable-activation)

You can enable or disable activation via `use_activation`

only works for cross-encoder models.