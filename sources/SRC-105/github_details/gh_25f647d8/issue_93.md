# [Issue #93] Not able to get DCGM stats for MIG partitions

source: https://github.com/NVIDIA/DCGM/issues/93
state: closed | updated: 2025-08-18T22:53:00Z
labels: documentation, question

## 正文

Hi,

I have a server with 4 A100-80GB GPUs and each GPU is partitioned to 3g.40gb, 2g.20gb and 2x 1.10gb partition. All the documentation at the following links suggests that we can use DCGM usage metrics for MIG partitions, but I have not been able to get any despite running the latest NVIDIA drivers/535.x, CUDA/12.2, DCGM/3.1.8 ... etc

https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-profiles
https://docs.nvidia.com/datacenter/dcgm/latest/gpu-telemetry/dcgm-exporter.html?highlight=mig

I've tried with older NVIDIA drivers/495.x, CUDA/11.5, DCGM/2.4.1  with no luck.


1) I submitted a job using Slurm to use one 1g.10gb partition
```
$ nvidia-smi
Thu Aug  3 18:05:19 2023
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.54.03              Driver Version: 535.54.03    CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A100-SXM4-80GB          On  | 00000000:01:00.0 Off |                   On |
| N/A   23C    P0              65W / 500W |     87MiB / 81920MiB |     N/A      Default |
|                                         |                      |              Enabled |
+-----------------------------------------+----------------------+----------------------+
|   1  NVIDIA A100-SXM4-80GB          On  | 00000000:41:00.0 Off |                   On |
| N/A   23C    P0              68W / 500W |     87MiB / 81920MiB |     N/A      Default |
|                                         |                      |              Enabled |
+-----------------------------------------+----------------------+----------------------+
|   2  NVIDIA A100-SXM4-80GB          On  | 00000000:81:00.0 Off |                   On |
| N/A   22C    P0              58W / 500W |     87MiB / 81920MiB |     N/A      Default |
|                                         |                      |              Enabled |
+-----------------------------------------+----------------------+----------------------+
|   3  NVIDIA A100-SXM4-80GB          On  | 00000000:C1:00.0 Off |                   On |
| N/A   22C    P0              69W / 500W |     87MiB / 81920MiB |     N/A      Default |
|                                         |                      |              Enabled |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| MIG devices:                                                                          |
+------------------+--------------------------------+-----------+-----------------------+
| GPU  GI  CI  MIG |                   Memory-Usage |        Vol|      Shared           |
|      ID  ID  Dev |                     BAR1-Usage | SM     Unc| CE ENC DEC OFA JPG    |
|                  |                                |        ECC|                       |
|==================+================================+===========+=======================|
|  0   13   0   0  |              12MiB /  9728MiB  | 14      0 |  1   0    0    0    0 |
|                  |               0MiB / 16383MiB  |           |                       |
+------------------+--------------------------------+-----------+-----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```


DCGMI seems to see all the partitions
```
$ dcgmi --version

dcgmi  version: 3.1.8

$ dcgmi discovery -c
+-------------------+--------------------------------------------------------------------+
| Instance Hierarchy                                                                     |
+===================+====================================================================+
| GPU 0             | GPU GPU-73fa6136-5962-8760-3543-871462d498eb (EntityID: 0)         |
| -> I 0/1          | GPU Instance (EntityID: 3)                                         |
|    -> CI 0/1/0    | Compute Instance (EntityID: 3)                                     |
| -> I 0/5          | GPU Instance (EntityID: 2)                                         |
|    -> CI 0/5/0    | Compute Instance (EntityID: 2)                                     |
| -> I 0/13         | GPU Instance (EntityID: 0)                                         |
|    -> CI 0/13/0   | Compute Instance (EntityID: 0)                                     |
| -> I 0/14         | GPU Instance (EntityID: 1)                                         |
|    -> CI 0/14/0   | Compute Instance (EntityID: 1)                                     |
+-------------------+--------------------------------------------------------------------+
| GPU 1             | GPU GPU-42508fe9-5646-a97b-1b99-890122f528e4 (EntityID: 1)         |
| -> I 1/1          | GPU Instance (EntityID: 10)                                        |
|    -> CI 1/1/0    | Compute Instance (EntityID: 10)                                    |
| -> I 1/5          | GPU Instance (EntityID: 9)                                         |
|    -> CI 1/5/0    | Compute Instance (EntityID: 9)                                     |
| -> I 1/13         | GPU Instance (EntityID: 7)                                         |
|    -> CI 1/13/0   | Compute Instance (EntityID: 7)                                     |
| -> I 1/14         | GPU Instance (EntityID: 8)                                         |
|    -> CI 1/14/0   | Compute Instance (EntityID: 8)                                     |
+-------------------+--------------------------------------------------------------------+
| GPU 2             | GPU GPU-413d0c6a-014f-3d2d-d675-81854947e47c (EntityID: 2)         |
| -> I 2/2          | GPU Instance (EntityID: 17)                                        |
|    -> CI 2/2/0    | Compute Instance (EntityID: 17)                                    |
| -> I 2/3          | GPU Instance (EntityID: 16)                                        |
|    -> CI 2/3/0    | Compute Instance (EntityID: 16)                                    |
| -> I 2/9          | GPU Instance (EntityID: 14)                                        |
|    -> CI 2/9/0    | Compute Instance (EntityID: 14)                                    |
| -> I 2/10         | GPU Instance (EntityID: 15)                                        |
|    -> CI 2/10/0   | Compute Instance (EntityID: 15)                                    |
+-------------------+--------------------------------------------------------------------+
| GPU 3             | GPU GPU-4dd9d50d-018e-f159-98a7-aa495640153b (EntityID: 3)         |
| -> I 3/2          | GPU Instance (EntityID: 24)                                        |
|    -> CI 3/2/0    | Compute Instance (EntityID: 24)                                    |
| -> I 3/3          | GPU Instance (EntityID: 23)                                        |
|    -> CI 3/3/0    | Compute Instance (EntityID: 23)                                    |
| -> I 3/9          | GPU Instance (EntityID: 21)                                        |
|    -> CI 3/9/0    | Compute Instance (EntityID: 21)                                    |
| -> I 3/10         | GPU Instance (EntityID: 22)                                        |
|    -> CI 3/10/0   | Compute Instance (EntityID: 22)                                    |
+-------------------+--------------------------------------------------------------------+
```

