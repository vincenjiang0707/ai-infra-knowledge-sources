# [Issue #4062] Unscorable samples silently leave the metric denominator, inflating headline scores

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4062
state: open | updated: 2026-09-04T02:02:26Z
labels: 

## 正文

## Summary

`lm_eval/evaluator.py` evaluate() collects metrics like this:

```python
metrics = task.process_results(doc, [req.filtered_resps[filter_key] for req in requests])
...
for metric, value in metrics.items():
    acc["raw_metrics"][(metric, filter_key)].append(value)
```

If a task's `process_results` returns an empty dict, or omits a metric key, for a given document (a natural way for a task author to say "could not score this one": refusal, unparseable answer, empty extraction), that document contributes to no metric and the aggregate is a mean over the surviving documents only. Nothing warns, nothing counts the dropped documents per metric, and `n-samples.effective` in the results is computed in `_compute_task_aggregations` as the length of the LAST metric's list (the code carries a TODO admitting this), so with heterogeneous keys even the reported effective count is the wrong number for the other metrics.

The score inflation is structural: whatever a model does to make itself unscorable is removed from the average rather than counted against it.

## Steps to reproduce

PoC (end-to-end through `lm_eval.evaluator.evaluate`, dummy LM, identical outputs in both runs): `poc_unscorable_denominator.py`

Six documents; the dummy model refuses on 2 and answers 4. The same model outputs are scored twice, differing only in the task's `process_results` convention. Observed (PROVED, run twice, byte-identical output):

```
model behavior: 2/6 docs refused (unscorable), 4/6 answered
[A: return empty dict for unscorable] acc=1.0  n-samples={'original': 6, 'effective': 4}
[B: return 0 for unscorable] acc=0.6666666666666666  n-samples={'original': 6, 'effective': 6}
RESULT: identical outputs, headline acc differs: True (1.0 vs 0.6666666666666666)
VERDICT: VULNERABLE
```

## Impact

Headline accuracy can be inflated by exactly the documents a model fails to answer in a scorable way. Two tasks measuring identical model behavior can differ by the scoring convention alone, and consumers of the results file have no per-metric dropped-count to detect it. Group aggregation compounds this: `Group.aggregate` weights subtasks by the reported `sample_len`, which inherits the same last-metric count. Any task family that maps refusals or parse failures to an empty result (a pattern the process_results contract makes natural) is affected.

## Suggested fix

Track denominators explicitly per (metric, filter): count evaluated documents per metric, count documents for which the metric was omitted, and report both (for example `n-samples: {original, effective, unscorable_per_metric}`) plus a warning when effective < original for any metric. Fix `sample_len` to be per metric rather than the last metric's length. Longer term, make the could-not-score case an explicit typed value in process_results rather than key omission.

## References

- PoC script: `poc_unscorable_denominator.py` (double-run REPRO: `REPRO-E1-F4.sh`, byte-identical)
- Pinned code: EleutherAI/lm-evaluation-harness @ 0f8479cc83a1b9652294d1c0257d22c7756155ec, lm_eval/evaluator.py lines 636 to 669, lm_eval/evaluator_utils.py `_compute_task_aggregations` lines 173 to 219 (sample_len TODO at line 204), lm_eval/api/group.py aggregate() lines 242 to 292


## 评论 (9)

### linhongyu510 · 2026-08-29

I would like to investigate this, but the scoring contract needs maintainer direction before implementation. A conservative first patch could preserve current aggregation values while adding an offline regression for heterogeneous metric keys, tracking effective counts per `(metric, filter)`, and emitting a warning when a document omits an expected metric. That would make denominator shrinkage visible without silently treating a missing metric as zero or changing existing task scores. Should the first patch stay within that observability boundary, or do maintainers want omission to become an explicit scoring value/error instead? I will hold off on code until the intended contract is confirmed.

### arthi-arumugam-git · 2026-08-31

I opened #4068 for one narrow piece of this, the `n-samples.effective` part, and deliberately left the scoring contract alone.

`sample_len = len(items)` sits inside the loop over metrics, so the reported count is whichever metric came last. With heterogeneous keys that makes it depend on dict ordering: the same raw metrics report 1 or 3 depending only on which key is first. #4068 takes the largest per-metric count instead, which is the number of documents that produced any metric at all, and is unchanged when every metric holds the same number of values.

That is only the reported count. It does not answer the larger question here, which is whether a document that drops out of a metric should be surfaced at all, and where. @linhongyu510 I think you are right that the aggregation semantics need maintainer direction before anyone changes them, and I have not touched them.


### AUTHENSOR · 2026-09-02

Thank you for the 0.4.13 fix to the effective-sample reporting. Re-checked today (b954108): the reporting half is fixed; the scoring-contract half still reproduces on identical outputs (mean 1.0 over 5 survivors where an honest judge reports 0.5 over 10). Reproduction harness available.

### arthi-arumugam-git · 2026-09-03

The reporting half landed in #4068. I left the scoring half alone on purpose, because it changes what a task's score means and that felt like a maintainer call rather than mine.

Since it still reproduces, here is the shape I would suggest, if it is useful.

The ambiguity is that an omitted metric key currently means two different things and the code cannot tell them apart: "this document was not applicable to this metric", and "this document could not be scored". The first arguably should leave the denominator. The second should not, or the mean quietly reports the score of only the samples that behaved.

A conservative version that changes no existing task's numbers: leave aggregation as it is, but track per `(metric, filter)` how many documents were expected against how many produced a value, and surface both in the results. Any task where those two differ becomes visible instead of silent, and a task author who wants omission to count as a failure can then opt into that explicitly rather than by accident.

Happy to open that if it is wanted, or to leave it if you would rather settle the contract first.


