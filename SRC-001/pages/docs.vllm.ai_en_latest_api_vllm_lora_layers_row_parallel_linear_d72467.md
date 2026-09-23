source: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/row_parallel_linear/
lastmod: 2026-09-23

#

`vllm.lora.layers.row_parallel_linear`

[¶](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear)

Classes:

-
–[RowParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithLoRA) -
–[RowParallelLinearWithShardedLoRA](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithShardedLoRA)Differs from RowParallelLinearWithLoRA by slicing the


##

`RowParallelLinearWithLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithLoRA)

Bases: [BaseLinearLayerWithLoRA](https://docs.vllm.ai/base_linear/#vllm.lora.layers.base_linear.BaseLinearLayerWithLoRA)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithLoRA.forward)Forward of RowParallelLinear.


## Source code in `vllm/lora/layers/row_parallel_linear.py`


###

`forward(input_)`

[¶](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithLoRA.forward)

Forward of RowParallelLinear.

Parameters:

-

(`input_`

[¶](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithLoRA.forward(input_))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor whose last dimension is

`input_size`

. If`input_is_parallel`

is set, then the last dimension is`input_size // tp_size`

.

Returns:

## Source code in `vllm/lora/layers/row_parallel_linear.py`


##

`RowParallelLinearWithShardedLoRA`

[¶](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithShardedLoRA)

Bases: [RowParallelLinearWithLoRA](https://docs.vllm.ai#vllm.lora.layers.row_parallel_linear.RowParallelLinearWithLoRA)

Differs from RowParallelLinearWithLoRA by slicing the LoRA B's also.

Based on S-LoRA, slicing happens along the output dim. This yields a combined partial sum from the row parallel base layer and column partitioned output from the LoRA.

## Source code in `vllm/lora/layers/row_parallel_linear.py`


|
|