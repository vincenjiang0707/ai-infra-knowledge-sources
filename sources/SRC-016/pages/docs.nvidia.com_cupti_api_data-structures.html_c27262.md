source: https://docs.nvidia.com/cupti/api/data-structures.html

# 7. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUPTI::PcSamplingUtil::BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#structcupti_1_1pcsamplingutil_1_1bufferinfo)[BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#structcupti_1_1pcsamplingutil_1_1bufferinfo)will be stored in the file for every buffer i.e for every call of UtilDumpPcSamplingBufferInFile() API.[CUPTI::PcSamplingUtil::CUptiUtil_GetBufferInfoParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetBufferInfoParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getbufferinfoparams)Params for

[CuptiUtilGetBufferInfo](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gae4c397f1c21a9baecdc74d38b1b783dd).[CUPTI::PcSamplingUtil::CUptiUtil_GetHeaderDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetHeaderDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getheaderdataparams)Params for

[CuptiUtilGetHeaderData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga873b630c7ec1a2ada140d2f03b6934c4).[CUPTI::PcSamplingUtil::CUptiUtil_GetPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetPcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getpcsampdataparams)Params for

[CuptiUtilGetPcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga454395b5da004e96767fa739178431ce).[CUPTI::PcSamplingUtil::CUptiUtil_MergePcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__MergePcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__mergepcsampdataparams)Params for

[CuptiUtilMergePcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga4987e223c4132503d622f29ce5a9546e).[CUPTI::PcSamplingUtil::CUptiUtil_PutPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__PutPcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__putpcsampdataparams)Params for

[CuptiUtilPutPcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gab58ca9a7592643aa51e93d938768d754).[CUPTI::PcSamplingUtil::Header](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1Header.html#structcupti_1_1pcsamplingutil_1_1header)[Header](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1Header.html#structcupti_1_1pcsamplingutil_1_1header)info will be stored in file.[CUPTI::PcSamplingUtil::PcSamplingStallReasons](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1PcSamplingStallReasons.html#structcupti_1_1pcsamplingutil_1_1pcsamplingstallreasons)All available stall reasons name and respective indexes will be stored in it.

[CUpti_Activity](https://docs.nvidia.com/structCUpti__Activity.html#structcupti__activity)The base activity record.

[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi)The activity record for a driver or runtime API invocation.

[CUpti_ActivityApiCbidOptions](https://docs.nvidia.com/structCUpti__ActivityApiCbidOptions.html#structcupti__activityapicbidoptions)Per-cbid enable/disable options for API activity kinds.

[CUpti_ActivityApiOptions](https://docs.nvidia.com/structCUpti__ActivityApiOptions.html#structcupti__activityapioptions)Kind-specific options for API activity kinds (RUNTIME, DRIVER).

[CUpti_ActivityAutoBoostState](https://docs.nvidia.com/structCUpti__ActivityAutoBoostState.html#structcupti__activityautobooststate)Device auto boost state structure.

[CUpti_ActivityBranch](https://docs.nvidia.com/structCUpti__ActivityBranch.html#structcupti__activitybranch)The activity record for source level result branch.

[CUpti_ActivityBranch2](https://docs.nvidia.com/structCUpti__ActivityBranch2.html#structcupti__activitybranch2)The activity record for source level result branch.

[CUpti_ActivityCdpKernel](https://docs.nvidia.com/structCUpti__ActivityCdpKernel.html#structcupti__activitycdpkernel)The activity record for CDP (CUDA Dynamic Parallelism) kernel.

[CUpti_ActivityComputeEngineCtxSwitch](https://docs.nvidia.com/structCUpti__ActivityComputeEngineCtxSwitch.html#structcupti__activitycomputeenginectxswitch)The activity record for trace of CUDA context switch events.

[CUpti_ActivityConfidentialComputeRotation](https://docs.nvidia.com/structCUpti__ActivityConfidentialComputeRotation.html#structcupti__activityconfidentialcomputerotation)Event related to confidential compute encryption rotation.

[CUpti_ActivityConfig](https://docs.nvidia.com/structCUpti__ActivityConfig.html#structcupti__activityconfig)Activity configuration.

[CUpti_ActivityContext](https://docs.nvidia.com/structCUpti__ActivityContext.html#structcupti__activitycontext)The activity record for a context.

[CUpti_ActivityContext2](https://docs.nvidia.com/structCUpti__ActivityContext2.html#structcupti__activitycontext2)The activity record for a context.

[CUpti_ActivityContext3](https://docs.nvidia.com/structCUpti__ActivityContext3.html#structcupti__activitycontext3)The activity record for a context.

[CUpti_ActivityContext4](https://docs.nvidia.com/structCUpti__ActivityContext4.html#structcupti__activitycontext4)The activity record for a context.

[CUpti_ActivityCudaEvent](https://docs.nvidia.com/structCUpti__ActivityCudaEvent.html#structcupti__activitycudaevent)The activity record for CUDA event.

[CUpti_ActivityCudaEvent2](https://docs.nvidia.com/structCUpti__ActivityCudaEvent2.html#structcupti__activitycudaevent2)The activity record for CUDA event.

[CUpti_ActivityDevice](https://docs.nvidia.com/structCUpti__ActivityDevice.html#structcupti__activitydevice)The activity record for a device.

[CUpti_ActivityDevice2](https://docs.nvidia.com/structCUpti__ActivityDevice2.html#structcupti__activitydevice2)The activity record for a device.

[CUpti_ActivityDevice3](https://docs.nvidia.com/structCUpti__ActivityDevice3.html#structcupti__activitydevice3)The activity record for a device.

[CUpti_ActivityDevice4](https://docs.nvidia.com/structCUpti__ActivityDevice4.html#structcupti__activitydevice4)The activity record for a device.

[CUpti_ActivityDevice5](https://docs.nvidia.com/structCUpti__ActivityDevice5.html#structcupti__activitydevice5)The activity record for a device.

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

[CUpti_ActivityGlobalAccess](https://docs.nvidia.com/structCUpti__ActivityGlobalAccess.html#structcupti__activityglobalaccess)The activity record for source-level global access.

[CUpti_ActivityGlobalAccess2](https://docs.nvidia.com/structCUpti__ActivityGlobalAccess2.html#structcupti__activityglobalaccess2)The activity record for source-level global access.

[CUpti_ActivityGlobalAccess3](https://docs.nvidia.com/structCUpti__ActivityGlobalAccess3.html#structcupti__activityglobalaccess3)The activity record for source-level global access.

[CUpti_ActivityGraphHostNode](https://docs.nvidia.com/structCUpti__ActivityGraphHostNode.html#structcupti__activitygraphhostnode)[CUpti_ActivityGraphTrace](https://docs.nvidia.com/structCUpti__ActivityGraphTrace.html#structcupti__activitygraphtrace)The activity record for trace of graph execution.

[CUpti_ActivityGraphTrace2](https://docs.nvidia.com/structCUpti__ActivityGraphTrace2.html#structcupti__activitygraphtrace2)The activity record for trace of graph execution.

[CUpti_ActivityGreenContext](https://docs.nvidia.com/structCUpti__ActivityGreenContext.html#structcupti__activitygreencontext)The activity record for a green context.

[CUpti_ActivityGreenContext2](https://docs.nvidia.com/structCUpti__ActivityGreenContext2.html#structcupti__activitygreencontext2)The activity record for a green context (version 2).

[CUpti_ActivityGreenContext3](https://docs.nvidia.com/structCUpti__ActivityGreenContext3.html#structcupti__activitygreencontext3)The activity record for a green context (version 3).

[CUpti_ActivityHostLaunch](https://docs.nvidia.com/structCUpti__ActivityHostLaunch.html#structcupti__activityhostlaunch)The activity record for host launch functions.

[CUpti_ActivityInstantaneousEvent](https://docs.nvidia.com/structCUpti__ActivityInstantaneousEvent.html#structcupti__activityinstantaneousevent)The activity record for an instantaneous CUPTI event.

[CUpti_ActivityInstantaneousEventInstance](https://docs.nvidia.com/structCUpti__ActivityInstantaneousEventInstance.html#structcupti__activityinstantaneouseventinstance)The activity record for an instantaneous CUPTI event with event domain instance information.

[CUpti_ActivityInstantaneousMetric](https://docs.nvidia.com/structCUpti__ActivityInstantaneousMetric.html#structcupti__activityinstantaneousmetric)The activity record for an instantaneous CUPTI metric.

[CUpti_ActivityInstantaneousMetricInstance](https://docs.nvidia.com/structCUpti__ActivityInstantaneousMetricInstance.html#structcupti__activityinstantaneousmetricinstance)The instantaneous activity record for a CUPTI metric with instance information.

[CUpti_ActivityInstructionCorrelation](https://docs.nvidia.com/structCUpti__ActivityInstructionCorrelation.html#structcupti__activityinstructioncorrelation)The activity record for source-level sass/source line-by-line correlation.

[CUpti_ActivityInstructionExecution](https://docs.nvidia.com/structCUpti__ActivityInstructionExecution.html#structcupti__activityinstructionexecution)The activity record for source-level instruction execution.

[CUpti_ActivityJit](https://docs.nvidia.com/structCUpti__ActivityJit.html#structcupti__activityjit)The activity record for JIT operations.

[CUpti_ActivityJit2](https://docs.nvidia.com/structCUpti__ActivityJit2.html#structcupti__activityjit2)The activity record for JIT operations.

[CUpti_ActivityKernel](https://docs.nvidia.com/structCUpti__ActivityKernel.html#structcupti__activitykernel)The activity record for kernel.

[CUpti_ActivityKernel10](https://docs.nvidia.com/structCUpti__ActivityKernel10.html#structcupti__activitykernel10)The activity record for kernel.

[CUpti_ActivityKernel11](https://docs.nvidia.com/structCUpti__ActivityKernel11.html#structcupti__activitykernel11)The activity record for kernel (version 11).

[CUpti_ActivityKernel12](https://docs.nvidia.com/structCUpti__ActivityKernel12.html#structcupti__activitykernel12)The activity record for kernel (version 12).

[CUpti_ActivityKernel13](https://docs.nvidia.com/structCUpti__ActivityKernel13.html#structcupti__activitykernel13)The activity record for kernel (version 13).

[CUpti_ActivityKernel2](https://docs.nvidia.com/structCUpti__ActivityKernel2.html#structcupti__activitykernel2)The activity record for kernel.

[CUpti_ActivityKernel3](https://docs.nvidia.com/structCUpti__ActivityKernel3.html#structcupti__activitykernel3)The activity record for a kernel (CUDA 6.5(with sm_52 support) onwards).

[CUpti_ActivityKernel4](https://docs.nvidia.com/structCUpti__ActivityKernel4.html#structcupti__activitykernel4)The activity record for a kernel (CUDA 9.0(with sm_70 support) onwards).

[CUpti_ActivityKernel5](https://docs.nvidia.com/structCUpti__ActivityKernel5.html#structcupti__activitykernel5)The activity record for a kernel (CUDA 11.0(with sm_80 support) onwards).

[CUpti_ActivityKernel6](https://docs.nvidia.com/structCUpti__ActivityKernel6.html#structcupti__activitykernel6)The activity record for kernel.

[CUpti_ActivityKernel7](https://docs.nvidia.com/structCUpti__ActivityKernel7.html#structcupti__activitykernel7)The activity record for kernel.

[CUpti_ActivityKernel8](https://docs.nvidia.com/structCUpti__ActivityKernel8.html#structcupti__activitykernel8)The activity record for kernel.

[CUpti_ActivityKernel9](https://docs.nvidia.com/structCUpti__ActivityKernel9.html#structcupti__activitykernel9)The activity record for kernel.

[CUpti_ActivityMarker](https://docs.nvidia.com/structCUpti__ActivityMarker.html#structcupti__activitymarker)The activity record providing a marker which is an instantaneous point in time.

[CUpti_ActivityMarker2](https://docs.nvidia.com/structCUpti__ActivityMarker2.html#structcupti__activitymarker2)The activity record providing a marker which is an instantaneous point in time.

[CUpti_ActivityMarkerData](https://docs.nvidia.com/structCUpti__ActivityMarkerData.html#structcupti__activitymarkerdata)The activity record providing detailed information for a marker.

[CUpti_ActivityMarkerData2](https://docs.nvidia.com/structCUpti__ActivityMarkerData2.html#structcupti__activitymarkerdata2)The activity record providing detailed information for a marker.

[CUpti_ActivityMemDecompress](https://docs.nvidia.com/structCUpti__ActivityMemDecompress.html#structcupti__activitymemdecompress)The activity record for trace of decompression operations.

[CUpti_ActivityMemcpy](https://docs.nvidia.com/structCUpti__ActivityMemcpy.html#structcupti__activitymemcpy)The activity record for memory copies.

[CUpti_ActivityMemcpy3](https://docs.nvidia.com/structCUpti__ActivityMemcpy3.html#structcupti__activitymemcpy3)The activity record for memory copies.

[CUpti_ActivityMemcpy4](https://docs.nvidia.com/structCUpti__ActivityMemcpy4.html#structcupti__activitymemcpy4)The activity record for memory copies.

[CUpti_ActivityMemcpy5](https://docs.nvidia.com/structCUpti__ActivityMemcpy5.html#structcupti__activitymemcpy5)The activity record for memory copies.

[CUpti_ActivityMemcpy6](https://docs.nvidia.com/structCUpti__ActivityMemcpy6.html#structcupti__activitymemcpy6)The activity record for memory copies (version 6).

[CUpti_ActivityMemcpy7](https://docs.nvidia.com/structCUpti__ActivityMemcpy7.html#structcupti__activitymemcpy7)The activity record for memory copies (version 7).

[CUpti_ActivityMemcpyPtoP](https://docs.nvidia.com/structCUpti__ActivityMemcpyPtoP.html#structcupti__activitymemcpyptop)The activity record for peer-to-peer memory copies.

[CUpti_ActivityMemcpyPtoP2](https://docs.nvidia.com/structCUpti__ActivityMemcpyPtoP2.html#structcupti__activitymemcpyptop2)The activity record for peer-to-peer memory copies.

[CUpti_ActivityMemcpyPtoP3](https://docs.nvidia.com/structCUpti__ActivityMemcpyPtoP3.html#structcupti__activitymemcpyptop3)The activity record for peer-to-peer memory copies.

[CUpti_ActivityMemcpyPtoP4](https://docs.nvidia.com/structCUpti__ActivityMemcpyPtoP4.html#structcupti__activitymemcpyptop4)The activity record for peer-to-peer memory copies.

[CUpti_ActivityMemory](https://docs.nvidia.com/structCUpti__ActivityMemory.html#structcupti__activitymemory)The activity record for memory.

[CUpti_ActivityMemory2](https://docs.nvidia.com/structCUpti__ActivityMemory2.html#structcupti__activitymemory2)The activity record for memory.

[CUpti_ActivityMemory3](https://docs.nvidia.com/structCUpti__ActivityMemory3.html#structcupti__activitymemory3)The activity record for memory.

[CUpti_ActivityMemory4](https://docs.nvidia.com/structCUpti__ActivityMemory4.html#structcupti__activitymemory4)The activity record for memory.

[CUpti_ActivityMemoryPool](https://docs.nvidia.com/structCUpti__ActivityMemoryPool.html#structcupti__activitymemorypool)The activity record for memory pool.

[CUpti_ActivityMemoryPool2](https://docs.nvidia.com/structCUpti__ActivityMemoryPool2.html#structcupti__activitymemorypool2)The activity record for memory pool.

[CUpti_ActivityMemoryPool3](https://docs.nvidia.com/structCUpti__ActivityMemoryPool3.html#structcupti__activitymemorypool3)The activity record for memory pool.

[CUpti_ActivityMemset](https://docs.nvidia.com/structCUpti__ActivityMemset.html#structcupti__activitymemset)The activity record for memset.

[CUpti_ActivityMemset2](https://docs.nvidia.com/structCUpti__ActivityMemset2.html#structcupti__activitymemset2)The activity record for memset.

[CUpti_ActivityMemset3](https://docs.nvidia.com/structCUpti__ActivityMemset3.html#structcupti__activitymemset3)The activity record for memset.

[CUpti_ActivityMemset4](https://docs.nvidia.com/structCUpti__ActivityMemset4.html#structcupti__activitymemset4)The activity record for memset (version 4).

[CUpti_ActivityMemset5](https://docs.nvidia.com/structCUpti__ActivityMemset5.html#structcupti__activitymemset5)The activity record for memset (version 5).

[CUpti_ActivityMetric](https://docs.nvidia.com/structCUpti__ActivityMetric.html#structcupti__activitymetric)The activity record for a CUPTI metric.

[CUpti_ActivityMetricInstance](https://docs.nvidia.com/structCUpti__ActivityMetricInstance.html#structcupti__activitymetricinstance)The activity record for a CUPTI metric with instance information.

[CUpti_ActivityModule](https://docs.nvidia.com/structCUpti__ActivityModule.html#structcupti__activitymodule)The activity record for a CUDA module.

[CUpti_ActivityName](https://docs.nvidia.com/structCUpti__ActivityName.html#structcupti__activityname)The activity record providing a name.

[CUpti_ActivityNvLink](https://docs.nvidia.com/structCUpti__ActivityNvLink.html#structcupti__activitynvlink)NVLink information.

[CUpti_ActivityNvLink2](https://docs.nvidia.com/structCUpti__ActivityNvLink2.html#structcupti__activitynvlink2)NVLink information.

[CUpti_ActivityNvLink3](https://docs.nvidia.com/structCUpti__ActivityNvLink3.html#structcupti__activitynvlink3)NVLink information.

[CUpti_ActivityNvLink4](https://docs.nvidia.com/structCUpti__ActivityNvLink4.html#structcupti__activitynvlink4)NVLink information.

[CUpti_ActivityNvLink5](https://docs.nvidia.com/structCUpti__ActivityNvLink5.html#structcupti__activitynvlink5)NVLink information.

[CUpti_ActivityNvLinkNpu](https://docs.nvidia.com/structCUpti__ActivityNvLinkNpu.html#structcupti__activitynvlinknpu)NPU identifier for NVLink connections.

[CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#unioncupti__activityobjectkindid)Identifiers for object kinds as specified by CUpti_ActivityObjectKind.

[CUpti_ActivityOpenAcc](https://docs.nvidia.com/structCUpti__ActivityOpenAcc.html#structcupti__activityopenacc)The base activity record for OpenAcc records.

[CUpti_ActivityOpenAccData](https://docs.nvidia.com/structCUpti__ActivityOpenAccData.html#structcupti__activityopenaccdata)The activity record for OpenACC data.

[CUpti_ActivityOpenAccLaunch](https://docs.nvidia.com/structCUpti__ActivityOpenAccLaunch.html#structcupti__activityopenacclaunch)The activity record for OpenACC launch.

[CUpti_ActivityOpenAccOther](https://docs.nvidia.com/structCUpti__ActivityOpenAccOther.html#structcupti__activityopenaccother)The activity record for OpenACC other.

[CUpti_ActivityOpenMp](https://docs.nvidia.com/structCUpti__ActivityOpenMp.html#structcupti__activityopenmp)The base activity record for OpenMp records.

[CUpti_ActivityOverhead](https://docs.nvidia.com/structCUpti__ActivityOverhead.html#structcupti__activityoverhead)The activity record for CUPTI and driver overheads.

[CUpti_ActivityOverhead2](https://docs.nvidia.com/structCUpti__ActivityOverhead2.html#structcupti__activityoverhead2)The activity record for CUPTI and driver overheads.

[CUpti_ActivityOverhead3](https://docs.nvidia.com/structCUpti__ActivityOverhead3.html#structcupti__activityoverhead3)The activity record for CUPTI and driver overheads.

[CUpti_ActivityOverheadCommandBufferFullData](https://docs.nvidia.com/structCUpti__ActivityOverheadCommandBufferFullData.html#structcupti__activityoverheadcommandbufferfulldata)The structure to provide additional data for CUPTI_ACTIVITY_OVERHEAD_COMMAND_BUFFER_FULL.

[CUpti_ActivityPCSampling](https://docs.nvidia.com/structCUpti__ActivityPCSampling.html#structcupti__activitypcsampling)The activity record for PC sampling.

[CUpti_ActivityPCSampling2](https://docs.nvidia.com/structCUpti__ActivityPCSampling2.html#structcupti__activitypcsampling2)The activity record for PC sampling.

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

[CUpti_ActivitySynchronization](https://docs.nvidia.com/structCUpti__ActivitySynchronization.html#structcupti__activitysynchronization)The activity record for synchronization management.

[CUpti_ActivitySynchronization2](https://docs.nvidia.com/structCUpti__ActivitySynchronization2.html#structcupti__activitysynchronization2)The activity record for synchronization management.

[CUpti_ActivityUnifiedMemoryCounter](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounter.html#structcupti__activityunifiedmemorycounter)The activity record for Unified Memory counters (deprecated in CUDA 7.0)

[CUpti_ActivityUnifiedMemoryCounter2](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounter2.html#structcupti__activityunifiedmemorycounter2)The activity record for Unified Memory counters (deprecated in 12.8)

[CUpti_ActivityUnifiedMemoryCounter3](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounter3.html#structcupti__activityunifiedmemorycounter3)The activity record for Unified Memory counters (CUDA 7.0 and beyond)

[CUpti_ActivityUnifiedMemoryCounterConfig](https://docs.nvidia.com/structCUpti__ActivityUnifiedMemoryCounterConfig.html#structcupti__activityunifiedmemorycounterconfig)Unified Memory counters configuration structure.

[CUpti_BufferCallbackCompleteInfo](https://docs.nvidia.com/structCUpti__BufferCallbackCompleteInfo.html#structcupti__buffercallbackcompleteinfo)[CUpti_BufferCallbackRequestInfo](https://docs.nvidia.com/structCUpti__BufferCallbackRequestInfo.html#structcupti__buffercallbackrequestinfo)[CUpti_CallbackData](https://docs.nvidia.com/structCUpti__CallbackData.html#structcupti__callbackdata)Data passed into a runtime or driver API callback function.

[CUpti_GetCubinCrcParams](https://docs.nvidia.com/structCUpti__GetCubinCrcParams.html#structcupti__getcubincrcparams)Params for cuptiGetCubinCrc.

[CUpti_GetSassToSourceCorrelationParams](https://docs.nvidia.com/structCUpti__GetSassToSourceCorrelationParams.html#structcupti__getsasstosourcecorrelationparams)Params for cuptiGetSassToSourceCorrelation.

[CUpti_GraphData](https://docs.nvidia.com/structCUpti__GraphData.html#structcupti__graphdata)CUDA graphs data passed into a resource callback function.

[CUpti_ModuleResourceData](https://docs.nvidia.com/structCUpti__ModuleResourceData.html#structcupti__moduleresourcedata)Module data passed into a resource callback function.

[CUpti_NvtxData](https://docs.nvidia.com/structCUpti__NvtxData.html#structcupti__nvtxdata)Data passed into a NVTX callback function.

[CUpti_NvtxExtPayloadAttr](https://docs.nvidia.com/structCUpti__NvtxExtPayloadAttr.html#structcupti__nvtxextpayloadattr)[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfo.html#structcupti__pcsamplingconfigurationinfo)PC sampling configuration information structure.

[CUpti_PCSamplingConfigurationInfoParams](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfoParams.html#structcupti__pcsamplingconfigurationinfoparams)PC sampling configuration structure.

[CUpti_PCSamplingData](https://docs.nvidia.com/structCUpti__PCSamplingData.html#structcupti__pcsamplingdata)Collected PC Sampling data.

[CUpti_PCSamplingDisableParams](https://docs.nvidia.com/structCUpti__PCSamplingDisableParams.html#structcupti__pcsamplingdisableparams)Params for cuptiPCSamplingDisable.

[CUpti_PCSamplingEnableParams](https://docs.nvidia.com/structCUpti__PCSamplingEnableParams.html#structcupti__pcsamplingenableparams)Params for cuptiPCSamplingEnable.

[CUpti_PCSamplingGetDataParams](https://docs.nvidia.com/structCUpti__PCSamplingGetDataParams.html#structcupti__pcsamplinggetdataparams)Params for cuptiPCSamplingEnable.

[CUpti_PCSamplingGetNumStallReasonsParams](https://docs.nvidia.com/structCUpti__PCSamplingGetNumStallReasonsParams.html#structcupti__pcsamplinggetnumstallreasonsparams)Params for cuptiPCSamplingGetNumStallReasons.

[CUpti_PCSamplingGetStallReasonsParams](https://docs.nvidia.com/structCUpti__PCSamplingGetStallReasonsParams.html#structcupti__pcsamplinggetstallreasonsparams)Params for cuptiPCSamplingGetStallReasons.

[CUpti_PCSamplingPCData](https://docs.nvidia.com/structCUpti__PCSamplingPCData.html#structcupti__pcsamplingpcdata)PC Sampling data.

[CUpti_PCSamplingStallReason](https://docs.nvidia.com/structCUpti__PCSamplingStallReason.html#structcupti__pcsamplingstallreason)PC Sampling stall reasons.

[CUpti_PCSamplingStartParams](https://docs.nvidia.com/structCUpti__PCSamplingStartParams.html#structcupti__pcsamplingstartparams)Params for cuptiPCSamplingStart.

[CUpti_PCSamplingStopParams](https://docs.nvidia.com/structCUpti__PCSamplingStopParams.html#structcupti__pcsamplingstopparams)Params for cuptiPCSamplingStop.

[CUpti_PmSampling_CounterDataImage_Initialize_Params](https://docs.nvidia.com/structCUpti__PmSampling__CounterDataImage__Initialize__Params.html#structcupti__pmsampling__counterdataimage__initialize__params)Params for cuptiPmSamplingCounterDataImageInitialize.

[CUpti_PmSampling_CounterData_GetSampleInfo_Params](https://docs.nvidia.com/structCUpti__PmSampling__CounterData__GetSampleInfo__Params.html#structcupti__pmsampling__counterdata__getsampleinfo__params)Params for cuptiPmSamplingCounterDataGetSampleInfo.

[CUpti_PmSampling_DecodeData_Params](https://docs.nvidia.com/structCUpti__PmSampling__DecodeData__Params.html#structcupti__pmsampling__decodedata__params)Params for cuptiPmSamplingDecodeData.

[CUpti_PmSampling_Disable_Params](https://docs.nvidia.com/structCUpti__PmSampling__Disable__Params.html#structcupti__pmsampling__disable__params)Params for cuptiPmSamplingDisable.

[CUpti_PmSampling_Enable_Params](https://docs.nvidia.com/structCUpti__PmSampling__Enable__Params.html#structcupti__pmsampling__enable__params)Params for cuptiPmSamplingEnable.

[CUpti_PmSampling_GetCounterAvailability_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterAvailability__Params.html#structcupti__pmsampling__getcounteravailability__params)Params for cuptiPmSamplingGetCounterData.

[CUpti_PmSampling_GetCounterDataInfo_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterDataInfo__Params.html#structcupti__pmsampling__getcounterdatainfo__params)Params for cuptiPmSamplingGetCounterDataInfo.

[CUpti_PmSampling_GetCounterDataSize_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterDataSize__Params.html#structcupti__pmsampling__getcounterdatasize__params)Params for cuptiPmSamplingGetCounterDataSize.

[CUpti_PmSampling_SetConfig_Params](https://docs.nvidia.com/structCUpti__PmSampling__SetConfig__Params.html#structcupti__pmsampling__setconfig__params)Params for cuptiPmSamplingSetConfig.

[CUpti_PmSampling_Start_Params](https://docs.nvidia.com/structCUpti__PmSampling__Start__Params.html#structcupti__pmsampling__start__params)Params for cuptiPmSamplingStart.

[CUpti_PmSampling_Stop_Params](https://docs.nvidia.com/structCUpti__PmSampling__Stop__Params.html#structcupti__pmsampling__stop__params)Params for cuptiPmSamplingStop.

[CUpti_Profiler_BeginPass_Params](https://docs.nvidia.com/structCUpti__Profiler__BeginPass__Params.html#structcupti__profiler__beginpass__params)Params for cuptiProfilerBeginPass.

[CUpti_Profiler_BeginSession_Params](https://docs.nvidia.com/structCUpti__Profiler__BeginSession__Params.html#structcupti__profiler__beginsession__params)Params for cuptiProfilerBeginSession.

[CUpti_Profiler_CounterDataImageOptions](https://docs.nvidia.com/structCUpti__Profiler__CounterDataImageOptions.html#structcupti__profiler__counterdataimageoptions)Input parameter to define the counterDataImage.

[CUpti_Profiler_CounterDataImage_CalculateScratchBufferSize_Params](https://docs.nvidia.com/structCUpti__Profiler__CounterDataImage__CalculateScratchBufferSize__Params.html#structcupti__profiler__counterdataimage__calculatescratchbuffersize__params)Params for cuptiProfilerCounterDataImageCalculateScratchBufferSize.

[CUpti_Profiler_CounterDataImage_CalculateSize_Params](https://docs.nvidia.com/structCUpti__Profiler__CounterDataImage__CalculateSize__Params.html#structcupti__profiler__counterdataimage__calculatesize__params)Params for cuptiProfilerCounterDataImageCalculateSize.

[CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params](https://docs.nvidia.com/structCUpti__Profiler__CounterDataImage__InitializeScratchBuffer__Params.html#structcupti__profiler__counterdataimage__initializescratchbuffer__params)Params for cuptiProfilerCounterDataImageInitializeScratchBuffer.

[CUpti_Profiler_CounterDataImage_Initialize_Params](https://docs.nvidia.com/structCUpti__Profiler__CounterDataImage__Initialize__Params.html#structcupti__profiler__counterdataimage__initialize__params)Params for cuptiProfilerCounterDataImageInitialize.

[CUpti_Profiler_DeInitialize_Params](https://docs.nvidia.com/structCUpti__Profiler__DeInitialize__Params.html#structcupti__profiler__deinitialize__params)Default parameter for cuptiProfilerDeInitialize.

[CUpti_Profiler_DeviceSupported_Params](https://docs.nvidia.com/structCUpti__Profiler__DeviceSupported__Params.html#structcupti__profiler__devicesupported__params)Params for cuptiProfilerDeviceSupported.

[CUpti_Profiler_DisableProfiling_Params](https://docs.nvidia.com/structCUpti__Profiler__DisableProfiling__Params.html#structcupti__profiler__disableprofiling__params)Params for cuptiProfilerDisableProfiling.

[CUpti_Profiler_EnableProfiling_Params](https://docs.nvidia.com/structCUpti__Profiler__EnableProfiling__Params.html#structcupti__profiler__enableprofiling__params)Params for cuptiProfilerEnableProfiling.

[CUpti_Profiler_EndPass_Params](https://docs.nvidia.com/structCUpti__Profiler__EndPass__Params.html#structcupti__profiler__endpass__params)Params for cuptiProfilerEndPass.

[CUpti_Profiler_EndSession_Params](https://docs.nvidia.com/structCUpti__Profiler__EndSession__Params.html#structcupti__profiler__endsession__params)Params for cuptiProfilerEndSession.

[CUpti_Profiler_FlushCounterData_Params](https://docs.nvidia.com/structCUpti__Profiler__FlushCounterData__Params.html#structcupti__profiler__flushcounterdata__params)Params for cuptiProfilerFlushCounterData.

[CUpti_Profiler_GetCounterAvailability_Params](https://docs.nvidia.com/structCUpti__Profiler__GetCounterAvailability__Params.html#structcupti__profiler__getcounteravailability__params)Params for cuptiProfilerGetCounterAvailability.

[CUpti_Profiler_Host_ConfigAddMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__ConfigAddMetrics__Params.html#structcupti__profiler__host__configaddmetrics__params)Params for cuptiProfilerHostConfigAddMetrics.

[CUpti_Profiler_Host_Deinitialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__Deinitialize__Params.html#structcupti__profiler__host__deinitialize__params)Params for cuptiProfilerHostDeinitialize.

[CUpti_Profiler_Host_EvaluateToGpuValues_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__EvaluateToGpuValues__Params.html#structcupti__profiler__host__evaluatetogpuvalues__params)Params for cuptiProfilerHostEvaluateToGpuValues.

[CUpti_Profiler_Host_GetBaseMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetBaseMetrics__Params.html#structcupti__profiler__host__getbasemetrics__params)Params for cuptiProfilerHostGetSupportedMetrics.

[CUpti_Profiler_Host_GetConfigImageSize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetConfigImageSize__Params.html#structcupti__profiler__host__getconfigimagesize__params)Params for cuptiProfilerHostGetConfigImageSize.

[CUpti_Profiler_Host_GetConfigImage_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetConfigImage__Params.html#structcupti__profiler__host__getconfigimage__params)Params for cuptiProfilerHostGetConfigImage.

[CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMaxNumHardwareMetricsPerPass__Params.html#structcupti__profiler__host__getmaxnumhardwaremetricsperpass__params)Params for cuptiProfilerHostGetMaxNumHardwareMetricsPerPass.

[CUpti_Profiler_Host_GetMetricProperties_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMetricProperties__Params.html#structcupti__profiler__host__getmetricproperties__params)Params for cuptiProfilerHostGetMetricProperties.

[CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMetricsInSinglePassSet__Params.html#structcupti__profiler__host__getmetricsinsinglepassset__params)Params for cuptiProfilerHostGetMetricsInSinglePassSet.

[CUpti_Profiler_Host_GetNumOfPasses_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetNumOfPasses__Params.html#structcupti__profiler__host__getnumofpasses__params)Params for cuptiProfilerHostGetNumOfPasses.

[CUpti_Profiler_Host_GetRangeName_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetRangeName__Params.html#structcupti__profiler__host__getrangename__params)Params for cuptiProfilerHostGetRangeName.

[CUpti_Profiler_Host_GetSinglePassSets_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSinglePassSets__Params.html#structcupti__profiler__host__getsinglepasssets__params)Params for cuptiProfilerHostGetSinglePassSets.

[CUpti_Profiler_Host_GetSubMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSubMetrics__Params.html#structcupti__profiler__host__getsubmetrics__params)Params for cuptiProfilerHostGetSubMetrics.

[CUpti_Profiler_Host_GetSupportedChips_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSupportedChips__Params.html#structcupti__profiler__host__getsupportedchips__params)Params for cuptiProfilerHostGetSupportedChips.

[CUpti_Profiler_Host_Initialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__Initialize__Params.html#structcupti__profiler__host__initialize__params)Params for cuptiProfilerHostInitialize.

[CUpti_Profiler_Host_SetDevicePartitionInfo_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__SetDevicePartitionInfo__Params.html#structcupti__profiler__host__setdevicepartitioninfo__params)Params for cuptiProfilerHostSetDevicePartitionInfo.

[CUpti_Profiler_Initialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Initialize__Params.html#structcupti__profiler__initialize__params)Default parameter for cuptiProfilerInitialize.

[CUpti_Profiler_IsPassCollected_Params](https://docs.nvidia.com/structCUpti__Profiler__IsPassCollected__Params.html#structcupti__profiler__ispasscollected__params)Params for cuptiProfilerIsPassCollected.

[CUpti_Profiler_PopRange_Params](https://docs.nvidia.com/structCUpti__Profiler__PopRange__Params.html#structcupti__profiler__poprange__params)[CUpti_Profiler_PushRange_Params](https://docs.nvidia.com/structCUpti__Profiler__PushRange__Params.html#structcupti__profiler__pushrange__params)[CUpti_Profiler_SetConfig_Params](https://docs.nvidia.com/structCUpti__Profiler__SetConfig__Params.html#structcupti__profiler__setconfig__params)Params for cuptiProfilerSetConfig.

[CUpti_Profiler_UnsetConfig_Params](https://docs.nvidia.com/structCUpti__Profiler__UnsetConfig__Params.html#structcupti__profiler__unsetconfig__params)Params for cuptiProfilerUnsetConfig.

[CUpti_RangeProfiler_CounterDataImage_Initialize_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterDataImage__Initialize__Params.html#structcupti__rangeprofiler__counterdataimage__initialize__params)Params for cuptiRangeProfilerCounterDataImageInitialize.

[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#structcupti__rangeprofiler__counterdata__getrangeinfo__params)Params for cuptiRangeProfilerCounterDataGetRangeInfo.

[CUpti_RangeProfiler_DecodeData_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__DecodeData__Params.html#structcupti__rangeprofiler__decodedata__params)Params for cuptiRangeProfilerDecodeData.

[CUpti_RangeProfiler_Disable_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Disable__Params.html#structcupti__rangeprofiler__disable__params)Params for cuptiRangeProfilerDisable.

[CUpti_RangeProfiler_Enable_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#structcupti__rangeprofiler__enable__params)Params for cuptiRangeProfilerEnable.

[CUpti_RangeProfiler_GetCounterDataInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataInfo__Params.html#structcupti__rangeprofiler__getcounterdatainfo__params)Params for cuptiRangeProfilerGetCounterDataInfo.

[CUpti_RangeProfiler_GetCounterDataSize_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#structcupti__rangeprofiler__getcounterdatasize__params)Params for cuptiRangeProfilerGetCounterDataSize.

[CUpti_RangeProfiler_GetDevicePartitionInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html#structcupti__rangeprofiler__getdevicepartitioninfo__params)Params for cuptiRangeProfilerGetDevicePartitionInfo.

[CUpti_RangeProfiler_PopRange_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__PopRange__Params.html#structcupti__rangeprofiler__poprange__params)Params for cuptiRangeProfilerPopRange.

[CUpti_RangeProfiler_PushRange_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__PushRange__Params.html#structcupti__rangeprofiler__pushrange__params)Params for cuptiRangeProfilerPushRange.

[CUpti_RangeProfiler_SetConfig_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#structcupti__rangeprofiler__setconfig__params)Params for cuptiRangeProfilerSetConfig.

[CUpti_RangeProfiler_Start_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Start__Params.html#structcupti__rangeprofiler__start__params)Params for cuptiRangeProfilerStart.

[CUpti_RangeProfiler_Stop_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#structcupti__rangeprofiler__stop__params)Params for cuptiRangeProfilerStop.

[CUpti_ResourceData](https://docs.nvidia.com/structCUpti__ResourceData.html#structcupti__resourcedata)Data passed into a resource callback function.

[CUpti_SassMetricsDisable_Params](https://docs.nvidia.com/structCUpti__SassMetricsDisable__Params.html#structcupti__sassmetricsdisable__params)Params for cuptiSassMetricsDisable.

[CUpti_SassMetricsEnable_Params](https://docs.nvidia.com/structCUpti__SassMetricsEnable__Params.html#structcupti__sassmetricsenable__params)Params for cuptiSassMetricsEnable.

[CUpti_SassMetricsFlushData_Params](https://docs.nvidia.com/structCUpti__SassMetricsFlushData__Params.html#structcupti__sassmetricsflushdata__params)Params for cuptiSassMetricsFlushData.

[CUpti_SassMetricsGetDataProperties_Params](https://docs.nvidia.com/structCUpti__SassMetricsGetDataProperties__Params.html#structcupti__sassmetricsgetdataproperties__params)Params for cuptiSassMetricsGetDataProperties.

[CUpti_SassMetricsSetConfig_Params](https://docs.nvidia.com/structCUpti__SassMetricsSetConfig__Params.html#structcupti__sassmetricssetconfig__params)Params for cuptiSassMetricsSetConfig.

[CUpti_SassMetricsUnsetConfig_Params](https://docs.nvidia.com/structCUpti__SassMetricsUnsetConfig__Params.html#structcupti__sassmetricsunsetconfig__params)Params for cuptiSassMetricsUnsetConfig.

[CUpti_SassMetrics_Config](https://docs.nvidia.com/structCUpti__SassMetrics__Config.html#structcupti__sassmetrics__config)[CUpti_SassMetrics_Data](https://docs.nvidia.com/structCUpti__SassMetrics__Data.html#structcupti__sassmetrics__data)[CUpti_SassMetrics_GetMetrics_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetMetrics__Params.html#structcupti__sassmetrics__getmetrics__params)Params for cuptiSassMetricsGetMetrics.

[CUpti_SassMetrics_GetNumOfMetrics_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetNumOfMetrics__Params.html#structcupti__sassmetrics__getnumofmetrics__params)Params for cuptiSassMetricsGetNumOfMetrics.

[CUpti_SassMetrics_GetProperties_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetProperties__Params.html#structcupti__sassmetrics__getproperties__params)Params for cuptiSassMetricsGetProperties.

[CUpti_SassMetrics_InstanceValue](https://docs.nvidia.com/structCUpti__SassMetrics__InstanceValue.html#structcupti__sassmetrics__instancevalue)[CUpti_SassMetrics_MetricDetails](https://docs.nvidia.com/structCUpti__SassMetrics__MetricDetails.html#structcupti__sassmetrics__metricdetails)[CUpti_StateData](https://docs.nvidia.com/structCUpti__StateData.html#structcupti__statedata)Data passed into a State callback function.

[CUpti_StreamAttrData](https://docs.nvidia.com/structCUpti__StreamAttrData.html#structcupti__streamattrdata)Stream attribute data passed into a resource callback function for CUPTI_CBID_RESOURCE_STREAM_ATTRIBUTE_CHANGED callback.

[CUpti_SubscriberParams](https://docs.nvidia.com/structCUpti__SubscriberParams.html#structcupti__subscriberparams)Params for cuptiSubscribe_v2.

[CUpti_SynchronizeData](https://docs.nvidia.com/structCUpti__SynchronizeData.html#structcupti__synchronizedata)Data passed into a synchronize callback function.

[NV::Cupti::Checkpoint::CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#structnv_1_1cupti_1_1checkpoint_1_1cupti__checkpoint)Configuration and handle for a CUPTI Checkpoint.