### AUTHENSOR · 2026-09-03

Thank you for the clear split on what landed vs what you deliberately left. Your proposed shape (distinguishing a missing metric key from an omitted one) is exactly the right axis: the reporting fix in #4068 addressed the counting half, but the scoring half needs the maintainers to decide what an absent metric key means for a task's aggregate. From our reproduction harness, the two states that matter are: all metrics present but one scores 0 vs one metric key absent entirely (the current code cannot distinguish them downstream). Happy to share the harness if it would help the design discussion.

### arthi-arumugam-git · 2026-09-03

Yes please, the harness would be useful, particularly if it covers both states rather than only the second.

To put the decision in one place: the reason the two cases cannot be told apart downstream is this loop,

```python
for metric, value in metrics.items():
    acc["raw_metrics"][(metric, filter_key)].append(value)
```

The append only runs for keys `process_results` actually returned. A key omitted for this document and a key that never applied to the task leave the same trace, which is none, so by aggregation time there is nothing left to branch on.

The information is not entirely lost, though. When `log_samples` is on, each logged example already stores `"metrics": list(metrics.keys())`, so the per-document key set does exist on that path. It just never reaches `raw_metrics`.

That leaves three possible contracts, and I think it is a one-line answer rather than a design discussion:

1. Omission means not applicable. Current behaviour: the mean is over the documents that produced the metric, so a task that drops half its documents reports the score of the half that survived.
2. Omission means unscored, excluded but counted. Aggregate values stay exactly as they are today, and expected against produced counts per `(metric, filter)` get reported alongside, so the shrinkage is visible. Nothing changes, it just stops being silent. Close to what @linhongyu510 proposed above.
3. Omission means failure, and the document counts as a zero. This one moves published numbers for any task that omits keys.

@baberabb, 2 is the only one that changes no existing task's score, so it looks like the safe default. Happy to open it, with the harness as the regression if AUTHENSOR is willing to share it. 1 or 3 are equally easy to build, they just need the call.


### AUTHENSOR · 2026-09-03

Harness shared: https://gist.github.com/AUTHENSOR/b3bbc2b38c7e2e8e186d6fb2f7154d13 (single file, deterministic across runs, no network or model inference, verified on b954108).

It covers both states, on identical model outputs (2 of 6 docs refuse):

- state 1, metric key absent (empty dict for unscorable docs): `acc=1.0`, `n-samples={'original': 6, 'effective': 4}`
- state 2, key present scoring 0: `acc=0.6666666666666666`

The same outputs grade 1.0 or 0.67 depending only on the task author's convention, and nothing downstream can tell which convention produced the number.

There is also a third run in the gist that may be useful for the contract 2 shape: one task, two metrics, where unscorable docs keep `acc` but omit `f1`. The same run aggregates acc over 6 and f1 over 4:

```
acc=0.6666666666666666 (every doc scored)
f1 =1.0 (unscorable docs silently left the f1 denominator)
logged per-doc key sets on the log_samples path: [('acc', 'f1'), ('acc',), ('acc', 'f1'), ('acc', 'f1'), ('acc',), ('acc', 'f1')]
```

That last line confirms the recovery path you identified: the per-document key set does exist on the log_samples path, so expected-vs-produced per (metric, filter) counts are derivable exactly there.

One thing the runs surfaced that I did not expect: current main already warns on the within-task divergence case (state 3 prints `Metrics were not scored on the same number of documents (acc,none=6, f1,none=4)`), but states 1 and 2 both run silent, because when every metric drops together there is no divergence left to detect. The silent case is the one that moves the headline number, which is another argument for the per-(metric, filter) counts over a divergence heuristic.

Happy for you to use it as the regression if contract 2 gets the call. States 1 and 2 are the assertion pair; state 3 is the reporting case.


### arthi-arumugam-git · 2026-09-04

That is a more thorough harness than I expected, thank you. The third run also settles the cost question: since the per-document key sets are already recorded on the `log_samples` path, contract 2 needs no new bookkeeping during evaluation, only for those counts to survive into aggregation.

The divergence finding is the part that changes the shape of the ask, though.

If main already prints `Metrics were not scored on the same number of documents` for the within-task case, then this repo has already decided that a shrinking denominator is worth telling the user about. On that reading contract 2 is not a new policy at all. It is the existing policy applied to the case the current heuristic structurally cannot see: when every metric drops the same document, divergence is zero, the warning goes quiet, and that is precisely the run where the headline number moves.

So the decision may be smaller than I made it sound. Not "what should an absent key mean", but "should the existing warning also cover the case it currently misses". The first is a semantics debate. The second is finishing something already started, and it still changes nobody's published numbers.


### arthi-arumugam-git · 2026-09-04

Opened #4092 with contract 2, so there is something concrete to accept or reject rather than a decision to make in the abstract. It is small and easy to close if you would rather settle the semantics a different way first.

It carries the per-`(metric, filter)` counts into `n-samples` as `per_metric`. They were already being computed for the divergence warning and then thrown away, and groups already report the same shape under `sample_count`, so tasks were the odd one out. No aggregate value changes.

@AUTHENSOR I ran your harness against the branch. State 3 now reports `per_metric: {"acc,none": 6, "f1,none": 4}` where before it showed only `effective: 6`, and state 1 reports `{"acc,none": 4}`. All three scores are byte for byte what they were: `1.0`, `0.667`, `1.0`. Credited you in the PR body; say the word if you would rather I did not.

Worth being explicit that this does not answer the question the issue actually asks. The same outputs still grade 1.0 or 0.667 depending on the task's convention. It only makes the denominator visible so the ambiguity stops being silent. The semantics are still yours to decide, and #4092 does not prejudge them.

