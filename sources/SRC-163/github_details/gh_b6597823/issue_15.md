# [Issue #15] Offline.py LLMEngine.__init__() missing 1 required positional argument: 'simulator_config'

source: https://github.com/LLMServe/DistServe/issues/15
state: open | updated: 2024-07-05T08:45:52Z
labels: help wanted

## 正文

I completed the installation of DistServe. When I tried to run the offline.py using my downloaded llama2 model, I encountered the following problem.

Traceback (most recent call last):
  File "/home/wangzhusheng/DistServe/./distserve/examples/offline.py", line 31, in <module>
    llm = OfflineLLM(
  File "/home/wangzhusheng/DistServe/distserve/llm.py", line 42, in __init__
    self.engine = LLMEngine(
TypeError: LLMEngine.__init__() missing 1 required positional argument: 'simulator_config'

So, I read the source code and find that there are 5 parameters in OfflineLLM class but 6 parameters in LLMEngine class, simulator_config is missing now. Could you please fix this issue in the provided examples?




## 评论 (5)

### PKUFlyingPig · 2024-06-14

Have you pulled the updated main branch? This bug has already been fixed in PR #11.

### fivebamboo694 · 2024-06-17

> Have you pulled the updated main branch? This bug has already been fixed in PR #11.

Thanks. This problem is fixed. However, when I try to run the command python ./examples/offline.py --model llama2-7B using my downloaded llama2-7B model, I encounter the following problem:

ray.exceptions.RayTaskError(RuntimeError): ray::ParaWorker.init_model() (pid=483561, ip=61.12.226.94, actor_id=2e36020ed4c51a284247d02201000000, repr=<distserve.worker.ParaWorker object at 0x7fca76f9a3e0>)
  File "/home/wangzhusheng/DistServe/distserve/worker.py", line 97, in init_model
    self.model.load_weight(path)
RuntimeError

INFO 12:56:58 Starting LLMEngine's event loops
INFO 12:56:58 (context) Forwarding with lengths [17, 6, 6, 8]
INFO 12:56:58 (context) 1 waiting, 0 finished but unaccepted, 5 blocks occupied by on-the-fly requests
INFO 12:56:58 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 12:56:58 (decoding) GPU blocks: 0 / 2044 (0.00%) used, (0 swapping out)
INFO 12:56:58 (decoding) 0 unaccepted, 0 waiting, 0 processing

When I use ctrl+c to quit, the following content is printed，

Gpt<T>::load() - llama2-7B/decoder.embed_tokens.weight.pt not found
Task exception was never retrieved
future: <Task finished name='Task-19' coro=<LLMEngine.start_all_event_loops() done, defined at /home/wangzhusheng/DistServe/distserve/engine.py:244> exception=RayTaskError(RuntimeError)(RuntimeError('Please load the weight before inference.'))>
Traceback (most recent call last):
  File "/home/wangzhusheng/DistServe/distserve/engine.py", line 251, in start_all_event_loops
    await asyncio.gather(
  File "/home/wangzhusheng/DistServe/distserve/single_stage_engine.py", line 423, in start_event_loop
    await asyncio.gather(event_loop1(), event_loop2())
  File "/home/wangzhusheng/DistServe/distserve/single_stage_engine.py", line 415, in event_loop1
    await self._step()
  File "/home/wangzhusheng/DistServe/distserve/single_stage_engine.py", line 355, in _step
    generated_tokens_ids = await self.batches_ret_futures[0]
ray.exceptions.RayTaskError(RuntimeError): ray::ParaWorker.step() (pid=483560, ip=61.12.226.94, actor_id=c68576230073ff4124b2037301000000, repr=<distserve.worker.ParaWorker object at 0x7fdcb850a470>)
  File "/home/wangzhusheng/DistServe/distserve/worker.py", line 217, in step
    generated_tokens_ids = self.model.forward(
RuntimeError: Please load the weight before inference.

Is there any idea to solve this problem? Let me know if I need to provide any further information. Thank you very much!





### PKUFlyingPig · 2024-06-18

Can you run `./examples/offline.py` directly? The script will automatically download the model `meta-llama/Llama-2-7b-hf` from huggingface and do the weight conversion.

### fivebamboo694 · 2024-06-18

> Can you run `./examples/offline.py` directly? The script will automatically download the model `meta-llama/Llama-2-7b-hf` from huggingface and do the weight conversion.

No, I am not able to run ./examples/offline.py directly because of some network connection problem. So, I try to use the downloaded model for simplicity.

### Chasingdreams6 · 2024-07-05

I got the same problem when I try to run local Llama7b chat model.
```cpp
(ParaWorker pid=59714) Gpt<T>::load() - /huggingface/hub/Llama-2-7b-hf/decoder.embed_tokens.weight.pt not found
Task exception was never retrieved
future: <Task finished name='Task-7' coro=<_wrap_awaitable() done, defined at /root/micromamba/envs/distserve/lib/python3.10/asyncio/tasks.py:643> exception=RayTaskError(RuntimeError)(RuntimeError(''))>
Traceback (most recent call last):
  File "/root/micromamba/envs/distserve/lib/python3.10/asyncio/tasks.py", line 650, in _wrap_awaitable
    return (yield from awaitable.__await__())
ray.exceptions.RayTaskError(RuntimeError): ray::ParaWorker.init_model() (pid=59713, ip=10.140.0.192, actor_id=cb94185f1857e5d5564fb66d01000000, repr=<distserve.worker.ParaWorker object at 0x7f75402f2ef0>)
  File "/app/distserve/distserve/worker.py", line 98, in init_model
    self.model.load_weight(path)
RuntimeError
```
It seems like my local 'decoder.embed_tokens.weight.pt' is missing, is the file offered by LLama, or generated by distServe?
