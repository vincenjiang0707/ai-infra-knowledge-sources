source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/ops/gluon/rel_mha_decode_gfx950/
lastmod: 2026-09-23

Pick num_kv_splits to balance occupancy against reduce overhead.

The launch grid is (batch * num_kv_heads * num_groups) * num_kv_splits work-groups. Too few splits under-fill the machine at low batch; too many leave each split with a handful of pages, so the reduce kernel dominates.

Return the smaller of two candidate counts: splits_for_occupancy (enough to fill ~wave_target waves of CUs) and splits_for_pages (~min_pages_per_split pages per split), with the pages candidate clamped to [min_page_splits, max_page_splits] so a short context still splits without launching empty work and a long one does not over-split where reduce cost outgrows the decode win.

## Source code in `vllm/models/inkling/amd/ops/gluon/rel_mha_decode_gfx950.py`


| def _select_num_kv_splits(
*,
batch: int,
num_kv_heads: int,
num_groups: int,
num_pages: int,
sm_count: int,
) -> int:
"""Pick num_kv_splits to balance occupancy against reduce overhead.
The launch grid is (batch * num_kv_heads * num_groups) * num_kv_splits
work-groups. Too few splits under-fill the machine at low batch; too many
leave each split with a handful of pages, so the reduce kernel dominates.
Return the smaller of two candidate counts: splits_for_occupancy (enough to
fill ~wave_target waves of CUs) and splits_for_pages (~min_pages_per_split
pages per split), with the pages candidate clamped to [min_page_splits,
max_page_splits] so a short context still splits without launching empty work
and a long one does not over-split where reduce cost outgrows the decode win.
"""
wave_target = 2
min_pages_per_split = 2
min_page_splits = 8
max_page_splits = 32
base_ctas = batch * num_kv_heads * num_groups
target_ctas = sm_count * wave_target
splits_for_occupancy = (target_ctas + base_ctas - 1) // base_ctas
splits_for_pages = num_pages // min_pages_per_split
min_page_splits = min(min_page_splits, num_pages)
if splits_for_pages < min_page_splits:
splits_for_pages = min_page_splits
if splits_for_pages > max_page_splits:
splits_for_pages = max_page_splits
return min(splits_for_occupancy, splits_for_pages)
|