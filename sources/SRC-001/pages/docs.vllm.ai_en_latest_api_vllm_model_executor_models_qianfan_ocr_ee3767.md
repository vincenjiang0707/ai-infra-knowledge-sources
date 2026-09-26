source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qianfan_ocr/
lastmod: 2026-09-24

#

`vllm.model_executor.models.qianfan_ocr`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qianfan_ocr)

Classes:

-
–[QianfanOCRForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.qianfan_ocr.QianfanOCRForConditionalGeneration)QianfanOCR multimodal model.

-
–[QianfanOCRProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.qianfan_ocr.QianfanOCRProcessingInfo)Image-only ProcessingInfo for QianfanOCR (no video support).


##

`QianfanOCRForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qianfan_ocr.QianfanOCRForConditionalGeneration)

Bases: [InternVLChatModel](https://docs.vllm.ai/internvl/#vllm.model_executor.models.internvl.InternVLChatModel)

QianfanOCR multimodal model.

Identical in structure to InternVLChatModel (InternViT vision encoder + pixel-shuffle MLP connector + Qwen3 language model). This class exists solely to register the `QianfanOCRForConditionalGeneration`

architecture name that appears in the model's config.json.

## Source code in `vllm/model_executor/models/qianfan_ocr.py`


##

`QianfanOCRProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qianfan_ocr.QianfanOCRProcessingInfo)

Bases: [BaseInternVLProcessingInfo](https://docs.vllm.ai/internvl/#vllm.model_executor.models.internvl.BaseInternVLProcessingInfo)

Image-only ProcessingInfo for QianfanOCR (no video support).