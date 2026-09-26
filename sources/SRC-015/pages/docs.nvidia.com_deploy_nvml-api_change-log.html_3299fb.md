source: https://docs.nvidia.com/deploy/nvml-api/change-log.html

# Change Log[#](https://docs.nvidia.com#change-log)

This chapter list changes in API and bug fixes that were introduced to the library.

## Changes between NVML v610 and v615[#](https://docs.nvidia.com#changes-between-nvml-v610-and-v615)

Added

and`NVML_GPU_RECOVERY_ACTION_BUS_RESET`

to`NVML_GPU_RECOVERY_ACTION_SYSTEM_REBOOT`

.`nvmlDeviceGpuRecoveryAction_t`

Added GPU Operational Event APIs to register and wait for structured events and retrieve their associated context records:

Added

to query the bank remapper status.`nvmlDeviceGetBankRemapperStatus_v1()`

Added a new temperature sensor type

to report the temperature from the hottest part of the GPU.`NVML_TEMPERATURE_GPU_MAX`

Added 2 new clock event reason bitmask values for board limit and reliability policies:

Added new

state.`NVML_NVLINK_STATE_ACTIVE_TRAFFIC_DISABLED`

Added

to asynchronously set Nvlink Bandwidth mode.`nvmlDeviceSetNvlinkBwModeAsync_v1()`

Added

to set device memory limits in a cgroup partition.`nvmlDeviceSetMemoryLimits_v1()`

Added

to get device memory limits in a cgroup partition.`nvmlDeviceGetMemoryLimits_v1()`

Modified

to account for cgroup memory partitions when called within the partition.`nvmlDeviceGetMemoryInfo_v2()`

Added

and`nvmlDeviceSetAdaptiveTgpMode_v1()`

to set and query Adaptive TGP mode.`nvmlDeviceGetAdaptiveTgpModeInfo_v1()`

Added

to get historical NVLink telemetry samples.`nvmlDeviceGetNvLinkTelemetrySamples_v1()`

Modified

to allow non-privileged access using WPPS capability.`nvmlDeviceWorkloadPowerProfileUpdateProfiles_v1()`

Added new Workload Power Profile types to

.`nvmlPowerProfileType_t`

Added GPM metrics

`NVML_GPM_METRIC_NVLINK_L[36..71]`

.Added missing comments on GPM metrics of C2C, cache, NVENC, GR CTXSW, and NVLink PER_SEC.

Added new GPU fabric clique types and structures for per-type clique information:

Added

to retrieve per-type fabric clique assignments.`nvmlDeviceGetGpuFabricInfo_v4()`

Deprecated

in favor of`nvmlGpuFabricInfo_v3_t`

.`nvmlGpuFabricInfo_v4_t`

Added new

`NVML_GPU_FABRIC_HEALTH_MASK_GFM_STATE*`

Health Mask flags to GPU Fabric Health Mask.

## Changes between NVML v595 and v610[#](https://docs.nvidia.com#changes-between-nvml-v595-and-v610)

Added new MCLK field IDs:

Added new NVLINK field IDs:

Added

to retrieve additional utilization information:`nvmlDeviceGetAccountingStats_v2()`

`sampleCount`

`sumGpuUtil`

`sumFbUtil`


Added a new NVLINK field ID:

Added support for new power scope

, which represents GPU base power.`NVML_POWER_SCOPE_GPU_BASE`

Added support in Power Management APIs:

`nvmlDeviceGetPowerManagementLimit_v2`


Added support for the following

fields with the new scope:`nvmlFieldValue_t`


Added support for detecting

on Thor Jetson platforms through:`nvmlClocksEventReasonSwThermalSlowdown`

Added

for MMA stall telemetry.`NVML_FI_DEV_MMA_STALL_PERCENT`

Updated field ID

value type from`NVML_FI_DEV_MMA_STALL_PERCENT`

to`NVML_VALUE_TYPE_UNSIGNED_INT`

.`NVML_VALUE_TYPE_DOUBLE`

Added

to get Performance Metric samples.`nvmlDevicePerfMetricsGetSamples_v1()`

Added

for State-Of-Charge Power Smoothing support.`NVML_FI_PWR_SMOOTHING_SOC_POWER_SMOOTHING_ENABLED`

Added public API support for Common Platform Error Record (CPER) data:

to retrieve CPER records using a caller-supplied buffer and cursor-based iteration.`nvmlSystemGetCPER_v1()`

for input and output values, including cursor, buffer, and buffer size.`nvmlGetCPER_v1_t`

for query filters and read position, including`nvmlCPERCursor_v1_t`

`cperTypeMask`

,`uuid`

, and`handle`

.and`nvmlCPERType_t`

for record type filtering.`NVML_CPER_ACCESS_TYPE_GPU`

for cursor initialization.`NVML_CPER_CURSOR_HANDLE_INIT`

Added size-query support by calling with

`buffer`

set to`NULL`

and`bufferSize`

set to`0`

. The API returnswith the required size, or`NVML_ERROR_INSUFFICIENT_SIZE`

with`NVML_SUCCESS`

`bufferSize`

set to`0`

when no records exist.


## Changes between NVML v590 and v595[#](https://docs.nvidia.com#changes-between-nvml-v590-and-v595)

Added new NVLINK field IDs:

Updated the descriptions of

and`nvmlGpmSampleGet()`

to emphasize that both device and MIG handles are supported by these APIs.`nvmlGpmQueryDeviceSupport()`

Added

to force GPU initialization when a previous`NVML_INIT_FLAG_FORCE_INIT`

was called with`nvmlInit`

`NO_GPUS`

and`NO_ATTACH`

flags.Updated the GPM metrics’ name from

`NVLINK1_L[0..17]`

to`NVLINK_L[18..35]`

.Updated Nvlink Version to include

.`NVML_NVLINK_VERSION_6_0`

Added a new API to retrieve GPU PRM counters:

.`nvmlDeviceReadPRMCounters_v1()`

Added new

enum to`NVML_GPU_RECOVERY_ACTION_RECOVER_IMEX_DOMAIN`

`nvmlDeviceGpuRecoveryAction_s`

.Added

, which returns the cumulative number of seconds the GPU has had the driver loaded.`nvmlDeviceGetBBXTimeData_v1()`

Added new GPM UTIL metric

.`NVML_GPM_METRIC_DMMA_TENSOR_UTIL`

Added new GPM raw metrics.

Added

to fetch the vGPU software scheduler state without taking ARR mode into account.`nvmlDeviceGetVgpuSchedulerState_v2()`

Added

to fetch the vGPU software scheduler state for the given GPU Instance without taking ARR mode into account.`nvmlGpuInstanceGetVgpuSchedulerState_v2()`

Added

to query new field weight in the vGPU software scheduler logs for the device.`nvmlDeviceGetVgpuSchedulerLog_v2()`

Added

to query new field weight in the vGPU software scheduler logs for the given GPU Instance.`nvmlGpuInstanceGetVgpuSchedulerLog_v2()`

Added

to set the vGPU scheduler state, with support for disabling ARR mode removed in this version.`nvmlDeviceSetVgpuSchedulerState_v2()`

Added

