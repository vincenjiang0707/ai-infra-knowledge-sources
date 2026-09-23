source: https://docs.vllm.ai/projects/recipes/en/stable/Qwen/Qwen3-Coder-480B-A35B.html
lastmod: 2026-04-27

# Qwen3-Coder Usage Guide[¶](https://docs.vllm.ai#qwen3-coder-usage-guide)

[Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) is an advanced large language model created by the Qwen team from Alibaba Cloud. vLLM already supports Qwen3-Coder, and `tool-call`

functionality will be available in vLLM v0.10.0 and higher You can install vLLM with `tool-call`

support using the following method:

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

### CUDA[¶](https://docs.vllm.ai#cuda)

### ROCm (MI300X, MI325X, MI355X)[¶](https://docs.vllm.ai#rocm-mi300x-mi325x-mi355x)

uv venv
source .venv/bin/activate
uv pip install vllm --extra-index-url https://wheels.vllm.ai/rocm/


[vLLM](https://vllm.ai/)

## Launching Qwen3-Coder with vLLM[¶](https://docs.vllm.ai#launching-qwen3-coder-with-vllm)

### Serving on 8xH200 (or H20) GPUs (141GB × 8)[¶](https://docs.vllm.ai#serving-on-8xh200-or-h20-gpus-141gb-8)

**BF16 Model**

vllm serve Qwen/Qwen3-Coder-480B-A35B-Instruct \
--max-model-len 32000 \
--enable-expert-parallel \
--tensor-parallel-size 8 \
--enable-auto-tool-choice \
--tool-call-parser qwen3_coder


**FP8 Model**

VLLM_USE_DEEP_GEMM=1 vllm serve Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \
--max-model-len 131072 \
--enable-expert-parallel \
--data-parallel-size 8 \
--enable-auto-tool-choice \
--tool-call-parser qwen3_coder


### Serving on 8xMI300x/MI325x/MI355x GPUs[¶](https://docs.vllm.ai#serving-on-8xmi300xmi325xmi355x-gpus)

**BF16 Model**

VLLM_ROCM_USE_AITER=1 vllm serve Qwen/Qwen3-Coder-480B-A35B-Instruct \
--max-model-len 32000 \
--enable-expert-parallel \
--tensor-parallel-size 8 \
--enable-auto-tool-choice \
--tool-call-parser qwen3_coder


**FP8 Model**

VLLM_ROCM_USE_AITER=1 vllm serve Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \
--trust-remote-code \
--max-model-len 131072 \
--enable-expert-parallel \
--data-parallel-size 8 \
--enable-auto-tool-choice \
--tool-call-parser qwen3_coder


## Performance Metrics[¶](https://docs.vllm.ai#performance-metrics)

### Evaluation[¶](https://docs.vllm.ai#evaluation)

We launched `Qwen3-Coder-480B-A35B-Instruct-FP8`

using vLLM and evaluated its performance using [EvalPlus](https://github.com/evalplus/evalplus). The results are displayed below:

| Dataset | Test Type | Pass@1 Score |
|---|---|---|
| HumanEval | Base tests | 0.939 |
| HumanEval+ | Base + extra tests | 0.902 |
| MBPP | Base tests | 0.918 |
| MBPP+ | Base + extra tests | 0.794 |

### Benchmarking[¶](https://docs.vllm.ai#benchmarking)

We used the following script to benchmark `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`


vllm bench serve \
--backend vllm \
--model Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \
--endpoint /v1/completions \
--dataset-name random \
--random-input 2048 \
--random-output 1024 \
--max-concurrency 10 \
--num-prompt 100


============ Serving Benchmark Result ============
Successful requests: 100
Benchmark duration (s): 776.49
Total input tokens: 204169
Total generated tokens: 102400
Request throughput (req/s): 0.13
Output token throughput (tok/s): 131.88
Total Token throughput (tok/s): 394.81
---------------Time to First Token----------------
Mean TTFT (ms): 7639.31
Median TTFT (ms): 6935.71
P99 TTFT (ms): 13766.68
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms): 68.43
Median TPOT (ms): 67.23
P99 TPOT (ms): 72.14
---------------Inter-token Latency----------------
Mean ITL (ms): 68.43
Median ITL (ms): 66.34
P99 ITL (ms): 69.38
==================================================


## Using Tips[¶](https://docs.vllm.ai#using-tips)

### BF16 Models[¶](https://docs.vllm.ai#bf16-models)

**Context Length Limitation**: A single H20 node cannot serve the original context length (262144). You can reduce the`max-model-len`

or increase`gpu-memory-utilization`

to work within memory constraints.

### FP8 Models[¶](https://docs.vllm.ai#fp8-models)

**Context Length Limitation**: A single H20 node cannot serve the original context length (262144). You can reduce the`max-model-len`

or increase`gpu-memory-utilization`

to work within memory constraints.**DeepGEMM Usage**: To use[DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), set`VLLM_USE_DEEP_GEMM=1`

. Follow the[setup instructions](https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/deepgemm/README.md#setup)to install it.**Tensor Parallelism Issue**: When using`tensor-parallel-size 8`

, the following failures are expected. Switch to data-parallel mode using`--data-parallel-size`

.**Additional Resources**: Refer to the[Data Parallel Deployment documentation](https://docs.vllm.ai/en/latest/serving/data_parallel_deployment.html)for more parallelism groups.

ERROR [multiproc_executor.py:511] File "/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
ERROR [multiproc_executor.py:511] lambda prefix: Qwen3MoeDecoderLayer(config=config,
ERROR [multiproc_executor.py:511] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR [multiproc_executor.py:511] File "/vllm/vllm/model_executor/models/qwen3_moe.py", line 278, in __init__
ERROR [multiproc_executor.py:511] self.mlp = Qwen3MoeSparseMoeBlock(config=config,
ERROR [multiproc_executor.py:511] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR [multiproc_executor.py:511] File "/vllm/vllm/model_executor/models/qwen3_moe.py", line 113, in __init__
ERROR [multiproc_executor.py:511] self.experts = FusedMoE(num_experts=config.num_experts,
ERROR [multiproc_executor.py:511] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR [multiproc_executor.py:511] File "/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 773, in __init__
ERROR [multiproc_executor.py:511] self.quant_method.create_weights(layer=self, **moe_quant_params)
ERROR [multiproc_executor.py:511] File "/vllm/vllm/model_executor/layers/quantization/fp8.py", line 573, in create_weights
ERROR [multiproc_executor.py:511] raise ValueError(
ERROR [multiproc_executor.py:511] ValueError: The output_size of gate's and up's weight = 320 is not divisible by weight quantization block_n = 128.


### Tool Calling[¶](https://docs.vllm.ai#tool-calling)

**Enable Tool Calls**: Add`--tool-call-parser qwen3_coder`

to enable tool call parsing functionality, please refer to:[tool_calling](https://docs.vllm.ai/en/latest/features/tool_calling.html)

## Roadmap[¶](https://docs.vllm.ai#roadmap)

- [x] Add benchmark results