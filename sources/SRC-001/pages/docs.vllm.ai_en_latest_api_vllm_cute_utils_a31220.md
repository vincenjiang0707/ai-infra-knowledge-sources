source: https://docs.vllm.ai/en/latest/api/vllm/cute_utils/
lastmod: 2026-09-24

def simple_tma_copy(atom, src, dst, mbar=None, cache_policy=None):
"""A simple helper that wraps group_modes() and tma_partition()
NOTE: this should be called WITHOUT cute.elect_one()
"""
if isinstance(atom.op, cpasync.CopyBulkTensorTileG2SOp):
gmem = src
smem = dst
elif isinstance(atom.op, cpasync.CopyBulkTensorTileS2GOp):
smem = src
gmem = dst
else:
raise ValueError
s_part, g_part = cpasync.tma_partition(
atom,
0,
cute.make_layout(1),
cute.group_modes(smem, 0),
cute.group_modes(gmem, 0),
)
if isinstance(atom.op, cpasync.CopyBulkTensorTileG2SOp):
cute.copy(atom, g_part, s_part, tma_bar_ptr=mbar, cache_policy=cache_policy)
elif isinstance(atom.op, cpasync.CopyBulkTensorTileS2GOp):
cute.copy(atom, s_part, g_part, cache_policy=cache_policy)
else:
raise ValueError