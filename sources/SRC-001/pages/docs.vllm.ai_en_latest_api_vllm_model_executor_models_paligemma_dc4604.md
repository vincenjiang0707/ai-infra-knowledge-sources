source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/paligemma/
lastmod: 2026-09-24

#

`vllm.model_executor.models.paligemma`

[¶](https://docs.vllm.ai#vllm.model_executor.models.paligemma)

Classes:

-
–[PaliGemmaImageEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.paligemma.PaliGemmaImageEmbeddingInputs)Dimensions:

-
–[PaliGemmaImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.paligemma.PaliGemmaImagePixelInputs)Dimensions:


##

`PaliGemmaImageEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.paligemma.PaliGemmaImageEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of images - ifs: Image feature size - hs: Hidden size (must match language model backbone)

## Source code in `vllm/model_executor/models/paligemma.py`


##

`PaliGemmaImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.paligemma.PaliGemmaImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of images - c: Number of channels (3) - h: Height - w: Width