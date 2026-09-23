source: https://docs.vllm.ai/en/latest/api/vllm/models/dots3_note/nvidia/audio_encoder/
lastmod: 2026-09-23

#

`vllm.models.dots3_note.nvidia.audio_encoder`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder)

Dots-path speech encoder for inference only (single GPU).

Ported from cybertron_alm `dots_audio_encoder/modeling_whisper.py`

. Upstream `WhisperEncoder`

is exposed as :class:`DotsSpeechEncoder`

.

Classes:

-
–[DotsSpeechEncoder](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder)Transformer encoder consisting of

*config.encoder_layers*self attention layers. Each layer is a

##

`DotsSpeechEncoder`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder)

Bases: `DotsSpeechPreTrainedModel`


Transformer encoder consisting of *config.encoder_layers* self attention layers. Each layer is a [`WhisperEncoderLayer`

].

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder(config))`WhisperConfig`

) –WhisperConfig


Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder.forward)Mel

`[B, n_mels, T]`

→ encoder hidden states. Inference-only.

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


|
|

###

`_conv2d_stem_one_chunk(chunk, chunk_valid_mel_lens=None)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder._conv2d_stem_one_chunk)

Run 3x Conv2d(stride=2) + GELU with per-layer masking.

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


###

`_forward_conv1d_stem(input_features)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder._forward_conv1d_stem)

Standard Conv1d stem: conv1 + conv2(stride=2), 2x downsample. Returns [B, T/2, embed_dim].

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


###

`_forward_conv2d_stem(input_features, input_seq_lens=None, audio_sample_lens=None)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder._forward_conv2d_stem)

Conv2D stem: 3x Conv2d(stride=2) → 8x downsample. Returns [B, T/8, embed_dim].

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


###

`_forward_latent_stem(input_features)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder._forward_latent_stem)

Latent input stem: conv1+GLU + conv2, stride=1, no downsample. Returns [B, T, embed_dim].

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


###

`_temporal_mask(feat, valid_lens)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder._temporal_mask)

Zero out temporal positions >= valid_lens. feat: [B,C,F,T], valid_lens: [B] tensor.

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


###

`forward(input_features, input_seq_lens=None, audio_sample_lens=None, output_attentions=None, output_hidden_states=None, return_dict=None)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.DotsSpeechEncoder.forward)

Mel `[B, n_mels, T]`

→ encoder hidden states. Inference-only.

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


|
|

##

`WhisperAttention`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-headed attention from 'Attention Is All You Need' paper.

Methods:

-
–[forward_flash_attn](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperAttention.forward_flash_attn)Dense eager attention with SGLang FA3 for packed variable-length input.


## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


|
|

###

`forward_flash_attn(hidden_states, cu_seqlens_q=None, cu_seqlens_kv=None, max_seqlen_q=None, max_seqlen_kv=None, output_attentions=False, rotary_cos=None, rotary_sin=None)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperAttention.forward_flash_attn)

Dense eager attention with SGLang FA3 for packed variable-length input.

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


##

`WhisperEncoderLayer`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward)Args:


## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


|
|

###

`forward(hidden_states, cu_seqlens_q=None, cu_seqlens_kv=None, max_seqlen_q=None, max_seqlen_kv=None, output_attentions=False, rotary_cos=None, rotary_sin=None)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward)

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input to the layer of shape

`(batch, seq_len, embed_dim)`

, or`(total_tokens, embed_dim)`

when`cu_seqlens_q`

is given. -

(`cu_seqlens_q`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward(cu_seqlens_q))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –Cumulative query sequence lengths for packed variable-length input. If

`None`

, the input is treated as a padded batch. -

(`cu_seqlens_kv`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward(cu_seqlens_kv))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –Cumulative key/value sequence lengths for packed variable-length input.

-

(`max_seqlen_q`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward(max_seqlen_q))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Longest query sequence in the packed batch.

-

(`max_seqlen_kv`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward(max_seqlen_kv))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Longest key/value sequence in the packed batch.

-

(`output_attentions`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward(output_attentions))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to also return the attention weights.

-

(`rotary_cos`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward(rotary_cos))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Cosine component of the rotary position embedding.

-

(`rotary_sin`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.audio_encoder.WhisperEncoderLayer.forward(rotary_sin))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Sine component of the rotary position embedding.


Returns:

-

–[Any](https://docs.python.org/3/library/typing.html#typing.Any)A tuple of the output hidden states, followed by the attention

-
`...`

–weights if

`output_attentions`

is`True`

.

## Source code in `vllm/models/dots3_note/nvidia/audio_encoder.py`


|
|