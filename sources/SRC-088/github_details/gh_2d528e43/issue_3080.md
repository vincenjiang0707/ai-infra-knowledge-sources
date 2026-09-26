# [Issue #3080] Fix Metric Calculation for Repeats

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3080
state: open | updated: 2026-08-16T06:22:41Z
labels: 

## 正文

Currently, the harness has a limitation in how it handles repeated outputs (multiple generations per sample). The existing system:

1. Tasks default to `take_first` filter if no filters are specified in config.
2. Metrics expect exactly one result per sample.
3. Repeats are expected to be handled in the filter pipeline (with the last filter typically being `take_first`).
4. Currently `take_first` needs to be the last filter for all filter pipelines (not just repeats).
5. The only way to handle multiple outputs per sample is to either use a custom metric (see [humaneval](https://github.com/EleutherAI/lm-evaluation-harness/blob/8bc46207618d5dc4a29edfd79e7da8c66bfebe9f/lm_eval/tasks/humaneval/utils.py#L13)) or override  `process_results()` with custom logic.

This design works for some repeat-based calculations like majority voting (since the filter can process all repeats and output a single result), but fails for metrics like pass@N that require the metric to be calculated on each repeat first, then aggregated later:

This makes it difficult to:
- Calculate metrics on each repeat/generation separately  
- Support pass@N style evaluation where you need metric scores per repeat

## Current Behavior

```
Sample → Multiple Outputs → filters -> take_first filter → Single Output → process_results → Metric
```

The `take_first` filter discards all but the first output.

## Fix

The metric calculation per sample is calculated in `evaluator.py` here:
https://github.com/EleutherAI/lm-evaluation-harness/blob/8bc46207618d5dc4a29edfd79e7da8c66bfebe9f/lm_eval/evaluator.py#L616-L617

however we might want to refactor this to a ConfigurableClass method.

We will also need to make modifications downstream:
- extend TaskOutput.calculate_aggregate_metric()  to support calculating metrics on each repeat individually, then aggregating those metric scores rather than aggregating raw outputs.
- allow metrics/task configs to specify aggregation strategies (max, mean, pass_at_n, etc.) for handling multiple metric values per sample.


 

## 评论 (6)

### Avelina9X · 2025-07-04

Alright so correct me if I'm wrong but there are actually two (or 3) types of aggregation strategy plus a bonus one:
1. for each (gold, [result * repeats]) we may want to aggregate by max/mean/pass_at_n/etc to get a per instance metric *before* accumulating the metrics across all samples as the metric we may be using might not actually work for multiple results.
2. for all [(all_gold, all_results[0]), ..., (all_gold, all_results[repeats-1])] we may want to accumulate metrics first and then aggregate by max/mean/pass_at_n/etc *after*.
3. (some weird combination of the two that needs to consider all results. Might be needed for pass@N?)

We would need to make changes to `ConfigurableTask.process_results()` such that if we're trying to use a metric that doesn't account for repeats we unwrap all results in the list, compute the metric on each gold+result[i] for all i, and then store a list of the metric values rather than a scalar.

Next we need to change `TaskOutput.calculate_aggregate_metric()` to account for lists instead of scalars for the metric and then depending on if we're doing (1) or (2) we do either do repeat_agg->metric_agg or metric_agg->repeat_agg. (For (3) we might needs something more complex.)

We should add additional fields to `ConfigurableTask` to determine if we want to do this repeat aggregation, and if perform it before or after (or determined by whatever (3) does), and for the actual repeat aggregations we can just re-use/register new aggregations in metrics.py.

### raspberryice · 2025-07-10

Thanks for picking this up! 
I've been implementing my own pass@k metric by overwriting the take_first filter with something like take_all and then using a custom process_results function. 

### owos · 2025-08-14

> Thanks for picking this up! I've been implementing my own pass@k metric by overwriting the take_first filter with something like take_all and then using a custom process_results function.

how exactly are you doing this?
I am currently interested in evaluating with pass@K too.

### fxmarty-amd · 2026-03-24

@baberabb this is not fixed, right? It seems like despite `repeats: xx` being higher than 1, the reported metrics correspond to a single run due to `take_first`

### fxmarty-amd · 2026-03-24

Shouldn't reported metrics be computing the mean of `pass@1` ? If I set `repeats: 10`, I expect to get the average metric over 10 runs.

### azrabano23 · 2026-08-16

I'd like to pick this up if no one is on it. I read through the current code paths and want to agree on a design before writing a PR. This is roughly Avelina's option (1): a per-instance aggregation stage between the filter pipeline and cross-sample aggregation.

**Where it hooks in.** Today `evaluate()` clones each request `req.repeats` times, the filter pipeline collapses `inst.resps` into `inst.filtered_resps[key]` (default `take_first`, built in `ConfigurableTask.__init__`), `process_results` assumes a single result in `results[0]` for `generate_until`, and `_compute_task_aggregations` in `evaluator_utils.py` reduces per-sample scalars with `task.aggregation()[metric]`.

Proposal: an optional per-metric key in `metric_list`:

```yaml
metric_list:
  - metric: exact_match
    repeats_aggregation: pass_at_k   # or: first | mean | max | callable
    k: [1, 10]
```

Semantics, in the `generate_until` branch of `process_results`: if `repeats_aggregation` is set, apply the metric to each element of the per-doc repeats list to get per-repeat scores, then reduce within the instance. `first` takes score[0], `mean`/`max` are the obvious reductions, and `pass_at_k` computes the unbiased estimator from Chen et al. 2021 (`1 - C(n-c, k)/C(n, k)` in stable product form, n = repeats, c = passing repeats), emitting a `pass@k` entry per k. Each instance still contributes scalars to `result_dict`, so `_compute_task_aggregations`, bootstrap stderr, and sample logging work unchanged.

**Filters and backward compatibility.** When any metric sets `repeats_aggregation` and no `filter_list` is given, the default pipeline becomes take-all instead of `take_first`, so repeats reach the metric. When the key is absent, nothing changes: existing configs, the `take_first` default, and humaneval's custom-filter-plus-callable approach are untouched. `first` must reproduce today's numbers exactly, which doubles as the regression test.

**Tests.** Estimator unit tests against brute-force enumeration over all C(n, k) subsets; an end-to-end dummy `generate_until` task with `repeats: n` checking first/mean/max/pass@k against hand-computed values; a parity test that configs without the key produce identical results.

I've implemented the unbiased pass@k estimator before, so that piece is low-risk. Happy to put this up as a PR if the direction looks right. @baberabb, any constraints I should design around? In particular, does the #3083 refactor plan to move per-sample metric computation out of `process_results`? I'd rather build on the intended shape than add to what's being streamlined.

