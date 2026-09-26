# [Issue #1648] perf(multi-turn): warmup still drains before the measured window, and benchmark conversations pay a cold first turn

source: https://github.com/modelscope/evalscope/issues/1648
state: open | updated: 2026-08-30T00:08:33Z
labels: 

## 正文

## Problem

`MultiTurnStrategy.run()` still runs warmup as a separate phase that completes in full before any benchmark conversation starts:

```python
# Two-phase dispatch: warmup conversations complete in full before any
# benchmark conversation starts.  ``_conv_index`` persists across
# phases so warmup and benchmark pull disjoint conversations from the
# dataset (first ``warmup_count`` vs. the rest).
```

That is the same defect #1641 fixed for the single-turn closed-loop path: the barrier drains server occupancy to zero, so the measured phase releases its first `parallel` requests within one event-loop tick against an idle server. Their TTFT carries a start-up burst that never recurs, and the reported percentiles treat that mixture as one distribution. On single-turn this overstated `p99` by **4.19x** (measured: 1609 ms reported vs 384 ms steady-state).

Multi-turn has a second, independent problem that single-turn does not: warmup and benchmark pull **disjoint** conversations, so every benchmark conversation still pays a cold first-turn prefill inside the measured window.

## Proposed direction

Two layers, mirroring what upstream vLLM does in `benchmarks/multi_turn/benchmark_serving_multi_turn.py`:

1. **No barrier between warmup and the measured portion**, as in #1641 — each warmup completion hands its slot to a measured request instead of draining first.
2. **First-turn warmup semantics**: warmup sends only the first turn of each conversation and writes the real reply back into the context; the benchmark phase then reuses the same conversations starting from turn 2. Cold prefill lands entirely in the un-measured warmup. Upstream does this with `client_args._replace(skip_first_turn=False, max_turns=1)` followed by reusing the returned conversations.

Note that (2) only pays off when the server has prefix caching enabled; without it the turn-2 prompt is longer and the burst can be worse. That trade-off needs to be stated wherever it is documented.

## Explicitly not the fix

Staggering the worker spawn across a ramp window (proposed in #1547) was evaluated and rejected. It trades a burst at the start of the measured window for an under-loaded stretch *inside* it, and upstream vLLM has no spawn stagger in either `serve.py` or its multi-turn benchmark. Details in #1547.


## 评论 (1)

### linhongyu510 · 2026-08-30

I traced the current `MultiTurnStrategy` on latest `main`. The two reported behaviors are still explicit in the implementation: `run()` awaits a complete warmup `_run_phase()` before starting the benchmark phase, and `_conv_index` advances across phases so benchmark workers consume different conversations with fresh contexts.

The no-barrier handoff looks independently safe to test with a deterministic fake client. The first-turn reuse part needs one product decision before I prepare a patch: should reusing warmed conversations from turn 2 be the default whenever `warmup_num > 0`, or should it be opt-in because it can make results worse when the target server has no prefix cache?

I would keep the change focused on `MultiTurnStrategy` and add offline tests for:

- no occupancy drain between warmup and measured work;
- first-turn responses being carried into the measured conversation context;
- warmup metrics remaining excluded;
- `warmup_count < parallel`, zero warmup, `max_turns=1`, and failed warmup turns;
- the selected no-prefix-cache behavior.

I will wait for the intended default/flag semantics before changing the scheduler.
