source: https://docs.vllm.ai/en/latest/examples/disaggregated/disaggregated_serving/
lastmod: 2026-09-24

# Disaggregated Serving[¶](https://docs.vllm.ai#disaggregated-serving)

Source [https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/disaggregated_serving](https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/disaggregated_serving).

This example contains scripts that demonstrate the disaggregated serving features of vLLM.

## Files[¶](https://docs.vllm.ai#files)

`disagg_proxy_demo.py`

- Demonstrates XpYd (X prefill instances, Y decode instances).`kv_events.sh`

- Demonstrates KV cache event publishing.`mooncake_connector`

- A proxy demo for MooncakeConnector.

## Example materials[¶](https://docs.vllm.ai#example-materials)

## disagg_proxy_demo.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This file provides a disaggregated prefilling proxy demo to demonstrate an
example usage of XpYd disaggregated prefilling.
We can launch multiple vllm instances (2 for prefill and 2 for decode), and
launch this proxy demo through:
python3 examples/disaggregated/disaggregated_serving/disagg_proxy_demo.py \
--model $model_name \
--prefill localhost:8100 localhost:8101 \
--decode localhost:8200 localhost:8201 \
--port 8000
Note: This demo will be removed once the PDController implemented in PR 15343
(https://github.com/vllm-project/vllm/pull/15343) supports XpYd.
"""
import argparse
import ipaddress
import itertools
import json
import logging
import os
import sys
from abc import ABC, abstractmethod
from collections.abc import Callable
import aiohttp
import requests
import uvicorn
from fastapi import APIRouter, Depends, FastAPI, Header, HTTPException, Request, status
from fastapi.responses import JSONResponse, StreamingResponse
AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(total=6 * 60 * 60)
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
class SchedulingPolicy(ABC):
@abstractmethod
def schedule(self, cycler: itertools.cycle):
raise NotImplementedError("Scheduling Proxy is not set.")
class Proxy:
def __init__(
self,
prefill_instances: list[str],
decode_instances: list[str],
model: str,
scheduling_policy: SchedulingPolicy,
custom_create_completion: Callable[[Request], StreamingResponse] | None = None,
custom_create_chat_completion: Callable[[Request], StreamingResponse]
| None = None,
):
self.prefill_instances = prefill_instances
self.decode_instances = decode_instances
self.prefill_cycler = itertools.cycle(prefill_instances)
self.decode_cycler = itertools.cycle(decode_instances)
self.model = model
self.scheduling_policy = scheduling_policy
self.custom_create_completion = custom_create_completion
self.custom_create_chat_completion = custom_create_chat_completion
self.router = APIRouter()
self.setup_routes()
def setup_routes(self):
self.router.post(
"/v1/completions", dependencies=[Depends(self.validate_json_request)]
)(
self.custom_create_completion
if self.custom_create_completion
else self.create_completion
)
self.router.post(
"/v1/chat/completions", dependencies=[Depends(self.validate_json_request)]
)(
self.custom_create_chat_completion
if self.custom_create_chat_completion
else self.create_chat_completion
)
self.router.get("/status", response_class=JSONResponse)(self.get_status)
self.router.post(
"/instances/add", dependencies=[Depends(self.api_key_authenticate)]
)(self.add_instance_endpoint)
async def validate_json_request(self, raw_request: Request):
content_type = raw_request.headers.get("content-type", "").lower()
if content_type != "application/json":
raise HTTPException(
status_code=415,
detail="Unsupported Media Type: Only 'application/json' is allowed",
)
def api_key_authenticate(self, x_api_key: str = Header(...)):
expected_api_key = os.environ.get("ADMIN_API_KEY")
if not expected_api_key:
logger.error("ADMIN_API_KEY is not set in the environment.")
raise HTTPException(
status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
detail="Server configuration error.",
)
if x_api_key != expected_api_key:
logger.warning("Unauthorized access attempt with API Key: %s", x_api_key)
raise HTTPException(
status_code=status.HTTP_403_FORBIDDEN,
detail="Forbidden: Invalid API Key.",
)
async def validate_instance(self, instance: str) -> bool:
url = f"http://{instance}/v1/models"
try:
async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as client:
logger.info("Verifying %s ...", instance)
async with client.get(url) as response:
if response.status == 200:
data = await response.json()
if "data" in data and len(data["data"]) > 0:
model_cur = data["data"][0].get("id", "")
if model_cur == self.model:
logger.info("Instance: %s could be added.", instance)
return True
else:
logger.warning(
"Mismatch model %s : %s != %s",
instance,
model_cur,
self.model,
)
return False
else:
return False
else:
return False
except aiohttp.ClientError as e:
logger.error(str(e))
return False
except Exception as e:
logger.error(str(e))
return False
async def add_instance_endpoint(self, request: Request):
try:
data = await request.json()
logger.warning(str(data))
instance_type = data.get("type")
instance = data.get("instance")
if instance_type not in ["prefill", "decode"]:
raise HTTPException(status_code=400, detail="Invalid instance type.")
if not instance or ":" not in instance:
raise HTTPException(status_code=400, detail="Invalid instance format.")
host, port_str = instance.split(":")
try:
if host != "localhost":
ipaddress.ip_address(host)
port = int(port_str)
if not (0 < port < 65536):
raise HTTPException(status_code=400, detail="Invalid port number.")
except Exception as e:
raise HTTPException(
status_code=400, detail="Invalid instance address."
) from e
is_valid = await self.validate_instance(instance)
if not is_valid:
raise HTTPException(
status_code=400, detail="Instance validation failed."
)
if instance_type == "prefill":
if instance not in self.prefill_instances:
self.prefill_instances.append(instance)
self.prefill_cycler = itertools.cycle(self.prefill_instances)
else:
raise HTTPException(
status_code=400, detail="Instance already exists."
)
else:
if instance not in self.decode_instances:
self.decode_instances.append(instance)
self.decode_cycler = itertools.cycle(self.decode_instances)
else:
raise HTTPException(
status_code=400, detail="Instance already exists."
)
return JSONResponse(
content={"message": f"Added {instance} to {instance_type}_instances."}
)
except HTTPException as http_exc:
raise http_exc
except Exception as e:
logger.error("Error in add_instance_endpoint: %s", str(e))
raise HTTPException(status_code=500, detail=str(e)) from e
async def forward_request(self, url, data, use_chunked=True):
async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as session:
headers = {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"}
try:
async with session.post(
url=url, json=data, headers=headers
) as response:
if 200 <= response.status < 300 or 400 <= response.status < 500:
if use_chunked:
async for chunk_bytes in response.content.iter_chunked(
1024
):
yield chunk_bytes
else:
content = await response.read()
yield content
else:
error_content = await response.text()
try:
error_content = json.loads(error_content)
except json.JSONDecodeError:
error_content = error_content
logger.error(
"Request failed with status %s: %s",
response.status,
error_content,
)
raise HTTPException(
status_code=response.status,
detail=f"Request failed with status {response.status}: "
f"{error_content}",
)
except aiohttp.ClientError as e:
logger.error("ClientError occurred: %s", str(e))
raise HTTPException(
status_code=502,
detail="Bad Gateway: Error communicating with upstream server.",
) from e
except Exception as e:
logger.error("Unexpected error: %s", str(e))
raise HTTPException(status_code=500, detail=str(e)) from e
def schedule(self, cycler: itertools.cycle) -> str:
return self.scheduling_policy.schedule(cycler)
async def get_status(self):
status = {
"prefill_node_count": len(self.prefill_instances),
"decode_node_count": len(self.decode_instances),
"prefill_nodes": self.prefill_instances,
"decode_nodes": self.decode_instances,
}
return status
async def create_completion(self, raw_request: Request):
try:
request = await raw_request.json()
kv_prepare_request = request.copy()
kv_prepare_request["max_tokens"] = 1
prefill_instance = self.schedule(self.prefill_cycler)
try:
async for _ in self.forward_request(
f"http://{prefill_instance}/v1/completions", kv_prepare_request
):
continue
except HTTPException as http_exc:
self.remove_instance_endpoint("prefill", prefill_instance)
raise http_exc
# Perform kv recv and decoding stage
decode_instance = self.schedule(self.decode_cycler)
try:
generator = self.forward_request(
f"http://{decode_instance}/v1/completions", request
)
except HTTPException as http_exc:
self.remove_instance_endpoint("decode", decode_instance)
raise http_exc
response = StreamingResponse(generator)
return response
except Exception:
import sys
exc_info = sys.exc_info()
print("Error occurred in disagg proxy server")
print(exc_info)
async def create_chat_completion(self, raw_request: Request):
try:
request = await raw_request.json()
# add params to request
kv_prepare_request = request.copy()
kv_prepare_request["max_tokens"] = 1
if "max_completion_tokens" in kv_prepare_request:
kv_prepare_request["max_completion_tokens"] = 1
# prefill stage
prefill_instance = self.schedule(self.prefill_cycler)
try:
async for _ in self.forward_request(
f"http://{prefill_instance}/v1/chat/completions", kv_prepare_request
):
continue
except HTTPException as http_exc:
self.remove_instance_endpoint("prefill", prefill_instance)
raise http_exc
# Perform kv recv and decoding stage
decode_instance = self.schedule(self.decode_cycler)
try:
generator = self.forward_request(
"http://" + decode_instance + "/v1/chat/completions", request
)
except HTTPException as http_exc:
self.remove_instance_endpoint("decode", decode_instance)
raise http_exc
response = StreamingResponse(content=generator)
return response
except Exception:
exc_info = sys.exc_info()
error_messages = [str(e) for e in exc_info if e]
print("Error occurred in disagg proxy server")
print(error_messages)
return StreamingResponse(
content=iter(error_messages), media_type="text/event-stream"
)
def remove_instance_endpoint(self, instance_type, instance):
if instance_type == "decode" and instance in self.decode_instances:
self.decode_instances.remove(instance)
self.decode_cycler = itertools.cycle(self.decode_instances)
if instance_type == "prefill" and instance in self.prefill_instances:
self.prefill_instances.remove(instance)
self.prefill_cycler = itertools.cycle(self.prefill_instances)
class RoundRobinSchedulingPolicy(SchedulingPolicy):
def __init__(self):
super().__init__()
def schedule(self, cycler: itertools.cycle) -> str:
return next(cycler)
class ProxyServer:
def __init__(
self,
args: argparse.Namespace,
scheduling_policy: SchedulingPolicy | None = None,
create_completion: Callable[[Request], StreamingResponse] | None = None,
create_chat_completion: Callable[[Request], StreamingResponse] | None = None,
):
self.validate_parsed_serve_args(args)
self.port = args.port
self.proxy_instance = Proxy(
prefill_instances=[] if args.prefill is None else args.prefill,
decode_instances=[] if args.decode is None else args.decode,
model=args.model,
scheduling_policy=(
scheduling_policy
if scheduling_policy is not None
else RoundRobinSchedulingPolicy()
),
custom_create_completion=create_completion,
custom_create_chat_completion=create_chat_completion,
)
def validate_parsed_serve_args(self, args: argparse.Namespace):
if not args.prefill:
raise ValueError("Please specify at least one prefill node.")
if not args.decode:
raise ValueError("Please specify at least one decode node.")
self.validate_instances(args.prefill)
self.validate_instances(args.decode)
self.verify_model_config(args.prefill, args.model)
self.verify_model_config(args.decode, args.model)
def validate_instances(self, instances: list):
for instance in instances:
if len(instance.split(":")) != 2:
raise ValueError(f"Invalid instance format: {instance}")
host, port = instance.split(":")
try:
if host != "localhost":
ipaddress.ip_address(host)
port = int(port)
if not (0 < port < 65536):
raise ValueError(f"Invalid port number in instance: {instance}")
except Exception as e:
raise ValueError(f"Invalid instance {instance}: {str(e)}") from e
def verify_model_config(self, instances: list, model: str) -> None:
model_suffix = model.split("/")[-1]
for instance in instances:
try:
response = requests.get(f"http://{instance}/v1/models")
if response.status_code == 200:
model_cur = response.json()["data"][0]["id"]
model_cur_suffix = model_cur.split("/")[-1]
if model_cur_suffix != model_suffix:
raise ValueError(
f"{instance} serves a different model: "
f"{model_cur} != {model}"
)
else:
raise ValueError(f"Cannot get model id from {instance}!")
except requests.RequestException as e:
raise ValueError(
f"Error communicating with {instance}: {str(e)}"
) from e
def run_server(self):
app = FastAPI()
app.include_router(self.proxy_instance.router)
config = uvicorn.Config(app, port=self.port, loop="uvloop")
server = uvicorn.Server(config)
server.run()
def parse_args():
# Todo: allow more config
parser = argparse.ArgumentParser("vLLM disaggregated proxy server.")
parser.add_argument("--model", "-m", type=str, required=True, help="Model name")
parser.add_argument(
"--prefill",
"-p",
type=str,
nargs="+",
help="List of prefill node URLs (host:port)",
)
parser.add_argument(
"--decode",
"-d",
type=str,
nargs="+",
help="List of decode node URLs (host:port)",
)
parser.add_argument(
"--port",
type=int,
default=8000,
help="Server port number",
)
return parser.parse_args()
if __name__ == "__main__":
args = parse_args()
proxy_server = ProxyServer(args=args)
proxy_server.run_server()


## disagg_proxy_multiturn.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Disaggregated Prefill/Decode Proxy with Bidirectional KV Transfer.
This proxy sits between clients and a vLLM Prefill/Decode (P/D) deployment,
routing multi-turn chat requests so that each turn reuses KV cache blocks
from the previous turn's Decode node via bidirectional KV transfer.
Architecture:
Client ──► Proxy ──► Prefill (P) ──► Decode (D)
│ │ │
│ kv_transfer_params flow: │
│ D finish ──► proxy caches │
│ next turn ──► proxy sends │
│ cached D blocks to P ──► │
│ P reads D blocks (bidir) │
│ P sends its blocks to D │
Per-request flow:
1. Client sends chat/completions request to proxy.
2. Proxy looks up cached D block info from the previous turn
(keyed by conversation_id).
3. If cache hit, proxy attaches D's block info to the request
so P can read D's KV blocks instead of recomputing.
4. Proxy sends request to P (max_tokens=1, non-streaming).
5. P returns kv_transfer_params with its own block info.
6. Proxy forwards request + P's block info to D (streaming).
7. D streams the response. The final chunk includes D's
kv_transfer_params, which the proxy caches for the next turn.
8. Proxy returns D's response to the client.
Conversation isolation:
Each request must include a ``conversation_id`` field (top-level in
the JSON body) to scope the KV cache across turns. Without it, the
proxy cannot link turns and falls back to no-cache behavior.
``conversation_id`` is a non-standard extension to the OpenAI Chat
Completions schema, consumed by this proxy and not forwarded to the
vLLM engine. Strict OpenAI-compatible frontends reject unknown
fields, so clients must opt in only when targeting this proxy.
Usage:
python disagg_proxy_multiturn.py \\
--host 0.0.0.0 --port 8000 \\
--prefiller-host 10.0.0.1 --prefiller-port 8100 \\
--decoder-host 10.0.0.2 --decoder-port 8200
Benchmarking:
Use ``benchmarks/multi_turn/benchmark_serving_multi_turn.py`` with
the ``--send-conversation-id`` flag to inject a per-conversation
``conversation_id`` into every request so this proxy can key
cross-turn KV cache reuse. The flag is *off by default*: without
it the benchmark sends OpenAI-schema-compliant payloads and every
turn lands as a cache MISS in this proxy.
Example:
python benchmarks/multi_turn/benchmark_serving_multi_turn.py \\
--model <MODEL> --served-model-name <NAME> \\
--url http://<proxy_host>:8000 \\
--input-file generate_multi_turn.json \\
--num-clients 2 --max-active-conversations 6 \\
--send-conversation-id
See ``docs/features/nixl_connector_usage.md`` for the broader
bidirectional-KV-transfer setup these benchmarks exercise.
Dependencies:
pip install fastapi uvicorn httpx
"""
from __future__ import annotations
import argparse
import itertools
import json
import logging
import os
import time
import uuid
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import Any
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
# Logging
logging.basicConfig(
format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
datefmt="%Y-%m-%d %H:%M:%S",
level=logging.INFO,
)
logger = logging.getLogger("disagg_proxy")
# Data structures
@dataclass
class CachedKVEntry:
"""KV transfer parameters cached from D's response for one turn."""
kv_transfer_params: dict[str, Any]
timestamp: float = field(default_factory=time.time)
class ConversationKVCache:
"""Per-conversation KV block cache.
Each conversation is identified by a ``conversation_id`` supplied by
the client. After D finishes a turn, its ``kv_transfer_params`` are
stored here. On the next turn, the proxy retrieves them so P can
read D's blocks via bidirectional KV transfer.
"""
def __init__(self, ttl_seconds: float = 600.0) -> None:
self._store: dict[str, CachedKVEntry] = {}
self._ttl = ttl_seconds
def get(self, conversation_id: str) -> dict[str, Any] | None:
"""Retrieve and consume cached KV params for a conversation.
Returns a *copy* of the kv_transfer_params dict, or None.
The entry is removed after retrieval (single-use).
"""
entry = self._store.pop(conversation_id, None)
if entry is None:
return None
age = time.time() - entry.timestamp
if age > self._ttl:
logger.info(
"conv=%s: stale cache entry (age=%.1fs > ttl=%.1fs), discarding",
conversation_id,
age,
self._ttl,
)
return None
logger.info(
"conv=%s: cache HIT (age=%.1fs)",
conversation_id,
age,
)
return dict(entry.kv_transfer_params)
def put(self, conversation_id: str, kv_params: dict[str, Any]) -> None:
"""Store D's kv_transfer_params for a conversation."""
self._store[conversation_id] = CachedKVEntry(
kv_transfer_params=dict(kv_params), # defensive copy
)
logger.info(
"conv=%s: cached D blocks (remote_request_id=%s, blocks=%d)",
conversation_id,
kv_params.get("remote_request_id", "?"),
len(kv_params.get("remote_block_ids", [[]])[0])
if kv_params.get("remote_block_ids")
else 0,
)
def evict_stale(self) -> int:
"""Remove entries older than TTL. Returns count of evicted entries."""
now = time.time()
stale = [
cid
for cid, entry in self._store.items()
if now - entry.timestamp > self._ttl
]
for cid in stale:
del self._store[cid]
return len(stale)
@property
def size(self) -> int:
return len(self._store)
# Global state
kv_cache = ConversationKVCache(
ttl_seconds=450.0
) # Must be < VLLM_NIXL_ABORT_REQUEST_TIMEOUT (480s)
# Service client helpers
@dataclass
class ServiceClient:
"""Wrapper around an httpx.AsyncClient for a P or D instance."""
client: httpx.AsyncClient
host: str
port: int
id: int
def _make_headers(request_id: str) -> dict[str, str]:
"""Build HTTP headers for upstream requests."""
headers = {"X-Request-Id": request_id}
api_key = os.environ.get("OPENAI_API_KEY")
if api_key:
headers["Authorization"] = f"Bearer {api_key}"
return headers
async def _send_to_prefill(
client: ServiceClient,
endpoint: str,
req_data: dict[str, Any],
request_id: str,
) -> dict[str, Any]:
"""Send a non-streaming prefill request (max_tokens=1).
Returns the JSON response from P, which includes kv_transfer_params.
"""
payload = req_data.copy()
payload["stream"] = False
payload["max_tokens"] = 1
payload.pop("max_completion_tokens", None)
payload.pop("min_tokens", None)
payload.pop("stream_options", None)
resp = await client.client.post(
endpoint,
json=payload,
headers=_make_headers(request_id),
)
resp.raise_for_status()
return resp.json()
async def _stream_from_decode(
client: ServiceClient,
endpoint: str,
req_data: dict[str, Any],
request_id: str,
conversation_id: str,
) -> tuple[str, str | None, dict[str, Any] | None, str, str | None, int | None]:
"""Stream response from D, capturing text and kv_transfer_params.
Returns (collected_text, finish_reason, kv_params, response_id, created).
Also stores kv_params in the conversation cache.
"""
payload = req_data.copy()
payload["stream"] = True
collected_text = ""
finish_reason: str | None = None
response_id: str | None = None
model_name: str | None = None
created: int | None = None
captured_kv: dict[str, Any] | None = None
async with client.client.stream(
"POST",
endpoint,
json=payload,
headers=_make_headers(request_id),
) as resp:
resp.raise_for_status()
async for line in resp.aiter_lines():
if not line or not line.startswith("data: "):
continue
if line == "data: [DONE]":
break
try:
chunk = json.loads(line[6:])
except json.JSONDecodeError:
continue
if response_id is None:
response_id = chunk.get("id")
model_name = chunk.get("model")
created = chunk.get("created")
for choice in chunk.get("choices", []):
collected_text += choice.get("text", "")
delta = choice.get("delta", {})
collected_text += delta.get("content", "")
if choice.get("finish_reason"):
finish_reason = choice["finish_reason"]
kv_params = chunk.get("kv_transfer_params")
if kv_params:
kv_params["remote_host"] = client.host
captured_kv = kv_params
if conversation_id:
kv_cache.put(conversation_id, kv_params)
return (
collected_text,
finish_reason,
captured_kv,
response_id or request_id,
model_name,
created,
)
async def _stream_from_decode_sse(
client: ServiceClient,
endpoint: str,
req_data: dict[str, Any],
request_id: str,
conversation_id: str,
):
"""Yield SSE chunks from D to the client, capturing kv_transfer_params."""
payload = req_data.copy()
payload["stream"] = True
async with client.client.stream(
"POST",
endpoint,
json=payload,
headers=_make_headers(request_id),
) as resp:
resp.raise_for_status()
async for line in resp.aiter_lines():
if not line:
yield "\n"
continue
if line.startswith("data: ") and line != "data: [DONE]":
try:
chunk = json.loads(line[6:])
kv_params = chunk.get("kv_transfer_params")
if kv_params and conversation_id:
kv_params["remote_host"] = client.host
kv_cache.put(conversation_id, kv_params)
except json.JSONDecodeError:
pass
yield line + "\n"
# FastAPI application
@asynccontextmanager
async def lifespan(app: FastAPI):
"""Initialize HTTP clients for P and D instances."""
app.state.prefill_clients: list[ServiceClient] = []
app.state.decode_clients: list[ServiceClient] = []
for i, (host, port) in enumerate(global_args.prefiller_instances):
app.state.prefill_clients.append(
ServiceClient(
client=httpx.AsyncClient(
timeout=None,
base_url=f"http://{host}:{port}/v1",
),
host=host,
port=port,
id=i,
)
)
for i, (host, port) in enumerate(global_args.decoder_instances):
app.state.decode_clients.append(
ServiceClient(
client=httpx.AsyncClient(
timeout=None,
base_url=f"http://{host}:{port}/v1",
),
host=host,
port=port,
id=i,
)
)
app.state.prefill_iter = itertools.cycle(range(len(app.state.prefill_clients)))
app.state.decode_iter = itertools.cycle(range(len(app.state.decode_clients)))
logger.info(
"Ready: %d prefill, %d decode instances",
len(app.state.prefill_clients),
len(app.state.decode_clients),
)
yield
for sc in app.state.prefill_clients + app.state.decode_clients:
await sc.client.aclose()
app = FastAPI(title="Disaggregated P/D Proxy (Multi-turn)", lifespan=lifespan)
def _next_client(app_state, role: str) -> ServiceClient:
if role == "prefill":
return app_state.prefill_clients[next(app_state.prefill_iter)]
return app_state.decode_clients[next(app_state.decode_iter)]
# Request handler
async def _handle_request(api_path: str, request: Request):
"""Core request handler for both /v1/chat/completions and /v1/completions."""
req_data = await request.json()
request_id = str(uuid.uuid4())
conversation_id: str = req_data.pop("conversation_id", "")
client_wants_stream = req_data.get("stream", False)
if not conversation_id:
logger.warning(
"[%s] No conversation_id provided — KV cache reuse disabled "
"for this request. Add a 'conversation_id' field to enable "
"cross-turn KV sharing. When using "
"benchmarks/multi_turn/benchmark_serving_multi_turn.py, pass "
"--send-conversation-id (off by default).",
request_id,
)
# Step 1: Look up cached D blocks from the previous turn
cached_kv = kv_cache.get(conversation_id) if conversation_id else None
if cached_kv:
# Tell P to read D's blocks (bidirectional transfer)
cached_kv["do_remote_decode"] = True
cached_kv["do_remote_prefill"] = False
req_data["kv_transfer_params"] = cached_kv
logger.info(
"[%s] conv=%s: sending D's cached blocks to P (remote_request_id=%s)",
request_id,
conversation_id,
cached_kv.get("remote_request_id"),
)
else:
# No cached blocks — P recomputes from scratch
req_data["kv_transfer_params"] = {
"do_remote_decode": True,
"do_remote_prefill": False,
"remote_engine_id": None,
"remote_block_ids": None,
"remote_host": None,
"remote_port": None,
}
logger.info("[%s] conv=%s: cache MISS", request_id, conversation_id)
# Step 2: Send to Prefill node (non-streaming, max_tokens=1)
prefill_client = _next_client(request.app.state, "prefill")
t0 = time.time()
prefill_resp = await _send_to_prefill(
prefill_client,
api_path,
req_data,
request_id,
)
logger.info(
"[%s] Prefill done in %.0fms",
request_id,
(time.time() - t0) * 1000,
)
# Attach P's kv_transfer_params for D to read P's blocks
p_kv_params = prefill_resp.get("kv_transfer_params", {})
if p_kv_params:
p_kv_params["remote_host"] = prefill_client.host
req_data["kv_transfer_params"] = p_kv_params
# Step 3: Stream from Decode node, capturing kv_transfer_params
decode_client = _next_client(request.app.state, "decode")
if client_wants_stream:
return StreamingResponse(
_stream_from_decode_sse(
decode_client,
api_path,
req_data,
request_id,
conversation_id,
),
media_type="text/event-stream",
)
text, finish_reason, _, resp_id, model, created = await _stream_from_decode(
decode_client,
api_path,
req_data,
request_id,
conversation_id,
)
# Build OpenAI-compatible response
is_chat = "messages" in req_data
if is_chat:
body = {
"id": resp_id,
"object": "chat.completion",
"created": created or int(time.time()),
"model": model or req_data.get("model", ""),
"choices": [
{
"index": 0,
"message": {"role": "assistant", "content": text},
"finish_reason": finish_reason,
}
],
"usage": None,
}
else:
body = {
"id": resp_id,
"object": "text_completion",
"created": created or int(time.time()),
"model": model or req_data.get("model", ""),
"choices": [
{
"index": 0,
"text": text,
"logprobs": None,
"finish_reason": finish_reason,
}
],
"usage": None,
}
return JSONResponse(content=body)
# Routes
@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
return await _handle_request("/chat/completions", request)
@app.post("/v1/completions")
async def completions(request: Request):
return await _handle_request("/completions", request)
@app.get("/health")
async def health():
evicted = kv_cache.evict_stale()
return {
"status": "ok",
"cached_conversations": kv_cache.size,
"evicted_stale": evicted,
}
# CLI
def parse_args() -> argparse.Namespace:
p = argparse.ArgumentParser(
description="Disaggregated P/D proxy with bidirectional KV transfer",
)
p.add_argument("--host", default="0.0.0.0")
p.add_argument("--port", type=int, default=8000)
p.add_argument(
"--prefiller-host",
"--prefiller-hosts",
dest="prefiller_hosts",
nargs="+",
default=["localhost"],
)
p.add_argument(
"--prefiller-port",
"--prefiller-ports",
dest="prefiller_ports",
type=int,
nargs="+",
default=[8100],
)
p.add_argument(
"--decoder-host",
"--decoder-hosts",
dest="decoder_hosts",
nargs="+",
default=["localhost"],
)
p.add_argument(
"--decoder-port",
"--decoder-ports",
dest="decoder_ports",
type=int,
nargs="+",
default=[8200],
)
args = p.parse_args()
if len(args.prefiller_hosts) != len(args.prefiller_ports):
p.error("Number of prefiller hosts must match ports")
if len(args.decoder_hosts) != len(args.decoder_ports):
p.error("Number of decoder hosts must match ports")
args.prefiller_instances = list(zip(args.prefiller_hosts, args.prefiller_ports))
args.decoder_instances = list(zip(args.decoder_hosts, args.decoder_ports))
return args
if __name__ == "__main__":
global global_args
global_args = parse_args()
import uvicorn
uvicorn.run(app, host=global_args.host, port=global_args.port)


## disagg_proxy_pushconnector_demo.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Push-mode disaggregated prefilling proxy demo.
Companion to ``disagg_proxy_demo.py`` (pull mode). The client-facing API is
the same; the difference is in how P and D coordinate the KV transfer:
* Pull mode: proxy forwards P's ``kv_transfer_params`` (including
``remote_block_ids``) to D, and D pulls KV from P via NIXL READ.
* Push mode: proxy hands D **only** P's coordinates
(``remote_engine_id``, ``remote_host``, ``remote_port``, ``tp_size``,
``pp_size``) and the shared ``remote_request_id``. D registers its locally
allocated blocks with P over a NIXL notification; P then pushes the KV to D via
NIXL WRITE.
Launch multiple vLLM instances configured with ``NixlPushConnector`` and
matching ``engine_id`` / ``side_channel_port``, then start this proxy:
python3 examples/disaggregated/disaggregated_serving/\
disagg_proxy_pushconnector_demo.py \
--model $model_name \
--prefill localhost:8100 \
--decode localhost:8200 \
--prefill-engine-id prefill-engine-001 \
--prefill-kv-host 10.0.0.1 \
--prefill-side-channel-port 5600 \
--prefill-tp-size 1 \
--prefill-pp-size 1 \
--port 8000
"""
import argparse
import asyncio
import contextlib
import ipaddress
import itertools
import json
import logging
import os
import sys
import uuid
from abc import ABC, abstractmethod
from collections.abc import Callable
import aiohttp
import uvicorn
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(total=6 * 60 * 60)
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
class SchedulingPolicy(ABC):
@abstractmethod
def schedule(self, cycler: itertools.cycle):
raise NotImplementedError("Scheduling Proxy is not set.")
class RoundRobinSchedulingPolicy(SchedulingPolicy):
def schedule(self, cycler: itertools.cycle) -> str:
return next(cycler)
class PushProxy:
"""Push-mode proxy.
The structure mirrors the pull-mode ``Proxy`` in
``disagg_proxy_demo.py``: an APIRouter with ``/v1/completions``,
``/v1/chat/completions``, ``/status`` and ``/instances/add``, plus
round-robin scheduling across multiple P / D instances.
Push-specific differences are confined to the request-handling
methods (``create_completion`` / ``create_chat_completion``):
* D's ``kv_transfer_params`` is built from CLI-provided P
coordinates instead of being derived from P's response.
* P and D requests are issued concurrently — D registers blocks and
waits while P prefills and pushes.
"""
def __init__(
self,
prefill_instances: list[str],
decode_instances: list[str],
model: str,
scheduling_policy: SchedulingPolicy,
prefill_engine_id: str,
prefill_kv_host: str,
prefill_side_channel_port: int,
prefill_tp_size: int,
prefill_pp_size: int,
custom_create_completion: Callable[[Request], StreamingResponse] | None = None,
custom_create_chat_completion: Callable[[Request], StreamingResponse]
| None = None,
):
self.prefill_instances = prefill_instances
self.decode_instances = decode_instances
self.prefill_cycler = itertools.cycle(prefill_instances)
self.decode_cycler = itertools.cycle(decode_instances)
self.model = model
self.scheduling_policy = scheduling_policy
# Push-mode metadata: D needs P's coordinates up-front. Pull mode
# learns these from P's response; push mode uses CLI args because
# D issues its registration before P responds.
self.push_metadata = {
"do_remote_decode": False,
"do_remote_prefill": True,
"remote_engine_id": prefill_engine_id,
"remote_host": prefill_kv_host,
"remote_port": prefill_side_channel_port,
"tp_size": prefill_tp_size,
"pp_size": prefill_pp_size,
}
self.custom_create_completion = custom_create_completion
self.custom_create_chat_completion = custom_create_chat_completion
self.router = APIRouter()
self.setup_routes()
# ── routes ──────────────────────────────────────────────────────── #
def setup_routes(self):
self.router.post(
"/v1/completions", dependencies=[Depends(self.validate_json_request)]
)(
self.custom_create_completion
if self.custom_create_completion
else self.create_completion
)
self.router.post(
"/v1/chat/completions", dependencies=[Depends(self.validate_json_request)]
)(
self.custom_create_chat_completion
if self.custom_create_chat_completion
else self.create_chat_completion
)
self.router.get("/status", response_class=JSONResponse)(self.get_status)
async def validate_json_request(self, raw_request: Request):
content_type = raw_request.headers.get("content-type", "").lower()
if content_type != "application/json":
raise HTTPException(
status_code=415,
detail="Unsupported Media Type: Only 'application/json' is allowed",
)
# ── HTTP forwarding ─────────────────────────────────────────────── #
async def forward_request(self, url, data, headers, use_chunked=True):
async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as session:
try:
async with session.post(
url=url, json=data, headers=headers
) as response:
if 200 <= response.status < 300 or 400 <= response.status < 500:
if use_chunked:
async for chunk_bytes in response.content.iter_chunked(
1024
):
yield chunk_bytes
else:
yield await response.read()
else:
error_content = await response.text()
with contextlib.suppress(json.JSONDecodeError):
error_content = json.loads(error_content)
logger.error(
"Request failed with status %s: %s",
response.status,
error_content,
)
raise HTTPException(
status_code=response.status,
detail=f"Request failed with status {response.status}: "
f"{error_content}",
)
except aiohttp.ClientError as e:
logger.error("ClientError occurred: %s", str(e))
raise HTTPException(
status_code=502,
detail="Bad Gateway: Error communicating with upstream server.",
) from e
except Exception as e:
logger.error("Unexpected error: %s", str(e))
raise HTTPException(status_code=500, detail=str(e)) from e
def schedule(self, cycler: itertools.cycle) -> str:
return self.scheduling_policy.schedule(cycler)
async def get_status(self):
return {
"mode": "push",
"prefill_node_count": len(self.prefill_instances),
"decode_node_count": len(self.decode_instances),
"prefill_nodes": self.prefill_instances,
"decode_nodes": self.decode_instances,
"prefill_engine_id": self.push_metadata["remote_engine_id"],
"prefill_kv_host": self.push_metadata["remote_host"],
"prefill_side_channel_port": self.push_metadata["remote_port"],
"prefill_tp_size": self.push_metadata["tp_size"],
"prefill_pp_size": self.push_metadata["pp_size"],
}
# ── push-mode request handling ──────────────────────────────────── #
def _build_decode_kv_params(self, request_id: str) -> dict:
"""Push-mode kv_transfer_params for D.
``remote_block_ids`` is intentionally omitted: D allocates its
own blocks and registers them with P; P determines the
prefill-side block IDs and ships them via the WRITE.
"""
params = self.push_metadata.copy()
params["remote_request_id"] = request_id
return params
def _common_headers(self, request_id: str) -> dict:
h = {"X-Request-Id": request_id}
api_key = os.environ.get("OPENAI_API_KEY")
if api_key:
h["Authorization"] = f"Bearer {api_key}"
return h
async def _push_completion(self, raw_request: Request, path: str):
"""Shared body for /v1/completions and /v1/chat/completions.
Push mode fires P and D concurrently:
* P runs a normal prefill (max_tokens=1, do_remote_decode=True).
* D runs the decode (do_remote_prefill=True, no remote_block_ids).
D blocks waiting for P's WRITE; the response streamed back to the
client is the decode output from D.
"""
request = await raw_request.json()
request_id = str(uuid.uuid4())
# Prefill leg (max_tokens=1, signals P to keep KV around for D).
prefill_request = request.copy()
prefill_request["max_tokens"] = 1
if "max_completion_tokens" in prefill_request:
prefill_request["max_completion_tokens"] = 1
prefill_request["kv_transfer_params"] = {
"do_remote_decode": True,
"do_remote_prefill": False,
"remote_engine_id": None,
"remote_block_ids": None,
"remote_host": None,
"remote_port": None,
}
# Decode leg (push mode: no remote_block_ids).
decode_request = request.copy()
decode_request["kv_transfer_params"] = self._build_decode_kv_params(request_id)
prefill_instance = self.schedule(self.prefill_cycler)
decode_instance = self.schedule(self.decode_cycler)
headers = self._common_headers(request_id)
async def drain_prefill():
async for _ in self.forward_request(
f"http://{prefill_instance}{path}", prefill_request, headers
):
continue
prefill_task = asyncio.create_task(drain_prefill())
async def stream_decode():
try:
async for chunk in self.forward_request(
f"http://{decode_instance}{path}", decode_request, headers
):
yield chunk
finally:
await prefill_task
return StreamingResponse(stream_decode(), media_type="application/json")
async def create_completion(self, raw_request: Request):
try:
return await self._push_completion(raw_request, "/v1/completions")
except HTTPException:
raise
except Exception:
exc_info = sys.exc_info()
print("Error occurred in disagg push proxy server")
print(exc_info)
raise
async def create_chat_completion(self, raw_request: Request):
try:
return await self._push_completion(raw_request, "/v1/chat/completions")
except HTTPException:
raise
except Exception:
exc_info = sys.exc_info()
error_messages = [str(e) for e in exc_info if e]
print("Error occurred in disagg push proxy server")
print(error_messages)
return StreamingResponse(
content=iter(error_messages), media_type="text/event-stream"
)
class PushProxyServer:
def __init__(
self,
args: argparse.Namespace,
scheduling_policy: SchedulingPolicy | None = None,
create_completion: Callable[[Request], StreamingResponse] | None = None,
create_chat_completion: Callable[[Request], StreamingResponse] | None = None,
):
self.validate_parsed_serve_args(args)
self.port = args.port
self.proxy_instance = PushProxy(
prefill_instances=[] if args.prefill is None else args.prefill,
decode_instances=[] if args.decode is None else args.decode,
model=args.model,
scheduling_policy=(
scheduling_policy
if scheduling_policy is not None
else RoundRobinSchedulingPolicy()
),
prefill_engine_id=args.prefill_engine_id,
prefill_kv_host=args.prefill_kv_host,
prefill_side_channel_port=args.prefill_side_channel_port,
prefill_tp_size=args.prefill_tp_size,
prefill_pp_size=args.prefill_pp_size,
custom_create_completion=create_completion,
custom_create_chat_completion=create_chat_completion,
)
def validate_parsed_serve_args(self, args: argparse.Namespace):
if not args.prefill:
raise ValueError("Please specify at least one prefill node.")
if not args.decode:
raise ValueError("Please specify at least one decode node.")
if not args.prefill_engine_id:
raise ValueError(
"--prefill-engine-id is required in push mode (it must match "
"the engine_id passed to the prefill vLLM instance via "
"--kv-transfer-config)."
)
if not args.prefill_kv_host:
raise ValueError(
"--prefill-kv-host is required in push mode (the IP / host "
"that the prefill vLLM advertises on its NIXL side channel)."
)
self.validate_instances(args.prefill)
self.validate_instances(args.decode)
def validate_instances(self, instances: list):
for instance in instances:
if len(instance.split(":")) != 2:
raise ValueError(f"Invalid instance format: {instance}")
host, port = instance.split(":")
try:
if host != "localhost":
ipaddress.ip_address(host)
port = int(port)
if not (0 < port < 65536):
raise ValueError(f"Invalid port number in instance: {instance}")
except Exception as e:
raise ValueError(f"Invalid instance {instance}: {str(e)}") from e
def run_server(self):
app = FastAPI()
app.include_router(self.proxy_instance.router)
config = uvicorn.Config(app, port=self.port, loop="uvloop")
server = uvicorn.Server(config)
server.run()
def parse_args():
parser = argparse.ArgumentParser("vLLM disaggregated push-mode proxy server.")
parser.add_argument("--model", "-m", type=str, required=True, help="Model name")
parser.add_argument(
"--prefill",
"-p",
type=str,
nargs="+",
help="List of prefill node URLs (host:port)",
)
parser.add_argument(
"--decode",
"-d",
type=str,
nargs="+",
help="List of decode node URLs (host:port)",
)
parser.add_argument(
"--port",
type=int,
default=8000,
help="Server port number",
)
# Push-mode specific: P's coordinates that D needs in advance.
parser.add_argument(
"--prefill-engine-id",
type=str,
required=True,
help=(
"engine_id of the prefill vLLM instance (must match "
"--kv-transfer-config engine_id on the prefill server)"
),
)
parser.add_argument(
"--prefill-kv-host",
type=str,
required=True,
help=(
"IP / host the prefill vLLM advertises on its NIXL side "
"channel (VLLM_NIXL_SIDE_CHANNEL_HOST)"
),
)
parser.add_argument(
"--prefill-side-channel-port",
type=int,
default=5600,
help="NIXL side channel port on the prefill node "
"(VLLM_NIXL_SIDE_CHANNEL_PORT, default 5600)",
)
parser.add_argument(
"--prefill-tp-size",
type=int,
default=1,
help="Tensor parallel size of the prefill vLLM instance",
)
parser.add_argument(
"--prefill-pp-size",
type=int,
default=1,
help="Pipeline parallel size of the prefill vLLM instance",
)
return parser.parse_args()
if __name__ == "__main__":
args = parse_args()
proxy_server = PushProxyServer(args=args)
proxy_server.run_server()


## kv_events.sh

#!/bin/bash
# This file demonstrates the KV cache event publishing
# We will launch a vllm instances configured to publish KV cache
# events and launch a simple subscriber to log those events.
set -xe
echo "🚧🚧 Warning: The usage of KV cache events is experimental and subject to change 🚧🚧"
sleep 1
MODEL_NAME=${HF_MODEL_NAME:-meta-llama/Meta-Llama-3.1-8B-Instruct}
# Trap the SIGINT signal (triggered by Ctrl+C)
trap 'cleanup' INT
# Cleanup function
cleanup() {
echo "Caught Ctrl+C, cleaning up..."
# Cleanup commands
pgrep python | xargs kill -9
pkill -f python
echo "Cleanup complete. Exiting."
exit 0
}
export VLLM_HOST_IP=$(hostname -I | awk '{print $1}')
# a function that waits vLLM server to start
wait_for_server() {
local port=$1
timeout 1200 bash -c "
until curl -s localhost:${port}/v1/completions > /dev/null; do
sleep 1
done" && return 0 || return 1
}
vllm serve "$MODEL_NAME" \
--port 8100 \
--max-model-len 100 \
--enforce-eager \
--gpu-memory-utilization 0.8 \
--trust-remote-code \
--kv-events-config \
'{"enable_kv_cache_events": true, "publisher": "zmq", "topic": "kv-events"}' &
wait_for_server 8100
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python3 "$SCRIPT_DIR/kv_events_subscriber.py" &
sleep 1
# serve two example requests
output1=$(curl -X POST -s http://localhost:8100/v1/completions \
-H "Content-Type: application/json" \
-d '{
"model": "'"$MODEL_NAME"'",
"prompt": "Explain quantum computing in simple terms a 5-year-old could understand.",
"max_tokens": 80,
"temperature": 0
}')
output2=$(curl -X POST -s http://localhost:8100/v1/completions \
-H "Content-Type: application/json" \
-d '{
"model": "'"$MODEL_NAME"'",
"prompt": "Explain quantum computing in simple terms a 50-year-old could understand.",
"max_tokens": 80,
"temperature": 0
}')
# Cleanup commands
pkill -9 -u "$USER" -f python
pkill -9 -u "$USER" -f vllm
sleep 1
echo "Cleaned up"
# Print the outputs of the curl requests
echo ""
echo "Output of first request: $output1"
echo "Output of second request: $output2"
echo "🎉🎉 Successfully finished 2 test requests! 🎉🎉"
echo ""


## moriio_toy_proxy_server.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
#
# Minimal single-node reference proxy for MoRI-IO prefill/decode disaggregation.
# It demonstrates the DP-rank pinning contract the connector expects: pick one
# prefill DP rank per request (flat_interleaved_dp_route) and pin BOTH legs to it
# via the ``X-data-parallel-rank`` header plus ``kv_transfer_params``
# (``remote_dp_rank`` / ``remote_dp_size`` / ``remote_tp_size``).
#
# Scope: single-node only. It intentionally does NOT supply the cross-pod
# Wide-EP (2P2D) peer info -- ``remote_hosts`` / ``multi_pod_hosts``,
# ``data_parallel_size_local``, ``is_request_leader``. In real multi-pod
# deployments that peer info is produced by a production routing sidecar, e.g.:
# * llm-d-router (https://github.com/llm-d/llm-d-router)
# * vLLM's own vllm-router (examples in the vllm-project org)
# * or any NIXL-shaped router that sets the same kv_transfer_params contract.
# Use this file as a protocol reference, not a production router.
import argparse
import asyncio
import copy
import logging
import os
import socket
import threading
import uuid
from urllib.parse import urlparse
import aiohttp
import msgpack
import zmq
from quart import Quart, Request, make_response, request
from vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common import (
MoRIIOConstants,
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
prefill_instances: list[dict] = []
decode_instances: list[dict] = []
request_nums = 0
app = Quart(__name__)
TRANSFER_TYPE = None
_list_lock = threading.RLock()
def _listen_for_register(hostname, port):
context = zmq.Context()
router_socket = context.socket(zmq.ROUTER)
router_socket.bind(f"tcp://{hostname}:{port}")
poller = zmq.Poller()
poller.register(router_socket, zmq.POLLIN)
global prefill_instances
global decode_instances
while True:
socks = dict(poller.poll())
if router_socket in socks:
remote_addr, msg = router_socket.recv_multipart()
data = msgpack.loads(msg)
if data.get("type") == "HELLO":
pass
elif data.get("type") in ("P", "D"):
role = data["type"]
required_keys = {
"http_address",
"zmq_address",
"dp_size",
"tp_size",
"transfer_mode",
}
missing = required_keys - data.keys()
if missing:
logger.error(
"Registration message missing required keys %s; skipping",
missing,
)
continue
# Derive request_address from http_address
# api path suffix is appended at request time
instance = {
"role": role,
"request_address": f"http://{data['http_address']}/v1",
"http_address": data["http_address"],
"zmq_address": data["zmq_address"],
"dp_size": data["dp_size"],
"tp_size": data["tp_size"],
"transfer_mode": data["transfer_mode"],
}
# zmq_address format: "host:IP,handshake:PORT,notify:PORT"
# Stored verbatim; embedded into the request_id by handle_request.
global TRANSFER_TYPE
transfer_mode = instance["transfer_mode"]
target_list = prefill_instances if role == "P" else decode_instances
with _list_lock:
if TRANSFER_TYPE is None:
TRANSFER_TYPE = transfer_mode
logger.info("SET TRANSFER TYPE TO %s", TRANSFER_TYPE)
elif transfer_mode != TRANSFER_TYPE:
logger.error(
"Mismatched transfer mode: expected %s, got %s;"
" skipping registration of %s",
TRANSFER_TYPE,
transfer_mode,
data["http_address"],
)
continue
existing_idx = next(
(
idx
for idx, i in enumerate(target_list)
if i.get("http_address") == data["http_address"]
),
None,
)
if existing_idx is not None:
target_list[existing_idx] = instance
logger.info(
"Updated existing %s instance: %s",
"Prefill" if role == "P" else "Decode",
instance,
)
else:
target_list.append(instance)
logger.info(
"Registered %s instance: %s",
"Prefill" if role == "P" else "Decode",
instance,
)
else:
logger.warning(
"Received message with unrecognized type %r; ignoring",
data.get("type"),
)
def start_service_discovery(hostname, port):
if not hostname:
hostname = socket.gethostname()
if port == 0:
raise ValueError("Port cannot be 0")
_listener_thread = threading.Thread(
target=_listen_for_register, args=(hostname, port), daemon=True
)
_listener_thread.start()
return _listener_thread
async def send_request_to_prefill(
endpoint, req_data, request_id, selected_prefill_dp_rank
):
req_data_copy = req_data
req_data_copy["kv_transfer_params"].update(
{
"do_remote_decode": True,
"do_remote_prefill": False,
"remote_engine_id": None,
"remote_block_ids": None,
}
)
req_data_copy["stream"] = False
req_data_copy["max_tokens"] = 1
if "max_completion_tokens" in req_data_copy:
req_data_copy["max_completion_tokens"] = 1
if "stream_options" in req_data_copy:
del req_data_copy["stream_options"]
async with aiohttp.ClientSession(
timeout=aiohttp.ClientTimeout(total=6 * 6000 * 6000)
) as session:
headers = {
"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
"X-Request-Id": request_id,
}
if selected_prefill_dp_rank is not None:
headers["X-data-parallel-rank"] = str(selected_prefill_dp_rank)
async with session.post(
url=endpoint, json=req_data_copy, headers=headers
) as response:
if response.status == 200:
return await response.json()
else:
error_message = (
f"send_request_to_prefill response ={response},"
f"reason={response.reason}, status={response.status},"
f"method={response.method}, url={response.url},"
f"real_url={response.real_url}"
)
raise RuntimeError(error_message)
async def start_decode_request(endpoint, req_data, request_id, selected_dp_rank=None):
session = aiohttp.ClientSession(
timeout=aiohttp.ClientTimeout(total=6 * 6000 * 6000)
)
headers = {
"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
"X-Request-Id": request_id,
}
# Pin the decode leg to the same DP rank as its prefill leg so both land on
# the same rank (vLLM reads this header directly; no engine-side routing).
if selected_dp_rank is not None:
headers["X-data-parallel-rank"] = str(selected_dp_rank)
response = await session.post(url=endpoint, json=req_data, headers=headers)
return session, response
async def stream_decode_response(session, response, request_id):
try:
if response.status == 200:
async for chunk_bytes in response.content.iter_chunked(1024):
yield chunk_bytes
else:
error_message = (
f"stream_decode_response response ={response},"
f"reason={response.reason}, status={response.status},"
f"method={response.method}, url={response.url},"
f"real_url={response.real_url}"
)
raise RuntimeError(error_message)
finally:
await session.close()
def flat_interleaved_dp_route(request_number, instances):
"""Flat round-robin over the full (instance, dp_rank) slot space.
ONE counter over (n_instances * dp_size) slots, so instance-selection and
DP-rank-selection are derived from the SAME index and can never alias. The
previous scheme computed instance = req % n and rank = req % dp from the
same counter with n | dp, which locked each instance to a stride-n subset
of its ranks (e.g. 2 prefill instances -> 4 of 8 ranks each -> half the
GPUs never receive a request, so the deployment falsely appears not to
scale).
Interleaved order — inst0_r0, inst1_r0, inst0_r1, inst1_r1, ... — so
consecutive requests alternate instances AND every rank gets walked.
Assumes homogeneous dp_size across a role's instances (true for the
DP<->DP and DP<->TP deployments this proxy targets). Returns
(instance_index, dp_rank); dp_rank is None when dp_size == 1 (e.g. a TP
decode), which avoids forwarding an out-of-range data-parallel rank.
"""
n = len(instances)
dp = instances[0]["dp_size"]
slot = (request_number - 1) % (n * dp)
inst_idx = slot % n
dp_rank = (slot // n) if dp > 1 else None
return inst_idx, dp_rank
@app.route("/health", methods=["GET"])
async def health():
# Benchmark harnesses and load balancers often probe the proxy URL and
# treat a non-200 response as a dead service. Backends expose /health, but
# this proxy used to lack one; report the proxy process itself as healthy.
return ("ok", 200)
@app.route("/v1/completions", methods=["POST"])
async def handle_completions_request():
return await handle_request("/completions", request)
@app.route("/v1/chat/completions", methods=["POST"])
async def handle_chat_completions_request():
return await handle_request("/chat/completions", request)
async def handle_request(api: str, request: Request):
try:
with _list_lock:
global request_nums
request_nums += 1
req_data = await request.get_json()
prefill_instance_endpoint = None
decode_instance_endpoint = None
error_msg = (
"Service Unavailable: No prefill or decode instances are registered."
)
if not prefill_instances or not decode_instances:
return await make_response(
(
error_msg,
503,
)
)
# Flat interleaved round-robin (see flat_interleaved_dp_route): ONE
# counter over the full (instance, dp_rank) slot space per role, so
# instance-selection and DP-rank-selection derive from the same index
# and can never alias. The old scheme keyed both on request_nums with
# n_instances | dp_size, stranding half the ranks (e.g. in 2P_DP8EP).
pid, selected_prefill_dp_rank = flat_interleaved_dp_route(
request_nums, prefill_instances
)
# Decode instance selection uses the same interleaved walk; in READ
# mode the decode reads KV from selected_prefill_dp_rank, so the
# decode's own dp_rank is not forwarded here.
did, _ = flat_interleaved_dp_route(request_nums, decode_instances)
prefill_instance_endpoint = prefill_instances[pid]
decode_instance_endpoint = decode_instances[did]
# Embed both zmq_addresses in the request_id so the connector can parse
# the peer's host/ports from it, similar to P2P-NCCL
uid = str(uuid.uuid4()).replace("-", "")
request_id = (
f"___prefill_addr_{prefill_instance_endpoint['zmq_address']}"
f"___decode_addr_{decode_instance_endpoint['zmq_address']}"
f"_{uid}"
)
transfer_id = f"{MoRIIOConstants.TRANSFER_PREFIX}-{str(uuid.uuid4())}"
req_data_to_prefill = copy.deepcopy(req_data)
req_data_to_prefill["kv_transfer_params"] = {}
req_data["kv_transfer_params"] = {}
req_data_to_prefill["kv_transfer_params"]["remote_dp_size"] = (
decode_instance_endpoint["dp_size"]
)
req_data_to_prefill["kv_transfer_params"]["remote_tp_size"] = (
decode_instance_endpoint["tp_size"]
)
req_data_to_prefill["kv_transfer_params"]["transfer_id"] = transfer_id
prefill_request_url = prefill_instance_endpoint["request_address"] + api
send_prefill_task = asyncio.create_task(
send_request_to_prefill(
prefill_request_url,
req_data_to_prefill,
request_id,
selected_prefill_dp_rank,
)
)
# max_completion_tokens takes precedence when present (that's the limit
# the backend enforces); fall back to max_tokens. If neither is set
# (e.g. benchmark clients that omit it), leave the request unchanged.
if "max_completion_tokens" in req_data:
req_data["max_completion_tokens"] -= 1
elif "max_tokens" in req_data:
req_data["max_tokens"] -= 1
req_data["kv_transfer_params"] = {
"do_remote_decode": False,
"do_remote_prefill": True,
"remote_engine_id": None,
"remote_block_ids": None,
"transfer_id": transfer_id,
}
if TRANSFER_TYPE == "READ":
# In read mode, prefill and decode are executed serially.
prefill_response = await send_prefill_task
prefill_kv = prefill_response["kv_transfer_params"]
req_data["kv_transfer_params"]["remote_engine_id"] = prefill_kv[
"remote_engine_id"
]
req_data["kv_transfer_params"]["remote_block_ids"] = prefill_kv[
"remote_block_ids"
]
req_data["kv_transfer_params"]["transfer_id"] = prefill_kv["transfer_id"]
if prefill_kv.get("tp_size") is not None:
req_data["kv_transfer_params"]["tp_size"] = prefill_kv["tp_size"]
req_data["kv_transfer_params"]["remote_dp_size"] = prefill_instance_endpoint[
"dp_size"
]
req_data["kv_transfer_params"]["remote_tp_size"] = prefill_instance_endpoint[
"tp_size"
]
if selected_prefill_dp_rank is not None:
req_data["kv_transfer_params"]["remote_dp_rank"] = selected_prefill_dp_rank
decode_request_url = decode_instance_endpoint["request_address"] + api
decode_request_task = asyncio.create_task(
start_decode_request(
decode_request_url, req_data, request_id, selected_prefill_dp_rank
)
)
session, decode_response = await decode_request_task
stream_generator = stream_decode_response(session, decode_response, request_id)
response = await make_response(stream_generator)
response.headers["Content-Type"] = decode_response.headers.get(
"Content-Type", "application/json"
)
return response
except Exception as e:
logger.exception("An error occurred while handling the request: %s", e)
return await make_response(
(
f"Internal Server Error: {e!s}",
500,
)
)
async def send_profile_cmd(req_data: dict, profiler_cmd: str):
assert profiler_cmd in {"start", "stop"}
with _list_lock:
p_instances = list(prefill_instances)
d_instances = list(decode_instances)
if not p_instances and not d_instances:
raise RuntimeError(
"Service Unavailable: No prefill or decode instances are registered."
)
headers = {
"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
}
tasks = []
async with aiohttp.ClientSession(
timeout=aiohttp.ClientTimeout(total=60)
) as session:
for instances in (p_instances, d_instances):
for inst in instances:
_p = urlparse(inst["request_address"])
url = f"http://{_p.hostname}:{_p.port}/{profiler_cmd}_profile"
tasks.append(
session.post(
url,
json=req_data,
headers=headers,
)
)
responses = await asyncio.gather(*tasks, return_exceptions=True)
for r in responses:
if isinstance(r, Exception):
raise r
if r.status >= 400:
msg = await r.text()
raise RuntimeError(f"{profiler_cmd}_profile failed: {r.status}, {msg}")
return await responses[0].json()
@app.post("/start_profile")
async def start_profile():
try:
req_data = await request.get_json()
return await send_profile_cmd(req_data, "start")
except Exception as e:
logger.exception("start_profile failed: %s", e)
return await make_response((str(e), 500))
@app.post("/stop_profile")
async def stop_profile():
try:
req_data = await request.get_json()
return await send_profile_cmd(req_data, "stop")
except Exception as e:
logger.exception("stop_profile failed: %s", e)
return await make_response((str(e), 500))
if __name__ == "__main__":
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=10001)
args = parser.parse_args()
t = start_service_discovery("0.0.0.0", 36367)
# High-concurrency hardening. Quart's app.run() uses a shallow listen
# backlog (100) and, with app.debug=True, adds per-request overhead that
# starves the single accept loop. Under a burst of ~512 simultaneous client
# connections the backlog overflows and the kernel RSTs the excess, so
# clients see "ClientOSError: [Errno 104] Connection reset by peer" before
# any response (~16% request loss at c=512). Serve via hypercorn with debug
# OFF and a deep backlog so the burst QUEUES (higher TTFT) instead of being
# reset -> 100% request success.
app.debug = False
app.config["BODY_TIMEOUT"] = 360000
app.config["RESPONSE_TIMEOUT"] = 360000
import asyncio
import os
from hypercorn.asyncio import serve as _hypercorn_serve
from hypercorn.config import Config as _HypercornConfig
_hcfg = _HypercornConfig()
_hcfg.bind = [f"0.0.0.0:{args.port}"]
# Deep listen backlog so a wide connection burst queues, not RSTs. NOTE:
# effective backlog is capped by the host's net.core.somaxconn (proxy runs
# --network host); kernel 6.x defaults to 4096. Override via
# PROXY_LISTEN_BACKLOG.
_hcfg.backlog = int(os.environ.get("PROXY_LISTEN_BACKLOG", "4096"))
# Long-lived SSE streams (8k1k decode ~5 min): never reap on keepalive.
_hcfg.keep_alive_timeout = 360000.0
asyncio.run(_hypercorn_serve(app, _hcfg))
t.join()