source: https://docs.vllm.ai/projects/recipes/en/stable/inclusionAI/Ring-1T-FP8.html
lastmod: 2026-04-27

# Ring-1T-FP8 Usage Guide[¶](https://docs.vllm.ai#ring-1t-fp8-usage-guide)

This guide describes how to run Ring-1T-FP8.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

## Installing vLLM (For AMD ROCm: MI300x/MI325x/MI355x)[¶](https://docs.vllm.ai#installing-vllm-for-amd-rocm-mi300xmi325xmi355x)

⚠️ The vLLM wheel for ROCm is compatible with Python 3.12, ROCm 7.0, and glibc >= 2.35. If your environment is incompatible, please use docker flow in [vLLM](https://vllm.ai/)

## Running Ring-1T-FP8 with FP8 KV Cache on 8xH200[¶](https://docs.vllm.ai#running-ring-1t-fp8-with-fp8-kv-cache-on-8xh200)

This guide covers the simplest way to run the model, using pure tensor parallel across 8 GPUs.

# Start server with FP8 model on 8 GPUs
vllm serve inclusionAI/Ring-1T-FP8 \
--trust-remote-code \
--tensor-parallel-size 8 \
--gpu-memory-utilization 0.97 \
--max_num_seqs 32 \
--kv-cache-dtype fp8 \
--compilation-config '{"use_inductor": false}' \
--served-model-name Ring-1T-FP8


- You can set
`--max-model-len`

to preserve memory.`--max-model-len=65536`

is usually good for most scenarios. - You can set
`--max-num-batched-tokens`

to balance throughput and latency, higher means higher throughput but higher latency.`--max-num-batched-tokens=32768`

is usually good for prompt-heavy workloads. But you can reduce it to 16384 and 8192 to reduce activation memory usage and decrease latency. - In the example, 97% of the total memory is used for this model, you can reduce it to a smaller number if an Out-Of-Memory (OOM) error occurs.

## Running Ring-1T-FP8 with FP8 KV Cache on 8xMI300x/MI325x/MI355x[¶](https://docs.vllm.ai#running-ring-1t-fp8-with-fp8-kv-cache-on-8xmi300xmi325xmi355x)

# Start server with FP8 model on 8 GPUs
export VLLM_ROCM_USE_AITER=1
vllm serve inclusionAI/Ring-1T-FP8 \
--trust-remote-code \
--tensor-parallel-size 8 \
--gpu-memory-utilization 0.9 \
--max_num_seqs 32 \
--kv-cache-dtype fp8 \
--served-model-name Ring-1T-FP8


`export VLLM_ROCM_USE_AITER=1`

for Better Performance on AMD GPUs. The default is `export VLLM_ROCM_USE_AITER=0`

## Sending Example Request[¶](https://docs.vllm.ai#sending-example-request)

You can send a request like the following to quickly verify the deployment.