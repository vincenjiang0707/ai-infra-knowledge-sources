# [Issue #1389] ValueError: GGUF model with architecture ernie4_5-moe is not supported yet.

source: https://github.com/PaddlePaddle/ERNIE/issues/1389
state: open | updated: 2026-01-14T03:40:02Z
labels: 

## 正文

使用vllm部署ernie-4.5-21B-A3B gguf模型，报错
```text
(APIServer pid=162062) Traceback (most recent call last):
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/bin/vllm", line 8, in <module>
(APIServer pid=162062)     sys.exit(main())
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 73, in main
(APIServer pid=162062)     args.dispatch_function(args)
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 60, in cmd
(APIServer pid=162062)     uvloop.run(run_server(args))
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
(APIServer pid=162062)     return loop.run_until_complete(wrapper())
(APIServer pid=162062)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=162062)     return await main
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 2024, in run_server
(APIServer pid=162062)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 2043, in run_server_worker
(APIServer pid=162062)     async with build_async_engine_client(
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=162062)     return await anext(self.gen)
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 195, in build_async_engine_client
(APIServer pid=162062)     async with build_async_engine_client_from_engine_args(
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=162062)     return await anext(self.gen)
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 221, in build_async_engine_client_from_engine_args
(APIServer pid=162062)     vllm_config = engine_args.create_engine_config(usage_context=usage_context)
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1351, in create_engine_config
(APIServer pid=162062)     maybe_override_with_speculators(
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/transformers_utils/config.py", line 530, in maybe_override_with_speculators
(APIServer pid=162062)     config_dict, _ = PretrainedConfig.get_config_dict(
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/transformers/configuration_utils.py", line 662, in get_config_dict
(APIServer pid=162062)     config_dict, kwargs = cls._get_config_dict(pretrained_model_name_or_path, **kwargs)
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/transformers/configuration_utils.py", line 753, in _get_config_dict
(APIServer pid=162062)     config_dict = load_gguf_checkpoint(resolved_config_file, return_tensors=False)["config"]
(APIServer pid=162062)   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/transformers/modeling_gguf_pytorch_utils.py", line 431, in load_gguf_checkpoint
(APIServer pid=162062)     raise ValueError(f"GGUF model with architecture {architecture} is not supported yet.")
(APIServer pid=162062) ValueError: GGUF model with architecture ernie4_5-moe is not supported yet.
```

请问目前是用什么环境版本能再本地跑起来4位量化的模型呢，希望本地单卡部署`ernie-4.5-21B`，显存大概有20g、22g、24g，
以下是推理环境：
```text
transformers==4.57.3
torch==2.9.0
vllm==0.11.2
```

cuda环境：
```text
NVIDIA-SMI 570.86.10              Driver Version: 570.86.10      CUDA Version: 12.8
```

## 评论 (5)

### CSWYF3634076 · 2025-12-04

目前应该是没有单独适配过guff模型到vllm上，看报错信息也是类似。
根据vllm文档目前支持是比较有限的https://docs.vllm.com.cn/en/latest/features/quantization/gguf.html。
可以使用--quantization fp8，进行8bit的在线量化，这个验证过是正常的。

如果你对推理框架不要求的话，可以使用FastDeploy进行部署，提供wint4在线量化。模型用PT后缀的就行，FastDeploy已经支持了torch风格权重。参考文档https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/get_started/ernie-4.5.md

### ykallan · 2025-12-04

