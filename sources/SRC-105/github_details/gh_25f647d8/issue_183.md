# [Issue #183] H800 can not open profile feature? Help...

source: https://github.com/NVIDIA/DCGM/issues/183
state: open | updated: 2025-03-19T09:36:13Z
labels: 

## 正文

dcgmi profile --resume
Error: unable to resume profiling metrics: Feature not supported.

NEED HELP ... PLZ!!!

my env is that >>>>>>>>>>>>>>>


Hostengine build info:
Version : 3.3.7
Build ID : 26
Build Date : 2024-07-09
Build Type : Release
Commit ID : 105620196e46a7ef2f99a1ce3e69a5d12af1e845
Branch Name : rel_dcgm_3_3
CPU Arch : x86_64
Build Platform : Linux 4.15.0-180-generic #189-Ubuntu SMP Wed May 18 14:13:57 UTC 2022 x86_64
CRC : c1b74febf52d45d29ae956b78c091857


+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.183.01             Driver Version: 535.183.01   CUDA Version: 12.5     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA H800                    Off | 00000000:16:00.0 Off |                    0 |
| N/A   29C    P0              73W / 700W |      3MiB / 81559MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   1  NVIDIA H800                    Off | 00000000:17:00.0 Off |                    0 |
| N/A   32C    P0              71W / 700W |      3MiB / 81559MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   2  NVIDIA H800                    Off | 00000000:40:00.0 Off |                    0 |
| N/A   33C    P0             117W / 700W |    743MiB / 81559MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   3  NVIDIA H800                    Off | 00000000:41:00.0 Off |                    0 |
| N/A   35C    P0              74W / 700W |      3MiB / 81559MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   4  NVIDIA H800                    Off | 00000000:96:00.0 Off |                    0 |
| N/A   29C    P0              72W / 700W |      3MiB / 81559MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   5  NVIDIA H800                    Off | 00000000:97:00.0 Off |                    0 |
| N/A   33C    P0              72W / 700W |      3MiB / 81559MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   6  NVIDIA H800                    Off | 00000000:C0:00.0 Off |                    0 |
| N/A   29C    P0              73W / 700W |      3MiB / 81559MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   7  NVIDIA H800                    Off | 00000000:C1:00.0 Off |                    0 |
| N/A   32C    P0              72W / 700W |      3MiB / 81559MiB |      0%      Default |
|                                         |                      |             Disabled


[root@dcef26e4e4ae /]# dcgmi modules -l
+-----------+--------------------+--------------------------------------------------+
| List Modules                                                                      |
| Status: Success                                                                   |
+===========+====================+==================================================+
| Module ID | Name               | State                                            |
+-----------+--------------------+--------------------------------------------------+
| 0         | Core               | Loaded                                           |
| 1         | NvSwitch           | Loaded                                           |
| 2         | VGPU               | Not loaded                                       |
| 3         | Introspection      | Not loaded                                       |
| 4         | Health             | Not loaded                                       |
| 5         | Policy             | Not loaded                                       |
| 6         | Config             | Not loaded                                       |
| 7         | Diag               | Not loaded                                       |
| 8         | Profiling          | Failed to load                                   |
| 9         | SysMon             | Not loaded    

## 评论 (2)

### cc8476 · 2024-08-06

add extro info:
nv-hostengine -f host.debug.log --log-level debug
Err: Failed to start DCGM Server: -7

### HH-66 · 2025-03-18

the same issue about L20 and dcgmi 4.1.1
Version : 4.1.1
Build ID : 11087
Build Date : 2025-02-14
Build Type : RelWithDebInfo
Commit ID : 3965d2e947bcea4c496759177222de6115bd58d0
Branch Name : v4.1.1
CPU Arch : x86_64
Build Platform : Linux 5.15.0-122-generic #132-Ubuntu SMP Thu Aug 29 13:45:52 UTC 2024 x86_64
CRC : 84de5921dcda2d8986924b6bcea05213

![Image](https://github.com/user-attachments/assets/f79c6dde-f39c-425b-9405-36fd14da6597)

![Image](https://github.com/user-attachments/assets/fc740670-2a5e-4ee3-ac61-854c93e4c3a2)


some debug log
![Image](https://github.com/user-attachments/assets/c249e6a7-e63f-4a94-8240-6ac541d906c2)

