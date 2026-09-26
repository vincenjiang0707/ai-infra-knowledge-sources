# [Issue #130] Deploy EAGLE-Qwen2 in vllm

source: https://github.com/SafeAILab/EAGLE/issues/130
state: open | updated: 2025-08-17T04:48:34Z
labels: 

## 正文

Thanks for your great work, I would like deploy Qwen2-7B-Instruct in vllm, my current command is:

`python3 -m vllm.entrypoints.openai.api_server \
    --host 0.0.0.0 \
    --trust-remote-code \
    --dtype half \
    --max-model-len 32768 \
    --port=7801 \
    --disable-log-requests \
    --model=/mnt/model/Qwen2-7B-Instruct \
    --tokenizer-mode=auto \
    --speculative-model=/mnt/model/EAGLE-Qwen2-7B-Instruct \
    --use-v2-block-manager \
    --num-speculative-tokens 2 \
    --enforce-eager \
    --tensor-parallel-size=2 \
    --gpu-memory-utilization 1`

but I encounted the following error:
` File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/qwen2.py", line 420, in load_weights
    param = params_dict[name]
KeyError: 'layers.0.self_attn.qkv_proj.weight'`

my vllm version is 0.6.1.post2, is there a mistake?

## 评论 (8)

### crownz248 · 2024-09-25

Same issue! Have you solve it now?

### IvanDeng0 · 2024-09-25

Not yet, I tried to change  architecture from 'qwen2' to 'eagle' in config.json but encountered another error

### crownz248 · 2024-09-25

