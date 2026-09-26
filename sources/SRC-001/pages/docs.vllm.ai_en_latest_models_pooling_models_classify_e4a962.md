source: https://docs.vllm.ai/en/latest/models/pooling_models/classify/
lastmod: 2026-09-24

# Classification Usages[¶](https://docs.vllm.ai#classification-usages)

Classification involves predicting which predefined category, class, or label best corresponds to a given input.

## Summary[¶](https://docs.vllm.ai#summary)

- Model Usage: (sequence) classification
- Pooling Task:
`classify`

- Offline APIs:
`LLM.classify(...)`

`LLM.encode(..., pooling_task="classify")`


- Online APIs:
[Classification API](https://docs.vllm.ai/#online-serving)(`/classify`

)- Pooling API (
`/pooling`

)


The key distinction between (sequence) classification and token classification lies in their output granularity: (sequence) classification produces a single result for an entire input sequence, whereas token classification yields a result for each individual token within the sequence.

Many classification models support both (sequence) classification and token classification. For further details on token classification, please refer to [this page](https://docs.vllm.ai/token_classify/).

Only when a classification model outputs num_labels equal to 1 can it be used as a scoring model and have its scoring API enabled, please refer to [this page](https://docs.vllm.ai/scoring/).

## Typical Use Cases[¶](https://docs.vllm.ai#typical-use-cases)

### Classification[¶](https://docs.vllm.ai#classification)

The most fundamental application of classification models is to categorize input data into predefined classes.

## Supported Models[¶](https://docs.vllm.ai#supported-models)

### Text-only Models[¶](https://docs.vllm.ai#text-only-models)

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`GPT2ForSequenceClassification`

`nie3e/sentiment-polish-gpt2-small`

`Qwen2ForSequenceClassification`

C`jason9693/Qwen2.5-1.5B-apeach`

`*Model`

C,`*ForCausalLM`

C, etc.### Multimodal Models[¶](https://docs.vllm.ai#multimodal-models)

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/supported_models/#list-of-multimodal-language-models).

| Architecture | Models | Inputs | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`Qwen2_5_VLForSequenceClassification`

CE++ VE+`muziyongshixin/Qwen2.5-VL-7B-for-VideoCls`

`*ForConditionalGeneration`

C,`*ForCausalLM`

C, etc.C Automatically converted into a classification model via `--convert classify`

. ([details](https://docs.vllm.ai/#model-conversion))

* Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as_seq_cls_model](https://docs.vllm.ai/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_seq_cls_model). By default, the class probabilities are extracted from the softmaxed hidden state corresponding to the last token.

### Cross-encoder Models[¶](https://docs.vllm.ai#cross-encoder-models)

Cross-encoder (aka reranker) models are a subset of classification models that accept two prompts as input and output num_labels equal to 1. Most classification models can also be used as [cross-encoder models](https://docs.vllm.ai/scoring/#cross-encoder-models). For more information on cross-encoder models, please refer to [this page](https://docs.vllm.ai/scoring/).

#### Text-only Models[¶](https://docs.vllm.ai#text-only-models_1)

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

#### Multimodal Models[¶](https://docs.vllm.ai#multimodal-models_1)

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

### Reward Models[¶](https://docs.vllm.ai#reward-models)

Using (sequence) classification models as reward models. For more information, see [Reward Models](https://docs.vllm.ai/reward/).

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`JambaForSequenceClassification`

`ai21labs/Jamba-tiny-reward-dev`

, etc.`Qwen3ForSequenceClassification`

C`Skywork/Skywork-Reward-V2-Qwen3-0.6B`

, etc.`LlamaForSequenceClassification`

C`Skywork/Skywork-Reward-V2-Llama-3.2-1B`

, etc.`*Model`

C,`*ForCausalLM`

C, etc.C Automatically converted into a classification model via `--convert classify`

. ([details](https://docs.vllm.ai/#model-conversion))

If your model is not in the above list, we will try to automatically convert the model using [as_seq_cls_model](https://docs.vllm.ai/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_seq_cls_model). By default, the class probabilities are extracted from the softmaxed hidden state corresponding to the last token.

## Offline Inference[¶](https://docs.vllm.ai#offline-inference)

### Pooling Parameters[¶](https://docs.vllm.ai#pooling-parameters)

The following [pooling parameters](https://docs.vllm.ai/api/vllm/#vllm.PoolingParams) are supported.

`LLM.classify`

[¶](https://docs.vllm.ai#llmclassify)

The [classify](https://docs.vllm.ai/api/vllm/entrypoints/pooling/offline/#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.classify) method outputs a probability vector for each prompt.

from vllm import LLM
llm = LLM(model="jason9693/Qwen2.5-1.5B-apeach", runner="pooling")
(output,) = llm.classify("Hello, my name is")
probs = output.outputs.probs
print(f"Class Probabilities: {probs!r} (size={len(probs)})")


A code example can be found here: [ examples/basic/offline_inference/classify.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/offline_inference/classify.py)

`LLM.encode`

[¶](https://docs.vllm.ai#llmencode)

The [encode](https://docs.vllm.ai/api/vllm/entrypoints/pooling/offline/#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode) method is available to all pooling models in vLLM.

Set `pooling_task="classify"`

when using `LLM.encode`

for classification Models:

from vllm import LLM
llm = LLM(model="jason9693/Qwen2.5-1.5B-apeach", runner="pooling")
(output,) = llm.encode("Hello, my name is", pooling_task="classify")
data = output.outputs.data
print(f"Data: {data!r}")


## Online Serving[¶](https://docs.vllm.ai#online-serving)

### Classification API[¶](https://docs.vllm.ai#classification-api)

Online `/classify`

API is similar to `LLM.classify`

.

#### Completion Parameters[¶](https://docs.vllm.ai#completion-parameters)

The following Classification API parameters are supported:

## Code

The following extra parameters are supported:

## Code

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
add_special_tokens: bool = Field(
default=True,
description=(
"If true (the default), special tokens (e.g. BOS) will be added to "
"the prompt."
),
)
use_activation: bool | None = Field(
default=None,
description="Whether to use activation for the pooler outputs. "
"`None` uses the pooler's default, which is `True` in most cases.",
)


#### Chat Parameters[¶](https://docs.vllm.ai#chat-parameters)

For chat-like input (i.e. if `messages`

is passed), the following parameters are supported:

these extra parameters are supported instead:

## Code

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
add_generation_prompt: bool = Field(
default=False,
description=(
"If true, the generation prompt will be added to the chat template. "
"This is a parameter used by chat template in tokenizer config of the "
"model."
),
)
continue_final_message: bool = Field(
default=False,
description=(
"If this is set, the chat will be formatted so that the final "
"message in the chat is open-ended, without any EOS tokens. The "
"model will continue this message rather than starting a new one. "
'This allows you to "prefill" part of the model\'s response for it. '
"Cannot be used at the same time as `add_generation_prompt`."
),
)
add_special_tokens: bool = Field(
default=False,
description=(
"If true, special tokens (e.g. BOS) will be added to the prompt "
"on top of what is added by the chat template. "
"For most models, the chat template takes care of adding the "
"special tokens so this should be set to false (as is the "
"default)."
),
)
chat_template: str | None = Field(
default=None,
description=(
"A Jinja template to use for this conversion. "
"As of transformers v4.44, default chat template is no longer "
"allowed, so you must provide a chat template if the tokenizer "
"does not define one."
),
)
chat_template_kwargs: dict[str, Any] | None = Field(
default=None,
description=(
"Additional keyword args to pass to the template renderer. "
"Will be accessible by the chat template."
),
)
media_io_kwargs: dict[str, dict[str, Any]] | None = Field(
default=None,
description=(
"Additional kwargs to pass to the media IO connectors, "
"keyed by modality. Merged with engine-level media_io_kwargs."
),
)
use_activation: bool | None = Field(
default=None,
description="Whether to use activation for the pooler outputs. "
"`None` uses the pooler's default, which is `True` in most cases.",
)


#### Example Requests[¶](https://docs.vllm.ai#example-requests)

Code example: [ examples/pooling/classify/classification_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/classify/classification_online.py)

You can classify multiple texts by passing an array of strings:

curl -v "http://127.0.0.1:8000/classify" \
-H "Content-Type: application/json" \
-d '{
"model": "jason9693/Qwen2.5-1.5B-apeach",
"input": [
"Loved the new café—coffee was great.",
"This update broke everything. Frustrating."
]
}'


## Response

```json
{
"id": "classify-7c87cac407b749a6935d8c7ce2a8fba2",
"object": "list",
"created": 1745383065,
"model": "jason9693/Qwen2.5-1.5B-apeach",
"data": [
{
"index": 0,
"label": "Default",
"probs": [
0.565970778465271,
0.4340292513370514
],
"num_classes": 2
},
{
"index": 1,
"label": "Spoiled",
"probs": [
0.26448777318000793,
0.7355121970176697
],
"num_classes": 2
}
],
"usage": {
"prompt_tokens": 20,
"total_tokens": 20,
"completion_tokens": 0,
"prompt_tokens_details": null
}
}
```


You can also pass a string directly to the `input`

field:

```bash
curl -v "http://127.0.0.1:8000/classify" \
-H "Content-Type: application/json" \
-d '{
"model": "jason9693/Qwen2.5-1.5B-apeach",
"input": "Loved the new café—coffee was great."
}'
```


## Response

```json
{
"id": "classify-9bf17f2847b046c7b2d5495f4b4f9682",
"object": "list",
"created": 1745383213,
"model": "jason9693/Qwen2.5-1.5B-apeach",
"data": [
{
"index": 0,
"label": "Default",
"probs": [
0.565970778465271,
0.4340292513370514
],
"num_classes": 2
}
],
"usage": {
"prompt_tokens": 10,
"total_tokens": 10,
"completion_tokens": 0,
"prompt_tokens_details": null
}
}
```


## More examples[¶](https://docs.vllm.ai#more-examples)

More examples can be found here: [ examples/pooling/classify](https://github.com/vllm-project/vllm/tree/main/examples/pooling/classify)

## Supported Features[¶](https://docs.vllm.ai#supported-features)

### Enable/disable activation[¶](https://docs.vllm.ai#enabledisable-activation)

You can enable or disable activation via `use_activation`

.

### Problem type (e.g. `multi_label_classification`

)[¶](https://docs.vllm.ai#problem-type-eg-multi_label_classification)

You can modify the `problem_type`

via problem_type in the Hugging Face config. The supported problem types are: `single_label_classification`

, `multi_label_classification`

, and `regression`

.

Implement alignment with transformers [ForSequenceClassificationLoss](https://github.com/huggingface/transformers/blob/57bb6db6ee4cfaccc45b8d474dfad5a17811ca60/src/transformers/loss/loss_utils.py#L92).

### Affine Score Calibration[¶](https://docs.vllm.ai#affine-score-calibration)

Affine Score Calibration, also known as [Platt Scaling](https://en.wikipedia.org/wiki/Platt_scaling) (Platt, 1999), is the most widely used method for calibrating classifier outputs into well-calibrated probabilities.

The calibration follows the transformation:

`activation((logit - logit_mean) / logit_sigma)`


| Parameter | Default | Description |
|---|---|---|
`logit_mean` | `None` | Mean subtracted from logits (centers scores) |
`logit_sigma` | `None` | Standard deviation used to scale logits after mean subtraction |

The computation order is as follows:

logits -= logit_mean # subtract mean (center scores)
logits /= logit_sigma # divide by sigma (scale)
logits = activation(logits) # e.g. sigmoid


Example configuration:

## Removed Features[¶](https://docs.vllm.ai#removed-features)

### Remove softmax from PoolingParams[¶](https://docs.vllm.ai#remove-softmax-from-poolingparams)

We have already removed `softmax`

and `activation`

from PoolingParams. Instead, use `use_activation`

, since we allow `classify`

and `token_classify`

to use any activation function.