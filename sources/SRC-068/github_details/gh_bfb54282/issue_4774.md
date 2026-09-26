# [Issue #4774] [Bug][v0.6.18rc9] test_trtllm_gen_fused_moe.py unit-timeout recurs (2h+)

source: https://github.com/flashinfer-ai/flashinfer/issues/4774
state: closed | updated: 2026-09-21T04:31:11Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18rc9 (eadfae36) CI reports a test error affecting 5 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers B300 / cu129, GB200 / cu130, GB200 / cu129, GB300 / cu130, GB300 / cu129 in flashinfer-ci.

## CI environment

- Commit: eadfae36
- Branch: release-v0.6.18
- Pipeline: [#64780358](https://nv/flashinfer-ci/-/pipelines/64780358)
- Affected scope: 5 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests/moe/test_trtllm_gen_fused_moe.py
- Failed jobs:
  - [unit_test_b300: [cu129]](https://nv/flashinfer-ci/-/jobs/413687940)
  - [unit_test_gb200: [cu130]](https://nv/flashinfer-ci/-/jobs/413687935)
  - [unit_test_gb200: [cu129]](https://nv/flashinfer-ci/-/jobs/413687934)
  - [unit_test_gb300: [cu130]](https://nv/flashinfer-ci/-/jobs/413687933)
  - [unit_test_gb300: [cu129]](https://nv/flashinfer-ci/-/jobs/413687932)

## Failure

```text
JUnit marked 8173 testcases as not executed due to timeout; these are NOT RUN, not individual testcase failures
```

## Reproduction

```bash
pytest 'tests/moe/test_trtllm_gen_fused_moe.py'
```

Generated from CI test identity; not independently verified.

## Case History
— regression after PR #3635/PR #4082 sharding


## 评论 (1)

### bkryu · 2026-08-31

Closing issue as it pertains to an rc version of 0.6.18 and 0.6.18 has been released
