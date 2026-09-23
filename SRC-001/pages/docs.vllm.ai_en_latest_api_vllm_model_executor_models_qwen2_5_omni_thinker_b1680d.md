source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen2_5_omni_thinker/
lastmod: 2026-09-23

#

`vllm.model_executor.models.qwen2_5_omni_thinker`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker)

Inference-only Qwen2.5-Omni model (thinker part).

Classes:

-
–[Qwen2_5OmniAudioFeatureInputs](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniAudioFeatureInputs)Dimensions:

-
–[Qwen2_5OmniThinkerForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration) -
–[Qwen2_5OmniThinkerMultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerMultiModalProcessor) -
–[Qwen2_5OmniThinkerProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerProcessingInfo)

Functions:

-
–[check_interleaved_audio_video](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.check_interleaved_audio_video)Check if video and audio positions are interleaved in any per-video span.

-
–[merge_interleaved_embeddings](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.merge_interleaved_embeddings)Merge embeddings for interleaved audio-in-video sequences.

-
–[unpad_and_flat_audio_features](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.unpad_and_flat_audio_features)Unpad and flatten batched audio features.


##

`Qwen2_5OmniAudioFeatureInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniAudioFeatureInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - na: Number of audios - nmb: Number of mel bins - msl: Maximum sequence length - tsl: Total sequence length

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


##

`Qwen2_5OmniThinkerForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

, [SupportsMRoPE](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMRoPE)`Qwen2_5OmniConditionalGenerationMixin`


Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration.get_mm_mapping)Get the module prefix in multimodal models

-
–[get_mrope_input_positions](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration.get_mrope_input_positions)Compute M-RoPE input positions using mm_features directly.

-
–[iter_mm_features](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration.iter_mm_features)Iterate over multimodal features sorted by position offset.


## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


|
|

###

`_compute_audio_token_count(audio_feature_length)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration._compute_audio_token_count)

###

`_compute_interleaved_positions(start_idx, data)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration._compute_interleaved_positions)

Compute positions for interleaved video+audio chunks.

Returns: (position_ids, total_token_count)

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


|
|

###

`_get_audio_for_video_mapping(mm_features)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration._get_audio_for_video_mapping)

Map video offset -> paired audio_feature_length for use_audio_in_video.

When use_audio_in_video=True, audio is interleaved within video chunks. The pairing is based on feature order in mm_features.

Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)],[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Tuple of (video_offset -> audio_feature_length mapping, set of paired audio offsets to skip)


## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration.get_mm_mapping)

Get the module prefix in multimodal models

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


###

`get_mrope_input_positions(input_tokens, mm_features)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration.get_mrope_input_positions)

Compute M-RoPE input positions using mm_features directly.

## Example for use_audio_in_video case

(V_i are vision position ids, A_i are audio position ids)

|V_1 ... V_n|A_1 ... A_n|V_n+1 ... V_2n|A_n+1 ... A_2n|... |vision chunk 1|audio chunk 1|vision chunk 2|audio chunk 2 |...

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


|
|

###

`iter_mm_features(mm_features)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerForConditionalGeneration.iter_mm_features)

Iterate over multimodal features sorted by position offset.

Yields: (offset, modality, feature_data) where feature_data contains: - image: {"grid_t", "grid_h", "grid_w", "t_factor"} - video: {"grid_t", "grid_h", "grid_w", "t_factor", "use_audio_in_video", "audio_feature_length"} - audio: {"audio_feature_length"}

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


|
|

##

`Qwen2_5OmniThinkerMultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerMultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/processor/#vllm.multimodal.processing.processor.BaseMultiModalProcessor)[[Qwen2_5OmniThinkerProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerProcessingInfo)]

Methods:

-
–[omni_get_updates_use_audio_in_video](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerMultiModalProcessor.omni_get_updates_use_audio_in_video)Get video prompt updates when

`use_audio_in_video`

is True.

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


|
|

###

`_derive_audio_from_video_placeholders(placeholders, mm_prompt_updates)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerMultiModalProcessor._derive_audio_from_video_placeholders)

Helper to derive audio placeholders from video placeholders when use_audio_in_video=True.

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


###

`_maybe_apply_prompt_updates(mm_items, mm_res)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerMultiModalProcessor._maybe_apply_prompt_updates)

Qwen2.5-Omni reimplements this function to handle `use_audio_in_video`

.

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


###

`omni_get_updates_use_audio_in_video(thinker_config, audio_len, video_grid_thw, video_second_per_grid_t)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerMultiModalProcessor.omni_get_updates_use_audio_in_video)

Get video prompt updates when `use_audio_in_video`

is True.

In this case, audio and vision update ids will be split into chunks and interleaved (details in `_omni_get_input_positions_tensor`

).

<|video_bos|><|VIDEO|><|video_eos|> => <|video_bos|><|audio_bos|>(... chunks ...)<|audio_eos|><|video_eos|>

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


##

`Qwen2_5OmniThinkerProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerProcessingInfo)

Bases:

, [Qwen2AudioProcessingInfo](https://docs.vllm.ai/qwen2_audio/#vllm.model_executor.models.qwen2_audio.Qwen2AudioProcessingInfo)`Qwen2_5_VLProcessingInfo`


Methods:

-
–[get_target_channels](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.Qwen2_5OmniThinkerProcessingInfo.get_target_channels)Return target audio channels for Qwen2.5 Omni models (mono).


## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


##

`check_interleaved_audio_video(is_video, is_audio, num_video, num_audio)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.check_interleaved_audio_video)

Check if video and audio positions are interleaved in any per-video span.

For use_audio_in_video=True, each video placeholder is expanded into one local span containing only video/audio pad tokens, bounded by non-pad tokens such as audio_start/audio_end. Check each contiguous V/A span independently instead of requiring all V/A tokens in the whole sequence to form one global dense range; otherwise multi-video requests can be misclassified as non-interleaved because of the boundary tokens between videos.

## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


##

`merge_interleaved_embeddings(inputs_embeds, multimodal_embeddings, is_video, is_audio, is_multimodal)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.merge_interleaved_embeddings)

Merge embeddings for interleaved audio-in-video sequences.

When use_audio_in_video=True, video and audio tokens are interleaved in the token sequence, but embeddings are provided as separate contiguous tensors. This function scatters each modality by the `modality`

attribute attached to each embedding tensor (set during encoder gather) and also supports image embeddings in the same interleaved request.

Parameters:

-

(`inputs_embeds`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.merge_interleaved_embeddings(inputs_embeds))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input embeddings tensor to merge into.

-

(`multimodal_embeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.merge_interleaved_embeddings(multimodal_embeddings))

) –[MultiModalEmbeddings](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.MultiModalEmbeddings)List of embedding tensors (video, audio, image).

-

(`is_video`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.merge_interleaved_embeddings(is_video))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Boolean mask for video token positions.

-

(`is_audio`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.merge_interleaved_embeddings(is_audio))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Boolean mask for audio token positions.

-

(`is_multimodal`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.merge_interleaved_embeddings(is_multimodal))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Boolean mask for all multimodal token positions.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The merged inputs_embeds tensor with multimodal embeddings scattered

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)to their correct positions.


## Source code in `vllm/model_executor/models/qwen2_5_omni_thinker.py`


##

`unpad_and_flat_audio_features(input_audio_features, audio_feature_lengths)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen2_5_omni_thinker.unpad_and_flat_audio_features)

Unpad and flatten batched audio features.