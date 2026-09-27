# [Issue #314] DCGM 4.7.0 dcgmi health returns "API version mismatch" on some hosts

source: https://github.com/NVIDIA/DCGM/issues/314
state: open | updated: 2026-09-22T15:40:31Z
labels: 

## 正文

We've installed DCGM 4.7.0 on some of our hosts and it works fine so far, but on one host the health system doesn't work:

```
$ dcgmi health --set a
Error: Unable to set health watches. Return: API version mismatch

$ dcgmi health -f
Error: Unable to get health watches. Return: API version mismatch

The API function (dcgmHealthSet etc.) all return DCGM_ST_VER_MISMATCH
```

DCGM 4.6.1 works fine on this host and other features like `stats` also work fine with 4.7.0. We've already completely removed DCGM and re-installed it, but it reports the same error.

Does anyone know how to debug, or even fix this?

The log file shows the same error when one of the health functions is called:

```
2026-09-21 15:58:36.273 INFO  [45265:45271] Loaded module 4 [./dcgmlib/src/DcgmHostEngineHandler.cpp:2775] [DcgmHostEngineHandler::LoadModule]
2026-09-21 15:58:36.273 ERROR [45265:45271] Version mismatch 2002028 != 300202c for module 0 subCommand 17 [./modules/DcgmModule.cpp:35] [DcgmModule::CheckVersion]
2026-09-21 15:58:36.273 ERROR [45265:45271] [[Health]] Error 'API version mismatch' while attempting to get entities for group 0 [/builds/dcgm/dcgm/modules/common/DcgmCoreProxy.cpp:667] [DcgmCoreProxy::GetGroupEntities]
2026-09-21 15:58:36.273 ERROR [45265:45271] [[Health]] Got st -12 from GetGroupEntities() [/builds/dcgm/dcgm/modules/health/DcgmHealthWatch.cpp:190] [DcgmHealthWatch::SetWatches]
2026-09-21 15:58:36.273 ERROR [45265:45271] [[Health]] Set Health Watches Err: Unable to set watches [/builds/dcgm/dcgm/modules/health/DcgmModuleHealth.cpp:60] [DcgmModuleHealth::ProcessSetSystems]
```

Host information:

