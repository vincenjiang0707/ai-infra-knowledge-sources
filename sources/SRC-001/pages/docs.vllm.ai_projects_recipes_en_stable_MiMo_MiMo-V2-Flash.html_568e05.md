source: https://docs.vllm.ai/projects/recipes/en/stable/MiMo/MiMo-V2-Flash.html
lastmod: 2026-04-27

# MiMo-V2-Flash Usage Guide[¶](https://docs.vllm.ai#mimo-v2-flash-usage-guide)

## Introduction[¶](https://docs.vllm.ai#introduction)

[MiMo-V2-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash) is a MoE language model with 309B total parameters and 15B active parameters. Designed for high-speed reasoning and agentic workflows, it utilizes a novel hybrid attention architecture and Multi-Token Prediction (MTP) to achieve state-of-the-art performance while significantly reducing inference costs.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

### NVIDIA[¶](https://docs.vllm.ai#nvidia)

### AMD[¶](https://docs.vllm.ai#amd)

Note: The vLLM wheel for ROCm requires Python 3.12, ROCm 7.0, and glibc >= 2.35. If your environment does not meet these requirements, please use the Docker-based setup as described in the

[documentation]. Supported GPUs: MI300X, MI325X, MI355X

uv venv
source .venv/bin/activate
uv pip install vllm --extra-index-url https://wheels.vllm.ai/rocm/


## Running MiMo-V2-Flash[¶](https://docs.vllm.ai#running-mimo-v2-flash)

run `TP`

like this:

### NVIDIA[¶](https://docs.vllm.ai#nvidia_1)

```bash
vllm serve XiaomiMiMo/MiMo-V2-Flash \
--host 0.0.0.0 \
--port 9001 \
--seed 1024 \
--served-model-name mimo_v2_flash \
--tensor-parallel-size 4 \
--trust-remote-code \
--gpu-memory-utilization 0.9 \
--generation-config vllm
```


### AMD[¶](https://docs.vllm.ai#amd_1)

```bash
export VLLM_ROCM_USE_AITER=0
vllm serve XiaomiMiMo/MiMo-V2-Flash \
--served-model-name mimo_v2_flash \
--tensor-parallel-size 4 \
--trust-remote-code \
--gpu-memory-utilization 0.9 \
--generation-config vllm
```


run `Tool Call`

like this:

```bash
vllm serve XiaomiMiMo/MiMo-V2-Flash \
--host 0.0.0.0 \
--port 9001 \
--seed 1024 \
--served-model-name mimo_v2_flash \
--tensor-parallel-size 4 \
--trust-remote-code \
--gpu-memory-utilization 0.9 \
--tool-call-parser qwen3_xml \
--reasoning-parser qwen3 \
--generation-config vllm
```


run `DP/TP/EP`

like this:

```bash
vllm serve XiaomiMiMo/MiMo-V2-Flash \
--host 0.0.0.0 \
--port 9001 \
--seed 1024 \
--served-model-name mimo_v2_flash \
--data-parallel-size 2 \
--tensor-parallel-size 4 \
--enable-expert-parallel \
--trust-remote-code \
--gpu-memory-utilization 0.9 \
--generation-config vllm
```


- You can set
`--max-model-len`

to preserve memory.`--max-model-len=65536`

is usually good for most scenarios and max is 128k. - You can set
`--max-num-batched-tokens`

to balance throughput and latency, higher means higher throughput but higher latency.`--max-num-batched-tokens=32768`

is usually good for prompt-heavy workloads. But you can reduce it to 16k and 8k to reduce activation memory usage and decrease latency. - vLLM conservatively uses 90% of GPU memory, you can set
`--gpu-memory-utilization=0.95`

to maximize KVCache. - Make sure to follow the command-line instructions to ensure the tool-calling functionality is properly enabled.

### curl Example[¶](https://docs.vllm.ai#curl-example)

You can run the following `curl`

command:

```
curl -X POST http://localhost:9001/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "mimo_v2_flash",
"messages": [
{
"role": "user",
"content": "Hello MiMo!"
}
],
"chat_template_kwargs": {
"enable_thinking": true
}
}'
```


- Set
`"enable_thinking": false`

or remove the`chat_template_kwargs`

section to disable thinking mode.

## Benchmarking[¶](https://docs.vllm.ai#benchmarking)

For benchmarking, disable prefix caching by adding `--no-enable-prefix-caching`

to the server command.

### Benchmark[¶](https://docs.vllm.ai#benchmark)

# Prompt-heavy benchmark (8k/1k)
vllm bench serve \
--model XiaomiMiMo/MiMo-V2-Flash \
--dataset-name random \
--random-input-len 8000 \
--random-output-len 1000 \
--request-rate 3 \
--num-prompts 1800 \
--ignore-eos


### Benchmark Configurations[¶](https://docs.vllm.ai#benchmark-configurations)

Test different workloads by adjusting input/output lengths:

**Prompt-heavy**: 8000 input / 1000 output**Decode-heavy**: 1000 input / 8000 output**Balanced**: 1000 input / 1000 output

### Expected Output[¶](https://docs.vllm.ai#expected-output)

It currently just runs, and many features—such as MTP—have not yet been added, so performance testing will be conducted later.

## Accuracy[¶](https://docs.vllm.ai#accuracy)

### GSM8K[¶](https://docs.vllm.ai#gsm8k)

Script

lm_eval \
```bash
--model local-chat-completions \
--tasks gsm8k \
--num_fewshot 5 \
--apply_chat_template \
--model_args model=mimo_v2_flash,base_url=http://0.0.0.0:9001/v1/chat/completions,num_concurrent=100,max_retries=20,tokenized_requests=False,tokenizer_backend=none,max_gen_toks=256
```


|Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.9128|± |0.0078|
| | |strict-match | 5|exact_match|↑ |0.9075|± |0.0080|


## TODO[¶](https://docs.vllm.ai#todo)

- [ ] Supports MTP.
- [ ] Provide stress test performance data.