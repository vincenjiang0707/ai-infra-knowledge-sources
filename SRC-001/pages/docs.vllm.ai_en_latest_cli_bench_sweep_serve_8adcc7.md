source: https://docs.vllm.ai/en/latest/cli/bench/sweep/serve/
lastmod: 2026-09-23

# vllm bench sweep serve[¶](https://docs.vllm.ai#vllm-bench-sweep-serve)

## JSON CLI Arguments[¶](https://docs.vllm.ai#json-cli-arguments)

When passing JSON CLI arguments, the following sets of arguments are equivalent:

`--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`

`--json-arg.key1 value1 --json-arg.key2.key3 value2`


Additionally, list elements can be passed individually using `+`

:

`--json-arg '{"key4": ["value3", "value4", "value5"]}'`

`--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`


## Arguments[¶](https://docs.vllm.ai#arguments)

`--serve-cmd`

[¶](https://docs.vllm.ai#-serve-cmd)

- The command used to run the server:
`vllm serve ...`


`--bench-cmd`

[¶](https://docs.vllm.ai#-bench-cmd)

- The command used to run the benchmark:
`vllm bench serve ...`


`--after-bench-cmd`

[¶](https://docs.vllm.ai#-after-bench-cmd)

- After a benchmark run is complete, invoke this command instead of the default
`ServerWrapper.clear_cache()`

.

`--show-stdout`

[¶](https://docs.vllm.ai#-show-stdout)

- If set, logs the standard output of subcommands. Useful for debugging but can be quite spammy.
- Default:
`False`


`--server-ready-timeout`

[¶](https://docs.vllm.ai#-server-ready-timeout)

- Timeout in seconds to wait for the server to become ready.
- Default:
`300`


`--serve-params`

[¶](https://docs.vllm.ai#-serve-params)

- Path to JSON file containing parameter combinations for the
`vllm serve`

command. Can be either a list of dicts or a dict where keys are benchmark names. If both`serve_params`

and`bench_params`

are given, this script will iterate over their Cartesian product.

`--link-vars`

[¶](https://docs.vllm.ai#-link-vars)

- Comma-separated list of linked variables between serve and bench, e.g. max_num_seqs=max_concurrency,max_model_len=random_input_len
- Default:
`""`


`--bench-params`

[¶](https://docs.vllm.ai#-bench-params)

- Path to JSON file containing parameter combinations for the
`vllm bench serve`

command. Can be either a list of dicts or a dict where keys are benchmark names. If both`serve_params`

and`bench_params`

are given, this script will iterate over their Cartesian product.

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
`3`


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