# [Issue #3574] [Bug]: Cannot load google/gemma-4-26B-A4B-it due to attn_dp sharding

source: https://github.com/AI-Hypercomputer/maxtext/issues/3574
state: closed | updated: 2026-04-28T17:24:33Z
labels: bug

## 正文

### Bug report

Hi, I am having an issue running Gemma 4 on a TPU VM:

```
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111] ValueError: Resource axis: attn_dp of PartitionSpec('data', None, ('model', 'attn_dp')) is not found in mesh: ('data', 'model').
```

Following this guide: https://github.com/AI-Hypercomputer/maxtext/blob/main/tests/end_to_end/tpu/gemma4/Run_Gemma4.md

And trying to do online inference.

Converted weights with:

```
HF_HOME=/dev/shm/huggingface_tmp USE_PATHWAYS=0 python3 -m maxtext.checkpoint_conversion.to_maxtext src/maxtext/configs/base.yml     model_name=gemma4-26b     hf_access_token=[...]     base_output_directory=/dev/shm/gemma4-26b/     use_multimodal=false     scan_layers=false hardware=cpu skip_jax_distributed_system=true --lazy_load_tensors=True
```

Startup script:

```
export MODEL_NAME=gemma4-26b
export CHECKPOINT_PATH=/dev/shm/gemma4-26b
vllm serve google/gemma-4-26B-A4B-it \
  --seed 42 \
  --max-model-len=5120 \
  --gpu-memory-utilization 0.97 \
  --no-enable-prefix-caching \
  --tensor-parallel-size 4 \
  --max-num-batched-tokens 4096 \
  --max_num_seqs 128 \
  --hf-overrides "{\"architectures\": [\"MaxTextForCausalLM\"]}" \
  --additional-config "{\"maxtext_config\": {\"model_name\": \"$MODEL_NAME\", \"log_config\": true, \"enable_dp_attention\": true, \"load_parameters_path\": \"$CHECKPOINT_PATH\"}}"
```

I realize that `enable_dp_attention` should be set to `true`, and I have done so, but VLLM doesn't seem to pick it up. I also tried adding `--data-parallel-size 2`, but no changes.

MaxText was installed from source (with uv).

Any clues?

Thanks!



### Logs/Output

<details>
<summary>Full log</summary>

