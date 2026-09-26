source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit/
lastmod: 2026-09-24

class AllReduceRMSNormWithReduceScatterEarlyExit:
"""One routed role plus one compact ReduceScatter role."""
def __init__(
self,
*,
rank: int,
tp_size: int,
latent_dim: int,
hidden_dim: int,
max_m: int,
max_token_ctas: int,
fp32_internal: bool = False,
include_reduce_scatter: bool = True,
include_routed: bool = True,
top_k: int = 0,
):
validate_shape(
tp_size=tp_size,
latent_dim=latent_dim,
hidden_dim=hidden_dim,
)
if not 0 <= rank < tp_size:
raise ValueError(f"rank must be in [0,{tp_size}), got {rank}")
if not include_routed and not include_reduce_scatter:
raise ValueError("at least one collective role must be enabled")
self.rank = rank
self.tp_size = tp_size
self.latent_dim = latent_dim
self.hidden_dim = hidden_dim
(
self.shard_dim,
mapped_cluster,
mapped_threads,
shared_roles,
) = _mapping(tp_size, latent_dim, hidden_dim)
seven_cta_geometry = (
include_routed
and max_m <= _SEVEN_CTA_MAX_M
and max_token_ctas == max_m
and (tp_size, latent_dim, hidden_dim) == (8, 3584, 7168)
)
self.seven_cta_geometry = seven_cta_geometry
self.single_token_geometry = seven_cta_geometry and max_m == 1
if include_reduce_scatter:
if seven_cta_geometry:
self.cluster_ctas = 7
self.threads = 64
shared_roles = (tp_size + self.cluster_ctas - 1) // self.cluster_ctas
else:
self.cluster_ctas = mapped_cluster
self.threads = mapped_threads
else:
if seven_cta_geometry:
self.threads, self.cluster_ctas = 64, 7
else:
self.threads, self.cluster_ctas = _select_routed_schedule(
tp_size, latent_dim, hidden_dim, max_m
)
self.shared_roles = 1 if include_reduce_scatter else shared_roles
self.shared_destination_stride = self.shared_roles * self.cluster_ctas
self.shared_destinations_per_cta = (
self.tp_size + self.shared_destination_stride - 1
) // self.shared_destination_stride
self.shard_vectors = self.shard_dim // VEC_BF16
# Diagnostic specialization: a one-role grid executes only the routed
# AllReduce/RMSNorm path. Keep this compile-time so the production
# fused path is unchanged when include_reduce_scatter=True.
if include_routed and include_reduce_scatter:
self.roles = 1 + self.shared_roles
elif include_routed:
self.roles = 1
else:
self.roles = self.shared_roles
self.warps = (self.threads + 31) // 32
self.last_warp_lanes = self.threads - (self.warps - 1) * 32
self.last_warp_mask = (1 << self.last_warp_lanes) - 1
# The upstream MNNVL oneshot protocol assigns one cluster to each
# token. Keep that exact ownership in the routed-only diagnostic;
# reusing a cluster for multiple token waves allows the Lamport
# generation metadata to change between waves.
self.token_ctas = (
min(max_m, max_token_ctas) if include_reduce_scatter else max_m
)
self.fp32_internal = fp32_internal
self.include_reduce_scatter = include_reduce_scatter
self.include_routed = include_routed
self.top_k = top_k
@cute.jit
def __call__(
self,
latent_source: cute.Tensor,
gamma: cute.Tensor,
latent_output: cute.Tensor,
routed_workspace: cute.Tensor,
latent_flags: cute.Tensor,
latent_multicast_ptr: Int64,
shared_source: cute.Tensor,
shared_output: cute.Tensor,
shared_workspace: cute.Tensor,
shared_flags: cute.Tensor,
shared_peer_ptrs: cute.Tensor,
m: Int32,
epsilon: Float32,
stream: cuda.CUstream,
expert_weights: cute.Tensor,
expanded_idx_to_permuted_idx: cute.Tensor,
):
grid_x = m if cutlass.const_expr(self.seven_cta_geometry) else self.token_ctas
self.kernel(
latent_source,
gamma,
latent_output,
routed_workspace,
latent_flags,
latent_multicast_ptr,
shared_source,
shared_output,
shared_workspace,
shared_flags,
shared_peer_ptrs,
m,
epsilon,
expert_weights,
expanded_idx_to_permuted_idx,
).launch(
grid=(grid_x, self.cluster_ctas, self.roles),
block=(self.threads, 1, 1),
cluster=(1, self.cluster_ctas, 1),
smem=2 * self.cluster_ctas * self.warps * 4,
stream=stream,
use_pdl=True,
)
@cute.kernel
def kernel(
self,
latent_source: cute.Tensor,
gamma: cute.Tensor,
latent_output: cute.Tensor,
routed_workspace: cute.Tensor,
latent_flags: cute.Tensor,
latent_multicast_ptr: Int64,
shared_source: cute.Tensor,
shared_output: cute.Tensor,
shared_workspace: cute.Tensor,
shared_flags: cute.Tensor,
shared_peer_ptrs: cute.Tensor,
m: Int32,
epsilon: Float32,
expert_weights: cute.Tensor,
expanded_idx_to_permuted_idx: cute.Tensor,
):
tidx, _, _ = cute.arch.thread_idx()
token_cta, cta_y, role = cute.arch.block_idx()
logical_role = role
if cutlass.const_expr(not self.include_routed):
# A shared-only grid starts at z=0, while _token_device reserves
# logical role 0 for the routed collective.
logical_role = role + Int32(1)
cluster_rank = cute.arch.make_warp_uniform(cute.arch.block_idx_in_cluster())
cute.arch.griddepcontrol_wait()
token = token_cta
parity = Int32(0)
while token < m:
self._token_device(
latent_source,
gamma,
latent_output,
routed_workspace,
latent_flags,
latent_multicast_ptr,
shared_source,
shared_output,
shared_workspace,
shared_flags,
shared_peer_ptrs,
m,
epsilon,
token,
parity,
token_cta,
cta_y,
logical_role,
cluster_rank,
tidx,
expert_weights,
expanded_idx_to_permuted_idx,
)
token = token + self.token_ctas
parity = parity ^ Int32(1)
@cute.jit
def _token_device(
self,
latent_source: cute.Tensor,
gamma: cute.Tensor,
latent_output: cute.Tensor,
routed_workspace: cute.Tensor,
latent_flags: cute.Tensor,
latent_multicast_ptr: Int64,
shared_source: cute.Tensor,
shared_output: cute.Tensor,
shared_workspace: cute.Tensor,
shared_flags: cute.Tensor,
shared_peer_ptrs: cute.Tensor,
m: Int32,
epsilon: Float32,
token: Int32,
parity: Int32,
token_cta: Int32,
cta_y: Int32,
role: Int32,
cluster_rank: Int32,
tidx: Int32,
expert_weights: cute.Tensor,
expanded_idx_to_permuted_idx: cute.Tensor,
):
if role == 0:
# ---------------- routed AllReduce + RMSNorm ----------------
packed_idx = cluster_rank * self.threads + tidx
element_offset = (
Int64(token) * self.latent_dim + Int64(packed_idx) * VEC_BF16
)
current_index = cute.arch.load((latent_flags.iterator + 0).llvm_ptr, Uint32)
dirty_index = cute.arch.load((latent_flags.iterator + 1).llvm_ptr, Uint32)
bytes_per_buffer = cute.arch.load(
(latent_flags.iterator + 2).llvm_ptr, Uint32
)
dirty_num_stages = cute.arch.load(
(latent_flags.iterator + 3).llvm_ptr, Uint32
)
bytes_to_clear = cute.arch.load(
(latent_flags.iterator + 4).llvm_ptr, Uint32
)
current_elements = Int64(current_index) * (
Int64(bytes_per_buffer) // Int64(2)
)
dirty_elements = Int64(dirty_index) * (Int64(bytes_per_buffer) // Int64(2))
if cutlass.const_expr(self.top_k > 0):
# finalize topk reduction
if cutlass.const_expr(
self.top_k == 16
and self.latent_dim == 3584
and expert_weights.element_type == BFloat16
):
gemm2_vector = cute.make_ptr(
BFloat16,
(
latent_source.iterator + Int64(packed_idx) * VEC_BF16
).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
route_indices = cute.make_ptr(
Int32,
(
expanded_idx_to_permuted_idx.iterator
+ Int64(token) * self.top_k
).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
route_weights = cute.make_ptr(
BFloat16,
(expert_weights.iterator + Int64(token) * self.top_k).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
local_packed = sanitize_negative_zero(
finalize_top16_bf16(
gemm2_vector,
route_indices,
route_weights,
)
)
else:
local_values = cute.make_rmem_tensor(
cute.make_layout((VEC_BF16,)), Float32
)
for element in cutlass.range_constexpr(VEC_BF16):
local_values[element] = Float32(0.0)
for slot in cutlass.range_constexpr(self.top_k):
permuted_idx = expanded_idx_to_permuted_idx[token, slot]
if permuted_idx >= Int32(0):
permuted_element = (
Int64(permuted_idx) * self.latent_dim
+ Int64(packed_idx) * VEC_BF16
)
permuted_ptr = cute.make_ptr(
BFloat16,
(latent_source.iterator + permuted_element).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
values = packed_u32x4_to_bf16x8(
load_global_u32x4(permuted_ptr, volatile=False)
)
weight = expert_weights[token, slot].to(Float32)
for element in cutlass.range_constexpr(VEC_BF16):
local_values[element] = (
local_values[element]
+ values[element].to(Float32) * weight
)
local_packed = sanitize_negative_zero(
bf16x8_to_packed_u32x4(local_values.load().to(BFloat16))
)
else:
local_ptr = cute.make_ptr(
BFloat16,
(latent_source.iterator + element_offset).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
local_packed = sanitize_negative_zero(
load_global_u32x4(local_ptr, volatile=False)
)
multicast_offset = (
Int64(current_index) * Int64(bytes_per_buffer)
+ (
(Int64(token) * self.tp_size + self.rank) * self.latent_dim
+ Int64(packed_idx) * VEC_BF16
)
* 2
)
stmc_bf16x8(
latent_multicast_ptr + multicast_offset,
local_packed,
)
cute.arch.griddepcontrol_launch_dependents()
if cutlass.const_expr(not self.single_token_geometry):
cute.arch.cluster_arrive()
if cluster_rank == 0 and tidx < 32:
cute.arch.cluster_wait()
if tidx == 0:
red_async_release_gpu_add_u32(
latent_flags.iterator + 8, Uint32(1)
)
global_tid = (
Int64(token) * self.cluster_ctas + Int64(cta_y)
) * self.threads + Int64(tidx)
total_threads = Int64(m) * self.cluster_ctas * self.threads
clear_fragments = (Int64(bytes_to_clear) + PACKED_BYTES - 1) // PACKED_BYTES
clear_idx = global_tid
if dirty_num_stages > Uint32(0):
while clear_idx < clear_fragments:
clear_ptr = cute.make_ptr(
BFloat16,
(
routed_workspace.iterator
+ dirty_elements
+ clear_idx * VEC_BF16
).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
store_lamport_sentinel_128(clear_ptr)
clear_idx = clear_idx + total_threads
rank_words = cute.make_rmem_tensor(
cute.make_layout((self.tp_size, 4), stride=(4, 1)), Uint32
)
for word in cutlass.range_constexpr(4):
rank_words[self.rank, word] = local_packed[word]
valid = False
while not valid:
valid = True
for source_rank in cutlass.range_constexpr(self.tp_size):
if cutlass.const_expr(source_rank != self.rank):
remote_element = current_elements + (
(Int64(token) * self.tp_size + source_rank)
* self.latent_dim
+ Int64(packed_idx) * VEC_BF16
)
remote_ptr = cute.make_ptr(
BFloat16,
(routed_workspace.iterator + remote_element).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
remote = load_global_u32x4(remote_ptr, volatile=True)
for word in cutlass.range_constexpr(4):
rank_words[source_rank, word] = remote[word]
valid = valid & (not fragment_is_dirty(remote))
accum = cute.make_rmem_tensor(cute.make_layout((VEC_BF16,)), Float32)
for element in cutlass.range_constexpr(VEC_BF16):
accum[element] = Float32(0.0)
for source_rank in cutlass.range_constexpr(self.tp_size):
values = packed_u32x4_to_bf16x8(
rank_words[source_rank, None].load()
).to(Float32)
for element in cutlass.range_constexpr(VEC_BF16):
accum[element] = accum[element] + values[element]
if cutlass.const_expr(self.fp32_internal):
# High-precision fused mode: retain the rank reduction in
# FP32 through the RMS square and row reduction.
norm_input = accum.load()
norm_square = norm_input * norm_input
else:
norm_input_bf16 = accum.load().to(BFloat16)
norm_input = norm_input_bf16.to(Float32)
# Upstream-compatible mode: FlashInfer evaluates BF16 *
# BF16 first, then promotes the rounded square to FP32.
norm_square = (norm_input_bf16 * norm_input_bf16).to(Float32)
thread_sum = norm_square.reduce(
cute.ReductionOp.ADD,
init_val=Float32(0.0),
reduction_profile=0,
)
smem = cutlass.utils.SmemAllocator()
cluster_sums = smem.allocate_tensor(
Float32,
cute.make_layout((2 * self.cluster_ctas * self.warps,)),
byte_alignment=16,
)
lane = cute.arch.lane_idx()
warp_idx = cute.arch.warp_idx()
warp_sum = warp_sum_specialized(
thread_sum,
warp_idx,
lane,
self.warps,
self.last_warp_lanes,
self.last_warp_mask,
)
# Alternate DSM slots until the next cluster synchronization so
# peers may safely begin publishing the following token wave.
parity_offset = parity * Int32(self.cluster_ctas * self.warps)
if lane < self.cluster_ctas:
local_slot = (
cluster_sums.iterator
+ parity_offset
+ cluster_rank * self.warps
+ warp_idx
)
remote_slot = map_shared_to_peer(local_slot, lane)
store_shared_cluster_f32(remote_slot, warp_sum)
cute.arch.cluster_arrive()
cute.arch.cluster_wait()
full_sum = Float32(0.0)
for peer in cutlass.range_constexpr(self.cluster_ctas):
peer_slot = cluster_sums.iterator + parity_offset + peer * self.warps
if cutlass.const_expr(self.warps == 4):
sum0, sum1, sum2, sum3 = load_shared_f32x4(peer_slot)
full_sum = full_sum + sum0 + sum1 + sum2 + sum3
elif cutlass.const_expr(self.warps == 2):
sum0, sum1 = load_shared_f32x2(peer_slot)
full_sum = full_sum + sum0 + sum1
else:
for peer_warp in cutlass.range_constexpr(self.warps):
full_sum = (
full_sum
+ cluster_sums[
parity_offset + peer * self.warps + peer_warp
]
)
inv_rms = cute.math.rsqrt(
full_sum / Float32(self.latent_dim) + epsilon, fastmath=True
)
gamma_ptr = cute.make_ptr(
BFloat16,
(gamma.iterator + Int64(packed_idx) * VEC_BF16).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
gamma_values = packed_u32x4_to_bf16x8(
load_global_u32x4(gamma_ptr, volatile=False)
)
result = (norm_input * inv_rms * gamma_values.to(Float32)).to(BFloat16)
store_global_u32x4(
Int64((latent_output.iterator + element_offset).toint()),
bf16x8_to_packed_u32x4(result),
volatile=False,
)
# The general schedule waits until every token cluster has loaded
# this generation. The M=1 schedule has only this cluster, whose
# DSM barrier above already covers all routed CTAs.
if (
token_cta == 0
and token + self.token_ctas >= m
and cta_y == 0
and tidx == 0
):
access_counter = latent_flags.iterator + 8
if cutlass.const_expr(not self.single_token_geometry):
arrived = load_volatile_u32(access_counter)
while arrived < Uint32(m):
arrived = load_volatile_u32(access_counter)
next_index = (current_index + Uint32(1)) % Uint32(NUM_LAMPORT_BUFFERS)
actual_bytes = Uint32(m) * Uint32(self.tp_size * self.latent_dim * 2)
cute.arch.store((latent_flags.iterator + 0).llvm_ptr, next_index)
cute.arch.store((latent_flags.iterator + 1).llvm_ptr, current_index)
cute.arch.store(
(latent_flags.iterator + 2).llvm_ptr,
bytes_per_buffer,
)
cute.arch.store((latent_flags.iterator + 3).llvm_ptr, Uint32(1))
cute.arch.store((latent_flags.iterator + 4).llvm_ptr, actual_bytes)
for index in cutlass.range_constexpr(5, 8):
cute.arch.store(
(latent_flags.iterator + index).llvm_ptr,
Uint32(0),
)
cute.arch.store(access_counter.llvm_ptr, Uint32(0))
else:
# ---------------- shared ReduceScatter ----------------
shared_group = role - 1
destination = shared_group * self.cluster_ctas + cluster_rank
current_index = cute.arch.load((shared_flags.iterator + 0).llvm_ptr, Uint32)
dirty_index = cute.arch.load((shared_flags.iterator + 1).llvm_ptr, Uint32)
bytes_per_buffer = cute.arch.load(
(shared_flags.iterator + 2).llvm_ptr, Uint32
)
dirty_num_stages = cute.arch.load(
(shared_flags.iterator + 3).llvm_ptr, Uint32
)
bytes_to_clear = cute.arch.load(
(shared_flags.iterator + 4).llvm_ptr, Uint32
)
current_elements = Int64(current_index) * (
Int64(bytes_per_buffer) // Int64(2)
)
dirty_elements = Int64(dirty_index) * (Int64(bytes_per_buffer) // Int64(2))
for destination_round in cutlass.range_constexpr(
self.shared_destinations_per_cta
):
round_destination = destination + Int32(
destination_round * self.shared_destination_stride
)
if round_destination < Int32(self.tp_size):
peer_base = cute.arch.load(
(shared_peer_ptrs.iterator + round_destination).llvm_ptr,
Int64,
)
vector = tidx
while vector < self.shard_vectors:
source_element = (
Int64(token) * self.hidden_dim
+ Int64(round_destination) * self.shard_dim
+ Int64(vector) * VEC_BF16
)
source_ptr = cute.make_ptr(
BFloat16,
(shared_source.iterator + source_element).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
local_packed = sanitize_negative_zero(
load_global_u32x4(source_ptr, volatile=False)
)
destination_element = current_elements + (
(Int64(token) * self.tp_size + self.rank) * self.shard_dim
+ Int64(vector) * VEC_BF16
)
store_global_u32x4(
peer_base + destination_element * 2,
local_packed,
volatile=False,
)
vector = vector + self.threads
cute.arch.griddepcontrol_launch_dependents()
# One arrival per shared cluster and token.
cute.arch.cluster_arrive()
if cluster_rank == 0 and tidx < 32:
cute.arch.cluster_wait()
if tidx == 0:
red_async_release_gpu_add_u32(shared_flags.iterator + 8, Uint32(1))
total_threads = Int64(m) * self.tp_size * self.threads
clear_fragments = (Int64(bytes_to_clear) + PACKED_BYTES - 1) // PACKED_BYTES
for destination_round in cutlass.range_constexpr(
self.shared_destinations_per_cta
):
round_destination = destination + Int32(
destination_round * self.shared_destination_stride
)
global_tid = (
Int64(token) * self.tp_size + Int64(round_destination)
) * self.threads + Int64(tidx)
clear_idx = global_tid
if round_destination < Int32(
self.tp_size
) and dirty_num_stages > Uint32(0):
while clear_idx < clear_fragments:
clear_ptr = cute.make_ptr(
BFloat16,
(
shared_workspace.iterator
+ dirty_elements
+ clear_idx * VEC_BF16
).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
store_lamport_sentinel_128(clear_ptr)
clear_idx = clear_idx + total_threads
if round_destination == self.rank:
vector = tidx
while vector < self.shard_vectors:
rank_words = cute.make_rmem_tensor(
cute.make_layout((self.tp_size, 4), stride=(4, 1)),
Uint32,
)
valid = False
while not valid:
valid = True
for source_rank in cutlass.range_constexpr(self.tp_size):
remote_element = current_elements + (
(Int64(token) * self.tp_size + source_rank)
* self.shard_dim
+ Int64(vector) * VEC_BF16
)
remote_ptr = cute.make_ptr(
BFloat16,
(
shared_workspace.iterator + remote_element
).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
remote = load_global_u32x4(remote_ptr, volatile=True)
for word in cutlass.range_constexpr(4):
rank_words[source_rank, word] = remote[word]
valid = valid & (not fragment_is_dirty(remote))
accum = cute.make_rmem_tensor(
cute.make_layout((VEC_BF16,)), Float32
)
for element in cutlass.range_constexpr(VEC_BF16):
accum[element] = Float32(0.0)
for source_rank in cutlass.range_constexpr(self.tp_size):
values = packed_u32x4_to_bf16x8(
rank_words[source_rank, None].load()
).to(Float32)
for element in cutlass.range_constexpr(VEC_BF16):
accum[element] = accum[element] + values[element]
result = accum.load().to(BFloat16)
output_element = (
Int64(token) * self.hidden_dim
+ self.rank * self.shard_dim
+ Int64(vector) * VEC_BF16
)
store_global_u32x4(
Int64((shared_output.iterator + output_element).toint()),
bf16x8_to_packed_u32x4(result),
volatile=False,
)
vector = vector + self.threads
cute.arch.barrier()
if (
token_cta == 0
and token + self.token_ctas >= m
and shared_group == 0
and cluster_rank == 0
and tidx == 0
):
access_counter = shared_flags.iterator + 8
arrived = load_volatile_u32(access_counter)
target = Uint32(m) * Uint32(self.shared_roles)
while arrived < target:
arrived = load_volatile_u32(access_counter)
next_index = (current_index + Uint32(1)) % Uint32(NUM_LAMPORT_BUFFERS)
actual_bytes = Uint32(m) * Uint32(self.tp_size * self.shard_dim * 2)
cute.arch.store((shared_flags.iterator + 0).llvm_ptr, next_index)
cute.arch.store((shared_flags.iterator + 1).llvm_ptr, current_index)
cute.arch.store(
(shared_flags.iterator + 2).llvm_ptr,
bytes_per_buffer,
)
cute.arch.store((shared_flags.iterator + 3).llvm_ptr, Uint32(1))
cute.arch.store((shared_flags.iterator + 4).llvm_ptr, actual_bytes)
for index in cutlass.range_constexpr(5, 8):
cute.arch.store(
(shared_flags.iterator + index).llvm_ptr,
Uint32(0),
)
cute.arch.store(access_counter.llvm_ptr, Uint32(0))