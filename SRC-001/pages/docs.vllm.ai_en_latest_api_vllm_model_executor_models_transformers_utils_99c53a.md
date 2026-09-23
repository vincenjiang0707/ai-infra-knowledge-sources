source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/utils/
lastmod: 2026-09-23

#

`vllm.model_executor.models.transformers.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils)

Transformers modeling backend utilities.

Functions:

-
–[attrsetter](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.attrsetter)Set a possibly nested attribute, like the inverse of attrgetter.

-
–[can_enable_torch_compile](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.can_enable_torch_compile)Callable to be passed to

`@support_torch_compile`

's`enable_if`

argument. -
–[init_on_device_without_buffers](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.init_on_device_without_buffers)A context manager under which models are initialized with all

-
–[maybe_per_layer](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.maybe_per_layer)Pick

`layer_idx`

's entry from a config field that may be sized per layer. -
–[named_state](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.named_state)`module`

's own state (i.e. named parameters and buffers). -
–[recursive_replace_linear](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.recursive_replace_linear)Recursively replace linear modules in the model as needed.

-
–[replace_conv_class](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_conv_class)Replace a Transformers Conv2d/Conv3d with vLLM's Conv2d/Conv3d.

-
–[replace_embedding_class](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_embedding_class)Replace

`nn.Embedding`

with`VocabParallelEmbedding`

. -
–[replace_linear_class](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_linear_class)Replace nn.Linear with one of vLLM's tensor parallel linear classes.


##

`_UninitializedEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils._UninitializedEmbedding)

Bases: [Embedding](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding)

Make `__init__`

inert, so that `VocabParallelEmbedding.__init__`

' call to `super().__init__`

does not invoke `nn.Embedding.__init__`

.

## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`_VocabParallelEmbeddingBase`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils._VocabParallelEmbeddingBase)

Bases:

, [VocabParallelEmbedding](https://docs.vllm.ai/layers/vocab_parallel_embedding/#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding)[_UninitializedEmbedding](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils._UninitializedEmbedding)

Orders `VocabParallelEmbedding`

ahead of `nn.Embedding`

in the MRO, so that `super().forward(...)`

in an `nn.Embedding`

subclass reaches vLLM's embedding.

## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`_rebase_on_vocab_parallel(cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils._rebase_on_vocab_parallel)

Subclass `cls`

so that `VocabParallelEmbedding`

supersedes its `nn.Embedding`

.

Parameters:

-

(`cls`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils._rebase_on_vocab_parallel(cls))

) –[type](https://docs.python.org/3/builtins/functions.html#type)[[Embedding](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding)]The

`nn.Embedding`

subclass to rebase. Cached, so a given`cls`

always maps to the same class.

Returns:

-

–[type](https://docs.python.org/3/builtins/functions.html#type)[[VocabParallelEmbedding](https://docs.vllm.ai/layers/vocab_parallel_embedding/#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding)]The new class, to assign to

`__class__`

of an instance of`cls`

.

## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`attrsetter(attr)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.attrsetter)

Set a possibly nested attribute, like the inverse of attrgetter.

## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`can_enable_torch_compile(vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.can_enable_torch_compile)

Callable to be passed to `@support_torch_compile`

's `enable_if`

argument.

Defaults to `True`

but is disabled in the following situations:

- The model uses dynamic rope scaling.

## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`init_on_device_without_buffers(device)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.init_on_device_without_buffers)

A context manager under which models are initialized with all parameters on the specified device. However buffers are not initialized on specified device.

Parameters:

-

(`device`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.init_on_device_without_buffers(device))``torch.device``

) –Device to initialize all parameters on.


## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`maybe_per_layer(value, layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.maybe_per_layer)

Pick `layer_idx`

's entry from a config field that may be sized per layer.

##

`named_state(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.named_state)

`module`

's own state (i.e. named parameters and buffers).

##

`recursive_replace_linear(model, quant_config, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.recursive_replace_linear)

Recursively replace linear modules in the model as needed.

## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`replace_conv_class(conv)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_conv_class)

Replace a Transformers Conv2d/Conv3d with vLLM's Conv2d/Conv3d.

Parameters:

-

(`conv`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_conv_class(conv))`TorchConv`

) –`nn.Conv2d`

or`nn.Conv3d`

to be replaced.

Returns:

-
`VllmConv | TorchConv`

–The new

`Conv2dLayer`

or`Conv3dLayer`

. If the conv module is not supported, -
`VllmConv | TorchConv`

–returns the original conv module.


## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`replace_embedding_class(embedding, quant_config=None, *, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_embedding_class)

Replace `nn.Embedding`

with `VocabParallelEmbedding`

.

Parameters:

-

(`embedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_embedding_class(embedding))

) –[Embedding](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding)The

`nn.Embedding`

holding a vocab table. -

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_embedding_class(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –Quantization config for the new embedding.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_embedding_class(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Qualname of

`embedding`

, used to look up its quantization method.

Returns:

-

–[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The module to install in

`embedding`

's place.

## Source code in `vllm/model_executor/models/transformers/utils.py`


##

`replace_linear_class(linear, style='replicate', quant_config=None, *, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_linear_class)

Replace nn.Linear with one of vLLM's tensor parallel linear classes.

Parameters:

-

(`linear`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_linear_class(linear))

) –[Linear](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html#torch.nn.Linear)`nn.Linear`

to be replaced. -

(`style`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_linear_class(style))`Style`

, default:`'replicate'`

) –Tensor parallel style of the new linear, e.g. "colwise".

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_linear_class(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –Quantization config for the new linear.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.utils.replace_linear_class(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Module prefix of the new linear, used for quantization lookup.


Returns:

-

–[ColumnParallelLinear](https://docs.vllm.ai/layers/linear/#vllm.model_executor.layers.linear.ColumnParallelLinear)|[RowParallelLinear](https://docs.vllm.ai/layers/linear/#vllm.model_executor.layers.linear.RowParallelLinear)|[ReplicatedLinear](https://docs.vllm.ai/layers/linear/#vllm.model_executor.layers.linear.ReplicatedLinear)The new linear.