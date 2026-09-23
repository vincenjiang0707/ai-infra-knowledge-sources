source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/utils/
lastmod: 2026-09-23

#

`vllm.model_executor.models.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils)

Classes:

-
–[AutoWeightsLoader](https://docs.vllm.ai#vllm.model_executor.models.utils.AutoWeightsLoader)Helper class to load weights into a

. It is able`torch.nn.Module`

-
–[PPMissingLayer](https://docs.vllm.ai#vllm.model_executor.models.utils.PPMissingLayer)A placeholder layer for missing layers in a pipeline parallel model.

-
–[WeightsMapper](https://docs.vllm.ai#vllm.model_executor.models.utils.WeightsMapper)Maps the name of each weight if they match the following patterns.


Functions:

-
–[collect_children](https://docs.vllm.ai#vllm.model_executor.models.utils.collect_children)Within this context, collect all direct child assignments to

`module`

, -
–[extract_layer_index](https://docs.vllm.ai#vllm.model_executor.models.utils.extract_layer_index)Extract the layer index from the module name.

-
–[fast_topk](https://docs.vllm.ai#vllm.model_executor.models.utils.fast_topk)Optimized topk implementation that uses torch.max for k=1 case.

-
–[flatten_bn](https://docs.vllm.ai#vllm.model_executor.models.utils.flatten_bn)Flatten the

`B`

and`N`

dimensions of batched multimodal inputs. -
–[get_draft_quant_config](https://docs.vllm.ai#vllm.model_executor.models.utils.get_draft_quant_config)Get quantization config for Draft models.

-
–[get_layer_index](https://docs.vllm.ai#vllm.model_executor.models.utils.get_layer_index)Given a signed vision feature layer, get the number of hidden layers

-
–[get_pp_missing_layer_names](https://docs.vllm.ai#vllm.model_executor.models.utils.get_pp_missing_layer_names)Get the names of the missing layers in a pipeline parallel model.

-
–[get_spec_layer_idx_from_weight_name](https://docs.vllm.ai#vllm.model_executor.models.utils.get_spec_layer_idx_from_weight_name)Return the MTP layer index a weight belongs to, or None.

-
–[init_vllm_registered_model](https://docs.vllm.ai#vllm.model_executor.models.utils.init_vllm_registered_model)Helper function to initialize an inner model registered to vLLM,

-
–[is_pp_missing_parameter](https://docs.vllm.ai#vllm.model_executor.models.utils.is_pp_missing_parameter)Check if a parameter is missing in a pipeline parallel model.

-
–[make_layers](https://docs.vllm.ai#vllm.model_executor.models.utils.make_layers)Make a list of layers with the given layer function, taking

-
–[maybe_fuse_shared_experts](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_fuse_shared_experts)Route AITER fused-shared-expert checkpoint weights into fused slots.

-
–[maybe_prefix](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_prefix)Add a prefix to a name if the prefix is non-empty.

-
–[no_init_weights](https://docs.vllm.ai#vllm.model_executor.models.utils.no_init_weights)Within this context, prevent weight initialization from using device memory and

-
–[process_eagle_weight](https://docs.vllm.ai#vllm.model_executor.models.utils.process_eagle_weight)Update EAGLE model flags based on loaded weight name.

-
–[scatter_output_slices](https://docs.vllm.ai#vllm.model_executor.models.utils.scatter_output_slices)Slice a concatenated output tensor and scatter into dest by index.

-
–[skip_spec_layers](https://docs.vllm.ai#vllm.model_executor.models.utils.skip_spec_layers)Drop MTP spec-layer weights (loaded by the MTP head, not the base model).

-
–[spec_decode_needs_target_embed](https://docs.vllm.ai#vllm.model_executor.models.utils.spec_decode_needs_target_embed)Whether the last PP rank needs the target input embedding.


Attributes:

-
([ShardId](https://docs.vllm.ai#vllm.model_executor.models.utils.ShardId)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)One shard of a stacked parameter. A tuple is a single contiguous span.

-
([ShardIds](https://docs.vllm.ai#vllm.model_executor.models.utils.ShardIds)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)One shard, or a list of shards the same weight is loaded into in turn.


##

`ShardId = str | int | tuple[int, ...]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.ShardId)

One shard of a stacked parameter. A tuple is a single contiguous span.

##