to set the vGPU scheduler state for the given GPU Instance, with support for disabling ARR mode removed in this version.`nvmlGpuInstanceSetVgpuSchedulerState_v2()`

Deprecated vGPU scheduler APIs:

Added

to force GSP unload on a vGPU host.`nvmlDeviceVgpuForceGspUnload()`

Added new Incorrect Configuration Status to

:`nvmlGpuFabricInfoV_t`

Added new

`NVML_GPU_FABRIC_HEALTH_MASK_PARTITION_ASSIGNED*`

Health Mask flags to GPU Fabric Health Mask.Added vGPU ‘NVIDIA RTX Virtual Game Dev’ as a licensed product for vGPU.

Added new MIG profile

for 3-slice graphics and media support.`NVML_GPU_INSTANCE_PROFILE_3_SLICE_GFX`


## Changes between v580 and v590[#](https://docs.nvidia.com#changes-between-v580-and-v590)

The following new functionality is exposed on NVIDIA display drivers version 590 Production or later.

Added new product architecture

.`NVML_DEVICE_ARCH_NPU3`

Deprecated

product brand.`NVML_BRAND_NVIDIA_DLA`

Added new

product brand.`NVML_BRAND_NVIDIA_NPU`

Added

to clear, set, or clobber existing workload power profiles from a single API.`nvmlDeviceWorkloadPowerProfileUpdateProfiles_v1()`

Deprecated workload power profile APIs, which will be removed in CUDA 15.0:

Added

field value to report the current EDPp multiplier as a percentage.`NVML_FI_DEV_EDPP_MULTIPLIER`

Added

to report whether or not there is unrepairable memory.`nvmlDeviceGetUnrepairableMemoryFlag_v1()`

Updated

and`nvmlDeviceGetVgpuSchedulerLog()`

to access the vGPU scheduler logs for the NVENC0 and NVENC1 engines.`nvmlGpuInstanceGetVgpuSchedulerState()`

Updated

to 36 to accommodate for more NvLinks in Rubin.`NVML_NVLINK_MAX_LINKS`

Added NVLINK1 GPM metrics for Rubin.

Added 14 new Power Smoothing field IDs for Delayed Power Smoothing:

Added four new Power Smoothing profile parameter IDs to set new Delayed Power Smoothing profile fields:

Added

to force GPU initialization when a previous`NVML_INIT_FLAG_FORCE_INIT`

was called with`nvmlInit`

`NO_GPUS`

and`NO_ATTACH`

flags.

## Changes between v575 and v580[#](https://docs.nvidia.com#changes-between-v575-and-v580)

The following new functionality is exposed on NVIDIA display drivers version 580 Production or later.

Added

to query the number of inactive remapped rows.`nvmlDeviceGetRemappedRows_v2()`

Added

and`NVML_FI_DEV_REMAPPED_ROWS_COR_INACTIVE`

for`NVML_FI_DEV_REMAPPED_ROWS_UNC_INACTIVE`

to query the number of inactive remapped rows.`nvmlDeviceGetFieldValues()`

Fixed bug with

`NVML_FI_PWR_SMOOTHING_*`

field value numbering, which was different than the v570 values.Adjusted

`NVML_FI_DEV_CLOCKS_EVENT_REASON_*`

and`NVML_FI_DEV_POWER_SYNC_BALANCING_*`

field value numbering to resolve overlap with`NVML_FI_PWR_SMOOTHING_*`

field values.Added

to clear, set, or clobber existing profiles from a single API.`nvmlDeviceWorkloadPowerProfileUpdateProfiles_v1()`

Added

to set RUSD (read only user shared data buffer) polling mask.`nvmlDeviceSetRusdSettings_v1()`

Added

to get the counts of SRAM unique uncorrected ECC errors.`nvmlDeviceGetSramUniqueUncorrectedEccErrorCounts()`

Deprecated Applications Clocks APIs, which will be removed in CUDA 14.0:

Deprecated

, which will be removed in CUDA 14.0.`nvmlDeviceGetViolationStatus()`

Added

to query device NVLINK info.`nvmlDeviceGetNvLinkInfo()`

Added

to retrieve the device GPU PDI.`nvmlDeviceGetPdi()`

Added Multi-GPU mode NVLINK Encryption

.`NVML_CC_SYSTEM_MULTIGPU_NVLE`

Added V2 struct to

to query NVLINK Firmware info.`nvmlDeviceGetNvLinkInfo()`

Added

to retrieve GPU PRM register contents.`nvmlDeviceReadWritePRM_v1()`

Added

to retrieve the addressing mode for the device.`nvmlDeviceGetAddressingMode()`

Added

to get ECC status info.`nvmlDeviceGetRepairStatus()`

Added DLA device support.

Added

, which allows for MIG GPU instance profile info to be queried with profileId instead of profile name.`nvmlDeviceGetGpuInstanceProfileInfoByIdV()`

Updated

to v3 to include a new Health Summary field and new Incorrect Configuration statuses.`nvmlGpuFabricInfoV_t`

is deprecated and will be removed in a future release.`nvmlGpuFabricInfo_v2_t`

New Incorrect Configuration Statuses:


Added

to query the current and supported power mizer modes on Maxwell and newer GPUs. Power mizer mode provides a hint to the driver as to how to manage GPU performance.`nvmlDeviceGetPowerMizerMode_v1()`

Added

to set the power mizer mode on Maxwell and newer GPUs.`nvmlDeviceSetPowerMizerMode_v1()`

Added

and`nvmlDeviceSetHostname_v1()`

to allow custom GPU hostname configuration.`nvmlDeviceGetHostname_v1()`


## Changes between v570 Update and v575[#](https://docs.nvidia.com#changes-between-v570-update-and-v575)

The following new functionality is exposed on NVIDIA display drivers version 575 Production or later.

Added

to create a system event set.`nvmlSystemEventSetCreate()`

Added

to release a system event set.`nvmlSystemEventSetFree()`

Added

to register system events on a system event set.`nvmlSystemRegisterEvents()`

Added

to wait for system event notification and obtain system event data.`nvmlSystemEventSetWait()`

Added

to query the currently creatable vGPU types on the user-provided GPU Instance.`nvmlGpuInstanceGetCreatableVgpus()`

Added

to query the maximum number of vGPU instances per GPU Instance for the given vGPU type.`nvmlVgpuTypeGetMaxInstancesPerGpuInstance()`

Added

to set the vGPU scheduler state for the given GPU Instance.`nvmlGpuInstanceSetVgpuSchedulerState()`

Added

to query the currently active vGPU instances on the user-provided GPU Instance.`nvmlGpuInstanceGetActiveVgpus()`

Added

to query the vGPU software scheduler state for the given GPU Instance.`nvmlGpuInstanceGetVgpuSchedulerState()`

Added

to query the vGPU software scheduler logs for the given GPU Instance.`nvmlGpuInstanceGetVgpuSchedulerLog()`

Added

to query the creatable vGPU placement IDs of the vGPU type within a GPU Instance.`nvmlGpuInstanceGetVgpuTypeCreatablePlacements()`

Added

to enable or disable vGPU heterogeneous mode for the GPU Instance.`nvmlGpuInstanceSetVgpuHeterogeneousMode()`

