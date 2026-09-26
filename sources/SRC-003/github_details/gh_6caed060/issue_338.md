# [Issue #338] GPU Stuck

source: https://github.com/vllm-project/vllm/issues/338
state: closed | updated: 2026-09-23T01:40:17Z
labels: bug

## 正文

<img width="966" alt="image" src="https://github.com/vllm-project/vllm/assets/23203109/ae28b18c-568d-49da-95f2-c039644dc19d">

I am using the vllm 0.1.1 version, Ubuntu 18.04. There is a server with 4 T4 GPU cards. 
I started 4 tasks simultaneously. But it seems that 2 out of 4 GPU was stuck.
May I ask why?

### multi-GPU offline inference
And When I try to run multi-GPU offline inference, it returns an error: the actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors.
The actor never ran - it was cancelled before it started running.

Unhandled exception: St13runtime_error. what(): NCCL Error 5: invalid usage

## 评论 (8)

### amazingkmy · 2023-07-03

i also have same issue, when i run "python -m vllm.entrypoints.api_server --tensor-parallel-size 4"

### MasKong · 2023-07-06

> i also have same issue, when i run "python -m vllm.entrypoints.api_server --tensor-parallel-size 4"

INFO 07-06 09:05:55 scheduler.py:254] Throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 3 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%

It seems that there is a problem during scheduling

### LiuXiaoxuanPKU · 2023-07-10

Could you provide the minimum code to reproduce the problem? Thanks a lot!

### MasKong · 2023-07-11

> Could you provide the minimum code to reproduce the problem? Thanks a lot!

The code is basically the same as the given example. The amount of data is around 1 million. Sometimes it got stuck after a few iterations. And sometimes it could run for more than a day without any problem....

And it seems that it worked after upgrading to version 0.1.2. So far I have run for 2 days and there is no problem. Thanks for your reply.

```
llm = LLM(model=model_path, tokenizer_mode='auto', tensor_parallel_size=tensor_parallel_size, swap_space=4, gpu_memory_utilization=0.9)
sampling_params = SamplingParams(temperature=0.1, top_k=-1, max_tokens=max_new_tokens, top_p=1)
outputs = llm.generate(part_batch_prompt, sampling_params, req_ids=part_req_ids, use_tqdm=True)
```

### MasKong · 2023-07-12

> Could you provide the minimum code to reproduce the problem? Thanks a lot!

The following command is employed to run inference code. And 2 out of 4 processes in a same server were killed. Is there any performance tuning instruction to avoid this problem? 
```
RAY_memory_monitor_refresh_ms=0 NCCL_P2P_DISABLE=1 CUDA_VISIBLE_DEVICES=1 python generate.py
```


### nootums · 2023-07-31

I'm facing this issue on 0.1.2 as well. 
I am trying to load llama-2-7b-chat-hf on 4 GPUs and it gets stuck loading the model. It gets stuck after VRAM usage hits 3919MB per GPU
<img width="639" alt="image" src="https://github.com/vllm-project/vllm/assets/65669681/46812a7b-ba37-479c-a0e2-b2aef6bcf91f">
Any way to fix this?


### Tomorrowxxy · 2023-08-18

#677 Same problem. Urgent need to solve

### hmellor · 2024-03-08

Closing this issue as stale as there has been no discussion in the past 3 months.

If you are still experiencing the issue you describe, feel free to re-open this issue.
