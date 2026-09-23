source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/common/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.pooler.common`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.common)

Classes:

##

`PoolingParamsUpdate`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.common.PoolingParamsUpdate)

Attributes:

-
([requires_token_ids](https://docs.vllm.ai#vllm.model_executor.layers.pooler.common.PoolingParamsUpdate.requires_token_ids)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Set this flag to enable CPU prompt token IDs for your pooler.


## Source code in `vllm/model_executor/layers/pooler/common.py`


###

`requires_token_ids = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.pooler.common.PoolingParamsUpdate.requires_token_ids)

Set this flag to enable CPU prompt token IDs for your pooler.