Added

to query the vGPU heterogeneous mode for the GPU Instance.`nvmlGpuInstanceGetVgpuHeterogeneousMode()`

Updated

to report whether GPU supports timesliced vGPU on MIG and whether MIG timesliced mode is enabled or not.`nvmlDeviceGetVgpuCapabilities()`

Updated

to set the MIG timesliced mode vGPU capability of a device.`nvmlDeviceSetVgpuCapabilities()`

Updated

to return`nvmlDeviceSetVgpuHeterogeneousMode()`

when in MIG mode.`NVML_ERROR_NOT_SUPPORTED`

Updated

to return`nvmlDeviceGetVgpuHeterogeneousMode()`

when in MIG mode.`NVML_ERROR_NOT_SUPPORTED`

Updated

to return`nvmlDeviceGetVgpuTypeCreatablePlacements()`

when in MIG mode.`NVML_ERROR_NOT_SUPPORTED`

Updated

to return`nvmlDeviceGetVgpuSchedulerLog()`

when in MIG mode.`NVML_ERROR_NOT_SUPPORTED`

Updated

to return`nvmlDeviceSetVgpuSchedulerState()`

when in MIG mode.`NVML_ERROR_NOT_SUPPORTED`

Updated

to return`nvmlDeviceGetVgpuSchedulerState()`

when in MIG mode.`NVML_ERROR_NOT_SUPPORTED`

Added 3 new

`NVML_FI_DEV_C2C_LINK_ERROR`

field IDs:Added

field ID.`NVML_FI_DEV_C2C_LINK_POWER_STATE`

Added new CTXSW GPM Metrics.

Added

that supports both ASCII and binary format UUID to retrieve the device handle.`nvmlDeviceGetHandleByUUIDV()`

Added 2 new

`NVML_FI_DEV_POWER_SYNC_BALANCING`

field IDs:Added 5 new Clock Event Reason Counters field IDs:

Updated

to better account for transient vs. permanent errors.`nvmlDeviceGetMemoryErrorCounter()`

Added MIG profiles that can allocate all or none of Decoder, Encoder, JPEG, and OFA engines.


## Changes between v565 and v570[#](https://docs.nvidia.com#changes-between-v565-and-v570)

The following new functionality is exposed on NVIDIA display drivers version 570 Production or later.

Added field values for data related to Power Smoothing

Added

to activate a specific Preset Profile for Power Smoothing`nvmlDevicePowerSmoothingActivatePresetProfile()`

Added

to enable/disable the Power Smoothing feature`nvmlDevicePowerSmoothingSetState()`

Added

to update parameters to preset profiles for Power Smoothing`nvmlDevicePowerSmoothingUpdatePresetProfileParam()`

Added new enums for fieldId NVML_FI_DEV_NVLINK_GET_STATE to expose INACTIVE, ACTIVE, and SLEEP state for a link

Added

to retrieve the thermal margin temperature (distance to nearest slowdown threshold).`nvmlDeviceGetMarginTemperature()`

Added

to get all supported Nvlink Bandwidth modes`nvmlDeviceGetNvlinkSupportedBwModes()`

Added

to get the current Nvlink Bandwidth mode`nvmlDeviceGetNvlinkBwMode()`

Added

to set the Nvlink Bandwidth mode`nvmlDeviceSetNvlinkBwMode()`

Added MIG profiles with support for graphics.

Added support for new recovery action - NVML_GPU_RECOVERY_ACTION_DRAIN_AND_RESET

Deprecated nvml fieldIds NVML_FI_DEV_RESET_STATUS and NVML_FI_DEV_DRAIN_AND_RESET_STATUS. Usee NVML_FI_DEV_GET_GPU_RECOVERY_ACTION instead

Added

and`nvmlDeviceGetDramEncryptionMode()`

to query and configure DRAM Encryption Mode`nvmlDeviceSetDramEncryptionMode()`

Added 3 new flags to GPU Fabric Health Mask:

NVML_GPU_FABRIC_HEALTH_MASK_SHIFT_ROUTE_RECOVERY

NVML_GPU_FABRIC_HEALTH_MASK_SHIFT_ROUTE_UNHEALTHY

NVML_GPU_FABRIC_HEALTH_MASK_SHIFT_ACCESS_TIMEOUT_RECOVERY


Added new counters for Nvlink5

to get sum of the number of errors in each Nvlink packet`NVML_FI_DEV_NVLINK_COUNT_EFFECTIVE_ERRORS`

to get Effective BER for effective errors`NVML_FI_DEV_NVLINK_COUNT_EFFECTIVE_BER`

to 15 to get count of symbol errors that are corrected`NVML_FI_DEV_NVLINK_COUNT_FEC_HISTORY_0`

Swapped the values of field IDs

and`NVML_FI_DEV_IS_MIG_MODE_INDEPENDENT_MIG_QUERY_CAPABLE`

to fix backwards compatibility with v550.`NVML_FI_DEV_NVLINK_GET_POWER_THRESHOLD_MAX`

New revision of

`nvmlPlatformInfo_t -- nvmlPlatformInfo_v2`

has been added. In this version the following fields from v1 have been renamedrackGuid to chassisSerialNumber

chassisPhysicalSlotNumber to slotNumber

computeSlotIndex to trayIndex

nodeIndex to hostId


is deprecated and will be removed in subsequent releases`nvmlPlatformInfo_v1`

Revert the fix for the issue where PCIe throughput (reported via

and nvidia-smi -q) is 1000 times bigger than its actual value`nvmlDeviceGetPcieThroughput()`


## Changes between v560 and v565[#](https://docs.nvidia.com#changes-between-v560-and-v565)

The following new functionality is exposed on NVIDIA display drivers version 565 Production or later.

Fixed the ECC error count mismatch between nvidia-smi query output and NVML APIs,

and`nvmlDeviceGetMemoryErrorCounter()`

.`nvmlDeviceGetFieldValues()`

Added new value NVML_CC_SYSTEM_CPU_CAPS_AMD_SNP_VTOM for CC CPU capability reporting.

Added

to retrieve a cooler’s control signal characteristics and target that cooler cools.`nvmlDeviceGetCoolerInfo()`

Added new value

for CC CPU capability reporting.`NVML_CC_SYSTEM_CPU_CAPS_AMD_SEV_SNP`

Added

to report the intended operating speed in rotations per minute (RPM) of the device’s specified fan.`nvmlDeviceGetFanSpeedRPM()`

Added

to retrieve a performance modes string with all the performance modes defined for this device along with their associated GPU Clock and Memory Clock values.`nvmlDeviceGetPerformanceModes()`

Added

to retrieve a string with the associated GPU Clock and Memory Clock values for the current pstate.`nvmlDeviceGetCurrentClockFreqs()`

Added

enum to define NvLink Version.`nvmlNvlinkVersion_t`

Added

to retrieve the platform information of a device.`nvmlDeviceGetPlatformInfo()`

Added new event type nvmlEventTypeGpuUnavailableError.

Removed support for

`nvmlDeviceGetNvLinkCrcLaneErrorCounter`

,`nvmlDeviceGetNvLinkEccLaneErrorCounter`

