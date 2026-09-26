source: https://docs.vllm.ai/projects/recipes/en/stable/Qwen/Qwen3-VL.html
lastmod: 2026-04-27

# Qwen3-VL Usage Guide[¶](https://docs.vllm.ai#qwen3-vl-usage-guide)

[Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) is the most powerful vision-language model in the Qwen series to date created by Alibaba Cloud.

This generation delivers comprehensive upgrades across the board: superior text understanding & generation, deeper visual perception & reasoning, extended context length, enhanced spatial and video dynamics comprehension, and stronger agent interaction capabilities.

Available in Dense and MoE architectures that scale from edge to cloud, with Instruct and reasoning‑enhanced Thinking editions for flexible, on‑demand deployment.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

uv venv
source .venv/bin/activate
# Install vLLM >=0.11.0
uv pip install -U vllm
# Install Qwen-VL utility library (recommended for offline inference)
uv pip install qwen-vl-utils==0.0.14


## Running Qwen3-VL[¶](https://docs.vllm.ai#running-qwen3-vl)

### Qwen3-VL-235B-A22B-Instruct[¶](https://docs.vllm.ai#qwen3-vl-235b-a22b-instruct)

This is the Qwen3-VL flagship MoE model, which requires a minimum of 8 GPUs, each with at least 80 GB of memory (e.g., A100, H100, or H200). On some types of hardware the model may not launch successfully with its default setting. Recommended approaches by hardware type are:

**H100 with**: Use FP8 checkpoint for optimal memory efficiency.`fp8`

**A100 & H100 with**: Either reduce`bfloat16`

`--max-model-len`

or restrict inference to images only.**H200 & B200**: Run the model out of the box, supporting full context length and concurrent image and video processing.

See sections below for detailed launch arguments for each configuration. We are actively working on optimizations and the recommended ways to launch the model will be updated accordingly.

## H100 (Image + Video Inference, FP8)

## H100 (Image Inference, FP8, TP4)

## A100 & H100 (Image Inference, BF16)

## A100 & H100 (Image + Video Inference, BF16)

## H200 & B200

ℹ️

Note

Qwen3-VL-235B-A22B-Instruct also excels on text-only tasks, ranking as the[#1 open model on text by lmarena.ai]at the time this guide was created.

You can enable text-only mode by passing`--limit-mm-per-prompt.video 0 --limit-mm-per-prompt.image 0`

, which skips the vision encoder and multimodal profiling to free up memory for additional KV cache.

### Configuration Tips[¶](https://docs.vllm.ai#configuration-tips)

- It's highly recommended to specify
`--limit-mm-per-prompt.video 0`

if your inference server will only process image inputs since enabling video inputs consumes more memory reserved for long video embeddings. Alternatively, you can skip memory profiling for multimodal inputs by`--skip-mm-profiling`

and lower`--gpu-memory-utilization`

accordingly at your own risk. - To avoid undesirable CPU contention, it's recommended to limit the number of threads allocated to preprocessing by setting the environment variable
`OMP_NUM_THREADS=1`

. This is particulaly useful and shows significant throughput improvement when deploying multiple vLLM instances on the same host. - You can set
`--max-model-len`

to preserve memory. By default the model's context length is 262K, but`--max-model-len 128000`

is good for most scenarios. - Specifying
`--async-scheduling`

improves the overall system performance by overlapping scheduling overhead with the decoding process.**Note: With vLLM >= 0.11.1, compatibility has been improved for structured output and sampling with penalties, but it may still be incompatible with speculative decoding (features merged but not yet released).**Check the latest releases for continued improvements. - Specifying
`--mm-encoder-tp-mode data`

deploys the vision encoder in a data-parallel fashion for better performance. This is because the vision encoder is very small, thus tensor parallelism brings little gain but incurs significant communication overhead. Enabling this feature does consume additional memory and may require adjustment on`--gpu-memory-utilization`

. - If your workload involves mostly
**unique**multimodal inputs only, it is recommended to pass`--mm-processor-cache-gb 0`

to avoid caching overhead. Otherwise, specifying`--mm-processor-cache-type shm`

enables this experimental feature which utilizes host shared memory to cache preprocessed input images and/or videos which shows better performance at a high TP setting. - vLLM supports Expert Parallelism (EP) via
`--enable-expert-parallel`

, which allows experts in MoE models to be deployed on separate GPUs for better throughput. Check out[Expert Parallelism Deployment](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html)for more details. - You can use
[benchmark_moe](https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_moe.py)to perform MoE Triton kernel tuning for your hardware. - You can further extend the model's context window with
`YaRN`

by passing`--rope-scaling '{"rope_type":"yarn","factor":3.0,"original_max_position_embeddings": 262144,"mrope_section":[24,20,20],"mrope_interleaved": true}' --max-model-len 1000000`


### Benchmark on VisionArena-Chat Dataset[¶](https://docs.vllm.ai#benchmark-on-visionarena-chat-dataset)

Once the server for the `Qwen3-VL-235B-A22B-Instruct`

model is running, open another terminal and run the benchmark client:

vllm bench serve \
```bash
--backend openai-chat \
--endpoint /v1/chat/completions \
--model Qwen/Qwen3-VL-235B-A22B-Instruct \
--dataset-name hf \
--dataset-path lmarena-ai/VisionArena-Chat \
--num-prompts 1000 \
--request-rate 20
```


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
model="Qwen/Qwen3-VL-235B-A22B-Instruct",
messages=messages,
max_tokens=2048
)
print(f"Response costs: {time.time() - start:.2f}s")
print(f"Generated text: {response.choices[0].message.content}")


For more usage examples, check out the [vLLM user guide for multimodal models](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html) and the [official Qwen3-VL GitHub Repository](https://github.com/QwenLM/Qwen3-VL)!

## AMD GPU Support[¶](https://docs.vllm.ai#amd-gpu-support)

Recommended approaches by hardware type are:

MI300X/MI325X/MI355X

Please follow the steps here to install and run Qwen3-VL models on AMD MI300X/MI325X/MI355X GPU.

### Step 1: Installing vLLM (AMD ROCm Backend: MI300X, MI325X, MI355X)[¶](https://docs.vllm.ai#step-1-installing-vllm-amd-rocm-backend-mi300x-mi325x-mi355x)

Note: The vLLM wheel for ROCm requires Python 3.12, ROCm 7.0, and glibc >= 2.35. If your environment does not meet these requirements, please use the Docker-based setup as described in the

[documentation].


### Step 2: Start the vLLM server[¶](https://docs.vllm.ai#step-2-start-the-vllm-server)

Run the vllm online serving

#### Inside the working dir, create a new directory named `miopen`

.[¶](https://docs.vllm.ai#inside-the-working-dir-create-a-new-directory-named-miopen)

### BF16[¶](https://docs.vllm.ai#bf16)

```bash
MIOPEN_USER_DB_PATH="$(pwd)/miopen" \
MIOPEN_FIND_MODE=FAST \
VLLM_ROCM_USE_AITER=1 \
SAFETENSORS_FAST_GPU=1 \
vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct \
--tensor-parallel 4 \
--mm-encoder-tp-mode data
```


### FP8[¶](https://docs.vllm.ai#fp8)

```bash
MIOPEN_USER_DB_PATH="$(pwd)/miopen" \
MIOPEN_FIND_MODE=FAST \
VLLM_USE_V1=1 \
VLLM_ROCM_USE_AITER=1 \
SAFETENSORS_FAST_GPU=1 \
vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 \
--tensor-parallel 4 \
--mm-encoder-tp-mode "data"
```