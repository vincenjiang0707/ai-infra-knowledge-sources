source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fusion/fused_act_quant/
lastmod: 2026-09-23

Producer side of the QuantizedActivation contract for activation layers.

Given an activation module and the downstream linear it feeds, fuse the activation with that linear's input quantization into a single kernel when the linear advertises a consumable input quantization key (see quant_activation.py). Falls back to the plain activation when nothing matches, so a model forward can always call maybe_fused_act_quant unconditionally.

This is the manual-fusion counterpart to ActivationQuantFusionPass: when fusion fires here, the activation and quantization are already consumed, so a compiler pass cannot fuse the same boundary again.

Functions:

##

`_relu_squared_static_fp8_quant_supported(act_fn, x, linear)`


Return whether the ReLU2 static-FP8 producer can consume this input.

## Source code in `vllm/model_executor/layers/fusion/fused_act_quant.py`


| def _relu_squared_static_fp8_quant_supported(
act_fn: torch.nn.Module,
x: torch.Tensor,
linear: LinearBase,
) -> bool:
"""Return whether the ReLU2 static-FP8 producer can consume this input."""
scale = getattr(linear, "input_scale", None)
return (
isinstance(act_fn, ReLUSquaredActivation)
and x.is_cuda
and x.dtype == torch.bfloat16
and x.is_contiguous()
and isinstance(scale, torch.Tensor)
and scale.dtype == torch.float32
and scale.device == x.device
and scale.numel() == 1
)
|

##

`_silu_and_mul_fp8_dynamic_128(x, linear)`


SiluAndMul + FP8 dynamic per-group (group=128) quantization.

## Source code in `vllm/model_executor/layers/fusion/fused_act_quant.py`


| def _silu_and_mul_fp8_dynamic_128(
x: torch.Tensor, linear: LinearBase
) -> QuantizedActivation:
"""SiluAndMul + FP8 dynamic per-group (group=128) quantization."""
return _silu_and_mul_fp8_dynamic_block(x, linear, 128, kFp8Dynamic128Sym)
|

##

`_silu_and_mul_fp8_dynamic_block(x, linear, group_size, quant_key)`


SiluAndMul + FP8 dynamic per-block quantization.

## Source code in `vllm/model_executor/layers/fusion/fused_act_quant.py`


| def _silu_and_mul_fp8_dynamic_block(
x: torch.Tensor, linear: LinearBase, group_size: int, quant_key: QuantKey
) -> QuantizedActivation:
"""SiluAndMul + FP8 dynamic per-block quantization."""
assert x.ndim == 2, f"Input must be 2D [batch, hidden*2], got {x.shape}"
d = x.shape[-1] // 2
out_shape = x.shape[:-1] + (d,)
num_tokens = x.shape[0]
num_groups = d // group_size
result = torch.empty((num_tokens, d), dtype=FP8_DTYPE, device=x.device)
scales = torch.empty((num_tokens, num_groups), dtype=torch.float32, device=x.device)
torch.ops._C.silu_and_mul_per_block_quant(
out=result,
input=x,
scales=scales,
group_size=group_size,
scale_ub=None,
is_scale_transposed=False,
)
return QuantizedActivation(
data=result.view(out_shape),
scale=scales.view(out_shape[:-1] + (num_groups,)),
orig_dtype=x.dtype,
orig_shape=out_shape,
quant_key=quant_key,
)
|

##

`_silu_and_mul_fp8_static(x, linear)`


SiluAndMul + FP8 static per-tensor quantization.

## Source code in `vllm/model_executor/layers/fusion/fused_act_quant.py`


| def _silu_and_mul_fp8_static(
x: torch.Tensor, linear: LinearBase
) -> QuantizedActivation:
"""SiluAndMul + FP8 static per-tensor quantization."""
d = x.shape[-1] // 2
out_shape = x.shape[:-1] + (d,)
result = torch.empty(out_shape, dtype=FP8_DTYPE, device=x.device)
# TODO(mgoin): read the consumer scale via the contract instead of reaching
# into the kernel-specific input_scale attribute.
scale = linear.input_scale
torch.ops._C.silu_and_mul_quant(result, x, scale)
return QuantizedActivation(
data=result,
scale=scale,
orig_dtype=x.dtype,
orig_shape=out_shape,
quant_key=kFp8StaticTensorSym,
)
|

##

`_silu_and_mul_nvfp4_dynamic(x, linear)`


SiluAndMul + NVFP4 dynamic quantization.

## Source code in `vllm/model_executor/layers/fusion/fused_act_quant.py`


| def _silu_and_mul_nvfp4_dynamic(
x: torch.Tensor, linear: LinearBase
) -> QuantizedActivation:
"""SiluAndMul + NVFP4 dynamic quantization."""
assert x.ndim == 2, f"Input must be 2D [batch, hidden*2], got {x.shape}"
d = x.shape[-1] // 2
out_shape = x.shape[:-1] + (d,)
num_tokens = x.shape[0]
# NVFP4 packs 2 values into 1 byte
result = torch.empty((num_tokens, d // 2), dtype=FP4_DTYPE, device=x.device)
# Block scale output: swizzled tensor-core layout
# [num_m_tiles, num_k_tiles, 32, 4, 4] of int32-packed FP8 scales, so the
# row/col extents must be padded to the 128x4 tile like
# scaled_fp4_quant's allocator (create_fp4_scale_tensor). Each group of 16
# elements shares one FP8 scale.
rounded_m = round_up(num_tokens, 128)
rounded_n = round_up(d // 16, 4)
block_scale = torch.empty(
(rounded_m, rounded_n // 4), dtype=torch.int32, device=x.device
).view(FP8_DTYPE)
# The kernel folds the global scale into the block scales, and the
# consumer GEMM's alpha (= input_global_scale * weight_global_scale)
# divides it back out, so quantize with the reciprocal like the unfused
# scaled_fp4_quant path does.
input_global_scale_inv = getattr(linear, "input_global_scale_inv", None)
assert input_global_scale_inv is not None, (
"input_global_scale_inv is required for NVFP4 quantization"
)
torch.ops._C.silu_and_mul_nvfp4_quant(
result, block_scale, x, input_global_scale_inv
)
return QuantizedActivation(
data=result.view(out_shape[:-1] + (d // 2,)),
scale=block_scale,
orig_dtype=x.dtype,
orig_shape=out_shape,
quant_key=kNvfp4Dynamic,
)
|

##

`maybe_fused_act_quant(act_fn, x, linear)`


Apply act_fn, fusing the downstream linear's input quant when possible.

Returns a QuantizedActivation when a fused kernel matches the activation and the consumer's effective input quantization key, else the plain activation.

## Source code in `vllm/model_executor/layers/fusion/fused_act_quant.py`


| def maybe_fused_act_quant(
act_fn: torch.nn.Module,
x: torch.Tensor,
linear: LinearBase,
) -> "torch.Tensor | QuantizedActivation":
"""Apply act_fn, fusing the downstream linear's input quant when possible.
Returns a QuantizedActivation when a fused kernel matches the activation and
the consumer's effective input quantization key, else the plain activation.
"""
key = get_input_quant_key(linear)
if key is not None:
registry_key = (type(act_fn), key)
producer = _FUSED_ACT_QUANT.get(registry_key)
support = _FUSED_ACT_QUANT_SUPPORT.get(registry_key)
if producer is not None and (support is None or support(act_fn, x, linear)):
return producer(x, linear)
return act_fn(x)
|