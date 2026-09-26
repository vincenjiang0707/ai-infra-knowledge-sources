# [Issue #5318] [Release] v0.7.0 branch is missing #5097 (sparse-MLA cpb L2 guard-rail halving for integrated GPUs / DGX Spark)

source: https://github.com/flashinfer-ai/flashinfer/issues/5318
state: closed | updated: 2026-09-21T17:02:40Z
labels: needs-triage

## 正文

## Summary

[#5097](https://github.com/flashinfer-ai/flashinfer/pull/5097) ("fix(mla): halve sparse-MLA cpb L2 guard-rail window on integrated GPUs (Spark)") landed on `main` on 2026-09-11, but is **not** in the v0.7.0 release branch. If v0.7.0 ships as-is, DGX Spark / GB10 users upgrading from 0.6.18.post1 lose an integrated-GPU-specific sparse-MLA fix that is currently only available on `main`.

v0.7.0 is still in prerelease (rc3, 2026-09-16), so there is still a window to cherry-pick.

## Verification

Using the compare API against #5097's merge commit `6a85444798d07fa541b5d38a27f626c49c8624e9`:

| ref | contains #5097 |
|---|---|
| `main` | yes (`ahead`) |
| `v0.7.0rc1` | **no** (`diverged`) |
| `v0.7.0rc2` | **no** (`diverged`) |
| `v0.7.0rc3` | **no** (`diverged`) |

The neighbouring Spark fix [#5048](https://github.com/flashinfer-ai/flashinfer/pull/5048) ("prevent intermittent hang in SM120 sparse-MLA swapAB prefill on DGX Spark", merged 2026-09-09) **is** in rc3, which places the release-branch cut between 2026-09-09 and 2026-09-11 — i.e. #5097 missed it by about two days.

## Why it matters on GB10

`l2_cache_bytes` is the regime switch inside `predict_time_s`:

```
min(g, c.sm_count) * cpb * c.bytes_per_chunk > c.l2_cache_bytes
```

On GB10 the device reports `L2_cache_size = 25165824`. With #5097 the cpb model uses the halved window; we can see this directly in calibration output on a GB10 (48 SMs, `is_integrated=1`):

```
{"inv_bw": 4.999999999999996e-13, "inv_rsm": 1.956e-10, "c0": 5.764e-06,
 "sm_count": 48, "bytes_per_chunk": 37376, "l2_cache_bytes": 12582912}
```

`l2_cache_bytes = 12582912` (12 MiB) is the halved value. Without #5097 the same code path would use 24 MiB and pick cpb on the wrong side of the DRAM/L2 regime boundary for part of the shape space.

## Request

Cherry-pick #5097 (`6a854447`) onto the v0.7.0 release branch before GA.

More generally: it may be worth a release-gate check that Spark/SM12x-tagged fixes merged after the branch cut are triaged for backport. We noticed this only because we pin the sparse-MLA sources as a source overlay and diff them against upstream; a user simply upgrading to v0.7.0 would get a silent behaviour change with no warning, since the constant is computed rather than asserted.

## Environment

- 2x DGX Spark (GB10, SM121, 48 SMs, `is_integrated=1`, driver 580.173.02)
- Currently pinned to flashinfer 0.6.18.post1 with #4802 sparse-MLA SM120 sources overlaid, plus #5048 and #5097 applied on top — which is what surfaced the gap when we evaluated moving to the 0.7.0 line.


## 评论 (2)

### aleozlx · 2026-09-21

already on rel branch

https://github.com/flashinfer-ai/flashinfer/commit/0b532418f6a56cff153196370c69a9bcfd8793d0

closing

### aleozlx · 2026-09-21

your agent didn't even look at rc2 :)
