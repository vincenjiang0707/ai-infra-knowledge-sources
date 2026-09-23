source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/fuser/
lastmod: 2026-09-23

#

`vllm.model_executor.models.transformers.fuser`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser)

Fuser detection for the Transformers modeling backend.

Classes:

-
–[Fusers](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.Fusers)Mapping from module class and shape to fusers, for all fusable modules.


Functions:

-
–[get_fuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.get_fuser)The first

`fuser_cls`

that applies to`module`

, if one does. -
–[get_fusers](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.get_fusers)Every fuser that could apply to

`module`

's class (cached), in`FUSERS`

order. -
–[key](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.key)Cache key for

`get_fusers`

. Considers module type and its immediate children.

Attributes:

-
([FUSERS](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.FUSERS)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[type](https://docs.python.org/3/builtins/functions.html#type)[[BaseFuser](https://docs.vllm.ai/fusers/#vllm.model_executor.models.transformers.fusers.BaseFuser)], ...]Every fuser, in priority order: those that redefine the forward first, then those


##

`FUSERS = (MLAFuser, GLUFuser, QKVFuser, PackedQKVFuser, MergedColumnParallelFuser, RMSNormFuser, AttentionFuser)`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.FUSERS)

Every fuser, in priority order: those that redefine the forward first, then those that leave it alone. A new fuser is added here.

##

`Fusers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.Fusers)

Bases: [UserDict](https://docs.python.org/3/library/collections.html#collections.UserDict)

Mapping from module class and shape to fusers, for all fusable modules.

Methods:

-
–[__getitem__](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.Fusers.__getitem__)The fusers this instance can take, in the order to apply them.


## Source code in `vllm/model_executor/models/transformers/fuser.py`


###

`__getitem__(m)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.Fusers.__getitem__)

The fusers this instance can take, in the order to apply them.

## Source code in `vllm/model_executor/models/transformers/fuser.py`


##

`get_fuser(module, fuser_cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.get_fuser)

The first `fuser_cls`

that applies to `module`

, if one does.

##

`get_fusers(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.get_fusers)

Every fuser that could apply to `module`

's class (cached), in `FUSERS`

order.

## Source code in `vllm/model_executor/models/transformers/fuser.py`


##

`key(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fuser.key)

Cache key for `get_fusers`

. Considers module type and its immediate children.