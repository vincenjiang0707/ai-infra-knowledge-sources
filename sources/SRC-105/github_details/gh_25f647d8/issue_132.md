# [Issue #132] How to get the module profile loaded?

source: https://github.com/NVIDIA/DCGM/issues/132
state: open | updated: 2025-09-16T06:53:08Z
labels: 

## 正文

Hello!  When I running the command below
 ` dcgmi dmon -e  1001`
the result is

>  Error setting watches. Result: -33: This request is serviced by a module of DCGM that is not currently loaded\

And when I check the module list with `dcgmi modules -l`,it shows that the profiling module failed to load. May I ask why and how can get the profile module loaded? Thanks a lot.

> +-----------+--------------------+--------------------------------------------------+
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
| 9         | SysMon             | Not loaded                                       |
+-----------+--------------------+--------------------------------------------------+

## 评论 (8)

### nikkon-dev · 2023-11-07

@jxh314,

There are a few limitations with the profiling module for GPUs. Firstly, it is not open-sourced. If you want to use it, you must obtain the module from the official DCGM packages, as it cannot be built from sources. Secondly, the profiling module only supports Tesla/Quadro grade GPUs and not RTX/GTX GPUs.

If you are using the module from the official datacenter-gpu-manager packages and still facing issues with loading it, please provide the debug logs from the nv-hostengine by running the command `nv-hostengine -f host.debug.log --log-level debug`. This is particularly relevant if you have V100/A100 GPUs.

### jxh314 · 2023-11-08

@nikkon-dev  Thanks  a lot!



### Xaraxia · 2024-02-22

I'm having this issue on A100 with MIG. Profiler will load on an identical system but without MIG. I'm on dcgm 3.1.7, saw nothing in the release notes to suggest this was fixed since. If there's a fix, I will seek approval for an out-of-downtime upgrade. But since you asked for a debug log, here's a debug log!

```
2024-02-22 13:03:43.501 DEBUG [4042437:4042440] DoOneUpdateAllFields returned 1708571043208144 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgmlib/src/DcgmCacheManager.cpp:2409] [DcgmCacheManager::UpdateAllFields]
2024-02-22 13:03:43.501 DEBUG [4042437:4042440] Entering dcgmModuleIdToName(dcgmModuleId_t id, char const **name) (8, 0x7fc255921070) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgmlib/entry_point.h:912] [dcgmModuleIdToName]
2024-02-22 13:03:43.501 DEBUG [4042437:4042440] Returning 0 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgmlib/entry_point.h:912] [dcgmModuleIdToName]
2024-02-22 13:03:43.501 DEBUG [4042437:4042440] [[Profiling]] Initialized logging for module 8 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/modules/DcgmModule.h:90] [DcgmModuleWithCoreProxy<moduleId>::DcgmModuleWithCoreProxy]
2024-02-22 13:03:43.501 DEBUG [4042437:4042440] [[Profiling]] __DCGM_PROF_NO_SKU_CHECK was NOT set. [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:582] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::ReadEnvironmentalVariables]
2024-02-22 13:03:43.514 DEBUG [4042437:4042440] [[Profiling]] NVPW_InitializeTarget() was successful. [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1365] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_DCGM_LoadDriver() was successful. [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1366] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_InitializeHost() was successful. [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1367] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_GetDeviceCount() was successful [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1380] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetPciBusIds() was successful. [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1397] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 7 (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 7 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 8 (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 8 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 9 (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 9 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 10 (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 10 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 11 (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 11 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 12 (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 12 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 13 (device: 0, bus: 33, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 13 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 7 (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 7 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 8 (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 8 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 9 (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 9 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 10 (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 10 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 11 (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 11 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 12 (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 12 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 13 (device: 0, bus: 129, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 13 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 7 (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 7 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 8 (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 8 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 9 (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 9 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 10 (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 10 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 11 (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 11 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 12 (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 12 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] NVPW_Device_GetMigAttributes was successful (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1419] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping MIG CI id: 13 (device: 0, bus: 226, domain: 0) [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1425] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Reason: gpuInstanceId = 13 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1426] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping a GPU unknown to LOP [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1457] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping a GPU unknown to LOP [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1457] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] [[Profiling]] Skipping a GPU unknown to LOP [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1457] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 ERROR [4042437:4042440] [[Profiling]] No GPU with LOP support were found. [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1551] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::InitLop]
2024-02-22 13:03:43.997 ERROR [4042437:4042440] [[Profiling]] DcgmModuleProfiling failed to initialize. See the logs. [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:502] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::DcgmModuleProfiling]
2024-02-22 13:03:43.997 ERROR [4042437:4042440] [[Profiling]] A runtime exception occured when creating module. Ex: DcgmModuleProfiling failed to initialize. See the logs. [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/modules/DcgmModule.h:146] [{anonymous}::SafeWrapper]
2024-02-22 13:03:43.997 ERROR [4042437:4042440] Failed to load module 8 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgmlib/src/DcgmHostEngineHandler.cpp:1734] [DcgmHostEngineHandler::LoadModule]
2024-02-22 13:03:43.997 ERROR [4042437:4042440] DCGM_PROFILING_SR_WATCH_FIELDS failed with -33 [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgmlib/src/DcgmHostEngineHandler.cpp:3536] [DcgmHostEngineHandler::WatchFieldGroup]
2024-02-22 13:03:43.997 DEBUG [4042437:4042440] Got 3 entities and 1 fields [/workspaces/dcgm-rel_dcgm_3_1-postmerge@2/dcgmlib/src/DcgmHostEngineHandler.cpp:3578] [DcgmHostEngineHandler::UnwatchFieldGroup]
```