@IvanDeng0 I have solve this issue, you need to convert the eagle model to adapt to vllm. You can refer to [vllm/model_executor/models/eagle.py:L126](https://github.com/vllm-project/vllm/blob/8fae5ed7f6bfd63b81310fcb24b310d9205c9687/vllm/model_executor/models/eagle.py#L126). But I encountered another problem, because fc layer of eagle-qwen2 has bias attribute, but vllm only considers the case without bias, so I still cannot deploy eagle-qwen2 successfully

### IvanDeng0 · 2024-09-29

@crownz248 Thanks(I tried, but eagle seems not support TP > 1), I noticed your other issue, have you tried convert the qwen2 weight to llama weight to deploy on vllm? (maybe refer to [https://github.com/Minami-su/character_AI_open/blob/main/Qwen2_llamafy_Mistralfy/llamafy_qwen_v2.py](url))

And, have you compared the performance (e.g. TTFT, TPOT)  of  llama with naive inference? 

### YuvalCheung · 2025-01-20

Have you solved this problem yet? I encountered the same issue while using sglang + eagle. Here is my deployment script:

```sh
CUDA_VISIBLE_DEVICES=2,5 python3 -m sglang.launch_server \
    --served-model-name Qwen \
    --model-path "/mnt/tenant-home_speed/Model/Qwen/Qwen2-7B-Instruct" \
    --speculative-algo EAGLE \
    --speculative-draft "/mnt/tenant-home_speed/Model/yuhuili/EAGLE-Qwen2-7B-Instruct" \
    --speculative-num-steps 2 \
    --speculative-eagle-topk 4 \
    --speculative-num-draft-tokens 16 \
    --host 0.0.0.0 \
    --port 6007 \
    --tensor 2 \
    --mem-fraction-static 0.7 \
```


After running it, I get an error message like this:

```
KeyError: 'layers.0.self_attn.qkv_proj.weight'

[2025-01-20 19:10:07] Received sigquit from a child proces. It usually means the child failed.
[2025-01-20 19:10:07 TP0] Scheduler hit an exception: Traceback (most recent call last):
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/scheduler.py", line 1652, in run_scheduler_process
    scheduler = Scheduler(server_args, port_args, gpu_id, tp_rank, dp_rank)
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/scheduler.py", line 221, in __init__
    self.draft_worker = EAGLEWorker(
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/speculative/eagle_worker.py", line 33, in __init__
    super().__init__(
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/tp_worker.py", line 68, in __init__
    self.model_runner = ModelRunner(
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_executor/model_runner.py", line 176, in __init__
    self.load_model()
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_executor/model_runner.py", line 281, in load_model
    self.model = get_model(
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_loader/__init__.py", line 22, in get_model
    return loader.load_model(
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_loader/loader.py", line 362, in load_model
    model.load_weights(self._get_all_weights(model_config, model))
  File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/models/qwen2.py", line 353, in load_weights
    param = params_dict[name]
KeyError: 'layers.0.self_attn.qkv_proj.weight'

Loading pt checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]

```

### souyang11 · 2025-03-24

> Have you solved this problem yet? I encountered the same issue while using sglang + eagle. Here is my deployment script:
> 
> CUDA_VISIBLE_DEVICES=2,5 python3 -m sglang.launch_server \
>     --served-model-name Qwen \
>     --model-path "/mnt/tenant-home_speed/Model/Qwen/Qwen2-7B-Instruct" \
>     --speculative-algo EAGLE \
>     --speculative-draft "/mnt/tenant-home_speed/Model/yuhuili/EAGLE-Qwen2-7B-Instruct" \
>     --speculative-num-steps 2 \
>     --speculative-eagle-topk 4 \
>     --speculative-num-draft-tokens 16 \
>     --host 0.0.0.0 \
>     --port 6007 \
>     --tensor 2 \
>     --mem-fraction-static 0.7 \
> After running it, I get an error message like this:
> 
> ```
> KeyError: 'layers.0.self_attn.qkv_proj.weight'
> 
> [2025-01-20 19:10:07] Received sigquit from a child proces. It usually means the child failed.
> [2025-01-20 19:10:07 TP0] Scheduler hit an exception: Traceback (most recent call last):
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/scheduler.py", line 1652, in run_scheduler_process
>     scheduler = Scheduler(server_args, port_args, gpu_id, tp_rank, dp_rank)
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/scheduler.py", line 221, in __init__
>     self.draft_worker = EAGLEWorker(
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/speculative/eagle_worker.py", line 33, in __init__
>     super().__init__(
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/tp_worker.py", line 68, in __init__
>     self.model_runner = ModelRunner(
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_executor/model_runner.py", line 176, in __init__
>     self.load_model()
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_executor/model_runner.py", line 281, in load_model
>     self.model = get_model(
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_loader/__init__.py", line 22, in get_model
>     return loader.load_model(
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_loader/loader.py", line 362, in load_model
>     model.load_weights(self._get_all_weights(model_config, model))
>   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/models/qwen2.py", line 353, in load_weights
>     param = params_dict[name]
> KeyError: 'layers.0.self_attn.qkv_proj.weight'
> 
> Loading pt checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
> ```

Have you solved this problem? When I tested it, I found that the throughput of qwen2-eagle had decreased.

### 1180300427 · 2025-05-26

> > Have you solved this problem yet? I encountered the same issue while using sglang + eagle. Here is my deployment script:
> > CUDA_VISIBLE_DEVICES=2,5 python3 -m sglang.launch_server 
> > --served-model-name Qwen 
> > --model-path "/mnt/tenant-home_speed/Model/Qwen/Qwen2-7B-Instruct" 
> > --speculative-algo EAGLE 
> > --speculative-draft "/mnt/tenant-home_speed/Model/yuhuili/EAGLE-Qwen2-7B-Instruct" 
> > --speculative-num-steps 2 
> > --speculative-eagle-topk 4 
> > --speculative-num-draft-tokens 16 
> > --host 0.0.0.0 
> > --port 6007 
> > --tensor 2 
> > --mem-fraction-static 0.7 
> > After running it, I get an error message like this:
> > ```
> > KeyError: 'layers.0.self_attn.qkv_proj.weight'
> > 
> > [2025-01-20 19:10:07] Received sigquit from a child proces. It usually means the child failed.
> > [2025-01-20 19:10:07 TP0] Scheduler hit an exception: Traceback (most recent call last):
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/scheduler.py", line 1652, in run_scheduler_process
> >     scheduler = Scheduler(server_args, port_args, gpu_id, tp_rank, dp_rank)
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/scheduler.py", line 221, in __init__
> >     self.draft_worker = EAGLEWorker(
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/speculative/eagle_worker.py", line 33, in __init__
> >     super().__init__(
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/managers/tp_worker.py", line 68, in __init__
> >     self.model_runner = ModelRunner(
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_executor/model_runner.py", line 176, in __init__
> >     self.load_model()
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_executor/model_runner.py", line 281, in load_model
> >     self.model = get_model(
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_loader/__init__.py", line 22, in get_model
> >     return loader.load_model(
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/model_loader/loader.py", line 362, in load_model
> >     model.load_weights(self._get_all_weights(model_config, model))
> >   File "/mnt/tenant-home_speed/shard/zhangyu/python_env/sglang/lib/python3.10/site-packages/sglang/srt/models/qwen2.py", line 353, in load_weights
> >     param = params_dict[name]
> > KeyError: 'layers.0.self_attn.qkv_proj.weight'
> > 
> > Loading pt checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
> > ```
> 
> Have you solved this problem? When I tested it, I found that the throughput of qwen2-eagle had decreased.

I have the same question , the throughput of qwen2-eagle had decreased. How do you solve the problem?

### kevinlu1248 · 2025-08-17

I get this on both vLLM and sglang