```
INFO 04-04 21:49:56 [__init__.py:59] TPU info: node_name=tpu-0 | tpu_type=v5litepod-16 | worker_id=3 | num_chips=4 | num_cores_per_chip=1
INFO 04-04 21:50:03 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors.
INFO 04-04 21:50:03 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 04-04 21:50:03 [interface.py:226] Failed to import from vllm._C: ModuleNotFoundError("No module named 'vllm._C'")
Check failed with unknown exit code: -6.
WARNING 04-04 21:50:05 [__init__.py:80] The quantization method 'awq' already exists and will be overwritten by the quantization config <class 'tpu_inference.layers.vllm.quantization.awq.VllmAWQConfig'>.
WARNING 04-04 21:50:05 [__init__.py:80] The quantization method 'compressed-tensors' already exists and will be overwritten by the quantization config <class 'tpu_inference.layers.vllm.quantization.compressed_tensors.compressed_tensors.VllmCompressedTensorsConfig'>.
WARNING 04-04 21:50:05 [__init__.py:80] The quantization method 'fp8' already exists and will be overwritten by the quantization config <class 'tpu_inference.layers.vllm.quantization.fp8.VllmFp8Config'>.
WARNING 04-04 21:50:05 [__init__.py:80] The quantization method 'mxfp4' already exists and will be overwritten by the quantization config <class 'tpu_inference.layers.vllm.quantization.mxfp4.VllmMxfp4Config'>.
INFO 04-04 21:50:06 [__init__.py:31] Registering MaxTextForCausalLM model with tpu_inference and vllm.
INFO 04-04 21:50:06 [model_loader.py:588] Registered JAX model MaxTextForCausalLM with tpu_inference and vLLM registries.
INFO 04-04 21:50:06 [__init__.py:33] Successfully registered MaxTextForCausalLM model.
(APIServer pid=1355885) INFO 04-04 21:50:06 [utils.py:292] 
(APIServer pid=1355885) INFO 04-04 21:50:06 [utils.py:292]        █     █     █▄   ▄█
(APIServer pid=1355885) INFO 04-04 21:50:06 [utils.py:292]  ▄▄ ▄█ █     █     █ ▀▄▀ █  version 0.17.0rc1.dev136+gee8a29511
(APIServer pid=1355885) INFO 04-04 21:50:06 [utils.py:292]   █▄█▀ █     █     █     █  model   google/gemma-4-26B-A4B-it
(APIServer pid=1355885) INFO 04-04 21:50:06 [utils.py:292]    ▀▀  ▀▀▀▀▀ ▀▀▀▀▀ ▀     ▀
(APIServer pid=1355885) INFO 04-04 21:50:06 [utils.py:292] 
(APIServer pid=1355885) INFO 04-04 21:50:06 [utils.py:228] non-default args: {'model_tag': 'google/gemma-4-26B-A4B-it', 'model': 'google/gemma-4-26B-A4B-it', 'seed': 42, 'max_model_len': 5120, 'hf_overrides': {'architectures': ['MaxTextForCausalLM']}, 'tensor_parallel_size': 4, 'gpu_memory_utilization': 0.97, 'enable_prefix_caching': False, 'max_num_batched_tokens': 4096, 'max_num_seqs': 128, 'additional_config': {'maxtext_config': {'model_name': 'gemma4-26b', 'log_config': True, 'enable_dp_attention': True, 'load_parameters_path': '/dev/shm/gemma4-26b'}}}
(APIServer pid=1355885) INFO 04-04 21:50:07 [model.py:531] Resolved architecture: MaxTextForCausalLM
(APIServer pid=1355885) INFO 04-04 21:50:07 [model.py:1554] Using max model len 5120
(APIServer pid=1355885) INFO 04-04 21:50:07 [scheduler.py:231] Chunked prefill is enabled with max_num_batched_tokens=4096.
(APIServer pid=1355885) INFO 04-04 21:50:07 [vllm.py:753] Asynchronous scheduling is enabled.
(APIServer pid=1355885) INFO 04-04 21:50:07 [tpu_platform.py:141] Initialized sharding configuration: ShardingConfigManager(total_devices=4, sharding_strategy=ShardingStrategy(tensor_parallelism=4, expert_parallelism=1, sequence_parallelism=1, data_parallelism=1, attention_data_parallelism=1, attention_data_expert_parallelism=1), device_indexes=None)
(APIServer pid=1355885) INFO 04-04 21:50:07 [__init__.py:108] Registered model loader `<class 'tpu_inference.models.vllm.vllm_model_loader.IncrementalModelLoader'>` with load format `tpu_streaming_loader`
(APIServer pid=1355885) WARNING 04-04 21:50:07 [__init__.py:97] Load format `runai_streamer` is already registered, and will be overwritten by the new loader class `<class 'tpu_inference.models.vllm.vllm_model_loader.RunaiIncrementalModelLoader'>`.
(APIServer pid=1355885) INFO 04-04 21:50:07 [__init__.py:108] Registered model loader `<class 'tpu_inference.models.vllm.vllm_model_loader.RunaiIncrementalModelLoader'>` with load format `runai_streamer`
(APIServer pid=1355885) INFO 04-04 21:50:07 [tpu_platform.py:182] Using KV cache block size: 256
(APIServer pid=1355885) INFO 04-04 21:50:07 [tpu_platform.py:193] Force using UniProcExecutor for JAX on single host without pipeline parallelism.
(APIServer pid=1355885) INFO 04-04 21:50:07 [compilation.py:286] Enabled custom fusions: norm_quant, act_quant
(APIServer pid=1355885) WARNING 04-04 21:50:10 [input_processor.py:80] The signature of Platform.validate_request has changed from `(cls, prompt, params, processed_inputs) -> None` to `(cls, processed_inputs, params) -> None`. The old signature will no longer be supported starting from v0.18.
(APIServer pid=1355885) WARNING 04-04 21:50:10 [tpu_platform.py:231] Pin memory is not supported on TPU.
INFO 04-04 21:50:14 [__init__.py:59] TPU info: node_name=tpu-0 | tpu_type=v5litepod-16 | worker_id=3 | num_chips=4 | num_cores_per_chip=1
INFO 04-04 21:50:22 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors.
INFO 04-04 21:50:22 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 04-04 21:50:22 [interface.py:226] Failed to import from vllm._C: ModuleNotFoundError("No module named 'vllm._C'")
Check failed with unknown exit code: -6.
(EngineCore_DP0 pid=1356450) WARNING 04-04 21:50:24 [__init__.py:80] The quantization method 'awq' already exists and will be overwritten by the quantization config <class 'tpu_inference.layers.vllm.quantization.awq.VllmAWQConfig'>.
(EngineCore_DP0 pid=1356450) WARNING 04-04 21:50:24 [__init__.py:80] The quantization method 'compressed-tensors' already exists and will be overwritten by the quantization config <class 'tpu_inference.layers.vllm.quantization.compressed_tensors.compressed_tensors.VllmCompressedTensorsConfig'>.
(EngineCore_DP0 pid=1356450) WARNING 04-04 21:50:24 [__init__.py:80] The quantization method 'fp8' already exists and will be overwritten by the quantization config <class 'tpu_inference.layers.vllm.quantization.fp8.VllmFp8Config'>.
(EngineCore_DP0 pid=1356450) WARNING 04-04 21:50:24 [__init__.py:80] The quantization method 'mxfp4' already exists and will be overwritten by the quantization config <class 'tpu_inference.layers.vllm.quantization.mxfp4.VllmMxfp4Config'>.
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:25 [__init__.py:31] Registering MaxTextForCausalLM model with tpu_inference and vllm.
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:25 [model_loader.py:588] Registered JAX model MaxTextForCausalLM with tpu_inference and vLLM registries.
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:25 [__init__.py:33] Successfully registered MaxTextForCausalLM model.
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:25 [core.py:103] Initializing a V1 LLM engine (v0.17.0rc1.dev136+gee8a29511) with config: model='google/gemma-4-26B-A4B-it', speculative_config=None, tokenizer='google/gemma-4-26B-A4B-it', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=5120, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=None, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=False, enable_layerwise_nvtx_tracing=False, enable_mfu_metrics=False, enable_mm_processor_stats=False, enable_logging_iteration_details=False), seed=42, served_model_name=google/gemma-4-26B-A4B-it, enable_prefix_caching=False, enable_chunked_prefill=True, pooler_config=None, compilation_config={'mode': <CompilationMode.DYNAMO_TRACE_ONCE: 2>, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'openxla', 'custom_ops': ['all'], 'splitting_ops': [], 'compile_mm_encoder': False, 'compile_sizes': None, 'compile_ranges_split_points': [4096], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.NONE: 0>, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {'fuse_norm_quant': True, 'fuse_act_quant': True, 'fuse_attn_quant': False, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse_allreduce_rms': False}, 'max_cudagraph_capture_size': None, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': False, 'assume_32_bit_indexing': False}, 'local_cache_dir': None, 'fast_moe_cold_start': True, 'static_all_moe_layers': []}
(EngineCore_DP0 pid=1356450) WARNING 04-04 21:50:25 [tpu_platform.py:231] Pin memory is not supported on TPU.
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:29 [parallel_state.py:1395] world_size=1 rank=0 local_rank=0 distributed_init_method=file:///tmp/tmpuk8sb45z backend=gloo
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:29 [parallel_state.py:1717] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 0, EP rank 0, EPLB rank N/A
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:30 [tpu_runner.py:302] Init mesh | mesh=Mesh('data': 1, 'model': 4, axis_types=(Auto, Auto))
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:30 [utils.py:94] Prepared token paddings: [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:30 [utils.py:60] Prepared request paddings: [8, 16, 32, 64, 128]
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:30 [compilation_manager.py:52] Enabling JAX compile cache.
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:30 [tpu_worker.py:279] Init worker | rank=0 | is_first_rank=True | is_last_rank=True | topology_order_id=0 | is_driver_worker=True | hbm=[(0.0, 15.75), (0.0, 15.75), (0.0, 15.75), (0.0, 15.75)]GiB |self.devices=[TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), TpuDevice(id=1, process_index=0, coords=(1,0,0), core_on_chip=0), TpuDevice(id=2, process_index=0, coords=(0,1,0), core_on_chip=0), TpuDevice(id=3, process_index=0, coords=(1,1,0), core_on_chip=0)] | total devices=[TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), TpuDevice(id=1, process_index=0, coords=(1,0,0), core_on_chip=0), TpuDevice(id=2, process_index=0, coords=(0,1,0), core_on_chip=0), TpuDevice(id=3, process_index=0, coords=(1,1,0), core_on_chip=0)] | local_devices=[TpuDevice(id=0, process_index=0, coords=(0,0,0), core_on_chip=0), TpuDevice(id=1, process_index=0, coords=(1,0,0), core_on_chip=0), TpuDevice(id=2, process_index=0, coords=(0,1,0), core_on_chip=0), TpuDevice(id=3, process_index=0, coords=(1,1,0), core_on_chip=0)]
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:30 [model_loader.py:381] Loading model with MODEL_IMPL_TYPE=auto
(EngineCore_DP0 pid=1356450) INFO 04-04 21:50:30 [model_loader.py:384] Resolved MODEL_IMPL_TYPE 'auto' to 'flax_nnx'
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111] EngineCore failed to start.
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111] Traceback (most recent call last):
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1085, in run_engine_core
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return func(*args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 843, in __init__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     super().__init__(
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 112, in __init__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return func(*args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/vllm/v1/executor/abstract.py", line 103, in __init__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     self._init_executor()
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/vllm/v1/executor/uniproc_executor.py", line 49, in _init_executor
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     self.driver_worker.load_model()
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/tpu_inference/worker/tpu_worker.py", line 391, in load_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     self.model_runner.load_model()
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/tpu_inference/runner/tpu_runner.py", line 536, in load_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     self.model_fn, self.compute_logits_fn, self.pooler_fn, self.combine_hidden_states_fn, multimodal_fns, self.state, self.lora_manager, self.model = get_model(
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]                                                                                                                                                       ^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/tpu_inference/models/common/model_loader.py", line 398, in get_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return get_flax_model(vllm_config, rng, mesh,
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/tpu_inference/models/common/model_loader.py", line 267, in get_flax_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     jit_model = _get_nnx_model(model_class, vllm_config, rng, mesh)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/tpu_inference/models/common/model_loader.py", line 235, in _get_nnx_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     model.load_weights(rng)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/maxtext_vllm_adapter/adapter.py", line 254, in load_weights
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     model, _ = model_creation_utils.create_nnx_model(
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/utils/model_creation_utils.py", line 246, in create_nnx_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     abstract_model = nnx.eval_shape(_create_model_partial)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/flax/nnx/transforms/transforms.py", line 272, in eval_shape
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     out = jax.eval_shape(_eval_shape_fn, *args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/flax/nnx/transforms/transforms.py", line 269, in _eval_shape_fn
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     out = f_call(*args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]           ^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/utils/model_creation_utils.py", line 241, in _create_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return from_config(config, devices, mesh, rngs=rngs, model_mode=model_mode)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/utils/model_creation_utils.py", line 206, in from_config
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     model = create_model(config, mesh, model_mode=model_mode, rngs=rngs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/utils/model_creation_utils.py", line 224, in create_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     model = get_transformer_model(config, mesh, quant, model_mode=model_mode, rngs=rngs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/utils/model_creation_utils.py", line 215, in get_transformer_model
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return models.Transformer(config, mesh, quant=quant, rngs=rngs, model_mode=model_mode)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/flax/nnx/pytreelib.py", line 400, in __call__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return _graph_node_meta_call(cls, *args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/flax/nnx/pytreelib.py", line 411, in _graph_node_meta_call
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     cls._pytree_meta_construct(node, *args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/flax/nnx/pytreelib.py", line 403, in _pytree_meta_construct
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     self.__init__(*args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/models/models.py", line 372, in __init__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     self.decoder.lazy_init(
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/layers/nnx_wrappers.py", line 220, in lazy_init
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return lazy_init(self, *args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/layers/nnx_wrappers.py", line 162, in lazy_init
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     _set_initializing(module, False)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/layers/nnx_wrappers.py", line 253, in __call__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     out, updates = self.to_nnx__module.init_with_output(_rngs, *args, method=method, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/layers/decoders.py", line 1061, in __call__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     y, returned_cache = layer(
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]                         ^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/layers/nnx_wrappers.py", line 437, in __call__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     out = method_fn(module, *args, **kwargs)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/src/maxtext/models/gemma4.py", line 327, in __call__
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     inputs = nn.with_logical_constraint(inputs, self.activation_axis_names)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/flax/linen/spmd.py", line 259, in with_logical_constraint
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return jax.tree_util.tree_map(
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/flax/linen/spmd.py", line 226, in _with_sharding_constraint_one_fallback
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return _with_sharding_constraint(
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/flax/linen/spmd.py", line 203, in _with_sharding_constraint
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return lax.with_sharding_constraint(x, axis_resources)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/sharding_impls.py", line 1056, in cached_named_sharding
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     return NamedSharding(mesh, pspec, memory_kind=memory_kind)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/named_sharding.py", line 483, in check_pspec
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     _check_mesh_resource_axis(mesh, spec)
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]   File "/home/nmilosev/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/named_sharding.py", line 538, in _check_mesh_resource_axis
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111]     raise ValueError(
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111] ValueError: Resource axis: attn_dp of PartitionSpec('data', None, ('model', 'attn_dp')) is not found in mesh: ('data', 'model').
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111] --------------------
(EngineCore_DP0 pid=1356450) ERROR 04-04 21:50:30 [core.py:1111] For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```
</details>

