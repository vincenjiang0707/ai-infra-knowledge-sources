# [Issue #2371] [Issue]: allGather tries to run with undefined protocol

source: https://github.com/NVIDIA/nccl/issues/2371
state: closed | updated: 2026-09-14T04:36:14Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs


`NCCL_DEBUG_FILE=ncclDebug.%h.%p` is broken on Windows, unable to provide ISOLATED log files per process. Attached is merged output stream from process group instead.

[ncclDebug.txt](https://github.com/user-attachments/files/31417496/ncclDebug.txt)

`NCCL_TOPO_DUMP_FILE=ncclSystem.txt` is broken on Windows, unable to provide topology dump.

### Steps to Reproduce the Issue

Trigger the execution of `allGather` in an MSVC build on Windows with Blackwell.

Reproduced specifically with https://github.com/SystemPanic/vllm-windows/releases/tag/v0.26.0 trying to run any model with `--tensor-parallel-size 2`. Unlike the repo instructions indicate, I was using ref 7b83616df3ae082a1f32bb74c27458bfe8153a13 of this repository, built with CUDA 13.3 for CUDA_ARCH 120. Not the outdated nccl-windows fork!

I was unable to test older versions.

### NCCL Version

2.31.2+cuda13.3

### Your platform details

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 596.51                 Driver Version: 596.51         CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 2000 Blac...  WDDM  |   00000000:41:00.0 Off |                    0 |
| 30%   37C    P8              4W /   70W |       0MiB /  16311MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 2000 Blac...  WDDM  |   00000000:61:00.0 Off |                    0 |
| 30%   37C    P8              7W /   70W |    1049MiB /  16311MiB |      3%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

ReBAR OFF. GPUs are on same PCIe switch, but isolated due to Windows WDDM.

Windows platform, bare metal.

### Error Message & Behavior

No previous warnings - logfile attached above is complete view of all NCCL output up to the point of crash.

An `allReduce` dispatch had succeeded just before the faulting `allGather`.

Integer division by zero in https://github.com/NVIDIA/nccl/blob/7b83616df3ae082a1f32bb74c27458bfe8153a13/src/enqueue/enqueue.cc#L2354

Tracing the state backwards with debugger in debug build revealed `loopSize = 0`, caused by `chunkSize = 0`, caused by `grainSize = 0xFFFFFFFFFFFFFFFF`, caused by `info->protocol = -1`. So a task where the protocol selection had failed for unknown reasons, was allowed to fall through to `calcCollChunking`. I was unable to follow the stack further back past the queue.

## 评论 (5)

### xiaofanl-nvidia · 2026-09-08

@Ext3h to confirm, are you using NCCL on native windows platforms? Not WSL, right? 

++ @nv-udeodhar 

### Ext3h · 2026-09-08

@xiaofanl-nvidia correct, native NCCL on Windows. Even though I'm aborting that experiment due to lack of maturity of the NCCL and the minimal multi-GPU support of the CUDA platform on Windows at the end of the week.

### nv-udeodhar · 2026-09-09

@Ext3h This issue has been fixed in the latest dev branch. Specifically in this commit: https://github.com/NVIDIA/nccl/commit/cc51d9d33dd4e2ea80c83212d207e934f1cf714e
Please confirm that it works for you as well.

### xiaofanl-nvidia · 2026-09-09

@Ext3h thank you for the feedback. NCCL support for native windows is indeed still experimental. We do have some internal bug fixes that we could share with you if you are interested. They are not merged because of regression risks for Linux and reviewer bandwidth limitations. 

### xiaofanl-nvidia · 2026-09-14

Closing as this specific issue has been fixed. Feel free to still reach out if there are other issues with NCCL on Windows! Thanks for trying it out! 
