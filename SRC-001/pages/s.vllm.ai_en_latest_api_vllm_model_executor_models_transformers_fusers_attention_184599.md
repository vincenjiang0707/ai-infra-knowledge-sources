source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/fusers/attention/
lastmod: 2026-09-23

#

`vllm.model_executor.models.transformers.fusers.attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention)

Attention fuser: the module that dispatches to the attention interface.

Classes:

-
–[AttentionFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser)A module that dispatches through the Transformers attention interface.


Functions:

-
–[interface_call](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.interface_call)The attention interface call in

`forward`

, if it makes exactly one.

##

`AttentionFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser)

Bases: [BaseFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.BaseFuser)

A module that dispatches through the Transformers attention interface.

Methods:

-
–[layer_index](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.layer_index)The layer

`module`

computes attention for, if it declares one. -
–[scale](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.scale)The softmax scale

`module`

passes to the interface, or`None`

. -
–[sinks](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.sinks)The per-head sink tensor

`module`

passes to the interface, or`None`

. -
–[validate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.validate)Whether

`module`

will actually dispatch to vLLM.

Attributes:

-
([s_aux_expr](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.s_aux_expr)`expr | None`

) –Source of the

`s_aux=`

the module hands the interface, if it hands one. -
([scale_expr](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.scale_expr)`expr | None`

) –Source of the

`scaling=`

the module hands the interface, if it hands one. -
([source_cls](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.source_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Class of the HF module that dispatches (for logging).


## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


|
|

###

`s_aux_expr = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.s_aux_expr)

Source of the `s_aux=`

the module hands the interface, if it hands one.

###

`scale_expr = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.scale_expr)

Source of the `scaling=`

the module hands the interface, if it hands one.

###

`source_cls`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.source_cls)

Class of the HF module that dispatches (for logging).

###

`layer_index(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.layer_index)

The layer `module`

computes attention for, if it declares one.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


###

`scale(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.scale)

The softmax scale `module`

passes to the interface, or `None`

.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


###

`sinks(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.sinks)

The per-head sink tensor `module`

passes to the interface, or `None`

.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


###

`validate(module, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.AttentionFuser.validate)

Whether `module`

will actually dispatch to vLLM.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


##

`_is_interface_lookup(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention._is_interface_lookup)

Whether `node`

reads an entry out of `ALL_ATTENTION_FUNCTIONS`

.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


##

`_resolve(node, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention._resolve)

The value of `node`

on `module`

, for literals and `self.<attr>`

.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


##

`interface_call(forward)`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.attention.interface_call)

The attention interface call in `forward`

, if it makes exactly one.