source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/multimodal/
lastmod: 2026-09-23

#

`vllm.model_executor.models.transformers.multimodal`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal)

Transformers modeling backend mixin for multi-modal models.

Classes:

-
–[LegacyMultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor)Locates placeholders by searching the prompt the HF processor has already

-
–[MultiModalMixin](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin) -
–[OffsetsMultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.OffsetsMultiModalProcessor)Locates placeholders from the

`text_replacement_offsets`

the HF processor

##

`LegacyMultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor)

Bases: [_MultiModalProcessorBase](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._MultiModalProcessorBase)

Locates placeholders by searching the prompt the HF processor has already expanded for the tokens of each modality.

Serves transformers versions with no `return_text_replacement_offsets`

. Placeholders found this way cannot be rebuilt from an unexpanded prompt, so this processor overrides `apply`

and gets no multi-modal processor cache. Remove it once `requirements/common.txt`

requires `transformers>=5.15.0`

.

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor.apply)Process the prompt and every multi-modal item in one HF processor call,


## Source code in `vllm/model_executor/models/transformers/multimodal.py`


|
|

###

`_apply_audio(prompt_ids, processed_data, num_audios)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor._apply_audio)

Take each contiguous run of the audio token as one item's placeholder, and record how many tokens the run holds.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_apply_vision(prompt_ids, processed_data, mm_items, hf_processor_mm_kwargs, mm_token_type_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor._apply_vision)

Split the positions the processor marks as image into one placeholder per item, sized by the token count it reports for each image.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_get_mm_token_ids(modality)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor._get_mm_token_ids)

Token ids marking where `modality`

sits in the prompt, which for some processors differ from the placeholder written into it.

The expanded prompt is all this path has to go on, so it takes the processor at its word about which tokens belong to the modality.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_get_num_multimodal_tokens(mm_items, hf_processor_mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor._get_num_multimodal_tokens)

Ask the HF processor how many tokens and patches each image expands to.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_get_prompt_updates(mm_items, hf_processor_mm_kwargs, out_mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor._get_prompt_updates)

Empty, because `apply`

writes the placeholder ranges itself rather than deriving them from updates.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`apply(inputs, timing_ctx)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.LegacyMultiModalProcessor.apply)

Process the prompt and every multi-modal item in one HF processor call, then read the placeholder ranges out of the token ids it returns.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


|
|

##

`MultiModalMixin`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin)

Bases:

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsMRoPE](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMRoPE)[Base](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.base.Base)

Methods:

-
–[get_language_model](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin.get_language_model)Transformers modeling backend multimodal classes do not contain a separate

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin.get_mm_mapping)Get the module prefix in multimodal models


## Source code in `vllm/model_executor/models/transformers/multimodal.py`


|
|

###

`_decorate_for_torch_compile()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin._decorate_for_torch_compile)

Decorate the model's decoder and encoder classes to indicate to vLLM that they support torch compile if `can_enable_torch_compile`

and `should_torch_compile_mm_encoder`

are True respectively.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_find_encoder_classes(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin._find_encoder_classes)

Modalities whose encoder cannot be told apart from the model itself are omitted, as are those `get_encoder`

rejects.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_select_item_kwargs(kwargs, index, num_items)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin._select_item_kwargs)

Narrow the entries of `kwargs`

that hold one row per item down to the item at `index`

. Length is all there is to match on, so an unrelated entry of the same length is narrowed too.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`get_language_model()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin.get_language_model)

Transformers modeling backend multimodal classes do not contain a separate vLLM language model class. Therefore, in order to return a language model vLLM class, we use a wrapper to give `self`

the same interface as a text model.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.MultiModalMixin.get_mm_mapping)

Get the module prefix in multimodal models

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


##

`OffsetsMultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.OffsetsMultiModalProcessor)

Bases: [_MultiModalProcessorBase](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._MultiModalProcessorBase)

Locates placeholders from the `text_replacement_offsets`

the HF processor reports, expressing each one as a `PromptUpdate`

.

Stating the expansion as an update is what lets it be rebuilt from an unexpanded prompt, so this processor takes the base class's processing path and with it the multi-modal processor cache.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


|
|

###

`_get_num_image_patches(hf_inputs, mm_data, num_images)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.OffsetsMultiModalProcessor._get_num_image_patches)

How many rows of the image fields belong to each image.

Taken from whichever per-image count the processor reports, and checked against the data it has to slice.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_get_num_patches_per_image(mm_data)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.OffsetsMultiModalProcessor._get_num_patches_per_image)

Ask the HF processor how many rows of image data each image produces.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_get_prompt_updates(mm_items, hf_processor_mm_kwargs, out_mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal.OffsetsMultiModalProcessor._get_prompt_updates)

Replace each modality's placeholder token with the token ids that item's replacement text encodes to, marking which of them hold embeddings.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


##

`_MultiModalProcessorBase`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._MultiModalProcessorBase)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)[MultiModalProcessingInfo]

Processing common to both Transformers backend processors: calling the HF processor, sizing images, and attributing its outputs to a modality.

Subclasses add the strategy for locating placeholders in the prompt.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


|
|

###

`_get_modality_field_names(modality)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._MultiModalProcessorBase._get_modality_field_names)

Names of the fields the sub-processor for `modality`

produces.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_get_slice_dim(data, total_rows)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._MultiModalProcessorBase._get_slice_dim)

Which dimension of a field holds the rows belonging to each item.

Some processors (e.g., Idefics3) return image fields with a leading batch dimension, putting the rows one dimension further in.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_partition_keys_by_modality(keys, modalities)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._MultiModalProcessorBase._partition_keys_by_modality)

Attribute each HF processor output key to the modality that produced it.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_unpad_audios(hf_inputs, mm_data, mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._MultiModalProcessorBase._unpad_audios)

Replace the audio fields with each audio processed on its own.

Processors pad every audio up to the longest in the call, which would leave an item's data dependent on what it was processed with. Unlike images, nothing in the output states how long each one really is, and processors pad a lone audio too, so the only way to know what an audio produces by itself is to process it by itself.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


###

`_unpad_images(hf_inputs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._MultiModalProcessorBase._unpad_images)

Trim each image back to its own size when the processor padded them all to the largest in the batch.

An image's data has to depend on nothing but that image, or the multi-modal processor cache would store it under that image's hash and later reuse it beside a different neighbour. Padding is re-applied when the encoder runs.

## Source code in `vllm/model_executor/models/transformers/multimodal.py`


##

`_get_embed_token_id(replacement_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.multimodal._get_embed_token_id)

The token an expansion repeats is the one holding the embeddings.