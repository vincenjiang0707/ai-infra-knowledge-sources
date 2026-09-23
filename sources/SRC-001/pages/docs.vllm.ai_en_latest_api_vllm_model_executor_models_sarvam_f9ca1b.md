source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/sarvam/
lastmod: 2026-09-23

#

`vllm.model_executor.models.sarvam`

[¶](https://docs.vllm.ai#vllm.model_executor.models.sarvam)

Classes:

-
–[SarvamMLAForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAForCausalLM) -
–[SarvamMLAModel](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAModel)Sarvam MLA backbone with stage-local EAGLE3 auxiliary capture.

-
–[SarvamMoEForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMoEForCausalLM)Same as BailingMoeForCausalLM, but normalizes gate expert_bias pre-load.


##

`SarvamMLAForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

, [SupportsEagle3](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle3)`SarvamMixtureOfExperts`


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAForCausalLM.forward)Return backbone outputs, including auxiliary states when captured.


## Source code in `vllm/model_executor/models/sarvam.py`


|
|

###

`_remap_config(config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAForCausalLM._remap_config)

Default the routing keys the released checkpoints omit.

## Source code in `vllm/model_executor/models/sarvam.py`


###

`forward(input_ids, positions, intermediate_tensors=None, inputs_embeds=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAForCausalLM.forward)

Return backbone outputs, including auxiliary states when captured.

## Source code in `vllm/model_executor/models/sarvam.py`


##

`SarvamMLAModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAModel)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)`EagleModelMixin`


Sarvam MLA backbone with stage-local EAGLE3 auxiliary capture.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAModel.forward)Run this stage and optionally return its auxiliary hidden states.


## Source code in `vllm/model_executor/models/sarvam.py`


|
|

###

`forward(input_ids, positions, intermediate_tensors, inputs_embeds=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMLAModel.forward)

Run this stage and optionally return its auxiliary hidden states.

Auxiliary captures are local to this stage, matching Qwen3 MoE. Pipeline transport carries only hidden states and residual; EAGLE3 capture across pipeline stages is not supported by this model.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors)|[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Intermediate tensors on non-final stages. On the final stage,

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors)|[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]normalized hidden states, paired with auxiliary states if captured.


## Source code in `vllm/model_executor/models/sarvam.py`


##

`SarvamMoEForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.sarvam.SarvamMoEForCausalLM)

Bases: `BailingMoeForCausalLM`


Same as BailingMoeForCausalLM, but normalizes gate expert_bias pre-load.