source: https://docs.vllm.ai/projects/recipes/en/stable/moonshotai/Kimi-K2.5.html
lastmod: 2026-04-27

# moonshotai/Kimi-K2.5 Usage Guide[¶](https://docs.vllm.ai#moonshotaikimi-k25-usage-guide)

[Kimi K2.5](https://huggingface.co/moonshotai/Kimi-K2.5) is an open-source, native multimodal agentic model built through continual pretraining on approximately 15 trillion mixed visual and text tokens atop Kimi-K2-Base. It seamlessly integrates vision and language understanding with advanced agentic capabilities, instant and thinking modes, as well as conversational and agentic paradigms.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

You can either install vLLM from pip or use the pre-built Docker image.

### Pip Install[¶](https://docs.vllm.ai#pip-install)

#### NVIDIA[¶](https://docs.vllm.ai#nvidia)

#### AMD[¶](https://docs.vllm.ai#amd)

Note: The vLLM wheel for ROCm requires Python 3.12, ROCm 7.2.1, and glibc >= 2.35. If your environment does not meet these requirements, please use the Docker-based setup as described above. Supported GPUs: MI300X, MI325X, MI355X.


uv venv --python 3.12
source .venv/bin/activate
uv pip install vllm --extra-index-url https://wheels.vllm.ai/rocm


### Use vLLM with Docker[¶](https://docs.vllm.ai#use-vllm-with-docker)

#### NVIDIA[¶](https://docs.vllm.ai#nvidia_1)

Pull the vLLM release image from [Docker Hub](https://hub.docker.com/r/vllm/vllm-openai/tags?name=17.0):

docker pull vllm/vllm-openai:v0.17.0-cu130 # CUDA 13.0
docker pull vllm/vllm-openai:v0.17.0 # Other CUDA versions


##### Hopper (x86_64)[¶](https://docs.vllm.ai#hopper-x86_64)

Verified on 8×H200 GPUs:

docker run --gpus all \
-p 8000:8000 \
--ipc=host \
vllm/vllm-openai:v0.17.0-cu130 moonshotai/Kimi-K2.5 \
--tensor-parallel-size 8 \
--mm-encoder-tp-mode data \
--tool-call-parser kimi_k2 \
--reasoning-parser kimi_k2 \
--enable-auto-tool-choice \
--trust-remote-code


##### Blackwell (aarch64)[¶](https://docs.vllm.ai#blackwell-aarch64)

NVIDIA Blackwell (e.g., GB200) is also supported via the aarch64 image:

docker run --gpus all \
-p 8000:8000 \
--ipc=host \
vllm/vllm-openai:v0.17.0-aarch64-cu130 moonshotai/Kimi-K2.5 \
--tensor-parallel-size 4 \
--mm-encoder-tp-mode data \
--tool-call-parser kimi_k2 \
--reasoning-parser kimi_k2 \
--enable-auto-tool-choice \
--trust-remote-code


##### Blackwell — NVIDIA NVFP4 weights (`nvidia/Kimi-K2.5-NVFP4`

)[¶](https://docs.vllm.ai#blackwell-nvidia-nvfp4-weights-nvidiakimi-k25-nvfp4)

[NVIDIA’s NVFP4 checkpoint](https://huggingface.co/nvidia/Kimi-K2.5-NVFP4) targets **Blackwell** (for example GB200). Accept any license terms on the model card before downloading. On Blackwell MoE models, enable FlashInfer FP4 MoE kernels (same pattern as other NVIDIA FP4 MoE recipes in this repo):

docker run --gpus all \
-p 8000:8000 \
--ipc=host \
-e VLLM_USE_FLASHINFER_MOE_FP4=1 \
vllm/vllm-openai:v0.17.0-aarch64-cu130 nvidia/Kimi-K2.5-NVFP4 \
--tensor-parallel-size 4 \
--mm-encoder-tp-mode data \
--compilation_config.pass_config.fuse_allreduce_rms true \
--tool-call-parser kimi_k2 \
--reasoning-parser kimi_k2 \
--enable-auto-tool-choice \
--trust-remote-code


For higher throughput on MoE stacks you can add expert parallelism; see [Expert Parallelism Deployment](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html). If you hit OOM, lower `--gpu-memory-utilization`

or adjust TP/EP to match your GPU count.

#### AMD (ROCm)[¶](https://docs.vllm.ai#amd-rocm)

Verified on 8× MI300X/MI355X GPUs:

docker run --device=/dev/kfd --device=/dev/dri \
--security-opt seccomp=unconfined \
--group-add video \
--ipc=host \
-p 8000:8000 \
-e VLLM_ROCM_USE_AITER=1 \
-e VLLM_ROCM_QUICK_REDUCE_QUANTIZATION=INT4 \
-e VLLM_ROCM_USE_AITER_RMSNORM=0 \
-v ~/.cache/huggingface:/root/.cache/huggingface \
vllm/vllm-openai-rocm:latest \
moonshotai/Kimi-K2.5 \
--tensor-parallel-size 8 \
--mm-encoder-tp-mode data \
--block-size=1 \
--tool-call-parser kimi_k2 \
--reasoning-parser kimi_k2 \
--enable-auto-tool-choice \
--enable-prefix-caching \
--trust-remote-code


## Running Kimi-K2.5 with vLLM[¶](https://docs.vllm.ai#running-kimi-k25-with-vllm)

See the following command to deploy Kimi-K2.5 with the vLLM inference server.

### NVIDIA[¶](https://docs.vllm.ai#nvidia_2)

The configuration below has been verified on 8xH200 GPUs.

vllm serve moonshotai/Kimi-K2.5 -tp 8 \
--mm-encoder-tp-mode data \
--tool-call-parser kimi_k2 \
--reasoning-parser kimi_k2 \
--enable-auto-tool-choice \
--trust-remote-code


`--reasoning-parser`

flag specifies the reasoning parser to use for extracting reasoning content from the model output.
### NVIDIA NVFP4 (`nvidia/Kimi-K2.5-NVFP4`

, Blackwell)[¶](https://docs.vllm.ai#nvidia-nvfp4-nvidiakimi-k25-nvfp4-blackwell)

Use the NVFP4 weights on Blackwell-class GPUs with FlashInfer MoE FP4 enabled:

export VLLM_USE_FLASHINFER_MOE_FP4=1
vllm serve nvidia/Kimi-K2.5-NVFP4 -tp 4 \
--mm-encoder-tp-mode data \
--compilation_config.pass_config.fuse_allreduce_rms true \
--tool-call-parser kimi_k2 \
--reasoning-parser kimi_k2 \
--enable-auto-tool-choice \
--trust-remote-code


### Disaggregated prefill/decode (`vllm serve`

, GB200 / NVFP4)[¶](https://docs.vllm.ai#disaggregated-prefilldecode-vllm-serve-gb200-nvfp4)

**Disaggregated** prefill/decode runs **separate** vLLM engines for prefill and decode, with KV cache moved between them using a **KV connector** (for example **NixlConnector**). Each engine is started with ** vllm serve** and a

**JSON payload. See the vLLM**

`--kv-transfer-config`

**for installation (NIXL / UCX), side-channel ports, multi-host layout, and proxy routing between prefiller and decoder HTTP ports.**

[NixlConnector usage guide](https://docs.vllm.ai/en/latest/features/nixl_connector_usage.html)The snippets below are **illustrative**: add Kimi-specific flags from the NVFP4 sections above (tooling parsers, compilation, attention/MoE tuning) and align batch limits with your workload. A common pattern on GB200 is ** --enforce-eager** on

**prefill**and

**on**

`--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}'`

**decode**(decode-only CUDA graphs).

#### Environment on a prefill worker[¶](https://docs.vllm.ai#environment-on-a-prefill-worker)

GB200 MoE FP4 (same idea as aggregated NVFP4 above):

export VLLM_USE_FLASHINFER_MOE_FP4=1
export VLLM_USE_NCCL_SYMM_MEM=1
export NCCL_CUMEM_ENABLE=1
export NCCL_MNNVL_ENABLE=1
export NCCL_NVLS_ENABLE=1


NIXL / UCX (see the NixlConnector doc for transport tuning):

**Per process** on a host (each vLLM worker needs a **unique** side-channel port on that host). When you run **one vllm serve per GPU** (data parallel), set

**per rank; if your launcher already pins GPUs (for example one process per node), you can omit it.**

`CUDA_VISIBLE_DEVICES`

export CUDA_VISIBLE_DEVICES=0
export VLLM_NIXL_SIDE_CHANNEL_PORT=<unique_port>
export VLLM_NIXL_SIDE_CHANNEL_HOST=<routable_ip_of_this_host> # when prefill/decode cross nodes; see NixlConnector doc


#### Prefill worker (`vllm serve`

, one rank)[¶](https://docs.vllm.ai#prefill-worker-vllm-serve-one-rank)

Use ** kv_producer** on prefiller instances. Replace

**with the address of**

`<prefill_dp_leader_ip>`

**data-parallel rank 0**inside the

**prefill**pool. Use

**for that pool’s DP coordinator (must be free on the leader host).**

`<prefill_dp_rpc_port>`

Give **each** `vllm serve`

on the **same machine** its own **HTTP --port**: co-located DP ranks cannot all bind

`<prefill_http_port>`

—use a distinct port per rank (for example base + `data_parallel_rank`

). The same rule applies to the decode pool (`<decode_http_port>`

per rank). Prefill and decode pools use **different**HTTP port ranges so the router can target them separately.

vllm serve nvidia/Kimi-K2.5-NVFP4 \
--host 0.0.0.0 \
--port <prefill_http_port_rank0> \
--served-model-name nvidia/Kimi-K2.5-NVFP4 \
--tensor-parallel-size 1 \
--data-parallel-size 4 \
--data-parallel-rank 0 \
--data-parallel-address <prefill_dp_leader_ip> \
--data-parallel-rpc-port <prefill_dp_rpc_port> \
--enable-expert-parallel \
--enforce-eager \
--kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_producer","kv_load_failure_policy":"fail"}' \
--trust-remote-code


#### Environment on a decode worker[¶](https://docs.vllm.ai#environment-on-a-decode-worker)

Match the **MoE FP4 / NCCL** and **UCX** exports you use on prefill unless you split them intentionally. Set ** VLLM_NIXL_SIDE_CHANNEL_PORT** and

**per worker the same way as prefill.**

`VLLM_NIXL_SIDE_CHANNEL_HOST`

#### Decode worker (`vllm serve`

, one rank)[¶](https://docs.vllm.ai#decode-worker-vllm-serve-one-rank)

vllm serve nvidia/Kimi-K2.5-NVFP4 \
--host 0.0.0.0 \
--port <decode_http_port_rank0> \
--served-model-name nvidia/Kimi-K2.5-NVFP4 \
--tensor-parallel-size 1 \
--data-parallel-size 16 \
--data-parallel-rank 0 \
--data-parallel-address <decode_dp_leader_ip> \
--data-parallel-rpc-port <decode_dp_rpc_port> \
--enable-expert-parallel \
--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
--kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_consumer","kv_load_failure_policy":"fail"}' \
--trust-remote-code


#### Expanding to multiple GPUs and nodes[¶](https://docs.vllm.ai#expanding-to-multiple-gpus-and-nodes)

**1. Data parallel + expert parallel** — With ** --data-parallel-size > 1**, run

**one**(typical for wide EP on GB200). Within

`vllm serve`

per GPU**one**pool (prefill or decode), all ranks share the same

**,**

`--data-parallel-size`

**(that pool’s rank-0 host), and**

`--data-parallel-address`

**. Each process still needs its own**

`--data-parallel-rpc-port`

**,**

`--data-parallel-rank`

**,**

`CUDA_VISIBLE_DEVICES`

**unique HTTP**on a given host (otherwise the second rank cannot bind the API server), and

`--port`

**unique**(see the NixlConnector doc for the base_port + dp_rank pattern).

`VLLM_NIXL_SIDE_CHANNEL_PORT`

on that host**Prefill and decode are two separate DP groups**: use

**different**

**values (for example**

`--data-parallel-rpc-port`

**vs**

`<prefill_dp_rpc_port>`

**) so their coordinators do not collide when rank-0 processes share a node;**

`<decode_dp_rpc_port>`

**can match or differ per pool, but the RPC ports must not clash on the same listener.**

`--data-parallel-address`

**2. Tensor parallel across nodes** — Without data parallel, use ** --master-addr**,

**,**

`--nnodes`

**, and**

`--node-rank`

**on followers, plus your KV transfer settings.**

`--headless`

**3. Request path** — You need a **frontend** in front of the prefiller and decoder ** vllm serve** endpoints so traffic is split correctly. The

**repo documents installation and usage, including**

[vLLM Router](https://github.com/vllm-project/router)**prefill/decode disaggregation**(for example

`--vllm-pd-disaggregation`

with `--prefill`

/ `--decode`

worker URLs). The vLLM docs also walk through **end to end. Another common choice is**

[disaggregated prefill serving](https://docs.vllm.ai/en/latest/examples/online_serving/disaggregated_prefill.html)**as a coordinating frontend.**

[Dynamo](https://github.com/ai-dynamo/dynamo)### AMD (ROCm)[¶](https://docs.vllm.ai#amd-rocm_1)

The configuration below has been verified on 8x MI300X/MI355X GPUs.

export VLLM_ROCM_USE_AITER=1 # Enable AITER optimization for attention and tensor operations
export VLLM_ROCM_QUICK_REDUCE_QUANTIZATION=INT4 # Use INT4 quantization for faster all-reduce operations
export VLLM_ROCM_USE_AITER_RMSNORM=0 # Disable AITER for RMSNorm layers
vllm serve moonshotai/Kimi-K2.5 -tp 8 \
--mm-encoder-tp-mode data \
--tool-call-parser kimi_k2 \
--reasoning-parser kimi_k2 \
--enable-auto-tool-choice \
--block-size=1 \
--mm-encoder-tp-mode data \
--trust-remote-code


### Configuration Tips[¶](https://docs.vllm.ai#configuration-tips)

`--async-scheduling`

has been turned on by default to improve the overall system performance by overlapping scheduling overhead with the decoding process. If you run into issue with this feature, please try turning off this feature and file a bug report to vLLM.- Specifying
`--mm-encoder-tp-mode data`

deploys the vision encoder in a data-parallel fashion for better performance. This is because the vision encoder is very small, thus tensor parallelism brings little gain but incurs significant communication overhead. Enabling this feature does consume additional memory and may require adjustment on`--gpu-memory-utilization`

. - If your workload involves mostly
**unique**multimodal inputs only, it is recommended to pass`--mm-processor-cache-gb 0`

to avoid caching overhead. Otherwise, specifying`--mm-processor-cache-type shm`

enables this experimental feature which utilizes host shared memory to cache preprocessed input images and/or videos which shows better performance at a high TP setting. - vLLM supports Expert Parallelism (EP) via
`--enable-expert-parallel`

, which allows experts in MoE models to be deployed on separate GPUs for better throughput. Check out[Expert Parallelism Deployment](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html)for more details. - You can use
[benchmark_moe](https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_moe.py)to perform MoE Triton kernel tuning for your hardware.

### Accelerating Kimi 2.5 with Eagle3 MTP[¶](https://docs.vllm.ai#accelerating-kimi-25-with-eagle3-mtp)

We recommend using [lightseekorg/kimi-k2.5-eagle3](https://huggingface.co/lightseekorg/kimi-k2.5-eagle3) and [nvidia/Kimi-K2.5-Thinking-Eagle3](https://huggingface.co/nvidia/Kimi-K2.5-Thinking-Eagle3) to accelerate inference of Kimi 2.5. This feature is supported in vLLM nightly and `vLLM>=0.18.0`

.

vllm serve moonshotai/Kimi-K2.5 \
--tensor-parallel-size 8 \
--speculative-config '{"model": <eagle3_model_name>, "method": "eagle3", "num_speculative_tokens": 3}' \
--trust-remote-code


### Benchmark on VisionArena-Chat Dataset[¶](https://docs.vllm.ai#benchmark-on-visionarena-chat-dataset)

Once the server for the `moonshotai/Kimi-K2.5`

model is running, open another terminal and run the benchmark client:

vllm bench serve \
--backend openai-chat \
--endpoint /v1/chat/completions \
--model moonshotai/Kimi-K2.5 \
--dataset-name hf \
--dataset-path lmarena-ai/VisionArena-Chat \
--num-prompts 1000 \
--request-rate 20 \
--trust-remote-code


### Consume the OpenAI API Compatible Server[¶](https://docs.vllm.ai#consume-the-openai-api-compatible-server)

import time
from openai import OpenAI
client = OpenAI(
api_key="EMPTY",
base_url="http://localhost:8000/v1",
timeout=3600
)
messages = [
{
"role": "user",
"content": [
{
"type": "image_url",
"image_url": {
"url": "https://ofasys-multimodal-wlcb-3-toshanghai.oss-accelerate.aliyuncs.com/wpf272043/keepme/image/receipt.png"
}
},
{
"type": "text",
"text": "Read all the text in the image."
}
]
}
]
start = time.time()
response = client.chat.completions.create(
model="moonshotai/Kimi-K2.5",
messages=messages,
max_tokens=2048
)
print(f"Response costs: {time.time() - start:.2f}s")
print(f"Generated text: {response.choices[0].message.content}")


For more usage examples, check out the [vLLM user guide for multimodal models](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html) and the [official Kimi-K2.5 Hugging Face page](https://huggingface.co/moonshotai/Kimi-K2.5)!