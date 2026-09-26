# [Issue #1349] PaddleOCR-vl sft后无法vllm部署

source: https://github.com/PaddlePaddle/ERNIE/issues/1349
state: open | updated: 2026-01-09T08:08:35Z
labels: 

## 正文

(APIServer pid=76722) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=76722) INFO 11-09 08:49:56 [model.py:547] Resolved architecture: PaddleOCRVLForConditionalGeneration
(APIServer pid=76722) INFO 11-09 08:49:56 [model.py:1510] Using max model len 16384
(APIServer pid=76722) INFO 11-09 08:49:56 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=131072.
(APIServer pid=76722) Traceback (most recent call last):
(APIServer pid=76722)   File "/usr/local/bin/paddlex_genai_server", line 8, in <module>
(APIServer pid=76722)     sys.exit(main())
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/genai/server.py", line 113, in main
(APIServer pid=76722)     run_genai_server(args)
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/genai/server.py", line 100, in run_genai_server
(APIServer pid=76722)     run_server_func(
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/genai/backends/vllm.py", line 68, in run_vllm_server
(APIServer pid=76722)     uvloop.run(run_server(args))
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/uvloop/__init__.py", line 69, in run
(APIServer pid=76722)     return loop.run_until_complete(wrapper())
(APIServer pid=76722)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=76722)     return await main
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=76722)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=76722)     async with build_async_engine_client(
(APIServer pid=76722)   File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=76722)     return await anext(self.gen)
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=76722)     async with build_async_engine_client_from_engine_args(
(APIServer pid=76722)   File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=76722)     return await anext(self.gen)
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
(APIServer pid=76722)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/utils/__init__.py", line 1572, in inner
(APIServer pid=76722)     return fn(*args, **kwargs)
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
(APIServer pid=76722)     return cls(
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/async_llm.py", line 114, in __init__
(APIServer pid=76722)     self.tokenizer = init_tokenizer_from_configs(
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/transformers_utils/tokenizer.py", line 286, in init_tokenizer_from_configs
(APIServer pid=76722)     return get_tokenizer(
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/transformers_utils/tokenizer.py", line 238, in get_tokenizer
(APIServer pid=76722)     raise e
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/vllm/transformers_utils/tokenizer.py", line 217, in get_tokenizer
(APIServer pid=76722)     tokenizer = AutoTokenizer.from_pretrained(
(APIServer pid=76722)   File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/tokenization_auto.py", line 1113, in from_pretrained
(APIServer pid=76722)     raise ValueError(
(APIServer pid=76722) ValueError: Tokenizer class Ernie4_5_Tokenizer does not exist or is not currently imported.


使用文心组件微调后，产出的tokenizer_config.py中tokenizer_class:"Ernie4_5_Tokenizer"
然后通过vllm部署启动，就报上面的错误，Ernie4_5_Tokenizer这个class是在ERNIE里的，检查了ERNIE是正常流程安装的。

## 评论 (20)

### forBlank · 2025-11-13

@1053234381 Hi, please try updating VLLM to the latest commit.

### 1053234381 · 2025-11-13

这是来自QQ邮箱的假期自动回复邮件。已收到邮件，谢谢！

### 1053234381 · 2025-11-27

这是来自QQ邮箱的假期自动回复邮件。已收到邮件，谢谢！

### lixingxing1231 · 2025-11-27

> [@1053234381](https://github.com/1053234381) Hi, please try updating VLLM to the latest commit.

已经升级到vllm0.11.2还是报同样的错误

### forBlank · 2025-11-27

@lixingxing1231 @1053234381 可以尝试将 tokenizer_config.json 里的 "tokenizer_class" 字段从 "Ernie4_5_Tokenizer" 改成 "LlamaTokenizer"

### lixingxing1231 · 2025-11-27

> [@lixingxing1231](https://github.com/lixingxing1231) [@1053234381](https://github.com/1053234381) 可以尝试将 tokenizer_config.json 里的 "tokenizer_class" 字段从 "Ernie4_5_Tokenizer" 改成 "LlamaTokenizer"

EngineCore failed to start.
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] Traceback (most recent call last):
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 82, in __init__
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; self._init_executor()
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 48, in _init_executor
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; self.collective_rpc("init_device")
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/utils/__init__.py", line 3060, in run_method
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return func(*args, **kwargs)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 611, in init_device
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; self.worker.init_device() &nbsp;# type: ignore
(EngineCore_DP0 pid=142) Process EngineCore_DP0:
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/worker/gpu_worker.py", line 201, in init_device
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; self.model_runner: GPUModelRunner = GPUModelRunner(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 383, in __init__
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; self.mm_budget = MultiModalBudget(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/worker/utils.py", line 47, in __init__
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; max_tokens_by_modality = mm_registry \
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/registry.py", line 168, in get_max_tokens_per_item_by_nonzero_modality
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; max_tokens_per_item = self.get_max_tokens_per_item_by_modality(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/registry.py", line 144, in get_max_tokens_per_item_by_modality
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return profiler.get_mm_max_contiguous_tokens(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 311, in get_mm_max_contiguous_tokens
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return self._get_mm_max_tokens(seq_len,
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 291, in _get_mm_max_tokens
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 170, in _get_dummy_mm_inputs
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; processor_inputs = factory.get_dummy_processor_inputs(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 92, in get_dummy_processor_inputs
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; dummy_text = self.get_dummy_text(mm_counts)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/models/paddleocr_vl_09b/_vllm.py", line 196, in get_dummy_text
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; processor = self.info.get_hf_processor()
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/models/paddleocr_vl_09b/_vllm.py", line 137, in get_hf_processor
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return self.ctx.get_hf_processor(**kwargs)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/inputs/registry.py", line 138, in get_hf_processor
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return super().get_hf_processor(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/inputs/registry.py", line 101, in get_hf_processor
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return cached_processor_from_config(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/transformers_utils/processor.py", line 143, in cached_processor_from_config
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return cached_get_processor(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/transformers_utils/processor.py", line 94, in get_processor
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; processor = AutoProcessor.from_pretrained(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/transformers/models/auto/processing_auto.py", line 387, in from_pretrained
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; processor_class = get_class_from_dynamic_module(
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 616, in get_class_from_dynamic_module
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return get_class_in_module(class_name, final_module, force_reload=force_download)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; File "/usr/local/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 313, in get_class_in_module
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] &nbsp; &nbsp; return getattr(module, class_name)
(EngineCore_DP0 pid=142) ERROR 11-27 07:15:17 [core.py:718] AttributeError: module 'transformers_modules.PaddleOCR_hyphen_VL_hyphen_SFT_hyphen_Bengali.processing_ppocrvl' has no attribute 'PPOCRVLProcessor'. Did you mean: 'PaddleOCRVLProcessor'?
(EngineCore_DP0 pid=142) Traceback (most recent call last):
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.run()
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 722, in run_engine_core
(EngineCore_DP0 pid=142) &nbsp; &nbsp; raise e
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=142) &nbsp; &nbsp; engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=142) &nbsp; &nbsp; super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 82, in __init__
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self._init_executor()
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 48, in _init_executor
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.collective_rpc("init_device")
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_DP0 pid=142) &nbsp; &nbsp; answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/utils/__init__.py", line 3060, in run_method
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return func(*args, **kwargs)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 611, in init_device
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.worker.init_device() &nbsp;# type: ignore
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/worker/gpu_worker.py", line 201, in init_device
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.model_runner: GPUModelRunner = GPUModelRunner(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 383, in __init__
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.mm_budget = MultiModalBudget(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/worker/utils.py", line 47, in __init__
(EngineCore_DP0 pid=142) &nbsp; &nbsp; max_tokens_by_modality = mm_registry \
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/registry.py", line 168, in get_max_tokens_per_item_by_nonzero_modality
(EngineCore_DP0 pid=142) &nbsp; &nbsp; max_tokens_per_item = self.get_max_tokens_per_item_by_modality(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/registry.py", line 144, in get_max_tokens_per_item_by_modality
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return profiler.get_mm_max_contiguous_tokens(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 311, in get_mm_max_contiguous_tokens
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return self._get_mm_max_tokens(seq_len,
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 291, in _get_mm_max_tokens
(EngineCore_DP0 pid=142) &nbsp; &nbsp; mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 170, in _get_dummy_mm_inputs
(EngineCore_DP0 pid=142) &nbsp; &nbsp; processor_inputs = factory.get_dummy_processor_inputs(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 92, in get_dummy_processor_inputs
(EngineCore_DP0 pid=142) &nbsp; &nbsp; dummy_text = self.get_dummy_text(mm_counts)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/models/paddleocr_vl_09b/_vllm.py", line 196, in get_dummy_text
(EngineCore_DP0 pid=142) &nbsp; &nbsp; processor = self.info.get_hf_processor()
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/models/paddleocr_vl_09b/_vllm.py", line 137, in get_hf_processor
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return self.ctx.get_hf_processor(**kwargs)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/inputs/registry.py", line 138, in get_hf_processor
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return super().get_hf_processor(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/inputs/registry.py", line 101, in get_hf_processor
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return cached_processor_from_config(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/transformers_utils/processor.py", line 143, in cached_processor_from_config
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return cached_get_processor(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/transformers_utils/processor.py", line 94, in get_processor
(EngineCore_DP0 pid=142) &nbsp; &nbsp; processor = AutoProcessor.from_pretrained(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/transformers/models/auto/processing_auto.py", line 387, in from_pretrained
(EngineCore_DP0 pid=142) &nbsp; &nbsp; processor_class = get_class_from_dynamic_module(
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 616, in get_class_from_dynamic_module
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return get_class_in_module(class_name, final_module, force_reload=force_download)
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 313, in get_class_in_module
(EngineCore_DP0 pid=142) &nbsp; &nbsp; return getattr(module, class_name)
(EngineCore_DP0 pid=142) AttributeError: module 'transformers_modules.PaddleOCR_hyphen_VL_hyphen_SFT_hyphen_Bengali.processing_ppocrvl' has no attribute 'PPOCRVLProcessor'. Did you mean: 'PaddleOCRVLProcessor'?
(EngineCore_DP0 pid=142) Exception ignored in: <function ExecutorBase.__del__ at 0x7f8e12d3f6d0&gt;
(EngineCore_DP0 pid=142) Traceback (most recent call last):
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 237, in __del__
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.shutdown()
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 76, in shutdown
(EngineCore_DP0 pid=142) &nbsp; &nbsp; worker.shutdown()
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 528, in shutdown
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.worker.shutdown()
(EngineCore_DP0 pid=142) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/worker/gpu_worker.py", line 675, in shutdown
(EngineCore_DP0 pid=142) &nbsp; &nbsp; self.model_runner.ensure_kv_transfer_shutdown()
(EngineCore_DP0 pid=142) AttributeError: 'NoneType' object has no attribute 'ensure_kv_transfer_shutdown'
[rank0]:[W1127 07:15:18.393856138 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
(APIServer pid=1) Traceback (most recent call last):
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/runpy.py", line 196, in _run_module_as_main
(APIServer pid=1) &nbsp; &nbsp; return _run_code(code, main_globals, None,
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/runpy.py", line 86, in _run_code
(APIServer pid=1) &nbsp; &nbsp; exec(code, run_globals)
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/server.py", line 117, in <module&gt;
(APIServer pid=1) &nbsp; &nbsp; main()
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/server.py", line 113, in main
(APIServer pid=1) &nbsp; &nbsp; run_genai_server(args)
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/server.py", line 100, in run_genai_server
(APIServer pid=1) &nbsp; &nbsp; run_server_func(
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/backends/vllm.py", line 68, in run_vllm_server
(APIServer pid=1) &nbsp; &nbsp; uvloop.run(run_server(args))
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/uvloop/__init__.py", line 69, in run
(APIServer pid=1) &nbsp; &nbsp; return loop.run_until_complete(wrapper())
(APIServer pid=1) &nbsp; File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=1) &nbsp; &nbsp; return await main
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1941, in run_server
(APIServer pid=1) &nbsp; &nbsp; await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1961, in run_server_worker
(APIServer pid=1) &nbsp; &nbsp; async with build_async_engine_client(
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=1) &nbsp; &nbsp; return await anext(self.gen)
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 179, in build_async_engine_client
(APIServer pid=1) &nbsp; &nbsp; async with build_async_engine_client_from_engine_args(
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=1) &nbsp; &nbsp; return await anext(self.gen)
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 221, in build_async_engine_client_from_engine_args
(APIServer pid=1) &nbsp; &nbsp; async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/utils/__init__.py", line 1589, in inner
(APIServer pid=1) &nbsp; &nbsp; return fn(*args, **kwargs)
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 212, in from_vllm_config
(APIServer pid=1) &nbsp; &nbsp; return cls(
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 136, in __init__
(APIServer pid=1) &nbsp; &nbsp; self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=1) &nbsp; &nbsp; return AsyncMPClient(*client_args)
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=1) &nbsp; &nbsp; super().__init__(
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=1) &nbsp; &nbsp; with launch_core_engines(vllm_config, executor_class,
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/contextlib.py", line 142, in __exit__
(APIServer pid=1) &nbsp; &nbsp; next(self.gen)
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/utils.py", line 729, in launch_core_engines
(APIServer pid=1) &nbsp; &nbsp; wait_for_engine_startup(
(APIServer pid=1) &nbsp; File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/utils.py", line 782, in wait_for_engine_startup
(APIServer pid=1) &nbsp; &nbsp; raise RuntimeError("Engine core initialization failed. "
(APIServer pid=1) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}


### xiyangyang99 · 2025-11-28

**I also encountered the same problem, and the output log after startup is as follows:**


(myenv) bowen@bowen-HP-Z6-G5-Workstation-Desktop-PC:/media/bowen/data/cor$ paddleocr genai_server --model_name PaddleOCR-VL-0.9B  --model_dir /home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali   --backend vllm --port 8118
/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:718: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
INFO 11-28 09:52:16 [__init__.py:216] Automatically detected platform cuda.
(APIServer pid=1022831) INFO 11-28 09:52:18 [api_server.py:1896] vLLM API server version 0.10.2
(APIServer pid=1022831) INFO 11-28 09:52:18 [utils.py:328] non-default args: {'api_server_count': 4, 'host': 'localhost', 'port': 8118, 'chat_template': '/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/chat_templates/PaddleOCR-VL-0.9B.jinja', 'model': '/home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali', 'trust_remote_code': True, 'max_model_len': 16384, 'served_model_name': ['PaddleOCR-VL-0.9B'], 'gpu_memory_utilization': 0.5, 'max_num_batched_tokens': 131072}
(APIServer pid=1022831) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=1022831) INFO 11-28 09:52:21 [__init__.py:742] Resolved architecture: PaddleOCRVLForConditionalGeneration
(APIServer pid=1022831) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=1022831) INFO 11-28 09:52:21 [__init__.py:1815] Using max model len 16384
(APIServer pid=1022831) INFO 11-28 09:52:21 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=131072.
(APIServer pid=1022831) Traceback (most recent call last):
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/bin/paddleocr", line 8, in <module>
(APIServer pid=1022831)     sys.exit(console_entry())
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddleocr/__main__.py", line 26, in console_entry
(APIServer pid=1022831)     main()
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddleocr/_cli.py", line 194, in main
(APIServer pid=1022831)     _execute(args)
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddleocr/_cli.py", line 183, in _execute
(APIServer pid=1022831)     args.executor(args)
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddleocr/_cli.py", line 157, in _run_genai_server
(APIServer pid=1022831)     run_genai_server(args)
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/server.py", line 100, in run_genai_server
(APIServer pid=1022831)     run_server_func(
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/backends/vllm.py", line 79, in run_vllm_server
(APIServer pid=1022831)     uvloop.run(run_server(args))
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/uvloop/__init__.py", line 69, in run
(APIServer pid=1022831)     return loop.run_until_complete(wrapper())
(APIServer pid=1022831)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=1022831)     return await main
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1941, in run_server
(APIServer pid=1022831)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1961, in run_server_worker
(APIServer pid=1022831)     async with build_async_engine_client(
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=1022831)     return await anext(self.gen)
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 179, in build_async_engine_client
(APIServer pid=1022831)     async with build_async_engine_client_from_engine_args(
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=1022831)     return await anext(self.gen)
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 221, in build_async_engine_client_from_engine_args
(APIServer pid=1022831)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/utils/__init__.py", line 1589, in inner
(APIServer pid=1022831)     return fn(*args, **kwargs)
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 212, in from_vllm_config
(APIServer pid=1022831)     return cls(
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 114, in __init__
(APIServer pid=1022831)     self.tokenizer = init_tokenizer_from_configs(
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/transformers_utils/tokenizer_group.py", line 123, in init_tokenizer_from_configs
(APIServer pid=1022831)     return TokenizerGroup(
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/transformers_utils/tokenizer_group.py", line 28, in __init__
(APIServer pid=1022831)     self.tokenizer = get_tokenizer(self.tokenizer_id, **tokenizer_config)
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/transformers_utils/tokenizer.py", line 238, in get_tokenizer
(APIServer pid=1022831)     raise e
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/transformers_utils/tokenizer.py", line 217, in get_tokenizer
(APIServer pid=1022831)     tokenizer = AutoTokenizer.from_pretrained(
(APIServer pid=1022831)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/models/auto/tokenization_auto.py", line 1137, in from_pretrained
(APIServer pid=1022831)     raise ValueError(
(APIServer pid=1022831) ValueError: Tokenizer class Ernie4_5_Tokenizer does not exist or is not currently imported.


### xiyangyang99 · 2025-11-28

> LlamaTokenizer

After I changed it to “LlamaTokenizer”, the output log is as follows：
(myenv) bowen@bowen-HP-Z6-G5-Workstation-Desktop-PC:/media/bowen/data/cor$ paddleocr genai_server --model_name PaddleOCR-VL-0.9B  --model_dir /home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali   --backend vllm --port 8118
/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:718: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
INFO 11-28 10:01:25 [__init__.py:216] Automatically detected platform cuda.
(APIServer pid=1027688) INFO 11-28 10:01:28 [api_server.py:1896] vLLM API server version 0.10.2
(APIServer pid=1027688) INFO 11-28 10:01:28 [utils.py:328] non-default args: {'api_server_count': 4, 'host': 'localhost', 'port': 8118, 'chat_template': '/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/chat_templates/PaddleOCR-VL-0.9B.jinja', 'model': '/home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali', 'trust_remote_code': True, 'max_model_len': 16384, 'served_model_name': ['PaddleOCR-VL-0.9B'], 'gpu_memory_utilization': 0.5, 'max_num_batched_tokens': 131072}
(APIServer pid=1027688) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=1027688) INFO 11-28 10:01:30 [__init__.py:742] Resolved architecture: PaddleOCRVLForConditionalGeneration
(APIServer pid=1027688) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=1027688) INFO 11-28 10:01:30 [__init__.py:1815] Using max model len 16384
(APIServer pid=1027688) INFO 11-28 10:01:30 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=131072.
INFO 11-28 10:01:37 [__init__.py:216] Automatically detected platform cuda.
(EngineCore_DP0 pid=1027883) INFO 11-28 10:01:39 [core.py:654] Waiting for init message from front-end.
(EngineCore_DP0 pid=1027883) /home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:718: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
(EngineCore_DP0 pid=1027883)   warnings.warn(warning_message)
(EngineCore_DP0 pid=1027883) INFO 11-28 10:01:43 [core.py:76] Initializing a V1 LLM engine (v0.10.2) with config: model='/home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali', speculative_config=None, tokenizer='/home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=PaddleOCR-VL-0.9B, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention"],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null}
[W1128 10:01:43.391892407 ProcessGroupNCCL.cpp:981] Warning: TORCH_NCCL_AVOID_RECORD_STREAMS is the default now, this environment variable is thus deprecated. (function operator())
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
(EngineCore_DP0 pid=1027883) INFO 11-28 10:01:43 [parallel_state.py:1165] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=1027883) WARNING 11-28 10:01:44 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer.
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718] EngineCore failed to start.
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718] Traceback (most recent call last):
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 82, in __init__
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     self._init_executor()
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 48, in _init_executor
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     self.collective_rpc("init_device")
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/utils/__init__.py", line 3060, in run_method
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     return func(*args, **kwargs)
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 611, in init_device
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     self.worker.init_device()  # type: ignore
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/worker/gpu_worker.py", line 201, in init_device
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     self.model_runner: GPUModelRunner = GPUModelRunner(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 383, in __init__
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     self.mm_budget = MultiModalBudget(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/worker/utils.py", line 47, in __init__
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     max_tokens_by_modality = mm_registry \
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/registry.py", line 168, in get_max_tokens_per_item_by_nonzero_modality
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     max_tokens_per_item = self.get_max_tokens_per_item_by_modality(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/registry.py", line 144, in get_max_tokens_per_item_by_modality
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     return profiler.get_mm_max_contiguous_tokens(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 311, in get_mm_max_contiguous_tokens
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     return self._get_mm_max_tokens(seq_len,
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 291, in _get_mm_max_tokens
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 170, in _get_dummy_mm_inputs
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     processor_inputs = factory.get_dummy_processor_inputs(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 92, in get_dummy_processor_inputs
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     dummy_text = self.get_dummy_text(mm_counts)
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/models/paddleocr_vl_09b/_vllm.py", line 196, in get_dummy_text
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     processor = self.info.get_hf_processor()
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/models/paddleocr_vl_09b/_vllm.py", line 137, in get_hf_processor
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     return self.ctx.get_hf_processor(**kwargs)
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/inputs/registry.py", line 138, in get_hf_processor
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     return super().get_hf_processor(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/inputs/registry.py", line 101, in get_hf_processor
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     return cached_processor_from_config(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/transformers_utils/processor.py", line 143, in cached_processor_from_config
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     return cached_get_processor(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/transformers_utils/processor.py", line 94, in get_processor
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     processor = AutoProcessor.from_pretrained(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/models/auto/processing_auto.py", line 387, in from_pretrained
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     processor_class = get_class_from_dynamic_module(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 604, in get_class_from_dynamic_module
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     final_module = get_cached_module_file(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 406, in get_cached_module_file
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     resolved_module_file = cached_file(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/utils/hub.py", line 322, in cached_file
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     file = cached_files(path_or_repo_id=path_or_repo_id, filenames=[filename], **kwargs)
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/utils/hub.py", line 437, in cached_files
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718]     raise OSError(
(EngineCore_DP0 pid=1027883) ERROR 11-28 10:01:45 [core.py:718] OSError: /home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali does not appear to have a file named processing_ppocrvl.py. Checkout 'https://huggingface.co//home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali/tree/main' for available files.
(EngineCore_DP0 pid=1027883) Process EngineCore_DP0:
(EngineCore_DP0 pid=1027883) Traceback (most recent call last):
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=1027883)     self.run()
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=1027883)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 722, in run_engine_core
(EngineCore_DP0 pid=1027883)     raise e
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=1027883)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=1027883)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 82, in __init__
(EngineCore_DP0 pid=1027883)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=1027883)     self._init_executor()
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 48, in _init_executor
(EngineCore_DP0 pid=1027883)     self.collective_rpc("init_device")
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_DP0 pid=1027883)     answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/utils/__init__.py", line 3060, in run_method
(EngineCore_DP0 pid=1027883)     return func(*args, **kwargs)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 611, in init_device
(EngineCore_DP0 pid=1027883)     self.worker.init_device()  # type: ignore
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/worker/gpu_worker.py", line 201, in init_device
(EngineCore_DP0 pid=1027883)     self.model_runner: GPUModelRunner = GPUModelRunner(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 383, in __init__
(EngineCore_DP0 pid=1027883)     self.mm_budget = MultiModalBudget(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/worker/utils.py", line 47, in __init__
(EngineCore_DP0 pid=1027883)     max_tokens_by_modality = mm_registry \
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/registry.py", line 168, in get_max_tokens_per_item_by_nonzero_modality
(EngineCore_DP0 pid=1027883)     max_tokens_per_item = self.get_max_tokens_per_item_by_modality(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/registry.py", line 144, in get_max_tokens_per_item_by_modality
(EngineCore_DP0 pid=1027883)     return profiler.get_mm_max_contiguous_tokens(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 311, in get_mm_max_contiguous_tokens
(EngineCore_DP0 pid=1027883)     return self._get_mm_max_tokens(seq_len,
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 291, in _get_mm_max_tokens
(EngineCore_DP0 pid=1027883)     mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 170, in _get_dummy_mm_inputs
(EngineCore_DP0 pid=1027883)     processor_inputs = factory.get_dummy_processor_inputs(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/multimodal/profiling.py", line 92, in get_dummy_processor_inputs
(EngineCore_DP0 pid=1027883)     dummy_text = self.get_dummy_text(mm_counts)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/models/paddleocr_vl_09b/_vllm.py", line 196, in get_dummy_text
(EngineCore_DP0 pid=1027883)     processor = self.info.get_hf_processor()
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/models/paddleocr_vl_09b/_vllm.py", line 137, in get_hf_processor
(EngineCore_DP0 pid=1027883)     return self.ctx.get_hf_processor(**kwargs)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/inputs/registry.py", line 138, in get_hf_processor
(EngineCore_DP0 pid=1027883)     return super().get_hf_processor(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/inputs/registry.py", line 101, in get_hf_processor
(EngineCore_DP0 pid=1027883)     return cached_processor_from_config(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/transformers_utils/processor.py", line 143, in cached_processor_from_config
(EngineCore_DP0 pid=1027883)     return cached_get_processor(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/transformers_utils/processor.py", line 94, in get_processor
(EngineCore_DP0 pid=1027883)     processor = AutoProcessor.from_pretrained(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/models/auto/processing_auto.py", line 387, in from_pretrained
(EngineCore_DP0 pid=1027883)     processor_class = get_class_from_dynamic_module(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 604, in get_class_from_dynamic_module
(EngineCore_DP0 pid=1027883)     final_module = get_cached_module_file(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 406, in get_cached_module_file
(EngineCore_DP0 pid=1027883)     resolved_module_file = cached_file(
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/utils/hub.py", line 322, in cached_file
(EngineCore_DP0 pid=1027883)     file = cached_files(path_or_repo_id=path_or_repo_id, filenames=[filename], **kwargs)
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/transformers/utils/hub.py", line 437, in cached_files
(EngineCore_DP0 pid=1027883)     raise OSError(
(EngineCore_DP0 pid=1027883) OSError: /home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali does not appear to have a file named processing_ppocrvl.py. Checkout 'https://huggingface.co//home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali/tree/main' for available files.
(EngineCore_DP0 pid=1027883) Exception ignored in: <function ExecutorBase.__del__ at 0x7f869a231870>
(EngineCore_DP0 pid=1027883) Traceback (most recent call last):
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 237, in __del__
(EngineCore_DP0 pid=1027883)     self.shutdown()
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 76, in shutdown
(EngineCore_DP0 pid=1027883)     worker.shutdown()
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 528, in shutdown
(EngineCore_DP0 pid=1027883)     self.worker.shutdown()
(EngineCore_DP0 pid=1027883)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/worker/gpu_worker.py", line 675, in shutdown
(EngineCore_DP0 pid=1027883)     self.model_runner.ensure_kv_transfer_shutdown()
(EngineCore_DP0 pid=1027883) AttributeError: 'NoneType' object has no attribute 'ensure_kv_transfer_shutdown'
[rank0]:[W1128 10:01:46.660106714 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
(APIServer pid=1027688) Traceback (most recent call last):
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/bin/paddleocr", line 8, in <module>
(APIServer pid=1027688)     sys.exit(console_entry())
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddleocr/__main__.py", line 26, in console_entry
(APIServer pid=1027688)     main()
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddleocr/_cli.py", line 194, in main
(APIServer pid=1027688)     _execute(args)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddleocr/_cli.py", line 183, in _execute
(APIServer pid=1027688)     args.executor(args)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddleocr/_cli.py", line 157, in _run_genai_server
(APIServer pid=1027688)     run_genai_server(args)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/server.py", line 100, in run_genai_server
(APIServer pid=1027688)     run_server_func(
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/paddlex/inference/genai/backends/vllm.py", line 79, in run_vllm_server
(APIServer pid=1027688)     uvloop.run(run_server(args))
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/uvloop/__init__.py", line 69, in run
(APIServer pid=1027688)     return loop.run_until_complete(wrapper())
(APIServer pid=1027688)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=1027688)     return await main
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1941, in run_server
(APIServer pid=1027688)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1961, in run_server_worker
(APIServer pid=1027688)     async with build_async_engine_client(
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=1027688)     return await anext(self.gen)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 179, in build_async_engine_client
(APIServer pid=1027688)     async with build_async_engine_client_from_engine_args(
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=1027688)     return await anext(self.gen)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 221, in build_async_engine_client_from_engine_args
(APIServer pid=1027688)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/utils/__init__.py", line 1589, in inner
(APIServer pid=1027688)     return fn(*args, **kwargs)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 212, in from_vllm_config
(APIServer pid=1027688)     return cls(
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 136, in __init__
(APIServer pid=1027688)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=1027688)     return AsyncMPClient(*client_args)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=1027688)     super().__init__(
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=1027688)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/contextlib.py", line 142, in __exit__
(APIServer pid=1027688)     next(self.gen)
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/utils.py", line 729, in launch_core_engines
(APIServer pid=1027688)     wait_for_engine_startup(
(APIServer pid=1027688)   File "/home/bowen/miniforge3/envs/myenv/lib/python3.10/site-packages/vllm/v1/engine/utils.py", line 782, in wait_for_engine_startup
(APIServer pid=1027688)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=1027688) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}


### forBlank · 2025-11-28

@lixingxing1231 @xiyangyang99 The issue is likely due to file renaming during updates, which causes the `Auto` class to fail when loading the processor. Please try the following:
1. Download the **latest version** of PaddleOCR-VL from **Hugging Face**.
2. Locate your **SFT-trained .safetensors** weights.
3. **Replace** the .safetensors file in the newly downloaded repository with your trained weights (this avoids the need for retraining).
4. Retry running inference with vllm based on this updated repository.

### xiyangyang99 · 2025-11-28

> [@lixingxing1231](https://github.com/lixingxing1231) [@xiyangyang99](https://github.com/xiyangyang99) The issue is likely due to file renaming during updates, which causes the `Auto` class to fail when loading the processor. Please try the following:
> 
>     1. Download the **latest version** of PaddleOCR-VL from **Hugging Face**.
> 
>     2. Locate your **SFT-trained .safetensors** weights.
> 
>     3. **Replace** the .safetensors file in the newly downloaded repository with your trained weights (this avoids the need for retraining).
> 
>     4. Retry running inference with vllm based on this updated repository.

I just want to deploy the fine tuned weights to Nvidiai gpu through VLLM. Instead of replacing official weights for deployment.

### xiyangyang99 · 2025-11-28

> [@lixingxing1231](https://github.com/lixingxing1231) [@xiyangyang99](https://github.com/xiyangyang99) The issue is likely due to file renaming during updates, which causes the `Auto` class to fail when loading the processor. Please try the following:
> 
>     1. Download the **latest version** of PaddleOCR-VL from **Hugging Face**.
> 
>     2. Locate your **SFT-trained .safetensors** weights.
> 
>     3. **Replace** the .safetensors file in the newly downloaded repository with your trained weights (this avoids the need for retraining).
> 
>     4. Retry running inference with vllm based on this updated repository.

What I mean is the weights adjusted by SFT, which were not actually used during inference, right? Even if I use the official safetensors, it won't affect my inference results for the same input after fine-tuning.

### forBlank · 2025-11-28

@xiyangyang99 

I understand your concern. You want a standard deployment workflow where you simply point vLLM to your specific SFT checkpoint folder, without modifying the official base model directory.

**The Reason:**
The issue is that **the configuration and code files** (e.g., `config.json`, `processor_config.json`, or model implementation python files) currently inside your SFT folder are outdated or conflicting, which causes the `Auto` loader to fail. The weights themselves are fine, but vLLM needs the latest configuration files to load them correctly.

To deploy your SFT weights successfully, you have two options:

**Option 1: Update Configs Manually (Fastest, No Retraining)**
You can keep your trained weights and just fix the environment files inside your SFT folder:

1. Download the **latest** PaddleOCR-VL files from Hugging Face (to get the updated configs).
2. Copy all the **non-weight** files (such as `.json` configs, `.py` model codes, and tokenizer files) from the latest official repository into your **SFT weights folder**, overwriting the old config files.
3. Do **NOT** overwrite your `.safetensors` weights.
4. Point vLLM to your SFT weights folder to start the inference.

This ensures your deployment uses your fine-tuned weights combined with the fixed loading logic.

**Option 2: Retrain with Latest Base Model (Cleanest)**
If you prefer not to manually modify files and want a completely clean deployment artifact:

1. Download the **latest** PaddleOCR-VL from Hugging Face.
2. Perform SFT training again using this new base model.
3. The resulting output folder will automatically contain the correct configuration and code files.
4. Deploy this new output folder directly with vLLM.

Both methods will allow you to deploy by pointing vllm directly to your fine-tuned path.


### xiyangyang99 · 2025-11-28

> [@xiyangyang99](https://github.com/xiyangyang99)
> 
> I understand your concern. You want a standard deployment workflow where you simply point vLLM to your specific SFT checkpoint folder, without modifying the official base model directory.
> 
> **The Reason:** The issue is that **the configuration and code files** (e.g., `config.json`, `processor_config.json`, or model implementation python files) currently inside your SFT folder are outdated or conflicting, which causes the `Auto` loader to fail. The weights themselves are fine, but vLLM needs the latest configuration files to load them correctly.
> 
> To deploy your SFT weights successfully, you have two options:
> 
> **Option 1: Update Configs Manually (Fastest, No Retraining)** You can keep your trained weights and just fix the environment files inside your SFT folder:
> 
>     1. Download the **latest** PaddleOCR-VL files from Hugging Face (to get the updated configs).
> 
>     2. Copy all the **non-weight** files (such as `.json` configs, `.py` model codes, and tokenizer files) from the latest official repository into your **SFT weights folder**, overwriting the old config files.
> 
>     3. Do **NOT** overwrite your `.safetensors` weights.
> 
>     4. Point vLLM to your SFT weights folder to start the inference.
> 
> 
> This ensures your deployment uses your fine-tuned weights combined with the fixed loading logic.
> 
> **Option 2: Retrain with Latest Base Model (Cleanest)** If you prefer not to manually modify files and want a completely clean deployment artifact:
> 
>     1. Download the **latest** PaddleOCR-VL from Hugging Face.
> 
>     2. Perform SFT training again using this new base model.
> 
>     3. The resulting output folder will automatically contain the correct configuration and code files.
> 
>     4. Deploy this new output folder directly with vLLM.
> 
> 
> Both methods will allow you to deploy by pointing vllm directly to your fine-tuned path.

Thank you for the author's response. We have already deduced according to the first method. However, the first inference took 5 seconds, and the second inference only took a few seconds. The current deployment method is paddleocr genai_server --model_name PaddleOCR-VL-0.9B --model_dir /home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali --backend vllm --port 8118 Is there a faster way to deploy the model directly without using the server or client in this way of deploying the server? I want to load the model into memory or video memory in advance when using it to improve the speed of inference. Excuse me, is there any good way?

### xiyangyang99 · 2025-11-28

> [@xiyangyang99](https://github.com/xiyangyang99)
> 
> I understand your concern. You want a standard deployment workflow where you simply point vLLM to your specific SFT checkpoint folder, without modifying the official base model directory.
> 
> **The Reason:** The issue is that **the configuration and code files** (e.g., `config.json`, `processor_config.json`, or model implementation python files) currently inside your SFT folder are outdated or conflicting, which causes the `Auto` loader to fail. The weights themselves are fine, but vLLM needs the latest configuration files to load them correctly.
> 
> To deploy your SFT weights successfully, you have two options:
> 
> **Option 1: Update Configs Manually (Fastest, No Retraining)** You can keep your trained weights and just fix the environment files inside your SFT folder:
> 
>     1. Download the **latest** PaddleOCR-VL files from Hugging Face (to get the updated configs).
> 
>     2. Copy all the **non-weight** files (such as `.json` configs, `.py` model codes, and tokenizer files) from the latest official repository into your **SFT weights folder**, overwriting the old config files.
> 
>     3. Do **NOT** overwrite your `.safetensors` weights.
> 
>     4. Point vLLM to your SFT weights folder to start the inference.
> 
> 
> This ensures your deployment uses your fine-tuned weights combined with the fixed loading logic.
> 
> **Option 2: Retrain with Latest Base Model (Cleanest)** If you prefer not to manually modify files and want a completely clean deployment artifact:
> 
>     1. Download the **latest** PaddleOCR-VL from Hugging Face.
> 
>     2. Perform SFT training again using this new base model.
> 
>     3. The resulting output folder will automatically contain the correct configuration and code files.
> 
>     4. Deploy this new output folder directly with vLLM.
> 
> 
> Both methods will allow you to deploy by pointing vllm directly to your fine-tuned path.

My local graphics card is RTX A6000, and the output log for inferring an image is as follows. The image size is not very large, and during inference, the config parameters are set to gpu memory tilization: 0.8, max num-seqs: 1024, but the inference speed is still very slow. Without using layout detection, pure recognition takes an average of 1.7 seconds per page. Is there any way to further optimize the inference speed?
This is my client request code:


from paddleocr import PaddleOCRVL
import time
pipeline = PaddleOCRVL(use_layout_detection=False,vl_rec_max_concurrency=1024,vl_rec_backend="vllm-server", vl_rec_server_url="http://127.0.0.1:8000/v1")
# pipeline = PaddleOCRVL(use_doc_orientation_classify=True) # 通过 use_doc_orientation_classify 指定是否使用文档方向分类模型
# pipeline = PaddleOCRVL(use_doc_unwarping=True) # 通过 use_doc_unwarping 指定是否使用文本图像矫正模块
# pipeline = PaddleOCRVL(use_layout_detection=True,vl_rec_model_name="PaddleOCR-VL-0.9B",
#         vl_rec_model_dir="/home/bowen/.paddlex/official_models/PaddleOCR-VL-SFT-Bengali",) # 通过 use_layout_detection 指定是否使用版面区域检测排序模块
start=time.time()
output = pipeline.predict("/media/bowen/data/cor/o/2025-11-27_17-17.png")
print("cost time is ",time.time()-start)




### Bobholamovic · 2025-11-28

Since we implemented a thread-based pipeline acceleration approach, inference performance is maximized when you pass a list of images at once or provide an image folder. For example:

```python
output = pipeline.predict("/media/bowen/data/cor/o")
```


### xiyangyang99 · 2025-12-01

> Since we implemented a thread-based pipeline acceleration approach, inference performance is maximized when you pass a list of images at once or provide an image folder. For example:
> 
> output = pipeline.predict("/media/bowen/data/cor/o")

Hello, thank you for your reply. I have tested according to the method you mentioned. I placed 15 pictures under the folder and the inference time took a total of 15.9 seconds. Can it be faster? Or is there any way? Using C++for high-performance deployment? Or should we use more powerful inference cards?

### Bobholamovic · 2025-12-01

Could you clarify the inference speed you anticipate for your use case?

### xiyangyang99 · 2025-12-01

Undoubtedly, the advantage of vl models lies in their excellent recognition accuracy! The expected inference speed is in the tens of milliseconds range on Nvidia RTX 3090. So vl still cannot meet the requirements for implementation in my usage scenario, so I chose traditional OCR to accomplish my task.

### 1053234381 · 2026-01-04

这是来自QQ邮箱的假期自动回复邮件。已收到邮件，谢谢！

### forBlank · 2026-01-05

@MYBao217 不会影响模型精度
