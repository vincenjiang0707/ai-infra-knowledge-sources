source: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/utils/
lastmod: 2026-09-24

#

`vllm.lora.layers.utils`

[¶](https://docs.vllm.ai#vllm.lora.layers.utils)

##

`_fully_sharded_can_replace(can_replace)`

[¶](https://docs.vllm.ai#vllm.lora.layers.utils._fully_sharded_can_replace)

Decorator which adds the condition of fully sharded loras intended to wrap can_replace_layer()

## Source code in `vllm/lora/layers/utils.py`


##

`_get_lora_device(base_layer)`

[¶](https://docs.vllm.ai#vllm.lora.layers.utils._get_lora_device)

Returns the device for where to place the LoRA tensors.

## Source code in `vllm/lora/layers/utils.py`


##

`_not_fully_sharded_can_replace(can_replace)`

[¶](https://docs.vllm.ai#vllm.lora.layers.utils._not_fully_sharded_can_replace)

Decorator which adds the condition of not using fully sharded loras intended to wrap can_replace_layer()