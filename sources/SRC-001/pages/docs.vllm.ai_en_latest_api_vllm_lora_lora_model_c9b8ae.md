source: https://docs.vllm.ai/en/latest/api/vllm/lora/lora_model/
lastmod: 2026-09-24

#

`vllm.lora.lora_model`

[¶](https://docs.vllm.ai#vllm.lora.lora_model)

Classes:

-
–[LoRAModel](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel)A LoRA fine-tuned model.

-
–[MoEEPLoadSpec](https://docs.vllm.ai#vllm.lora.lora_model.MoEEPLoadSpec)Per-expert-parallel slicing metadata for one FusedMoEFactory LoRA module.


##

`LoRAModel`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel)

A LoRA fine-tuned model.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.__init__)Args:

-
–[clone](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.clone)Return a copy of the object with different ids.

-
–[from_local_checkpoint](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint)Create a LoRAModel from a local checkpoint.

-
–[from_lora_tensors](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_lora_tensors)Create a LoRAModel from a dictionary of tensors.

-
–[get_lora](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.get_lora)Get LoRA for a given module by name.


## Source code in `vllm/lora/lora_model.py`


|
|

###

`__init__(lora_model_id, rank, loras, is_3d_lora_weight=False, *, modules_to_save=None)`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.__init__)

Args: lora_model_id: The integer id for the lora model. rank: lora rank. loras: module name -> weights for lora-replaced layers. is_3d_lora_weight: Whether the on-disk MoE adapter is in the 3D fused (gate_up_proj / down_proj) layout. Propagated from the originating LoRARequest. Only consulted by the LoRA model manager when enable_mixed_moe_lora_format is on.

## Source code in `vllm/lora/lora_model.py`


###

`_should_skip_module(module_name, skip_prefixes)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel._should_skip_module)

Check if a module should be skipped based on skip prefixes.

## Source code in `vllm/lora/lora_model.py`


###

`clone(lora_model_id)`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.clone)

Return a copy of the object with different ids.

Will share the underlying tensors.

## Source code in `vllm/lora/lora_model.py`


###

`from_local_checkpoint(lora_dir, expected_lora_modules, peft_helper, *, lora_model_id=None, device='cuda', dtype=None, model_vocab_size=None, weights_mapper=None, tensorizer_config_dict=None, skip_prefixes=None, moe_ep_spec=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint)

Create a LoRAModel from a local checkpoint.

Parameters:

-

(`lora_dir`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(lora_dir))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The local path that has lora data.

-

(`expected_lora_modules`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(expected_lora_modules))

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Name of modules that are expected to be replaced by lora.

-

(`peft_helper`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(peft_helper))

) –[PEFTHelper](https://docs.vllm.ai/peft_helper/#vllm.lora.peft_helper.PEFTHelper)Loaded lora configuration information.

-

(`lora_model_id`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(lora_model_id))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –LoRA model id. If not given, automatically set by a global counter.

-

(`device`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(device))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'cuda'`

) –Device where the lora model is loaded.

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –dtype of the lora model weights.

-

(`model_vocab_size`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(model_vocab_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Vocab size of the base model, used to size the embedding deltas.

-

(`weights_mapper`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(weights_mapper))

, default:[WeightsMapper](https://docs.vllm.ai/model_executor/models/utils/#vllm.model_executor.models.utils.WeightsMapper)| None`None`

) –Optional mapper rewriting checkpoint weight names to vLLM names.

-

(`tensorizer_config_dict`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(tensorizer_config_dict))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)| None`None`

) –Optional tensorizer config used to load the checkpoint via tensorizer instead of from disk.

-

(`skip_prefixes`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(skip_prefixes))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –List of module name prefixes to skip during loading. Models can define this to skip modules not used in inference (e.g., MTP layers). Format: ["mtp."]

-

(`moe_ep_spec`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_local_checkpoint(moe_ep_spec))

, default:[MoEEPLoadSpec](https://docs.vllm.ai#vllm.lora.lora_model.MoEEPLoadSpec)| None`None`

) –When 2D FusedMoEFactory LoRA modules are present with expert parallelism enabled, the (ep_rank, local, global) slicing metadata shared across all MoE layers. Non-local expert weights are skipped at read time instead of being loaded and discarded later.


Returns:

-

–[LoRAModel](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel)Loaded LoRA Model.


## Source code in `vllm/lora/lora_model.py`


|
|

###

`from_lora_tensors(lora_model_id, tensors, peft_helper, device='cuda', dtype=None, model_vocab_size=None, weights_mapper=None, skip_prefixes=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.LoRAModel.from_lora_tensors)

Create a LoRAModel from a dictionary of tensors.

## Source code in `vllm/lora/lora_model.py`


##

`MoEEPLoadSpec`

`dataclass`

[¶](https://docs.vllm.ai#vllm.lora.lora_model.MoEEPLoadSpec)

Per-expert-parallel slicing metadata for one FusedMoEFactory LoRA module.

Threaded into the LoRA loader so per-expert weights from EP ranks other than this one can be skipped before they ever hit CPU memory.

## Source code in `vllm/lora/lora_model.py`


##

`_is_remote_expert_key(raw_name, spec)`

[¶](https://docs.vllm.ai#vllm.lora.lora_model._is_remote_expert_key)

Decide whether a checkpoint key belongs to a non-local expert.