### Environment Information

TPU v5e (single host, 4 accelerators)
maxtext commit `9777a4cf9574f3d10c591e25450cea1b1dde7e01`

<details>
<summary>Full env</summary>

```
absl-py==2.3.1
aiofiles==25.1.0
aiohappyeyeballs==2.6.1
aiohttp==3.13.3
aiohttp-cors==0.8.1
aiosignal==1.4.0
annotated-doc==0.0.4
annotated-types==0.7.0
anthropic==0.84.0
antlr4-python3-runtime==4.9.3
anyio==4.13.0
aqtp==0.9.0
array-record==0.8.3
astor==0.8.1
astroid==4.0.2
asttokens==3.0.1
astunparse==1.6.3
attrs==25.4.0
auditwheel==6.5.0
black==24.10.0
blake3==1.0.8
blobfile==3.1.0
boto3==1.42.56
botocore==1.42.56
build==1.3.0
cachetools==6.2.2
cbor2==5.8.0
certifi==2026.2.25
cffi==2.0.0
cfgv==3.5.0
charset-normalizer==3.4.4
cheroot==11.1.2
chex==0.1.91
click==8.3.2
cloud-accelerator-diagnostics==0.1.1
cloud-tpu-diagnostics==0.1.5
cloudpickle==3.1.2
clu==0.0.12
cmake==4.2.1
colorama==0.4.6
colorful==0.5.8
comm==0.2.3
compressed-tensors==0.13.0
contourpy==1.3.3
coverage==7.12.0
cryptography==46.0.5
cycler==0.12.1
dacite==1.9.2
dataclasses-json==0.6.7
datasets==4.6.0
debugpy==1.8.20
decorator==5.2.1
depyf==0.20.0
dill==0.4.0
diskcache==5.6.3
distlib==0.4.0
distro==1.9.0
dm-tree==0.1.9
dnspython==2.8.0
docstring-parser==0.17.0
drjax==0.1.4
editdistance==0.8.1
einops==0.8.1
einshape==1.0
email-validator==2.3.0
entrypoints==0.4
etils==1.13.0
evaluate==0.4.6
execnet==2.1.2
executing==2.2.1
fastapi==0.122.0
fastapi-cli==0.0.24
fastapi-cloud-cli==0.13.0
fastar==0.8.0
fastjsonschema==2.21.2
filelock==3.25.2
flatbuffers==25.9.23
flax==0.12.4
fonttools==4.60.1
frozenlist==1.8.0
fsspec==2026.3.0
gast==0.6.0
gcsfs==2026.1.0
gguf==0.17.1
google-api-core==2.28.1
google-api-python-client==2.187.0
google-auth==2.43.0
google-auth-httplib2==0.2.1
google-auth-oauthlib==1.2.2
google-cloud-aiplatform==1.128.0
google-cloud-appengine-logging==1.7.0
google-cloud-audit-log==0.4.0
google-cloud-bigquery==3.38.0
google-cloud-core==2.5.0
google-cloud-logging==3.12.1
google-cloud-mldiagnostics==0.5.10
google-cloud-monitoring==2.28.0
google-cloud-resource-manager==1.15.0
google-cloud-storage==3.9.0
google-cloud-storage-control==1.10.0
google-crc32c==1.7.1
google-genai==1.52.0
google-jetstream @ https://github.com/AI-Hypercomputer/JetStream/archive/29329e8e73820993f77cfc8efe34eb2a73f5de98.zip
google-metrax==0.2.4
google-pasta==0.2.0
google-resumable-media==2.8.0
google-tunix @ https://github.com/google/tunix/archive/336d102fe32ca0edbe42a8f66ff0fd533cebdf52.zip
googleapis-common-protos==1.72.0
grain==0.2.15
grpc-google-iam-v1==0.14.3
grpcio==1.78.0
grpcio-reflection==1.71.0
grpcio-status==1.71.2
gspread==6.2.1
gviz-api==1.10.0
h11==0.16.0
h5py==3.15.1
hf-transfer==0.1.9
hf-xet==1.4.3
httpcore==1.0.9
httplib2==0.31.0
httptools==0.7.1
httpx==0.28.1
httpx-sse==0.4.3
huggingface-hub==1.9.0
humanize==4.14.0
hypothesis==6.142.1
identify==2.6.15
idna==3.11
ijson==3.5.0
immutabledict==4.2.2
importlab==0.8.1
importlib-metadata==8.7.0
importlib-resources==6.5.2
iniconfig==2.3.0
interegular==0.3.3
ipykernel==7.2.0
ipython==9.10.0
ipython-pygments-lexers==1.1.1
ipywidgets==8.1.8
isort==7.0.0
jaraco-classes==3.4.0
jaraco-context==6.1.0
jaraco-functools==4.3.0
jax==0.8.3
jaxlib==0.8.3
jaxtyping==0.3.3
jedi==0.19.2
jeepney==0.9.0
jinja2==3.1.6
jiter==0.13.0
jmespath==1.1.0
joblib==1.5.2
jsonlines==4.0.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
jupyter-client==8.8.0
jupyter-core==5.9.1
jupyterlab-widgets==3.0.16
kagglehub==0.3.13
keras==3.12.0
keyring==25.7.0
keyrings-google-artifactregistry-auth==1.1.2
kiwisolver==1.4.9
lark==1.2.2
latex2sympy2-extended==1.11.0
libclang==18.1.1
libcst==1.8.6
libtpu==0.0.32
llguidance==1.3.0
llvmlite==0.47.0
lm-format-enforcer==0.11.3
loguru==0.7.3
lxml==6.0.2
markdown==3.10
markdown-it-py==4.0.0
markupsafe==3.0.3
marshmallow==3.26.2
math-verify==0.9.0
matplotlib==3.10.7
matplotlib-inline==0.2.1
-e file:///home/nmilosev/maxtext
maxtext-vllm-adapter @ file:///home/nmilosev/maxtext/src/maxtext/integration/vllm
mccabe==0.7.0
mcp==1.26.0
mdurl==0.1.2
mistral-common==1.9.1
ml-collections==1.1.0
ml-dtypes==0.5.4
ml-goodput-measurement==0.0.15
mlperf-logging @ https://github.com/mlcommons/logging/archive/38ab22670527888c8eb7825a4ece176fcc36a95d.zip
model-hosting-container-standards==0.1.13
more-itertools==10.8.0
mpmath==1.3.0
msgpack==1.1.2
msgspec==0.20.0
multidict==6.7.0
multiprocess==0.70.18
mypy-extensions==1.1.0
namex==0.1.0
nbclient==0.10.4
nbformat==5.10.4
nest-asyncio==1.6.0
networkx==3.6
ninja==1.13.0
nixl==0.3.0
nltk==3.9.2
nodeenv==1.9.1
numba==0.65.0
numpy==2.4.4
numpy-typing-compat==20250818.2.2
nvidia-cublas-cu12==12.8.4.1
nvidia-cuda-cupti-cu12==12.8.90
nvidia-cuda-nvrtc-cu12==12.8.93
nvidia-cuda-runtime-cu12==12.8.90
nvidia-cudnn-cu12==9.10.2.21
nvidia-cufft-cu12==11.3.3.83
nvidia-cufile-cu12==1.13.1.3
nvidia-curand-cu12==10.3.9.90
nvidia-cusolver-cu12==11.7.3.90
nvidia-cusparse-cu12==12.5.8.93
nvidia-cusparselt-cu12==0.7.1
nvidia-nccl-cu12==2.27.5
nvidia-nvjitlink-cu12==12.8.93
nvidia-nvshmem-cu12==3.3.20
nvidia-nvtx-cu12==12.8.90
oauthlib==3.3.1
omegaconf==2.3.0
openai==2.24.0
openai-harmony==0.0.8
opencensus==0.11.4
opencensus-context==0.1.3
opencv-python-headless==4.13.0.92
opentelemetry-api==1.39.1
opentelemetry-exporter-otlp==1.39.1
opentelemetry-exporter-otlp-proto-common==1.39.1
opentelemetry-exporter-otlp-proto-grpc==1.39.1
opentelemetry-exporter-otlp-proto-http==1.39.1
opentelemetry-exporter-prometheus==0.60b1
opentelemetry-proto==1.39.1
opentelemetry-sdk==1.39.1
opentelemetry-semantic-conventions==0.60b1
opentelemetry-semantic-conventions-ai==0.4.15
opt-einsum==3.4.0
optax==0.2.6
optree==0.18.0
optype==0.14.0
orbax-checkpoint==0.11.28
orbax-export==0.0.8
outlines-core==0.2.11
packaging==26.0
pandas==2.3.3
papermill==2.7.0
parameterized==0.9.0
parso==0.8.6
partial-json-parser==0.2.1.1.post7
pathspec==0.12.1
pathwaysutils==0.1.4
perfetto==0.16.0
pexpect==4.9.0
pillow==12.0.0
pip==26.0.1
platformdirs==4.9.2
pluggy==1.6.0
portpicker==1.6.0
pre-commit==4.5.0
prometheus-client==0.23.1
prometheus-fastapi-instrumentator==7.1.0
promise==2.3
prompt-toolkit==3.0.52
propcache==0.4.1
proto-plus==1.26.1
protobuf==5.29.6
psutil==7.2.2
ptyprocess==0.7.0
pure-eval==0.2.3
py-cpuinfo==9.0.0
py-spy==0.4.1
pyarrow==22.0.0
pyasn1==0.6.1
pyasn1-modules==0.4.2
pybase64==1.4.3
pycnite==2024.7.31
pycountry==26.2.16
pycparser==3.0
pycryptodomex==3.23.0
pydantic==2.12.5
pydantic-core==2.41.5
pydantic-extra-types==2.11.0
pydantic-settings==2.13.1
pydot==4.0.1
pyelftools==0.32
pyglove==0.4.5
pygments==2.20.0
pyink==24.10.1
pyjwt==2.11.0
pylatexenc==2.10
pylint==4.0.3
pyparsing==3.2.5
pyproject-hooks==1.2.0
pytest==8.4.2
pytest-mock==3.15.1
pytest-xdist==3.8.0
python-dateutil==2.9.0.post0
python-dotenv==1.2.1
python-json-logger==4.0.0
python-multipart==0.0.22
pytype==2024.10.11
pytz==2025.2
pyyaml==6.0.3
pyzmq==27.1.0
qwix==0.1.4
ray==2.54.0
referencing==0.37.0
regex==2026.4.4
requests==2.32.5
requests-oauthlib==2.0.0
rich==14.3.3
rich-toolkit==0.19.7
rignore==0.7.6
rpds-py==0.30.0
rsa==4.9.1
runai-model-streamer==0.15.4
runai-model-streamer-gcs==0.15.4
runai-model-streamer-s3==0.15.4
s3transfer==0.16.0
safetensors==0.7.0
scipy==1.16.3
scipy-stubs==1.16.3.0
secretstorage==3.5.0
sentencepiece==0.2.1
sentry-sdk==2.53.0
seqio==0.0.20
setproctitle==1.3.7
setuptools==78.1.0
setuptools-scm==9.2.2
shapely==2.1.2
shellingham==1.5.4
shortuuid==1.0.13
simple-parsing==0.1.7
simplejson==3.20.2
six==1.17.0
smart-open==7.5.1
sniffio==1.3.1
sortedcontainers==2.4.0
sse-starlette==3.2.0
stack-data==0.6.3
starlette==0.50.0
supervisor==4.3.0
sympy==1.14.0
tabulate==0.9.0
tenacity==9.1.4
tensorboard==2.20.0
tensorboard-data-server==0.7.2
tensorboard-plugin-profile==2.13.0
tensorboardx==2.6.4
tensorflow==2.20.0
tensorflow-datasets==4.9.9
tensorflow-metadata==1.17.2
tensorflow-text==2.20.0
tensorstore==0.1.79
termcolor==3.2.0
tiktoken==0.12.0
tokamax==0.0.8
tokenizers==0.22.2
toml==0.10.2
tomlkit==0.13.3
toolz==1.1.0
torch==2.9.0
torchax==0.0.11
torchvision==0.24.0
tornado==6.5.4
tpu-inference @ https://github.com/vllm-project/tpu-inference/archive/0cae84fc9a883ba1bde02d4f07930e6af9e92958.zip
tpu-info==0.7.1
tqdm==4.67.3
traitlets==5.14.3
transformers==5.5.0
treescope==0.1.10
triton==3.5.0
typeguard==2.13.3
typer==0.24.1
typing-extensions==4.15.0
typing-inspect==0.9.0
typing-inspection==0.4.2
tzdata==2025.2
uritemplate==4.2.0
urllib3==2.5.0
uv==0.10.6
uvicorn==0.38.0
uvloop==0.22.1
virtualenv==20.35.4
vllm @ git+https://github.com/vllm-project/vllm@ee8a29511fc69e3f0f6291fa6ff1cf6e47f7750d
wadler-lindig==0.1.7
watchfiles==1.1.1
wcwidth==0.6.0
websockets==15.0.1
werkzeug==3.1.3
wheel==0.46.3
widgetsnbextension==4.0.15
wrapt==2.0.1
xgrammar==0.1.29
xprof==2.21.1
xxhash==3.6.0
yapf==0.43.0
yarl==1.22.0
zipp==3.23.0
zstandard==0.25.0
```
</details>

### Additional Context

_No response_

## 评论 (2)

### NicoGrande · 2026-04-06

Hi @nmilosev - could you try appending `NEW_MODEL_DESIGN=1` to your vLLM serve command? 

tpu-inference initializes a 2D mesh (containing only `model` and `data` physical axes) unless this enviornonment variable is set. If you are interested, this is the relevant mesh creation logic: https://github.com/vllm-project/tpu-inference/blob/ca1f5bb41e529b98be8411ce492a6611180d611d/tpu_inference/layers/common/sharding.py#L74-L97

### NicoGrande · 2026-04-28

Closing issue for now! Please feel free to re-open if you have more questions @nmilosev !