, andon Blackwell.`nvmlDeviceGetNvLinkErrorCounter()`

Removed support for fieldIds

,`NVML_FI_DEV_NVLINK_ERROR_DL_REPLAY`

, and`NVML_FI_DEV_NVLINK_ERROR_DL_RECOVERY`

on Blackwell.`NVML_FI_DEV_NVLINK_ERROR_DL_CRC`

Added

to get the vGPU runtime state size.`nvmlVgpuInstanceGetRuntimeStateSize()`

Updated

function to report both Heterogeneous and Homogeneous vGPU placements.`nvmlDeviceGetVgpuTypeSupportedPlacements()`

Updated nvmlDeviceGetVgpuCapabilities to report the Homogeneous vGPU capability.

Added new event type

.`nvmlEventTypeGpuRecoveryAction`

Added new fieldId to query GPU recovery action

.`NVML_FI_DEV_GET_GPU_RECOVERY_ACTION`

Deprecated fieldIds:

to get Number of VL15 MADs dropped on a link in NVLink5`NVML_FI_DEV_NVLINK_COUNT_VL15_DROPPED`

to get BER per lane for lane 0`NVML_FI_DEV_NVLINK_COUNT_RAW_BER_LANE0`

to get BER per lane for lane 1`NVML_FI_DEV_NVLINK_COUNT_RAW_BER_LANE1`

to get BER per link. Sum of all the raw errors per lane/Bits received per link`NVML_FI_DEV_NVLINK_COUNT_RAW_BER`

to get Sum of the number of errors in each Nvlink packet`NVML_FI_DEV_NVLINK_COUNT_EFFECTIVE_ERRORS`

to get Effective BER for effective errors`NVML_FI_DEV_NVLINK_COUNT_EFFECTIVE_BER`



## Changes between v555 and v560[#](https://docs.nvidia.com#changes-between-v555-and-v560)

The following new functionality is exposed on NVIDIA display drivers version 560 Production or later.

Added field values

and`NVML_FI_DEV_PCIE_OUTBOUND_ATOMICS_MASK`

for`NVML_FI_DEV_PCIE_INBOUND_ATOMICS_MASK`

.`nvmlDeviceGetFieldValues()`

Added field IDs

and`NVML_FI_DEV_RESET_STATUS`

which correspond to the nvidia-smi output.`NVML_FI_DEV_DRAIN_AND_RESET_STATUS`

Added

`NVML_DEVICE_ARCH_T23X`

architecture type.Added

to query the BAR1 information of a vGPU type.`nvmlVgpuTypeGetBAR1Info()`

Added new event types,

,`nvmlEventTypeSingleBitEccErrorStorm`

,`nvmlEventTypeDramRetirementEvent`

,`nvmlEventTypeDramRetirementFailure`

and`nvmlEventTypeNonFatalPoisonError`

.`nvmlEventTypeFatalPoisonError`

Added

to query the driver branch information.`nvmlSystemGetDriverBranch()`


## Changes between v550 and v555[#](https://docs.nvidia.com#changes-between-v550-and-v555)

The following new functionality is exposed on NVIDIA display drivers version 555 Production or later.

Added

to query min, max and current clock offset value on a Maxwell and later GPU for a specified clock. Note:`nvmlDeviceGetClockOffsets()`

,`nvmlDeviceGetGpcClkVfOffset()`

,`nvmlDeviceGetMemClkVfOffset()`

and`nvmlDeviceGetGpcClkMinMaxVfOffset()`

will be deprecated in a future release. Use`nvmlDeviceGetMemClkMinMaxVfOffset()`

instead.`nvmlDeviceGetClockOffsets()`

Added

to control clock offset value on a Maxwell and later GPU for a specified clock. Note:`nvmlDeviceSetClockOffsets()`

and`nvmlDeviceSetGpcClkVfOffset()`

will be deprecated in a future release. Use`nvmlDeviceSetMemClkVfOffset()`

instead.`nvmlDeviceSetClockOffsets()`

Added two new field IDs

and`NVML_FI_DEV_PCIE_COUNT_TX_BYTES`

for`NVML_FI_DEV_PCIE_COUNT_RX_BYTES`

.`nvmlDeviceGetFieldValues()`

Added new API

`nvmlDeviceGetCapabilities`

with the first capability bit`NVML_DEV_CAP_EGM`

for Extended GPU Memory (EGM) capability.Added

`multiGpuMode`

display on CC enabled system via new APIor “`nvmlSystemGetConfComputeSettings()`

`nvidia-smi conf-compute --get-multigpu-mode`

” or “`nvidia-smi conf-compute -mgm`

”.Added new field ID

to get the Max Nvlink Power Threshold for a device.`NVML_FI_DEV_NVLINK_GET_POWER_THRESHOLD_MAX`


## Changes between v545 and v550[#](https://docs.nvidia.com#changes-between-v545-and-v550)

The following new functionality is exposed on NVIDIA display drivers version 550 Production or later.

Added

to query the NUMA node of a GPU.`nvmlDeviceGetNumaNodeId()`

Added new GPM metric ID

to`NVML_GPM_METRIC_NVOFA_1_UTIL`

.`nvmlGpmMetricId_t`

Added new field ID

, to check MIG query capable device irrespective of MIG mode.`NVML_FI_DEV_IS_MIG_MODE_INDEPENDENT_MIG_QUERY_CAPABLE`

Deprecated

and added`NVML_P2P_CAPS_INDEX_PROP`

to reflect the same P2P capability.`NVML_P2P_CAPS_INDEX_PCI`

Added

to retrieve the recent utilization and process ID for all running processes.`nvmlDeviceGetProcessesUtilizationInfo()`

Added new struct

, which includes the new utilization of NVJPG and NVOFA.`nvmlProcessesUtilizationInfo_v1_t`

Added

to retrieve the recent utilization for vGPU instances running on a physical GPU.`nvmlDeviceGetVgpuInstancesUtilizationInfo()`

Added

to retrieve the recent utilization for processes running on vGPU instances on a physical GPU.`nvmlDeviceGetVgpuProcessesUtilizationInfo()`

Added

to enable or disable vGPU heterogenous mode for the device.`nvmlDeviceSetVgpuHeterogeneousMode()`

Added

to query the vGPU heterogenous mode for the device.`nvmlDeviceGetVgpuHeterogeneousMode()`

Added

to query placement ID of the active vGPU instance.`nvmlVgpuInstanceGetPlacementId()`

Added

to query the supported vGPU placement IDs of a vGPU type.`nvmlDeviceGetVgpuTypeSupportedPlacements()`

Added

to query the creatable vGPU placement IDs of a vGPU type.`nvmlDeviceGetVgpuTypeCreatablePlacements()`

Added support to display confidential compute protected memory along with

`fb`

and`bar1`

in`nvidia-smi pmon`

and`dmon`

commands.Added

to query GPU Fabric Probe Info for the device.`nvmlDeviceGetGpuFabricInfoV()`

Deprecated

. This function should not be used, and will be removed in a future release. Use`nvmlDeviceGetGpuFabricInfo()`

instead.`nvmlDeviceGetGpuFabricInfoV()`

Modified

