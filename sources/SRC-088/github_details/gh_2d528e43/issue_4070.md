# [Issue #4070] At 0 (or 100%) accuracy the reported stderr is exactly 0.0 at any N, so null results claim infinite precision; a boundary-aware interval or flag would fix it

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4070
state: open | updated: 2026-09-13T01:14:22Z
labels: 

## 正文


## Summary

`mean_stderr` returns 0.0 for an all-zero score vector at any sample size, and
`bootstrap_stderr` agrees, because every resample of zeros is zeros. End to end, a model
that scores 0 on a task is reported as `0.0 +- 0.0000`: a 25-question run and a
5000-question run claim identical, infinite certainty that the capability is absent. The
same holds symmetrically at perfect scores. This is expected behavior of CLT/Wald
standard errors at the boundary, but the harness's numbers are quoted directly in model
cards and leaderboards, where `+- 0.0000` reads as precision rather than as a degenerate
estimator.

## Relation to open issues

#3966 documents stderr = 0.0 for scores strictly between 0 and 1 and correctly concludes
those records are internally inconsistent; its analysis notes in passing that stderr can
only legitimately be 0 "when the score is exactly 0 or exactly 1". This report is about
that remaining, legitimate case: the value is internally consistent and still the wrong
thing to publish, because at the boundary the estimator degenerates exactly where the
claim (capability absent, or saturated) is strongest. #4017 and #4019 propose Wilson CIs
at the output layer; the boundary case here is arguably the sharpest argument for them,
since it is where the missing interval is not merely narrow but absent entirely.

## Reproduction

lm-eval 0.4.12 (release) and 0.4.13.dev0 (current main), Python 3.13.14, macOS. Unit
level, identical on both versions:

| input | mean_stderr |
|-------|-------------|
| 0/10 | 0.0 |
| 0/25 | 0.0 |
| 0/100 | 0.0 |
| 0/1000 | 0.0 |
| 0/5000 | 0.0 |
| 517/1000 control | 0.0158 (correct) |
| bootstrap_stderr, 0/1000, 1000 iters | 0.0 |

End to end:

```python
res = lm_eval.simple_evaluate(model="dummy", tasks=["gsm8k"], limit=25, random_seed=0)
# results.gsm8k: exact_match 0.0, exact_match_stderr 0.0 (both filters)
```

## Why this matters

1. The null result is the case that matters for capability rule-outs, and it is the one
   case where the reported uncertainty is maximally wrong: the true 95% upper bound at
   0/25 is about 13.7% (Clopper-Pearson) or 9.5% (Jeffreys), not 0.
2. Sample size becomes invisible exactly at the boundary. Downstream readers cannot
   distinguish a cheap null from an exhaustive one, though the two support very
   different claims.
3. Aggregations inherit the zero: pooled and combined stderrs over subtasks treat a
   boundary subtask as contributing zero variance, tightening group intervals.

## Possible directions

- Report a one-sided Jeffreys or Wilson bound when a metric sits exactly on a boundary
  (the rule of three, 3/N, is the crude version and costs one line). If the Wilson CI
  proposal in #4017/#4019 lands, the boundary case comes for free and this issue reduces
  to a test case for it.
- Or leave the stderr as is but emit a boundary flag column so tables can render
  `0.0 (<= 0.095 at 95%)` instead of `0.0 +- 0.0`.
- Either change is metric-layer only and touches no task definitions.

Happy to PR either variant with tests if there is appetite.


## 评论 (2)

### fabio-rovai · 2026-08-31

Adding a data point on real-world prevalence, since the issue as filed only showed synthetic runs.

The published Open LLM Leaderboard results files already contain this behavior. The file for openai-community/gpt2 publishes four rows of `exact_match 0.0` with `exact_match_stderr 0.0` on `leaderboard_math_*_hard` subtasks, with n = 123, 132, 280 and 135: four null results at four different sample sizes, all claiming identical zero uncertainty, where the 95% upper bounds actually differ by a factor of ~2.5 (about 0.030 at n=123 vs 0.011 at n=280).

A random sample of 96 models from the results dataset finds 23 models (24%) publishing at least one boundary row with stderr exactly 0.0, 67 such rows in the sample, including the symmetric perfect-score case (`acc_norm 1.0` with stderr `0.0`). Sweep script is a single file and I am happy to share it.


### buyan201430-code · 2026-09-13

Additional check of published result files.

I scanned 100 randomly sampled result files from `open-llm-leaderboard/results` (revision `aa81ecc38fdc5708254b833923368970efdf5ef5`, seed 1, all 100 fetched on 2026-09-13) for rows where the metric is exactly 0.0 or 1.0 and the reported stderr is exactly 0.0 (filter `none`; n taken from `n-samples.effective`).

- 31/100 files contained at least one matching row; 115 matching rows in total (per-task breakdown is in the CSV).
- Published files also contain three matching rows with `acc_norm = 1.0` on `leaderboard_bbh_temporal_sequences` (n = 250).
- 18 matching rows are group-level entries (`leaderboard`: 10; `leaderboard_math_hard`: 8).

Script, per-row CSV, pinned dataset revision, and the sampled file list: https://gist.github.com/buyan201430-code/1a1185b4bee51d17e2db84b1aae06fe3

