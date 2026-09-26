source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glmasr/
lastmod: 2026-09-24

#

`vllm.model_executor.models.glmasr`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr)

Classes:

-
–[GlmAsrDummyInputsBuilder](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrDummyInputsBuilder)Builder for dummy inputs used in profiling and testing.

-
–[GlmAsrEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEmbeddingInputs)Dimensions:

-
–[GlmAsrEncoder](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoder)Optimized GLM-ASR Audio Encoder with vLLM native implementation.

-
–[GlmAsrEncoderAttention](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderAttention)Optimized Multi-headed Grouped Query Attention for GLM-ASR encoder.

-
–[GlmAsrEncoderLayer](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderLayer)Optimized Transformer encoder layer for GLM-ASR.

-
–[GlmAsrEncoderMLP](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderMLP)Optimized MLP for GLM-ASR encoder.

-
–[GlmAsrEncoderRotaryEmbedding](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderRotaryEmbedding)Rotary Position Embedding for GLM-ASR encoder.

-
–[GlmAsrFeatureInputs](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrFeatureInputs)Dimensions:

-
–[GlmAsrForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrForConditionalGeneration) -
–[GlmAsrMultiModalDataParser](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrMultiModalDataParser)Custom parser for GLM-ASR multimodal data.

-
–[GlmAsrMultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrMultiModalProcessor)GLM-ASR processor that inherits directly from BaseMultiModalProcessor

-
–[GlmAsrMultiModalProjector](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrMultiModalProjector)Projects audio encoder outputs to language model hidden space.

-
–[GlmAsrProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrProcessingInfo)Processing information provider for GLM-ASR model.


##

`GlmAsrDummyInputsBuilder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrDummyInputsBuilder)

Bases: [BaseDummyInputsBuilder](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseDummyInputsBuilder)[[GlmAsrProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrProcessingInfo)]

Builder for dummy inputs used in profiling and testing.

Generates dummy text prompts and audio data that match the expected format for GLM-ASR model inputs. Used for memory profiling and performance benchmarking.

## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size - naf: Number of audio features - hs: Hidden size (must match the hidden size of language model backbone)

## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Optimized GLM-ASR Audio Encoder with vLLM native implementation.

This encoder processes audio features through convolutional layers followed by transformer layers with rotary position embeddings. Optimized for performance with: - QKVParallelLinear for fused attention projections - Tensor parallelism support via ColumnParallelLinear/RowParallelLinear - Quantization support - Flash Attention (SDPA)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoder.forward)Forward pass through the encoder.


## Source code in `vllm/model_executor/models/glmasr.py`


|
|

###

`_get_feat_extract_output_lengths(input_lengths)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoder._get_feat_extract_output_lengths)

Compute the output length after convolutions.

Parameters:

Returns:

## Source code in `vllm/model_executor/models/glmasr.py`


###

`forward(input_features)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoder.forward)

Forward pass through the encoder.

Parameters:

Returns:

-
(`_GlmAsrEncoderOutput`


) –[_GlmAsrEncoderOutput](https://docs.vllm.ai#vllm.model_executor.models.glmasr._GlmAsrEncoderOutput)Object with .last_hidden_state attribute containing [batch_size, seq_len', hidden_size] where seq_len' is the sequence length after convolutions


## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrEncoderAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Optimized Multi-headed Grouped Query Attention for GLM-ASR encoder.

Uses vLLM's QKVParallelLinear for fused projections, ApplyRotaryEmb for rotary position embeddings, and MMEncoderAttention for hardware-optimized attention computation with automatic backend selection.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderAttention.forward)Args:


## Source code in `vllm/model_executor/models/glmasr.py`


|
|

###

`forward(hidden_states, rotary_pos_emb_cos, rotary_pos_emb_sin)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderAttention.forward)

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderAttention.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[batch_size, seq_len, hidden_size]

-

(`rotary_pos_emb_cos`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderAttention.forward(rotary_pos_emb_cos))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[seq_len, rotary_dim/2] - cosine of rotary embeddings

-

(`rotary_pos_emb_sin`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderAttention.forward(rotary_pos_emb_sin))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[seq_len, rotary_dim/2] - sine of rotary embeddings


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[batch_size, seq_len, hidden_size]


## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrEncoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Optimized Transformer encoder layer for GLM-ASR. Combines attention and MLP with residual connections and layer norms.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderLayer.forward)Args:


## Source code in `vllm/model_executor/models/glmasr.py`


###

