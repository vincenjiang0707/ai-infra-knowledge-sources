# [Issue #1818] Support rank-contiguous GB200 local groups in NIXL EP HT

source: https://github.com/ai-dynamo/nixl/issues/1818
state: open | updated: 2026-06-25T09:07:41Z
labels: NIXL EP

## 正文

# Design issue draft: Support rank-contiguous GB200 local groups in NIXL EP HT

## Problem

NIXL EP high-throughput mode currently assumes each CUDA-IPC/NVLink-local group contains 8 ranks:

```text
rdma_rank = rank / 8
nvl_rank  = rank % 8
```

That mapping is correct for 8-GPU-local deployments, but it is too rigid for GB200 deployments where each worker or pod exposes 4 CUDA-IPC-local GPUs. In those deployments, ranks `0..3` and `4..7` may belong to different workers, but the current mapping treats `0..7` as one local group and can try to use CUDA IPC across a worker boundary.

## Proposed change

Add an explicit `nvl_group_size` parameter to the EP `Buffer` API, defaulting to `8` for backward compatibility.

The high-throughput EP mapping becomes:

```text
rdma_rank = rank / nvl_group_size
nvl_rank  = rank % nvl_group_size
```

For GB200-style 4-GPU-local workers, users pass `nvl_group_size=4`. Ranks `0..3`, `4..7`, `8..11`, etc. are then treated as local CUDA-IPC groups, and inter-group traffic uses the existing EP RDMA/fabric path.

## Scope

- Preserve the default `nvl_group_size=8` behavior for existing users.
- Support equal-size, rank-contiguous groups where `nvl_group_size` divides the active rank count for multi-group HT.
- Keep `NUM_MAX_NVL_PEERS=8` as the fixed scratch-layout maximum while guarding active lanes with runtime group size.
- Add GB200-oriented validation coverage for `nvl_group_size=4` layouts.

## Non-goals

- This is not arbitrary topology discovery.
- This does not support non-contiguous scheduler placement.
- This does not introduce a rank-to-group mapping table.
- This does not move CUDA VMM helpers into shared utils.

## Validation plan

- Existing default `nvl_group_size=8` HT tests continue to pass.
- GB200-style `nvl_group_size=4` layouts pass for `2x4`, `3x4`, `4x4`, `5x4`, and `6x4`.
- `1x4` is documented as a boundary case because there is no remote RDMA group to exercise.
- Invalid group sizes fail early: zero, negative, greater than 8, non-divisors of 8, and incompatible multi-group rank counts.

## Proposed PR stack

1. Prepare the EP API and validation for configurable local group size.
2. Update the HT runtime mapping and active-lane guards.
3. Add GB200 validation wrapper and documentation.


## 评论 (1)

### ebarilanM · 2026-06-24

Thanks for you contrbution, it is indeed something we should handle 
