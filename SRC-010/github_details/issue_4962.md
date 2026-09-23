# [Issue #4962] [Bug]

source: https://github.com/InternLM/lmdeploy/issues/4962
state: open | updated: 2026-09-15T12:08:37Z
labels: awaiting response

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [ ] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

4卡 nvidia A10 部署报错 

[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][WARN][0914.14:00:25.876730][turbomind.cc:123] `max_context_token_num` is not set, default to 16384.
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][FATAL][0914.14:00:37.807188][cast.cu:264] CUDA error: no kernel image is available for execution on the device
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][FATAL][0914.14:00:37.807196][cast.cu:264] CUDA error: no kernel image is available for execution on the device
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][FATAL][0914.14:00:37.807204][cast.cu:264] CUDA error: no kernel image is available for execution on the device
[TM][FATAL][0914.14:00:37.807214][cast.cu:264] CUDA error: no kernel image is available for execution on the device
*** stacktrace of thread 0x7f30d3fff640 ***
  [ 0] TM_CUDA_CHECK @ cast.cu:264
*** stacktrace of thread 0x7f30d37fe640 ***
  [ 0] TM_CUDA_CHECK @ cast.cu:264
*** stacktrace of thread 0x7f3066283640 ***
  [ 0] TM_CUDA_CHECK @ cast.cu:264
*** stacktrace of thread 0x7f30d88fe640 ***
  [ 0] TM_CUDA_CHECK @ cast.cu:264
/root/startlmdeploy.sh: line 11:     7 Aborted                 (core dumped) lmdeploy serve api_server /root/hf_model/Qwen/Qwen3.8-27B-FP8 --model-name pkumlm_txt --backend turbomind --server-port 8000 --api-keys pkulesbrain_mlm_txt --model-format fp8 --reasoning-parser default --tool-call-parser qwen3coder --enable-prefix-caching --eager-mode --rope-scaling-factor 0.2 --session-len 16384 --log-level REQUEST --max-batch-size 2 --tp 4 --cache-max-entry-count 0.85

### Reproduction

<img width="2722" height="768" alt="Image" src="https://github.com/user-attachments/assets/1e30cea1-5fd3-4f67-8890-c9a3f615f0f2" />

### Environment

```Shell
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A10                     Off |   00000000:31:00.0 Off |                    0 |
|  0%   76C    P0             99W /  150W |    6931MiB /  23028MiB |     15%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA A10                     Off |   00000000:4B:00.0 Off |                    0 |
|  0%   67C    P0             69W /  150W |    1469MiB /  23028MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA A10                     Off |   00000000:98:00.0 Off |                    0 |
|  0%   61C    P0             64W /  150W |    1469MiB /  23028MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA A10                     Off |   00000000:B1:00.0 Off |                    0 |
|  0%   64C    P0             67W /  150W |    1469MiB /  23028MiB |      7%      Default |
|                                         |                        |                  N/A |
```

### Error traceback

```Shell
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][WARN][0914.14:00:25.876730][turbomind.cc:123] `max_context_token_num` is not set, default to 16384.
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][FATAL][0914.14:00:37.807188][cast.cu:264] CUDA error: no kernel image is available for execution on the device
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][FATAL][0914.14:00:37.807196][cast.cu:264] CUDA error: no kernel image is available for execution on the device
[TM][WARN] Invalid TM_LOG_LEVEL='REQUEST'. Using default level.
[TM][FATAL][0914.14:00:37.807204][cast.cu:264] CUDA error: no kernel image is available for execution on the device
[TM][FATAL][0914.14:00:37.807214][cast.cu:264] CUDA error: no kernel image is available for execution on the device
*** stacktrace of thread 0x7f30d3fff640 ***
  [ 0] TM_CUDA_CHECK @ cast.cu:264
*** stacktrace of thread 0x7f30d37fe640 ***
  [ 0] TM_CUDA_CHECK @ cast.cu:264
*** stacktrace of thread 0x7f3066283640 ***
  [ 0] TM_CUDA_CHECK @ cast.cu:264
*** stacktrace of thread 0x7f30d88fe640 ***
  [ 0] TM_CUDA_CHECK @ cast.cu:264
/root/startlmdeploy.sh: line 11:     7 Aborted                 (core dumped) lmdeploy serve api_server /root/hf_model/Qwen/Qwen3.8-27B-FP8 --model-name pkumlm_txt --backend turbomind --server-port 8000 --api-keys pkulesbrain_mlm_txt --model-format fp8 --reasoning-parser default --tool-call-parser qwen3coder --enable-prefix-caching --eager-mode --rope-scaling-factor 0.2 --session-len 16384 --log-level REQUEST --max-batch-size 2 --tp 4 --cache-max-entry-count 0.85
```

## 评论 (3)

### lvhan028 · 2026-09-14

使用的 lmdeploy 版本是哪个呢？

### lvhan028 · 2026-09-15

You can try v0.17.0

### github-actions[bot] · 2026-09-23

This issue is marked as stale because it has been marked as invalid or awaiting response for 7 days without any further response. It will be closed in 5 days if the stale label is not removed or if there is no further response.
