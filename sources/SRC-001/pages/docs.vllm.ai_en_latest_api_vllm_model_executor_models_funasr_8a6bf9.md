source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/funasr/
lastmod: 2026-09-24

#

`vllm.model_executor.models.funasr`

[¶](https://docs.vllm.ai#vllm.model_executor.models.funasr)

Classes:

-
–[FunASRAudioInputs](https://docs.vllm.ai#vllm.model_executor.models.funasr.FunASRAudioInputs)Dimensions:


##

`FunASRAudioInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.funasr.FunASRAudioInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - b: Batch size - nmb: Number of mel bins - t: Time frames (M)