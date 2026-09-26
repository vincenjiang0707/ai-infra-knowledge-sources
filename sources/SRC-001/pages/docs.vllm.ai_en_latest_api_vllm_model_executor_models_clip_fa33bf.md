source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/clip/
lastmod: 2026-09-24

#

`vllm.model_executor.models.clip`

[¶](https://docs.vllm.ai#vllm.model_executor.models.clip)

Classes:

-
–[CLIPAttention](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPAttention) -
–[CLIPEncoder](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPEncoder)Transformer encoder consisting of

`config.num_hidden_layers`

self -
–[CLIPImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPImagePixelInputs)Dimensions:


Functions:

-
–[dual_encoder_has_text_tokens](https://docs.vllm.ai#vllm.model_executor.models.clip.dual_encoder_has_text_tokens)Whether a dual-encoder pooling batch still contains text tokens.

-
–[merge_dual_encoder_text_and_vision](https://docs.vllm.ai#vllm.model_executor.models.clip.merge_dual_encoder_text_and_vision)Restore vision embeddings on multimodal tokens after the text encoder.


##

`CLIPAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPAttention.forward)Input shape: Batch x Time x Channel.


## Source code in `vllm/model_executor/models/clip.py`


###

`forward(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPAttention.forward)

Input shape: Batch x Time x Channel.

## Source code in `vllm/model_executor/models/clip.py`


##

`CLIPEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPEncoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer encoder consisting of `config.num_hidden_layers`

self attention layers. Each layer is a [`CLIPEncoderLayer`

].

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPEncoder(config))`CLIPTextConfig | CLIPVisionConfig`

) –CLIPConfig


## Source code in `vllm/model_executor/models/clip.py`


##

`CLIPImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.clip.CLIPImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of images - c: Number of channels (3) - h: Height of each image - w: Width of each image

## Source code in `vllm/model_executor/models/clip.py`


##

`dual_encoder_has_text_tokens(has_mm_embeddings, is_multimodal)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.clip.dual_encoder_has_text_tokens)

Whether a dual-encoder pooling batch still contains text tokens.

`embed_input_ids`

used to treat "the batch has any image embeddings" as "the whole batch is vision-only". Mixed image+text batches then skipped the text encoder, so completion-style text embeddings collapsed (issue

### 53091). Honor the per-token `is_multimodal`

mask instead.[¶](https://docs.vllm.ai#vllm.model_executor.models.clip.dual_encoder_has_text_tokens--53091-honor-the-per-token-is_multimodal-mask-instead)

## Source code in `vllm/model_executor/models/clip.py`


##

`merge_dual_encoder_text_and_vision(text_features, vision_embeds, is_multimodal)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.clip.merge_dual_encoder_text_and_vision)

Restore vision embeddings on multimodal tokens after the text encoder.

The model runner builds `is_multimodal`

on CPU; text and vision features are on the compute device.