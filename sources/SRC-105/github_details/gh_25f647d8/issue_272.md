# [Issue #272] DCGM 4.5.0: nvbandwidth fails in runlevel 3/4 with "MCUTIL > 10%" immediately after Diagnostic (GpuBurn) even on idle systems; nvbandwidth passes when run standalone

source: https://github.com/NVIDIA/DCGM/issues/272
state: open | updated: 2026-01-29T19:36:23Z
labels: 

## 正文

Seeing a reproducible nvbandwidth failure on DCGM 4.5.0 when running runlevel 3 (and likely 4) on H100x8 NVSwitch nodes.

Symptom:
- `sudo dcgmi diag -r 3` -> nvbandwidth FAIL with:
  "The memory copy utilization for the GPU: X is greater than 10%. This may affect the results of the nvbandwidth test."
- Same node, same conditions:
  `dcgmi diag -r nvbandwidth` -> PASS

This happens on idle hosts (no jobs / no background burn-in agents, nvidia-smi shows no processes). The GPU index that triggers varies (GPU2/GPU3/GPU5 etc).

Debug log suggests ordering/cooldown:
- Diagnostic plugin (GpuBurnWorker) runs, then nvbandwidth starts almost immediately.
Example:
  09:54:30.303 Test nvbandwidth start
  09:54:30.346 ERROR [[nvbandwidth]] MCUTIL > 10% for GPU 2 (NVBandwidthPlugin.cpp:275)

Extra Notes:
- DCGM 4.4.2 passes on the same node where 4.5.0 fails.

Questions:
1) Is MCUTIL>10% supposed to hard-fail nvbandwidth in runlevel runs (message says "may affect")?
2) If not, can nvbandwidth retry/wait for MCUTIL to settle, or can runlevel sequencing include a cooldown between Diagnostic and nvbandwidth?

Note:
- 4.5.0 binaries are available via NVIDIA CUDA Ubuntu repo (datacenter-gpu-manager 1:4.5.0-1), but I don't see a corresponding v4.5.0 tag/source snapshot in this GitHub repo yet, so I can’t check the plugin logic changes. I’m just reporting the observed behavior.

