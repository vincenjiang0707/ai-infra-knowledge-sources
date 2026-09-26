source: https://github.com/vllm-project/guidellm/issues/244

Given that [#238](https://github.com/vllm-project/guidellm/pull/238) will land and that [#243](https://github.com/vllm-project/guidellm/issues/243) will turn into a PR and land as well, it would be incredible to have target metric MOE stopping.

Basically this feature is 2 new options:

`--target-metric`

- the metric to use as the target for MOE stopping, of the form ["all", "ttft", "ttft-p90", "itl-median"....] (default: "all")
`--target-moe`

- the allowed error in the metric measurement (in percentages) as reflected in the MOE of that metric.

In a benchmark run, when the MOE value of the target metric reaches the target MOE - the benchmark will end with the termination reason "target_moe_reached".

This feature will include a simple ETA value.

Essentially, calculate the amount of samples required to reach the MOE (assuming the average sample weight consists), then use the RPS to extrapolate time.

A feature like this would make guidellm much faster and reliable for most use-cases.

Given that #238 will land and that #243 will turn into a PR and land as well, it would be incredible to have target metric MOE stopping.

Basically this feature is 2 new options:

`--target-metric`

- the metric to use as the target for MOE stopping, of the form ["all", "ttft", "ttft-p90", "itl-median"....] (default: "all")`--target-moe`

- the allowed error in the metric measurement (in percentages) as reflected in the MOE of that metric.In a benchmark run, when the MOE value of the target metric reaches the target MOE - the benchmark will end with the termination reason "target_moe_reached".

This feature will include a simple ETA value.

Essentially, calculate the amount of samples required to reach the MOE (assuming the average sample weight consists), then use the RPS to extrapolate time.

A feature like this would make guidellm much faster and reliable for most use-cases.