source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/fusers/rms_norm/
lastmod: 2026-09-24

#

`vllm.model_executor.models.transformers.fusers.rms_norm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm)

RMSNorm fuser: detect the norm structurally and swap in vLLM's fused RMSNorm.

Classes:

-
–[RMSNormFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser)Fuser for RMSNorm patterns, including Gemma-style zero-centered weights.

-
–[TPAwareGemmaRMSNorm](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.TPAwareGemmaRMSNorm)`GemmaRMSNorm`

that reconstructs a TP-sharded input before normalizing. -
–[TPAwareNormMixin](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.TPAwareNormMixin)Mixin for RMSNorms that reconstructs a TP-sharded input before normalizing.

-
–[TPAwareRMSNorm](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.TPAwareRMSNorm)`RMSNorm`

that reconstructs a TP-sharded input before normalizing.

##

`RMSNormFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser)

Bases: [BaseFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.BaseFuser)

Fuser for RMSNorm patterns, including Gemma-style zero-centered weights.

Methods:

-
–[fuse](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.fuse)Fuse the matched RMSNorm pattern into a vLLM fused RMSNorm CustomOp.

-
–[match](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.match)Match a graph to the RMSNorm pattern, returning a fuser if found.


Attributes:

-
([eps](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.eps)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| None`eps`

itself, when it is not held in an attribute (see`_eps_source`

). -
([eps_attr](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.eps_attr)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneAttribute holding

`eps`

, read per instance in`fuse`

. -
([source_cls](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.source_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Class name of the norm this was matched from (for logging).

-
([zero_centered](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.zero_centered)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Gemma-style

`(1 + weight)`

scaling (weight initialised at zero).

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


|
|

###

`eps = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.eps)

`eps`

itself, when it is not held in an attribute (see `_eps_source`

).

###

`eps_attr = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.eps_attr)

Attribute holding `eps`

, read per instance in `fuse`

.

###

`source_cls`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.source_cls)

Class name of the norm this was matched from (for logging).

###

`zero_centered`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.zero_centered)

Gemma-style `(1 + weight)`

scaling (weight initialised at zero).

###

`_eps_from_graph(graph)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser._eps_from_graph)

Extract the `eps`

constant from the graph, if present.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


###

`_eps_source(graph, module)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser._eps_source)

Where `fuse`

should read `eps`

from, resolved once per class.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


###

`fuse(module, prefix, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.fuse)

Fuse the matched RMSNorm pattern into a vLLM fused RMSNorm CustomOp.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


###

`match(graph, module)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.RMSNormFuser.match)

Match a graph to the RMSNorm pattern, returning a fuser if found.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`TPAwareGemmaRMSNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.TPAwareGemmaRMSNorm)

Bases:

, [TPAwareNormMixin](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.TPAwareNormMixin)`GemmaRMSNorm`


`GemmaRMSNorm`

that reconstructs a TP-sharded input before normalizing.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`TPAwareNormMixin`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.TPAwareNormMixin)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Mixin for RMSNorms that reconstructs a TP-sharded input before normalizing.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`TPAwareRMSNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.TPAwareRMSNorm)

Bases:

, [TPAwareNormMixin](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm.TPAwareNormMixin)`RMSNorm`


`RMSNorm`

that reconstructs a TP-sharded input before normalizing.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`_has_trailing_compute(graph, node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm._has_trailing_compute)

Does the forward compute anything after `node`

before returning?

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`_is_inverse_sqrt(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm._is_inverse_sqrt)

Detect `rsqrt(v)`

, or the `pow(v, -0.5)`

/ `v ** -0.5`

spelling of it.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`_is_one_plus(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm._is_one_plus)

`1 + weight`

in either operand order (marks a zero-centered weight).

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`_is_squared(node, x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm._is_squared)

`x**2`

, `x.square()`

or `x * x`

, through any dtype casts.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`_operand(node, index, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm._operand)

Operand `index`

of `node`

, whether it was passed positionally or as `name`

.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`_variance_eps(rsqrt, x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.rms_norm._variance_eps)

`eps`

from `rsqrt(mean(x**2, -1) + eps)`

, or `None`

if not that shape.