# [Issue #4913] [Bug][v0.6.18] test_trtllm_gen_moe_autotune_tactics.py Error in function 'operator()' at /workspace/flashinfer/csrc/fused_moe/trtllm_backend/trtllm_fused_moe_routing_custom.cuh:897: Got CUDA error

source: https://github.com/flashinfer-ai/flashinfer/issues/4913
state: closed | updated: 2026-09-21T04:31:19Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18 (0b79dc1b) CI reports a test assertion affecting 2 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers framework CI in flashinfer-ci.

## CI environment

- Commit: 0b79dc1b
- Branch: main
- Pipeline: [#65618325](https://nv/flashinfer-ci/-/pipelines/65618325)
- Affected scope: 2 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests.moe.test_trtllm_gen_moe_autotune_tactics::test_nvfp4_per_token_all_tactics_are_correct[Relu2]
- Failed jobs:
  - [unit_test_gb200_cu134](https://nv/flashinfer-ci/-/jobs/420573594)
  - [unit_test_gb300_cu134](https://nv/flashinfer-ci/-/jobs/420573589)

## Failure

```text
AssertionError: Per-token NVFP4 tactic [128, 3] failed accuracy for Relu2
```

## Reproduction

```bash
pytest 'tests/moe/test_trtllm_gen_moe_autotune_tactics.py::test_nvfp4_per_token_all_tactics_are_correct[Relu2]'
```

Generated from CI test identity; not independently verified.

## Case History
- 4 confirmed failure pipeline(s); first seen 2026-08-29, last seen 2026-09-01.
- 2026-09-01 — 0.6.18 (0b79dc1b) — unknown GPU / unknown CUDA — [pipeline #65618325](https://nv/flashinfer-ci/-/pipelines/65618325) / [job](https://nv/flashinfer-ci/-/jobs/420573589)
- 2026-08-31 — 0.6.18 (2cc51dcf) — unknown GPU / unknown CUDA — [pipeline #65430604](https://nv/flashinfer-ci/-/pipelines/65430604) / [job](https://nv/flashinfer-ci/-/jobs/418997447)
- 2026-08-30 — 0.6.18 (44428003) — unknown GPU / unknown CUDA — [pipeline #65302610](https://nv/flashinfer-ci/-/pipelines/65302610) / [job](https://nv/flashinfer-ci/-/jobs/417964746)
- 2026-08-29 — 0.6.18 (44428003) — unknown GPU / unknown CUDA — [pipeline #65193842](https://nv/flashinfer-ci/-/pipelines/65193842) / [job](https://nv/flashinfer-ci/-/jobs/417072426)



## 评论 (1)

### nvamyt · 2026-09-09

Not found this error with commit(866acb62):  
https://nv/flashinfer-ci/-/jobs/430135918/artifacts/external_file/batch-b17d7abca663264d.log