`forward(hidden_states, rotary_pos_emb_cos, rotary_pos_emb_sin)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderLayer.forward)

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderLayer.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[batch_size, seq_len, hidden_size]

-

(`rotary_pos_emb_cos`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderLayer.forward(rotary_pos_emb_cos))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[seq_len, rotary_dim/2] - cosine of rotary embeddings

-

(`rotary_pos_emb_sin`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderLayer.forward(rotary_pos_emb_sin))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[seq_len, rotary_dim/2] - sine of rotary embeddings


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[batch_size, seq_len, hidden_size]


## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrEncoderMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Optimized MLP for GLM-ASR encoder. Uses vLLM's parallel linear layers for better performance.

## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrEncoderRotaryEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderRotaryEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Rotary Position Embedding for GLM-ASR encoder.

Computes rotary position embeddings on-demand for efficiency. Only caches inv_freq as a buffer; cos/sin are computed during forward to avoid wasted computation during initialization and ensure correct device placement.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderRotaryEmbedding.forward)Compute rotary position frequencies for given sequence length.


## Source code in `vllm/model_executor/models/glmasr.py`


###

`forward(seq_len)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrEncoderRotaryEmbedding.forward)

Compute rotary position frequencies for given sequence length.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Frequency tensor with shape [seq_len, dim/2]. Use .cos() and

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor).sin() to get the rotary embedding components.


## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrFeatureInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrFeatureInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - num_chunks: Number of audio chunks (flattened) - nmb: Number of mel bins - num_audios: Number of original audio files

## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)[SupportsTranscription](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription)

Methods:

-
–[get_generation_prompt](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrForConditionalGeneration.get_generation_prompt)Get the generation prompt to be used for transcription requests.


## Source code in `vllm/model_executor/models/glmasr.py`


|
|

###

`_get_audio_token(model_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrForConditionalGeneration._get_audio_token)

Get the audio token from processor.

Similar to get_placeholder_str but returns single token.

## Source code in `vllm/model_executor/models/glmasr.py`


###

`get_generation_prompt(stt_params)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrForConditionalGeneration.get_generation_prompt)

Get the generation prompt to be used for transcription requests.

## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrMultiModalDataParser`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrMultiModalDataParser)

Bases: [MultiModalDataParser](https://docs.vllm.ai/multimodal/parse/#vllm.multimodal.parse.MultiModalDataParser)

Custom parser for GLM-ASR multimodal data.

Extends the base parser to handle GLM-ASR specific audio data formats, including both pre-computed audio embeddings and raw audio features.

## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrMultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrMultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)['GlmAsrProcessingInfo']

GLM-ASR processor that inherits directly from BaseMultiModalProcessor for better performance and cleaner implementation.

## Source code in `vllm/model_executor/models/glmasr.py`


|
|

##

`GlmAsrMultiModalProjector`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrMultiModalProjector)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Projects audio encoder outputs to language model hidden space.

This projector uses a two-layer MLP to map audio features from the encoder's intermediate size to the language model's hidden size. Uses vLLM's parallel linear layers for tensor parallelism support.

## Architecture

- Linear layer: intermediate_size -> hidden_size * 2
- Activation function (e.g., GELU)
- Linear layer: hidden_size * 2 -> hidden_size

## Source code in `vllm/model_executor/models/glmasr.py`


##

`GlmAsrProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr.GlmAsrProcessingInfo)

Bases: [BaseProcessingInfo](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseProcessingInfo)

Processing information provider for GLM-ASR model.

Provides access to model configuration, processor, and feature extractor needed for audio preprocessing and multimodal integration.

## Source code in `vllm/model_executor/models/glmasr.py`


##

`_GlmAsrEncoderOutput`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr._GlmAsrEncoderOutput)

Simple output container compatible with transformers' BaseModelOutput.

This lightweight container holds the encoder output and is compatible with the transformers library's output format while being more efficient than a full dataclass.

Attributes:

-
–`last_hidden_state`

Final layer hidden states from the encoder. Shape: [batch_size, seq_len, hidden_size]


## Source code in `vllm/model_executor/models/glmasr.py`


##

`_glmasr_field_config(hf_inputs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr._glmasr_field_config)

Configure multimodal field batching strategy for GLM-ASR.

Determines how to batch audio inputs based on whether chunking is used. When chunk_counts is present, features are flattened across chunks; otherwise, they are batched normally.

Parameters:

Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[MultiModalFieldConfig](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.MultiModalFieldConfig)]Dictionary mapping field names to MultiModalFieldConfig objects that specify batching behavior.