2) I created group ID 2 to monitor the relevant MIG device (instance 3)
``` 
$ dcgmi group --list
+-------------------+----------------------------------------------------------+
| GROUPS                                                                       |
| 3 groups found.                                                              |
+===================+==========================================================+
| Groups            |                                                          |
| -> 0              |                                                          |
|    -> Group ID    | 0                                                        |
|    -> Group Name  | DCGM_ALL_SUPPORTED_GPUS                                  |
|    -> Entities    | GPU 0, GPU 1, GPU 2, GPU 3                               |
| -> 1              |                                                          |
|    -> Group ID    | 1                                                        |
|    -> Group Name  | DCGM_ALL_SUPPORTED_NVSWITCHES                            |
|    -> Entities    | None                                                     |
| -> 2              |                                                          |
|    -> Group ID    | 2                                                        |
|    -> Group Name  | 952404                                                   |
|    -> Entities    | GPU_CI 3                                                 |
+-------------------+----------------------------------------------------------+
```

3) I enabled monitoring and started collecting stats
```
dcgmi stats -g 2 -e
dcgmi stats -g 2 -s $SLURM_JOBID
```

4) I ran a GPU calculation

5) I monitored the usage as the calculation is running, but no relevant stats appear.

```
$ dcgmi stats -g 2 -j $SLURM_JOBID
Successfully retrieved statistics for job: 952404.
+------------------------------------------------------------------------------+
| Summary                                                                      |
+====================================+=========================================+
|-----  Execution Stats  ------------+-----------------------------------------|
| Start Time                         | Thu Aug  3 16:35:00 2023                |
| End Time                           | Thu Aug  3 18:21:32 2023                |
| Total Execution Time (sec)         | 6391.9                                  |
| No. of Processes                   | 0                                       |
+-----  Performance Stats  ----------+-----------------------------------------+
| Energy Consumed (Joules)           | Not Specified                           |
| Power Usage (Watts)                | Avg: N/A, Max: N/A, Min: N/A            |
| Max GPU Memory Used (bytes)        | 0                                       |
| Clocks and PCIe Performance        | Available per GPU in verbose mode       |
+-----  Event Stats  ----------------+-----------------------------------------+
| Single Bit ECC Errors              | Not Specified                           |
| Double Bit ECC Errors              | Not Specified                           |
| PCIe Replay Warnings               | Not Specified                           |
| Critical XID Errors                | 0                                       |
+-----  Slowdown Stats  -------------+-----------------------------------------+
| Due to - Power (%)                 | Not Supported                           |
|        - Thermal (%)               | Not Supported                           |
|        - Reliability (%)           | Not Supported                           |
|        - Board Limit (%)           | Not Supported                           |
|        - Low Utilization (%)       | Not Supported                           |
|        - Sync Boost (%)            | Not Specified                           |
+-----  Overall Health  -------------+-----------------------------------------+
| Overall Health                     | Healthy                                 |
+------------------------------------+-----------------------------------------+
```

