source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/openai/
lastmod: 2026-09-24

class ChatCommand(CLISubcommand):
"""The `chat` subcommand for the vLLM CLI."""
name = "chat"
@staticmethod
def cmd(args: argparse.Namespace) -> None:
model_name, client = _interactive_cli(args)
system_prompt = args.system_prompt
stats = args.stats
conversation: list[ChatCompletionMessageParam] = []
if system_prompt is not None:
conversation.append({"role": "system", "content": system_prompt})
create_kwargs = {"model": model_name, "stream": True}
if stats:
create_kwargs["stream_options"] = {"include_usage": True}
if args.quick is not None:
conversation.append({"role": "user", "content": args.quick})
stream = client.chat.completions.create(
messages=conversation, **create_kwargs
)
output = _print_chat_stream(stream, stats)
conversation.append({"role": "assistant", "content": output})
return
print("Please enter a message for the chat model:")
while True:
try:
input_message = input("> ")
except EOFError:
break
conversation.append({"role": "user", "content": input_message})
stream = client.chat.completions.create(
messages=conversation, **create_kwargs
)
output = _print_chat_stream(stream, stats)
conversation.append({"role": "assistant", "content": output})
@staticmethod
def add_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Add CLI arguments for the chat command."""
_add_query_options(parser)
parser.add_argument(
"--system-prompt",
type=str,
default=None,
help=(
"The system prompt to be added to the chat template, "
"used for models that support system prompts."
),
)
parser.add_argument(
"-q",
"--quick",
type=str,
metavar="MESSAGE",
help=("Send a single prompt as MESSAGE and print the response, then exit."),
)
parser.add_argument(
"--stats",
action="store_true",
help="Print TTFT and TPS statistics after each response.",
)
return parser
def subparser_init(
self, subparsers: argparse._SubParsersAction
) -> FlexibleArgumentParser:
parser = subparsers.add_parser(
"chat",
help="Generate chat completions via the running API server.",
description="Generate chat completions via the running API server.",
usage="vllm chat [options]",
)
return ChatCommand.add_cli_args(parser)