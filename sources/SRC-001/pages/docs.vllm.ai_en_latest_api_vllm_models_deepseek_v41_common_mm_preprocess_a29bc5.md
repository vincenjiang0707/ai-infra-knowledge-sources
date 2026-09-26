source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/common/mm_preprocess/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v41.common.mm_preprocess`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess)

Multimodal preprocessing for the DeepSeek-V4.1 vision variant.

The image transform and image-span construction are ported from the official repository's `image_processor.py`

so that token counts bit-match the reference. Each `<｜deepseek_image｜>`

placeholder in the prompt expands to `[IMAGE_START] + ([IMAGE] * n_llm_w + [IMAGE_NEW_LINE]) * n_llm_h + [IMAGE_END]`

; every span position carries `image_token_id`

(129264) in `input_ids`

and the roles ride along in a per-image `types`

tensor (the reference's out-of-band `token_types`

). IMAGE slots receive aligner rows in reading order; the delimiters take the learned `image_start`

/ `image_newline`

/ `image_end`

vectors.

The token stream matches the reference exactly: no compressor-alignment pad is inserted (the reference pools image tokens across compressor-group boundaries freely).

Classes:

-
–[DeepseekV4VLImageProcessor](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.DeepseekV4VLImageProcessor)Per-image transform (the PIL-input equivalent of the reference

-
–[DeepseekV4VLProcessor](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.DeepseekV4VLProcessor)Minimal stand-in for the HF processor of DeepSeek-V4.1 vision models.


Functions:

-
–[image_sentinel_mask](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.image_sentinel_mask)Boolean mask for image-span positions.

-
–[image_token_types](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.image_token_types)Reading-order span layout: one IMAGE_NEW_LINE per row.

-
–[llm_grid](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.llm_grid)Token grid the aligner produces from a patch grid of this pixel size.

-
–[load_image](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.load_image)Transform one PIL image into ViT patches.

-
–[safe_resize](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.safe_resize)Shrink the pixel size until the image costs at most max_n_token LLM

-
–[solve_resize_ratio](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.solve_resize_ratio)Largest aspect-preserving pixel size whose token grid still fits in

-
–[validate_image_sentinel_ids](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.validate_image_sentinel_ids)Check the image token id against the tokenizer.


##

`DeepseekV4VLImageProcessor`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.DeepseekV4VLImageProcessor)

Per-image transform (the PIL-input equivalent of the reference `load_image`

).

## Source code in `vllm/models/deepseek_v41/common/mm_preprocess.py`


##

`DeepseekV4VLProcessor`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.DeepseekV4VLProcessor)

Minimal stand-in for the HF processor of DeepSeek-V4.1 vision models.

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

.`types`

: concatenated per-image pad-free span roles (IMAGE_START/IMAGE/IMAGE_NEW_LINE/IMAGE_END); every span position carries`image_token_id`

in the prompt's token ids.

## Source code in `vllm/models/deepseek_v41/common/mm_preprocess.py`


##

`image_sentinel_mask(token_ids)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.image_sentinel_mask)

##

`image_token_types(n_llm_h, n_llm_w)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.image_token_types)

Reading-order span layout: one IMAGE_NEW_LINE per row.

## Source code in `vllm/models/deepseek_v41/common/mm_preprocess.py`


##

`llm_grid(best_height, best_width, patch_size, downsample_ratio)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.llm_grid)

Token grid the aligner produces from a patch grid of this pixel size.

## Source code in `vllm/models/deepseek_v41/common/mm_preprocess.py`


##

`load_image(image, *, patch_size, downsample_ratio, max_n_token, min_pixels, max_wh_ratio)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.load_image)

Transform one PIL image into ViT patches.

Same math as the reference `load_image`

, except the image is already decoded (vLLM supplies PIL images instead of a record dict).

## Source code in `vllm/models/deepseek_v41/common/mm_preprocess.py`


##

`safe_resize(height, width, best_height, best_width, patch_size, downsample_ratio, max_n_token)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.safe_resize)

Shrink the pixel size until the image costs at most max_n_token LLM tokens.

## Source code in `vllm/models/deepseek_v41/common/mm_preprocess.py`


##

`solve_resize_ratio(height, width, patch_size, downsample_ratio, max_n_token)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.solve_resize_ratio)

Largest aspect-preserving pixel size whose token grid still fits in max_n_token. Returns (best_height, best_width).

## Source code in `vllm/models/deepseek_v41/common/mm_preprocess.py`


##

`validate_image_sentinel_ids(tokenizer)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.mm_preprocess.validate_image_sentinel_ids)

Check the image token id against the tokenizer.