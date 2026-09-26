# [Issue #1082] [BUG]

source: https://github.com/PaddlePaddle/ERNIE/issues/1082
state: closed | updated: 2026-01-07T12:02:18Z
labels: 

## 正文

ERROR    2025-08-01 13:47:52,704 3233322 engine.py[line:206] Failed to launch worker processes, check log/workerlog.* for more details.

## 评论 (17)

### Fridayfairy · 2025-08-01

<img width="1091" height="583" alt="Image" src="https://github.com/user-attachments/assets/3b34b07e-3b9f-4a4d-958d-38beb89c6b2c" />
(paddle_py312) ycx@user-NF5468-M7-A0-R0-00:/data1/JYModels$ pip list | grep fast
fast_dataindex                           0.1.2
fastapi                                  0.116.1
fastdeploy-gpu                           2.0.0.dev20250731
fastrlock                                0.8.3
fastsafetensors                          0.1.14
opentelemetry-instrumentation-fastapi    0.57b0
(paddle_py312) ycx@user-NF5468-M7-A0-R0-00:/data1/JYModels$ pip list | grep padd
paddleformers                            0.1.1
paddlepaddle-gpu                         3.1.0
use_triton_in_paddle                     0.1.0

### Jonathans575 · 2025-08-01

Hi Fridayfairy,

Thanks for reporting this issue and providing the initial logs! To help us better diagnose the problem, could you please share the following additional details from your logs:

Complete worker logs (workerlog.* files):
Please attach the full content of all relevant worker log files (e.g., workerlog.0, workerlog.1, etc.).


### Weishaoya · 2025-08-10

<img width="2234" height="1181" alt="Image" src="https://github.com/user-attachments/assets/f5f3db8c-3f1d-4dc5-840f-7fd5eaee8675" />

<img width="2234" height="1181" alt="Image" src="https://github.com/user-attachments/assets/b4e4b56a-7134-484e-8581-58cc58e9dca9" />
<img width="2234" height="1181" alt="Image" src="https://github.com/user-attachments/assets/0e606558-1e32-4dc4-b01b-9054e9ecc242" />

the same issue

### Jonathans575 · 2025-08-11

Hi Weishaoya,

Thanks for reporting the issue! To help us better diagnose and reproduce the problem, could you please share the following details about your environment?

Python Version: [output of python --version or python3 --version]
Package Versions:
[Project Name]: [version, e.g., 1.2.3]
Key dependencies (e.g., paddlepaddle, fastdeploy)

### Weishaoya · 2025-08-12

> Hi Weishaoya,
> 
> Thanks for reporting the issue! To help us better diagnose and reproduce the problem, could you please share the following details about your environment?
> 
> Python Version: [output of python --version or python3 --version] Package Versions: [Project Name]: [version, e.g., 1.2.3] Key dependencies (e.g., paddlepaddle, fastdeploy)

已解决！之前是基于python3.12创建的环境，改成python3.10后，再安装paddlepaddle和fastdeploy就可以了

### a31413510 · 2025-08-12

好的，后续有问题随时交流

### CosmosYi · 2025-08-16

same problem! @Jonathans575 

My environment info: 
GPUs: 4090 x8 
python: 3.10.18
paddlepaddle-gpu: 3.1.0
fastdeploy-gpu: 2.1.0

### Jonathans575 · 2025-08-18

Hi CosmosYi,

Thanks for reporting the issue! To help us investigate and resolve it faster, could you provide the following details?
 
1. **Steps to Reproduce**:  
   Please describe the exact actions that triggered the error.
 
2. **Error Logs/Messages**:  
   - If there’s an error message in the console/terminal, copy and paste the full output here.  
   - If the application generates logs, check the relevant log file (e.g., `logs/`) and share the relevant excerpt.

### CosmosYi · 2025-08-19


Hi Jonathans575,
Thanks for your reply! @Jonathans575 

