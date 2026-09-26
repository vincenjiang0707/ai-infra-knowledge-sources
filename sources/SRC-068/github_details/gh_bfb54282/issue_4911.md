# [Issue #4911] [Bug]test_recurrent_kda_prefill.py  ModuleNotFoundError: No module named 'cutlass.experimental', ImportError: backend='cute-dsl' requires nvidia-cutlass-dsl>=4.7.0 (cutlass.experimental);

source: https://github.com/flashinfer-ai/flashinfer/issues/4911
state: closed | updated: 2026-09-21T04:31:17Z
labels: needs-triage, ci: health, op: linear attention

## 正文

## Summary
FlashInfer main CI reports 2 distinct saved failure signature(s) affecting 2 selected test(s) across 2 environment(s). The evidence from 2 selected failure group(s) is de-duplicated by failure, job, environment, and history pipeline below.

## CI environment
- Commit: 0b79dc1b
- Branch: main
- Pipeline: [#65618325](https://nv/flashinfer-ci/-/pipelines/65618325)
- Affected tests:
  - tests.kda.test_recurrent_kda_prefill::test_cute_dsl_lpt_sequence_order_is_content_cached
  - tests.kda.test_recurrent_kda_prefill::test_frozen_bt16_combined_h12_fixed512_matches_cute
- Environments:
  - unit_test_b300_cu134, unit_test_gb200_cu134, unit_test_gb300_cu134, unit_test_h100_cu134, unit_test_rtx-pro-6000-blackwell_cu134 / unknown GPU / unknown CUDA
  - unit_test_b300_cu134, unit_test_gb200_cu134, unit_test_gb300_cu134 / unknown GPU / unknown CUDA
- Failed jobs:
  - [unit_test_gb300_cu134 #420573589](https://nv/flashinfer-ci/-/jobs/420573589)
  - [unit_test_gb200_cu134 #420573594](https://nv/flashinfer-ci/-/jobs/420573594)
  - [unit_test_b300_cu134 #420573599](https://nv/flashinfer-ci/-/jobs/420573599)
  - [unit_test_h100_cu134 #420573605](https://nv/flashinfer-ci/-/jobs/420573605)
  - [unit_test_rtx-pro-6000-blackwell_cu134 #420794921](https://nv/flashinfer-ci/-/jobs/420794921)
  - 1 additional jobs omitted.

## Failure

**Failure 1 — affects tests.kda.test_recurrent_kda_prefill::test_cute_dsl_lpt_sequence_order_is_content_cached**

```text
ModuleNotFoundError: No module named 'cutlass.experimental'
```

**Failure 2 — affects tests.kda.test_recurrent_kda_prefill::test_frozen_bt16_combined_h12_fixed512_matches_cute**

```text
ImportError: backend='cute-dsl' requires nvidia-cutlass-dsl>=4.7.0 (cutlass.experimental); backend='auto' falls back to Cake
```

## Reproduction

```bash
pytest \
  'tests/kda/test_recurrent_kda_prefill.py::test_cute_dsl_lpt_sequence_order_is_content_cached' \
  'tests/kda/test_recurrent_kda_prefill.py::test_frozen_bt16_combined_h12_fixed512_matches_cute'
```

Generated from 2 saved CI test identities; run from the FlashInfer repository root. Not independently verified.

## Case History
3 unique confirmed historical failure pipeline(s) shown; first seen 2026-08-29, last seen 2026-09-02.
- 2026-09-02 —   (3a4e7052) — unit_test_b300_cu134, unit_test_gb200_cu134, unit_test_gb300_cu134, unit_test_h100_cu134, unit_test_rtx-pro-6000-blackwell_cu134 / unknown GPU / unknown CUDA; unit_test_b300_cu134, unit_test_gb200_cu134, unit_test_gb300_cu134 / unknown GPU / unknown CUDA — [pipeline #65814627](https://nv/flashinfer-ci/-/pipelines/65814627) — affects tests.kda.test_recurrent_kda_prefill::test_cute_dsl_lpt_sequence_order_is_content_cached, tests.kda.test_recurrent_kda_prefill::test_frozen_bt16_combined_h12_fixed512_matches_cute / [unit_test_gb300_cu134 #422236745](https://nv/flashinfer-ci/-/jobs/422236745), [unit_test_gb200_cu134 #422236768](https://nv/flashinfer-ci/-/jobs/422236768), [unit_test_b300_cu134 #422236780](https://nv/flashinfer-ci/-/jobs/422236780), [unit_test_h100_cu134 #422236800](https://nv/flashinfer-ci/-/jobs/422236800), [unit_test_rtx-pro-6000-blackwell_cu134 #422236810](https://nv/flashinfer-ci/-/jobs/422236810)
- 2026-09-01 —  (0b79dc1b) — unit_test_b300_cu134, unit_test_gb200_cu134, unit_test_gb300_cu134, unit_test_h100_cu134, unit_test_rtx-pro-6000-blackwell_cu134 / unknown GPU / unknown CUDA; unit_test_b300_cu134, unit_test_gb200_cu134, unit_test_gb300_cu134 / unknown GPU / unknown CUDA — [pipeline #65618325](https://nv/flashinfer-ci/-/pipelines/65618325) — affects tests.kda.test_recurrent_kda_prefill::test_cute_dsl_lpt_sequence_order_is_content_cached, tests.kda.test_recurrent_kda_prefill::test_frozen_bt16_combined_h12_fixed512_matches_cute / [unit_test_gb300_cu134 #420573589](https://nv/flashinfer-ci/-/jobs/420573589), [unit_test_gb200_cu134 #420573594](https://nv/flashinfer-ci/-/jobs/420573594), [unit_test_b300_cu134 #420573599](https://nv/flashinfer-ci/-/jobs/420573599), [unit_test_h100_cu134 #420573605](https://nv/flashinfer-ci/-/jobs/420573605), [unit_test_rtx-pro-6000-blackwell_cu134 #420794921](https://nv/flashinfer-ci/-/jobs/420794921)
- 2026-08-31 —  (2cc51dcf) — unit_test_b300_cu134, unit_test_gb200_cu134, unit_test_gb300_cu134, unit_test_h100_cu134, unit_test_rtx-pro-6000-blackwell_cu134 / unknown GPU / unknown CUDA; unit_test_b300_cu134, unit_test_gb200_cu134, unit_test_gb300_cu134 / unknown GPU / unknown CUDA — [pipeline #65430604](https://nv/flashinfer-ci/-/pipelines/65430604) — affects tests.kda.test_recurrent_kda_prefill::test_cute_dsl_lpt_sequence_order_is_content_cached, tests.kda.test_recurrent_kda_prefill::test_frozen_bt16_combined_h12_fixed512_matches_cute / [unit_test_gb300_cu134 #418997447](https://nv/flashinfer-ci/-/jobs/418997447), [unit_test_gb200_cu134 #418997460](https://nv/flashinfer-ci/-/jobs/418997460), [unit_test_b300_cu134 #418997484](https://nv/flashinfer-ci/-/jobs/418997484), [unit_test_h100_cu134 #418997494](https://nv/flashinfer-ci/-/jobs/418997494), [unit_test_rtx-pro-6000-blackwell_cu134 #418997514](https://nv/flashinfer-ci/-/jobs/418997514)
- Additional history pipelines omitted: 4 older confirmed failure entry(s).



## 评论 (1)

### XFDG · 2026-09-12

Hi, I retested this on a B200 (SM100) against current `main` (`d70a043f`) with CUDA 13.1 and `nvidia-cutlass-dsl` 4.8.0.dev0.

`import cutlass.experimental` now succeeds. The original `test_cute_dsl_lpt_sequence_order_is_content_cached` node was reworked by #5021 (`b6aed597`) into `test_cute_dsl_device_sequence_order_buffer_is_stream_cached`; that current replacement passes. The other reported regression node also passes:

- `test_cute_dsl_device_sequence_order_buffer_is_stream_cached`: 1 passed
- `test_frozen_bt16_combined_h12_fixed512_matches_cute`: 1 passed

This issue is therefore not reproducible on current `main`; no additional patch or duplicate PR appears necessary.

