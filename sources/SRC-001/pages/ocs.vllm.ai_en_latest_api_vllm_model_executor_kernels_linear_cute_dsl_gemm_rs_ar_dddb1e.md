source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar/
lastmod: 2026-09-23

class GemmRsAr:
"""Own the symmetric workspace for GEMM-RS/AR launches.
All TP ranks must belong to one NVLink domain for multimem instructions.
Each instance is bound to either RS or AR. A vLLM worker has one static
sequence-parallel topology, so the process-wide singleton only needs one
mode. Two independent mode-specific singletons would lift that restriction
but duplicate the large symmetric workspace. A future mixed-mode design
should instead use lightweight RS/AR frontends over one shared multicast
workspace; that is outside this integration's current scope.
"""
def __init__(self, *, max_M: int, N: int, all_reduce: bool = False) -> None:
tp_group = get_tp_group()
group = tp_group.device_group
rank = tp_group.rank_in_group
world_size = tp_group.world_size
device = torch.device("cuda", torch.accelerator.current_device_index())
assert 1 < world_size <= 16
assert 128 % world_size == 0
assert max_M >= 128 and N % 128 == 0
max_M = (max_M + world_size - 1) // world_size * world_size
self.rank = rank
self.world_size = world_size
self.max_M = max_M
self.N = N
self.device = device
self.all_reduce = all_reduce
self.dtypes: set[str] = set()
self.partial = symm_mem.empty((max_M, N), dtype=torch.bfloat16, device=device)
self.partial_handle = symm_mem.rendezvous(self.partial, group)
if self.partial_handle.multicast_ptr == 0:
raise RuntimeError("GEMM-RS/AR requires NVLink multicast memory")
self.partial_mc_ptr = make_ptr(
BFloat16,
self.partial_handle.multicast_ptr,
cute.AddressSpace.gmem,
assumed_align=32,
)
grid_m = (max_M + 127) // 128
cta_group = 2 if max_M >= 1024 or grid_m % 2 == 0 else 1
grid_m = (grid_m + cta_group - 1) // cta_group * cta_group
self.num_sms = torch.cuda.get_device_properties(device).multi_processor_count
max_flags = grid_m * (N // 128) + self.num_sms
self.flags = symm_mem.empty(max_flags, dtype=torch.int32, device=device)
self.flags_handle = symm_mem.rendezvous(self.flags, group)
if self.flags_handle.multicast_ptr == 0:
raise RuntimeError("GEMM-RS/AR requires NVLink multicast memory")
self.flags.zero_()
self.flags_mc_ptr = make_ptr(
Int32,
self.flags_handle.multicast_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
self.peer_flag_ptr = make_ptr(
Int64,
self.flags_handle.buffer_ptrs_dev,
cute.AddressSpace.gmem,
assumed_align=8,
)
torch.accelerator.synchronize(device)
tp_group.barrier()
def can_run(self, linear: LinearBase) -> bool:
from vllm.model_executor.kernels.linear.mxfp8.flashinfer import (
FlashInferCutedslMxfp8LinearKernel,
FlashInferCutlassMxfp8LinearKernel,
)
# Called before weight loading; online quantization starts on meta.
if isinstance(linear.quant_method, UnquantizedLinearMethod):
dtype, k_alignment = "bf16", 64
if linear.weight.dtype != torch.bfloat16:
return False
else:
method = getattr(linear, "scheme", linear.quant_method)
kernel = getattr(method, "kernel", None)
if not isinstance(
kernel,
(
FlashInferCutedslMxfp8LinearKernel,
FlashInferCutlassMxfp8LinearKernel,
),
):
return False
dtype, k_alignment = "mxfp8", 128
w = linear.weight
if (
w.ndim != 2
or w.shape[0] != self.N
or w.shape[1] % k_alignment != 0
or (w.device != self.device and not w.is_meta)
or not w.is_contiguous()
):
return False
self.dtypes.add(dtype)
return True
def warn_incompatible_projection(self) -> None:
logger.warning_once(
"Some projections are incompatible with GEMM-RS/AR; using the "
"unfused path instead.",
scope="global",
)
def should_run(self, x: torch.Tensor) -> bool:
# Use the same threshold for RS and AR for now. Small-M shapes are
# supported but faster on the existing LL path.
return x.shape[0] >= 128
def apply(self, x: torch.Tensor, linear: LinearBase) -> torch.Tensor:
from vllm.model_executor.kernels.linear.mxfp8.flashinfer import (
FlashInferCutedslMxfp8LinearKernel,
)
method = getattr(linear, "scheme", linear.quant_method)
w = linear.weight
if isinstance(
getattr(method, "kernel", None), FlashInferCutedslMxfp8LinearKernel
):
# This backend stores a column-major [K, N] view after loading.
w = w.t()
w_sf = getattr(linear, "weight_scale", None)
assert x.ndim == 2
M, K = x.shape
assert 0 < M <= self.max_M
assert x.dtype == torch.bfloat16
assert x.device == self.device
assert x.is_contiguous()
assert w.device == self.device
N = self.N
dtype = "mxfp8" if w.dtype == torch.float8_e4m3fn else "bf16"
x_sf = None
if dtype == "mxfp8":
from vllm.model_executor.layers.quantization.utils.mxfp8_utils import (
mxfp8_e4m3_quantize,
)
assert w_sf is not None
assert w_sf.dtype == torch.uint8 and w_sf.device == self.device
assert w_sf.ndim == 1 and w_sf.is_contiguous()
assert w_sf.numel() == N * (K // 32)
assert w.shape == (N, K) and K % 128 == 0
assert w.is_contiguous()
x, x_sf = mxfp8_e4m3_quantize(x, is_sf_swizzled_layout=True)
# The kernel declares the scales as E8M0; the stored/quantized
# tensors carry the same bits as uint8.
x_sf = x_sf.view(torch.float8_e8m0fnu)
w_sf = w_sf.view(torch.float8_e8m0fnu)
else:
assert w_sf is None
assert w.shape == (N, K) and K % 64 == 0
assert w.dtype == torch.bfloat16
assert w.is_contiguous()
padded_M = (M + self.world_size - 1) // self.world_size
padded_M *= self.world_size
local_M = padded_M // self.world_size
grid_m = (M + 127) // 128
# Avoid padding small odd grids; 2-CTA wins consistently for M >= 1024.
cta_group = 2 if M >= 1024 or grid_m % 2 == 0 else 1
grid_m = (grid_m + cta_group - 1) // cta_group * cta_group
num_tiles = grid_m * (N // 128)
num_ctas = min(num_tiles, self.num_sms)
num_ctas = num_ctas // cta_group * cta_group
assert self.flags.numel() >= num_tiles + num_ctas
output = None
if not self.all_reduce:
output = torch.empty((local_M, N), dtype=torch.bfloat16, device=self.device)
# The kernel never touches rows at or beyond M. Callers that hand
# in an unpadded M (DeepSeek-V4.1 slices the SP all-gather back to
# the real token count) expect the same zero padding rows that
# ``sp_reduce_scatter`` produces, so clear them here. This is a
# no-op whenever M is already a multiple of the TP size.
valid_rows = min(max(M - self.rank * local_M, 0), local_M)
if valid_rows < local_M:
output[valid_rows:].zero_()
compiled = Sm100GemmRsAr.compile(
self.rank,
self.world_size,
cta_group,
self.all_reduce,
dtype=dtype,
)
compiled(
x,
w,
x_sf,
w_sf,
self.partial[:padded_M],
self.partial_mc_ptr,
output,
self.flags,
self.flags_mc_ptr,
self.peer_flag_ptr,
num_ctas,
)
if self.all_reduce:
# AttnRes may retain output past the next workspace reuse.
# A future kernel could overlap this copy using an extra warp or
# the communication warp.
return self.partial[:M].clone()
assert output is not None
return output