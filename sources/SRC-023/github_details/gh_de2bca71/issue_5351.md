# [Issue #5351] [Bug] Gluon MHA imports removed Triton utils module

source: https://github.com/ROCm/aiter/issues/5351
state: closed | updated: 2026-09-08T18:03:09Z
labels: 

## 正文

## Problem

After [#4147](https://github.com/ROCm/aiter/pull/4147) merged on top of the utils reorganization in [#5061](https://github.com/ROCm/aiter/pull/5061), the gfx950 Gluon MHA module imports `aiter.ops.triton.utils.core`. That module no longer exists; the exported config helpers now live in `aiter.ops.triton.utils.config_utils`.

As a result, MHA test files fail during pytest collection with:

```text
ModuleNotFoundError: No module named 'aiter.ops.triton.utils.core'\n```\n\n## Evidence\n\n- [Triton Test failure on current `main`](https://github.com/ROCm/aiter/actions/runs/34246454827)\n- [`main` MI35X shard 3 failure](https://github.com/ROCm/aiter/actions/runs/34246454827/job/102132338976)\n- [`main` MI300X shard 3 failure](https://github.com/ROCm/aiter/actions/runs/34246454827/job/102132339181)\n- [Independent reproduction after PR #4761 merged current `main`](https://github.com/ROCm/aiter/actions/runs/34257169809)\n\nThe same collection error appears in shards 3, 4, 5, and 7 on both MI35X and MI300X, depending on which MHA test file each shard contains.\n\n## Proposed fix\n\nImport `AITER_TRITON_CONFIGS_PATH` and `load_config_json` from `aiter.ops.triton.utils.config_utils`.

## 评论 (1)

### vorapolsiloai · 2026-09-08

The bug and evidence are tracked directly in #5352; a separate issue is unnecessary.
