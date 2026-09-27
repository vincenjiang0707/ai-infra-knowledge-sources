source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fusion/mm_input_norm/
lastmod: 2026-09-27

#

`vllm.model_executor.layers.fusion.mm_input_norm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm)

Fused Normalisation on the Device.

Equivalent to::

```
output = (input * rescale_factor - image_mean) / image_std
```


This is implemented as a single per-channel affine transform::

```
output = input * weight[c] + bias[c]
```


where::

```
weight = rescale_factor / image_std
bias = -image_mean / image_std
```


Classes:

-
–[FusedMMInputNorm](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm)Module that applies rescaling and normalisation to input images.

-
–[IdentityInputNorm](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.IdentityInputNorm)Stand-in used when the processor requires no rescale/normalise.

-
–[NormParams](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.NormParams)Resolved per-channel affine parameters (flags already folded in).


Functions:

-
–[build_mm_input_norm](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.build_mm_input_norm)Build the input normalisation module for a model.

-
–[fused_mm_input_norm_triton](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.fused_mm_input_norm_triton)Fused per-channel affine transform for normalisation.


##

`FusedMMInputNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Module that applies rescaling and normalisation to input images. Equivalent to: output = (input * rescale_factor - mean) / std

Dtype semantics:

- Input dtype — the dtype of the
`pixel_values`

argument to`forward_*`

. It is`uint8`

when`mm_device_do_normalize`

is enabled (raw bytes travel to the device unprocessed) and equals`visual_dtype`

otherwise. - Output dtype — the
`visual_dtype`

argument of`forward_*`

. The computation itself is always fp32, independent of the output dtype (e.g. compute fp32, emit bf16).

Platform dispatch:

`forward_native`

— pure PyTorch eager path, used as the semantic reference and default fallback on all platforms.`forward_cuda`

— Triton kernel path for CUDA devices.`forward_xpu`

— custom XPU kernel path.`forward_oot`

— out-of-tree platform override entry point; falls back to`forward_native`

unless a plugin overrides it.

Methods:

-
–[forward_cuda](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm.forward_cuda)Triton kernel path for CUDA devices.

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm.forward_native)Pure PyTorch eager implementation.

-
–[forward_oot](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm.forward_oot)Out-of-tree platform override entrypoint.

-
–[forward_xpu](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm.forward_xpu)XPU fused custom kernel path.


## Source code in `vllm/model_executor/layers/fusion/mm_input_norm.py`


|
|

###

`forward_cuda(pixel_values, visual_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm.forward_cuda)

Triton kernel path for CUDA devices.

## Source code in `vllm/model_executor/layers/fusion/mm_input_norm.py`


###

`forward_native(pixel_values, visual_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm.forward_native)

Pure PyTorch eager implementation.

This is the semantic reference implementation and the fallback used on any platform without a specialised kernel.

## Source code in `vllm/model_executor/layers/fusion/mm_input_norm.py`


###

`forward_oot(pixel_values, visual_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm.forward_oot)

Out-of-tree platform override entrypoint.

###

`forward_xpu(pixel_values, visual_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.FusedMMInputNorm.forward_xpu)

XPU fused custom kernel path.

On XPU, fuse the whole rescale + normalise into a single custom kernel. The eager path materializes an fp32 intermediate and then casts back, which adds device-side compute that cancels the bandwidth saving of transferring uint8 pixel_values. The fused kernel reads uint8 directly and writes `visual_dtype`

in one pass.

## Source code in `vllm/model_executor/layers/fusion/mm_input_norm.py`


##

`IdentityInputNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.IdentityInputNorm)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Stand-in used when the processor requires no rescale/normalise.

Not a no-op: with `mm_device_do_normalize`

enabled, raw `uint8`

pixels travel to the device unprocessed and must be cast to `visual_dtype`

here.

## Source code in `vllm/model_executor/layers/fusion/mm_input_norm.py`


##

`NormParams`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.NormParams)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Resolved per-channel affine parameters (flags already folded in).

Attributes:

-
([is_identity](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.NormParams.is_identity)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether

`weight = rescale/std`

and`bias = -mean/std`

are

## Source code in `vllm/model_executor/layers/fusion/mm_input_norm.py`


###

`is_identity`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.NormParams.is_identity)

Whether `weight = rescale/std`

and `bias = -mean/std`

are numerically the identity transform (mirrors `torch.allclose`

's default fp32 tolerances).

##

`_load_norm_params(model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm._load_norm_params)

Resolve the per-channel affine parameters `(image_mean, image_std, rescale_factor)`

from the processor config, falling back to the image processor object.

## Source code in `vllm/model_executor/layers/fusion/mm_input_norm.py`


##

`build_mm_input_norm(model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.build_mm_input_norm)

Build the input normalisation module for a model.

Returns an `IdentityInputNorm`

when device-side normalisation is disabled or the processor's rescale/normalise is numerically the identity transform; otherwise a `FusedMMInputNorm`

built from the processor's parameters.

## Source code in `vllm/model_executor/layers/fusion/mm_input_norm.py`


##

`fused_mm_input_norm_triton(inputs, outputs, weight, bias)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.fused_mm_input_norm_triton)

Fused per-channel affine transform for normalisation.

Parameters:

-

(`inputs`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.fused_mm_input_norm_triton(inputs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor, shape

`(N, C, L)`

. A contiguous copy is materialized internally if needed. -

(`outputs`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.fused_mm_input_norm_triton(outputs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor, contiguous and shaped exactly

`(N, C, L)`

. -

(`weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.fused_mm_input_norm_triton(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Per-channel scale, shape

`(C,)`

. -

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.mm_input_norm.fused_mm_input_norm_triton(bias))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Per-channel shift, shape

`(C,)`

.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`outputs`

, for chaining.