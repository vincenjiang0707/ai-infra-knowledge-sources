# [Issue #238] [ Incompatible CUDA compute capability ] pulse_test does not support CUDA Compute Capability 12 (e.g. RTX 5090)

source: https://github.com/NVIDIA/DCGM/issues/238
state: open | updated: 2025-11-17T14:45:20Z
labels: 

## 正文

### `pulse_test` does not support CUDA Compute Capability 12 (e.g. RTX 5090)

Hi DCGM team,

We are using the latest DCGM version (`4.2.3`) and encountered an issue when running `pulse_test` diagnostics on an **RTX 5090** GPU.

---

### **System Information:**

- **GPU:** NVIDIA RTX 5090  
- **Driver Version:** 570.153.02  
- **CUDA Version:** 12.8  
- **DCGM Version:** 4.2.3  

---

### **Problem:**

When running the following command:

```bash
dcgmi diag -r 4 -c dcgmi.config
```

With the following `dcgmi.config` contents:

```yaml
version: "3.1.7"
spec: dcgm-diag-v1
skus:
  - name: GeForce RTX 5090
    id: 2b85
    pulse_test:
      is_allowed: true
```

We receive the following error in the log:

```
[[pulse_test]] Incompatible CUDA compute capability major version: 12
```

---

### **Related `nvvs.log` Snippet:**

```
2025-06-27 06:32:30.783 DEBUG [71830:71830] Test pulse_test start [/builds/dcgm/dcgm/nvvs/src/TestFramework.cpp:871] [TestFramework::GoList]
...
2025-06-27 06:32:30.806 ERROR [71830:71830] [[pulse_test]] Incompatible CUDA compute capability major version: 12 [/builds/dcgm/dcgm/dcgm_private/nvvs/plugin_src/pulsetest/src/PulseTestPlugin.cpp:599] [PulseTestPlugin::PopulateArgV]
...
2025-06-27 06:32:30.964 DEBUG [71830:71830] Cannot read the max HBM operating temperature for gpuId 7: Success: INT64 value is blank. [/builds/dcgm/dcgm/nvvs/src/DcgmRecorder.cpp:1265] [DcgmRecorder::CheckHBMErrorFields]
2025-06-27 06:32:33.519 DEBUG [71830:71830] Test pulse_test had result 2. Configless is false [/builds/dcgm/dcgm/nvvs/src/TestFramework.cpp:895] [TestFramework::GoList]
```

---

### **Questions:**

1. Is there a plan to support **Compute Capability 12.0** in the `pulse_test` plugin?
2. Is there any **workaround** or **timeline** for full **CC 12.x** support in DCGM diagnostics?

---

Thanks for your support and development of DCGM!


## 评论 (2)

### StickOnAStick · 2025-09-17

Running into the same issue with 2x a16's w/ **Cuda 13.0**

```bash
$ dcgmi diag -r 4
Detected unsupported Cuda version
Detected unsupported Cuda version
$ nvidia-smi
Wed Sep 17 13:51:45 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.07              Driver Version: 580.82.07      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A16                     On  |   00000000:85:00.0 Off |                    0 |
|  0%   30C    P8             12W /   62W |      14MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA A16                     On  |   00000000:86:00.0 Off |                    0 |
|  0%   27C    P8             11W /   62W |      14MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA A16                     On  |   00000000:87:00.0 Off |                    0 |
|  0%   33C    P8             12W /   62W |      14MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA A16                     On  |   00000000:88:00.0 Off |                    0 |
|  0%   35C    P8             12W /   62W |      14MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA A16                     On  |   00000000:C5:00.0 Off |                    0 |
|  0%   30C    P8             12W /   62W |      14MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA A16                     On  |   00000000:C6:00.0 Off |                    0 |
|  0%   28C    P8             12W /   62W |      14MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA A16                     On  |   00000000:C7:00.0 Off |                    0 |
|  0%   35C    P8             12W /   62W |      14MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA A16                     On  |   00000000:C8:00.0 Off |                    0 |
|  0%   35C    P8             12W /   62W |      14MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1774      G   /usr/lib/xorg/Xorg                        4MiB |
|    1   N/A  N/A            1774      G   /usr/lib/xorg/Xorg                        4MiB |
|    2   N/A  N/A            1774      G   /usr/lib/xorg/Xorg                        4MiB |
|    3   N/A  N/A            1774      G   /usr/lib/xorg/Xorg                        4MiB |
|    4   N/A  N/A            1774      G   /usr/lib/xorg/Xorg                        4MiB |
|    5   N/A  N/A            1774      G   /usr/lib/xorg/Xorg                        4MiB |
|    6   N/A  N/A            1774      G   /usr/lib/xorg/Xorg                        4MiB |
|    7   N/A  N/A            1774      G   /usr/lib/xorg/Xorg                        4MiB |
+-----------------------------------------------------------------------------------------+
```



### sebito91 · 2025-11-17

There is a v4.4.2 which was recently [released](https://docs.nvidia.com/datacenter/dcgm/latest/release-notes/changelog.html#id2), might want to try with that version? It doesn't list your GPU model but it does support other recent Blackwell GPUs.
