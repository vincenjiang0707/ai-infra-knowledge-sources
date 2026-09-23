source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/common/mm_preprocess/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.common.mm_preprocess`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess)

Multimodal preprocessing for the DeepSeek-V4 vision variants (DeepSeek-V4-Flash-Vision-Exp).

The image transform and sentinel-block construction are ported from the official repository's `image_processor.py`

so that token counts bit-match the reference. Each `<｜deepseek_image｜>`

placeholder in the prompt expands to a variable-length block of sentinel tokens; only positions with `type == IMAGE`

receive vision embeddings, the other sentinels are looked up from learned embedding vectors in the model.

Unlike the reference (which uses out-of-vocab ids `vocab_size + type`

), the sentinel block borrows five consecutive reserved tokenizer tokens (`<|place_holder_mm_span_0431|>`

.. `_0435|>`

): they are special tokens the tokenizer never emits from plain text, so the ids stay in-vocabulary and work with stock token validation, logprobs and detokenization. The ids are pure markers — every sentinel position's embedding is overwritten with vision/sentinel vectors before the decoder layers see it, exactly like the reference's out-of-vocab scheme.

Classes:

-
–[DeepseekV4VLImageProcessor](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.DeepseekV4VLImageProcessor)Per-image transform (the PIL-input equivalent of the reference

-
–[DeepseekV4VLProcessor](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.DeepseekV4VLProcessor)Minimal stand-in for the HF processor of DeepSeek-V4 vision models.


Functions:

-
–[build_image_block](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.build_image_block)Builds the N-layout token types (final order) and the aligner-row order

-
–[build_image_block_pad_free](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.build_image_block_pad_free)`build_image_block`

without the position-dependent compressor pad. -
–[grid_tokens](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.grid_tokens)Number of LLM tokens the aligner grid occupies (N-layout, including

-
–[image_sentinel_mask](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.image_sentinel_mask)Boolean mask for image-block sentinel positions (in-vocab ids).

-
–[load_image](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.load_image)Transform one PIL image into ViT patches.

-
–[validate_image_sentinel_ids](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.validate_image_sentinel_ids)Check the borrowed sentinel ids against the tokenizer.


##

`DeepseekV4VLImageProcessor`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.DeepseekV4VLImageProcessor)

Per-image transform (the PIL-input equivalent of the reference `load_image`

).

## Source code in `vllm/models/deepseek_v4/common/mm_preprocess.py`


##

`DeepseekV4VLProcessor`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.DeepseekV4VLProcessor)

Minimal stand-in for the HF processor of DeepSeek-V4 vision models.

The official repository ships image preprocessing as plain functions in `image_processor.py`

(no `auto_map`

processor), so this class wraps their ports directly and the model loads without `--trust-remote-code`

.

`__call__`

returns a `BatchFeature`

with one entry per image (flattened across images):

`patches`

:`(sum(n_vit_h * n_vit_w), 3, p, p)`

bf16 ViT patches.`vit_grid`

:`(num_images, 2)`

int64`[n_vit_h, n_vit_w]`

.`llm_grid`

:`(num_images, 2)`

int64`[n_llm_h, n_llm_w]`

.`perm`

: concatenated per-image`(n_llm_h * n_llm_w,)`

int64 index selecting aligner outputs into the final N-layout order.`types`

: concatenated per-image pad-free sentinel block types;`block ids = IMAGE_SENTINEL_BASE_ID + types`

.

## Source code in `vllm/models/deepseek_v4/common/mm_preprocess.py`


##

`build_image_block(n_llm_h, n_llm_w, start_pos)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.build_image_block)

Builds the N-layout token types (final order) and the aligner-row order for IMAGE slots.

## Source code in `vllm/models/deepseek_v4/common/mm_preprocess.py`


##

`build_image_block_pad_free(n_llm_h, n_llm_w)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.build_image_block_pad_free)

`build_image_block`

without the position-dependent compressor pad.

`start_pos`

is chosen so that `compress_pad == 0`

; the pad is instead prepended when the block is spliced into the final prompt, where its position is known.

## Source code in `vllm/models/deepseek_v4/common/mm_preprocess.py`


##

`grid_tokens(best_height, best_width, patch_size, downsample_ratio)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.grid_tokens)

Number of LLM tokens the aligner grid occupies (N-layout, including row/align padding).

## Source code in `vllm/models/deepseek_v4/common/mm_preprocess.py`


##

`image_sentinel_mask(token_ids)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.image_sentinel_mask)

Boolean mask for image-block sentinel positions (in-vocab ids).

## Source code in `vllm/models/deepseek_v4/common/mm_preprocess.py`


##

`load_image(image, *, patch_size, downsample_ratio, max_n_token, min_pixels, max_wh_ratio)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.load_image)

Transform one PIL image into ViT patches.

Same math as the reference `load_image`

, except the image is already decoded (vLLM supplies PIL images instead of a record dict).

## Source code in `vllm/models/deepseek_v4/common/mm_preprocess.py`


##

`validate_image_sentinel_ids(tokenizer)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.mm_preprocess.validate_image_sentinel_ids)

Check the borrowed sentinel ids against the tokenizer.