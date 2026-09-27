# [Issue #283] NV_ERR_STATE_IN_USE errors when running DCGM on an empty ADA6000

source: https://github.com/NVIDIA/DCGM/issues/283
state: closed | updated: 2026-03-18T15:15:07Z
labels: 

## 正文

Hi :)

Please excuse if this error isn't in the right project, I'm not quite sure about it. I'm working on upgrading our GPU fleet to latest nvidia-open and cuda-drivers in a Kubernetes environment and since that I oberve the DCGM exporter crashlooping based on a an error. Errors in dmesg:

```
[Thu Mar  5 16:55:27 2026] NVRM: GPU0 nvCheckOkFailedNoLog: Check failed: State in use [NV_ERR_STATE_IN_USE] (0x00000063) returned from pRmApi->Control(pRmApi, pClient->hClient, hObject, NVB0CC_CTRL_CMD_INTERNAL_ALLOC_PMA_STREAM, &internalParams, sizeof(internalParams)) @ kern_profiler_v2_ctrl.c:315
```

The node doesn't have any workloads running on it and the only thing that interacts with the GPU is the NVIDIA dcgm exporter https://github.com/NVIDIA/dcgm-exporter.

```
/# nvidia-smi
Thu Mar  5 17:52:45 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.48.01              Driver Version: 590.48.01      CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:01:00.0 Off |                  Off |
| 30%   31C    P8             23W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

```

/# apt list --installed | grep datacenter
datacenter-gpu-manager-4-core/unknown,now 1:4.5.2-1 amd64 [installed,automatic]
datacenter-gpu-manager-4-cuda13/unknown,now 1:4.5.2-1 amd64 [installed]
datacenter-gpu-manager-4-proprietary-cuda13/unknown,now 1:4.5.2-1 amd64 [installed,automatic]
datacenter-gpu-manager-4-proprietary/unknown,now 1:4.5.2-1 amd64 [installed,automatic]
```

```
● nvidia-dcgm.service - NVIDIA DCGM service
     Loaded: loaded (/usr/lib/systemd/system/nvidia-dcgm.service; enabled; preset: enabled)
     Active: active (running) since Thu 2026-03-05 14:52:58 UTC; 3h 1min ago
 Invocation: 8ea0709a4bde4795b932f78b679b8a6a
   Main PID: 1191 (nv-hostengine)
      Tasks: 18 (limit: 38469)
     Memory: 434M (peak: 435.9M)
        CPU: 1min 17.401s
     CGroup: /system.slice/nvidia-dcgm.service
             └─1191 /usr/bin/nv-hostengine -n --service-account nvidia-dcgm

Mar 05 14:52:58 gpu-ada-o systemd[1]: Started nvidia-dcgm.service - NVIDIA DCGM service.
Mar 05 14:52:58 gpu-ada-o nv-hostengine[1191]: DCGM initialized
Mar 05 14:52:58 gpu-ada-o nv-hostengine[1191]: Started host engine version 4.5.2 using port number: 5555
```

## 评论 (1)

### m3co-code · 2026-03-18

Ok the issue was simply multiple processes trying to get metrics from the dcgm exporter. Closing the issue as this is a known limitation.
