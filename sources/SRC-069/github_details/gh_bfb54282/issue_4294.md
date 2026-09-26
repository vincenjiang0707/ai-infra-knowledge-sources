# [Issue #4294] [Bug][v0.6.17]test_selected_tactic_disables_async_memset_while_tuning  ValueError: Expected a cuda device, but got: cpu

source: https://github.com/flashinfer-ai/flashinfer/issues/4294
state: closed | updated: 2026-09-21T04:30:54Z
labels: ci: health, v0.6.17

## 正文

## Summary
Found this issue in FlashInfer CI.

## CI metadata
- Triage case: `case_019fb754fb2d365932b17b8e44e9`
- Test case: `tests.moe.test_cute_dsl_fused_moe.TestAutotuneReplayMemsetContract`
- FlashInfer commit: `5e496907`
- Pipeline: [pipeline](https://gitlab-master.nvidia.com/dl/flashinfer/flashinfer-ci/-/pipelines/60411411)
- Job name(s): `unit_test_b300: [cu130]`, `unit_test_b300: [cu129]`, `unit_test_gb200: [cu130]`, `unit_test_gb200: [cu129]`
- Branch: `main`
- Environment: `B300` / `cu130`

## Failed Jobs
- [unit_test_b300](https://nv/flashinfer-ci/-/jobs/380040559): `B300` / `cu130`
- [unit_test_b300](https://nv/flashinfer-ci/-/jobs/380040558): `B300` / `cu129`
- [unit_test_gb200](https://nv/flashinfer-ci/-/jobs/380040553): `GB200` / `cu130`
- [unit_test_gb200](https://nv/flashinfer-ci/-/jobs/380040552): `GB200` / `cu129`

## Failure
```text
ValueError: Expected a cuda device, but got: cpu
```
## Likely root cause
https://github.com/flashinfer-ai/flashinfer/pull/4192
## Reproduction command
```bash
pytest 'tests.moe.test_cute_dsl_fused_moe.TestAutotuneReplayMemsetContract'
```


## Suggest fix
set device="cuda" to each torch.empty / torch.zeros / torch.ones



## 评论 (3)

### cindyzxq · 2026-08-03

Looks like https://github.com/flashinfer-ai/flashinfer/pull/4301 has fixed this issue.  

### cindyzxq · 2026-08-03

@aleozlx @bkryu should we need cherry-pick this PR to release-v0.6.17 branch?

### aleozlx · 2026-08-04

cherry picked to release branch

https://github.com/flashinfer-ai/flashinfer/commit/32b54da4de31e43ba4a0d731e3c744eba49d3562

closing