and`nvmlDeviceGetGpuInstanceProfileInfo()`

to no longer require MIG being enabled.`nvmlDeviceGetGpuInstancePossiblePlacements_v2()`

Added new encoder type

and`NVML_ENCODER_QUERY_AV1`

to enumeration`NVML_ENCODER_QUERY_UNKNOWN`

.`nvmlEncoderType_t`

Added

to set confidential compute key rotation threshold.`nvmlSystemSetConfComputeKeyRotationThresholdInfo()`

Added

to query confidential compute key rotation threshold detail.`nvmlSystemGetConfComputeKeyRotationThresholdInfo()`

Added

to set the desirable vGPU capability of a device.`nvmlDeviceSetVgpuCapabilities()`


## Changes between v535 and v545[#](https://docs.nvidia.com#changes-between-v535-and-v545)

The following new functionality is exposed on NVIDIA display drivers version 545 Production or later.

Added a new error code

to be returned if no supported GPUS are found during initialization.`NVML_ERROR_GPU_NOT_FOUND`

In

,`nvmlGpuFabricInfo_v2_t`

`partitionId`

has been renamed to`cliqueId`

.Added new versioned structs

and`nvmlGpuInstanceProfileInfo_v3_t`

.`nvmlComputeInstanceProfileInfo_v3_t`

Added

for retrieving the timestamp and duration of the latest flush of the BBX object to the inforom storage.`nvmlDeviceGetLastBBXFlushTime()`

Added

to report out power usage for GPU Memory.`NVML_POWER_SCOPE_MEMORY`

Added

which expands`nvmlDeviceGetPciInfo_v3()`

to also report PCI base and sub classcodes.`nvmlDeviceGetPciInfo`

Added new struct

, which is used in`nvmlPciInfoExt_v1_t`

.`nvmlDeviceGetPciInfoExt()`

Added

API to get information about Compute, Graphics or MPS-Compute processes running on a GPU with protected memory usage info.`nvmlDeviceGetRunningProcessDetailList()`


## Changes between v530 and v535[#](https://docs.nvidia.com#changes-between-v530-and-v535)

The following new functionality is exposed on NVIDIA display drivers version 535 Production or later.

Added

to query SRAM ECC error status for the device.`nvmlDeviceGetSramEccErrorStatus()`

Added

for getting device module ID.`nvmlDeviceGetModuleId()`

Updated

API to report undersized power source.`nvmlDeviceGetPowerSource()`

Added:cpp:func:nvmlDeviceGetJpgUtilization and

APIs.`nvmlDeviceGetOfaUtilization()`

Added

and`nvmlSystemGetNvlinkBwMode()`

APIs.`nvmlSystemSetNvlinkBwMode()`

Added

to set the vGPU scheduler state.`nvmlDeviceSetVgpuSchedulerState()`

Added new field ID

for device’s resetless MIG capability.`NVML_FI_DEV_IS_RESETLESS_MIG_SUPPORTED`

Added

to get information about Compute processes running on a GPU.`nvmlDeviceGetComputeRunningProcesses_v3()`

Added

to get information about Graphics processes running on a GPU.`nvmlDeviceGetGraphicsRunningProcesses_v3()`

Added

to get information about MPS-Compute processes running on a GPU.`nvmlDeviceGetMPSComputeRunningProcesses_v3()`

Added

to get information about Compute, Graphics or MPS-Compute processes running on a GPU with protected memory usage info.`nvmlDeviceGetRunningProcessDetailList()`

Added

for retrieving the timestamp and duration of the latest flush of the BBX object to the inforom storage.`nvmlDeviceGetLastBBXFlushTime()`

Added new field ID

for PCIe correctable errors counter.`NVML_FI_DEV_PCIE_COUNT_CORRECTABLE_ERRORS`

Added new field ID

for PCIe NAK Receive counter.`NVML_FI_DEV_PCIE_COUNT_NAKS_RECEIVED`

Added new field ID

for PCIe receiver error counter.`NVML_FI_DEV_PCIE_COUNT_RECEIVER_ERROR`

Added new field ID

for PCIe bad TLP counter.`NVML_FI_DEV_PCIE_COUNT_BAD_TLP`

Added new field ID

for NAK Send counter.`NVML_FI_DEV_PCIE_COUNT_NAKS_SENT`

Added new field ID

for PCIe bad DLLP counter.`NVML_FI_DEV_PCIE_COUNT_BAD_DLLP`

Added new field ID

for PCIe non fatal error counter.`NVML_FI_DEV_PCIE_COUNT_NON_FATAL_ERROR`

Added new field ID

for PCIe fatal error counter.`NVML_FI_DEV_PCIE_COUNT_FATAL_ERROR`

Added new field ID

for PCIe unsupported request counter.`NVML_FI_DEV_PCIE_COUNT_UNSUPPORTED_REQ`

Added new field ID

for PCIe LCRC error counter.`NVML_FI_DEV_PCIE_COUNT_LCRC_ERROR`

Added

`new field ID NVML_FI_DEV_PCIE_COUNT_LANE_ERROR`

for per lane error counter with scope as PCIe lane number.Added

`nvmlDeviceGetPowerUsage_v2`

to retrieve current power usage.Added

`nvmlDeviceGetTotalEnergyConsumption_v2`

to get current energy consumption.Added

to set the power limit.`nvmlDeviceSetPowerManagementLimit_v2()`

Added new field IDs,

`NVML_FI_GPU_POWER_AVERAGE`

and`NVML_FI_GPU_POWER_INSTANT`

, to query power usage.Renamed

`nvmlDeviceCcuGetStreamState`

toand`nvmlGpmQueryIfStreamingEnabled()`

`nvmlDeviceCcuSetStreamState`

to.`nvmlGpmSetStreamingEnabled()`

Added support to display confidential compute protected memory along with fb and bar1 in

`nvidia-smi pmon`

and`dmon`

commands.Added new field IDs

,`NVML_FI_DEV_TEMPERATURE_SHUTDOWN_TLIMIT`

,`NVML_FI_DEV_TEMPERATURE_SLOWDOWN_TLIMIT`

, and`NVML_FI_DEV_TEMPERATURE_MEM_MAX_TLIMIT`

to query temperature thresholds on Ada and later architectures.`NVML_FI_DEV_TEMPERATURE_GPU_MAX_TLIMIT`

Introduced

`ClockEventReasons`

and related APIs which should be used instead of`ClockThrottleReasons`

. Deprecated`ClockThrottleReasons`

.Added ability to get GPS Temperature Threshold with

using the new enum`nvmlDeviceGetTemperatureThreshold()`

.`NVML_TEMPERATURE_THRESHOLD_GPS_CURR`


## Changes between v525 and v530[#](https://docs.nvidia.com#changes-between-v525-and-v530)

The following new functionality is exposed on NVIDIA display drivers version 530 Production or later.

Fixed a typo in

: added a new enum entry for`nvmlGpuP2PStatus_t`

with the same numeric value as the existing erroneous entry (”`NVML_P2P_STATUS_CHIPSET_NOT_SUPPORTED`

”).`NVML_P2P_STATUS_CHIPSET_NOT_SUPPORED`

Added

