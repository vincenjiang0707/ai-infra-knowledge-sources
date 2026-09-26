# [Issue #52] offline.py got stuck and shows "CUDA error: no kernel image is available for execution on the device"

source: https://github.com/LLMServe/DistServe/issues/52
state: closed | updated: 2024-12-03T06:48:26Z
labels: 

## 正文

I set up my conda environment according to `environment.yml`, and executed the offline.py by `python offline.py --model /workspace/CXL/DistServe/Llama-2-7b-hf/`
The output shows:
```
INFO 05:29:00 For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-tes
ting/llama-tokenizer' instead of the original tokenizer.
INFO 05:29:00 Initializing placement group
2024-12-02 05:29:02,844 WARNING services.py:1996 -- WARNING: The object store is using /tmp instead of /dev/shm because /dev/shm has only 67104768 bytes available. T$
is will harm performance! You may be able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by pas$
ing '--shm-size=10.24gb' to 'docker run' (or add it to the run_options list in a Ray cluster config). Make sure to set this to more than 30% of available RAM.
2024-12-02 05:29:02,994 INFO worker.py:1743 -- Started a local Ray instance. View the dashboard at 127.0.0.1:8265 
INFO 05:29:04 Initializing context stage LLM engine
INFO 05:29:04 For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-te$
ting/llama-tokenizer' instead of the original tokenizer.
INFO 05:29:04 Initializing decoding stage LLM engine
INFO 05:29:04 For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-te$
ting/llama-tokenizer' instead of the original tokenizer.
INFO 05:29:04 Initializing CONTEXT workers
INFO 05:29:04 Initializing workers
INFO 05:29:04 Initializing DECODING workers
INFO 05:29:04 Initializing workers
INFO 05:29:06 Initializing CONTEXT models
INFO 05:29:06 Initializing DECODING models
(ParaWorker pid=50578) INFO 05:29:06 Worker context.#0 created on host 91467870d497 and gpu #0
(ParaWorker pid=50578) INFO 05:29:06 Find cached model weights in /root/.cache/distserve/models----workspace--CXL--DistServe--Llama-2-7b-hf--/.
INFO 05:29:29 Initializing CONTEXT kvcaches
INFO 05:29:29 Profiling available blocks
INFO 05:29:29 Profiling result: num_gpu_blocks: 2043, num_cpu_blocks: 128
INFO 05:29:29 The engine performs context stage, setting num_cpu_blocks to 1
INFO 05:29:29 Allocating kv cache
INFO 05:29:29 Scheduler: FCFS(max_batch_size=4, max_tokens_per_batch=16384)
INFO 05:29:29 Block manager: BlockManager(max_num_gpu_blocks=2043, max_num_cpu_blocks=1, blocksize=16)
(ParaWorker pid=50578) INFO 05:29:29 (worker context.#0) model /workspace/CXL/DistServe/Llama-2-7b-hf/ loaded
(ParaWorker pid=50578) INFO 05:29:29 runtime peak memory: 12.594 GB
(ParaWorker pid=50578) INFO 05:29:29 total GPU memory: 31.733 GB
(ParaWorker pid=50578) INFO 05:29:29 kv cache size for one token: 0.50000 MB
(ParaWorker pid=50578) INFO 05:29:29 num_gpu_blocks: 2043
(ParaWorker pid=50578) INFO 05:29:29 num_cpu_blocks: 128
(ParaWorker pid=50579) INFO 05:29:06 Worker decoding.#0 created on host 91467870d497 and gpu #2
(ParaWorker pid=50579) INFO 05:29:06 Find cached model weights in /root/.cache/distserve/models----workspace--CXL--DistServe--Llama-2-7b-hf--/.
INFO 05:29:31 Initializing DECODING kvcaches
INFO 05:29:31 Profiling available blocks
INFO 05:29:31 Profiling result: num_gpu_blocks: 2043, num_cpu_blocks: 128
INFO 05:29:31 Allocating kv cache
INFO 05:29:31 Scheduler: FCFS(max_batch_size=4, max_tokens_per_batch=16384)
INFO 05:29:31 Block manager: BlockManager(max_num_gpu_blocks=2043, max_num_cpu_blocks=128, blocksize=16)
INFO 05:29:31 Starting LLMEngine's event loops
INFO 05:29:31 (context) Forwarding with lengths [17, 6, 6, 8]
INFO 05:29:31 (context) 1 waiting, 0 finished but unaccepted, 5 blocks occupied by on-the-fly requests
INFO 05:29:31 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 05:29:31 (decoding) GPU blocks: 0 / 2043 (0.00%) used, (0 swapping out)
INFO 05:29:31 (decoding) 0 unaccepted, 0 waiting, 0 processing
INFO 05:29:32 (context) 1 waiting, 0 finished but unaccepted, 5 blocks occupied by on-the-fly requests
INFO 05:29:32 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 05:29:32 (decoding) GPU blocks: 0 / 2043 (0.00%) used, (0 swapping out)
INFO 05:29:32 (decoding) 0 unaccepted, 0 waiting, 0 processing
INFO 05:29:33 (context) 1 waiting, 0 finished but unaccepted, 5 blocks occupied by on-the-fly requests
INFO 05:29:33 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 05:29:33 (decoding) GPU blocks: 0 / 2043 (0.00%) used, (0 swapping out)
INFO 05:29:33 (decoding) 0 unaccepted, 0 waiting, 0 processing
INFO 05:29:34 (context) 1 waiting, 0 finished but unaccepted, 5 blocks occupied by on-the-fly requests
INFO 05:29:34 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 05:29:34 (decoding) GPU blocks: 0 / 2043 (0.00%) used, (0 swapping out)
INFO 05:29:34 (decoding) 0 unaccepted, 0 waiting, 0 processing
INFO 05:29:35 (context) 1 waiting, 0 finished but unaccepted, 5 blocks occupied by on-the-fly requests
INFO 05:29:35 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 05:29:35 (decoding) GPU blocks: 0 / 2043 (0.00%) used, (0 swapping out)
INFO 05:29:35 (decoding) 0 unaccepted, 0 waiting, 0 processing
INFO 05:29:36 (context) 1 waiting, 0 finished but unaccepted, 5 blocks occupied by on-the-fly requests
INFO 05:29:36 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 05:29:36 (decoding) GPU blocks: 0 / 2043 (0.00%) used, (0 swapping out)
INFO 05:29:36 (decoding) 0 unaccepted, 0 waiting, 0 processing
```
the task is stuck on that waiting stage, so I stop it manually with `ctrl+C` and the traceback shows:
```
^CTraceback (most recent call last):                                                                                                                         [38/1882]
  File "/workspace/CXL/DistServe/examples/offline.py", line 67, in <module>
    outputs = llm.generate(prompts=prompts, sampling_params=sampling_params)
  File "/workspace/CXL/DistServe/distserve/llm.py", line 97, in generate
    return asyncio.run(generate_main())
  File "/opt/conda/envs/distserve/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/opt/conda/envs/distserve/lib/python3.10/asyncio/base_events.py", line 636, in run_until_complete
    self.run_forever()
  File "/opt/conda/envs/distserve/lib/python3.10/asyncio/base_events.py", line 603, in run_forever
    self._run_once()
  File "/opt/conda/envs/distserve/lib/python3.10/asyncio/base_events.py", line 1871, in _run_once
    event_list = self._selector.select(timeout)
  File "/opt/conda/envs/distserve/lib/python3.10/selectors.py", line 469, in select
    fd_event_list = self._selector.poll(timeout, max_ev)
KeyboardInterrupt
(ParaWorker pid=50579) INFO 05:29:31 (worker decoding.#0) model /workspace/CXL/DistServe/Llama-2-7b-hf/ loaded
(ParaWorker pid=50579) INFO 05:29:31 runtime peak memory: 12.594 GB
(ParaWorker pid=50579) INFO 05:29:31 total GPU memory: 31.733 GB
(ParaWorker pid=50579) INFO 05:29:31 kv cache size for one token: 0.50000 MB
(ParaWorker pid=50579) INFO 05:29:31 num_gpu_blocks: 2043
(ParaWorker pid=50579) INFO 05:29:31 num_cpu_blocks: 128
Task exception was never retrieved
future: <Task finished name='Task-19' coro=<LLMEngine.start_all_event_loops() done, defined at /workspace/CXL/DistServe/distserve/engine.py:244> exception=RayTaskErr$
r(RuntimeError)(RuntimeError('CUDA error: no kernel image is available for execution on the device\nCompile with `TORCH_USE_CUDA_DSA` to enable device-side assertion$
.\n'))>
Traceback (most recent call last):
  File "/workspace/CXL/DistServe/distserve/engine.py", line 251, in start_all_event_loops
    await asyncio.gather(
  File "/workspace/CXL/DistServe/distserve/single_stage_engine.py", line 423, in start_event_loop
    await asyncio.gather(event_loop1(), event_loop2())
  File "/workspace/CXL/DistServe/distserve/single_stage_engine.py", line 415, in event_loop1
    await self._step()
  File "/workspace/CXL/DistServe/distserve/single_stage_engine.py", line 355, in _step
    generated_tokens_ids = await self.batches_ret_futures[0]
ray.exceptions.RayTaskError(RuntimeError): ray::ParaWorker.step() (pid=50578, ip=172.17.0.3, actor_id=7881b09e52688af37133678601000000, repr=<distserve.worker.ParaWor
ker object at 0x7f4c64515300>)
  File "/workspace/CXL/DistServe/distserve/worker.py", line 217, in step
    generated_tokens_ids = self.model.forward(
RuntimeError: CUDA error: no kernel image is available for execution on the device
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```
Why this error could happen and how can I fix it? I've already tried to change the torch version and cuda version but neither seems to work for me.
the details of my env are:
```
(distserve) root@91467870d497:/workspace/CXL/DistServe/examples# conda list | grep -E 'cuda|torch'
cuda-cccl                 12.4.127             ha770c72_1    conda-forge
cuda-cccl_linux-64        12.4.127             ha770c72_1    conda-forge
cuda-compiler             12.1.0                        0    nvidia
cuda-cudart               12.1.55                       0    nvidia
cuda-cudart-dev           12.1.55                       0    nvidia
cuda-cudart-static        12.1.55                       0    nvidia
cuda-cuobjdump            12.1.55                       0    nvidia
cuda-cupti                12.1.105                      0    nvidia
cuda-cupti-static         12.4.127             ha770c72_1    conda-forge
cuda-cuxxfilt             12.1.55                       0    nvidia
cuda-driver-dev           12.1.55                       0    nvidia
cuda-libraries            12.1.0                        0    nvidia
cuda-libraries-dev        12.1.0                        0    nvidia
cuda-libraries-static     12.1.0                        0    nvidia
cuda-minimal-build        12.1.0                        0    nvidia
cuda-nvcc                 12.1.66                       0    nvidia
cuda-nvprune              12.1.55                       0    nvidia
cuda-nvrtc                12.1.105                      0    nvidia
cuda-nvrtc-dev            12.1.55                       0    nvidia
cuda-nvrtc-static         12.1.55                       0    nvidia
cuda-nvtx                 12.1.105                      0    nvidia
cuda-opencl               12.4.127                      0    nvidia
cuda-opencl-dev           12.1.56                       0    nvidia
cuda-profiler-api         12.1.55                       0    nvidia
cuda-runtime              12.1.0                        0    nvidia
cuda-version              12.4                 h3060b56_3    conda-forge
cupy-cuda12x              13.3.0                   pypi_0    pypi
nvidia-cuda-cupti-cu12    12.4.127                 pypi_0    pypi
nvidia-cuda-nvrtc-cu12    12.4.127                 pypi_0    pypi
nvidia-cuda-runtime-cu12  12.4.127                 pypi_0    pypi
pytorch                   2.2.2           py3.10_cuda12.1_cudnn8.9.2_0    pytorch
pytorch-cuda              12.1                 ha16c6d3_5    pytorch
pytorch-mutex             1.0                        cuda    pytorch
torch                     2.5.1                    pypi_0    pypi
torchtriton               2.2.0                     py310    pytorch
torchvision               0.20.1                   pypi_0    pypi
``` 
the GPUs are Tesla V100-SXM2-32GB

