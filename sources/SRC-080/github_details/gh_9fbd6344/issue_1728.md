# [Issue #1728] Where can I get a model-opt that is compatible with drive Thor-U ?

source: https://github.com/NVIDIA/Model-Optimizer/issues/1728
state: closed | updated: 2026-07-16T04:05:16Z
labels: stale, waiting for feedback

## 正文

My board is drive thor-u (drive os is 7030)
I want to run autotune(onnx) on the board.

Where can I get a model-opt that is compatible with drive Thor-U ?

## 评论 (9)

### kevalmorabia97 · 2026-06-15

What error do you get when you try to install modelopt on your machine?

```
pip install nvidia-modelopt[onnx]
```

### lix19937 · 2026-06-16

@kevalmorabia97 I will try it.
BTW, Is Autotune planned to be embedded into trtexec or provide an executable program to run on the soc-tegra-board ? 
 

### kevalmorabia97 · 2026-06-16

I'm not sure about that. Generally best way is to install modelopt in your system of choice and run auto-tune from it. Does that work for you?

### lix19937 · 2026-06-16

@kevalmorabia97  `pip install nvidia-modelopt` passed, but when run    

(mopt) nvidia@tegra-ubuntu:/data/lix$ python3  ./test.py 

```
2026-06-16 03:57:07.888021326 [W:onnxruntime:Default, device_discovery.cc:325 DiscoverDevicesForPlatform] GPU device discovery failed: device_discovery.cc:92 ReadFileContents Failed to open file: "/sys/class/drm/card0/device/vendor"
/data/anaconda3/envs/mopt/lib/python3.12/site-packages/torch/cuda/__init__.py:187: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 12080). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:119.)
  return torch._C._cuda_getDeviceCount() > 0
2026-06-16 03:57:09,640 - [modelopt][onnx] - ERROR - TensorRT initialization failed: PyTorch with CUDA support not available. Please install torch with CUDA: pip install torch
Traceback (most recent call last):

``` 

with `pip install nvidia-modelopt`, get torch cpu version ,but no gpu-aarch64 version 

### kevalmorabia97 · 2026-06-16

Can you install pytorch separately before or after installing modelopt. Or see if there is a pre-built pytorch with cuda docker image compatible with your machine?

### lix19937 · 2026-06-16

@kevalmorabia97 Thanks, I can not get drive os 7030 thor-u aarch64 docker image, Here I just choose `TrtExecBenchmark` to bypass the torch-gpu cu13 aarch64 issue.  Running as follow:    

```
(mopt) nvidia@tegra-ubuntu:/ota/lix$ python3  ./test.py 
2022-01-09 06:56:53.152540056 [W:onnxruntime:Default, device_discovery.cc:325 DiscoverDevicesForPlatform] GPU device discovery failed: device_discovery.cc:92 ReadFileContents Failed to open file: "/sys/class/drm/card0/device/vendor"
/ota/gw00348951/mopt/lib/python3.12/site-packages/torch/cuda/__init__.py:187: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 12080). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:119.)
  return torch._C._cuda_getDeviceCount() > 0
2022-01-09 06:56:54,958 - [modelopt][onnx] - INFO - Trtexec benchmark initialized
2022-01-09 06:56:54,958 - [modelopt][onnx] - INFO - Loading model: ResNet50.onnx
2022-01-09 06:56:55,025 - [modelopt][onnx] - INFO - Initializing autotuner (quant_type=int8, default_dq_dtype=float32)
2022-01-09 06:56:55,035 - [modelopt][onnx] - INFO - Initializing autotuner
2022-01-09 06:56:55,035 - [modelopt][onnx] - INFO - Discovering optimization regions
2022-01-09 06:56:55,036 - [modelopt][onnx] - INFO - Phase 1: Bottom-up partitioning
2022-01-09 06:56:55,037 - [modelopt][onnx] - INFO - Partitioning graph (176 nodes)
2022-01-09 06:56:55,038 - [modelopt][onnx] - INFO - Partitioning complete: 21 regions, 176/176 nodes (100.0%)
2022-01-09 06:56:55,038 - [modelopt][onnx] - INFO - Phase 1 complete: 21 regions, 176/176 nodes (100.0%)
2022-01-09 06:56:55,038 - [modelopt][onnx] - INFO - Phase 2: Top-down refinement
2022-01-09 06:56:55,050 - [modelopt][onnx] - INFO - Phase 2 complete: refined 16/21 regions
2022-01-09 06:56:55,051 - [modelopt][onnx] - INFO - Discovery complete: 53 regions (37 LEAF, 16 COMPOSITE, 0 ROOT)
2022-01-09 06:56:55,051 - [modelopt][onnx] - INFO - Starting new autotuning session
2022-01-09 06:56:55,051 - [modelopt][onnx] - INFO - Ready to profile 53 regions
2022-01-09 06:56:55,051 - [modelopt][onnx] - INFO - Measuring baseline (no Q/DQ)
2022-01-09 06:56:55,419 - [modelopt][onnx] - INFO - Exported baseline model with 0 Q/DQ pairs  → out/baseline.onnx
2022-01-09 06:57:16,158 - [modelopt][onnx] - INFO - TrtExec benchmark (median): 1.18 ms
2022-01-09 06:57:16,158 - [modelopt][onnx] - INFO - Baseline latency: 1.177 ms
2022-01-09 06:57:16,158 - [modelopt][onnx] - INFO - Baseline: 1.18 ms
2022-01-09 06:57:16,158 - [modelopt][onnx] - INFO - Starting region profiling (30 schemes per region)
2022-01-09 06:57:16,158 - [modelopt][onnx] - INFO - Region 1/53 (ID=0, level=0)
2022-01-09 06:57:16,159 - [modelopt][onnx] - INFO - Profiling region 0 [level 0, size4, starting fresh]
2022-01-09 06:57:16,159 - [modelopt][onnx] - INFO - Scheme #1: generated new scheme (0 Q/DQ points)
2022-01-09 06:57:16,331 - [modelopt][onnx] - INFO - Exported INT8 model with 0 Q/DQ pairs 
2022-01-09 06:57:25,267 - [modelopt][onnx] - INFO - TrtExec benchmark (median): 1.17 ms
2022-01-09 06:57:25,267 - [modelopt][onnx] - INFO - Scheme #1: 1.172 ms (1.00x speedup)
2022-01-09 06:57:25,268 - [modelopt][onnx] - INFO - Scheme #2: generated new scheme (1 Q/DQ points)
2022-01-09 06:57:25,528 - [modelopt][onnx] - INFO - Exported INT8 model with 2 Q/DQ pairs 
2022-01-09 06:57:34,588 - [modelopt][onnx] - INFO - TrtExec benchmark (median): 1.18 ms
2022-01-09 06:57:34,589 - [modelopt][onnx] - INFO - Scheme #2: 1.180 ms (1.00x speedup)

``` 

### lix19937 · 2026-06-16

Some tips:   
https://discuss.pytorch.org/t/unable-to-access-cuda-using-torch-on-aarch64-architecture/185741/4     
https://forums.developer.nvidia.com/t/onnx-runtime-gpu/327411    

### github-actions[bot] · 2026-07-01

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-07-16

This issue was closed because it has been 14 days without activity since it has been marked as stale.
