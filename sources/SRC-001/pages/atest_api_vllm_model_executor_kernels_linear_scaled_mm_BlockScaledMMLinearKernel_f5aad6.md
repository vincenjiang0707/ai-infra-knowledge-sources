source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/BlockScaledMMLinearKernel/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel)

Classes:

-
–[FP8BlockParams](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.FP8BlockParams) -
–[Fp8BlockScaledDynamicMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.Fp8BlockScaledDynamicMMLinearKernel)Dynamic FP8 block-scaled kernel that dispatches at runtime.


##

`FP8BlockParams`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.FP8BlockParams)

Bases: [FP8Params](https://docs.vllm.ai/base/#vllm.model_executor.kernels.linear.base.FP8Params)

Attributes:

-
([block_scale_attr](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.FP8BlockParams.block_scale_attr)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Fp8LinearMethod registers the block scale as

`weight_scale_inv`

,

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/BlockScaledMMLinearKernel.py`


###

`block_scale_attr`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.FP8BlockParams.block_scale_attr)

Fp8LinearMethod registers the block scale as `weight_scale_inv`

, compressed-tensors as `weight_scale`

.

##

`Fp8BlockScaledDynamicMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.Fp8BlockScaledDynamicMMLinearKernel)

Bases: `Fp8BlockScaledMMLinearKernel`

, [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Dynamic FP8 block-scaled kernel that dispatches at runtime.

Extends Fp8BlockScaledMMLinearKernel to inherit apply_weights and overrides apply_block_scaled_mm to dispatch between two sub-kernels using torch.cond.

## Subclasses must define

base_type: The primary kernel class. fallback_type: The fallback kernel class.