source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_gemm/
lastmod: 2026-09-23

class FusedAddMulticastGemm:
"""Persistent Blackwell GEMM with a shared-add epilogue.
B priming may overlap the producer collective. The PDL wait before A
loading orders both inputs before the shared-add epilogue.
"""
def __init__(
self,
mma_tiler_mn: tuple[int, int],
cluster_shape_mn: tuple[int, int],
b_prime_stages: int = 2,
):
self.acc_dtype = cutlass.Float32
self.cluster_shape_mn = cluster_shape_mn
self.mma_tiler = (*mma_tiler_mn, 1)
# B primes the combined A+B pipeline before the PDL wait.
self.b_prime_stages = b_prime_stages
self.cta_group = tcgen05.CtaGroup.ONE
self.epilogue_warp_id = (0, 1, 2, 3)
self.mma_warp_id = 4
self.tma_warp_id = 5
self.threads_per_cta = 32 * len(
(self.mma_warp_id, self.tma_warp_id, *self.epilogue_warp_id)
)
self.epilog_sync_bar_id = 1
self.tmem_alloc_sync_bar_id = 2
def _create_tiled_mma(self):
return utils.sm100.make_trivial_tiled_mma(
self.a_dtype,
self.a_major_mode,
self.b_major_mode,
self.acc_dtype,
self.cta_group,
self.mma_tiler[:2],
)
def _setup_attributes(self):
"""Derive layouts and stage counts from the compiled tensor shapes."""
tiled_mma = self._create_tiled_mma()
mma_inst_shape_k = cute.size(tiled_mma.shape_mnk, mode=[2])
mma_inst_tile_k = 4
self.mma_tiler = (
self.mma_tiler[0],
self.mma_tiler[1],
mma_inst_shape_k * mma_inst_tile_k,
)
self.cta_tile_shape_mnk = (
self.mma_tiler[0] // cute.size(tiled_mma.thr_id.shape),
self.mma_tiler[1],
self.mma_tiler[2],
)
self.cluster_layout_vmnk = cute.tiled_divide(
cute.make_layout((*self.cluster_shape_mn, 1)),
(tiled_mma.thr_id.shape,),
)
self.num_mcast_ctas_a = cute.size(self.cluster_layout_vmnk.shape[2])
self.num_mcast_ctas_b = cute.size(self.cluster_layout_vmnk.shape[1])
self.is_a_mcast = self.num_mcast_ctas_a > 1
self.is_b_mcast = self.num_mcast_ctas_b > 1
self.epi_tile = utils.sm100.compute_epilogue_tile_shape(
self.cta_tile_shape_mnk,
False,
self.c_layout,
self.c_dtype,
)
c_smem_layout = utils.sm100.make_smem_layout_epi(
self.c_dtype, self.c_layout, self.epi_tile, 1
)
self.num_acc_stage, self.num_ab_stage, self.num_c_stage = _compute_stages(
tiled_mma,
self.mma_tiler,
self.a_dtype,
self.b_dtype,
self.c_dtype,
utils.get_smem_capacity_in_bytes(),
c_smem_layout,
)
self.a_smem_layout_staged = utils.sm100.make_smem_layout_a(
tiled_mma, self.mma_tiler, self.a_dtype, self.num_ab_stage
)
self.b_smem_layout_staged = utils.sm100.make_smem_layout_b(
tiled_mma, self.mma_tiler, self.b_dtype, self.num_ab_stage
)
self.c_smem_layout_staged = utils.sm100.make_smem_layout_epi(
self.c_dtype, self.c_layout, self.epi_tile, self.num_c_stage
)
self.num_tmem_alloc_cols = self._compute_num_tmem_alloc_cols(
tiled_mma, self.mma_tiler, self.num_acc_stage, "sm_100"
)
@cute.jit
def __call__(
self,
a: cute.Tensor,
b: cute.Tensor,
c: cute.Tensor,
shared_shard: cute.Tensor,
c_multicast_i64: cutlass.Int64,
max_active_clusters: cutlass.Constexpr,
stream: cuda.CUstream,
):
"""Launch the persistent GEMM."""
# Preserve C's logical strided layout but point the TMA descriptor at
# this rank's shard inside the LSA multicast mapping. One TMA store is
# therefore replicated into the same shard on all eight ranks.
c = cute.make_tensor(
cute.make_ptr(
c.element_type,
c_multicast_i64,
cute.AddressSpace.gmem,
assumed_align=16,
),
c.layout,
)
self.a_dtype: type[cutlass.Numeric] = a.element_type
self.b_dtype: type[cutlass.Numeric] = b.element_type
self.c_dtype: type[cutlass.Numeric] = c.element_type
self.a_major_mode = utils.LayoutEnum.from_tensor(a).mma_major_mode()
self.b_major_mode = utils.LayoutEnum.from_tensor(b).mma_major_mode()
self.c_layout = utils.LayoutEnum.from_tensor(c)
if cutlass.const_expr(self.a_dtype != self.b_dtype):
raise TypeError(f"Type must match: {self.a_dtype} != {self.b_dtype}")
tiled_mma = self._create_tiled_mma()
self._setup_attributes()
if cutlass.const_expr(self.b_prime_stages > self.num_ab_stage):
raise ValueError(
"b_prime_stages exceeds the compiled A/B pipeline stage count"
)
atom_thr_size = cute.size(tiled_mma.thr_id.shape)
a_op = utils.sm100.cluster_shape_to_tma_atom_A(
self.cluster_shape_mn, tiled_mma.thr_id
)
a_smem_layout = cute.slice_(self.a_smem_layout_staged, (None, None, None, 0))
tma_atom_a, tma_tensor_a = cute.nvgpu.make_tiled_tma_atom_A(
a_op,
a,
a_smem_layout,
self.mma_tiler,
tiled_mma,
self.cluster_layout_vmnk.shape,
internal_type=(
cutlass.TFloat32 if a.element_type is cutlass.Float32 else None
),
)
b_op = utils.sm100.cluster_shape_to_tma_atom_B(
self.cluster_shape_mn, tiled_mma.thr_id
)
b_smem_layout = cute.slice_(self.b_smem_layout_staged, (None, None, None, 0))
tma_atom_b, tma_tensor_b = cute.nvgpu.make_tiled_tma_atom_B(
b_op,
b,
b_smem_layout,
self.mma_tiler,
tiled_mma,
self.cluster_layout_vmnk.shape,
internal_type=(
cutlass.TFloat32 if b.element_type is cutlass.Float32 else None
),
)
a_copy_size = cute.size_in_bytes(self.a_dtype, a_smem_layout)
b_copy_size = cute.size_in_bytes(self.b_dtype, b_smem_layout)
self.num_tma_load_bytes = (a_copy_size + b_copy_size) * atom_thr_size
epi_smem_layout = cute.select(self.c_smem_layout_staged, mode=[0, 1])
tma_atom_c, tma_tensor_c = cpasync.make_tiled_tma_atom(
cpasync.CopyBulkTensorTileS2GOp(), c, epi_smem_layout, self.epi_tile
)
tile_sched_params, grid = self._compute_grid(
c, self.cta_tile_shape_mnk, self.cluster_shape_mn, max_active_clusters
)
self.kernel(
tiled_mma,
tma_atom_a,
tma_tensor_a,
tma_atom_b,
tma_tensor_b,
tma_atom_c,
tma_tensor_c,
self.cluster_layout_vmnk,
self.a_smem_layout_staged,
self.b_smem_layout_staged,
self.c_smem_layout_staged,
self.epi_tile,
tile_sched_params,
shared_shard,
).launch(
grid=grid,
block=[self.threads_per_cta, 1, 1],
cluster=(*self.cluster_shape_mn, 1),
stream=stream,
use_pdl=True,
)
return
@cute.kernel
def kernel(
self,
tiled_mma: cute.TiledMma,
tma_atom_a: cute.CopyAtom,
mA_mkl: cute.Tensor,
tma_atom_b: cute.CopyAtom,
mB_nkl: cute.Tensor,
tma_atom_c: cute.CopyAtom,
mC_mnl: cute.Tensor,
cluster_layout_vmnk: cute.Layout,
a_smem_layout_staged: cute.ComposedLayout,
b_smem_layout_staged: cute.ComposedLayout,
c_smem_layout_staged: cute.Layout | cute.ComposedLayout,
epi_tile: cute.Tile,
tile_sched_params: utils.PersistentTileSchedulerParams,
shared_shard: cute.Tensor,
):
self._gemm_device(
tiled_mma,
tma_atom_a,
mA_mkl,
tma_atom_b,
mB_nkl,
tma_atom_c,
mC_mnl,
cluster_layout_vmnk,
a_smem_layout_staged,
b_smem_layout_staged,
c_smem_layout_staged,
epi_tile,
tile_sched_params,
shared_shard,
)
@cute.jit
def _gemm_device(
self,
tiled_mma: cute.TiledMma,
tma_atom_a: cute.CopyAtom,
mA_mkl: cute.Tensor,
tma_atom_b: cute.CopyAtom,
mB_nkl: cute.Tensor,
tma_atom_c: cute.CopyAtom,
mC_mnl: cute.Tensor,
cluster_layout_vmnk: cute.Layout,
a_smem_layout_staged: cute.ComposedLayout,
b_smem_layout_staged: cute.ComposedLayout,
c_smem_layout_staged: cute.Layout | cute.ComposedLayout,
epi_tile: cute.Tile,
tile_sched_params: utils.PersistentTileSchedulerParams,
shared_shard: cute.Tensor,
):
warp_idx = cute.arch.warp_idx()
warp_idx = cute.arch.make_warp_uniform(warp_idx)
if warp_idx == self.tma_warp_id:
cpasync.prefetch_descriptor(tma_atom_a)
cpasync.prefetch_descriptor(tma_atom_b)
cpasync.prefetch_descriptor(tma_atom_c)
bidx, bidy, bidz = cute.arch.block_idx()
mma_tile_coord_v = bidx % cute.size(tiled_mma.thr_id.shape)
is_leader_cta = mma_tile_coord_v == 0
cta_rank_in_cluster = cute.arch.make_warp_uniform(
cute.arch.block_idx_in_cluster()
)
block_in_cluster_coord_vmnk = cluster_layout_vmnk.get_flat_coord(
cta_rank_in_cluster
)
tidx, _, _ = cute.arch.thread_idx()
@cute.struct
class SharedStorage:
ab_full_mbar_ptr: cute.struct.MemRange[cutlass.Int64, self.num_ab_stage * 2]
acc_full_mbar_ptr: cute.struct.MemRange[
cutlass.Int64, self.num_acc_stage * 2
]
tmem_dealloc_mbar_ptr: cutlass.Int64
tmem_holding_buf: cutlass.Int32
smem = utils.SmemAllocator()
storage = smem.allocate(SharedStorage)
ab_pipeline_producer_group = pipeline.CooperativeGroup(pipeline.Agent.Thread)
num_tma_producer = self.num_mcast_ctas_a + self.num_mcast_ctas_b - 1
ab_pipeline_consumer_group = pipeline.CooperativeGroup(
pipeline.Agent.Thread, num_tma_producer
)
ab_pipeline = pipeline.PipelineTmaUmma.create(
barrier_storage=storage.ab_full_mbar_ptr.data_ptr(),
num_stages=self.num_ab_stage,
producer_group=ab_pipeline_producer_group,
consumer_group=ab_pipeline_consumer_group,
tx_count=self.num_tma_load_bytes,
cta_layout_vmnk=cluster_layout_vmnk,
defer_sync=True,
)
ab_producer, ab_consumer = ab_pipeline.make_participants()
acc_pipeline_producer_group = pipeline.CooperativeGroup(pipeline.Agent.Thread)
num_acc_consumer_threads = len(self.epilogue_warp_id)
acc_pipeline_consumer_group = pipeline.CooperativeGroup(
pipeline.Agent.Thread, num_acc_consumer_threads
)
acc_pipeline = pipeline.PipelineUmmaAsync.create(
barrier_storage=storage.acc_full_mbar_ptr.data_ptr(),
num_stages=self.num_acc_stage,
producer_group=acc_pipeline_producer_group,
consumer_group=acc_pipeline_consumer_group,
cta_layout_vmnk=cluster_layout_vmnk,
defer_sync=True,
)
tmem_alloc_barrier = pipeline.NamedBarrier(
barrier_id=self.tmem_alloc_sync_bar_id,
num_threads=32 * len((self.mma_warp_id, *self.epilogue_warp_id)),
)
tmem = utils.TmemAllocator(
storage.tmem_holding_buf,
barrier_for_retrieve=tmem_alloc_barrier,
allocator_warp_id=self.epilogue_warp_id[0],
is_two_cta=False,
two_cta_tmem_dealloc_mbar_ptr=storage.tmem_dealloc_mbar_ptr,
)
pipeline_init_arrive(cluster_shape_mn=cluster_layout_vmnk, is_relaxed=True)
sA = smem.allocate_tensor(
element_type=self.a_dtype,
layout=a_smem_layout_staged.outer,
byte_alignment=128,
swizzle=a_smem_layout_staged.inner,
)
sB = smem.allocate_tensor(
element_type=self.b_dtype,
layout=b_smem_layout_staged.outer,
byte_alignment=128,
swizzle=b_smem_layout_staged.inner,
)
a_full_mcast_mask = None
b_full_mcast_mask = None
if cutlass.const_expr(self.is_a_mcast or self.is_b_mcast):
a_full_mcast_mask = cpasync.create_tma_multicast_mask(
cluster_layout_vmnk, block_in_cluster_coord_vmnk, mcast_mode=2
)
b_full_mcast_mask = cpasync.create_tma_multicast_mask(
cluster_layout_vmnk, block_in_cluster_coord_vmnk, mcast_mode=1
)
gA_mkl = cute.local_tile(
mA_mkl, cute.slice_(self.mma_tiler, (None, 0, None)), (None, None, None)
)
gB_nkl = cute.local_tile(
mB_nkl, cute.slice_(self.mma_tiler, (0, None, None)), (None, None, None)
)
gC_mnl = cute.local_tile(
mC_mnl, cute.slice_(self.mma_tiler, (None, None, 0)), (None, None, None)
)
# Shared shard is physically [M, shard_dim]. Give it the same logical MNL
# view as C so its epilogue partition is coordinate-identical.
mShared_mnl = cute.make_tensor(
shared_shard.iterator,
cute.append(shared_shard.layout, cute.make_layout((1,), stride=(0,))),
)
gShared_mnl = cute.local_tile(
mShared_mnl,
cute.slice_(self.mma_tiler, (None, None, 0)),
(None, None, None),
)
k_tile_cnt = cute.size(gA_mkl, mode=[3])
thr_mma = tiled_mma.get_slice(mma_tile_coord_v)
tCgA = thr_mma.partition_A(gA_mkl)
tCgB = thr_mma.partition_B(gB_nkl)
tCgC = thr_mma.partition_C(gC_mnl)
tCgShared = thr_mma.partition_C(gShared_mnl)
# Predicate the partial M tile when M is smaller than the MMA tile.
idC = cute.make_identity_tensor(mC_mnl.shape)
cC_mnl = cute.local_tile(
idC, cute.slice_(self.mma_tiler, (None, None, 0)), (None, None, None)
)
tCcC = thr_mma.partition_C(cC_mnl)
a_cta_layout = cute.make_layout(
cute.slice_(cluster_layout_vmnk, (0, 0, None, 0)).shape
)
tAsA, tAgA = cpasync.tma_partition(
tma_atom_a,
block_in_cluster_coord_vmnk[2],
a_cta_layout,
cute.group_modes(sA, 0, 3),
cute.group_modes(tCgA, 0, 3),
)
b_cta_layout = cute.make_layout(
cute.slice_(cluster_layout_vmnk, (0, None, 0, 0)).shape
)
tBsB, tBgB = cpasync.tma_partition(
tma_atom_b,
block_in_cluster_coord_vmnk[1],
b_cta_layout,
cute.group_modes(sB, 0, 3),
cute.group_modes(tCgB, 0, 3),
)
tCrA = tiled_mma.make_fragment_A(sA)
tCrB = tiled_mma.make_fragment_B(sB)
acc_shape = tiled_mma.partition_shape_C(self.mma_tiler[:2])
tCtAcc_fake = tiled_mma.make_fragment_C(
cute.append(acc_shape, self.num_acc_stage)
)
pipeline_init_wait(cluster_shape_mn=cluster_layout_vmnk)
gemm_grid_z = cute.arch.grid_dim()[2]
tile_sched = utils.StaticPersistentTileScheduler.create(
tile_sched_params,
cute.arch.block_idx(),
(
cute.arch.grid_dim()[0],
cute.arch.grid_dim()[1],
gemm_grid_z,
),
)
work_tile = tile_sched.initial_work_tile_info()
if warp_idx == self.tma_warp_id:
while work_tile.is_valid_tile:
cur_tile_coord = work_tile.tile_idx
mma_tile_coord_mnl = (
cur_tile_coord[0] // cute.size(tiled_mma.thr_id.shape),
cur_tile_coord[1],
cur_tile_coord[2],
)
tAgA_slice = tAgA[
(None, mma_tile_coord_mnl[0], None, mma_tile_coord_mnl[2])
]
tBgB_slice = tBgB[
(None, mma_tile_coord_mnl[1], None, mma_tile_coord_mnl[2])
]
# Prime a short prefix of the existing combined A+B ring with
# B only. Its barrier still expects A+B bytes, so the MMA
# consumer cannot observe a half-filled stage.
ab_producer.reset()
peek_ab_empty_status = ab_producer.try_acquire()
for k_tile in cutlass.range(0, self.b_prime_stages, 1, unroll=1):
handle = ab_producer.acquire_and_advance(peek_ab_empty_status)
cute.copy(
tma_atom_b,
tBgB_slice[(None, handle.count)],
tBsB[(None, handle.index)],
tma_bar_ptr=handle.barrier,
mcast_mask=b_full_mcast_mask,
)
peek_ab_empty_status = cutlass.Boolean(1)
if handle.count + 1 < self.b_prime_stages:
peek_ab_empty_status = ab_producer.try_acquire()
cute.arch.griddepcontrol_wait()
# Supply A to the very same stages after the producer AR has
# programmatically released this dependent kernel.
a_fill_state = pipeline.make_pipeline_state(
pipeline.PipelineUserType.Producer, self.num_ab_stage
)
for k_tile in cutlass.range(0, self.b_prime_stages, 1, unroll=1):
a_barrier = ab_pipeline.producer_get_barrier(a_fill_state)
cute.copy(
tma_atom_a,
tAgA_slice[(None, k_tile)],
tAsA[(None, a_fill_state.index)],
tma_bar_ptr=a_barrier,
mcast_mask=a_full_mcast_mask,
)
a_fill_state.advance()
peek_ab_empty_status = ab_producer.try_acquire()
for k_tile in cutlass.range(
self.b_prime_stages, k_tile_cnt, 1, unroll=1
):
handle = ab_producer.acquire_and_advance(peek_ab_empty_status)
cute.copy(
tma_atom_a,
tAgA_slice[(None, handle.count)],
tAsA[(None, handle.index)],
tma_bar_ptr=handle.barrier,
mcast_mask=a_full_mcast_mask,
)
cute.copy(
tma_atom_b,
tBgB_slice[(None, handle.count)],
tBsB[(None, handle.index)],
tma_bar_ptr=handle.barrier,
mcast_mask=b_full_mcast_mask,
)
peek_ab_empty_status = cutlass.Boolean(1)
if handle.count + 1 < k_tile_cnt:
peek_ab_empty_status = ab_producer.try_acquire()
tile_sched.advance_to_next_work()
work_tile = tile_sched.get_current_work()
ab_producer.tail()
if warp_idx == self.mma_warp_id:
tmem.wait_for_alloc()
tmem_ptr = tmem.retrieve_ptr(self.acc_dtype)
tCtAcc_base = cute.make_tensor(tmem_ptr, tCtAcc_fake.layout)
acc_producer_state = pipeline.make_pipeline_state(
pipeline.PipelineUserType.Producer, self.num_acc_stage
)
while work_tile.is_valid_tile:
cur_tile_coord = work_tile.tile_idx
mma_tile_coord_mnl = (
cur_tile_coord[0] // cute.size(tiled_mma.thr_id.shape),
cur_tile_coord[1],
cur_tile_coord[2],
)
tCtAcc = tCtAcc_base[(None, None, None, acc_producer_state.index)]
ab_consumer.reset()
peek_ab_full_status = cutlass.Boolean(1)
if is_leader_cta:
peek_ab_full_status = ab_consumer.try_wait()
if is_leader_cta:
acc_pipeline.producer_acquire(acc_producer_state)
tiled_mma.set(tcgen05.Field.ACCUMULATE, False)
for k_tile in range(k_tile_cnt):
if is_leader_cta:
handle = ab_consumer.wait_and_advance(peek_ab_full_status)
num_kblocks = cute.size(tCrA, mode=[2])
for kblk_idx in cutlass.range(num_kblocks, unroll_full=True):
kblk_crd = (None, None, kblk_idx, handle.index)
cute.gemm(
tiled_mma,
tCtAcc,
tCrA[kblk_crd],
tCrB[kblk_crd],
tCtAcc,
)
tiled_mma.set(tcgen05.Field.ACCUMULATE, True)
handle.release()
peek_ab_full_status = cutlass.Boolean(1)
if handle.count + 1 < k_tile_cnt:
peek_ab_full_status = ab_consumer.try_wait()
if is_leader_cta:
acc_pipeline.producer_commit(acc_producer_state)
acc_producer_state.advance()
tile_sched.advance_to_next_work()
work_tile = tile_sched.get_current_work()
acc_pipeline.producer_tail(acc_producer_state)
sC = smem.allocate_tensor(
element_type=self.c_dtype,
layout=c_smem_layout_staged.outer,
byte_alignment=128,
swizzle=c_smem_layout_staged.inner,
)
if warp_idx < self.mma_warp_id:
tmem.allocate(self.num_tmem_alloc_cols)
tmem.wait_for_alloc()
tmem_ptr = tmem.retrieve_ptr(self.acc_dtype)
tCtAcc_base = cute.make_tensor(tmem_ptr, tCtAcc_fake.layout)
acc_consumer_state = pipeline.make_pipeline_state(
pipeline.PipelineUserType.Consumer, self.num_acc_stage
)
c_producer_group = pipeline.CooperativeGroup(
pipeline.Agent.Thread,
32 * len(self.epilogue_warp_id),
)
c_pipeline = pipeline.PipelineTmaStore.create(
num_stages=self.num_c_stage, producer_group=c_producer_group
)
while work_tile.is_valid_tile:
cur_tile_coord = work_tile.tile_idx
mma_tile_coord_mnl = (
cur_tile_coord[0] // cute.size(tiled_mma.thr_id.shape),
cur_tile_coord[1],
cur_tile_coord[2],
)
tile_sched.advance_to_next_work()
work_tile = tile_sched.get_current_work()
num_tiles_executed = tile_sched.num_tiles_executed
acc_consumer_state = _epilogue_tma_store_add_shared(
self,
tidx,
warp_idx,
tma_atom_c,
tCtAcc_base,
sC,
tCgC,
tCgShared,
tCcC,
mC_mnl,
mShared_mnl,
epi_tile,
num_tiles_executed,
mma_tile_coord_mnl,
acc_consumer_state,
acc_pipeline,
c_pipeline,
)
c_pipeline.producer_tail()
tmem.relinquish_alloc_permit()
tmem.free(tmem_ptr)
# Allow the Lamport copy to become resident before this grid
# fully retires. Its griddepcontrol.wait still enforces complete
# producer-grid ordering before mailbox inspection.
cute.arch.griddepcontrol_launch_dependents()
@staticmethod
def _compute_grid(
c: cute.Tensor,
cta_tile_shape_mnk: tuple[int, int, int],
cluster_shape_mn: tuple[int, int],
max_active_clusters: cutlass.Constexpr,
) -> tuple[utils.PersistentTileSchedulerParams, tuple[int, int, int]]:
"""Build the static persistent schedule."""
c_shape = cute.slice_(cta_tile_shape_mnk, (None, None, 0))
gc = cute.zipped_divide(c, tiler=c_shape)
num_ctas_mnl = gc[(0, (None, None, None))].shape
cluster_shape_mnl = (*cluster_shape_mn, 1)
tile_sched_params = utils.PersistentTileSchedulerParams(
num_ctas_mnl, cluster_shape_mnl
)
grid = utils.StaticPersistentTileScheduler.get_grid_shape(
tile_sched_params, max_active_clusters
)
return tile_sched_params, grid
@staticmethod
def _compute_num_tmem_alloc_cols(
tiled_mma: cute.TiledMma,
mma_tiler: tuple[int, int, int],
num_acc_stage: int,
arch: str,
) -> int:
"""Return the required tensor-memory column count."""
acc_shape = tiled_mma.partition_shape_C(mma_tiler[:2])
tCtAcc_fake = tiled_mma.make_fragment_C(cute.append(acc_shape, num_acc_stage))
num_tmem_alloc_cols = utils.get_num_tmem_alloc_cols(tCtAcc_fake, arch=arch)
return num_tmem_alloc_cols