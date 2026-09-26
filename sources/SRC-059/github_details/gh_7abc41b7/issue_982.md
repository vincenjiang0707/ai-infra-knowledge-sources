# [Issue #982] A800-80GB * 1卡模型加载完后一直卡住进度无法使用

source: https://github.com/PaddlePaddle/ERNIE/issues/982
state: closed | updated: 2025-07-14T03:30:58Z
labels: 

## 正文

python -m fastdeploy.entrypoints.openai.api_server \
 --model baidu/ERNIE-4.5-VL-28B-A3B-Paddle \
 --port 8180 \
 --metrics-port 8181 \
 --engine-worker-queue-port 8182 \
 --max-model-len 32768 \
 --enable-mm \
 --reasoning-parser ernie-45-vl \
 --max-num-seqs 32
启动日志如下：
tail fastdeploy.log
INFO 2025-07-04 09:26:55,988 1041 config.py[line:135] Parameter `COMPRESSION_RATIO` will use default value 1.0.
INFO 2025-07-04 09:27:17,955 1041 engine.py[line:1068] Launch worker service command: PADDLE_TRAINER_ID=0 PADDLE_TRAINERS_NUM=1 TRAINER_INSTANCES_NUM=1 TRAINER_INSTANCES=0.0.0.0 ENABLE_FASTDEPLOY_LOAD_MODEL_CONCURRENCY=0 LOAD_STATE_DICT_THREAD_NUM=1 PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python FLAGS_use_append_attn=1 NCCL_ALGO=Ring FLAGS_hardamard_moe_block_size=128 FLAGS_max_partition_size=1024 SOT_LOG_LEVEL=0 SOT_UNSAFE_CACHE_FASTPATH=1 SOT_ENABLE_0_SIZE_FALLBACK=0 FLAGS_specialize_device_in_dy2st=1 FLAGS_enable_async_fast_gc=0 FLAGS_pir_interpreter_record_stream_for_gc_cache=1 /root/miniconda3/bin/python -u -m paddle.distributed.launch --log_dir log --nnodes 1 --devices 0 /root/miniconda3/lib/python3.12/site-packages/fastdeploy/engine/../worker/vl_worker_process.py --max_num_seqs 32 --max_model_len 32768 --gpu_memory_utilization 0.9 --model_name_or_path baidu/ERNIE-4.5-VL-28B-A3B-Paddle --device_ids 0 --tensor_parallel_size 1 --engine_worker_queue_port 8182 --total_block_num 576 --block_size 64 --enc_dec_block_num 2 --eos_tokens_lens 1 --pad_token_id 0 --engine_pid 1041 --max_num_batched_tokens 32768 --splitwise_role mixed --kv_cache_ratio 0.75 --expert_parallel_size 1 --quantization None --ori_vocab_size 103367 --speculative_method None --speculative_max_draft_token_num 1 --speculative_model_name_or_path None --speculative_model_quantization WINT8 --max_capture_batch_size 64 --guided_decoding_backend off --do_profile 2>log/launch_worker.log
INFO 2025-07-04 09:27:20,957 1162 config.py[line:135] Parameter `COMPRESSION_RATIO` will use default value 1.0.
WARNING 2025-07-04 09:27:22,578 1162 import_ops.py[line:47] Ops of fastdeploy.model_executor.ops.cpu import failed, it may be not compiled.
WARNING 2025-07-04 09:27:22,579 1162 import_ops.py[line:47] Ops of fastdeploy.model_executor.ops.xpu import failed, it may be not compiled.
WARNING 2025-07-04 09:27:22,579 1162 import_ops.py[line:47] Ops of fastdeploy.model_executor.ops.npu import failed, it may be not compiled.
INFO 2025-07-04 09:28:43,844 1162 engine_worker_queue.py[line:219] Connected EngineWorkerQueue client_id: 0, number of connected clients: 2
WARNING 2025-07-04 09:28:45,569 1041 import_ops.py[line:47] Ops of fastdeploy.model_executor.ops.cpu import failed, it may be not compiled.
WARNING 2025-07-04 09:28:45,569 1041 import_ops.py[line:47] Ops of fastdeploy.model_executor.ops.xpu import failed, it may be not compiled.
WARNING 2025-07-04 09:28:45,570 1041 import_ops.py[line:47] Ops of fastdeploy.model_executor.ops.npu import failed, it may be not compiled.