### nikkon-dev · 2024-02-22

@Xaraxia,

Could you provide the `nvidia-smi` and `nvidia-smi -q` output? 

Please kindly provide more information about your setup. Specifically, let us know if you are running nv-hostengine on a bare-metal host or inside a container. From the logs you provided, it appears that dcgm can detect some MIG instances but not all devices. Please note that for MIG configurations to work properly, dcgm needs to run on the host and access the entire device rather than just individual MIG instances. Also, it's important to ensure that CUDA_VISIBLE_DEVICES is not set for dcgm.

### Xaraxia · 2024-02-26

Hi nikkon-dev,

This is running on a bare-metal host as root using the nvidia systemd service. HPC jobs can see and use the MIG instances.

```
root        5380       1 13 Feb06 ?        2-14:13:45 /usr/local/sbin/dcgm-exporter
root     4059539       1  0 Feb22 ?        00:00:37 /usr/bin/nv-hostengine -n --service-account nvidia-dcgm

```
[bun005-smi.txt](https://github.com/NVIDIA/DCGM/files/14398366/bun005-smi.txt)



### Saigut · 2024-03-26

Hello, here is output of NVIDIA GeForce RTX 4090. RTX 4090 can't load `Profiling` module, right ?

```
# dcgmi modules -l
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
| 9         | SysMon             | Failed to load                                   |
+-----------+--------------------+--------------------------------------------------+
```

### jxh314 · 2024-03-26

It appears to be the case. I get the same result as you when running the ``dcgmi modules -l`` command.
@Saigut 





### HH-66 · 2025-03-18

@nikkon-dev hello, the same issue on L20 and dcgmi 4.1.1
Version : 4.1.1
Build ID : 11087
Build Date : 2025-02-14
Build Type : RelWithDebInfo
Commit ID : 3965d2e947bcea4c496759177222de6115bd58d0
Branch Name : v4.1.1
CPU Arch : x86_64
Build Platform : Linux 5.15.0-122-generic https://github.com/NVIDIA/DCGM/issues/132-Ubuntu SMP Thu Aug 29 13:45:52 UTC 2024 x86_64
CRC : 84de5921dcda2d8986924b6bcea05213

![Image](https://github.com/user-attachments/assets/f79c6dde-f39c-425b-9405-36fd14da6597)

![Image](https://github.com/user-attachments/assets/fc740670-2a5e-4ee3-ac61-854c93e4c3a2)


nvidia-smi -q

==============NVSMI LOG==============

Timestamp                                 : Tue Mar 18 14:08:47 2025
Driver Version                            : 535.161.08
CUDA Version                              : 12.2

Attached GPUs                             : 1
GPU 00000000:12:00.0
    Product Name                          : NVIDIA L20
    Product Brand                         : NVIDIA
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1325023055321
    GPU UUID                              : GPU-d717428d-21dc-7e52-c1c0-e7223a614f66
    Minor Number                          : 3
    VBIOS Version                         : 95.02.7C.00.04
    MultiGPU Board                        : No
    Board ID                              : 0x1200
    Board Part Number                     : 900-2G133-00A0-000
    GPU Part Number                       : 26BA-888-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0265.00.01
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2025/03/05 07:10:50.434
        Latest Duration                   : 43061 us
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GSP Firmware Version                  : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x12
        Device                            : 0x00
        Domain                            : 0x0000
        Device Id                         : 0x26BA10DE
        Bus Id                            : 00000000:12:00.0
        Sub System Id                     : 0x195710DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 5
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 0 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : N/A
    Performance State                     : P8
    Clocks Event Reasons
        Idle                              : Active
        Applications Clocks Setting       : Not Active
        SW Power Cap                      : Not Active
        HW Slowdown                       : Not Active
            HW Thermal Slowdown           : Not Active
            HW Power Brake Slowdown       : Not Active
        Sync Boost                        : Not Active
        SW Thermal Slowdown               : Not Active
        Display Clock Setting             : Not Active
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 46068 MiB
        Reserved                          : 471 MiB
        Used                              : 0 MiB
        Free                              : 45595 MiB
    BAR1 Memory Usage
        Total                             : 65536 MiB
        Used                              : 1 MiB
        Free                              : 65535 MiB
    Conf Compute Protected Memory Usage
        Total                             : 0 MiB
        Used                              : 0 MiB
        Free                              : 0 MiB
    Compute Mode                          : Default
    Utilization
        Gpu                               : 0 %
        Memory                            : 0 %
        Encoder                           : 0 %
        Decoder                           : 0 %
        JPEG                              : 0 %
        OFA                               : 0 %
    Encoder Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    FBC Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    ECC Mode
        Current                           : Enabled
        Pending                           : Enabled
    ECC Errors
        Volatile
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
        Aggregate
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
            SRAM Threshold Exceeded       : No
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : 0
            SRAM SM                       : 0
            SRAM Microcontroller          : 0
            SRAM PCIE                     : 0
            SRAM Other                    : 0
    Retired Pages
        Single Bit ECC                    : N/A
        Double Bit ECC                    : N/A
        Pending Page Blacklist            : N/A
    Remapped Rows
        Correctable Error                 : 0
        Uncorrectable Error               : 0
        Pending                           : No
        Remapping Failure Occurred        : No
        Bank Remap Availability Histogram
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : 58 C
        GPU Shutdown T.Limit Temp         : -5 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 36.13 W
        Current Power Limit               : 350.00 W
        Requested Power Limit             : 350.00 W
        Default Power Limit               : 350.00 W
        Min Power Limit                   : 150.00 W
        Max Power Limit                   : 350.00 W
    Module Power Readings
        Power Draw                        : N/A
        Current Power Limit               : N/A
        Requested Power Limit             : N/A
        Default Power Limit               : N/A
        Min Power Limit                   : N/A
        Max Power Limit                   : N/A
    Clocks
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2520 MHz
        Memory                            : 9001 MHz
    Default Applications Clocks
        Graphics                          : 2520 MHz
        Memory                            : 9001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2520 MHz
        SM                                : 2520 MHz
        Memory                            : 9001 MHz
        Video                             : 1965 MHz
    Max Customer Boost Clocks
        Graphics                          : 2520 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 915.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
    Processes                             : None

