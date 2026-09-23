source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/layernorm/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.layernorm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm)

Custom normalization layers.

Classes:

-
–[GemmaRMSNorm](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.GemmaRMSNorm)RMS normalization for Gemma.

-
–[LayerNorm](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.LayerNorm)Layer Normalization.

-
–[RMSNorm](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNorm)Root mean square normalization.

-
–[RMSNormGated](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated)RMS Normalization with optional gating.


##

`GemmaRMSNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.GemmaRMSNorm)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

RMS normalization for Gemma.

## Two differences from the above RMSNorm

- x * (1 + w) instead of x * w.
- (x * w).to(orig_dtype) instead of x.to(orig_dtype) * w.

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.GemmaRMSNorm.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/layernorm.py`


###

`forward_native(x, residual=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.GemmaRMSNorm.forward_native)

PyTorch-native implementation equivalent to forward().

## Source code in `vllm/model_executor/layers/layernorm.py`


##

`LayerNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.LayerNorm)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Layer Normalization.

## Source code in `vllm/model_executor/layers/layernorm.py`


##

`RMSNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNorm)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Root mean square normalization.

Computes x -> w * x / sqrt(E[x^2] + eps) where w is the learned weight. Refer to https://arxiv.org/abs/1910.07467

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNorm.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/layernorm.py`


|
|

###

`forward_native(x, residual=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNorm.forward_native)

PyTorch-native implementation equivalent to forward().

## Source code in `vllm/model_executor/layers/layernorm.py`


##

`RMSNormGated`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

RMS Normalization with optional gating.

This is a native PyTorch implementation that supports: - Standard RMS normalization - Group RMS normalization - Optional gating with SiLU activation

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__)Initialize RMSNormGated.

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.forward_native)PyTorch-native implementation equivalent to forward().

-
–[forward_static](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.forward_static)Pure-PyTorch RMS normalization with optional gating.


## Source code in `vllm/model_executor/layers/layernorm.py`


|
|

###

`__init__(hidden_size, eps=1e-05, group_size=None, norm_before_gate=False, device=None, dtype=None, activation='swish')`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__)

Initialize RMSNormGated.

Parameters:

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the hidden dimension

-

(`eps`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__(eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-05`

) –Epsilon for numerical stability

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__(group_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –If not None, do GroupNorm with each group having group_size elements. group_size=None is equivalent to group_size=hidden_size (i.e. there's only 1 group).

-

(`norm_before_gate`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__(norm_before_gate))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True and z is provided: out = norm(x) * silu(z) If False and z is provided: out = norm(x * silu(z))

-

(`device`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__(device))

, default:[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)| None`None`

) –Device to create parameters on

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__(dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for parameters

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.__init__(activation))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'swish'`

) –Activation function name for gating


## Source code in `vllm/model_executor/layers/layernorm.py`


###

`forward_native(x, z=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.forward_native)

PyTorch-native implementation equivalent to forward().

## Source code in `vllm/model_executor/layers/layernorm.py`


###

`forward_static(x, z, weight, epsilon, orig_dtype, group_size=None, norm_before_gate=True, activation='swish')`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.layernorm.RMSNormGated.forward_static)

Pure-PyTorch RMS normalization with optional gating.

This static method contains the full native logic so that both `forward_native`

and `MatcherRMSNormGated`

(used by the compilation pattern matcher) can share the same implementation.

If *z* is not None and *norm_before_gate* is True: `out = rms_norm(x) * act(z)`

If *z* is not None and *norm_before_gate* is False: `out = rms_norm(x * act(z))`