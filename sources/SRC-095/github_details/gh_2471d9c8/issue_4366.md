# [Issue #4366] [Bug] Failed to serve LLM using DP vLLM

source: https://github.com/ray-project/kuberay/issues/4366
state: open | updated: 2026-09-22T16:57:52Z
labels: stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

1. I was trying to serve LLM (Qwen2.5-0.5B-Instruct) using Data Parallelism, supported by vLLM, in k8s with RayServe. I have k8s cluster with 3 masters, 2 CPU worker nodes and 2 GPU worker nodes, each containing 1 Nvidia Tesla T4. I used manifest provided below.
```
apiVersion: ray.io/v1
kind: RayService
metadata:
  name: ray-serve-qwen
  namespace: ml-kuberay
spec:
  serveConfigV2: |
    applications:
    - name: llms
      import_path: ray.serve.llm:build_openai_app
      route_prefix: "/"
      args:
        llm_configs:
        - model_loading_config:
            model_id: qwen2.5-0.5b-instruct
            model_source: Qwen/Qwen2.5-0.5B-Instruct
          accelerator_type: "T4"
          runtime_env:
            env_vars:
              VLLM_USE_V1: "1"
          engine_kwargs:
            data_parallel_size: 2
            data_parallel_backend: ray
            data_parallel_size_local: 1
            max_model_len: 2048
            dtype: float16
            gpu_memory_utilization: 0.95
            enforce_eager: true
  rayClusterConfig:
    rayVersion: "2.51.0"
    headGroupSpec:
      rayStartParams:
        dashboard-host: "0.0.0.0"
        num-cpus: "0"
        num-gpus: "0"
      template:
        spec:
          containers:
          - name: ray-head
            image: rayproject/ray-llm:2.51.0-py311-cu128
            ports:
            - containerPort: 8000
              name: serve
              protocol: TCP
            - containerPort: 8080
              name: metrics
              protocol: TCP
            - containerPort: 6379
              name: gcs
              protocol: TCP
            - containerPort: 8265
              name: dashboard
              protocol: TCP
            - containerPort: 10001
              name: client
              protocol: TCP
            resources:
              limits:
                cpu: 2
                memory: 4Gi
              requests:
                cpu: 2
                memory: 4Gi
    workerGroupSpecs:
    - replicas: 2
      numOfHosts: 1
      groupName: gpu-group
      rayStartParams:
        num-cpus: "8"
        num-gpus: "1"
      template:
        spec:
          containers:
          - name: ray-worker
            image: rayproject/ray-llm:2.51.0-py311-cu128
            env:
            - name: HUGGING_FACE_HUB_TOKEN
              valueFrom:
                secretKeyRef:
                  name: hf-token
                  key: hf_token
            resources:
              limits:
                cpu: 8
                memory: 16Gi
                nvidia.com/gpu: "1"
              requests:
                cpu: 8
                memory: 16Gi
                nvidia.com/gpu: "1"
```
2. I was expecting data parallel deployment of qwen2.5 on two GPUs, similar to manually running `vllm serve Qwen/Qwen2.5-0.5B-Instruct --data-parallel-size 2 --data-parallel-size-local 1 --data-parallel-backend=ray`. Running `vllm serve` on one of the worker nodes successfully launched DP inference. However, when using RayServe, I always face the following problem `Not enough resources to allocate 2 placement groups, only created 1 placement groups.` and my deployment fails.
3. Complete log of model serving:
```
INFO 2026-01-12 05:52:49,920 controller 1004 -- Controller starting (version='2.51.0').
INFO 2026-01-12 05:52:49,927 controller 1004 -- Starting proxy on node 'a6cf1509e3756f463ad7fa92dd278e7f039e91655059f00cce1501ba' listening on '0.0.0.0:8000'.
INFO 2026-01-12 05:52:51,002 controller 1004 -- Deploying new app 'llms'.
INFO 2026-01-12 05:52:51,003 controller 1004 -- Importing and building app 'llms'.
INFO 2026-01-12 05:52:51,015 controller 1004 -- Received new config for application 'llms'. Cancelling previous request.
INFO 2026-01-12 05:52:51,015 controller 1004 -- Importing and building app 'llms'.
INFO 2026-01-12 05:53:02,879 controller 1004 -- Imported and built app 'llms' successfully.
INFO 2026-01-12 05:53:02,883 controller 1004 -- Deploying new version of Deployment(name='LLMServer:qwen2_5-0_5b-instruct', app='llms') (initial target replicas: 1).
INFO 2026-01-12 05:53:02,884 controller 1004 -- Deploying new version of Deployment(name='OpenAiIngress', app='llms') (initial target replicas: 1).
INFO 2026-01-12 05:53:02,990 controller 1004 -- Adding 1 replica to Deployment(name='LLMServer:qwen2_5-0_5b-instruct', app='llms').
INFO 2026-01-12 05:53:02,991 controller 1004 -- Starting Replica(id='6zrhrqfq', deployment='LLMServer:qwen2_5-0_5b-instruct', app='llms').
INFO 2026-01-12 05:53:02,992 controller 1004 -- Adding 1 replica to Deployment(name='OpenAiIngress', app='llms').
INFO 2026-01-12 05:53:02,993 controller 1004 -- Starting Replica(id='0rci2gyy', deployment='OpenAiIngress', app='llms').
INFO 2026-01-12 05:53:14,477 controller 1004 -- Starting proxy on node 'd71fe25d4a9e1e8159dd30d9c05f78dd50dc75021b927b9aeac18361' listening on '0.0.0.0:8000'.
WARNING 2026-01-12 05:53:33,039 controller 1004 -- Deployment 'LLMServer:qwen2_5-0_5b-instruct' in application 'llms' has 1 replicas that have taken more than 30s to initialize.
This may be caused by a slow __init__ or reconfigure method.
WARNING 2026-01-12 05:53:33,039 controller 1004 -- Deployment 'OpenAiIngress' in application 'llms' has 1 replicas that have taken more than 30s to initialize.
This may be caused by a slow __init__ or reconfigure method.
ERROR 2026-01-12 05:53:37,931 controller 1004 -- Exception in Replica(id='6zrhrqfq', deployment='LLMServer:qwen2_5-0_5b-instruct', app='llms'), the replica will be stopped.
Traceback (most recent call last):
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/deployment_state.py", line 771, in check_ready
    ) = ray.get(self._ready_obj_ref)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 2961, in get
    values, debugger_breakpoint = worker.get_objects(
                                  ^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 1026, in get_objects
    raise value.as_instanceof_cause()
ray.exceptions.RayTaskError(RuntimeError): ray::ServeReplica:llms:LLMServer:qwen2_5-0_5b-instruct.initialize_and_get_metadata() (pid=316, ip=10.233.69.249, actor_id=aa3366c129ab60063f7f77cd01000000, repr=<ray.serve._private.replica.ServeReplica:llms:LLMServer:qwen2_5-0_5b-instruct object at 0x71bfb2382010>)
  File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 456, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 1228, in initialize_and_get_metadata
    await self._replica_impl.initialize(deployment_config)
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 928, in initialize
    raise RuntimeError(traceback.format_exc()) from None
RuntimeError: Traceback (most recent call last):
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 890, in initialize
    await self._user_callable_wrapper.initialize_callable()
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 1649, in initialize_callable
    await self._call_func_or_gen(
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 1595, in _call_func_or_gen
    result = await result
             ^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/llm/_internal/serve/core/server/llm_server.py", line 145, in __init__
    await self.start()
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/llm/_internal/serve/core/server/llm_server.py", line 191, in start
    await asyncio.wait_for(self._start_engine(), timeout=ENGINE_START_TIMEOUT_S)
  File "/home/ray/anaconda3/lib/python3.11/asyncio/tasks.py", line 489, in wait_for
    return fut.result()
           ^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/llm/_internal/serve/core/server/llm_server.py", line 237, in _start_engine
    await self.engine.start()
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/llm/_internal/serve/engines/vllm/vllm_engine.py", line 186, in start
    self._engine_client = self._start_async_llm_engine(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/llm/_internal/serve/engines/vllm/vllm_engine.py", line 323, in _start_async_llm_engine
    engine_client = AsyncLLM(
                    ^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 134, in __init__
    self.engine_core = EngineCoreClient.make_async_mp_client(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 101, in make_async_mp_client
    return DPLBAsyncMPClient(*client_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 1125, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 975, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 769, in __init__
    super().__init__(
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 448, in __init__
    with launch_core_engines(vllm_config, executor_class,
  File "/home/ray/anaconda3/lib/python3.11/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 659, in launch_core_engines
    engine_actor_manager = CoreEngineActorManager(
                           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 259, in __init__
    CoreEngineActorManager.create_dp_placement_groups(vllm_config)
  File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 377, in create_dp_placement_groups
    raise ValueError(
ValueError: Not enough resources to allocate 2 placement groups, only created 1 placement groups. Available resources: {'42b4896ba1c9868d50df871c7698060b6f43eb10080dc8a8e8868c6b': {'CPU': 8.0, 'object_store_memory': 5110795468.0, 'memory': 17179869184.0, 'node:10.233.68.19': 1.0, 'accelerator_type:T4': 1.0, 'GPU': 1.0}, 'd71fe25d4a9e1e8159dd30d9c05f78dd50dc75021b927b9aeac18361': {'bundle_group_1e0456933982710c020b48c42ddf01000000': 999.999, 'GPU_group_0_1e0456933982710c020b48c42ddf01000000': 1.0, 'GPU_group_1e0456933982710c020b48c42ddf01000000': 1.0, 'accelerator_type:T4_group_0_1e0456933982710c020b48c42ddf01000000': 0.001, 'CPU': 7.0, 'memory': 17179869184.0, 'accelerator_type:T4_group_1e0456933982710c020b48c42ddf01000000': 0.001, 'bundle_group_0_1e0456933982710c020b48c42ddf01000000': 999.999, 'accelerator_type:T4': 0.999, 'node:10.233.69.249': 1.0, 'object_store_memory': 5110569369.0}, 'a6cf1509e3756f463ad7fa92dd278e7f039e91655059f00cce1501ba': {'CPU': 3.0, 'node:__internal_head__': 0.999, 'object_store_memory': 982191362.0, 'memory': 4294967296.0, 'node:10.233.68.84': 1.0}}
INFO 2026-01-12 05:53:37,934 controller 1004 -- Stopping Replica(id='6zrhrqfq', deployment='LLMServer:qwen2_5-0_5b-instruct', app='llms') (currently ReplicaState.STARTING).
```

