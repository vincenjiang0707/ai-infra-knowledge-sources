source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/vision/
lastmod: 2026-09-24

#

`vllm.model_executor.models.vision`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision)

Classes:

-
–[FusedInputNorm](https://docs.vllm.ai#vllm.model_executor.models.vision.FusedInputNorm)Module that applies rescaling and normalization to input images.


Functions:

-
–[get_fp8_padded_hidden_size](https://docs.vllm.ai#vllm.model_executor.models.vision.get_fp8_padded_hidden_size)Return the padded hidden size for FP8 ViT encoder attention, or

-
–[get_load_balance_assignment](https://docs.vllm.ai#vllm.model_executor.models.vision.get_load_balance_assignment)Generate load balancing assignment and metadata

-
–[get_multimodal_config](https://docs.vllm.ai#vllm.model_executor.models.vision.get_multimodal_config)Return the current

`MultiModalConfig`

, or`None`

when no engine -
–[get_vit_attn_backend](https://docs.vllm.ai#vllm.model_executor.models.vision.get_vit_attn_backend)Get the attention backend for Vision Transformer.

-
–[is_vit_use_data_parallel](https://docs.vllm.ai#vllm.model_executor.models.vision.is_vit_use_data_parallel)Get the tensor parallel type for Vision Transformer.

-
–[resolve_visual_encoder_outputs](https://docs.vllm.ai#vllm.model_executor.models.vision.resolve_visual_encoder_outputs)Given the outputs a visual encoder module that may correspond to the

-
–[run_dp_sharded_mrope_vision_model](https://docs.vllm.ai#vllm.model_executor.models.vision.run_dp_sharded_mrope_vision_model)Run a vision model with data parallelism (DP) sharding.

-
–[run_dp_sharded_vision_model](https://docs.vllm.ai#vllm.model_executor.models.vision.run_dp_sharded_vision_model)Run a vision model with data parallelism (DP) sharding. The function


##

`FusedInputNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.FusedInputNorm)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Module that applies rescaling and normalization to input images. Equivalent to: output = (input * rescale_factor - mean) / std

## Source code in `vllm/model_executor/models/vision.py`


|
|

##

`_get_vit_attn_backend(head_size, dtype, *, attn_backend_override=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision._get_vit_attn_backend)

Get the available attention backend for Vision Transformer.

## Source code in `vllm/model_executor/models/vision.py`


##

`get_fp8_padded_hidden_size(num_heads, head_dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.get_fp8_padded_hidden_size)

Return the padded hidden size for FP8 ViT encoder attention, or `None`

when FP8 is not enabled.

cuDNN FP8 prefill attention requires `head_dim`

to be a multiple of 16. For non-aligned `head_dim`

(e.g. 72), Q/K/V are padded to the nearest multiple of 16.

## Source code in `vllm/model_executor/models/vision.py`


##

`get_load_balance_assignment(sizes, num_gpus=2)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.get_load_balance_assignment)

Generate load balancing assignment and metadata for distributing data across GPUs. The load is determined by the total image sizes, not the number of images.

Parameters:

-

(`sizes`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.get_load_balance_assignment(sizes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The size of each image

-

(`num_gpus`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.get_load_balance_assignment(num_gpus))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`2`

) –Number of GPUs to balance across


Returns:

-
(`shuffle_indices`


) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Indices to reorder data for balanced loading

-
(`gpu_sample_counts`


) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Number of samples assigned to each GPU

-
(`grouped_sizes_per_gpu`


) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Total size assigned to each GPU


## Source code in `vllm/model_executor/models/vision.py`


##

`get_multimodal_config()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.get_multimodal_config)

Return the current `MultiModalConfig`

, or `None`

when no engine config context is active (e.g., during unit tests) or when the current `model_config`

does not carry a `multimodal_config`

(e.g., minimal stubs used in tests).

## Source code in `vllm/model_executor/models/vision.py`


##

`get_vit_attn_backend(head_size, dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.get_vit_attn_backend)

Get the attention backend for Vision Transformer.

## Source code in `vllm/model_executor/models/vision.py`


##

`is_vit_use_data_parallel(num_heads=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.is_vit_use_data_parallel)

Get the tensor parallel type for Vision Transformer.

## Source code in `vllm/model_executor/models/vision.py`


##

`resolve_visual_encoder_outputs(encoder_outputs, post_layer_norm, *, select_layers=None, max_possible_layers=None, last_hs_proc=None, feature_select_strategy=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.resolve_visual_encoder_outputs)

Given the outputs a visual encoder module that may correspond to the output of the last layer, or a list of hidden states to be stacked, handle post normalization and resolve it into a single output tensor.

Parameters:

-

(`encoder_outputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.resolve_visual_encoder_outputs(encoder_outputs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Output of encoder's last layer or all hidden states.

-

(`post_layer_norm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.resolve_visual_encoder_outputs(post_layer_norm))

) –[LayerNorm](https://pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html#torch.nn.LayerNorm)| NonePost norm to apply to the output of the encoder.

-

(`select_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.resolve_visual_encoder_outputs(select_layers))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –Optional layer indices to grab from the encoder outputs; if provided, encoder outputs must be a list.

-

(`max_possible_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.resolve_visual_encoder_outputs(max_possible_layers))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Total layers in the fully loaded visual encoder.

-

(`last_hs_proc`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.resolve_visual_encoder_outputs(last_hs_proc))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] | None`None`

) –Optional callable to be applied to the last layer if it is used, e.g., pooling head for Siglip. This is done prior to feature selection and layer normalization. If select_layers are provided, the output of last_hs_proc must be able to be concatenated with the other select_layers along the last dimension.

-

(`feature_select_strategy`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.resolve_visual_encoder_outputs(feature_select_strategy))`VisionFeatureSelectStrategy | None`

, default:`None`

) –Defines how to select the hidden states from each layer.


## Source code in `vllm/model_executor/models/vision.py`


|
|

##

`run_dp_sharded_mrope_vision_model(vision_model, pixel_values, grid_thw_list, *, rope_type)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.run_dp_sharded_mrope_vision_model)

Run a vision model with data parallelism (DP) sharding. The function will shard the input image tensor on the first dimension and run the vision model. This function is used to run the vision model with mrope.

Parameters:

-

(`vision_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.run_dp_sharded_mrope_vision_model(vision_model))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)Vision model.

-

(`pixel_values`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.run_dp_sharded_mrope_vision_model(pixel_values))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Image/Video input tensor.

-

(`grid_thw_list`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.run_dp_sharded_mrope_vision_model(grid_thw_list))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]List of grid dimensions for each image

-

(`rope_type`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.run_dp_sharded_mrope_vision_model(rope_type))

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['rope_3d', 'rope_2d']Type of rope used in the vision model. Different rope types have different dimension to do ViT. "rope_3d" for 3D rope (e.g., Qwen2.5-VL) "rope_2d" for 2D rope (e.g., Kimi-VL)


Returns:

## Example

## Source code in `vllm/model_executor/models/vision.py`


|
|

##

`run_dp_sharded_vision_model(image_input, vision_model)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.vision.run_dp_sharded_vision_model)

Run a vision model with data parallelism (DP) sharding. The function will shard the input image tensor on the first dimension and run the vision model

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor: Output image embeddings