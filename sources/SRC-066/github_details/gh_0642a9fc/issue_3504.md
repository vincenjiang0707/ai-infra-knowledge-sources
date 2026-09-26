# [Issue #3504] Five conv filter tile access iterators invert the byte scaling in add_pointer_offset (8/sizeof_bits instead of sizeof_bits/8)

source: https://github.com/NVIDIA/cutlass/issues/3504
state: open | updated: 2026-09-13T04:05:11Z
labels: CUTLASS C++

## 正文

### Description

Five conv filter tile access iterators invert the byte scaling in `add_pointer_offset`: they compute `pointer_offset * 8 / sizeof_bits<Element>::value` where every sibling iterator uses `pointer_offset * sizeof_bits<Element>::value / 8`.

Affected sites:

- include/cutlass/conv/threadblock/conv2d_fprop_filter_tile_access_iterator_analytic.h:194
- include/cutlass/conv/threadblock/conv2d_fprop_filter_tile_access_iterator_fixed_channels.h:165
- include/cutlass/conv/threadblock/conv2d_fprop_filter_tile_access_iterator_few_channels.h:167
- include/cutlass/conv/threadblock/conv3d_fprop_filter_tile_access_iterator_analytic.h:160
- include/cutlass/conv/threadblock/depthwise_fprop_filter_tile_access_iterator_direct_conv_optimized.h:162

For fp32 (32 bits) the inverted form is a silent no-op multiplier of 8/32 vs the correct 4; for fp16 it scales offsets by 1/2 instead of 2. All 30+ sibling iterators (activation/dgrad/wgrad variants) use the correct form, e.g. conv2d_dgrad_filter_tile_access_iterator_analytic.h:187.

Currently latent: no in-tree caller passes nonzero element-granularity pointer offsets into these mainloop A/B iterators (kernels call `add_pointer_offset` on the epilogue D iterator only). The defect surfaces for any external user advancing these public iterators manually.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3623.
