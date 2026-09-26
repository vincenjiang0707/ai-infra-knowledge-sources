# [Issue #5000] [Bug] test_trtllm_gen_moe_autotune_tactics.py  assert ('flashinfer::trtllm_fp4_block_scale_moe', 'MoERunner') in set()

source: https://github.com/flashinfer-ai/flashinfer/issues/5000
state: closed | updated: 2026-09-21T04:31:30Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18 (6c14bbd5) CI reports a test assertion affecting 10 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers B200 / cu134, GB200 / cu134, GB300 / cu134, VR200 / cu134, B200 / cu130, B200 / cu129, GB200 / cu130, GB200 / cu129, GB300 / cu130, GB300 / cu129 in flashinfer-ci.

## CI environment

- Commit: 6c14bbd5
- Branch: main
- Pipeline: [#66471033](https://nv/flashinfer-ci/-/pipelines/66471033)
- Affected scope: 10 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests/moe/test_trtllm_gen_moe_autotune_tactics.py
- Failed jobs:
  - [unit_test_b200_cu134](https://nv/flashinfer-ci/-/jobs/427851528)
  - [unit_test_gb200_cu134](https://nv/flashinfer-ci/-/jobs/427851487)
  - [unit_test_gb300_cu134](https://nv/flashinfer-ci/-/jobs/427851446)
  - [unit_test_vr200_cu134](https://nv/flashinfer-ci/-/jobs/427851413)
  - [unit_test_b200: [cu130]](https://nv/flashinfer-ci/-/jobs/427850921)
  - [unit_test_b200: [cu129]](https://nv/flashinfer-ci/-/jobs/427850898)
  - [unit_test_gb200: [cu130]](https://nv/flashinfer-ci/-/jobs/427850688)
  - [unit_test_gb200: [cu129]](https://nv/flashinfer-ci/-/jobs/427850657)
  - [unit_test_gb300: [cu130]](https://nv/flashinfer-ci/-/jobs/427850604)
  - [unit_test_gb300: [cu129]](https://nv/flashinfer-ci/-/jobs/427850502)

## Failure

```text
AssertionError: [DeepSeekFp8] forced tactic was not dispatched — autotuner did not log a cache hit; check `_moe_profile_shapes` (scale_dim) against the actual MoEInputs layout. assert ('flashinfer::trtllm_fp8_block_scale_moe', 'MoERunner') in set()  +  where set() = <flashinfer.autotuner.autotuner.A
```

## Reproduction

```bash
pytest 'tests/moe/test_trtllm_gen_moe_autotune_tactics.py'
```

Generated from CI test identity; not independently verified.

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-09-06, last seen 2026-09-06.
- 2026-09-06 — (6c14bbd5) — B200, GB200, GB300, VR200 / cu129, cu130, cu134 — [pipeline #66471033](https://nv/flashinfer-ci/-/pipelines/66471033) / [job](https://nv/flashinfer-ci/-/jobs/427850502)


## 评论 (3)

### cindyzxq · 2026-09-11

Likely caused by https://github.com/flashinfer-ai/flashinfer/pull/3861: MoERunner now includes runner parameters in cache key extras, but the test still injects keys with empty extras (). This mismatch causes the cache miss and assertion failure. Update the test helper to use the runner’s actual extras.
cc: @aleozlx @YangXu1990uiuc 

### XFDG · 2026-09-13

Retested/inspected this against current main on B200 (SM100). The cache-key mismatch from the reported 6c14bbd5 build has been resolved by #4361 (commit c05407ceff): `_force_tactic_in_autotuner_cache` now receives the actual runner and persists `runner.get_cache_key_extras([])` instead of the old empty extras tuple. Comparing c05407ceff with its parent confirms that exact regression fix. The current targeted DeepSeekFp8 node node now gets past JIT setup, but an independent default-tactic runtime error occurs before this test reaches its cache-hit assertion, so I am not opening a duplicate patch for #5000.

### nvamyt · 2026-09-14

Not found this issue with v0.7rc2[#67720432](https://nv/flashinfer-ci/-/pipelines/67720432)
