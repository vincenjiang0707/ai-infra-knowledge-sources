# [Issue #3494] Sm90VisitorImplBase fixed-size specializations advance workspace by raw sizes while get_workspace_size/initialize_workspace round to 16

source: https://github.com/NVIDIA/cutlass/issues/3494
state: open | updated: 2026-09-13T05:09:01Z
labels: CUTLASS C++

## 正文

### Description

In `include/cutlass/epilogue/fusion/sm90_visitor_tma_warpspecialized.hpp`, the hand-written `Sm90VisitorImplBase` specializations for 2, 3, and 4 ops advance per-op workspace offsets by the **raw** `Op::get_workspace_size(...)` value in `to_underlying_arguments`, while their own `get_workspace_size` and `initialize_workspace` round every op's size up to `MinWorkspaceAlignment` (16) before advancing. The generic variadic base rounds consistently in all three functions; only these specializations diverge.

- 2-op specialization: lines 995-997 (`op_1_workspace = op_0_workspace + op_0_workspace_size`, no rounding), vs rounding in 1013-1022 and 1030-1041
- 3-op specialization: lines 1093-1097
- 4-op specialization: lines 1210-1216

### Consequence

If an earlier op's workspace size is not a multiple of 16 and any later op has nonzero workspace, `Params` produced by `to_underlying_arguments` point that later op at `[ws+raw, ws+raw+size)` while `initialize_workspace` initialized `[ws+round16(raw), ...)`. On device the later op then reads/writes a region that was never initialized and partially overlaps the previous op's workspace.

Today only `Sm90RowReduction` / `Sm90ColReduction` allocate workspace among stock ops, and their trailing tile-counter block (`ceil_div(N, tile_N) * sizeof(int)`, line 1156 / `ceil_div(M, tile_M) * sizeof(int)`, line 1745) is not always a 16-multiple: e.g. N=600 with tile_N=128 gives ceil_div=5 -> 20 bytes. So the divergence is reachable whenever such a reduction sits at position < last in a <=4-op EVT tree followed by another workspace consumer. I have not constructed an end-to-end failing fusion; this is a static analysis of the offset bookkeeping, filed because the inconsistency is objective.

### Suggested fix

Round each op's size to `MinWorkspaceAlignment` when advancing offsets in the three `to_underlying_arguments` overloads, matching the variadic base (lines 504-507). Alternatively delegate the fixed-size specializations to the same shared helper so the two paths cannot drift again.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3631.
