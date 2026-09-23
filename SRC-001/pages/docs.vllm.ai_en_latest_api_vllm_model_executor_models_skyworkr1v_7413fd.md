source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/skyworkr1v/
lastmod: 2026-09-23

#

`vllm.model_executor.models.skyworkr1v`

[¶](https://docs.vllm.ai#vllm.model_executor.models.skyworkr1v)

Classes:

-
–[SkyworkR1VImageEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.skyworkr1v.SkyworkR1VImageEmbeddingInputs)Dimensions:

-
–[SkyworkR1VImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.skyworkr1v.SkyworkR1VImagePixelInputs)Dimensions:


##

`SkyworkR1VImageEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.skyworkr1v.SkyworkR1VImageEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - ni: Number of images - ifs: Image feature size - hs: Hidden size (must match the hidden size of language model backbone)

## Source code in `vllm/model_executor/models/skyworkr1v.py`


##

`SkyworkR1VImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.skyworkr1v.SkyworkR1VImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bnp: Batch size * number of images * (1 + num_patches) - c: Number of channels (3) - h: Height - w: Width - bn: Batch size * number of images