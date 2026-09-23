source: https://docs.vllm.ai/en/latest/api/vllm/config/lora/
lastmod: 2026-09-23

#

`vllm.config.lora`

[¶](https://docs.vllm.ai#vllm.config.lora)

Classes:

-
–[LoRAConfig](https://docs.vllm.ai#vllm.config.lora.LoRAConfig)Configuration for LoRA.


##

`LoRAConfig`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig)

Configuration for LoRA.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([default_mm_loras](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.default_mm_loras)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneDictionary mapping specific modalities to LoRA model paths; this field

-
([enable_mixed_moe_lora_format](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.enable_mixed_moe_lora_format)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, force the engine to use the universal 2D MoE LoRA wrapper

-
([enable_moe_shared_loras](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.enable_moe_shared_loras)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, load MoE expert adapters in the "shared-outer" layout, where the

-
([enable_tower_connector_lora](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.enable_tower_connector_lora)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, LoRA support for the tower (vision encoder) and connector -
([fully_sharded_loras](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.fully_sharded_loras)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)By default, only half of the LoRA computation is sharded with tensor

-
([lora_dtype](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.lora_dtype)

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| LoRADTypeData type for LoRA. If auto, will default to base model dtype.

-
([max_cpu_loras](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.max_cpu_loras)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of LoRAs to store in CPU memory. Must be >= than

-
([max_lora_rank](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.max_lora_rank)`MaxLoRARanks`

) –Max LoRA rank.

-
([max_loras](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.max_loras)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Max number of LoRAs in a single batch.

-
([specialize_active_lora](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.specialize_active_lora)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to construct lora kernel grid by the number of active LoRA adapters.

-
([target_modules](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.target_modules)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneRestrict LoRA to specific module suffixes (e.g., ["o_proj", "qkv_proj"]).


## Source code in `vllm/config/lora.py`


|
|

###

`default_mm_loras = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.default_mm_loras)

Dictionary mapping specific modalities to LoRA model paths; this field is only applicable to multimodal models and should be leveraged when a model always expects a LoRA to be active when a given modality is present. Note that currently, if a request provides multiple additional modalities, each of which have their own LoRA, we do NOT apply default_mm_loras because we currently only support one lora adapter per prompt. When run in offline mode, the lora IDs for n modalities will be automatically assigned to 1-n with the names of the modalities in alphabetic order.

###

`enable_mixed_moe_lora_format = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.enable_mixed_moe_lora_format)

If True, force the engine to use the universal 2D MoE LoRA wrapper (`FusedMoEWithLoRA`

) regardless of the model's `is_3d_moe_weight`

flag, so that 2D-format and 3D-format MoE LoRA adapters can be served in the same deployment. Only meaningful for MoE models; ignored otherwise. Default False keeps the existing model-driven behavior.

###

`enable_moe_shared_loras = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.enable_moe_shared_loras)

If True, load MoE expert adapters in the "shared-outer" layout, where the gate/up (`w1`

/`w3`

) lora_A and the down (`w2`

) lora_B are shared across all experts (stored once with expert-dim 1) instead of per-expert. The shared factors are broadcast to the expert count at kernel time. Only meaningful for MoE models whose adapters use this layout; ignored otherwise.

###

`enable_tower_connector_lora = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.enable_tower_connector_lora)

If `True`

, LoRA support for the tower (vision encoder) and connector of multimodal models will be enabled. This is an experimental feature and currently only supports some MM models such as the Qwen VL series. The default is False.

###

`fully_sharded_loras = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.fully_sharded_loras)

By default, only half of the LoRA computation is sharded with tensor parallelism. Enabling this will use the fully sharded layers. At high sequence length, max rank or tensor parallel size, this is likely faster.

###

`lora_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.lora_dtype)

Data type for LoRA. If auto, will default to base model dtype.

###

`max_cpu_loras = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.max_cpu_loras)

Maximum number of LoRAs to store in CPU memory. Must be >= than `max_loras`

.

###

`max_lora_rank = 16`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.max_lora_rank)

Max LoRA rank.

###

`max_loras = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.max_loras)

Max number of LoRAs in a single batch.

###

`specialize_active_lora = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.specialize_active_lora)

Whether to construct lora kernel grid by the number of active LoRA adapters. When set to True, separate cuda graphs will be captured for different counts of active LoRAs (powers of 2 up to max_loras), which can improve performance for variable LoRA usage patterns at the cost of increased startup time and memory usage. Only takes effect when cudagraph_specialize_lora is True.

###

`target_modules = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.target_modules)

Restrict LoRA to specific module suffixes (e.g., ["o_proj", "qkv_proj"]). If None, all supported LoRA modules are used. This allows deployment-time control over which modules have LoRA applied, useful for performance tuning.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.lora.LoRAConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.