Complete log of running `vllm serve` manually:
```
(base) ray@ray-serve-llm-raycluster-sknht-gpu-group-worker-kvgwz:~$ vllm serve Qwen/Qwen2.5-0.5B-Instruct --data-parallel-size 2 --data-parallel-size-local 1 --data-parallel-backend=ray
INFO 01-12 06:14:20 [__init__.py:216] Automatically detected platform cuda.
(APIServer pid=5332) INFO 01-12 06:14:25 [api_server.py:1839] vLLM API server version 0.11.0
(APIServer pid=5332) INFO 01-12 06:14:25 [utils.py:233] non-default args: {'model_tag': 'Qwen/Qwen2.5-0.5B-Instruct', 'model': 'Qwen/Qwen2.5-0.5B-Instruct', 'data_parallel_size': 2, 'data_parallel_size_local': 1, 'data_parallel_backend': 'ray'}
(APIServer pid=5332) INFO 01-12 06:14:26 [model.py:547] Resolved architecture: Qwen2ForCausalLM
(APIServer pid=5332) WARNING 01-12 06:14:26 [model.py:1682] Your device 'Tesla T4' (with compute capability 7.5) doesn't support torch.bfloat16. Falling back to torch.float16 for compatibility.
(APIServer pid=5332) WARNING 01-12 06:14:26 [model.py:1733] Casting torch.bfloat16 to torch.float16.
(APIServer pid=5332) INFO 01-12 06:14:26 [model.py:1510] Using max model len 32768
(APIServer pid=5332) INFO 01-12 06:14:26 [arg_utils.py:1271] Using host IP 10.233.68.19 as ray-based data parallel address
(APIServer pid=5332) INFO 01-12 06:14:26 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048.
(APIServer pid=5332) INFO 01-12 06:14:28 [utils.py:651] Started DP Coordinator process (PID: 5409)
(APIServer pid=5332) INFO 01-12 06:14:28 [utils.py:657] Starting ray-based data parallel backend
(APIServer pid=5332) INFO 01-12 06:14:28 [ray_env.py:63] RAY_NON_CARRY_OVER_ENV_VARS from config: set()
(APIServer pid=5332) INFO 01-12 06:14:28 [ray_env.py:65] Copying the following environment variables to DPEngineCoreActor: ['LD_LIBRARY_PATH', 'VLLM_WORKER_MULTIPROC_METHOD', 'VLLM_USE_V1']
(APIServer pid=5332) INFO 01-12 06:14:28 [ray_env.py:68] If certain env vars should NOT be copied, add them to /home/ray/.config/vllm/ray_non_carry_over_env_vars.json file
(APIServer pid=5332) 2026-01-12 06:14:28,042	INFO worker.py:1691 -- Using address ray-serve-llm-raycluster-sknht-head-svc.nova-ml-kuberay.svc.cluster.local:6379 set in the environment variable RAY_ADDRESS
(APIServer pid=5332) 2026-01-12 06:14:28,045	INFO worker.py:1832 -- Connecting to existing Ray cluster at address: ray-serve-llm-raycluster-sknht-head-svc.nova-ml-kuberay.svc.cluster.local:6379...
(APIServer pid=5332) 2026-01-12 06:14:28,072	INFO worker.py:2003 -- Connected to Ray cluster. View the dashboard at http://10.233.68.84:8265
(APIServer pid=5332) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py:2051: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
(APIServer pid=5332)   warnings.warn(
(APIServer pid=5332) INFO 01-12 06:14:28 [utils.py:319] Creating placement groups for data parallel
INFO 01-12 06:14:31 [__init__.py:216] Automatically detected platform cuda.
(APIServer pid=5332) (pid=5439, ip=10.233.69.249) INFO 01-12 06:15:14 [__init__.py:216] Automatically detected platform cuda.
(APIServer pid=5332) (DPEngineCoreActor pid=5862) [Gloo] Rank 0 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:17 [core.py:77] Initializing a V1 LLM engine (v0.11.0) with config: model='Qwen/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=2, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen2.5-0.5B-Instruct, enable_prefix_caching=True, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.sparse_attn_indexer"],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":[2,1],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null}
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) ERROR 01-12 06:15:19 [fa_utils.py:57] Cannot use FA version 2 is not supported due to FA2 is only supported on devices with compute capability >= 8
(APIServer pid=5332) (pid=5862) INFO 01-12 06:14:33 [__init__.py:216] Automatically detected platform cuda.
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:20 [parallel_state.py:1047] Adjusting world_size=2 rank=1 distributed_init_method=tcp://10.233.68.19:54291 for DP
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:21 [__init__.py:1384] Found nccl from library libnccl.so.2
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:21 [pynccl.py:103] vLLM is using nccl==2.27.3
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:21 [cuda_communicator.py:100] Using AllGather-ReduceScatter all2all manager.
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:21 [parallel_state.py:1208] rank 1 in world size 2 is assigned as DP rank 1, PP rank 0, TP rank 0, EP rank 1
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) WARNING 01-12 06:15:21 [topk_topp_sampler.py:66] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer.
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:21 [gpu_model_runner.py:2602] Starting to load model Qwen/Qwen2.5-0.5B-Instruct...
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:22 [gpu_model_runner.py:2634] Loading model from scratch...
(APIServer pid=5332) (DPEngineCoreActor pid=5862) [Gloo] Rank 0 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1 [repeated 13x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:36 [core.py:77] Initializing a V1 LLM engine (v0.11.0) with config: model='Qwen/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=2, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen2.5-0.5B-Instruct, enable_prefix_caching=True, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.sparse_attn_indexer"],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":[2,1],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null}
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:22 [cuda.py:372] Using FlexAttention backend on V1 engine.
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:22 [weight_utils.py:392] Using model weights format ['*.safetensors']
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:27 [weight_utils.py:413] Time spent downloading weights for Qwen/Qwen2.5-0.5B-Instruct: 4.551074 seconds
(APIServer pid=5332) (DPEngineCoreActor pid=5862) ERROR 01-12 06:14:38 [fa_utils.py:57] Cannot use FA version 2 is not supported due to FA2 is only supported on devices with compute capability >= 8
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:39 [parallel_state.py:1047] Adjusting world_size=2 rank=0 distributed_init_method=tcp://10.233.68.19:54291 for DP
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:40 [__init__.py:1384] Found nccl from library libnccl.so.2 [repeated 3x across cluster]
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:40 [pynccl.py:103] vLLM is using nccl==2.27.3 [repeated 3x across cluster]
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:40 [cuda_communicator.py:100] Using AllGather-ReduceScatter all2all manager.
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:40 [parallel_state.py:1208] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(APIServer pid=5332) (DPEngineCoreActor pid=5862) WARNING 01-12 06:14:41 [topk_topp_sampler.py:66] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer.
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:41 [gpu_model_runner.py:2602] Starting to load model Qwen/Qwen2.5-0.5B-Instruct...
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:41 [gpu_model_runner.py:2634] Loading model from scratch...
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:27 [weight_utils.py:450] No model.safetensors.index.json found in remote.
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:41 [cuda.py:372] Using FlexAttention backend on V1 engine.
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:28 [default_loader.py:267] Loading weights took 0.91 seconds
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:42 [weight_utils.py:392] Using model weights format ['*.safetensors']
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:28 [gpu_model_runner.py:2653] Model loading took 0.9271 GiB and 6.191529 seconds
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  1.10it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  1.10it/s]
(APIServer pid=5332) (DPEngineCoreActor pid=5862)
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:37 [backends.py:548] Using cache directory: /home/ray/.cache/vllm/torch_compile_cache/722293a0af/rank_0_1/backbone for vLLM's torch.compile
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:37 [backends.py:559] Dynamo bytecode transform time: 5.57 s
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:48 [weight_utils.py:413] Time spent downloading weights for Qwen/Qwen2.5-0.5B-Instruct: 6.345009 seconds
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:48 [weight_utils.py:450] No model.safetensors.index.json found in remote.
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:49 [default_loader.py:267] Loading weights took 0.93 seconds
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:50 [gpu_model_runner.py:2653] Model loading took 0.9271 GiB and 8.124228 seconds
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:40 [backends.py:197] Cache the graph for dynamic shape for later use
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) [rank1]:W0112 06:15:41.124000 5439 anaconda3/lib/python3.11/site-packages/torch/_inductor/utils.py:1436] [0/0] Not enough SMs to use max_autotune_gemm mode
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:55 [backends.py:218] Compiling a graph for dynamic shape takes 17.88 s
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:56 [backends.py:548] Using cache directory: /home/ray/.cache/vllm/torch_compile_cache/722293a0af/rank_0_0/backbone for vLLM's torch.compile
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:56 [backends.py:559] Dynamo bytecode transform time: 6.02 s
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:14:59 [backends.py:197] Cache the graph for dynamic shape for later use
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:58 [monitor.py:34] torch.compile takes 23.45 s in total
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:15:59 [gpu_worker.py:298] Available KV cache memory: 10.74 GiB
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:16:00 [kv_cache_utils.py:1087] GPU KV cache size: 938,544 tokens
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:16:00 [kv_cache_utils.py:1091] Maximum concurrency for 32,768 tokens per request: 28.64x
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) WARNING 01-12 06:16:00 [gpu_model_runner.py:3663] CUDAGraphMode.FULL_AND_PIECEWISE is not supported with FlexAttentionMetadataBuilder backend (support: AttentionCGSupport.NEVER); setting cudagraph_mode=PIECEWISE because attention is compiled piecewise
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:15:14 [backends.py:218] Compiling a graph for dynamic shape takes 17.62 s
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):   0%|          | 0/67 [00:00<?, ?it/s]
(APIServer pid=5332) (DPEngineCoreActor pid=5862) [rank0]:W0112 06:15:00.560000 5862 anaconda3/lib/python3.11/site-packages/torch/_inductor/utils.py:1436] [0/0] Not enough SMs to use max_autotune_gemm mode
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):   3%|▎         | 2/67 [00:00<00:03, 18.60it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):   6%|▌         | 4/67 [00:00<00:03, 19.23it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  10%|█         | 7/67 [00:00<00:02, 21.11it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  15%|█▍        | 10/67 [00:00<00:02, 21.69it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  19%|█▉        | 13/67 [00:00<00:02, 22.17it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  24%|██▍       | 16/67 [00:00<00:02, 22.84it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  28%|██▊       | 19/67 [00:00<00:02, 23.78it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  33%|███▎      | 22/67 [00:00<00:01, 24.55it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  37%|███▋      | 25/67 [00:01<00:01, 24.99it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  42%|████▏     | 28/67 [00:01<00:01, 25.42it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  46%|████▋     | 31/67 [00:01<00:01, 25.51it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  51%|█████     | 34/67 [00:01<00:01, 25.03it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  55%|█████▌    | 37/67 [00:01<00:01, 24.96it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  60%|█████▉    | 40/67 [00:01<00:01, 24.49it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  64%|██████▍   | 43/67 [00:01<00:00, 24.72it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  69%|██████▊   | 46/67 [00:01<00:00, 23.81it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  73%|███████▎  | 49/67 [00:02<00:00, 23.13it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  78%|███████▊  | 52/67 [00:02<00:00, 23.79it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  82%|████████▏ | 55/67 [00:02<00:00, 24.19it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  87%|████████▋ | 58/67 [00:02<00:00, 24.18it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  91%|█████████ | 61/67 [00:02<00:00, 23.12it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):  96%|█████████▌| 64/67 [00:02<00:00, 23.61it/s]
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████| 67/67 [00:02<00:00, 23.28it/s]
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:16:05 [gpu_model_runner.py:3480] Graph capturing finished in 5 secs, took 0.37 GiB
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:15:18 [monitor.py:34] torch.compile takes 23.64 s in total
(APIServer pid=5332) (DPEngineCoreActor pid=5862) INFO 01-12 06:15:19 [gpu_worker.py:298] Available KV cache memory: 10.74 GiB
(APIServer pid=5332) (DPEngineCoreActor pid=5439, ip=10.233.69.249) INFO 01-12 06:16:05 [core.py:210] init engine (profile, create kv cache, warmup model) took 36.44 seconds
INFO 01-12 06:15:25 [coordinator.py:187] All engine subscriptions received by DP coordinator
(APIServer pid=5332) INFO 01-12 06:15:26 [api_server.py:1634] Supported_tasks: ['generate']
(APIServer pid=5332) WARNING 01-12 06:15:26 [model.py:1389] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`.
(APIServer pid=5332) INFO 01-12 06:15:26 [serving_responses.py:137] Using default chat sampling params from model: {'repetition_penalty': 1.1, 'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
(APIServer pid=5332) INFO 01-12 06:15:27 [serving_chat.py:139] Using default chat sampling params from model: {'repetition_penalty': 1.1, 'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
(APIServer pid=5332) INFO 01-12 06:15:27 [serving_completion.py:76] Using default completion sampling params from model: {'repetition_penalty': 1.1, 'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
(APIServer pid=5332) INFO 01-12 06:15:27 [api_server.py:1912] Starting vLLM API server 0 on http://0.0.0.0:8000
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:34] Available routes are:
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /openapi.json, Methods: GET, HEAD
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /docs, Methods: GET, HEAD
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /docs/oauth2-redirect, Methods: GET, HEAD
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /redoc, Methods: GET, HEAD
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /health, Methods: GET
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /load, Methods: GET
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /ping, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /ping, Methods: GET
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /tokenize, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /detokenize, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/models, Methods: GET
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /version, Methods: GET
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/responses, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/responses/{response_id}, Methods: GET
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/responses/{response_id}/cancel, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/chat/completions, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/completions, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/embeddings, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /pooling, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /classify, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /score, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/score, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/audio/translations, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /rerank, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v1/rerank, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /v2/rerank, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /scale_elastic_ep, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /is_scaling_elastic_ep, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /invocations, Methods: POST
(APIServer pid=5332) INFO 01-12 06:15:27 [launcher.py:42] Route: /metrics, Methods: GET
(APIServer pid=5332) INFO:     Started server process [5332]
(APIServer pid=5332) INFO:     Waiting for application startup.
(APIServer pid=5332) INFO:     Application startup complete.
```

### Reproduction script

1. Apply RayService manifest, provided earlier.
2. Check serve logs.

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (2)

### Future-Outlier · 2026-01-24

Hi, 
1. can you provide `kubectl get pods`'s result?
2. can you provide ray dashboard's screenshot for us to get node's information?
3. can you come to ray's slack, kuberay channel or ray server channel to discuss this issue?

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
