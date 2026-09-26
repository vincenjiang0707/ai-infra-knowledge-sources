source: https://docs.nvidia.com/cupti/api/group__CUPTI__PROFILER__API.html

# 6.9. CUPTI Profiling API[#](https://docs.nvidia.com#cupti-profiling-api)

Functions, types, and enums that implement the CUPTI Profiling API.

## 6.9.1. Data Structures[#](https://docs.nvidia.com#data-structures)

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

[CUpti_Profiler_Initialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Initialize__Params.html#structcupti__profiler__initialize__params)Default parameter for cuptiProfilerInitialize.

[CUpti_Profiler_IsPassCollected_Params](https://docs.nvidia.com/structCUpti__Profiler__IsPassCollected__Params.html#structcupti__profiler__ispasscollected__params)Params for cuptiProfilerIsPassCollected.

[CUpti_Profiler_PopRange_Params](https://docs.nvidia.com/structCUpti__Profiler__PopRange__Params.html#structcupti__profiler__poprange__params)[CUpti_Profiler_PushRange_Params](https://docs.nvidia.com/structCUpti__Profiler__PushRange__Params.html#structcupti__profiler__pushrange__params)[CUpti_Profiler_SetConfig_Params](https://docs.nvidia.com/structCUpti__Profiler__SetConfig__Params.html#structcupti__profiler__setconfig__params)Params for cuptiProfilerSetConfig.

[CUpti_Profiler_UnsetConfig_Params](https://docs.nvidia.com/structCUpti__Profiler__UnsetConfig__Params.html#structcupti__profiler__unsetconfig__params)Params for cuptiProfilerUnsetConfig.


## 6.9.2. Macros[#](https://docs.nvidia.com#macros)

[CUpti_Profiler_BeginPass_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1gab5fe1d45dfd8888581eb709920ee833d)[CUpti_Profiler_BeginSession_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1gad305a7d172f07ba7a4720114e513f09f)[CUpti_Profiler_CounterDataImageOptions_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga8fe9d3a79db63147e1748342b5bce723)[CUpti_Profiler_CounterDataImage_CalculateScratchBufferSize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga95dc7991e8edd7d6902313ba25db8fad)[CUpti_Profiler_CounterDataImage_CalculateSize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga579ff7365d5c18a1fe5cee6c2303808d)[CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga94b177c001b3f8adc04f0320de36ff44)[CUpti_Profiler_CounterDataImage_Initialize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga4ca84755116396800ae9df46be585a45)[CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga5e77fb55dc80d62dee8c7621a709feb1)[CUpti_Profiler_DeviceSupported_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga87a54677b3cd64fec67d51ca316b5658)[CUpti_Profiler_DisableProfiling_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1gaffd26a80acbe32853644864693195679)[CUpti_Profiler_EnableProfiling_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga4329977eddeffa0cfda4604bdbfdae18)[CUpti_Profiler_EndPass_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga5fa1bf2ce361afac389c3f3b8a699da2)[CUpti_Profiler_EndSession_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga73eeab7c0b0439d2eb14bd13fe9bf751)[CUpti_Profiler_FlushCounterData_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga03c9ce387f3a8d19e1f36d9d1577e818)[CUpti_Profiler_GetCounterAvailability_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1gac94ee61418d05fdf5ee2eb99193e514a)[CUpti_Profiler_Initialize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga93c1ed6ff6fd5f113930909b7fe9bd90)[CUpti_Profiler_IsPassCollected_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga1209928fd2b1e27ee10695dc21c7e091)[CUpti_Profiler_PopRange_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1gaa4c9373ca3a7aa7c2897f5cba554150c)[CUpti_Profiler_PushRange_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga57f1c913897076c598c6e51ed7cc3615)[CUpti_Profiler_SetConfig_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga9140ef9840542190eedf1992c1c81cc9)[CUpti_Profiler_UnsetConfig_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__api_1ga596977722d7474009c343098865836c2)

## 6.9.3. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUpti_ProfilerRange](https://docs.nvidia.com#group__cupti__profiler__api_1gaa6faef578b53da403b15878e05d1b395)Profiler range attribute.

[CUpti_ProfilerReplayMode](https://docs.nvidia.com#group__cupti__profiler__api_1gad6960f26de20f317a784ee565743e457)Profiler replay attribute.

[CUpti_Profiler_API](https://docs.nvidia.com#group__cupti__profiler__api_1ga28394e0ca7a2ba0eaab79ce6accf1cff)Profiler API types.

[CUpti_Profiler_Support_Level](https://docs.nvidia.com#group__cupti__profiler__api_1gae9c7f68d6d33973878b56e39fb9cfa52)Generic support level enum for CUPTI.


## 6.9.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiProfilerBeginPass](https://docs.nvidia.com#group__cupti__profiler__api_1ga8c96f8bcc440b84a243369d1e41d1520)(CUpti_Profiler_BeginPass_Params *pParams) Replay API: used for multipass collection.

- CUptiResult
[cuptiProfilerBeginSession](https://docs.nvidia.com#group__cupti__profiler__api_1ga19d3db3d5081911499ee8884f8a858ab)(CUpti_Profiler_BeginSession_Params *pParams) Begin profiling session sets up the profiling on the device.

- CUptiResult
[cuptiProfilerCounterDataImageCalculateScratchBufferSize](https://docs.nvidia.com#group__cupti__profiler__api_1ga21e53b286d5fcca64ef63b92694deb17)(CUpti_Profiler_CounterDataImage_CalculateScratchBufferSize_Params *pParams) A temporary storage for CounterData image needed for internal operations.

- CUptiResult
[cuptiProfilerCounterDataImageCalculateSize](https://docs.nvidia.com#group__cupti__profiler__api_1ga5bb34e2042b3675158f2d5a922f34125)(CUpti_Profiler_CounterDataImage_CalculateSize_Params *pParams) A CounterData image allocates space for values for each counter for each range.

- CUptiResult
[cuptiProfilerCounterDataImageInitialize](https://docs.nvidia.com#group__cupti__profiler__api_1ga80b20bca8a7d0de2a103f81b4c98339c)(CUpti_Profiler_CounterDataImage_Initialize_Params *pParams) - CUptiResult
[cuptiProfilerCounterDataImageInitializeScratchBuffer](https://docs.nvidia.com#group__cupti__profiler__api_1ga5e9263e64c3d63c14ed4d77a1ca96549)(CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params *pParams) - CUptiResult
[cuptiProfilerDeInitialize](https://docs.nvidia.com#group__cupti__profiler__api_1ga9d49c7e7e0707ad0260effdc5ab9021b)(CUpti_Profiler_DeInitialize_Params *pParams) DeInitializes the profiler interface.

- CUptiResult
[cuptiProfilerDeviceSupported](https://docs.nvidia.com#group__cupti__profiler__api_1gaef5552aa70dede36361da992a82f2cb4)(CUpti_Profiler_DeviceSupported_Params *pParams) Query device compatibility with Profiling API.

- CUptiResult
[cuptiProfilerDisableProfiling](https://docs.nvidia.com#group__cupti__profiler__api_1gaa64dfbcde27a202af83e1795fdd4a484)(CUpti_Profiler_DisableProfiling_Params *pParams) Disable Profiling.

- CUptiResult
[cuptiProfilerEnableProfiling](https://docs.nvidia.com#group__cupti__profiler__api_1ga287bf4dc8e3acb547a1d082c8b337837)(CUpti_Profiler_EnableProfiling_Params *pParams) Enables Profiling.

- CUptiResult
[cuptiProfilerEndPass](https://docs.nvidia.com#group__cupti__profiler__api_1gaaab3e227e392cd92da172d49506f6cd8)(CUpti_Profiler_EndPass_Params *pParams) Replay API: used for multipass collection.

- CUptiResult
[cuptiProfilerEndSession](https://docs.nvidia.com#group__cupti__profiler__api_1gabe577146ea3e1f187913ae906260530d)(CUpti_Profiler_EndSession_Params *pParams) Ends profiling session.

- CUptiResult
[cuptiProfilerFlushCounterData](https://docs.nvidia.com#group__cupti__profiler__api_1gad2c936e79a90a46a29dcfc409166c39b)(CUpti_Profiler_FlushCounterData_Params *pParams) Decode all the submitted passes.

- CUptiResult
[cuptiProfilerGetCounterAvailability](https://docs.nvidia.com#group__cupti__profiler__api_1gae88e65505f6f863ac5b85026cd12da5c)(CUpti_Profiler_GetCounterAvailability_Params *pParams) Query counter availibility.

- CUptiResult
[cuptiProfilerInitialize](https://docs.nvidia.com#group__cupti__profiler__api_1gad64f44975cdfa93a1c179eb8c8d51b53)(CUpti_Profiler_Initialize_Params *pParams) Initializes the profiler interface.

- CUptiResult
[cuptiProfilerIsPassCollected](https://docs.nvidia.com#group__cupti__profiler__api_1ga4f57f687f8837e74e73668cd8412259b)(CUpti_Profiler_IsPassCollected_Params *pParams) Asynchronous call to query if the submitted pass to GPU is collected.

- CUptiResult
[cuptiProfilerPopRange](https://docs.nvidia.com#group__cupti__profiler__api_1ga4fb53a9736ed17cd8910dc491b958f9a)(CUpti_Profiler_PopRange_Params *pParams) Range API's : Pop user range.

- CUptiResult
[cuptiProfilerPushRange](https://docs.nvidia.com#group__cupti__profiler__api_1gab300cc3e24b408e4c5cfed310fed084f)(CUpti_Profiler_PushRange_Params *pParams) Range API's : Push user range.

- CUptiResult
[cuptiProfilerSetConfig](https://docs.nvidia.com#group__cupti__profiler__api_1gaa1ff2f08b95cf9534b3ec1e73dcfda5b)(CUpti_Profiler_SetConfig_Params *pParams) Set metrics configuration to be profiled.

- CUptiResult
[cuptiProfilerUnsetConfig](https://docs.nvidia.com#group__cupti__profiler__api_1ga20449fe304f3f3cd0b174f63ab868054)(CUpti_Profiler_UnsetConfig_Params *pParams) Unset metrics configuration profiled.


## 6.9.5. Macros[#](https://docs.nvidia.com#id1)

-
CUpti_Profiler_BeginPass_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_BeginPass_Params_STRUCT_SIZE)

-
CUpti_Profiler_BeginSession_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_BeginSession_Params_STRUCT_SIZE)

-
CUpti_Profiler_CounterDataImageOptions_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_CounterDataImageOptions_STRUCT_SIZE)

-
CUpti_Profiler_CounterDataImage_CalculateScratchBufferSize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_CounterDataImage_CalculateScratchBufferSize_Params_STRUCT_SIZE)

-
CUpti_Profiler_CounterDataImage_CalculateSize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_CounterDataImage_CalculateSize_Params_STRUCT_SIZE)

-
CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params_STRUCT_SIZE)

-
CUpti_Profiler_CounterDataImage_Initialize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_CounterDataImage_Initialize_Params_STRUCT_SIZE)

-
CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE)

-
CUpti_Profiler_DeviceSupported_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_DeviceSupported_Params_STRUCT_SIZE)

-
CUpti_Profiler_DisableProfiling_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_DisableProfiling_Params_STRUCT_SIZE)

-
CUpti_Profiler_EnableProfiling_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_EnableProfiling_Params_STRUCT_SIZE)

-
CUpti_Profiler_EndPass_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_EndPass_Params_STRUCT_SIZE)

-
CUpti_Profiler_EndSession_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_EndSession_Params_STRUCT_SIZE)

-
CUpti_Profiler_FlushCounterData_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_FlushCounterData_Params_STRUCT_SIZE)

-
CUpti_Profiler_GetCounterAvailability_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_GetCounterAvailability_Params_STRUCT_SIZE)

-
CUpti_Profiler_Initialize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Initialize_Params_STRUCT_SIZE)

-
CUpti_Profiler_IsPassCollected_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_IsPassCollected_Params_STRUCT_SIZE)

-
CUpti_Profiler_PopRange_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_PopRange_Params_STRUCT_SIZE)

-
CUpti_Profiler_PushRange_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_PushRange_Params_STRUCT_SIZE)

-
CUpti_Profiler_SetConfig_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_SetConfig_Params_STRUCT_SIZE)

-
CUpti_Profiler_UnsetConfig_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_UnsetConfig_Params_STRUCT_SIZE)

## 6.9.6. Enumerations[#](https://docs.nvidia.com#id2)

-
enum CUpti_ProfilerRange
[#](https://docs.nvidia.com#_CPPv419CUpti_ProfilerRange) Profiler range attribute.

A metric enabled in the session’s configuration is collected separately per unique range-stack in the pass. This is an attribute to collect metrics around each kernel in a profiling session or in an user defined range.

*Values:*-
enumerator CUPTI_Range_INVALID
[#](https://docs.nvidia.com#_CPPv4N19CUpti_ProfilerRange19CUPTI_Range_INVALIDE) Invalid value.


-
enumerator CUPTI_AutoRange
[#](https://docs.nvidia.com#_CPPv4N19CUpti_ProfilerRange15CUPTI_AutoRangeE) Ranges are auto defined around each kernel in a profiling session.


-
enumerator CUPTI_UserRange
[#](https://docs.nvidia.com#_CPPv4N19CUpti_ProfilerRange15CUPTI_UserRangeE) A range in which metric data to be collected is defined by the user.


-
enumerator CUPTI_Range_COUNT
[#](https://docs.nvidia.com#_CPPv4N19CUpti_ProfilerRange17CUPTI_Range_COUNTE) Range count.


-
enumerator CUPTI_Range_INVALID

-
enum CUpti_ProfilerReplayMode
[#](https://docs.nvidia.com#_CPPv424CUpti_ProfilerReplayMode) Profiler replay attribute.

For metrics which require multipass collection, a replay of the GPU kernel(s) is required. This is an attribute which specify how the replay of the kernel(s) to be measured is done.

*Values:*-
enumerator CUPTI_Replay_INVALID
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ProfilerReplayMode20CUPTI_Replay_INVALIDE) Invalid Value.


-
enumerator CUPTI_ApplicationReplay
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ProfilerReplayMode23CUPTI_ApplicationReplayE) Replay is done by CUPTI user around the process.


-
enumerator CUPTI_KernelReplay
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ProfilerReplayMode18CUPTI_KernelReplayE) Replay is done around kernel implicitly by CUPTI.


-
enumerator CUPTI_UserReplay
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ProfilerReplayMode16CUPTI_UserReplayE) Replay is done by CUPTI user within a process.


-
enumerator CUPTI_Replay_COUNT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ProfilerReplayMode18CUPTI_Replay_COUNTE) Replay count.


-
enumerator CUPTI_Replay_INVALID

-
enum CUpti_Profiler_API
[#](https://docs.nvidia.com#_CPPv418CUpti_Profiler_API) Profiler API types.

*Values:*-
enumerator CUPTI_PROFILER_RANGE_PROFILING
[#](https://docs.nvidia.com#_CPPv4N18CUpti_Profiler_API30CUPTI_PROFILER_RANGE_PROFILINGE) CUPTI APIs for range based profiling (cuptiProfiler*)


-
enumerator CUPTI_PROFILER_PC_SAMPLING
[#](https://docs.nvidia.com#_CPPv4N18CUpti_Profiler_API26CUPTI_PROFILER_PC_SAMPLINGE) CUPTI APIs collecting pc sampling data (cuptiPcSampling*)


-
enumerator CUPTI_PROFILER_SASS_METRICS
[#](https://docs.nvidia.com#_CPPv4N18CUpti_Profiler_API27CUPTI_PROFILER_SASS_METRICSE) CUPTI APIs collecting SASS metrics data (cuptiSassMetrics*)


-
enumerator CUPTI_PROFILER_PM_SAMPLING
[#](https://docs.nvidia.com#_CPPv4N18CUpti_Profiler_API26CUPTI_PROFILER_PM_SAMPLINGE) CUPTI APIs collecting PM Sampling data (cuptiPmSampling*)


-
enumerator CUPTI_PROFILER_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N18CUpti_Profiler_API22CUPTI_PROFILER_UNKNOWNE)

-
enumerator CUPTI_PROFILER_RANGE_PROFILING

-
enum CUpti_Profiler_Support_Level
[#](https://docs.nvidia.com#_CPPv428CUpti_Profiler_Support_Level) Generic support level enum for CUPTI.

*Values:*-
enumerator CUPTI_PROFILER_CONFIGURATION_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N28CUpti_Profiler_Support_Level36CUPTI_PROFILER_CONFIGURATION_UNKNOWNE) Configuration support level unknown - either detection code errored out before setting this value, or unable to determine it.


-
enumerator CUPTI_PROFILER_CONFIGURATION_UNSUPPORTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_Profiler_Support_Level40CUPTI_PROFILER_CONFIGURATION_UNSUPPORTEDE) Profiling is unavailable. For specific feature fields, this means that the current configuration of this feature does not work with profiling. For instance, SLI-enabled devices do not support profiling, and this value would be returned for SLI on an SLI-enabled device.


-
enumerator CUPTI_PROFILER_CONFIGURATION_DISABLED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_Profiler_Support_Level37CUPTI_PROFILER_CONFIGURATION_DISABLEDE) Profiling would be available for this configuration, but was disabled by the system.


-
enumerator CUPTI_PROFILER_CONFIGURATION_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N28CUpti_Profiler_Support_Level38CUPTI_PROFILER_CONFIGURATION_SUPPORTEDE) Profiling is supported. For specific feature fields, this means that the current configuration of this feature works with profiling. For instance, SLI-enabled devices do not support profiling, and this value would only be returned for devices which are not SLI-enabled.


-
enumerator CUPTI_PROFILER_CONFIGURATION_LIMITED_SUPPORT
[#](https://docs.nvidia.com#_CPPv4N28CUpti_Profiler_Support_Level44CUPTI_PROFILER_CONFIGURATION_LIMITED_SUPPORTE) Profiling is supported, but only for a limited set of metrics.


-
enumerator CUPTI_PROFILER_CONFIGURATION_UNKNOWN

## 6.9.7. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerBeginPass( ,[CUpti_Profiler_BeginPass_Params](https://docs.nvidia.com/structCUpti__Profiler__BeginPass__Params.html#_CPPv431CUpti_Profiler_BeginPass_Params)*pParamsReplay API: used for multipass collection.

These APIs are used if user chooses to replay by itself

[CUPTI_UserReplay](https://docs.nvidia.com#group__cupti__profiler__api_1ggad6960f26de20f317a784ee565743e457aa052699f076ad798166b7b653b0ce14e)or[CUPTI_ApplicationReplay](https://docs.nvidia.com#group__cupti__profiler__api_1ggad6960f26de20f317a784ee565743e457a298b65c9526dabe7113fdb5b9e45c957)for multipass collection of the metrics configurations. It’s a no-op in case of[CUPTI_KernelReplay](https://docs.nvidia.com#group__cupti__profiler__api_1ggad6960f26de20f317a784ee565743e457ac2e3d8f8e8ad65399ae39f6d0e266bc8).**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv422cuptiProfilerBeginPassP31CUpti_Profiler_BeginPass_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerBeginSession( ,[CUpti_Profiler_BeginSession_Params](https://docs.nvidia.com/structCUpti__Profiler__BeginSession__Params.html#_CPPv434CUpti_Profiler_BeginSession_Params)*pParamsBegin profiling session sets up the profiling on the device.

Although, it doesn’t start the profiling but GPU resources needed for profiling are allocated. Outside of a session, the GPU will return to its normal operating state.

**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv425cuptiProfilerBeginSessionP34CUpti_Profiler_BeginSession_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerCounterDataImageCalculateScratchBufferSize(
) A temporary storage for CounterData image needed for internal operations.

Use these APIs to calculate the allocation size and initialize counterData image scratch buffer.

**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv455cuptiProfilerCounterDataImageCalculateScratchBufferSizeP65CUpti_Profiler_CounterDataImage_CalculateScratchBufferSize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerCounterDataImageCalculateSize(
) A CounterData image allocates space for values for each counter for each range.

User borne the resposibility of managing the counterDataImage allocations. CounterDataPrefix contains meta data about the metrics that will be stored in counterDataImage. Use these APIs to calculate the allocation size and initialize counterData image.

**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv442cuptiProfilerCounterDataImageCalculateSizeP52CUpti_Profiler_CounterDataImage_CalculateSize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerCounterDataImageInitialize(
)

[#](https://docs.nvidia.com#_CPPv439cuptiProfilerCounterDataImageInitializeP49CUpti_Profiler_CounterDataImage_Initialize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerCounterDataImageInitializeScratchBuffer(
)

[#](https://docs.nvidia.com#_CPPv452cuptiProfilerCounterDataImageInitializeScratchBufferP62CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerDeInitialize( ,[CUpti_Profiler_DeInitialize_Params](https://docs.nvidia.com/structCUpti__Profiler__DeInitialize__Params.html#_CPPv434CUpti_Profiler_DeInitialize_Params)*pParamsDeInitializes the profiler interface.


[#](https://docs.nvidia.com#_CPPv425cuptiProfilerDeInitializeP34CUpti_Profiler_DeInitialize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerDeviceSupported( ,[CUpti_Profiler_DeviceSupported_Params](https://docs.nvidia.com/structCUpti__Profiler__DeviceSupported__Params.html#_CPPv437CUpti_Profiler_DeviceSupported_Params)*pParamsQuery device compatibility with Profiling API.

Use this call to determine whether a compute device and configuration are compatible with the Profiling API. If the configuration does not support profiling, one of several flags will indicate why.


[#](https://docs.nvidia.com#_CPPv428cuptiProfilerDeviceSupportedP37CUpti_Profiler_DeviceSupported_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerDisableProfiling( ,[CUpti_Profiler_DisableProfiling_Params](https://docs.nvidia.com/structCUpti__Profiler__DisableProfiling__Params.html#_CPPv438CUpti_Profiler_DisableProfiling_Params)*pParamsDisable Profiling.

In

[CUPTI_AutoRange](https://docs.nvidia.com#group__cupti__profiler__api_1ggaa6faef578b53da403b15878e05d1b395aee196550a6a859439d2a4aa4ab531cf0), these APIs are used to enable/disable profiling for the kernels to be executed in a profiling session.**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv429cuptiProfilerDisableProfilingP38CUpti_Profiler_DisableProfiling_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerEnableProfiling( ,[CUpti_Profiler_EnableProfiling_Params](https://docs.nvidia.com/structCUpti__Profiler__EnableProfiling__Params.html#_CPPv437CUpti_Profiler_EnableProfiling_Params)*pParamsEnables Profiling.

In

[CUPTI_AutoRange](https://docs.nvidia.com#group__cupti__profiler__api_1ggaa6faef578b53da403b15878e05d1b395aee196550a6a859439d2a4aa4ab531cf0), these APIs are used to enable/disable profiling for the kernels to be executed in a profiling session.**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv428cuptiProfilerEnableProfilingP37CUpti_Profiler_EnableProfiling_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerEndPass( ,[CUpti_Profiler_EndPass_Params](https://docs.nvidia.com/structCUpti__Profiler__EndPass__Params.html#_CPPv429CUpti_Profiler_EndPass_Params)*pParamsReplay API: used for multipass collection.

These APIs are used if user chooses to replay by itself

[CUPTI_UserReplay](https://docs.nvidia.com#group__cupti__profiler__api_1ggad6960f26de20f317a784ee565743e457aa052699f076ad798166b7b653b0ce14e)or[CUPTI_ApplicationReplay](https://docs.nvidia.com#group__cupti__profiler__api_1ggad6960f26de20f317a784ee565743e457a298b65c9526dabe7113fdb5b9e45c957)for multipass collection of the metrics configurations. Its a no-op in case of[CUPTI_KernelReplay](https://docs.nvidia.com#group__cupti__profiler__api_1ggad6960f26de20f317a784ee565743e457ac2e3d8f8e8ad65399ae39f6d0e266bc8). Returns information for next pass.**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv420cuptiProfilerEndPassP29CUpti_Profiler_EndPass_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerEndSession( ,[CUpti_Profiler_EndSession_Params](https://docs.nvidia.com/structCUpti__Profiler__EndSession__Params.html#_CPPv432CUpti_Profiler_EndSession_Params)*pParamsEnds profiling session.

Frees up the GPU resources acquired for profiling. Outside of a session, the GPU will return to it’s normal operating state.

**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv423cuptiProfilerEndSessionP32CUpti_Profiler_EndSession_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerFlushCounterData( ,[CUpti_Profiler_FlushCounterData_Params](https://docs.nvidia.com/structCUpti__Profiler__FlushCounterData__Params.html#_CPPv438CUpti_Profiler_FlushCounterData_Params)*pParamsDecode all the submitted passes.

Flush Counter data API to ensure every pass is decoded into the counterDataImage passed at beginSession. This will cause the CPU/GPU sync to collect all the undecoded pass.

**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv429cuptiProfilerFlushCounterDataP38CUpti_Profiler_FlushCounterData_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerGetCounterAvailability(
) Query counter availibility.

Use this API to query counter availability information in a buffer which can be used to filter unavailable raw metrics on host. Note: This API may fail, if any profiling or sampling session is active on the specified context or its device.


[#](https://docs.nvidia.com#_CPPv435cuptiProfilerGetCounterAvailabilityP44CUpti_Profiler_GetCounterAvailability_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerInitialize( ,[CUpti_Profiler_Initialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Initialize__Params.html#_CPPv432CUpti_Profiler_Initialize_Params)*pParamsInitializes the profiler interface.

Loads the required libraries in the process address space. Sets up the hooks with the CUDA driver.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_NOT_INITIALIZED**– if CUPTI could not dynamically load the nvperf* libraries. Ensure libnvperf_host.so and libnvperf_target.so, shipped alongside libcupti.so, are discoverable by the dynamic linker.



[#](https://docs.nvidia.com#_CPPv423cuptiProfilerInitializeP32CUpti_Profiler_Initialize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerIsPassCollected( ,[CUpti_Profiler_IsPassCollected_Params](https://docs.nvidia.com/structCUpti__Profiler__IsPassCollected__Params.html#_CPPv437CUpti_Profiler_IsPassCollected_Params)*pParamsAsynchronous call to query if the submitted pass to GPU is collected.

**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv428cuptiProfilerIsPassCollectedP37CUpti_Profiler_IsPassCollected_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerPopRange( ,[CUpti_Profiler_PopRange_Params](https://docs.nvidia.com/structCUpti__Profiler__PopRange__Params.html#_CPPv430CUpti_Profiler_PopRange_Params)*pParamsRange API’s : Pop user range.

Counter data is collected per unique range-stack. Identified by a string label passsed by the user. It’s an invalid operation in case of

[CUPTI_AutoRange](https://docs.nvidia.com#group__cupti__profiler__api_1ggaa6faef578b53da403b15878e05d1b395aee196550a6a859439d2a4aa4ab531cf0).**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv421cuptiProfilerPopRangeP30CUpti_Profiler_PopRange_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerPushRange( ,[CUpti_Profiler_PushRange_Params](https://docs.nvidia.com/structCUpti__Profiler__PushRange__Params.html#_CPPv431CUpti_Profiler_PushRange_Params)*pParamsRange API’s : Push user range.

Counter data is collected per unique range-stack. Identified by a string label passsed by the user. It’s an invalid operation in case of

[CUPTI_AutoRange](https://docs.nvidia.com#group__cupti__profiler__api_1ggaa6faef578b53da403b15878e05d1b395aee196550a6a859439d2a4aa4ab531cf0).**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv422cuptiProfilerPushRangeP31CUpti_Profiler_PushRange_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerSetConfig( ,[CUpti_Profiler_SetConfig_Params](https://docs.nvidia.com/structCUpti__Profiler__SetConfig__Params.html#_CPPv431CUpti_Profiler_SetConfig_Params)*pParamsSet metrics configuration to be profiled.

Use these APIs to set the config to profile in a session. It can be used for advanced cases such as where multiple configurations are collected into a single CounterData Image on the need basis, without restarting the session.

**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv422cuptiProfilerSetConfigP31CUpti_Profiler_SetConfig_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerUnsetConfig( ,[CUpti_Profiler_UnsetConfig_Params](https://docs.nvidia.com/structCUpti__Profiler__UnsetConfig__Params.html#_CPPv433CUpti_Profiler_UnsetConfig_Params)*pParamsUnset metrics configuration profiled.

**DEPRECATED**This function is deprecated as of CUDA 13.0 and will be removed in the future. It is recommended to use the Range Profiling API from the header cupti_range_profiler.h.

[#](https://docs.nvidia.com#_CPPv424cuptiProfilerUnsetConfigP33CUpti_Profiler_UnsetConfig_Params)