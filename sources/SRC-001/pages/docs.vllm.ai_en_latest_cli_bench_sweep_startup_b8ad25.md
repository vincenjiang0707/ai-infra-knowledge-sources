source: https://docs.vllm.ai/en/latest/cli/bench/sweep/startup/
lastmod: 2026-09-24

# vllm bench sweep startup[¶](https://docs.vllm.ai#vllm-bench-sweep-startup)

## JSON CLI Arguments[¶](https://docs.vllm.ai#json-cli-arguments)

When passing JSON CLI arguments, the following sets of arguments are equivalent:

`--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`

`--json-arg.key1 value1 --json-arg.key2.key3 value2`


Additionally, list elements can be passed individually using `+`

:

`--json-arg '{"key4": ["value3", "value4", "value5"]}'`

`--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`


## Arguments[¶](https://docs.vllm.ai#arguments)

`--startup-cmd`

[¶](https://docs.vllm.ai#-startup-cmd)

- The command used to run the startup benchmark.
- Default:
`vllm bench startup`


`--serve-params`

[¶](https://docs.vllm.ai#-serve-params)

- Path to JSON file containing parameter combinations for the
`vllm serve`

command. Only parameters supported by`vllm bench startup`

will be applied.

`--startup-params`

[¶](https://docs.vllm.ai#-startup-params)

- Path to JSON file containing parameter combinations for the
`vllm bench startup`

command.

`--strict-params`

[¶](https://docs.vllm.ai#-strict-params)

- If set, unknown parameters in sweep files raise an error instead of being ignored.
- Default:
`False`


`-o`

, `--output-dir`

[¶](https://docs.vllm.ai#-o-output-dir)

- The main directory to which results are written.
- Default:
`results`


`-e`

, `--experiment-name`

[¶](https://docs.vllm.ai#-e-experiment-name)

- The name of this experiment (defaults to current timestamp). Results will be stored under
`output_dir/experiment_name`

.

`--num-runs`

[¶](https://docs.vllm.ai#-num-runs)

- Number of runs per parameter combination.
- Default:
`1`


`--show-stdout`

[¶](https://docs.vllm.ai#-show-stdout)

- If set, logs the standard output of subcommands.
- Default:
`False`


`--dry-run`

[¶](https://docs.vllm.ai#-dry-run)

- If set, prints the commands to run, then exits without executing them.
- Default:
`False`


`--resume`

[¶](https://docs.vllm.ai#-resume)

- Resume a previous execution of this script, i.e., only run parameter combinations for which there are still no output files under
`output_dir/experiment_name`

. - Default:
`False`