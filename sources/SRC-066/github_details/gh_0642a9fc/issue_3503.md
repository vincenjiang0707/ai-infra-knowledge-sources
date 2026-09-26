# [Issue #3503] Fused fprop scale/bias iterator advances without the split-k factor and drifts from activation channels

source: https://github.com/NVIDIA/cutlass/issues/3503
state: open | updated: 2026-09-18T08:43:03Z
labels: CUTLASS C++

## 正文

### Description

In the fused (scale/bias) fprop mainloop, the scale/bias vector iterator and the activation/filter iterators disagree on the per-R*S-cycle channel stride when `split_k_slices > 1`, so scale/bias drift to the wrong channel blocks.

- Activation iterator on gemm-k wrap (include/cutlass/conv/threadblock/conv2d_fprop_activation_tile_access_iterator_analytic.h ~line 216, `_optimized` analogue ~314): `filter_c_ += Shape::kColumn * problem_size_.split_k_slices;`
- Scale/bias iterator on the same wrap (include/cutlass/conv/threadblock/predicated_scale_bias_vector_access_iterator.h:247-262): calls `add_tile_offset(TensorCoord(1, 0))`, which advances by a single `ThreadblockShape::kContiguous`, with no split-k factor.

Both start consistently at channel `threadblock_tile_idx.k() * kK` (implicit_gemm_convolution_fusion.h ~296-337), so the divergence accumulates once the loop wraps past R*S. With interleaved slice partitioning, each additional R*S cycle applies bias/scale from one kK-block earlier than the channels the activations actually carry. This needs `split_k_slices > 1` and more than one C-channel block per slice (`ceil(ceil(C/S)/kK) >= 2`) to appear, e.g. split_k_slices=4, C=256, ThreadblockShape::kK=32, R*S>=2: from the second cycle on, bias[64+j*32] is applied where the activations come from channels 192+. The result is silent wrong numerics, not an OOB.

The same pattern exists in the conv3d fusion headers (conv3d_fprop_activation_tile_access_iterator_analytic/_optimized vs the shared scale/bias iterator). Wgrad fusion is unaffected: it loads scale/bias once, with no per-tile advance.

The device layer explicitly supports split-k for fused fprop (workspace handling in include/cutlass/conv/device/implicit_gemm_convolution_fusion.h ~148-175), so the combination is reachable through the public API.

This finding is from static verification of the two advance paths; I have not built an end-to-end failing kernel, but the stride mismatch is exactly the missing `split_k_slices` factor and the start offsets agree.

### Suggested fix

Multiply the scale/bias iterator's wrap stride by `problem_size.split_k_slices` in `advance()`, mirroring the activation iterators.


## 评论 (1)

### 0z5a · 2026-09-18

I would like to take this if it is still available.