`ShardIds = ShardId | list[ShardId]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.ShardIds)

One shard, or a list of shards the same weight is loaded into in turn.

##

`AutoWeightsLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.AutoWeightsLoader)

Helper class to load weights into a [ torch.nn.Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module). It is able to automatically detect child modules and parameters while iterating over the weights only once.

The weight loading logic for individual modules can be overridden by defining a `load_weights`

method.

Similarly, the weight loading logic for individual parameters can be overridden by defining a `weight_loader`

method.

Detailed weight loading information can be viewed by setting the environment variable `VLLM_LOGGING_LEVEL=DEBUG`

.

## Source code in `vllm/model_executor/models/utils.py`


|
|

###

`_add_loadable_non_param_tensors(module, child_params)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.AutoWeightsLoader._add_loadable_non_param_tensors)

Add tensor names that are not in the model params that may be in the safetensors, e.g., batch normalization stats and registered buffers.

## Source code in `vllm/model_executor/models/utils.py`


###

`_check_skipped_aliases(autoloaded_weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.AutoWeightsLoader._check_skipped_aliases)

Guard against skipping an alias whose canonical name never loads.

## Source code in `vllm/model_executor/models/utils.py`


##

`PPMissingLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.PPMissingLayer)

Bases: [Identity](https://pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity)

A placeholder layer for missing layers in a pipeline parallel model.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.utils.PPMissingLayer.forward)Return the first arg from args or the first value from kwargs.


## Source code in `vllm/model_executor/models/utils.py`


###

`forward(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.PPMissingLayer.forward)

##

`WeightsMapper`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.WeightsMapper)

Maps the name of each weight if they match the following patterns.

If a key maps to a value of `None`

, the corresponding weight is ignored.

Methods:

-
–[__or__](https://docs.vllm.ai#vllm.model_executor.models.utils.WeightsMapper.__or__)Combine two

`WeightsMapper`

s by merging their mappings. -
–[get_rename_mapper](https://docs.vllm.ai#vllm.model_executor.models.utils.WeightsMapper.get_rename_mapper)Mapper variant keeping only the renames.


## Source code in `vllm/model_executor/models/utils.py`


|
|

###

`__or__(other)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.WeightsMapper.__or__)

Combine two `WeightsMapper`

s by merging their mappings.

## Source code in `vllm/model_executor/models/utils.py`


###

`_map_name(key)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.WeightsMapper._map_name)

Map a weight name (backward-compatible wrapper that discards shard_id).

###

`_map_name_with_shard(key)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.WeightsMapper._map_name_with_shard)

Map a weight name and extract any shard_id metadata.

Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[ShardIds](https://docs.vllm.ai#vllm.model_executor.models.utils.ShardIds)| None] | None(mapped_name, shard_id) if the name should be kept. A list of shard

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[ShardIds](https://docs.vllm.ai#vllm.model_executor.models.utils.ShardIds)| None] | Noneids means the weight is loaded into each of those shards in turn.

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[ShardIds](https://docs.vllm.ai#vllm.model_executor.models.utils.ShardIds)| None] | NoneNone if the name should be dropped.


## Source code in `vllm/model_executor/models/utils.py`


###

`get_rename_mapper()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.WeightsMapper.get_rename_mapper)

Mapper variant keeping only the renames.

This is what consumers that *name* modules rather than load them need: LoRA name parsing and the quantization config's layer lists.

Stacked maps are dropped so that constituent names (e.g. `q_proj`

) survive rather than being rewritten to the stacked vLLM name (`qkv_proj`

). Mappings to `None`

are dropped because "do not load this weight" is meaningless to such a consumer, and applying it would silently shrink a quantization config's ignore list or make LoRA name parsing fail.

## Source code in `vllm/model_executor/models/utils.py`


##

`_embedding_count_expression(embeddings)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils._embedding_count_expression)

Constructs a debugging representation of the number of embeddings in the NestedTensors.

## Source code in `vllm/model_executor/models/utils.py`


##

`_flatten_embeddings(embeddings)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils._flatten_embeddings)

Recursively flattens and concatenates NestedTensors on all but the last dimension.

## Source code in `vllm/model_executor/models/utils.py`


##

`_get_tied_embedding_params(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils._get_tied_embedding_params)

Map each tied word embedding qualname to the first name it aliases.

## Source code in `vllm/model_executor/models/utils.py`


##

`_merge_multimodal_embeddings(inputs_embeds, multimodal_embeddings, is_multimodal)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils._merge_multimodal_embeddings)

