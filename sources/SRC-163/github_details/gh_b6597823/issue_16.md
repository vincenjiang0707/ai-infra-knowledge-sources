# [Issue #16] Decode Wrong Token

source: https://github.com/LLMServe/DistServe/issues/16
state: open | updated: 2025-06-27T04:41:37Z
labels: help wanted

## 正文

model: Llama-2-7b-hf
step: 
1、python3 converter.py --input "Llama-2-7b-hf/*.bin"--output /datasets/distserve/llama-7b  --dtype float16 --model llama
2、python3 api_server/distserve_api_server.py --port 6902 --model /datasets/distserve/llama-7b --context-tensor-parallel-size 1 --decoding-tensor-parallel-size 1
3、python3 evaluation/2-benchmark-serving/0-prepare-dataset.py --dataset-path Sharegpt
4、python3 evaluation/2-benchmark-serving/2-benchmark-serving.py --port 6902 

the error message:
![image](https://github.com/LLMServe/DistServe/assets/71002153/f620cccc-b4c4-4ea6-ac1c-c5d45cae069d)
SwiftTransformer/src/csrc/model/gpt/gpt.cc:278 'cudaMemcpy(ith_context_req_req_index.ptr, ith_context_req_req_index_cpu, sizeof(int64_t) * batch_size, cudaMemcpyHostToDevice)': (700) an illegal memory access was encountered

## 评论 (9)

### PKUFlyingPig · 2024-06-18

For llama2, you do not need to download the weights yourself. Just launch the api_server with `--model meta-llama/Llama-2-7b-hf` (the name matches the official name on huggingface), distserve will download and convert the weights for you.

### sitabulaixizawaluduo · 2024-06-18

> For llama2, you do not need to download the weights yourself. Just launch the api_server with `--model meta-llama/Llama-2-7b-hf` (the name matches the official name on huggingface), distserve will download and convert the weights for you.

Is there a difference between the two method? the LLama model which I used is also download from huggingface

### PKUFlyingPig · 2024-06-18

You may refer to the [downloader code](https://github.com/LLMServe/DistServe/tree/main/distserve/downloader) to see if you have missed some details during convertering.

### wangguanggg · 2024-07-27

@PKUFlyingPig my environment is the same as above, when the max_token is short is 20, it runs well. But when it is 512,it crash as above, can you help us to fix it, please?

### liweiqing1997 · 2024-08-13

一样的问题呢。
```

(decoding) Warning: Cannot decode token with id 139556372349952. Error: out of range integral type conversion attempted
^[[36m(ParaWorker pid=92789)
^[[0m [ERROR] CUDA error /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/SwiftTransformer/src/csrc/model/gpt/gpt.cc:278 'cudaMemcpy(ith_context_req_req_index.ptr, ith_context_req_req_index_cpu, sizeof(int64_t) * batch_size, cudaMemcpyHostToDevice)': (700) an illegal memory access was encountered
^[[36m(ParaWorker pid=92789)^[[0m INFO 13:51:35 (worker decoding.#0) model /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/converted_llama2/llama-2-7b-chat-ms loaded
^[[36m(ParaWorker pid=92789)^[[0m INFO 13:51:35 runtime peak memory: 13.068 GB
^[[36m(ParaWorker pid=92789)^[[0m INFO 13:51:35 total GPU memory: 79.151 GB
^[[36m(ParaWorker pid=92789)^[[0m INFO 13:51:35 kv cache size for one token: 0.50000 MB
^[[36m(ParaWorker pid=92789)^[[0m INFO 13:51:35 num_gpu_blocks: 7445
^[[36m(ParaWorker pid=92789)^[[0m INFO 13:51:35 num_cpu_blocks: 2048
INFO 13:53:26 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
INFO 13:53:26 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
INFO 13:53:26 (decoding) GPU blocks: 17 / 7445 (0.23%) used, (0 swapping out)
INFO 13:53:26 (decoding) 0 unaccepted, 0 waiting, 1 processing
^[[33m(raylet)^[[0m [2024-08-13 13:53:27,026 E 85978 86010] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2024-08-13_13-51-03_278533_85668 is over 95% full, available space: 232025309184; capacity: 17453327216640. Object creation will fail if spilling is required.
INFO 13:53:27 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
INFO 13:53:27 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
INFO 13:53:27 (decoding) GPU blocks: 17 / 7445 (0.23%) used, (0 swapping out)
INFO 13:53:27 (decoding) 0 unaccepted, 0 waiting, 1 processing
Traceback (most recent call last):
  File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/api_server/distserve_api_server.py", line 155, in start_event_loop_wrapper
    await task
  File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/llm.py", line 167, in start_event_loop
    await self.engine.start_all_event_loops()
  File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/engine.py", line 251, in start_all_event_loops
    await asyncio.gather(
  File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 663, in start_event_loop
    await asyncio.gather(event_loop1(), event_loop2(), event_loop3())
  File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 654, in event_loop2
    await self._step()
  File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 600, in _step
    generated_tokens_ids = await self.batches_ret_futures[0]
ray.exceptions.RayActorError: The actor died unexpectedly before finishing this task.
	class_name: ParaWorker
	actor_id: 7ea542eba0c6a45ad8374aec01000000
	pid: 92789
	namespace: 533540a2-e59a-4a17-8fa5-234a5621488f
	ip: 172.17.0.8
The actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors.

```

### liweiqing1997 · 2024-08-13

> 一样的问题呢。
> 
> ```
> 
> (decoding) Warning: Cannot decode token with id 139556372349952. Error: out of range integral type conversion attempted
> �[36m(ParaWorker pid=92789)
> �[0m [ERROR] CUDA error /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/SwiftTransformer/src/csrc/model/gpt/gpt.cc:278 'cudaMemcpy(ith_context_req_req_index.ptr, ith_context_req_req_index_cpu, sizeof(int64_t) * batch_size, cudaMemcpyHostToDevice)': (700) an illegal memory access was encountered
> �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 (worker decoding.#0) model /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/converted_llama2/llama-2-7b-chat-ms loaded
> �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 runtime peak memory: 13.068 GB
> �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 total GPU memory: 79.151 GB
> �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 kv cache size for one token: 0.50000 MB
> �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 num_gpu_blocks: 7445
> �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 num_cpu_blocks: 2048
> INFO 13:53:26 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
> INFO 13:53:26 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
> INFO 13:53:26 (decoding) GPU blocks: 17 / 7445 (0.23%) used, (0 swapping out)
> INFO 13:53:26 (decoding) 0 unaccepted, 0 waiting, 1 processing
> �[33m(raylet)�[0m [2024-08-13 13:53:27,026 E 85978 86010] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2024-08-13_13-51-03_278533_85668 is over 95% full, available space: 232025309184; capacity: 17453327216640. Object creation will fail if spilling is required.
> INFO 13:53:27 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
> INFO 13:53:27 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
> INFO 13:53:27 (decoding) GPU blocks: 17 / 7445 (0.23%) used, (0 swapping out)
> INFO 13:53:27 (decoding) 0 unaccepted, 0 waiting, 1 processing
> Traceback (most recent call last):
>   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/api_server/distserve_api_server.py", line 155, in start_event_loop_wrapper
>     await task
>   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/llm.py", line 167, in start_event_loop
>     await self.engine.start_all_event_loops()
>   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/engine.py", line 251, in start_all_event_loops
>     await asyncio.gather(
>   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 663, in start_event_loop
>     await asyncio.gather(event_loop1(), event_loop2(), event_loop3())
>   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 654, in event_loop2
>     await self._step()
>   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 600, in _step
>     generated_tokens_ids = await self.batches_ret_futures[0]
> ray.exceptions.RayActorError: The actor died unexpectedly before finishing this task.
> 	class_name: ParaWorker
> 	actor_id: 7ea542eba0c6a45ad8374aec01000000
> 	pid: 92789
> 	namespace: 533540a2-e59a-4a17-8fa5-234a5621488f
> 	ip: 172.17.0.8
> The actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors.
> ```

当prompt的长度过长的时候就会出现这个错误。

### Avabowler · 2024-08-29

> > 一样的问题呢。
> > ```
> > 
> > (decoding) Warning: Cannot decode token with id 139556372349952. Error: out of range integral type conversion attempted
> > �[36m(ParaWorker pid=92789)
> > �[0m [ERROR] CUDA error /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/SwiftTransformer/src/csrc/model/gpt/gpt.cc:278 'cudaMemcpy(ith_context_req_req_index.ptr, ith_context_req_req_index_cpu, sizeof(int64_t) * batch_size, cudaMemcpyHostToDevice)': (700) an illegal memory access was encountered
> > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 (worker decoding.#0) model /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/converted_llama2/llama-2-7b-chat-ms loaded
> > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 runtime peak memory: 13.068 GB
> > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 total GPU memory: 79.151 GB
> > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 kv cache size for one token: 0.50000 MB
> > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 num_gpu_blocks: 7445
> > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 num_cpu_blocks: 2048
> > INFO 13:53:26 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
> > INFO 13:53:26 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
> > INFO 13:53:26 (decoding) GPU blocks: 17 / 7445 (0.23%) used, (0 swapping out)
> > INFO 13:53:26 (decoding) 0 unaccepted, 0 waiting, 1 processing
> > �[33m(raylet)�[0m [2024-08-13 13:53:27,026 E 85978 86010] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2024-08-13_13-51-03_278533_85668 is over 95% full, available space: 232025309184; capacity: 17453327216640. Object creation will fail if spilling is required.
> > INFO 13:53:27 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
> > INFO 13:53:27 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
> > INFO 13:53:27 (decoding) GPU blocks: 17 / 7445 (0.23%) used, (0 swapping out)
> > INFO 13:53:27 (decoding) 0 unaccepted, 0 waiting, 1 processing
> > Traceback (most recent call last):
> >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/api_server/distserve_api_server.py", line 155, in start_event_loop_wrapper
> >     await task
> >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/llm.py", line 167, in start_event_loop
> >     await self.engine.start_all_event_loops()
> >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/engine.py", line 251, in start_all_event_loops
> >     await asyncio.gather(
> >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 663, in start_event_loop
> >     await asyncio.gather(event_loop1(), event_loop2(), event_loop3())
> >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 654, in event_loop2
> >     await self._step()
> >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 600, in _step
> >     generated_tokens_ids = await self.batches_ret_futures[0]
> > ray.exceptions.RayActorError: The actor died unexpectedly before finishing this task.
> > 	class_name: ParaWorker
> > 	actor_id: 7ea542eba0c6a45ad8374aec01000000
> > 	pid: 92789
> > 	namespace: 533540a2-e59a-4a17-8fa5-234a5621488f
> > 	ip: 172.17.0.8
> > The actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors.
> > ```
> 
> 当prompt的长度过长的时候就会出现这个错误。

我也遇到了这个问题，我发现貌似是SwiftTransformer中[findmax函数](https://github.com/LLMServe/SwiftTransformer/blob/main/src/csrc/kernel/findmax.cu#L24)的max_idx没有初始化，所以返回了一个错误的token_idx，给他初始赋个词表内的值应该就能解决问题。但按理来说max_idx肯定在接下来的查询词表概率中最大的值的计算中会被赋值，可是似乎有些时候没被赋值？这似乎说明SwiftTransformer在某些情况下计算的结果是错误的？这一错误也会导致生成结果混乱，如[issue #40](https://github.com/LLMServe/DistServe/issues/40)所示。 @PKUFlyingPig 请问作者你们在实验时遇到过这种情况吗？

### WANG-WADE · 2024-10-18

> > > 一样的问题呢。
> > > ```
> > > 
> > > (decoding) Warning: Cannot decode token with id 139556372349952. Error: out of range integral type conversion attempted
> > > �[36m(ParaWorker pid=92789)
> > > �[0m [ERROR] CUDA error /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/SwiftTransformer/src/csrc/model/gpt/gpt.cc:278 'cudaMemcpy(ith_context_req_req_index.ptr, ith_context_req_req_index_cpu, sizeof(int64_t) * batch_size, cudaMemcpyHostToDevice)': (700) an illegal memory access was encountered
> > > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 (worker decoding.#0) model /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/converted_llama2/llama-2-7b-chat-ms loaded
> > > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 runtime peak memory: 13.068 GB
> > > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 total GPU memory: 79.151 GB
> > > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 kv cache size for one token: 0.50000 MB
> > > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 num_gpu_blocks: 7445
> > > �[36m(ParaWorker pid=92789)�[0m INFO 13:51:35 num_cpu_blocks: 2048
> > > INFO 13:53:26 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
> > > INFO 13:53:26 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
> > > INFO 13:53:26 (decoding) GPU blocks: 17 / 7445 (0.23%) used, (0 swapping out)
> > > INFO 13:53:26 (decoding) 0 unaccepted, 0 waiting, 1 processing
> > > �[33m(raylet)�[0m [2024-08-13 13:53:27,026 E 85978 86010] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2024-08-13_13-51-03_278533_85668 is over 95% full, available space: 232025309184; capacity: 17453327216640. Object creation will fail if spilling is required.
> > > INFO 13:53:27 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
> > > INFO 13:53:27 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
> > > INFO 13:53:27 (decoding) GPU blocks: 17 / 7445 (0.23%) used, (0 swapping out)
> > > INFO 13:53:27 (decoding) 0 unaccepted, 0 waiting, 1 processing
> > > Traceback (most recent call last):
> > >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/api_server/distserve_api_server.py", line 155, in start_event_loop_wrapper
> > >     await task
> > >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/llm.py", line 167, in start_event_loop
> > >     await self.engine.start_all_event_loops()
> > >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/engine.py", line 251, in start_all_event_loops
> > >     await asyncio.gather(
> > >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 663, in start_event_loop
> > >     await asyncio.gather(event_loop1(), event_loop2(), event_loop3())
> > >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 654, in event_loop2
> > >     await self._step()
> > >   File "/mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/distserve/single_stage_engine.py", line 600, in _step
> > >     generated_tokens_ids = await self.batches_ret_futures[0]
> > > ray.exceptions.RayActorError: The actor died unexpectedly before finishing this task.
> > > 	class_name: ParaWorker
> > > 	actor_id: 7ea542eba0c6a45ad8374aec01000000
> > > 	pid: 92789
> > > 	namespace: 533540a2-e59a-4a17-8fa5-234a5621488f
> > > 	ip: 172.17.0.8
> > > The actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors.
> > > ```
> > 
> > 
> > 当prompt的长度过长的时候就会出现这个错误。
> 
> 我也遇到了这个问题，我发现貌似是SwiftTransformer中[findmax函数](https://github.com/LLMServe/SwiftTransformer/blob/main/src/csrc/kernel/findmax.cu#L24)的max_idx没有初始化，所以返回了一个错误的token_idx，给他初始赋个词表内的值应该就能解决问题。但按理来说max_idx肯定在接下来的查询词表概率中最大的值的计算中会被赋值，可是似乎有些时候没被赋值？这似乎说明SwiftTransformer在某些情况下计算的结果是错误的？这一错误也会导致生成结果混乱，如[issue #40](https://github.com/LLMServe/DistServe/issues/40)所示。 @PKUFlyingPig 请问作者你们在实验时遇到过这种情况吗？

一样的问题，应该是作者在论文中只针对OPT做了验证实验，其他模型并没做扩展

### Sabiha1225 · 2025-06-27

I got this "CUDA error /mnt/data_disk101/data_disk/lwq/LLM_INFER/DistServe/SwiftTransformer/src/csrc/model/gpt/gpt.cc:278 'cudaMemcpy(ith_context_req_req_index.ptr, ith_context_req_req_index_cpu, sizeof(int64_t) * batch_size, cudaMemcpyHostToDevice)': (700) an illegal memory access was encountered" error with opt-125M, opt-1.3B, opt-6.7B with ShareGPT dataset. I could not run the opt models. How did you solve the error? Why this error is happening?