```
$ cat /etc/*release*
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.5 LTS"
PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy

$ nvidia-smi
Mon Sep 14 09:09:11 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  Tesla P100-PCIE-16GB           Off |   00000000:31:00.0 Off |                    0 |
| N/A   34C    P0             27W /  250W |       0MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

$ dcgmi discovery --list
1 GPU found (Active).
+--------+----------------------------------------------------------------------+
| GPU ID | Device Information                                                   |
+--------+----------------------------------------------------------------------+
| 0      | Name: Tesla P100-PCIE-16GB                                           |
|        | PCI Bus ID: 00000000:31:00.0                                         |
|        | Device UUID: GPU-c12a000a-e4c9-1239-320a-4b6be760446d                |
+--------+----------------------------------------------------------------------+
0 NvSwitches found.
+-----------+
| Switch ID |
+-----------+
+-----------+
0 ConnectX found.
+----------+
| ConnectX |
+----------+
+----------+
0 CPUs found.
+--------+----------------------------------------------------------------------+
| CPU ID | Device Information                                                   |
+--------+----------------------------------------------------------------------+
+--------+----------------------------------------------------------------------+
mweiss@maui:~$ dcgmi --version

dcgmi  version: 4.7.0

$ nv-hostengine --version
Version : 4.7.0
Build ID : 24637
Build Date : 2026-09-09
Build Type : RelWithDebInfo
Commit ID : 63d151480cf54e78592861e42a69b786dc73751b
Branch Name : v4.7.0
CPU Arch : x86_64
Build Platform : Linux 7.0.0-31-generic #31~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Aug 10 09:38:02
UTC 2 x86_64
CRC : 209ebd9bbc4f1659ac404093f5f6f040

$ dpkg -l | grep -i dcgm
ii  datacenter-gpu-manager-4-core                  1:4.7.0-1                                        amd64        Metapackage for the CUDA-independent DCGM host-engine runtime
ii  datacenter-gpu-manager-4-cuda13                1:4.7.0-1                                        amd64        DCGM diagnostic and profiling binaries for CUDA 13
ii  datacenter-gpu-manager-4-cuda13-cublas         1:4.7.0-1                                        amd64        NVIDIA® cuBLAS runtime libraries used by DCGM CUDA13 binaries
ii  datacenter-gpu-manager-4-cuda13-curand         1:4.7.0-1                                        amd64        NVIDIA® cuRAND runtime library used by DCGM CUDA13 binaries
ii  datacenter-gpu-manager-4-cuda13-cusparselt     1:4.7.0-1                                        amd64        NVIDIA® cuSPARSELt runtime library used by DCGM CUDA13 binaries
ii  datacenter-gpu-manager-4-cuda13-nccl           1:4.7.0-1                                        amd64        NVIDIA® NCCL runtime library used by DCGM CUDA13 binaries
ii  datacenter-gpu-manager-4-cuda13-ubergemm2      1:4.7.0-1                                        amd64        UBERGEMM2 GPU workload for DCGM CUDA 13 diagnostics
ii  datacenter-gpu-manager-4-dcgmproftesterkernels 1:4.7.0-1                                        amd64        CUDA kernels for the DCGM profiling workload generators
ii  datacenter-gpu-manager-4-module-config         1:4.7.0-1                                        amd64        DCGM GPU configuration module
ii  datacenter-gpu-manager-4-module-diag           1:4.7.0-1                                        amd64        DCGM single-node diagnostics module and runner
ii  datacenter-gpu-manager-4-module-health         1:4.7.0-1                                        amd64        DCGM passive health-monitoring module
ii  datacenter-gpu-manager-4-module-introspect     1:4.7.0-1                                        amd64        DCGM host-engine introspection module
ii  datacenter-gpu-manager-4-module-nvswitch       1:4.7.0-1                                        amd64        DCGM NVSwitch and ConnectX monitoring module
ii  datacenter-gpu-manager-4-module-policy         1:4.7.0-1                                        amd64        DCGM GPU policy notification module
ii  datacenter-gpu-manager-4-module-sysmon         1:4.7.0-1                                        amd64        DCGM NVIDIA CPU monitoring module
ii  datacenter-gpu-manager-4-proprietary           1:4.7.0-1                                        amd64        Proprietary CUDA-independent DCGM components
ii  datacenter-gpu-manager-4-proprietary-cuda13    1:4.7.0-1                                        amd64        Proprietary DCGM diagnostic plugins for CUDA 13
ii  datacenter-gpu-manager-4-python3               1:4.7.0-1                                        amd64        Python 3 bindings and monitoring integrations for DCGM
ii  dcgmi                                          1:4.7.0-1                                        amd64        Command-line client for NVIDIA Data Center GPU Manager (DCGM)
ii  libdcgm                                        1:4.7.0-1                                        amd64        DCGM host-engine runtime library
ii  nv-hostengine                                  1:4.7.0-1                                        amd64        Standalone DCGM host engine and system service
````

## 评论 (2)

### apmccartney-nv · 2026-09-21

Did you restart the nvidia-dcgm systemd service after upgrading?

Better yet, please collect and respond with the output of the following

```
$ dcgmi -v
```

(Note: `dcgmi -v` is not the same as `dcgmi --version`)

### maxweiss · 2026-09-22

> Did you restart the nvidia-dcgm systemd service after upgrading?
> 
> Better yet, please collect and respond with the output of the following
> 
> ```
> $ dcgmi -v
> ```
> 
> (Note: `dcgmi -v` is not the same as `dcgmi --version`)

Yes, we have restarted the service and rebootet the host multiple times.

```
$ dcgmi -v

Local build info:
Version : 4.7.0
Build ID : 24637
Build Date : 2026-09-09
Build Type : RelWithDebInfo
Commit ID : 63d151480cf54e78592861e42a69b786dc73751b
Branch Name : v4.7.0
CPU Arch : x86_64
Build Platform : Linux 7.0.0-31-generic #31~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Aug 10 09:38:02 UTC 2 x86_64
CRC : 209ebd9bbc4f1659ac404093f5f6f040

Hostengine build info:
Version : 4.7.0
Build ID : 24637
Build Date : 2026-09-09
Build Type : RelWithDebInfo
Commit ID : 63d151480cf54e78592861e42a69b786dc73751b
Branch Name : v4.7.0
CPU Arch : x86_64
Build Platform : Linux 7.0.0-31-generic #31~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Aug 10 09:38:02 UTC 2 x86_64
CRC : 209ebd9bbc4f1659ac404093f5f6f040
```
