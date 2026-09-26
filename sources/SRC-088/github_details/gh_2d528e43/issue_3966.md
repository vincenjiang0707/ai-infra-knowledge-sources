# [Issue #3966] leaderboard_math: exact_match_stderr published as exactly 0.0 for scores strictly between 0 and 1

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3966
state: open | updated: 2026-08-04T17:56:20Z
labels: 

## 正文

Some published Open LLM Leaderboard result files report `exact_match_stderr,none` as exactly `0.0`
for `leaderboard_math_*` subtasks whose score is strictly between 0 and 1.

`exact_match` isn't in the `bootstrappable` list, so `stderr_for_metric` returns `mean_stderr`:

```python
def mean_stderr(arr):
    return sample_stddev(arr) / math.sqrt(len(arr))
```

For a 0/1 score vector that is `sqrt(p(1-p)/(n-1))`, and it can only be `0` when every item score is
identical — i.e. when the score is exactly 0 or exactly 1. So a record with a score of 0.86 and a
stderr of 0.0 is internally inconsistent: those two numbers can't have come from the same vector.

### Example

`CombinHorizon/huihui-ai-abliterated-Qwen2.5-32B-Inst-BaseMerge-TIES`,
`results_2025-02-13T18-27-04.338360.json` — all seven MATH subtasks:

| subtask | n | k | score | published stderr | `sqrt(p(1-p)/(n-1))` |
|---|---|---|---|---|---|
| algebra_hard | 307 | 263 | 0.856678 | **0.0** | 0.020031 |
| prealgebra_hard | 193 | 152 | 0.787565 | **0.0** | 0.029519 |
| num_theory_hard | 154 | 109 | 0.707792 | **0.0** | 0.036767 |
| counting_and_prob_hard | 123 | 71 | 0.577236 | **0.0** | 0.044725 |
| geometry_hard | 132 | 58 | 0.439394 | **0.0** | 0.043363 |
| precalculus_hard | 135 | 47 | 0.348148 | **0.0** | 0.041153 |
| intermediate_algebra_hard | 280 | 87 | 0.310714 | **0.0** | 0.027706 |

The same model's earlier file (`results_2024-12-07T...`) has 0.000000 on every MATH subtask with a
stderr of 0.0, which is correct — the scores really are all-zero there. The later run produced real
scores but kept the zero stderrs.

### Extent

Across 60 sampled models in `open-llm-leaderboard/results`, **56 (model, task, metric) records have a
score strictly between 0 and 1 and a stderr of exactly 0.0. All 56 are `leaderboard_math_*`
`exact_match`; 11 of the 60 models are affected**, usually on 5–7 of their 7 MATH subtasks. No other
task family shows it — for `bbh`, `gpqa`, `musr`, `mmlu` and `ifeval` the published stderr matches
`sqrt(p(1-p)/(n-1))` exactly.

### Reproduce

```python
import json, math, urllib.request, urllib.parse

p = ("CombinHorizon/huihui-ai-abliterated-Qwen2.5-32B-Inst-BaseMerge-TIES/"
     "results_2025-02-13T18-27-04.338360.json")
u = ("https://huggingface.co/datasets/open-llm-leaderboard/results/resolve/main/"
     + urllib.parse.quote(p))
d = json.loads(urllib.request.urlopen(u).read())
ns, groups = d["n-samples"], set(d.get("group_subtasks") or {})

for t, v in d["results"].items():
    if not t.startswith("leaderboard_math") or t in groups or t not in ns:
        continue
    n = ns[t].get("effective") or ns[t].get("original")
    s, se = v["exact_match,none"], v["exact_match_stderr,none"]
    print(f"{t:44s} n={n:4d} score={s:.6f} stderr={se} "
          f"closed_form={math.sqrt(s*(1-s)/(n-1)):.6f}")
```

I haven't been able to tell from the artifacts alone whether the zero is written by the harness or
somewhere in the leaderboard's pipeline — `stderr_for_metric` returns `None` when
`bootstrap_iters <= 0`, which would show as a missing field rather than `0.0`, so it doesn't look
like that path. Happy to dig further if it's useful to have more cases listed.


## 评论 (4)

### ipezygj · 2026-07-30

Widened the sample, since the original numbers came from only 60 models.

**420 models sampled from `open-llm-leaderboard/results` (latest results file per model): 107 affected
(25.5%), 423 records with a score strictly between 0 and 1 and a stderr of exactly `0.0`.**

All 423 are still `leaderboard_math_*` `exact_match` — no other task family produces one at this
sample size either. Affected models usually have several of their seven MATH subtasks hit; 23 of the
107 have all seven.

### It appears to stop in early February 2025

Grouping every dated result file I have by run month:

| month | affected | total | share |
|---|---|---|---|
| 2024-06 | 10 | 27 | 37.0% |
| 2024-07 | 7 | 28 | 25.0% |
| 2024-08 | 4 | 24 | 16.7% |
| 2024-09 | 16 | 47 | 34.0% |
| 2024-10 | 11 | 45 | 24.4% |
| 2024-11 | 9 | 42 | 21.4% |
| 2024-12 | 21 | 67 | 31.3% |
| 2025-01 | 29 | 94 | 30.9% |
| 2025-02 | 9 | 77 | 11.7% |
| **2025-03** | **0** | **23** | **0.0%** |

The last affected run in the sample is dated **2025-02-06**; the newest run of any kind is
2025-03-13. If the rate were still ~25%, seeing 0 of 23 would be about a 0.1% event, so this looks
like a real change rather than thin data — though 23 runs is not many, and I'd treat the exact date as
approximate.

