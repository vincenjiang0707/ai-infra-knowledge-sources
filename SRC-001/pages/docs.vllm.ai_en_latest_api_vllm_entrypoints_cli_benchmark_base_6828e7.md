source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/base/
lastmod: 2026-09-23

#

`vllm.entrypoints.cli.benchmark.base`

[¶](https://docs.vllm.ai#vllm.entrypoints.cli.benchmark.base)

Classes:

-
–[BenchmarkSubcommandBase](https://docs.vllm.ai#vllm.entrypoints.cli.benchmark.base.BenchmarkSubcommandBase)The base class of subcommands for

`vllm bench`

.

##

`BenchmarkSubcommandBase`

[¶](https://docs.vllm.ai#vllm.entrypoints.cli.benchmark.base.BenchmarkSubcommandBase)

Bases: [CLISubcommand](https://docs.vllm.ai/types/#vllm.entrypoints.cli.types.CLISubcommand)

The base class of subcommands for `vllm bench`

.

Methods:

-
–[add_cli_args](https://docs.vllm.ai#vllm.entrypoints.cli.benchmark.base.BenchmarkSubcommandBase.add_cli_args)Add the CLI arguments to the parser.

-
–[cmd](https://docs.vllm.ai#vllm.entrypoints.cli.benchmark.base.BenchmarkSubcommandBase.cmd)Run the benchmark.