source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/hrm_text/
lastmod: 2026-09-23

#

`vllm.model_executor.models.hrm_text`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hrm_text)

HRM-Text: Hierarchical Reasoning Model — Text variant.

## Reference Hugging Face implementation

src/transformers/models/hrm_text/modeling_hrm_text.py

The model performs a hierarchical recurrent forward over two transformer stacks (`H`

slow, `L`

fast) inside nested loops. Each recurrence step gets its own KV cache slot via a unique vLLM-visible layer index. The PrefixLM attention pattern (prompt bidirectional, response causal) is realized by reusing `EncoderOnlyAttention`

(which sets `causal=False`

unconditionally on every metadata build) but with `attn_type=DECODER`

so the KV cache is allocated; see `HrmTextAttention`

for usage.

The on-disk `attn.gqkv_proj.weight`

(rows concatenated as `[gate | q | k | v]`

) is loaded by a single `MergedColumnParallelLinear`

with four equal-sized output partitions; its weight loader auto-splits the fused tensor along the output dim by `output_sizes`

(the same path used by Phi-3's fused gate_up_proj).

Classes:

-
–[HrmTextAttention](https://docs.vllm.ai#vllm.model_executor.models.hrm_text.HrmTextAttention)One self-attention block; weights shared across recurrence steps.

-
–[HrmTextForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.hrm_text.HrmTextForCausalLM)Hierarchical Reasoning Model — Text variant, causal LM.

-
–[HrmTextModel](https://docs.vllm.ai#vllm.model_executor.models.hrm_text.HrmTextModel)Hierarchical recurrent transformer body.

-
–[HrmTextStack](https://docs.vllm.ai#vllm.model_executor.models.hrm_text.HrmTextStack)A single transformer stack — used twice (H and L).


##

`HrmTextAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hrm_text.HrmTextAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

One self-attention block; weights shared across recurrence steps.

HF transformers writes a single fused `attn.gqkv_proj.weight`

on disk (per `transformers/conversion_mapping.py`

`"hrm_text"`

mapping; rows are concatenated as `[gate | q | k | v]`

along `dim=0`

). We mirror that on the model side with a single `MergedColumnParallelLinear`

whose four equal output partitions are sharded along the head axis under TP; its weight loader auto-splits the fused tensor (same path used by Phi-3's fused gate_up_proj). HF's runtime config currently hardcodes MHA (`num_key_value_groups=1`

); GQA would require `QKVParallelLinear`

semantics for q/k/v shard replication and is left for a follow-up if/when HF adds it.

## Holds

- parameters: gqkv_proj, o_proj, rotary_emb (shared across cycles).
`attn_per_step`

: a`nn.ModuleDict`

keyed by recurrence step (as a string), each value an`EncoderOnlyAttention`

(with`attn_type=DECODER`

so the KV cache is allocated; the`EncoderOnlyAttention`

wrapper sets`causal=False`

on every metadata build). The L stack steps are`[high_cycle_idx*(L_cycles+1)+low_cycle_idx]`

and the H stack steps are`[high_cycle_idx*(L_cycles+1)+L_cycles]`

; the two ranges are disjoint so each instance registers a unique vLLM`layer_name`

(`model.{H,L}_module.layers.{global_idx}.self_attn`

) and gets its own KV cache slot. The global layer index per recurrence step is`step * num_layers_per_stack + layer_idx_in_stack`

, matching the HF transformers`cycle_offset`

formula in`modeling_hrm_text.py`

.

## Source code in `vllm/model_executor/models/hrm_text.py`


|
|

##

`HrmTextForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hrm_text.HrmTextForCausalLM)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Hierarchical Reasoning Model — Text variant, causal LM.

Reference: src/transformers/models/hrm_text/modeling_hrm_text.py

## Source code in `vllm/model_executor/models/hrm_text.py`


##

`HrmTextModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hrm_text.HrmTextModel)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Hierarchical recurrent transformer body.

Forward (matches HF main exactly, src/transformers/models/hrm_text/modeling_hrm_text.py:495-547):

```
hidden_states_high_cycle = embed(input_ids) * embedding_scale
hidden_states_low_cycle = z_L_init.expand_as(hidden_states_high_cycle)
for high_cycle_idx in range(H_cycles):
for low_cycle_idx in range(L_cycles):
step = high_cycle_idx * (L_cycles + 1) + low_cycle_idx
hidden_states_low_cycle = L_module(
hidden_states_low_cycle + hidden_states_high_cycle,
current_step=step,
)
step = high_cycle_idx * (L_cycles + 1) + L_cycles
hidden_states_high_cycle = H_module(
hidden_states_high_cycle + hidden_states_low_cycle,
current_step=step,
)
return hidden_states_high_cycle
```


## Source code in `vllm/model_executor/models/hrm_text.py`


|
|

##

`HrmTextStack`

[¶](https://docs.vllm.ai#vllm.model_executor.models.hrm_text.HrmTextStack)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

A single transformer stack — used twice (H and L).