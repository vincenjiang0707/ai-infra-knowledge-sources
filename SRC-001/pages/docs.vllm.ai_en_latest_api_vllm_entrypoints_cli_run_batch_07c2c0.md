source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/run_batch/
lastmod: 2026-09-23

Bases: [CLISubcommand](../types/#vllm.entrypoints.cli.types.CLISubcommand)


The `run-batch`

subcommand for vLLM CLI.

## Source code in `vllm/entrypoints/cli/run_batch.py`


| class RunBatchSubcommand(CLISubcommand):
"""The `run-batch` subcommand for vLLM CLI."""
name = "run-batch"
@staticmethod
def cmd(args: argparse.Namespace) -> None:
from vllm.entrypoints.launchers.run_batch import main as run_batch_main
logger.info(
"vLLM batch processing API version %s", importlib.metadata.version("vllm")
)
logger.info("args: %s", args)
# Start the Prometheus metrics server.
# LLMEngine uses the Prometheus client
# to publish metrics at the /metrics endpoint.
if args.enable_metrics:
from prometheus_client import start_http_server
logger.info("Prometheus metrics enabled")
start_http_server(port=args.port, addr=args.url)
else:
logger.info("Prometheus metrics disabled")
asyncio.run(run_batch_main(args))
def subparser_init(
self, subparsers: argparse._SubParsersAction
) -> FlexibleArgumentParser:
from vllm.entrypoints.launchers.run_batch import make_arg_parser
run_batch_parser = subparsers.add_parser(
self.name,
help="Run batch prompts and write results to file.",
description=(
"Run batch prompts using vLLM's OpenAI-compatible API.\n"
"Supports local or HTTP input/output files."
),
usage="vllm run-batch -i INPUT.jsonl -o OUTPUT.jsonl --model <model>",
)
run_batch_parser = make_arg_parser(run_batch_parser)
run_batch_parser.epilog = VLLM_SUBCMD_PARSER_EPILOG.format(subcmd=self.name)
return run_batch_parser
|