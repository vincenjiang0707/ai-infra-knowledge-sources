source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/pytorch/
lastmod: 2026-09-24

class BlockWiseTorchFP8ScaledMMLinearKernel(Fp8BlockScaledMMLinearKernel):
"""FP8 block-scaled linear kernel using ``torch._scaled_mm``.
Implements the block-scaled path of ``torch._scaled_mm``, which
dispatches on the shapes of the scale tensors. For ``A = [M, K]`` and
``B = [K, N]`` (both fp8) the op's block path requires, with float32
scales:
* 1x128 activation: ``scale_a = [M, ceil(K / 128)]``
* 128x128 weight: ``scale_b = [ceil(K / 128), ceil(N / 128)]``
"""
def __init__(self, config: FP8ScaledMMLinearLayerConfig) -> None:
super().__init__(config)
act_scale_descriptor = config.activation_quant_key.scale
self.quant_fp8 = QuantFP8(
static=act_scale_descriptor.static,
group_shape=act_scale_descriptor.group_shape,
num_token_padding=self.get_output_padding(),
use_ue8m0=False,
column_major_scales=current_platform.is_cuda_alike(),
)
@classmethod
def is_supported(
cls, compute_capability: int | None = None
) -> tuple[bool, str | None]:
if not (current_platform.is_cuda_alike() or current_platform.is_xpu()):
return False, "requires CUDA, ROCm or XPU."
# torch._scaled_mm DeepSeek-style (1x128, 128x128) block scaling is
# only implemented for SM90 (Hopper) on NVIDIA CUDA. See PyTorch's
# _check_deepseek_support():
# https://github.com/pytorch/pytorch/blob/33812ece06e2b0d597f73fbe41de03a83f9109f9/aten/src/ATen/native/cuda/ScaledBlas.cpp#L804-L820 # noqa: E501
if current_platform.is_cuda():
is_sm90 = (
compute_capability == 90
if compute_capability is not None
else current_platform.is_device_capability(90)
)
if not is_sm90:
return (
False,
"DeepSeek-style (1x128, 128x128) block scaling on CUDA "
"requires compute capability 90 (Hopper).",
)
return True, None
@classmethod
def can_implement(
cls, config: FP8ScaledMMLinearLayerConfig
) -> tuple[bool, str | None]:
can_implement_base, reason = super().can_implement(config)
if not can_implement_base:
return can_implement_base, reason
act_group_shape = config.activation_quant_key.scale.group_shape
if act_group_shape != GroupShape(1, 128):
return (
False,
"requires 1x128 activation quantization.",
)
weight_group_shape = config.weight_quant_key.scale.group_shape
if weight_group_shape != GroupShape(128, 128):
return (
False,
"requires 128x128 block weight quantization.",
)
return True, None
def apply_block_scaled_mm(
self,
A: torch.Tensor,
B: torch.Tensor,
As: torch.Tensor,
Bs: torch.Tensor,
) -> torch.Tensor:
# torch._scaled_mm implemented by cuBLASLt requires the M dimension to be a
# multiple of 4; pad A (and its column-major scale) up and slice back.
# https://docs.nvidia.com/cuda/cublas/index.html?highlight=128%2520element%25201D%2520and%2520128x128%25202D#scaling-factors-layouts # noqa: E501
M = A.shape[0]
pad = (-M) % 4 if current_platform.is_cuda() else 0
if pad:
Ap = A.new_empty((M + pad, A.shape[1]))
Ap[:M] = A
A = Ap
# As is column-major [M, ceil(K/128)] (stride (1, M)); build a padded
# column-major buffer and copy only the valid rows. Padded rows are left
# uninitialized — they don't affect the sliced-back output.
Asp = As.new_empty((As.shape[1], M + pad)).t()
Asp[:M] = As
As = Asp
output = torch._scaled_mm(
A,
B.t(),
scale_a=As,
scale_b=Bs.t(),
out_dtype=self.config.out_dtype,
)
if type(output) is tuple and len(output) == 2:
output = output[0]
if pad:
output = output[:M, :]
return output