# [Issue #239] dcgmproftester -t 1007 no longer shows gflops

source: https://github.com/NVIDIA/DCGM/issues/239
state: open | updated: 2026-09-01T09:43:14Z
labels: 

## 正文

[diag-skus.yaml.in](https://github.com/NVIDIA/DCGM/blob/master/nvvs/diag-skus.yaml.in) contains assorted comments like "# dcgmproftester -t 1007 measures at ~41000, multiply by .75 to get ~30750", and in the past I've used the same recipe to generate config files for GeForce GPUs. However, at some point this command seems to have stopped reporting the gflops achieved.

## Actual behaviour

With latest version 4.2.3 (I've also seen similar behaviour with 3.3.7 but haven't bisected beyond that):

```
$ docker run --net=host -t --runtime=nvidia --gpus=all --rm --entrypoint /usr/bin/dcgmproftester12 nvcr.io/nvidia/cloud-native/dcgm:4.2.3-1-ubuntu22.04 -t 1007 --no-dcgm-validation
Skipping CreateDcgmGroups() since DCGM validation is disabled
Worker 0:0[1007]: Fp32EngineActive: target 0.00, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Fp32EngineActive: target max, dcgm 0
Worker 0:0[1007]: Message: std::setenv successfully set CUDA_VISIBLE_DEVICES to GPU-8a210f77-19be-2067-8fa1-11463df32fe2
Bus ID 00000000:81:00.0 mapped to cuda device ID 0
DCGM CudaContext Init completed successfully.

CU_DEVICE_ATTRIBUTE_MAX_THREADS_PER_MULTIPROCESSOR: 1536
CUDA_VISIBLE_DEVICES: GPU-8a210f77-19be-2067-8fa1-11463df32fe2
CU_DEVICE_ATTRIBUTE_MULTIPROCESSOR_COUNT: 48
CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_MULTIPROCESSOR: 102400
CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR: 8
CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR: 6
CU_DEVICE_ATTRIBUTE_GLOBAL_MEMORY_BUS_WIDTH: 256
CU_DEVICE_ATTRIBUTE_MEMORY_CLOCK_RATE: 9501
Max Memory bandwidth: 608064000000 bytes (608.1 GiB)
CU_DEVICE_ATTRIBUTE_ECC_SUPPORT: false
GPU 0, TestField 1007 test PASSED.
All Tests Passed.
```

## Expected behaviour

3.1.3 used to report the gflops:

```
$ docker run --net=host -t --runtime=nvidia --gpus=all --rm --entrypoint /usr/bin/dcgmproftester12 nvcr.io/nvidia/cloud-native/dcgm:3.1.3-1-ubuntu20.04 -t 1007 --no-dcgm-validation
Skipping CreateDcgmGroups() since DCGM validation is disabled
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (0.0 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12238.2 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12254.6 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12258.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12255.3 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12254.9 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12257.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12259.6 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12255.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12255.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12254.6 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12250.0 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12252.3 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12253.5 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12254.7 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12252.2 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12252.2 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12251.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12251.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12249.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12251.3 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12251.5 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12253.6 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12255.5 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12250.8 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12249.4 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12257.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12257.1 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12253.9 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12253.7 gflops).
Worker 0:0[1007]: Fp32EngineActive: generated ???, dcgm 0.000 (12251.4 gflops).
Worker 0:0[1007]: Message: DCGM CudaContext Init completed successfully.

CU_DEVICE_ATTRIBUTE_MAX_THREADS_PER_MULTIPROCESSOR: 1536
CUDA_VISIBLE_DEVICES: GPU-8a210f77-19be-2067-8fa1-11463df32fe2
CU_DEVICE_ATTRIBUTE_MULTIPROCESSOR_COUNT: 48
CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_MULTIPROCESSOR: 102400
CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR: 8
CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR: 6
CU_DEVICE_ATTRIBUTE_GLOBAL_MEMORY_BUS_WIDTH: 256
CU_DEVICE_ATTRIBUTE_MEMORY_CLOCK_RATE: 9501
Max Memory bandwidth: 608064000000 bytes (608.1 GiB)
CU_DEVICE_ATTRIBUTE_ECC_SUPPORT: false
GPU 0, TestField 1007 test PASSED.
All Tests Passed.
```

## 评论 (2)

### bmerry · 2026-08-26

Is there any appetite for addressing this? Will it help if we make a PR? We're no longer able to run DCGM 3.x Docker images because they don't support CUDA 13, which is making it difficult for us to write config files for new GPUs.

### EatonEmmerich · 2026-09-01

It seems that this functionality used to be the default and now it's behind the `--cublas` flag