> 目前应该是没有单独适配过guff模型到vllm上，看报错信息也是类似。 根据vllm文档目前支持是比较有限的[https://docs.vllm.com.cn/en/latest/features/quantization/gguf.html。](https://docs.vllm.com.cn/en/latest/features/quantization/gguf.html%E3%80%82) 可以使用--quantization fp8，进行8bit的在线量化，这个验证过是正常的。
> 
> 如果你对推理框架不要求的话，可以使用FastDeploy进行部署，提供wint4在线量化。模型用PT后缀的就行，FastDeploy已经支持了torch风格权重。参考文档https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/get_started/ernie-4.5.md

双卡2080ti 共44g显存，fastdeploy加载报错
启动命令如下：
```text
export CUDA_VISIBLE_DEVICES=0,1
python -m fastdeploy.entrypoints.openai.api_server \
       --model baidu/ERNIE-4.5-21B-A3B-WINT4-Paddle \
       --port 8180 \
       --metrics-port 8181 \
       --engine-worker-queue-port 8182 \
       --quantization wint4 \
       --max-model-len 4396 \
       --max-num-seqs 32 \
       --enable-prefix-caching \
       --swap-space 10
```
报错内容：
```text
[2025-12-04 17:36:43,187] [ WARNING] - PretrainedTokenizer will be deprecated and removed in the next major release. Please migrate to Hugging Face's transformers.PreTrainedTokenizer. Checkout paddleformers/transformers/qwen/tokenizer.py for an example: use class QWenTokenizer(PaddleTokenizerMixin, hf.PreTrainedTokenizer) to support multisource download and Paddle tokenizer operations.
INFO     2025-12-04 17:36:45,160 293018 engine.py[line:144] Waiting for worker processes to be ready...
Loading Weights: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:51<00:00,  1.94it/s]Loading Layers:   0%|                                                                                                                                     | 0/100 [00:24<?, ?it/s]ERROR    2025-12-04 17:38:05,728 293018 engine.py[line:153] Failed to launch worker processes, check log/workerlog.* for more details.


```
其中log内容如下：
```text
(base) [root@localhost log]# cat console_error.log
ERROR    2025-12-04 17:38:05,728 293018 engine.py[line:153] Failed to launch worker processes, check log/workerlog.* for more details.
(base) [root@localhost log]# cat worker_process.log
INFO     2025-12-04 17:36:52,976 293713 worker_process.py[line:758] parallel_config.use_ep False
INFO     2025-12-04 17:36:52,976 293713 worker_process.py[line:759] parallel_config.tensor_parallel_size 1
INFO     2025-12-04 17:36:52,976 293713 worker_process.py[line:760] parallel_config.tensor_parallel_rank 0
INFO     2025-12-04 17:36:52,976 293713 worker_process.py[line:761] parallel_config.engine_worker_queue_port 8182
INFO     2025-12-04 17:36:52,980 293713 worker_process.py[line:774] ===========quantization_config==============
INFO     2025-12-04 17:36:52,980 293713 worker_process.py[line:779] Model Status: Original (will apply online quantization)
INFO     2025-12-04 17:36:52,980 293713 worker_process.py[line:781] None
INFO     2025-12-04 17:36:52,980 293713 worker_process.py[line:785] - Dynamic load weight: False
INFO     2025-12-04 17:36:52,980 293713 worker_process.py[line:786] - Load strategy: normal
INFO     2025-12-04 17:36:52,982 293712 worker_process.py[line:758] parallel_config.use_ep False
INFO     2025-12-04 17:36:52,982 293712 worker_process.py[line:759] parallel_config.tensor_parallel_size 1
INFO     2025-12-04 17:36:52,982 293712 worker_process.py[line:760] parallel_config.tensor_parallel_rank 0
INFO     2025-12-04 17:36:52,982 293712 worker_process.py[line:761] parallel_config.engine_worker_queue_port 8182
INFO     2025-12-04 17:36:52,986 293712 worker_process.py[line:774] ===========quantization_config==============
INFO     2025-12-04 17:36:52,986 293712 worker_process.py[line:779] Model Status: Original (will apply online quantization)
INFO     2025-12-04 17:36:52,986 293712 worker_process.py[line:781] None
INFO     2025-12-04 17:36:52,986 293712 worker_process.py[line:785] - Dynamic load weight: False
INFO     2025-12-04 17:36:52,986 293712 worker_process.py[line:786] - Load strategy: normal

```




### ykallan · 2025-12-04

当我加上参数 `--tensor-parallel-size 2`会报错：
```text
[2025-12-04 17:44:39,233] [ WARNING] - PretrainedTokenizer will be deprecated and removed in the next major release. Please migrate to Hugging Face's transformers.PreTrainedTokenizer. Checkout paddleformers/transformers/qwen/tokenizer.py for an example: use class QWenTokenizer(PaddleTokenizerMixin, hf.PreTrainedTokenizer) to support multisource download and Paddle tokenizer operations.
INFO     2025-12-04 17:44:41,242 294488 engine.py[line:144] Waiting for worker processes to be ready...
Loading Weights:   0%|                                                                                                                                    | 0/100 [00:05<?, ?it/s]ERROR    2025-12-04 17:44:51,749 294488 engine.py[line:153] Failed to launch worker processes, check log/workerlog.* for more details.
ERROR    2025-12-04 17:44:58,224 294488 engine.py[line:424] Error extracting sub services: [Errno 3] No such process, Traceback (most recent call last):
  File "/root/miniconda3/envs/fastdeploy/lib/python3.12/site-packages/fastdeploy/engine/engine.py", line 421, in _exit_sub_services
    pgid = os.getpgid(self.worker_proc.pid)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ProcessLookupError: [Errno 3] No such process

/root/miniconda3/envs/fastdeploy/lib/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 2 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

```

### ykallan · 2025-12-04

请问目前21b有4位量化的模型权重吗。单卡22g，跑再大一点的量化有点费劲
目前环境如下：
```text
fastdeploy-gpu                           2.3.0
paddlepaddle-gpu                         3.2.2
transformers                             4.55.4
```

### Jiang-Jia-Jun · 2026-01-14

@ykallan 21B目前我们没有提供4Bit量化，只有WINT4的量化支持，但仍然最少需要48G的显存。也就是24G的显存的话，需要双卡
