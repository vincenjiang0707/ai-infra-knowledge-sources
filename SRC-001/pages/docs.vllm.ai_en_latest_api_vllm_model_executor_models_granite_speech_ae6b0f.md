source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/granite_speech/
lastmod: 2026-09-23

#

`vllm.model_executor.models.granite_speech`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech)

Inference-only IBM Granite speech model.

Classes:

-
–[GraniteSpeechAudioInputs](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechAudioInputs)Audio input features for Granite Speech model.

-
–[GraniteSpeechCTCEncoder](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechCTCEncoder)CTC Encoder comprising conformer blocks and additional linear layers.

-
–[GraniteSpeechConformerAttention](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerAttention)Attention for conformer blocks using Shaw's relative positional

-
–[GraniteSpeechConformerBlock](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerBlock)Conformer block, consisting largely of linear layers,

-
–[GraniteSpeechConformerConvModule](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerConvModule)Conformer conv module consisting of several 1D/depthwise 1D

-
–[GraniteSpeechConformerDepthWiseConv1d](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerDepthWiseConv1d)Wrapper for padded 1D pointwise convolution.

-
–[GraniteSpeechConformerFeedForward](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerFeedForward)Feedforward module for conformer encoder blocks.

-
–[GraniteSpeechForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration)

##

`GraniteSpeechAudioInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechAudioInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Audio input features for Granite Speech model.

## Dimensions

- b: Batch size
- fi: Number of input features from the Mel spectrogram.
- fo: Number of output features, i.e. the embedding size.
- 160: Fixed feature dimension for Mel spectrogram features

Attributes:

-
([audio_embed_sizes](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechAudioInputs.audio_embed_sizes)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)],[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(b)]List of audio embedding sizes for each item in batch.

-
([input_features](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechAudioInputs.input_features)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(b, fi, 160)]Audio input features.

-
([input_features_mask](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechAudioInputs.input_features_mask)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(b, fo)]Mask for variable length audio features.


## Source code in `vllm/model_executor/models/granite_speech.py`


##

`GraniteSpeechCTCEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechCTCEncoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

CTC Encoder comprising conformer blocks and additional linear layers.

## Source code in `vllm/model_executor/models/granite_speech.py`


##

`GraniteSpeechConformerAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Attention for conformer blocks using Shaw's relative positional embeddings. See the following [paper](https://arxiv.org/pdf/1803.02155) for more details.

## Source code in `vllm/model_executor/models/granite_speech.py`


|
|

##

`GraniteSpeechConformerBlock`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerBlock)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Conformer block, consisting largely of linear layers, attention, and convolutional layers.

## Source code in `vllm/model_executor/models/granite_speech.py`


##

`GraniteSpeechConformerConvModule`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerConvModule)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Conformer conv module consisting of several 1D/depthwise 1D convolutional layers.

## Source code in `vllm/model_executor/models/granite_speech.py`


##

`GraniteSpeechConformerDepthWiseConv1d`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerDepthWiseConv1d)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Wrapper for padded 1D pointwise convolution.

## Source code in `vllm/model_executor/models/granite_speech.py`


##

`GraniteSpeechConformerFeedForward`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechConformerFeedForward)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Feedforward module for conformer encoder blocks.

## Source code in `vllm/model_executor/models/granite_speech.py`


##

`GraniteSpeechForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)[SupportsTranscription](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription)

Methods:

-
–[embed_multimodal](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.embed_multimodal)Compute the audio embeddings if audio inputs are present.

-
–[get_generation_prompt](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.get_generation_prompt)Get the generation prompt to be used for transcription requests.

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.get_mm_mapping)Get the module prefix in multimodal models.

-
–[get_num_audio_tokens](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.get_num_audio_tokens)Get the number of audio tokens for an audio duration in sec.

-
–[get_speech_to_text_config](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.get_speech_to_text_config)Get the stt config for this model.


## Source code in `vllm/model_executor/models/granite_speech.py`


|
|

###

`_build_input_features_mask(audio_embed_sizes)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration._build_input_features_mask)

Calculate the input features mask, which will generally be used to mask the padded features for all entries in the batch except for those with the most audio features.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor: Mask of shape (bsz, num_features) to be applied to

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)the audio features prior to splitting the audio embeddings.


## Source code in `vllm/model_executor/models/granite_speech.py`


###

`_pad_and_stack_input_features(input_features)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration._pad_and_stack_input_features)

Given a list of input features of varying length, pad them to the same length and stack them into a torch.Tensor.

NOTE: Usually, padding is done in the input processor/feature extractor and zero padded prior to the computation of the Mel features; the resulting values are only constant within a batch and generally nonzero (i.e., slightly negative nums); we should validate that this is okay since we don't use a feature attention mask, but the more important thing is that we apply the input_features_mask with variable len batches.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor: Tensor of shape [bsz, num_features, 160], where

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)num_features is the max number of features of any entry in the

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)batch.


## Source code in `vllm/model_executor/models/granite_speech.py`


###

`_process_audio_input(audio_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration._process_audio_input)

Compute the audio features to be merged into the LLM embeddings.

Parameters:

-

(`audio_input`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration._process_audio_input(audio_input))

) –[GraniteSpeechAudioInputs](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechAudioInputs)GraniteSpeechAudioInputs Audio inputs object containing Mel features, an input features mask, and the (flattened) number of audio tokens per instance.


Returns:

## Source code in `vllm/model_executor/models/granite_speech.py`


###

`embed_multimodal(**kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.embed_multimodal)

Compute the audio embeddings if audio inputs are present.

## Source code in `vllm/model_executor/models/granite_speech.py`


###

`get_generation_prompt(stt_params)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.get_generation_prompt)

Get the generation prompt to be used for transcription requests.

## Source code in `vllm/model_executor/models/granite_speech.py`


###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.get_mm_mapping)

Get the module prefix in multimodal models.

## Source code in `vllm/model_executor/models/granite_speech.py`


###

`get_num_audio_tokens(audio_duration_s, stt_config, model_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.get_num_audio_tokens)

Get the number of audio tokens for an audio duration in sec.

## Source code in `vllm/model_executor/models/granite_speech.py`


###

`get_speech_to_text_config(model_config, task_type)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite_speech.GraniteSpeechForConditionalGeneration.get_speech_to_text_config)

Get the stt config for this model.