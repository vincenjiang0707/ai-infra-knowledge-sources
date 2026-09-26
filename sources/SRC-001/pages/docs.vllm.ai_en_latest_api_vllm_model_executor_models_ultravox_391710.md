source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/ultravox/
lastmod: 2026-09-24

#

`vllm.model_executor.models.ultravox`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox)

PyTorch Ultravox model.

Classes:

-
–[StackAudioFrames](https://docs.vllm.ai#vllm.model_executor.models.ultravox.StackAudioFrames)Stack the audio embedding frames to reduce the sequence length by a factor

-
–[UltravoxAudioEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioEmbeddingInputs)Dimensions:

-
–[UltravoxAudioFeatureInputs](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioFeatureInputs)Dimensions:

-
–[UltravoxModel](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel) -
–[UltravoxProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxProcessingInfo) -
–[UltravoxWhisperEncoder](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxWhisperEncoder)Ultravox's

`ModifiedWhisperEncoder`

on top of vLLM's`WhisperEncoder`

.

Functions:

-
–[pad_and_concat_to_dim3](https://docs.vllm.ai#vllm.model_executor.models.ultravox.pad_and_concat_to_dim3)Pad and concatenate a list of tensors.


##

`StackAudioFrames`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.StackAudioFrames)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Stack the audio embedding frames to reduce the sequence length by a factor of `stack_factor`

.

## Source code in `vllm/model_executor/models/ultravox.py`


##

`UltravoxAudioEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - b: batch size - na: number of audios - afs: audio feature size - hs: hidden size

## Source code in `vllm/model_executor/models/ultravox.py`


##

`UltravoxAudioFeatureInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioFeatureInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - b: batch size - n: number of chunks - t: Time frames (M) - nmb: Number of mel bins

Attributes:

-
([lens](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioFeatureInputs.lens)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(bn)]Length of the audio frames per chunk. Used for attention mask in WhisperEncoder.

-
([num_chunks](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioFeatureInputs.num_chunks)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(n)]Number of chunks per audio. Used for flattening the audio features.

-
([token_len](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioFeatureInputs.token_len)

) –[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[TensorShape](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorShape)(bn)]Length of the audio tokens per chunk. Used for flattening the audio features.


## Source code in `vllm/model_executor/models/ultravox.py`


###

`lens`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioFeatureInputs.lens)

Length of the audio frames per chunk. Used for attention mask in WhisperEncoder.

###

`num_chunks`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioFeatureInputs.num_chunks)

Number of chunks per audio. Used for flattening the audio features.

###

`token_len`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxAudioFeatureInputs.token_len)

Length of the audio tokens per chunk. Used for flattening the audio features.

##

`UltravoxModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)[SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.forward)Run forward pass for Ultravox.

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.get_mm_mapping)Get the module prefix in multimodal models.


## Source code in `vllm/model_executor/models/ultravox.py`


|
|

###

`forward(input_ids, positions, intermediate_tensors=None, inputs_embeds=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.forward)

Run forward pass for Ultravox.

One key thing to understand is the `input_ids`

already accounts for the positions of the to-be-inserted audio embeddings. The to-be-inserted audio has a size that is essentially 6.25 tokens per second of audio.

This way, the `positions`

and `attn_metadata`

are consistent with the `input_ids`

.

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.forward(input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneFlattened (concatenated) input_ids corresponding to a batch.

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Position indices for the input tokens.

-

(`intermediate_tensors`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.forward(intermediate_tensors))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Intermediate tensors from prior forward pass.

-

(`inputs_embeds`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.forward(inputs_embeds))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional tensor of input embeddings.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.forward(**kwargs))

, default:[object](https://docs.python.org/3/builtins/functions.html#object)`{}`

) –Multimodal inputs for this batch, forwarded to the multimodal embedding path.


## Source code in `vllm/model_executor/models/ultravox.py`


###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxModel.get_mm_mapping)

Get the module prefix in multimodal models.

## Source code in `vllm/model_executor/models/ultravox.py`


##

`UltravoxProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Methods:

-
–[get_target_channels](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxProcessingInfo.get_target_channels)Return target audio channels for Ultravox models (mono).


## Source code in `vllm/model_executor/models/ultravox.py`


##

`UltravoxWhisperEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.UltravoxWhisperEncoder)

Bases: `WhisperEncoder`


Ultravox's `ModifiedWhisperEncoder`

on top of vLLM's `WhisperEncoder`

.

Like the original (a modified HF whisper encoder, see https://github.com/huggingface/transformers/issues/25744), it accepts mel inputs shorter than 30s (positions are sliced to the input length) and confines attention to each chunk's valid frames based on `audio_lens`

(via segmented `cu_seqlens`

instead of a dense key-padding mask), so its outputs match the HF implementation for valid positions. The linears are vLLM-native so the tower can be wrapped for LoRA.

## Source code in `vllm/model_executor/models/ultravox.py`


##

`_build_chunk_attn_metadata(attn, feature_lens, seq_len, hidden_size, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox._build_chunk_attn_metadata)

Segmented varlen attention metadata for a padded batch of audio chunks.

Each padded row contributes up to two sequences to `cu_seqlens`

: its valid frames and its padding tail. Attention therefore never crosses a valid/padding boundary (equivalent to the key-padding mask the HF implementation uses), while every row still flows through the (potentially LoRA-wrapped) linears, keeping the per-chunk token counts constant as required by `get_mm_lora_token_counts`

. Queries at padding positions produce (garbage) outputs, which are trimmed by `audio_token_len`

downstream.

## Source code in `vllm/model_executor/models/ultravox.py`


##

`pad_and_concat_to_dim3(features)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.ultravox.pad_and_concat_to_dim3)

Pad and concatenate a list of tensors.

## output

Tensor of shape [B, C, M] where M is the maximum length of the input tensors, B is the sum of the batch sizes of the input tensors. C must be the same for all input tensors.