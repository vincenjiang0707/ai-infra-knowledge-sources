# [Issue #4799] [Bug][v0.6.18rc10] cudnn._compiled_module.cudnnGraphNotSupportedError: Mixed-form sequence lengths (cu_seq_len on one side with seq_len on the other) require cuDNN 9.25.0 or above

source: https://github.com/flashinfer-ai/flashinfer/issues/4799
state: open | updated: 2026-09-21T04:31:14Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18rc10 (e62941a1) CI reports a test assertion affecting 3 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers framework CI in flashinfer-ci.

## CI environment

- Commit: e62941a1
- Branch: release-v0.6.18
- Pipeline: [#64977547](https://nv/flashinfer-ci/-/pipelines/64977547)
- Affected scope: 3 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests/attention/test_cudnn_prefill_paged_cu_seqlens.py
- Failed jobs:
  - [unit_test_b300_cu134](https://nv/flashinfer-ci/-/jobs/415265485)
  - [unit_test_gb200_cu134](https://nv/flashinfer-ci/-/jobs/415265484)
  - [unit_test_gb300_cu134](https://nv/flashinfer-ci/-/jobs/415265483)

## Failure

```text
E   cudnn._compiled_module.cudnnGraphNotSupportedError: Mixed-form sequence lengths (cu_seq_len on one side with seq_len on the other) require cuDNN 9.25.0 or above
```

## Reproduction

```bash
pytest tests/attention/test_cudnn_prefill_paged_cu_seqlens.py
```

Generated from CI test identity; not independently verified.

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-08-28, last seen 2026-08-28.
- 2026-08-28 — 0.6.18rc10 (e62941a1) — unknown GPU / unknown CUDA — [pipeline #64977547](https://nv/flashinfer-ci/-/pipelines/64977547) / [job](https://nv/flashinfer-ci/-/jobs/415265483)



## 评论 (1)

### yufeiwu-nv · 2026-09-18

Also found on perf test
