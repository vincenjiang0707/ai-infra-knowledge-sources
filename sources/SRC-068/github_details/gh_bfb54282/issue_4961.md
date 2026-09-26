# [Issue #4961] [Bug] test_dcp_spec_fp8.py RuntimeError: DCP speculative FMHA requires compute capability 10.0 (B200/GB200) or 10.3 (B300/GB300), got 10.7

source: https://github.com/flashinfer-ai/flashinfer/issues/4961
state: open | updated: 2026-09-21T04:31:23Z
labels: needs-triage, ci: health, arch: sm107

## 正文

## Summary
FlashInfer main(971b0a6b) CI reports a test assertion affecting 1 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers unknown / cu134 in flashinfer-ci.

## CI environment

- Commit: 971b0a6b
- Branch: main
- Pipeline: [#66007281](https://nv/flashinfer-ci/-/pipelines/66007281)
- Affected scope: 1 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests/attention/test_dcp_spec_fp8.py
- Failed jobs:
  - [unit_test_vr200_cu134](https://nv/flashinfer-ci/-/jobs/423917323)

## Failure

```text
RuntimeError: DCP speculative FMHA requires compute capability 10.0 (B200/GB200) or 10.3 (B300/GB300), got 10.7
```

## Reproduction

```bash
pytest 'tests/attention/test_dcp_spec_fp8.py'
```

Generated from CI test identity; not independently verified.

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-09-03, last seen 2026-09-03.
- 2026-09-03 —  (971b0a6b) — unknown GPU / cu134 — [pipeline #66007281](https://nv/flashinfer-ci/-/pipelines/66007281) / [job](https://nv/flashinfer-ci/-/jobs/423917323)


## 评论 (1)

### nvamyt · 2026-09-04

Belows cases seems same root cause: 
Affected tests:
```python
tests.moe.test_trtllm_gen_routing::test_unsupported_fused_shared_experts_rejected[DeepSeekV3_no_groups]
tests.moe.test_trtllm_gen_routing.py::test_invalid_group_args_rejected
tests.moe.test_trtllm_gen_routing::test_custom_routing_methods[Default-uniform-logits_dtype0-8-16-1-1]
tests.attn_scores.test_attn_scores_adversarial::test_adv_fp4_boundaries[128-1-32]
tests.attn_scores.test_attn_scores_adversarial::test_adv_context_boundaries_fp8[1-1-32]
tests.gemm.test_groupwise_scaled_gemm_fp8::test_fp8_groupwise_gemm[cutile-K-128-128-128]
tests.moe.test_unified_moe.py::test_cute_dsl_typed_activation_matches_flat_reference[activation0-QuantVariant.NVFP4]
tests.moe.test_unified_moe.py::test_cute_dsl_typed_activation_matches_flat_reference[activation3-QuantVariant.NVFP4]
tests.moe.test_unified_moe.py::test_cute_dsl_typed_activation_matches_flat_reference[activation2-QuantVariant.NVFP4]
``` 
Environments:
unit_test_vr200_cu134 / unknown GPU / cu134
Failed jobs:
[unit_test_vr200_cu134 #423917323](https://nv/flashinfer-ci/-/jobs/423917323)
Failure
Failure 1 — affects tests.moe.test_trtllm_gen_routing::test_unsupported_fused_shared_experts_rejected[DeepSeekV3_no_groups]
```shell
AssertionError: Regex pattern did not match. Expected regex: 'fusing shared expert' Actual message: 'trtllm_gen_routing does not support compute capability 107'
``` 

Failure 2 — affects tests.moe.test_trtllm_gen_routing.py::test_invalid_group_args_rejected
```shell
AssertionError: Regex pattern did not match. Expected regex: 'n_group should not be zero' Actual message: 'trtllm_gen_routing does not support compute capability 107'
``` 
Failure 3 — affects tests.moe.test_trtllm_gen_routing::test_custom_routing_methods[Default-uniform-logits_dtype0-8-16-1-1]
```shell
flashinfer.utils.BackendSupportedError: trtllm_gen_routing does not support compute capability 107
``` 

Failure 4 — affects  tests/attention/test_block_sparse.py::test_block_sparse_attention
Failed jobs: [unit_test_vr200_cu134](https://nv/flashinfer-ci/-/jobs/433555495)
```text
RuntimeError: vsa_sm100_blk128 backend requires SM100/SM103, current device is SM107
```
