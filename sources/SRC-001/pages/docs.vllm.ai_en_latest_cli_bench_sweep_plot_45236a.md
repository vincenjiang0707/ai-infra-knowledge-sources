source: https://docs.vllm.ai/en/latest/cli/bench/sweep/plot/
lastmod: 2026-09-23

# vllm bench sweep plot[¶](https://docs.vllm.ai#vllm-bench-sweep-plot)

## JSON CLI Arguments[¶](https://docs.vllm.ai#json-cli-arguments)

When passing JSON CLI arguments, the following sets of arguments are equivalent:

`--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`

`--json-arg.key1 value1 --json-arg.key2.key3 value2`


Additionally, list elements can be passed individually using `+`

:

`--json-arg '{"key4": ["value3", "value4", "value5"]}'`

`--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`


## Arguments[¶](https://docs.vllm.ai#arguments)

`--fig-dir`

[¶](https://docs.vllm.ai#-fig-dir)

- The directory to save the figures, relative to
`OUTPUT_DIR`

. By default, the same directory is used. - Default:
`""`


`--fig-by`

[¶](https://docs.vllm.ai#-fig-by)

- A comma-separated list of variables, such that a separate figure is created for each combination of these variables.
- Default:
`""`


`--row-by`

[¶](https://docs.vllm.ai#-row-by)

- A comma-separated list of variables, such that a separate row is created for each combination of these variables.
- Default:
`""`


`--col-by`

[¶](https://docs.vllm.ai#-col-by)

- A comma-separated list of variables, such that a separate column is created for each combination of these variables.
- Default:
`""`


`--curve-by`

[¶](https://docs.vllm.ai#-curve-by)

- A comma-separated list of variables, such that a separate curve is created for each combination of these variables.

`--var-x`

[¶](https://docs.vllm.ai#-var-x)

- The variable for the x-axis.
- Default:
`total_token_throughput`


`--var-y`

[¶](https://docs.vllm.ai#-var-y)

- The variable for the y-axis
- Default:
`median_ttft_ms`


`--filter-by`

[¶](https://docs.vllm.ai#-filter-by)

- A comma-separated list of statements indicating values to filter by. This is useful to remove outliers. Example:
`max_concurrency<1000,max_num_batched_tokens<=4096`

means plot only the points where`max_concurrency`

is less than 1000 and`max_num_batched_tokens`

is no greater than 4096. - Default:
`""`


`--bin-by`

[¶](https://docs.vllm.ai#-bin-by)

- A comma-separated list of statements indicating values to bin by. This is useful to avoid plotting points that are too close together. Example:
`request_throughput%%1`

means use a bin size of 1 for the`request_throughput`

variable. - Default:
`""`


`--scale-x`

[¶](https://docs.vllm.ai#-scale-x)

- The scale to use for the x-axis. Currently only accepts string values such as 'log' and 'sqrt'. See also: https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html

`--scale-y`

[¶](https://docs.vllm.ai#-scale-y)

- The scale to use for the y-axis. Currently only accepts string values such as 'log' and 'sqrt'. See also: https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html

`--fig-name`

[¶](https://docs.vllm.ai#-fig-name)

- Name prefix for the output figure file. Group data is always appended when present. Default: 'FIGURE'. Example: --fig-name my_performance_plot
- Default:
`FIGURE`


`--no-error-bars`

[¶](https://docs.vllm.ai#-no-error-bars)

- If set, disables error bars on the plot. By default, error bars are shown.
- Default:
`False`


`--fig-height`

[¶](https://docs.vllm.ai#-fig-height)

- Height of each subplot in inches. Default: 6.4
- Default:
`6.4`


`--fig-dpi`

[¶](https://docs.vllm.ai#-fig-dpi)

- Resolution of the output figure in dots per inch. Default: 300
- Default:
`300`


`--dry-run`

[¶](https://docs.vllm.ai#-dry-run)

- If set, prints the information about each figure to plot, then exits without drawing them.
- Default:
`False`