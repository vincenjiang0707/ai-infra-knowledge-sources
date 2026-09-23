source: https://docs.vllm.ai/en/latest/examples/disaggregated/lmcache/
lastmod: 2026-09-23

# LMCache Examples[¶](https://docs.vllm.ai#lmcache-examples)

Source [https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/lmcache](https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/lmcache).

This folder demonstrates how to use LMCache with vLLM v1 for KV cache offloading, disaggregated prefilling, and KV cache sharing.

## Integration modes[¶](https://docs.vllm.ai#integration-modes)

LMCache integrates with vLLM v1 in two ways:

**In-process mode**(`LMCacheConnectorV1`

): LMCache runs inside the vLLM process and is configured through environment variables or a YAML config file (`LMCACHE_CONFIG_FILE`

). This is the simplest way to add single-node CPU/disk offloading.**Multi-process (MP) mode**(`LMCacheMPConnector`

): LMCache runs as a standalone server (`lmcache server`

) that owns the KV cache storage; one or more vLLM instances connect to it. This is the recommended mode for distributed KV storage and for sharing KV cache across instances. See the[LMCache docs](https://docs.lmcache.ai)for the full MP setup.

## 1. CPU offload (in-process)[¶](https://docs.vllm.ai#1-cpu-offload-in-process)

`python cpu_offload_lmcache.py`

- CPU offloading with`LMCacheConnectorV1`

for vLLM v1.

## 2. CPU offload (multi-process)[¶](https://docs.vllm.ai#2-cpu-offload-multi-process)

`bash cpu_offload_lmcache_mp.sh`

- CPU offloading with`LMCacheMPConnector`

, using a standalone`lmcache server`

. vLLM provides a built-in shortcut for this setup via`--kv-offloading-backend lmcache`

and`--kv-offloading-size <GiB>`

.

## 3. Disaggregated Prefill in vLLM v1[¶](https://docs.vllm.ai#3-disaggregated-prefill-in-vllm-v1)

This example demonstrates how to run LMCache with disaggregated prefill using NIXL on a single node.

### Prerequisites[¶](https://docs.vllm.ai#prerequisites)

- Install
[LMCache](https://github.com/LMCache/LMCache). You can simply run`pip install lmcache`

. - Install
[NIXL](https://github.com/ai-dynamo/nixl). - At least 2 GPUs
- Valid Hugging Face token (HF_TOKEN) for Llama 3.1 8B Instruct.

### Usage[¶](https://docs.vllm.ai#usage)

Run `cd disagg_prefill_lmcache_v1`

to get into `disagg_prefill_lmcache_v1`

folder, and then run

to run disaggregated prefill and benchmark the performance.

### Components[¶](https://docs.vllm.ai#components)

#### Server Scripts[¶](https://docs.vllm.ai#server-scripts)

`disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh`

- Launches individual vLLM servers for prefill/decode, and also launches the proxy server.`disagg_prefill_lmcache_v1/disagg_proxy_server.py`

- FastAPI proxy server that coordinates between prefiller and decoder`disagg_prefill_lmcache_v1/disagg_example_nixl.sh`

- Main script to run the example

#### Configuration[¶](https://docs.vllm.ai#configuration)

`disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml`

- Configuration for prefiller server`disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml`

- Configuration for decoder server

#### Log Files[¶](https://docs.vllm.ai#log-files)

The main script generates several log files:

`prefiller.log`

- Logs from the prefill server`decoder.log`

- Logs from the decode server`proxy.log`

- Logs from the proxy server

## 4. KV Cache Sharing[¶](https://docs.vllm.ai#4-kv-cache-sharing)

The `kv_cache_sharing_lmcache_v1.py`

example demonstrates how to share KV caches between vLLM v1 instances through a centralized LMCache server.

## Example materials[¶](https://docs.vllm.ai#example-materials)

## cpu_offload_lmcache.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This file demonstrates the example usage of CPU offloading
with LMCache in vLLM v1.
Note that `lmcache` is needed to run this example.
Requirements:
https://docs.lmcache.ai/getting_started/installation.html#prerequisites
Learn more about LMCache environment setup, please refer to:
https://docs.lmcache.ai/getting_started/installation.html
"""
import contextlib
import os
import time
from dataclasses import asdict
from lmcache.integration.vllm.utils import ENGINE_NAME
from lmcache.v1.cache_engine import LMCacheEngineBuilder
from vllm import LLM, SamplingParams
from vllm.config import KVTransferConfig
from vllm.engine.arg_utils import EngineArgs
def setup_environment_variables():
# LMCache-related environment variables
# LMCache is set to use 256 tokens per chunk
os.environ["LMCACHE_CHUNK_SIZE"] = "256"
# Enable local CPU backend in LMCache
os.environ["LMCACHE_LOCAL_CPU"] = "True"
# Set local CPU memory limit to 5.0 GB
os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0"
@contextlib.contextmanager
def build_llm_with_lmcache(model: str):
ktc = KVTransferConfig(
kv_connector="LMCacheConnectorV1",
kv_role="kv_both",
)
# Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
# memory. Reduce the value if your GPU has less memory.
# Note: LMCache supports chunked prefill (see vLLM#14505, LMCache#392).
llm_args = EngineArgs(
model=model,
kv_transfer_config=ktc,
max_model_len=8000,
gpu_memory_utilization=0.8,
)
llm = LLM(**asdict(llm_args))
try:
yield llm
finally:
# Clean up lmcache backend
LMCacheEngineBuilder.destroy(ENGINE_NAME)
def print_output(
llm: LLM,
prompt: list[str],
sampling_params: SamplingParams,
req_str: str,
):
# Should be able to see logs like the following:
# `LMCache INFO: Storing KV cache for 6006 out of 6006 tokens for request 0`
# This indicates that the KV cache has been stored in LMCache.
start = time.time()
outputs = llm.generate(prompt, sampling_params)
print("-" * 50)
for output in outputs:
generated_text = output.outputs[0].text
print(f"Generated text: {generated_text!r}")
print(f"Generation took {time.time() - start:.2f} seconds, {req_str} request done.")
print("-" * 50)
def main():
model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
setup_environment_variables()
with build_llm_with_lmcache(model) as llm:
# This example script runs two requests with a shared prefix.
# Define the shared prompt and specific prompts
shared_prompt = "Hello, how are you?" * 1000
first_prompt = [
shared_prompt + "Hello, my name is",
]
second_prompt = [
shared_prompt + "Tell me a very long story",
]
sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)
# Print the first output
print_output(llm, first_prompt, sampling_params, "first")
time.sleep(1)
# print the second output
print_output(llm, second_prompt, sampling_params, "second")
if __name__ == "__main__":
main()


## cpu_offload_lmcache_mp.sh

#!/bin/bash
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
#
# CPU offloading with LMCache in multi-process (MP) mode.
#
# In MP mode, LMCache runs as a standalone server process (`lmcache server`)
# that owns the KV cache storage. One or more vLLM instances connect to it via
# the `LMCacheMPConnector`. This is the recommended way to run LMCache for
# distributed KV storage and for sharing KV cache across vLLM instances.
#
# vLLM ships a built-in shortcut for this setup: pass `--kv-offloading-backend
# lmcache` together with `--kv-offloading-size <GiB>` and vLLM wires up the
# `LMCacheMPConnector` for you (it defaults to the LMCache server at
# tcp://localhost:5555, matching the `lmcache server` default).
#
# Requires `lmcache` to be installed (`pip install lmcache`).
# Learn more: https://docs.lmcache.ai
set -euo pipefail
MODEL=${MODEL:-meta-llama/Meta-Llama-3.1-8B-Instruct}
# 1. Launch the standalone LMCache server (binds tcp://localhost:5555 by
# default). `--l1-size-gb` sets the CPU memory budget for the L1 cache.
echo "Starting LMCache server..."
lmcache server --host localhost --port 5555 --l1-size-gb 5 &
LMCACHE_SERVER_PID=$!
trap 'kill $LMCACHE_SERVER_PID 2>/dev/null || true' EXIT
# 2. Launch vLLM and offload KV cache to the LMCache server.
# The MP connector currently requires the non-hybrid KV cache manager.
echo "Starting vLLM server with LMCache MP offloading..."
vllm serve "$MODEL" \
--port 8000 \
--kv-offloading-size 5 \
--kv-offloading-backend lmcache \
--disable-hybrid-kv-cache-manager
# Equivalent explicit configuration (instead of the two flags above):
# --kv-transfer-config \
# '{"kv_connector":"LMCacheMPConnector","kv_role":"kv_both",
# "kv_connector_extra_config":{"lmcache.mp.host":"tcp://localhost",
# "lmcache.mp.port":5555}}'


## disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml

## disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml

## disagg_prefill_lmcache_v1/disagg_example_nixl.sh

#!/bin/bash
echo "Warning: LMCache disaggregated prefill support for vLLM v1 is experimental and subject to change."
PIDS=()
# Switch to the directory of the current script
cd "$(dirname "${BASH_SOURCE[0]}")"
check_hf_token() {
if [ -z "$HF_TOKEN" ]; then
echo "HF_TOKEN is not set. Please set it to your Hugging Face token."
exit 1
fi
if [[ "$HF_TOKEN" != hf_* ]]; then
echo "HF_TOKEN is not a valid Hugging Face token. Please set it to your Hugging Face token."
exit 1
fi
echo "HF_TOKEN is set and valid."
}
check_num_gpus() {
# can you check if the number of GPUs are >=2 via nvidia-smi/rocm-smi?
if ! which rocm-smi > /dev/null 2>&1; then
num_gpus=$(nvidia-smi --query-gpu=name --format=csv,noheader | wc -l)
else
num_gpus=$(rocm-smi --showid | grep -c Instinct)
fi
if [ "$num_gpus" -lt 2 ]; then
echo "You need at least 2 GPUs to run disaggregated prefill."
exit 1
else
echo "Found $num_gpus GPUs."
fi
}
ensure_python_library_installed() {
echo "Checking if $1 is installed..."
if ! python3 -c "import $1" > /dev/null 2>&1; then
if [ "$1" == "nixl" ]; then
echo "$1 is not installed. Please refer to https://github.com/ai-dynamo/nixl for installation."
else
echo "$1 is not installed. Please install it via pip install $1."
fi
exit 1
else
echo "$1 is installed."
fi
}
cleanup() {
echo "Stopping everything…"
trap - INT TERM # prevent re-entrancy
kill -- -$$ # negative PID == “this whole process-group”
wait # reap children so we don't leave zombies
exit 0
}
wait_for_server() {
local port=$1
local timeout_seconds=1200
local start_time=$(date +%s)
echo "Waiting for server on port $port..."
while true; do
if curl -s "localhost:${port}/v1/completions" > /dev/null; then
return 0
fi
local now=$(date +%s)
if (( now - start_time >= timeout_seconds )); then
echo "Timeout waiting for server"
return 1
fi
sleep 1
done
}
main() {
check_hf_token
check_num_gpus
ensure_python_library_installed lmcache
ensure_python_library_installed nixl
ensure_python_library_installed pandas
ensure_python_library_installed datasets
ensure_python_library_installed vllm
trap cleanup INT
trap cleanup USR1
trap cleanup TERM
echo "Launching prefiller, decoder and proxy..."
echo "Please check prefiller.log, decoder.log and proxy.log for logs."
bash disagg_vllm_launcher.sh prefiller \
> >(tee prefiller.log) 2>&1 &
prefiller_pid=$!
PIDS+=("$prefiller_pid")
bash disagg_vllm_launcher.sh decoder \
> >(tee decoder.log) 2>&1 &
decoder_pid=$!
PIDS+=("$decoder_pid")
python3 disagg_proxy_server.py \
--host localhost \
--port 9000 \
--prefiller-host localhost \
--prefiller-port 8100 \
--decoder-host localhost \
--decoder-port 8200 \
> >(tee proxy.log) 2>&1 &
proxy_pid=$!
PIDS+=("$proxy_pid")
wait_for_server 8100
wait_for_server 8200
wait_for_server 9000
echo "All servers are up. Starting benchmark..."
# begin benchmark
cd ../../../../benchmarks/
vllm bench serve --port 9000 --seed "$(date +%s)" \
--model meta-llama/Llama-3.1-8B-Instruct \
--dataset-name random --random-input-len 7500 --random-output-len 200 \
--num-prompts 200 --burstiness 100 --request-rate 3.6 | tee benchmark.log
echo "Benchmarking done. Cleaning up..."
cleanup
}
main


## disagg_prefill_lmcache_v1/disagg_proxy_server.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
import argparse
import os
import time
from contextlib import asynccontextmanager
import httpx
import numpy as np
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
@asynccontextmanager
async def lifespan(app: FastAPI):
"""Lifespan context manager to handle startup and shutdown events."""
# Startup: Initialize clients
prefiller_base_url = (
f"http://{global_args.prefiller_host}:{global_args.prefiller_port}/v1"
)
decoder_base_url = (
f"http://{global_args.decoder_host}:{global_args.decoder_port}/v1"
)
app.state.prefill_client = httpx.AsyncClient(
timeout=None,
base_url=prefiller_base_url,
limits=httpx.Limits(
max_connections=None,
max_keepalive_connections=None,
),
)
app.state.decode_client = httpx.AsyncClient(
timeout=None,
base_url=decoder_base_url,
limits=httpx.Limits(
max_connections=None,
max_keepalive_connections=None,
),
)
yield
# Shutdown: Close clients
await app.state.prefill_client.aclose()
await app.state.decode_client.aclose()
# Update FastAPI app initialization to use lifespan
app = FastAPI(lifespan=lifespan)
class StatsCalculator:
def __init__(self):
self._stats = []
self._last_log_time = time.time()
def add(self, value):
self._stats.append(value)
if time.time() - self._last_log_time > 5:
self._log_stats()
self._last_log_time = time.time()
def _log_stats(self):
# Print average, median, and 99th percentile
np_arr = np.array(self._stats)
output_str = (
f"\nNum requests: {len(self._stats)}"
"\nPrefill node TTFT stats:"
f"\n - Average (ms): {np.mean(np_arr)}"
f"\n - Median (ms): {np.median(np_arr)}"
f"\n - 99th Percentile (ms): {np.percentile(np_arr, 99)}\n"
)
print(
"===============================",
output_str,
"===============================",
)
stats_calculator = StatsCalculator()
counter = 0
def parse_args():
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=8000)
parser.add_argument("--host", type=str, default="localhost")
parser.add_argument("--prefiller-host", type=str, default="localhost")
parser.add_argument("--prefiller-port", type=int, default=8100)
parser.add_argument("--decoder-host", type=str, default="localhost")
parser.add_argument("--decoder-port", type=int, default=8200)
args = parser.parse_args()
return args
# Initialize variables to hold the persistent clients
app.state.prefill_client = None
app.state.decode_client = None
async def send_request_to_service(
client: httpx.AsyncClient, endpoint: str, req_data: dict
):
"""Send a request to a service using a persistent client."""
req_data = req_data.copy()
req_data["max_tokens"] = 1
if "max_completion_tokens" in req_data:
req_data["max_completion_tokens"] = 1
headers = {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"}
response = await client.post(endpoint, json=req_data, headers=headers)
response.raise_for_status()
# read/consume the response body to release the connection
# otherwise, it would http.ReadError
await response.aread()
return response
async def stream_service_response(
client: httpx.AsyncClient, endpoint: str, req_data: dict
):
"""Asynchronously stream the response from a service using a persistent client."""
headers = {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"}
async with client.stream(
"POST", endpoint, json=req_data, headers=headers
) as response:
response.raise_for_status()
async for chunk in response.aiter_bytes():
yield chunk
@app.post("/v1/completions")
async def handle_completions(request: Request):
global counter, stats_calculator
counter += 1
st = time.time()
try:
req_data = await request.json()
# Send request to prefill service, ignore the response
await send_request_to_service(
app.state.prefill_client, "/completions", req_data
)
et = time.time()
stats_calculator.add(et - st)
# Stream response from decode service
async def generate_stream():
async for chunk in stream_service_response(
app.state.decode_client, "/completions", req_data
):
yield chunk
return StreamingResponse(generate_stream(), media_type="text/event-stream")
except Exception as e:
import sys
import traceback
exc_info = sys.exc_info()
print("Error occurred in disagg prefill proxy server - completions endpoint")
print(e)
print("".join(traceback.format_exception(*exc_info)))
raise
@app.post("/v1/chat/completions")
async def handle_chat_completions(request: Request):
global counter, stats_calculator
counter += 1
st = time.time()
try:
req_data = await request.json()
# Send request to prefill service, ignore the response
await send_request_to_service(
app.state.prefill_client, "/chat/completions", req_data
)
et = time.time()
stats_calculator.add(et - st)
# Stream response from decode service
async def generate_stream():
async for chunk in stream_service_response(
app.state.decode_client, "/chat/completions", req_data
):
yield chunk
return StreamingResponse(generate_stream(), media_type="text/event-stream")
except Exception as e:
import sys
import traceback
exc_info = sys.exc_info()
print(
"Error occurred in disagg prefill proxy server - chat completions endpoint"
)
print(e)
print("".join(traceback.format_exception(*exc_info)))
raise
if __name__ == "__main__":
global global_args
global_args = parse_args()
import uvicorn
uvicorn.run(app, host=global_args.host, port=global_args.port)


## disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh

#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ $# -lt 1 ]]; then
echo "Usage: $0 <prefiller | decoder> [model]"
exit 1
fi
if [[ $# -eq 1 ]]; then
echo "Using default model: meta-llama/Llama-3.1-8B-Instruct"
MODEL="meta-llama/Llama-3.1-8B-Instruct"
else
echo "Using model: $2"
MODEL=$2
fi
# The prefillers and decoders in LMCache use the same hash seed for all chunk keys.
# This seed must be aligned so that decoders can identify and retrieve KV cache
# entries stored by prefillers.
#
# WARNING: Using a fixed hash seed is insecure and makes the application vulnerable to
# denial-of-service attacks. In a production environment, this should be set to a
# secure random value. This is set to a fixed value for demonstration purposes only.
export PYTHONHASHSEED=${VLLM_PYTHON_HASH_SEED:-123}
if [[ $1 == "prefiller" ]]; then
# Prefiller listens on port 8100
prefill_config_file=$SCRIPT_DIR/configs/lmcache-prefiller-config.yaml
UCX_TLS=cuda_ipc,cuda_copy,tcp \
LMCACHE_CONFIG_FILE=$prefill_config_file \
VLLM_ENABLE_V1_MULTIPROCESSING=1 \
VLLM_WORKER_MULTIPROC_METHOD=spawn \
CUDA_VISIBLE_DEVICES=0 \
vllm serve "$MODEL" \
--port 8100 \
--enforce-eager \
--kv-transfer-config \
'{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_producer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "producer1"}}'
elif [[ $1 == "decoder" ]]; then
# Decoder listens on port 8200
decode_config_file=$SCRIPT_DIR/configs/lmcache-decoder-config.yaml
UCX_TLS=cuda_ipc,cuda_copy,tcp \
LMCACHE_CONFIG_FILE=$decode_config_file \
VLLM_ENABLE_V1_MULTIPROCESSING=1 \
VLLM_WORKER_MULTIPROC_METHOD=spawn \
CUDA_VISIBLE_DEVICES=1 \
vllm serve "$MODEL" \
--port 8200 \
--enforce-eager \
--kv-transfer-config \
'{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_consumer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "consumer1"}}'
else
echo "Invalid role: $1"
echo "Should be either prefiller, decoder"
exit 1
fi


## kv_cache_sharing_lmcache_v1.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This file demonstrates the example usage of remote KV cache sharing
with LMCache.
We will launch 2 vllm instances, and launch an additional LMCache server.
KV cache is transferred in the following manner:
(1) vLLM instance 1 -> LMCache server (KV cache store).
(2) LMCache server -> vLLM instance 2 (KV cache reuse/retrieve).
Note that lmcache needs to be installed to run this example.
Learn more about LMCache in https://github.com/LMCache/LMCache.
"""
import os
import subprocess
import time
from multiprocessing import Event, Process
from lmcache.integration.vllm.utils import ENGINE_NAME
from lmcache.v1.cache_engine import LMCacheEngineBuilder
from vllm import LLM, SamplingParams
from vllm.config import KVTransferConfig
# LMCache-related environment variables
# The port to start LMCache server
port = 8100
# LMCache is set to use 256 tokens per chunk
os.environ["LMCACHE_CHUNK_SIZE"] = "256"
# Disable local CPU backend in LMCache
os.environ["LMCACHE_LOCAL_CPU"] = "False"
# Set local CPU memory buffer limit to 5.0 GB
os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0"
# Set the remote URL for LMCache server
os.environ["LMCACHE_REMOTE_URL"] = f"lm://localhost:{port}"
# Set the serializer/deserializer between vllm and LMCache server
# `naive` indicates using raw bytes of the tensor without any compression
os.environ["LMCACHE_REMOTE_SERDE"] = "naive"
prompts = [
"Hello, how are you?" * 1000,
]
def run_store(store_done, prompts):
# We use GPU 0 for KV cache store process.
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)
ktc = KVTransferConfig(kv_connector="LMCacheConnectorV1", kv_role="kv_both")
# Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
# memory. Reduce the value if your GPU has less memory.
llm = LLM(
model="mistralai/Mistral-7B-Instruct-v0.2",
kv_transfer_config=ktc,
max_model_len=8000,
gpu_memory_utilization=0.8,
enforce_eager=True,
)
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
generated_text = output.outputs[0].text
print(f"Generated text: {generated_text!r}")
print("KV cache store is finished.")
store_done.set()
# Clean up lmcache backend
LMCacheEngineBuilder.destroy(ENGINE_NAME)
def run_retrieve(store_done, prompts, timeout=1):
# We use GPU 1 for KV cache retrieve process.
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)
ktc = KVTransferConfig(kv_connector="LMCacheConnectorV1", kv_role="kv_both")
# Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
# of memory. Reduce the value if your GPU has less memory.
llm = LLM(
model="mistralai/Mistral-7B-Instruct-v0.2",
kv_transfer_config=ktc,
max_model_len=8000,
gpu_memory_utilization=0.8,
enforce_eager=True,
)
print("Waiting for KV cache store to finish...")
store_done.wait()
time.sleep(timeout)
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
generated_text = output.outputs[0].text
print(f"Generated text: {generated_text!r}")
# Clean up lmcache backend
LMCacheEngineBuilder.destroy(ENGINE_NAME)
def run_lmcache_server(port):
server_proc = subprocess.Popen(
["python", "-m", "lmcache.v1.server", "localhost", str(port)]
)
return server_proc
def main():
store_done = Event()
store_process = Process(target=run_store, args=(store_done, prompts))
retrieve_process = Process(target=run_retrieve, args=(store_done, prompts))
lmcache_server_process = run_lmcache_server(port)
# Start KV cache store process
store_process.start()
# Start KV cache retrieve process
retrieve_process.start()
# Clean up the processes
store_process.join()
retrieve_process.terminate()
lmcache_server_process.terminate()
lmcache_server_process.wait()
if __name__ == "__main__":
main()