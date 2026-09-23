source: https://docs.vllm.ai/en/latest/examples/applications/api_server/
lastmod: 2026-09-23

# API Server[¶](https://docs.vllm.ai#api-server)

Source [https://github.com/vllm-project/vllm/tree/main/examples/applications/api_server](https://github.com/vllm-project/vllm/tree/main/examples/applications/api_server).

## Client[¶](https://docs.vllm.ai#client)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Example Python client for `examples/applications/api_server/server.py`
Start the demo server:
python examples/applications/api_server/server.py --model <model_name>
NOTE: The API server is used only for demonstration and simple performance
benchmarks. It is not intended for production use.
For production use, we recommend `vllm serve` and the OpenAI client API.
"""
import argparse
import json
from argparse import Namespace
from collections.abc import Iterable
import requests
def clear_line(n: int = 1) -> None:
LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"
for _ in range(n):
print(LINE_UP, end=LINE_CLEAR, flush=True)
def post_http_request(
prompt: str, api_url: str, n: int = 1, stream: bool = False
) -> requests.Response:
headers = {"User-Agent": "Test Client"}
pload = {
"prompt": prompt,
"n": n,
"temperature": 0.0,
"max_tokens": 16,
"stream": stream,
}
response = requests.post(api_url, headers=headers, json=pload, stream=stream)
return response
def get_streaming_response(response: requests.Response) -> Iterable[list[str]]:
for chunk in response.iter_lines(
chunk_size=8192, decode_unicode=False, delimiter=b"\n"
):
if chunk:
data = json.loads(chunk.decode("utf-8"))
output = data["text"]
yield output
def get_response(response: requests.Response) -> list[str]:
data = json.loads(response.content)
output = data["text"]
return output
def parse_args():
parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, default="localhost")
parser.add_argument("--port", type=int, default=8000)
parser.add_argument("--n", type=int, default=1)
parser.add_argument("--prompt", type=str, default="San Francisco is a")
parser.add_argument("--stream", action="store_true")
return parser.parse_args()
def main(args: Namespace):
prompt = args.prompt
api_url = f"http://{args.host}:{args.port}/generate"
n = args.n
stream = args.stream
print(f"Prompt: {prompt!r}\n", flush=True)
response = post_http_request(prompt, api_url, n, stream)
if stream:
num_printed_lines = 0
for h in get_streaming_response(response):
clear_line(num_printed_lines)
num_printed_lines = 0
for i, line in enumerate(h):
num_printed_lines += 1
print(f"Beam candidate {i}: {line!r}", flush=True)
else:
output = get_response(response)
for i, line in enumerate(output):
print(f"Beam candidate {i}: {line!r}", flush=True)
if __name__ == "__main__":
args = parse_args()
main(args)


## Server[¶](https://docs.vllm.ai#server)

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""NOTE: This API server is used only for demonstrating usage of AsyncEngine
and simple performance benchmarks. It is not intended for production use.
For production use, we recommend using our OpenAI compatible server.
We are also not going to accept PRs modifying this file.
"""
import asyncio
import json
import ssl
from argparse import Namespace
from collections.abc import AsyncGenerator
from typing import Any
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response, StreamingResponse
import vllm.envs as envs
from vllm.engine.arg_utils import AsyncEngineArgs
from vllm.engine.async_llm_engine import AsyncLLMEngine
from vllm.entrypoints.launchers.launcher import serve_http
from vllm.entrypoints.serve.utils.api_utils import with_cancellation
from vllm.logger import init_logger
from vllm.sampling_params import SamplingParams
from vllm.usage.usage_lib import UsageContext
from vllm.utils import random_uuid
from vllm.utils.argparse_utils import FlexibleArgumentParser
from vllm.utils.system_utils import set_ulimit
from vllm.version import __version__ as VLLM_VERSION
logger = init_logger("api_server")
app = FastAPI()
engine = None
@app.get("/health")
async def health() -> Response:
"""Health check."""
return Response(status_code=200)
@app.post("/generate")
async def generate(request: Request) -> Response:
"""Generate completion for the request.
The request should be a JSON object with the following fields:
- prompt: the prompt to use for the generation.
- stream: whether to stream the results or not.
- other fields: the sampling parameters (See `SamplingParams` for details).
"""
request_dict = await request.json()
return await _generate(request_dict, raw_request=request)
@with_cancellation
async def _generate(request_dict: dict, raw_request: Request) -> Response:
prompt = request_dict.pop("prompt")
stream = request_dict.pop("stream", False)
# Since SamplingParams is created fresh per request, safe to skip clone
sampling_params = SamplingParams(**request_dict, skip_clone=True)
request_id = random_uuid()
assert engine is not None
results_generator = engine.generate(prompt, sampling_params, request_id)
# Streaming case
async def stream_results() -> AsyncGenerator[bytes, None]:
async for request_output in results_generator:
prompt = request_output.prompt
assert prompt is not None
text_outputs = [prompt + output.text for output in request_output.outputs]
ret = {"text": text_outputs}
yield (json.dumps(ret) + "\n").encode("utf-8")
if stream:
return StreamingResponse(stream_results())
# Non-streaming case
final_output = None
try:
async for request_output in results_generator:
final_output = request_output
except asyncio.CancelledError:
return Response(status_code=499)
assert final_output is not None
prompt = final_output.prompt
assert prompt is not None
text_outputs = [prompt + output.text for output in final_output.outputs]
ret = {"text": text_outputs}
return JSONResponse(ret)
def build_app(args: Namespace) -> FastAPI:
global app
app.root_path = args.root_path
return app
async def init_app(
args: Namespace,
llm_engine: AsyncLLMEngine | None = None,
) -> FastAPI:
app = build_app(args)
global engine
engine_args = AsyncEngineArgs.from_cli_args(args)
engine = (
llm_engine
if llm_engine is not None
else AsyncLLMEngine.from_engine_args(
engine_args, usage_context=UsageContext.API_SERVER
)
)
app.state.engine_client = engine
app.state.args = args
return app
async def run_server(
args: Namespace, llm_engine: AsyncLLMEngine | None = None, **uvicorn_kwargs: Any
) -> None:
logger.info("vLLM API server version %s", VLLM_VERSION)
logger.info("args: %s", args)
set_ulimit()
app = await init_app(args, llm_engine)
assert engine is not None
shutdown_task = await serve_http(
app,
sock=None,
enable_ssl_refresh=args.enable_ssl_refresh,
host=args.host,
port=args.port,
log_level=args.log_level,
timeout_keep_alive=envs.VLLM_HTTP_TIMEOUT_KEEP_ALIVE,
ssl_keyfile=args.ssl_keyfile,
ssl_certfile=args.ssl_certfile,
ssl_ca_certs=args.ssl_ca_certs,
ssl_cert_reqs=args.ssl_cert_reqs,
**uvicorn_kwargs,
)
await shutdown_task
if __name__ == "__main__":
parser = FlexibleArgumentParser()
parser.add_argument("--host", type=str, default=None)
parser.add_argument("--port", type=parser.check_port, default=8000)
parser.add_argument("--ssl-keyfile", type=str, default=None)
parser.add_argument("--ssl-certfile", type=str, default=None)
parser.add_argument(
"--ssl-ca-certs", type=str, default=None, help="The CA certificates file"
)
parser.add_argument(
"--enable-ssl-refresh",
action="store_true",
default=False,
help="Refresh SSL Context when SSL certificate files change",
)
parser.add_argument(
"--ssl-cert-reqs",
type=int,
default=int(ssl.CERT_NONE),
help="Whether client certificate is required (see stdlib ssl module's)",
)
parser.add_argument(
"--root-path",
type=str,
default=None,
help="FastAPI root_path when app is behind a path based routing proxy",
)
parser.add_argument("--log-level", type=str, default="debug")
parser = AsyncEngineArgs.add_cli_args(parser)
args = parser.parse_args()
asyncio.run(run_server(args))