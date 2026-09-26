# [Issue #3164] [Question][Carver] TensorCorePolicy: tiles whose smem_cost × pipeline_stage exceeds smem_cap are pruned rather than downgraded, and the shared.dyn fallback in _assign_block_size looks unreachable

source: https://github.com/tile-ai/tilelang/issues/3164
state: open | updated: 2026-09-04T06:09:06Z
labels: question

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### Questions

Two related observations in `tilelang/carver/roller/policy/` (line numbers identical on
`v0.1.13` and `main` @ `73bbff58`):

1. `TensorCorePolicy.infer_node_smem_usage` multiplies the shared-memory estimate by
   `self.pipeline_stage` (`tensorcore.py:83`). `DefaultPolicy.compute_tile_dict` then marks
   the tile invalid as soon as `td.smem_cost > self.arch.smem_cap` (`default.py:558-559`),
   and invalid tiles are filtered out of the search (`default.py:119`, `:132`). So a tile
   that would fit with `pipeline_stage = 1` but not with the arch-fixed `pipeline_stage = 2`
   is dropped entirely instead of being kept with a lower stage count. Is this pruning
   intended, or would a capacity-driven stage fallback (`max S s.t. S × smem_tile ≤ smem_cap`)
   be welcome? It mainly affects large tiles (e.g. fp16 128x256x32 at 2 stages is close to
   the 48 KB default `smem_cap`).

2. `_assign_block_size` (`tensorcore.py:328-333`) has a branch
   `if td.smem_cost > self.arch.smem_cap: shared_scope = "shared.dyn"`. Given (1), a tile
   reaching this point has already passed the same check, so the branch appears dead. It is
   then followed by an unconditional `codegen_dict.shared_scope = "shared.dyn"` (comment: a
   dummy to be removed), which also makes the earlier conditional assignment for
   `out_dtype == float32` (`:324`) dead. Is the unconditional `shared.dyn` meant to stay?

Asking before proposing a change: a stage fallback would touch the same lines, and the
answer to (2) decides whether it should also clean up the dead branches.

## 评论 (1)

### KellyFrog · 2026-09-04

Hi! Thanks for your question.

For question (1), I think it is the expected behavior as tilelang expect users to have knowledge of what they are actually doing. Allowing auto-fallbacks may silently change the user's expected semantics. So it may be wise to raise an error when arguments given by users do no fit hard constrains.

For question (2), it seems you are right. We will work on that.

However, these issues are not very urgent. Enhancements are welcomed, but this is not our top priority.

Best regaurds.
