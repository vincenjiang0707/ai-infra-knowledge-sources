source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen2_audio/
lastmod: 2026-09-23

#

`vllm.model_executor.models.qwen2_audio`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_audio)

Inference-only Qwen2-Audio model compatible with HuggingFace weights.

Classes:

-
–[Qwen2AudioEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.qwen2_audio.Qwen2AudioEmbeddingInputs)Dimensions:

-
–[Qwen2AudioFeatureInputs](https://docs.vllm.ai#vllm.model_executor.models.qwen2_audio.Qwen2AudioFeatureInputs)Dimensions:

-
–[Qwen2AudioProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.qwen2_audio.Qwen2AudioProcessingInfo)

##

`Qwen2AudioEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_audio.Qwen2AudioEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size - naf: Number of audio features - hs: Hidden size (must match the hidden size of language model backbone)

## Source code in `vllm/model_executor/models/qwen2_audio.py`


##

`Qwen2AudioFeatureInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_audio.Qwen2AudioFeatureInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - na: Number of audios - nmb: Number of mel bins

## Source code in `vllm/model_executor/models/qwen2_audio.py`


##

`Qwen2AudioProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_audio.Qwen2AudioProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Methods:

-
–[get_target_channels](https://docs.vllm.ai#vllm.model_executor.models.qwen2_audio.Qwen2AudioProcessingInfo.get_target_channels)Return target audio channels for Qwen2 Audio models (mono).