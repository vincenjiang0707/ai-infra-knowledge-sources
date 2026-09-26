source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fusion/relu2_fp8_quant/
lastmod: 2026-09-24

BF16 ReLU2 followed by static per-tensor FP8 quantization.

## Source code in `vllm/model_executor/layers/fusion/relu2_fp8_quant.py`


| def relu_squared_static_fp8_quant(
x: torch.Tensor, linear: LinearBase
) -> QuantizedActivation:
"""BF16 ReLU2 followed by static per-tensor FP8 quantization."""
assert x.dtype == torch.bfloat16
assert x.is_contiguous()
scale = linear.input_scale
assert scale.dtype == torch.float32
assert x.device == scale.device
assert scale.numel() == 1
output = torch.empty_like(x, dtype=current_platform.fp8_dtype())
if x.numel() != 0:
block_size = min(triton.next_power_of_2(x.shape[-1]), 2048)
num_warps = min(max(block_size // 256, 1), 4)
grid = lambda meta: (triton.cdiv(x.numel(), meta["BLOCK_SIZE"]),)
_relu_squared_static_fp8_quant_kernel[grid](
x,
scale,
output,
x.numel(),
FP8_MIN=_FP8_MIN,
FP8_MAX=_FP8_MAX,
BLOCK_SIZE=block_size,
num_warps=num_warps,
)
return QuantizedActivation(
data=output,
scale=scale,
orig_dtype=x.dtype,
orig_shape=x.shape,
quant_key=kFp8StaticTensorSym,
)
|