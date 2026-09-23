source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/parameter/
lastmod: 2026-09-23

#

`vllm.model_executor.parameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter)

Classes:

-
–[BasevLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter)Base parameter for vLLM linear layers. Extends the torch.nn.parameter

-
–[ChannelQuantScaleParameter](https://docs.vllm.ai#vllm.model_executor.parameter.ChannelQuantScaleParameter)Parameter class for weight scales loaded for weights with

-
–[GroupQuantScaleParameter](https://docs.vllm.ai#vllm.model_executor.parameter.GroupQuantScaleParameter)Parameter class for weight scales loaded for weights with

-
–[ModelWeightParameter](https://docs.vllm.ai#vllm.model_executor.parameter.ModelWeightParameter)Parameter class for linear layer weights. Uses both column and

-
–[PackedColumnParameter](https://docs.vllm.ai#vllm.model_executor.parameter.PackedColumnParameter)Parameter for model parameters which are packed on disk

-
–[PackedvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.PackedvLLMParameter)Parameter for model weights which are packed on disk.

-
–[PerTensorScaleParameter](https://docs.vllm.ai#vllm.model_executor.parameter.PerTensorScaleParameter)Parameter class for scales where the number of scales is

-
–[RowvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.RowvLLMParameter)Parameter class defining weight_loading functionality


##

`BasevLLMParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter)

Bases: `Parameter`


Base parameter for vLLM linear layers. Extends the torch.nn.parameter by taking in a linear weight loader. Will copy the loaded weight into the parameter when the provided weight loader is called.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter.__init__)Initialize the BasevLLMParameter.


## Source code in `vllm/model_executor/parameter.py`


|
|

###

`__init__(data, weight_loader)`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter.__init__)

Initialize the BasevLLMParameter.

Parameters:

-

(`data`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter.__init__(data))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch tensor with the parameter data

-

(`weight_loader`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter.__init__(weight_loader))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)weight loader callable


## Source code in `vllm/model_executor/parameter.py`


##

`BlockQuantScaleParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.BlockQuantScaleParameter)

Bases:

, [_ColumnvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter._ColumnvLLMParameter)[RowvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.RowvLLMParameter)

Parameter class for weight scales loaded for weights with block-wise quantization. Uses both column and row parallelism.

## Source code in `vllm/model_executor/parameter.py`


##

`ChannelQuantScaleParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.ChannelQuantScaleParameter)

Bases: [_ColumnvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter._ColumnvLLMParameter)

Parameter class for weight scales loaded for weights with channel-wise quantization. Equivalent to _ColumnvLLMParameter.

## Source code in `vllm/model_executor/parameter.py`


##

`GroupQuantScaleParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.GroupQuantScaleParameter)

Bases:

, [_ColumnvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter._ColumnvLLMParameter)[RowvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.RowvLLMParameter)

Parameter class for weight scales loaded for weights with grouped quantization. Uses both column and row parallelism.

## Source code in `vllm/model_executor/parameter.py`


##

`ModelWeightParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.ModelWeightParameter)

Bases:

, [_ColumnvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter._ColumnvLLMParameter)[RowvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.RowvLLMParameter)

Parameter class for linear layer weights. Uses both column and row parallelism.

## Source code in `vllm/model_executor/parameter.py`


##

`PackedColumnParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.PackedColumnParameter)

Bases: [_ColumnvLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter._ColumnvLLMParameter)

Parameter for model parameters which are packed on disk and support column parallelism only. See PackedvLLMParameter for more details on the packed properties.

## Source code in `vllm/model_executor/parameter.py`


##

`PackedvLLMParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.PackedvLLMParameter)

Bases: [ModelWeightParameter](https://docs.vllm.ai#vllm.model_executor.parameter.ModelWeightParameter)

Parameter for model weights which are packed on disk. Example: GPTQ Marlin weights are int4 or int8, packed into int32. Extends the ModelWeightParameter to take in the packed factor, the packed dimension, and optionally, marlin tile size for marlin kernels. Adjusts the shard_size and shard_offset for fused linear layers model weight loading by accounting for packing and optionally, marlin tile size.

## Source code in `vllm/model_executor/parameter.py`


##

`PerTensorScaleParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.PerTensorScaleParameter)

Bases: [BasevLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter)

Parameter class for scales where the number of scales is equivalent to the number of logical matrices in fused linear layers (e.g. for QKV, there are 3 scales loaded from disk). This is relevant to weights with per-tensor quantization. Adds functionality to map the scalers to a shard during weight loading.

Note: additional parameter manipulation may be handled for each quantization config specifically, within process_weights_after_loading

## Source code in `vllm/model_executor/parameter.py`


###

`_load_into_shard_id(loaded_weight, shard_id, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.PerTensorScaleParameter._load_into_shard_id)

Slice the parameter data based on the shard id for loading.

## Source code in `vllm/model_executor/parameter.py`


##

`RowvLLMParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.RowvLLMParameter)

Bases: [BasevLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter)

Parameter class defining weight_loading functionality (load_row_parallel_weight) for parameters being loaded into linear layers with row parallel functionality. Requires an input_dim to be defined.

## Source code in `vllm/model_executor/parameter.py`


##

`SharedWeightParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.SharedWeightParameter)

Bases: [BasevLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter)

Parameter for weights with many shared tensors across a model.

For example, when applying transforms to the "gate" and "up" partitions of `MergedColumnParallelLinear`

, the transform weights must stay separate tensors in order to allow for tensor memory sharing between layers.

Methods:

-
–[add_partition](https://docs.vllm.ai#vllm.model_executor.parameter.SharedWeightParameter.add_partition)Add a partition to the weight parameter. Partitions whose

`data_key`


## Source code in `vllm/model_executor/parameter.py`


|
|

###

`add_partition(index, data_key, *args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.SharedWeightParameter.add_partition)

Add a partition to the weight parameter. Partitions whose `data_key`

is the same will share tensor data

Parameters:

-

(`index`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.SharedWeightParameter.add_partition(index))

) –[int](https://docs.python.org/3/builtins/functions.html#int)index of partition to add

-

(`data_key`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.SharedWeightParameter.add_partition(data_key))

) –[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable)hashable key used to key shared tensors

-

(`*args`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.SharedWeightParameter.add_partition(*args))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`()`

) –arguments for

`torch.empty`

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.SharedWeightParameter.add_partition(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –keyword arguments for

`torch.empty`


## Source code in `vllm/model_executor/parameter.py`


##

`_ColumnvLLMParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter._ColumnvLLMParameter)

Bases: [BasevLLMParameter](https://docs.vllm.ai#vllm.model_executor.parameter.BasevLLMParameter)

Private class defining weight loading functionality (load_merged_column_weight, load_qkv_weight) for parameters being loaded into linear layers with column parallelism. This includes QKV and MLP layers which are not already fused on disk. Requires an output dimension to be defined. Called within the weight loader of each of the column parallel linear layers.

## Source code in `vllm/model_executor/parameter.py`


##

`permute_param_layout_(param, input_dim, output_dim, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.parameter.permute_param_layout_)

Permute a parameter's layout to the specified input and output dimensions, useful for forcing the parameter into a known layout, for example, if I need a packed (quantized) weight matrix to be in the layout {input_dim = 0, output_dim = 1, packed_dim = 0} then I can call: permute_param_layout_(x, input_dim=0, output_dim=1, packed_dim=0) to ensure x is in the correct layout (permuting it to the correct layout if required, asserting if it cannot get it to the correct layout)