Merge `multimodal_embeddings`

into `inputs_embeds`

by overwriting the positions in `inputs_embeds`

corresponding to placeholder tokens in `input_ids`

.

## Note

This updates `inputs_embeds`

in place.

## Source code in `vllm/model_executor/models/utils.py`


##

`collect_children(module, *, targets=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.collect_children)

Within this context, collect all direct child assignments to `module`

, returning a list of children names that is internally updated until the context is exited.

If `targets`

is set, instead collect descendents of `module`

that are an instance of `targets`

, even if they aren't direct children.

## Source code in `vllm/model_executor/models/utils.py`


##

`extract_layer_index(layer_name, num_attn_module=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.extract_layer_index)

Extract the layer index from the module name.

Examples: - "encoder.layers.0" -> 0 - "encoder.layers.1.self_attn" -> 1 - "2.self_attn" -> 2 - "model.encoder.layers.0.sub.1" -> ValueError if num_attn_module == 1

## Source code in `vllm/model_executor/models/utils.py`


##

`fast_topk(values, topk, dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.fast_topk)

Optimized topk implementation that uses torch.max for k=1 case.

This function provides better performance for the common case of k=1 by using torch.max instead of the more general torch.topk.

Parameters:

-

(`values`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.fast_topk(values))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor to find top-k values from

-

(`topk`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.fast_topk(topk))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of top values to return (k). Must be > 0.

-

(`dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.fast_topk(dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Dimension along which to compute topk


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tuple of (values, indices) where values are the top-k values

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)and indices are their corresponding indices in the input tensor


## Source code in `vllm/model_executor/models/utils.py`


##

`flatten_bn(x, *, concat=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.flatten_bn)

Flatten the `B`

and `N`

dimensions of batched multimodal inputs.

The input tensor should have shape `(B, N, ...)`

.

## Source code in `vllm/model_executor/models/utils.py`


##

`get_draft_quant_config(vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_draft_quant_config)

Get quantization config for Draft models.

Draft models should use their own quantization config instead of the verifier/target model's config. This helper retrieves the draft model's quantization config.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_draft_quant_config(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)The vLLM configuration object.


Returns:

-

–[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| NoneThe draft model's config if available, None otherwise.


## Source code in `vllm/model_executor/models/utils.py`


##

`get_layer_index(feature_layer_index, num_hidden_layers)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_layer_index)

Given a signed vision feature layer, get the number of hidden layers needed to leverage it.

Parameters:

-

(`feature_layer_index`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_layer_index(feature_layer_index))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of a required layer in the visual encoder.

-

(`num_hidden_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_layer_index(num_hidden_layers))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The total number of hidden layers in the visual encoder.


## Source code in `vllm/model_executor/models/utils.py`


##

`get_pp_missing_layer_names(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_pp_missing_layer_names)

Get the names of the missing layers in a pipeline parallel model.

## Source code in `vllm/model_executor/models/utils.py`


##

`get_spec_layer_idx_from_weight_name(config, weight_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_spec_layer_idx_from_weight_name)

