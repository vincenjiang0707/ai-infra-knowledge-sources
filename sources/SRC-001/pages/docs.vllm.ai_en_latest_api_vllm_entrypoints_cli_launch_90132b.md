source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/launch/
lastmod: 2026-09-24

#

`vllm.entrypoints.cli.launch`

[¶](https://docs.vllm.ai#vllm.entrypoints.cli.launch)

Classes:

-
–[LaunchSubcommand](https://docs.vllm.ai#vllm.entrypoints.cli.launch.LaunchSubcommand)The

`launch`

subcommand for the vLLM CLI. -
–[LaunchSubcommandBase](https://docs.vllm.ai#vllm.entrypoints.cli.launch.LaunchSubcommandBase)The base class of subcommands for

`vllm launch`

. -
–[RenderSubcommand](https://docs.vllm.ai#vllm.entrypoints.cli.launch.RenderSubcommand)`vllm launch render`

starts a GPU-less rendering server for preprocessing

##

`LaunchSubcommand`

[¶](https://docs.vllm.ai#vllm.entrypoints.cli.launch.LaunchSubcommand)

Bases: [CLISubcommand](https://docs.vllm.ai/types/#vllm.entrypoints.cli.types.CLISubcommand)

The `launch`

subcommand for the vLLM CLI.

Uses nested sub-subcommands so each component can define its own arguments independently (e.g. `vllm launch render`

).

## Source code in `vllm/entrypoints/cli/launch.py`


##

`LaunchSubcommandBase`

[¶](https://docs.vllm.ai#vllm.entrypoints.cli.launch.LaunchSubcommandBase)

Bases: [CLISubcommand](https://docs.vllm.ai/types/#vllm.entrypoints.cli.types.CLISubcommand)

The base class of subcommands for `vllm launch`

.

Methods:

-
–[add_cli_args](https://docs.vllm.ai#vllm.entrypoints.cli.launch.LaunchSubcommandBase.add_cli_args)Add the CLI arguments to the parser.


## Source code in `vllm/entrypoints/cli/launch.py`


###

`add_cli_args(parser)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.cli.launch.LaunchSubcommandBase.add_cli_args)

Add the CLI arguments to the parser.

By default, uses the subcommand's docstring as the description and adds the standard vLLM serving arguments. Subclasses can override to add component-specific arguments.

## Source code in `vllm/entrypoints/cli/launch.py`


##

`RenderSubcommand`

[¶](https://docs.vllm.ai#vllm.entrypoints.cli.launch.RenderSubcommand)

Bases: [LaunchSubcommandBase](https://docs.vllm.ai#vllm.entrypoints.cli.launch.LaunchSubcommandBase)

`vllm launch render`

starts a GPU-less rendering server for preprocessing and postprocessing only.

This command reuses the standard serving parser, so model, frontend, networking, and related CLI options follow the same conventions as [ vllm serve](https://docs.vllm.ai/cli/serve/).