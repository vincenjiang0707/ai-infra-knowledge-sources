# [Issue #2882] [TRITON][CI] Fix `test_pa_decode.py` flakiness in `gfx942`

source: https://github.com/ROCm/aiter/issues/2882
state: open | updated: 2026-08-31T06:14:57Z
labels: bug

## 正文

We've been recently exposed **(April 22nd, 2026)** to flaky behavior of `op_tests/triton_tests/attention/test_pa_decode.py::test_paged_attn` Triton unit test. It happens only in **MI325** CI runners, i.e. `gfx942` architecture. It was observed in more than one PR, we can take [PR 2612](https://github.com/ROCm/aiter/pull/2612#issuecomment-4297115815) as an example.

This test produces inconsistent results - passing and failing intermittently - without any changes to the code, eroding trust in testing and stalling CI. Sometimes it pass, sometimes it fails with an abort error, crashing the `pytest` process and the whole shard execution. Upon abortion, the workaround solution is to trigger a shard rerun.

It usually happens on **Triton Tests (MI325) / Shard 3**, but it can change given shard rebalancing and some recent PRs merged with the goal of speeding up CI.

**Important notice:** We may need to enable Triton CI on MI325 runners to validate the fix, given that [PR 2871](https://github.com/ROCm/aiter/pull/2871) has disabled it and has set MI35X runners as the default ones.

## 评论 (3)

### brunomazzottiamd · 2026-04-23

@azaidy, can you please prioritize / assign this ticket? It was a request from @gyohuangxin, in the scope of https://github.com/ROCm/aiter/pull/2612. Thanks!

### brunomazzottiamd · 2026-04-27

@gyohuangxin, I couldn't reproduce the abort failure locally. We're thinking about monitoring CI for a while an report the failures as they happen in this ticket. Do you agree with our aproach?

### gyohuangxin · 2026-04-28

> [@gyohuangxin](https://github.com/gyohuangxin), I couldn't reproduce the abort failure locally. We're thinking about monitoring CI for a while an report the failures as they happen in this ticket. Do you agree with our aproach?

Sure, I agree with that. Please updated if you have any finding thanks!
