# [Issue #210] DCGM v4.0 Profiling Module Not loaded

source: https://github.com/NVIDIA/DCGM/issues/210
state: closed | updated: 2025-03-12T10:13:45Z
labels: 

## 正文

After updating dcgm to v4.0, the profiling module stopped loading.

**System specs:**
Ubuntu: 22.04
CUDA Version: 12.8
Driver Version: 570.86.10
GPU: tried on NVIDIA L4, L40S and T4 (same results)

The following is logs are from L4.

`dcgmi modules -l`

```
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
| 8         | Profiling          | Not loaded                                       |
| 9         | SysMon             | Not loaded                                       |
+-----------+--------------------+--------------------------------------------------+
```

Debug logs after running `nv-hostengine -f host.debug.log --log-level debug`. There are essentially more logs but it's same NvSwitch logs repeated over and over with no logs related to Profiling module.

```
2025-01-23 22:23:52.097 DEBUG [46345:46345] Initialized base logger [/builds/dcgm/dcgm/dcgmlib/src/DcgmApi.cpp:5277] [{anonymous}::StartEmbeddedV2]
2025-01-23 22:23:52.105 DEBUG [46345:46345] Not changing to a home directory - 'DCGM_HOME_DIR' is not defined in the environment. [/builds/dcgm/dcgm/dcgmlib/src/DcgmApi.cpp:5290] [{anonymous}::StartEmbeddedV2]
2025-01-23 22:23:52.105 INFO  [46345:46345] version:4.0.0;arch:x86_64;buildtype:RelWithDebInfo;buildid:10349;builddate:2024-12-10;commit:4288e26f9a6fdabf2f48827baca7c26d0bff23f5;branch:v4.0.0;buildplatform:Linux 5.15.0-122-generic #132-Ubuntu SMP Thu Aug 29 13:45:
52 UTC 2024 x86_64;;crc:ab4177067a165f926320c6f1623b7337 [/builds/dcgm/dcgm/dcgmlib/src/DcgmApi.cpp:5294] [{anonymous}::StartEmbeddedV2]
2025-01-23 22:23:53.664 DEBUG [46345:46345] __DCGM_XID_KMSG__ unset. Not loading [/builds/dcgm/dcgm/dcgmlib/src/DcgmKmsgReader.cpp:40] [ReadEnvXidAndUpdate]
2025-01-23 22:23:53.664 DEBUG [46345:46345] __DCGM_TEST_KMSG_FILENAME__ unset. Not loading [/builds/dcgm/dcgm/dcgmlib/src/DcgmKmsgReader.cpp:149] [ReadEnvKmsgFilenameAndUpdate]
2025-01-23 22:23:53.664 DEBUG [46345:46345] Set m_forceProfMetricsThroughGpm to 0 [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:945] [DcgmCacheManager::DcgmCacheManager]
2025-01-23 22:23:53.664 INFO  [46345:46345] Parsed driver string is 5708610, IsR450OrNewer: 1, IsR520OrNewer: 1 [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:2692] [DcgmCacheManager::ReadAndCacheDriverVersions]
2025-01-23 22:23:53.670 DEBUG [46345:46345] nvmlDevice 0x70c21641c158 is arch 8 [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:1558] [DcgmCacheManager::HelperGetLiveChipArch]
2025-01-23 22:23:53.670 INFO  [46345:46345] Detected 0 NVLinks for GPU 0 [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:1277] [DcgmCacheManager::InitializeNvLinkCount]
2025-01-23 22:23:53.670 DEBUG [46345:46345] [CacheManager][MIG] nvmlDeviceGetMigMode result: (3) Not Supported. CurrentMode: 0, PendingMode: 0 [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:706] [DcgmCacheManager::InitializeGpuInstances]
2025-01-23 22:23:53.670 DEBUG [46345:46345] Cannot check for MIG devices: Not Supported [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:725] [DcgmCacheManager::InitializeGpuInstances]
2025-01-23 22:23:53.670 DEBUG [46345:46345] Added GPU 0000:31:00.0 with GPU ID 0 to the pciBusGpuIdMap [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:1255] [DcgmCacheManager::MergeNewlyDetectedGpuList]
2025-01-23 22:23:53.670 DEBUG [46345:46345] Allowlist NOT bypassed with env variable [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:1032] [DcgmCacheManager::IsGpuAllowlisted]
2025-01-23 22:23:53.670 DEBUG [46345:46345] gpuId 0, arch 8 is on the allowlist. [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:1056] [DcgmCacheManager::IsGpuAllowlisted]
2025-01-23 22:23:53.670 DEBUG [46345:46345] gpuId 0 has migIsEnabledForGpu = 0 migIsEnabledForAnyGpu 0 [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:12957] [DcgmCacheManager::UpdateNvLinkLinkState]
2025-01-23 22:23:53.670 DEBUG [46345:46345] gpuId 0 has migIsEnabledForAnyGpu 0 [/builds/dcgm/dcgm/dcgmlib/src/DcgmTopology.cpp:462] [UpdateNvLinkLinkStateFromNvml]
2025-01-23 22:23:53.670 INFO  [46345:46345] Got 0 excluded GPUs [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:1092] [DcgmCacheManager::ReadAndCacheGpuExclusionList]
2025-01-23 22:23:53.670 DEBUG [46345:46345] gpuId 0, desiredEvents x8, m_currentEventMask x0 [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:2556] [DcgmCacheManager::ManageDeviceEvents]
2025-01-23 22:23:53.671 DEBUG [46345:46345] Set nvmlIndex 0 event mask to x8 [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:2611] [DcgmCacheManager::ManageDeviceEvents]
2025-01-23 22:23:53.671 INFO  [46345:46345] Created thread named "cache_mgr_event" ID 283117120 DcgmThread ptr 0x0x2290c2e0 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:115] [DcgmThread::Start]
2025-01-23 22:23:53.671 DEBUG [46345:46359] Thread handle 283117120 running [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:300] [DcgmThread::RunInternal]
2025-01-23 22:23:53.671 INFO  [46345:46359] DcgmCacheManagerEventThread started [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:13317] [DcgmCacheManagerEventThread::run]
2025-01-23 22:23:53.671 INFO  [46345:46345] Created thread named "" ID 199231040 DcgmThread ptr 0x0x2290bbe0 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:115] [DcgmThread::Start]
2025-01-23 22:23:53.671 DEBUG [46345:46359] __DCGM_FATAL_XIDS__ unset. Not loading [/builds/dcgm/dcgm/dcgmlib/src/DcgmCacheManager.cpp:6907] [ReadEnvForFatalXids]
2025-01-23 22:23:53.671 DEBUG [46345:46360] Thread handle 199231040 running [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:300] [DcgmThread::RunInternal]
2025-01-23 22:23:53.671 INFO  [46345:46345] AddEntityToGroup groupId 0, eg 1, eid 0 added to the group [/builds/dcgm/dcgm/dcgmlib/src/DcgmGroupManager.cpp:683] [DcgmGroupInfo::AddEntityToGroup]
2025-01-23 22:23:53.671 DEBUG [46345:46345] Added GroupId 0 name DCGM_ALL_SUPPORTED_GPUS for connectionId 0 [/builds/dcgm/dcgm/dcgmlib/src/DcgmGroupManager.cpp:273] [DcgmGroupManager::AddNewGroup]
2025-01-23 22:23:53.672 DEBUG [46345:46345] Entering dcgmModuleIdToName(dcgmModuleId_t id, char const **name) (1, 0x7fff4271f630) [/builds/dcgm/dcgm/dcgmlib/entry_point.h:857] [dcgmModuleIdToName]
2025-01-23 22:23:53.672 DEBUG [46345:46345] Returning 0 [/builds/dcgm/dcgm/dcgmlib/entry_point.h:857] [dcgmModuleIdToName]
2025-01-23 22:23:53.672 DEBUG [46345:46345] [[NvSwitch]] Initialized logging for module 1 [/builds/dcgm/dcgm/modules/DcgmModule.h:90] [DcgmModuleWithCoreProxy<moduleId>::DcgmModuleWithCoreProxy]
2025-01-23 22:23:53.672 DEBUG [46345:46345] [[NvSwitch]] Loading NVSDM [/builds/dcgm/dcgm/modules/nvswitch/DcgmModuleNvSwitch.cpp:29] [DcgmNs::createSwitchManager]
2025-01-23 22:23:53.672 DEBUG [46345:46345] [[NvSwitch]] Initializing NVSDM Manager [/builds/dcgm/dcgm/modules/nvswitch/DcgmNvsdmManager.cpp:468] [DcgmNs::DcgmNvsdmManager::Init]
2025-01-23 22:23:53.672 ERROR [46345:46345] [[NvSwitch]] Could not load NVSDM [/builds/dcgm/dcgm/modules/nvswitch/DcgmNvsdmManager.cpp:501] [DcgmNs::DcgmNvsdmManager::AttachToNvsdm]
2025-01-23 22:23:53.672 ERROR [46345:46345] [[NvSwitch]] AttachToNvsdm() returned -25 [/builds/dcgm/dcgm/modules/nvswitch/DcgmNvsdmManager.cpp:473] [DcgmNs::DcgmNvsdmManager::Init]
2025-01-23 22:23:53.672 DEBUG [46345:46345] [[NvSwitch]] Loading NSCQ [/builds/dcgm/dcgm/modules/nvswitch/DcgmModuleNvSwitch.cpp:37] [DcgmNs::createSwitchManager]
2025-01-23 22:23:53.672 WARN  [46345:46345] [[NvSwitch]] Not attached to NVSDM [/builds/dcgm/dcgm/modules/nvswitch/DcgmNvsdmManager.cpp:520] [DcgmNs::DcgmNvsdmManager::DetachFromNvsdm]
2025-01-23 22:23:53.672 ERROR [46345:46345] [[NvSwitch]] Could not load NSCQ. dlwrap_attach ret: Can not access a needed shared library (-79): If this system has NvSwitches, please ensure that the package libnvidia-nscq is installed on your system and that the ser
vice user has permissions to access it. [/builds/dcgm/dcgm/modules/nvswitch/DcgmNscqManager.cpp:500] [DcgmNs::DcgmNscqManager::AttachToNscq]
2025-01-23 22:23:53.672 ERROR [46345:46345] [[NvSwitch]] AttachToNscq() returned -25 [/builds/dcgm/dcgm/modules/nvswitch/DcgmNscqManager.cpp:336] [DcgmNs::DcgmNscqManager::Init]
2025-01-23 22:23:53.672 WARN  [46345:46345] [[NvSwitch]] Could not initialize NSCQ. Ret: DCGM library could not be found [/builds/dcgm/dcgm/modules/nvswitch/DcgmModuleNvSwitch.cpp:45] [DcgmNs::createSwitchManager]
2025-01-23 22:23:53.672 DEBUG [46345:46345] [[NvSwitch]] Constructing NvSwitch Module [/builds/dcgm/dcgm/modules/nvswitch/DcgmModuleNvSwitch.cpp:55] [DcgmNs::DcgmModuleNvSwitch::DcgmModuleNvSwitch]
2025-01-23 22:23:53.672 INFO  [46345:46345] [[NvSwitch]] Created thread named "" ID 188745280 DcgmThread ptr 0x0x22964468 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:115] [DcgmThread::Start]
2025-01-23 22:23:53.672 INFO  [46345:46345] Loaded module 1 [/builds/dcgm/dcgm/dcgmlib/src/DcgmHostEngineHandler.cpp:1913] [DcgmHostEngineHandler::LoadModule]
2025-01-23 22:23:53.672 DEBUG [46345:46361] [[NvSwitch]] Thread handle 188745280 running [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:300] [DcgmThread::RunInternal]
2025-01-23 22:23:53.672 DEBUG [46345:46361] [[NvSwitch]] Rescanning switch states [/builds/dcgm/dcgm/modules/nvswitch/DcgmModuleNvSwitch.cpp:451] [DcgmNs::DcgmModuleNvSwitch::RunOnce]
```

## 评论 (3)

### jksjaz · 2025-01-24

@nikkon-dev Do you know some way that would output better logs to debug?

### jksjaz · 2025-02-10

Updating to DCGMI 4.1 solved the issue.

### justayo1337 · 2025-03-12

Good day, seeing a similar profiling issue with the L4s and H100s 
- OS: SLES15 SP5  
- CUDA Version: 12.6
- Driver Version 560.28.03
- GPU: On a single chassis: 4 L4s and 2 H100s

Tried with version 4.1.1 at the nvidia cuda repos and hitting issues with the new version. Everything seemingly works well with the 3.3.9 version but having to move away from that due to this bug on the dcgm-exporter  available at that version https://github.com/NVIDIA/dcgm-exporter/issues/412

To also note, tested on SLES15 SP5 with the A2s and profiling seems to work fine on that generation. But the Hopper and Ada architectures are failing
