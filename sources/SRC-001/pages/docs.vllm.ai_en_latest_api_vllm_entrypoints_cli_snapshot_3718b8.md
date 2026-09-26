source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/snapshot/
lastmod: 2026-09-24

Bases: [CLISubcommand](../types/#vllm.entrypoints.cli.types.CLISubcommand)


The `snapshot`

subcommand for the vLLM CLI.

## Source code in `vllm/entrypoints/cli/snapshot.py`


| class SnapshotSubcommand(CLISubcommand):
"""The `snapshot` subcommand for the vLLM CLI."""
name = "snapshot"
def __init__(self, *, create_requested: bool = False) -> None:
self.create_requested = create_requested
@staticmethod
def cmd(args: argparse.Namespace) -> None:
args.snapshot_dispatch(args)
def subparser_init(
self, subparsers: argparse._SubParsersAction
) -> FlexibleArgumentParser:
parser = subparsers.add_parser(
self.name,
help="Create, inspect, or restore an initialized vLLM snapshot.",
usage="vllm snapshot <create|inspect|restore> [options]",
)
actions = parser.add_subparsers(required=True, dest="snapshot_action")
create_parser = actions.add_parser(
"create", help="Create a snapshot from an initialized TP1 engine."
)
if self.create_requested:
from vllm.entrypoints.launchers.cli_args import make_arg_parser
create_parser = make_arg_parser(create_parser)
else:
create_parser.add_argument("model_tag", nargs="?")
create_parser.add_argument("--snapshot-dir", required=True)
create_parser.set_defaults(snapshot_dispatch=run_create)
inspect_parser = actions.add_parser(
"inspect", help="Inspect a snapshot without restoring it."
)
inspect_parser.add_argument("snapshot_dir")
inspect_parser.set_defaults(snapshot_dispatch=run_inspect)
restore_parser = actions.add_parser(
"restore", help="Restore a same-host TP1 snapshot."
)
restore_parser.add_argument("snapshot_dir")
restore_parser.add_argument("--host", default=None)
restore_parser.add_argument("--port", type=int, default=8000)
restore_parser.set_defaults(snapshot_dispatch=run_restore)
return parser
|