source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/linear/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.linear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear)

Classes:

-
–[ColumnParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear)Linear layer with column parallelism.

-
–[DCPGroupColumnParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.DCPGroupColumnParallelLinear)Column-parallel linear whose weight is sharded across DCP groups.

-
–[KimiK3MergedQKVGateLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.KimiK3MergedQKVGateLinear)Kimi-K3 QKV-A projection fused with its output-gate projection.

-
–[LinearBase](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase)Base linear layer.

-
–[LinearMethodBase](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase)Base class for different (maybe quantized) linear methods.

-
–[MergedColumnParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear)Packed linear layers with column parallelism.

-
–[MinimaxM3QKVParallelLinearWithIndexer](https://docs.vllm.ai#vllm.model_executor.layers.linear.MinimaxM3QKVParallelLinearWithIndexer)QKV projection fused with a lightning-indexer's index_q/index_k.

-
–[QKVParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear)Linear layers for the attention's QKV transformation.

-
–[ReplicatedLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear)Replicated linear layer.

-
–[RowParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear)Linear layer with row parallelism.

-
–[UnquantizedLinearMethod](https://docs.vllm.ai#vllm.model_executor.layers.linear.UnquantizedLinearMethod)Linear method without quantization.


Functions:

-
–[adjust_scalar_to_fused_array](https://docs.vllm.ai#vllm.model_executor.layers.linear.adjust_scalar_to_fused_array)For fused modules (QKV and MLP) we have an array of length

-
–[register_weight_loader_v2_supported_method](https://docs.vllm.ai#vllm.model_executor.layers.linear.register_weight_loader_v2_supported_method)Decorator to register a LinearMethod as supporting weight_loader_v2.


##

`ColumnParallelLinear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear)

Bases: [LinearBase](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase)

Linear layer with column parallelism.

The linear layer is defined as Y = XA + b. A is parallelized along its second dimension as A = [A_1, ..., A_p].

Parameters:

-

(`input_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(input_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)first dimension of matrix A.

-

(`output_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(output_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)second dimension of matrix A.

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, add bias.

-

(`gather_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(gather_output))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, call all-gather on output and make Y available to all GPUs, otherwise, every GPU will have its output which is Y_i = XA_i

-

(`skip_bias_add`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(skip_bias_add))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –This was added to enable performance optimizations where bias can be fused with other element-wise operations. we skip adding bias but instead return it.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for the parameters.

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –Quantization configure.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –The name of the layer in the state dict, including all parents (e.g. model.layers.0.qkv_proj)

-

(`return_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(return_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, return bias together with outputs in forward pass.

-

(`disable_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(disable_tp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, weights matrix won't be sharded through tp rank.

-

(`tp_rank`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(tp_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Override the tensor-parallel rank used for sharding. Defaults to the global TP rank. Used to shard at a coarser granularity than one shard per rank (see

`DCPGroupColumnParallelLinear`

). -

(`tp_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear(tp_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Override the tensor-parallel world size used for sharding. Defaults to the global TP world size.


## Source code in `vllm/model_executor/layers/linear.py`


|
|

##

`DCPGroupColumnParallelLinear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.DCPGroupColumnParallelLinear)

Bases: [ColumnParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear)

Column-parallel linear whose weight is sharded across DCP groups.

With Decode Context Parallelism (DCP) the KV cache is sharded across a DCP group, so MLA decode must attend the group's full head set. This layer shards its output across DCP *groups* (effective tp size `tp_size // dcp_world_size`

) rather than across every rank, so each rank in a group holds the whole group's heads, letting decode skip the query all-gather.

:meth:`forward`

returns the group's full head set. :meth:`_local_view`

extracts this rank's TP shard for prefill.

## Source code in `vllm/model_executor/layers/linear.py`


###

`_local_view(out)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.DCPGroupColumnParallelLinear._local_view)

Slice this rank's tp head shard from a group-heads output.

`out`

is head-shaped, i.e. `(..., group_heads, head_dim)`

.

## Source code in `vllm/model_executor/layers/linear.py`


##

`KimiK3MergedQKVGateLinear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.KimiK3MergedQKVGateLinear)

Bases: [MergedColumnParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear)

Kimi-K3 QKV-A projection fused with its output-gate projection.

NOTE: Kimi-K3-specific. This is tailored to its replicated Q/KV latent projections and tensor-parallel output gate; it is not a general-purpose linear layer. It lives here alongside `MergedColumnParallelLinear`

, whose sharding and weight-loading machinery it reuses.

The per-rank shard layout is `[q_a | kv_a | gate]`

. The latent shards stay replicated across tensor-parallel ranks while the gate shard is tensor-parallel, matching the standalone projections they replace.

## Source code in `vllm/model_executor/layers/linear.py`


|
|

##

`LinearBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase)

Bases: [PluggableLayer](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.PluggableLayer)

Base linear layer.

Parameters:

-

(`input_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase(input_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)input dimension of the linear layer.

-

(`output_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase(output_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)output dimension of the linear layer.

-

(`skip_bias_add`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase(skip_bias_add))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, skip adding bias but instead return it.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for the parameters.

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –Quantization configure.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Prefix for parameter names.

-

(`return_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase(return_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, return bias together with outputs in forward pass.

-

(`disable_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase(disable_tp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, tensor parallelism will be disabled for this layer.


## Source code in `vllm/model_executor/layers/linear.py`


|
|

##

`LinearMethodBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase)

Bases: [QuantizeMethodBase](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase)

Base class for different (maybe quantized) linear methods.

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.apply)Apply the weights in layer to the input tensor.

-
–[create_weights](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.create_weights)Create weights for a linear layer.


## Source code in `vllm/model_executor/layers/linear.py`


###

`apply(layer, x, bias=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.apply)

Apply the weights in layer to the input tensor. Expects create_weights to have been called before on the layer.

## Source code in `vllm/model_executor/layers/linear.py`


###

`create_weights(layer, input_size_per_partition, output_partition_sizes, input_size, output_size, params_dtype, **extra_weight_attrs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.create_weights)

Create weights for a linear layer. The weights will be set as attributes of the layer.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.create_weights(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The layer that is using the LinearMethodBase factory.

-

(`input_size_per_partition`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.create_weights(input_size_per_partition))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the weight input dim on rank X.

-

(`output_partition_sizes`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.create_weights(output_partition_sizes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Sizes of the output dim of each logical weight on rank X. E.g., output_partition_sizes for QKVLinear is a list contains the width of Wq, Wk, Wv on rank X.

-

(`input_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.create_weights(input_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the input dim of the weight across all ranks.

-

(`output_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.create_weights(output_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the output dim of the weight across all ranks.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase.create_weights(params_dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Datatype of the parameters.


## Source code in `vllm/model_executor/layers/linear.py`


##

`MergedColumnParallelLinear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear)

Bases: [ColumnParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear)

Packed linear layers with column parallelism.

Similar to ColumnParallelLinear, but the weight matrix is concatenated along the output dimension. When the weight matrix is loaded, the different partitions are sharded separately.

Parameters:

-

(`input_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(input_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)input dimension of the linear layer.

-

(`output_sizes`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(output_sizes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]list of output dimensions of the linear layer.

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, add bias.

-

(`gather_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(gather_output))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, call all-gather on output and make the output available to all GPUs, otherwise, every GPU will have its own output.

-

(`skip_bias_add`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(skip_bias_add))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –This was added to enable performance optimizations where bias can be fused with other element-wise operations. we skip adding bias but instead return it.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for the parameters.

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –Quantization configure.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –The name of the layer in the state dict, including all parents (e.g. model.layers.0.qkv_proj)

-

(`return_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(return_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, return bias together with outputs in forward pass.

-

(`disable_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear(disable_tp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, all weights matrix won't be sharded, this layer will be treated as a "Replicated" MergedLinear.


## Source code in `vllm/model_executor/layers/linear.py`


|
|

###

`_load_fused_module_from_checkpoint(param, loaded_weight, output_sizes=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MergedColumnParallelLinear._load_fused_module_from_checkpoint)

Handle special case for models where MLP layers are already fused on disk. In this case, we have no shard id. This function determines the shard id by splitting these layers and then calls the weight loader using the shard id.

An example of a model with these fused layers: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

## Source code in `vllm/model_executor/layers/linear.py`


##

`MinimaxM3QKVParallelLinearWithIndexer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.MinimaxM3QKVParallelLinearWithIndexer)

Bases: [QKVParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear)

QKV projection fused with a lightning-indexer's index_q/index_k.

NOTE: MiniMax-M3-specific. This is tailored to the M3 sparse-attention layers (it assumes the indexer's head count equals the KV head count and shares the main head_dim); it is not a general-purpose linear layer. It lives here only to sit alongside QKVParallelLinear, whose sharding / weight-loading machinery it reuses.

A single column-parallel GEMM emits, per rank::

```
[q | k | v | index_q | index_k]
```


`index_q`

must have the same head count as the KV heads (`total_num_index_heads == total_num_kv_heads`

) and `index_head_size == head_size`

, so it shards exactly like K/V -- including the KV-head *replication* path when `tp_size > total_num_kv_heads`

(this is what makes a TP size greater than the KV-head count work). `index_k`

is a single shared head, replicated to every rank.

## Source code in `vllm/model_executor/layers/linear.py`


|
|

##

`QKVParallelLinear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear)

Bases: [ColumnParallelLinear](https://docs.vllm.ai#vllm.model_executor.layers.linear.ColumnParallelLinear)

Linear layers for the attention's QKV transformation.

Linear layers for the linear transformation of the query, key, and value vectors in the attention layer. The weight matrix is concatenated along the output dimension. The layer is parallelized along the head dimension. When the number of key/value heads is smaller than the number of query heads (e.g., multi-query/grouped-query attention), the key/value head may be replicated while the query heads are partitioned.

Parameters:

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)input hidden state size of the transformer.

-

(`head_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(head_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of each attention head.

-

(`total_num_heads`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(total_num_heads))

) –[int](https://docs.python.org/3/builtins/functions.html#int)total number of attention query heads.

-

(`total_num_kv_heads`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(total_num_kv_heads))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –total number of attention key/value heads. If None, assume total_num_kv_heads = total_num_heads.

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, add bias.

-

(`skip_bias_add`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(skip_bias_add))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –This was added to enable performance optimizations where bias can be fused with other element-wise operations. we skip adding bias but instead return it.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for the parameters.

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –Quantization configure.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –The name of the layer in the state dict, including all parents (e.g. model.layers.0.qkv_proj)

-

(`return_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(return_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, return bias together with outputs in forward pass.

-

(`disable_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear(disable_tp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, weights matrix won't be sharded through tp rank.


## Source code in `vllm/model_executor/layers/linear.py`


|
|

###

`_load_fused_module_from_checkpoint(param, loaded_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.QKVParallelLinear._load_fused_module_from_checkpoint)

Handle special case for models where QKV layers are already fused on disk. In this case, we have no shard id. This function determines the shard id by splitting these layers and then calls the weight loader using the shard id.

An example of a model with these fused layers: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

## Source code in `vllm/model_executor/layers/linear.py`


##

`ReplicatedLinear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear)

Bases: [LinearBase](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase)

Replicated linear layer.

Parameters:

-

(`input_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(input_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)input dimension of the linear layer.

-

(`output_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(output_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)output dimension of the linear layer.

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, add bias.

-

(`skip_bias_add`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(skip_bias_add))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, skip adding bias but instead return it.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for the parameters.

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –Quantization configure.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –The name of the layer in the state dict, including all parents (e.g. model.layers.0.qkv_proj)

-

(`return_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(return_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, return bias together with outputs in forward pass.

-

(`disable_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.ReplicatedLinear(disable_tp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Take no effect for replicated linear layers.


## Source code in `vllm/model_executor/layers/linear.py`


|
|

##

`RowParallelLinear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear)

Bases: [LinearBase](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearBase)

Linear layer with row parallelism.

The linear layer is defined as Y = XA + b. A is parallelized along its first dimension and X along its second dimension as: - - | A_1 | | . | A = | . | X = [X_1, ..., X_p] | . | | A_p | - -

Parameters:

-

(`input_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(input_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)first dimension of matrix A.

-

(`output_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(output_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)second dimension of matrix A.

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, add bias. Note that bias is not parallelized.

-

(`input_is_parallel`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(input_is_parallel))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, we assume that the input is already split across the GPUs and we do not split again.

-

(`skip_bias_add`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(skip_bias_add))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –This was added to enable performance optimization where bias can be fused with other element-wise operations. We skip adding bias but instead return it.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for the parameters.

-

(`reduce_results`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(reduce_results))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, call all-reduce on output and make Y available to all GPUs, otherwise, every GPU will have its output which is Y = X_iA_i

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –Quantization configure.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –The name of the layer in the state dict, including all parents (e.g. model.layers.0.down_proj)

-

(`return_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(return_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If true, return bias together with outputs in forward pass.

-

(`disable_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.RowParallelLinear(disable_tp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, weights matrix won't be sharded through tp rank.


## Source code in `vllm/model_executor/layers/linear.py`


|
|

##

`UnquantizedLinearMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.UnquantizedLinearMethod)

Bases: [LinearMethodBase](https://docs.vllm.ai#vllm.model_executor.layers.linear.LinearMethodBase)

Linear method without quantization.

## Source code in `vllm/model_executor/layers/linear.py`


##

`adjust_scalar_to_fused_array(param_data, loaded_weight, shard_id)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.adjust_scalar_to_fused_array)

For fused modules (QKV and MLP) we have an array of length N that holds 1 scale for each "logical" matrix. So the param is an array of length N. The loaded_weight corresponds to one of the shards on disk. Here, we slice the param based on the shard_id for loading.

## Source code in `vllm/model_executor/layers/linear.py`


##

`register_weight_loader_v2_supported_method(cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.linear.register_weight_loader_v2_supported_method)

Decorator to register a LinearMethod as supporting weight_loader_v2.