to fetch the vGPU software scheduler logs.`nvmlDeviceGetVgpuSchedulerLog()`

Added

to fetch the vGPU software scheduler state.`nvmlDeviceGetVgpuSchedulerState()`

Added

to fetch the vGPU software scheduler capabilities.`nvmlDeviceGetVgpuSchedulerCapabilities()`


## Changes between v520 and v525[#](https://docs.nvidia.com#changes-between-v520-and-v525)

The following new functionality is exposed on NVIDIA display drivers version 525 Production or later.

Added

`nvmlDeviceGetPcieAtomicCaps`

to report PCIe atomic capabilities.Added

`nvmlDeviceCcuGetStreamState`

API to report the counter collection unit stream state.Added

`nvmlDeviceCcuSetStreamState`

API to set the counter collection unit stream state.Removed support for

`NVML_FI_DEV_LINK_SPEED_MBPS_L{0..}`

field IDs in Hopper. Replaced withwith scope as link ID.`NVML_FI_DEV_NVLINK_GET_SPEED`

Removed support for

`NVML_FI_DEV_NVLINK_CRC_FLIT_ERROR_COUNT{0..}`

field IDs in Hopper. Replaced withwith scope as link ID.`NVML_FI_DEV_NVLINK_ERROR_DL_CRC`

Removed support for

`NVML_FI_DEV_NVLINK_REPLAY_ERROR_COUNT_L{0..}`

field IDs in Hopper. Replaced withwith scope as link ID.`NVML_FI_DEV_NVLINK_ERROR_DL_REPLAY`

Removed support for

`NVML_FI_DEV_NVLINK_RECOVERY_ERROR_COUNT_{0..}`

field IDs in Hopper. Replaced withwith scope as link ID.`NVML_FI_DEV_NVLINK_ERROR_DL_RECOVERY`

Added new field ID

to get nvlink state.`NVML_FI_DEV_NVLINK_GET_STATE`

Added new field ID

to get nvlink version.`NVML_FI_DEV_NVLINK_GET_VERSION`

Added new field ID

to get C2C link count.`NVML_FI_DEV_C2C_LINK_COUNT`

Added new field ID

to get C2C link status.`NVML_FI_DEV_C2C_LINK_GET_STATUS`

Added new field ID

to get C2C link bandwidth.`NVML_FI_DEV_C2C_LINK_GET_MAX_BW`


## Changes between v515 and v520[#](https://docs.nvidia.com#changes-between-v515-and-v520)

The following new functionality is exposed on NVIDIA display drivers version 520 Production or later.

Added

API to report the MemClk VF offset value.`nvmlDeviceGetMemClkVfOffset()`

Added

API to set the MemClk VF offset value.`nvmlDeviceSetMemClkVfOffset()`

Added

API to report the Memory clock min and max VF offset that user can set for a specified GPU.`nvmlDeviceGetMemClkMinMaxVfOffset()`

Added

API to report the intended target speed of the device’s specified fan.`nvmlDeviceGetTargetFanSpeed()`

Added

API to report the Graphics clock min and max VF offset that user can set for a specified GPU.`nvmlDeviceGetGpcClkMinMaxVfOffset()`

Added

to calculate GPM metrics from two GPM samples.`nvmlGpmMetricsGet()`

Added

to free allocated GPM sample.`nvmlGpmSampleFree()`

Added

to allocate a GPM sample.`nvmlGpmSampleAlloc()`

Added

to retrieve a GPM snapshot.`nvmlGpmSampleGet()`

Added

to query whether a device supports GPM`nvmlGpmQueryDeviceSupport()`

Added

`nvmlDeviceGetSupportedPowerModes`

API to report the GPU’s supported power mode mask.Added

`nvmlDeviceGetPowerMode`

API to report the GPU’s current power mode.Added

`nvmlDeviceSetPowerMode`

API to set the new power mode.Added

API to report the control policy for a specified GPU fan.`nvmlDeviceGetFanControlPolicy_v2()`

Added

API to set the control policy for a specified GPU fan.`nvmlDeviceSetFanControlPolicy()`


## Changes between v510 and v515[#](https://docs.nvidia.com#changes-between-v510-and-v515)

The following new functionality is exposed on NVIDIA display drivers version 515 Production or later.

Added

`nvmlDeviceGetDefaultECCMode`

API to report the GPU’s default ECC Mode.Added

API to report the GPU’s PCIe link speed.`nvmlDeviceGetPcieSpeed()`

Added

API to report the GPU’s P-states information.`nvmlDeviceGetDynamicPstatesInfo()`

Added

API to set the GPU’s fan speed.`nvmlDeviceSetFanSpeed_v2()`

Added

API to set the GPU’s default fan speed.`nvmlDeviceSetDefaultFanSpeed_v2()`

Added

API to report the GPU’s thermal system information.`nvmlDeviceGetThermalSettings()`

Added

API to report the min and max clocks of some clock domain for a given PState.`nvmlDeviceGetMinMaxClockOfPState()`

Added

API to get all supported Performance States (P-States) for the GPU.`nvmlDeviceGetSupportedPerformanceStates()`

Added

API to report the GPCCLK VF offset value.`nvmlDeviceGetGpcClkVfOffset()`

Added

API to set the GPCCLK VF offset value.`nvmlDeviceSetGpcClkVfOffset()`

Added

API to report the min and max fan speed that user can set for a specified GPU fan.`nvmlDeviceGetMinMaxFanSpeed()`


## Changes between v495 and v510[#](https://docs.nvidia.com#changes-between-v495-and-v510)

The following new functionality is exposed on NVIDIA display drivers version 510 Production or later.

Added

and`nvmlDeviceGetGpuInstanceProfileInfoV()`

APIs to include the profile name in their output.`nvmlGpuInstanceGetComputeInstanceProfileInfoV()`

Added

API to report the GPU’s Memory Bus Width.`nvmlDeviceGetMemoryBusWidth()`

Added

API to report the GPU’s PCIe Max Speed.`nvmlDeviceGetPcieLinkMaxSpeed()`

Added

API to report the GPU’s power source as AC or battery.`nvmlDeviceGetPowerSource()`

Added

API to report the GPU’s number of fans.`nvmlDeviceGetNumFans()`

Added

API to report the GPU’s number of cores.`nvmlDeviceGetNumGpuCores()`

Added

. The new version accounts separately for system-reserved memory, and includes it in the used memory amount. The previous version of the API reduced the total memory amount by the amount of system-reserved memory.`nvmlDeviceGetMemoryInfo_v2()`

Added

API to report the status of adaptive clocking for the GPU.`nvmlDeviceGetAdaptiveClockInfoStatus()`


## Changes between v465 and v470[#](https://docs.nvidia.com#changes-between-v465-and-v470)

The following new functionality is exposed on NVIDIA display drivers version 470 Production or later.

Added new MIG GPU instance profile NVML_GPU_INSTANCE_PROFILE_1_SLICE_REV1.

Added

. The previous version of the API will not support the profiles with possible placements greater than its total capacity, such as NVML_GPU_INSTANCE_PROFILE_1_SLICE_REV1.`nvmlDeviceGetGpuInstancePossiblePlacements_v2()`