tail api_server.log
INFO 2025-07-04 09:26:54,407 1041 api_server.py[line:80] FastDeploy LLM API server starting... 1041

tail worker.log
INFO 2025-07-04 09:27:22,950 1162 vl_worker_process.py[line:213] quantization : None
INFO 2025-07-04 09:27:22,950 1162 vl_worker_process.py[line:213] enable_static_graph_inference: False
INFO 2025-07-04 09:27:22,950 1162 vl_worker_process.py[line:213] use_cudagraph : False
INFO 2025-07-04 09:27:22,950 1162 vl_worker_process.py[line:213] max_capture_batch_size: 64
INFO 2025-07-04 09:27:22,950 1162 vl_worker_process.py[line:213] guided_decoding_backend: off
INFO 2025-07-04 09:27:22,950 1162 vl_worker_process.py[line:213] disable_any_whitespace: True
INFO 2025-07-04 09:27:22,950 1162 vl_worker_process.py[line:214] =====================================================

INFO 2025-07-04 09:28:43,844 1162 vl_worker_process.py[line:424] before activate gpu memory: 58.05706071853638 GiB.
INFO 2025-07-04 09:28:43,884 1162 vl_worker_process.py[line:437] used gpu memory: 59.684814453125 GiB.

启动后进度条一直卡在
[2025-07-04 09:27:14,848] [ INFO] - loading configuration file baidu/ERNIE-4.5-VL-28B-A3B-Paddle/preprocessor_config.json
INFO 2025-07-04 09:27:17,977 1041 engine.py[line:206] Waitting worker processes ready...
Loading Weights: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [01:11<00:00, 1.41it/s]
Loading Layers: 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:10<00:00, 9.52it/s]
这里，且无法访问接口
http://0.0.0.0:8180/v1/chat/completions
请分析一下我要如何修复

## 评论 (6)

### ming1753 · 2025-07-04

看下workerlog.0的日志

### chatdl · 2025-07-04

> 看下workerlog.0的日志

