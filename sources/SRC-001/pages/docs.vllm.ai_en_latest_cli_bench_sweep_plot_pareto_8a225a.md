source: https://docs.vllm.ai/en/latest/cli/bench/sweep/plot_pareto/
lastmod: 2026-09-24

# vllm bench sweep plot_pareto[¶](https://docs.vllm.ai#vllm-bench-sweep-plot_pareto)

## JSON CLI Arguments[¶](https://docs.vllm.ai#json-cli-arguments)

When passing JSON CLI arguments, the following sets of arguments are equivalent:

`--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`

`--json-arg.key1 value1 --json-arg.key2.key3 value2`


Additionally, list elements can be passed individually using `+`

:

`--json-arg '{"key4": ["value3", "value4", "value5"]}'`

`--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`


## Arguments[¶](https://docs.vllm.ai#arguments)

`--user-count-var`

[¶](https://docs.vllm.ai#-user-count-var)

- Result key that stores concurrent user count. Falls back to max_concurrent_requests if missing.
- Default:
`max_concurrency`


`--gpu-count-var`

[¶](https://docs.vllm.ai#-gpu-count-var)

- Result key that stores GPU count. If not provided, falls back to num_gpus/gpu_count or tensor_parallel_size * pipeline_parallel_size.

`--label-by`

[¶](https://docs.vllm.ai#-label-by)

- Comma-separated list of fields to annotate on Pareto frontier points.
- Default:
`max_concurrency,gpu_count`


`--dry-run`

[¶](https://docs.vllm.ai#-dry-run)

- If set, prints the figures to plot without drawing them.
- Default:
`False`