source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/granitemoeshared/
lastmod: 2026-09-24

#

`vllm.model_executor.models.granitemoeshared`

[¶](https://docs.vllm.ai#vllm.model_executor.models.granitemoeshared)

Inference-only GraniteMoeShared model.

The architecture is the same as granitemoe but with the addition of shared experts.

Also serves the `granitemoe_swa`

checkpoints (`GraniteMoeSWAForCausalLM`

), which add the same per-layer sliding window, attention sink and per-layer RoPE support as `granite_swa`

(see `granite.py`

).