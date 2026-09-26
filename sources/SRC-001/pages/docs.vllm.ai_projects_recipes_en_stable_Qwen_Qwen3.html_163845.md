source: https://docs.vllm.ai/projects/recipes/en/stable/Qwen/Qwen3.html
lastmod: 2026-04-27

# Qwen3 Usage Guide[¶](https://docs.vllm.ai#qwen3-usage-guide)

## Introduction[¶](https://docs.vllm.ai#introduction)

This guide provides step-by-step instructions for running the Qwen3 series using vLLM. The guide is intended for developers and practitioners seeking high-throughput or low-latency inference on the targeted accelerated stack.

### TPU Deployment[¶](https://docs.vllm.ai#tpu-deployment)

## AMD GPU Support[¶](https://docs.vllm.ai#amd-gpu-support)

Recommended approaches by hardware type are:

MI300X/MI325X/MI355X

Please follow the steps here to install and run Qwen3 models on AMD MI300X/MI325X/MI355X GPU.

### Step 1: Installing vLLM (AMD ROCm Backend: MI300X, MI325X, MI355X)[¶](https://docs.vllm.ai#step-1-installing-vllm-amd-rocm-backend-mi300x-mi325x-mi355x)

Note: The vLLM wheel for ROCm requires Python 3.12, ROCm 7.0, and glibc >= 2.35. If your environment does not meet these requirements, please use the Docker-based setup as described in the

[documentation].


### Step 2: Start the vLLM server[¶](https://docs.vllm.ai#step-2-start-the-vllm-server)

### BF16[¶](https://docs.vllm.ai#bf16)

```bash
HIP_VISIBLE_DEVICES="4,5,6,7" \
VLLM_USE_V1=1 \
VLLM_ROCM_USE_AITER=1 \
VLLM_ROCM_USE_AITER_MHA=0 \
VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1 \
VLLM_USE_TRITON_FLASH_ATTN=0 \
SAFETENSORS_FAST_GPU=1 \
vllm serve Qwen/Qwen3-235B-A22B \
--trust-remote-code \
-tp 4 \
--disable-log-requests \
--swap-space 32 \
--distributed-executor-backend mp \
--max-num-batched-tokens 32768 \
--max-model-len 32768 \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.8
```


### FP8[¶](https://docs.vllm.ai#fp8)

```bash
HIP_VISIBLE_DEVICES="4,5,6,7" \
VLLM_USE_V1=1 \
VLLM_ROCM_USE_AITER=1 \
VLLM_ROCM_USE_AITER_MHA=0 \
VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1 \
VLLM_USE_TRITON_FLASH_ATTN=0 \
SAFETENSORS_FAST_GPU=1 \
vllm serve Qwen/Qwen3-235B-A22B-FP8 \
--trust-remote-code \
-tp 4 \
--disable-log-requests \
--swap-space 16 \
--distributed-executor-backend mp \
--max-num-batched-tokens 32768 \
--max-model-len 32768 \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.8
```