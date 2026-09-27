# [Issue #3163] [Feature Request] Qwen3.6-27B need support

source: https://github.com/LMCache/LMCache/issues/3163
state: closed | updated: 2026-09-22T02:23:20Z
labels: stale

## 正文

**Label**
Please label your issue with "new feature" and any other relevant labels so that it can easily be easily categorized under [LMCache Onboarding](https://github.com/LMCache/LMCache/issues/1882)

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.


## 评论 (12)

### yoo-kumaneko · 2026-04-29

Would you mind elaborating on which specific feature in Qwen3.6 is currently blocking support?

### zacario-li · 2026-04-30

My server: 8 X A100-40G NVLink
vllm version: 0.19.1


my lmcache_config.yaml:
```chunk_size: 256
local_cpu: true
max_local_cpu_size: 80
remote_url: "lm://lmcache-server:65432"
remote_serde: "cachegen"
enable_async_loading: true
```
my vllm serve script:
```
--host 0.0.0.0 \
  --port 8000 \
  --served-model-name Qwen3.6-27B \
  --trust-remote-code \
  --max-model-len 262144 \
  --gpu-memory-utilization 0.75 \
  --enable-prefix-caching \
  --generation-config vllm \
  --tensor-parallel-size 4 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --disable-sliding-window \
  --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}'
```

when I start the serve, I got an error:
```
Hybrid KV cache manager is disabled for this hybrid model, This means we do not enable any optimizations for saving KV cache memory (e.g., dropping the KV cache outside the sliding window). The compute of layers like sliding window is still saved.
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949] WorkerProc hit an exception.
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949] Traceback (most recent call last):
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 944, in worker_busy_loop
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     output = func(*args, **kwargs)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     return func(*args, **kwargs)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 381, in determine_available_memory
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory()
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     return func(*args, **kwargs)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5864, in profile_cudagraph_memory
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     self._init_minimal_kv_cache_for_profiling()
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5804, in _init_minimal_kv_cache_for_profiling
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     kv_cache_groups = get_kv_cache_groups(self.vllm_config, kv_cache_spec)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/core/kv_cache_utils.py", line 1236, in get_kv_cache_groups
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     unify_hybrid_kv_cache_specs(kv_cache_spec)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/core/kv_cache_utils.py", line 1216, in unify_hybrid_kv_cache_specs
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     raise ValueError(
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949] ValueError: Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type.
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949] Traceback (most recent call last):
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 944, in worker_busy_loop
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     output = func(*args, **kwargs)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     return func(*args, **kwargs)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 381, in determine_available_memory
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory()
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     return func(*args, **kwargs)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5864, in profile_cudagraph_memory
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     self._init_minimal_kv_cache_for_profiling()
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5804, in _init_minimal_kv_cache_for_profiling
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     kv_cache_groups = get_kv_cache_groups(self.vllm_config, kv_cache_spec)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/core/kv_cache_utils.py", line 1236, in get_kv_cache_groups
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     unify_hybrid_kv_cache_specs(kv_cache_spec)
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/core/kv_cache_utils.py", line 1216, in unify_hybrid_kv_cache_specs
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]     raise ValueError(
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949] ValueError: Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type.
(Worker_TP0 pid=98743) ERROR 04-30 19:50:08 [multiproc_executor.py:949]
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108] EngineCore failed to start.
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108] Traceback (most recent call last):
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1082, in run_engine_core
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     return func(*args, **kwargs)
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     super().__init__(
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 124, in __init__
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     kv_cache_config = self._initialize_kv_caches(vllm_config)
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     return func(*args, **kwargs)
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 247, in _initialize_kv_caches
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/executor/abstract.py", line 136, in determine_available_memory
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     return self.collective_rpc("determine_available_memory")
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 397, in collective_rpc
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     return aggregate(get_response())
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]                      ^^^^^^^^^^^^^^
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]   File "/root/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 380, in get_response
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108]     raise RuntimeError(
(EngineCore pid=98495) ERROR 04-30 19:50:08 [core.py:1108] RuntimeError: Worker failed with error 'Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type.', please check the stack trace above for the root cause
```

### ApostaC · 2026-05-04

We probably need to implement the mamba support as well? IIUC, Qwen-3.6 series uses mamba layers.

### z7d1 · 2026-05-26

Same Error & Exception in start with Qwen3.5-27B: 
```txt
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962] WorkerProc hit an exception.
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962] Traceback (most recent call last):
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]   File "/data/vllm_source/vllm/v1/executor/multiproc_executor.py", line 957, in worker_busy_loop
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]     output = func(*args, **kwargs)
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]   File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]     return func(*args, **kwargs)
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]   File "/data/vllm_source/vllm/v1/worker/gpu_worker.py", line 385, in determine_available_memory
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]     cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory()
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]   File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]     return func(*args, **kwargs)
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]   File "/data/vllm_source/vllm/v1/worker/gpu_model_runner.py", line 5951, in profile_cudagraph_memory
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]     self._init_minimal_kv_cache_for_profiling()
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]   File "/data/vllm_source/vllm/v1/worker/gpu_model_runner.py", line 5870, in _init_minimal_kv_cache_for_profiling
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]     kv_cache_groups = get_kv_cache_groups(self.vllm_config, kv_cache_spec)
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]   File "/data/vllm_source/vllm/v1/core/kv_cache_utils.py", line 1625, in get_kv_cache_groups
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]     unify_hybrid_kv_cache_specs(kv_cache_spec)
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]   File "/data/vllm_source/vllm/v1/core/kv_cache_utils.py", line 1407, in unify_hybrid_kv_cache_specs
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962]     raise ValueError(
(Worker_TP0 pid=541) ERROR 05-26 02:41:53 [multiproc_executor.py:962] ValueError: Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type.
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136] EngineCore failed to start.
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136] Traceback (most recent call last):
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/engine/core.py", line 1110, in run_engine_core
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     return func(*args, **kwargs)
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/engine/core.py", line 876, in __init__
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     super().__init__(
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/engine/core.py", line 128, in __init__
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     kv_cache_config = self._initialize_kv_caches(vllm_config)
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     return func(*args, **kwargs)
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/engine/core.py", line 250, in _initialize_kv_caches
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/executor/abstract.py", line 147, in determine_available_memory
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     return self.collective_rpc("determine_available_memory")
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/executor/multiproc_executor.py", line 403, in collective_rpc
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     return future if non_block else future.result()
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/executor/multiproc_executor.py", line 90, in result
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     return super().result()
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/usr/lib/python3.10/concurrent/futures/_base.py", line 451, in result
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     return self.__get_result()
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/usr/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     raise self._exception
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/executor/multiproc_executor.py", line 94, in _wait_for_response
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     response = self.aggregate(self.get_response())
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]   File "/data/vllm_source/vllm/v1/executor/multiproc_executor.py", line 390, in get_response
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136]     raise RuntimeError(
(EngineCore pid=463) ERROR 05-26 02:41:53 [core.py:1136] RuntimeError: Worker failed with error 'Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type.', please check the stack trace above for the root cause
```

### anhalu · 2026-05-29

Any update on that issues ? 

### WenbinHou · 2026-05-30

+1 for this issue 👀 

### alexander-parra-glean · 2026-06-04

https://github.com/alexander-parra-glean/LMCache put up a fork to attempt to support hybrid attention. It was verified on `gemma4 26b a4b` running on L4s, but have to build new wheel to test against `gemma4` on A100 and `qwen3.6`. Feel free to try it

### closer-finger · 2026-06-10

same problem when i use qwen3.5 series models

### rfyiamcool · 2026-06-21

failed to use vllm depoy qwen3.6-2.7B on 2 * A800 (80G)

```
(EngineCore pid=101681)   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 390, in get_response
(EngineCore pid=101681)     raise RuntimeError(
(EngineCore pid=101681) RuntimeError: Worker failed with error 'Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type.', please check the stack trace above for the root cause
```

lm and vllm config

```
root@d8rin7cp420c73e7s2q0-yn6zc:~/workspace# cat lm.sh
lmcache server \
  --host 127.0.0.1 \
  --port 5555 \
  --chunk-size 784 \
  --http-host 0.0.0.0 \
  --http-port 8080 \
  --l1-size-gb 64 \
  --eviction-policy LRU \
  --eviction-trigger-watermark 0.8 \
  --eviction-ratio 0.2 \
  --max-workers 4

root@d8rin7cp420c73e7s2q0-yn6zc:~/workspace# cat vllm.sh
export VLLM_API_KEY='xxx'

python -m vllm.entrypoints.openai.api_server \
  --model /root/public-storage/model/Qwen/Qwen3.6-27B/ \
  --served-model-name Qwen3.6-27B \
  --tensor-parallel-size 2 \
  --gpu-memory-utilization 0.90 \
  --max-model-len 262144 \
  --trust-remote-code \
  --dtype bfloat16 \
  --api-key "${VLLM_API_KEY}" \
  --enable-prefix-caching \
  --mamba-cache-mode align \
  --max-num-batched-tokens 1567 \
  --disable-hybrid-kv-cache-manager \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --mm-encoder-tp-mode data \
  --kv-transfer-config '{"kv_connector":"LMCacheMPConnector","kv_role":"kv_both","kv_connector_extra_config":{"lmcache.mp.host":"127.0.0.1","lmcache.mp.port":5555}}' \
  --port 8000 \
  --host 0.0.0.0
```

### yoo-kumaneko · 2026-06-22

@rfyiamcool 
Try removing the "--disable-hybrid-kv-cache-manager" flag, as the hybrid manager should already be supported by the latest LMCache for now.

### github-actions[bot] · 2026-08-22

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### github-actions[bot] · 2026-09-22

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant!
