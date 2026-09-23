source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/layers/
lastmod: 2026-09-23

#

`vllm.model_executor.models.transformers.layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.layers)

Layer provider resolution for the Transformers modeling backend.

When `VLLM_USE_HW_AGNOSTIC`

is set, layer symbols are imported from `vllm.model_executor.hw_agnostic.layers.<module>`

, falling back to `vllm.model_executor.layers.<module>`

for anything not yet ported. The resolved source of every symbol is logged so it is clear which layers run hw-agnostic and which fell back to vLLM.

Functions:

-
–[get_act_and_mul_fn](https://docs.vllm.ai#vllm.model_executor.models.transformers.layers.get_act_and_mul_fn)Fused activation-and-mul op for

`act_fn_name`

, preferring hw-agnostic.

##

`_resolve(module, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.layers._resolve)

Return `name`

from the hw-agnostic `module`

when enabled and available, else from vLLM. Logs which source was used.

## Source code in `vllm/model_executor/models/transformers/layers.py`


##

`get_act_and_mul_fn(act_fn_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.layers.get_act_and_mul_fn)

Fused activation-and-mul op for `act_fn_name`

, preferring hw-agnostic.

Resolved per call because the op is name-parameterized: an activation with no hw-agnostic equivalent falls back to vLLM individually.