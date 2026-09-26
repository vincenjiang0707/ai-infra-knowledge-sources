source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/moe/
lastmod: 2026-09-24

#

`vllm.models.inkling.amd.moe`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe)

Inkling mixture-of-experts on vLLM's MoERunner abstraction.

Overfit to the served checkpoint: sigmoid gate (+ selection bias) top-k over the routed experts, log-sigmoid renormalization over the k routed + S shared "sink" logits, scaled by route_scale * global_scale. The routed top-k goes through vLLM's MoERunner (which handles TP/EP); the sink experts run in :class:`InklingSinkExperts`

-- replicated across EP ranks (every token activates every sink) and always bf16 (the checkpoint excludes every `shared_experts`

from quantization).

MXFP4 routed experts reuse vLLM's Quark OCP MXFP4 fused-MoE method; excluded (bf16) layers fall back to the unquantized method. The checkpoint's fused stacked tensors (interleaved gate/up rows, `.scale`

/ `.scale2`

/ `.input_amax`

aux tensors) are translated to the standard per-expert loads in :meth:`InklingMoE.load_expert_weight`

.

Classes:

-
–[InklingGate](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingGate)Sigmoid gate with selection bias, log-sigmoid renorm after top-k, and

-
–[InklingMoE](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingMoE) -
–[InklingSinkExperts](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingSinkExperts)Shared "sink" experts with per-token gammas, in bf16.

-
–[InklingSinkExpertsLinear](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingSinkExpertsLinear)LoRA-capable implementation of the Inkling sink experts.


Functions:

-
–[inkling_gate_select](https://docs.vllm.ai#vllm.models.inkling.amd.moe.inkling_gate_select)Sigmoid + bias + top-k + log-sigmoid renorm; returns (weights, ids).


##

`InklingGate`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingGate)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Sigmoid gate with selection bias, log-sigmoid renorm after top-k, and global scale (the served checkpoint's only configuration).

Methods:

-
–[compute_logits](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingGate.compute_logits)fp32 gate logits [T, n_total_experts + pad] (pad columns are junk).

-
–[select_experts](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingGate.select_experts)Full selection: (weights, ids) of [T, K + S]. The first K entries


## Source code in `vllm/models/inkling/amd/moe.py`


###

`compute_logits(x)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingGate.compute_logits)

fp32 gate logits [T, n_total_experts + pad] (pad columns are junk).

###

`select_experts(gating_output)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingGate.select_experts)

Full selection: (weights, ids) of [T, K + S]. The first K entries are the routed top-k; the S trailing entries are the sink gammas.

## Source code in `vllm/models/inkling/amd/moe.py`


##

`InklingMoE`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingMoE)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[finalize_load](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingMoE.finalize_load)Post-load fixups for zeroed padding experts.

-
–[load_expert_weight](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingMoE.load_expert_weight)Load one checkpoint expert tensor.


## Source code in `vllm/models/inkling/amd/moe.py`


|
|

###

`_local_expert_slots()`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingMoE._local_expert_slots)

Global expert id -> local slot for this rank's expert partition.

## Source code in `vllm/models/inkling/amd/moe.py`


###

`_select_routed(hidden_states, gating_output, topk, renormalize)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingMoE._select_routed)

MoERunner `custom_routing_function`

: the routed top-k slice of the full (routed + sink) selection.

forward() stashes its selection (keyed by logits identity) so the gate select runs once per layer; the fallback covers paths where the runner re-derives the logits (e.g. naive DP dispatch).

## Source code in `vllm/models/inkling/amd/moe.py`


###

`finalize_load()`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingMoE.finalize_load)

Post-load fixups for zeroed padding experts.

## Source code in `vllm/models/inkling/amd/moe.py`


###

`load_expert_weight(name, weight)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingMoE.load_expert_weight)

Load one checkpoint expert tensor.

`name`

is relative to the mlp module: `experts.<t>`

(routed stack) or `shared_experts.shared_<t>`

(sink experts). Returns the loaded param names (relative to this module).

## Source code in `vllm/models/inkling/amd/moe.py`


|
|

##

`InklingSinkExperts`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingSinkExperts)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Shared "sink" experts with per-token gammas, in bf16.

Replicated across EP ranks (every token activates every sink, so EP-sharding them would hotspot the owning rank) and TP-sharded on the intermediate dim so the output remains a TP-partial sum like the routed output. The sinks are always bf16 (the checkpoint excludes every `shared_experts`

from quantization): the experts concatenate into two plain dense GEMMs with the fused sink epilogue between them.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingSinkExperts.forward)`sum_e gammas[:, e] * MLP_e(x)`

(TP-partial along d_mlp). -
–[load_weight](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingSinkExperts.load_weight)Load one checkpoint sink tensor (stacked over the S experts).


## Source code in `vllm/models/inkling/amd/moe.py`


###

`forward(x, gammas)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingSinkExperts.forward)

`sum_e gammas[:, e] * MLP_e(x)`

(TP-partial along d_mlp).

## Source code in `vllm/models/inkling/amd/moe.py`


###

`load_weight(key, weight)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingSinkExperts.load_weight)

Load one checkpoint sink tensor (stacked over the S experts).

## Source code in `vllm/models/inkling/amd/moe.py`


##

`InklingSinkExpertsLinear`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.InklingSinkExpertsLinear)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

LoRA-capable implementation of the Inkling sink experts.

## Source code in `vllm/models/inkling/amd/moe.py`


##

`_inkling_moe_ep_size()`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe._inkling_moe_ep_size)

EP size the MoERunner layer will run with (mirrors FusedMoEParallelConfig.make: experts shard over tp * dp * pcp when expert parallelism is enabled).

## Source code in `vllm/models/inkling/amd/moe.py`


##

`inkling_gate_select(logits, n_gate_experts, n_routed_experts, topk, n_shared_experts, bias, route_scale, global_scale)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.moe.inkling_gate_select)

Sigmoid + bias + top-k + log-sigmoid renorm; returns (weights, ids).