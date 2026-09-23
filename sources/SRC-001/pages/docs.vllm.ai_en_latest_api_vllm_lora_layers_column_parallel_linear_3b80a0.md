source: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/column_parallel_linear/
lastmod: 2026-09-23

#

`vllm.lora.layers.column_parallel_linear`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear)

Classes:

-
–[ColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA)LoRA on top of ColumnParallelLinear layer.

-
–[ColumnParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithShardedLoRA)Differs from ColumnParallelLinearWithLoRA by slicing LoRA A also.

-
–[MergedColumnParallelLinearVariableSliceWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearVariableSliceWithLoRA)MergedColumnParallelLinear with variable number of slices (3+).

-
–[MergedColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA)ColumnParallelLinear layer that is composed of 2 sublayers (slices)

-
–[MergedColumnParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithShardedLoRA)Differs from MergedColumnParallelLinearWithLoRA by slicing the

-
–[MergedQKVParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedQKVParallelLinearWithLoRA)MergedColumnParallelLinear layer that is composed of 3 sublayers (slices)

-
–[MergedQKVParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedQKVParallelLinearWithShardedLoRA)Differs from MergedQKVParallelLinearWithLoRA by slicing the

-
–[QKVParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.QKVParallelLinearWithLoRA)ColumnParallelLinear layer that is specifically designed for

-
–[QKVParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.QKVParallelLinearWithShardedLoRA)Differs from QKVParallelLinearWithLoRA by slicing the


##

`ColumnParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA)

Bases: [BaseLinearLayerWithLoRA](https://docs.vllm.ai/base_linear/#vllm.lora.layers.base_linear.BaseLinearLayerWithLoRA)

LoRA on top of ColumnParallelLinear layer. LoRA B is sliced for tensor parallelism. There are two types for the `base_layer`

: 1. ColumnParallelLinear, e.g.`dense_h_to_4h`

in `FalconForCausalLM`

. 2. MergedColumnParallelLinear, e.g.`gate_up_proj`

in `Phi3ForCausalLM`

.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA.forward)Forward of ColumnParallelLinear


## Source code in `vllm/lora/layers/column_parallel_linear.py`


|
|

###

`forward(input_)`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA.forward)

Forward of ColumnParallelLinear

Parameters:

Returns:

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`ColumnParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithShardedLoRA)

Bases: [ColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA)

Differs from ColumnParallelLinearWithLoRA by slicing LoRA A also.

Based on S-LoRA, slicing happens along the rank dim.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedColumnParallelLinearVariableSliceWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearVariableSliceWithLoRA)

Bases: [MergedColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA)

MergedColumnParallelLinear with variable number of slices (3+).

This handles cases where the checkpoint has a single weight for the whole module (not split into slices), but the layer itself has multiple slices.

Methods:

-
–[set_lora](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearVariableSliceWithLoRA.set_lora)Override to handle single tensor weights


## Source code in `vllm/lora/layers/column_parallel_linear.py`


###

`set_lora(index, lora_a, lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearVariableSliceWithLoRA.set_lora)

Override to handle single tensor weights that need to be split into slices.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedColumnParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA)

Bases: [ColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA)

ColumnParallelLinear layer that is composed of 2 sublayers (slices) packed together (e.g. gate_proj + up_proj -> gate_up_proj).

This means we have 2 LoRAs, each applied to one half of the layer.

Both slices must have the same size.

Methods:

-
–[create_lora_weights](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA.create_lora_weights)The main reason for overriding this function is to enhance code

-
–[expand_packed_lora](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA.expand_packed_lora)Expand packed adapter groups when they don't match n_slices.


## Source code in `vllm/lora/layers/column_parallel_linear.py`


|
|

###

`create_lora_weights(max_loras, lora_config, model_config=None)`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA.create_lora_weights)

The main reason for overriding this function is to enhance code maintainability.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


###

`expand_packed_lora(lora_a, lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA.expand_packed_lora)

Expand packed adapter groups when they don't match n_slices. E.g. in_proj_qkv (covers Q+K+V) + in_proj_z.

A None group member means that member was not adapted; the slice(s) it covers are emitted as None placeholders so subsequent groups stay aligned and those slices are left at base weights. This matches the None-tolerance already present in slice_lora_b() and the set_lora() stacking loop.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedColumnParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithShardedLoRA)

Bases: [MergedColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA)

Differs from MergedColumnParallelLinearWithLoRA by slicing the LoRA A's also.

Based on S-LoRA, slicing happens along the rank dim.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedQKVParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedQKVParallelLinearWithLoRA)

Bases: [MergedColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedColumnParallelLinearWithLoRA)

MergedColumnParallelLinear layer that is composed of 3 sublayers (slices) packed together in qkv proj fashion (q_proj + k_proj + v_proj -> qkv_proj).

This means we have 3 LoRAs, each applied to one slice of the layer.

Q slice may have different shape than K and V slices (which both have the same shape).

Methods:

-
–[create_lora_weights](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedQKVParallelLinearWithLoRA.create_lora_weights)The main reason for overloading this function is to handle inconsistent


## Source code in `vllm/lora/layers/column_parallel_linear.py`


###

`create_lora_weights(max_loras, lora_config, model_config=None)`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedQKVParallelLinearWithLoRA.create_lora_weights)

The main reason for overloading this function is to handle inconsistent weight dimensions in qkv lora.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`MergedQKVParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedQKVParallelLinearWithShardedLoRA)

Bases: [MergedQKVParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.MergedQKVParallelLinearWithLoRA)

Differs from MergedQKVParallelLinearWithLoRA by slicing the LoRA A's also.

Based on S-LoRA, slicing happens along the rank dim.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`QKVParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.QKVParallelLinearWithLoRA)

Bases: [ColumnParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.ColumnParallelLinearWithLoRA)

ColumnParallelLinear layer that is specifically designed for qkv_proj. Certain models, such as chatglm3 and baichuan-7b, only contains a single LoRA within their qkv_proj layer.

During inference with Tensor Parallel, the weights of lora_b must be accurately partitioned according to the respective ranks.

Q slice may have different shape than K and V slices (which both have the same shape).

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`QKVParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.QKVParallelLinearWithShardedLoRA)

Bases: [QKVParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear.QKVParallelLinearWithLoRA)

Differs from QKVParallelLinearWithLoRA by slicing the LoRA A's also.

Based on S-LoRA, slicing happens along the rank dim.

## Source code in `vllm/lora/layers/column_parallel_linear.py`


##

`_mcp_apply(x, bias, layer)`

[¶](https://docs.vllm.ai#vllm.lora.layers.column_parallel_linear._mcp_apply)

Fully-sharded (S-LoRA) apply path for column-parallel LoRA layers.