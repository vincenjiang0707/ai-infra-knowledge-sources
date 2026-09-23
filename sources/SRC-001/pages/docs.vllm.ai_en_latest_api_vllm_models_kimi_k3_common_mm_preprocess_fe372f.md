source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/common/mm_preprocess/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.common.mm_preprocess`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess)

Shared Kimi-K3 multimodal preprocessing.

Classes:

-
–[KimiK3DummyInputsBuilder](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3DummyInputsBuilder)Builds image-based dummy inputs for K3 profiling.

-
–[KimiK3MultiModalProcessor](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3MultiModalProcessor)Image-only multi-modal processor for Kimi-K3.

-
–[KimiK3ProcessingInfo](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3ProcessingInfo)Processing information for the image-only Kimi-K3 model.


##

`KimiK3DummyInputsBuilder`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3DummyInputsBuilder)

Bases: [BaseDummyInputsBuilder](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseDummyInputsBuilder)[[KimiK3ProcessingInfo](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3ProcessingInfo)]

Builds image-based dummy inputs for K3 profiling.

The dummy text is made of `<|kimi_image_placeholder|>`

tokens — exactly the placeholder that K3's `_get_prompt_updates`

expands — and the dummy mm data is a plain list of PIL images under the `image`

key.

## Source code in `vllm/models/kimi_k3/common/mm_preprocess.py`


##

`KimiK3MultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3MultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)[[KimiK3ProcessingInfo](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3ProcessingInfo)]

Image-only multi-modal processor for Kimi-K3.

## Source code in `vllm/models/kimi_k3/common/mm_preprocess.py`


|
|

###

`_get_mm_fields_config(hf_inputs, hf_processor_mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3MultiModalProcessor._get_mm_fields_config)

Slice the flattened patch tensor back into per-image items.

`pixel_values`

holds all patches from every image concatenated; each image's patch count is `prod(grid_thws[i])`

. `grid_thws`

is one `[N_t, N_h, N_w]`

row per image.

## Source code in `vllm/models/kimi_k3/common/mm_preprocess.py`


###

`_get_prompt_updates(mm_items, hf_processor_mm_kwargs, out_mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3MultiModalProcessor._get_prompt_updates)

Expand each K3 image placeholder into a resolution-aware update.

K3's prompt carries a single `<|kimi_image_placeholder|>`

token per image. This replaces that token with `<|media_begin|>image {w}x{h}<|media_content|>{pads}<|media_end|>`

, embedding the per-image resolution in the prompt and marking only the `<|media_pad|>`

positions as embedding slots (the number of pads is the feature size returned by `media_tokens_calculator`

).

## Source code in `vllm/models/kimi_k3/common/mm_preprocess.py`


##

`KimiK3ProcessingInfo`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.common.mm_preprocess.KimiK3ProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Processing information for the image-only Kimi-K3 model.

K3 uses the standard `image`

modality (unlike K2.5's unified `vision_chunk`

), so it builds its own `KimiK3Processor`

wrapper around the checkpoint's image processor and resolves the `<|media_pad|>`

token id the same way K2.5 does.

## Source code in `vllm/models/kimi_k3/common/mm_preprocess.py`


|
|