## 评论 (3)

### interestingLSY · 2024-12-03

When compiling the kernels (or say, building the Docker image), nvcc will target to all visible GPUs. I suspect that you might have used incorrect command-line parameters when building the Docker image, which could result in nvcc not being able to see the GPUs. You can try inserting RUN nvidia-smi into your Dockerfile to confirm whether the GPUs are visible during the build process.



### FuHaoTHU · 2024-12-03

> When compiling the kernels (or say, building the Docker image), nvcc will target to all visible GPUs. I suspect that you might have used incorrect command-line parameters when building the Docker image, which could result in nvcc not being able to see the GPUs. You can try inserting RUN nvidia-smi into your Dockerfile to confirm whether the GPUs are visible during the build process.

Thanks for your reply, but I confirmed that nvidia-smi and nvcc works well in my Dockerfile:
```
(distserve) root@91467870d497:/workspace/CXL/DistServe# nvidia-smi 
Tue Dec  3 03:18:09 2024       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  Tesla V100-SXM2-32GB           Off |   00000000:1A:00.0 Off |                    0 |
| N/A   37C    P0             58W /  300W |    2375MiB /  32768MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  Tesla V100-SXM2-32GB           Off |   00000000:3D:00.0 Off |                    0 |
| N/A   35C    P0             42W /  300W |       3MiB /  32768MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  Tesla V100-SXM2-32GB           Off |   00000000:3E:00.0 Off |                    0 |
| N/A   39C    P0             41W /  300W |       3MiB /  32768MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  Tesla V100-SXM2-32GB           Off |   00000000:88:00.0 Off |                    0 |
| N/A   41C    P0             46W /  300W |       3MiB /  32768MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   4  Tesla V100-SXM2-32GB           Off |   00000000:89:00.0 Off |                    0 |
| N/A   37C    P0             40W /  300W |       3MiB /  32768MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   5  Tesla V100-SXM2-32GB           Off |   00000000:B1:00.0 Off |                    0 |
| N/A   38C    P0             42W /  300W |       3MiB /  32768MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   6  Tesla V100-SXM2-32GB           Off |   00000000:B2:00.0 Off |                    0 |
| N/A   38C    P0             41W /  300W |       3MiB /  32768MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
+-----------------------------------------------------------------------------------------+
(distserve) root@91467870d497:/workspace/CXL/DistServe# python
Python 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.get_arch_list()
['sm_50', 'sm_60', 'sm_61', 'sm_70', 'sm_75', 'sm_80', 'sm_86', 'sm_90']
>>> torch.cuda.is_available()
True
>>> 
(distserve) root@91467870d497:/workspace/CXL/DistServe# nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Tue_Feb__7_19:32:13_PST_2023
Cuda compilation tools, release 12.1, V12.1.66
Build cuda_12.1.r12.1/compiler.32415258_0
```
and I can even run other inference project like this:
```
(distserve) root@91467870d497:/workspace/llama2# python run_inference.py 
Loading tokenizer and model from local path...
Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:02<00:00,  1.08s/it]
GPU 0 - Free memory: 30118 MB
GPU 1 - Free memory: 32490 MB
GPU 2 - Free memory: 32490 MB
GPU 3 - Free memory: 32490 MB
GPU 4 - Free memory: 32490 MB
GPU 5 - Free memory: 32490 MB
GPU 6 - Free memory: 32490 MB
Using GPU 1 for inference
Using CUDA device: cuda:1
Tokenizing input text: Hello, how are you today?
Generating output...
Generated Text:  Hello, how are you today? I am so excited to share with you the newest stamp set from The Ton, "The Trio"! I am also so excited to share with you my first video tutorial. I hope you enjoy it
```
so maybe that's not where the problem is?

