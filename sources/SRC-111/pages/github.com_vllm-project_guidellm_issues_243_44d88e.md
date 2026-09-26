source: https://github.com/vllm-project/guidellm/issues/243

Currently, the output report includes many aggregated measured metrics, essentially the following matrix:

| \ |
µ |
σ |
min |
max |
p001 |
p01 |
p05 |
p10 |
p25 |
p50 |
p75 |
p90 |
095 |
p99 |
p999 |
| E2E |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| TTFT |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| ITL |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| TPUT |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

This matrix has one big flaw - it does not include any measure of reliability for the measurements.

For example, given the values of two identical benchmarks, but the first one ran for 10 seconds, and the second one ran for 10 minutes. The statistics measured in the second benchmark are much more reliable, because it has x60 more samples.

Since this is basically an estimation task, we should probably calculate a MOE value (e.g ±3.3%) for each measured metric in the matrix, it's a well accepted, simple and interpretable reliability measure.

## Algorithmic Requirements

There are many reasons for measurements to be unreliable, that should reflect in the MOE values.

Here are the 4 top ones:

- Amount of samples
- STD of the measured metric
- Precision of the RPS (scheduling discrepancies)
- Out of Distribution samples (anomalies / temporal interferences)

## Proposed Algorithm

Here is the outline of an algorithm that achieves that MOE estimation given all of the requirements:

- Define a weight per sample, all samples start with weight 1
- Multiply the weights by a RPS precision penalty, using a gaussian similarity (
`RPS_penalty=gaussian(target_RPS-acutal_RPS)`

)
- Multiply the weights by an Out of Distribution penalty, using autocorrelation (
`OOD_penalty=mutual_information(current_sample, adjacent_sample)`

)
- Then, proceed to calculate MOE normally with a t-student distribution (given the weights).

That way, samples with non precise RPS, or Out of Distribution samples with temporal correlation will be discounted from the final estimation.

Here are a few cases that the proposed algorithm was designed to handle:

**Low RPS** - usually guidellm is used with the `--max-seconds`

option, but when the RPS is particularly low (e.g 2, 1, 0.25) the amount of samples is much lower than higher RPSs, making the measurements much less reliable.
**Reaching the max concurrency** - when guidellm reaches the maximum configured concurrency, the measurements no longer faithfully represent the configured RPS.
**Batched samples** - when a server handles K requests in a single batch, the measured metrics of these requests are highly correlated, in other words they contain less information than K random samples.
**Temporary server unavailability** - if for any reason the server is temporarily not able to respond, the temporary spike in metrics will be ignored when calculating the MOE.
**Unstable capacity** - In many cases the server capacity may unintentionally vary mid benchmark (e.g APIs/multi-pod deployments), which heavily affects the measured metrics.

[@markurtz](https://github.com/markurtz) I will soon send you a private doc and code demonstrating this algorithm.

Currently, the output report includes many aggregated measured metrics, essentially the following matrix:

This matrix has one big flaw - it does not include any measure of reliability for the measurements.

For example, given the values of two identical benchmarks, but the first one ran for 10 seconds, and the second one ran for 10 minutes. The statistics measured in the second benchmark are much more reliable, because it has x60 more samples.

Since this is basically an estimation task, we should probably calculate a MOE value (e.g ±3.3%) for each measured metric in the matrix, it's a well accepted, simple and interpretable reliability measure.

## Algorithmic Requirements

There are many reasons for measurements to be unreliable, that should reflect in the MOE values.

Here are the 4 top ones:

## Proposed Algorithm

Here is the outline of an algorithm that achieves that MOE estimation given all of the requirements:

`RPS_penalty=gaussian(target_RPS-acutal_RPS)`

)`OOD_penalty=mutual_information(current_sample, adjacent_sample)`

)That way, samples with non precise RPS, or Out of Distribution samples with temporal correlation will be discounted from the final estimation.

Here are a few cases that the proposed algorithm was designed to handle:

Low RPS- usually guidellm is used with the`--max-seconds`

option, but when the RPS is particularly low (e.g 2, 1, 0.25) the amount of samples is much lower than higher RPSs, making the measurements much less reliable.Reaching the max concurrency- when guidellm reaches the maximum configured concurrency, the measurements no longer faithfully represent the configured RPS.Batched samples- when a server handles K requests in a single batch, the measured metrics of these requests are highly correlated, in other words they contain less information than K random samples.Temporary server unavailability- if for any reason the server is temporarily not able to respond, the temporary spike in metrics will be ignored when calculating the MOE.Unstable capacity- In many cases the server capacity may unintentionally vary mid benchmark (e.g APIs/multi-pod deployments), which heavily affects the measured metrics.@markurtz I will soon send you a private doc and code demonstrating this algorithm.