tail workerlog.0 
    return self.forward(*inputs, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/fastdeploy/model_executor/layers/normalization.py", line 122, in forward
    norm_out = self.norm_func(
               ^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/paddle/incubate/nn/functional/fused_rms_norm.py", line 110, in fused_rms_norm
    raise ValueError(
ValueError: begin_norm_axis must be in range [0, 1), but got 1
/root/miniconda3/lib/python3.12/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 6 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

tail worker.log
INFO     2025-07-04 17:43:58,730 1543  vl_worker_process.py[line:213] quantization        :      None
INFO     2025-07-04 17:43:58,730 1543  vl_worker_process.py[line:213] enable_static_graph_inference:      False
INFO     2025-07-04 17:43:58,730 1543  vl_worker_process.py[line:213] use_cudagraph       :      False
INFO     2025-07-04 17:43:58,730 1543  vl_worker_process.py[line:213] max_capture_batch_size:      64
INFO     2025-07-04 17:43:58,730 1543  vl_worker_process.py[line:213] guided_decoding_backend:      off
INFO     2025-07-04 17:43:58,730 1543  vl_worker_process.py[line:213] disable_any_whitespace:      True
INFO     2025-07-04 17:43:58,730 1543  vl_worker_process.py[line:214] =====================================================

INFO     2025-07-04 17:45:31,118 1543  vl_worker_process.py[line:424] before activate gpu memory: 55.6566698551178 GiB.
INFO     2025-07-04 17:45:31,194 1543  vl_worker_process.py[line:437] used gpu memory: 56.8577880859375 GiB.

nvidia-smi
Fri Jul  4 17:48:38 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 565.57.01              Driver Version: 565.57.01      CUDA Version: 12.7     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H800 PCIe               On  |   00000000:18:00.0 Off |                  Off |
| N/A   31C    P0             50W /  350W |       4MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+


### ming1753 · 2025-07-07

FastDeploy只支持paddle格式的模型，检查下是否使用FastDeploy加载torch格式的模型(ERNIE-4.5-VL-28B-A3B-PT)了呢？
更多内容参考文档：https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/get_started/quick_start_vl.md

### chatdl · 2025-07-07

https://www.modelscope.cn/models/PaddlePaddle/ERNIE-4.5-VL-28B-A3B-Paddle/file/view/master/README.md?status=1
模型在这个链接下载的，模型是paddle格式的

test_fastdeploy.py 测试代码
import os
os.environ["OMP_NUM_THREADS"] = "1"  # 解决OpenBLAS警告

import fastdeploy as fd
import paddle

print("="*50)
print("验证FastDeploy安装:")
try:
    print(f"FastDeploy版本: {fd.__version__}")
    print(f"可用后端: {fd.get_available_backends()}")
    runtime = fd.RuntimeOption()
    runtime.use_gpu()
    print("RuntimeOption创建成功")
except Exception as e:
    print(f"FastDeploy验证失败: {str(e)}")

print("\n" + "="*50)
print("验证PaddlePaddle安装:")
try:
    print(f"Paddle版本: {paddle.__version__}")
    print(f"可用GPU数量: {paddle.device.cuda.device_count()}")
    print(f"当前设备: {paddle.device.get_device()}")
except Exception as e:
    print(f"Paddle验证失败: {str(e)}")

python test_fastdeploy.py 
==================================================
验证FastDeploy安装:
FastDeploy验证失败: module 'fastdeploy' has no attribute '__version__'

==================================================
验证PaddlePaddle安装:
Paddle版本: 3.1.0
可用GPU数量: 1
当前设备: gpu:0


使用的AutoDL平台，无法启动docker,通过https://paddlepaddle.github.io/FastDeploy/get_started/installation/nvidia_gpu/这个里面的命令分别安装了fastdeploy-gpu、fastdeploy-gpu
pip show fastdeploy-gpu
Name: fastdeploy-gpu
Version: 2.0.0
Summary: FastDeploy: Large Language Model Serving.
Home-page: https://github.com/PaddlePaddle/FastDeploy
Author: PaddlePaddle
Author-email: dltp@baidu.com
License: Apache 2.0
Location: /root/miniconda3/lib/python3.12/site-packages
Requires: aiozmq, crcmod, cupy-cuda12x, decord, etcd3, fastapi, flake8, gradio, httpx, moviepy, openai, paddleformers, pre-commit, prometheus-client, pybind11, pynvml, redis, ruamel.yaml, setuptools, setuptools-scm, tabulate, tool_helpers, tqdm, triton, use-triton-in-paddle, uvicorn, visualdl, xlwt, yapf, zmq
Required-by: 
root@autodl-container-304c4b8481-d9846cb0:~/autodl-tmp# pip show fastdeploy-gpu
Name: fastdeploy-gpu
Version: 2.0.0
Summary: FastDeploy: Large Language Model Serving.
Home-page: https://github.com/PaddlePaddle/FastDeploy
Author: PaddlePaddle
Author-email: dltp@baidu.com
License: Apache 2.0
Location: /root/miniconda3/lib/python3.12/site-packages
Requires: aiozmq, crcmod, cupy-cuda12x, decord, etcd3, fastapi, flake8, gradio, httpx, moviepy, openai, paddleformers, pre-commit, prometheus-client, pybind11, pynvml, redis, ruamel.yaml, setuptools, setuptools-scm, tabulate, tool_helpers, tqdm, triton, use-triton-in-paddle, uvicorn, visualdl, xlwt, yapf, zmq
Required-by: 

### ming1753 · 2025-07-08

我们本地复现一下这个问题，有进展会同步～

### ming1753 · 2025-07-08

参考 https://github.com/PaddlePaddle/FastDeploy/issues/2739 中提供的解法