## Changes between v460 and v465[#](https://docs.nvidia.com#changes-between-v460-and-v465)

The following new functionality is exposed on NVIDIA display drivers version 465 Production or later.

Added new NVML_BRAND_* enumeration values for NVIDIA, NVIDIA_RTX, GEFORCE_RTX, QUADRO_RTX and TITAN_RTX.

Updated

to make it MIG-aware.`nvmlDeviceGetHandleByUUID()`

Updated

to return MIG UUIDs in the canonical format, ‘MIG-UUID’.`nvmlDeviceGetUUID()`

Updated

to accept both UUID formats, ‘MIG-UUID’ and ‘MIG-GPU UUID/GID/CID’.`nvmlDeviceGetHandleByUUID()`

The

and`nvmlDeviceSetAPIRestriction()`

APIs would no longer support the ability to toggle root-only requirement for`nvmlDeviceGetAPIRestriction()`

and`nvmlDeviceSetApplicationsClocks()`

.`nvmlDeviceResetApplicationsClocks()`


## Changes between v450 and v460[#](https://docs.nvidia.com#changes-between-v450-and-v460)

The following new functionality is exposed on NVIDIA display drivers version 460 Production or later.

Added

to allow placement specification when creating a new MIG GPU instance.`nvmlDeviceCreateGpuInstanceWithPlacement()`


## Changes between v445 and v450[#](https://docs.nvidia.com#changes-between-v445-and-v450)

The following new functionality is exposed on NVIDIA display drivers version 450 Production or later.

Updated

and`nvmlDeviceGetFanSpeed()`

for allowing fan speeds greater than 100% to be reported.`nvmlDeviceGetFanSpeed_v2()`

Added

to determine the closest processor(s) within a NUMA node or socket.`nvmlDeviceGetCpuAffinityWithinScope()`

Added

to determine the closest NUMA node(s) within a NUMA node or socket.`nvmlDeviceGetMemoryAffinity()`

Added support to query and disable MIG mode on Windows.


## Changes between v418 and v445[#](https://docs.nvidia.com#changes-between-v418-and-v445)

The following new functionality is exposed on NVIDIA display drivers version 445 Production or later.

Added support for the NVIDIA Ampere architecture.

Added support for Multi Instance GPU management. Refer to the “Multi Instance GPU Management” section for details.


## Changes between v361 and v418[#](https://docs.nvidia.com#changes-between-v361-and-v418)

The following new functionality is exposed on NVIDIA display drivers version 418 Production or later.

Added support for the Volta and Turing architectures, bug fixes, performance improvements, and new features.


## Changes between v349 and v361[#](https://docs.nvidia.com#changes-between-v349-and-v361)

The following new functionality is exposed on NVIDIA display drivers version 361 Production or later.

Added

to return GPU part numbers`nvmlDeviceGetBoardPartNumber()`

Removed support for exclusive thread compute mode (Deprecated in 7.5)

Added NVML_CLOCK_VIDEO (encoder/decoder) clock type as a supported clock type for

and`nvmlDeviceGetClockInfo()`

.`nvmlDeviceGetMaxClockInfo()`


## Changes between v346 and v349[#](https://docs.nvidia.com#changes-between-v346-and-v349)

The following new functionality is exposed on NVIDIA display drivers version 349 Production or later.

Added

to find the common path between two devices.`nvmlDeviceGetTopologyCommonAncestor()`

Added

to get a set of GPUs given a path level.`nvmlDeviceGetTopologyNearestGpus()`

Added

to retrieve a set of GPUs with a given CPU affinity.`nvmlSystemGetTopologyGpuSet()`

Discontinued Perl bindings support.

Updated

,`nvmlDeviceGetAccountingPids()`

and`nvmlDeviceGetAccountingBufferSize()`

to report accounting information for both active and terminated processes. The execution time field in`nvmlDeviceGetAccountingStats()`

structure is populated only when the process is terminated.`nvmlAccountingStats_t`


## Changes between v340 and v346[#](https://docs.nvidia.com#changes-between-v340-and-v346)

The following new functionality is exposed on NVIDIA display drivers version 346 Production or later.

Added

`nvmlDeviceGetGraphicsRunningProcesses_v2`

to get information about Graphics Processes running on a device.Added

to get PCI replay counters.`nvmlDeviceGetPcieReplayCounter()`

Added

to get PCI utilization information.`nvmlDeviceGetPcieThroughput()`

Discontinued Perl bindings support.


## Changes between NVML v331 and v340[#](https://docs.nvidia.com#changes-between-nvml-v331-and-v340)

The following new functionality is exposed on NVIDIA display drivers version 340 Production or later.

Added

to get recent power, utilization and clock samples for the GPU.`nvmlDeviceGetSamples()`

Added

to get temperature thresholds for the GPU.`nvmlDeviceGetTemperatureThreshold()`

Added

to get the brand name of the GPU.`nvmlDeviceGetBrand()`

Added

to get the duration of time during which the device was throttled (lower than requested clocks) due to power or thermal constraints. Violations due to thermal capping is not supported at this time.`nvmlDeviceGetViolationStatus()`

Added

to get the GPU video encoder utilization.`nvmlDeviceGetEncoderUtilization()`

Added

to get the GPU video decoder utilization.`nvmlDeviceGetDecoderUtilization()`

Added

to get the closest processor(s) affinity to a particular GPU.`nvmlDeviceGetCpuAffinity()`

Added

to set the affinity of a particular GPU to the closest processor.`nvmlDeviceSetCpuAffinity()`

Added

to clear the affinity of a particular GPU.`nvmlDeviceClearCpuAffinity()`

Added

to get a unique boardId for the running system.`nvmlDeviceGetBoardId()`

Added

to get whether the device is on a multiGPU board.`nvmlDeviceGetMultiGpuBoard()`

Added

and`nvmlDeviceGetAutoBoostedClocksEnabled()`

for querying and setting the state of auto boosted clocks on supporting hardware.`nvmlDeviceSetAutoBoostedClocksEnabled()`

Added

for setting the default state of auto boosted clocks on supporting hardware.`nvmlDeviceSetDefaultAutoBoostedClocksEnabled()`


## Changes between NVML v5.319 Update and v331[#](https://docs.nvidia.com#changes-between-nvml-v5-319-update-and-v331)

The following new functionality is exposed on NVIDIA display drivers version 331 or later.

Added

to get the minor number for the device.`nvmlDeviceGetMinorNumber()`

Added

to get BAR1 total, available and used memory size.`nvmlDeviceGetBAR1MemoryInfo()`

Added

to get the information related to bridge chip firmware.`nvmlDeviceGetBridgeChipInfo()`

Added enforced power limit query API

`nvmlDeviceGetEnforcedPowerLimit()`

Updated

to return xid event data in case of xid error event.`nvmlEventSetWait`


## Changes between NVML v5.319 RC and v5.319 Update[#](https://docs.nvidia.com#changes-between-nvml-v5-319-rc-and-v5-319-update)

The following new functionality is exposed on NVIDIA display drivers version 319 Update or later.

Added

and`nvmlDeviceSetAPIRestriction()`

