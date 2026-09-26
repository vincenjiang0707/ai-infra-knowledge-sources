# [Issue #4396] [Bug][v0.6.17][gb300]tests/gemm/test_groupwise_scaled_gemm_fp8.py:201: Mismatched elements: 124 / 8192 (1.5%)

source: https://github.com/flashinfer-ai/flashinfer/issues/4396
state: open | updated: 2026-09-21T04:30:58Z
labels: duplicate, flaky, ci: health

## 正文

### Summary
Found this issue in FlashInfer CI.

### CI metadata
Test case: tests/gemm/test_groupwise_scaled_gemm_fp8.py::test_fp8_groupwise_gemm_small_batch_size[K-256-256-32]
FlashInfer commit: d4cd4c764bdaf8d59bb9a7c2ccbdf0bf4d36a8c6
Pipeline: [pipeline](https://nv/flashinfer-ci/-/pipelines/61491878)
Job name(s): unit_test_gb300: [cu130]
Branch: release-v0.6.17
Environment: gb300
### Failed Jobs
[unit_test_gb300](https://nv/flashinfer-ci/-/jobs/388035432): gb300 / cu130
### Failure
```shell
     Mismatched elements: 124 / 8192 (1.5%)
     Greatest absolute difference: 1.71875 at index (8, 42) (up to 0.01 allowed)
     Greatest relative difference: 90.0 at index (8, 123) (up to 0.01 allowed)
 /workspace/flashinfer/tests/gemm/test_groupwise_scaled_gemm_fp8.py:201: AssertionError: Tensor-likes are not close!
``` 

### Reproduction command
```python
pytest 'tests.gemm.test_groupwise_scaled_gemm_fp8'
``` 

## 评论 (3)

### aleozlx · 2026-08-07

Investigated. Summary: **pre-existing CUTLASS race, not an rc3→rc4 regression, not gb300-specific — and a recurrence of #3944.**

## Duplicate of #3944

#3944 (filed 2026-07-13, closed 2026-07-17, labeled `ci: health`) reports the identical signature on **b300**:

- same test id `test_fp8_groupwise_gemm_small_batch_size[K-256-256-32]`
- same `124` mismatched elements
- same `Greatest absolute difference: 1.71875 at index (8, 42)`
- same `Greatest relative difference: 90.0 at index (8, 123)`

It recurred on the rc3 nightly (`124 / 4096`, 3.0% — same 124 elements, smaller denominator), then was closed after a comment that rc4 did not reproduce it. It was closed on a passing run, not on a fix, which is what a sub-1%-per-launch race looks like when triaged as flake.

## Not an rc4 regression

`csrc/gemm_groupwise_sm100.cu` and `include/flashinfer/gemm/gemm_groupwise_sm100.cuh` are **byte-identical between `main` and `release-v0.6.17`** at d4cd4c76, and last changed by #2327 (Jan 2026). rc4 adds only MoE commits over rc3. It also reproduces on **B200/SM100**, so it is not SM103-specific.

## Root cause

`gemm_fp8_nt_groupwise` (cutlass backend) routes `m <= 32` to `CutlassGroupwiseScaledGEMMSM100LowLatency`, which computes `D^T = B^T @ A^T` so it can use a 16-wide N tile instead of spending a 128-wide M tile on ≤32 rows. That A/B swap **mirrors the blockwise scale granularities**: the collective runs with `ScaleMsPerTile == 1` / `ScaleNsPerTile == 16` instead of the usual `128` / `1`.

That mirrored configuration races in the CUTLASS SM100 blockwise-scaling mainloop’s `cp.async` scale-factor pipeline (`sm100_mma_warpspecialized_blockwise_scaling.hpp`, `load_sf`): a scale-factor column is occasionally consumed before its `cp.async` lands. That scale is shared by every row of the CTA’s M tile, so one stale value corrupts **exactly one output row of exactly one N tile** — which is why the report shows both extreme indices in row 8, and why the general kernel never shows it on identical inputs.

Note it is a **race, not bad data**: it is not seed-reproducible, so replaying the CI seed does nothing.

## Evidence (GB300 / SM103, 6000 invocations per m, n=k=256, mode K)

| m | before | after |
|---|--------|-------|
| 24 | 18/6000 | 0/6000 |
| 28 | 25/6000 | 0/6000 |
| 32 | 36/6000 | 0/6000 |
| **total** | **79/18000 (0.44%)** | **0/18000** |

Reproduced 0/18000 on a second GB300. Unpatched B200 also fails (`125/8192`, one row, one block). General kernel on identical inputs: 0/100.

## Fix — #4409

1. Stop dispatching to the low-latency small-batch kernel (`kEnableLowLatencySmallBatch = false`). The kernel and its instantiations are kept, so re-enabling is a one-line change once CUTLASS is fixed.
2. Companion fix: the fallback exposed `can_implement failed` for MN-major scales with `m % 4 != 0` (a constraint only ever enforced for `m > 32`). Added pad-and-slice, which also fixes pre-existing breakage at m=33/127/129/130 MN.

Post-fix on GB300: `266 passed`, `16 passed`, and `658 passed, 63 skipped` (identical to the pre-fix baseline).

### Trade-offs / caveats, stated plainly

- This **forfeits the 10–40% small-batch speedup** from #2327. It is avoidance, not a repair of the underlying CUTLASS defect.
- The **exact CUTLASS defect line was not pinned** — it was localized to the `load_sf` cp.async pipeline by signature and elimination, not by instrumenting CUTLASS.
- #4409 targets `main`; **`release-v0.6.17` carries byte-identical code and should get a cherry-pick.**

Given #3944 was already closed once as flaky and came back, I would not recommend closing this as flake again.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

### aleozlx · 2026-08-07

**Correction to my earlier comment:** I said `release-v0.6.17` "should get a cherry-pick". Retracting that.

`2bf87713` (#2327, 2026-01-13) is an ancestor of **v0.6.13, v0.6.14, v0.6.15, v0.6.16 and v0.6.16.post2**, so this has shipped in at least five releases over ~7 months with **no field reports** — every sighting is CI (#3944, now this one).

0.6.17 therefore is not broken relative to anything users already run. Cherry-picking the fix would trade a rare, never-reported glitch for a **guaranteed 10-40% small-batch perf regression** landing at rc4/rc5 — a change users *would* notice, for a problem they have not.

**Revised: leave `release-v0.6.17` as-is; fix it properly on `main` for 0.6.18.** #4409 is now a draft while the remedy is decided (disabling the fast path costs #2327 wholesale; the better answer is repairing the CUTLASS scale-factor pipeline and keeping the speedup).

Everything in my previous comment about the *root cause* stands unchanged — the race, the evidence, and the fact that the tolerance is not the problem.

One thing worth keeping straight for future triage: "no user complaints in 7 months" makes this **not urgent**, not **not real**. A silent wrong row in a GEMM is precisely the class of defect users cannot observe or report. Please do not close this as flaky — that is what happened to #3944, and it cost a second full investigation to re-derive.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

### aleozlx · 2026-08-07

not a release blocker for 0.6.17 based on the above

and i will not submit the fix above (Claude proposed)
