# [Issue #5510] [Bug] main H100 CI red since #5482: test_build_targets_follow_flashinfer_cuda_arch_list expects sm_107a on a cu129 image

source: https://github.com/flashinfer-ai/flashinfer/issues/5510
state: closed | updated: 2026-09-24T08:32:13Z
labels: needs-triage

## 正文

## Summary

Since #5482 merged (2026-09-23 12:29 UTC), the GitHub `JIT Unittest (H100)` lane fails on `main` for every PR, on exactly one node:

```
tests/utils/test_cake_sampling.py::test_build_targets_follow_flashinfer_cuda_arch_list
E   At index 0 diff: '-gencode=arch=compute_100f,code=sm_100f' != '-gencode=arch=compute_107a,code=sm_107a'
tests/utils/test_cake_sampling.py:561: AssertionError
```

Seen on two independent PRs whose merge commits include #5482, same node, same diff, everything else green:

- #5504 (per-token alpha for mm_fp4): [job 107383563414](https://github.com/flashinfer-ai/flashinfer/actions/runs/35920561852/job/107383563414), merge of b164f82 into f476158; 229,310 passed, 1 failed.
- prune-test-trtllm-attention-decode: [job 107419378874](https://github.com/flashinfer-ai/flashinfer/actions/runs/35931622405/job/107419378874), merge of 0c53a4f into 0f96675; 598 source files passed, 1 failed.

Main's own post-merge runs have not produced a completed H100 job yet because each is cancelled by the next push.

## Cause

The H100 lane runs `flashinfer-ci-cu129:20260822-9a0e83b`, whose nvcc does not support sm_107. `CompilationContext.get_nvcc_flags_list` (flashinfer/compilation_context.py) applies the SM107 -> sm_100f fallback whenever the toolkit lacks sm_107 support:

```python
apply_sm107_mapping = (
    map_sm107_to_100f and not cutlass_supports_sm107()
) or not _nvcc_supports_sm107()
```

The test's second block sets `FLASHINFER_CUDA_ARCH_LIST="10.7 11.0"` with an **unsuffixed** `10.7` and asserts `compute_107a` unconditionally. The test's own comment says suffixed entries are what skip the toolkit probe, and the first block (`"9.0 10.3 12.0f"`) happens to pass only because sm_90 / sm_103 are supported by nvcc 12.9.

## Suggested fix

Either use a suffixed entry (`"10.7a 11.0a"`) in that block so the probe is skipped as the comment intends, or make the expected `-gencode` for 10.7 depend on `_nvcc_supports_sm107()` (expect `compute_100f` on toolkits without sm_107).

cc @yyihuang


## 评论 (2)

### aleozlx · 2026-09-24

Fix in #5511.

### saltyminty · 2026-09-24

It seems that this failure from https://github.com/flashinfer-ai/flashinfer/pull/5482 was exposed by https://github.com/flashinfer-ai/flashinfer/pull/4981, which went in after. Unfortunate timing.
