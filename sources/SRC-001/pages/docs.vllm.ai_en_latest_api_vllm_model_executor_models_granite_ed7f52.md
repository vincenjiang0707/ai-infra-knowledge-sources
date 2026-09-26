source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/granite/
lastmod: 2026-09-24

#

`vllm.model_executor.models.granite`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite)

Inference-only IBM Granite model compatible with HuggingFace weights.

Also serves the `granite_swa`

checkpoints (`GraniteSWAForCausalLM`

), supporting three additional features: per-layer sliding window attention (`layer_types`

), a learnable per-head attention sink (`self_attn.sinks`

), and a per-layer RoPE base (`layer_rope_theta`

, with 0 for NoPE).

Functions:

-
–[granite_layer_attn_params](https://docs.vllm.ai#vllm.model_executor.models.granite.granite_layer_attn_params)Resolve one layer's sliding window, RoPE base and sink usage.


##

`granite_layer_attn_params(config, layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granite.granite_layer_attn_params)

Resolve one layer's sliding window, RoPE base and sink usage.

Plain Granite configs carry no SWA fields and fall back to full attention, global RoPE base and no sink. HF SWA checkpoints use sinks without a dedicated flag, so assume true when `layer_types`

is used, and allow `attention_sinks`

to override that decision.

Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)| NoneSliding window size (

`None`

for full attention), RoPE base theta (`0`

-

–[float](https://docs.python.org/3/builtins/functions.html#float)for NoPE), and attention sink presence/absence.