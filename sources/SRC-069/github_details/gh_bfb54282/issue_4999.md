# [Issue #4999] [Bug] test_sparse_mla_sm120_cpb_model assert 0.0042064361572265625 <= (1.25 * 0.0028502678871154784)

source: https://github.com/flashinfer-ai/flashinfer/issues/4999
state: closed | updated: 2026-09-21T04:31:28Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer main (6c14bbd5) CI reports a test assertion affecting 1 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers Spark / cu130 in flashinfer-ci.

## CI environment

- Commit: 6c14bbd5
- Branch: main
- Pipeline: [#66471033](https://nv/flashinfer-ci/-/pipelines/66471033)
- Affected scope: 1 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests.attention.test_sparse_mla_sm120_cpb_model::test_model_cpb_accuracy_guard_dual_cache[128-2176-64]
- Failed jobs:
  - [unit_test_spark: [cu130]](https://nv/flashinfer-ci/-/jobs/427851073)

## Failure

```text
assert 0.0042064361572265625 <= (1.25 * 0.0028502678871154784)
```

## Reproduction

```bash
pytest 'tests/attention/test_sparse_mla_sm120_cpb_model.py::test_model_cpb_accuracy_guard_dual_cache[128-2176-64]'
pytest 'tests/attention/test_sparse_mla_sm120_cpb_model.py::test_model_cpb_accuracy_guard_dual_cache[1024-2176-64]'
```

Generated from CI test identity; not independently verified.

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-09-06, last seen 2026-09-06.
- 2026-09-06 — (6c14bbd5) — Spark / cu130 — [pipeline #66471033](https://nv/flashinfer-ci/-/pipelines/66471033) / [job](https://nv/flashinfer-ci/-/jobs/427851073)


## 评论 (4)

### Champollion9012 · 2026-09-08

Ran both parametrizations from the Reproduction block on **discrete SM120**, at this issue's own
commit. Both pass, so the accuracy guard is not exceeded on sm_120.

**Environment**

```
GPU     NVIDIA RTX PRO 6000 Blackwell Server Edition, cc 12.0, driver 590.48.01
CUDA    13.1, torch 2.13.0+cu130
repo    6c14bbd5 (the commit in this report), submodules at their pinned revisions
```

| test | result |
|---|---|
| `test_model_cpb_accuracy_guard_dual_cache[128-2176-64]` | **PASSED**, 21.68 s (includes the first JIT build) |
| `test_model_cpb_accuracy_guard_dual_cache[1024-2176-64]` | **PASSED**, 2.38 s |

I also ran the whole of `tests/attention/test_sparse_mla_sm120.py` at the same commit: **488 passed
in 14.30 s**, which is the suite #5001 reports as 488 timeout nodes on Spark.

## Why an SM120-named suite is reporting from Spark

`tests/attention/test_sparse_mla_sm120.py` gates on the *family*, not on SM120:

```python
pytestmark = pytest.mark.skipif(
    not torch.cuda.is_available() or not is_sm12x_supported(torch.device("cuda")),
    reason="Sparse-MLA SM120 requires SM12x.",
)
```

Probed on this card:

```
cc = (12, 0)   is_sm12x = True   is_sm120a = True   is_sm121a = False
```

On a Spark that is the mirror image, so `is_sm12x_supported` admits both and the SM120-named suites
have been executing on SM121. `flashinfer.utils` already exposes the narrower `is_sm120a_supported`
and `is_sm121a_supported`, and there is precedent for splitting them per-arch in
PR #4606 ("test: skip SM120 FMHA v2 tests on SM121").

## What this does and does not establish

It establishes that the sparse-MLA kernels are healthy on discrete sm_120 at 6c14bbd5, and that
neither failure is a property of sm_120.

It does **not** tell you whether the Spark failures are a real SM121 kernel defect or an
environment/timing artifact on that runner — I have no Spark and cannot distinguish those. So I am
deliberately not proposing "narrow the gate to SM120" as the fix: if the SM121 side is a genuine bug,
narrowing would hide it rather than fix it. That call is yours.

Happy to run any additional shape, tolerance, or parametrization on discrete sm_120 if it would help
separate the two, and to open a PR for whichever direction you prefer once that is decided.


### bkryu · 2026-09-10

Thanks @Champollion9012 for your analysis. It appears then that SM120 is fine, but I can reproduce the issue on a DGX Spark (SM121).

Issue could be from sm121a vs. sm120a, Spark having far fewer SMs. Currently looking

### aleozlx · 2026-09-11

Reopening: this still reproduces on **v0.7.0rc1** (`07869c61`).

The closing discussion established that the guard is not exceeded on discrete SM120 (RTX PRO 6000, cc 12.0) but does reproduce on DGX Spark (SM121) — that second half was never resolved, and release validation for v0.7.0rc1 hit it again on Spark, on both CUDA 12.9 and CUDA 13.0:

```text
assert 0.004230095863342285 <= (1.25 * 0.0028645880222320555)
assert 0.004230584144592285 <= (1.25 * 0.0028621439933776854)
assert 0.005783331871032715 <= (1.25 * 0.003930003881454468)
assert 0.005794772148132324 <= (1.25 * 0.003956975936889648)
```

The first two match this issue's original `0.0042064361572265625 <= (1.25 * 0.0028502678871154784)` to three significant figures. One of the two larger ones is reported against `test_model_cpb_accuracy_guard_dual_cache`, so the dual-cache path shows the same overshoot with a different baseline.

All four are roughly 18% above the allowed `1.25 ×` bound, and all four are Spark-only — no SM120, SM100 or SM103 environment in the same validation run reported them. That is consistent with the sm121a-vs-sm120a / lower-SM-count hypothesis raised when this was closed.

Flagging for triage rather than asserting a root cause: I have not reproduced this myself, and I do not have a first-bad commit for it.

### aleozlx · 2026-09-11

My mistake — reclosing.

I reopened this on rc1 evidence without checking what had closed it. #5097 ("fix(mla): halve sparse-MLA cpb L2 guard-rail window on integrated GPUs (Spark)") merged 2026-09-11 and fixes exactly this; the v0.7.0rc1 tag was cut on 2026-09-09, so the fix is on `main` but not on the release branch yet.

So the rc1 failures I quoted are expected for that tag and are not evidence of an unresolved bug — they just need the fix carried onto `release-v0.7.0`. Sorry for the noise.