`transformers_version` splits the same way, which I'd read as a proxy for run date rather than a
cause: 0/31 on 4.48.3 and 0/22 on 4.49.0, against 29/76 on 4.47.0, 21/87 on 4.48.0 and 14/45 on
4.44.2.

If it was fixed, the ~423 affected records already published still carry `0.0`, so anything consuming
those files for uncertainty (or filtering on stderr) will read them as exact.


### ipezygj · 2026-07-30

One more thing worth knowing: **the zeros propagate to the group row.**

On groups with no zero subtask, the published `leaderboard_math_hard` stderr is reproduced by
combining the children's own stderrs in quadrature with sample weights — 342 of 342 — and not by
pooling item scores (12 of 342). So a subtask whose stderr is `0.0` contributes zero variance, and a
group whose subtasks are all zero comes out zero as well.

That is what happens. Of 116 model/group rows with at least one zero subtask, **51 publish a
`leaderboard_math_hard` stderr of exactly 0.0** while the group score is not 0.

Example, `ehristoforu/trd-7b-it`, `results_2025-02-13T18-27-04.338360.json`:

```
leaderboard_math_hard        score=0.031722   stderr=0.0

  algebra_hard               n=307  k= 14  score=0.045603  stderr=0.0   closed-form=0.011926
  counting_and_prob_hard     n=123  k=  2  score=0.016260  stderr=0.0   closed-form=0.011450
  geometry_hard              n=132  k=  2  score=0.015152  stderr=0.0   closed-form=0.010673
  intermediate_algebra_hard  n=280  k=  5  score=0.017857  stderr=0.0   closed-form=0.007929
  num_theory_hard            n=154  k=  8  score=0.051948  stderr=0.0   closed-form=0.017941
  prealgebra_hard            n=193  k=  8  score=0.041451  stderr=0.0   closed-form=0.014385
  precalculus_hard           n=135  k=  3  score=0.022222  stderr=0.0   closed-form=0.012734
```

Every subtask has solved instances, so none of these zeros is the legitimate all-wrong case. (I did
check that separately: of the 64 groups I found with a zero stderr, all 64 have every child at zero,
so nothing here contradicts the combination rule — 13 of them are the genuine case where the model
scored 0 everywhere.)

Practical effect: a group-level MATH number is published as if it had no sampling uncertainty at all.
Anything that reads `leaderboard_math_hard`'s stderr — for error bars, or for a significance test
between two models — gets zero rather than a missing value, which is the failure mode that doesn't
announce itself.


### ipezygj · 2026-08-01

Following up with a check against current `main` (`f4d4b3de`), because it changes whether this is actionable here.

**The harness side looks already fixed.** Three things I verified:

**1. `mean_stderr` is correct on the exact example above.** Reconstructing the `algebra_hard` vector (n=307, k=263) and running the repo's own `mean` / `mean_stderr`:

```
score              = 0.856678
mean_stderr        = 0.020031
sqrt(p(1-p)/(n-1)) = 0.020031
```

So the metric function reproduces the value the report expects, to six decimals.

**2. When no stderr function is available the harness writes the string `"N/A"`, never `0.0`** — `lm_eval/evaluator_utils.py`:

```python
if isinstance(bootstrap_iters, int) and bootstrap_iters > 0:
    stderr_fn = stderr_for_metric(...)
    agg_metrics[f"{metric}_stderr,{filter_key}"] = (
        stderr_fn(items) if (stderr_fn and len(items) > 1) else "N/A"
    )
else:
    agg_metrics[f"{metric}_stderr,{filter_key}"] = "N/A"
```

`stderr_for_metric(mean, bootstrap_iters=0)` returns `None`, which lands in the `"N/A"` branch rather than being coerced to a number.

**3. Group aggregation guards against it rather than pooling it** — `lm_eval/api/group.py`:

```python
if len(stderrs) == len(values) and "N/A" not in stderrs:
    group_metrics[stderr_key] = pooled_sample_stderr(stderrs, sizes)
else:
    group_metrics[stderr_key] = "N/A"
```

So I don't think current `main` can emit a `0.0` stderr next to a score strictly between 0 and 1, and the "51 group rows inherit the zero" path is guarded too.

I could **not** identify which change fixed it, and I have not established what produced the zeros in the first place — the affected result files are from early 2025 and I only fetched recent history. So this is an observation about current behaviour, not a diagnosis. **If a maintainer can confirm, this can be closed as already fixed.**

---

One thing that is *not* fixed by that, flagged only so the two don't get conflated when this closes: **the published records still contain the impossible values.** Downloading those files from `open-llm-leaderboard/results` today still gives a score of 0.857 with a stderr of 0.0, so anything deriving confidence intervals from that dataset inherits it. That is a leaderboard-data question rather than a harness one, and I'll raise it on that side.


### ipezygj · 2026-08-04

Closing the loop on my own report, since the answer turned out not to be here.

Two facts settle it:

1. **The harness is not the source.** As posted above, current `main` writes `"N/A"` rather than `0.0` when no stderr function is available, and group aggregation refuses to pool when any child is `"N/A"`. I could not construct a path on `main` that emits `0.0` beside a score strictly between 0 and 1.

2. **The affected data is frozen.** `open-llm-leaderboard/results` has `lastModified` 2025-03-15 and is no longer updated, so the 423 records are a static artefact of an older harness rather than something a fix here would reach.

That leaves the exposure entirely on the consumer side — the dataset still shows ~22k downloads, and 25.5% of the models I sampled carry an interior score with a stderr of exactly 0.0, which silently reads as "measured with perfect precision" to anything that averages or filters on error bars.

So there is nothing actionable in this repository and I'd suggest closing it. Thanks for the harness, and apologies for the noise — the check that produced this is more useful pointed at published results than at the code that produced them.