1. Steps to Reproduce:
    I followed the tutorial (https://aistudio.baidu.com/projectdetail/9357717?channelType=0), and the problem occurred when I ran the following command:
python -m fastdeploy.entrypoints.openai.api_server
--model work/models
--port 8180
--metrics-port 8181
--engine-worker-queue-port 8182
--max-model-len 32768
--enable-mm
--reasoning-parser ernie-45-vl \

2. The error log is the same as the one provided by the poster, and I have copied it here:

<img width="2182" height="1166" alt="Image" src="https://github.com/user-attachments/assets/764c7df7-39cc-4cd0-a59b-b6dad7b3f038" /> 

### Jonathans575 · 2025-08-19

Hi, CosmosYi,

Please show the error log in log/workerlog.*.

### CosmosYi · 2025-08-19

OK, here it is:

```
/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:715: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml
  warnings.warn(
[2025-08-16 21:37:22,415] [    INFO] distributed_strategy.py:333 - distributed strategy initialized
======================= Modified FLAGS detected =======================
FLAGS(name='FLAGS_cudnn_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cudnn/lib', default_value='')
FLAGS(name='FLAGS_enable_pir_in_executor', current_value=True, default_value=False)
FLAGS(name='FLAGS_cusparse_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cusparse/lib', default_value='')
FLAGS(name='FLAGS_cublas_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cublas/lib', default_value='')
FLAGS(name='FLAGS_specialize_device_in_dy2st', current_value=True, default_value=False)
FLAGS(name='FLAGS_curand_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/curand/lib', default_value='')
FLAGS(name='FLAGS_selected_gpus', current_value='0', default_value='')
FLAGS(name='FLAGS_pir_interpreter_record_stream_for_gc_cache', current_value=True, default_value=False)
FLAGS(name='FLAGS_nvidia_package_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia', default_value='')
FLAGS(name='FLAGS_cuda_cccl_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cuda_cccl/include/', default_value='')
FLAGS(name='FLAGS_cupti_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cuda_cupti/lib', default_value='')
FLAGS(name='FLAGS_cusolver_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cusolver/lib', default_value='')
FLAGS(name='FLAGS_nccl_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/nccl/lib', default_value='')
=======================================================================
/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/distributed/parallel.py:1053: UserWarning: Currently not a parallel execution environment, `paddle.distributed.init_parallel_env` will not do anything.
  warnings.warn(
[2025-08-16 21:37:22,416] [    INFO] topology.py:370 - Total 1 pipe comm group(s) create successfully!
/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/distributed/communication/group.py:145: UserWarning: Current global rank 0 is not in group _default_pg10
  warnings.warn(
[2025-08-16 21:37:22,779] [    INFO] topology.py:370 - Total 1 data comm group(s) create successfully!
[2025-08-16 21:37:22,779] [    INFO] topology.py:370 - Total 1 model comm group(s) create successfully!
[2025-08-16 21:37:22,779] [    INFO] topology.py:370 - Total 1 sharding comm group(s) create successfully!
[2025-08-16 21:37:22,779] [    INFO] topology.py:288 - HybridParallelInfo: rank_id: 0, mp_degree: 1, sharding_degree: 1, pp_degree: 1, dp_degree: 1, sep_degree: 1, mp_group: [0],  sharding_group: [0], pp_group: [0], dp_group: [0], sep:group: None, check/clip group: [0]
^[[32m[2025-08-16 21:37:22,779] [    INFO]^[[0m - Loading configuration file /home/supervisor/data/LCY/Models/ERNIE-4.5-VL-28B-A3B-Paddle/config.json^[[0m
^[[33m[2025-08-16 21:37:22,779] [ WARNING]^[[0m - You are using a model of type ernie4_5_moe_vl to instantiate a model of type . This is not supported for all configurations of models and can yield errors.^[[0m
^[[32m[2025-08-16 21:38:02,982] [    INFO]^[[0m - loading configuration file /home/supervisor/data/LCY/Models/ERNIE-4.5-VL-28B-A3B-Paddle/preprocessor_config.json^[[0m
Traceback (most recent call last):
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/engine/../worker/worker_process.py", line 753, in <module>
    run_worker_proc()
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/engine/../worker/worker_process.py", line 731, in run_worker_proc
    worker_proc.init_device()
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/engine/../worker/worker_process.py", line 432, in init_device
    self.worker.init_device()
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/worker/gpu_worker.py", line 73, in init_device
    self.model_runner: GPUModelRunner = GPUModelRunner(
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/worker/gpu_model_runner.py", line 128, in __init__
    self._init_share_inputs(self.parallel_config.max_num_seqs)
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/worker/gpu_model_runner.py", line 741, in _init_share_inputs
    self.share_inputs["rope_emb"] = paddle.full(
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/tensor/creation.py", line 1525, in full
    return fill_constant(shape=shape, dtype=dtype, value=fill_value, name=name)
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/tensor/creation.py", line 1105, in fill_constant
    out = _C_ops.full(shape, value, dtype, place)
MemoryError: 

--------------------------------------
C++ Traceback (most recent call last):
--------------------------------------
0   paddle::pybind::eager_api_full(_object*, _object*, _object*)
1   full_ad_func(paddle::experimental::IntArrayBase<paddle::Tensor>, paddle::experimental::ScalarBase<paddle::Tensor>, phi::DataType, phi::Place)
2   paddle::experimental::full(paddle::experimental::IntArrayBase<paddle::Tensor> const&, paddle::experimental::ScalarBase<paddle::Tensor> const&, phi::DataType, phi::Place const&)
3   void phi::FullKernel<float, phi::GPUContext>(phi::GPUContext const&, paddle::experimental::IntArrayBase<phi::DenseTensor> const&, paddle::experimental::ScalarBase<phi::DenseTensor> const&, phi::DataType, phi::DenseTensor*)
4   float* phi::DeviceContext::Alloc<float>(phi::TensorBase*, unsigned long, bool) const
5   phi::DenseTensor::AllocateFrom(phi::Allocator*, phi::DataType, unsigned long, bool)
6   paddle::memory::allocation::Allocator::Allocate(unsigned long)
7   paddle::memory::allocation::StatAllocator::AllocateImpl(unsigned long)
8   paddle::memory::allocation::Allocator::Allocate(unsigned long)
9   paddle::memory::allocation::Allocator::Allocate(unsigned long)
10  std::string phi::enforce::GetCompleteTraceBackString<std::string >(std::string&&, char const*, int)
11  common::enforce::GetCurrentTraceBackString[abi:cxx11](bool)

----------------------
Error Message Summary:
----------------------
ResourceExhaustedError: 

Out of memory error on GPU 0. Cannot allocate 128.000000MB memory on GPU 0, 23.431824GB memory has been allocated and available memory is only 97.625000MB.

Please check whether there is any other process using GPU 0.
1. If yes, please stop them, or start PaddlePaddle on another GPU.
2. If no, please decrease the batch size of your model. 
 (at /paddle/paddle/phi/core/memory/allocation/cuda_allocator.cc:71)

/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:715: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml
  warnings.warn(
[2025-08-18 13:38:19,575] [    INFO] distributed_strategy.py:333 - distributed strategy initialized
======================= Modified FLAGS detected =======================
FLAGS(name='FLAGS_nvidia_package_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia', default_value='')
FLAGS(name='FLAGS_selected_gpus', current_value='0', default_value='')
FLAGS(name='FLAGS_nccl_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/nccl/lib', default_value='')
FLAGS(name='FLAGS_cuda_cccl_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cuda_cccl/include/', default_value='')
FLAGS(name='FLAGS_cusolver_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cusolver/lib', default_value='')
FLAGS(name='FLAGS_pir_interpreter_record_stream_for_gc_cache', current_value=True, default_value=False)
FLAGS(name='FLAGS_cudnn_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cudnn/lib', default_value='')
FLAGS(name='FLAGS_cublas_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cublas/lib', default_value='')
FLAGS(name='FLAGS_enable_pir_in_executor', current_value=True, default_value=False)
FLAGS(name='FLAGS_specialize_device_in_dy2st', current_value=True, default_value=False)
FLAGS(name='FLAGS_cusparse_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cusparse/lib', default_value='')
FLAGS(name='FLAGS_cupti_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/cuda_cupti/lib', default_value='')
FLAGS(name='FLAGS_curand_dir', current_value='/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/../nvidia/curand/lib', default_value='')
=======================================================================
/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/distributed/parallel.py:1053: UserWarning: Currently not a parallel execution environment, `paddle.distributed.init_parallel_env` will not do anything.
  warnings.warn(
[2025-08-18 13:38:19,576] [    INFO] topology.py:370 - Total 1 pipe comm group(s) create successfully!
/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/paddle/distributed/communication/group.py:145: UserWarning: Current global rank 0 is not in group _default_pg10
  warnings.warn(
[2025-08-18 13:38:19,778] [    INFO] topology.py:370 - Total 1 data comm group(s) create successfully!
[2025-08-18 13:38:19,778] [    INFO] topology.py:370 - Total 1 model comm group(s) create successfully!
[2025-08-18 13:38:19,778] [    INFO] topology.py:370 - Total 1 sharding comm group(s) create successfully!
[2025-08-18 13:38:19,778] [    INFO] topology.py:288 - HybridParallelInfo: rank_id: 0, mp_degree: 1, sharding_degree: 1, pp_degree: 1, dp_degree: 1, sep_degree: 1, mp_group: [0],  sharding_group: [0], pp_group: [0], dp_group: [0], sep:group: None, check/clip group: [0]
^[[32m[2025-08-18 13:38:19,778] [    INFO]^[[0m - Loading configuration file /home/supervisor/data/LCY/Models/ERNIE-4.5-VL-28B-A3B-Paddle/config.json^[[0m
^[[33m[2025-08-18 13:38:19,779] [ WARNING]^[[0m - You are using a model of type ernie4_5_moe_vl to instantiate a model of type . This is not supported for all configurations of models and can yield errors.^[[0m
INFO     2025-08-18 13:38:23,717 950733 cuda.py[line:56] Using APPEND ATTN backend.
^[[32m[2025-08-18 13:38:23,717] [    INFO]^[[0m - Starting to load model Ernie4_5_VLMoeForConditionalGeneration^[[0m
^[[32m[2025-08-18 13:38:23,717] [    INFO]^[[0m - Load the model and weights using DefaultModelLoader^[[0m
^[[32m[2025-08-18 13:38:23,717] [    INFO]^[[0m - Starting to load model Ernie4_5_VLMoeForConditionalGeneration^[[0m
Traceback (most recent call last):
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/engine/../worker/worker_process.py", line 753, in <module>
    run_worker_proc()
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/engine/../worker/worker_process.py", line 734, in run_worker_proc
    worker_proc.load_model()
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/engine/../worker/worker_process.py", line 436, in load_model
    self.worker.load_model()
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/worker/gpu_worker.py", line 164, in load_model
    self.model_runner.load_model()
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/worker/gpu_model_runner.py", line 833, in load_model
    self.model = model_loader.load_model(fd_config=self.fd_config)
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/model_executor/model_loader/default_loader.py", line 78, in load_model
    model = model_cls(fd_config)
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/model_executor/models/ernie4_5_vl/ernie4_5_vl_moe.py", line 516, in __init__
    self.ernie = Ernie4_5_VLModel(fd_config=fd_config)
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/model_executor/graph_optimization/decorator.py", line 55, in __init__
    origin_init(self, fd_config=fd_config, **kwargs)
  File "/home/supervisor/data/Anaconda3/envs/ernie/lib/python3.10/site-packages/fastdeploy/model_executor/models/ernie4_5_vl/ernie4_5_vl_moe.py", line 365, in __init__
    self.im_patch_id = fd_config.model_config.im_patch_id
AttributeError: 'ModelConfig' object has no attribute 'im_patch_id'

```

### Jonathans575 · 2025-08-19

Hi, CosmosYi,

Based on this log, it seems that your GPU memory has run out (OOM - Out Of Memory). You could try enabling Winograd T4 (wint4) quantization and see if that works.

### CosmosYi · 2025-08-19

Hi Jonathans575,
Thanks very much! I will try it.

### Jonathans575 · 2025-08-25

Hi CosmosYi,

Issue resolved - closing now. Feel free to reopen or create a new one if needed!

Happy coding!
Best regards

### faan-fan · 2025-09-17

我使用飞浆AI创建的项目，运行以下代码也报相同错误了
!python -m fastdeploy.entrypoints.openai.api_server \
       --model baidu/ERNIE-4.5-0.3B-Paddle \
       --port 8180 \
       --metrics-port 8181 \
       --engine-worker-queue-port 8182 \
       --max-model-len 32768 \
       --max-num-seqs 32

/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:718: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
Processing 9 items: 100%|████████████████████| 9.00/9.00 [00:00<00:00, 24.8it/s]
[2025-09-17 16:41:19,735] [    INFO] - Using download source: huggingface
[2025-09-17 16:41:19,736] [    INFO] - Loading configuration file /home/aistudio/data/models/PaddlePaddle/ERNIE-4.5-0.3B-Paddle/config.json
[2025-09-17 16:41:19,736] [ WARNING] - You are using a model of type ernie4_5 to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
[2025-09-17 16:41:19,801] [    INFO] - Using download source: huggingface
[2025-09-17 16:41:19,802] [    INFO] - Loading configuration file /home/aistudio/data/models/PaddlePaddle/ERNIE-4.5-0.3B-Paddle/config.json
[2025-09-17 16:41:19,802] [ WARNING] - You are using a model of type ernie4_5 to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml
  warnings.warn(
[2025-09-17 16:41:20,842] [    INFO] - Using download source: huggingface
[2025-09-17 16:41:20,842] [    INFO] - Loading configuration file /home/aistudio/data/models/PaddlePaddle/ERNIE-4.5-0.3B-Paddle/generation_config.json
/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/generation/configuration_utils.py:250: UserWarning: using greedy search strategy. However, `temperature` is set to `0.8` -- this flag is only used in sample-based generation modes. You should set `decode_strategy="greedy_search" ` or unset `temperature`. This was detected when initializing the generation config instance, which means the corresponding file may hold incorrect parameterization and should be fixed.
  warnings.warn(
/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/generation/configuration_utils.py:255: UserWarning: using greedy search strategy. However, `top_p` is set to `0.8` -- this flag is only used in sample-based generation modes. You should set `decode_strategy="greedy_search" ` or unset `top_p`. This was detected when initializing the generation config instance, which means the corresponding file may hold incorrect parameterization and should be fixed.
  warnings.warn(
[2025-09-17 16:41:20,843] [ WARNING] - PretrainedTokenizer will be deprecated and removed in the next major release. Please migrate to Hugging Face's transformers.PreTrainedTokenizer. Checkout paddleformers/transformers/qwen/tokenizer.py for an example: use class QWenTokenizer(PaddleTokenizerMixin, hf.PreTrainedTokenizer) to support multisource download and Paddle tokenizer operations.
INFO     2025-09-17 16:41:25,372 1286  engine.py[line:202] Waitting worker processes ready...
Loading Weights:   0%|                                  | 0/100 [00:08<?, ?it/s]
ERROR    2025-09-17 16:41:38,896 1286  engine.py[line:206] Failed to launch worker processes, check log/workerlog.* for more details.
Error extracting sub services: [Errno 3] No such process


### Jonathans575 · 2025-09-23

Hi, faan-fan,

Please show the error log in log/workerlog.*.

### nepeplwu · 2026-01-07

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
