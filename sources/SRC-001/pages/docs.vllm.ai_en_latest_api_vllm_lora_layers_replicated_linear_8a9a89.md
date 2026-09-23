source: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/replicated_linear/
lastmod: 2026-09-23

#

`vllm.lora.layers.replicated_linear`

[¶](https://docs.vllm.ai#vllm.lora.layers.replicated_linear)

Classes:

##

`ReplicatedLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA)

Bases: [BaseLinearLayerWithLoRA](https://docs.vllm.ai/base_linear/#vllm.lora.layers.base_linear.BaseLinearLayerWithLoRA)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.forward)Forward of ReplicatedLinearWithLoRA.

-
–[slice_lora_a](https://docs.vllm.ai#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.slice_lora_a)Slice lora a if splitting for tensor parallelism.

-
–[slice_lora_b](https://docs.vllm.ai#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.slice_lora_b)Slice lora b if splitting with tensor parallelism.


## Source code in `vllm/lora/layers/replicated_linear.py`


###

`forward(input_)`

[¶](https://docs.vllm.ai#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.forward)

Forward of ReplicatedLinearWithLoRA.

Parameters:

Returns:

## Source code in `vllm/lora/layers/replicated_linear.py`


###

`slice_lora_a(lora_a)`

[¶](https://docs.vllm.ai#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.slice_lora_a)

Slice lora a if splitting for tensor parallelism.

###

`slice_lora_b(lora_b)`

[¶](https://docs.vllm.ai#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.slice_lora_b)

Slice lora b if splitting with tensor parallelism.