, with initial ability to toggle root-only requirement for`nvmlDeviceGetAPIRestriction()`

and`nvmlDeviceSetApplicationsClocks()`

.`nvmlDeviceResetApplicationsClocks()`


## Changes between NVML v4.304 Production and v5.319 RC[#](https://docs.nvidia.com#changes-between-nvml-v4-304-production-and-v5-319-rc)

The following new functionality is exposed on NVIDIA display drivers version 319 RC or later.

Added _v2 versions of

and`nvmlDeviceGetHandleByIndex`

that also count devices not accessible by current user`nvmlDeviceGetCount`

(default) can also return NVML_ERROR_NO_PERMISSION`nvmlDeviceGetHandleByIndex_v2()`


Added

and`nvmlInit_v2()`

that is safer and thus recommended function for initializing the library`nvmlDeviceGetHandleByIndex_v2()`

lazily initializes only requested devices (queried with nvmlDeviceGetHandle*)`nvmlInit_v2()`

nvml.h defines

and`nvmlInit_v2()`

as default functions`nvmlDeviceGetHandleByIndex_v2()`


Added

`nvmlDeviceGetIndex()`

Added NVML_ERROR_GPU_IS_LOST to report GPUs that have fallen off the bus.

All NVML device APIs can return this error code, as a GPU can fall off the bus at any time.


Added new class of APIs for gathering process statistics (

`nvmlAccountingStats`

)Application Clocks are no longer supported on GPU’s from Quadro product line

Added APIs to support dynamic page retirement. See

and`nvmlDeviceGetRetiredPages()`

`nvmlDeviceGetRetiredPagesPendingStatus()`

Renamed

to`nvmlClocksThrottleReasonUserDefinedClocks`

. Old name is deprecated and can be removed in one of the next major releases.`nvmlClocksThrottleReasonApplicationsClocksSetting`

Added

and updated documentation to clarify how it differs from`nvmlDeviceGetDisplayActive()`

`nvmlDeviceGetDisplayMode()`


## Changes between NVML v4.304 RC and v4.304 Production[#](https://docs.nvidia.com#changes-between-nvml-v4-304-rc-and-v4-304-production)

The following new functionality is exposed on NVIDIA display drivers version 304 Production or later.

## Changes between NVML v3.295 and v4.304 RC[#](https://docs.nvidia.com#changes-between-nvml-v3-295-and-v4-304-rc)

The following new functionality is exposed on NVIDIA display drivers version 304 RC or later.

Added

and`nvmlDeviceGetInforomConfigurationChecksum()`

.`nvmlDeviceValidateInforom()`

Added

and updated documentation to clarify how it differs from`nvmlDeviceGetDisplayActive()`

.`nvmlDeviceGetDisplayMode()`

Added new error return value for initialization failure due to kernel module not receiving interrupts.

Added

,`nvmlDeviceSetApplicationsClocks()`

,`nvmlDeviceGetApplicationsClock()`

.`nvmlDeviceResetApplicationsClocks()`

Added

and`nvmlDeviceGetSupportedMemoryClocks()`

.`nvmlDeviceGetSupportedGraphicsClocks()`

Added

,`nvmlDeviceGetPowerManagementLimitConstraints()`

and`nvmlDeviceGetPowerManagementDefaultLimit()`

.`nvmlDeviceSetPowerManagementLimit()`

Expanded

to support all CUDA capable GPUs.`nvmlDeviceGetUUID()`

Deprecated

in favor of`nvmlDeviceGetDetailedEccErrors()`

.`nvmlDeviceGetMemoryErrorCounter()`

Added

to support reporting of texture memory error counters.`NVML_MEMORY_LOCATION_TEXTURE_MEMORY`

Added

and`nvmlDeviceGetCurrentClocksThrottleReasons()`

.`nvmlDeviceGetSupportedClocksThrottleReasons()`

is now also reported on supported Kepler devices.`NVML_CLOCK_SM`

Dropped support for GT200 based Tesla brand GPUs: C1060, M1060, S1070.


## Changes between NVML v2.285 and v3.295[#](https://docs.nvidia.com#changes-between-nvml-v2-285-and-v3-295)

The following new functionality is exposed on NVIDIA display drivers version 295 or later.

Deprecated

in favor of newly added`nvmlDeviceGetHandleBySerial()`

.`nvmlDeviceGetHandleByUUID()`

Marked the input parameters of

,`nvmlDeviceGetHandleBySerial()`

and`nvmlDeviceGetHandleByUUID()`

as const.`nvmlDeviceGetHandleByPciBusId`

Added

.`nvmlDeviceOnSameBoard()`

Added

`nvmlConstants`

defines.Added

,`nvmlDeviceGetMaxPcieLinkGeneration()`

,`nvmlDeviceGetMaxPcieLinkWidth()`

,:cpp:func:nvmlDeviceGetCurrPcieLinkWidth.`nvmlDeviceGetCurrPcieLinkGeneration()`

Format change of

output to match the UUID standard. This function will return a different value.`nvmlDeviceGetUUID()`

will report zero for unsupported ECC error counters when a subset of ECC error counters are supported.`nvmlDeviceGetDetailedEccErrors()`


## Changes between NVML v1.0 and v2.285[#](https://docs.nvidia.com#changes-between-nvml-v1-0-and-v2-285)

The following new functionality is exposed on NVIDIA display drivers version 285 or later.

Added possibility to query separately current and pending driver model with

`nvmlDeviceGetDriverModel`

.Fixed error message when querying pending driver model with

`nvmlDeviceGetDriverModel`

on non-Admin user account.Fixed problem when

wouldn’t update.`nvmlDeviceGetDisplayMode()`


Added API

function to report VBIOS version.`nvmlDeviceGetVbiosVersion()`

Added pciSubSystemId to

struct.`nvmlPciInfo_t`

Added API

function to convert error code to string.`nvmlErrorString()`

Updated docs to indicate we support M2075 and C2075.

Added API

function to report HIC firmware version.`nvmlSystemGetHicVersion()`

Added NVML versioning support

Functions that changed API and/or size of structs have appended versioning suffix (e.g., nvmlDeviceGetPciInfo_v2). Appropriate C defines have been added that map old function names to the newer version of the function.


Added support for concurrent library usage by multiple libraries.

Added API

function for reporting device’s clock limits.`nvmlDeviceGetMaxClockInfo()`

Added new error code NVML_ERROR_DRIVER_NOT_LOADED used by

.`nvmlInit`

Extended

struct with new field: sub system id.`nvmlPciInfo_t`

Added NVML support on Windows guest account.

Changed format of pciBusId string (to XXXX:XX:XX.X) of

.`nvmlPciInfo_t`

Parsing of busId in

is less restrictive. You can pass 0:2:0.0 or 0000:02:00 and other variations.`nvmlDeviceGetHandleByPciBusId`

Added API for events waiting for GPU events (Linux only) see docs of

`nvmlEvents`

.Added API

`nvmlDeviceGetComputeRunningProcesses_v2`

andfunctions for looking up currently running compute applications.`nvmlSystemGetProcessName()`

Deprecated

in favor of`nvmlDeviceGetPowerState()`

.`nvmlDeviceGetPerformanceState()`