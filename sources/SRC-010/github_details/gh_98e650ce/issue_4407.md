# [Issue #4407] [Bug] Does lmdeploy support deploying glm-5 on A800 or A100, or are there any plans to support it?

source: https://github.com/InternLM/lmdeploy/issues/4407
state: open | updated: 2026-06-05T09:16:48Z
labels: 

## 正文

### Checklist

- [ ] 1. I have searched related issues but cannot get the expected help.
- [ ] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

Does lmdeploy support deploying glm-5 on A800 or A100, or are there any plans to support it? 

### Reproduction

Does lmdeploy support deploying glm-5 on A800 or A100, or are there any plans to support it? 

### Environment

```Shell
Does lmdeploy support deploying glm-5 on A800 or A100, or are there any plans to support it?
```

### Error traceback

```Shell

```

## 评论 (10)

### lvhan028 · 2026-03-12

Already supported it. 
You can use the latest main branch and use pytorch engine to deploy it.

### lvhan028 · 2026-03-12

But we haven't implemented its tool call parser.

### yangzhipeng1108 · 2026-03-13

thanks

### yangzhipeng1108 · 2026-03-13

lmdeploy serve api_server \
    /modelshare_readonly/zhipu/GLM-5  \
    --backend pytorch \
    --tp 32  --dtype float16 \
    --server-port 40000 \
    --max_batch_size 128 \
    --distributed-executor-backend ray  \
    --cache-max-entry-count 0.9
The following generation flags are not valid and may be ignored: ['top_p']. Set `TRANSFORMERS_VERBOSITY=info` for more details.
2026-03-13 10:15:05,676 - lmdeploy - WARNING - transformers.py:22 - LMDeploy requires transformers version: [4.33.0 ~ 4.57.3], but found version: 5.2.0
2026-03-13 10:15:06,517 INFO worker.py:1810 -- Connecting to existing Ray cluster at address: 10.88.0.44:6379...
2026-03-13 10:15:06,556 INFO worker.py:1810 -- Connecting to existing Ray cluster at address: 10.88.0.44:6379...
2026-03-13 10:15:06,604 INFO worker.py:2013 -- Connected to Ray cluster.
/usr/local/lib/python3.10/dist-packages/ray/_private/worker.py:2052: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
  warnings.warn(
(RayWorkerWrapper pid=297851) [Gloo] Rank 0 is connected to 31 peer ranks. Expected number of connected peer ranks is : 31
Process mp_engine_proc:
Traceback (most recent call last):
  File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/mp_engine/zmq_engine.py", line 109, in _mp_proc
    engine = Engine.from_pretrained(
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/engine.py", line 225, in from_pretrained
    return cls(
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/engine.py", line 145, in __init__
    self.executor.init()
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/executor/base.py", line 244, in init
    self.build_model()
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/executor/ray_executor.py", line 326, in build_model
    self.collective_rpc('build_model')
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/executor/ray_executor.py", line 322, in collective_rpc
    return ray.get([getattr(worker, method).remote(*args, **kwargs) for worker in self.workers], timeout=timeout)
  File "/usr/local/lib/python3.10/dist-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/ray/_private/worker.py", line 2981, in get
    values, debugger_breakpoint = worker.get_objects(
  File "/usr/local/lib/python3.10/dist-packages/ray/_private/worker.py", line 1012, in get_objects
    raise value.as_instanceof_cause()
ray.exceptions.RayTaskError(RuntimeError): ray::RayWorkerWrapper.build_model() (pid=204922, ip=10.88.0.47, actor_id=df6ea170924aca6ab26175d905000000, repr=<lmdeploy.pytorch.engine.executor.ray_executor.RayWorkerWrapper object at 0x7fca744f8bb0>)
  File "/usr/lib/python3.10/concurrent/futures/_base.py", line 458, in result
    return self.__get_result()
  File "/usr/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/executor/base_worker.py", line 92, in build_model
    self.model_agent.build_model()
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/model_agent/agent.py", line 1084, in build_model
    self._build_model()
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/engine/model_agent/agent.py", line 1071, in _build_model
    patched_model = build_patched_model(self.model_config, device=device, build_model_ctx=build_model_ctx)
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/models/patch.py", line 214, in build_patched_model
    return build_model_from_hf_config(model_config, dtype=dtype, device=device, build_model_ctx=build_model_ctx)
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/models/patch.py", line 199, in build_model_from_hf_config
    model_cls = _get_model_class(model_config, module_map)
  File "/usr/local/lib/python3.10/dist-packages/lmdeploy/pytorch/models/patch.py", line 185, in _get_model_class
    raise RuntimeError(f'Can not found rewrite for architectures: {architectures}')
RuntimeError: Can not found rewrite for architectures: ['GlmMoeDsaForCausalLM']
2026-03-13 10:15:16,062 ERROR worker.py:439 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerWrapper.build_model() (pid=297870, ip=10.88.0.44, actor_id=a873947fcce1d1334063e0cd05000000, repr=<lmdeploy.pytorch.engine.executor.ray_executor.RayWorkerWrapper object at 0x7fa7cbff4b50>)

### yangzhipeng1108 · 2026-03-13

lmdeploy == 0.12.1  transformers  ==5.2.0

### lvhan028 · 2026-03-13

GLM5-support feature has been merged to main but not be released yet. 
You can use the latest main branch as follows:
```
git clone https://github.com/InternLM/lmdeploy
export PYTHONPATH=$(pwd)/lmdeploy
```
**Note on deployment requirements:**
GLM-5 has 744B parameters, so the weight memory footprint is approximately 1.5TB.
To deploy it, you'll likely need 4× A100 (80GB) nodes with expert parallelism enabled (e.g., --dp 32 --ep 32).

We haven't been able to validate this configuration on our A100 test platform due to resource constraints, so results may vary. You're welcome to give it a shot and share your feedback with the community!

### chenxichen95 · 2026-03-23

@lvhan028 Hello, I am deploying GLM-5 on an A800 using the lmdeploy:v0.12.2-cu12.8 image and the following error:
2026-03-23 09:48:17,048 - lmdeploy - ERROR - base.py:55 - AssertionError: DeepSeek-V3.2 requires flash_mla to be available.
2026-03-23 09:48:17,048 - lmdeploy - ERROR - base.py:56 - <Model> check failed!
Checking failed with error DeepSeek-V3.2 requires flash_mla to be available.. Please send issue to LMDeploy with error logs.

And I check the [flash_mla_available](https://github.com/InternLM/lmdeploy/blob/160f8857b47f2d9665b0a7d260bf2312dab96b04/lmdeploy/pytorch/configurations/utils.py#L9) function, It requires sm greater than 9 
If flash_mla requires sm greater than 9, does that mean lmdeploy cannot deploy GLM-5 using a800?

### lvhan028 · 2026-03-23

Pytorch engine has mla fallback mechanism, doesn't it? @grimoire 


### xliangwu · 2026-03-24

> But we haven't implemented its tool call parser.

Is this feature under development? if I want to  use GLM-5 for coding or openclaw, request contains lots of tools. 

thanks.

### zt1024 · 2026-06-05

@lvhan028   "thank you，Is it possible to deploy GLM-5 using LMDeploy on an 8x A100 environment and enable 4-bit KV cache quantization with --quant-policy 4?"