I would appreciate it if you would let me know if it is still possible to get statistics for MIG partitions. My main interest is to get the GPU memory utilization for every Slurm job so that I can advise users to submit their jobs to a MIG partition of the proper size. If there are other tools to accomplish the same task, I would love to learn about them as well.

Thanks.



Perhaps other relevant info:
====
OS:
- RHEL/Rocky 8.5 - 4.18.0-348.7.1.el8_5.x86_64

Relevant Packages:
- nvidia-mig-manager-0.5.3-1.x86_64
- datacenter-gpu-manager-3.1.8-1.x86_64
- nvidia-persistenced-535.54.03-1.el8.x86_64
- kmod-nvidia-latest-dkms-535.54.03-1.el8.x86_64
- nvidia-modprobe-535.54.03-1.el8.x86_64
- nvidia-libXNVCtrl-535.54.03-1.el8.x86_64
- nvidia-driver-cuda-libs-535.54.03-1.el8.x86_64
- nvidia-gds-12-2-12.2.0-1.x86_64
- nvidia-mig-manager-0.5.3-1.x86_64
- nvidia-libXNVCtrl-devel-535.54.03-1.el8.x86_64
- nvidia-driver-535.54.03-1.el8.x86_64
- nvidia-driver-cuda-535.54.03-1.el8.x86_64
- nvidia-xconfig-535.54.03-1.el8.x86_64
- nvidia-fs-2.16.1-1.x86_64
- dnf-plugin-nvidia-2.0-1.el8.noarch
- nvidia-kmod-common-535.54.03-1.el8.noarch
- nvidia-settings-535.54.03-1.el8.x86_64
- nvidia-fs-dkms-2.16.1-1.x86_64
- nvidia-driver-NVML-535.54.03-1.el8.x86_64
- nvidia-driver-NvFBCOpenGL-535.54.03-1.el8.x86_64
- nvidia-gds-12.2.0-1.x86_64
- nvidia-driver-libs-535.54.03-1.el8.x86_64
- nvidia-driver-devel-535.54.03-1.el8.x86_64


```
$ systemctl status nvidia-dcgm
● nvidia-dcgm.service - NVIDIA DCGM service
   Loaded: loaded (/usr/lib/systemd/system/nvidia-dcgm.service; enabled; vendor preset: disabled)
   Active: active (running) since Thu 2023-08-03 16:30:36 EDT; 1h 43min ago
 Main PID: 677643 (nv-hostengine)
    Tasks: 7 (limit: 3299392)
   Memory: 91.8M
   CGroup: /system.slice/nvidia-dcgm.service
           └─677643 /usr/bin/nv-hostengine -n --service-account nvidia-dcgm

Aug 03 16:30:36 *** systemd[1]: Started NVIDIA DCGM service.
Aug 03 16:30:37 *** nv-hostengine[677643]: Started host engine version 3.1.8 using port number: 5555
```


## 评论 (6)

### nikkon-dev · 2023-08-03

@berhane,

Unfortunately, the `dcgmi stats` are not supported on MIG-enabled configurations. 
The stats functionality uses the [Accounting mode](https://docs.nvidia.com/deploy/nvml-api/group__nvmlAccountingStats.html) under the hood, and it does not support MIG. 

WBR,
Nik

### berhane · 2023-08-03

> @berhane,
> 
> Unfortunately, the `dcgmi stats` are not supported on MIG-enabled configurations. The stats functionality uses the [Accounting mode](https://docs.nvidia.com/deploy/nvml-api/group__nvmlAccountingStats.html) under the hood, and it does not support MIG.
> 
> WBR, Nik

Thanks for the clarifications, @nikkon-dev. I'll keep looking for ways to get the "Max GPU Memory" used by a Slurm job running on a particular MIG device.

### nikkon-dev · 2023-08-04

@berhane,

If you could use DCGM C API directly, DCGM can store watched metrics for a configured amount of time, and the API provides a way to get all stored values since some timestamp. 

Unfortunately, either dcgmi tool or dcgm-exporter provides only the latest stored value.

### berhane · 2023-08-04

Thank you, @nikkon-dev . I'll see if ChatGPT can write that code for me so that I don't have to learn DCGM's C API :). I wasn't lucky on my first try.

### yun-li-ai · 2025-08-18

Hi @berhane , I am also facing the same issue. Do you have any luck getting the value?

### berhane · 2025-08-18

> Hi [@berhane](https://github.com/berhane) , I am also facing the same issue. Do you have any luck getting the value?

Hi @yun-li-ai : we have been extracting MIG device metrics using the DCGM prometheus exporters:
https://github.com/NVIDIA/dcgm-exporter
