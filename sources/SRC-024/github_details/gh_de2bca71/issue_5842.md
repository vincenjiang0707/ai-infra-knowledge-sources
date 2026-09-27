# [Issue #5842] [HIP][CK] Add Relu2 (Squared ReLU) activation support to CK-Tile fused MoE GEMM

source: https://github.com/ROCm/aiter/issues/5842
state: open | updated: 2026-09-25T09:06:52Z
labels: 

## 正文

## Summary
Add support for the Relu2 (Squared ReLU, `relu(x)^2`) activation to the CK-Tile 2-stage fused MoE GEMM path, alongside the existing Silu/Swiglu activations.

## Root cause

NemotronH's MoE layers use Squared ReLU (relu(x)^2) as their activation function. Tier 1 (https://github.com/ROCm/aiter/pull/5689) added a standalone relu2 kernel so aiter could compute this activation directly instead of falling back to eager PyTorch, but that PR only covered the simple elementwise case, not the fused MoE GEMM path.

The fused MoE GEMM path (csrc/ck_tile_gemm_moe_2stages/) didn't support relu2 at all.

## PR

This PR in progress to support the ReLU2 activation to the CK-Tile fused MoE GEMM path

https://github.com/ROCm/aiter/pull/5708/




## 评论 (1)

### shantipriya-amd · 2026-09-25

PR in progress