### FuHaoTHU · 2024-12-03

> > When compiling the kernels (or say, building the Docker image), nvcc will target to all visible GPUs. I suspect that you might have used incorrect command-line parameters when building the Docker image, which could result in nvcc not being able to see the GPUs. You can try inserting RUN nvidia-smi into your Dockerfile to confirm whether the GPUs are visible during the build process.
> 
> Thanks for your reply, but I confirmed that nvidia-smi and nvcc works well in my Dockerfile:
> 
> ```
> (distserve) root@91467870d497:/workspace/CXL/DistServe# nvidia-smi 
> Tue Dec  3 03:18:09 2024       
> +-----------------------------------------------------------------------------------------+
> | NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.4     |
> |-----------------------------------------+------------------------+----------------------+
> | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
> | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
> |                                         |                        |               MIG M. |
> |=========================================+========================+======================|
> |   0  Tesla V100-SXM2-32GB           Off |   00000000:1A:00.0 Off |                    0 |
> | N/A   37C    P0             58W /  300W |    2375MiB /  32768MiB |      0%      Default |
> |                                         |                        |                  N/A |
> +-----------------------------------------+------------------------+----------------------+
> |   1  Tesla V100-SXM2-32GB           Off |   00000000:3D:00.0 Off |                    0 |
> | N/A   35C    P0             42W /  300W |       3MiB /  32768MiB |      0%      Default |
> |                                         |                        |                  N/A |
> +-----------------------------------------+------------------------+----------------------+
> |   2  Tesla V100-SXM2-32GB           Off |   00000000:3E:00.0 Off |                    0 |
> | N/A   39C    P0             41W /  300W |       3MiB /  32768MiB |      0%      Default |
> |                                         |                        |                  N/A |
> +-----------------------------------------+------------------------+----------------------+
> |   3  Tesla V100-SXM2-32GB           Off |   00000000:88:00.0 Off |                    0 |
> | N/A   41C    P0             46W /  300W |       3MiB /  32768MiB |      0%      Default |
> |                                         |                        |                  N/A |
> +-----------------------------------------+------------------------+----------------------+
> |   4  Tesla V100-SXM2-32GB           Off |   00000000:89:00.0 Off |                    0 |
> | N/A   37C    P0             40W /  300W |       3MiB /  32768MiB |      0%      Default |
> |                                         |                        |                  N/A |
> +-----------------------------------------+------------------------+----------------------+
> |   5  Tesla V100-SXM2-32GB           Off |   00000000:B1:00.0 Off |                    0 |
> | N/A   38C    P0             42W /  300W |       3MiB /  32768MiB |      0%      Default |
> |                                         |                        |                  N/A |
> +-----------------------------------------+------------------------+----------------------+
> |   6  Tesla V100-SXM2-32GB           Off |   00000000:B2:00.0 Off |                    0 |
> | N/A   38C    P0             41W /  300W |       3MiB /  32768MiB |      0%      Default |
> |                                         |                        |                  N/A |
> +-----------------------------------------+------------------------+----------------------+
>                                                                                          
> +-----------------------------------------------------------------------------------------+
> | Processes:                                                                              |
> |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
> |        ID   ID                                                               Usage      |
> |=========================================================================================|
> +-----------------------------------------------------------------------------------------+
> (distserve) root@91467870d497:/workspace/CXL/DistServe# python
> Python 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] on linux
> Type "help", "copyright", "credits" or "license" for more information.
> >>> import torch
> >>> torch.cuda.get_arch_list()
> ['sm_50', 'sm_60', 'sm_61', 'sm_70', 'sm_75', 'sm_80', 'sm_86', 'sm_90']
> >>> torch.cuda.is_available()
> True
> >>> 
> (distserve) root@91467870d497:/workspace/CXL/DistServe# nvcc --version
> nvcc: NVIDIA (R) Cuda compiler driver
> Copyright (c) 2005-2023 NVIDIA Corporation
> Built on Tue_Feb__7_19:32:13_PST_2023
> Cuda compilation tools, release 12.1, V12.1.66
> Build cuda_12.1.r12.1/compiler.32415258_0
> ```
> 
> and I can even run other inference project like this:
> 
> ```
> (distserve) root@91467870d497:/workspace/llama2# python run_inference.py 
> Loading tokenizer and model from local path...
> Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:02<00:00,  1.08s/it]
> GPU 0 - Free memory: 30118 MB
> GPU 1 - Free memory: 32490 MB
> GPU 2 - Free memory: 32490 MB
> GPU 3 - Free memory: 32490 MB
> GPU 4 - Free memory: 32490 MB
> GPU 5 - Free memory: 32490 MB
> GPU 6 - Free memory: 32490 MB
> Using GPU 1 for inference
> Using CUDA device: cuda:1
> Tokenizing input text: Hello, how are you today?
> Generating output...
> Generated Text:  Hello, how are you today? I am so excited to share with you the newest stamp set from The Ton, "The Trio"! I am also so excited to share with you my first video tutorial. I hope you enjoy it
> ```
> 
> so maybe that's not where the problem is?

Solved! It appears that when compiling SwiftTransformer I set the wrong `TORCH_CUDA_ARCH_LIST`. By setting it to `TORCH_CUDA_ARCH_LIST=7.0 7.2 7.5 8.0 8.6 8.7 9.0+PTX` both the offline and online project now works well. Refer to https://github.com/LLMServe/DistServe/issues/21#issue-2394185270.
