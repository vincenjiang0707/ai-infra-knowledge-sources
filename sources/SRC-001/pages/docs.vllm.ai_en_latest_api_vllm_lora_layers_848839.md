source: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/
lastmod: 2026-09-24

#

`vllm.lora.layers`

[¶](https://docs.vllm.ai#vllm.lora.layers)

Modules:

-
–[base](https://docs.vllm.ai/base/#vllm.lora.layers.base) -
–[base_linear](https://docs.vllm.ai/base_linear/#vllm.lora.layers.base_linear) -
–[column_parallel_linear](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear) -
–[fused_moe](https://docs.vllm.ai/fused_moe/#vllm.lora.layers.fused_moe) -
–[logits_processor](https://docs.vllm.ai/logits_processor/#vllm.lora.layers.logits_processor) -
–[replicated_linear](https://docs.vllm.ai/replicated_linear/#vllm.lora.layers.replicated_linear) -
–[row_parallel_linear](https://docs.vllm.ai/row_parallel_linear/#vllm.lora.layers.row_parallel_linear) -
–[utils](https://docs.vllm.ai/utils/#vllm.lora.layers.utils)

Classes:

-
–[BaseLayerWithLoRA](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA) -
–[ColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.ColumnParallelLinearWithLoRA)LoRA on top of ColumnParallelLinear layer.

-
–[ColumnParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.ColumnParallelLinearWithShardedLoRA)Differs from ColumnParallelLinearWithLoRA by slicing LoRA A also.

-
–[FusedMoE3DWithLoRA](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA) -
–[FusedMoEWithLoRA](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA) -
–[LogitsProcessorWithLoRA](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA)LoRA wrapper for LogitsProcessor, with extra logic to handle the

-
–[MergedColumnParallelLinearVariableSliceWithLoRA](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearVariableSliceWithLoRA)MergedColumnParallelLinear with variable number of slices (3+).

-
–[MergedColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearWithLoRA)ColumnParallelLinear layer that is composed of 2 sublayers (slices)

-
–[MergedColumnParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearWithShardedLoRA)Differs from MergedColumnParallelLinearWithLoRA by slicing the

-
–[MergedQKVParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.MergedQKVParallelLinearWithLoRA)MergedColumnParallelLinear layer that is composed of 3 sublayers (slices)

-
–[MergedQKVParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.MergedQKVParallelLinearWithShardedLoRA)Differs from MergedQKVParallelLinearWithLoRA by slicing the

-
–[QKVParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.QKVParallelLinearWithLoRA)ColumnParallelLinear layer that is specifically designed for

-
–[QKVParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.QKVParallelLinearWithShardedLoRA)Differs from QKVParallelLinearWithLoRA by slicing the

-
–[ReplicatedLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.ReplicatedLinearWithLoRA) -
–[RowParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.RowParallelLinearWithLoRA) -
–[RowParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.RowParallelLinearWithShardedLoRA)Differs from RowParallelLinearWithLoRA by slicing the


##

`BaseLayerWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[can_replace_layer](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.can_replace_layer)Returns True if the layer can be replaced by this LoRA layer.

-
–[create_lora_weights](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.create_lora_weights)Initializes lora matrices.

-
–[load_weights](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.load_weights)Load checkpoint weights into the wrapped base layer.

-
–[reset_lora](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.reset_lora)Resets the lora weights at index back to 0.

-
–[set_lora](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.set_lora)Overwrites lora tensors at index.

-
–[slice_lora_a](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.slice_lora_a)Slice lora a if splitting for tensor parallelism.

-
–[slice_lora_b](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.slice_lora_b)Slice lora b if splitting with tensor parallelism.


## Source code in `vllm/lora/layers/base.py`


###

`can_replace_layer(source_layer, lora_config, packed_modules_list, model_config=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.can_replace_layer)

Returns True if the layer can be replaced by this LoRA layer.

## Source code in `vllm/lora/layers/base.py`


###

`create_lora_weights(max_loras, lora_config, model_config=None)`

[¶](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.create_lora_weights)

###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.load_weights)

Load checkpoint weights into the wrapped base layer.

## Source code in `vllm/lora/layers/base.py`


###

`reset_lora(index)`

[¶](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.reset_lora)

###

`set_lora(index, lora_a, lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.set_lora)

###

`slice_lora_a(lora_a)`

[¶](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.slice_lora_a)

###

`slice_lora_b(lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.BaseLayerWithLoRA.slice_lora_b)

##

`ColumnParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.ColumnParallelLinearWithLoRA)

Bases: [BaseLinearLayerWithLoRA](https://docs.vllm.ai/base_linear/#vllm.lora.layers.base_linear.BaseLinearLayerWithLoRA)

LoRA on top of ColumnParallelLinear layer. LoRA B is sliced for tensor parallelism. There are two types for the `base_layer`

: 1. ColumnParallelLinear, e.g.`dense_h_to_4h`

in `FalconForCausalLM`

. 2. MergedColumnParallelLinear, e.g.`gate_up_proj`

in `Phi3ForCausalLM`

.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.lora.layers.ColumnParallelLinearWithLoRA.forward)Forward of ColumnParallelLinear


## Source code in `vllm/lora/layers/column_parallel_linear.py`


|
|

###

`forward(input_)`

[¶](https://docs.vllm.ai#vllm.lora.layers.ColumnParallelLinearWithLoRA.forward)

Forward of ColumnParallelLinear

Parameters:

Returns:

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`ColumnParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.ColumnParallelLinearWithShardedLoRA)

Bases: [ColumnParallelLinearWithLoRA](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA)

Differs from ColumnParallelLinearWithLoRA by slicing LoRA A also.

Based on S-LoRA, slicing happens along the rank dim.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`FusedMoE3DWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA)

Bases: [FusedMoEWithLoRA](https://docs.vllm.ai/fused_moe/#vllm.lora.layers.fused_moe.FusedMoEWithLoRA)

Methods:

-
–[can_replace_layer](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.can_replace_layer)Returns True if the layer can be replaced by this LoRA layer.

-
–[create_lora_weights](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.create_lora_weights)Initializes lora matrices.

-
–[set_lora](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.set_lora)Overwrites lora tensors at index.


Attributes:

-
–[w13_input_size](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.w13_input_size)Full size.

-
–[w13_output_size](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.w13_output_size)Full size.

-
–[w2_input_size](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.w2_input_size)Full size.

-
–[w2_output_size](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.w2_output_size)Full size.


## Source code in `vllm/lora/layers/fused_moe.py`


|
|

###

`w13_input_size`

`property`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.w13_input_size)

Full size.

###

`w13_output_size`

`property`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.w13_output_size)

Full size.

###

`w2_input_size`

`property`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.w2_input_size)

Full size.

###

`w2_output_size`

`property`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.w2_output_size)

Full size.

###

`can_replace_layer(source_layer, lora_config, packed_modules_list, model_config=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.can_replace_layer)

Returns True if the layer can be replaced by this LoRA layer.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`create_lora_weights(max_loras, lora_config, model_config=None)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.create_lora_weights)

Initializes lora matrices.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`set_lora(index, lora_a, lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoE3DWithLoRA.set_lora)

Overwrites lora tensors at index.

## Source code in `vllm/lora/layers/fused_moe.py`


##

`FusedMoEWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA)

Bases: [BaseLayerWithLoRA](https://docs.vllm.ai/base/#vllm.lora.layers.base.BaseLayerWithLoRA)

Methods:

-
–[can_replace_layer](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA.can_replace_layer)Returns True if the layer can be replaced by this LoRA layer.

-
–[create_lora_weights](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA.create_lora_weights)Initializes lora matrices.

-
–[reset_lora](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA.reset_lora)Resets the lora weights at index back to 0.

-
–[set_lora](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA.set_lora)Overwrites lora tensors at index.


## Source code in `vllm/lora/layers/fused_moe.py`


|
|

###

`_w13_a_num_experts`

`property`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA._w13_a_num_experts)

Expert-dim of the w13 lora_A buffer: 1 when shared.

###

`_w2_b_num_experts`

`property`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA._w2_b_num_experts)

Expert-dim of the w2 lora_B buffer: 1 when shared.

###

`_match_expert_dim(src, buffer)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA._match_expert_dim)

Align a LoRA factor's expert-dim (dim 0) to its stacked buffer.

Equal dims pass through. When the buffer is collapsed to expert-dim 1 (a shared factor) but the source carries per-expert copies, keep the first — every expert shares the same factor, so the copies are identical for a real adapter and irrelevant (zeros) for the dummy.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`_slice_w13_a(w13_lora_a)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA._slice_w13_a)

Applies to FusedMoEWithLoRA and FusedMoE3DWithLoRA.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`_slice_w2_a(w2_lora_a)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA._slice_w2_a)

Applies to FusedMoEWithLoRA and FusedMoE3DWithLoRA.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`_slice_w2_b(w2_lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA._slice_w2_b)

Applies to FusedMoEWithLoRA and FusedMoE3DWithLoRA.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`can_replace_layer(source_layer, lora_config, packed_modules_list, model_config=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA.can_replace_layer)

Returns True if the layer can be replaced by this LoRA layer.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`create_lora_weights(max_loras, lora_config, model_config=None)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA.create_lora_weights)

Initializes lora matrices.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`reset_lora(index)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA.reset_lora)

Resets the lora weights at index back to 0.

## Source code in `vllm/lora/layers/fused_moe.py`


###

`set_lora(index, lora_a, lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.FusedMoEWithLoRA.set_lora)

Overwrites lora tensors at index.

## Source code in `vllm/lora/layers/fused_moe.py`


##

`LogitsProcessorWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA)

Bases: [BaseLayerWithLoRA](https://docs.vllm.ai/base/#vllm.lora.layers.base.BaseLayerWithLoRA)

LoRA wrapper for LogitsProcessor, with extra logic to handle the application of the LoRA adapter.

Parameters:

-

(`base_layer`

[¶](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA(base_layer))

) –[LogitsProcessor](https://docs.vllm.ai/model_executor/layers/logits_processor/#vllm.model_executor.layers.logits_processor.LogitsProcessor)LogitsProcessor layer

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)hidden size of the model

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA(dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)data type of the model

-

(`device`

[¶](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)device of the model

-

(`sharded_to_full_mapping`

[¶](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA(sharded_to_full_mapping))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | Noneindex mapping from sharded vocab to full vocab received from base_layer.get_sharded_to_full_mapping(). If None, no reindexing will be done.


Methods:

-
–[reset_sharded_to_full_mapping](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA.reset_sharded_to_full_mapping)Restore the TP logits mapping after its GPU memory is reused.


## Source code in `vllm/lora/layers/logits_processor.py`


|
|

###

`reset_sharded_to_full_mapping()`

[¶](https://docs.vllm.ai#vllm.lora.layers.LogitsProcessorWithLoRA.reset_sharded_to_full_mapping)

Restore the TP logits mapping after its GPU memory is reused.

## Source code in `vllm/lora/layers/logits_processor.py`


##

`MergedColumnParallelLinearVariableSliceWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearVariableSliceWithLoRA)

Bases: [MergedColumnParallelLinearWithLoRA](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA)

MergedColumnParallelLinear with variable number of slices (3+).

This handles cases where the checkpoint has a single weight for the whole module (not split into slices), but the layer itself has multiple slices.

Methods:

-
–[set_lora](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearVariableSliceWithLoRA.set_lora)Override to handle single tensor weights


## Source code in `vllm/lora/layers/column_parallel_linear.py`


###

`set_lora(index, lora_a, lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearVariableSliceWithLoRA.set_lora)

Override to handle single tensor weights that need to be split into slices.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedColumnParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearWithLoRA)

Bases: [ColumnParallelLinearWithLoRA](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA)

ColumnParallelLinear layer that is composed of 2 sublayers (slices) packed together (e.g. gate_proj + up_proj -> gate_up_proj).

This means we have 2 LoRAs, each applied to one half of the layer.

Both slices must have the same size.

Methods:

-
–[create_lora_weights](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearWithLoRA.create_lora_weights)The main reason for overriding this function is to enhance code

-
–[expand_packed_lora](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearWithLoRA.expand_packed_lora)Expand packed adapter groups when they don't match n_slices.


## Source code in `vllm/lora/layers/column_parallel_linear.py`


|
|

###

`create_lora_weights(max_loras, lora_config, model_config=None)`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearWithLoRA.create_lora_weights)

The main reason for overriding this function is to enhance code maintainability.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


###

`expand_packed_lora(lora_a, lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearWithLoRA.expand_packed_lora)

Expand packed adapter groups when they don't match n_slices. E.g. in_proj_qkv (covers Q+K+V) + in_proj_z.

A None group member means that member was not adapted; the slice(s) it covers are emitted as None placeholders so subsequent groups stay aligned and those slices are left at base weights. This matches the None-tolerance already present in slice_lora_b() and the set_lora() stacking loop.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedColumnParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedColumnParallelLinearWithShardedLoRA)

Bases: [MergedColumnParallelLinearWithLoRA](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA)

Differs from MergedColumnParallelLinearWithLoRA by slicing the LoRA A's also.

Based on S-LoRA, slicing happens along the rank dim.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedQKVParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedQKVParallelLinearWithLoRA)

Bases: [MergedColumnParallelLinearWithLoRA](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA)

MergedColumnParallelLinear layer that is composed of 3 sublayers (slices) packed together in qkv proj fashion (q_proj + k_proj + v_proj -> qkv_proj).

This means we have 3 LoRAs, each applied to one slice of the layer.

Q slice may have different shape than K and V slices (which both have the same shape).

Methods:

-
–[create_lora_weights](https://docs.vllm.ai#vllm.lora.layers.MergedQKVParallelLinearWithLoRA.create_lora_weights)The main reason for overloading this function is to handle inconsistent


## Source code in `vllm/lora/layers/column_parallel_linear.py`


###

`create_lora_weights(max_loras, lora_config, model_config=None)`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedQKVParallelLinearWithLoRA.create_lora_weights)

The main reason for overloading this function is to handle inconsistent weight dimensions in qkv lora.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedQKVParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.MergedQKVParallelLinearWithShardedLoRA)

Bases: [MergedQKVParallelLinearWithLoRA](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear.MergedQKVParallelLinearWithLoRA)

Differs from MergedQKVParallelLinearWithLoRA by slicing the LoRA A's also.

Based on S-LoRA, slicing happens along the rank dim.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`QKVParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.QKVParallelLinearWithLoRA)

Bases: [ColumnParallelLinearWithLoRA](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA)

ColumnParallelLinear layer that is specifically designed for qkv_proj. Certain models, such as chatglm3 and baichuan-7b, only contains a single LoRA within their qkv_proj layer.

During inference with Tensor Parallel, the weights of lora_b must be accurately partitioned according to the respective ranks.

Q slice may have different shape than K and V slices (which both have the same shape).

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`QKVParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.QKVParallelLinearWithShardedLoRA)

Bases: [QKVParallelLinearWithLoRA](https://docs.vllm.ai/column_parallel_linear/#vllm.lora.layers.column_parallel_linear.QKVParallelLinearWithLoRA)

Differs from QKVParallelLinearWithLoRA by slicing the LoRA A's also.

Based on S-LoRA, slicing happens along the rank dim.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`ReplicatedLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.ReplicatedLinearWithLoRA)

Bases: [BaseLinearLayerWithLoRA](https://docs.vllm.ai/base_linear/#vllm.lora.layers.base_linear.BaseLinearLayerWithLoRA)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.lora.layers.ReplicatedLinearWithLoRA.forward)Forward of ReplicatedLinearWithLoRA.

-
–[slice_lora_a](https://docs.vllm.ai#vllm.lora.layers.ReplicatedLinearWithLoRA.slice_lora_a)Slice lora a if splitting for tensor parallelism.

-
–[slice_lora_b](https://docs.vllm.ai#vllm.lora.layers.ReplicatedLinearWithLoRA.slice_lora_b)Slice lora b if splitting with tensor parallelism.


## Source code in `vllm/lora/layers/replicated_linear.py`


###

`forward(input_)`

[¶](https://docs.vllm.ai#vllm.lora.layers.ReplicatedLinearWithLoRA.forward)

Forward of ReplicatedLinearWithLoRA.

Parameters:

Returns:

## Source code in `vllm/lora/layers/replicated_linear.py`


###

`slice_lora_a(lora_a)`

[¶](https://docs.vllm.ai#vllm.lora.layers.ReplicatedLinearWithLoRA.slice_lora_a)

Slice lora a if splitting for tensor parallelism.

###

`slice_lora_b(lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.ReplicatedLinearWithLoRA.slice_lora_b)

Slice lora b if splitting with tensor parallelism.

##

`RowParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.RowParallelLinearWithLoRA)

Bases: [BaseLinearLayerWithLoRA](https://docs.vllm.ai/base_linear/#vllm.lora.layers.base_linear.BaseLinearLayerWithLoRA)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.lora.layers.RowParallelLinearWithLoRA.forward)Forward of RowParallelLinear.


## Source code in `vllm/lora/layers/row_parallel_linear.py`


###

`forward(input_)`

[¶](https://docs.vllm.ai#vllm.lora.layers.RowParallelLinearWithLoRA.forward)

Forward of RowParallelLinear.

Parameters:

-

(`input_`

[¶](https://docs.vllm.ai#vllm.lora.layers.RowParallelLinearWithLoRA.forward(input_))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor whose last dimension is

`input_size`

. If`input_is_parallel`

is set, then the last dimension is`input_size // tp_size`

.

Returns:

## Source code in `vllm/lora/layers/row_parallel_linear.py`


##

`RowParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.RowParallelLinearWithShardedLoRA)

Bases: [RowParallelLinearWithLoRA](https://docs.vllm.ai/row_parallel_linear/#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithLoRA)

Differs from RowParallelLinearWithLoRA by slicing the LoRA B's also.

Based on S-LoRA, slicing happens along the output dim. This yields a combined partial sum from the row parallel base layer and column partitioned output from the LoRA.

## Source code in `vllm/lora/layers/row_parallel_linear.py`


|
|