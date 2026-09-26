# [Issue #243] Margin Of Errors (MOE) in output report

source: https://github.com/vllm-project/guidellm/issues/243
state: open | updated: 2026-09-23T19:30:02Z
labels: internal

## 正文

Currently, the output report includes many aggregated measured metrics, essentially the following matrix:
| \ | µ | σ | min | max | p001 | p01 | p05 | p10 | p25 | p50 | p75 | p90 | 095 | p99 | p999 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| E2E |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TTFT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ITL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TPUT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

This matrix has one big flaw - it does not include any measure of reliability for the measurements.
For example, given the values of two identical benchmarks, but the first one ran for 10 seconds, and the second one ran for 10 minutes. The statistics measured in the second benchmark are much more reliable, because it has x60 more samples.

Since this is basically an estimation task, we should probably calculate a MOE value (e.g ±3.3%) for each measured metric in the matrix, it's a well accepted, simple and interpretable reliability measure.

## Algorithmic Requirements
There are many reasons for measurements to be unreliable, that should reflect in the MOE values.
Here are the 4 top ones:
1. Amount of samples
2. STD of the measured metric
3. Precision of the RPS (scheduling discrepancies)
4. Out of Distribution samples (anomalies / temporal interferences)

## Proposed Algorithm
Here is the outline of an algorithm that achieves that MOE estimation given all of the requirements:
1. Define a weight per sample, all samples start with weight 1
2. Multiply the weights by a RPS precision penalty, using a gaussian similarity (`RPS_penalty=gaussian(target_RPS-acutal_RPS)`)
3. Multiply the weights by an Out of Distribution penalty, using autocorrelation (`OOD_penalty=mutual_information(current_sample, adjacent_sample)`)
4. Then, proceed to calculate MOE normally with a t-student distribution (given the weights).
That way, samples with non precise RPS, or Out of Distribution samples with temporal correlation will be discounted from the final estimation.

Here are a few cases that the proposed algorithm was designed to handle:
* **Low RPS** - usually guidellm is used with the `--max-seconds` option, but when the RPS is particularly low (e.g 2, 1, 0.25) the amount of samples is much lower than higher RPSs, making the measurements much less reliable.
* **Reaching the max concurrency** - when guidellm reaches the maximum configured concurrency, the measurements no longer faithfully represent the configured RPS.
* **Batched samples** - when a server handles K requests in a single batch, the measured metrics of these requests are highly correlated, in other words they contain less information than K random samples.
* **Temporary server unavailability** - if for any reason the server is temporarily not able to respond, the temporary spike in metrics will be ignored when calculating the MOE.
* **Unstable capacity** - In many cases the server capacity may unintentionally vary mid benchmark (e.g APIs/multi-pod deployments), which heavily affects the measured metrics.

@markurtz I will soon send you a private doc and code demonstrating this algorithm.

## 评论 (1)

### QHarshil · 2026-09-19

@markurtz, I noticed this is still assigned to you. I've been investigating #243 and have a reproducible case plus an implementation. If you're still actively working on this, please let me know and I'm happy to coordinate rather than duplicate work.

I ran repeated benchmarks against the mock server to understand what a reliability measure here would actually need to represent.

Two results seem relevant.

First, the percentile point estimates are order statistics, so at small sample counts they degrade in a way the report does not signal. `Percentiles.from_pdf` puts p99 at rank `ceil(0.99n)`. With fewer than 100 observations that rank is n, so p99 is the single slowest observed request. On a 10 second run I measured n=71, reported p99 128.42 ms, and max 128.42 ms. Across twelve otherwise identical runs, p99 ranged from 115.83 to 146.66 ms, a 23.5% spread, while the mean moved 8.5%.

Second, not every existing distribution supports the same interpretation of uncertainty. For unweighted request-level metrics, a within-run confidence interval on the mean tracked the observed run-to-run variation reasonably in the workloads I tested. TPOT and ITL did not. In one variable-load experiment, observed run-to-run SD was 1.8x for TPOT and 3.2x for ITL relative to the corresponding within-run estimate. For ITL, a nominal 95% interval covered 9 of 16 repeated-run means. Lag-1 request autocorrelation was near zero, while run-level ITL was strongly associated with that run's token throughput (r=-0.76 over those 16 runs), suggesting a shared run-level condition that a single-run request-sampling interval cannot observe. This may be related to the workload-level behavior being discussed in #602. I have not validated that mechanism against a real vLLM server.

My preference is therefore to scope the first implementation to distributions containing one unweighted observation per request. Those receive a confidence interval for the mean and nonparametric intervals for the reported percentiles. Percentile intervals are null when the sample is too small to place two order statistics around the requested percentile. TPOT, ITL, and derived rate distributions remain point estimates for now rather than displaying an interval with a stronger interpretation than the data supports.

The confidence level is configurable through `--metrics kind=generative,confidence=...`, defaults to 0.95, and can be set to null to disable interval calculation. The JSON report carries structured mean and percentile intervals. Console output shows the mean margin and marks a displayed percentile with `*` when the estimator applies but the sample is too small to bound it. CSV exports the mean and percentile intervals while preserving every existing column position.

This also affects the design of #244. That issue uses examples such as `itl-median` for precision-based stopping. Under the scope above, ITL would not yet be eligible for that stopping criterion because #243 deliberately does not assign it an uncertainty estimate. I think that is preferable to allowing the stopping policy to act on an interval we already know can materially understate run-to-run variability, but it is worth deciding explicitly before #244 is implemented.

#1163 has the implementation, so the schema and estimator shape are concrete rather than only described here. Does this scope look reasonable?

