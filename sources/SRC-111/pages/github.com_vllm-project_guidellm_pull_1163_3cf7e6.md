source: https://github.com/vllm-project/guidellm/pull/1163

## Conversation


[QHarshil](https://github.com/QHarshil)changed the title

Sep 19, 2026


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 23, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

I like this, and it seems to work; however I'm uncomfortable with the model of dynamically shuffling CSV columns. While retaining column compatibility is a good thing, I'm not sure this is the best approach.

Every statistic in a report is an estimate from a finite number of requests, and nothing in the output says how precisely it was measured. The percentiles are order statistics, so p99 sits at rank ceil(0.99n). Below 100 successful requests that rank is n, and the reported p99 is the slowest single request, printed with the same authority as the mean. Across twelve identical ten second runs against the mock server the reported p99 varied by 23.5% while the mean varied by 8.5%. DistributionSummary now carries an interval for the mean and one for each percentile, at a level set through --metrics and recorded once per benchmark. A percentile interval is null where the sample cannot place two order statistics around it, which takes 72 requests for p95, 368 for p99 and 3688 for p999. Reporting null there is the point: it marks the percentiles a short run cannot support. The console marks such a percentile rather than printing it as though it were measured. Intervals are attached only to distributions holding one unweighted observation per request. Time per output token and inter-token latency stay point estimates because, in a repeated-run variable-load experiment, their within-run intervals understated observed run-to-run variation by 1.8x and 3.2x respectively. The measurements were associated with a shared run-level load condition that a single-run request-sampling interval cannot observe. Derived rate distributions are excluded separately: their time-weighted construction does not meet the estimator's request-sample assumption, and that construction is itself under discussion in[vllm-project#602]. The estimator rejects any weight other than one, so a later caller cannot opt an unsupported distribution into inference. The quantile functions and interval estimators move to a shared module, which removes an import of approx_t_ppf from a scheduler constraint into a benchmark profile. approx_t_ppf moves unchanged with a re-export left behind, and wilson_interval keeps deriving its quantile from it rather than from the exact normal quantile. The two differ by 2.2e-4, enough to move a Wilson upper bound of exactly 1.0 to just below it and turn a goodput probe that met a 100% attainment target into one that missed it. New inference uses an accurate t quantile, since the approximation is 49% low at one degree of freedom and 6% low at three. Assisted-by: Claude Code claude-opus-5 Signed-off-by: QHarshil <harshil_c@hotmail.com>

The interval columns were written beside each metric and then moved to the end of the row by matching header names, so the code that wrote a column no longer said where it went, and any later column with a matching name would have been moved too. They are now written by one method called after every other column, listing only the metrics that carry intervals. Listing them explicitly also drops the columns that could never hold a value. Every distribution used to get Mean CI and Percentile CIs, including time per output token, inter-token latency and the rate metrics, which never carry an interval. On a 107 request run that took the addition from 95 columns to 27, with the 238 existing columns and every populated interval value unchanged. The percentile intervals are now read with model_dump rather than getattr, and a code comment points at the metrics guide's new location under docs/en. Assisted-by: Claude Code claude-opus-5 Signed-off-by: QHarshil <harshil_c@hotmail.com>

[QHarshil](https://github.com/QHarshil)

[force-pushed](https://github.com/vllm-project/guidellm/compare/fe087289d3b2b201286223d76e41c78ab631bd00..57ffa99ce539b44d43fb4df7b58150d1d071dfda)the feat/measurement-uncertainty branch from

[to](https://github.com/vllm-project/guidellm/commit/fe087289d3b2b201286223d76e41c78ab631bd00)

`fe08728`


`57ffa99`

[Compare](https://github.com/vllm-project/guidellm/compare/fe087289d3b2b201286223d76e41c78ab631bd00..57ffa99ce539b44d43fb4df7b58150d1d071dfda)

September 23, 2026 23:51

[QHarshil](https://github.com/QHarshil)requested review from

[dfeddema](https://github.com/dfeddema),

[jaredoconnell](https://github.com/jaredoconnell)and

[sjmonson](https://github.com/sjmonson)as

[code owners](https://github.com/vllm-project/guidellm/blob/4e2cd400113c0ef005b1376a7ffb44abf416c8cb/CODEOWNERS#L2)

September 23, 2026 23:51

Contributor
Author

|
Replaced the reordering with a separate section written after all existing columns, listing only the metrics that can carry an interval. That also cuts the CSV addition from 95 columns to 27. The old version wrote interval columns for every distribution, and 68 were always empty. Rebased onto main for the docs move in |

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Every number in a benchmark report is a point estimate with no statement of how precisely it was measured. That matters most for the percentiles, which are order statistics:

`Percentiles.from_pdf`

puts p99 at rank`ceil(0.99n)`

, so below 100 successful requests the reported p99 is the slowest single request. I confirmed this on a ten second run: n=71, reported p99 128.42 ms, max 128.42 ms. Across twelve identical runs of that length the reported p99 ranged 115.83 to 146.66 ms, a 23.5% spread, while the mean moved 8.5%.This adds a confidence interval for the mean and for each percentile, for supported unweighted request-level distributions only. Token-weighted and derived rate distributions stay point estimates, for the reason below.

## Details

`guidellm/utils/statistics.py`

with`normal_ppf`

, an accurate`t_ppf`

,`wilson_interval`

,`mean_confidence_interval`

and`quantile_confidence_interval`

.`wilson_interval`

moves here from`goodput.py`

and`approx_t_ppf`

from`saturation.py`

, which removes the cross-layer import at`goodput.py:18`

.`ConfidenceInterval`

,`PercentileIntervals`

and`SampleUncertainty`

, and`mean_ci`

/`percentile_cis`

on`DistributionSummary`

. Both are nullable, so reports written before this load unchanged.`confidence`

to`--metrics kind=generative`

, default 0.95,`null`

to disable. Recorded once per benchmark as`config.confidence`

.`84.1 ±1.7`

, and marks a percentile the sample cannot bound with`*`

plus a footnote.`Mean CI`

,`Percentile CIs`

and the confidence level at the end of each row. Verified against`main`

: all 238 pre-existing columns keep their exact position.Two behavioural notes:

No change to existing metric values or scheduler and profile decisions.`wilson_interval`

keeps its current arithmetic rather than moving to the exact normal quantile. The two differ by 2.2e-4, which moves a Wilson upper bound of exactly 1.0 to just below it and would turn a goodput probe meeting a 100% attainment target into one that missed it. Five bounds are pinned by exact equality against`main`

. Console and CSV output do change. Correcting the over-saturation detector's quantile is left as a separate deliberate change.Percentile intervals are absent by design on short runs.Below the sample size that supports two order statistics the field is`null`

rather than a bound the observations cannot support: at the default 95% confidence level, 72 requests for p95, 368 for p99 and 3688 for p999.## Notes for review

At 100k observations, uncertainty compilation adds about 13.5 ms per distribution on my machine, or about 0.15 s across the eleven enabled metrics, once during final report compilation.

#1101 and #1102 also touch

`benchmark/schemas/metrics.py`

and its tests. The regions differ, but whichever lands second will need a rebase.## Test Plan

`tox -e lint-check`

,`tox -e type-check`

: pass.`tox -e test-unit`

: 3382 passed. The 14`tests/unit/utils/test_audio.py`

failures are a missing local FFmpeg;`python -c "import torchcodec"`

fails identically in the same environment with no GuideLLM code involved.`tox -e test-integration`

: 28 passed, 25 xfailed.`t_ppf`

is checked against published Student's t tables for df 1 to 1000 at five confidence levels, plus symmetry, monotonicity and domain errors. Both interval estimators are checked for coverage over repeated samples.`[109.56, 115.92]`

, p99`[119.13, 142.08]`

, p999`null`

.## Related Issues

## Use of AI

## git log

commit

34e8526Author: QHarshil harshil_c@hotmail.com

Date: Fri Sep 18 18:48:45 2026 -0700

commit

57ffa99Author: QHarshil harshil_c@hotmail.com

Date: Wed Sep 23 12:06:28 2026 -0700

Assisted-by: Claude Code claude-opus-5

Signed-off-by: QHarshil harshil_c@hotmail.com