# [Issue #53] [ERROR] CUDA error

source: https://github.com/LLMServe/DistServe/issues/53
state: closed | updated: 2025-02-08T01:45:56Z
labels: 

## 正文

I would like to ask, I have two virtual machines, each with only one GPU Nividia A10, I modified the source code, started the ray cluster with two machines, and started the api server with the following command, there will be the following error, what is the problem? Thank you very much
python -m distserve.api_server.distserve_api_server \
    --host 0.0.0.0 \
    --port 8000 \
    --model openai-community/gpt2 \
    --tokenizer openai-community/gpt2 \
    --context-tensor-parallel-size 1 \
    --context-pipeline-parallel-size 1 \
    --decoding-tensor-parallel-size 1 \
    --decoding-pipeline-parallel-size 1 \
    --block-size 16 \
    --max-num-blocks-per-req 128 \
    --gpu-memory-utilization 0.95 \
    --swap-space 16 \
    --context-sched-policy fcfs \
    --context-max-batch-size 128 \
    --context-max-tokens-per-batch 8192 \
    --decoding-sched-policy fcfs \
    --decoding-max-batch-size 1024 \
    --decoding-max-tokens-per-batch 65536

<img width="1358" alt="image" src="https://github.com/user-attachments/assets/02aab532-1596-4e92-85af-8ee45b720e61" />
<img width="1066" alt="image" src="https://github.com/user-attachments/assets/39bebaec-32e4-4602-ac17-2d07d4224f24" />


## 评论 (2)

### interestingLSY · 2024-12-25

Currently DistServe relies on `cudaIpcMemHandle` for KV cache transferring. For one particular layer, DistServe requires the corresponding prefill & decoding instances to be reside on two GPUs on the same node, and those GPUs must be connected via NVLink (not really sure about this).

### MSMsssss · 2024-12-26

> 目前 DistServe 依赖于`cudaIpcMemHandle`KV 缓存传输。对于某一层，DistServe 要求相应的预填充和解码实例驻留在同一个节点上的两个 GPU 上，并且这些 GPU 必须通过 NVLink 连接（对此不太确定）。

Get, Thank you very much