Return the MTP layer index a weight belongs to, or None.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_spec_layer_idx_from_weight_name(config))

) –[ModelConfig](https://docs.vllm.ai/config/model/#vllm.config.model.ModelConfig)The model config; must expose

`num_hidden_layers`

and, for MTP checkpoints,`num_nextn_predict_layers`

. -

(`weight_name`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.get_spec_layer_idx_from_weight_name(weight_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Checkpoint weight name to classify.


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe absolute layer index for an MTP-layer weight, else None.


## Source code in `vllm/model_executor/models/utils.py`


##

`init_vllm_registered_model(vllm_config, *, prefix='', hf_config=None, architectures=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.init_vllm_registered_model)

Helper function to initialize an inner model registered to vLLM, based on the arguments passed to the outer vLLM model.

## Source code in `vllm/model_executor/models/utils.py`


##

`is_pp_missing_parameter(name, model)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.is_pp_missing_parameter)

Check if a parameter is missing in a pipeline parallel model.

## Source code in `vllm/model_executor/models/utils.py`


##

`make_layers(num_hidden_layers, layer_fn, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.make_layers)

Make a list of layers with the given layer function, taking pipeline parallelism into account.

Parameters:

-

(`num_hidden_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.make_layers(num_hidden_layers))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of hidden layers in the model.

-

(`layer_fn`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.make_layers(layer_fn))`LayerFn`

) –Function to create a layer given its index.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.make_layers(prefix))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Prefix for layer names.


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[ModuleList](https://pytorch.org/docs/stable/generated/torch.nn.ModuleList.html#torch.nn.ModuleList)]Tuple of (start_layer, end_layer, modules).


## Source code in `vllm/model_executor/models/utils.py`


##

`maybe_fuse_shared_experts(weights, *, n_routed_experts, n_shared_experts, ckpt_prefix='mlp.shared_experts', enabled=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_fuse_shared_experts)

Route AITER fused-shared-expert checkpoint weights into fused slots.

When AITER fused-shared-experts is active, shared experts are packed into the routed expert tensor. The checkpoint stores them under `ckpt_prefix`

as a single (possibly widened) tensor; this splits it into `n_shared_experts`

chunks named `mlp.experts.{n_routed_experts + j}`

so the `RoutedExperts`

loader treats them as extra experts. Yields the input unchanged when the fusion is inactive, so callers can wrap unconditionally.

Parameters:

-

(`weights`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_fuse_shared_experts(weights))

) –[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Iterable of

`(name, tensor)`

checkpoint pairs. -

(`n_routed_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_fuse_shared_experts(n_routed_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of routed experts; offsets the fused slots.

-

(`n_shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_fuse_shared_experts(n_shared_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of shared experts packed into the tensor.

-

(`ckpt_prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_fuse_shared_experts(ckpt_prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'mlp.shared_experts'`

) –Checkpoint module name of the shared experts.

-

(`enabled`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_fuse_shared_experts(enabled))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)| None`None`

) –Whether AITER fused-shared-experts is active. Defaults to

`rocm_aiter_ops.is_fusion_moe_shared_experts_enabled()`

; pass an explicit value only when the model gates on something more (e.g. quant-spec compatibility) and it must match its construction-time decision.

Yields:

## Source code in `vllm/model_executor/models/utils.py`


##

`maybe_prefix(prefix, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_prefix)

Add a prefix to a name if the prefix is non-empty.

Parameters:

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_prefix(prefix))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The prefix to add. If empty, no prefix will be added.

-

(`name`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.maybe_prefix(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name to potentially prefix.


Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)The string "prefix.name" if prefix was non-empty, otherwise just "name".


## Source code in `vllm/model_executor/models/utils.py`


##

`no_init_weights(module, placeholder, *, targets=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.no_init_weights)

Within this context, prevent weight initialization from using device memory and replace direct child assignments to `module`

with the result of `placeholder()`

.

If `targets`

is set, instead prevent weight initialization and replace assignments where the child is an instance of `targets`

, even if they aren't direct children of `module`

.

## Source code in `vllm/model_executor/models/utils.py`


##

`process_eagle_weight(model, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.process_eagle_weight)

Update EAGLE model flags based on loaded weight name. This should be called during weight loading to detect if a model has its own lm_head or embed_tokens weight.

Parameters:

-

(`model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.process_eagle_weight(model))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The model instance (must support EAGLE)

-

(`name`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.process_eagle_weight(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name of the weight to process


## Source code in `vllm/model_executor/models/utils.py`


##

`scatter_output_slices(output, indices, per_item_out_tokens, dest, clone=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.scatter_output_slices)

Slice a concatenated output tensor and scatter into dest by index.

## Source code in `vllm/model_executor/models/utils.py`


##

`skip_spec_layers(weights, config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.skip_spec_layers)

Drop MTP spec-layer weights (loaded by the MTP head, not the base model).

Parameters:

-

(`weights`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.skip_spec_layers(weights))

) –[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Iterable of

`(name, tensor)`

checkpoint pairs. -

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.skip_spec_layers(config))

) –[ModelConfig](https://docs.vllm.ai/config/model/#vllm.config.model.ModelConfig)The model config, passed to

`get_spec_layer_idx_from_weight_name`

.

Yields:

## Source code in `vllm/model_executor/models/utils.py`


##

`spec_decode_needs_target_embed(vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.utils.spec_decode_needs_target_embed)

Whether the last PP rank needs the target input embedding.