# [Issue #29] 求助，运行一直异常退出，llama-7b-hf模型，A100, worker 一直出现异常退出

source: https://github.com/LLMServe/DistServe/issues/29
state: closed | updated: 2024-11-26T21:34:02Z
labels: 

## 正文

我用了2张卡，A100的机器,  看着也没用啥显存，pp和tp就是1，但是一直异常退出错误信息如下：

INFO 12:20:10 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
INFO 12:20:10 (decoding) CPU blocks: 0 / 2048 (0.00%) used, (0 swapping in)
INFO 12:20:10 (decoding) GPU blocks: 70 / 7467 (0.94%) used, (0 swapping out)
INFO 12:20:10 (decoding) 0 unaccepted, 0 waiting, 1 processing
INFO 12:20:10 (context) Forwarding with lengths [1139]
(context) Warning: Cannot decode token with id 137438954496. Error: out of range integral type conversion attempted
(raylet) A worker died or was killed while executing a task by an unexpected system error. To troubleshoot the problem, check the logs for the dead worker. RayTask ID: ffffffffffffffff4643ca20eddd0f767dfb6f8f07000000 Worker ID: 6536068ce8f7629c0e7caa88c83529a6f763a124689fcb5e43d25636 Node ID: a1ac48022b082e341024d15358be110126114be06dc797078ce8c65c Worker IP address: 33.137.92.88 Worker port: 10151 Worker PID: 18503 Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors.
Traceback (most recent call last):
  File "/DistServe/distserve/api_server/distserve_api_server.py", line 159, in start_event_loop_wrapper
    await task
  File "/DistServe/distserve/llm.py", line 167, in start_event_loop
    await self.engine.start_all_event_loops()
  File "/DistServe/distserve/engine.py", line 251, in start_all_event_loops
    await asyncio.gather(
  File "/DistServe/distserve/single_stage_engine.py", line 663, in start_event_loop
    await asyncio.gather(event_loop1(), event_loop2(), event_loop3())
  File "/DistServe/distserve/single_stage_engine.py", line 654, in event_loop2
    await self._step()
  File "/DistServe/distserve/single_stage_engine.py", line 600, in _step
    generated_tokens_ids = await self.batches_ret_futures[0]
ray.exceptions.RayActorError: The actor died unexpectedly before finishing this task.
	class_name: ParaWorker
	actor_id: 4643ca20eddd0f767dfb6f8f07000000
	pid: 18503
	namespace: 336d29b2-5654-4240-bec9-7def73115ad1
	ip: 33.137.92.88
The actor is dead because its worker process has died. Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors.

配置信息如下：

sampling_params = SamplingParams(
    n=1,
    use_beam_search=0,
    temperature=1,
    top_p=1,
    max_tokens=512,
    stop=["\n"]
 )

## 评论 (3)

### meda0719 · 2024-09-08

@dingzhiqiang Hi zhiqiang, how is the problem solved? I met the same one.

### awer-A · 2024-11-08

@meda0719 @dingzhiqiang Hi, how is the problem solved? I met the same one.

### lei-houjyu · 2024-11-26

Changing the model to facebook/opt-6.7b works for me. #16 