Debug snippets below.
```shell
2026-01-16 09:51:36.803 DEBUG [3279516:3280237] [[diagnostic]] computeTime: 35.27699112892151, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:37.076 DEBUG [3279516:3279516] [[diagnostic]] Thread 140545372317248 had !m_hasExited [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:232] [DcgmThread::Wait]
2026-01-16 09:51:37.092 DEBUG [3279516:3280408] [[diagnostic]] computeTime: 9.4824960231781, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:37.717 DEBUG [3279516:3280365] [[diagnostic]] computeTime: 19.259401082992554, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:37.962 DEBUG [3279516:3280408] [[diagnostic]] computeTime: 10.3525869846344, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:38.129 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542872622656 had !m_hasExited [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:232] [DcgmThread::Wait]
2026-01-16 09:51:38.488 DEBUG [3279516:3280324] [[diagnostic]] computeTime: 28.506460905075073, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:38.608 DEBUG [3279516:3280365] [[diagnostic]] computeTime: 20.1501681804657, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:39.182 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542864229952 had !m_hasExited [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:232] [DcgmThread::Wait]
2026-01-16 09:51:39.361 DEBUG [3279516:3280324] [[diagnostic]] computeTime: 29.379581928253174, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:39.370 DEBUG [3279516:3280376] [[diagnostic]] computeTime: 16.359700918197632, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:39.589 DEBUG [3279516:3280237] [[diagnostic]] computeTime: 38.063048124313354, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:40.226 DEBUG [3279516:3280331] [[diagnostic]] computeTime: 25.997331142425537, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:40.235 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542855837248 had !m_hasExited [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:232] [DcgmThread::Wait]
2026-01-16 09:51:40.455 DEBUG [3279516:3280237] [[diagnostic]] computeTime: 38.92840814590454, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:41.195 DEBUG [3279516:3280318] [[diagnostic]] computeTime: 35.44190001487732, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:41.288 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542637766208 had !m_hasExited [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:232] [DcgmThread::Wait]
2026-01-16 09:51:42.196 DEBUG [3279516:3280376] [[diagnostic]] computeTime: 19.185595989227295, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:42.265 DEBUG [3279516:3279965] [[diagnostic]] computeTime: 45.01917600631714, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:42.341 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542629373504 had !m_hasExited [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:232] [DcgmThread::Wait]
2026-01-16 09:51:43.068 DEBUG [3279516:3280331] [[diagnostic]] computeTime: 28.839499950408936, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:51:43.078 DEBUG [3279516:3280376] [[diagnostic]] computeTime: 20.06779384613037, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:50:02.419 INFO  [3279516:3279516] Created thread named "" ID 1908102720 DcgmThread ptr 0x0x141733f0 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:119] [DcgmThread::Start]
2026-01-16 09:50:02.419 DEBUG [3279516:3279541] Thread handle 1908102720 running [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:305] [DcgmThread::RunInternal]
2026-01-16 09:50:02.419 DEBUG [3279516:3279541] HangDetectMonitor: Running [/builds/dcgm/dcgm/common/HangDetectMonitor.h:294] [HangDetectMonitor::run]
2026-01-16 09:50:02.419 DEBUG [3279516:3279541] HangDetectMonitor: Successfully enqueued periodic task check [/builds/dcgm/dcgm/common/HangDetectMonitor.h:311] [HangDetectMonitor::run]
2026-01-16 09:50:02.423 DEBUG [3279516:3279516] Test CUDA Main Library start [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:214] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.423 DEBUG [3279516:3279516] Set global parameter do_test -> libraries_cuda. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:50:02.423 DEBUG [3279516:3279516] Test CUDA Main Library had result 0. Configless is true [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:222] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.423 DEBUG [3279516:3279516] Test Denylist start [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:214] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.423 DEBUG [3279516:3279516] Set global parameter do_test -> denylist. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Test Denylist had result 0. Configless is true [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:222] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Test Environmental Variables start [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:214] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Set global parameter do_test -> env_variables. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable NSIGHT_CUDA_DEBUGGER not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable CUDA_INJECTION32_PATH not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable CUDA_INJECTION64_PATH not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable CUDA_AUTO_BOOST not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable CUDA_ENABLE_COREDUMP_ON_EXCEPTION not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable CUDA_COREDUMP_FILE not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable CUDA_DEVICE_WAITS_ON_EXCEPTION not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable CUDA_PROFILE not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable COMPUTE_PROFILE not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Env Variable OPENCL_PROFILE not found (GOOD) [/builds/dcgm/dcgm/nvvs/src/Software.cpp:951] [Software::checkForBadEnvVaribles]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Test Environmental Variables had result 0. Configless is true [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:222] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Test Fabric Manager start [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:214] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.427 DEBUG [3279516:3279516] Set global parameter do_test -> fabric_manager. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:50:02.429 DEBUG [3279516:3279516] Fabric manager successfully started for GPU 0 [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1003] [Software::checkFabricManager]
2026-01-16 09:50:02.430 DEBUG [3279516:3279516] Fabric manager successfully started for GPU 1 [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1003] [Software::checkFabricManager]
2026-01-16 09:50:02.430 DEBUG [3279516:3279516] Fabric manager successfully started for GPU 2 [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1003] [Software::checkFabricManager]
2026-01-16 09:50:02.431 DEBUG [3279516:3279516] Fabric manager successfully started for GPU 3 [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1003] [Software::checkFabricManager]
2026-01-16 09:50:02.431 DEBUG [3279516:3279516] Fabric manager successfully started for GPU 4 [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1003] [Software::checkFabricManager]
2026-01-16 09:50:02.432 DEBUG [3279516:3279516] Fabric manager successfully started for GPU 5 [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1003] [Software::checkFabricManager]
2026-01-16 09:50:02.432 DEBUG [3279516:3279516] Fabric manager successfully started for GPU 6 [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1003] [Software::checkFabricManager]
2026-01-16 09:50:02.437 DEBUG [3279516:3279516] Fabric manager successfully started for GPU 7 [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1003] [Software::checkFabricManager]
2026-01-16 09:50:02.437 DEBUG [3279516:3279516] Test Fabric Manager had result 0. Configless is true [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:222] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.437 DEBUG [3279516:3279516] Test Graphics Processes start [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:214] [SoftwarePluginFramework::Run]
2026-01-16 09:50:02.437 DEBUG [3279516:3279516] Set global parameter do_test -> graphics_processes. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:50:02.437 WARN  [3279516:3279516] Error getting the graphics pids for GPU 0. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:598] [Software::checkForGraphicsProcesses]
2026-01-16 09:50:02.437 INFO  [3279516:3279516] Test software: Error getting the graphics pids for GPU 0. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/PluginTest.cpp:221] [PluginTest::AddInfo]
2026-01-16 09:50:02.437 WARN  [3279516:3279516] Error getting the graphics pids for GPU 1. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:598] [Software::checkForGraphicsProcesses]
2026-01-16 09:50:02.437 INFO  [3279516:3279516] Test software: Error getting the graphics pids for GPU 1. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/PluginTest.cpp:221] [PluginTest::AddInfo]
2026-01-16 09:50:02.438 WARN  [3279516:3279516] Error getting the graphics pids for GPU 2. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:598] [Software::checkForGraphicsProcesses]
2026-01-16 09:50:02.438 INFO  [3279516:3279516] Test software: Error getting the graphics pids for GPU 2. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/PluginTest.cpp:221] [PluginTest::AddInfo]
2026-01-16 09:50:02.438 WARN  [3279516:3279516] Error getting the graphics pids for GPU 3. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:598] [Software::checkForGraphicsProcesses]
2026-01-16 09:50:02.438 INFO  [3279516:3279516] Test software: Error getting the graphics pids for GPU 3. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/PluginTest.cpp:221] [PluginTest::AddInfo]
2026-01-16 09:50:02.438 WARN  [3279516:3279516] Error getting the graphics pids for GPU 4. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:598] [Software::checkForGraphicsProcesses]
2026-01-16 09:50:02.438 INFO  [3279516:3279516] Test software: Error getting the graphics pids for GPU 4. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/PluginTest.cpp:221] [PluginTest::AddInfo]
2026-01-16 09:50:02.438 WARN  [3279516:3279516] Error getting the graphics pids for GPU 5. Status = -32 skipping check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:598] [Software::checkForGraphicsProcesses]
2026-01-16 09:50:03.007 WARN  [3279516:3279516] gpuId 5 returned status 0, value 9223372036854775792 for DCGM_FI_DEV_MEMORY_UNREPAIRABLE_FLAG. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:1049] [Software::checkUnrepairableMemory]
2026-01-16 09:50:03.007 DEBUG [3279516:3279516] Set global parameter do_test -> libraries_nvml. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:50:03.007 DEBUG [3279516:3279516] Test NVML Library had result 0. Configless is true [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:222] [SoftwarePluginFramework::Run]
2026-01-16 09:50:03.007 DEBUG [3279516:3279516] Test Page Retirement/Row Remap start [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:214] [SoftwarePluginFramework::Run]
2026-01-16 09:50:03.007 DEBUG [3279516:3279516] Set global parameter do_test -> page_retirement. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:50:03.008 WARN  [3279516:3279516] gpuId 0 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_PENDING. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:688] [Software::checkPageRetirement]
2026-01-16 09:50:03.008 WARN  [3279516:3279516] gpuId 0 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_DBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:729] [Software::checkPageRetirement]
2026-01-16 09:50:03.008 WARN  [3279516:3279516] gpuId 0 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_SBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:750] [Software::checkPageRetirement]
2026-01-16 09:50:03.009 WARN  [3279516:3279516] gpuId 1 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_PENDING. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:688] [Software::checkPageRetirement]
2026-01-16 09:50:03.009 WARN  [3279516:3279516] gpuId 1 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_DBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:729] [Software::checkPageRetirement]
2026-01-16 09:50:03.009 WARN  [3279516:3279516] gpuId 1 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_SBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:750] [Software::checkPageRetirement]
2026-01-16 09:50:03.010 WARN  [3279516:3279516] gpuId 2 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_PENDING. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:688] [Software::checkPageRetirement]
2026-01-16 09:50:03.010 WARN  [3279516:3279516] gpuId 2 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_DBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:729] [Software::checkPageRetirement]
2026-01-16 09:50:03.010 WARN  [3279516:3279516] gpuId 2 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_SBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:750] [Software::checkPageRetirement]
2026-01-16 09:50:03.010 WARN  [3279516:3279516] gpuId 3 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_PENDING. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:688] [Software::checkPageRetirement]
2026-01-16 09:50:03.011 WARN  [3279516:3279516] gpuId 3 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_DBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:729] [Software::checkPageRetirement]
2026-01-16 09:50:03.011 WARN  [3279516:3279516] gpuId 3 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_SBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:750] [Software::checkPageRetirement]
2026-01-16 09:50:03.011 WARN  [3279516:3279516] gpuId 4 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_PENDING. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:688] [Software::checkPageRetirement]
2026-01-16 09:50:03.012 WARN  [3279516:3279516] gpuId 4 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_DBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:729] [Software::checkPageRetirement]
2026-01-16 09:50:03.012 WARN  [3279516:3279516] gpuId 4 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_SBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:750] [Software::checkPageRetirement]
2026-01-16 09:50:03.012 WARN  [3279516:3279516] gpuId 5 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_PENDING. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:688] [Software::checkPageRetirement]
2026-01-16 09:50:03.012 WARN  [3279516:3279516] gpuId 5 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_DBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:729] [Software::checkPageRetirement]
2026-01-16 09:50:03.013 WARN  [3279516:3279516] gpuId 5 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_SBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:750] [Software::checkPageRetirement]
2026-01-16 09:50:03.013 WARN  [3279516:3279516] gpuId 6 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_PENDING. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:688] [Software::checkPageRetirement]
2026-01-16 09:50:03.013 WARN  [3279516:3279516] gpuId 6 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_DBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:729] [Software::checkPageRetirement]
2026-01-16 09:50:03.014 WARN  [3279516:3279516] gpuId 6 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_SBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:750] [Software::checkPageRetirement]
2026-01-16 09:50:03.014 WARN  [3279516:3279516] gpuId 7 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_PENDING. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:688] [Software::checkPageRetirement]
2026-01-16 09:50:03.014 WARN  [3279516:3279516] gpuId 7 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_DBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:729] [Software::checkPageRetirement]
2026-01-16 09:50:03.014 WARN  [3279516:3279516] gpuId 7 returned status 0, value 9223372036854775794for DCGM_FI_DEV_RETIRED_SBE. Skipping this check. [/builds/dcgm/dcgm/nvvs/src/Software.cpp:750] [Software::checkPageRetirement]
2026-01-16 09:50:03.017 DEBUG [3279516:3279516] Test Page Retirement/Row Remap had result 0. Configless is true [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:222] [SoftwarePluginFramework::Run]
2026-01-16 09:50:03.017 DEBUG [3279516:3279516] Test Permissions and OS-related Blocks start [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:214] [SoftwarePluginFramework::Run]
2026-01-16 09:50:03.017 DEBUG [3279516:3279516] Set global parameter do_test -> permissions. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:50:03.017 DEBUG [3279516:3279516] Test Permissions and OS-related Blocks had result 0. Configless is true [/builds/dcgm/dcgm/nvvs/src/SoftwarePluginFramework.cpp:222] [SoftwarePluginFramework::Run]
2026-01-16 09:54:28.730 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542629373504 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:28.730 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542620980800 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:29.586 DEBUG [3279516:3280408] [[diagnostic]] computeTime: 181.9764530658722, InitBufferTime: 0 [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:1421] [GpuBurnWorker::run]
2026-01-16 09:54:29.586 DEBUG [3279516:3280408] [[diagnostic]] Thread id 671082048 stopped [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:314] [DcgmThread::RunInternal]
2026-01-16 09:54:29.587 DEBUG [3279516:3279516] [[diagnostic]] Thread 140540590941760 had m_alreadyJoined 0 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:29.587 DEBUG [3279516:3279516] [[diagnostic]] Done waiting for threads. should_stop=0, failedEarly=false [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:637] [GpuBurnPlugin::RunTest]
2026-01-16 09:54:29.587 DEBUG [3279516:3279516] [[diagnostic]] Thread 140545372317248 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:29.669 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542872622656 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:29.752 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542864229952 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:29.835 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542855837248 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:29.917 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542637766208 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:30.000 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542629373504 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:30.084 DEBUG [3279516:3279516] [[diagnostic]] Thread 140542620980800 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:30.167 DEBUG [3279516:3279516] [[diagnostic]] Thread 140540590941760 had m_alreadyJoined 1 [/builds/dcgm/dcgm/common/DcgmThread/DcgmThread.cpp:236] [DcgmThread::Wait]
2026-01-16 09:54:30.249 DEBUG [3279516:3279516] [[diagnostic]] Go::RunTest: result=true, should_stop=false [/builds/dcgm/dcgm/nvvs/plugin_src/diagnostic/DiagnosticPlugin.cpp:411] [GpuBurnPlugin::Go]
2026-01-16 09:54:30.249 DEBUG [3279516:3279516] Unregistering task 3279516/3279516 [/builds/dcgm/dcgm/common/HangDetectMonitor.cpp:416] [HangDetectMonitor::RemoveMonitoredTask]
2026-01-16 09:54:30.249 DEBUG [3279516:3279516] Deleted fingerprint for task 3279516 of pid 3279516 [/builds/dcgm/dcgm/common/FingerprintStore.cpp:124] [FingerprintStore::Delete]
2026-01-16 09:54:30.265 DEBUG [3279516:3279516] Called; errors = 0, info = 24, results = 8 [/builds/dcgm/dcgm/nvvs/src/PluginLibTest.cpp:228] [PluginLibTest::PopulateEntityResults]
2026-01-16 09:54:30.265 DEBUG [3279516:3279516] Plugin returned unknown type of aux data. Expected JSON_VALUE_AUX_DATA_TYPE (1), got 0 [/builds/dcgm/dcgm/nvvs/src/PluginLibTest.cpp:280] [PluginLibTest::PopulateEntityResults]
2026-01-16 09:54:30.267 INFO  [3279516:3279516] Checking for common errors [/builds/dcgm/dcgm/nvvs/src/PluginCoreFunctionality.cpp:157] [PluginCoreFunctionality::PluginEnded]
2026-01-16 09:54:30.303 DEBUG [3279516:3279516] Test diagnostic had result 0. Configless is true [/builds/dcgm/dcgm/nvvs/src/TestFramework.cpp:957] [TestFramework::GoList]
2026-01-16 09:54:30.303 DEBUG [3279516:3279516] Writing diag info for test diagnostic [/builds/dcgm/dcgm/nvvs/src/TestFramework.cpp:855] [TestFramework::WriteDiagStatusToChannel]
2026-01-16 09:54:30.303 DEBUG [3279516:3279516] Test nvbandwidth start [/builds/dcgm/dcgm/nvvs/src/TestFramework.cpp:926] [TestFramework::GoList]
2026-01-16 09:54:30.344 DEBUG [3279516:3279516] Unable to retrieve fingerprint for task 3279516 of pid 3279516 [/builds/dcgm/dcgm/common/FingerprintStore.cpp:92] [FingerprintStore::Retrieve]
2026-01-16 09:54:30.344 DEBUG [3279516:3279516] Set global parameter is_allowed -> True. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:54:30.344 DEBUG [3279516:3279516] Set global parameter logfile_type -> 0.000000. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:54:30.346 ERROR [3279516:3279516] [[nvbandwidth]] The memory copy utilization for the GPU: 2 is greater than 10%. This may affect the results of the nvbandwidth test. [/builds/dcgm/dcgm/nvvs/plugin_src/nvbandwidth/NVBandwidthPlugin.cpp:275] [DcgmNs::Nvvs::Plugins::NVBandwidth::NVBandwidthPlugin::Go]
2026-01-16 09:54:30.346 WARN  [3279516:3279516] Test nvbandwidth: The memory copy utilization for the GPU: 2 is greater than 10%. This may affect the results of the nvbandwidth test. (grpId:1, entityId:2) [/builds/dcgm/dcgm/nvvs/src/PluginTest.cpp:179] [PluginTest::AddError]
2026-01-16 09:54:30.346 DEBUG [3279516:3279516] Unregistering task 3279516/3279516 [/builds/dcgm/dcgm/common/HangDetectMonitor.cpp:416] [HangDetectMonitor::RemoveMonitoredTask]
2026-01-16 09:54:30.346 DEBUG [3279516:3279516] Deleted fingerprint for task 3279516 of pid 3279516 [/builds/dcgm/dcgm/common/FingerprintStore.cpp:124] [FingerprintStore::Delete]
2026-01-16 09:54:30.354 DEBUG [3279516:3279516] Called; errors = 1, info = 0, results = 8 [/builds/dcgm/dcgm/nvvs/src/PluginLibTest.cpp:228] [PluginLibTest::PopulateEntityResults]
2026-01-16 09:54:30.354 DEBUG [3279516:3279516] Plugin returned unknown type of aux data. Expected JSON_VALUE_AUX_DATA_TYPE (1), got 0 [/builds/dcgm/dcgm/nvvs/src/PluginLibTest.cpp:280] [PluginLibTest::PopulateEntityResults]
2026-01-16 09:54:30.355 INFO  [3279516:3279516] Checking for common errors [/builds/dcgm/dcgm/nvvs/src/PluginCoreFunctionality.cpp:157] [PluginCoreFunctionality::PluginEnded]
2026-01-16 09:54:30.534 DEBUG [3279516:3279516] Test nvbandwidth had result 2. Configless is true [/builds/dcgm/dcgm/nvvs/src/TestFramework.cpp:957] [TestFramework::GoList]
2026-01-16 09:54:30.534 DEBUG [3279516:3279516] Writing diag info for test nvbandwidth [/builds/dcgm/dcgm/nvvs/src/TestFramework.cpp:855] [TestFramework::WriteDiagStatusToChannel]
2026-01-16 09:54:30.535 DEBUG [3279516:3279516] Test pcie start [/builds/dcgm/dcgm/nvvs/src/TestFramework.cpp:926] [TestFramework::GoList]
2026-01-16 09:54:31.116 DEBUG [3279516:3279516] Unable to retrieve fingerprint for task 3279516 of pid 3279516 [/builds/dcgm/dcgm/common/FingerprintStore.cpp:92] [FingerprintStore::Retrieve]
2026-01-16 09:54:31.130 DEBUG [3279516:3279516] [[pcie]] Using copy sizes for GPUs prior to Blackwell [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Pcie.cpp:792] [BusGrind::SetCopySizes]
2026-01-16 09:54:31.130 DEBUG [3279516:3279516] Set global parameter is_allowed -> True. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:54:31.130 DEBUG [3279516:3279516] Set global parameter logfile_type -> 0.000000. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:54:31.130 DEBUG [3279516:3279516] Set global parameter target_stress -> 29250.000000. st 0 [/builds/dcgm/dcgm/nvvs/src/TestParameters.cpp:284] [TestParameters::SetString]
2026-01-16 09:54:31.136 DEBUG [3279516:3279516] [[pcie]] Testing GPUs 0 and 1 for p2p issues. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:235] [Brokenp2p::RunTest]
2026-01-16 09:54:31.511 DEBUG [3279516:3279516] [[pcie]] Memory device 0 and p2p writer device 1 passed. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:261] [Brokenp2p::RunTest]
2026-01-16 09:54:31.511 DEBUG [3279516:3279516] [[pcie]] Testing GPUs 0 and 2 for p2p issues. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:235] [Brokenp2p::RunTest]
2026-01-16 09:54:32.018 DEBUG [3279516:3279516] [[pcie]] Memory device 0 and p2p writer device 2 passed. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:261] [Brokenp2p::RunTest]
2026-01-16 09:54:32.018 DEBUG [3279516:3279516] [[pcie]] Testing GPUs 0 and 3 for p2p issues. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:235] [Brokenp2p::RunTest]
2026-01-16 09:54:32.516 DEBUG [3279516:3279516] [[pcie]] Memory device 0 and p2p writer device 3 passed. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:261] [Brokenp2p::RunTest]
2026-01-16 09:54:32.516 DEBUG [3279516:3279516] [[pcie]] Testing GPUs 0 and 4 for p2p issues. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:235] [Brokenp2p::RunTest]
2026-01-16 09:54:33.015 DEBUG [3279516:3279516] [[pcie]] Memory device 0 and p2p writer device 4 passed. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:261] [Brokenp2p::RunTest]
2026-01-16 09:54:33.015 DEBUG [3279516:3279516] [[pcie]] Testing GPUs 0 and 5 for p2p issues. [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/Brokenp2p.cpp:235] [Brokenp2p::RunTest]
``` 

## 评论 (3)

### mattmalec · 2026-01-20

we're also experiencing this issue and had to downgrade to 4.4.2 to recover

### LiweiPeng · 2026-01-28

On my H100 GPU node, I hit the same error with both DCGMI 4.5.0 and 4.4.2. Running 'dcgmi diag -r 3' failed with the above error message. Running 'dcgmi diag -r nvbandwidth' passed. What could be wrong?

dcgmi diag -r 3:

<img width="1725" height="1314" alt="Image" src="https://github.com/user-attachments/assets/1cef8398-4b6b-45a9-be7a-41c889cdbcf3" />


dcgmi diag -r nvbandwidth
<img width="2408" height="1132" alt="Image" src="https://github.com/user-attachments/assets/bbc92e27-e226-4576-a2d5-695db922aa76" />

### paravz · 2026-01-29

Same issue on H100 using v4.4.2 'dcgmi diag -r 4' fails a gpu, while `dcgmi diag -r nvbandwidth` passes (multiple iterations)
