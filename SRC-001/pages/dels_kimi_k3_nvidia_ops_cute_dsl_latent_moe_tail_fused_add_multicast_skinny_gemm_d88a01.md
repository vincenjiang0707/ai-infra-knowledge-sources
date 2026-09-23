source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm/
lastmod: 2026-09-23

class FusedAddMulticastSkinnyGemm:
"""SIMT GEMM adapted from the existing Skinny GEMM."""
def __init__(
self,
*,
num_rows: int,
hidden_dim: int,
config: SkinnyConfig,
) -> None:
if config.block_size % 32:
raise ValueError("skinny block_size must be a multiple of 32")
self.num_rows = num_rows
self.hidden_dim = hidden_dim
self.block_size = config.block_size
self.outputs_per_block = config.outputs_per_block
self.k_unroll = config.k_unroll
self.vector_width = config.vector_width
self.prefetch_b_before_pdl = config.prefetch_b_before_pdl
self.num_warps = config.block_size // 32
@cute.jit
def __call__(
self,
gA: cute.Tensor,
gB: cute.Tensor,
gShared: cute.Tensor,
output_multicast_ptr: Int64,
stream: cuda.CUstream,
) -> None:
n = cute.size(gB, mode=[0])
k = cute.size(gA, mode=[1])
copy_a = cute.make_copy_atom(
cute.nvgpu.CopyG2ROp(),
BFloat16,
num_bits_per_copy=self.vector_width * BFloat16.width,
load_cache_mode=cute.nvgpu.LoadCacheMode.ALWAYS,
)
copy_b = cute.make_copy_atom(
cute.nvgpu.CopyG2ROp(),
BFloat16,
num_bits_per_copy=self.vector_width * BFloat16.width,
load_cache_mode=cute.nvgpu.LoadCacheMode.STREAMING,
)
self.kernel(
gA,
gB,
gShared,
output_multicast_ptr,
k,
copy_a,
copy_b,
).launch(
grid=[cute.ceil_div(n, self.outputs_per_block), 1, 1],
block=[self.block_size, 1, 1],
smem=(self.num_rows * self.outputs_per_block * self.num_warps * 4),
stream=stream,
use_pdl=True,
min_blocks_per_mp=1,
)
@cute.kernel
def kernel(
self,
gA: cute.Tensor,
gB: cute.Tensor,
gShared: cute.Tensor,
output_multicast_ptr: Int64,
k_extent: cutlass.Int32,
copy_a: cute.CopyAtom,
copy_b: cute.CopyAtom,
) -> None:
tidx, _, _ = cute.arch.thread_idx()
block_idx, _, _ = cute.arch.block_idx()
warp_idx = cute.arch.warp_idx()
outputs_per_block: cutlass.Constexpr = self.outputs_per_block
vector_width: cutlass.Constexpr = self.vector_width
block_size: cutlass.Constexpr = self.block_size
num_warps: cutlass.Constexpr = self.num_warps
num_rows: cutlass.Constexpr = self.num_rows
acc = cute.make_rmem_tensor(
cute.make_layout(
(num_rows, outputs_per_block),
stride=(outputs_per_block, 1),
),
Float32,
)
acc.fill(0.0)
n_base = block_idx * outputs_per_block
k_tile_size: cutlass.Constexpr = block_size * vector_width
num_k_tiles = k_extent // k_tile_size
gA_vec = cute.logical_divide(gA, (None, vector_width))
gB_vec = cute.logical_divide(gB, (None, vector_width))
tA_all = cute.logical_divide(gA_vec, (None, (None, block_size)))
tB_all = cute.logical_divide(gB_vec, (None, (None, block_size)))
tA = tA_all[None, (None, (tidx, None))]
a_regs = cute.make_rmem_tensor(
cute.make_layout(
(num_rows, vector_width),
stride=(vector_width, 1),
),
BFloat16,
)
b_regs = cute.make_rmem_tensor(
cute.make_layout(
(outputs_per_block, vector_width),
stride=(vector_width, 1),
),
BFloat16,
)
if const_expr(self.prefetch_b_before_pdl):
for ni in cutlass.range_constexpr(outputs_per_block):
tB = tB_all[n_base + ni, (None, (tidx, None))]
cute.copy(copy_b, tB[None, 0], b_regs[ni, None])
cute.arch.griddepcontrol_wait()
for mi in cutlass.range_constexpr(num_rows):
cute.copy(copy_a, tA[mi, None, 0], a_regs[mi, None])
if const_expr(not self.prefetch_b_before_pdl):
for ni in cutlass.range_constexpr(outputs_per_block):
tB = tB_all[n_base + ni, (None, (tidx, None))]
cute.copy(copy_b, tB[None, 0], b_regs[ni, None])
for vi in cutlass.range_constexpr(vector_width):
for mi in cutlass.range_constexpr(num_rows):
for ni in cutlass.range_constexpr(outputs_per_block):
acc[mi, ni] = fma_f32_bf16(
a_regs[mi, vi],
b_regs[ni, vi],
acc[mi, ni],
)
for k_tile in cutlass.range(1, num_k_tiles, unroll=self.k_unroll):
for mi in cutlass.range_constexpr(num_rows):
cute.copy(
copy_a,
tA[mi, None, k_tile],
a_regs[mi, None],
)
for ni in cutlass.range_constexpr(outputs_per_block):
tB = tB_all[n_base + ni, (None, (tidx, None))]
cute.copy(copy_b, tB[None, k_tile], b_regs[ni, None])
for vi in cutlass.range_constexpr(vector_width):
for mi in cutlass.range_constexpr(num_rows):
for ni in cutlass.range_constexpr(outputs_per_block):
acc[mi, ni] = fma_f32_bf16(
a_regs[mi, vi],
b_regs[ni, vi],
acc[mi, ni],
)
for mi in cutlass.range_constexpr(num_rows):
for ni in cutlass.range_constexpr(outputs_per_block):
acc[mi, ni] = cute.arch.warp_reduction_sum(acc[mi, ni])
smem_layout = cute.make_layout(
(num_rows, outputs_per_block, num_warps),
stride=(outputs_per_block * num_warps, num_warps, 1),
)
smem = cutlass.utils.SmemAllocator()
partials = smem.allocate_tensor(
Float32,
smem_layout,
byte_alignment=16,
)
with cute.arch.elect_one():
for mi in cutlass.range_constexpr(num_rows):
for ni in cutlass.range_constexpr(outputs_per_block):
partials[mi, ni, warp_idx] = acc[mi, ni]
cute.arch.sync_threads()
if tidx == 0:
fused = cute.make_rmem_tensor(
cute.make_layout((outputs_per_block,)),
BFloat16,
)
for mi in cutlass.range_constexpr(num_rows):
for ni in cutlass.range_constexpr(outputs_per_block):
total = (
partials[mi, ni, None]
.load()
.reduce(
cute.ReductionOp.ADD,
init_val=Float32(0.0),
reduction_profile=0,
)
)
gemm_value = Float32(total).to(BFloat16)
fused[ni] = (
gemm_value.to(Float32) + gShared[mi, n_base + ni].to(Float32)
).to(BFloat16)
output_offset = Int64((mi * self.hidden_dim + n_base) * 2)
if const_expr(outputs_per_block == 2):
packed = sanitize_negative_zero_u32(bf16x2_to_u32(fused.load()))
store_global_u32(
output_multicast_ptr + output_offset,
packed,
)
elif const_expr(outputs_per_block == 4):
packed = sanitize_negative_zero_u32x2(
bf16x4_to_packed_u32x2(fused.load())
)
store_global_u32x2(
output_multicast_ptr + output_offset,
packed,
)
else:
packed = sanitize_negative_zero(
bf16x8_to_packed_u32x4(fused.load())
)
store_global_u32x4(
output_multicast_ptr + output_offset,
packed,
)
cute.arch.griddepcontrol_launch_dependents()