# [Issue #58] How to use DistServe with ray?

source: https://github.com/LLMServe/DistServe/issues/58
state: open | updated: 2025-04-24T06:16:08Z
labels: 

## 正文

I want to use DistServe for some experiments. But I do not know the logic of using it. First I use one terminal with `ray start --head` to start ray
Then I followed the /distserve/api_server/distserve_api_server.py using
```
CUDA_VISIBLE_DEVICES=0 python -m distserve.api_server.distserve_api_server \
    --host <ray ip>\
    --port 8000 \
    --model  <model path> \
    --tokenizer <model path>\
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
```
but I get an error  as followed:

```
Traceback (most recent call last):
  File "/data/software/miniconda/envs/distserve/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/data/software/miniconda/envs/distserve/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/data/Infer/DistServe/distserve/api_server/distserve_api_server.py", line 134, in <module>
    engine = AsyncLLM.from_engine_args(args)
  File "/data/Infer/DistServe/distserve/llm.py", line 124, in from_engine_args
    return AsyncLLM(
  File "/data/Infer/DistServe/distserve/llm.py", line 119, in __init__
    asyncio.run(self.engine.initialize())
  File "/data/software/miniconda/envs/distserve/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/data/software/miniconda/envs/distserve/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/data/Infer/DistServe/distserve/engine.py", line 208, in initialize
    await asyncio.gather(
  File "/data/Infer/DistServe/distserve/single_stage_engine.py", line 120, in initialize
    await self._init_workers()
  File "/data/Infer/DistServe/distserve/single_stage_engine.py", line 168, in _init_workers
    worker = ParaWorker.options(
  File "/data/software/miniconda/envs/distserve/lib/python3.10/site-packages/ray/actor.py", line 869, in remote
    return actor_cls._remote(args=args, kwargs=kwargs, **updated_options)
  File "/data/software/miniconda/envs/distserve/lib/python3.10/site-packages/ray/_private/auto_init_hook.py", line 21, in auto_init_wrapper
    return fn(*args, **kwargs)
  File "/data/software/miniconda/envs/distserve/lib/python3.10/site-packages/ray/util/tracing/tracing_helper.py", line 384, in _invocation_actor_class_remote_span
    return method(self, args, kwargs, *_args, **_kwargs)
  File "/data/software/miniconda/envs/distserve/lib/python3.10/site-packages/ray/actor.py", line 1079, in _remote
    worker.function_actor_manager.export_actor_class(
  File "/data/software/miniconda/envs/distserve/lib/python3.10/site-packages/ray/_private/function_manager.py", line 487, in export_actor_class
    serialized_actor_class = pickle_dumps(
  File "/data/software/miniconda/envs/distserve/lib/python3.10/site-packages/ray/_private/serialization.py", line 78, in pickle_dumps
    raise TypeError(msg) from e
TypeError: Could not serialize the actor class distserve.worker.ParaWorker.__init__:
================================================================================
Checking Serializability of <class 'distserve.worker._modify_class.<locals>.Class'>
================================================================================
!!! FAIL serialization: '_OpNamespace' object is not callable
    Serializing '__init__' <function ParaWorker.__init__ at 0x7f2d67235cf0>...
    Serializing '__ray_call__' <function _modify_class.<locals>.Class.__ray_call__ at 0x7f2d67235d80>...
    Serializing '__ray_ready__' <function _modify_class.<locals>.Class.__ray_ready__ at 0x7f2d67235e10>...
    Serializing '__ray_terminate__' <function _modify_class.<locals>.Class.__ray_terminate__ at 0x7f2d67235ea0>...
    Serializing '_get_block_size_in_bytes' <function ParaWorker._get_block_size_in_bytes at 0x7f2d67235f30>...
    Serializing '_profile_num_available_blocks' <function ParaWorker._profile_num_available_blocks at 0x7f2d67235fc0>...
    Serializing 'clear_request_resource' <function ParaWorker.clear_request_resource at 0x7f2d67236050>...
    Serializing 'clear_request_resource_batched' <function ParaWorker.clear_request_resource_batched at 0x7f2d672360e0>...
    Serializing 'init_kvcache_and_swap' <function ParaWorker.init_kvcache_and_swap at 0x7f2d67236170>...
    !!! FAIL serialization: '_OpNamespace' object is not callable
    Detected 7 global variables. Checking serializability...
        Serializing '_is_tracing_enabled' <function _is_tracing_enabled at 0x7f2d676df0a0>...
        Serializing '_opentelemetry' None...
        Serializing '__name__' ray.util.tracing.tracing_helper...
        Serializing '_use_context' <function _use_context at 0x7f2d6745e950>...
        Serializing '_DictPropagator' <class 'ray.util.tracing.tracing_helper._DictPropagator'>...
        Serializing '_actor_span_consumer_name' <function _actor_span_consumer_name at 0x7f2d6745ecb0>...
        Serializing '_actor_hydrate_span_args' <function _actor_hydrate_span_args at 0x7f2d6745eb90>...
    Detected 1 nonlocal variables. Checking serializability...
        Serializing 'method' <function ParaWorker.init_kvcache_and_swap at 0x7f2d672353f0>...
        !!! FAIL serialization: '_OpNamespace' object is not callable
        Detected 1 global variables. Checking serializability...
            Serializing 'torch' <module 'torch' from '/data/lkx/software/miniconda/envs/distserve/lib/python3.10/site-packages/torch/__init__.py'>...
        WARNING: Did not find non-serializable object in <function ParaWorker.init_kvcache_and_swap at 0x7f2d672353f0>. This may be an oversight.
    Serializing '_get_block_size_in_bytes' <function ParaWorker._get_block_size_in_bytes at 0x7f2d67235f30>...
================================================================================
Variable: 

        FailTuple(method [obj=<function ParaWorker.init_kvcache_and_swap at 0x7f2d672353f0>, parent=<function ParaWorker.init_kvcache_and_swap at 0x7f2d67236170>])

was found to be non-serializable. There may be multiple other undetected variables that were non-serializable. 
Consider either removing the instantiation/imports of these variables or moving the instantiation into the scope of the function/class. 
================================================================================
Check https://docs.ray.io/en/master/ray-core/objects/serialization.html#troubleshooting for more information.
If you have any suggestions on how to improve this error message, please reach out to the Ray developers on github.com/ray-project/ray/issues/
================================================================================
```

## 评论 (2)

### Haoyanlong · 2025-04-24

@Liaukx , hello!Is th is issue resolved?I have the same problem?

![Image](https://github.com/user-attachments/assets/442a5388-e538-4f34-b193-517800335e06)

### Liaukx · 2025-04-24

> [@Liaukx](https://github.com/Liaukx) , hello!Is th is issue resolved?I have the same problem?
> 
> ![Image](https://github.com/user-attachments/assets/442a5388-e538-4f34-b193-517800335e06)

I solved this, however I forgot how to solve. And if you are use single node, multi devices, it is no need to use ray. And the version of SwiftTransformer also impacts the installation of distserve. 
