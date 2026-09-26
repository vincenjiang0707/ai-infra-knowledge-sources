source: https://docs.vllm.ai/en/latest/models/pooling_models/token_classify/
lastmod: 2026-09-24

# Token Classification Usages[¶](https://docs.vllm.ai#token-classification-usages)

## Summary[¶](https://docs.vllm.ai#summary)

- Model Usage: token classification
- Pooling Tasks:
`token_classify`

- Offline APIs:
`LLM.encode(..., pooling_task="token_classify")`


- Online APIs:
- Pooling API (
`/pooling`

)

- Pooling API (

The key distinction between (sequence) classification and token classification lies in their output granularity: (sequence) classification produces a single result for an entire input sequence, whereas token classification yields a result for each individual token within the sequence.

Many classification models support both (sequence) classification and token classification. For further details on (sequence) classification, please refer to [this page](https://docs.vllm.ai/classify/).

Note

Pooling multitask support has been removed since v0.21. When the default pooling task (classify) is not what you want, you need to manually specify it via `PoolerConfig(task="token_classify")`

offline or `--pooler-config.task token_classify`

online.

## Typical Use Cases[¶](https://docs.vllm.ai#typical-use-cases)

### Named Entity Recognition (NER)[¶](https://docs.vllm.ai#named-entity-recognition-ner)

For implementation examples, see:

Offline: [ examples/pooling/token_classify/ner_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_classify/ner_offline.py)

Online: [ examples/pooling/token_classify/ner_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_classify/ner_online.py)

### Forced Alignment[¶](https://docs.vllm.ai#forced-alignment)

Forced alignment takes audio and reference text as input and produces word-level timestamps.

Offline: [ examples/pooling/token_classify/forced_alignment_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_classify/forced_alignment_offline.py)

### Sparse retrieval (lexical matching)[¶](https://docs.vllm.ai#sparse-retrieval-lexical-matching)

The BAAI/bge-m3 model leverages token classification for sparse retrieval. For more information, see [this page](https://docs.vllm.ai/specific_models/#baaibge-m3).

## Supported Models[¶](https://docs.vllm.ai#supported-models)

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`BertForTokenClassification`

`boltuix/NeuroBERT-NER`

(see note), etc.`ModernBertForTokenClassification`

`disham993/electrical-ner-ModernBERT-base`

`OpenAIPrivacyFilterForTokenClassification`

`openai/privacy-filter`

`Qwen3ForTokenClassification`

C`bd2lcco/Qwen3-0.6B-finetuned`

`RobertaForTokenClassification`

`Jean-Baptiste/roberta-large-ner-english`

`XLMRobertaForTokenClassification`

`Davlan/xlm-roberta-base-ner-hrl`

`*Model`

C,`*ForCausalLM`

C, etc.C Automatically converted into a classification model via `--convert classify`

. ([details](https://docs.vllm.ai/#model-conversion)) * Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as_seq_cls_model](https://docs.vllm.ai/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_seq_cls_model). By default, the class probabilities are extracted from the softmaxed hidden state corresponding to the last token.

### Multimodal Models[¶](https://docs.vllm.ai#multimodal-models)

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/supported_models/#list-of-multimodal-language-models).

| Architecture | Models | Inputs | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`Qwen3ASRForcedAlignerForTokenClassification`

+`Qwen/Qwen3-ForcedAligner-0.6B`

(see note)Note

Forced alignment usage requires `--hf-overrides '{"architectures": ["Qwen3ASRForcedAlignerForTokenClassification"]}'`

. Please refer to [ examples/pooling/token_classify/forced_alignment_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_classify/forced_alignment_offline.py).

### Reward Models[¶](https://docs.vllm.ai#reward-models)

Using token classification models as reward models. For details on reward models, see [Reward Models](https://docs.vllm.ai/reward/).

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`InternLM2ForRewardModel`

`internlm/internlm2-1_8b-reward`

, `internlm/internlm2-7b-reward`

, etc.`Qwen2ForRewardModel`

`Qwen/Qwen2.5-Math-RM-72B`

, etc.`*Model`

C,`*ForCausalLM`

C, etc.C Automatically converted into a classification model via `--convert classify`

. ([details](https://docs.vllm.ai/#model-conversion))

If your model is not in the above list, we will try to automatically convert the model using [as_seq_cls_model](https://docs.vllm.ai/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_seq_cls_model).

## Offline Inference[¶](https://docs.vllm.ai#offline-inference)

### Pooling Parameters[¶](https://docs.vllm.ai#pooling-parameters)

The following [pooling parameters](https://docs.vllm.ai/api/vllm/#vllm.PoolingParams) are supported.

`LLM.encode`

[¶](https://docs.vllm.ai#llmencode)

The [encode](https://docs.vllm.ai/api/vllm/entrypoints/pooling/offline/#vllm.entrypoints.pooling.offline.PoolingOfflineMixin.encode) method is available to all pooling models in vLLM.

Set `pooling_task="token_classify"`

when using `LLM.encode`

for token classification Models:

from vllm import LLM
llm = LLM(model="boltuix/NeuroBERT-NER", runner="pooling")
(output,) = llm.encode("Hello, my name is", pooling_task="token_classify")
data = output.outputs.data
print(f"Data: {data!r}")


## Online Serving[¶](https://docs.vllm.ai#online-serving)

Please refer to the [Pooling API](https://docs.vllm.ai/#pooling-api) and use `"task":"token_classify"`

.

## More examples[¶](https://docs.vllm.ai#more-examples)

More examples can be found here: [ examples/pooling/token_classify](https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_classify)

## Supported Features[¶](https://docs.vllm.ai#supported-features)

Token classification features should be consistent with (sequence) classification. For more information, see [this page](https://docs.vllm.ai/classify/#supported-features).