source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetrics__InstanceValue.html

Skip to main content
Back to top
Ctrl
+
K
Cupti
v2026.3.1 |
Archive
Search
Ctrl
+
K
Search
Ctrl
+
K
Cupti
v2026.3.1 |
Archive
Table of Contents
1. Release Notes
2. Usage
3. Library support
4. Special Configurations
5. Tutorial
6. Modules
6.1. CUPTI Activity API
6.2. CUPTI Callback API
6.3. CUPTI Checkpoint API
6.4. CUPTI Clock Control API
6.5. CUPTI PC Sampling API
6.6. CUPTI PC Sampling Utility API
6.7. CUPTI PM Sampling API
6.8. CUPTI Profiler Host API
6.9. CUPTI Profiling API
6.10. CUPTI Range Profiling API
6.11. CUPTI Result Codes
6.12. CUPTI SASS Metrics API
6.13. CUPTI Version
7. Data Structures
7.1. CUpti_Activity
7.2. CUpti_ActivityAPI
7.3. CUpti_ActivityApiCbidOptions
7.4. CUpti_ActivityApiOptions
7.5. CUpti_ActivityAutoBoostState
7.6. CUpti_ActivityBranch
7.7. CUpti_ActivityBranch2
7.8. CUpti_ActivityCdpKernel
7.9. CUpti_ActivityComputeEngineCtxSwitch
7.10. CUpti_ActivityConfidentialComputeRotation
7.11. CUpti_ActivityConfig
7.12. CUpti_ActivityContext
7.13. CUpti_ActivityContext2
7.14. CUpti_ActivityContext3
7.15. CUpti_ActivityContext4
7.16. CUpti_ActivityCudaEvent
7.17. CUpti_ActivityCudaEvent2
7.18. CUpti_ActivityDevice
7.19. CUpti_ActivityDevice2
7.20. CUpti_ActivityDevice3
7.21. CUpti_ActivityDevice4
7.22. CUpti_ActivityDevice5
7.23. CUpti_ActivityDevice6
7.24. CUpti_ActivityDeviceAttribute
7.25. CUpti_ActivityDeviceGraphTrace
7.26. CUpti_ActivityEnvironment
7.27. CUpti_ActivityEnvironmentCooling
7.28. CUpti_ActivityEnvironmentPower
7.29. CUpti_ActivityEnvironmentSpeed
7.30. CUpti_ActivityEnvironmentTemperature
7.31. CUpti_ActivityEvent
7.32. CUpti_ActivityEventInstance
7.33. CUpti_ActivityExternalCorrelation
7.34. CUpti_ActivityFieldLayoutEntry
7.35. CUpti_ActivityFieldSelection
7.36. CUpti_ActivityFunction
7.37. CUpti_ActivityGlobalAccess
7.38. CUpti_ActivityGlobalAccess2
7.39. CUpti_ActivityGlobalAccess3
7.40. CUpti_ActivityGraphHostNode
7.41. CUpti_ActivityGraphTrace
7.42. CUpti_ActivityGraphTrace2
7.43. CUpti_ActivityGreenContext
7.44. CUpti_ActivityGreenContext2
7.45. CUpti_ActivityGreenContext3
7.46. CUpti_ActivityHostLaunch
7.47. CUpti_ActivityInstantaneousEvent
7.48. CUpti_ActivityInstantaneousEventInstance
7.49. CUpti_ActivityInstantaneousMetric
7.50. CUpti_ActivityInstantaneousMetricInstance
7.51. CUpti_ActivityInstructionCorrelation
7.52. CUpti_ActivityInstructionExecution
7.53. CUpti_ActivityJit
7.54. CUpti_ActivityJit2
7.55. CUpti_ActivityKernel
7.56. CUpti_ActivityKernel10
7.57. CUpti_ActivityKernel11
7.58. CUpti_ActivityKernel12
7.59. CUpti_ActivityKernel13
7.60. CUpti_ActivityKernel2
7.61. CUpti_ActivityKernel3
7.62. CUpti_ActivityKernel4
7.63. CUpti_ActivityKernel5
7.64. CUpti_ActivityKernel6
7.65. CUpti_ActivityKernel7
7.66. CUpti_ActivityKernel8
7.67. CUpti_ActivityKernel9
7.68. CUpti_ActivityMarker
7.69. CUpti_ActivityMarker2
7.70. CUpti_ActivityMarkerData
7.71. CUpti_ActivityMarkerData2
7.72. CUpti_ActivityMemDecompress
7.73. CUpti_ActivityMemcpy
7.74. CUpti_ActivityMemcpy3
7.75. CUpti_ActivityMemcpy4
7.76. CUpti_ActivityMemcpy5
7.77. CUpti_ActivityMemcpy6
7.78. CUpti_ActivityMemcpy7
7.79. CUpti_ActivityMemcpyPtoP
7.80. CUpti_ActivityMemcpyPtoP2
7.81. CUpti_ActivityMemcpyPtoP3
7.82. CUpti_ActivityMemcpyPtoP4
7.83. CUpti_ActivityMemory
7.84. CUpti_ActivityMemory2
7.85. CUpti_ActivityMemory3
7.86. CUpti_ActivityMemory4
7.87. CUpti_ActivityMemoryPool
7.88. CUpti_ActivityMemoryPool2
7.89. CUpti_ActivityMemoryPool3
7.90. CUpti_ActivityMemset
7.91. CUpti_ActivityMemset2
7.92. CUpti_ActivityMemset3
7.93. CUpti_ActivityMemset4
7.94. CUpti_ActivityMemset5
7.95. CUpti_ActivityMetric
7.96. CUpti_ActivityMetricInstance
7.97. CUpti_ActivityModule
7.98. CUpti_ActivityName
7.99. CUpti_ActivityNvLink
7.100. CUpti_ActivityNvLink2
7.101. CUpti_ActivityNvLink3
7.102. CUpti_ActivityNvLink4
7.103. CUpti_ActivityNvLink5
7.104. CUpti_ActivityNvLinkNpu
7.105. CUpti_ActivityObjectKindId
7.106. CUpti_ActivityOpenAcc
7.107. CUpti_ActivityOpenAccData
7.108. CUpti_ActivityOpenAccLaunch
7.109. CUpti_ActivityOpenAccOther
7.110. CUpti_ActivityOpenMp
7.111. CUpti_ActivityOverhead
7.112. CUpti_ActivityOverhead2
7.113. CUpti_ActivityOverhead3
7.114. CUpti_ActivityOverheadCommandBufferFullData
7.115. CUpti_ActivityPCSampling
7.116. CUpti_ActivityPCSampling2
7.117. CUpti_ActivityPCSampling3
7.118. CUpti_ActivityPCSamplingConfig
7.119. CUpti_ActivityPCSamplingRecordInfo
7.120. CUpti_ActivityPcie
7.121. CUpti_ActivityPcieBridgeAttr
7.122. CUpti_ActivityPcieGpuAttr
7.123. CUpti_ActivityPreemption
7.124. CUpti_ActivityRecordLayout
7.125. CUpti_ActivitySharedAccess
7.126. CUpti_ActivitySourceLocator
7.127. CUpti_ActivityStream
7.128. CUpti_ActivitySynchronization
7.129. CUpti_ActivitySynchronization2
7.130. CUpti_ActivityUnifiedMemoryCounter
7.131. CUpti_ActivityUnifiedMemoryCounter2
7.132. CUpti_ActivityUnifiedMemoryCounter3
7.133. CUpti_ActivityUnifiedMemoryCounterConfig
7.134. CUpti_BufferCallbackCompleteInfo
7.135. CUpti_BufferCallbackRequestInfo
7.136. CUpti_CallbackData
7.137. CUpti_GetCubinCrcParams
7.138. CUpti_GetSassToSourceCorrelationParams
7.139. CUpti_GraphData
7.140. CUpti_ModuleResourceData
7.141. CUpti_NvtxData
7.142. CUpti_NvtxExtPayloadAttr
7.143. CUpti_PCSamplingConfigurationInfo
7.144. CUpti_PCSamplingConfigurationInfoParams
7.145. CUpti_PCSamplingData
7.146. CUpti_PCSamplingDisableParams
7.147. CUpti_PCSamplingEnableParams
7.148. CUpti_PCSamplingGetDataParams
7.149. CUpti_PCSamplingGetNumStallReasonsParams
7.150. CUpti_PCSamplingGetStallReasonsParams
7.151. CUpti_PCSamplingPCData
7.152. CUpti_PCSamplingStallReason
7.153. CUpti_PCSamplingStartParams
7.154. CUpti_PCSamplingStopParams
7.155. CUpti_PmSampling_CounterDataImage_Initialize_Params
7.156. CUpti_PmSampling_CounterData_GetSampleInfo_Params
7.157. CUpti_PmSampling_DecodeData_Params
7.158. CUpti_PmSampling_Disable_Params
7.159. CUpti_PmSampling_Enable_Params
7.160. CUpti_PmSampling_GetCounterAvailability_Params
7.161. CUpti_PmSampling_GetCounterDataInfo_Params
7.162. CUpti_PmSampling_GetCounterDataSize_Params
7.163. CUpti_PmSampling_SetConfig_Params
7.164. CUpti_PmSampling_Start_Params
7.165. CUpti_PmSampling_Stop_Params
7.166. CUpti_Profiler_BeginPass_Params
7.167. CUpti_Profiler_BeginSession_Params
7.168. CUpti_Profiler_CounterDataImageOptions
7.169. CUpti_Profiler_CounterDataImage_CalculateScratchBufferSize_Params
7.170. CUpti_Profiler_CounterDataImage_CalculateSize_Params
7.171. CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params
7.172. CUpti_Profiler_CounterDataImage_Initialize_Params
7.173. CUpti_Profiler_DeInitialize_Params
7.174. CUpti_Profiler_DeviceSupported_Params
7.175. CUpti_Profiler_DisableProfiling_Params
7.176. CUpti_Profiler_EnableProfiling_Params
7.177. CUpti_Profiler_EndPass_Params
7.178. CUpti_Profiler_EndSession_Params
7.179. CUpti_Profiler_FlushCounterData_Params
7.180. CUpti_Profiler_GetCounterAvailability_Params
7.181. CUpti_Profiler_Host_ConfigAddMetrics_Params
7.182. CUpti_Profiler_Host_Deinitialize_Params
7.183. CUpti_Profiler_Host_EvaluateToGpuValues_Params
7.184. CUpti_Profiler_Host_GetBaseMetrics_Params
7.185. CUpti_Profiler_Host_GetConfigImageSize_Params
7.186. CUpti_Profiler_Host_GetConfigImage_Params
7.187. CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params
7.188. CUpti_Profiler_Host_GetMetricProperties_Params
7.189. CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params
7.190. CUpti_Profiler_Host_GetNumOfPasses_Params
7.191. CUpti_Profiler_Host_GetRangeName_Params
7.192. CUpti_Profiler_Host_GetSinglePassSets_Params
7.193. CUpti_Profiler_Host_GetSubMetrics_Params
7.194. CUpti_Profiler_Host_GetSupportedChips_Params
7.195. CUpti_Profiler_Host_Initialize_Params
7.196. CUpti_Profiler_Host_SetDevicePartitionInfo_Params
7.197. CUpti_Profiler_Initialize_Params
7.198. CUpti_Profiler_IsPassCollected_Params
7.199. CUpti_Profiler_PopRange_Params
7.200. CUpti_Profiler_PushRange_Params
7.201. CUpti_Profiler_SetConfig_Params
7.202. CUpti_Profiler_UnsetConfig_Params
7.203. CUpti_RangeProfiler_CounterDataImage_Initialize_Params
7.204. CUpti_RangeProfiler_CounterData_GetRangeInfo_Params
7.205. CUpti_RangeProfiler_DecodeData_Params
7.206. CUpti_RangeProfiler_Disable_Params
7.207. CUpti_RangeProfiler_Enable_Params
7.208. CUpti_RangeProfiler_GetCounterDataInfo_Params
7.209. CUpti_RangeProfiler_GetCounterDataSize_Params
7.210. CUpti_RangeProfiler_GetDevicePartitionInfo_Params
7.211. CUpti_RangeProfiler_PopRange_Params
7.212. CUpti_RangeProfiler_PushRange_Params
7.213. CUpti_RangeProfiler_SetConfig_Params
7.214. CUpti_RangeProfiler_Start_Params
7.215. CUpti_RangeProfiler_Stop_Params
7.216. CUpti_ResourceData
7.217. CUpti_SassMetricsDisable_Params
7.218. CUpti_SassMetricsEnable_Params
7.219. CUpti_SassMetricsFlushData_Params
7.220. CUpti_SassMetricsGetDataProperties_Params
7.221. CUpti_SassMetricsSetConfig_Params
7.222. CUpti_SassMetricsUnsetConfig_Params
7.223. CUpti_SassMetrics_Config
7.224. CUpti_SassMetrics_Data
7.225. CUpti_SassMetrics_GetMetrics_Params
7.226. CUpti_SassMetrics_GetNumOfMetrics_Params
7.227. CUpti_SassMetrics_GetProperties_Params
7.228. CUpti_SassMetrics_InstanceValue
7.229. CUpti_SassMetrics_MetricDetails
7.230. CUpti_StateData
7.231. CUpti_StreamAttrData
7.232. CUpti_SubscriberParams
7.233. CUpti_SynchronizeData
8. Namespaces
8.1. CUPTI
8.1.1. PcSamplingUtil
8.1.1.1. BufferInfo
8.1.1.2. CUptiUtil_GetBufferInfoParams
8.1.1.3. CUptiUtil_GetHeaderDataParams
8.1.1.4. CUptiUtil_GetPcSampDataParams
8.1.1.5. CUptiUtil_MergePcSampDataParams
8.1.1.6. CUptiUtil_PutPcSampDataParams
8.1.1.7. Header
8.1.1.8. PcSamplingStallReasons
8.2. NV
8.2.1. Cupti
8.2.1.1. Checkpoint
Copyright and Licenses
Notices
7.
Data Structures
7.228.
CUpti_SassMetrics_InstanceValue
7.228.
CUpti_SassMetrics_InstanceValue
#
struct
CUpti_SassMetrics_InstanceValue
#
On this page
CUpti_SassMetrics_InstanceValue