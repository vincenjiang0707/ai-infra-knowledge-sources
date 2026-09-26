source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl/
lastmod: 2026-09-24

@cute.jit
def _load_q_and_rope(
positions: cute.Tensor,
q: cute.Tensor,
cos_sin_cache: cute.Tensor,
num_heads: cutlass.Constexpr,
coarsen: cutlass.Constexpr,
tb_size: cutlass.Constexpr,
subwarp_size: cutlass.Constexpr,
threads_per_token: cutlass.Constexpr,
nope_dim: cutlass.Constexpr,
rope_dim: cutlass.Constexpr,
cos_sin_dtype: cutlass.Constexpr,
):
"""Compute thread indices, load Q (BF16), and apply interleaved RoPE.
Returns a tuple
(q_bf16x2, tid, global_tid, sublane, token_id, head_tile_id,
head_start, in_bounds, num_token_heads)
where ``q_bf16x2`` is a (coarsen, 8) rmem tile of Uint32 packed
bf16x2 pairs covering the 16 BF16 lanes owned by this thread for
each of ``coarsen`` heads. RoPE is applied in place to the
trailing ``rope_dim`` lanes; the leading nope lanes pass through.
"""
block_id, _, _ = cute.arch.block_idx()
tid, _, _ = cute.arch.thread_idx()
num_tokens = q.shape[0]
num_token_heads = num_tokens * num_heads
global_tid = block_id * tb_size + tid
global_subwarp_id = global_tid // subwarp_size
sublane = tid % subwarp_size
token_id = global_subwarp_id // (num_heads // coarsen)
head_tile_id = global_subwarp_id % (num_heads // coarsen)
head_start = head_tile_id * coarsen
# NOTE: token_id may exceed bounds, hence we need to add load/store guards
# we can't do early exit because CuteDSL doesn't support it. and we also need
# all threads in a warp to be active since we utilize warp shuffle later.
# must_in_bounds is constexpr, True when a token spans a whole number of
# threadblocks. Then num_tokens * threads_per_token is always a multiple of
# tb_size, so the trailing block never straddles num_tokens and the compiler
# removes the bounds check. Otherwise the guard has to stay: e.g. 32 heads
# with coarsen=4 needs 64 threads per token, so an odd num_tokens leaves half
# of the last block addressing token num_tokens.
must_in_bounds = cutlass.const_expr(threads_per_token % tb_size == 0)
in_bounds = must_in_bounds or (token_id < num_tokens)
cp_op = cute.nvgpu.CopyUniversalOp()
_layout = cute.make_layout((coarsen, 8), stride=(8, 1))
q_bf16x2 = cute.make_rmem_tensor(_layout, Uint32)
if in_bounds:
# we can't do cute.copy() on the whole 2D tile directly because
# cute.copy() wants the 1st mode to be covered by the copy atom,
# and other modes as for loop. there is no fast way to
# "transpose" the tensor view.
q_tile = cute.local_tile(
q[token_id, None, None],
tiler=(coarsen, 16),
coord=(head_tile_id, sublane),
)
cp_u32x8 = cute.make_copy_atom(cp_op, Uint32, num_bits_per_copy=256)
for i in cutlass.range_constexpr(coarsen):
src = cute.recast_tensor(q_tile[i, None], Uint32)
cute.copy(cp_u32x8, src, q_bf16x2[i, None])
# RoPE applies only to the trailing rope_dim values. We keep the rounded
# BF16 result in q_bits so the later amax and quantization see BF16.
# cos_sin_cache layout: [max_pos, rope_dim]
if in_bounds and sublane * 16 >= nope_dim:
cos_vals = cute.make_rmem_tensor((8,), Float32)
sin_vals = cute.make_rmem_tensor((8,), Float32)
pos = positions[token_id]
# select 8 elems from cos and sin
cos_id = sublane - nope_dim // 16
sin_id = cos_id + rope_dim // 16
cos_src = cute.local_tile(cos_sin_cache[pos, None], tiler=(8,), coord=(cos_id,))
sin_src = cute.local_tile(cos_sin_cache[pos, None], tiler=(8,), coord=(sin_id,))
cp_f32x8 = cute.make_copy_atom(cp_op, Float32, num_bits_per_copy=256)
cp_u32x4 = cute.make_copy_atom(cp_op, Uint32, num_bits_per_copy=128)
if const_expr(cos_sin_dtype is Float32):
cute.copy(cp_f32x8, cos_src, cos_vals)
cute.copy(cp_f32x8, sin_src, sin_vals)
else:
cos_bf16x2 = cute.make_rmem_tensor((4,), Uint32)
sin_bf16x2 = cute.make_rmem_tensor((4,), Uint32)
cute.copy(cp_u32x4, cute.recast_tensor(cos_src, Uint32), cos_bf16x2)
cute.copy(cp_u32x4, cute.recast_tensor(sin_src, Uint32), sin_bf16x2)
for i in cutlass.range_constexpr(4):
cos0, cos1 = cvt.bf16x2_to_fp32x2(cos_bf16x2[i])
sin0, sin1 = cvt.bf16x2_to_fp32x2(sin_bf16x2[i])
cos_vals[i * 2] = cos0
cos_vals[i * 2 + 1] = cos1
sin_vals[i * 2] = sin0
sin_vals[i * 2 + 1] = sin1
for i in cutlass.range_constexpr(coarsen):
for j in cutlass.range_constexpr(8):
q0, q1 = cvt.bf16x2_to_fp32x2(q_bf16x2[i, j])
rot0 = q0 * cos_vals[j] - q1 * sin_vals[j]
rot1 = q0 * sin_vals[j] + q1 * cos_vals[j]
# convert back to BF16 to match numerics
q_bf16x2[i, j] = cvt.fp32x2_to_bf16x2(rot0, rot1)
return (
q_bf16x2,
tid,
global_tid,
sublane,
token_id,
head_tile_id,
head_start,
in_bounds,
num_token_heads,
)