source: https://docs.nvidia.com/cupti/api/group__CUPTI__ACTIVITY__API.html

# 6.1. CUPTI Activity API[#](https://docs.nvidia.com#cupti-activity-api)

Functions, types, and enums that implement the CUPTI Activity API.

## 6.1.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUpti_Activity](https://docs.nvidia.com/structCUpti__Activity.html#structcupti__activity)The base activity record.

[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi)The activity record for a driver or runtime API invocation.

[CUpti_ActivityApiCbidOptions](https://docs.nvidia.com/structCUpti__ActivityApiCbidOptions.html#structcupti__activityapicbidoptions)Per-cbid enable/disable options for API activity kinds.

[CUpti_ActivityApiOptions](https://docs.nvidia.com/structCUpti__ActivityApiOptions.html#structcupti__activityapioptions)Kind-specific options for API activity kinds (RUNTIME, DRIVER).

[CUpti_ActivityAutoBoostState](https://docs.nvidia.com/structCUpti__ActivityAutoBoostState.html#structcupti__activityautobooststate)Device auto boost state structure.

[CUpti_ActivityBranch2](https://docs.nvidia.com/structCUpti__ActivityBranch2.html#structcupti__activitybranch2)The activity record for source level result branch.

[CUpti_ActivityCdpKernel](https://docs.nvidia.com/structCUpti__ActivityCdpKernel.html#structcupti__activitycdpkernel)The activity record for CDP (CUDA Dynamic Parallelism) kernel.

[CUpti_ActivityComputeEngineCtxSwitch](https://docs.nvidia.com/structCUpti__ActivityComputeEngineCtxSwitch.html#structcupti__activitycomputeenginectxswitch)The activity record for trace of CUDA context switch events.

[CUpti_ActivityConfidentialComputeRotation](https://docs.nvidia.com/structCUpti__ActivityConfidentialComputeRotation.html#structcupti__activityconfidentialcomputerotation)Event related to confidential compute encryption rotation.

[CUpti_ActivityConfig](https://docs.nvidia.com/structCUpti__ActivityConfig.html#structcupti__activityconfig)Activity configuration.

[CUpti_ActivityContext4](https://docs.nvidia.com/structCUpti__ActivityContext4.html#structcupti__activitycontext4)The activity record for a context.

[CUpti_ActivityCudaEvent2](https://docs.nvidia.com/structCUpti__ActivityCudaEvent2.html#structcupti__activitycudaevent2)The activity record for CUDA event.

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6)The activity record for a device.

[CUpti_ActivityDeviceAttribute](https://docs.nvidia.com/structCUpti__ActivityDeviceAttribute.html#structcupti__activitydeviceattribute)The activity record for a device attribute.

[CUpti_ActivityDeviceGraphTrace](https://docs.nvidia.com/structCUpti__ActivityDeviceGraphTrace.html#structcupti__activitydevicegraphtrace)The activity record for trace of device graph execution.

[CUpti_ActivityEnvironment](https://docs.nvidia.com/structCUpti__ActivityEnvironment.html#structcupti__activityenvironment)The activity record for CUPTI environmental data.

[CUpti_ActivityEnvironmentCooling](https://docs.nvidia.com/structCUpti__ActivityEnvironmentCooling.html#structcupti__activityenvironmentcooling)Data returned for CUPTI_ACTIVITY_ENVIRONMENT_COOLING environment kind.

[CUpti_ActivityEnvironmentPower](https://docs.nvidia.com/structCUpti__ActivityEnvironmentPower.html#structcupti__activityenvironmentpower)Data returned for CUPTI_ACTIVITY_ENVIRONMENT_POWER environment kind.

[CUpti_ActivityEnvironmentSpeed](https://docs.nvidia.com/structCUpti__ActivityEnvironmentSpeed.html#structcupti__activityenvironmentspeed)Data returned for CUPTI_ACTIVITY_ENVIRONMENT_SPEED environment kind.

[CUpti_ActivityEnvironmentTemperature](https://docs.nvidia.com/structCUpti__ActivityEnvironmentTemperature.html#structcupti__activityenvironmenttemperature)Data returned for CUPTI_ACTIVITY_ENVIRONMENT_TEMPERATURE environment kind.

[CUpti_ActivityEvent](https://docs.nvidia.com/structCUpti__ActivityEvent.html#structcupti__activityevent)The activity record for a CUPTI event.

[CUpti_ActivityEventInstance](https://docs.nvidia.com/structCUpti__ActivityEventInstance.html#structcupti__activityeventinstance)The activity record for a CUPTI event with instance information.

[CUpti_ActivityExternalCorrelation](https://docs.nvidia.com/structCUpti__ActivityExternalCorrelation.html#structcupti__activityexternalcorrelation)The activity record for correlation with external records.

[CUpti_ActivityFieldLayoutEntry](https://docs.nvidia.com/structCUpti__ActivityFieldLayoutEntry.html#structcupti__activityfieldlayoutentry)[CUpti_ActivityFieldSelection](https://docs.nvidia.com/structCUpti__ActivityFieldSelection.html#structcupti__activityfieldselection)[CUpti_ActivityFunction](https://docs.nvidia.com/structCUpti__ActivityFunction.html#structcupti__activityfunction)The activity record for global/device functions.

[CUpti_ActivityGlobalAccess3](https://docs.nvidia.com/structCUpti__ActivityGlobalAccess3.html#structcupti__activityglobalaccess3)The activity record for source-level global access.

[CUpti_ActivityGraphHostNode](https://docs.nvidia.com/structCUpti__ActivityGraphHostNode.html#structcupti__activitygraphhostnode)[CUpti_ActivityGraphTrace2](https://docs.nvidia.com/structCUpti__ActivityGraphTrace2.html#structcupti__activitygraphtrace2)The activity record for trace of graph execution.

[CUpti_ActivityGreenContext3](https://docs.nvidia.com/structCUpti__ActivityGreenContext3.html#structcupti__activitygreencontext3)The activity record for a green context (version 3).

[CUpti_ActivityHostLaunch](https://docs.nvidia.com/structCUpti__ActivityHostLaunch.html#structcupti__activityhostlaunch)The activity record for host launch functions.

[CUpti_ActivityInstantaneousEvent](https://docs.nvidia.com/structCUpti__ActivityInstantaneousEvent.html#structcupti__activityinstantaneousevent)The activity record for an instantaneous CUPTI event.

[CUpti_ActivityInstantaneousEventInstance](https://docs.nvidia.com/structCUpti__ActivityInstantaneousEventInstance.html#structcupti__activityinstantaneouseventinstance)The activity record for an instantaneous CUPTI event with event domain instance information.

[CUpti_ActivityInstantaneousMetric](https://docs.nvidia.com/structCUpti__ActivityInstantaneousMetric.html#structcupti__activityinstantaneousmetric)The activity record for an instantaneous CUPTI metric.

[CUpti_ActivityInstantaneousMetricInstance](https://docs.nvidia.com/structCUpti__ActivityInstantaneousMetricInstance.html#structcupti__activityinstantaneousmetricinstance)The instantaneous activity record for a CUPTI metric with instance information.

[CUpti_ActivityInstructionCorrelation](https://docs.nvidia.com/structCUpti__ActivityInstructionCorrelation.html#structcupti__activityinstructioncorrelation)The activity record for source-level sass/source line-by-line correlation.

[CUpti_ActivityInstructionExecution](https://docs.nvidia.com/structCUpti__ActivityInstructionExecution.html#structcupti__activityinstructionexecution)The activity record for source-level instruction execution.

[CUpti_ActivityJit2](https://docs.nvidia.com/structCUpti__ActivityJit2.html#structcupti__activityjit2)The activity record for JIT operations.

[CUpti_ActivityKernel13](https://docs.nvidia.com/structCUpti__ActivityKernel13.html#structcupti__activitykernel13)The activity record for kernel (version 13).

[CUpti_ActivityMarker2](https://docs.nvidia.com/structCUpti__ActivityMarker2.html#structcupti__activitymarker2)The activity record providing a marker which is an instantaneous point in time.

[CUpti_ActivityMarkerData2](https://docs.nvidia.com/structCUpti__ActivityMarkerData2.html#structcupti__activitymarkerdata2)The activity record providing detailed information for a marker.

[CUpti_ActivityMemDecompress](https://docs.nvidia.com/structCUpti__ActivityMemDecompress.html#structcupti__activitymemdecompress)The activity record for trace of decompression operations.

[CUpti_ActivityMemcpy7](https://docs.nvidia.com/structCUpti__ActivityMemcpy7.html#structcupti__activitymemcpy7)The activity record for memory copies (version 7).

[CUpti_ActivityMemcpyPtoP4](https://docs.nvidia.com/structCUpti__ActivityMemcpyPtoP4.html#structcupti__activitymemcpyptop4)The activity record for peer-to-peer memory copies.

[CUpti_ActivityMemory](https://docs.nvidia.com/structCUpti__ActivityMemory.html#structcupti__activitymemory)The activity record for memory.

[CUpti_ActivityMemory4](https://docs.nvidia.com/structCUpti__ActivityMemory4.html#structcupti__activitymemory4)The activity record for memory.

[CUpti_ActivityMemoryPool3](https://docs.nvidia.com/structCUpti__ActivityMemoryPool3.html#structcupti__activitymemorypool3)The activity record for memory pool.

[CUpti_ActivityMemset5](https://docs.nvidia.com/structCUpti__ActivityMemset5.html#structcupti__activitymemset5)The activity record for memset (version 5).

[CUpti_ActivityMetric](https://docs.nvidia.com/structCUpti__ActivityMetric.html#structcupti__activitymetric)The activity record for a CUPTI metric.

[CUpti_ActivityMetricInstance](https://docs.nvidia.com/structCUpti__ActivityMetricInstance.html#structcupti__activitymetricinstance)The activity record for a CUPTI metric with instance information.

[CUpti_ActivityModule](https://docs.nvidia.com/structCUpti__ActivityModule.html#structcupti__activitymodule)The activity record for a CUDA module.

[CUpti_ActivityName](https://docs.nvidia.com/structCUpti__ActivityName.html#structcupti__activityname)The activity record providing a name.

[CUpti_ActivityNvLink5](https://docs.nvidia.com/structCUpti__ActivityNvLink5.html#structcupti__activitynvlink5)NVLink information.

[CUpti_ActivityNvLinkNpu](https://docs.nvidia.com/structCUpti__ActivityNvLinkNpu.html#structcupti__activitynvlinknpu)NPU identifier for NVLink connections.

[CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#unioncupti__activityobjectkindid)Identifiers for object kinds as specified by CUpti_ActivityObjectKind.

[CUpti_ActivityOpenAcc](https://docs.nvidia.com/structCUpti__ActivityOpenAcc.html#structcupti__activityopenacc)The base activity record for OpenAcc records.

[CUpti_ActivityOpenAccData](https://docs.nvidia.com/structCUpti__ActivityOpenAccData.html#structcupti__activityopenaccdata)The activity record for OpenACC data.

[CUpti_ActivityOpenAccLaunch](https://docs.nvidia.com/structCUpti__ActivityOpenAccLaunch.html#structcupti__activityopenacclaunch)The activity record for OpenACC launch.

[CUpti_ActivityOpenAccOther](https://docs.nvidia.com/structCUpti__ActivityOpenAccOther.html#structcupti__activityopenaccother)The activity record for OpenACC other.

[CUpti_ActivityOpenMp](https://docs.nvidia.com/structCUpti__ActivityOpenMp.html#structcupti__activityopenmp)The base activity record for OpenMp records.

[CUpti_ActivityOverhead3](https://docs.nvidia.com/structCUpti__ActivityOverhead3.html#structcupti__activityoverhead3)The activity record for CUPTI and driver overheads.

[CUpti_ActivityOverheadCommandBufferFullData](https://docs.nvidia.com/structCUpti__ActivityOverheadCommandBufferFullData.html#structcupti__activityoverheadcommandbufferfulldata)The structure to provide additional data for CUPTI_ACTIVITY_OVERHEAD_COMMAND_BUFFER_FULL.

[CUpti_ActivityPCSampling3](https://docs.nvidia.com/structCUpti__ActivityPCSampling3.html#structcupti__activitypcsampling3)The activity record for PC sampling.

[CUpti_ActivityPCSamplingConfig](https://docs.nvidia.com/structCUpti__ActivityPCSamplingConfig.html#structcupti__activitypcsamplingconfig)PC sampling configuration structure.

[CUpti_ActivityPCSamplingRecordInfo](https://docs.nvidia.com/structCUpti__ActivityPCSamplingRecordInfo.html#structcupti__activitypcsamplingrecordinfo)The activity record for record status for PC sampling.

[CUpti_ActivityPcie](https://docs.nvidia.com/structCUpti__ActivityPcie.html#structcupti__activitypcie)PCI devices information required to construct topology.

[CUpti_ActivityPcieBridgeAttr](https://docs.nvidia.com/structCUpti__ActivityPcieBridgeAttr.html#structcupti__activitypciebridgeattr)Attributes for more information about PCI Bridge (bridgeAttr).

[CUpti_ActivityPcieGpuAttr](https://docs.nvidia.com/structCUpti__ActivityPcieGpuAttr.html#structcupti__activitypciegpuattr)Attributes for more information about GPU (gpuAttr).

[CUpti_ActivityPreemption](https://docs.nvidia.com/structCUpti__ActivityPreemption.html#structcupti__activitypreemption)The activity record for a preemption of a CDP kernel.

[CUpti_ActivityRecordLayout](https://docs.nvidia.com/structCUpti__ActivityRecordLayout.html#structcupti__activityrecordlayout)[CUpti_ActivitySharedAccess](https://docs.nvidia.com/structCUpti__ActivitySharedAccess.html#structcupti__activitysharedaccess)The activity record for source-level shared access.

[CUpti_ActivitySourceLocator](https://docs.nvidia.com/structCUpti__ActivitySourceLocator.html#structcupti__activitysourcelocator)The activity record for source locator.

[CUpti_ActivityStream](https://docs.nvidia.com/structCUpti__ActivityStream.html#structcupti__activitystream)The activity record for CUDA stream.

[CUpti_ActivitySynchronization2](https://docs.nvidia.com/structCUpti__ActivitySynchronization2.html#structcupti__activitysynchronization2)The activity record for synchronization management.

[CUpti_ActivityUnifiedMemoryCounter3](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounter3.html#structcupti__activityunifiedmemorycounter3)The activity record for Unified Memory counters (CUDA 7.0 and beyond)

[CUpti_ActivityUnifiedMemoryCounterConfig](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounterConfig.html#structcupti__activityunifiedmemorycounterconfig)Unified Memory counters configuration structure.

[CUpti_BufferCallbackCompleteInfo](https://docs.nvidia.com/structCUpti__BufferCallbackCompleteInfo.html#structcupti__buffercallbackcompleteinfo)[CUpti_BufferCallbackRequestInfo](https://docs.nvidia.com/structCUpti__BufferCallbackRequestInfo.html#structcupti__buffercallbackrequestinfo)[CUpti_NvtxExtPayloadAttr](https://docs.nvidia.com/structCUpti__NvtxExtPayloadAttr.html#structcupti__nvtxextpayloadattr)

## 6.1.2. Macros[#](https://docs.nvidia.com#macros)

[CUPTI_ACTIVITY_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__activity__api_1ga9813e5edca6e0e8abe29e27953ef06ea)[CUPTI_AUTO_BOOST_INVALID_CLIENT_PID](https://docs.nvidia.com#group__cupti__activity__api_1ga43ce5c40a7db28eba98f969fd830dc76)An invalid/unknown process id.

[CUPTI_CORRELATION_ID_UNKNOWN](https://docs.nvidia.com#group__cupti__activity__api_1ga97e26d46f328081037f013942dbb82c5)An invalid/unknown correlation ID.

[CUPTI_DECOMPRESSED_BYTES_UNKNOWN](https://docs.nvidia.com#group__cupti__activity__api_1ga0701caf1f2f2f61af39e8861853f34e3)An invalid/unknown value for decompressed bytes.

[CUPTI_FUNCTION_INDEX_ID_INVALID](https://docs.nvidia.com#group__cupti__activity__api_1ga3877af5383ad7f9b89aa38d1ae137b0c)An invalid function index ID.

[CUPTI_GRID_ID_UNKNOWN](https://docs.nvidia.com#group__cupti__activity__api_1ga55b5747de740c3daaa3aa63650eb654e)An invalid/unknown grid ID.

[CUPTI_MAX_GPUS](https://docs.nvidia.com#group__cupti__activity__api_1ga7d663d67fae524707955caf1eb0e213b)[CUPTI_NVLINK_INVALID_PORT](https://docs.nvidia.com#group__cupti__activity__api_1gaec9d5c6508090f41530b7a2e0e68b3b4)Invalid/unknown NVLink port number.

[CUPTI_SOURCE_LOCATOR_ID_UNKNOWN](https://docs.nvidia.com#group__cupti__activity__api_1ga79142ac09b1bf1b37cf6db06be375533)The source-locator ID that indicates an unknown source location.

[CUPTI_SYNCHRONIZATION_INVALID_VALUE](https://docs.nvidia.com#group__cupti__activity__api_1gad7733ba3c3dc5ac4330a882bbb6f6985)An invalid/unknown value.

[CUPTI_TIMESTAMP_UNKNOWN](https://docs.nvidia.com#group__cupti__activity__api_1ga03ed33cb1e0d4bf43c446ee3375d0c18)An invalid/unknown timestamp for a start, end, queued, submitted, or completed time.

[CUpti_ActivityConfig_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__activity__api_1gabdd51563fc7712f949821af390a1ad1c)

## 6.1.3. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUpti_ActivityApiFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga7f6cdcfa3ff6dfde9b2035376a7b57be)Enum identifiers for fields in

[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi).[CUpti_ActivityAttribute](https://docs.nvidia.com#group__cupti__activity__api_1ga1c31fe3f8ea0e46c6c20dd454a6caab6)Activity attributes.

[CUpti_ActivityComputeApiKind](https://docs.nvidia.com#group__cupti__activity__api_1gaf46dcec421da358ab4e9edad76774179)The kind of a compute API.

[CUpti_ActivityComputeEngineCtxSwitchFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga69df63d5b9337b6d8ebebac70e61a8ad)Enum identifiers for fields in

[CUpti_ActivityComputeEngineCtxSwitch](https://docs.nvidia.com/structCUpti__ActivityComputeEngineCtxSwitch.html#structcupti__activitycomputeenginectxswitch).[CUpti_ActivityConfidentialComputeRotationFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga459b6fc14f3c21c909509b7d5f4d4542)Enum identifiers for fields in

[CUpti_ActivityConfidentialComputeRotation](https://docs.nvidia.com/structCUpti__ActivityConfidentialComputeRotation.html#structcupti__activityconfidentialcomputerotation).[CUpti_ActivityContextFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga626a82c5475272d0ec3ee2d0107a287f)Enum identifiers for fields to trace context.

[CUpti_ActivityCudaEventFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gaa59800f6dbb791502aefa271d5bd8a1e)Enum identifiers for fields to trace CUDA Event operations.

[CUpti_ActivityDeviceFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gac4a39d3b06f24e840f8ff519b2fbf88a)Enum identifiers for fields in

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6).[CUpti_ActivityDeviceGraphTraceFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gab1b07c4af18f09521fb0f4350b6a4cf6)Enum identifiers for fields in

[CUpti_ActivityDeviceGraphTrace](https://docs.nvidia.com/structCUpti__ActivityDeviceGraphTrace.html#structcupti__activitydevicegraphtrace).[CUpti_ActivityEnvironmentFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga460e6e399dc0b7d18b074e8bbccc04f4)Enum identifiers for fields in

[CUpti_ActivityEnvironment](https://docs.nvidia.com/structCUpti__ActivityEnvironment.html#structcupti__activityenvironment).[CUpti_ActivityEnvironmentKind](https://docs.nvidia.com#group__cupti__activity__api_1gaea1ccba1baca62ba5d6919e5685bfedf)The kind of environment data.

[CUpti_ActivityExternalCorrelationFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga3063e6e9b948c8005584474a94b6eac2)Enum identifiers for fields in

[CUpti_ActivityExternalCorrelation](https://docs.nvidia.com/structCUpti__ActivityExternalCorrelation.html#structcupti__activityexternalcorrelation).[CUpti_ActivityFlag](https://docs.nvidia.com#group__cupti__activity__api_1gaaef8ced52897c4377b0aee6196c37639)Flags associated with activity records.

[CUpti_ActivityGraphHostNodeFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga4bcac415c2f3683b6ee838bcd250b802)Enum identifiers for fields in CUpti_ActivityGraphHostNode.

[CUpti_ActivityGraphTraceFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga8fb0f1a011b4436d233d2efd1d272a03)Enum identifiers for fields to trace graph execution.

[CUpti_ActivityGreenContextFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gad98a9bb79e40a643a64eef096e9c532e)Enum identifiers for fields to trace green context information.

[CUpti_ActivityHostLaunchFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gac4a06569af0b015c3652aa4058525ba3)Enum identifiers for fields in

[CUpti_ActivityHostLaunch](https://docs.nvidia.com/structCUpti__ActivityHostLaunch.html#structcupti__activityhostlaunch).[CUpti_ActivityInstructionClass](https://docs.nvidia.com#group__cupti__activity__api_1gabb6c00413aa3491f7da9e9cbbecf4133)SASS instruction classification.

[CUpti_ActivityJitEntryType](https://docs.nvidia.com#group__cupti__activity__api_1ga0367503f3fc0af7b3c5051a9408efa80)The types of JIT entry.

[CUpti_ActivityJitFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga069e6c461f5bae276a542edf7f579015)Enum identifiers for fields to trace JIT operations.

[CUpti_ActivityJitOperationType](https://docs.nvidia.com#group__cupti__activity__api_1ga2dc4ccb146a37875b3d8564b8100e59a)The types of JIT compilation operations.

[CUpti_ActivityKernelFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga65aba0d6c51c6f37af79a5347dfa4781)Enum identifiers for fields to trace kernel operations.

[CUpti_ActivityKind](https://docs.nvidia.com#group__cupti__activity__api_1gaefed720d5a60c3e8b286cd386c4913e3)The kinds of activity records.

[CUpti_ActivityLaunchType](https://docs.nvidia.com#group__cupti__activity__api_1gad054e12847a4a5a0ece53d2cb6dc6d8c)The type of the CUDA kernel launch.

[CUpti_ActivityMarkerDataFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga4e3cf0d304628c41751c8ab6053dfa42)Enum identifiers for fields to trace detailed information for a marker.

[CUpti_ActivityMarkerFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga26d43dbc0519d06605f7c84806c82e19)Enum identifiers for fields to trace NVTX markers/ranges.

[CUpti_ActivityMemDecompressFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga8bfa18d38590a3599f92b5bf17a358d8)Enum identifiers for fields to trace decompression operations.

[CUpti_ActivityMemcpy2FieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga88652ccd558fef38e9d705a103c8ba5e)Enum identifiers for fields to trace peer-to-peer memory copies.

[CUpti_ActivityMemcpyFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga833d20fb594911f85e73c357f76960d8)Enum identifiers for fields to trace memory copies.

[CUpti_ActivityMemcpyKind](https://docs.nvidia.com#group__cupti__activity__api_1ga10056d66c2ee966fc5cde439eb0a3661)The kind of a memory copy, indicating the source and destination targets of the copy.

[CUpti_ActivityMemoryFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga72382ee5de5e7044e93e479ceb026ef1)Enum identifiers for fields to trace memory allocation and free operation.

[CUpti_ActivityMemoryKind](https://docs.nvidia.com#group__cupti__activity__api_1ga9969b86f0e54989b27080dc6083263bc)The kinds of memory accessed by a memory operation/copy.

[CUpti_ActivityMemoryOperationType](https://docs.nvidia.com#group__cupti__activity__api_1ga6404b89cfbbd60e04204244d230b15c4)Memory operation types.

[CUpti_ActivityMemoryPoolFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gac19a0c40c52e22f600861221aa09c4bc)Enum identifiers for fields to trace CUDA memory pool creation, destruction and trimming.

[CUpti_ActivityMemoryPoolOperationType](https://docs.nvidia.com#group__cupti__activity__api_1ga878fb2c94e0051169fdf0ca7982612a2)Memory pool operation types.

[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8)Memory pool types.

[CUpti_ActivityMemsetFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gaaece6d1740661d5d08ccc34fc51e8c5c)Enum identifiers for fields to trace memset operations.

[CUpti_ActivityNameFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga3bb9af42d353c6b5144e197757fef2dd)Enum identifiers for fields in

[CUpti_ActivityName](https://docs.nvidia.com/structCUpti__ActivityName.html#structcupti__activityname).[CUpti_ActivityNvLinkFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga65f5704f8a8d640f1b8ed17a548308b6)Enum identifiers for fields in

[CUpti_ActivityNvLink5](https://docs.nvidia.com/structCUpti__ActivityNvLink5.html#structcupti__activitynvlink5).[CUpti_ActivityObjectKind](https://docs.nvidia.com#group__cupti__activity__api_1ga9b6136c1123883722ded735eb52cf270)The kinds of activity objects.

[CUpti_ActivityOpenAccDataFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga5ec2b37371860516501774fc00540814)Enum identifiers for fields in

[CUpti_ActivityOpenAccData](https://docs.nvidia.com/structCUpti__ActivityOpenAccData.html#structcupti__activityopenaccdata).[CUpti_ActivityOpenAccLaunchFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga10d51e5f7b79326011bab272b114118d)Enum identifiers for fields in

[CUpti_ActivityOpenAccLaunch](https://docs.nvidia.com/structCUpti__ActivityOpenAccLaunch.html#structcupti__activityopenacclaunch).[CUpti_ActivityOpenAccOtherFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gac9eb42594554ed4dbd6f68f81ca154c5)Enum identifiers for fields in

[CUpti_ActivityOpenAccOther](https://docs.nvidia.com/structCUpti__ActivityOpenAccOther.html#structcupti__activityopenaccother).[CUpti_ActivityOpenMpFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga3ffba50e7f0db12f9baf6062027672f6)Enum identifiers for fields in

[CUpti_ActivityOpenMp](https://docs.nvidia.com/structCUpti__ActivityOpenMp.html#structcupti__activityopenmp).[CUpti_ActivityOverheadFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gac82b13f89949fdb561150bb2ad4b00f0)Enum identifiers for fields to trace CUPTI and driver overhead information.

[CUpti_ActivityOverheadKind](https://docs.nvidia.com#group__cupti__activity__api_1gacc8863d79c939f6bb57324db4503b265)The kinds of activity overhead.

[CUpti_ActivityPCSamplingPeriod](https://docs.nvidia.com#group__cupti__activity__api_1gaa51d59f0407cce71516a53875bf825fe)Sampling period for PC sampling method.

[CUpti_ActivityPCSamplingStallReason](https://docs.nvidia.com#group__cupti__activity__api_1ga57bafb9baafeae0880dae6eaa1a8e12d)The stall reason for PC sampling activity.

[CUpti_ActivityPartitionedGlobalCacheConfig](https://docs.nvidia.com#group__cupti__activity__api_1ga9d3467131ce6c87aa85f3a5a43f83484)Partitioned global caching option.

[CUpti_ActivityPcieFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga301e6106afa8d95c3fb5b4dfca5cbbc2)Enum identifiers for fields in

[CUpti_ActivityPcie](https://docs.nvidia.com/structCUpti__ActivityPcie.html#structcupti__activitypcie).[CUpti_ActivityPreemptionKind](https://docs.nvidia.com#group__cupti__activity__api_1ga7609527c3c6c122a8bb5b1e5d1ae1c4a)The kind of a preemption activity.

[CUpti_ActivityStreamFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga08bbcdf181f5edd9879bab88b5c9eed6)Enum identifiers for fields to trace CUDA Stream operations.

[CUpti_ActivityStreamFlag](https://docs.nvidia.com#group__cupti__activity__api_1ga10b985831ad4db3bd401953e999c877a)stream type.

[CUpti_ActivitySynchronizationFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1ga6071871c1762112a1e6fa0cde67fa51c)Enum identifiers for fields to trace various CUDA synchronization APIs.

[CUpti_ActivitySynchronizationType](https://docs.nvidia.com#group__cupti__activity__api_1ga80e1eb47615e31021f574df8ebbe5d9a)Synchronization type.

[CUpti_ActivityThreadIdType](https://docs.nvidia.com#group__cupti__activity__api_1gac6fcebeb84a89d8f1862d31338efd4c5)Thread-Id types.

[CUpti_ActivityUnifiedMemoryAccessType](https://docs.nvidia.com#group__cupti__activity__api_1ga58bc092ea88426687492fdea7b1c0ff3)Memory access type for unified memory page faults.

[CUpti_ActivityUnifiedMemoryCounterKind](https://docs.nvidia.com#group__cupti__activity__api_1ga601877eb6f7d248a5f538fd74b8fa782)Kind of the Unified Memory counter.

[CUpti_ActivityUnifiedMemoryCounterScope](https://docs.nvidia.com#group__cupti__activity__api_1gacf829db187f1553461cea1a6c9e6748b)Scope of the unified memory counter (deprecated in CUDA 7.0)

[CUpti_ActivityUnifiedMemoryMigrationCause](https://docs.nvidia.com#group__cupti__activity__api_1gac5e53db4204f170a6c31e520e080c1fc)Migration cause of the Unified Memory counter.

[CUpti_ActivityUnifiedMemoryRemoteMapCause](https://docs.nvidia.com#group__cupti__activity__api_1gac38ad61408d643a789562314cd18d6b7)Remote memory map cause of the Unified Memory counter.

[CUpti_ActivityUvmCounterFieldIds](https://docs.nvidia.com#group__cupti__activity__api_1gad76d3ebe68f07cb4509d70e1dd9dd507)Enum identifiers for fields in

[CUpti_ActivityUnifiedMemoryCounter3](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounter3.html#structcupti__activityunifiedmemorycounter3).[CUpti_ChannelType](https://docs.nvidia.com#group__cupti__activity__api_1gabc1dae9c4f50bae5a0068ec0e8dd2cdd)[CUpti_ComputeEngineCtxSwitchOperationType](https://docs.nvidia.com#group__cupti__activity__api_1ga8aa75b4a8ba6922a70c7a5754f278008)The operation type of CUDA context switch event records.

[CUpti_ConfidentialComputeRotationEventType](https://docs.nvidia.com#group__cupti__activity__api_1ga2453dc66ae13b07775b53dbd2481e142)[CUpti_ContextCigMode](https://docs.nvidia.com#group__cupti__activity__api_1gab2e08c379417a33e351316db8ff9ad8f)CIG (CUDA in Graphics) Modes.

[CUpti_DevType](https://docs.nvidia.com#group__cupti__activity__api_1gad67907716d28ba51253f08d3e0bd0dda)The device type for device connected to NVLink.

[CUpti_DeviceGraphLaunchMode](https://docs.nvidia.com#group__cupti__activity__api_1ga55d6dad35d3ac4c54d84614b92310179)The launch mode for device graph execution.

[CUpti_DeviceVirtualizationMode](https://docs.nvidia.com#group__cupti__activity__api_1ga5ec1eab2a306637e8d49bcf8a678cc40)This indicates the virtualization mode in which CUDA device is running.

[CUpti_EnvironmentClocksThrottleReason](https://docs.nvidia.com#group__cupti__activity__api_1ga3dcc6c3e9409a1183932febfdde58173)Reasons for clock throttling.

[CUpti_ExternalCorrelationKind](https://docs.nvidia.com#group__cupti__activity__api_1ga9ac4ae6e6237e99db3f8b4c66df2f9aa)The kind of external APIs supported for correlation.

[CUpti_FuncExecutionModel](https://docs.nvidia.com#group__cupti__activity__api_1gaf6d8c1b48d630571b8c2551d8e1f8c5a)The execution model of a kernel function.

[CUpti_FuncShmemLimitConfig](https://docs.nvidia.com#group__cupti__activity__api_1ga6662b8786c121eed35068b4c1cc931ab)The shared memory limit per block config for a kernel This should be used to set 'cudaOccFuncShmemConfig' field in occupancy calculator API.

[CUpti_LinkFlag](https://docs.nvidia.com#group__cupti__activity__api_1ga819d686d23d2a3dfed9cc1d3c4ecb162)Link flags.

[CUpti_NvtxExtPayloadType](https://docs.nvidia.com#group__cupti__activity__api_1ga7ba18e78e9dc9c0a60296ec01f5c3bc4)[CUpti_OpenAccConstructKind](https://docs.nvidia.com#group__cupti__activity__api_1gaad1f871f3bfe3f626520561cc767881e)The OpenAcc parent construct kind for OpenAcc activity records.

[CUpti_OpenAccEventKind](https://docs.nvidia.com#group__cupti__activity__api_1ga0e638b0b6a210164345ab159bcba6717)The OpenAcc event kind for OpenAcc activity records.

[CUpti_OpenMpEventKind](https://docs.nvidia.com#group__cupti__activity__api_1gaade3401ec307a5dcea9960275fb6c6f6)[CUpti_PcieDeviceType](https://docs.nvidia.com#group__cupti__activity__api_1ga21881d93eb4622a660f0ebd8e2fd2bab)Field to differentiate whether PCIE Activity record is of a GPU or a PCI Bridge.

[CUpti_PcieGen](https://docs.nvidia.com#group__cupti__activity__api_1ga3cc86677bf301c75dc24ed2adef85145)PCIE Generation.


## 6.1.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiActivityConfigurePCSampling](https://docs.nvidia.com#group__cupti__activity__api_1ga115305aadc838df99d88283fc64c4317)(CUcontext ctx, CUpti_ActivityPCSamplingConfig *config) Set PC sampling configuration.

- CUptiResult
[cuptiActivityConfigureUnifiedMemoryCounter](https://docs.nvidia.com#group__cupti__activity__api_1ga8ec9b1229ba07a98aac9db4600d4325c)(CUpti_ActivityUnifiedMemoryCounterConfig *config, uint32_t count) Set Unified Memory Counter configuration.

- CUptiResult
[cuptiActivityDisable](https://docs.nvidia.com#group__cupti__activity__api_1gabc086f5a89450f4e3b75c6f6832f569c)(CUpti_ActivityKind kind) Disable collection of a specific kind of activity record.

- CUptiResult
[cuptiActivityDisableContext](https://docs.nvidia.com#group__cupti__activity__api_1ga90d628b01bcc8044b86060e8a1ff7457)(CUcontext context, CUpti_ActivityKind kind) Disable collection of a specific kind of activity record for a context.

- CUptiResult
[cuptiActivityDisable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga550569082abf3e8c017114881b9f7832)(CUpti_SubscriberHandle subscriber, CUpti_ActivityKind kind, CUpti_ActivityConfig *pActivityConfig) Disable collection of a specific kind of activity record for the subscriber.

- CUptiResult
[cuptiActivityEnable](https://docs.nvidia.com#group__cupti__activity__api_1ga348cf81393b39ab2f89604aaaa8defc2)(CUpti_ActivityKind kind) Enable collection of a specific kind of activity record.

- CUptiResult
[cuptiActivityEnableAllSyncRecords](https://docs.nvidia.com#group__cupti__activity__api_1ga50569b93538b588842914823fc622825)(uint8_t enable) Enables collecting records for all synchronization operations.

- CUptiResult
[cuptiActivityEnableAllocationSource](https://docs.nvidia.com#group__cupti__activity__api_1ga91a099d4e899f9dc513c4e474d9c45b2)(uint8_t enable) Enables tracking the source library for memory allocation requests.

- CUptiResult
[cuptiActivityEnableAndDump](https://docs.nvidia.com#group__cupti__activity__api_1ga12080fe6fdacf80869db472e41b98027)(CUpti_ActivityKind kind) Enable collection of a specific kind of activity record.

- CUptiResult
[cuptiActivityEnableAndDump_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3303f9ceb4eb1d604f00985badb3c7ea)(CUpti_SubscriberHandle subscriber, CUpti_ActivityKind kind, CUpti_ActivityConfig *activityConfig) Enable collection of a specific kind of activity record.

- CUptiResult
[cuptiActivityEnableContext](https://docs.nvidia.com#group__cupti__activity__api_1ga2e2ee46c089fa139481e434f1b0f4cfc)(CUcontext context, CUpti_ActivityKind kind) Enable collection of a specific kind of activity record for a context.

- CUptiResult
[cuptiActivityEnableCudaEventDeviceTimestamps](https://docs.nvidia.com#group__cupti__activity__api_1ga86a82dd4c053b885030dc12863c4b209)(uint8_t enable) Enable/Disable collecting device timestamp for CUPTI_ACTIVITY_KIND_CUDA_EVENT record.

- CUptiResult
[cuptiActivityEnableDeviceGraph](https://docs.nvidia.com#group__cupti__activity__api_1ga21718968b8e42071354e703eda63a000)(uint8_t enable) Controls the collection of records for device launched graphs.

- CUptiResult
[cuptiActivityEnableDriverApi](https://docs.nvidia.com#group__cupti__activity__api_1gaada27f148dd634f0c7466db1cb2a6a78)(CUpti_CallbackId cbid, uint8_t enable) Controls the collection of activity records for specific CUDA Driver APIs.

- CUptiResult
[cuptiActivityEnableDriverApi_v2](https://docs.nvidia.com#group__cupti__activity__api_1gac4ce555fd7cd1c2dacfff655629c198c)(CUpti_SubscriberHandle subscriber, CUpti_CallbackId cbid, uint8_t enable) Controls the collection of activity records for specific CUDA Driver APIs for a given subscriber.

- CUptiResult
[cuptiActivityEnableHWTrace](https://docs.nvidia.com#group__cupti__activity__api_1gaa8f1642a87b1ef876014c766e798f534)(uint8_t enable) Enables CUDA kernel timestamp collection via Hardware Event System (HES).

- CUptiResult
[cuptiActivityEnableLatencyTimestamps](https://docs.nvidia.com#group__cupti__activity__api_1ga4b50c0c1634913f8157cfcfe84f19fa9)(uint8_t enable) Controls the collection of queued and submitted timestamps for kernels.

- CUptiResult
[cuptiActivityEnableLaunchAttributes](https://docs.nvidia.com#group__cupti__activity__api_1ga5fc8cdb0ce9c2cb08a990d26c700f969)(uint8_t enable) Controls the collection of launch attributes for kernels.

- CUptiResult
[cuptiActivityEnableRuntimeApi](https://docs.nvidia.com#group__cupti__activity__api_1gaaad5fd7a8f998e475588623eb65dac9a)(CUpti_CallbackId cbid, uint8_t enable) Controls the collection of activity records for specific CUDA Runtime APIs.

- CUptiResult
[cuptiActivityEnableRuntimeApi_v2](https://docs.nvidia.com#group__cupti__activity__api_1gafb1a4d0b599b9fc3f23d303e608d7ccd)(CUpti_SubscriberHandle subscriber, CUpti_CallbackId cbid, uint8_t enable) Controls the collection of activity records for specific CUDA Runtime APIs for a given subscriber.

- CUptiResult
[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)(CUpti_SubscriberHandle subscriber, CUpti_ActivityKind kind, CUpti_ActivityConfig *pActivityConfig) Enable collection of a specific kind of activity record for the subscriber.

- CUptiResult
[cuptiActivityFlush](https://docs.nvidia.com#group__cupti__activity__api_1ga805065d34981e9284b9943e753b20122)(CUcontext context, uint32_t streamId, uint32_t flag) Wait for all activity records to be delivered via the completion callback.

- CUptiResult
[cuptiActivityFlushAll](https://docs.nvidia.com#group__cupti__activity__api_1gabae7160b2db7e97247a0d23812e373eb)(uint32_t flag) Request to deliver activity records via the buffer completion callback.

- CUptiResult
[cuptiActivityFlushPeriod](https://docs.nvidia.com#group__cupti__activity__api_1gaded430c34c6b7dbf935377c65c7d6491)(uint32_t time) Sets the flush period for the worker thread.

- CUptiResult
[cuptiActivityGetAttribute](https://docs.nvidia.com#group__cupti__activity__api_1ga92859af3b4bc569577d386dea71404b2)(CUpti_ActivityAttribute attr, size_t *valueSize, void *value) Read an activity API attribute.

- CUptiResult
[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)(CUpti_SubscriberHandle subscriber, CUpti_ActivityAttribute attr, size_t *valueSize, void *value) Read an activity API attribute.

- CUptiResult
[cuptiActivityGetEnabledKinds](https://docs.nvidia.com#group__cupti__activity__api_1ga2f1244039cfd99e85f902641e2f345b6)(CUpti_SubscriberHandle subscriber, CUpti_ActivityKind *buffer, uint32_t *bufferSize, uint32_t *enabledKindsCount) Get the enabled activity kinds for a subscriber.

- CUptiResult
[cuptiActivityGetNextRecord](https://docs.nvidia.com#group__cupti__activity__api_1gab397f490a0df4a1633ea7b6e2420294f)(uint8_t *buffer, size_t validBufferSizeBytes, CUpti_Activity **record) Iterate over the activity records in a buffer.

- CUptiResult
[cuptiActivityGetNextRecord_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga1fecc132589644064b6e67a5f0407245)(CUpti_SubscriberHandle subscriber, uint8_t *buffer, size_t validBufferSizeBytes, CUpti_Activity **record) Iterate over the activity records in the supplied buffer.

- CUptiResult
[cuptiActivityGetNumDroppedRecords](https://docs.nvidia.com#group__cupti__activity__api_1ga496d13eb1f4f4fcce37ce3f3434c5e4a)(CUcontext context, uint32_t streamId, size_t *dropped) Get the number of activity records that were dropped of insufficient buffer space.

- CUptiResult
[cuptiActivityGetNumDroppedRecords_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ad9ec6b9519ff9e5ff89bc0d825cdd2)(CUpti_SubscriberHandle subscriber, CUcontext context, uint32_t streamId, size_t *dropped) Get the number of dropped activity records for a specific subscriber.

- CUptiResult
[cuptiActivityGetStructSize](https://docs.nvidia.com#group__cupti__activity__api_1ga01087d6787a94ebc50242d0bc0fe8acb)(CUpti_ActivityKind activityKind, uint32_t version, size_t *activityStructSize) Get the size of the activity struct for a given CUPTI version.

- CUptiResult
[cuptiActivityPopExternalCorrelationId](https://docs.nvidia.com#group__cupti__activity__api_1ga47395bf12ff55f30822d408b940567e3)(CUpti_ExternalCorrelationKind kind, uint64_t *lastId) Pop an external correlation id for the calling thread.

- CUptiResult
[cuptiActivityPopExternalCorrelationId_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga7dc13d2d4d28c976ac6d811d1107dbb3)(CUpti_SubscriberHandle subscriber, CUpti_ExternalCorrelationKind kind, uint64_t *lastId) Pop an external correlation id for a specific subscriber.

- CUptiResult
[cuptiActivityPushExternalCorrelationId](https://docs.nvidia.com#group__cupti__activity__api_1ga2c373f1be967db0227fa4d42a593d1a0)(CUpti_ExternalCorrelationKind kind, uint64_t id) Push an external correlation id for the calling thread.

- CUptiResult
[cuptiActivityPushExternalCorrelationId_v2](https://docs.nvidia.com#group__cupti__activity__api_1gaca9e4785bd022998e5f194c8101db4f2)(CUpti_SubscriberHandle subscriber, CUpti_ExternalCorrelationKind kind, uint64_t id) Push an external correlation id for a specific subscriber.

- CUptiResult
[cuptiActivityRegisterCallbacks](https://docs.nvidia.com#group__cupti__activity__api_1ga237e2401b0ce69dcb265b1f9079f0b65)(CUpti_BuffersCallbackRequestFunc funcBufferRequested, CUpti_BuffersCallbackCompleteFunc funcBufferCompleted) Registers callback functions with CUPTI for activity buffer handling.

- CUptiResult
[cuptiActivityRegisterCallbacks_v2](https://docs.nvidia.com#group__cupti__activity__api_1gacbe1ba1b75f76472038cb2fd34d84e09)(CUpti_SubscriberHandle subscriber, CUpti_BuffersCallbackRequestFunc_v2 funcBufferRequested, CUpti_BuffersCallbackCompleteFunc_v2 funcBufferCompleted) Registers callback functions with CUPTI for activity buffer handling for the subscriber.

- CUptiResult
[cuptiActivityRegisterTimestampCallback](https://docs.nvidia.com#group__cupti__activity__api_1gac168c4a9b5f4e9bd7553ca26118a307d)(CUpti_TimestampCallbackFunc funcTimestamp) Registers callback function with CUPTI for providing timestamp.

- CUptiResult
[cuptiActivitySetAttribute](https://docs.nvidia.com#group__cupti__activity__api_1gaa4ce1e3f22626c5c2a8b450a996fe580)(CUpti_ActivityAttribute attr, size_t *valueSize, void *value) Write an activity API attribute.

- CUptiResult
[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb)(CUpti_SubscriberHandle subscriber, CUpti_ActivityAttribute attr, size_t *valueSize, void *value) Write an activity API attribute.

- CUptiResult
[cuptiComputeCapabilitySupported](https://docs.nvidia.com#group__cupti__activity__api_1ga22c5ce610ffbf5940b7c05be54fc813d)(int major, int minor, int *support) Check support for a compute capability.

- CUptiResult
[cuptiDeviceSupported](https://docs.nvidia.com#group__cupti__activity__api_1ga2493c952b9ceccf953ade5a6816fefdb)(CUdevice dev, int *support) Check support for a compute device.

- CUptiResult
[cuptiDeviceVirtualizationMode](https://docs.nvidia.com#group__cupti__activity__api_1ga395c59b62aeac395e38ced9d40677c76)(CUdevice dev, CUpti_DeviceVirtualizationMode *mode) Query the virtualization mode of the device.

- CUptiResult
[cuptiFinalize](https://docs.nvidia.com#group__cupti__activity__api_1gaad1be905ea718ed54246e52e02667e8f)(void) Detach CUPTI from the running process.

- CUptiResult
[cuptiGetAutoBoostState](https://docs.nvidia.com#group__cupti__activity__api_1ga1ac1cce5ce788b9f2c679d13e982384b)(CUcontext context, CUpti_ActivityAutoBoostState *state) Get auto boost state.

- CUptiResult
[cuptiGetContextId](https://docs.nvidia.com#group__cupti__activity__api_1ga036dfd802a6c28c7e4239c82ed98df21)(CUcontext context, uint32_t *contextId) Get the ID of a context.

- CUptiResult
[cuptiGetCudaEventId](https://docs.nvidia.com#group__cupti__activity__api_1gafd938555b8ecba0fe0f7420cb6b5a6a9)(CUevent event, uint32_t *pEventId) Get the unique ID of a CUDA event.

- CUptiResult
[cuptiGetDeviceId](https://docs.nvidia.com#group__cupti__activity__api_1ga0cc36b42dbf08fffc772e9c932749c77)(CUcontext context, uint32_t *deviceId) Get the ID of a device.

- CUptiResult
[cuptiGetGraphExecId](https://docs.nvidia.com#group__cupti__activity__api_1ga3a3fd5d89e51eeece46635d614624aa3)(CUgraphExec graphExec, uint32_t *pId) Get the unique ID of executable graph.

- CUptiResult
[cuptiGetGraphId](https://docs.nvidia.com#group__cupti__activity__api_1ga4add923efce4731de28c9f0b04e1e3f9)(CUgraph graph, uint32_t *pId) Get the unique ID of graph.

- CUptiResult
[cuptiGetGraphNodeId](https://docs.nvidia.com#group__cupti__activity__api_1ga22370b53102428305a97cb37fbc14678)(CUgraphNode node, uint64_t *nodeId) Get the unique ID of a graph node.

- CUptiResult
[cuptiGetLastError](https://docs.nvidia.com#group__cupti__activity__api_1ga0c83719b0248e09ef94390000d3f1035)(void) Returns the last error from a cupti call or callback.

- CUptiResult
[cuptiGetStreamId](https://docs.nvidia.com#group__cupti__activity__api_1ga04ece23d24e29e8d98daadba09f1839c)(CUcontext context, CUstream stream, uint32_t *streamId) Get the ID of a stream.

- CUptiResult
[cuptiGetStreamIdEx](https://docs.nvidia.com#group__cupti__activity__api_1ga062d04c62fdfeed9adb8157cecbaaa55)(CUcontext context, CUstream stream, uint8_t perThreadStream, uint32_t *streamId) Get the ID of a stream.

- CUptiResult
[cuptiGetThreadIdType](https://docs.nvidia.com#group__cupti__activity__api_1gabc957f426b741e46d6e9a99a43a974b5)(CUpti_ActivityThreadIdType *type) Get the thread-id type.

- CUptiResult
[cuptiGetTimestamp](https://docs.nvidia.com#group__cupti__activity__api_1ga7d8294c686b5293237a6daae8eae3dde)(uint64_t *timestamp) Get the CUPTI timestamp.

- CUptiResult
[cuptiGetTimestamp_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga47495782fa9a5d6b128bfa569f3dec2d)(CUpti_SubscriberHandle subscriber, uint64_t *timestamp) Get the CUPTI timestamp.

- CUptiResult
[cuptiIsTracingSessionRunning](https://docs.nvidia.com#group__cupti__activity__api_1ga3792165063639b175d8ef05d00cfc542)(uint8_t *isRunning) Check whether a CUPTI tracing session is still running.

- CUptiResult
[cuptiSetThreadIdType](https://docs.nvidia.com#group__cupti__activity__api_1ga1821f090b841d60643ee37d977d9c64a)(CUpti_ActivityThreadIdType type) Set the thread-id type.


## 6.1.5. Typedefs[#](https://docs.nvidia.com#typedefs)

[CUpti_BuffersCallbackCompleteFunc](https://docs.nvidia.com#group__cupti__activity__api_1gae569889fa879df2dc9e6449b49445e77)Function type for callback used by CUPTI to return a buffer of activity records.

[CUpti_BuffersCallbackCompleteFunc_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga36aa0d0c92c516c614b4b1259e455b3d)Function type for callback used by CUPTI to return a buffer of activity records.

[CUpti_BuffersCallbackRequestFunc](https://docs.nvidia.com#group__cupti__activity__api_1ga071f445bef24e41610fa79ca7d5a7d55)Function type for callback used by CUPTI to request an empty buffer for storing activity records.

[CUpti_BuffersCallbackRequestFunc_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga40af94885fbe3bb9228cd411393b05ec)Function type for callback used by CUPTI to request an empty buffer for storing activity records.

[CUpti_TimestampCallbackFunc](https://docs.nvidia.com#group__cupti__activity__api_1gaac55368b2963f8ee13389dc42db72395)Function type for callback used by CUPTI to request a timestamp to be used in activity records.


## 6.1.6. Macros[#](https://docs.nvidia.com#id1)

-
CUPTI_ACTIVITY_STRUCT_SIZE(
*type_*,*lastfield_*)[#](https://docs.nvidia.com#c.CUPTI_ACTIVITY_STRUCT_SIZE)

-
CUPTI_AUTO_BOOST_INVALID_CLIENT_PID
[#](https://docs.nvidia.com#c.CUPTI_AUTO_BOOST_INVALID_CLIENT_PID) An invalid/unknown process id.


-
CUPTI_CORRELATION_ID_UNKNOWN
[#](https://docs.nvidia.com#c.CUPTI_CORRELATION_ID_UNKNOWN) An invalid/unknown correlation ID.

A correlation ID of this value indicates that there is no correlation for the activity record.


-
CUPTI_DECOMPRESSED_BYTES_UNKNOWN
[#](https://docs.nvidia.com#c.CUPTI_DECOMPRESSED_BYTES_UNKNOWN) An invalid/unknown value for decompressed bytes.


-
CUPTI_FUNCTION_INDEX_ID_INVALID
[#](https://docs.nvidia.com#c.CUPTI_FUNCTION_INDEX_ID_INVALID) An invalid function index ID.


-
CUPTI_GRID_ID_UNKNOWN
[#](https://docs.nvidia.com#c.CUPTI_GRID_ID_UNKNOWN) An invalid/unknown grid ID.


-
CUPTI_MAX_GPUS
[#](https://docs.nvidia.com#c.CUPTI_MAX_GPUS)

-
CUPTI_NVLINK_INVALID_PORT
[#](https://docs.nvidia.com#c.CUPTI_NVLINK_INVALID_PORT) Invalid/unknown NVLink port number.


-
CUPTI_SOURCE_LOCATOR_ID_UNKNOWN
[#](https://docs.nvidia.com#c.CUPTI_SOURCE_LOCATOR_ID_UNKNOWN) The source-locator ID that indicates an unknown source location.

There is not an actual

[CUpti_ActivitySourceLocator](https://docs.nvidia.com/structCUpti__ActivitySourceLocator.html#structcupti__activitysourcelocator)object corresponding to this value.

-
CUPTI_SYNCHRONIZATION_INVALID_VALUE
[#](https://docs.nvidia.com#c.CUPTI_SYNCHRONIZATION_INVALID_VALUE) An invalid/unknown value.


-
CUPTI_TIMESTAMP_UNKNOWN
[#](https://docs.nvidia.com#c.CUPTI_TIMESTAMP_UNKNOWN) An invalid/unknown timestamp for a start, end, queued, submitted, or completed time.


-
CUpti_ActivityConfig_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_ActivityConfig_STRUCT_SIZE)

## 6.1.7. Enumerations[#](https://docs.nvidia.com#id2)

-
enum CUpti_ActivityApiFieldIds
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityApiFieldIds) Enum identifiers for fields in

[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi).Each enum value corresponds to a field in

[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi)and describes the data type and purpose of that field.*Values:*-
enumerator API_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds14API_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always either CUPTI_ACTIVITY_KIND_DRIVER or CUPTI_ACTIVITY_KIND_RUNTIME.


-
enumerator API_FIELD_CBID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds14API_FIELD_CBIDE) CUpti_CallbackId cbid; Callback ID of the CUDA driver/runtime API function.


-
enumerator API_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds15API_FIELD_STARTE) uint64_t start; Start timestamp of the CUDA driver/runtime API call (in nanoseconds).


-
enumerator API_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds13API_FIELD_ENDE) uint64_t end; End timestamp of the CUDA driver/runtime API call (in nanoseconds).


-
enumerator API_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds20API_FIELD_PROCESS_IDE) uint32_t processId; ID of the process executing the CUDA driver/runtime API call.


-
enumerator API_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds19API_FIELD_THREAD_IDE) uint64_t threadId; ID of the thread executing the CUDA driver/runtime API call.


-
enumerator API_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds24API_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this CUDA driver/runtime API invocation.

This ID matches the correlation ID of the associated kernel, memcpy, or memset activity record that the API call initiated.


-
enumerator API_FIELD_RETURN_VALUE
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds22API_FIELD_RETURN_VALUEE) uint32_t returnValue; Return value of the CUDA driver/runtime API call (CUresult or cudaError_t).


-
enumerator API_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityApiFieldIds13API_FIELD_MAXE) Total number of defined fields.


-
enumerator API_FIELD_KIND

-
enum CUpti_ActivityAttribute
[#](https://docs.nvidia.com#_CPPv423CUpti_ActivityAttribute) Activity attributes.

These attributes are used to control the behavior of the activity API.

*Values:*-
enumerator CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute38CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZEE) The device memory size (in bytes) reserved for storing profiling data for concurrent kernels (activity kind

[CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL](https://docs.nvidia.com#group__cupti__activity__api_1ggaefed720d5a60c3e8b286cd386c4913e3a55d11bb9d376e95d141ddd13468f0b7a)), memcopies and memsets for each buffer on a context.The value is a size_t.

There is a limit on how many device buffers can be allocated per context. User can query and set this limit using the attribute

[CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_POOL_LIMIT](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a3e84be3bdc3dc8a3477a56a1247287cc). CUPTI doesn’t pre-allocate all the buffers, it pre-allocates only those many buffers as set by the attribute[CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_PRE_ALLOCATE_VALUE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a21f4deb586a4d759218e1d7f9530395f). When all of the data in a buffer is consumed, it is added in the reuse pool, and CUPTI picks a buffer from this pool when a new buffer is needed. Thus memory footprint does not scale with the kernel count. Applications with the high density of kernels, memcopies and memsets might result in having CUPTI to allocate more device buffers. CUPTI allocates another buffer only when it runs out of the buffers in the reuse pool.Since buffer allocation happens in the main application thread, this might result in stalls in the critical path. CUPTI pre-allocates 3 buffers of the same size to mitigate this issue. User can query and set the pre-allocation limit using the attribute

[CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_PRE_ALLOCATE_VALUE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a21f4deb586a4d759218e1d7f9530395f).Having larger buffer size leaves less device memory for the application. Having smaller buffer size increases the risk of dropping timestamps for records if too many kernels or memcopies or memsets are launched at one time.

This value only applies to new buffer allocations. Set this value before initializing CUDA or before creating a context to ensure it is considered for the following allocations.

The default value is 3200000 (~3MB) which can accommodate profiling data up to 100,000 kernels, memcopies and memsets combined.

Note: Starting with the CUDA 12.0 Update 1 release, CUPTI allocates the profiling buffer in the device memory by default, which may improve the performance of the tracing run. To change the preferred location to page-locked host memory, refer to the attribute

[CUPTI_ACTIVITY_ATTR_MEM_ALLOCATION_TYPE_HOST_PINNED](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a0baaaf2f89ee9a711b635ea3bc4b2e1e). The size of the memory and maximum number of pools are still controlled by the attributes[CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6ad4ba37cb123069fa778513f87cbb4b37)and[CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_POOL_LIMIT](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a3e84be3bdc3dc8a3477a56a1247287cc).Note: The actual amount of device memory per buffer reserved by CUPTI might be larger.


-
enumerator CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE_CDP
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute42CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE_CDPE) The device memory size (in bytes) reserved for storing profiling data for CDP operations for each buffer on a context.

The value is a size_t.

Having larger buffer size means less flush operations but consumes more device memory. This value only applies to new allocations.

Set this value before initializing CUDA or before creating a context to ensure it is considered for the following allocations.

The default value is 8388608 (8MB).

Note: The actual amount of device memory per context reserved by CUPTI might be larger.


-
enumerator CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_POOL_LIMIT
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute44CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_POOL_LIMITE) The maximum number of device memory buffers per context.

The value is a size_t.

For an application with high rate of kernel launches, memcopies and memsets having a bigger pool limit helps in timestamp collection for all these activities at the expense of a larger memory footprint. Refer to the description of the attribute

[CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6ad4ba37cb123069fa778513f87cbb4b37)for more details.Setting this value will not modify the number of memory buffers currently stored.

Set this value before initializing CUDA to ensure the limit is not exceeded.

The default value is 250.


-
enumerator CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_SIZE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute49CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_SIZEE) This attribute is not supported starting with CUDA 12.3 CUPTI no longer uses profiling semaphore pool to store profiling data.

There is a limit on how many semaphore pools can be allocated per context. User can query and set this limit using the attribute

[CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_LIMIT](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6ad58f5aa6e9afbbcd2f7f7d6bd0896b8b). CUPTI doesn’t pre-allocate all the semaphore pools, it pre-allocates only those many semaphore pools as set by the attribute[CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_PRE_ALLOCATE_VALUE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a52ecb99e83c0fa9da4bea4250089f3dd). When all of the data in a semaphore pool is consumed, it is added in the reuse pool, and CUPTI picks a semaphore pool from the reuse pool when a new semaphore pool is needed. Thus memory footprint does not scale with the kernel count. Applications with the high density of kernels might result in having CUPTI to allocate more semaphore pools. CUPTI allocates another semaphore pool only when it runs out of the semaphore pools in the reuse pool.Since semaphore pool allocation happens in the main application thread, this might result in stalls in the critical path. CUPTI pre-allocates 3 semaphore pools of the same size to mitigate this issue. User can query and set the pre-allocation limit using the attribute

[CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_PRE_ALLOCATE_VALUE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a52ecb99e83c0fa9da4bea4250089f3dd).Having larger semaphore pool size leaves less device memory for the application. Having smaller semaphore pool size increases the risk of dropping timestamps for kernel records if too many kernels are issued/launched at one time.

This value only applies to new semaphore pool allocations. Set this value before initializing CUDA or before creating a context to ensure it is considered for the following allocations.

The default value is 25000 which can accommodate profiling data for upto 25,000 kernels.


-
enumerator CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_LIMIT
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute50CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_LIMITE) This attribute is not supported starting with CUDA 12.3 CUPTI no longer uses profiling semaphore pool to store profiling data.

The maximum number of profiling semaphore pools per context. The value is a size_t.

Refer to the description of the attribute

[CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_SIZE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a8ee6c22d0d55bb65700974bf9b1d75c2)for more details.Set this value before initializing CUDA to ensure the limit is not exceeded.

The default value is 250.


-
enumerator CUPTI_ACTIVITY_ATTR_ZEROED_OUT_ACTIVITY_BUFFER
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute46CUPTI_ACTIVITY_ATTR_ZEROED_OUT_ACTIVITY_BUFFERE) The flag to indicate whether user should provide activity buffer of zero value.

The value is a uint8_t.

If the value of this attribute is non-zero, user should provide a zero value buffer in the

[CUpti_BuffersCallbackRequestFunc](https://docs.nvidia.com#group__cupti__activity__api_1ga071f445bef24e41610fa79ca7d5a7d55). If the user does not provide a zero value buffer after setting this to non-zero, the activity buffer may contain some uninitialized values when CUPTI returns it in[CUpti_BuffersCallbackCompleteFunc](https://docs.nvidia.com#group__cupti__activity__api_1gae569889fa879df2dc9e6449b49445e77)If the value of this attribute is zero, CUPTI will initialize the user buffer received in the

[CUpti_BuffersCallbackRequestFunc](https://docs.nvidia.com#group__cupti__activity__api_1ga071f445bef24e41610fa79ca7d5a7d55)to zero before filling it. If the user sets this to zero, a few stalls may appear in critical path because CUPTI will zero out the buffer in the main thread. Set this value before returning from[CUpti_BuffersCallbackRequestFunc](https://docs.nvidia.com#group__cupti__activity__api_1ga071f445bef24e41610fa79ca7d5a7d55)to ensure it is considered for all the subsequent user buffers.The default value is 0.


-
enumerator CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_PRE_ALLOCATE_VALUE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute52CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_PRE_ALLOCATE_VALUEE) Number of device buffers to pre-allocate for a context during the initialization phase.

The value is a size_t.

Refer to the description of the attribute

[CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6ad4ba37cb123069fa778513f87cbb4b37)for details.This value must be less than the maximum number of device buffers set using the attribute

[CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_POOL_LIMIT](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a3e84be3bdc3dc8a3477a56a1247287cc)Set this value before initializing CUDA or before creating a context to ensure it is considered by the CUPTI.

The default value is set to 3 to ping pong between these buffers (if possible).


-
enumerator CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_PRE_ALLOCATE_VALUE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute58CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_PRE_ALLOCATE_VALUEE) This attribute is not supported starting with CUDA 12.3 CUPTI no longer uses profiling semaphore pool to store profiling data.

Number of profiling semaphore pools to pre-allocate for a context during the initialization phase. The value is a size_t.

Refer to the description of the attribute

[CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_SIZE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a8ee6c22d0d55bb65700974bf9b1d75c2)for details.This value must be less than the maximum number of profiling semaphore pools set using the attribute

[CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_LIMIT](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6ad58f5aa6e9afbbcd2f7f7d6bd0896b8b)Set this value before initializing CUDA or before creating a context to ensure it is considered by the CUPTI.

The default value is set to 3 to ping pong between these pools (if possible).


-
enumerator CUPTI_ACTIVITY_ATTR_MEM_ALLOCATION_TYPE_HOST_PINNED
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute51CUPTI_ACTIVITY_ATTR_MEM_ALLOCATION_TYPE_HOST_PINNEDE) Allocate page-locked (pinned) host memory for storing profiling data for concurrent kernels, memcopies and memsets for each buffer on a context.

The value is a uint8_t.

From CUDA 11.2 through CUDA 12.0 GA releases, CUPTI allocated the profiling buffer in pinned host memory by default. Allocating excessive amounts of pinned memory may degrade system performance, as it reduces the amount of memory available to the system for paging. For this reason user might want to change the location from pinned host memory to device memory by setting value of this attribute to 0.

Using page-locked (pinned) host memory buffers is not supported on confidential computing devices. If this attribute is set to 1, CUPTI will return error CUPTI_ERROR_NOT_SUPPORTED.

The default value is 0.


-
enumerator CUPTI_ACTIVITY_ATTR_PER_THREAD_ACTIVITY_BUFFER
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute46CUPTI_ACTIVITY_ATTR_PER_THREAD_ACTIVITY_BUFFERE) Request activity buffers per-thread to store CUPTI activity records in the activity buffer on per-thread basis.

The value is a uint8_t.

The attribute should be set before registering the buffer callbacks using cuptiActivityRegisterCallbacks API and before any of the CUPTI activity kinds are enabled. This makes sure that all the records are stored in activity buffers allocated per-thread. Changing this attribute in the middle of the profiling session will result in undefined behavior.

The default value is 1.


-
enumerator CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE_DEVICE_GRAPHS
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute52CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE_DEVICE_GRAPHSE) The device memory size (in bytes) reserved for storing profiling data for device graph operations for each buffer on a context.

The value is a size_t.

Having larger buffer size means less flush operations but consumes more device memory. This value only applies to new allocations.

Set this value before initializing CUDA or before creating a context to ensure it is considered for the following allocations.

The default value is 16777216 (16MB).

Note: The actual amount of device memory per context reserved by CUPTI might be larger.


-
enumerator CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDS
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute40CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDSE) Enable user-defined activity records.

The value is a uint8_t.

When this attribute is enabled, CUPTI activity records will contain only the fields that are enabled for collection by the user. This can help to reduce the size of each activity record and decrease the overall memory consumption for activity collection.

This attribute must be set before enabling any CUPTI activity kinds. The activity kinds should be enabled/disabled using CUPTI API

[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)and[cuptiActivityDisable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga550569082abf3e8c017114881b9f7832)respectively.Minimum CUPTI Version: CUPTI_API_VERSION 130200 (CUDA 13.2) — beta. Productized (no longer beta) in CUPTI_API_VERSION 130300 (CUDA 13.3). The CUPTI version can be queried using

[cuptiGetVersion()](https://docs.nvidia.com/group__CUPTI__VERSION__API.html#group__cupti__version__api_1ga0e63a0d235c5e7e5231cc78ec63fa981)API.Refer these links for online documentation: CUPTI Activity User-Defined Records:

[https://docs.nvidia.com/cupti/main/main.html#cupti-user-defined-activity-records](https://docs.nvidia.com/cupti/main/main.html#cupti-user-defined-activity-records)Tutorial:[https://docs.nvidia.com/cupti/tutorial/tutorial.html#tutorial-activity-user-defined-records](https://docs.nvidia.com/cupti/tutorial/tutorial.html#tutorial-activity-user-defined-records)Refer sample cupti_user_defined_records for usage.The default value is 0 i.e. CUPTI will provide records with all fields.


-
enumerator CUPTI_ACTIVITY_ATTR_MULTIPLE_SUBSCRIBER_STATE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute45CUPTI_ACTIVITY_ATTR_MULTIPLE_SUBSCRIBER_STATEE) Allow multiple subscribers.

The value is a uint8_t.

If 0, only a single subscriber is allowed. If 1, multiple subscribers are allowed. If 2, this option has not been set by a prior subscriber, if there were any. In this case, the subscriber is free to set it during cuptiSubscribe_v2 call. Note that this attribute cannot be set by cuptiActivitySetAttribute or cuptiActivitySetAttribute_v2. It can however be queried using cuptiActivityGetAttribute_v2.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_HES
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute30CUPTI_ACTIVITY_ATTR_ENABLE_HESE) Get the HES (Hardware Events System) enabled flag.

The value is a uint8_t.

If 0, HES (Hardware Events System) is disabled. If 1, HES (Hardware Events System) is enabled. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2. This attribute is not subscriber specific, and the subscriber parameter is ignored. All subscribers will share the same HES enabled flag. However, this attribute must be set before enabling any activity kind by any subscriber. However, it can be queried using cuptiActivityGetAttribute_v2.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_ALLOCATION_SOURCE_TRACKING
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute53CUPTI_ACTIVITY_ATTR_ENABLE_ALLOCATION_SOURCE_TRACKINGE) Get the allocation source library tracking enabled flag (for the specified subscriber).

The value is a uint8_t.

If 0, allocation source library tracking is disabled. If 1, allocation source library tracking is enabled. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber. Note that the cuptiActivityEnableAllocationSource API cannot be used when multiple subscribers are allowed.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_KERNEL_LATENCY_TIMESTAMPS
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute52CUPTI_ACTIVITY_ATTR_ENABLE_KERNEL_LATENCY_TIMESTAMPSE) Get the latency timestamp tracking enabled flag (for the specified subscriber).

The value is a uint8_t.

This can be used to toggle collecting latency timestamps for kernel records.

If 0, latency timestamp tracking is disabled. If 1, latency timestamp tracking is enabled. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_ALL_SYNC_RECORDS
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute43CUPTI_ACTIVITY_ATTR_ENABLE_ALL_SYNC_RECORDSE) Get the all sync records enabled flag (for the specified subscriber).

The value is a uint8_t.

This can be used to toggle collecting sync records for all synchronization operations (whether to include records for synchronization operations which return non-zero CUDA status). By default, this flag is set to 0. If this flag is set to 1, sync records are collected for all synchronization operations (even if they return non-zero CUDA status). Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_CUDA_EVENT_DEVICE_TIMESTAMPS
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute55CUPTI_ACTIVITY_ATTR_ENABLE_CUDA_EVENT_DEVICE_TIMESTAMPSE) Get the event device timestamps enabled flag (for the specified subscriber).

The value is a uint8_t.

This can be used to toggle collecting event device timestamps for CUDA event records. By default, this flag is set to 0. If this flag is set to 1, event device timestamps are collected for CUDA event records. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_KERNEL_LAUNCH_ATTRIBUTES
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute51CUPTI_ACTIVITY_ATTR_ENABLE_KERNEL_LAUNCH_ATTRIBUTESE) Get the launch attributes for kernel enabled flag (for the specified subscriber).

The value is a uint8_t.

This can be used to toggle collecting launch attributes for kernel records. By default, this flag is set to 0. If this flag is set to 1, launch attributes are collected for kernel records. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_DEVICE_GRAPH_TRACE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute45CUPTI_ACTIVITY_ATTR_ENABLE_DEVICE_GRAPH_TRACEE) Get the device graph trace enabled flag (for the specified subscriber).

The value is a uint8_t.

This can be used to toggle collecting device graph trace for graph records. By default, this flag is set to 0. If this flag is set to 1, device graph trace is collected for graph records. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_MULTI_SUBSCRIBER_GRAPH_TRACE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute55CUPTI_ACTIVITY_ATTR_ENABLE_MULTI_SUBSCRIBER_GRAPH_TRACEE) Get the multi-subscriber graph level trace enabled flag.

The value is a uint8_t.

This attribute is only relevant for multi-subscriber mode. CUPTI currently does not support different subscribers to ask for node level trace and graph level trace concurrently. If this flag is disabled, body nodes of a graph are reported under normal concurrent kernel/ memcpy/ memset records. If this flag is enabled, body nodes of a graph are not reported under normal concurrent kernel/ memcpy/ memset records, but the graph is entirely reported as part of a single graph trace record(if CUPTI_ACTIVITY_KIND_GRAPH_TRACE is enabled for the subscriber). Note that this behavior is consistent across all subscribers, regardless of which activities each subscriber is enabling.

If 0, multi-subscriber graph level trace is disabled. If 1, multi-subscriber graph level trace is enabled. The default value is 0. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber. However, this attribute must be set before enabling any activity kind by any subscriber. This attribute is not subscriber specific, and the subscriber parameter is ignored. All subscribers will share the same multi-subscriber graph level trace enabled flag.


-
enumerator CUPTI_ACTIVITY_ATTR_THREAD_ID_TYPE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute34CUPTI_ACTIVITY_ATTR_THREAD_ID_TYPEE) Get or set the thread ID type (for the specified subscriber).

The value is a CUpti_ActivityThreadIdType.

This attribute specifies the method used by CUPTI to obtain thread IDs. The default value is CUPTI_ACTIVITY_THREAD_ID_TYPE_DEFAULT. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber.


-
enumerator CUPTI_ACTIVITY_ATTR_TIMESTAMP_CALLBACK
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute38CUPTI_ACTIVITY_ATTR_TIMESTAMP_CALLBACKE) Get or set the timestamp callback function (for the specified subscriber).

The value is a CUpti_TimestampCallbackFunc.

This attribute allows registering a custom timestamp callback function that CUPTI will use instead of its default CPU timer. The value can be NULL to unregister the callback. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2 for the specified subscriber.


-
enumerator CUPTI_ACTIVITY_ATTR_ENABLE_CIG_MODE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute35CUPTI_ACTIVITY_ATTR_ENABLE_CIG_MODEE) Get or set the CIG (CUDA in Graphics) mode.

The value is a uint8_t.

This attribute allows enabling or disabling the CIG mode. Note that this attribute can be set by cuptiActivitySetAttribute_v2 and queried using cuptiActivityGetAttribute_v2.


-
enumerator CUPTI_ACTIVITY_ATTR_COUNT
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute25CUPTI_ACTIVITY_ATTR_COUNTE)

-
enumerator CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityAttribute43CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE

-
enum CUpti_ActivityComputeApiKind
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityComputeApiKind) The kind of a compute API.

*Values:*-
enumerator CUPTI_ACTIVITY_COMPUTE_API_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityComputeApiKind34CUPTI_ACTIVITY_COMPUTE_API_UNKNOWNE) The compute API is not known.


-
enumerator CUPTI_ACTIVITY_COMPUTE_API_CUDA
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityComputeApiKind31CUPTI_ACTIVITY_COMPUTE_API_CUDAE) The compute APIs are for CUDA.


-
enumerator CUPTI_ACTIVITY_COMPUTE_API_CUDA_MPS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityComputeApiKind35CUPTI_ACTIVITY_COMPUTE_API_CUDA_MPSE) The compute APIs are for CUDA running in MPS (Multi-Process Service) environment.


-
enumerator CUPTI_ACTIVITY_COMPUTE_API_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityComputeApiKind36CUPTI_ACTIVITY_COMPUTE_API_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_COMPUTE_API_UNKNOWN

-
enum CUpti_ActivityComputeEngineCtxSwitchFieldIds
[#](https://docs.nvidia.com#_CPPv444CUpti_ActivityComputeEngineCtxSwitchFieldIds) Enum identifiers for fields in

[CUpti_ActivityComputeEngineCtxSwitch](https://docs.nvidia.com/structCUpti__ActivityComputeEngineCtxSwitch.html#structcupti__activitycomputeenginectxswitch).Each enum value corresponds to a field in

[CUpti_ActivityComputeEngineCtxSwitch](https://docs.nvidia.com/structCUpti__ActivityComputeEngineCtxSwitch.html#structcupti__activitycomputeenginectxswitch)and describes the data type and purpose of that field.*Values:*-
enumerator COMPUTE_ENGINE_CTX_SWITCH_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N44CUpti_ActivityComputeEngineCtxSwitchFieldIds36COMPUTE_ENGINE_CTX_SWITCH_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_COMPUTE_ENGINE_CTX_SWITCH.


-
enumerator COMPUTE_ENGINE_CTX_SWITCH_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N44CUpti_ActivityComputeEngineCtxSwitchFieldIds42COMPUTE_ENGINE_CTX_SWITCH_FIELD_CONTEXT_IDE) uint32_t contextId; ID of the CUDA context.


-
enumerator COMPUTE_ENGINE_CTX_SWITCH_FIELD_TIMESTAMP
[#](https://docs.nvidia.com#_CPPv4N44CUpti_ActivityComputeEngineCtxSwitchFieldIds41COMPUTE_ENGINE_CTX_SWITCH_FIELD_TIMESTAMPE) uint64_t timestamp; Timestamp at which the context switch operation occurs.


-
enumerator COMPUTE_ENGINE_CTX_SWITCH_FIELD_OPERATION_TYPE
[#](https://docs.nvidia.com#_CPPv4N44CUpti_ActivityComputeEngineCtxSwitchFieldIds46COMPUTE_ENGINE_CTX_SWITCH_FIELD_OPERATION_TYPEE) CUpti_ComputeEngineCtxSwitchOperationType operationType; Type of the Compute Engine Context switch operation.


-
enumerator COMPUTE_ENGINE_CTX_SWITCH_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N44CUpti_ActivityComputeEngineCtxSwitchFieldIds35COMPUTE_ENGINE_CTX_SWITCH_FIELD_MAXE) Total number of defined fields.


-
enumerator COMPUTE_ENGINE_CTX_SWITCH_FIELD_KIND

-
enum CUpti_ActivityConfidentialComputeRotationFieldIds
[#](https://docs.nvidia.com#_CPPv449CUpti_ActivityConfidentialComputeRotationFieldIds) Enum identifiers for fields in

[CUpti_ActivityConfidentialComputeRotation](https://docs.nvidia.com/structCUpti__ActivityConfidentialComputeRotation.html#structcupti__activityconfidentialcomputerotation).Each enum value corresponds to a field in

[CUpti_ActivityConfidentialComputeRotation](https://docs.nvidia.com/structCUpti__ActivityConfidentialComputeRotation.html#structcupti__activityconfidentialcomputerotation)and describes the data type and purpose of that field.*Values:*-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N49CUpti_ActivityConfidentialComputeRotationFieldIds40CONFIDENTIAL_COMPUTE_ROTATION_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_CONFIDENTIAL_COMPUTE_ROTATION.


-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_EVENT_TYPE
[#](https://docs.nvidia.com#_CPPv4N49CUpti_ActivityConfidentialComputeRotationFieldIds46CONFIDENTIAL_COMPUTE_ROTATION_FIELD_EVENT_TYPEE) CUpti_ConfidentialComputeRotationEventType eventType; Type of event.


-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N49CUpti_ActivityConfidentialComputeRotationFieldIds45CONFIDENTIAL_COMPUTE_ROTATION_FIELD_DEVICE_IDE) uint32_t deviceId; Device ID.


-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N49CUpti_ActivityConfidentialComputeRotationFieldIds46CONFIDENTIAL_COMPUTE_ROTATION_FIELD_CONTEXT_IDE) uint32_t contextId; Context ID.


-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_CHANNEL_ID
[#](https://docs.nvidia.com#_CPPv4N49CUpti_ActivityConfidentialComputeRotationFieldIds46CONFIDENTIAL_COMPUTE_ROTATION_FIELD_CHANNEL_IDE) uint32_t channelId; Channel ID.


-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_CHANNEL_TYPE
[#](https://docs.nvidia.com#_CPPv4N49CUpti_ActivityConfidentialComputeRotationFieldIds48CONFIDENTIAL_COMPUTE_ROTATION_FIELD_CHANNEL_TYPEE) CUpti_ChannelType channelType; Channel Type.


-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_TIMESTAMP
[#](https://docs.nvidia.com#_CPPv4N49CUpti_ActivityConfidentialComputeRotationFieldIds45CONFIDENTIAL_COMPUTE_ROTATION_FIELD_TIMESTAMPE) uint64_t timestamp; Timestamp in ns.


-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N49CUpti_ActivityConfidentialComputeRotationFieldIds39CONFIDENTIAL_COMPUTE_ROTATION_FIELD_MAXE) Total number of defined fields.


-
enumerator CONFIDENTIAL_COMPUTE_ROTATION_FIELD_KIND

-
enum CUpti_ActivityContextFieldIds
[#](https://docs.nvidia.com#_CPPv429CUpti_ActivityContextFieldIds) Enum identifiers for fields to trace context.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_CONTEXT.

*Values:*-
enumerator CONTEXT_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds18CONTEXT_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_CONTEXT.


-
enumerator CONTEXT_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds24CONTEXT_FIELD_CONTEXT_IDE) uint32_t contextId; The ID of the context.


-
enumerator CONTEXT_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds23CONTEXT_FIELD_DEVICE_IDE) uint32_t deviceId; The ID of the device associated with the context.


-
enumerator CONTEXT_FIELD_COMPUTE_API_KIND
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds30CONTEXT_FIELD_COMPUTE_API_KINDE) uint16_t computeApiKind; The compute API kind associated with the context.


-
enumerator CONTEXT_FIELD_NULL_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds28CONTEXT_FIELD_NULL_STREAM_IDE) uint32_t nullStreamId; The ID for the NULL stream in this context.


-
enumerator CONTEXT_FIELD_PARENT_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds31CONTEXT_FIELD_PARENT_CONTEXT_IDE) uint32_t parentContextId; The ID of the parent context.

It would be 0 if context does not have parent.


-
enumerator CONTEXT_FIELD_IS_GREEN_CONTEXT
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds30CONTEXT_FIELD_IS_GREEN_CONTEXTE) uint8_t isGreenContext; Indicates whether the context is a green context.


-
enumerator CONTEXT_FIELD_NUM_MULTIPROCESSORS
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds33CONTEXT_FIELD_NUM_MULTIPROCESSORSE) uint16_t numMultiprocessors; Number of multiprocessors assigned to the green context.

Invalid if the field ‘isGreenContext’ is 0.


-
enumerator CONTEXT_FIELD_CIG_MODE
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds22CONTEXT_FIELD_CIG_MODEE) CUpti_ContextCigMode cigMode; The CIG mode of the context.


-
enumerator CONTEXT_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds24CONTEXT_FIELD_PROCESS_IDE) uint32_t processId; The ID of the process associated with the context.


-
enumerator CONTEXT_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityContextFieldIds17CONTEXT_FIELD_MAXE) Total number of defined fields.


-
enumerator CONTEXT_FIELD_KIND

-
enum CUpti_ActivityCudaEventFieldIds
[#](https://docs.nvidia.com#_CPPv431CUpti_ActivityCudaEventFieldIds) Enum identifiers for fields to trace CUDA Event operations.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_CUDA_EVENT.

*Values:*-
enumerator CUDA_EVENT_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds21CUDA_EVENT_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_CONTEXT.


-
enumerator CUDA_EVENT_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds31CUDA_EVENT_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this CUDA Event operation.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator CUDA_EVENT_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds27CUDA_EVENT_FIELD_CONTEXT_IDE) uint32_t contextId; The ID of the context where the event was recorded.


-
enumerator CUDA_EVENT_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds26CUDA_EVENT_FIELD_STREAM_IDE) uint32_t streamId; The compute stream where the event was recorded.


-
enumerator CUDA_EVENT_FIELD_EVENT_ID
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds25CUDA_EVENT_FIELD_EVENT_IDE) uint64_t eventId; A unique event ID to identify the event record.


-
enumerator CUDA_EVENT_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds26CUDA_EVENT_FIELD_DEVICE_IDE) uint32_t deviceId; The ID of the device where the event was recorded.


-
enumerator CUDA_EVENT_FIELD_DEVICE_TIMESTAMP
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds33CUDA_EVENT_FIELD_DEVICE_TIMESTAMPE) uint64_t deviceTimestamp; The device-side timestamp on CUDA event record (in nanoseconds).

Collection of this field is disabled by default. It can be enabled by calling CUPTI API

[cuptiActivityEnableCudaEventDeviceTimestamps](https://docs.nvidia.com#group__cupti__activity__api_1ga86a82dd4c053b885030dc12863c4b209)

-
enumerator CUDA_EVENT_FIELD_CUDA_EVENT_SYNC_ID
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds35CUDA_EVENT_FIELD_CUDA_EVENT_SYNC_IDE) uint64_t cudaEventSyncId; A unique ID to associate event synchronization records with the latest CUDA Event record.

Similar field is added in

[CUpti_ActivitySynchronization2](https://docs.nvidia.com/structCUpti__ActivitySynchronization2.html#structcupti__activitysynchronization2)to associate CUDA Event record to the synchronization record.The same CUDA event can be used multiple times, so the event id will not be unique to correlate the synchronization record with the latest CUDA Event record. This field will be unique and can be used to do the required correlation.


-
enumerator CUDA_EVENT_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N31CUpti_ActivityCudaEventFieldIds20CUDA_EVENT_FIELD_MAXE) Total number of defined fields.


-
enumerator CUDA_EVENT_FIELD_KIND

-
enum CUpti_ActivityDeviceFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityDeviceFieldIds) Enum identifiers for fields in

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6).Each enum value corresponds to a field in

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6)and describes the data type and purpose of that field.*Values:*-
enumerator DEVICE_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds17DEVICE_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_DEVICE.


-
enumerator DEVICE_FIELD_FLAGS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds18DEVICE_FIELD_FLAGSE) CUpti_ActivityFlag flags; Flags associated with the device.


-
enumerator DEVICE_FIELD_GLOBAL_MEMORY_BANDWIDTH
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds36DEVICE_FIELD_GLOBAL_MEMORY_BANDWIDTHE) uint64_t globalMemoryBandwidth; Global memory bandwidth available on the device (in kBytes/sec).


-
enumerator DEVICE_FIELD_GLOBAL_MEMORY_SIZE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds31DEVICE_FIELD_GLOBAL_MEMORY_SIZEE) uint64_t globalMemorySize; Amount of global memory on the device (in bytes).


-
enumerator DEVICE_FIELD_CONSTANT_MEMORY_SIZE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds33DEVICE_FIELD_CONSTANT_MEMORY_SIZEE) uint32_t constantMemorySize; Amount of constant memory on the device (in bytes).


-
enumerator DEVICE_FIELD_L2_CACHE_SIZE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds26DEVICE_FIELD_L2_CACHE_SIZEE) uint32_t l2CacheSize; Size of the L2 cache on the device (in bytes).


-
enumerator DEVICE_FIELD_NUM_THREADS_PER_WARP
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds33DEVICE_FIELD_NUM_THREADS_PER_WARPE) uint32_t numThreadsPerWarp; Number of threads per warp on the device.


-
enumerator DEVICE_FIELD_CORE_CLOCK_RATE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds28DEVICE_FIELD_CORE_CLOCK_RATEE) uint32_t coreClockRate; Core clock rate of the device (in kHz).


-
enumerator DEVICE_FIELD_NUM_MEMCPY_ENGINES
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds31DEVICE_FIELD_NUM_MEMCPY_ENGINESE) uint32_t numMemcpyEngines; Number of memory copy engines on the device.


-
enumerator DEVICE_FIELD_NUM_MULTIPROCESSORS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds32DEVICE_FIELD_NUM_MULTIPROCESSORSE) uint32_t numMultiprocessors; Number of multiprocessors on the device.


-
enumerator DEVICE_FIELD_MAX_IPC
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds20DEVICE_FIELD_MAX_IPCE) uint32_t maxIPC; Maximum instructions per cycle possible on each device multiprocessor.


-
enumerator DEVICE_FIELD_MAX_WARPS_PER_MULTIPROCESSOR
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds41DEVICE_FIELD_MAX_WARPS_PER_MULTIPROCESSORE) uint32_t maxWarpsPerMultiprocessor; Maximum number of warps that can be present on a multiprocessor.


-
enumerator DEVICE_FIELD_MAX_BLOCKS_PER_MULTIPROCESSOR
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds42DEVICE_FIELD_MAX_BLOCKS_PER_MULTIPROCESSORE) uint32_t maxBlocksPerMultiprocessor; Maximum number of blocks that can be present on a multiprocessor.


-
enumerator DEVICE_FIELD_MAX_SHARED_MEMORY_PER_MULTIPROCESSOR
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds49DEVICE_FIELD_MAX_SHARED_MEMORY_PER_MULTIPROCESSORE) uint32_t maxSharedMemoryPerMultiprocessor; Maximum amount of shared memory available per multiprocessor (in bytes).


-
enumerator DEVICE_FIELD_MAX_REGISTERS_PER_MULTIPROCESSOR
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds45DEVICE_FIELD_MAX_REGISTERS_PER_MULTIPROCESSORE) uint32_t maxRegistersPerMultiprocessor; Maximum number of 32-bit registers available per multiprocessor.


-
enumerator DEVICE_FIELD_MAX_REGISTERS_PER_BLOCK
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds36DEVICE_FIELD_MAX_REGISTERS_PER_BLOCKE) uint32_t maxRegistersPerBlock; Maximum number of registers that can be allocated to a block.


-
enumerator DEVICE_FIELD_MAX_SHARED_MEMORY_PER_BLOCK
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds40DEVICE_FIELD_MAX_SHARED_MEMORY_PER_BLOCKE) uint32_t maxSharedMemoryPerBlock; Maximum amount of shared memory that can be assigned to a block (in bytes).


-
enumerator DEVICE_FIELD_MAX_THREADS_PER_BLOCK
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds34DEVICE_FIELD_MAX_THREADS_PER_BLOCKE) uint32_t maxThreadsPerBlock; Maximum number of threads allowed in a block.


-
enumerator DEVICE_FIELD_MAX_BLOCK_DIM_X
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds28DEVICE_FIELD_MAX_BLOCK_DIM_XE) uint32_t maxBlockDimX; Maximum allowed X dimension for a block.


-
enumerator DEVICE_FIELD_MAX_BLOCK_DIM_Y
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds28DEVICE_FIELD_MAX_BLOCK_DIM_YE) uint32_t maxBlockDimY; Maximum allowed Y dimension for a block.


-
enumerator DEVICE_FIELD_MAX_BLOCK_DIM_Z
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds28DEVICE_FIELD_MAX_BLOCK_DIM_ZE) uint32_t maxBlockDimZ; Maximum allowed Z dimension for a block.


-
enumerator DEVICE_FIELD_MAX_GRID_DIM_X
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds27DEVICE_FIELD_MAX_GRID_DIM_XE) uint32_t maxGridDimX; Maximum allowed X dimension for a grid.


-
enumerator DEVICE_FIELD_MAX_GRID_DIM_Y
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds27DEVICE_FIELD_MAX_GRID_DIM_YE) uint32_t maxGridDimY; Maximum allowed Y dimension for a grid.


-
enumerator DEVICE_FIELD_MAX_GRID_DIM_Z
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds27DEVICE_FIELD_MAX_GRID_DIM_ZE) uint32_t maxGridDimZ; Maximum allowed Z dimension for a grid.


-
enumerator DEVICE_FIELD_COMPUTE_CAPABILITY_MAJOR
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds37DEVICE_FIELD_COMPUTE_CAPABILITY_MAJORE) uint32_t computeCapabilityMajor; Compute capability for the device (major number).


-
enumerator DEVICE_FIELD_COMPUTE_CAPABILITY_MINOR
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds37DEVICE_FIELD_COMPUTE_CAPABILITY_MINORE) uint32_t computeCapabilityMinor; Compute capability for the device (minor number).


-
enumerator DEVICE_FIELD_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds15DEVICE_FIELD_IDE) uint32_t id; Device ID.


-
enumerator DEVICE_FIELD_ECC_ENABLED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds24DEVICE_FIELD_ECC_ENABLEDE) uint32_t eccEnabled; ECC enabled flag for device.


-
enumerator DEVICE_FIELD_UUID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds17DEVICE_FIELD_UUIDE) CUuuid uuid; Device UUID.


-
enumerator DEVICE_FIELD_NAME
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds17DEVICE_FIELD_NAMEE) const char *name; Device name.


-
enumerator DEVICE_FIELD_IS_CUDA_VISIBLE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds28DEVICE_FIELD_IS_CUDA_VISIBLEE) uint8_t isCudaVisible; Flag to indicate whether the device is visible to CUDA.


-
enumerator DEVICE_FIELD_IS_MIG_ENABLED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds27DEVICE_FIELD_IS_MIG_ENABLEDE) uint8_t isMigEnabled; MIG enabled flag for device.


-
enumerator DEVICE_FIELD_GPU_INSTANCE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds28DEVICE_FIELD_GPU_INSTANCE_IDE) uint32_t gpuInstanceId; GPU instance ID for MIG enabled devices.


-
enumerator DEVICE_FIELD_COMPUTE_INSTANCE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds32DEVICE_FIELD_COMPUTE_INSTANCE_IDE) uint32_t computeInstanceId; Compute instance ID for MIG enabled devices.


-
enumerator DEVICE_FIELD_MIG_UUID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds21DEVICE_FIELD_MIG_UUIDE) CUuuid migUuid; MIG UUID.


-
enumerator DEVICE_FIELD_IS_NUMA_NODE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds25DEVICE_FIELD_IS_NUMA_NODEE) uint32_t isNumaNode; NUMA node flag for device.


-
enumerator DEVICE_FIELD_NUMA_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds20DEVICE_FIELD_NUMA_IDE) uint32_t numaId; NUMA node ID of the GPU memory.


-
enumerator DEVICE_FIELD_NUM_TPCS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds21DEVICE_FIELD_NUM_TPCSE) uint32_t numTpcs; Number of TPCs on the device.


-
enumerator DEVICE_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityDeviceFieldIds16DEVICE_FIELD_MAXE) Total number of defined fields.


-
enumerator DEVICE_FIELD_KIND

-
enum CUpti_ActivityDeviceGraphTraceFieldIds
[#](https://docs.nvidia.com#_CPPv438CUpti_ActivityDeviceGraphTraceFieldIds) Enum identifiers for fields in

[CUpti_ActivityDeviceGraphTrace](https://docs.nvidia.com/structCUpti__ActivityDeviceGraphTrace.html#structcupti__activitydevicegraphtrace).Each enum value corresponds to a field in

[CUpti_ActivityDeviceGraphTrace](https://docs.nvidia.com/structCUpti__ActivityDeviceGraphTrace.html#structcupti__activitydevicegraphtrace)and describes the data type and purpose of that field.*Values:*-
enumerator DEVICE_GRAPH_TRACE_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds29DEVICE_GRAPH_TRACE_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE.


-
enumerator DEVICE_GRAPH_TRACE_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds34DEVICE_GRAPH_TRACE_FIELD_DEVICE_IDE) uint32_t deviceId; ID of the device where the first node of the graph is executed.


-
enumerator DEVICE_GRAPH_TRACE_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds30DEVICE_GRAPH_TRACE_FIELD_STARTE) uint64_t start; Start timestamp for the graph execution (in ns).


-
enumerator DEVICE_GRAPH_TRACE_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds28DEVICE_GRAPH_TRACE_FIELD_ENDE) uint64_t end; End timestamp for the graph execution (in ns).


-
enumerator DEVICE_GRAPH_TRACE_FIELD_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds33DEVICE_GRAPH_TRACE_FIELD_GRAPH_IDE) uint32_t graphId; Unique ID of the graph that is launched.


-
enumerator DEVICE_GRAPH_TRACE_FIELD_LAUNCHER_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds42DEVICE_GRAPH_TRACE_FIELD_LAUNCHER_GRAPH_IDE) uint32_t launcherGraphId; Unique ID of the graph that has launched this graph.


-
enumerator DEVICE_GRAPH_TRACE_FIELD_DEVICE_LAUNCH_MODE
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds43DEVICE_GRAPH_TRACE_FIELD_DEVICE_LAUNCH_MODEE) uint32_t deviceLaunchMode; Type of launch.


-
enumerator DEVICE_GRAPH_TRACE_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds35DEVICE_GRAPH_TRACE_FIELD_CONTEXT_IDE) uint64_t contextId; ID of the context where the first node of the graph is executed.


-
enumerator DEVICE_GRAPH_TRACE_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds34DEVICE_GRAPH_TRACE_FIELD_STREAM_IDE) uint64_t streamId; ID of the stream where the graph is being launched.

This is the only record that has 64-bit streamId to accommodate device-side created streams.


-
enumerator DEVICE_GRAPH_TRACE_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityDeviceGraphTraceFieldIds28DEVICE_GRAPH_TRACE_FIELD_MAXE) Total number of defined fields.


-
enumerator DEVICE_GRAPH_TRACE_FIELD_KIND

-
enum CUpti_ActivityEnvironmentFieldIds
[#](https://docs.nvidia.com#_CPPv433CUpti_ActivityEnvironmentFieldIds) Enum identifiers for fields in

[CUpti_ActivityEnvironment](https://docs.nvidia.com/structCUpti__ActivityEnvironment.html#structcupti__activityenvironment).Each enum value corresponds to a field in

[CUpti_ActivityEnvironment](https://docs.nvidia.com/structCUpti__ActivityEnvironment.html#structcupti__activityenvironment)and describes the data type and purpose of that field.*Values:*-
enumerator ENVIRONMENT_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityEnvironmentFieldIds22ENVIRONMENT_FIELD_KINDE) CUpti_ActivityKind kind; Kind of activity record: CUPTI_ACTIVITY_KIND_ENVIRONMENT.


-
enumerator ENVIRONMENT_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityEnvironmentFieldIds27ENVIRONMENT_FIELD_DEVICE_IDE) uint32_t deviceId; The ID of the device


-
enumerator ENVIRONMENT_FIELD_TIMESTAMP
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityEnvironmentFieldIds27ENVIRONMENT_FIELD_TIMESTAMPE) uint64_t timestamp; The timestamp when this sample was retrieved, in ns.

A value of 0 indicates that timestamp information could not be collected for the marker.


-
enumerator ENVIRONMENT_FIELD_ENVIRONMENT_KIND
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityEnvironmentFieldIds34ENVIRONMENT_FIELD_ENVIRONMENT_KINDE) CUpti_ActivityEnvironmentKind environmentKind; The kind of data reported in this record.


-
enumerator ENVIRONMENT_FIELD_ENVIRONMENT_KIND_DATA
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityEnvironmentFieldIds39ENVIRONMENT_FIELD_ENVIRONMENT_KIND_DATAE) union data; Depending on the value of environmentKind, this field contains additional information about the environment.

[CUpti_ActivityEnvironmentSpeed](https://docs.nvidia.com/structCUpti__ActivityEnvironmentSpeed.html#structcupti__activityenvironmentspeed)speed if environmentKind is CUPTI_ACTIVITY_ENVIRONMENT_SPEED[CUpti_ActivityEnvironmentTemperature](https://docs.nvidia.com/structCUpti__ActivityEnvironmentTemperature.html#structcupti__activityenvironmenttemperature)temperature if environmentKind is CUPTI_ACTIVITY_ENVIRONMENT_TEMPERATURE[CUpti_ActivityEnvironmentPower](https://docs.nvidia.com/structCUpti__ActivityEnvironmentPower.html#structcupti__activityenvironmentpower)power if environmentKind is CUPTI_ACTIVITY_ENVIRONMENT_POWER[CUpti_ActivityEnvironmentCooling](https://docs.nvidia.com/structCUpti__ActivityEnvironmentCooling.html#structcupti__activityenvironmentcooling)cooling if environmentKind is CUPTI_ACTIVITY_ENVIRONMENT_COOLING The size of this field is determined by the largest structure among the possible types it can hold.

-
enumerator ENVIRONMENT_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityEnvironmentFieldIds21ENVIRONMENT_FIELD_MAXE) Total number of defined fields.


-
enumerator ENVIRONMENT_FIELD_KIND

-
enum CUpti_ActivityEnvironmentKind
[#](https://docs.nvidia.com#_CPPv429CUpti_ActivityEnvironmentKind) The kind of environment data.

Used to indicate what type of data is being reported by an environment activity record.

*Values:*-
enumerator CUPTI_ACTIVITY_ENVIRONMENT_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityEnvironmentKind34CUPTI_ACTIVITY_ENVIRONMENT_UNKNOWNE) Unknown data.


-
enumerator CUPTI_ACTIVITY_ENVIRONMENT_SPEED
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityEnvironmentKind32CUPTI_ACTIVITY_ENVIRONMENT_SPEEDE) The environment data is related to speed.


-
enumerator CUPTI_ACTIVITY_ENVIRONMENT_TEMPERATURE
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityEnvironmentKind38CUPTI_ACTIVITY_ENVIRONMENT_TEMPERATUREE) The environment data is related to temperature.


-
enumerator CUPTI_ACTIVITY_ENVIRONMENT_POWER
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityEnvironmentKind32CUPTI_ACTIVITY_ENVIRONMENT_POWERE) The environment data is related to power.


-
enumerator CUPTI_ACTIVITY_ENVIRONMENT_COOLING
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityEnvironmentKind34CUPTI_ACTIVITY_ENVIRONMENT_COOLINGE) The environment data is related to cooling.


-
enumerator CUPTI_ACTIVITY_ENVIRONMENT_COUNT
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityEnvironmentKind32CUPTI_ACTIVITY_ENVIRONMENT_COUNTE)

-
enumerator CUPTI_ACTIVITY_ENVIRONMENT_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityEnvironmentKind41CUPTI_ACTIVITY_ENVIRONMENT_KIND_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_ENVIRONMENT_UNKNOWN

-
enum CUpti_ActivityExternalCorrelationFieldIds
[#](https://docs.nvidia.com#_CPPv441CUpti_ActivityExternalCorrelationFieldIds) Enum identifiers for fields in

[CUpti_ActivityExternalCorrelation](https://docs.nvidia.com/structCUpti__ActivityExternalCorrelation.html#structcupti__activityexternalcorrelation).This activity record correlates native CUDA records (e.g. CUDA Driver API, kernels, memcpys, …) with records from external APIs such as OpenACC. (CUPTI_ACTIVITY_KIND_EXTERNAL_CORRELATION).

*Values:*-
enumerator EXTERNAL_CORRELATION_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityExternalCorrelationFieldIds31EXTERNAL_CORRELATION_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_EXTERNAL_CORRELATION.


-
enumerator EXTERNAL_CORRELATION_FIELD_EXTERNAL_KIND
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityExternalCorrelationFieldIds40EXTERNAL_CORRELATION_FIELD_EXTERNAL_KINDE) CUpti_ExternalCorrelationKind externalKind; Kind of external API this record correlated to.


-
enumerator EXTERNAL_CORRELATION_FIELD_EXTERNAL_ID
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityExternalCorrelationFieldIds38EXTERNAL_CORRELATION_FIELD_EXTERNAL_IDE) uint64_t externalId; Correlation ID of the associated non-CUDA API record.


-
enumerator EXTERNAL_CORRELATION_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityExternalCorrelationFieldIds41EXTERNAL_CORRELATION_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID of the associated CUDA driver or runtime API record.


-
enumerator EXTERNAL_CORRELATION_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityExternalCorrelationFieldIds30EXTERNAL_CORRELATION_FIELD_MAXE) Total number of defined fields.


-
enumerator EXTERNAL_CORRELATION_FIELD_KIND

-
enum CUpti_ActivityFlag
[#](https://docs.nvidia.com#_CPPv418CUpti_ActivityFlag) Flags associated with activity records.

Activity record flags. Flags can be combined by bitwise OR to associated multiple flags with an activity record. Each flag is specific to a certain activity kind, as noted below.

*Values:*-
enumerator CUPTI_ACTIVITY_FLAG_NONE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag24CUPTI_ACTIVITY_FLAG_NONEE) Indicates the activity record has no flags.


-
enumerator CUPTI_ACTIVITY_FLAG_DEVICE_CONCURRENT_KERNELS
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag45CUPTI_ACTIVITY_FLAG_DEVICE_CONCURRENT_KERNELSE) Indicates the activity represents a device that supports concurrent kernel execution.

Valid for CUPTI_ACTIVITY_KIND_DEVICE.


-
enumerator CUPTI_ACTIVITY_FLAG_DEVICE_ATTRIBUTE_CUDEVICE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag45CUPTI_ACTIVITY_FLAG_DEVICE_ATTRIBUTE_CUDEVICEE) Indicates if the activity represents a CUdevice_attribute value or a CUpti_DeviceAttribute value.

Valid for CUPTI_ACTIVITY_KIND_DEVICE_ATTRIBUTE.


-
enumerator CUPTI_ACTIVITY_FLAG_MEMCPY_ASYNC
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag32CUPTI_ACTIVITY_FLAG_MEMCPY_ASYNCE) Indicates the activity represents an asynchronous memcpy operation.

Valid for CUPTI_ACTIVITY_KIND_MEMCPY.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_INSTANTANEOUS
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag40CUPTI_ACTIVITY_FLAG_MARKER_INSTANTANEOUSE) Indicates the activity represents an instantaneous marker.

Valid for CUPTI_ACTIVITY_KIND_MARKER.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_START
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag32CUPTI_ACTIVITY_FLAG_MARKER_STARTE) Indicates the activity represents a region start marker.

Valid for CUPTI_ACTIVITY_KIND_MARKER.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_END
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag30CUPTI_ACTIVITY_FLAG_MARKER_ENDE) Indicates the activity represents a region end marker.

Valid for CUPTI_ACTIVITY_KIND_MARKER.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIRE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag39CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIREE) Indicates the activity represents an attempt to acquire a user defined synchronization object.

Valid for CUPTI_ACTIVITY_KIND_MARKER.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIRE_SUCCESS
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag47CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIRE_SUCCESSE) Indicates the activity represents success in acquiring the user defined synchronization object.

Valid for CUPTI_ACTIVITY_KIND_MARKER.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIRE_FAILED
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag46CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIRE_FAILEDE) Indicates the activity represents failure in acquiring the user defined synchronization object.

Valid for CUPTI_ACTIVITY_KIND_MARKER.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_SYNC_RELEASE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag39CUPTI_ACTIVITY_FLAG_MARKER_SYNC_RELEASEE) Indicates the activity represents releasing a reservation on user defined synchronization object.

Valid for CUPTI_ACTIVITY_KIND_MARKER.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_COLOR_NONE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag37CUPTI_ACTIVITY_FLAG_MARKER_COLOR_NONEE) Indicates the activity represents a marker that does not specify a color.

Valid for CUPTI_ACTIVITY_KIND_MARKER_DATA.


-
enumerator CUPTI_ACTIVITY_FLAG_MARKER_COLOR_ARGB
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag37CUPTI_ACTIVITY_FLAG_MARKER_COLOR_ARGBE) Indicates the activity represents a marker that specifies a color in alpha-red-green-blue format.

Valid for CUPTI_ACTIVITY_KIND_MARKER_DATA.


-
enumerator CUPTI_ACTIVITY_FLAG_GLOBAL_ACCESS_KIND_SIZE_MASK
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag48CUPTI_ACTIVITY_FLAG_GLOBAL_ACCESS_KIND_SIZE_MASKE) The number of bytes requested by each thread Valid for

[CUpti_ActivityGlobalAccess3](https://docs.nvidia.com/structCUpti__ActivityGlobalAccess3.html#structcupti__activityglobalaccess3).

-
enumerator CUPTI_ACTIVITY_FLAG_GLOBAL_ACCESS_KIND_LOAD
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag43CUPTI_ACTIVITY_FLAG_GLOBAL_ACCESS_KIND_LOADE) If bit in this flag is set, the access was load, else it is a store access.

Valid for

[CUpti_ActivityGlobalAccess3](https://docs.nvidia.com/structCUpti__ActivityGlobalAccess3.html#structcupti__activityglobalaccess3).

-
enumerator CUPTI_ACTIVITY_FLAG_GLOBAL_ACCESS_KIND_CACHED
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag45CUPTI_ACTIVITY_FLAG_GLOBAL_ACCESS_KIND_CACHEDE) If this bit in flag is set, the load access was cached else it is uncached.

Valid for

[CUpti_ActivityGlobalAccess3](https://docs.nvidia.com/structCUpti__ActivityGlobalAccess3.html#structcupti__activityglobalaccess3).

-
enumerator CUPTI_ACTIVITY_FLAG_METRIC_OVERFLOWED
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag37CUPTI_ACTIVITY_FLAG_METRIC_OVERFLOWEDE) If this bit in flag is set, the metric value overflowed.

Valid for

[CUpti_ActivityMetric](https://docs.nvidia.com/structCUpti__ActivityMetric.html#structcupti__activitymetric)and[CUpti_ActivityMetricInstance](https://docs.nvidia.com/structCUpti__ActivityMetricInstance.html#structcupti__activitymetricinstance).

-
enumerator CUPTI_ACTIVITY_FLAG_METRIC_VALUE_INVALID
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag40CUPTI_ACTIVITY_FLAG_METRIC_VALUE_INVALIDE) If this bit in flag is set, the metric value couldn’t be calculated.

This occurs when a value(s) required to calculate the metric is missing. Valid for

[CUpti_ActivityMetric](https://docs.nvidia.com/structCUpti__ActivityMetric.html#structcupti__activitymetric)and[CUpti_ActivityMetricInstance](https://docs.nvidia.com/structCUpti__ActivityMetricInstance.html#structcupti__activitymetricinstance).

-
enumerator CUPTI_ACTIVITY_FLAG_INSTRUCTION_VALUE_INVALID
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag45CUPTI_ACTIVITY_FLAG_INSTRUCTION_VALUE_INVALIDE) If this bit in flag is set, the source level metric value couldn’t be calculated.

This occurs when a value(s) required to calculate the source level metric cannot be evaluated. Valid for

[CUpti_ActivityInstructionExecution](https://docs.nvidia.com/structCUpti__ActivityInstructionExecution.html#structcupti__activityinstructionexecution).

-
enumerator CUPTI_ACTIVITY_FLAG_INSTRUCTION_CLASS_MASK
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag42CUPTI_ACTIVITY_FLAG_INSTRUCTION_CLASS_MASKE) The mask for the instruction class,

[CUpti_ActivityInstructionClass](https://docs.nvidia.com#group__cupti__activity__api_1gabb6c00413aa3491f7da9e9cbbecf4133)Valid for[CUpti_ActivityInstructionExecution](https://docs.nvidia.com/structCUpti__ActivityInstructionExecution.html#structcupti__activityinstructionexecution)and[CUpti_ActivityInstructionCorrelation](https://docs.nvidia.com/structCUpti__ActivityInstructionCorrelation.html#structcupti__activityinstructioncorrelation).

-
enumerator CUPTI_ACTIVITY_FLAG_FLUSH_FORCED
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag32CUPTI_ACTIVITY_FLAG_FLUSH_FORCEDE) When calling cuptiActivityFlushAll, this flag can be set to force CUPTI to flush all records in the buffer, whether finished or not.


-
enumerator CUPTI_ACTIVITY_FLAG_SHARED_ACCESS_KIND_SIZE_MASK
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag48CUPTI_ACTIVITY_FLAG_SHARED_ACCESS_KIND_SIZE_MASKE) The number of bytes requested by each thread Valid for

[CUpti_ActivitySharedAccess](https://docs.nvidia.com/structCUpti__ActivitySharedAccess.html#structcupti__activitysharedaccess).

-
enumerator CUPTI_ACTIVITY_FLAG_SHARED_ACCESS_KIND_LOAD
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag43CUPTI_ACTIVITY_FLAG_SHARED_ACCESS_KIND_LOADE) If bit in this flag is set, the access was load, else it is a store access.

Valid for

[CUpti_ActivitySharedAccess](https://docs.nvidia.com/structCUpti__ActivitySharedAccess.html#structcupti__activitysharedaccess).

-
enumerator CUPTI_ACTIVITY_FLAG_MEMSET_ASYNC
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag32CUPTI_ACTIVITY_FLAG_MEMSET_ASYNCE) Indicates the activity represents an asynchronous memset operation.

Valid for CUPTI_ACTIVITY_KIND_MEMSET.


-
enumerator CUPTI_ACTIVITY_FLAG_THRASHING_IN_CPU
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag36CUPTI_ACTIVITY_FLAG_THRASHING_IN_CPUE) Indicates the activity represents thrashing in CPU.

Valid for counter of kind CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_THRASHING in CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTER


-
enumerator CUPTI_ACTIVITY_FLAG_THROTTLING_IN_CPU
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag37CUPTI_ACTIVITY_FLAG_THROTTLING_IN_CPUE) Indicates the activity represents page throttling in CPU.

Valid for counter of kind CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_THROTTLING in CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTER


-
enumerator CUPTI_ACTIVITY_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityFlag29CUPTI_ACTIVITY_FLAG_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_FLAG_NONE

-
enum CUpti_ActivityGraphHostNodeFieldIds
[#](https://docs.nvidia.com#_CPPv435CUpti_ActivityGraphHostNodeFieldIds) Enum identifiers for fields in CUpti_ActivityGraphHostNode.

Each enum value corresponds to a field in CUpti_ActivityGraphHostNode and describes the data type and purpose of that field.

*Values:*-
enumerator GRAPH_HOST_NODE_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds26GRAPH_HOST_NODE_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_GRAPH_HOST_NODE.


-
enumerator GRAPH_HOST_NODE_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds31GRAPH_HOST_NODE_FIELD_STREAM_IDE) uint32_t streamId; ID of the stream that waits for the graph host node to finish.


-
enumerator GRAPH_HOST_NODE_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds32GRAPH_HOST_NODE_FIELD_CONTEXT_IDE) uint32_t contextId; ID of the CUDA context to which the waiting CUDA stream belongs.


-
enumerator GRAPH_HOST_NODE_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds31GRAPH_HOST_NODE_FIELD_DEVICE_IDE) uint32_t deviceId; ID of the CUDA device to which the CUDA context and stream belong.


-
enumerator GRAPH_HOST_NODE_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds36GRAPH_HOST_NODE_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID of the graph host node operation.


-
enumerator GRAPH_HOST_NODE_FIELD_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds30GRAPH_HOST_NODE_FIELD_GRAPH_IDE) uint32_t graphId; Unique ID of the graph that executed this host node through graph launch.


-
enumerator GRAPH_HOST_NODE_FIELD_GRAPH_NODE_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds35GRAPH_HOST_NODE_FIELD_GRAPH_NODE_IDE) uint64_t graphNodeId; Unique ID of the graph node that executed this host node through graph launch.


-
enumerator GRAPH_HOST_NODE_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds32GRAPH_HOST_NODE_FIELD_PROCESS_IDE) uint32_t processId; ID of the process where the host node is executing.


-
enumerator GRAPH_HOST_NODE_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds31GRAPH_HOST_NODE_FIELD_THREAD_IDE) uint64_t threadId; ID of the thread where the host node is executing.


-
enumerator GRAPH_HOST_NODE_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds27GRAPH_HOST_NODE_FIELD_STARTE) uint64_t start; Start timestamp.


-
enumerator GRAPH_HOST_NODE_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds25GRAPH_HOST_NODE_FIELD_ENDE) uint64_t end; End timestamp.


-
enumerator GRAPH_HOST_NODE_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityGraphHostNodeFieldIds25GRAPH_HOST_NODE_FIELD_MAXE) Total number of defined fields.


-
enumerator GRAPH_HOST_NODE_FIELD_KIND

-
enum CUpti_ActivityGraphTraceFieldIds
[#](https://docs.nvidia.com#_CPPv432CUpti_ActivityGraphTraceFieldIds) Enum identifiers for fields to trace graph execution.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_GRAPH_TRACE.

*Values:*-
enumerator GRAPH_TRACE_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds22GRAPH_TRACE_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_GRAPH_TRACE.


-
enumerator GRAPH_TRACE_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds32GRAPH_TRACE_FIELD_CORRELATION_IDE) uint64_t correlationId; The correlation ID of the graph launch.


-
enumerator GRAPH_TRACE_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds23GRAPH_TRACE_FIELD_STARTE) uint64_t start; The start timestamp for the graph execution, in ns.


-
enumerator GRAPH_TRACE_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds21GRAPH_TRACE_FIELD_ENDE) uint64_t end; The end timestamp for the graph execution, in ns.


-
enumerator GRAPH_TRACE_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds27GRAPH_TRACE_FIELD_DEVICE_IDE) uint32_t deviceId; The ID of the device where the first node of the graph is executed.

If this is INT_MAX, then the start is on the host.


-
enumerator GRAPH_TRACE_FIELD_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds26GRAPH_TRACE_FIELD_GRAPH_IDE) uint32_t graphId; The unique ID of the graph that is launched.


-
enumerator GRAPH_TRACE_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds28GRAPH_TRACE_FIELD_CONTEXT_IDE) uint32_t contextId; The ID of the context where the first node of the graph is executed.

If this is INT_MAX, then the start is on the host.


-
enumerator GRAPH_TRACE_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds27GRAPH_TRACE_FIELD_STREAM_IDE) uint32_t streamId; The ID of the stream where the graph is being launched.


-
enumerator GRAPH_TRACE_FIELD_END_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds31GRAPH_TRACE_FIELD_END_DEVICE_IDE) uint32_t endDeviceId; The ID of the device where last node of the graph is executed.


-
enumerator GRAPH_TRACE_FIELD_END_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds32GRAPH_TRACE_FIELD_END_CONTEXT_IDE) uint32_t endContextId; The ID of the context where the last node of the graph is executed.


-
enumerator GRAPH_TRACE_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityGraphTraceFieldIds21GRAPH_TRACE_FIELD_MAXE) Total number of defined fields.


-
enumerator GRAPH_TRACE_FIELD_KIND

-
enum CUpti_ActivityGreenContextFieldIds
[#](https://docs.nvidia.com#_CPPv434CUpti_ActivityGreenContextFieldIds) Enum identifiers for fields to trace green context information.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_GREEN_CONTEXT.

*Values:*-
enumerator GREEN_CONTEXT_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds24GREEN_CONTEXT_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_GREEN_CONTEXT.


-
enumerator GREEN_CONTEXT_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds30GREEN_CONTEXT_FIELD_CONTEXT_IDE) uint32_t contextId; The context ID of the green context.


-
enumerator GREEN_CONTEXT_FIELD_PARENT_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds37GREEN_CONTEXT_FIELD_PARENT_CONTEXT_IDE) uint32_t parentContextId; The ID of the parent context.


-
enumerator GREEN_CONTEXT_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds29GREEN_CONTEXT_FIELD_DEVICE_IDE) uint32_t deviceId; The device ID associated with the green context.


-
enumerator GREEN_CONTEXT_FIELD_NUM_MULTIPROCESSORS
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds39GREEN_CONTEXT_FIELD_NUM_MULTIPROCESSORSE) uint16_t numMultiprocessors; The number of multiprocessors (SMs) allocated to the green context.


-
enumerator GREEN_CONTEXT_FIELD_NUM_TPCS
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds28GREEN_CONTEXT_FIELD_NUM_TPCSE) uint32_t numTpcs; The number of TPCs allocated to the green context.


-
enumerator GREEN_CONTEXT_FIELD_LOGICAL_TPC_MASK_SIZE
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds41GREEN_CONTEXT_FIELD_LOGICAL_TPC_MASK_SIZEE) uint8_t logicalTpcMaskSize; The size (in 32-bit words) of the logical TPC mask.


-
enumerator GREEN_CONTEXT_FIELD_LOGICAL_TPC_MASK
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds36GREEN_CONTEXT_FIELD_LOGICAL_TPC_MASKE) uint32_t logicalTpcMask[32]; The logical TPC mask for the green context.


-
enumerator GREEN_CONTEXT_FIELD_WORKQUEUE_RESOURCE_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds41GREEN_CONTEXT_FIELD_WORKQUEUE_RESOURCE_IDE) uint64_t workqueueResourceId; The work queue resource ID associated with the green context.

Refer

- Param CUdevWorkqueueConfigScope:
in cuda.h for possible values.



-
enumerator GREEN_CONTEXT_FIELD_WORKQUEUE_CONCURRENCY_LIMIT
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds47GREEN_CONTEXT_FIELD_WORKQUEUE_CONCURRENCY_LIMITE) uint32_t workqueueConcurrencyLimit; The concurrency limit for the work queue associated with the green context.


-
enumerator GREEN_CONTEXT_FIELD_WORKQUEUE_SHARING_SCOPE
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds43GREEN_CONTEXT_FIELD_WORKQUEUE_SHARING_SCOPEE) uint32_t workqueueSharingScope; The sharing scope for the work queue associated with the green context.


-
enumerator GREEN_CONTEXT_FIELD_WORKQUEUE_CHANNEL_COUNT
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds43GREEN_CONTEXT_FIELD_WORKQUEUE_CHANNEL_COUNTE) uint32_t workqueueChannelCount; The number of HW channels assigned to this green context’s work queue.


-
enumerator GREEN_CONTEXT_FIELD_WORKQUEUE_CHANNEL_IDS
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds41GREEN_CONTEXT_FIELD_WORKQUEUE_CHANNEL_IDSE) uint32_t workqueueChannelIds[32]; Array of HW channel IDs assigned to this green context’s work queue.


-
enumerator GREEN_CONTEXT_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityGreenContextFieldIds23GREEN_CONTEXT_FIELD_MAXE) Total number of defined fields.


-
enumerator GREEN_CONTEXT_FIELD_KIND

-
enum CUpti_ActivityHostLaunchFieldIds
[#](https://docs.nvidia.com#_CPPv432CUpti_ActivityHostLaunchFieldIds) Enum identifiers for fields in

[CUpti_ActivityHostLaunch](https://docs.nvidia.com/structCUpti__ActivityHostLaunch.html#structcupti__activityhostlaunch).Each enum value corresponds to a field in

[CUpti_ActivityHostLaunch](https://docs.nvidia.com/structCUpti__ActivityHostLaunch.html#structcupti__activityhostlaunch)and describes the data type and purpose of that field.*Values:*-
enumerator HOST_LAUNCH_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds22HOST_LAUNCH_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_HOST_LAUNCH.


-
enumerator HOST_LAUNCH_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds27HOST_LAUNCH_FIELD_STREAM_IDE) uint32_t streamId; ID of the CUDA stream to which the waiting CUDA stream belongs.


-
enumerator HOST_LAUNCH_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds28HOST_LAUNCH_FIELD_CONTEXT_IDE) uint32_t contextId; ID of the CUDA context to which the waiting CUDA stream belongs.


-
enumerator HOST_LAUNCH_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds27HOST_LAUNCH_FIELD_DEVICE_IDE) uint32_t deviceId; ID of the CUDA device to which the CUDA context and stream belong.


-
enumerator HOST_LAUNCH_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds32HOST_LAUNCH_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID of the host launch operation.


-
enumerator HOST_LAUNCH_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds28HOST_LAUNCH_FIELD_PROCESS_IDE) uint32_t processId; ID of the process where the host function is executing.


-
enumerator HOST_LAUNCH_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds27HOST_LAUNCH_FIELD_THREAD_IDE) uint64_t threadId; ID of the thread where the host function is executing.


-
enumerator HOST_LAUNCH_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds23HOST_LAUNCH_FIELD_STARTE) uint64_t start; Start timestamp.


-
enumerator HOST_LAUNCH_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds21HOST_LAUNCH_FIELD_ENDE) uint64_t end; End timestamp.


-
enumerator HOST_LAUNCH_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityHostLaunchFieldIds21HOST_LAUNCH_FIELD_MAXE) Total number of defined fields.


-
enumerator HOST_LAUNCH_FIELD_KIND

-
enum CUpti_ActivityInstructionClass
[#](https://docs.nvidia.com#_CPPv430CUpti_ActivityInstructionClass) SASS instruction classification.

The sass instruction are broadly divided into different class. Each enum represents a classification.

*Values:*-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass40CUPTI_ACTIVITY_INSTRUCTION_CLASS_UNKNOWNE) The instruction class is not known.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_FP_32
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass38CUPTI_ACTIVITY_INSTRUCTION_CLASS_FP_32E) Represents a 32 bit floating point operation.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_FP_64
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass38CUPTI_ACTIVITY_INSTRUCTION_CLASS_FP_64E) Represents a 64 bit floating point operation.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_INTEGER
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass40CUPTI_ACTIVITY_INSTRUCTION_CLASS_INTEGERE) Represents an integer operation.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_BIT_CONVERSION
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass47CUPTI_ACTIVITY_INSTRUCTION_CLASS_BIT_CONVERSIONE) Represents a bit conversion operation.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_CONTROL_FLOW
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass45CUPTI_ACTIVITY_INSTRUCTION_CLASS_CONTROL_FLOWE) Represents a control flow instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_GLOBAL
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass39CUPTI_ACTIVITY_INSTRUCTION_CLASS_GLOBALE) Represents a global load-store instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_SHARED
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass39CUPTI_ACTIVITY_INSTRUCTION_CLASS_SHAREDE) Represents a shared load-store instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_LOCAL
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass38CUPTI_ACTIVITY_INSTRUCTION_CLASS_LOCALE) Represents a local load-store instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_GENERIC
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass40CUPTI_ACTIVITY_INSTRUCTION_CLASS_GENERICE) Represents a generic load-store instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_SURFACE
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass40CUPTI_ACTIVITY_INSTRUCTION_CLASS_SURFACEE) Represents a surface load-store instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_CONSTANT
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass41CUPTI_ACTIVITY_INSTRUCTION_CLASS_CONSTANTE) Represents a constant load instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_TEXTURE
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass40CUPTI_ACTIVITY_INSTRUCTION_CLASS_TEXTUREE) Represents a texture load-store instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_GLOBAL_ATOMIC
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass46CUPTI_ACTIVITY_INSTRUCTION_CLASS_GLOBAL_ATOMICE) Represents a global atomic instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_SHARED_ATOMIC
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass46CUPTI_ACTIVITY_INSTRUCTION_CLASS_SHARED_ATOMICE) Represents a shared atomic instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_SURFACE_ATOMIC
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass47CUPTI_ACTIVITY_INSTRUCTION_CLASS_SURFACE_ATOMICE) Represents a surface atomic instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_INTER_THREAD_COMMUNICATION
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass59CUPTI_ACTIVITY_INSTRUCTION_CLASS_INTER_THREAD_COMMUNICATIONE) Represents a inter-thread communication instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_BARRIER
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass40CUPTI_ACTIVITY_INSTRUCTION_CLASS_BARRIERE) Represents a barrier instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_MISCELLANEOUS
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass46CUPTI_ACTIVITY_INSTRUCTION_CLASS_MISCELLANEOUSE) Represents some miscellaneous instructions which do not fit in the above classification.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_FP_16
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass38CUPTI_ACTIVITY_INSTRUCTION_CLASS_FP_16E) Represents a 16 bit floating point operation.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_UNIFORM
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass40CUPTI_ACTIVITY_INSTRUCTION_CLASS_UNIFORME) Represents uniform instruction.


-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityInstructionClass47CUPTI_ACTIVITY_INSTRUCTION_CLASS_KIND_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_INSTRUCTION_CLASS_UNKNOWN

-
enum CUpti_ActivityJitEntryType
[#](https://docs.nvidia.com#_CPPv426CUpti_ActivityJitEntryType) The types of JIT entry.

To be used in

[CUpti_ActivityJit](https://docs.nvidia.com/structCUpti__ActivityJit.html#structcupti__activityjit).*Values:*-
enumerator CUPTI_ACTIVITY_JIT_ENTRY_INVALID
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityJitEntryType32CUPTI_ACTIVITY_JIT_ENTRY_INVALIDE)

-
enumerator CUPTI_ACTIVITY_JIT_ENTRY_PTX_TO_CUBIN
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityJitEntryType37CUPTI_ACTIVITY_JIT_ENTRY_PTX_TO_CUBINE) PTX to CUBIN.


-
enumerator CUPTI_ACTIVITY_JIT_ENTRY_NVVM_IR_TO_PTX
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityJitEntryType39CUPTI_ACTIVITY_JIT_ENTRY_NVVM_IR_TO_PTXE) NVVM-IR to PTX.


-
enumerator CUPTI_ACTIVITY_JIT_ENTRY_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityJitEntryType39CUPTI_ACTIVITY_JIT_ENTRY_TYPE_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_JIT_ENTRY_INVALID

-
enum CUpti_ActivityJitFieldIds
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityJitFieldIds) Enum identifiers for fields to trace JIT operations.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_JIT.

*Values:*-
enumerator JIT_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds14JIT_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_JIT.


-
enumerator JIT_FIELD_ENTRY_TYPE
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds20JIT_FIELD_ENTRY_TYPEE) CUpti_ActivityJitEntryType jitEntryType; The JIT entry type.


-
enumerator JIT_FIELD_OPERATION_TYPE
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds24JIT_FIELD_OPERATION_TYPEE) CUpti_ActivityJitOperationType jitOperationType; The JIT operation type.


-
enumerator JIT_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds19JIT_FIELD_DEVICE_IDE) uint32_t deviceId; The device ID.


-
enumerator JIT_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds15JIT_FIELD_STARTE) uint64_t start; The start timestamp for the JIT operation (in nanoseconds).


-
enumerator JIT_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds13JIT_FIELD_ENDE) uint64_t end; The end timestamp for the JIT operation (in nanoseconds).


-
enumerator JIT_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds24JIT_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this JIT operation.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator JIT_FIELD_OPERATION_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds34JIT_FIELD_OPERATION_CORRELATION_IDE) uint64_t jitOperationCorrelationId; The correlation ID to correlate JIT compilation, load and store operations.

Each JIT compilation unit is assigned a unique correlation ID at the time of the JIT compilation. This correlation id can be used to find the matching JIT cache load/store records.


-
enumerator JIT_FIELD_CACHE_SIZE
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds20JIT_FIELD_CACHE_SIZEE) uint64_t cacheSize; The size of compute cache.


-
enumerator JIT_FIELD_CACHE_PATH
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds20JIT_FIELD_CACHE_PATHE) const char* cachePath; The path where the fat binary is cached.


-
enumerator JIT_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds20JIT_FIELD_PROCESS_IDE) uint32_t processId; The ID of the process where the JIT operation is executing.


-
enumerator JIT_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds19JIT_FIELD_THREAD_IDE) uint64_t threadId; The ID of the thread where the JIT operation is executing.


-
enumerator JIT_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityJitFieldIds13JIT_FIELD_MAXE) Total number of defined fields.


-
enumerator JIT_FIELD_KIND

-
enum CUpti_ActivityJitOperationType
[#](https://docs.nvidia.com#_CPPv430CUpti_ActivityJitOperationType) The types of JIT compilation operations.

To be used in

[CUpti_ActivityJit](https://docs.nvidia.com/structCUpti__ActivityJit.html#structcupti__activityjit).*Values:*-
enumerator CUPTI_ACTIVITY_JIT_OPERATION_INVALID
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityJitOperationType36CUPTI_ACTIVITY_JIT_OPERATION_INVALIDE)

-
enumerator CUPTI_ACTIVITY_JIT_OPERATION_CACHE_LOAD
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityJitOperationType39CUPTI_ACTIVITY_JIT_OPERATION_CACHE_LOADE) Loaded from the compute cache.


-
enumerator CUPTI_ACTIVITY_JIT_OPERATION_CACHE_STORE
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityJitOperationType40CUPTI_ACTIVITY_JIT_OPERATION_CACHE_STOREE) Stored in the compute cache.


-
enumerator CUPTI_ACTIVITY_JIT_OPERATION_COMPILE
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityJitOperationType36CUPTI_ACTIVITY_JIT_OPERATION_COMPILEE) JIT compilation.


-
enumerator CUPTI_ACTIVITY_JIT_OPERATION_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityJitOperationType43CUPTI_ACTIVITY_JIT_OPERATION_TYPE_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_JIT_OPERATION_INVALID

-
enum CUpti_ActivityKernelFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityKernelFieldIds) Enum identifiers for fields to trace kernel operations.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL.

*Values:*-
enumerator KERNEL_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds17KERNEL_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always either CUPTI_ACTIVITY_KIND_KERNEL or CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL.


-
enumerator KERNEL_FIELD_CACHE_CONFIG_REQUESTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds35KERNEL_FIELD_CACHE_CONFIG_REQUESTEDE) uint8_t requested; Indicates the cache configuration requested by the kernel.

Values are from CUfunc_cache enumeration.


-
enumerator KERNEL_FIELD_CACHE_CONFIG_EXECUTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds34KERNEL_FIELD_CACHE_CONFIG_EXECUTEDE) uint8_t executed; Indicates the cache configuration actually used during kernel execution.

Values are from CUfunc_cache enumeration.


-
enumerator KERNEL_FIELD_SHARED_MEMORY_CONFIG
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds33KERNEL_FIELD_SHARED_MEMORY_CONFIGE) uint8_t sharedMemoryConfig; Specifies the shared memory configuration used for the kernel.

Values are from CUsharedconfig enumeration.


-
enumerator KERNEL_FIELD_REGISTERS_PER_THREAD
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds33KERNEL_FIELD_REGISTERS_PER_THREADE) uint16_t registersPerThread; Number of registers required for each thread executing the kernel.


-
enumerator KERNEL_FIELD_PARTITIONED_GLOBAL_CACHE_REQUESTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds47KERNEL_FIELD_PARTITIONED_GLOBAL_CACHE_REQUESTEDE) CUpti_ActivityPartitionedGlobalCacheConfig requested; Partitioned global caching requested for the kernel.

Relevant for devices requiring this to enable caching.


-
enumerator KERNEL_FIELD_PARTITIONED_GLOBAL_CACHE_EXECUTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds46KERNEL_FIELD_PARTITIONED_GLOBAL_CACHE_EXECUTEDE) CUpti_ActivityPartitionedGlobalCacheConfig executed; Partitioned global caching actually used during kernel execution.


-
enumerator KERNEL_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds18KERNEL_FIELD_STARTE) uint64_t start; Start timestamp for the kernel execution (in nanoseconds).

A value of 0 indicates timestamp couldn’t be collected.


-
enumerator KERNEL_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds16KERNEL_FIELD_ENDE) uint64_t end; End timestamp for the kernel execution (in nanoseconds).

A value of 0 indicates timestamp couldn’t be collected.


-
enumerator KERNEL_FIELD_COMPLETED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds22KERNEL_FIELD_COMPLETEDE) uint64_t completed; Completion timestamp for the kernel execution, including all child kernels (in nanoseconds).

CUPTI_TIMESTAMP_UNKNOWN if unknown.


-
enumerator KERNEL_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds22KERNEL_FIELD_DEVICE_IDE) uint32_t deviceId; ID of the device where the kernel is executing.


-
enumerator KERNEL_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds23KERNEL_FIELD_CONTEXT_IDE) uint64_t contextId; ID of the context where the kernel is executing.


-
enumerator KERNEL_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds22KERNEL_FIELD_STREAM_IDE) uint64_t streamId; ID of the stream where the kernel is executing.


-
enumerator KERNEL_FIELD_GRID_X
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds19KERNEL_FIELD_GRID_XE) int32_t gridX; X-dimension of the grid size for the kernel.


-
enumerator KERNEL_FIELD_GRID_Y
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds19KERNEL_FIELD_GRID_YE) int32_t gridY; Y-dimension of the grid size for the kernel.


-
enumerator KERNEL_FIELD_GRID_Z
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds19KERNEL_FIELD_GRID_ZE) int32_t gridZ; Z-dimension of the grid size for the kernel.


-
enumerator KERNEL_FIELD_BLOCK_X
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds20KERNEL_FIELD_BLOCK_XE) int32_t blockX; X-dimension of the block size for the kernel.


-
enumerator KERNEL_FIELD_BLOCK_Y
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds20KERNEL_FIELD_BLOCK_YE) int32_t blockY; Y-dimension of the block size for the kernel.


-
enumerator KERNEL_FIELD_BLOCK_Z
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds20KERNEL_FIELD_BLOCK_ZE) int32_t blockZ; Z-dimension of the block size for the kernel.


-
enumerator KERNEL_FIELD_STATIC_SHARED_MEMORY
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds33KERNEL_FIELD_STATIC_SHARED_MEMORYE) int32_t staticSharedMemory; Amount of static shared memory allocated for the kernel, in bytes.


-
enumerator KERNEL_FIELD_DYNAMIC_SHARED_MEMORY
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds34KERNEL_FIELD_DYNAMIC_SHARED_MEMORYE) int32_t dynamicSharedMemory; Amount of dynamic shared memory reserved for the kernel, in bytes.


-
enumerator KERNEL_FIELD_LOCAL_MEMORY_PER_THREAD
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds36KERNEL_FIELD_LOCAL_MEMORY_PER_THREADE) uint32_t localMemoryPerThread; Amount of local memory reserved per thread, in bytes.


-
enumerator KERNEL_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds27KERNEL_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID of the kernel, Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator KERNEL_FIELD_GRID_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds20KERNEL_FIELD_GRID_IDE) int64_t gridId; Unique grid ID assigned to the kernel at runtime.


-
enumerator KERNEL_FIELD_NAME
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds17KERNEL_FIELD_NAMEE) const char* name; Name of the kernel.

Shared across all activity records for the same kernel.


-
enumerator KERNEL_FIELD_QUEUED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds19KERNEL_FIELD_QUEUEDE) uint64_t queued; Timestamp when the kernel was queued in the command buffer (in nanoseconds).

CUPTI_TIMESTAMP_UNKNOWN if not collected.


-
enumerator KERNEL_FIELD_SUBMITTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds22KERNEL_FIELD_SUBMITTEDE) uint64_t submitted; Timestamp when the command buffer containing the kernel launch was submitted to the GPU (in nanoseconds).

CUPTI_TIMESTAMP_UNKNOWN if not collected.


-
enumerator KERNEL_FIELD_LAUNCH_TYPE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds24KERNEL_FIELD_LAUNCH_TYPEE) uint8_t launchType; Indicates if the kernel was executed via a regular launch or a cooperative launch.

See CUpti_ActivityLaunchType.


-
enumerator KERNEL_FIELD_IS_SHARED_MEMORY_CARVEOUT_REQUESTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds48KERNEL_FIELD_IS_SHARED_MEMORY_CARVEOUT_REQUESTEDE) uint8_t isSharedMemoryCarveoutRequested; Indicates if CU_FUNC_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT was updated for the kernel launch.


-
enumerator KERNEL_FIELD_SHARED_MEMORY_CARVEOUT_REQUESTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds45KERNEL_FIELD_SHARED_MEMORY_CARVEOUT_REQUESTEDE) uint8_t sharedMemoryCarveoutRequested; Shared memory carveout value requested for the function, as a percentage of the total resource.


-
enumerator KERNEL_FIELD_SHARED_MEMORY_EXECUTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds35KERNEL_FIELD_SHARED_MEMORY_EXECUTEDE) uint32_t sharedMemoryExecuted; Shared memory size set by the driver, in bytes.


-
enumerator KERNEL_FIELD_GRAPH_NODE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds26KERNEL_FIELD_GRAPH_NODE_IDE) uint64_t graphNodeId; Unique ID of the graph node that launched this kernel through graph launch APIs.

0 if not launched through graph APIs.


-
enumerator KERNEL_FIELD_SHMEM_LIMIT_CONFIG
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds31KERNEL_FIELD_SHMEM_LIMIT_CONFIGE) CUpti_FuncShmemLimitConfig shmemLimitConfig; Shared memory limit configuration for the kernel, indicating if a higher per-block dynamic shared memory limit was opted.


-
enumerator KERNEL_FIELD_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds21KERNEL_FIELD_GRAPH_IDE) uint32_t graphId; Unique ID of the graph that launched this kernel through graph launch APIs.

0 if not launched through graph APIs.


-
enumerator KERNEL_FIELD_ACCESS_POLICY_WINDOW
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds33KERNEL_FIELD_ACCESS_POLICY_WINDOWE) CUaccessPolicyWindow* pAccessPolicyWindow; Pointer to the access policy window structure.

Defined in cuda.h.


-
enumerator KERNEL_FIELD_CHANNEL_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds23KERNEL_FIELD_CHANNEL_IDE) uint32_t channelID; ID of the hardware channel on which the kernel is launched.


-
enumerator KERNEL_FIELD_CHANNEL_TYPE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds25KERNEL_FIELD_CHANNEL_TYPEE) CUpti_ChannelType channelType; Type of the channel used for kernel launch.


-
enumerator KERNEL_FIELD_CLUSTER_X
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds22KERNEL_FIELD_CLUSTER_XE) int32_t clusterX; X-dimension of the cluster size for the kernel.

Valid for devices with compute capability 9.0 and higher.


-
enumerator KERNEL_FIELD_CLUSTER_Y
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds22KERNEL_FIELD_CLUSTER_YE) int32_t clusterY; Y-dimension of the cluster size for the kernel.

Valid for devices with compute capability 9.0 and higher.


-
enumerator KERNEL_FIELD_CLUSTER_Z
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds22KERNEL_FIELD_CLUSTER_ZE) int32_t clusterZ; Z-dimension of the cluster size for the kernel.

Valid for devices with compute capability 9.0 and higher.


-
enumerator KERNEL_FIELD_CLUSTER_SCHEDULING_POLICY
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds38KERNEL_FIELD_CLUSTER_SCHEDULING_POLICYE) uint32_t clusterSchedulingPolicy; Cluster scheduling policy for the kernel.

Refer to CUclusterSchedulingPolicy. Valid for devices with compute capability 9.0 and higher.


-
enumerator KERNEL_FIELD_LOCAL_MEMORY_TOTAL
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds31KERNEL_FIELD_LOCAL_MEMORY_TOTALE) uint64_t localMemoryTotal_v2; Total amount of local memory reserved for the kernel, in bytes.


-
enumerator KERNEL_FIELD_MAX_POTENTIAL_CLUSTER_SIZE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds39KERNEL_FIELD_MAX_POTENTIAL_CLUSTER_SIZEE) uint32_t maxPotentialClusterSize; Maximum cluster size for the kernel.


-
enumerator KERNEL_FIELD_MAX_ACTIVE_CLUSTERS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds32KERNEL_FIELD_MAX_ACTIVE_CLUSTERSE) uint32_t maxActiveClusters; Maximum number of clusters that could co-exist on the target device for the kernel.


-
enumerator KERNEL_FIELD_IS_DEVICE_LAUNCHED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds31KERNEL_FIELD_IS_DEVICE_LAUNCHEDE) uint8_t isDeviceLaunched; This field is set to 1 if the kernel is part of a device launched graph.


-
enumerator KERNEL_FIELD_LAUNCH_PRIORITY
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds28KERNEL_FIELD_LAUNCH_PRIORITYE) int32_t priority; The launch priority of the kernel.


-
enumerator KERNEL_FIELD_EXECUTION_MODEL
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds28KERNEL_FIELD_EXECUTION_MODELE) uint32_t executionModel; The execution model of the kernel function.

See also

[CUpti_FuncExecutionModel](https://docs.nvidia.com#group__cupti__activity__api_1gaf6d8c1b48d630571b8c2551d8e1f8c5a)for possible values.

-
enumerator KERNEL_FIELD_SOURCE_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds28KERNEL_FIELD_SOURCE_GRAPH_IDE) uint32_t sourceGraphId; The unique graph ID of the node from which the kernel node was instantiated or last updated.

This field will be 0 if the kernel is not launched through graph launch APIs.


-
enumerator KERNEL_FIELD_SOURCE_GRAPH_NODE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds33KERNEL_FIELD_SOURCE_GRAPH_NODE_IDE) uint64_t sourceGraphNodeId; The unique graph node ID of the node from which the kernel node was instantiated or last updated.

This field will be 0 if the kernel is not launched through graph launch APIs.


-
enumerator KERNEL_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityKernelFieldIds16KERNEL_FIELD_MAXE) Total number of defined fields.


-
enumerator KERNEL_FIELD_KIND

-
enum CUpti_ActivityKind
[#](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind) The kinds of activity records.

Each activity record kind represents information about a GPU or an activity occurring on a CPU or GPU. Each kind is associated with a activity record structure that holds the information associated with the kind.

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

See also

*Values:*-
enumerator CUPTI_ACTIVITY_KIND_INVALID
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind27CUPTI_ACTIVITY_KIND_INVALIDE) The activity record is invalid.


-
enumerator CUPTI_ACTIVITY_KIND_MEMCPY
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_MEMCPYE) A host<->host, host<->device, or device<->device memory copy.

For peer to peer memory copy, use the kind CUPTI_ACTIVITY_KIND_MEMCPY2. The corresponding activity record structure is

[CUpti_ActivityMemcpy7](https://docs.nvidia.com/structCUpti__ActivityMemcpy7.html#structcupti__activitymemcpy7).

-
enumerator CUPTI_ACTIVITY_KIND_MEMSET
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_MEMSETE) A memory set executing on the GPU.

The corresponding activity record structure is

[CUpti_ActivityMemset5](https://docs.nvidia.com/structCUpti__ActivityMemset5.html#structcupti__activitymemset5).

-
enumerator CUPTI_ACTIVITY_KIND_KERNEL
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_KERNELE) A kernel executing on the GPU.

This activity kind may significantly change the overall performance characteristics of the application because all kernel executions are serialized on the GPU. Other activity kind for kernel CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL doesn’t break kernel concurrency. The corresponding activity record structure is

[CUpti_ActivityKernel13](https://docs.nvidia.com/structCUpti__ActivityKernel13.html#structcupti__activitykernel13)

-
enumerator CUPTI_ACTIVITY_KIND_DRIVER
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_DRIVERE) A CUDA driver API function execution.

The corresponding activity record structure is

[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi).

-
enumerator CUPTI_ACTIVITY_KIND_RUNTIME
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind27CUPTI_ACTIVITY_KIND_RUNTIMEE) A CUDA runtime API function execution.

The corresponding activity record structure is

[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi).

-
enumerator CUPTI_ACTIVITY_KIND_EVENT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind25CUPTI_ACTIVITY_KIND_EVENTE) A performance counter (aka event) value.

The corresponding activity record structure is

[CUpti_ActivityEvent](https://docs.nvidia.com/structCUpti__ActivityEvent.html#structcupti__activityevent). This activity cannot be directly enabled or disabled. Information collected using the Event API. can be stored in the corresponding activity record. Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used.

-
enumerator CUPTI_ACTIVITY_KIND_METRIC
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_METRICE) A performance metric value.

The corresponding activity record structure is

[CUpti_ActivityMetric](https://docs.nvidia.com/structCUpti__ActivityMetric.html#structcupti__activitymetric). This activity cannot be directly enabled or disabled. Information collected using the Metric API. can be stored in the corresponding activity record. Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used.

-
enumerator CUPTI_ACTIVITY_KIND_DEVICE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_DEVICEE) Information about a CUDA device.

The corresponding activity record structure is

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6).

-
enumerator CUPTI_ACTIVITY_KIND_CONTEXT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind27CUPTI_ACTIVITY_KIND_CONTEXTE) Information about a CUDA context.

The corresponding activity record structure is

[CUpti_ActivityContext4](https://docs.nvidia.com/structCUpti__ActivityContext4.html#structcupti__activitycontext4).

-
enumerator CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind37CUPTI_ACTIVITY_KIND_CONCURRENT_KERNELE) A kernel executing on the GPU.

This activity kind doesn’t break kernel concurrency. The corresponding activity record structure is

[CUpti_ActivityKernel13](https://docs.nvidia.com/structCUpti__ActivityKernel13.html#structcupti__activitykernel13).

-
enumerator CUPTI_ACTIVITY_KIND_NAME
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind24CUPTI_ACTIVITY_KIND_NAMEE) Resource naming done via NVTX APIs for thread, device, context, etc.

The corresponding activity record structure is

[CUpti_ActivityName](https://docs.nvidia.com/structCUpti__ActivityName.html#structcupti__activityname).

-
enumerator CUPTI_ACTIVITY_KIND_MARKER
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_MARKERE) Instantaneous, start, or end NVTX marker.

The corresponding activity record structure is

[CUpti_ActivityMarker2](https://docs.nvidia.com/structCUpti__ActivityMarker2.html#structcupti__activitymarker2).

-
enumerator CUPTI_ACTIVITY_KIND_MARKER_DATA
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind31CUPTI_ACTIVITY_KIND_MARKER_DATAE) Extended, optional, data about a NVTX marker.

User must enable CUPTI_ACTIVITY_KIND_MARKER as well to get records for marker data. The corresponding activity record structure is

[CUpti_ActivityMarkerData2](https://docs.nvidia.com/structCUpti__ActivityMarkerData2.html#structcupti__activitymarkerdata2).

-
enumerator CUPTI_ACTIVITY_KIND_SOURCE_LOCATOR
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind34CUPTI_ACTIVITY_KIND_SOURCE_LOCATORE) Source information about source level result.

The corresponding activity record structure is

[CUpti_ActivitySourceLocator](https://docs.nvidia.com/structCUpti__ActivitySourceLocator.html#structcupti__activitysourcelocator). Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used. Enabling it will return the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED. Instead, use the SASS Metric APIs from the cupti_sass_metrics.h header.

-
enumerator CUPTI_ACTIVITY_KIND_GLOBAL_ACCESS
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind33CUPTI_ACTIVITY_KIND_GLOBAL_ACCESSE) Results for source-level global access.

The corresponding activity record structure is

[CUpti_ActivityGlobalAccess3](https://docs.nvidia.com/structCUpti__ActivityGlobalAccess3.html#structcupti__activityglobalaccess3). Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used. Enabling it will return the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED. Instead, use the SASS Metric APIs from the cupti_sass_metrics.h header.

-
enumerator CUPTI_ACTIVITY_KIND_BRANCH
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_BRANCHE) Results for source-level branch.

The corresponding activity record structure is

[CUpti_ActivityBranch2](https://docs.nvidia.com/structCUpti__ActivityBranch2.html#structcupti__activitybranch2). Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used. Enabling it will return the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED. Instead, use the SASS Metric APIs from the cupti_sass_metrics.h header.

-
enumerator CUPTI_ACTIVITY_KIND_OVERHEAD
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind28CUPTI_ACTIVITY_KIND_OVERHEADE) Overhead added by CUPTI, Compiler, CUDA driver etc.

The corresponding activity record structure is

[CUpti_ActivityOverhead3](https://docs.nvidia.com/structCUpti__ActivityOverhead3.html#structcupti__activityoverhead3).

-
enumerator CUPTI_ACTIVITY_KIND_CDP_KERNEL
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind30CUPTI_ACTIVITY_KIND_CDP_KERNELE) A CDP (CUDA Dynamic Parallel) kernel executing on the GPU.

The corresponding activity record structure is

[CUpti_ActivityCdpKernel](https://docs.nvidia.com/structCUpti__ActivityCdpKernel.html#structcupti__activitycdpkernel). This activity cannot be directly enabled or disabled. It is enabled and disabled through concurrent kernel activity i.e. _CONCURRENT_KERNEL.

-
enumerator CUPTI_ACTIVITY_KIND_PREEMPTION
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind30CUPTI_ACTIVITY_KIND_PREEMPTIONE) Preemption activity record indicating a preemption of a CDP (CUDA Dynamic Parallel) kernel executing on the GPU.

The corresponding activity record structure is

[CUpti_ActivityPreemption](https://docs.nvidia.com/structCUpti__ActivityPreemption.html#structcupti__activitypreemption).

-
enumerator CUPTI_ACTIVITY_KIND_ENVIRONMENT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind31CUPTI_ACTIVITY_KIND_ENVIRONMENTE) Environment activity records indicating power, clock, thermal, etc.

levels of the GPU. The corresponding activity record structure is

[CUpti_ActivityEnvironment](https://docs.nvidia.com/structCUpti__ActivityEnvironment.html#structcupti__activityenvironment).

-
enumerator CUPTI_ACTIVITY_KIND_EVENT_INSTANCE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind34CUPTI_ACTIVITY_KIND_EVENT_INSTANCEE) An performance counter value associated with a specific event domain instance.

The corresponding activity record structure is

[CUpti_ActivityEventInstance](https://docs.nvidia.com/structCUpti__ActivityEventInstance.html#structcupti__activityeventinstance). This activity cannot be directly enabled or disabled. Information collected using the Event API. can be stored in the corresponding activity record. Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used.

-
enumerator CUPTI_ACTIVITY_KIND_MEMCPY2
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind27CUPTI_ACTIVITY_KIND_MEMCPY2E) A peer to peer memory copy.

The corresponding activity record structure is

[CUpti_ActivityMemcpyPtoP4](https://docs.nvidia.com/structCUpti__ActivityMemcpyPtoP4.html#structcupti__activitymemcpyptop4).

-
enumerator CUPTI_ACTIVITY_KIND_METRIC_INSTANCE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind35CUPTI_ACTIVITY_KIND_METRIC_INSTANCEE) A performance metric value associated with a specific metric domain instance.

The corresponding activity record structure is

[CUpti_ActivityMetricInstance](https://docs.nvidia.com/structCUpti__ActivityMetricInstance.html#structcupti__activitymetricinstance). This activity cannot be directly enabled or disabled. Information collected using the Metric API. can be stored in the corresponding activity record. Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used.

-
enumerator CUPTI_ACTIVITY_KIND_INSTRUCTION_EXECUTION
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind41CUPTI_ACTIVITY_KIND_INSTRUCTION_EXECUTIONE) Results for source-level instruction execution.

The corresponding activity record structure is

[CUpti_ActivityInstructionExecution](https://docs.nvidia.com/structCUpti__ActivityInstructionExecution.html#structcupti__activityinstructionexecution). Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used. Enabling it will return the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED. Instead, use the SASS Metric APIs from the cupti_sass_metrics.h header.

-
enumerator CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTER
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind42CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTERE) Unified Memory counter record.

The corresponding activity record structure is

[CUpti_ActivityUnifiedMemoryCounter3](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounter3.html#structcupti__activityunifiedmemorycounter3).

-
enumerator CUPTI_ACTIVITY_KIND_FUNCTION
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind28CUPTI_ACTIVITY_KIND_FUNCTIONE) Device global/function record.

The corresponding activity record structure is

[CUpti_ActivityFunction](https://docs.nvidia.com/structCUpti__ActivityFunction.html#structcupti__activityfunction).

-
enumerator CUPTI_ACTIVITY_KIND_MODULE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_MODULEE) CUDA Module record.

The corresponding activity record structure is

[CUpti_ActivityModule](https://docs.nvidia.com/structCUpti__ActivityModule.html#structcupti__activitymodule). This activity cannot be directly enabled or disabled. Information collected using the module callback can be be stored in the corresponding activity record.

-
enumerator CUPTI_ACTIVITY_KIND_DEVICE_ATTRIBUTE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind36CUPTI_ACTIVITY_KIND_DEVICE_ATTRIBUTEE) A device attribute value.

The corresponding activity record structure is

[CUpti_ActivityDeviceAttribute](https://docs.nvidia.com/structCUpti__ActivityDeviceAttribute.html#structcupti__activitydeviceattribute). This activity cannot be directly enabled or disabled. Information collected using attributes CUpti_DeviceAttribute or CUdevice_attribute can be stored in the corresponding activity record.

-
enumerator CUPTI_ACTIVITY_KIND_SHARED_ACCESS
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind33CUPTI_ACTIVITY_KIND_SHARED_ACCESSE) Results for source-level shared access.

The corresponding activity record structure is

[CUpti_ActivitySharedAccess](https://docs.nvidia.com/structCUpti__ActivitySharedAccess.html#structcupti__activitysharedaccess). Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used. Enabling it will return the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED. Instead, use the SASS Metric APIs from the cupti_sass_metrics.h header.

-
enumerator CUPTI_ACTIVITY_KIND_PC_SAMPLING
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind31CUPTI_ACTIVITY_KIND_PC_SAMPLINGE) PC sampling information for kernels.

This will serialize kernels. The corresponding activity record structure is

[CUpti_ActivityPCSampling3](https://docs.nvidia.com/structCUpti__ActivityPCSampling3.html#structcupti__activitypcsampling3). Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used. Enabling it will return the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED. Instead, use the PC Sampling API from the cupti_pcsampling.h header, which allows concurrent kernel execution.

-
enumerator CUPTI_ACTIVITY_KIND_PC_SAMPLING_RECORD_INFO
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind43CUPTI_ACTIVITY_KIND_PC_SAMPLING_RECORD_INFOE) Summary information about PC sampling records.

The corresponding activity record structure is

[CUpti_ActivityPCSamplingRecordInfo](https://docs.nvidia.com/structCUpti__ActivityPCSamplingRecordInfo.html#structcupti__activitypcsamplingrecordinfo). Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used. Enabling it will return the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED. Instead, use the PC Sampling API from the cupti_pcsampling.h header.

-
enumerator CUPTI_ACTIVITY_KIND_INSTRUCTION_CORRELATION
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind43CUPTI_ACTIVITY_KIND_INSTRUCTION_CORRELATIONE) SASS/Source line-by-line correlation record.

This will generate sass/source correlation for functions that have source level analysis or pc sampling results. The records will be generated only when either of source level analysis or pc sampling activity is enabled. The corresponding activity record structure is

[CUpti_ActivityInstructionCorrelation](https://docs.nvidia.com/structCUpti__ActivityInstructionCorrelation.html#structcupti__activityinstructioncorrelation). Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used. Enabling it will return the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED. Instead, use the SASS Metric APIs from the cupti_sass_metrics.h header.

-
enumerator CUPTI_ACTIVITY_KIND_OPENACC_DATA
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind32CUPTI_ACTIVITY_KIND_OPENACC_DATAE) OpenACC data events.

The corresponding activity record structure is

[CUpti_ActivityOpenAccData](https://docs.nvidia.com/structCUpti__ActivityOpenAccData.html#structcupti__activityopenaccdata).

-
enumerator CUPTI_ACTIVITY_KIND_OPENACC_LAUNCH
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind34CUPTI_ACTIVITY_KIND_OPENACC_LAUNCHE) OpenACC launch events.

The corresponding activity record structure is

[CUpti_ActivityOpenAccLaunch](https://docs.nvidia.com/structCUpti__ActivityOpenAccLaunch.html#structcupti__activityopenacclaunch).

-
enumerator CUPTI_ACTIVITY_KIND_OPENACC_OTHER
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind33CUPTI_ACTIVITY_KIND_OPENACC_OTHERE) OpenACC other events.

The corresponding activity record structure is

[CUpti_ActivityOpenAccOther](https://docs.nvidia.com/structCUpti__ActivityOpenAccOther.html#structcupti__activityopenaccother).

-
enumerator CUPTI_ACTIVITY_KIND_CUDA_EVENT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind30CUPTI_ACTIVITY_KIND_CUDA_EVENTE) Information about a CUDA event (cudaEvent).

The corresponding activity record structure is

[CUpti_ActivityCudaEvent2](https://docs.nvidia.com/structCUpti__ActivityCudaEvent2.html#structcupti__activitycudaevent2).

-
enumerator CUPTI_ACTIVITY_KIND_STREAM
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_STREAME) Information about a CUDA stream.

The corresponding activity record structure is

[CUpti_ActivityStream](https://docs.nvidia.com/structCUpti__ActivityStream.html#structcupti__activitystream).

-
enumerator CUPTI_ACTIVITY_KIND_SYNCHRONIZATION
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind35CUPTI_ACTIVITY_KIND_SYNCHRONIZATIONE) Records for CUDA synchronization primitives.

The corresponding activity record structure is

[CUpti_ActivitySynchronization2](https://docs.nvidia.com/structCUpti__ActivitySynchronization2.html#structcupti__activitysynchronization2).

-
enumerator CUPTI_ACTIVITY_KIND_EXTERNAL_CORRELATION
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind40CUPTI_ACTIVITY_KIND_EXTERNAL_CORRELATIONE) Records for correlation of different programming APIs.

The corresponding activity record structure is

[CUpti_ActivityExternalCorrelation](https://docs.nvidia.com/structCUpti__ActivityExternalCorrelation.html#structcupti__activityexternalcorrelation).

-
enumerator CUPTI_ACTIVITY_KIND_NVLINK
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_NVLINKE) NVLink topology information.

The corresponding activity record structure is

[CUpti_ActivityNvLink5](https://docs.nvidia.com/structCUpti__ActivityNvLink5.html#structcupti__activitynvlink5).

-
enumerator CUPTI_ACTIVITY_KIND_INSTANTANEOUS_EVENT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind39CUPTI_ACTIVITY_KIND_INSTANTANEOUS_EVENTE) Instantaneous Event information.

The corresponding activity record structure is

[CUpti_ActivityInstantaneousEvent](https://docs.nvidia.com/structCUpti__ActivityInstantaneousEvent.html#structcupti__activityinstantaneousevent). This activity can not be directly enabled or disabled. Information collected using the Event API can be stored in the corresponding activity record. Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used.

-
enumerator CUPTI_ACTIVITY_KIND_INSTANTANEOUS_EVENT_INSTANCE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind48CUPTI_ACTIVITY_KIND_INSTANTANEOUS_EVENT_INSTANCEE) Instantaneous Event information for a specific event domain instance.

The corresponding activity record structure is

[CUpti_ActivityInstantaneousEventInstance](https://docs.nvidia.com/structCUpti__ActivityInstantaneousEventInstance.html#structcupti__activityinstantaneouseventinstance). This activity can not be directly enabled or disabled. Information collected using the Event API can be stored in the corresponding activity record. Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used.

-
enumerator CUPTI_ACTIVITY_KIND_INSTANTANEOUS_METRIC
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind40CUPTI_ACTIVITY_KIND_INSTANTANEOUS_METRICE) Instantaneous Metric information The corresponding activity record structure is

[CUpti_ActivityInstantaneousMetric](https://docs.nvidia.com/structCUpti__ActivityInstantaneousMetric.html#structcupti__activityinstantaneousmetric).This activity cannot be directly enabled or disabled. Information collected using the Metric API can be stored in the corresponding activity record. Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used.


-
enumerator CUPTI_ACTIVITY_KIND_INSTANTANEOUS_METRIC_INSTANCE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind49CUPTI_ACTIVITY_KIND_INSTANTANEOUS_METRIC_INSTANCEE) Instantaneous Metric information for a specific metric domain instance.

The corresponding activity record structure is

[CUpti_ActivityInstantaneousMetricInstance](https://docs.nvidia.com/structCUpti__ActivityInstantaneousMetricInstance.html#structcupti__activityinstantaneousmetricinstance). This activity cannot be directly enabled or disabled. Information collected using the Metric API can be stored in the corresponding activity record. Starting with the CUDA 13.0 release, this enum is unsupported and should no longer be used.

-
enumerator CUPTI_ACTIVITY_KIND_MEMORY
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_MEMORYE) Memory activity tracking allocation and freeing of the memory The corresponding activity record structure is

[CUpti_ActivityMemory](https://docs.nvidia.com/structCUpti__ActivityMemory.html#structcupti__activitymemory).

-
enumerator CUPTI_ACTIVITY_KIND_PCIE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind24CUPTI_ACTIVITY_KIND_PCIEE) PCI devices information used for PCI topology.

The corresponding activity record structure is

[CUpti_ActivityPcie](https://docs.nvidia.com/structCUpti__ActivityPcie.html#structcupti__activitypcie).

-
enumerator CUPTI_ACTIVITY_KIND_OPENMP
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind26CUPTI_ACTIVITY_KIND_OPENMPE) OpenMP parallel events.

The corresponding activity record structure is

[CUpti_ActivityOpenMp](https://docs.nvidia.com/structCUpti__ActivityOpenMp.html#structcupti__activityopenmp).

-
enumerator CUPTI_ACTIVITY_KIND_INTERNAL_LAUNCH_API
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind39CUPTI_ACTIVITY_KIND_INTERNAL_LAUNCH_APIE) A CUDA driver kernel launch occurring outside of any public API function execution.

Tools can handle these like records for driver API launch functions, although the cbid field is not used here. The corresponding activity record structure is

[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi).

-
enumerator CUPTI_ACTIVITY_KIND_MEMORY2
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind27CUPTI_ACTIVITY_KIND_MEMORY2E) Memory activity tracking allocation and freeing of the memory The corresponding activity record structure is

[CUpti_ActivityMemory4](https://docs.nvidia.com/structCUpti__ActivityMemory4.html#structcupti__activitymemory4).

-
enumerator CUPTI_ACTIVITY_KIND_MEMORY_POOL
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind31CUPTI_ACTIVITY_KIND_MEMORY_POOLE) Memory pool activity tracking creation, destruction and trimming of the memory pool.

The corresponding activity record structure is

[CUpti_ActivityMemoryPool3](https://docs.nvidia.com/structCUpti__ActivityMemoryPool3.html#structcupti__activitymemorypool3).

-
enumerator CUPTI_ACTIVITY_KIND_GRAPH_TRACE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind31CUPTI_ACTIVITY_KIND_GRAPH_TRACEE) Activity record for graph-level information.

The corresponding activity record structure is

[CUpti_ActivityGraphTrace2](https://docs.nvidia.com/structCUpti__ActivityGraphTrace2.html#structcupti__activitygraphtrace2).

-
enumerator CUPTI_ACTIVITY_KIND_JIT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind23CUPTI_ACTIVITY_KIND_JITE) JIT (Just-in-time) operation tracking.

The corresponding activity record structure is

[CUpti_ActivityJit2](https://docs.nvidia.com/structCUpti__ActivityJit2.html#structcupti__activityjit2).

-
enumerator CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind38CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACEE) This activity can not be directly enabled or disabled when using predefined records.

It is enabled when CUPTI_ACTIVITY_KIND_GRAPH_TRACE is enabled and device graph trace is enabled through API

[cuptiActivityEnableDeviceGraph()](https://docs.nvidia.com#group__cupti__activity__api_1ga21718968b8e42071354e703eda63a000). For user defined activity records, this activity kind must be explicitly enabled through API[cuptiActivityEnable_v2()](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)The corresponding activity record structure is[CUpti_ActivityDeviceGraphTrace](https://docs.nvidia.com/structCUpti__ActivityDeviceGraphTrace.html#structcupti__activitydevicegraphtrace).

-
enumerator CUPTI_ACTIVITY_KIND_MEM_DECOMPRESS
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind34CUPTI_ACTIVITY_KIND_MEM_DECOMPRESSE) Tracing batches of copies that are to be decompressed.

The corresponding activity record structure is

[CUpti_ActivityMemDecompress](https://docs.nvidia.com/structCUpti__ActivityMemDecompress.html#structcupti__activitymemdecompress).

-
enumerator CUPTI_ACTIVITY_KIND_CONFIDENTIAL_COMPUTE_ROTATION
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind49CUPTI_ACTIVITY_KIND_CONFIDENTIAL_COMPUTE_ROTATIONE) Tracing new overheads introduced on some hardware due when confidential computing is enabled.

The corresponding activity record structure is

[CUpti_ActivityConfidentialComputeRotation](https://docs.nvidia.com/structCUpti__ActivityConfidentialComputeRotation.html#structcupti__activityconfidentialcomputerotation).

-
enumerator CUPTI_ACTIVITY_KIND_GRAPH_HOST_NODE
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind35CUPTI_ACTIVITY_KIND_GRAPH_HOST_NODEE) Tracing of host execution nodes of the CUDA graph, i.e.

nodes of type CU_GRAPH_NODE_TYPE_HOST. The corresponding activity record structure is CUpti_ActivityGraphHostNode.


-
enumerator CUPTI_ACTIVITY_KIND_COMPUTE_ENGINE_CTX_SWITCH
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind45CUPTI_ACTIVITY_KIND_COMPUTE_ENGINE_CTX_SWITCHE) An activity denoting the switching of Compute Engine contexts in/out of the GPU.

The corresponding activity record structure is

[CUpti_ActivityComputeEngineCtxSwitch](https://docs.nvidia.com/structCUpti__ActivityComputeEngineCtxSwitch.html#structcupti__activitycomputeenginectxswitch).

-
enumerator CUPTI_ACTIVITY_KIND_HOST_LAUNCH
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind31CUPTI_ACTIVITY_KIND_HOST_LAUNCHE) An activity kind denoting the launch of a host function through cu(da)LaunchHostFunc API.

The corresponding activity record structure is

[CUpti_ActivityHostLaunch](https://docs.nvidia.com/structCUpti__ActivityHostLaunch.html#structcupti__activityhostlaunch).

-
enumerator CUPTI_ACTIVITY_KIND_GREEN_CONTEXT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind33CUPTI_ACTIVITY_KIND_GREEN_CONTEXTE) An activity kind denoting the allocation of a green context.

The corresponding activity record structure is

[CUpti_ActivityGreenContext3](https://docs.nvidia.com/structCUpti__ActivityGreenContext3.html#structcupti__activitygreencontext3).

-
enumerator CUPTI_ACTIVITY_KIND_COUNT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind25CUPTI_ACTIVITY_KIND_COUNTE) Count of supported activity kinds.


-
enumerator CUPTI_ACTIVITY_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityKind29CUPTI_ACTIVITY_KIND_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_KIND_INVALID

-
enum CUpti_ActivityLaunchType
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityLaunchType) The type of the CUDA kernel launch.

*Values:*-
enumerator CUPTI_ACTIVITY_LAUNCH_TYPE_REGULAR
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityLaunchType34CUPTI_ACTIVITY_LAUNCH_TYPE_REGULARE) The kernel was launched via a regular kernel call.


-
enumerator CUPTI_ACTIVITY_LAUNCH_TYPE_COOPERATIVE_SINGLE_DEVICE
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityLaunchType52CUPTI_ACTIVITY_LAUNCH_TYPE_COOPERATIVE_SINGLE_DEVICEE) The kernel was launched via API cudaLaunchCooperativeKernel() or cuLaunchCooperativeKernel()


-
enumerator CUPTI_ACTIVITY_LAUNCH_TYPE_COOPERATIVE_MULTI_DEVICE
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityLaunchType51CUPTI_ACTIVITY_LAUNCH_TYPE_COOPERATIVE_MULTI_DEVICEE) The kernel was launched via API cudaLaunchCooperativeKernelMultiDevice() or cuLaunchCooperativeKernelMultiDevice()


-
enumerator CUPTI_ACTIVITY_LAUNCH_TYPE_CBL_COMMANDLIST
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityLaunchType42CUPTI_ACTIVITY_LAUNCH_TYPE_CBL_COMMANDLISTE) The kernel was launched as a CBL commandlist.


-
enumerator CUPTI_ACTIVITY_LAUNCH_TYPE_REGULAR

-
enum CUpti_ActivityMarkerDataFieldIds
[#](https://docs.nvidia.com#_CPPv432CUpti_ActivityMarkerDataFieldIds) Enum identifiers for fields to trace detailed information for a marker.

User must enable CUPTI_ACTIVITY_KIND_MARKER as well to get records for marker data. These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_MARKER_DATA.

*Values:*-
enumerator MARKER_DATA_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds22MARKER_DATA_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_MARKER_DATA.


-
enumerator MARKER_DATA_FIELD_FLAGS
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds23MARKER_DATA_FIELD_FLAGSE) CUpti_ActivityFlag flags; Flags associated with the marker.


-
enumerator MARKER_DATA_FIELD_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds20MARKER_DATA_FIELD_IDE) uint32_t id; Marker ID.


-
enumerator MARKER_DATA_FIELD_PAYLOAD_KIND
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds30MARKER_DATA_FIELD_PAYLOAD_KINDE) CUpti_MetricValueKind payloadKind; Defines the payload format for the value associated with the marker.


-
enumerator MARKER_DATA_FIELD_PAYLOAD
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds25MARKER_DATA_FIELD_PAYLOADE) CUpti_MetricValue payload; The payload value.


-
enumerator MARKER_DATA_FIELD_COLOR
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds23MARKER_DATA_FIELD_COLORE) uint32_t color; The color for the marker.


-
enumerator MARKER_DATA_FIELD_CATEGORY
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds26MARKER_DATA_FIELD_CATEGORYE) uint32_t category; The category for the marker.


-
enumerator MARKER_DATA_FIELD_CUPTI_DOMAIN_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds33MARKER_DATA_FIELD_CUPTI_DOMAIN_IDE) uint32_t cuptiDomainId; CUPTI maintained domain id required for NVTX extended payloads.


-
enumerator MARKER_DATA_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMarkerDataFieldIds21MARKER_DATA_FIELD_MAXE) Total number of defined fields.


-
enumerator MARKER_DATA_FIELD_KIND

-
enum CUpti_ActivityMarkerFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityMarkerFieldIds) Enum identifiers for fields to trace NVTX markers/ranges.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_MARKER.

*Values:*-
enumerator MARKER_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds17MARKER_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_MARKER.


-
enumerator MARKER_FIELD_FLAGS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds18MARKER_FIELD_FLAGSE) CUpti_ActivityFlag flags; Flags associated with the marker.


-
enumerator MARKER_FIELD_TIMESTAMP
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds22MARKER_FIELD_TIMESTAMPE) uint64_t timestamp; Timestamp for the marker (in ns).


-
enumerator MARKER_FIELD_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds15MARKER_FIELD_IDE) uint32_t id; Marker ID.


-
enumerator MARKER_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds23MARKER_FIELD_PROCESS_IDE) uint32_t processId; The process ID of the process where the overhead is occurring.


-
enumerator MARKER_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds22MARKER_FIELD_THREAD_IDE) uint64_t threadId; The thread ID of the process where the overhead is occurring.


-
enumerator MARKER_FIELD_NAME
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds17MARKER_FIELD_NAMEE) const char *name; Marker name for an instantaneous or start marker.


-
enumerator MARKER_FIELD_DOMAIN
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds19MARKER_FIELD_DOMAINE) const char *domain; Name of the domain to which this marker belongs.


-
enumerator MARKER_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMarkerFieldIds16MARKER_FIELD_MAXE) Total number of defined fields.


-
enumerator MARKER_FIELD_KIND

-
enum CUpti_ActivityMemDecompressFieldIds
[#](https://docs.nvidia.com#_CPPv435CUpti_ActivityMemDecompressFieldIds) Enum identifiers for fields to trace decompression operations.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_MEM_DECOMPRESS.

*Values:*-
enumerator MEM_DECOMPRESS_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds25MEM_DECOMPRESS_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_MEM_DECOMPRESS.


-
enumerator MEM_DECOMPRESS_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds30MEM_DECOMPRESS_FIELD_DEVICE_IDE) uint32_t deviceId; The ID of the device where the decompression operation was recorded.


-
enumerator MEM_DECOMPRESS_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds31MEM_DECOMPRESS_FIELD_CONTEXT_IDE) uint32_t contextId; The ID of the context where the decompression operation was recorded.


-
enumerator MEM_DECOMPRESS_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds30MEM_DECOMPRESS_FIELD_STREAM_IDE) uint32_t streamId; The compute stream where the decompression operation was recorded.


-
enumerator MEM_DECOMPRESS_FIELD_CHANNEL_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds31MEM_DECOMPRESS_FIELD_CHANNEL_IDE) uint32_t channelId; The ID of the HW channel on which the decompression operation was recorded.


-
enumerator MEM_DECOMPRESS_FIELD_CHANNEL_TYPE
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds33MEM_DECOMPRESS_FIELD_CHANNEL_TYPEE) CUpti_ChannelType channelType; The type of the channel on which the decompression operation was recorded.


-
enumerator MEM_DECOMPRESS_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds35MEM_DECOMPRESS_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this decompression operation.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator MEM_DECOMPRESS_FIELD_NUMBER_OF_OPERATIONS
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds41MEM_DECOMPRESS_FIELD_NUMBER_OF_OPERATIONSE) uint32_t numberOfOperations; The number of decompression operations in this batch.


-
enumerator MEM_DECOMPRESS_FIELD_SOURCE_BYTES
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds33MEM_DECOMPRESS_FIELD_SOURCE_BYTESE) uint64_t sourceBytes; The total number of bytes to be read and decompressed in the batch operation.


-
enumerator MEM_DECOMPRESS_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds26MEM_DECOMPRESS_FIELD_STARTE) uint64_t start; Start timestamp of the decompression operation, in nanoseconds.


-
enumerator MEM_DECOMPRESS_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds24MEM_DECOMPRESS_FIELD_ENDE) uint64_t end; End timestamp of the decompression operation, in nanoseconds.


-
enumerator MEM_DECOMPRESS_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityMemDecompressFieldIds24MEM_DECOMPRESS_FIELD_MAXE) Total number of defined fields.


-
enumerator MEM_DECOMPRESS_FIELD_KIND

-
enum CUpti_ActivityMemcpy2FieldIds
[#](https://docs.nvidia.com#_CPPv429CUpti_ActivityMemcpy2FieldIds) Enum identifiers for fields to trace peer-to-peer memory copies.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_MEMCPY2.

*Values:*-
enumerator MEMCPY2_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds18MEMCPY2_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_MEMCPY2.


-
enumerator MEMCPY2_FIELD_COPY_KIND
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds23MEMCPY2_FIELD_COPY_KINDE) uint8_t copyKind; Type of memory copy.

ALways CUPTI_ACTIVITY_MEMCPY_KIND_P2P.

See also


-
enumerator MEMCPY2_FIELD_SRC_KIND
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds22MEMCPY2_FIELD_SRC_KINDE) uint8_t srcKind; Kind of source memory used in the copy.

See also


-
enumerator MEMCPY2_FIELD_DST_KIND
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds22MEMCPY2_FIELD_DST_KINDE) uint8_t dstKind; Kind of destination memory used in the copy.

See also


-
enumerator MEMCPY2_FIELD_FLAGS
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds19MEMCPY2_FIELD_FLAGSE) uint8_t flags; Flags associated with the memory copy.

See also


-
enumerator MEMCPY2_FIELD_BYTES
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds19MEMCPY2_FIELD_BYTESE) uint64_t bytes; Number of bytes transferred during the memory copy.


-
enumerator MEMCPY2_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds19MEMCPY2_FIELD_STARTE) uint64_t start; Start timestamp for the memory copy (in nanoseconds).

A value of 0 indicates timestamp couldn’t be collected.


-
enumerator MEMCPY2_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds17MEMCPY2_FIELD_ENDE) uint64_t end; End timestamp for the memory copy (in nanoseconds).

A value of 0 indicates timestamp couldn’t be collected.


-
enumerator MEMCPY2_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds23MEMCPY2_FIELD_DEVICE_IDE) uint32_t deviceId; Device where the memory copy is occurring.


-
enumerator MEMCPY2_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds24MEMCPY2_FIELD_CONTEXT_IDE) uint32_t contextId; CUDA context where the memory copy is occurring.


-
enumerator MEMCPY2_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds23MEMCPY2_FIELD_STREAM_IDE) uint32_t streamId; Stream in which the memory copy is occurring.


-
enumerator MEMCPY2_FIELD_SRC_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds27MEMCPY2_FIELD_SRC_DEVICE_IDE) uint32_t srcDeviceId; Device from which memory is being copied.


-
enumerator MEMCPY2_FIELD_SRC_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds28MEMCPY2_FIELD_SRC_CONTEXT_IDE) uint32_t srcContextId; CUDA context owning the source memory.


-
enumerator MEMCPY2_FIELD_DST_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds27MEMCPY2_FIELD_DST_DEVICE_IDE) uint32_t dstDeviceId; Device to which memory is being copied.


-
enumerator MEMCPY2_FIELD_DST_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds28MEMCPY2_FIELD_DST_CONTEXT_IDE) uint32_t dstContextId; CUDA context owning the destination memory.


-
enumerator MEMCPY2_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds28MEMCPY2_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this memory copy.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator MEMCPY2_FIELD_GRAPH_NODE_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds27MEMCPY2_FIELD_GRAPH_NODE_IDE) uint64_t graphNodeId; ID of the graph node that launched this memcpy.

0 if not launched via a CUDA Graph.


-
enumerator MEMCPY2_FIELD_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds22MEMCPY2_FIELD_GRAPH_IDE) uint32_t graphId; ID of the CUDA Graph associated with this memory copy.

0 if not launched via a CUDA Graph.


-
enumerator MEMCPY2_FIELD_CHANNEL_ID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds24MEMCPY2_FIELD_CHANNEL_IDE) uint32_t channelID; Hardware channel ID used for the memory copy.


-
enumerator MEMCPY2_FIELD_CHANNEL_TYPE
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds26MEMCPY2_FIELD_CHANNEL_TYPEE) CUpti_ChannelType channelType; Type of the hardware channel.


-
enumerator MEMCPY2_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityMemcpy2FieldIds17MEMCPY2_FIELD_MAXE) Total number of defined fields.


-
enumerator MEMCPY2_FIELD_KIND

-
enum CUpti_ActivityMemcpyFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityMemcpyFieldIds) Enum identifiers for fields to trace memory copies.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_MEMCPY.

*Values:*-
enumerator MEMCPY_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds17MEMCPY_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_MEMCPY.


-
enumerator MEMCPY_FIELD_COPY_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds22MEMCPY_FIELD_COPY_KINDE) uint8_t copyKind; Type of memory copy operation.

See also


-
enumerator MEMCPY_FIELD_SRC_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds21MEMCPY_FIELD_SRC_KINDE) uint8_t srcKind; Memory kind of the source location.

See also


-
enumerator MEMCPY_FIELD_DST_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds21MEMCPY_FIELD_DST_KINDE) uint8_t dstKind; Memory kind of the destination location.

See also


-
enumerator MEMCPY_FIELD_FLAGS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds18MEMCPY_FIELD_FLAGSE) uint8_t flags; Flags associated with the memory copy.

See also


-
enumerator MEMCPY_FIELD_BYTES
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds18MEMCPY_FIELD_BYTESE) uint64_t bytes; Number of bytes copied during the memory operation.


-
enumerator MEMCPY_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds18MEMCPY_FIELD_STARTE) uint64_t start; Start timestamp of the memory copy, in nanoseconds.

A value of 0 indicates timestamp couldn’t be collected.


-
enumerator MEMCPY_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds16MEMCPY_FIELD_ENDE) uint64_t end; End timestamp of the memory copy, in nanoseconds.

A value of 0 indicates timestamp couldn’t be collected.


-
enumerator MEMCPY_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds22MEMCPY_FIELD_DEVICE_IDE) uint32_t deviceId; ID of the device where the memory copy occurred.


-
enumerator MEMCPY_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds23MEMCPY_FIELD_CONTEXT_IDE) uint32_t contextId; ID of the CUDA context where the memory copy occurred.


-
enumerator MEMCPY_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds22MEMCPY_FIELD_STREAM_IDE) uint32_t streamId; ID of the stream where the memory copy occurred.


-
enumerator MEMCPY_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds27MEMCPY_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this memory copy.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator MEMCPY_FIELD_GRAPH_NODE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds26MEMCPY_FIELD_GRAPH_NODE_IDE) uint64_t graphNodeId; ID of the CUDA Graph node that launched this memory copy.

0 if not launched via a CUDA Graph.


-
enumerator MEMCPY_FIELD_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds21MEMCPY_FIELD_GRAPH_IDE) uint32_t graphId; ID of the CUDA Graph that launched this memory copy.

0 if not launched via a CUDA Graph.


-
enumerator MEMCPY_FIELD_CHANNEL_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds23MEMCPY_FIELD_CHANNEL_IDE) uint32_t channelID; ID of the hardware channel on which this memory copy was executed.


-
enumerator MEMCPY_FIELD_CHANNEL_TYPE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds25MEMCPY_FIELD_CHANNEL_TYPEE) CUpti_ChannelType channelType; Type of the hardware channel used.


-
enumerator MEMCPY_FIELD_IS_DEVICE_LAUNCHED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds31MEMCPY_FIELD_IS_DEVICE_LAUNCHEDE) uint8_t isDeviceLaunched; This field is set to 1 if the kernel is part of a device launched graph.


-
enumerator MEMCPY_FIELD_COPY_COUNT
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds23MEMCPY_FIELD_COPY_COUNTE) uint64_t copyCount; Number of individual memcpy operations traced in this record.

>1 if batched using MemcpyBatchAsync; otherwise 1.


-
enumerator MEMCPY_FIELD_SOURCE_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds28MEMCPY_FIELD_SOURCE_GRAPH_IDE) uint32_t sourceGraphId; The unique graph ID of the node from which the memcpy node was instantiated or last updated.

This field will be 0 if the memcpy is not launched through graph launch APIs.


-
enumerator MEMCPY_FIELD_SOURCE_GRAPH_NODE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds33MEMCPY_FIELD_SOURCE_GRAPH_NODE_IDE) uint64_t sourceGraphNodeId; The unique graph node ID of the node from which the memcpy node was instantiated or last updated.

This field will be 0 if the memcpy is not launched through graph launch APIs.


-
enumerator MEMCPY_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemcpyFieldIds16MEMCPY_FIELD_MAXE) Total number of defined fields.


-
enumerator MEMCPY_FIELD_KIND

-
enum CUpti_ActivityMemcpyKind
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityMemcpyKind) The kind of a memory copy, indicating the source and destination targets of the copy.

Each kind represents the source and destination targets of a memory copy. Targets are host, device, and array.

*Values:*-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind34CUPTI_ACTIVITY_MEMCPY_KIND_UNKNOWNE) The memory copy kind is not known.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_HTOD
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_HTODE) A host to device memory copy.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_DTOH
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_DTOHE) A device to host memory copy.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_HTOA
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_HTOAE) A host to device array memory copy.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_ATOH
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_ATOHE) A device array to host memory copy.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_ATOA
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_ATOAE) A device array to device array memory copy.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_ATOD
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_ATODE) A device array to device memory copy.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_DTOA
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_DTOAE) A device to device array memory copy.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_DTOD
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_DTODE) A device to device memory copy on the same device.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_HTOH
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_HTOHE) A host to host memory copy.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_PTOP
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind31CUPTI_ACTIVITY_MEMCPY_KIND_PTOPE) A peer to peer memory copy across different devices.


-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemcpyKind36CUPTI_ACTIVITY_MEMCPY_KIND_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_MEMCPY_KIND_UNKNOWN

-
enum CUpti_ActivityMemoryFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityMemoryFieldIds) Enum identifiers for fields to trace memory allocation and free operation.

This activity record provides separate records for memory allocation and memory release operations. This allows to correlate the corresponding driver and runtime API activity record with the memory operation.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_MEMORY2.

*Values:*-
enumerator MEMORY_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds17MEMORY_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_MEMORY2.


-
enumerator MEMORY_FIELD_OPERATION_TYPE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds27MEMORY_FIELD_OPERATION_TYPEE) CUpti_ActivityMemoryOperationType memoryOperationType; The memory operation requested by the user.


-
enumerator MEMORY_FIELD_MEMORY_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds24MEMORY_FIELD_MEMORY_KINDE) CUpti_ActivityMemoryKind memoryKind; The memory kind requested by the user.


-
enumerator MEMORY_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds27MEMORY_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID of the memory operation.


-
enumerator MEMORY_FIELD_ADDRESS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds20MEMORY_FIELD_ADDRESSE) uint64_t address; Virtual address of the allocation.


-
enumerator MEMORY_FIELD_BYTES
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds18MEMORY_FIELD_BYTESE) uint64_t bytes; Number of bytes of memory allocated.


-
enumerator MEMORY_FIELD_TIMESTAMP
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds22MEMORY_FIELD_TIMESTAMPE) uint64_t timestamp; Start timestamp for the memory operation (in ns).


-
enumerator MEMORY_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds23MEMORY_FIELD_PROCESS_IDE) uint32_t processId; ID of the process to which this record belongs.


-
enumerator MEMORY_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds22MEMORY_FIELD_DEVICE_IDE) uint32_t deviceId; ID of the device where the memory operation is taking place.


-
enumerator MEMORY_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds23MEMORY_FIELD_CONTEXT_IDE) uint32_t contextId; ID of the context.


-
enumerator MEMORY_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds22MEMORY_FIELD_STREAM_IDE) uint32_t streamId; ID of the stream.


-
enumerator MEMORY_FIELD_IS_ASYNC
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds21MEMORY_FIELD_IS_ASYNCE) uint32_t isAsync; Whether the memory operation happens through async memory APIs.


-
enumerator MEMORY_FIELD_POOL_TYPE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds22MEMORY_FIELD_POOL_TYPEE) CUpti_ActivityMemoryPoolType memoryPoolConfig.memoryPoolType; Type of the memory pool.


-
enumerator MEMORY_FIELD_POOL_ADDRESS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds25MEMORY_FIELD_POOL_ADDRESSE) uint64_t memoryPoolConfig.address; Base address of the memory pool.


-
enumerator MEMORY_FIELD_POOL_RELEASE_THRESHOLD
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds35MEMORY_FIELD_POOL_RELEASE_THRESHOLDE) uint64_t memoryPoolConfig.releaseThreshold; Release threshold of the memory pool in bytes.


-
enumerator MEMORY_FIELD_POOL_SIZE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds22MEMORY_FIELD_POOL_SIZEE) uint64_t memoryPoolConfig.pool.size; Size of memory pool in bytes.


-
enumerator MEMORY_FIELD_POOL_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds28MEMORY_FIELD_POOL_PROCESS_IDE) uint64_t memoryPoolConfig.pool.processId; Process ID of the memory pools.


-
enumerator MEMORY_FIELD_POOL_UTILIZED_SIZE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds31MEMORY_FIELD_POOL_UTILIZED_SIZEE) uint64_t memoryPoolConfig.utilizedSize; Utilized size of the memory pool.


-
enumerator MEMORY_FIELD_SOURCE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds19MEMORY_FIELD_SOURCEE) const char* source; Shared object or binary that the memory allocation request comes from.


-
enumerator MEMORY_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryFieldIds16MEMORY_FIELD_MAXE) Total number of defined fields.


-
enumerator MEMORY_FIELD_KIND

-
enum CUpti_ActivityMemoryKind
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityMemoryKind) The kinds of memory accessed by a memory operation/copy.

Each kind represents the type of the memory accessed by a memory operation/copy.

*Values:*-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind34CUPTI_ACTIVITY_MEMORY_KIND_UNKNOWNE) The memory kind is unknown.


-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_PAGEABLE
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind35CUPTI_ACTIVITY_MEMORY_KIND_PAGEABLEE) The memory is pageable.


-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_PINNED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind33CUPTI_ACTIVITY_MEMORY_KIND_PINNEDE) The memory is pinned.


-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_DEVICE
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind33CUPTI_ACTIVITY_MEMORY_KIND_DEVICEE) The memory is on the device.


-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_ARRAY
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind32CUPTI_ACTIVITY_MEMORY_KIND_ARRAYE) The memory is an array.


-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_MANAGED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind34CUPTI_ACTIVITY_MEMORY_KIND_MANAGEDE) The memory is managed.


-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_DEVICE_STATIC
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind40CUPTI_ACTIVITY_MEMORY_KIND_DEVICE_STATICE) The memory is device static.


-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_MANAGED_STATIC
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind41CUPTI_ACTIVITY_MEMORY_KIND_MANAGED_STATICE) The memory is managed static.


-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryKind36CUPTI_ACTIVITY_MEMORY_KIND_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_MEMORY_KIND_UNKNOWN

-
enum CUpti_ActivityMemoryOperationType
[#](https://docs.nvidia.com#_CPPv433CUpti_ActivityMemoryOperationType) Memory operation types.

Describes the type of memory operation, to be used with

[CUpti_ActivityMemory4](https://docs.nvidia.com/structCUpti__ActivityMemory4.html#structcupti__activitymemory4).*Values:*-
enumerator CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_INVALID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityMemoryOperationType44CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_INVALIDE) The operation is invalid.


-
enumerator CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_ALLOCATION
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityMemoryOperationType47CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_ALLOCATIONE) Memory is allocated.


-
enumerator CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_RELEASE
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityMemoryOperationType44CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_RELEASEE) Memory is released.


-
enumerator CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityMemoryOperationType46CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_MEMORY_OPERATION_TYPE_INVALID

-
enum CUpti_ActivityMemoryPoolFieldIds
[#](https://docs.nvidia.com#_CPPv432CUpti_ActivityMemoryPoolFieldIds) Enum identifiers for fields to trace CUDA memory pool creation, destruction and trimming.

This activity record provides separate records for memory pool creation, destruction and trimming operations. This allows to correlate the corresponding driver and runtime API activity record with the memory pool operation.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_MEMORY_POOL.

*Values:*-
enumerator MEMORY_POOL_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds22MEMORY_POOL_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_MEMORY_POOL.


-
enumerator MEMORY_POOL_FIELD_OPERATION_TYPE
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds32MEMORY_POOL_FIELD_OPERATION_TYPEE) CUpti_ActivityMemoryPoolOperationType memoryPoolOperationType; The memory operation requested by the user.


-
enumerator MEMORY_POOL_FIELD_POOL_TYPE
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds27MEMORY_POOL_FIELD_POOL_TYPEE) CUpti_ActivityMemoryPoolType memoryPoolType; The type of the memory pool.


-
enumerator MEMORY_POOL_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds32MEMORY_POOL_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this memory pool operation.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator MEMORY_POOL_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds28MEMORY_POOL_FIELD_PROCESS_IDE) uint32_t processId; ID of the process to which this record belongs.


-
enumerator MEMORY_POOL_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds27MEMORY_POOL_FIELD_DEVICE_IDE) uint32_t deviceId; ID of the device where the memory pool is created.


-
enumerator MEMORY_POOL_FIELD_MIN_BYTES_TO_KEEP
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds35MEMORY_POOL_FIELD_MIN_BYTES_TO_KEEPE) size_t minBytesToKeep; Minimum bytes to keep of the memory pool.


-
enumerator MEMORY_POOL_FIELD_ADDRESS
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds25MEMORY_POOL_FIELD_ADDRESSE) uint64_t address; Virtual address of the allocation.


-
enumerator MEMORY_POOL_FIELD_SIZE
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds22MEMORY_POOL_FIELD_SIZEE) uint64_t size; Size of the memory pool operation in bytes.


-
enumerator MEMORY_POOL_FIELD_RELEASE_THRESHOLD
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds35MEMORY_POOL_FIELD_RELEASE_THRESHOLDE) uint64_t releaseThreshold; Release threshold of the memory pool.


-
enumerator MEMORY_POOL_FIELD_TIMESTAMP
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds27MEMORY_POOL_FIELD_TIMESTAMPE) uint64_t timestamp; Start timestamp for the memory operation (in ns).


-
enumerator MEMORY_POOL_FIELD_UTILIZED_SIZE
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds31MEMORY_POOL_FIELD_UTILIZED_SIZEE) uint64_t utilizedSize; Utilized size of the memory pool.


-
enumerator MEMORY_POOL_FIELD_IS_MANAGED_POOL
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds33MEMORY_POOL_FIELD_IS_MANAGED_POOLE) uint8_t isManagedPool; Whether the pool is of managed memory allocation or pinned memory allocation.


-
enumerator MEMORY_POOL_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityMemoryPoolFieldIds21MEMORY_POOL_FIELD_MAXE) Total number of defined fields.


-
enumerator MEMORY_POOL_FIELD_KIND

-
enum CUpti_ActivityMemoryPoolOperationType
[#](https://docs.nvidia.com#_CPPv437CUpti_ActivityMemoryPoolOperationType) Memory pool operation types.

Describes the type of memory pool operation, to be used with

[CUpti_ActivityMemoryPool2](https://docs.nvidia.com/structCUpti__ActivityMemoryPool2.html#structcupti__activitymemorypool2).*Values:*-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_INVALID
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityMemoryPoolOperationType49CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_INVALIDE) The operation is invalid.


-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_CREATED
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityMemoryPoolOperationType49CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_CREATEDE) Memory pool is created.


-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_DESTROYED
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityMemoryPoolOperationType51CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_DESTROYEDE) Memory pool is destroyed.


-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_TRIMMED
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityMemoryPoolOperationType49CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_TRIMMEDE) Memory pool is trimmed.


-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityMemoryPoolOperationType51CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_INVALID

-
enum CUpti_ActivityMemoryPoolType
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityMemoryPoolType) Memory pool types.

Describes the type of memory pool, to be used with

[CUpti_ActivityMemory4](https://docs.nvidia.com/structCUpti__ActivityMemory4.html#structcupti__activitymemory4).*Values:*-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_TYPE_INVALID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryPoolType39CUPTI_ACTIVITY_MEMORY_POOL_TYPE_INVALIDE) The operation is invalid.


-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryPoolType37CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCALE) Memory pool is local to the process.


-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_TYPE_IMPORTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryPoolType40CUPTI_ACTIVITY_MEMORY_POOL_TYPE_IMPORTEDE) Memory pool is imported by the process.


-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemoryPoolType41CUPTI_ACTIVITY_MEMORY_POOL_TYPE_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_MEMORY_POOL_TYPE_INVALID

-
enum CUpti_ActivityMemsetFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityMemsetFieldIds) Enum identifiers for fields to trace memset operations.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_MEMSET.

*Values:*-
enumerator MEMSET_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds17MEMSET_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_MEMSET.


-
enumerator MEMSET_FIELD_VALUE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds18MEMSET_FIELD_VALUEE) uint32_t value; Value being written to memory by the memset.


-
enumerator MEMSET_FIELD_BYTES
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds18MEMSET_FIELD_BYTESE) uint64_t bytes; Number of bytes being set.


-
enumerator MEMSET_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds18MEMSET_FIELD_STARTE) uint64_t start; Start timestamp for the memset operation (in nanoseconds).

A value of 0 indicates timestamp couldn’t be collected.


-
enumerator MEMSET_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds16MEMSET_FIELD_ENDE) uint64_t end; End timestamp for the memset operation (in nanoseconds).

A value of 0 indicates timestamp couldn’t be collected.


-
enumerator MEMSET_FIELD_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds22MEMSET_FIELD_DEVICE_IDE) uint32_t deviceId; Device on which the memset is occurring.


-
enumerator MEMSET_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds23MEMSET_FIELD_CONTEXT_IDE) uint32_t contextId; CUDA context where the memset is occurring.


-
enumerator MEMSET_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds22MEMSET_FIELD_STREAM_IDE) uint32_t streamId; Stream where the memset is occurring.


-
enumerator MEMSET_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds27MEMSET_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this memset operation.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator MEMSET_FIELD_FLAGS
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds18MEMSET_FIELD_FLAGSE) uint16_t flags; Flags associated with the memset.

See also


-
enumerator MEMSET_FIELD_MEMORY_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds24MEMSET_FIELD_MEMORY_KINDE) uint16_t memoryKind; Kind of memory being set.

See also


-
enumerator MEMSET_FIELD_GRAPH_NODE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds26MEMSET_FIELD_GRAPH_NODE_IDE) uint64_t graphNodeId; CUDA Graph node ID that executed this memset.


-
enumerator MEMSET_FIELD_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds21MEMSET_FIELD_GRAPH_IDE) uint32_t graphId; CUDA Graph ID that executed this memset.


-
enumerator MEMSET_FIELD_CHANNEL_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds23MEMSET_FIELD_CHANNEL_IDE) uint32_t channelID; Hardware channel ID used by the memset.


-
enumerator MEMSET_FIELD_CHANNEL_TYPE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds25MEMSET_FIELD_CHANNEL_TYPEE) CUpti_ChannelType channelType; Type of hardware channel used by the memset.


-
enumerator MEMSET_FIELD_IS_DEVICE_LAUNCHED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds31MEMSET_FIELD_IS_DEVICE_LAUNCHEDE) uint8_t isDeviceLaunched; This field is set to 1 if the kernel is part of a device launched graph.


-
enumerator MEMSET_FIELD_SOURCE_GRAPH_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds28MEMSET_FIELD_SOURCE_GRAPH_IDE) uint32_t sourceGraphId; The unique graph ID of the node from which the memset node was instantiated or last updated.

This field will be 0 if the memset is not launched through graph launch APIs.


-
enumerator MEMSET_FIELD_SOURCE_GRAPH_NODE_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds33MEMSET_FIELD_SOURCE_GRAPH_NODE_IDE) uint64_t sourceGraphNodeId; The unique graph node ID of the node from which the memset node was instantiated or last updated.

This field will be 0 if the memset is not launched through graph launch APIs.


-
enumerator MEMSET_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMemsetFieldIds16MEMSET_FIELD_MAXE) Total number of defined fields.


-
enumerator MEMSET_FIELD_KIND

-
enum CUpti_ActivityNameFieldIds
[#](https://docs.nvidia.com#_CPPv426CUpti_ActivityNameFieldIds) Enum identifiers for fields in

[CUpti_ActivityName](https://docs.nvidia.com/structCUpti__ActivityName.html#structcupti__activityname).Each enum value corresponds to a field in

[CUpti_ActivityName](https://docs.nvidia.com/structCUpti__ActivityName.html#structcupti__activityname)and describes the data type and purpose of that field.*Values:*-
enumerator NAME_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityNameFieldIds15NAME_FIELD_KINDE) CUpti_ActivityKind kind; Kind of activity record: CUPTI_ACTIVITY_KIND_NAME.


-
enumerator NAME_FIELD_OBJECT_KIND
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityNameFieldIds22NAME_FIELD_OBJECT_KINDE) CUpti_ActivityObjectKind objectKind; Kind of activity object being named.


-
enumerator NAME_FIELD_OBJECT_ID
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityNameFieldIds20NAME_FIELD_OBJECT_IDE) [CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#unioncupti__activityobjectkindid)objectId; Identifier for the activity object being named.

-
enumerator NAME_FIELD_NAME
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityNameFieldIds15NAME_FIELD_NAMEE) const char *name; The name.


-
enumerator NAME_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityNameFieldIds14NAME_FIELD_MAXE) Total number of defined fields.


-
enumerator NAME_FIELD_KIND

-
enum CUpti_ActivityNvLinkFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityNvLinkFieldIds) Enum identifiers for fields in

[CUpti_ActivityNvLink5](https://docs.nvidia.com/structCUpti__ActivityNvLink5.html#structcupti__activitynvlink5).Each enum value corresponds to a field in

[CUpti_ActivityNvLink5](https://docs.nvidia.com/structCUpti__ActivityNvLink5.html#structcupti__activitynvlink5)and describes the data type and purpose of that field.*Values:*-
enumerator NVLINK_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds17NVLINK_FIELD_KINDE) CUpti_ActivityKind kind; Kind of activity record: CUPTI_ACTIVITY_KIND_NVLINK.


-
enumerator NVLINK_FIELD_NVLINK_VERSION
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds27NVLINK_FIELD_NVLINK_VERSIONE) uint32_t nvlinkVersion; NvLink version.


-
enumerator NVLINK_FIELD_TYPE_DEV0
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds22NVLINK_FIELD_TYPE_DEV0E) CUpti_DevType typeDev0; Type of device 0.


-
enumerator NVLINK_FIELD_TYPE_DEV1
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds22NVLINK_FIELD_TYPE_DEV1E) CUpti_DevType typeDev1; Type of device 1.


-
enumerator NVLINK_FIELD_ID_DEV0
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds20NVLINK_FIELD_ID_DEV0E) union idDev0; If typeDev0 is CUPTI_DEV_TYPE_GPU, UUID for device 0.

If typeDev0 is CUPTI_DEV_TYPE_NPU,

[CUpti_ActivityNvLinkNpu](https://docs.nvidia.com/structCUpti__ActivityNvLinkNpu.html#structcupti__activitynvlinknpu)for NPU.

-
enumerator NVLINK_FIELD_ID_DEV1
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds20NVLINK_FIELD_ID_DEV1E) union idDev1; If typeDev1 is CUPTI_DEV_TYPE_GPU, UUID for device 1.

If typeDev1 is CUPTI_DEV_TYPE_NPU,

[CUpti_ActivityNvLinkNpu](https://docs.nvidia.com/structCUpti__ActivityNvLinkNpu.html#structcupti__activitynvlinknpu)for NPU.

-
enumerator NVLINK_FIELD_FLAG
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds17NVLINK_FIELD_FLAGE) uint32_t flag; Flag gives capabilities of the link (CUpti_LinkFlag).


-
enumerator NVLINK_FIELD_PHYSICAL_NVLINK_COUNT
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds34NVLINK_FIELD_PHYSICAL_NVLINK_COUNTE) uint32_t physicalNvLinkCount; Number of physical NVLinks present between two devices.


-
enumerator NVLINK_FIELD_PORT_DEV0
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds22NVLINK_FIELD_PORT_DEV0E) uint32_t* portDev0; Port numbers for NVLinks connected to device 0.


-
enumerator NVLINK_FIELD_PORT_DEV1
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds22NVLINK_FIELD_PORT_DEV1E) uint32_t* portDev1; Port numbers for NVLinks connected to device 1.


-
enumerator NVLINK_FIELD_BANDWIDTH
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds22NVLINK_FIELD_BANDWIDTHE) uint64_t bandwidth; Bandwidth of NVLink in kbytes/sec.


-
enumerator NVLINK_FIELD_NVSWITCH_CONNECTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds31NVLINK_FIELD_NVSWITCH_CONNECTEDE) uint8_t nvswitchConnected; NVSwitch is connected as an intermediate node.


-
enumerator NVLINK_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityNvLinkFieldIds16NVLINK_FIELD_MAXE) Total number of defined fields.


-
enumerator NVLINK_FIELD_KIND

-
enum CUpti_ActivityObjectKind
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityObjectKind) The kinds of activity objects.

See also

*Values:*-
enumerator CUPTI_ACTIVITY_OBJECT_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityObjectKind29CUPTI_ACTIVITY_OBJECT_UNKNOWNE) The object kind is not known.


-
enumerator CUPTI_ACTIVITY_OBJECT_PROCESS
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityObjectKind29CUPTI_ACTIVITY_OBJECT_PROCESSE) A process.


-
enumerator CUPTI_ACTIVITY_OBJECT_THREAD
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityObjectKind28CUPTI_ACTIVITY_OBJECT_THREADE) A thread.


-
enumerator CUPTI_ACTIVITY_OBJECT_DEVICE
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityObjectKind28CUPTI_ACTIVITY_OBJECT_DEVICEE) A device.


-
enumerator CUPTI_ACTIVITY_OBJECT_CONTEXT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityObjectKind29CUPTI_ACTIVITY_OBJECT_CONTEXTE) A context.


-
enumerator CUPTI_ACTIVITY_OBJECT_STREAM
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityObjectKind28CUPTI_ACTIVITY_OBJECT_STREAME) A stream.


-
enumerator CUPTI_ACTIVITY_OBJECT_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityObjectKind31CUPTI_ACTIVITY_OBJECT_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_OBJECT_UNKNOWN

-
enum CUpti_ActivityOpenAccDataFieldIds
[#](https://docs.nvidia.com#_CPPv433CUpti_ActivityOpenAccDataFieldIds) Enum identifiers for fields in

[CUpti_ActivityOpenAccData](https://docs.nvidia.com/structCUpti__ActivityOpenAccData.html#structcupti__activityopenaccdata).Each enum value corresponds to a field in

[CUpti_ActivityOpenAccData](https://docs.nvidia.com/structCUpti__ActivityOpenAccData.html#structcupti__activityopenaccdata)and documents the exact meaning of that field.*Values:*-
enumerator OPENACC_DATA_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds23OPENACC_DATA_FIELD_KINDE) CUpti_ActivityKind kind; The activity record kind.

Must be CUPTI_ACTIVITY_KIND_OPENACC_DATA.


-
enumerator OPENACC_DATA_FIELD_EVENT_KIND
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds29OPENACC_DATA_FIELD_EVENT_KINDE) CUpti_OpenAccEventKind eventKind; CUPTI OpenACC event kind.


-
enumerator OPENACC_DATA_FIELD_PARENT_CONSTRUCT
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds35OPENACC_DATA_FIELD_PARENT_CONSTRUCTE) CUpti_OpenAccConstructKind parentConstruct; Parent OpenACC construct kind.

For PGI OpenACC runtime < 16.1, this is always CUPTI_OPENACC_CONSTRUCT_KIND_UNKNOWN.


-
enumerator OPENACC_DATA_FIELD_VERSION
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds26OPENACC_DATA_FIELD_VERSIONE) uint32_t version; Version number.


-
enumerator OPENACC_DATA_FIELD_IMPLICIT
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds27OPENACC_DATA_FIELD_IMPLICITE) uint32_t implicit; 1 if this is an implicit event (e.g.

implicit wait), 0 otherwise.


-
enumerator OPENACC_DATA_FIELD_DEVICE_TYPE
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds30OPENACC_DATA_FIELD_DEVICE_TYPEE) uint32_t deviceType; OpenACC device type.


-
enumerator OPENACC_DATA_FIELD_DEVICE_NUMBER
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds32OPENACC_DATA_FIELD_DEVICE_NUMBERE) uint32_t deviceNumber; OpenACC device number.


-
enumerator OPENACC_DATA_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds28OPENACC_DATA_FIELD_THREAD_IDE) uint32_t threadId; Thread ID.


-
enumerator OPENACC_DATA_FIELD_ASYNC
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds24OPENACC_DATA_FIELD_ASYNCE) uint64_t async; Value of the async() clause of the corresponding directive.


-
enumerator OPENACC_DATA_FIELD_ASYNC_MAP
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds28OPENACC_DATA_FIELD_ASYNC_MAPE) uint64_t asyncMap; Internal asynchronous queue number used.


-
enumerator OPENACC_DATA_FIELD_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds26OPENACC_DATA_FIELD_LINE_NOE) uint32_t lineNo; Line number of the directive or construct start.

A non-positive value indicates unknown.


-
enumerator OPENACC_DATA_FIELD_END_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds30OPENACC_DATA_FIELD_END_LINE_NOE) uint32_t endLineNo; Line number of the end of the OpenACC construct.

A non-positive value indicates unknown.


-
enumerator OPENACC_DATA_FIELD_FUNC_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds31OPENACC_DATA_FIELD_FUNC_LINE_NOE) uint32_t funcLineNo; First line number of the function in which the event occurred.

A non-positive value indicates unknown.


-
enumerator OPENACC_DATA_FIELD_FUNC_END_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds35OPENACC_DATA_FIELD_FUNC_END_LINE_NOE) uint32_t funcEndLineNo; Last line number of the function in which the event occurred.

A non-positive value indicates unknown.


-
enumerator OPENACC_DATA_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds24OPENACC_DATA_FIELD_STARTE) uint64_t start; CUPTI start timestamp (in ns).


-
enumerator OPENACC_DATA_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds22OPENACC_DATA_FIELD_ENDE) uint64_t end; CUPTI end timestamp (in ns).


-
enumerator OPENACC_DATA_FIELD_CU_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds31OPENACC_DATA_FIELD_CU_DEVICE_IDE) uint32_t cuDeviceId; CUDA device ID.

Valid only if deviceType is acc_device_nvidia.


-
enumerator OPENACC_DATA_FIELD_CU_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds32OPENACC_DATA_FIELD_CU_CONTEXT_IDE) uint32_t cuContextId; CUDA context ID.

Valid only if deviceType is acc_device_nvidia.


-
enumerator OPENACC_DATA_FIELD_CU_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds31OPENACC_DATA_FIELD_CU_STREAM_IDE) uint32_t cuStreamId; CUDA stream ID.

Valid only if deviceType is acc_device_nvidia.


-
enumerator OPENACC_DATA_FIELD_CU_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds32OPENACC_DATA_FIELD_CU_PROCESS_IDE) uint32_t cuProcessId; Process ID where the OpenACC activity is executing.


-
enumerator OPENACC_DATA_FIELD_CU_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds31OPENACC_DATA_FIELD_CU_THREAD_IDE) uint64_t cuThreadId; Thread ID where the OpenACC activity is executing.


-
enumerator OPENACC_DATA_FIELD_EXTERNAL_ID
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds30OPENACC_DATA_FIELD_EXTERNAL_IDE) uint32_t externalId; OpenACC correlation ID.

Matches the externalId from the corresponding CUPTI_EXTERNAL_CORRELATION_KIND_OPENACC record.


-
enumerator OPENACC_DATA_FIELD_SRC_FILE
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds27OPENACC_DATA_FIELD_SRC_FILEE) const char* srcFile; Pointer to a null-terminated string containing the source file name or path, if known.


-
enumerator OPENACC_DATA_FIELD_FUNC_NAME
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds28OPENACC_DATA_FIELD_FUNC_NAMEE) const char* funcName; Pointer to a null-terminated string containing the function name.


-
enumerator OPENACC_DATA_FIELD_BYTES
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds24OPENACC_DATA_FIELD_BYTESE) uint64_t bytes; Number of bytes involved in the operation.


-
enumerator OPENACC_DATA_FIELD_HOST_PTR
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds27OPENACC_DATA_FIELD_HOST_PTRE) uint64_t hostPtr; Host pointer, if available.


-
enumerator OPENACC_DATA_FIELD_DEVICE_PTR
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds29OPENACC_DATA_FIELD_DEVICE_PTRE) uint64_t devicePtr; Device pointer, if available.


-
enumerator OPENACC_DATA_FIELD_VAR_NAME
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds27OPENACC_DATA_FIELD_VAR_NAMEE) const char* varName; Pointer to a null-terminated string containing the variable name for which this event is triggered.


-
enumerator OPENACC_DATA_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityOpenAccDataFieldIds22OPENACC_DATA_FIELD_MAXE) Total number of defined fields.


-
enumerator OPENACC_DATA_FIELD_KIND

-
enum CUpti_ActivityOpenAccLaunchFieldIds
[#](https://docs.nvidia.com#_CPPv435CUpti_ActivityOpenAccLaunchFieldIds) Enum identifiers for fields in

[CUpti_ActivityOpenAccLaunch](https://docs.nvidia.com/structCUpti__ActivityOpenAccLaunch.html#structcupti__activityopenacclaunch).Each enum value corresponds to a field in

[CUpti_ActivityOpenAccLaunch](https://docs.nvidia.com/structCUpti__ActivityOpenAccLaunch.html#structcupti__activityopenacclaunch)and documents the exact meaning of that field.*Values:*-
enumerator OPENACC_LAUNCH_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds25OPENACC_LAUNCH_FIELD_KINDE) CUpti_ActivityKind kind; The activity record kind, must be CUPTI_ACTIVITY_KIND_OPENACC_LAUNCH.


-
enumerator OPENACC_LAUNCH_FIELD_EVENT_KIND
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds31OPENACC_LAUNCH_FIELD_EVENT_KINDE) CUpti_OpenAccEventKind eventKind; CUPTI OpenACC event kind.


-
enumerator OPENACC_LAUNCH_FIELD_PARENT_CONSTRUCT
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds37OPENACC_LAUNCH_FIELD_PARENT_CONSTRUCTE) CUpti_OpenAccConstructKind parentConstruct; CUPTI OpenACC parent construct kind.


-
enumerator OPENACC_LAUNCH_FIELD_VERSION
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds28OPENACC_LAUNCH_FIELD_VERSIONE) uint32_t version; Version number.


-
enumerator OPENACC_LAUNCH_FIELD_IMPLICIT
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds29OPENACC_LAUNCH_FIELD_IMPLICITE) uint32_t implicit; 1 for implicit event, 0 otherwise.


-
enumerator OPENACC_LAUNCH_FIELD_DEVICE_TYPE
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds32OPENACC_LAUNCH_FIELD_DEVICE_TYPEE) uint32_t deviceType; Device type.


-
enumerator OPENACC_LAUNCH_FIELD_DEVICE_NUMBER
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds34OPENACC_LAUNCH_FIELD_DEVICE_NUMBERE) uint32_t deviceNumber; Device number.


-
enumerator OPENACC_LAUNCH_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds30OPENACC_LAUNCH_FIELD_THREAD_IDE) uint32_t threadId; Thread identifier.


-
enumerator OPENACC_LAUNCH_FIELD_ASYNC
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds26OPENACC_LAUNCH_FIELD_ASYNCE) uint64_t async; Value of async() clause of the corresponding directive.


-
enumerator OPENACC_LAUNCH_FIELD_ASYNC_MAP
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds30OPENACC_LAUNCH_FIELD_ASYNC_MAPE) uint64_t asyncMap; Internal asynchronous queue number used.


-
enumerator OPENACC_LAUNCH_FIELD_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds28OPENACC_LAUNCH_FIELD_LINE_NOE) uint32_t lineNo; Line number of the directive or construct.


-
enumerator OPENACC_LAUNCH_FIELD_END_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds32OPENACC_LAUNCH_FIELD_END_LINE_NOE) uint32_t endLineNo; Line number of the end of the construct.


-
enumerator OPENACC_LAUNCH_FIELD_FUNC_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds33OPENACC_LAUNCH_FIELD_FUNC_LINE_NOE) uint32_t funcLineNo; Starting line number of the function.


-
enumerator OPENACC_LAUNCH_FIELD_FUNC_END_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds37OPENACC_LAUNCH_FIELD_FUNC_END_LINE_NOE) uint32_t funcEndLineNo; Ending line number of the function.


-
enumerator OPENACC_LAUNCH_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds26OPENACC_LAUNCH_FIELD_STARTE) uint64_t start; CUPTI start timestamp.


-
enumerator OPENACC_LAUNCH_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds24OPENACC_LAUNCH_FIELD_ENDE) uint64_t end; CUPTI end timestamp.


-
enumerator OPENACC_LAUNCH_FIELD_CU_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds33OPENACC_LAUNCH_FIELD_CU_DEVICE_IDE) uint32_t cuDeviceId; CUDA device id.


-
enumerator OPENACC_LAUNCH_FIELD_CU_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds34OPENACC_LAUNCH_FIELD_CU_CONTEXT_IDE) uint32_t cuContextId; CUDA context id.


-
enumerator OPENACC_LAUNCH_FIELD_CU_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds33OPENACC_LAUNCH_FIELD_CU_STREAM_IDE) uint32_t cuStreamId; CUDA stream id.


-
enumerator OPENACC_LAUNCH_FIELD_CU_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds34OPENACC_LAUNCH_FIELD_CU_PROCESS_IDE) uint32_t cuProcessId; Process id where the activity is executing.


-
enumerator OPENACC_LAUNCH_FIELD_CU_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds33OPENACC_LAUNCH_FIELD_CU_THREAD_IDE) uint64_t cuThreadId; Thread id where the activity is executing.


-
enumerator OPENACC_LAUNCH_FIELD_EXTERNAL_ID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds32OPENACC_LAUNCH_FIELD_EXTERNAL_IDE) uint32_t externalId; OpenACC correlation id.


-
enumerator OPENACC_LAUNCH_FIELD_SRC_FILE
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds29OPENACC_LAUNCH_FIELD_SRC_FILEE) const char *srcFile; Pointer to null-terminated string containing source file name or path.


-
enumerator OPENACC_LAUNCH_FIELD_FUNC_NAME
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds30OPENACC_LAUNCH_FIELD_FUNC_NAMEE) const char *funcName; Pointer to null-terminated string containing function name.


-
enumerator OPENACC_LAUNCH_FIELD_NUM_GANGS
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds30OPENACC_LAUNCH_FIELD_NUM_GANGSE) uint64_t numGangs; Number of gangs created for this kernel launch.


-
enumerator OPENACC_LAUNCH_FIELD_NUM_WORKERS
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds32OPENACC_LAUNCH_FIELD_NUM_WORKERSE) uint64_t numWorkers; Number of workers created for this kernel launch.


-
enumerator OPENACC_LAUNCH_FIELD_VECTOR_LENGTH
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds34OPENACC_LAUNCH_FIELD_VECTOR_LENGTHE) uint64_t vectorLength; Number of vector lanes created for this kernel launch.


-
enumerator OPENACC_LAUNCH_FIELD_KERNEL_NAME
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds32OPENACC_LAUNCH_FIELD_KERNEL_NAMEE) const char *kernelName; Pointer to null-terminated string containing kernel name.


-
enumerator OPENACC_LAUNCH_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityOpenAccLaunchFieldIds24OPENACC_LAUNCH_FIELD_MAXE) Total number of defined fields.


-
enumerator OPENACC_LAUNCH_FIELD_KIND

-
enum CUpti_ActivityOpenAccOtherFieldIds
[#](https://docs.nvidia.com#_CPPv434CUpti_ActivityOpenAccOtherFieldIds) Enum identifiers for fields in

[CUpti_ActivityOpenAccOther](https://docs.nvidia.com/structCUpti__ActivityOpenAccOther.html#structcupti__activityopenaccother).Each enum value corresponds to a field in

[CUpti_ActivityOpenAccOther](https://docs.nvidia.com/structCUpti__ActivityOpenAccOther.html#structcupti__activityopenaccother)and documents the exact meaning of that field.*Values:*-
enumerator OPENACC_OTHER_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds24OPENACC_OTHER_FIELD_KINDE) CUpti_ActivityKind kind; The activity record kind, must be CUPTI_ACTIVITY_KIND_OPENACC_OTHER.


-
enumerator OPENACC_OTHER_FIELD_EVENT_KIND
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds30OPENACC_OTHER_FIELD_EVENT_KINDE) CUpti_OpenAccEventKind eventKind; CUPTI OpenACC event kind.


-
enumerator OPENACC_OTHER_FIELD_PARENT_CONSTRUCT
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds36OPENACC_OTHER_FIELD_PARENT_CONSTRUCTE) CUpti_OpenAccConstructKind parentConstruct; CUPTI OpenACC parent construct kind.


-
enumerator OPENACC_OTHER_FIELD_VERSION
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds27OPENACC_OTHER_FIELD_VERSIONE) uint32_t version; Version number.


-
enumerator OPENACC_OTHER_FIELD_IMPLICIT
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds28OPENACC_OTHER_FIELD_IMPLICITE) uint32_t implicit; 1 for implicit event, 0 otherwise.


-
enumerator OPENACC_OTHER_FIELD_DEVICE_TYPE
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds31OPENACC_OTHER_FIELD_DEVICE_TYPEE) uint32_t deviceType; Device type.


-
enumerator OPENACC_OTHER_FIELD_DEVICE_NUMBER
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds33OPENACC_OTHER_FIELD_DEVICE_NUMBERE) uint32_t deviceNumber; Device number.


-
enumerator OPENACC_OTHER_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds29OPENACC_OTHER_FIELD_THREAD_IDE) uint32_t threadId; Thread identifier.


-
enumerator OPENACC_OTHER_FIELD_ASYNC
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds25OPENACC_OTHER_FIELD_ASYNCE) uint64_t async; Value of async() clause of the corresponding directive.


-
enumerator OPENACC_OTHER_FIELD_ASYNC_MAP
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds29OPENACC_OTHER_FIELD_ASYNC_MAPE) uint64_t asyncMap; Internal asynchronous queue number used.


-
enumerator OPENACC_OTHER_FIELD_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds27OPENACC_OTHER_FIELD_LINE_NOE) uint32_t lineNo; Line number of the directive or construct.


-
enumerator OPENACC_OTHER_FIELD_END_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds31OPENACC_OTHER_FIELD_END_LINE_NOE) uint32_t endLineNo; Line number of the end of the construct.


-
enumerator OPENACC_OTHER_FIELD_FUNC_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds32OPENACC_OTHER_FIELD_FUNC_LINE_NOE) uint32_t funcLineNo; Starting line number of the function.


-
enumerator OPENACC_OTHER_FIELD_FUNC_END_LINE_NO
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds36OPENACC_OTHER_FIELD_FUNC_END_LINE_NOE) uint32_t funcEndLineNo; Ending line number of the function.


-
enumerator OPENACC_OTHER_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds25OPENACC_OTHER_FIELD_STARTE) uint64_t start; CUPTI start timestamp.


-
enumerator OPENACC_OTHER_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds23OPENACC_OTHER_FIELD_ENDE) uint64_t end; CUPTI end timestamp.


-
enumerator OPENACC_OTHER_FIELD_CU_DEVICE_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds32OPENACC_OTHER_FIELD_CU_DEVICE_IDE) uint32_t cuDeviceId; CUDA device id.


-
enumerator OPENACC_OTHER_FIELD_CU_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds33OPENACC_OTHER_FIELD_CU_CONTEXT_IDE) uint32_t cuContextId; CUDA context id.


-
enumerator OPENACC_OTHER_FIELD_CU_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds32OPENACC_OTHER_FIELD_CU_STREAM_IDE) uint32_t cuStreamId; CUDA stream id.


-
enumerator OPENACC_OTHER_FIELD_CU_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds33OPENACC_OTHER_FIELD_CU_PROCESS_IDE) uint32_t cuProcessId; Process id where the activity is executing.


-
enumerator OPENACC_OTHER_FIELD_CU_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds32OPENACC_OTHER_FIELD_CU_THREAD_IDE) uint64_t cuThreadId; Thread id where the activity is executing.


-
enumerator OPENACC_OTHER_FIELD_EXTERNAL_ID
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds31OPENACC_OTHER_FIELD_EXTERNAL_IDE) uint32_t externalId; OpenACC correlation id.


-
enumerator OPENACC_OTHER_FIELD_SRC_FILE
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds28OPENACC_OTHER_FIELD_SRC_FILEE) const char *srcFile; Pointer to null-terminated string containing source file name or path.


-
enumerator OPENACC_OTHER_FIELD_FUNC_NAME
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds29OPENACC_OTHER_FIELD_FUNC_NAMEE) const char *funcName; Pointer to null-terminated string containing function name.


-
enumerator OPENACC_OTHER_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityOpenAccOtherFieldIds23OPENACC_OTHER_FIELD_MAXE) Total number of defined fields.


-
enumerator OPENACC_OTHER_FIELD_KIND

-
enum CUpti_ActivityOpenMpFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityOpenMpFieldIds) Enum identifiers for fields in

[CUpti_ActivityOpenMp](https://docs.nvidia.com/structCUpti__ActivityOpenMp.html#structcupti__activityopenmp).This activity record records OpenMP activity information.

*Values:*-
enumerator OPENMP_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityOpenMpFieldIds17OPENMP_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_OPENMP.


-
enumerator OPENMP_FIELD_EVENT_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityOpenMpFieldIds23OPENMP_FIELD_EVENT_KINDE) CUpti_OpenMpEventKind eventKind; CUPTI OpenMP event kind (.

See also

CUpti_OpenMpEventKind)


-
enumerator OPENMP_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityOpenMpFieldIds18OPENMP_FIELD_STARTE) uint64_t start; CUPTI start timestamp


-
enumerator OPENMP_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityOpenMpFieldIds16OPENMP_FIELD_ENDE) uint64_t end; CUPTI end timestamp


-
enumerator OPENMP_FIELD_CU_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityOpenMpFieldIds25OPENMP_FIELD_CU_THREAD_IDE) uint64_t cuThreadId; The ID of the thread where the OpenMP activity is executing.


-
enumerator OPENMP_FIELD_CU_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityOpenMpFieldIds26OPENMP_FIELD_CU_PROCESS_IDE) uint32_t cuProcessId; The ID of the process where the OpenMP activity is executing.


-
enumerator OPENMP_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityOpenMpFieldIds16OPENMP_FIELD_MAXE) Total number of defined fields.


-
enumerator OPENMP_FIELD_KIND

-
enum CUpti_ActivityOverheadFieldIds
[#](https://docs.nvidia.com#_CPPv430CUpti_ActivityOverheadFieldIds) Enum identifiers for fields to trace CUPTI and driver overhead information.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_OVERHEAD.

*Values:*-
enumerator OVERHEAD_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds19OVERHEAD_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_OVERHEAD.


-
enumerator OVERHEAD_FIELD_OVERHEAD_KIND
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds28OVERHEAD_FIELD_OVERHEAD_KINDE) CUpti_ActivityOverheadKind overheadKind; The kind of overhead, CUPTI, DRIVER, COMPILER etc.


-
enumerator OVERHEAD_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds25OVERHEAD_FIELD_PROCESS_IDE) uint32_t processId; The process ID of the process where the overhead is occurring.


-
enumerator OVERHEAD_FIELD_THREAD_ID
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds24OVERHEAD_FIELD_THREAD_IDE) uint64_t threadId; The thread ID of the process where the overhead is occurring.


-
enumerator OVERHEAD_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds20OVERHEAD_FIELD_STARTE) uint64_t start; The start timestamp for the overhead, in nanoseconds.


-
enumerator OVERHEAD_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds18OVERHEAD_FIELD_ENDE) uint64_t end; The end timestamp for the overhead, in nanoseconds.


-
enumerator OVERHEAD_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds29OVERHEAD_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this overhead record.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator OVERHEAD_FIELD_OVERHEAD_DATA
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds28OVERHEAD_FIELD_OVERHEAD_DATAE) void *overheadData; Pointer to the struct with additional details about the overhead.

Refer CUpti_ActivityOverheadKind enum and the corresponding structure to typecast and access additional overhead data. Client is responsible for freeing this memory using the free function when done.


-
enumerator OVERHEAD_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityOverheadFieldIds18OVERHEAD_FIELD_MAXE) Total number of defined fields.


-
enumerator OVERHEAD_FIELD_KIND

-
enum CUpti_ActivityOverheadKind
[#](https://docs.nvidia.com#_CPPv426CUpti_ActivityOverheadKind) The kinds of activity overhead.

*Values:*-
enumerator CUPTI_ACTIVITY_OVERHEAD_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind31CUPTI_ACTIVITY_OVERHEAD_UNKNOWNE) The overhead kind is not known.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_DRIVER_COMPILER
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind39CUPTI_ACTIVITY_OVERHEAD_DRIVER_COMPILERE) Compiler overhead.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_CUPTI_BUFFER_FLUSH
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind42CUPTI_ACTIVITY_OVERHEAD_CUPTI_BUFFER_FLUSHE) Activity buffer flush overhead.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_CUPTI_INSTRUMENTATION
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind45CUPTI_ACTIVITY_OVERHEAD_CUPTI_INSTRUMENTATIONE) CUPTI instrumentation overhead.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_CUPTI_RESOURCE
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind38CUPTI_ACTIVITY_OVERHEAD_CUPTI_RESOURCEE) CUPTI resource creation and destruction overhead.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_RUNTIME_TRIGGERED_MODULE_LOADING
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind56CUPTI_ACTIVITY_OVERHEAD_RUNTIME_TRIGGERED_MODULE_LOADINGE) CUDA Runtime triggered module loading overhead.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_LAZY_FUNCTION_LOADING
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind45CUPTI_ACTIVITY_OVERHEAD_LAZY_FUNCTION_LOADINGE) Lazy function loading overhead.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_COMMAND_BUFFER_FULL
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind43CUPTI_ACTIVITY_OVERHEAD_COMMAND_BUFFER_FULLE) Overhead due to lack of command buffer space.

Refer

[CUpti_ActivityOverheadCommandBufferFullData](https://docs.nvidia.com/structCUpti__ActivityOverheadCommandBufferFullData.html#structcupti__activityoverheadcommandbufferfulldata)for more details.

-
enumerator CUPTI_ACTIVITY_OVERHEAD_ACTIVITY_BUFFER_REQUEST
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind47CUPTI_ACTIVITY_OVERHEAD_ACTIVITY_BUFFER_REQUESTE) Overhead due to activity buffer request.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_UVM_ACTIVITY_INIT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind41CUPTI_ACTIVITY_OVERHEAD_UVM_ACTIVITY_INITE) Overhead due to UVM activity initialization.


-
enumerator CUPTI_ACTIVITY_OVERHEAD_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityOverheadKind33CUPTI_ACTIVITY_OVERHEAD_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_OVERHEAD_UNKNOWN

-
enum CUpti_ActivityPCSamplingPeriod
[#](https://docs.nvidia.com#_CPPv430CUpti_ActivityPCSamplingPeriod) Sampling period for PC sampling method.

Sampling period can be set using

[cuptiActivityConfigurePCSampling](https://docs.nvidia.com#group__cupti__activity__api_1ga115305aadc838df99d88283fc64c4317)*Values:*-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_INVALID
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingPeriod41CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_INVALIDE) The PC sampling period is not set.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_MIN
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingPeriod37CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_MINE) Minimum sampling period available on the device.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_LOW
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingPeriod37CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_LOWE) Sampling period in lower range.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_MID
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingPeriod37CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_MIDE) Medium sampling period.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_HIGH
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingPeriod38CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_HIGHE) Sampling period in higher range.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_MAX
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingPeriod37CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_MAXE) Maximum sampling period available on the device.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingPeriod43CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_PERIOD_INVALID

-
enum CUpti_ActivityPCSamplingStallReason
[#](https://docs.nvidia.com#_CPPv435CUpti_ActivityPCSamplingStallReason) The stall reason for PC sampling activity.

*Values:*-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_INVALID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason40CUPTI_ACTIVITY_PC_SAMPLING_STALL_INVALIDE) Invalid reason.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_NONE
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason37CUPTI_ACTIVITY_PC_SAMPLING_STALL_NONEE) No stall, instruction is selected for issue.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_INST_FETCH
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason43CUPTI_ACTIVITY_PC_SAMPLING_STALL_INST_FETCHE) Warp is blocked because next instruction is not yet available, because of instruction cache miss, or because of branching effects.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_EXEC_DEPENDENCY
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason48CUPTI_ACTIVITY_PC_SAMPLING_STALL_EXEC_DEPENDENCYE) Instruction is waiting on an arithmetic dependency.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_MEMORY_DEPENDENCY
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason50CUPTI_ACTIVITY_PC_SAMPLING_STALL_MEMORY_DEPENDENCYE) Warp is blocked because it is waiting for a memory access to complete.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_TEXTURE
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason40CUPTI_ACTIVITY_PC_SAMPLING_STALL_TEXTUREE) Texture sub-system is fully utilized or has too many outstanding requests.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_SYNC
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason37CUPTI_ACTIVITY_PC_SAMPLING_STALL_SYNCE) Warp is blocked as it is waiting at __syncthreads() or at memory barrier.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_CONSTANT_MEMORY_DEPENDENCY
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason59CUPTI_ACTIVITY_PC_SAMPLING_STALL_CONSTANT_MEMORY_DEPENDENCYE) Warp is blocked waiting for

**constant**memory and immediate memory access to complete.

-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_PIPE_BUSY
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason42CUPTI_ACTIVITY_PC_SAMPLING_STALL_PIPE_BUSYE) Compute operation cannot be performed due to the required resources not being available.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_MEMORY_THROTTLE
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason48CUPTI_ACTIVITY_PC_SAMPLING_STALL_MEMORY_THROTTLEE) Warp is blocked because there are too many pending memory operations.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_NOT_SELECTED
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason45CUPTI_ACTIVITY_PC_SAMPLING_STALL_NOT_SELECTEDE) Warp was ready to issue, but some other warp issued instead.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_OTHER
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason38CUPTI_ACTIVITY_PC_SAMPLING_STALL_OTHERE) Miscellaneous reasons.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_SLEEPING
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason41CUPTI_ACTIVITY_PC_SAMPLING_STALL_SLEEPINGE) Sleeping.


-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N35CUpti_ActivityPCSamplingStallReason42CUPTI_ACTIVITY_PC_SAMPLING_STALL_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_PC_SAMPLING_STALL_INVALID

-
enum CUpti_ActivityPartitionedGlobalCacheConfig
[#](https://docs.nvidia.com#_CPPv442CUpti_ActivityPartitionedGlobalCacheConfig) Partitioned global caching option.

*Values:*-
enumerator CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ActivityPartitionedGlobalCacheConfig54CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_UNKNOWNE) Partitioned global cache config unknown.


-
enumerator CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ActivityPartitionedGlobalCacheConfig60CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_NOT_SUPPORTEDE) Partitioned global cache not supported.


-
enumerator CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_OFF
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ActivityPartitionedGlobalCacheConfig50CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_OFFE) Partitioned global cache config off.


-
enumerator CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_ON
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ActivityPartitionedGlobalCacheConfig49CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_ONE) Partitioned global cache config on.


-
enumerator CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ActivityPartitionedGlobalCacheConfig56CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_PARTITIONED_GLOBAL_CACHE_CONFIG_UNKNOWN

-
enum CUpti_ActivityPcieFieldIds
[#](https://docs.nvidia.com#_CPPv426CUpti_ActivityPcieFieldIds) Enum identifiers for fields in

[CUpti_ActivityPcie](https://docs.nvidia.com/structCUpti__ActivityPcie.html#structcupti__activitypcie).Each enum value corresponds to a field in

[CUpti_ActivityPcie](https://docs.nvidia.com/structCUpti__ActivityPcie.html#structcupti__activitypcie)and describes the data type and purpose of that field.*Values:*-
enumerator PCIE_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds15PCIE_FIELD_KINDE) CUpti_ActivityKind kind; Kind of activity record: CUPTI_ACTIVITY_KIND_PCIE.


-
enumerator PCIE_FIELD_TYPE
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds15PCIE_FIELD_TYPEE) CUpti_PcieDeviceType type; Type of device in topology, CUpti_PcieDeviceType.


-
enumerator PCIE_FIELD_ID
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds13PCIE_FIELD_IDE) union id; A unique identifier for GPU or Bridge in Topology.

CUdevice devId if type is CUPTI_PCIE_DEVICE_TYPE_GPU uint32_t bridgeId if type is CUPTI_PCIE_DEVICE_TYPE_BRIDGE


-
enumerator PCIE_FIELD_DOMAIN
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds17PCIE_FIELD_DOMAINE) uint32_t domain; Domain for the GPU or Bridge, required to identify which PCIE bus it belongs to in multiple NUMA systems.


-
enumerator PCIE_FIELD_PCIE_GENERATION
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds26PCIE_FIELD_PCIE_GENERATIONE) uint16_t pcieGeneration; PCIE Generation of GPU or Bridge.


-
enumerator PCIE_FIELD_LINK_RATE
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds20PCIE_FIELD_LINK_RATEE) uint16_t linkRate; Link rate of the GPU or bridge in gigatransfers per second (GT/s).


-
enumerator PCIE_FIELD_LINK_WIDTH
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds21PCIE_FIELD_LINK_WIDTHE) uint16_t linkWidth; Link width of the GPU or bridge.


-
enumerator PCIE_FIELD_UPSTREAM_BUS
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds23PCIE_FIELD_UPSTREAM_BUSE) uint16_t upstreamBus; Upstream bus ID for the GPU or PCI bridge.

Required to identify which bus it is connected to in the topology.


-
enumerator PCIE_FIELD_ATTR
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds15PCIE_FIELD_ATTRE) union attr; Attributes for more information about GPU (gpuAttr) or PCI Bridge (bridgeAttr).

[CUpti_ActivityPcieGpuAttr](https://docs.nvidia.com/structCUpti__ActivityPcieGpuAttr.html#structcupti__activitypciegpuattr)gpuAttr if type is CUPTI_PCIE_DEVICE_TYPE_GPU[CUpti_ActivityPcieBridgeAttr](https://docs.nvidia.com/structCUpti__ActivityPcieBridgeAttr.html#structcupti__activitypciebridgeattr)bridgeAttr if type is CUPTI_PCIE_DEVICE_TYPE_BRIDGE The size of this field is determined by the largest structure among the possible types it can hold.

-
enumerator PCIE_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityPcieFieldIds14PCIE_FIELD_MAXE) Total number of defined fields.


-
enumerator PCIE_FIELD_KIND

-
enum CUpti_ActivityPreemptionKind
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityPreemptionKind) The kind of a preemption activity.

*Values:*-
enumerator CUPTI_ACTIVITY_PREEMPTION_KIND_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityPreemptionKind38CUPTI_ACTIVITY_PREEMPTION_KIND_UNKNOWNE) The preemption kind is not known.


-
enumerator CUPTI_ACTIVITY_PREEMPTION_KIND_SAVE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityPreemptionKind35CUPTI_ACTIVITY_PREEMPTION_KIND_SAVEE) Preemption to save CDP block.


-
enumerator CUPTI_ACTIVITY_PREEMPTION_KIND_RESTORE
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityPreemptionKind38CUPTI_ACTIVITY_PREEMPTION_KIND_RESTOREE) Preemption to restore CDP block.


-
enumerator CUPTI_ACTIVITY_PREEMPTION_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityPreemptionKind40CUPTI_ACTIVITY_PREEMPTION_KIND_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_PREEMPTION_KIND_UNKNOWN

-
enum CUpti_ActivityStreamFieldIds
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityStreamFieldIds) Enum identifiers for fields to trace CUDA Stream operations.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_STREAM.

*Values:*-
enumerator STREAM_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityStreamFieldIds17STREAM_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_STREAM.


-
enumerator STREAM_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityStreamFieldIds23STREAM_FIELD_CONTEXT_IDE) uint32_t contextId; The ID of the context where the stream was created.


-
enumerator STREAM_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityStreamFieldIds22STREAM_FIELD_STREAM_IDE) uint32_t streamId; A unique stream ID to identify the stream.


-
enumerator STREAM_FIELD_PRIORITY
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityStreamFieldIds21STREAM_FIELD_PRIORITYE) int32_t priority; The clamped priority for the stream.


-
enumerator STREAM_FIELD_FLAG
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityStreamFieldIds17STREAM_FIELD_FLAGE) CUpti_ActivityStreamFlag flag; Flags associated with the stream.


-
enumerator STREAM_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityStreamFieldIds27STREAM_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this CUDA Stream operation.


-
enumerator STREAM_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityStreamFieldIds16STREAM_FIELD_MAXE) Total number of defined fields.


-
enumerator STREAM_FIELD_KIND

-
enum CUpti_ActivityStreamFlag
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityStreamFlag) stream type.

The types of stream to be used with

[CUpti_ActivityStream](https://docs.nvidia.com/structCUpti__ActivityStream.html#structcupti__activitystream).*Values:*-
enumerator CUPTI_ACTIVITY_STREAM_CREATE_FLAG_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityStreamFlag41CUPTI_ACTIVITY_STREAM_CREATE_FLAG_UNKNOWNE) Unknown data.


-
enumerator CUPTI_ACTIVITY_STREAM_CREATE_FLAG_DEFAULT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityStreamFlag41CUPTI_ACTIVITY_STREAM_CREATE_FLAG_DEFAULTE) Default stream.


-
enumerator CUPTI_ACTIVITY_STREAM_CREATE_FLAG_NON_BLOCKING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityStreamFlag46CUPTI_ACTIVITY_STREAM_CREATE_FLAG_NON_BLOCKINGE) Non-blocking stream.


-
enumerator CUPTI_ACTIVITY_STREAM_CREATE_FLAG_NULL
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityStreamFlag38CUPTI_ACTIVITY_STREAM_CREATE_FLAG_NULLE) Null stream.


-
enumerator CUPTI_ACTIVITY_STREAM_CREATE_MASK
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityStreamFlag33CUPTI_ACTIVITY_STREAM_CREATE_MASKE) Stream create Mask.


-
enumerator CUPTI_ACTIVITY_STREAM_CREATE_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityStreamFlag43CUPTI_ACTIVITY_STREAM_CREATE_FLAG_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_STREAM_CREATE_FLAG_UNKNOWN

-
enum CUpti_ActivitySynchronizationFieldIds
[#](https://docs.nvidia.com#_CPPv437CUpti_ActivitySynchronizationFieldIds) Enum identifiers for fields to trace various CUDA synchronization APIs.

These field IDs are used to reference specific fields when dynamically selecting or parsing activity records of CUPTI_ACTIVITY_KIND_SYNCHRONIZATION.

*Values:*-
enumerator SYNCHRONIZATION_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds26SYNCHRONIZATION_FIELD_KINDE) CUpti_ActivityKind kind; Kind of this activity record.

Always CUPTI_ACTIVITY_KIND_SYNCHRONIZATION.


-
enumerator SYNCHRONIZATION_FIELD_TYPE
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds26SYNCHRONIZATION_FIELD_TYPEE) CUpti_ActivitySynchronizationType type; The type of synchronization operation.


-
enumerator SYNCHRONIZATION_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds27SYNCHRONIZATION_FIELD_STARTE) uint64_t start; The start timestamp for the synchronization operation (in nanoseconds).


-
enumerator SYNCHRONIZATION_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds25SYNCHRONIZATION_FIELD_ENDE) uint64_t start; The start timestamp for the synchronization operation (in nanoseconds).


-
enumerator SYNCHRONIZATION_FIELD_CORRELATION_ID
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds36SYNCHRONIZATION_FIELD_CORRELATION_IDE) uint64_t correlationId; Correlation ID assigned to this synchronization operation.

Matches the correlation ID in the CUDA driver/runtime API activity record that launched it.


-
enumerator SYNCHRONIZATION_FIELD_CONTEXT_ID
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds32SYNCHRONIZATION_FIELD_CONTEXT_IDE) uint32_t contextId; CUDA context where the operation is occurring.


-
enumerator SYNCHRONIZATION_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds31SYNCHRONIZATION_FIELD_STREAM_IDE) uint32_t streamId; The compute stream where the synchronization operation is occurring.

CUPTI_SYNCHRONIZATION_INVALID_VALUE indicates that the field is not applicable for this record.


-
enumerator SYNCHRONIZATION_FIELD_CUDA_EVENT_ID
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds35SYNCHRONIZATION_FIELD_CUDA_EVENT_IDE) uint64_t cudaEventId; The CUDA event ID for which the synchronization operation is called.

CUPTI_SYNCHRONIZATION_INVALID_VALUE indicates that the field is not applicable for this record.


-
enumerator SYNCHRONIZATION_FIELD_CUDA_EVENT_SYNC_ID
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds40SYNCHRONIZATION_FIELD_CUDA_EVENT_SYNC_IDE) uint64_t cudaEventSyncId; A unique ID to associate event synchronization records with the latest CUDA Event record.

Similar field is added in CUpti_ActivityCudaEventFieldIds to associate synchronization record to the CUDA Event record.

The same CUDA event can be used multiple times, so the event id will not be unique to correlate the synchronization record with the latest CUDA Event record. This field will be unique and can be used to do the required correlation.

A CUPTI_SYNCHRONIZATION_INVALID_VALUE value indicates that the field is not applicable for this record. Valid only for synchronization records related to CUDA Events.


-
enumerator SYNCHRONIZATION_FIELD_RETURN_VALUE
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds34SYNCHRONIZATION_FIELD_RETURN_VALUEE) uint32_t returnValue; The return value for the synchronization operation.

Use cuptiActivityEnableAllSyncRecords API to enable/disable collection of synchronization records with return value being non-zero. This will be a CUresult value.


-
enumerator SYNCHRONIZATION_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivitySynchronizationFieldIds25SYNCHRONIZATION_FIELD_MAXE) Total number of defined fields.


-
enumerator SYNCHRONIZATION_FIELD_KIND

-
enum CUpti_ActivitySynchronizationType
[#](https://docs.nvidia.com#_CPPv433CUpti_ActivitySynchronizationType) Synchronization type.

The types of synchronization to be used with

[CUpti_ActivitySynchronization2](https://docs.nvidia.com/structCUpti__ActivitySynchronization2.html#structcupti__activitysynchronization2).*Values:*-
enumerator CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivitySynchronizationType43CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_UNKNOWNE) Unknown data.


-
enumerator CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_EVENT_SYNCHRONIZE
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivitySynchronizationType53CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_EVENT_SYNCHRONIZEE) Event synchronize API.


-
enumerator CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_STREAM_WAIT_EVENT
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivitySynchronizationType53CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_STREAM_WAIT_EVENTE) Stream wait event API.


-
enumerator CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_STREAM_SYNCHRONIZE
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivitySynchronizationType54CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_STREAM_SYNCHRONIZEE) Stream synchronize API.


-
enumerator CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_CONTEXT_SYNCHRONIZE
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivitySynchronizationType55CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_CONTEXT_SYNCHRONIZEE) Context synchronize API.


-
enumerator CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivitySynchronizationType45CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_SYNCHRONIZATION_TYPE_UNKNOWN

-
enum CUpti_ActivityThreadIdType
[#](https://docs.nvidia.com#_CPPv426CUpti_ActivityThreadIdType) Thread-Id types.

CUPTI uses different methods to obtain the thread-id depending on the support and the underlying platform. This enum documents these methods for each type. APIs

[cuptiSetThreadIdType](https://docs.nvidia.com#group__cupti__activity__api_1ga1821f090b841d60643ee37d977d9c64a)and[cuptiGetThreadIdType](https://docs.nvidia.com#group__cupti__activity__api_1gabc957f426b741e46d6e9a99a43a974b5)can be used to set and get the thread-id type.*Values:*-
enumerator CUPTI_ACTIVITY_THREAD_ID_TYPE_DEFAULT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityThreadIdType37CUPTI_ACTIVITY_THREAD_ID_TYPE_DEFAULTE) Default type Windows uses API GetCurrentThreadId() Linux/Mac/Android/QNX use POSIX pthread API pthread_self()


-
enumerator CUPTI_ACTIVITY_THREAD_ID_TYPE_SYSTEM
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityThreadIdType36CUPTI_ACTIVITY_THREAD_ID_TYPE_SYSTEME) This type is based on the system API available on the underlying platform and thread-id obtained is supposed to be unique for the process lifetime.

Windows uses API GetCurrentThreadId() Linux uses syscall SYS_gettid Mac uses syscall SYS_thread_selfid Android/QNX use gettid()


-
enumerator CUPTI_ACTIVITY_THREAD_ID_TYPE_SIZE
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityThreadIdType34CUPTI_ACTIVITY_THREAD_ID_TYPE_SIZEE) Add new enums before this field.


-
enumerator CUPTI_ACTIVITY_THREAD_ID_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityThreadIdType39CUPTI_ACTIVITY_THREAD_ID_TYPE_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_THREAD_ID_TYPE_DEFAULT

-
enum CUpti_ActivityUnifiedMemoryAccessType
[#](https://docs.nvidia.com#_CPPv437CUpti_ActivityUnifiedMemoryAccessType) Memory access type for unified memory page faults.

This is valid for

[CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_GPU_PAGE_FAULT](https://docs.nvidia.com#group__cupti__activity__api_1gga601877eb6f7d248a5f538fd74b8fa782a49ecdbc6d0c9b52829c8bc276932b7bf)and[CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_CPU_PAGE_FAULT_COUNT](https://docs.nvidia.com#group__cupti__activity__api_1gga601877eb6f7d248a5f538fd74b8fa782a94faffc246c392748ab7f0de9a858b22)*Values:*-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityUnifiedMemoryAccessType49CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_UNKNOWNE) The unified memory access type is not known.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_READ
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityUnifiedMemoryAccessType46CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_READE) The page fault was triggered by read memory instruction.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_WRITE
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityUnifiedMemoryAccessType47CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_WRITEE) The page fault was triggered by write memory instruction.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_ATOMIC
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityUnifiedMemoryAccessType48CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_ATOMICE) The page fault was triggered by atomic memory instruction.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_PREFETCH
[#](https://docs.nvidia.com#_CPPv4N37CUpti_ActivityUnifiedMemoryAccessType50CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_PREFETCHE) The page fault was triggered by memory prefetch operation.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_ACCESS_TYPE_UNKNOWN

-
enum CUpti_ActivityUnifiedMemoryCounterKind
[#](https://docs.nvidia.com#_CPPv438CUpti_ActivityUnifiedMemoryCounterKind) Kind of the Unified Memory counter.

Many activities are associated with Unified Memory mechanism; among them are transfers from host to device, device to host, page fault at host side.

*Values:*-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind50CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_UNKNOWNE) The unified memory counter kind is not known.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_HTOD
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind62CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_HTODE) Number of bytes transferred from host to device.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_DTOH
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind62CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_DTOHE) Number of bytes transferred from device to host.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_CPU_PAGE_FAULT_COUNT
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind63CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_CPU_PAGE_FAULT_COUNTE) Number of CPU page faults, this is only supported on 64 bit Linux and Mac platforms.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_GPU_PAGE_FAULT
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind57CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_GPU_PAGE_FAULTE) Number of GPU page faults, this is only supported on devices with compute capability 6.0 and higher and 64 bit Linux platforms.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_THRASHING
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind52CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_THRASHINGE) Thrashing occurs when data is frequently accessed by multiple processors and has to be constantly migrated around to achieve data locality.

In this case the overhead of migration may exceed the benefits of locality. This is only supported on 64 bit Linux platforms.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_THROTTLING
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind53CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_THROTTLINGE) Throttling is a prevention technique used by the driver to avoid further thrashing.

Here, the driver doesn’t service the fault for one of the contending processors for a specific period of time, so that the other processor can run at full-speed. This is only supported on 64 bit Linux platforms.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_REMOTE_MAP
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind53CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_REMOTE_MAPE) In case throttling does not help, the driver tries to pin the memory to a processor for a specific period of time.

One of the contending processors will have slow access to the memory, while the other will have fast access. This is only supported on 64 bit Linux platforms.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_DTOD
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind62CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_DTODE) Number of bytes transferred from one device to another device.

This is only supported on 64 bit Linux platforms.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_COUNT
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind48CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_COUNTE)

-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N38CUpti_ActivityUnifiedMemoryCounterKind52CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_UNKNOWN

-
enum CUpti_ActivityUnifiedMemoryCounterScope
[#](https://docs.nvidia.com#_CPPv439CUpti_ActivityUnifiedMemoryCounterScope) Scope of the unified memory counter (deprecated in CUDA 7.0)

*Values:*-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N39CUpti_ActivityUnifiedMemoryCounterScope51CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_UNKNOWNE) The unified memory counter scope is not known.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_PROCESS_SINGLE_DEVICE
[#](https://docs.nvidia.com#_CPPv4N39CUpti_ActivityUnifiedMemoryCounterScope65CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_PROCESS_SINGLE_DEVICEE) Collect unified memory counter for single process on one device.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_PROCESS_ALL_DEVICES
[#](https://docs.nvidia.com#_CPPv4N39CUpti_ActivityUnifiedMemoryCounterScope63CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_PROCESS_ALL_DEVICESE) Collect unified memory counter for single process across all devices.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_COUNT
[#](https://docs.nvidia.com#_CPPv4N39CUpti_ActivityUnifiedMemoryCounterScope49CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_COUNTE)

-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N39CUpti_ActivityUnifiedMemoryCounterScope53CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_FORCE_INTE)

-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_SCOPE_UNKNOWN

-
enum CUpti_ActivityUnifiedMemoryMigrationCause
[#](https://docs.nvidia.com#_CPPv441CUpti_ActivityUnifiedMemoryMigrationCause) Migration cause of the Unified Memory counter.

This is valid for

[CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_HTOD](https://docs.nvidia.com#group__cupti__activity__api_1gga601877eb6f7d248a5f538fd74b8fa782a7c4755228387e83351ae02b5ea5157f1)and[CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_DTOH](https://docs.nvidia.com#group__cupti__activity__api_1gga601877eb6f7d248a5f538fd74b8fa782aef4bdc9da8f158bf337bdf2aedd8d780)and[CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_BYTES_TRANSFER_DTOD](https://docs.nvidia.com#group__cupti__activity__api_1gga601877eb6f7d248a5f538fd74b8fa782a4fe8185509ddecb727197de672cb6e2b)*Values:*-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryMigrationCause53CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_UNKNOWNE) The unified memory migration cause is not known.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_USER
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryMigrationCause50CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_USERE) The unified memory migrated due to an explicit call from the user e.g.

cudaMemPrefetchAsync


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_COHERENCE
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryMigrationCause55CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_COHERENCEE) The unified memory migrated to guarantee data coherence e.g.

CPU/GPU faults on Pascal+ and kernel launch on pre-Pascal GPUs


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_PREFETCH
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryMigrationCause54CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_PREFETCHE) The unified memory was speculatively migrated by the UVM driver before being accessed by the destination processor to improve performance.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_EVICTION
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryMigrationCause54CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_EVICTIONE) The unified memory migrated to the CPU because it was evicted to make room for another block of memory on the GPU.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_ACCESS_COUNTERS
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryMigrationCause61CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_ACCESS_COUNTERSE) The unified memory migrated to another processor because of access counter notifications.

Only frequently accessed pages are migrated between CPU and GPU, or between peer GPUs.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_MIGRATION_CAUSE_UNKNOWN

-
enum CUpti_ActivityUnifiedMemoryRemoteMapCause
[#](https://docs.nvidia.com#_CPPv441CUpti_ActivityUnifiedMemoryRemoteMapCause) Remote memory map cause of the Unified Memory counter.

This is valid for

[CUPTI_ACTIVITY_UNIFIED_MEMORY_COUNTER_KIND_REMOTE_MAP](https://docs.nvidia.com#group__cupti__activity__api_1gga601877eb6f7d248a5f538fd74b8fa782ad6e6079c49b8024aab5afd22c3ec1706)*Values:*-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryRemoteMapCause54CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_UNKNOWNE) The cause of mapping to remote memory was unknown.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_COHERENCE
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryRemoteMapCause56CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_COHERENCEE) Mapping to remote memory was added to maintain data coherence.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_THRASHING
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryRemoteMapCause56CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_THRASHINGE) Mapping to remote memory was added to prevent further thrashing.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_POLICY
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryRemoteMapCause53CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_POLICYE) Mapping to remote memory was added to enforce the hints specified by the programmer or by performance heuristics of the UVM driver.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_OUT_OF_MEMORY
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryRemoteMapCause60CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_OUT_OF_MEMORYE) Mapping to remote memory was added because there is no more memory available on the processor and eviction was not possible.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_EVICTION
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityUnifiedMemoryRemoteMapCause55CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_EVICTIONE) Mapping to remote memory was added after the memory was evicted to make room for another block of memory on the GPU.


-
enumerator CUPTI_ACTIVITY_UNIFIED_MEMORY_REMOTE_MAP_CAUSE_UNKNOWN

-
enum CUpti_ActivityUvmCounterFieldIds
[#](https://docs.nvidia.com#_CPPv432CUpti_ActivityUvmCounterFieldIds) Enum identifiers for fields in

[CUpti_ActivityUnifiedMemoryCounter3](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounter3.html#structcupti__activityunifiedmemorycounter3).Each enum value corresponds to a field in

[CUpti_ActivityUnifiedMemoryCounter3](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounter3.html#structcupti__activityunifiedmemorycounter3)and describes the data type and purpose of that field.*Values:*-
enumerator UVM_COUNTER_FIELD_KIND
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds22UVM_COUNTER_FIELD_KINDE) CUpti_ActivityKind kind; Kind of activity record: CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTER.


-
enumerator UVM_COUNTER_FIELD_COUNTER_KIND
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds30UVM_COUNTER_FIELD_COUNTER_KINDE) CUpti_ActivityUnifiedMemoryCounterKind counterKind; The Unified Memory counter kind.


-
enumerator UVM_COUNTER_FIELD_VALUE
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds23UVM_COUNTER_FIELD_VALUEE) uint64_t value; Value of the counter.


-
enumerator UVM_COUNTER_FIELD_START
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds23UVM_COUNTER_FIELD_STARTE) uint64_t start; Start timestamp of the counter (in ns).


-
enumerator UVM_COUNTER_FIELD_END
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds21UVM_COUNTER_FIELD_ENDE) uint64_t end; End timestamp of the counter (in ns).


-
enumerator UVM_COUNTER_FIELD_ADDRESS
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds25UVM_COUNTER_FIELD_ADDRESSE) uint64_t address; Virtual base address of the page/s being transferred.


-
enumerator UVM_COUNTER_FIELD_SRC_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds24UVM_COUNTER_FIELD_SRC_IDE) uint32_t srcId; ID of the source CPU/device.


-
enumerator UVM_COUNTER_FIELD_DST_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds24UVM_COUNTER_FIELD_DST_IDE) uint32_t dstId; ID of the destination CPU/device.


-
enumerator UVM_COUNTER_FIELD_STREAM_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds27UVM_COUNTER_FIELD_STREAM_IDE) uint32_t streamId; ID of the stream causing the transfer.


-
enumerator UVM_COUNTER_FIELD_PROCESS_ID
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds28UVM_COUNTER_FIELD_PROCESS_IDE) uint32_t processId; ID of the process to which this record belongs.


-
enumerator UVM_COUNTER_FIELD_FLAGS
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds23UVM_COUNTER_FIELD_FLAGSE) uint32_t flags; Flags associated with this record.


-
enumerator UVM_COUNTER_FIELD_PROCESSORS
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds28UVM_COUNTER_FIELD_PROCESSORSE) uint64_t processors[5]; Bitmask of devices involved in the operation.


-
enumerator UVM_COUNTER_FIELD_MAX
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityUvmCounterFieldIds21UVM_COUNTER_FIELD_MAXE) Total number of defined fields.


-
enumerator UVM_COUNTER_FIELD_KIND

-
enum CUpti_ChannelType
[#](https://docs.nvidia.com#_CPPv417CUpti_ChannelType) *Values:*-
enumerator CUPTI_CHANNEL_TYPE_INVALID
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ChannelType26CUPTI_CHANNEL_TYPE_INVALIDE)

-
enumerator CUPTI_CHANNEL_TYPE_COMPUTE
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ChannelType26CUPTI_CHANNEL_TYPE_COMPUTEE) Channel is used for standard work launch and tracking.


-
enumerator CUPTI_CHANNEL_TYPE_ASYNC_MEMCPY
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ChannelType31CUPTI_CHANNEL_TYPE_ASYNC_MEMCPYE) Channel is used by an asynchronous copy engine For confidential compute configurations, work launch and completion are done using the copy engines.


-
enumerator CUPTI_CHANNEL_TYPE_DECOMP
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ChannelType25CUPTI_CHANNEL_TYPE_DECOMPE) Channel is used for memory decompression operations.


-
enumerator CUPTI_CHANNEL_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ChannelType28CUPTI_CHANNEL_TYPE_FORCE_INTE)

-
enumerator CUPTI_CHANNEL_TYPE_INVALID

-
enum CUpti_ComputeEngineCtxSwitchOperationType
[#](https://docs.nvidia.com#_CPPv441CUpti_ComputeEngineCtxSwitchOperationType) The operation type of CUDA context switch event records.

*Values:*-
enumerator CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_INVALID
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ComputeEngineCtxSwitchOperationType49CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_INVALIDE)

-
enumerator CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_START
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ComputeEngineCtxSwitchOperationType47CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_STARTE) The start of the CUDA context switch operation.


-
enumerator CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_END
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ComputeEngineCtxSwitchOperationType45CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_ENDE) The end of the CUDA context switch operation.


-
enumerator CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_COUNT
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ComputeEngineCtxSwitchOperationType47CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_COUNTE)

-
enumerator CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_INVALID

-
enum CUpti_ConfidentialComputeRotationEventType
[#](https://docs.nvidia.com#_CPPv442CUpti_ConfidentialComputeRotationEventType) *Values:*-
enumerator CUPTI_CONFIDENTIAL_COMPUTE_INVALID_ROTATION_EVENT
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ConfidentialComputeRotationEventType49CUPTI_CONFIDENTIAL_COMPUTE_INVALID_ROTATION_EVENTE)

-
enumerator CUPTI_CONFIDENTIAL_COMPUTE_KEY_ROTATION_CHANNEL_BLOCKED
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ConfidentialComputeRotationEventType55CUPTI_CONFIDENTIAL_COMPUTE_KEY_ROTATION_CHANNEL_BLOCKEDE) This channel has been blocked from accepting new CUDA work so a key rotation can be done.


-
enumerator CUPTI_CONFIDENTIAL_COMPUTE_KEY_ROTATION_CHANNEL_DRAINED
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ConfidentialComputeRotationEventType55CUPTI_CONFIDENTIAL_COMPUTE_KEY_ROTATION_CHANNEL_DRAINEDE) This channel remains blocked and all queued CUDA work has completed.

Other clients or channels may cause delays in starting the key rotation.


-
enumerator CUPTI_CONFIDENTIAL_COMPUTE_KEY_ROTATION_CHANNEL_UNBLOCKED
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ConfidentialComputeRotationEventType57CUPTI_CONFIDENTIAL_COMPUTE_KEY_ROTATION_CHANNEL_UNBLOCKEDE) Key rotations have completed and this channel is unblocked.


-
enumerator CUPTI_CONFIDENTIAL_COMPUTE_EVENT_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N42CUpti_ConfidentialComputeRotationEventType47CUPTI_CONFIDENTIAL_COMPUTE_EVENT_TYPE_FORCE_INTE)

-
enumerator CUPTI_CONFIDENTIAL_COMPUTE_INVALID_ROTATION_EVENT

-
enum CUpti_ContextCigMode
[#](https://docs.nvidia.com#_CPPv420CUpti_ContextCigMode) CIG (CUDA in Graphics) Modes.

Describes the CIG modes associated with the CUDA context.

*Values:*-
enumerator CUPTI_CONTEXT_CIG_MODE_NONE
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ContextCigMode27CUPTI_CONTEXT_CIG_MODE_NONEE) Regular (non-CIG) mode.


-
enumerator CUPTI_CONTEXT_CIG_MODE_CIG
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ContextCigMode26CUPTI_CONTEXT_CIG_MODE_CIGE) CIG mode.


-
enumerator CUPTI_CONTEXT_CIG_MODE_CIG_FALLBACK
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ContextCigMode35CUPTI_CONTEXT_CIG_MODE_CIG_FALLBACKE) CIG fallback mode.


-
enumerator CUPTI_CONTEXT_CIG_MODE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ContextCigMode32CUPTI_CONTEXT_CIG_MODE_FORCE_INTE)

-
enumerator CUPTI_CONTEXT_CIG_MODE_NONE

-
enum CUpti_DevType
[#](https://docs.nvidia.com#_CPPv413CUpti_DevType) The device type for device connected to NVLink.

*Values:*-
enumerator CUPTI_DEV_TYPE_INVALID
[#](https://docs.nvidia.com#_CPPv4N13CUpti_DevType22CUPTI_DEV_TYPE_INVALIDE)

-
enumerator CUPTI_DEV_TYPE_GPU
[#](https://docs.nvidia.com#_CPPv4N13CUpti_DevType18CUPTI_DEV_TYPE_GPUE) The device type is GPU.


-
enumerator CUPTI_DEV_TYPE_NPU
[#](https://docs.nvidia.com#_CPPv4N13CUpti_DevType18CUPTI_DEV_TYPE_NPUE) The device type is NVLink processing unit in CPU.


-
enumerator CUPTI_DEV_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N13CUpti_DevType24CUPTI_DEV_TYPE_FORCE_INTE)

-
enumerator CUPTI_DEV_TYPE_INVALID

-
enum CUpti_DeviceGraphLaunchMode
[#](https://docs.nvidia.com#_CPPv427CUpti_DeviceGraphLaunchMode) The launch mode for device graph execution.

*Values:*-
enumerator CUPTI_DEVICE_GRAPH_LAUNCH_MODE_INVALID
[#](https://docs.nvidia.com#_CPPv4N27CUpti_DeviceGraphLaunchMode38CUPTI_DEVICE_GRAPH_LAUNCH_MODE_INVALIDE)

-
enumerator CUPTI_DEVICE_GRAPH_LAUNCH_MODE_FIRE_AND_FORGET
[#](https://docs.nvidia.com#_CPPv4N27CUpti_DeviceGraphLaunchMode46CUPTI_DEVICE_GRAPH_LAUNCH_MODE_FIRE_AND_FORGETE)

-
enumerator CUPTI_DEVICE_GRAPH_LAUNCH_MODE_TAIL
[#](https://docs.nvidia.com#_CPPv4N27CUpti_DeviceGraphLaunchMode35CUPTI_DEVICE_GRAPH_LAUNCH_MODE_TAILE)

-
enumerator CUPTI_DEVICE_GRAPH_LAUNCH_MODE_FIRE_AND_FORGET_AS_SIBLING
[#](https://docs.nvidia.com#_CPPv4N27CUpti_DeviceGraphLaunchMode57CUPTI_DEVICE_GRAPH_LAUNCH_MODE_FIRE_AND_FORGET_AS_SIBLINGE)

-
enumerator CUPTI_DEVICE_GRAPH_LAUNCH_MODE_INVALID

-
enum CUpti_DeviceVirtualizationMode
[#](https://docs.nvidia.com#_CPPv430CUpti_DeviceVirtualizationMode) This indicates the virtualization mode in which CUDA device is running.

*Values:*-
enumerator CUPTI_DEVICE_VIRTUALIZATION_MODE_NONE
[#](https://docs.nvidia.com#_CPPv4N30CUpti_DeviceVirtualizationMode37CUPTI_DEVICE_VIRTUALIZATION_MODE_NONEE) No virtualization mode is associated with the device i.e.

it’s a baremetal GPU


-
enumerator CUPTI_DEVICE_VIRTUALIZATION_MODE_PASS_THROUGH
[#](https://docs.nvidia.com#_CPPv4N30CUpti_DeviceVirtualizationMode45CUPTI_DEVICE_VIRTUALIZATION_MODE_PASS_THROUGHE) The device is associated with the pass-through GPU.

In this mode, an entire physical GPU is directly assigned to one virtual machine (VM).


-
enumerator CUPTI_DEVICE_VIRTUALIZATION_MODE_VIRTUAL_GPU
[#](https://docs.nvidia.com#_CPPv4N30CUpti_DeviceVirtualizationMode44CUPTI_DEVICE_VIRTUALIZATION_MODE_VIRTUAL_GPUE) The device is associated with the virtual GPU (vGPU).

In this mode multiple virtual machines (VMs) have simultaneous, direct access to a single physical GPU.


-
enumerator CUPTI_DEVICE_VIRTUALIZATION_MODE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N30CUpti_DeviceVirtualizationMode42CUPTI_DEVICE_VIRTUALIZATION_MODE_FORCE_INTE)

-
enumerator CUPTI_DEVICE_VIRTUALIZATION_MODE_NONE

-
enum CUpti_EnvironmentClocksThrottleReason
[#](https://docs.nvidia.com#_CPPv437CUpti_EnvironmentClocksThrottleReason) Reasons for clock throttling.

The possible reasons that a clock can be throttled. There can be more than one reason that a clock is being throttled so these types can be combined by bitwise OR. These are used in the clocksThrottleReason field in the Environment Activity Record.

*Values:*-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_GPU_IDLE
[#](https://docs.nvidia.com#_CPPv4N37CUpti_EnvironmentClocksThrottleReason37CUPTI_CLOCKS_THROTTLE_REASON_GPU_IDLEE) Nothing is running on the GPU and the clocks are dropping to idle state.


-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_USER_DEFINED_CLOCKS
[#](https://docs.nvidia.com#_CPPv4N37CUpti_EnvironmentClocksThrottleReason48CUPTI_CLOCKS_THROTTLE_REASON_USER_DEFINED_CLOCKSE) The GPU clocks are limited by a user specified limit.


-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_SW_POWER_CAP
[#](https://docs.nvidia.com#_CPPv4N37CUpti_EnvironmentClocksThrottleReason41CUPTI_CLOCKS_THROTTLE_REASON_SW_POWER_CAPE) A software power scaling algorithm is reducing the clocks below requested clocks.


-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_HW_SLOWDOWN
[#](https://docs.nvidia.com#_CPPv4N37CUpti_EnvironmentClocksThrottleReason40CUPTI_CLOCKS_THROTTLE_REASON_HW_SLOWDOWNE) Hardware slowdown to reduce the clock by a factor of two or more is engaged.

This is an indicator of one of the following: 1) Temperature is too high, 2) External power brake assertion is being triggered (e.g. by the system power supply), 3) Change in power state.


-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N37CUpti_EnvironmentClocksThrottleReason36CUPTI_CLOCKS_THROTTLE_REASON_UNKNOWNE) Some unspecified factor is reducing the clocks.


-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_UNSUPPORTED
[#](https://docs.nvidia.com#_CPPv4N37CUpti_EnvironmentClocksThrottleReason40CUPTI_CLOCKS_THROTTLE_REASON_UNSUPPORTEDE) Throttle reason is not supported for this GPU.


-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_NONE
[#](https://docs.nvidia.com#_CPPv4N37CUpti_EnvironmentClocksThrottleReason33CUPTI_CLOCKS_THROTTLE_REASON_NONEE) No clock throttling.


-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N37CUpti_EnvironmentClocksThrottleReason38CUPTI_CLOCKS_THROTTLE_REASON_FORCE_INTE)

-
enumerator CUPTI_CLOCKS_THROTTLE_REASON_GPU_IDLE

-
enum CUpti_ExternalCorrelationKind
[#](https://docs.nvidia.com#_CPPv429CUpti_ExternalCorrelationKind) The kind of external APIs supported for correlation.

Custom correlation kinds are reserved for usage in external tools.

See also

*Values:*-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_INVALID
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ExternalCorrelationKind39CUPTI_EXTERNAL_CORRELATION_KIND_INVALIDE)

-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ExternalCorrelationKind39CUPTI_EXTERNAL_CORRELATION_KIND_UNKNOWNE) The external API is unknown to CUPTI.


-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_OPENACC
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ExternalCorrelationKind39CUPTI_EXTERNAL_CORRELATION_KIND_OPENACCE) The external API is OpenACC.


-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_CUSTOM0
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ExternalCorrelationKind39CUPTI_EXTERNAL_CORRELATION_KIND_CUSTOM0E) The external API is custom0.


-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_CUSTOM1
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ExternalCorrelationKind39CUPTI_EXTERNAL_CORRELATION_KIND_CUSTOM1E) The external API is custom1.


-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_CUSTOM2
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ExternalCorrelationKind39CUPTI_EXTERNAL_CORRELATION_KIND_CUSTOM2E) The external API is custom2.


-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_SIZE
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ExternalCorrelationKind36CUPTI_EXTERNAL_CORRELATION_KIND_SIZEE) Add new kinds before this line.


-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ExternalCorrelationKind41CUPTI_EXTERNAL_CORRELATION_KIND_FORCE_INTE)

-
enumerator CUPTI_EXTERNAL_CORRELATION_KIND_INVALID

-
enum CUpti_FuncExecutionModel
[#](https://docs.nvidia.com#_CPPv424CUpti_FuncExecutionModel) The execution model of a kernel function.

This should be used to set executionModel field in kernel records.

*Values:*-
enumerator CUPTI_FUNC_EXECUTION_MODEL_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N24CUpti_FuncExecutionModel34CUPTI_FUNC_EXECUTION_MODEL_UNKNOWNE)

-
enumerator CUPTI_FUNC_EXECUTION_MODEL_SIMT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_FuncExecutionModel31CUPTI_FUNC_EXECUTION_MODEL_SIMTE)

-
enumerator CUPTI_FUNC_EXECUTION_MODEL_TILE
[#](https://docs.nvidia.com#_CPPv4N24CUpti_FuncExecutionModel31CUPTI_FUNC_EXECUTION_MODEL_TILEE)

-
enumerator CUPTI_FUNC_EXECUTION_MODEL_HYBRID
[#](https://docs.nvidia.com#_CPPv4N24CUpti_FuncExecutionModel33CUPTI_FUNC_EXECUTION_MODEL_HYBRIDE)

-
enumerator CUPTI_FUNC_EXECUTION_MODEL_SIZE
[#](https://docs.nvidia.com#_CPPv4N24CUpti_FuncExecutionModel31CUPTI_FUNC_EXECUTION_MODEL_SIZEE)

-
enumerator CUPTI_FUNC_EXECUTION_MODEL_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_FuncExecutionModel36CUPTI_FUNC_EXECUTION_MODEL_FORCE_INTE)

-
enumerator CUPTI_FUNC_EXECUTION_MODEL_UNKNOWN

-
enum CUpti_FuncShmemLimitConfig
[#](https://docs.nvidia.com#_CPPv426CUpti_FuncShmemLimitConfig) The shared memory limit per block config for a kernel This should be used to set ‘cudaOccFuncShmemConfig’ field in occupancy calculator API.

*Values:*-
enumerator CUPTI_FUNC_SHMEM_LIMIT_DEFAULT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_FuncShmemLimitConfig30CUPTI_FUNC_SHMEM_LIMIT_DEFAULTE) The shared memory limit config is default.


-
enumerator CUPTI_FUNC_SHMEM_LIMIT_OPTIN
[#](https://docs.nvidia.com#_CPPv4N26CUpti_FuncShmemLimitConfig28CUPTI_FUNC_SHMEM_LIMIT_OPTINE) User has opted for a higher dynamic shared memory limit using function attribute ‘cudaFuncAttributeMaxDynamicSharedMemorySize’ for runtime API or CU_FUNC_ATTRIBUTE_MAX_DYNAMIC_SHARED_SIZE_BYTES for driver API.


-
enumerator CUPTI_FUNC_SHMEM_LIMIT_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_FuncShmemLimitConfig32CUPTI_FUNC_SHMEM_LIMIT_FORCE_INTE)

-
enumerator CUPTI_FUNC_SHMEM_LIMIT_DEFAULT

-
enum CUpti_LinkFlag
[#](https://docs.nvidia.com#_CPPv414CUpti_LinkFlag) Link flags.

Describes link properties, to be used with

[CUpti_ActivityNvLink](https://docs.nvidia.com/structCUpti__ActivityNvLink.html#structcupti__activitynvlink).*Values:*-
enumerator CUPTI_LINK_FLAG_INVALID
[#](https://docs.nvidia.com#_CPPv4N14CUpti_LinkFlag23CUPTI_LINK_FLAG_INVALIDE) The flag is invalid.


-
enumerator CUPTI_LINK_FLAG_PEER_ACCESS
[#](https://docs.nvidia.com#_CPPv4N14CUpti_LinkFlag27CUPTI_LINK_FLAG_PEER_ACCESSE) Is peer to peer access supported by this link.


-
enumerator CUPTI_LINK_FLAG_SYSMEM_ACCESS
[#](https://docs.nvidia.com#_CPPv4N14CUpti_LinkFlag29CUPTI_LINK_FLAG_SYSMEM_ACCESSE) Is system memory access supported by this link.


-
enumerator CUPTI_LINK_FLAG_PEER_ATOMICS
[#](https://docs.nvidia.com#_CPPv4N14CUpti_LinkFlag28CUPTI_LINK_FLAG_PEER_ATOMICSE) Is peer atomic access supported by this link.


-
enumerator CUPTI_LINK_FLAG_SYSMEM_ATOMICS
[#](https://docs.nvidia.com#_CPPv4N14CUpti_LinkFlag30CUPTI_LINK_FLAG_SYSMEM_ATOMICSE) Is system memory atomic access supported by this link.


-
enumerator CUPTI_LINK_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N14CUpti_LinkFlag25CUPTI_LINK_FLAG_FORCE_INTE)

-
enumerator CUPTI_LINK_FLAG_INVALID

-
enum CUpti_NvtxExtPayloadType
[#](https://docs.nvidia.com#_CPPv424CUpti_NvtxExtPayloadType) *Values:*-
enumerator CUPTI_NVTX_EXT_PAYLOAD_TYPE_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N24CUpti_NvtxExtPayloadType35CUPTI_NVTX_EXT_PAYLOAD_TYPE_UNKNOWNE) The payload type is not known.


-
enumerator CUPTI_NVTX_EXT_PAYLOAD_TYPE_SCHEMA
[#](https://docs.nvidia.com#_CPPv4N24CUpti_NvtxExtPayloadType34CUPTI_NVTX_EXT_PAYLOAD_TYPE_SCHEMAE) The payload type is a schema.


-
enumerator CUPTI_NVTX_EXT_PAYLOAD_TYPE_ENUM
[#](https://docs.nvidia.com#_CPPv4N24CUpti_NvtxExtPayloadType32CUPTI_NVTX_EXT_PAYLOAD_TYPE_ENUME) The payload type is an enum.


-
enumerator CUPTI_NVTX_EXT_PAYLOAD_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_NvtxExtPayloadType37CUPTI_NVTX_EXT_PAYLOAD_TYPE_FORCE_INTE)

-
enumerator CUPTI_NVTX_EXT_PAYLOAD_TYPE_UNKNOWN

-
enum CUpti_OpenAccConstructKind
[#](https://docs.nvidia.com#_CPPv426CUpti_OpenAccConstructKind) The OpenAcc parent construct kind for OpenAcc activity records.

*Values:*-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind36CUPTI_OPENACC_CONSTRUCT_KIND_UNKNOWNE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_PARALLEL
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind37CUPTI_OPENACC_CONSTRUCT_KIND_PARALLELE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_KERNELS
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind36CUPTI_OPENACC_CONSTRUCT_KIND_KERNELSE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_LOOP
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind33CUPTI_OPENACC_CONSTRUCT_KIND_LOOPE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_DATA
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind33CUPTI_OPENACC_CONSTRUCT_KIND_DATAE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_ENTER_DATA
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind39CUPTI_OPENACC_CONSTRUCT_KIND_ENTER_DATAE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_EXIT_DATA
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind38CUPTI_OPENACC_CONSTRUCT_KIND_EXIT_DATAE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_HOST_DATA
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind38CUPTI_OPENACC_CONSTRUCT_KIND_HOST_DATAE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_ATOMIC
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind35CUPTI_OPENACC_CONSTRUCT_KIND_ATOMICE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_DECLARE
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind36CUPTI_OPENACC_CONSTRUCT_KIND_DECLAREE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_INIT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind33CUPTI_OPENACC_CONSTRUCT_KIND_INITE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_SHUTDOWN
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind37CUPTI_OPENACC_CONSTRUCT_KIND_SHUTDOWNE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_SET
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind32CUPTI_OPENACC_CONSTRUCT_KIND_SETE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_UPDATE
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind35CUPTI_OPENACC_CONSTRUCT_KIND_UPDATEE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_ROUTINE
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind36CUPTI_OPENACC_CONSTRUCT_KIND_ROUTINEE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_WAIT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind33CUPTI_OPENACC_CONSTRUCT_KIND_WAITE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_RUNTIME_API
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind40CUPTI_OPENACC_CONSTRUCT_KIND_RUNTIME_APIE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26CUpti_OpenAccConstructKind38CUPTI_OPENACC_CONSTRUCT_KIND_FORCE_INTE)

-
enumerator CUPTI_OPENACC_CONSTRUCT_KIND_UNKNOWN

-
enum CUpti_OpenAccEventKind
[#](https://docs.nvidia.com#_CPPv422CUpti_OpenAccEventKind) The OpenAcc event kind for OpenAcc activity records.

See also

CUpti_ActivityKindOpenAcc

*Values:*-
enumerator CUPTI_OPENACC_EVENT_KIND_INVALID
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind32CUPTI_OPENACC_EVENT_KIND_INVALIDE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_DEVICE_INIT
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind36CUPTI_OPENACC_EVENT_KIND_DEVICE_INITE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_DEVICE_SHUTDOWN
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind40CUPTI_OPENACC_EVENT_KIND_DEVICE_SHUTDOWNE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_RUNTIME_SHUTDOWN
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind41CUPTI_OPENACC_EVENT_KIND_RUNTIME_SHUTDOWNE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_ENQUEUE_LAUNCH
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind39CUPTI_OPENACC_EVENT_KIND_ENQUEUE_LAUNCHE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_ENQUEUE_UPLOAD
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind39CUPTI_OPENACC_EVENT_KIND_ENQUEUE_UPLOADE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_ENQUEUE_DOWNLOAD
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind41CUPTI_OPENACC_EVENT_KIND_ENQUEUE_DOWNLOADE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_WAIT
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind29CUPTI_OPENACC_EVENT_KIND_WAITE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_IMPLICIT_WAIT
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind38CUPTI_OPENACC_EVENT_KIND_IMPLICIT_WAITE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_COMPUTE_CONSTRUCT
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind42CUPTI_OPENACC_EVENT_KIND_COMPUTE_CONSTRUCTE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_UPDATE
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind31CUPTI_OPENACC_EVENT_KIND_UPDATEE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_ENTER_DATA
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind35CUPTI_OPENACC_EVENT_KIND_ENTER_DATAE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_EXIT_DATA
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind34CUPTI_OPENACC_EVENT_KIND_EXIT_DATAE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_CREATE
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind31CUPTI_OPENACC_EVENT_KIND_CREATEE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_DELETE
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind31CUPTI_OPENACC_EVENT_KIND_DELETEE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_ALLOC
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind30CUPTI_OPENACC_EVENT_KIND_ALLOCE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_FREE
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind29CUPTI_OPENACC_EVENT_KIND_FREEE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N22CUpti_OpenAccEventKind34CUPTI_OPENACC_EVENT_KIND_FORCE_INTE)

-
enumerator CUPTI_OPENACC_EVENT_KIND_INVALID

-
enum CUpti_OpenMpEventKind
[#](https://docs.nvidia.com#_CPPv421CUpti_OpenMpEventKind) *Values:*-
enumerator CUPTI_OPENMP_EVENT_KIND_INVALID
[#](https://docs.nvidia.com#_CPPv4N21CUpti_OpenMpEventKind31CUPTI_OPENMP_EVENT_KIND_INVALIDE)

-
enumerator CUPTI_OPENMP_EVENT_KIND_PARALLEL
[#](https://docs.nvidia.com#_CPPv4N21CUpti_OpenMpEventKind32CUPTI_OPENMP_EVENT_KIND_PARALLELE)

-
enumerator CUPTI_OPENMP_EVENT_KIND_TASK
[#](https://docs.nvidia.com#_CPPv4N21CUpti_OpenMpEventKind28CUPTI_OPENMP_EVENT_KIND_TASKE)

-
enumerator CUPTI_OPENMP_EVENT_KIND_THREAD
[#](https://docs.nvidia.com#_CPPv4N21CUpti_OpenMpEventKind30CUPTI_OPENMP_EVENT_KIND_THREADE)

-
enumerator CUPTI_OPENMP_EVENT_KIND_IDLE
[#](https://docs.nvidia.com#_CPPv4N21CUpti_OpenMpEventKind28CUPTI_OPENMP_EVENT_KIND_IDLEE)

-
enumerator CUPTI_OPENMP_EVENT_KIND_WAIT_BARRIER
[#](https://docs.nvidia.com#_CPPv4N21CUpti_OpenMpEventKind36CUPTI_OPENMP_EVENT_KIND_WAIT_BARRIERE)

-
enumerator CUPTI_OPENMP_EVENT_KIND_WAIT_TASKWAIT
[#](https://docs.nvidia.com#_CPPv4N21CUpti_OpenMpEventKind37CUPTI_OPENMP_EVENT_KIND_WAIT_TASKWAITE)

-
enumerator CUPTI_OPENMP_EVENT_KIND_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N21CUpti_OpenMpEventKind33CUPTI_OPENMP_EVENT_KIND_FORCE_INTE)

-
enumerator CUPTI_OPENMP_EVENT_KIND_INVALID

-
enum CUpti_PcieDeviceType
[#](https://docs.nvidia.com#_CPPv420CUpti_PcieDeviceType) Field to differentiate whether PCIE Activity record is of a GPU or a PCI Bridge.

*Values:*-
enumerator CUPTI_PCIE_DEVICE_TYPE_GPU
[#](https://docs.nvidia.com#_CPPv4N20CUpti_PcieDeviceType26CUPTI_PCIE_DEVICE_TYPE_GPUE) PCIE GPU record.


-
enumerator CUPTI_PCIE_DEVICE_TYPE_BRIDGE
[#](https://docs.nvidia.com#_CPPv4N20CUpti_PcieDeviceType29CUPTI_PCIE_DEVICE_TYPE_BRIDGEE) PCIE Bridge record.


-
enumerator CUPTI_PCIE_DEVICE_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N20CUpti_PcieDeviceType32CUPTI_PCIE_DEVICE_TYPE_FORCE_INTE)

-
enumerator CUPTI_PCIE_DEVICE_TYPE_GPU

-
enum CUpti_PcieGen
[#](https://docs.nvidia.com#_CPPv413CUpti_PcieGen) PCIE Generation.

Enumeration of PCIE Generation for pcie activity attribute pcieGeneration

*Values:*-
enumerator CUPTI_PCIE_GEN_GEN1
[#](https://docs.nvidia.com#_CPPv4N13CUpti_PcieGen19CUPTI_PCIE_GEN_GEN1E) PCIE Generation 1.


-
enumerator CUPTI_PCIE_GEN_GEN2
[#](https://docs.nvidia.com#_CPPv4N13CUpti_PcieGen19CUPTI_PCIE_GEN_GEN2E) PCIE Generation 2.


-
enumerator CUPTI_PCIE_GEN_GEN3
[#](https://docs.nvidia.com#_CPPv4N13CUpti_PcieGen19CUPTI_PCIE_GEN_GEN3E) PCIE Generation 3.


-
enumerator CUPTI_PCIE_GEN_GEN4
[#](https://docs.nvidia.com#_CPPv4N13CUpti_PcieGen19CUPTI_PCIE_GEN_GEN4E) PCIE Generation 4.


-
enumerator CUPTI_PCIE_GEN_GEN5
[#](https://docs.nvidia.com#_CPPv4N13CUpti_PcieGen19CUPTI_PCIE_GEN_GEN5E) PCIE Generation 5.


-
enumerator CUPTI_PCIE_GEN_GEN6
[#](https://docs.nvidia.com#_CPPv4N13CUpti_PcieGen19CUPTI_PCIE_GEN_GEN6E) PCIE Generation 6.


-
enumerator CUPTI_PCIE_GEN_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N13CUpti_PcieGen24CUPTI_PCIE_GEN_FORCE_INTE)

-
enumerator CUPTI_PCIE_GEN_GEN1

## 6.1.8. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityConfigurePCSampling( *CUcontext ctx*,,[CUpti_ActivityPCSamplingConfig](https://docs.nvidia.com/structCUpti__ActivityPCSamplingConfig.html#_CPPv430CUpti_ActivityPCSamplingConfig)*configSet PC sampling configuration.

For Pascal and older GPU architectures this API must be called before enabling activity kind CUPTI_ACTIVITY_KIND_PC_SAMPLING. There is no such requirement for Volta and newer GPU architectures.

For Volta and newer GPU architectures if this API is called in the middle of execution, PC sampling configuration will be updated for subsequent kernel launches.

Starting with CUDA 13.0, this function is unsupported and should not be used. It always returns the error code CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED.

- Parameters:
**ctx**– The context**config**– A pointer to[CUpti_ActivityPCSamplingConfig](https://docs.nvidia.com/structCUpti__ActivityPCSamplingConfig.html#structcupti__activitypcsamplingconfig)structure containing PC sampling configuration.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_OPERATION**– if this api is called while some valid event collection method is set.**CUPTI_ERROR_INVALID_PARAMETER**– if`config`

is NULL or any parameter in the`config`

structures is not a valid value**CUPTI_ERROR_NOT_SUPPORTED**– Indicates that the system/device does not support the unified memory counters



[#](https://docs.nvidia.com#_CPPv432cuptiActivityConfigurePCSampling9CUcontextP30CUpti_ActivityPCSamplingConfig)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityConfigureUnifiedMemoryCounter( ,[CUpti_ActivityUnifiedMemoryCounterConfig](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounterConfig.html#_CPPv440CUpti_ActivityUnifiedMemoryCounterConfig)*config*uint32_t count*,Set Unified Memory Counter configuration.

Set the configuration before enabling the corresponding activity kind CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTER. The API should be called after CUDA driver initialization.

- Parameters:
**config**– A pointer to[CUpti_ActivityUnifiedMemoryCounterConfig](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounterConfig.html#structcupti__activityunifiedmemorycounterconfig)structures containing Unified Memory counter configuration.**count**– Number of Unified Memory counter configuration structures

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`config`

is NULL or any parameter in the`config`

structures is not a valid value**CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED**– One potential reason is that platform (OS/arch) does not support the unified memory counters**CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED_ON_DEVICE**– Indicates that the device does not support the unified memory counters**CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED_ON_NON_P2P_DEVICES**– Indicates that multi-GPU configuration without P2P support between any pair of devices does not support the unified memory counters



[#](https://docs.nvidia.com#_CPPv442cuptiActivityConfigureUnifiedMemoryCounterP40CUpti_ActivityUnifiedMemoryCounterConfig8uint32_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityDisable()[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv420cuptiActivityDisable18CUpti_ActivityKind) Disable collection of a specific kind of activity record.

Disable collection of a specific kind of activity record. Multiple kinds can be disabled by calling this function multiple times. By default all activity kinds are disabled for collection.

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityDisable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga550569082abf3e8c017114881b9f7832). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**kind**– The kind of activity record to stop collecting- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_KIND**– if the activity kind is not supported



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityDisableContext( *CUcontext context*,,[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)kindDisable collection of a specific kind of activity record for a context.

Disable collection of a specific kind of activity record for a context. This setting done by this API will supersede the global settings for activity records. Multiple kinds can be enabled by calling this function multiple times.

- Parameters:
**context**– The context for which activity is to be disabled**kind**– The kind of activity record to stop collecting

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_KIND**– if the activity kind is not supported



[#](https://docs.nvidia.com#_CPPv427cuptiActivityDisableContext9CUcontext18CUpti_ActivityKind)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityDisable_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)kind,[CUpti_ActivityConfig](https://docs.nvidia.com/structCUpti__ActivityConfig.html#_CPPv420CUpti_ActivityConfig)*pActivityConfigDisable collection of a specific kind of activity record for the subscriber.

Disable collection of a specific kind of activity record. Multiple kinds can be disabled by calling this function multiple times. By default all activity kinds are disabled for collection.

- Parameters:
**subscriber**– The subscriber handle.**kind**– The kind of activity record to stop collecting**pActivityConfig**– The activity config. It can be NULL.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_KIND**– if the activity kind is not supported



[#](https://docs.nvidia.com#_CPPv423cuptiActivityDisable_v222CUpti_SubscriberHandle18CUpti_ActivityKindP20CUpti_ActivityConfig)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnable()[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv419cuptiActivityEnable18CUpti_ActivityKind) Enable collection of a specific kind of activity record.

Enable collection of a specific kind of activity record. Multiple kinds can be enabled by calling this function multiple times. By default all activity kinds are disabled for collection.

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**kind**– The kind of activity record to collect- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_NOT_COMPATIBLE**– if the activity kind cannot be enabled**CUPTI_ERROR_INVALID_KIND**– if the activity kind is not supported



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableAllSyncRecords(*uint8_t enable*)[#](https://docs.nvidia.com#_CPPv433cuptiActivityEnableAllSyncRecords7uint8_t) Enables collecting records for all synchronization operations.

CUPTI provides CUDA event query and stream query records via CUPTI_ACTIVITY_KIND_SYNCHRONIZATION. Using this API, CUPTI client can disable to record CUDA event query and stream query records for queries for which the operations have not yet been completed on the CUDA event/stream.

By default, the record is generated for all CUDA events and stream irrespective of whether the operations have been completed on the CUDA event/stream.

Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_ENABLE_ALL_SYNC_RECORDS](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6aa28a70b12b14922174ab36c3e80bee8a), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**enable**– is a boolean, denoting whether to enable or disable the collection of all CUDA event query and stream query records- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableAllocationSource(*uint8_t enable*)[#](https://docs.nvidia.com#_CPPv435cuptiActivityEnableAllocationSource7uint8_t) Enables tracking the source library for memory allocation requests.

This API is used to control whether or not we track the source library of memory allocation requests. Default value is 0, i.e. it is not tracked. The activity kind CUPTI_ACTIVITY_KIND_MEMORY2 needs to be enabled, and if this flag is set, we get the full path of the shared object responsible for the GPU memory allocation request in the member source in the

[CUpti_ActivityMemory4](https://docs.nvidia.com/structCUpti__ActivityMemory4.html#structcupti__activitymemory4)records. Also note that this feature adds runtime overhead.Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_ENABLE_ALLOCATION_SOURCE_TRACKING](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a547b4e0f0f34ea780127ec8cb501673e), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**enable**– is a boolean, denoting whether the source library of the memory allocation request needs to be tracked- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableAndDump()[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv426cuptiActivityEnableAndDump18CUpti_ActivityKind) Enable collection of a specific kind of activity record.

For certain activity kinds it dumps existing records.

In general, the behavior of this API is similar to the API

[cuptiActivityEnable](https://docs.nvidia.com#group__cupti__activity__api_1ga348cf81393b39ab2f89604aaaa8defc2)i.e. it enables the collection of a specific kind of activity record. Additionally, this API can help in dumping the records for activities which happened in the past before enabling the corresponding activity kind. The API allows to get records for the current resource allocations done in CUDA For CUPTI_ACTIVITY_KIND_DEVICE, existing device records are dumped For CUPTI_ACTIVITY_KIND_CONTEXT, existing context records are dumped For CUPTI_ACTIVITY_KIND_STREAM, existing stream records are dumped For CUPTI_ACTIVITY_KIND_ NVLINK, existing NVLINK records are dumped For CUPTI_ACTIVITY_KIND_PCIE, existing PCIE records are dumped For other activities, the behavior is similar to the API[cuptiActivityEnable](https://docs.nvidia.com#group__cupti__activity__api_1ga348cf81393b39ab2f89604aaaa8defc2)Device records are emitted in CUPTI on CUDA driver initialization. Those records can only be retrieved by the user if CUPTI is attached before CUDA initialization. Context and stream records are emitted on context and stream creation. The use case of the API is to provide the records for CUDA resources (contexts/streams/devices) that are currently active if user late attaches CUPTI.

Before calling this function, the user must register buffer callbacks to get the activity records by calling

[cuptiActivityRegisterCallbacks](https://docs.nvidia.com#group__cupti__activity__api_1ga237e2401b0ce69dcb265b1f9079f0b65). If the user does not register the buffers and calls API[cuptiActivityEnableAndDump](https://docs.nvidia.com#group__cupti__activity__api_1ga12080fe6fdacf80869db472e41b98027), then CUPTI will enable the activity kind but not provide any records for that activity kind.Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityEnableAndDump_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3303f9ceb4eb1d604f00985badb3c7ea). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**kind**– The kind of activity record to collect- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_UNKNOWN**– if buffer is not initialized.**CUPTI_ERROR_NOT_COMPATIBLE**– if the activity kind cannot be enabled**CUPTI_ERROR_INVALID_KIND**– if the activity kind is not supported



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableAndDump_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)kind,[CUpti_ActivityConfig](https://docs.nvidia.com/structCUpti__ActivityConfig.html#_CPPv420CUpti_ActivityConfig)*activityConfigEnable collection of a specific kind of activity record.

For certain activity kinds it dumps existing records.

In general, the behavior of this API is similar to the API

[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)i.e. it enables the collection of a specific kind of activity record. Additionally, this API can help in dumping the records for activities which happened in the past before enabling the corresponding activity kind. The API allows to get records for the current resource allocations done in CUDA For CUPTI_ACTIVITY_KIND_DEVICE, existing device records are dumped For CUPTI_ACTIVITY_KIND_CONTEXT, existing context records are dumped For CUPTI_ACTIVITY_KIND_STREAM, existing stream records are dumped For CUPTI_ACTIVITY_KIND_ NVLINK, existing NVLINK records are dumped For CUPTI_ACTIVITY_KIND_PCIE, existing PCIE records are dumped For other activities, the behavior is similar to the API[cuptiActivityEnable](https://docs.nvidia.com#group__cupti__activity__api_1ga348cf81393b39ab2f89604aaaa8defc2)Device records are emitted in CUPTI on CUDA driver initialization. Those records can only be retrieved by the user if CUPTI is attached before CUDA initialization. Context and stream records are emitted on context and stream creation. The use case of the API is to provide the records for CUDA resources (contexts/streams/devices) that are currently active if user late attaches CUPTI.

Before calling this function, the user must register buffer callbacks to get the activity records by calling

[cuptiActivityRegisterCallbacks_v2](https://docs.nvidia.com#group__cupti__activity__api_1gacbe1ba1b75f76472038cb2fd34d84e09). If the user does not register the buffers and calls API[cuptiActivityEnableAndDump_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3303f9ceb4eb1d604f00985badb3c7ea), then CUPTI will enable the activity kind but not provide any records for that activity kind.- Parameters:
**subscriber**– The subscriber handle.**kind**– The kind of activity record to collect**activityConfig**– The activity config. It can be NULL.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_UNKNOWN**– if buffer is not initialized.**CUPTI_ERROR_NOT_COMPATIBLE**– if the activity kind cannot be enabled**CUPTI_ERROR_INVALID_KIND**– if the activity kind is not supported



[#](https://docs.nvidia.com#_CPPv429cuptiActivityEnableAndDump_v222CUpti_SubscriberHandle18CUpti_ActivityKindP20CUpti_ActivityConfig)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableContext( *CUcontext context*,,[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)kindEnable collection of a specific kind of activity record for a context.

Enable collection of a specific kind of activity record for a context. This setting done by this API will supersede the global settings for activity records enabled by

[cuptiActivityEnable](https://docs.nvidia.com#group__cupti__activity__api_1ga348cf81393b39ab2f89604aaaa8defc2). Multiple kinds can be enabled by calling this function multiple times.- Parameters:
**context**– The context for which activity is to be enabled**kind**– The kind of activity record to collect

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_NOT_COMPATIBLE**– if the activity kind cannot be enabled**CUPTI_ERROR_INVALID_KIND**– if the activity kind is not supported



[#](https://docs.nvidia.com#_CPPv426cuptiActivityEnableContext9CUcontext18CUpti_ActivityKind)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableCudaEventDeviceTimestamps( *uint8_t enable*,Enable/Disable collecting device timestamp for CUPTI_ACTIVITY_KIND_CUDA_EVENT record.

CUPTI provides device timestamps via ‘deviceTimestamp’ field in CUPTI_ACTIVITY_KIND_CUDA_EVENT records. Using this API, CUPTI client can enable or disable the collection of CUDA event device timestamps. By default, the collection of CUDA event device timestamps is disabled.

Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_ENABLE_CUDA_EVENT_DEVICE_TIMESTAMPS](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a0ff4f3341fcb3207a47457fca8d210db), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**enable**– is a boolean, denoting whether to enable or disable the collection of CUDA event device timestamps- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–



[#](https://docs.nvidia.com#_CPPv444cuptiActivityEnableCudaEventDeviceTimestamps7uint8_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableDeviceGraph(*uint8_t enable*)[#](https://docs.nvidia.com#_CPPv430cuptiActivityEnableDeviceGraph7uint8_t) Controls the collection of records for device launched graphs.

This API is used to control the collection of records for device launched graphs. Default value is 0, i.e. these records are not collected. If the kind CUPTI_ACTIVITY_KIND_GRAPH_TRACE is selected, then CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE records will also be emitted for device graphs. This applies for both Hardware Event System (HES) and SW instrumentation method. Otherwise records for device graphs will be collected at node granularity and the field ‘isDeviceLaunched’ for memcpy, memset and kernel records will be set for device graph nodes. This collection is done only if Hardware Event System (HES) is enabled. This API needs to be called before initialization of CUDA and this setting should not be changed during the profiling session.

Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_ENABLE_DEVICE_GRAPH_TRACE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a3e71698ae85745fdefa78a9028470f2b), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**enable**– is a boolean, denoting whether these records should be collected- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableDriverApi( ,[CUpti_CallbackId](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv416CUpti_CallbackId)cbid*uint8_t enable*,Controls the collection of activity records for specific CUDA Driver APIs.

Activity kind CUPTI_ACTIVITY_KIND_DRIVER controls the collection of either all CUDA Driver APIs or none. API cuptiActivityEnableDriverApi can be used for fine-grained control, it allows enabling/disabling tracing of a specific set of CUDA Driver APIs. To disable collection of a small set of CUDA Driver APIs, user can first enable the collection of all Driver APIs using the activity kind CUPTI_ACTIVITY_KIND_DRIVER and call this API to disable specific Driver APIs. And to enable the collection of a small set of CUDA Driver APIs, user can call this API without using the activity kind CUPTI_ACTIVITY_KIND_DRIVER.

Note: Activity kind CUPTI_ACTIVITY_KIND_DRIVER overrides the settings done by this API if it is called after the API.

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityEnableDriverApi_v2](https://docs.nvidia.com#group__cupti__activity__api_1gac4ce555fd7cd1c2dacfff655629c198c). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**cbid**– callback id of the CUDA Driver API. This can be found in the header cupti_driver_cbid.h.**enable**– is a boolean, denoting whether to enable or disable the collection

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–



[#](https://docs.nvidia.com#_CPPv428cuptiActivityEnableDriverApi16CUpti_CallbackId7uint8_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableDriverApi_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_CallbackId](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv416CUpti_CallbackId)cbid*uint8_t enable*,Controls the collection of activity records for specific CUDA Driver APIs for a given subscriber.

This is the per-subscriber version of

[cuptiActivityEnableDriverApi](https://docs.nvidia.com#group__cupti__activity__api_1gaada27f148dd634f0c7466db1cb2a6a78). It allows each subscriber to independently enable or disable tracing of specific CUDA Driver APIs.Note

This API is supported with user-defined activity records (see

[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)with[CUpti_ActivityConfig::fieldSelection](https://docs.nvidia.com/structCUpti__ActivityConfig.html#structcupti__activityconfig_1a0b2c250f1cc0fce05421a909644c0a9c)). When using user-defined records, the activity kind must first be registered via[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)before calling this API to control per-cbid collection. Support for cbid filtering with user-defined records requires CUPTI_API_VERSION 130400 or later.Note

If cbid-level filtering is only needed at enable time and does not change thereafter, the

[CUpti_ActivityApiCbidOptions](https://docs.nvidia.com/structCUpti__ActivityApiCbidOptions.html#structcupti__activityapicbidoptions)allowlist/denylist passed through[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)is a simpler alternative to calling this API per cbid.- Parameters:
**subscriber**– Handle to the subscriber. Must have been previously created via[cuptiSubscribe_v2](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga817004c126bedadf956162f20de18491).**cbid**– callback id of the CUDA Driver API.**enable**– is a boolean, denoting whether to enable or disable the collection

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if the subscriber handle is invalid or cbid is out of range



[#](https://docs.nvidia.com#_CPPv431cuptiActivityEnableDriverApi_v222CUpti_SubscriberHandle16CUpti_CallbackId7uint8_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableHWTrace(*uint8_t enable*)[#](https://docs.nvidia.com#_CPPv426cuptiActivityEnableHWTrace7uint8_t) Enables CUDA kernel timestamp collection via Hardware Event System (HES).

This API enables hardware-based collection of CUDA kernel timestamps as an alternative to the traditional software instrumentation and semaphore-based approach. HES-based collection provides lower overhead and more accurate timing measurements.

This API must be called after CUDA driver initialization but before creating the CUDA context. As a generic solution, this API can be called from the CUPTI_CBID_RESOURCE_CU_INIT_FINISHED callback. Once enabled, HES-based tracing persists for the entire profiling session and cannot be disabled.

This API can also be called before CUDA driver initialization. After driver initialization, CUPTI may switch to traditional semaphore-based tracing and return error through callback with domain CUPTI_CB_DOMAIN_STATE if HES-based tracing cannot be supported.

Note

This feature is only available on NVIDIA Blackwell architecture and later.

Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_ENABLE_HES](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a14e0aa6c612db191463aef08debfba6e), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**enable**– is a boolean flag to enable (true) HES-based timestamp collection.- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_SUPPORTED**– if HW trace cannot be enabled on the current platform**CUPTI_ERROR_VIRTUALIZED_DEVICE_NOT_SUPPORTED**–**CUPTI_ERROR_CONFIDENTIAL_COMPUTING_NOT_SUPPORTED**–**CUPTI_ERROR_CMP_DEVICE_NOT_SUPPORTED**–**CUPTI_ERROR_MIG_DEVICE_NOT_SUPPORTED**–**CUPTI_ERROR_SLI_DEVICE_NOT_SUPPORTED**–**CUPTI_ERROR_WSL_DEVICE_NOT_SUPPORTED**–**CUPTI_ERROR_HES_TRACE_NOT_SUPPORTED_ON_MPS**–



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableLatencyTimestamps(*uint8_t enable*)[#](https://docs.nvidia.com#_CPPv436cuptiActivityEnableLatencyTimestamps7uint8_t) Controls the collection of queued and submitted timestamps for kernels.

This API is used to control the collection of queued and submitted timestamps for kernels whose records are provided through the struct

[CUpti_ActivityKernel13](https://docs.nvidia.com/structCUpti__ActivityKernel13.html#structcupti__activitykernel13). Default value is 0, i.e. these timestamps are not collected. This API needs to be called before initialization of CUDA and this setting should not be changed during the profiling session.This API is not supported if the HW trace is enabled through the API

[cuptiActivityEnableHWTrace](https://docs.nvidia.com#group__cupti__activity__api_1gaa8f1642a87b1ef876014c766e798f534).Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_ENABLE_KERNEL_LATENCY_TIMESTAMPS](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6aa33a966f717b6648bee4b189f576bb83), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**enable**– is a boolean, denoting whether these timestamps should be collected- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableLaunchAttributes(*uint8_t enable*)[#](https://docs.nvidia.com#_CPPv435cuptiActivityEnableLaunchAttributes7uint8_t) Controls the collection of launch attributes for kernels.

This API is used to control the collection of launch attributes for kernels whose records are provided through the struct

[CUpti_ActivityKernel13](https://docs.nvidia.com/structCUpti__ActivityKernel13.html#structcupti__activitykernel13). Default value is 0, i.e. these attributes are not collected.Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_ENABLE_KERNEL_LAUNCH_ATTRIBUTES](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a4a2dffd50799d80031f86466bbd4c973), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**enable**– is a boolean denoting whether these launch attributes should be collected


-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableRuntimeApi( ,[CUpti_CallbackId](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv416CUpti_CallbackId)cbid*uint8_t enable*,Controls the collection of activity records for specific CUDA Runtime APIs.

Activity kind CUPTI_ACTIVITY_KIND_RUNTIME controls the collection of either all CUDA Runtime APIs or none. API cuptiActivityEnableRuntimeApi can be used for fine-grained control, it allows enabling/disabling tracing of a specific set of CUDA Runtime APIs. To disable collection of a small set of CUDA Runtime APIs, user can first enable the collection of all Runtime APIs using the activity kind CUPTI_ACTIVITY_KIND_RUNTIME and call this API to disable specific Runtime APIs. And to enable the collection of a small set of CUDA Runtime APIs, user can call this API without using the activity kind CUPTI_ACTIVITY_KIND_RUNTIME.

Note: Activity kind CUPTI_ACTIVITY_KIND_RUNTIME overrides the settings done by this API if it is called after the API.

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityEnableRuntimeApi_v2](https://docs.nvidia.com#group__cupti__activity__api_1gafb1a4d0b599b9fc3f23d303e608d7ccd). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**cbid**– callback id of the CUDA Runtime API. This can be found in the header cupti_runtime_cbid.h.**enable**– is a boolean, denoting whether to enable or disable the collection

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–



[#](https://docs.nvidia.com#_CPPv429cuptiActivityEnableRuntimeApi16CUpti_CallbackId7uint8_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnableRuntimeApi_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_CallbackId](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv416CUpti_CallbackId)cbid*uint8_t enable*,Controls the collection of activity records for specific CUDA Runtime APIs for a given subscriber.

This is the per-subscriber version of

[cuptiActivityEnableRuntimeApi](https://docs.nvidia.com#group__cupti__activity__api_1gaaad5fd7a8f998e475588623eb65dac9a). It allows each subscriber to independently enable or disable tracing of specific CUDA Runtime APIs.Note

This API is supported with user-defined activity records (see

[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)with[CUpti_ActivityConfig::fieldSelection](https://docs.nvidia.com/structCUpti__ActivityConfig.html#structcupti__activityconfig_1a0b2c250f1cc0fce05421a909644c0a9c)). When using user-defined records, the activity kind must first be registered via[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)before calling this API to control per-cbid collection. Support for cbid filtering with user-defined records requires CUPTI_API_VERSION 130400 or later.Note

If cbid-level filtering is only needed at enable time and does not change thereafter, the

[CUpti_ActivityApiCbidOptions](https://docs.nvidia.com/structCUpti__ActivityApiCbidOptions.html#structcupti__activityapicbidoptions)allowlist/denylist passed through[cuptiActivityEnable_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga563584d948863ce4d7688847096149d2)is a simpler alternative to calling this API per cbid.- Parameters:
**subscriber**– Handle to the subscriber. Must have been previously created via[cuptiSubscribe_v2](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga817004c126bedadf956162f20de18491).**cbid**– callback id of the CUDA Runtime API.**enable**– is a boolean, denoting whether to enable or disable the collection

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if the subscriber handle is invalid or cbid is out of range



[#](https://docs.nvidia.com#_CPPv432cuptiActivityEnableRuntimeApi_v222CUpti_SubscriberHandle16CUpti_CallbackId7uint8_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityEnable_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)kind,[CUpti_ActivityConfig](https://docs.nvidia.com/structCUpti__ActivityConfig.html#_CPPv420CUpti_ActivityConfig)*pActivityConfigEnable collection of a specific kind of activity record for the subscriber.

Enable collection of a specific kind of activity record. Multiple kinds can be enabled by calling this function multiple times. By default all activity kinds are disabled for collection.

- Parameters:
**subscriber**– The subscriber handle.**kind**– The kind of activity record to collect**pActivityConfig**– The activity config. It can be NULL.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_NOT_COMPATIBLE**– if the activity kind cannot be enabled**CUPTI_ERROR_INVALID_KIND**– if the activity kind is not supported



[#](https://docs.nvidia.com#_CPPv422cuptiActivityEnable_v222CUpti_SubscriberHandle18CUpti_ActivityKindP20CUpti_ActivityConfig)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityFlush( *CUcontext context*,*uint32_t streamId*,*uint32_t flag*,Wait for all activity records to be delivered via the completion callback.

This function does not return until all activity records associated with the specified context/stream are returned to the CUPTI client using the callback registered in cuptiActivityRegisterCallbacks. To ensure that all activity records are complete, the requested stream(s), if any, are synchronized.

If

`context`

is NULL, the global activity records (i.e. those not associated with a particular stream) are flushed (in this case no streams are synchronized). If`context`

is a valid CUcontext and`streamId`

is 0, the buffers of all streams of this context are flushed. Otherwise, the buffers of the specified stream in this context is flushed.Before calling this function, the buffer handling callback api must be activated by calling cuptiActivityRegisterCallbacks.

**DEPRECATED**This method is deprecated CONTEXT and STREAMID will be ignored. Use cuptiActivityFlushAll to flush all data. Calling restrictions are the same as for cuptiActivityFlushAll.- Parameters:
**context**– A valid CUcontext or NULL.**streamId**– The stream ID.**flag**– The flag can be set to indicate a forced flush. See CUpti_ActivityFlag

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_CUPTI_ERROR_INVALID_OPERATION**– if not preceded by a successful call to cuptiActivityRegisterCallbacks**CUPTI_ERROR_UNKNOWN**– an internal error occurred



[#](https://docs.nvidia.com#_CPPv418cuptiActivityFlush9CUcontext8uint32_t8uint32_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityFlushAll(*uint32_t flag*)[#](https://docs.nvidia.com#_CPPv421cuptiActivityFlushAll8uint32_t) Request to deliver activity records via the buffer completion callback.

This function returns the activity records associated with all contexts/streams (and the global buffers not associated with any stream) to the CUPTI client using the callback registered in cuptiActivityRegisterCallbacks.

This is a blocking call but it doesn’t issue any CUDA synchronization calls implicitly thus it’s not guaranteed that all activities are completed on the underlying devices. Activity record is considered as completed if it has all the information filled up including the timestamps if any. It is the client’s responsibility to issue necessary CUDA synchronization calls before calling this function if all activity records with complete information are expected to be delivered.

Behavior of the function based on the input flag: (-) ::For default flush i.e. when flag is set as 0, it returns all the activity buffers which have all the activity records completed, buffers need not to be full though. It doesn’t return buffers which have one or more incomplete records. Default flush can be done at a regular interval in a separate thread. (-) ::For forced flush i.e. when flag CUPTI_ACTIVITY_FLAG_FLUSH_FORCED is passed to the function, it returns all the activity buffers including the ones which have one or more incomplete activity records. It’s suggested for clients to do the force flush before the termination of the profiling session to allow remaining buffers to be delivered. In general, it can be done in the at-exit handler.

Before calling this function, the buffer handling callback api must be activated by calling cuptiActivityRegisterCallbacks.

This function can be called from application or control threads outside a CUPTI callback. If called from a CUPTI callback, it must be called only from API trace callbacks in CUPTI_CB_DOMAIN_RUNTIME_API or CUPTI_CB_DOMAIN_DRIVER_API callback domains. Do not call this function from activity buffer callbacks or any other non-API-trace callbacks, including callbacks related to state, resource, synchronization, launch, memory operations, or graph activity.

When multiple subscribers are allowed, the buffers of all subscribers are flushed with the same flag. It is not possible to flush the buffers of only a specific subscriber.

See also

- Parameters:
**flag**– The flag can be set to indicate a forced flush. See CUpti_ActivityFlag- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_OPERATION**– if not preceded by a successful call to cuptiActivityRegisterCallbacks**CUPTI_ERROR_UNKNOWN**– an internal error occurred



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityFlushPeriod(*uint32_t time*)[#](https://docs.nvidia.com#_CPPv424cuptiActivityFlushPeriod8uint32_t) Sets the flush period for the worker thread.

CUPTI creates a worker thread to minimize the perturbance for the application created threads. CUPTI offloads certain operations from the application threads to the worker thread, this includes synchronization of profiling resources between host and device, delivery of the activity buffers to the client using the callback registered in cuptiActivityRegisterCallbacks. For performance reasons, CUPTI wakes up the worker thread based on certain heuristics.

This API is used to control the flush period of the worker thread. This setting will override the CUPTI heuristics. Setting time to zero disables the periodic flush and restores the default behavior.

Periodic flush can return only those activity buffers which are full and have all the activity records completed.

It’s allowed to use the API

[cuptiActivityFlushAll](https://docs.nvidia.com#group__cupti__activity__api_1gabae7160b2db7e97247a0d23812e373eb)to flush the data on-demand, even when client sets the periodic flush.See also

- Parameters:
**time**– flush period in milliseconds (ms)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityGetAttribute( ,[CUpti_ActivityAttribute](https://docs.nvidia.com#_CPPv423CUpti_ActivityAttribute)attr*size_t *valueSize*,*void *value*,Read an activity API attribute.

Read an activity API attribute and return it in

`*value`

. In case of multiple subscribers, use cuptiActivityGetAttribute_v2 to read the attribute for the subscriber.Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**attr**– The attribute to read**valueSize**– Size of buffer pointed by the value, and returns the number of bytes written to`value`

**value**– Returns the value of the attribute

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`valueSize`

or`value`

is NULL, or if`attr`

is not an activity attribute**CUPTI_ERROR_PARAMETER_SIZE_NOT_SUFFICIENT**– Indicates that the`value`

buffer is too small to hold the attribute value.



[#](https://docs.nvidia.com#_CPPv425cuptiActivityGetAttribute23CUpti_ActivityAttributeP6size_tPv)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityGetAttribute_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_ActivityAttribute](https://docs.nvidia.com#_CPPv423CUpti_ActivityAttribute)attr*size_t *valueSize*,*void *value*,Read an activity API attribute.

This function is similar to cuptiActivityGetAttribute. Note that in case of multiple subscribers, only cuptiActivityGetAttribute_v2 can be used to read the attribute for the subscriber.

Read an activity API attribute and return it in

`*value`

.- Parameters:
**subscriber**– The subscriber handle.**attr**– The attribute to read**valueSize**– Size of buffer pointed by the value, and returns the number of bytes written to`value`

**value**– Returns the value of the attribute

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`valueSize`

or`value`

is NULL, or if`attr`

is not an activity attribute**CUPTI_ERROR_PARAMETER_SIZE_NOT_SUFFICIENT**– Indicates that the`value`

buffer is too small to hold the attribute value.



[#](https://docs.nvidia.com#_CPPv428cuptiActivityGetAttribute_v222CUpti_SubscriberHandle23CUpti_ActivityAttributeP6size_tPv)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityGetEnabledKinds( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)*buffer*uint32_t *bufferSize*,*uint32_t *enabledKindsCount*,Get the enabled activity kinds for a subscriber.

Note

If the provided buffer size is not sufficient to store all the enabled activity kinds, we populate the buffer with as much as we can, but return the true value of the number of enabled activity kinds in

`enabledKindsCount`

.- Parameters:
**subscriber**– The subscriber handle. If NULL, the union of activity kinds enabled across all subscribers is returned.**buffer**– The buffer to store the enabled activity kinds. If NULL, the number of enabled activity kinds is returned in`enabledKindsCount`

.**bufferSize**– The size of the buffer. If NULL, only the number of enabled activity kinds is returned in`enabledKindsCount`

. If NULL and`buffer`

is not NULL, CUPTI_ERROR_INVALID_PARAMETER is returned.**enabledKindsCount**– The number of enabled activity kinds. If NULL, CUPTI_ERROR_INVALID_PARAMETER is returned.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`enabledKindsCount`

is NULL or if`subscriber`

is invalid.



[#](https://docs.nvidia.com#_CPPv428cuptiActivityGetEnabledKinds22CUpti_SubscriberHandleP18CUpti_ActivityKindP8uint32_tP8uint32_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityGetNextRecord( *uint8_t *buffer*,*size_t validBufferSizeBytes*,,[CUpti_Activity](https://docs.nvidia.com/structCUpti__Activity.html#_CPPv414CUpti_Activity)**recordIterate over the activity records in a buffer.

This is a helper function to iterate over the activity records in a buffer. A buffer of activity records is typically obtained by receiving a CUpti_BuffersCallbackCompleteFunc callback. Stop iterating the buffer when an error occurs.

An example of typical usage:

CUpti_Activity *record = NULL; CUptiResult status = CUPTI_SUCCESS; do { status = cuptiActivityGetNextRecord(buffer, validSize, &record); if(status == CUPTI_SUCCESS) { // Use record here... } else if (status == CUPTI_ERROR_MAX_LIMIT_REACHED) break; else if (status == CUPTI_ERROR_INVALID_KIND) break; else { goto Error; } } while (1);

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityGetNextRecord_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga1fecc132589644064b6e67a5f0407245). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**buffer**– The buffer containing activity records**record**– Inputs the previous record returned by cuptiActivityGetNextRecord and returns the next activity record from the buffer. If input value is NULL, returns the first activity record in the buffer. Records of certain kinds like CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL may contain invalid (0) timestamps, indicating that no timing information could be collected for lack of device memory.**validBufferSizeBytes**– The number of valid bytes in the buffer.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_MAX_LIMIT_REACHED**– if no more records in the buffer**CUPTI_ERROR_INVALID_PARAMETER**– if`buffer`

is NULL.**CUPTI_ERROR_INVALID_KIND**– if activity record is either incomplete or invalid



[#](https://docs.nvidia.com#_CPPv426cuptiActivityGetNextRecordP7uint8_t6size_tPP14CUpti_Activity)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityGetNextRecord_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber*uint8_t *buffer*,*size_t validBufferSizeBytes*,,[CUpti_Activity](https://docs.nvidia.com/structCUpti__Activity.html#_CPPv414CUpti_Activity)**recordIterate over the activity records in the supplied buffer.

This function is similar to

[cuptiActivityGetNextRecord](https://docs.nvidia.com#group__cupti__activity__api_1gab397f490a0df4a1633ea7b6e2420294f)and accepts a subscriber handle. It should be used instead of[cuptiActivityGetNextRecord](https://docs.nvidia.com#group__cupti__activity__api_1gab397f490a0df4a1633ea7b6e2420294f)when using subscriber-aware V2 APIs.An example of typical usage:

CUpti_Activity *record = NULL; CUptiResult status = CUPTI_SUCCESS; do { status = cuptiActivityGetNextRecord_v2(subscriber, buffer, validSize, &record); if(status == CUPTI_SUCCESS) { // Use record here... } else if (status == CUPTI_ERROR_MAX_LIMIT_REACHED) break; else if (status == CUPTI_ERROR_INVALID_KIND) break; else { goto Error; } } while (1);

- Parameters:
**subscriber**– Handle to the subscriber whose record layout should be used.**buffer**– The buffer containing activity records**validBufferSizeBytes**– The number of valid bytes in the buffer.**record**– Inputs the previous record returned by cuptiActivityGetNextRecord_v2 and returns the next activity record from the buffer. If input value is NULL, returns the first activity record in the buffer.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_MAX_LIMIT_REACHED**– if no more records in the buffer**CUPTI_ERROR_INVALID_PARAMETER**– if`subscriber`

,`buffer`

or`record`

is NULL.**CUPTI_ERROR_INVALID_KIND**– if activity record is either incomplete or invalid



[#](https://docs.nvidia.com#_CPPv429cuptiActivityGetNextRecord_v222CUpti_SubscriberHandleP7uint8_t6size_tPP14CUpti_Activity)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityGetNumDroppedRecords( *CUcontext context*,*uint32_t streamId*,*size_t *dropped*,Get the number of activity records that were dropped of insufficient buffer space.

Get the number of records that were dropped because of insufficient buffer space. The dropped count includes records that could not be recorded because CUPTI did not have activity buffer space available for the record (because the CUpti_BuffersCallbackRequestFunc callback did not return an empty buffer of sufficient size) and also CDP records that could not be record because the device-size buffer was full (size is controlled by the CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE_CDP attribute). The dropped count maintained for the queue is reset to zero when this function is called.

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityGetNumDroppedRecords_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ad9ec6b9519ff9e5ff89bc0d825cdd2). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**context**– The context, or NULL to get dropped count from global queue**streamId**– The stream ID**dropped**– The number of records that were dropped since the last call to this function.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`dropped`

is NULL



[#](https://docs.nvidia.com#_CPPv433cuptiActivityGetNumDroppedRecords9CUcontext8uint32_tP6size_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityGetNumDroppedRecords_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber*CUcontext context*,*uint32_t streamId*,*size_t *dropped*,Get the number of dropped activity records for a specific subscriber.

This is the per-subscriber version of

[cuptiActivityGetNumDroppedRecords](https://docs.nvidia.com#group__cupti__activity__api_1ga496d13eb1f4f4fcce37ce3f3434c5e4a).Note

This API resets the subscriber’s dropped record count to 0 after reading.

- Parameters:
**subscriber**– The subscriber handle**context**– CUDA context (reserved for future use)**streamId**– Stream ID (reserved for future use)**dropped**– Returns the number of dropped records

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_INVALID_PARAMETER**– if`subscriber`

or`dropped`

is NULL



[#](https://docs.nvidia.com#_CPPv436cuptiActivityGetNumDroppedRecords_v222CUpti_SubscriberHandle9CUcontext8uint32_tP6size_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityGetStructSize( ,[CUpti_ActivityKind](https://docs.nvidia.com#_CPPv418CUpti_ActivityKind)activityKind*uint32_t version*,*size_t *activityStructSize*,Get the size of the activity struct for a given CUPTI version.

This API is applicable only for predefined activity structs.

- Parameters:
**activityKind**– The activity kind to get the size for.**activityStructSize**– The size of the activity struct.**version**– The version of the CUPTI API. If 0, returns size for current version. If non-zero, returns size for the specified version. The version format is xxyyzz, e.g., 130000 for CUPTI 13.0, 130100 for CUPTI 13.1. The version of CUPTI can be queried using cuptiGetVersion API. Only versions >= 130000 are supported.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`activityStructSize`

is NULL**CUPTI_ERROR_INVALID_KIND**– if`activityKind`

is invalid.**CUPTI_ERROR_NOT_SUPPORTED**– if`version`

is non-zero and is less than 130000.



[#](https://docs.nvidia.com#_CPPv426cuptiActivityGetStructSize18CUpti_ActivityKind8uint32_tP6size_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityPopExternalCorrelationId( ,[CUpti_ExternalCorrelationKind](https://docs.nvidia.com#_CPPv429CUpti_ExternalCorrelationKind)kind*uint64_t *lastId*,Pop an external correlation id for the calling thread.

This function notifies CUPTI that the calling thread is leaving an external API region.

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityPopExternalCorrelationId_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga7dc13d2d4d28c976ac6d811d1107dbb3). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**kind**– The kind of external API activities should be correlated with.**lastId**– If the function returns successful, contains the last external correlation id for this`kind`

, can be NULL.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– The external API kind is invalid.**CUPTI_ERROR_QUEUE_EMPTY**– No external id is currently associated with`kind`

.



[#](https://docs.nvidia.com#_CPPv437cuptiActivityPopExternalCorrelationId29CUpti_ExternalCorrelationKindP8uint64_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityPopExternalCorrelationId_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_ExternalCorrelationKind](https://docs.nvidia.com#_CPPv429CUpti_ExternalCorrelationKind)kind*uint64_t *lastId*,Pop an external correlation id for a specific subscriber.

Subscriber aware V2 version of

[cuptiActivityPopExternalCorrelationId](https://docs.nvidia.com#group__cupti__activity__api_1ga47395bf12ff55f30822d408b940567e3). This allows each subscriber to maintain its own external correlation context.- Parameters:
**subscriber**– The subscriber handle.**kind**– The kind of external API to pop correlation for.**lastId**– Returns the last external correlation id popped, can be NULL.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if subscriber or kind is invalid.**CUPTI_ERROR_QUEUE_EMPTY**– No external id is currently associated with`kind`

for this subscriber.



[#](https://docs.nvidia.com#_CPPv440cuptiActivityPopExternalCorrelationId_v222CUpti_SubscriberHandle29CUpti_ExternalCorrelationKindP8uint64_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityPushExternalCorrelationId( ,[CUpti_ExternalCorrelationKind](https://docs.nvidia.com#_CPPv429CUpti_ExternalCorrelationKind)kind*uint64_t id*,Push an external correlation id for the calling thread.

This function notifies CUPTI that the calling thread is entering an external API region. When a CUPTI activity API record is created while within an external API region and CUPTI_ACTIVITY_KIND_EXTERNAL_CORRELATION is enabled, the activity API record will be preceded by a

[CUpti_ActivityExternalCorrelation](https://docs.nvidia.com/structCUpti__ActivityExternalCorrelation.html#structcupti__activityexternalcorrelation)record for each[CUpti_ExternalCorrelationKind](https://docs.nvidia.com#group__cupti__activity__api_1ga9ac4ae6e6237e99db3f8b4c66df2f9aa).Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityPushExternalCorrelationId_v2](https://docs.nvidia.com#group__cupti__activity__api_1gaca9e4785bd022998e5f194c8101db4f2). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**kind**– The kind of external API activities should be correlated with.**id**– External correlation id.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– The external API kind is invalid



[#](https://docs.nvidia.com#_CPPv438cuptiActivityPushExternalCorrelationId29CUpti_ExternalCorrelationKind8uint64_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityPushExternalCorrelationId_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_ExternalCorrelationKind](https://docs.nvidia.com#_CPPv429CUpti_ExternalCorrelationKind)kind*uint64_t id*,Push an external correlation id for a specific subscriber.

Subscriber aware V2 version of

[cuptiActivityPushExternalCorrelationId](https://docs.nvidia.com#group__cupti__activity__api_1ga2c373f1be967db0227fa4d42a593d1a0). This allows each subscriber to maintain its own external correlation context.- Parameters:
**subscriber**– The subscriber handle.**kind**– The kind of external API activities should be correlated with.**id**– External correlation id.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if subscriber or kind is invalid.



[#](https://docs.nvidia.com#_CPPv441cuptiActivityPushExternalCorrelationId_v222CUpti_SubscriberHandle29CUpti_ExternalCorrelationKind8uint64_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityRegisterCallbacks( ,[CUpti_BuffersCallbackRequestFunc](https://docs.nvidia.com#_CPPv432CUpti_BuffersCallbackRequestFunc)funcBufferRequested,[CUpti_BuffersCallbackCompleteFunc](https://docs.nvidia.com#_CPPv433CUpti_BuffersCallbackCompleteFunc)funcBufferCompletedRegisters callback functions with CUPTI for activity buffer handling.

This function registers two callback functions to be used in asynchronous buffer handling. If registered, activity record buffers are handled using asynchronous requested/completed callbacks from CUPTI.

Registering these callbacks prevents the client from using CUPTI’s blocking enqueue/dequeue functions.

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivityRegisterCallbacks_v2](https://docs.nvidia.com#group__cupti__activity__api_1gacbe1ba1b75f76472038cb2fd34d84e09). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**funcBufferRequested**– callback which is invoked when an empty buffer is requested by CUPTI**funcBufferCompleted**– callback which is invoked when a buffer containing activity records is available from CUPTI

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if either`funcBufferRequested`

or`funcBufferCompleted`

is NULL



[#](https://docs.nvidia.com#_CPPv430cuptiActivityRegisterCallbacks32CUpti_BuffersCallbackRequestFunc33CUpti_BuffersCallbackCompleteFunc)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityRegisterCallbacks_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_BuffersCallbackRequestFunc_v2](https://docs.nvidia.com#_CPPv435CUpti_BuffersCallbackRequestFunc_v2)funcBufferRequested,[CUpti_BuffersCallbackCompleteFunc_v2](https://docs.nvidia.com#_CPPv436CUpti_BuffersCallbackCompleteFunc_v2)funcBufferCompletedRegisters callback functions with CUPTI for activity buffer handling for the subscriber.

This function registers two callback functions to be used in asynchronous buffer handling. If registered, activity record buffers are handled using asynchronous requested/completed callbacks from CUPTI.

Registering these callbacks prevents the client from using CUPTI’s blocking enqueue/dequeue functions.

- Parameters:
**subscriber**– The subscriber handle.**funcBufferRequested**– callback which is invoked when an empty buffer is requested by CUPTI**funcBufferCompleted**– callback which is invoked when a buffer containing activity records is available from CUPTI

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if either`funcBufferRequested`

or`funcBufferCompleted_v2`

is NULL



[#](https://docs.nvidia.com#_CPPv433cuptiActivityRegisterCallbacks_v222CUpti_SubscriberHandle35CUpti_BuffersCallbackRequestFunc_v236CUpti_BuffersCallbackCompleteFunc_v2)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivityRegisterTimestampCallback( ,[CUpti_TimestampCallbackFunc](https://docs.nvidia.com#_CPPv427CUpti_TimestampCallbackFunc)funcTimestampRegisters callback function with CUPTI for providing timestamp.

This function registers a callback function to obtain timestamp of user’s choice instead of using CUPTI provided timestamp. By default CUPTI uses different methods, based on the underlying platform, to retrieve the timestamp Linux (x86_64, aarch64 sbsa, aarch64) uses clock_gettime(CLOCK_REALTIME) Windows uses QueryPerformanceCounter() WSL (Windows Subsystem for Linux) uses clock_gettime(CLOCK_MONOTONIC_RAW) as CLOCK_REALTIME can cause backward jumps. QNX uses ClockCycles() Timestamps retrieved using these methods are converted to nanosecond if needed before usage.

Timestamps for GPU activities such as kernels, memory copies and memset operations are recorded directly on the GPU. To provide a unified and normalized view of these timestamps in relation to CPU time, CUPTI performs a linear interpolation to convert GPU timestamps into CPU timestamps during post-processing. For activities where timestamps are captured on the GPU, the timestamp callback is invoked during the post-processing phase, while converting GPU timestamps into CPU timestamps. For activities for which timestamps are captured directly on the CPU, the timestamp callback is invoked immediately at the time of the activity.

The registration of timestamp callback should be done before any of the CUPTI activity kinds are enabled to make sure that all the records report the timestamp using the callback function registered through cuptiActivityRegisterTimestampCallback API.

Changing the timestamp callback function in CUPTI through cuptiActivityRegisterTimestampCallback API in the middle of the profiling session can cause records generated prior to the change to report timestamps through previous timestamp method.

Note

This API will be deprecated in a future release. In CUDA 13.4 and later, the corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_TIMESTAMP_CALLBACK](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6aa1fbc417df466cf304818955dc570b46), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**funcTimestamp**– callback which is invoked when a timestamp is needed by CUPTI- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`funcTimestamp`

is NULL**CUPTI_ERROR_NOT_INITIALIZED**–



[#](https://docs.nvidia.com#_CPPv438cuptiActivityRegisterTimestampCallback27CUpti_TimestampCallbackFunc)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivitySetAttribute( ,[CUpti_ActivityAttribute](https://docs.nvidia.com#_CPPv423CUpti_ActivityAttribute)attr*size_t *valueSize*,*void *value*,Write an activity API attribute.

Write an activity API attribute. In case of multiple subscribers, use cuptiActivitySetAttribute_v2 to write the attribute for the subscriber.

Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**attr**– The attribute to write**valueSize**– The size, in bytes, of the value**value**– The attribute value to write

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_NOT_SUPPORTED**– if multiple subscribers are not allowed.**CUPTI_ERROR_INVALID_PARAMETER**– if`valueSize`

or`value`

is NULL, or if`attr`

is not an activity attribute**CUPTI_ERROR_PARAMETER_SIZE_NOT_SUFFICIENT**– Indicates that the`value`

buffer is too small to hold the attribute value.



[#](https://docs.nvidia.com#_CPPv425cuptiActivitySetAttribute23CUpti_ActivityAttributeP6size_tPv)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiActivitySetAttribute_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_ActivityAttribute](https://docs.nvidia.com#_CPPv423CUpti_ActivityAttribute)attr*size_t *valueSize*,*void *value*,Write an activity API attribute.

Write an activity API attribute. In case of multiple subscribers, use cuptiActivitySetAttribute_v2 to write the attribute for the subscriber.

- Parameters:
**subscriber**– The subscriber handle.**attr**– The attribute to write**valueSize**– The size, in bytes, of the value**value**– The attribute value to write

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`valueSize`

or`value`

is NULL, or if`attr`

is not an activity attribute**CUPTI_ERROR_PARAMETER_SIZE_NOT_SUFFICIENT**– Indicates that the`value`

buffer is too small to hold the attribute value.



[#](https://docs.nvidia.com#_CPPv428cuptiActivitySetAttribute_v222CUpti_SubscriberHandle23CUpti_ActivityAttributeP6size_tPv)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiComputeCapabilitySupported( *int major*,*int minor*,*int *support*,Check support for a compute capability.

This function is used to check the support for a device based on it’s compute capability. It sets the

`support`

when the compute capability is supported by the current version of CUPTI, and clears it otherwise. This version of CUPTI might not support all GPUs sharing the same compute capability. It is suggested to use API[cuptiDeviceSupported](https://docs.nvidia.com#group__cupti__activity__api_1ga2493c952b9ceccf953ade5a6816fefdb)which provides correct information.See also

- Parameters:
**major**– The major revision number of the compute capability**minor**– The minor revision number of the compute capability**support**– Pointer to an integer to return the support status

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`support`

is NULL



[#](https://docs.nvidia.com#_CPPv431cuptiComputeCapabilitySupportediiPi)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiDeviceSupported(*CUdevice dev*,*int *support*)[#](https://docs.nvidia.com#_CPPv420cuptiDeviceSupported8CUdevicePi) Check support for a compute device.

This function is used to check the support for a compute device. It sets the

`support`

when the device is supported by the current version of CUPTI, and clears it otherwise.See also

- Parameters:
**dev**– The device handle returned by CUDA Driver API cuDeviceGet**support**– Pointer to an integer to return the support status

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`support`

is NULL**CUPTI_ERROR_INVALID_DEVICE**– if`dev`

is not a valid device



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiDeviceVirtualizationMode( *CUdevice dev*,,[CUpti_DeviceVirtualizationMode](https://docs.nvidia.com#_CPPv430CUpti_DeviceVirtualizationMode)*modeQuery the virtualization mode of the device.

This function is used to query the virtualization mode of the CUDA device.

- Parameters:
**dev**– The device handle returned by CUDA Driver API cuDeviceGet**mode**– Pointer to an CUpti_DeviceVirtualizationMode to return the virtualization mode

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_DEVICE**– if`dev`

is not a valid device**CUPTI_ERROR_INVALID_PARAMETER**– if`mode`

is NULL



[#](https://docs.nvidia.com#_CPPv429cuptiDeviceVirtualizationMode8CUdeviceP30CUpti_DeviceVirtualizationMode)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiFinalize(*void*)[#](https://docs.nvidia.com#_CPPv413cuptiFinalizev) Detach CUPTI from the running process.

This API detaches the CUPTI from the running process. It destroys and cleans up all the resources associated with CUPTI in the current process. After CUPTI detaches from the process, the process will keep on running with no CUPTI attached to it. For safe operation of the API, it is recommended this API is invoked from the exit callsite of any of the CUDA Driver or Runtime API. Otherwise CUPTI client needs to make sure that required CUDA synchronization and CUPTI activity buffer flush is done before calling the API. Sample code showing the usage of the API in the cupti callback handler code:

void CUPTIAPI cuptiCallbackHandler(void *userdata, CUpti_CallbackDomain domain, CUpti_CallbackId cbid, void *cbdata) { const CUpti_CallbackData *cbInfo = (CUpti_CallbackData *)cbdata; // Take this code path when CUPTI detach is requested if (detachCupti) { switch(domain) { case CUPTI_CB_DOMAIN_RUNTIME_API: case CUPTI_CB_DOMAIN_DRIVER_API: if (cbInfo->callbackSite == CUPTI_API_EXIT) { // call the CUPTI detach API cuptiFinalize(); } break; default: break; } } }


-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetAutoBoostState( *CUcontext context*,,[CUpti_ActivityAutoBoostState](https://docs.nvidia.com/structCUpti__ActivityAutoBoostState.html#_CPPv428CUpti_ActivityAutoBoostState)*stateGet auto boost state.

The profiling results can be inconsistent in case auto boost is enabled. CUPTI tries to disable auto boost while profiling. It can fail to disable in cases where user does not have the permissions or CUDA_AUTO_BOOST env variable is set. The function can be used to query whether auto boost is enabled.

- Parameters:
**context**– A valid CUcontext.**state**– A pointer to[CUpti_ActivityAutoBoostState](https://docs.nvidia.com/structCUpti__ActivityAutoBoostState.html#structcupti__activityautobooststate)structure which contains the current state and the id of the process that has requested the current state

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`CUcontext`

or`state`

is NULL**CUPTI_ERROR_NOT_SUPPORTED**– Indicates that the device does not support auto boost**CUPTI_ERROR_UNKNOWN**– an internal error occurred



[#](https://docs.nvidia.com#_CPPv422cuptiGetAutoBoostState9CUcontextP28CUpti_ActivityAutoBoostState)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetContextId(*CUcontext context*,*uint32_t *contextId*)[#](https://docs.nvidia.com#_CPPv417cuptiGetContextId9CUcontextP8uint32_t) Get the ID of a context.

Get the ID of a context.

- Parameters:
**context**– The context**contextId**– Returns a process-unique ID for the context

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_CONTEXT**– The context is NULL or not valid.**CUPTI_ERROR_INVALID_PARAMETER**– if`contextId`

is NULL



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetCudaEventId(*CUevent event*,*uint32_t *pEventId*)[#](https://docs.nvidia.com#_CPPv419cuptiGetCudaEventId7CUeventP8uint32_t) Get the unique ID of a CUDA event.

Returns the unique ID of the CUDA event. The ID matches the eventId field reported in

[CUpti_ActivityCudaEvent2](https://docs.nvidia.com/structCUpti__ActivityCudaEvent2.html#structcupti__activitycudaevent2)activity records.- Parameters:
**event**– The CUDA event.**pEventId**– Returns the unique ID of the event.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`event`

or`pEventId`

is NULL



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetDeviceId(*CUcontext context*,*uint32_t *deviceId*)[#](https://docs.nvidia.com#_CPPv416cuptiGetDeviceId9CUcontextP8uint32_t) Get the ID of a device.

If

`context`

is NULL, returns the ID of the device that contains the currently active context. If`context`

is non-NULL, returns the ID of the device which contains that context. Operates in a similar manner to cudaGetDevice() or cuCtxGetDevice() but may be called from within callback functions.- Parameters:
**context**– The context, or NULL to indicate the current context.**deviceId**– Returns the ID of the device that is current for the calling thread.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_DEVICE**– if unable to get device ID**CUPTI_ERROR_INVALID_PARAMETER**– if`deviceId`

is NULL



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetGraphExecId(*CUgraphExec graphExec*,*uint32_t *pId*)[#](https://docs.nvidia.com#_CPPv419cuptiGetGraphExecId11CUgraphExecP8uint32_t) Get the unique ID of executable graph.

Returns the unique ID of executable CUDA graph.

- Parameters:
**graphExec**– The executable graph.**pId**– Returns the unique ID of the executable graph

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`graph`

is NULL



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetGraphId(*CUgraph graph*,*uint32_t *pId*)[#](https://docs.nvidia.com#_CPPv415cuptiGetGraphId7CUgraphP8uint32_t) Get the unique ID of graph.

Returns the unique ID of CUDA graph.

- Parameters:
**graph**– The graph.**pId**– Returns the unique ID of the graph

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`graph`

is NULL



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetGraphNodeId(*CUgraphNode node*,*uint64_t *nodeId*)[#](https://docs.nvidia.com#_CPPv419cuptiGetGraphNodeId11CUgraphNodeP8uint64_t) Get the unique ID of a graph node.

Returns the unique ID of the CUDA graph node.

- Parameters:
**node**– The graph node.**nodeId**– Returns the unique ID of the node

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_PARAMETER**– if`node`

is NULL



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetLastError(*void*)[#](https://docs.nvidia.com#_CPPv417cuptiGetLastErrorv) Returns the last error from a cupti call or callback.

Returns the last error that has been produced by any of the cupti api calls or the callback in the same host thread and resets it to CUPTI_SUCCESS.


-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetStreamId( *CUcontext context*,*CUstream stream*,*uint32_t *streamId*,Get the ID of a stream.

Get the ID of a stream. The stream ID is unique within a context (i.e. all streams within a context will have unique stream IDs).

**DEPRECATED**This method is deprecated as of CUDA 8.0. Use method cuptiGetStreamIdEx instead.- Parameters:
**context**– If non-NULL then the stream is checked to ensure that it belongs to this context. Typically this parameter should be null.**stream**– The stream**streamId**– Returns a context-unique ID for the stream

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_STREAM**– if unable to get stream ID, or if`context`

is non-NULL and`stream`

does not belong to the context**CUPTI_ERROR_INVALID_PARAMETER**– if`streamId`

is NULL



[#](https://docs.nvidia.com#_CPPv416cuptiGetStreamId9CUcontext8CUstreamP8uint32_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetStreamIdEx( *CUcontext context*,*CUstream stream*,*uint8_t perThreadStream*,*uint32_t *streamId*,Get the ID of a stream.

Get the ID of a stream. The stream ID is unique within a context (i.e. all streams within a context will have unique stream IDs).

- Parameters:
**context**– If non-NULL then the stream is checked to ensure that it belongs to this context. Typically this parameter should be null.**stream**– The stream**perThreadStream**– Flag to indicate if program is compiled for per-thread streams**streamId**– Returns a context-unique ID for the stream

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**–**CUPTI_ERROR_INVALID_STREAM**– if unable to get stream ID, or if`context`

is non-NULL and`stream`

does not belong to the context**CUPTI_ERROR_INVALID_PARAMETER**– if`streamId`

is NULL



[#](https://docs.nvidia.com#_CPPv418cuptiGetStreamIdEx9CUcontext8CUstream7uint8_tP8uint32_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetThreadIdType()[CUpti_ActivityThreadIdType](https://docs.nvidia.com#_CPPv426CUpti_ActivityThreadIdType)*type[#](https://docs.nvidia.com#_CPPv420cuptiGetThreadIdTypeP26CUpti_ActivityThreadIdType) Get the thread-id type.

Returns the thread-id type used in CUPTI This API is not supported when multiple subscribers are allowed.

Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_THREAD_ID_TYPE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a66e86f013312c2145c96ada722be96d2), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`type`

is NULL



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetTimestamp(*uint64_t *timestamp*)[#](https://docs.nvidia.com#_CPPv417cuptiGetTimestampP8uint64_t) Get the CUPTI timestamp.

Returns a timestamp normalized to correspond with the start and end timestamps reported in the CUPTI activity records. The timestamp is reported in nanoseconds.

Note

This API will be deprecated in a future release. In CUDA 13.4 and later, the corresponding V2 API is

[cuptiGetTimestamp_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga47495782fa9a5d6b128bfa569f3dec2d). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**timestamp**– Returns the CUPTI timestamp- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`timestamp`

is NULL



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetTimestamp_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv422CUpti_SubscriberHandle)subscriber*uint64_t *timestamp*,Get the CUPTI timestamp.

If a subscriber registers a particular timestamp callback, this API will use that callback to get the timestamp. In CUDA 13.3, this API falls back to

[cuptiGetTimestamp()](https://docs.nvidia.com#group__cupti__activity__api_1ga7d8294c686b5293237a6daae8eae3dde). In CUDA 13.4 and later, this API provides the timestamp callback registered by the requesting subscriber.Returns a timestamp normalized to correspond with the start and end timestamps reported in the CUPTI activity records. The timestamp is reported in nanoseconds.

- Parameters:
**subscriber**– The subscriber handle**timestamp**– Returns the CUPTI timestamp

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`timestamp`

is NULL or`subscriber`

is NULL



[#](https://docs.nvidia.com#_CPPv420cuptiGetTimestamp_v222CUpti_SubscriberHandleP8uint64_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiIsTracingSessionRunning(*uint8_t *isRunning*)[#](https://docs.nvidia.com#_CPPv428cuptiIsTracingSessionRunningP7uint8_t) Check whether a CUPTI tracing session is still running.

This API returns true if a CUPTI library is already loaded by another CUPTI user by using any CUPTI API. This API returns false when CUPTI is finalized and there is no CUPTI currently loaded and active. Can be used to determine if it is safe to unload your CUPTI based tool. Note that this API itself does not load the CUPTI library, it merely checks if a CUPTI library is already loaded by another CUPTI user.

- Parameters:
**isRunning**– Returns whether the tracing session is still running.- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`isRunning`

is NULL.**CUPTI_ERROR_UNKNOWN**– if an unknown error occurred.



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSetThreadIdType()[CUpti_ActivityThreadIdType](https://docs.nvidia.com#_CPPv426CUpti_ActivityThreadIdType)type[#](https://docs.nvidia.com#_CPPv420cuptiSetThreadIdType26CUpti_ActivityThreadIdType) Set the thread-id type.

CUPTI uses the method corresponding to set type to generate the thread-id. See enum

[CUpti_ActivityThreadIdType](https://docs.nvidia.com#group__cupti__activity__api_1gac6fcebeb84a89d8f1862d31338efd4c5)for the list of methods. Activity records having thread-id field contain the same value. Thread id type must not be changed during the profiling session to avoid thread-id value mismatch across activity records. This API is not supported when multiple subscribers are allowed.Note

This API will be deprecated in a future release. The corresponding V2 activity attribute is

[CUPTI_ACTIVITY_ATTR_THREAD_ID_TYPE](https://docs.nvidia.com#group__cupti__activity__api_1gga1c31fe3f8ea0e46c6c20dd454a6caab6a66e86f013312c2145c96ada722be96d2), which can be queried or modified via[cuptiActivityGetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga3ab1442a04b4a17fc81c332b037863b4)and[cuptiActivitySetAttribute_v2](https://docs.nvidia.com#group__cupti__activity__api_1ga0bccac4c9713063bd383a208fe23ceeb). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_SUPPORTED**– if`type`

is not supported on the platform



## 6.1.9. Typedefs[#](https://docs.nvidia.com#id4)

-
typedef void (*CUpti_BuffersCallbackCompleteFunc)(CUcontext context, uint32_t streamId, uint8_t *buffer, size_t size, size_t validSize)
[#](https://docs.nvidia.com#_CPPv433CUpti_BuffersCallbackCompleteFunc) Function type for callback used by CUPTI to return a buffer of activity records.

This callback function returns to the CUPTI client a buffer containing activity records. The buffer contains

`validSize`

bytes of activity records which should be read using cuptiActivityGetNextRecord. The number of dropped records can be read using cuptiActivityGetNumDroppedRecords. After this call CUPTI relinquished ownership of the buffer and will not use it anymore. The client may return the buffer to CUPTI using the CUpti_BuffersCallbackRequestFunc callback. Note: CUDA 6.0 onwards, all buffers returned by this callback are global buffers i.e. there is no context/stream specific buffer. User needs to parse the global buffer to extract the context/stream specific activity records.- Param context:
The context this buffer is associated with. If NULL, the buffer is associated with the global activities. This field is deprecated as of CUDA 6.0 and will always be NULL.

- Param streamId:
The stream id this buffer is associated with. This field is deprecated as of CUDA 6.0 and will always be NULL.

- Param buffer:
The activity record buffer.

- Param size:
The total size of the buffer in bytes as set in CUpti_BuffersCallbackRequestFunc.

- Param validSize:
The number of valid bytes in the buffer.



-
typedef void (*CUpti_BuffersCallbackCompleteFunc_v2)(uint8_t *buffer, size_t size, size_t validSize,
[CUpti_BufferCallbackCompleteInfo](https://docs.nvidia.com/structCUpti__BufferCallbackCompleteInfo.html#_CPPv432CUpti_BufferCallbackCompleteInfo)*pBufferCompleteInfo)[#](https://docs.nvidia.com#_CPPv436CUpti_BuffersCallbackCompleteFunc_v2) Function type for callback used by CUPTI to return a buffer of activity records.

This callback function returns to the CUPTI client a buffer containing activity records. The buffer contains

`validSize`

bytes of activity records which should be read using cuptiActivityGetNextRecord. The number of dropped records can be read using cuptiActivityGetNumDroppedRecords. After this call CUPTI relinquished ownership of the buffer and will not use it anymore. The client may return the buffer to CUPTI using the CUpti_BuffersCallbackRequestFunc callback. Note: CUDA 6.0 onwards, all buffers returned by this callback are global buffers i.e. there is no context/stream specific buffer. User needs to parse the global buffer to extract the context/stream specific activity records.- Param buffer:
The activity record buffer.

- Param size:
The total size of the buffer in bytes as set in CUpti_BuffersCallbackRequestFunc.

- Param validSize:
The number of valid bytes in the buffer.

- Param pBufferCompleteInfo:
Additional information about the completed buffer.



-
typedef void (*CUpti_BuffersCallbackRequestFunc)(uint8_t **buffer, size_t *size, size_t *maxNumRecords)
[#](https://docs.nvidia.com#_CPPv432CUpti_BuffersCallbackRequestFunc) Function type for callback used by CUPTI to request an empty buffer for storing activity records.

This callback function signals the CUPTI client that an activity buffer is needed by CUPTI. The activity buffer is used by CUPTI to store activity records. The callback function can decline the request by setting

`*buffer`

to NULL. In this case CUPTI may drop activity records.- Param buffer:
Returns the new buffer. If set to NULL then no buffer is returned.

- Param size:
Returns the size of the returned buffer.

- Param maxNumRecords:
Returns the maximum number of records that should be placed in the buffer. If 0 then the buffer is filled with as many records as possible. If > 0 the buffer is filled with at most that many records before it is returned.



-
typedef void (*CUpti_BuffersCallbackRequestFunc_v2)(uint8_t **buffer, size_t *size, size_t *maxNumRecords,
[CUpti_BufferCallbackRequestInfo](https://docs.nvidia.com/structCUpti__BufferCallbackRequestInfo.html#_CPPv431CUpti_BufferCallbackRequestInfo)*pBufferRequestInfo)[#](https://docs.nvidia.com#_CPPv435CUpti_BuffersCallbackRequestFunc_v2) Function type for callback used by CUPTI to request an empty buffer for storing activity records.

This callback function signals the CUPTI client that an activity buffer is needed by CUPTI. The activity buffer is used by CUPTI to store activity records. The callback function can decline the request by setting

`*buffer`

to NULL. In this case CUPTI may drop activity records.- Param buffer:
Returns the new buffer. If set to NULL then no buffer is returned.

- Param size:
Returns the size of the returned buffer.

- Param maxNumRecords:
Returns the maximum number of records that should be placed in the buffer. If 0 then the buffer is filled with as many records as possible. If > 0 the buffer is filled with at most that many records before it is returned.

- Param pBufferRequestInfo:
Additional information about the requested buffer.



-
typedef uint64_t (*CUpti_TimestampCallbackFunc)(void)
[#](https://docs.nvidia.com#_CPPv427CUpti_TimestampCallbackFunc) Function type for callback used by CUPTI to request a timestamp to be used in activity records.

This callback function signals the CUPTI client that a timestamp needs to be returned. This timestamp would be treated as normalized timestamp to be used for various purposes in CUPTI. For example to store start and end timestamps reported in the CUPTI activity records. The returned timestamp must be in nanoseconds.