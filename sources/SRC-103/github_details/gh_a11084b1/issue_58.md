# [Issue #58] [Issue]: rocprofv3 only collecting HIP_API trace

source: https://github.com/ROCm/rocprofiler-sdk/issues/58
state: closed | updated: 2025-07-23T14:09:47Z
labels: Under Investigation

## 正文

### Problem Description

I'm evaluating rocprofv3 as a replacement for Radeon GPU Profiler, and I'm running into an issue where it's only collecting HIP_API traces.

Since I'm running a gfx1100 GPU I'm making sure to set the performance profile to stable before running any tests

```
============================================= ROCm System Management Interface =============================================
======================================================= Concise Info =======================================================
Device  Node  IDs              Temp    Power  Partitions          SCLK     MCLK     Fan    Perf        PwrCap  VRAM%  GPU%
              (DID,     GUID)  (Edge)  (Avg)  (Mem, Compute, ID)
============================================================================================================================
0       1     0x744c,   19824  41.0°C  83.0W  N/A, N/A, 0         1823Mhz  1249Mhz  34.9%  stable_std  303.0W  8%     100%
============================================================================================================================
=================================================== End of ROCm SMI Log ====================================================
```

For test evaluation I'm using [some incremental sgemm implementations](https://github.com/seb-v/fp32_sgemm_amd):

```
$ bash build.sh
$ rocprofv3 -S --sys-trace -- ./sgemm
```

I would expect the `--sys-trace` option to collect at least a HIP_API and HSA trace, but after the program finishes, the profiler only output a HIP_API trace:

```
E20250429 21:37:18.497306 124163256406080 output_stream.cpp:105] Opened result file: /home/delusional/Documents/fp32_sgemm_amd/delusionalStation/117142_hip_api_trace.csv
E20250429 21:37:18.543394 124163256406080 output_stream.cpp:105] Opened result file: /home/delusional/Documents/fp32_sgemm_amd/delusionalStation/117142_agent_info.csv
```

I've tried adding `-g` to the hipcc compiler commands (just as a hail mary) but that makes no difference. If I replace the `--sys-trace` with `--hsa-trace` the profiler produces no output besides the agent info.

The agent info file doesn't seem all that interesting (except for the model name, ip discovery is a real odd model name)

```
"Node_Id","Logical_Node_Id","Agent_Type","Cpu_Cores_Count","Simd_Count","Cpu_Core_Id_Base","Simd_Id_Base","Max_Waves_Per_Simd","Lds_Size_In_Kb","Gds_Size_In_Kb","Num_Gws","Wave_Front_Size","Num_Xcc","Cu_Count","Array_Count","Num_Shader_Banks","Simd_Arrays_Per_Engine","Cu_Per_Simd_Array","Simd_Per_Cu","Max_Slots_Scratch_Cu","Gfx_Target_Version","Vendor_Id","Device_Id","Location_Id","Domain","Drm_Render_Minor","Num_Sdma_Engines","Num_Sdma_Xgmi_Engines","Num_Sdma_Queues_Per_Engine","Num_Cp_Queues","Max_Engine_Clk_Ccompute","Max_Engine_Clk_Fcompute","Sdma_Fw_Version","Fw_Version","Capability","Cu_Per_Engine","Max_Waves_Per_Cu","Family_Id","Workgroup_Max_Size","Grid_Max_Size","Local_Mem_Size","Hive_Id","Gpu_Id","Workgroup_Max_Dim_X","Workgroup_Max_Dim_Y","Workgroup_Max_Dim_Z","Grid_Max_Dim_X","Grid_Max_Dim_Y","Grid_Max_Dim_Z","Name","Vendor_Name","Product_Name","Model_Name"
0,0,"CPU",16,0,0,0,0,0,0,0,0,1,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4560,0,0,0,0,0,0,23,0,0,0,0,0,0,0,0,0,0,0,"AMD Ryzen 7 3800X 8-Core Processor","CPU","AMD Ryzen 7 3800X 8-Core Processor",""
1,1,"GPU",0,192,0,2147487744,16,64,0,64,32,1,96,12,6,2,8,2,32,110000,4098,29772,3072,0,128,2,0,6,8,4560,2371,24,542,671588992,16,32,145,1024,4294967295,0,0,19824,1024,1024,1024,4294967295,4294967295,4294967295,"gfx1100","AMD","AMD Radeon RX 7900 XTX","ip discovery"
```

`rocprofv2` does successfully capture HSA and memory allocation information on this same system. I'm hoping rocprofv3 will provide better ATT output.

I also ran the test suite, just to give you a slightly more nuanced view of the entire system:

```
79% tests passed, 50 tests failed out of 242

Label Time Summary:
application-replay    =   5.89 sec*proc (5 tests)
integration-tests     = 148.04 sec*proc (111 tests)
pc-sampling           =   9.54 sec*proc (21 tests)
unittests             =   9.38 sec*proc (133 tests)

Total Test time (real) = 157.72 sec

The following tests did not run:
	 72 - pc_sampling.rocprofiler_configure_pc_sampling_service (Skipped)
	 74 - pc_sampling.pc_sampling_vs_dispatch_counter_collection (Skipped)
	 75 - pc_sampling.pc_sampling_vs_device_counter_collection (Skipped)
	 76 - pc_sampling.dispatch_counter_collection_vs_pc_sampling (Skipped)
	 77 - pc_sampling.device_counter_collection_vs_pc_sampling (Skipped)
	 78 - pc_sampling.query_configs_agent_does_not_exists (Skipped)
	 79 - pc_sampling.query_configs_after_service_setup (Skipped)
	 88 - rocprofiler_lib.agent_visibility_multigpu (Skipped)
	 89 - rocprofiler_lib.agent_visibility_inverted_multigpu (Skipped)
	149 - pc-sampling-integration-test (Skipped)
	209 - rocprofv3-test-execute-app-abort (Disabled)
	210 - rocprofv3-test-validate-app-abort (Disabled)
	220 - rocprofv3-test-pc-sampling-host-trap-exec-mask-manipulation-input-cmd-execute (Skipped)
	221 - rocprofv3-test-pc-sampling-host-trap-exec-mask-manipulation-input-json-execute (Skipped)
	222 - rocprofv3-test-pc-sampling-host-trap-exec-mask-manipulation-input-yaml-execute (Skipped)
	223 - rocprofv3-test-pc-sampling-host-trap-exec-mask-manipulation-input-cmd-validate (Skipped)
	224 - rocprofv3-test-pc-sampling-host-trap-exec-mask-manipulation-input-json-validate (Skipped)
	225 - rocprofv3-test-pc-sampling-host-trap-exec-mask-manipulation-input-yaml-validate (Skipped)
	226 - rocprofv3-test-pc-sampling-host-trap-transpose-multiple-agents-input-cmd-execute (Skipped)
	227 - rocprofv3-test-pc-sampling-host-trap-transpose-multiple-agents-input-json-execute (Skipped)
	228 - rocprofv3-test-pc-sampling-host-trap-transpose-multiple-agents-input-yaml-execute (Skipped)
	229 - rocprofv3-test-pc-sampling-host-trap-transpose-multiple-agents-input-cmd-validate (Skipped)
	230 - rocprofv3-test-pc-sampling-host-trap-transpose-multiple-agents-input-json-validate (Skipped)
	231 - rocprofv3-test-pc-sampling-host-trap-transpose-multiple-agents-input-yaml-validate (Skipped)

The following tests FAILED:
	 47 - device_counting_service_test.raw_sq_waves_verify (Subprocess aborted) unittests
	103 - rocprofiler_lib.callback_external_correlation (Failed) unittests
	104 - rocprofiler_lib.buffered_external_correlation (Failed) unittests
	105 - rocprofiler_lib.intercept_table_and_callback_tracing (Failed) unittests
	106 - rocprofiler_lib.intercept_table_and_callback_tracing_disable_context (Failed) unittests
	108 - rocprofiler_lib.callback_registration_lambda_with_result (Failed) unittests
	109 - rocprofiler_lib.buffer_registration_lambda_with_result (Failed) unittests
	135 - test-kernel-tracing-validate (Failed)             integration-tests
	137 - test-async-copy-tracing-validate (Failed)         integration-tests
	139 - test-memory-allocation-tracing-validate (Failed)  integration-tests
	141 - test-scratch-memory-tracing-validate (Failed)     integration-tests
	145 - test-page-migration-validate (Failed)             integration-tests
	146 - thread-trace-api-single-test (Subprocess aborted) integration-tests
	147 - thread-trace-api-multi-test (Subprocess aborted)  integration-tests
	148 - thread-trace-api-agent-test (Subprocess aborted)  integration-tests
	151 - test-hip-graph-tracing-validate (Failed)          integration-tests
	152 - test-counter-collection-execute (Subprocess aborted) integration-tests
	153 - test-counter-collection-validate (Failed)         integration-tests
	155 - test-conversion-script-convert (Failed)           integration-tests
	156 - test-conversion-script-validate (Failed)          integration-tests
	159 - rocprofv3-test-trace-validate (Failed)            integration-tests
	160 - rocprofv3-test-trace-input-json-validate (Failed) integration-tests
	163 - rocprofv3-test-systrace-validate (Failed)         integration-tests
	164 - rocprofv3-test-systrace-input-json-validate (Failed) integration-tests
	166 - rocprofv3-test-tracing-plus-counter-collection-validate-pmc_1 (Failed) application-replay integration-tests
	167 - rocprofv3-test-tracing-plus-counter-collection-validate-pmc_2 (Failed) application-replay integration-tests
	168 - rocprofv3-test-tracing-plus-counter-collection-validate-pmc_3 (Failed) application-replay integration-tests
	169 - rocprofv3-test-tracing-plus-counter-collection-validate-pmc_4 (Failed) application-replay integration-tests
	171 - rocprofv3-test-tracing-plus-counter-collection-cmdl-single-validate (Failed) integration-tests
	173 - rocprofv3-test-tracing-plus-counter-collection-cmdl-multiple-validate (Failed) integration-tests
	178 - rocprofv3-test-trace-hip-in-libraries-validate (Failed) integration-tests
	180 - rocprofv3-test-counter-collection-pmc1-validate (Failed) integration-tests
	182 - rocprofv3-test-counter-collection-txt-pmc2-execute-validate (Failed) integration-tests
	185 - rocprofv3-test-counter-collection-json-pmc1-validate (Failed) integration-tests
	186 - rocprofv3-test-counter-collection-yaml-pmc1-validate (Failed) integration-tests
	194 - rocprofv3-test-counter-collection-kernel-filtering-input-json-validate (Failed) integration-tests
	195 - rocprofv3-test-counter-collection-kernel-filtering-input-yaml-validate (Failed) integration-tests
	196 - rocprofv3-test-counter-collection-kernel-filtering-input-cmd-validate (Failed) integration-tests
	200 - rocprofv3-test-counter-collection-pmc1-extra-counters-validate (Failed) integration-tests
	202 - rocprofv3-test-hsa-multiqueue-validate (Failed)   integration-tests
	204 - rocprofv3-test-kernel-rename-cmd-line-validate (Failed) integration-tests
	206 - rocprofv3-test-kernel-rename-inp-yaml-validate (Failed) integration-tests
	208 - rocprofv3-test-memory-allocation-tracing-validate (Failed) integration-tests
	212 - rocprofv3-test-summary-cmd-line-validate (Failed) integration-tests
	214 - rocprofv3-test-summary-inp-yaml-validate (Failed) integration-tests
	216 - rocprofv3-test-roctracer-roctx-trace-validate (Failed) integration-tests
	219 - rocprofv3-test-scratch-memory-tracing-validate (Failed) integration-tests
	233 - rocprofv3-test-collection-period-validate (Failed) integration-tests
	237 - rocprofv3-test-hsa-multiqueue-att-cmd-validate (Failed) integration-tests
	238 - rocprofv3-test-hsa-multiqueue-att-json-validate (Failed) integration-tests
```

### Operating System

Arch Linux

### CPU

AMD Ryzen 7 3800X

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.3.3

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (17)

### ppanchad-amd · 2025-04-30

Hi @DelusionalLogic. Internal ticket has been created to investigate your issue. Thanks!

### huanrwan-amd · 2025-07-07

Hi @DelusionalLogic ,
Sorry for the late response, did you try with latest ROCm? https://rocm.docs.amd.com/en/latest/about/release-notes.html
I am able to collect all traces in your example, using:
`rocprofv3 -d ./result-output --output-format csv pftrace --sys-trace -- ./sgemm`

<img width="1019" height="316" alt="Image" src="https://github.com/user-attachments/assets/0d9bed28-e442-4e3d-80c7-6010c8d7841a" />

### DelusionalLogic · 2025-07-09

No worries about the timing, I'm not paying for this support :)

I'm still seeing the issue on rocm 6.4.1 after a full rebuild of rocprofiler-sdk commit e8e49fe76971000a42a5a177d9a727d16dd0ebcf.


```
$ rocprofiler-sdk/build/bin/rocprofv3 --output-format csv  --sys-trace -- ./sgemm
Kernel 0 : ROCBLAS
4.24461 ms -> 32391.5 GFLOPS
--------------------
Kernel 1 : Naive
135.068 ms -> 1017.93 GFLOPS
--------------------
Kernel 2 : LDS
33.7014 ms -> 4079.63 GFLOPS
--------------------
Kernel 3 : Registers
6.23919 ms -> 22036.4 GFLOPS
--------------------
Kernel 4 : GMEM Double buffer
5.17334 ms -> 26576.5 GFLOPS
--------------------
Kernel 5 :  LDS Utilization Optimization
4.37633 ms -> 31416.6 GFLOPS
--------------------
Kernel 6 : VALU optimizations
3.83212 ms -> 35878.1 GFLOPS
--------------------
Kernel 7 : Unroll inner loop
3.30915 ms -> 41548.2 GFLOPS
--------------------
Kernel 8 : Batched GMem loads
2.80619 ms -> 48995 GFLOPS
--------------------
E20250709 08:48:14.999374 140526283231552 output_stream.cpp:105] Opened result file: /home/delusional/Documents/fp32_sgemm_amd/delusionalStation/28448_hip_api_trace.csv
E20250709 08:48:15.038966 140526283231552 output_stream.cpp:105] Opened result file: /home/delusional/Documents/fp32_sgemm_amd/delusionalStation/28448_agent_info.csv
```

```
$ tree delusionalStation
delusionalStation
├── 28448_agent_info.csv
└── 28448_hip_api_trace.csv

1 directory, 2 files
```

### huanrwan-amd · 2025-07-09

@DelusionalLogic Can you please add logs while profiling: --log-level info? and post the logs?
`rocprofv3 -d ./result-output --output-format csv pftrace --sys-trace --log-level info -- ./sgemm`

### DelusionalLogic · 2025-07-09

Of course.

```
$ rocprofiler-sdk/build/bin/rocprofv3 --output-format csv --log-level info  --sys-trace -- ./sgemm

- rocprofv3 configuration:
	- ROCPROFILER_LIBRARY_CTOR=1
	- LD_PRELOAD=/home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/rocprofiler-sdk/librocprofiler-sdk-tool.so:/home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/librocprofiler-sdk.so:/home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/librocprofiler-sdk-roctx.so
	- ROCP_TOOL_LIBRARIES=/home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/rocprofiler-sdk/librocprofiler-sdk-tool.so
	- LD_LIBRARY_PATH=/home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib
	- ROCPROF_OUTPUT_PATH=/home/delusional/Documents/fp32_sgemm_amd
	- ROCPROF_OUTPUT_FORMAT=csv
	- ROCPROF_HIP_COMPILER_API_TRACE=1
	- ROCPROF_HIP_RUNTIME_API_TRACE=1
	- ROCPROF_HSA_CORE_API_TRACE=1
	- ROCPROF_HSA_AMD_EXT_API_TRACE=1
	- ROCPROF_HSA_IMAGE_EXT_API_TRACE=1
	- ROCPROF_HSA_FINALIZER_EXT_API_TRACE=1
	- ROCPROF_MARKER_API_TRACE=1
	- ROCPROF_RCCL_API_TRACE=1
	- ROCPROF_ROCDECODE_API_TRACE=1
	- ROCPROF_KERNEL_TRACE=1
	- ROCPROF_MEMORY_COPY_TRACE=1
	- ROCPROF_MEMORY_ALLOCATION_TRACE=1
	- ROCPROF_SCRATCH_MEMORY_TRACE=1
	- ROCPROF_STATS_SUMMARY_OUTPUT=stderr
	- ROCPROF_LOG_LEVEL=info
	- ROCPROFILER_LOG_LEVEL=info
	- ROCTX_LOG_LEVEL=info

logging initialized via ROCPROFILER_LOG_LEVEL. Log Level: info. Verbose Log Level: 3
rocprofiler_set_api_table("hip_compiler", 60400, 0, ..., 1)
rocprofiler initialize called...
rocprofiler initialize started...
invoke_client_configures
[ROCP_TOOL_LIBRARIES] searching /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/rocprofiler-sdk/librocprofiler-sdk-tool.so for rocprofiler_configure
Initializing rocprofiler-sdk library...
rocprofiler initialize called...
rocprofiler initialize ignored...
rocprofiler-sdk library initialized
I20250709 16:40:57.435762 140032605917504 agent.cpp:499] agent-1 (GPU 0) has a rocr index = 0
I20250709 16:40:57.435776 140032605917504 agent.cpp:439] agent-1 :: ROCR_VISIBLE_DEVICE = true
I20250709 16:40:57.435780 140032605917504 agent.cpp:431] agent-1 ::  HIP_VISIBLE_DEVICE = true
I20250709 16:40:57.435793 140032605917504 pc_sampling.cpp:54] PC sampling unavailable. The feature is implicitly disabled. To use it on a supported architecture, set ROCPROFILER_PC_SAMPLING_BETA_ENABLED=ON in the environment
I20250709 16:40:57.435896 140032605917504 registration.cpp:371] searching linux-vdso.so.1 for rocprofiler_configure
I20250709 16:40:57.435902 140032605917504 registration.cpp:387] Shared library 'linux-vdso.so.1' either does not exist or is a broken symbolic link
I20250709 16:40:57.435906 140032605917504 registration.cpp:371] searching /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/rocprofiler-sdk/librocprofiler-sdk-tool.so for rocprofiler_configure
I20250709 16:40:57.460718 140032605917504 registration.cpp:392] dlopening /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/rocprofiler-sdk/librocprofiler-sdk-tool.so for rocprofiler_configure
I20250709 16:40:57.460738 140032605917504 registration.cpp:371] searching /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/librocprofiler-sdk.so for rocprofiler_configure
I20250709 16:40:57.486446 140032605917504 registration.cpp:392] dlopening /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/librocprofiler-sdk.so for rocprofiler_configure
I20250709 16:40:57.486499 140032605917504 registration.cpp:402] |_/home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/librocprofiler-sdk.so did not contain rocprofiler_configure symbol
I20250709 16:40:57.486502 140032605917504 registration.cpp:371] searching /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/librocprofiler-sdk-roctx.so for rocprofiler_configure
I20250709 16:40:57.488482 140032605917504 registration.cpp:378] Shared library '/home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/librocprofiler-sdk-roctx.so' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.488529 140032605917504 registration.cpp:371] searching /opt/rocm/lib/librocblas.so.4 for rocprofiler_configure
I20250709 16:40:57.527516 140032605917504 registration.cpp:378] Shared library '/opt/rocm/lib/librocblas.so.4' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.528914 140032605917504 registration.cpp:371] searching /opt/rocm/lib/libamdhip64.so.6 for rocprofiler_configure
I20250709 16:40:57.537942 140032605917504 registration.cpp:378] Shared library '/opt/rocm/lib/libamdhip64.so.6' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.538324 140032605917504 registration.cpp:371] searching /usr/lib/libstdc++.so.6 for rocprofiler_configure
I20250709 16:40:57.558456 140032605917504 registration.cpp:378] Shared library '/usr/lib/libstdc++.so.6' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.558722 140032605917504 registration.cpp:371] searching /usr/lib/libm.so.6 for rocprofiler_configure
I20250709 16:40:57.559471 140032605917504 registration.cpp:378] Shared library '/usr/lib/libm.so.6' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.559482 140032605917504 registration.cpp:371] searching /usr/lib/libgcc_s.so.1 for rocprofiler_configure
I20250709 16:40:57.559971 140032605917504 registration.cpp:378] Shared library '/usr/lib/libgcc_s.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.559982 140032605917504 registration.cpp:371] searching /usr/lib/libc.so.6 for rocprofiler_configure
I20250709 16:40:57.561587 140032605917504 registration.cpp:378] Shared library '/usr/lib/libc.so.6' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.561616 140032605917504 registration.cpp:371] searching /usr/lib/libatomic.so.1 for rocprofiler_configure
I20250709 16:40:57.561971 140032605917504 registration.cpp:378] Shared library '/usr/lib/libatomic.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.561981 140032605917504 registration.cpp:371] searching /opt/rocm/lib/libamd_comgr.so.3 for rocprofiler_configure
I20250709 16:40:57.630056 140032605917504 registration.cpp:378] Shared library '/opt/rocm/lib/libamd_comgr.so.3' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.632154 140032605917504 registration.cpp:371] searching /usr/lib/libelf.so.1 for rocprofiler_configure
I20250709 16:40:57.632408 140032605917504 registration.cpp:378] Shared library '/usr/lib/libelf.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.632416 140032605917504 registration.cpp:371] searching /usr/lib/libdw.so.1 for rocprofiler_configure
I20250709 16:40:57.632850 140032605917504 registration.cpp:378] Shared library '/usr/lib/libdw.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.632860 140032605917504 registration.cpp:371] searching /lib64/ld-linux-x86-64.so.2 for rocprofiler_configure
I20250709 16:40:57.633021 140032605917504 registration.cpp:378] Shared library '/lib64/ld-linux-x86-64.so.2' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.633027 140032605917504 registration.cpp:371] searching /opt/rocm/lib/libhsa-amd-aqlprofile64.so.1 for rocprofiler_configure
I20250709 16:40:57.634172 140032605917504 registration.cpp:378] Shared library '/opt/rocm/lib/libhsa-amd-aqlprofile64.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.634190 140032605917504 registration.cpp:371] searching /usr/lib/libdrm.so.2 for rocprofiler_configure
I20250709 16:40:57.634429 140032605917504 registration.cpp:378] Shared library '/usr/lib/libdrm.so.2' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.634437 140032605917504 registration.cpp:371] searching /usr/lib/libdrm_amdgpu.so.1 for rocprofiler_configure
I20250709 16:40:57.634627 140032605917504 registration.cpp:378] Shared library '/usr/lib/libdrm_amdgpu.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.634633 140032605917504 registration.cpp:371] searching /opt/rocm/lib/librocprofiler-register.so.0 for rocprofiler_configure
I20250709 16:40:57.634872 140032605917504 registration.cpp:392] dlopening /opt/rocm/lib/librocprofiler-register.so.0 for rocprofiler_configure
I20250709 16:40:57.634899 140032605917504 registration.cpp:402] |_/opt/rocm/lib/librocprofiler-register.so.0 did not contain rocprofiler_configure symbol
I20250709 16:40:57.634902 140032605917504 registration.cpp:371] searching /opt/rocm/lib/../lib/libroctx64.so.4 for rocprofiler_configure
I20250709 16:40:57.635030 140032605917504 registration.cpp:378] Shared library '/opt/rocm/lib/../lib/libroctx64.so.4' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.635036 140032605917504 registration.cpp:371] searching /opt/rocm/lib/libhsa-runtime64.so.1 for rocprofiler_configure
I20250709 16:40:57.636186 140032605917504 registration.cpp:378] Shared library '/opt/rocm/lib/libhsa-runtime64.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.636200 140032605917504 registration.cpp:371] searching /usr/lib/libnuma.so.1 for rocprofiler_configure
I20250709 16:40:57.636407 140032605917504 registration.cpp:378] Shared library '/usr/lib/libnuma.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.636414 140032605917504 registration.cpp:371] searching /usr/lib/libz.so.1 for rocprofiler_configure
I20250709 16:40:57.636585 140032605917504 registration.cpp:378] Shared library '/usr/lib/libz.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.636591 140032605917504 registration.cpp:371] searching /usr/lib/libzstd.so.1 for rocprofiler_configure
I20250709 16:40:57.637144 140032605917504 registration.cpp:378] Shared library '/usr/lib/libzstd.so.1' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.637158 140032605917504 registration.cpp:371] searching /usr/lib/liblzma.so.5 for rocprofiler_configure
I20250709 16:40:57.637390 140032605917504 registration.cpp:378] Shared library '/usr/lib/liblzma.so.5' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.637398 140032605917504 registration.cpp:371] searching /usr/lib/libbz2.so.1.0 for rocprofiler_configure
I20250709 16:40:57.637547 140032605917504 registration.cpp:378] Shared library '/usr/lib/libbz2.so.1.0' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.637553 140032605917504 registration.cpp:371] searching /usr/lib/libfmt.so.11 for rocprofiler_configure
I20250709 16:40:57.637785 140032605917504 registration.cpp:378] Shared library '/usr/lib/libfmt.so.11' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.637793 140032605917504 registration.cpp:371] searching /usr/lib/libglog.so.2 for rocprofiler_configure
I20250709 16:40:57.638262 140032605917504 registration.cpp:378] Shared library '/usr/lib/libglog.so.2' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.638277 140032605917504 registration.cpp:371] searching /usr/lib/libgflags.so.2.2 for rocprofiler_configure
I20250709 16:40:57.638624 140032605917504 registration.cpp:378] Shared library '/usr/lib/libgflags.so.2.2' did not contain the 'rocprofiler_configure' symbol (search method: ELF parsing) required by rocprofiler-sdk for tools
I20250709 16:40:57.638639 140032605917504 registration.cpp:429] find_clients found 1 clients
I20250709 16:40:57.638646 140032605917504 registration.cpp:499] rocprofiler::registration::invoke_client_configures() invoking configure function from /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/lib/rocprofiler-sdk/librocprofiler-sdk-tool.so (addr=0x00007f5bea4aa210)
I20250709 16:40:57.638742 140032605917504 logging.cpp:159] logging initialized via ROCPROF_LOG_LEVEL. Log Level: info. Verbose Log Level: 3
I20250709 16:40:57.638792 140032605917504 tool.cpp:1955] rocprofv3 is using rocprofiler-sdk v0.6.0 (0.6.0)
I20250709 16:40:57.638797 140032605917504 registration.cpp:534] invoke_client_initializers
I20250709 16:40:57.638822 140032605917504 metrics.cpp:197] counter_defs.yaml is being looked up via install path
I20250709 16:40:57.638840 140032605917504 metrics.cpp:124] Loading Counter Config: /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/share/rocprofiler-sdk/counter_defs.yaml
I20250709 16:40:57.661351 140032605917504 metrics.cpp:197] counter_defs.yaml is being looked up via install path
I20250709 16:40:57.661380 140032605917504 metrics.cpp:124] Loading Counter Config: /home/delusional/Documents/fp32_sgemm_amd/rocprofiler-sdk/build/share/rocprofiler-sdk/counter_defs.yaml
I20250709 16:40:57.691986 140032605917504 tool.cpp:1570] creating dedicated callback thread for buffer 48216
I20250709 16:40:57.692124 140032605917504 tool.cpp:1574] assigning buffer 48216 to callback thread 1
I20250709 16:40:57.692129 140032605917504 tool.cpp:1570] creating dedicated callback thread for buffer 48217
I20250709 16:40:57.692228 140032605917504 tool.cpp:1574] assigning buffer 48217 to callback thread 2
I20250709 16:40:57.692240 140032605917504 tool.cpp:1570] creating dedicated callback thread for buffer 48212
I20250709 16:40:57.692338 140032605917504 tool.cpp:1574] assigning buffer 48212 to callback thread 3
I20250709 16:40:57.692342 140032605917504 tool.cpp:1570] creating dedicated callback thread for buffer 48213
I20250709 16:40:57.692449 140032605917504 tool.cpp:1574] assigning buffer 48213 to callback thread 4
I20250709 16:40:57.692454 140032605917504 tool.cpp:1570] creating dedicated callback thread for buffer 48214
I20250709 16:40:57.692569 140032605917504 tool.cpp:1574] assigning buffer 48214 to callback thread 5
I20250709 16:40:57.692579 140032605917504 tool.cpp:1570] creating dedicated callback thread for buffer 48215
I20250709 16:40:57.692695 140032605917504 tool.cpp:1574] assigning buffer 48215 to callback thread 6
I20250709 16:40:57.692700 140032605917504 tool.cpp:1570] creating dedicated callback thread for buffer 48218
I20250709 16:40:57.692803 140032605917504 tool.cpp:1574] assigning buffer 48218 to callback thread 7
I20250709 16:40:57.692809 140032605917504 tool.cpp:1570] creating dedicated callback thread for buffer 48219
I20250709 16:40:57.692911 140032605917504 tool.cpp:1574] assigning buffer 48219 to callback thread 8
I20250709 16:40:57.693438 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.694065 140032400676544 tool.cpp:763] Executing buffered tracing callback for 585 headers
I20250709 16:40:57.694487 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.694843 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.695189 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.695590 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.695945 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.696301 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.696627 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.697015 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.697397 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.697729 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.698096 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.698449 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.698819 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.699147 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
I20250709 16:40:57.699388 140032605917504 tool.cpp:1166] initializing rocprofv3...
I20250709 16:40:57.699400 140032605917504 tool.cpp:1994] rocprofv3: main function wrapper will be invoked...
Kernel 0 : ROCBLAS
I20250709 16:40:57.699422 140032605917504 registration.cpp:786] rocprofiler_set_api_table("hip", 60400, 0, ..., 1)
I20250709 16:40:57.699639 140032605917504 runtime_initialization.cpp:123] HIP runtime has been initialized
4.28931 ms -> 32054 GFLOPS
--------------------
Kernel 1 : Naive
146.287 ms -> 939.86 GFLOPS
--------------------
Kernel 2 : LDS
I20250709 16:41:01.520691 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
33.9027 ms -> 4055.41 GFLOPS
--------------------
Kernel 3 : Registers
6.23652 ms -> 22045.8 GFLOPS
--------------------
Kernel 4 : GMEM Double buffer
5.38551 ms -> 25529.5 GFLOPS
--------------------
Kernel 5 :  LDS Utilization Optimization
4.01258 ms -> 34264.5 GFLOPS
--------------------
Kernel 6 : VALU optimizations
I20250709 16:41:02.541273 140032400676544 tool.cpp:763] Executing buffered tracing callback for 567 headers
3.56114 ms -> 38608.2 GFLOPS
--------------------
Kernel 7 : Unroll inner loop
3.29162 ms -> 41769.5 GFLOPS
--------------------
Kernel 8 : Batched GMem loads
2.81282 ms -> 48879.6 GFLOPS
--------------------
I20250709 16:41:02.832309 140032605917504 tool.cpp:1998] rocprofv3: main function has returned with exit code: 0
I20250709 16:41:02.832321 140032605917504 tool.cpp:1183] invoked: finalize_rocprofv3
I20250709 16:41:02.832323 140032605917504 tool.cpp:1186] finalizing rocprofv3: caller='rocprofv3_main'...
I20250709 16:41:02.832327 140032605917504 registration.cpp:576] invoke_client_finalizer(client_id=2191994836)
I20250709 16:41:02.832350 140032605917504 tool.cpp:274] flushing buffers...
I20250709 16:41:02.832353 140032605917504 tool.cpp:279] flushing buffer 48216
I20250709 16:41:02.832384 140032409069248 buffer.cpp:211] buffer at 48216 is empty...
I20250709 16:41:02.832410 140032605917504 tool.cpp:279] flushing buffer 48217
I20250709 16:41:02.832447 140032400676544 tool.cpp:763] Executing buffered tracing callback for 279 headers
I20250709 16:41:02.832526 140032605917504 tool.cpp:279] flushing buffer 48212
I20250709 16:41:02.832550 140032392283840 buffer.cpp:211] buffer at 48212 is empty...
I20250709 16:41:02.832562 140032605917504 tool.cpp:279] flushing buffer 48213
I20250709 16:41:02.832578 140032174192320 buffer.cpp:211] buffer at 48213 is empty...
I20250709 16:41:02.832592 140032605917504 tool.cpp:279] flushing buffer 48214
I20250709 16:41:02.832610 140032165799616 buffer.cpp:211] buffer at 48214 is empty...
I20250709 16:41:02.832623 140032605917504 tool.cpp:279] flushing buffer 48215
I20250709 16:41:02.832639 140032157406912 buffer.cpp:211] buffer at 48215 is empty...
I20250709 16:41:02.832655 140032605917504 tool.cpp:279] flushing buffer 48218
I20250709 16:41:02.832673 140032149014208 buffer.cpp:211] buffer at 48218 is empty...
I20250709 16:41:02.832686 140032605917504 tool.cpp:279] flushing buffer 48219
I20250709 16:41:02.832698 140032140621504 buffer.cpp:211] buffer at 48219 is empty...
I20250709 16:41:02.832707 140032605917504 tool.cpp:283] Buffers flushed
I20250709 16:41:02.832712 140032605917504 tool.cpp:274] flushing buffers...
I20250709 16:41:02.832715 140032605917504 tool.cpp:279] flushing buffer 48216
I20250709 16:41:02.832726 140032409069248 buffer.cpp:211] buffer at 48216 is empty...
I20250709 16:41:02.832735 140032605917504 tool.cpp:279] flushing buffer 48217
I20250709 16:41:02.832747 140032400676544 buffer.cpp:211] buffer at 48217 is empty...
I20250709 16:41:02.832758 140032605917504 tool.cpp:279] flushing buffer 48212
I20250709 16:41:02.832769 140032392283840 buffer.cpp:211] buffer at 48212 is empty...
I20250709 16:41:02.832777 140032605917504 tool.cpp:279] flushing buffer 48213
I20250709 16:41:02.832788 140032174192320 buffer.cpp:211] buffer at 48213 is empty...
I20250709 16:41:02.832796 140032605917504 tool.cpp:279] flushing buffer 48214
I20250709 16:41:02.832808 140032165799616 buffer.cpp:211] buffer at 48214 is empty...
I20250709 16:41:02.832816 140032605917504 tool.cpp:279] flushing buffer 48215
I20250709 16:41:02.832827 140032157406912 buffer.cpp:211] buffer at 48215 is empty...
I20250709 16:41:02.832836 140032605917504 tool.cpp:279] flushing buffer 48218
I20250709 16:41:02.832845 140032149014208 buffer.cpp:211] buffer at 48218 is empty...
I20250709 16:41:02.832852 140032605917504 tool.cpp:279] flushing buffer 48219
I20250709 16:41:02.832863 140032140621504 buffer.cpp:211] buffer at 48219 is empty...
I20250709 16:41:02.832871 140032605917504 tool.cpp:283] Buffers flushed
I20250709 16:41:02.833413 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-kernel_trace.dat'...
I20250709 16:41:02.833852 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hsa_api_trace.dat'...
I20250709 16:41:02.833878 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hip_api_trace.dat'...
I20250709 16:41:02.836737 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hip_api_trace.dat'...
E20250709 16:41:02.836955 140032605917504 output_stream.cpp:105] Opened result file: /home/delusional/Documents/fp32_sgemm_amd/delusionalStation/44176_hip_api_trace.csv
I20250709 16:41:02.873781 140032605917504 csv_output_file.cpp:40] Closing result file: hip_api_trace
I20250709 16:41:02.874354 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-memory_copy_trace.dat'...
I20250709 16:41:02.874905 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-memory_allocation_trace.dat'...
I20250709 16:41:02.875385 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-marker_api_trace.dat'...
I20250709 16:41:02.875824 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-rccl_api_trace.dat'...
I20250709 16:41:02.876333 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-scratch_memory_trace.dat'...
I20250709 16:41:02.876831 140032605917504 tmp_file.cpp:123] opening temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-rocdecode_api_trace.dat'...
I20250709 16:41:02.876838 140032605917504 tool.cpp:1704] Number of services generating output: 9
E20250709 16:41:02.876982 140032605917504 output_stream.cpp:105] Opened result file: /home/delusional/Documents/fp32_sgemm_amd/delusionalStation/44176_agent_info.csv
I20250709 16:41:02.877014 140032605917504 csv_output_file.cpp:40] Closing result file: agent_info
I20250709 16:41:02.877028 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-kernel_trace.dat'...
I20250709 16:41:02.877031 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-kernel_trace.dat'...
I20250709 16:41:02.877038 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-kernel_trace.dat'...
I20250709 16:41:02.877093 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hsa_api_trace.dat'...
I20250709 16:41:02.877098 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hsa_api_trace.dat'...
I20250709 16:41:02.877106 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hsa_api_trace.dat'...
I20250709 16:41:02.877213 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hip_api_trace.dat'...
I20250709 16:41:02.877217 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hip_api_trace.dat'...
I20250709 16:41:02.877224 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-hip_api_trace.dat'...
I20250709 16:41:02.877860 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-memory_copy_trace.dat'...
I20250709 16:41:02.877865 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-memory_copy_trace.dat'...
I20250709 16:41:02.877872 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-memory_copy_trace.dat'...
I20250709 16:41:02.877900 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-memory_allocation_trace.dat'...
I20250709 16:41:02.877904 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-memory_allocation_trace.dat'...
I20250709 16:41:02.877911 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-memory_allocation_trace.dat'...
I20250709 16:41:02.877937 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-marker_api_trace.dat'...
I20250709 16:41:02.877940 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-marker_api_trace.dat'...
I20250709 16:41:02.877946 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-marker_api_trace.dat'...
I20250709 16:41:02.877972 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-scratch_memory_trace.dat'...
I20250709 16:41:02.877976 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-scratch_memory_trace.dat'...
I20250709 16:41:02.877982 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-scratch_memory_trace.dat'...
I20250709 16:41:02.878007 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-rccl_api_trace.dat'...
I20250709 16:41:02.878010 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-rccl_api_trace.dat'...
I20250709 16:41:02.878017 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-rccl_api_trace.dat'...
I20250709 16:41:02.878041 140032605917504 tmp_file.cpp:64] flushing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-rocdecode_api_trace.dat'...
I20250709 16:41:02.878045 140032605917504 tmp_file.cpp:91] closing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-rocdecode_api_trace.dat'...
I20250709 16:41:02.878052 140032605917504 tmp_file.cpp:134] removing temporary file: '/home/delusional/Documents/fp32_sgemm_amd/.rocprofv3/43268-44176-rocdecode_api_trace.dat'...
I20250709 16:41:02.878087 140032605917504 tool.cpp:2002] rocprofv3 finished. exit code: 0
I20250709 16:41:02.886164 140032605917504 tool.cpp:1183] invoked: finalize_rocprofv3
I20250709 16:41:02.886180 140032605917504 tool.cpp:1193] finalize_rocprofv3('atexit') ignored: already finalized
I20250709 16:41:02.886206 140032605917504 registration.cpp:706] finalizing rocprofiler (value=0)
I20250709 16:41:02.887279 140032605917504 registration.cpp:693] ignoring finalization request (value=1)
```

Please note that I do not include `pftrace` output. I don't think that makes a difference, and the extra output probably just makes it harder to understand what's going on.

### huanrwan-amd · 2025-07-09

@DelusionalLogic comparing with logs on my side, the successful case has hsa and hip runtime initialized:
```
I20250709 10:49:50.720236 137180312682752 registration.cpp:786] rocprofiler_set_api_table("hip", 60400, 0, ..., 1)
I20250709 10:49:50.720774 137180312682752 runtime_initialization.cpp:123] HIP runtime has been initialized
I20250709 10:49:50.744759 137180312682752 registration.cpp:786] rocprofiler_set_api_table("hsa", 71901, 0, ..., 1)
I20250709 10:49:50.744930 137180312682752 agent.cpp:1054] # agent node maps: 2
I20250709 10:49:50.745056 137180312682752 runtime_initialization.cpp:123] HSA runtime has been initialized
```
But in your logs there is only hip runtime:
```
I20250709 16:40:57.699422 140032605917504 registration.cpp:786] rocprofiler_set_api_table("hip", 60400, 0, ..., 1)
I20250709 16:40:57.699639 140032605917504 runtime_initialization.cpp:123] HIP runtime has been initialized
```
Have you update the ROCm and driver? I have ROCm 6.4.1 as the base and amdgpu driver as following
```
rocm22@rocm22:~/code/tool/github/fp32_sgemm_amd$ dkms status
amdgpu/6.12.12-2164967.22.04, 6.8.0-52-generic, x86_64: installed
rocm22@rocm22:~/code/tool/github/fp32_sgemm_amd$ amd-smi
AMD System Management Interface | Version: 25.4.2+aca1101 | ROCm version: 6.4.1 |
```


### DelusionalLogic · 2025-07-09

I'm running the amdgpu kernel module provided by arch in the `linux-firmware-amdgpu` package.

```
$ modinfo amdgpu
filename:       /lib/modules/6.15.4-arch2-1/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko.zst
license:        GPL and additional rights
description:    AMD GPU
author:         AMD linux driver team
firmware:       amdgpu/navi12_gpu_info.bin
firmware:       amdgpu/arcturus_gpu_info.bin
firmware:       amdgpu/raven2_gpu_info.bin
firmware:       amdgpu/picasso_gpu_info.bin
firmware:       amdgpu/raven_gpu_info.bin
firmware:       amdgpu/vega12_gpu_info.bin
firmware:       amdgpu/vega10_gpu_info.bin
import_ns:      DMA_BUF
firmware:       amdgpu/aldebaran_ip_discovery.bin
firmware:       amdgpu/arcturus_ip_discovery.bin
firmware:       amdgpu/picasso_ip_discovery.bin
firmware:       amdgpu/raven2_ip_discovery.bin
firmware:       amdgpu/raven_ip_discovery.bin
firmware:       amdgpu/vega20_ip_discovery.bin
firmware:       amdgpu/vega12_ip_discovery.bin
firmware:       amdgpu/vega10_ip_discovery.bin
firmware:       amdgpu/ip_discovery.bin
firmware:       amdgpu/mullins_mec.bin
firmware:       amdgpu/mullins_rlc.bin
firmware:       amdgpu/mullins_ce.bin
firmware:       amdgpu/mullins_me.bin
firmware:       amdgpu/mullins_pfp.bin
firmware:       amdgpu/kabini_mec.bin
firmware:       amdgpu/kabini_rlc.bin
firmware:       amdgpu/kabini_ce.bin
firmware:       amdgpu/kabini_me.bin
firmware:       amdgpu/kabini_pfp.bin
firmware:       amdgpu/kaveri_mec2.bin
firmware:       amdgpu/kaveri_mec.bin
firmware:       amdgpu/kaveri_rlc.bin
firmware:       amdgpu/kaveri_ce.bin
firmware:       amdgpu/kaveri_me.bin
firmware:       amdgpu/kaveri_pfp.bin
firmware:       amdgpu/hawaii_mec.bin
firmware:       amdgpu/hawaii_rlc.bin
firmware:       amdgpu/hawaii_ce.bin
firmware:       amdgpu/hawaii_me.bin
firmware:       amdgpu/hawaii_pfp.bin
firmware:       amdgpu/bonaire_mec.bin
firmware:       amdgpu/bonaire_rlc.bin
firmware:       amdgpu/bonaire_ce.bin
firmware:       amdgpu/bonaire_me.bin
firmware:       amdgpu/bonaire_pfp.bin
firmware:       amdgpu/mullins_sdma1.bin
firmware:       amdgpu/mullins_sdma.bin
firmware:       amdgpu/kabini_sdma1.bin
firmware:       amdgpu/kabini_sdma.bin
firmware:       amdgpu/kaveri_sdma1.bin
firmware:       amdgpu/kaveri_sdma.bin
firmware:       amdgpu/hawaii_sdma1.bin
firmware:       amdgpu/hawaii_sdma.bin
firmware:       amdgpu/bonaire_sdma1.bin
firmware:       amdgpu/bonaire_sdma.bin
firmware:       amdgpu/si58_mc.bin
firmware:       amdgpu/hainan_mc.bin
firmware:       amdgpu/oland_mc.bin
firmware:       amdgpu/verde_mc.bin
firmware:       amdgpu/pitcairn_mc.bin
firmware:       amdgpu/tahiti_mc.bin
firmware:       amdgpu/hainan_rlc.bin
firmware:       amdgpu/hainan_ce.bin
firmware:       amdgpu/hainan_me.bin
firmware:       amdgpu/hainan_pfp.bin
firmware:       amdgpu/oland_rlc.bin
firmware:       amdgpu/oland_ce.bin
firmware:       amdgpu/oland_me.bin
firmware:       amdgpu/oland_pfp.bin
firmware:       amdgpu/verde_rlc.bin
firmware:       amdgpu/verde_ce.bin
firmware:       amdgpu/verde_me.bin
firmware:       amdgpu/verde_pfp.bin
firmware:       amdgpu/pitcairn_rlc.bin
firmware:       amdgpu/pitcairn_ce.bin
firmware:       amdgpu/pitcairn_me.bin
firmware:       amdgpu/pitcairn_pfp.bin
firmware:       amdgpu/tahiti_rlc.bin
firmware:       amdgpu/tahiti_ce.bin
firmware:       amdgpu/tahiti_me.bin
firmware:       amdgpu/tahiti_pfp.bin
firmware:       amdgpu/topaz_mc.bin
firmware:       amdgpu/hawaii_mc.bin
firmware:       amdgpu/bonaire_mc.bin
firmware:       amdgpu/polaris12_k_mc.bin
firmware:       amdgpu/polaris10_k_mc.bin
firmware:       amdgpu/polaris11_k_mc.bin
firmware:       amdgpu/polaris12_32_mc.bin
firmware:       amdgpu/polaris12_mc.bin
firmware:       amdgpu/polaris10_mc.bin
firmware:       amdgpu/polaris11_mc.bin
firmware:       amdgpu/tonga_mc.bin
firmware:       amdgpu/vega12_asd.bin
firmware:       amdgpu/vega12_sos.bin
firmware:       amdgpu/vega10_cap.bin
firmware:       amdgpu/vega10_asd.bin
firmware:       amdgpu/vega10_sos.bin
firmware:       amdgpu/raven_ta.bin
firmware:       amdgpu/raven2_ta.bin
firmware:       amdgpu/picasso_ta.bin
firmware:       amdgpu/raven2_asd.bin
firmware:       amdgpu/picasso_asd.bin
firmware:       amdgpu/raven_asd.bin
firmware:       amdgpu/beige_goby_ta.bin
firmware:       amdgpu/beige_goby_sos.bin
firmware:       amdgpu/dimgrey_cavefish_ta.bin
firmware:       amdgpu/dimgrey_cavefish_sos.bin
firmware:       amdgpu/vangogh_toc.bin
firmware:       amdgpu/vangogh_asd.bin
firmware:       amdgpu/navy_flounder_ta.bin
firmware:       amdgpu/navy_flounder_sos.bin
firmware:       amdgpu/sienna_cichlid_cap.bin
firmware:       amdgpu/sienna_cichlid_ta.bin
firmware:       amdgpu/sienna_cichlid_sos.bin
firmware:       amdgpu/arcturus_ta.bin
firmware:       amdgpu/arcturus_asd.bin
firmware:       amdgpu/arcturus_sos.bin
firmware:       amdgpu/navi12_cap.bin
firmware:       amdgpu/navi12_ta.bin
firmware:       amdgpu/navi12_asd.bin
firmware:       amdgpu/navi12_sos.bin
firmware:       amdgpu/navi14_ta.bin
firmware:       amdgpu/navi14_asd.bin
firmware:       amdgpu/navi14_sos.bin
firmware:       amdgpu/navi10_ta.bin
firmware:       amdgpu/navi10_asd.bin
firmware:       amdgpu/navi10_sos.bin
firmware:       amdgpu/vega20_ta.bin
firmware:       amdgpu/vega20_asd.bin
firmware:       amdgpu/vega20_sos.bin
firmware:       amdgpu/green_sardine_ta.bin
firmware:       amdgpu/green_sardine_asd.bin
firmware:       amdgpu/renoir_ta.bin
firmware:       amdgpu/renoir_asd.bin
firmware:       amdgpu/psp_14_0_4_ta.bin
firmware:       amdgpu/psp_14_0_4_toc.bin
firmware:       amdgpu/psp_14_0_1_ta.bin
firmware:       amdgpu/psp_14_0_1_toc.bin
firmware:       amdgpu/psp_14_0_0_ta.bin
firmware:       amdgpu/psp_14_0_0_toc.bin
firmware:       amdgpu/psp_13_0_14_ta.bin
firmware:       amdgpu/psp_13_0_14_sos.bin
firmware:       amdgpu/psp_13_0_12_ta.bin
firmware:       amdgpu/psp_13_0_12_sos.bin
firmware:       amdgpu/psp_13_0_6_ta.bin
firmware:       amdgpu/psp_13_0_6_sos.bin
firmware:       amdgpu/psp_13_0_11_ta.bin
firmware:       amdgpu/psp_13_0_11_toc.bin
firmware:       amdgpu/psp_13_0_10_ta.bin
firmware:       amdgpu/psp_13_0_10_sos.bin
firmware:       amdgpu/psp_13_0_7_ta.bin
firmware:       amdgpu/psp_13_0_7_sos.bin
firmware:       amdgpu/psp_13_0_0_ta.bin
firmware:       amdgpu/psp_13_0_0_sos.bin
firmware:       amdgpu/psp_13_0_8_ta.bin
firmware:       amdgpu/psp_13_0_8_toc.bin
firmware:       amdgpu/psp_13_0_5_ta.bin
firmware:       amdgpu/psp_13_0_5_toc.bin
firmware:       amdgpu/yellow_carp_ta.bin
firmware:       amdgpu/yellow_carp_toc.bin
firmware:       amdgpu/aldebaran_cap.bin
firmware:       amdgpu/aldebaran_ta.bin
firmware:       amdgpu/aldebaran_sos.bin
firmware:       amdgpu/psp_13_0_4_ta.bin
firmware:       amdgpu/psp_13_0_4_toc.bin
firmware:       amdgpu/psp_14_0_5_ta.bin
firmware:       amdgpu/psp_14_0_5_toc.bin
firmware:       amdgpu/psp_14_0_3_ta.bin
firmware:       amdgpu/psp_14_0_3_sos.bin
firmware:       amdgpu/psp_14_0_2_ta.bin
firmware:       amdgpu/psp_14_0_2_sos.bin
firmware:       amdgpu/vegam_rlc.bin
firmware:       amdgpu/vegam_mec2.bin
firmware:       amdgpu/vegam_mec.bin
firmware:       amdgpu/vegam_me.bin
firmware:       amdgpu/vegam_pfp.bin
firmware:       amdgpu/vegam_ce.bin
firmware:       amdgpu/polaris12_rlc.bin
firmware:       amdgpu/polaris12_mec2_2.bin
firmware:       amdgpu/polaris12_mec2.bin
firmware:       amdgpu/polaris12_mec_2.bin
firmware:       amdgpu/polaris12_mec.bin
firmware:       amdgpu/polaris12_me_2.bin
firmware:       amdgpu/polaris12_me.bin
firmware:       amdgpu/polaris12_pfp_2.bin
firmware:       amdgpu/polaris12_pfp.bin
firmware:       amdgpu/polaris12_ce_2.bin
firmware:       amdgpu/polaris12_ce.bin
firmware:       amdgpu/polaris11_rlc.bin
firmware:       amdgpu/polaris11_mec2_2.bin
firmware:       amdgpu/polaris11_mec2.bin
firmware:       amdgpu/polaris11_mec_2.bin
firmware:       amdgpu/polaris11_mec.bin
firmware:       amdgpu/polaris11_me_2.bin
firmware:       amdgpu/polaris11_me.bin
firmware:       amdgpu/polaris11_pfp_2.bin
firmware:       amdgpu/polaris11_pfp.bin
firmware:       amdgpu/polaris11_ce_2.bin
firmware:       amdgpu/polaris11_ce.bin
firmware:       amdgpu/polaris10_rlc.bin
firmware:       amdgpu/polaris10_mec2_2.bin
firmware:       amdgpu/polaris10_mec2.bin
firmware:       amdgpu/polaris10_mec_2.bin
firmware:       amdgpu/polaris10_mec.bin
firmware:       amdgpu/polaris10_me_2.bin
firmware:       amdgpu/polaris10_me.bin
firmware:       amdgpu/polaris10_pfp_2.bin
firmware:       amdgpu/polaris10_pfp.bin
firmware:       amdgpu/polaris10_ce_2.bin
firmware:       amdgpu/polaris10_ce.bin
firmware:       amdgpu/fiji_rlc.bin
firmware:       amdgpu/fiji_mec2.bin
firmware:       amdgpu/fiji_mec.bin
firmware:       amdgpu/fiji_me.bin
firmware:       amdgpu/fiji_pfp.bin
firmware:       amdgpu/fiji_ce.bin
firmware:       amdgpu/topaz_rlc.bin
firmware:       amdgpu/topaz_mec.bin
firmware:       amdgpu/topaz_me.bin
firmware:       amdgpu/topaz_pfp.bin
firmware:       amdgpu/topaz_ce.bin
firmware:       amdgpu/tonga_rlc.bin
firmware:       amdgpu/tonga_mec2.bin
firmware:       amdgpu/tonga_mec.bin
firmware:       amdgpu/tonga_me.bin
firmware:       amdgpu/tonga_pfp.bin
firmware:       amdgpu/tonga_ce.bin
firmware:       amdgpu/stoney_rlc.bin
firmware:       amdgpu/stoney_mec.bin
firmware:       amdgpu/stoney_me.bin
firmware:       amdgpu/stoney_pfp.bin
firmware:       amdgpu/stoney_ce.bin
firmware:       amdgpu/carrizo_rlc.bin
firmware:       amdgpu/carrizo_mec2.bin
firmware:       amdgpu/carrizo_mec.bin
firmware:       amdgpu/carrizo_me.bin
firmware:       amdgpu/carrizo_pfp.bin
firmware:       amdgpu/carrizo_ce.bin
firmware:       amdgpu/aldebaran_sjt_mec2.bin
firmware:       amdgpu/aldebaran_sjt_mec.bin
firmware:       amdgpu/aldebaran_rlc.bin
firmware:       amdgpu/aldebaran_mec2.bin
firmware:       amdgpu/aldebaran_mec.bin
firmware:       amdgpu/green_sardine_rlc.bin
firmware:       amdgpu/green_sardine_mec2.bin
firmware:       amdgpu/green_sardine_mec.bin
firmware:       amdgpu/green_sardine_me.bin
firmware:       amdgpu/green_sardine_pfp.bin
firmware:       amdgpu/green_sardine_ce.bin
firmware:       amdgpu/renoir_rlc.bin
firmware:       amdgpu/renoir_mec.bin
firmware:       amdgpu/renoir_me.bin
firmware:       amdgpu/renoir_pfp.bin
firmware:       amdgpu/renoir_ce.bin
firmware:       amdgpu/arcturus_rlc.bin
firmware:       amdgpu/arcturus_mec.bin
firmware:       amdgpu/raven_kicker_rlc.bin
firmware:       amdgpu/raven2_rlc.bin
firmware:       amdgpu/raven2_mec2.bin
firmware:       amdgpu/raven2_mec.bin
firmware:       amdgpu/raven2_me.bin
firmware:       amdgpu/raven2_pfp.bin
firmware:       amdgpu/raven2_ce.bin
firmware:       amdgpu/picasso_rlc_am4.bin
firmware:       amdgpu/picasso_rlc.bin
firmware:       amdgpu/picasso_mec2.bin
firmware:       amdgpu/picasso_mec.bin
firmware:       amdgpu/picasso_me.bin
firmware:       amdgpu/picasso_pfp.bin
firmware:       amdgpu/picasso_ce.bin
firmware:       amdgpu/raven_rlc.bin
firmware:       amdgpu/raven_mec2.bin
firmware:       amdgpu/raven_mec.bin
firmware:       amdgpu/raven_me.bin
firmware:       amdgpu/raven_pfp.bin
firmware:       amdgpu/raven_ce.bin
firmware:       amdgpu/vega20_rlc.bin
firmware:       amdgpu/vega20_mec2.bin
firmware:       amdgpu/vega20_mec.bin
firmware:       amdgpu/vega20_me.bin
firmware:       amdgpu/vega20_pfp.bin
firmware:       amdgpu/vega20_ce.bin
firmware:       amdgpu/vega12_rlc.bin
firmware:       amdgpu/vega12_mec2.bin
firmware:       amdgpu/vega12_mec.bin
firmware:       amdgpu/vega12_me.bin
firmware:       amdgpu/vega12_pfp.bin
firmware:       amdgpu/vega12_ce.bin
firmware:       amdgpu/vega10_rlc.bin
firmware:       amdgpu/vega10_mec2.bin
firmware:       amdgpu/vega10_mec.bin
firmware:       amdgpu/vega10_me.bin
firmware:       amdgpu/vega10_pfp.bin
firmware:       amdgpu/vega10_ce.bin
firmware:       amdgpu/gc_9_4_4_sjt_mec.bin
firmware:       amdgpu/gc_9_4_3_sjt_mec.bin
firmware:       amdgpu/gc_9_5_0_rlc.bin
firmware:       amdgpu/gc_9_4_4_rlc.bin
firmware:       amdgpu/gc_9_4_3_rlc.bin
firmware:       amdgpu/gc_9_5_0_mec.bin
firmware:       amdgpu/gc_9_4_4_mec.bin
firmware:       amdgpu/gc_9_4_3_mec.bin
firmware:       amdgpu/gc_10_3_7_rlc.bin
firmware:       amdgpu/gc_10_3_7_mec2.bin
firmware:       amdgpu/gc_10_3_7_mec.bin
firmware:       amdgpu/gc_10_3_7_me.bin
firmware:       amdgpu/gc_10_3_7_pfp.bin
firmware:       amdgpu/gc_10_3_7_ce.bin
firmware:       amdgpu/gc_10_3_6_rlc.bin
firmware:       amdgpu/gc_10_3_6_mec2.bin
firmware:       amdgpu/gc_10_3_6_mec.bin
firmware:       amdgpu/gc_10_3_6_me.bin
firmware:       amdgpu/gc_10_3_6_pfp.bin
firmware:       amdgpu/gc_10_3_6_ce.bin
firmware:       amdgpu/cyan_skillfish2_rlc.bin
firmware:       amdgpu/cyan_skillfish2_mec2.bin
firmware:       amdgpu/cyan_skillfish2_mec.bin
firmware:       amdgpu/cyan_skillfish2_me.bin
firmware:       amdgpu/cyan_skillfish2_pfp.bin
firmware:       amdgpu/cyan_skillfish2_ce.bin
firmware:       amdgpu/yellow_carp_rlc.bin
firmware:       amdgpu/yellow_carp_mec2.bin
firmware:       amdgpu/yellow_carp_mec.bin
firmware:       amdgpu/yellow_carp_me.bin
firmware:       amdgpu/yellow_carp_pfp.bin
firmware:       amdgpu/yellow_carp_ce.bin
firmware:       amdgpu/beige_goby_rlc.bin
firmware:       amdgpu/beige_goby_mec2.bin
firmware:       amdgpu/beige_goby_mec.bin
firmware:       amdgpu/beige_goby_me.bin
firmware:       amdgpu/beige_goby_pfp.bin
firmware:       amdgpu/beige_goby_ce.bin
firmware:       amdgpu/dimgrey_cavefish_rlc.bin
firmware:       amdgpu/dimgrey_cavefish_mec2.bin
firmware:       amdgpu/dimgrey_cavefish_mec.bin
firmware:       amdgpu/dimgrey_cavefish_me.bin
firmware:       amdgpu/dimgrey_cavefish_pfp.bin
firmware:       amdgpu/dimgrey_cavefish_ce.bin
firmware:       amdgpu/vangogh_rlc.bin
firmware:       amdgpu/vangogh_mec2.bin
firmware:       amdgpu/vangogh_mec.bin
firmware:       amdgpu/vangogh_me.bin
firmware:       amdgpu/vangogh_pfp.bin
firmware:       amdgpu/vangogh_ce.bin
firmware:       amdgpu/navy_flounder_rlc.bin
firmware:       amdgpu/navy_flounder_mec2.bin
firmware:       amdgpu/navy_flounder_mec.bin
firmware:       amdgpu/navy_flounder_me.bin
firmware:       amdgpu/navy_flounder_pfp.bin
firmware:       amdgpu/navy_flounder_ce.bin
firmware:       amdgpu/sienna_cichlid_rlc.bin
firmware:       amdgpu/sienna_cichlid_mec2.bin
firmware:       amdgpu/sienna_cichlid_mec.bin
firmware:       amdgpu/sienna_cichlid_me.bin
firmware:       amdgpu/sienna_cichlid_pfp.bin
firmware:       amdgpu/sienna_cichlid_ce.bin
firmware:       amdgpu/navi12_rlc.bin
firmware:       amdgpu/navi12_mec2.bin
firmware:       amdgpu/navi12_mec.bin
firmware:       amdgpu/navi12_me.bin
firmware:       amdgpu/navi12_pfp.bin
firmware:       amdgpu/navi12_ce.bin
firmware:       amdgpu/navi14_rlc.bin
firmware:       amdgpu/navi14_mec2.bin
firmware:       amdgpu/navi14_mec.bin
firmware:       amdgpu/navi14_me.bin
firmware:       amdgpu/navi14_pfp.bin
firmware:       amdgpu/navi14_ce.bin
firmware:       amdgpu/navi14_mec2_wks.bin
firmware:       amdgpu/navi14_mec_wks.bin
firmware:       amdgpu/navi14_me_wks.bin
firmware:       amdgpu/navi14_pfp_wks.bin
firmware:       amdgpu/navi14_ce_wks.bin
firmware:       amdgpu/navi10_rlc.bin
firmware:       amdgpu/navi10_mec2.bin
firmware:       amdgpu/navi10_mec.bin
firmware:       amdgpu/navi10_me.bin
firmware:       amdgpu/navi10_pfp.bin
firmware:       amdgpu/navi10_ce.bin
firmware:       amdgpu/gc_11_5_3_imu.bin
firmware:       amdgpu/gc_11_5_2_imu.bin
firmware:       amdgpu/gc_11_5_1_imu.bin
firmware:       amdgpu/gc_11_5_0_imu.bin
firmware:       amdgpu/gc_11_0_4_imu.bin
firmware:       amdgpu/gc_11_0_3_imu.bin
firmware:       amdgpu/gc_11_0_2_imu.bin
firmware:       amdgpu/gc_11_0_1_imu.bin
firmware:       amdgpu/gc_11_0_0_imu.bin
firmware:       amdgpu/gc_11_5_3_rlc.bin
firmware:       amdgpu/gc_11_5_3_mec.bin
firmware:       amdgpu/gc_11_5_3_me.bin
firmware:       amdgpu/gc_11_5_3_pfp.bin
firmware:       amdgpu/gc_11_5_2_rlc.bin
firmware:       amdgpu/gc_11_5_2_mec.bin
firmware:       amdgpu/gc_11_5_2_me.bin
firmware:       amdgpu/gc_11_5_2_pfp.bin
firmware:       amdgpu/gc_11_5_1_rlc.bin
firmware:       amdgpu/gc_11_5_1_mec.bin
firmware:       amdgpu/gc_11_5_1_me.bin
firmware:       amdgpu/gc_11_5_1_pfp.bin
firmware:       amdgpu/gc_11_5_0_rlc.bin
firmware:       amdgpu/gc_11_5_0_mec.bin
firmware:       amdgpu/gc_11_5_0_me.bin
firmware:       amdgpu/gc_11_5_0_pfp.bin
firmware:       amdgpu/gc_11_0_4_rlc.bin
firmware:       amdgpu/gc_11_0_4_mec.bin
firmware:       amdgpu/gc_11_0_4_me.bin
firmware:       amdgpu/gc_11_0_4_pfp.bin
firmware:       amdgpu/gc_11_0_3_rlc.bin
firmware:       amdgpu/gc_11_0_3_mec.bin
firmware:       amdgpu/gc_11_0_3_me.bin
firmware:       amdgpu/gc_11_0_3_pfp.bin
firmware:       amdgpu/gc_11_0_2_rlc.bin
firmware:       amdgpu/gc_11_0_2_mec.bin
firmware:       amdgpu/gc_11_0_2_me.bin
firmware:       amdgpu/gc_11_0_2_pfp.bin
firmware:       amdgpu/gc_11_0_1_rlc.bin
firmware:       amdgpu/gc_11_0_1_mec.bin
firmware:       amdgpu/gc_11_0_1_me.bin
firmware:       amdgpu/gc_11_0_1_pfp.bin
firmware:       amdgpu/gc_11_0_0_toc.bin
firmware:       amdgpu/gc_11_0_0_rlc_1.bin
firmware:       amdgpu/gc_11_0_0_rlc.bin
firmware:       amdgpu/gc_11_0_0_mec.bin
firmware:       amdgpu/gc_11_0_0_me.bin
firmware:       amdgpu/gc_11_0_0_pfp.bin
firmware:       amdgpu/gc_12_0_1_toc.bin
firmware:       amdgpu/gc_12_0_1_rlc.bin
firmware:       amdgpu/gc_12_0_1_mec.bin
firmware:       amdgpu/gc_12_0_1_me.bin
firmware:       amdgpu/gc_12_0_1_pfp.bin
firmware:       amdgpu/gc_12_0_0_toc.bin
firmware:       amdgpu/gc_12_0_0_rlc.bin
firmware:       amdgpu/gc_12_0_0_mec.bin
firmware:       amdgpu/gc_12_0_0_me.bin
firmware:       amdgpu/gc_12_0_0_pfp.bin
firmware:       amdgpu/gc_12_0_1_imu.bin
firmware:       amdgpu/gc_12_0_0_imu.bin
firmware:       amdgpu/topaz_sdma1.bin
firmware:       amdgpu/topaz_sdma.bin
firmware:       amdgpu/vegam_sdma1.bin
firmware:       amdgpu/vegam_sdma.bin
firmware:       amdgpu/polaris12_sdma1.bin
firmware:       amdgpu/polaris12_sdma.bin
firmware:       amdgpu/polaris11_sdma1.bin
firmware:       amdgpu/polaris11_sdma.bin
firmware:       amdgpu/polaris10_sdma1.bin
firmware:       amdgpu/polaris10_sdma.bin
firmware:       amdgpu/stoney_sdma.bin
firmware:       amdgpu/fiji_sdma1.bin
firmware:       amdgpu/fiji_sdma.bin
firmware:       amdgpu/carrizo_sdma1.bin
firmware:       amdgpu/carrizo_sdma.bin
firmware:       amdgpu/tonga_sdma1.bin
firmware:       amdgpu/tonga_sdma.bin
firmware:       amdgpu/aldebaran_sdma.bin
firmware:       amdgpu/green_sardine_sdma.bin
firmware:       amdgpu/renoir_sdma.bin
firmware:       amdgpu/arcturus_sdma.bin
firmware:       amdgpu/raven2_sdma.bin
firmware:       amdgpu/picasso_sdma.bin
firmware:       amdgpu/raven_sdma.bin
firmware:       amdgpu/vega20_sdma1.bin
firmware:       amdgpu/vega20_sdma.bin
firmware:       amdgpu/vega12_sdma1.bin
firmware:       amdgpu/vega12_sdma.bin
firmware:       amdgpu/vega10_sdma1.bin
firmware:       amdgpu/vega10_sdma.bin
firmware:       amdgpu/sdma_4_4_5.bin
firmware:       amdgpu/sdma_4_4_2.bin
firmware:       amdgpu/cyan_skillfish2_sdma1.bin
firmware:       amdgpu/cyan_skillfish2_sdma.bin
firmware:       amdgpu/navi12_sdma1.bin
firmware:       amdgpu/navi12_sdma.bin
firmware:       amdgpu/navi14_sdma1.bin
firmware:       amdgpu/navi14_sdma.bin
firmware:       amdgpu/navi10_sdma1.bin
firmware:       amdgpu/navi10_sdma.bin
firmware:       amdgpu/sdma_5_2_7.bin
firmware:       amdgpu/sdma_5_2_6.bin
firmware:       amdgpu/yellow_carp_sdma.bin
firmware:       amdgpu/vangogh_sdma.bin
firmware:       amdgpu/beige_goby_sdma.bin
firmware:       amdgpu/dimgrey_cavefish_sdma.bin
firmware:       amdgpu/navy_flounder_sdma.bin
firmware:       amdgpu/sienna_cichlid_sdma.bin
firmware:       amdgpu/sdma_6_1_3.bin
firmware:       amdgpu/sdma_6_1_2.bin
firmware:       amdgpu/sdma_6_1_1.bin
firmware:       amdgpu/sdma_6_1_0.bin
firmware:       amdgpu/sdma_6_0_3.bin
firmware:       amdgpu/sdma_6_0_2.bin
firmware:       amdgpu/sdma_6_0_1.bin
firmware:       amdgpu/sdma_6_0_0.bin
firmware:       amdgpu/sdma_7_0_1.bin
firmware:       amdgpu/sdma_7_0_0.bin
firmware:       amdgpu/gc_11_5_3_mes1.bin
firmware:       amdgpu/gc_11_5_3_mes_2.bin
firmware:       amdgpu/gc_11_5_2_mes1.bin
firmware:       amdgpu/gc_11_5_2_mes_2.bin
firmware:       amdgpu/gc_11_5_1_mes1.bin
firmware:       amdgpu/gc_11_5_1_mes_2.bin
firmware:       amdgpu/gc_11_5_0_mes1.bin
firmware:       amdgpu/gc_11_5_0_mes_2.bin
firmware:       amdgpu/gc_11_0_4_mes1.bin
firmware:       amdgpu/gc_11_0_4_mes_2.bin
firmware:       amdgpu/gc_11_0_4_mes.bin
firmware:       amdgpu/gc_11_0_3_mes1.bin
firmware:       amdgpu/gc_11_0_3_mes_2.bin
firmware:       amdgpu/gc_11_0_3_mes.bin
firmware:       amdgpu/gc_11_0_2_mes1.bin
firmware:       amdgpu/gc_11_0_2_mes_2.bin
firmware:       amdgpu/gc_11_0_2_mes.bin
firmware:       amdgpu/gc_11_0_1_mes1.bin
firmware:       amdgpu/gc_11_0_1_mes_2.bin
firmware:       amdgpu/gc_11_0_1_mes.bin
firmware:       amdgpu/gc_11_0_0_mes1.bin
firmware:       amdgpu/gc_11_0_0_mes_2.bin
firmware:       amdgpu/gc_11_0_0_mes.bin
firmware:       amdgpu/gc_12_0_1_uni_mes.bin
firmware:       amdgpu/gc_12_0_1_mes1.bin
firmware:       amdgpu/gc_12_0_1_mes.bin
firmware:       amdgpu/gc_12_0_0_uni_mes.bin
firmware:       amdgpu/gc_12_0_0_mes1.bin
firmware:       amdgpu/gc_12_0_0_mes.bin
firmware:       amdgpu/vega20_uvd.bin
firmware:       amdgpu/vega12_uvd.bin
firmware:       amdgpu/vega10_uvd.bin
firmware:       amdgpu/vegam_uvd.bin
firmware:       amdgpu/polaris12_uvd.bin
firmware:       amdgpu/polaris11_uvd.bin
firmware:       amdgpu/polaris10_uvd.bin
firmware:       amdgpu/stoney_uvd.bin
firmware:       amdgpu/fiji_uvd.bin
firmware:       amdgpu/carrizo_uvd.bin
firmware:       amdgpu/tonga_uvd.bin
firmware:       amdgpu/mullins_uvd.bin
firmware:       amdgpu/hawaii_uvd.bin
firmware:       amdgpu/kaveri_uvd.bin
firmware:       amdgpu/kabini_uvd.bin
firmware:       amdgpu/bonaire_uvd.bin
firmware:       amdgpu/oland_uvd.bin
firmware:       amdgpu/pitcairn_uvd.bin
firmware:       amdgpu/verde_uvd.bin
firmware:       amdgpu/tahiti_uvd.bin
firmware:       amdgpu/vega20_vce.bin
firmware:       amdgpu/vega12_vce.bin
firmware:       amdgpu/vega10_vce.bin
firmware:       amdgpu/vegam_vce.bin
firmware:       amdgpu/polaris12_vce.bin
firmware:       amdgpu/polaris11_vce.bin
firmware:       amdgpu/polaris10_vce.bin
firmware:       amdgpu/stoney_vce.bin
firmware:       amdgpu/fiji_vce.bin
firmware:       amdgpu/carrizo_vce.bin
firmware:       amdgpu/tonga_vce.bin
firmware:       amdgpu/mullins_vce.bin
firmware:       amdgpu/hawaii_vce.bin
firmware:       amdgpu/kaveri_vce.bin
firmware:       amdgpu/kabini_vce.bin
firmware:       amdgpu/bonaire_vce.bin
firmware:       amdgpu/vcn_5_0_1.bin
firmware:       amdgpu/vcn_5_0_0.bin
firmware:       amdgpu/vcn_4_0_6_1.bin
firmware:       amdgpu/vcn_4_0_6.bin
firmware:       amdgpu/vcn_4_0_5.bin
firmware:       amdgpu/vcn_4_0_4.bin
firmware:       amdgpu/vcn_4_0_3.bin
firmware:       amdgpu/vcn_4_0_2.bin
firmware:       amdgpu/vcn_4_0_0.bin
firmware:       amdgpu/vcn_3_1_2.bin
firmware:       amdgpu/yellow_carp_vcn.bin
firmware:       amdgpu/beige_goby_vcn.bin
firmware:       amdgpu/dimgrey_cavefish_vcn.bin
firmware:       amdgpu/vangogh_vcn.bin
firmware:       amdgpu/navy_flounder_vcn.bin
firmware:       amdgpu/sienna_cichlid_vcn.bin
firmware:       amdgpu/navi12_vcn.bin
firmware:       amdgpu/navi14_vcn.bin
firmware:       amdgpu/navi10_vcn.bin
firmware:       amdgpu/aldebaran_vcn.bin
firmware:       amdgpu/green_sardine_vcn.bin
firmware:       amdgpu/renoir_vcn.bin
firmware:       amdgpu/arcturus_vcn.bin
firmware:       amdgpu/raven2_vcn.bin
firmware:       amdgpu/picasso_vcn.bin
firmware:       amdgpu/raven_vcn.bin
firmware:       amdgpu/vpe_6_1_3.bin
firmware:       amdgpu/vpe_6_1_1.bin
firmware:       amdgpu/vpe_6_1_0.bin
firmware:       amdgpu/umsch_mm_4_0_0.bin
firmware:       amdgpu/beige_goby_smc.bin
firmware:       amdgpu/dimgrey_cavefish_smc.bin
firmware:       amdgpu/navy_flounder_smc.bin
firmware:       amdgpu/sienna_cichlid_smc.bin
firmware:       amdgpu/navi12_smc.bin
firmware:       amdgpu/navi14_smc.bin
firmware:       amdgpu/navi10_smc.bin
firmware:       amdgpu/arcturus_smc.bin
firmware:       amdgpu/smu_13_0_10.bin
firmware:       amdgpu/smu_13_0_7.bin
firmware:       amdgpu/smu_13_0_0.bin
firmware:       amdgpu/aldebaran_smc.bin
firmware:       amdgpu/smu_13_0_14.bin
firmware:       amdgpu/smu_13_0_6.bin
firmware:       amdgpu/smu_14_0_3.bin
firmware:       amdgpu/smu_14_0_2.bin
firmware:       amdgpu/vega20_smc.bin
firmware:       amdgpu/vega12_smc.bin
firmware:       amdgpu/vega10_acg_smc.bin
firmware:       amdgpu/vega10_smc.bin
firmware:       amdgpu/vegam_smc.bin
firmware:       amdgpu/polaris12_k_smc.bin
firmware:       amdgpu/polaris12_smc.bin
firmware:       amdgpu/polaris11_k2_smc.bin
firmware:       amdgpu/polaris11_k_smc.bin
firmware:       amdgpu/polaris11_smc_sk.bin
firmware:       amdgpu/polaris11_smc.bin
firmware:       amdgpu/polaris10_k2_smc.bin
firmware:       amdgpu/polaris10_k_smc.bin
firmware:       amdgpu/polaris10_smc_sk.bin
firmware:       amdgpu/polaris10_smc.bin
firmware:       amdgpu/fiji_smc.bin
firmware:       amdgpu/tonga_k_smc.bin
firmware:       amdgpu/tonga_smc.bin
firmware:       amdgpu/topaz_k_smc.bin
firmware:       amdgpu/topaz_smc.bin
firmware:       amdgpu/hawaii_k_smc.bin
firmware:       amdgpu/hawaii_smc.bin
firmware:       amdgpu/bonaire_k_smc.bin
firmware:       amdgpu/bonaire_smc.bin
firmware:       amdgpu/banks_k_2_smc.bin
firmware:       amdgpu/hainan_k_smc.bin
firmware:       amdgpu/hainan_smc.bin
firmware:       amdgpu/oland_k_smc.bin
firmware:       amdgpu/oland_smc.bin
firmware:       amdgpu/verde_k_smc.bin
firmware:       amdgpu/verde_smc.bin
firmware:       amdgpu/pitcairn_k_smc.bin
firmware:       amdgpu/pitcairn_smc.bin
firmware:       amdgpu/tahiti_smc.bin
firmware:       amdgpu/dcn_4_0_1_dmcub.bin
firmware:       amdgpu/dcn_3_6_dmcub.bin
firmware:       amdgpu/dcn_3_5_1_dmcub.bin
firmware:       amdgpu/dcn_3_5_dmcub.bin
firmware:       amdgpu/navi12_dmcu.bin
firmware:       amdgpu/raven_dmcu.bin
firmware:       amdgpu/dcn_3_2_1_dmcub.bin
firmware:       amdgpu/dcn_3_2_0_dmcub.bin
firmware:       amdgpu/dcn_3_1_6_dmcub.bin
firmware:       amdgpu/dcn_3_1_5_dmcub.bin
firmware:       amdgpu/dcn_3_1_4_dmcub.bin
firmware:       amdgpu/yellow_carp_dmcub.bin
firmware:       amdgpu/beige_goby_dmcub.bin
firmware:       amdgpu/dimgrey_cavefish_dmcub.bin
firmware:       amdgpu/vangogh_dmcub.bin
firmware:       amdgpu/green_sardine_dmcub.bin
firmware:       amdgpu/navy_flounder_dmcub.bin
firmware:       amdgpu/sienna_cichlid_dmcub.bin
firmware:       amdgpu/renoir_dmcub.bin
srcversion:     13E3D53034E5EB28310F761
alias:          pci:v00001002d*sv*sd*bc12sc00i00*
alias:          pci:v00001002d*sv*sd*bc03sc80i00*
alias:          pci:v00001002d*sv*sd*bc03sc00i00*
alias:          pci:v00001002d0000743Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00007424sv*sd*bc*sc*i*
alias:          pci:v00001002d00007423sv*sd*bc*sc*i*
alias:          pci:v00001002d00007422sv*sd*bc*sc*i*
alias:          pci:v00001002d00007421sv*sd*bc*sc*i*
alias:          pci:v00001002d00007420sv*sd*bc*sc*i*
alias:          pci:v00001002d0000143Fsv*sd*bc*sc*i*
alias:          pci:v00001002d000013FEsv*sd*bc*sc*i*
alias:          pci:v00001002d00007410sv*sd*bc*sc*i*
alias:          pci:v00001002d0000740Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000740Csv*sd*bc*sc*i*
alias:          pci:v00001002d00007408sv*sd*bc*sc*i*
alias:          pci:v00001002d000073FFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073EFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073EDsv*sd*bc*sc*i*
alias:          pci:v00001002d000073ECsv*sd*bc*sc*i*
alias:          pci:v00001002d000073EBsv*sd*bc*sc*i*
alias:          pci:v00001002d000073EAsv*sd*bc*sc*i*
alias:          pci:v00001002d000073E9sv*sd*bc*sc*i*
alias:          pci:v00001002d000073E8sv*sd*bc*sc*i*
alias:          pci:v00001002d000073E3sv*sd*bc*sc*i*
alias:          pci:v00001002d000073E2sv*sd*bc*sc*i*
alias:          pci:v00001002d000073E1sv*sd*bc*sc*i*
alias:          pci:v00001002d000073E0sv*sd*bc*sc*i*
alias:          pci:v00001002d000073DFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073DEsv*sd*bc*sc*i*
alias:          pci:v00001002d000073DDsv*sd*bc*sc*i*
alias:          pci:v00001002d000073DCsv*sd*bc*sc*i*
alias:          pci:v00001002d000073DBsv*sd*bc*sc*i*
alias:          pci:v00001002d000073DAsv*sd*bc*sc*i*
alias:          pci:v00001002d000073C3sv*sd*bc*sc*i*
alias:          pci:v00001002d000073C1sv*sd*bc*sc*i*
alias:          pci:v00001002d000073C0sv*sd*bc*sc*i*
alias:          pci:v00001002d00001681sv*sd*bc*sc*i*
alias:          pci:v00001002d0000164Dsv*sd*bc*sc*i*
alias:          pci:v00001002d000073BFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000073AEsv*sd*bc*sc*i*
alias:          pci:v00001002d000073ADsv*sd*bc*sc*i*
alias:          pci:v00001002d000073ACsv*sd*bc*sc*i*
alias:          pci:v00001002d000073ABsv*sd*bc*sc*i*
alias:          pci:v00001002d000073A9sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A8sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A5sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000073A0sv*sd*bc*sc*i*
alias:          pci:v00001002d00007362sv*sd*bc*sc*i*
alias:          pci:v00001002d00007360sv*sd*bc*sc*i*
alias:          pci:v00001002d0000164Csv*sd*bc*sc*i*
alias:          pci:v00001002d00001638sv*sd*bc*sc*i*
alias:          pci:v00001002d00001636sv*sd*bc*sc*i*
alias:          pci:v00001002d000015E7sv*sd*bc*sc*i*
alias:          pci:v00001002d0000734Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00007347sv*sd*bc*sc*i*
alias:          pci:v00001002d00007341sv*sd*bc*sc*i*
alias:          pci:v00001002d00007340sv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000731Asv*sd*bc*sc*i*
alias:          pci:v00001002d00007319sv*sd*bc*sc*i*
alias:          pci:v00001002d00007318sv*sd*bc*sc*i*
alias:          pci:v00001002d00007312sv*sd*bc*sc*i*
alias:          pci:v00001002d00007310sv*sd*bc*sc*i*
alias:          pci:v00001002d00007390sv*sd*bc*sc*i*
alias:          pci:v00001002d0000738Esv*sd*bc*sc*i*
alias:          pci:v00001002d00007388sv*sd*bc*sc*i*
alias:          pci:v00001002d0000738Csv*sd*bc*sc*i*
alias:          pci:v00001002d000015D8sv*sd*bc*sc*i*
alias:          pci:v00001002d000015DDsv*sd*bc*sc*i*
alias:          pci:v00001002d000066AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000066A7sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A4sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000066A0sv*sd*bc*sc*i*
alias:          pci:v00001002d000069AFsv*sd*bc*sc*i*
alias:          pci:v00001002d000069A3sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000069A0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000687Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000686Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006869sv*sd*bc*sc*i*
alias:          pci:v00001002d00006868sv*sd*bc*sc*i*
alias:          pci:v00001002d00006867sv*sd*bc*sc*i*
alias:          pci:v00001002d00006864sv*sd*bc*sc*i*
alias:          pci:v00001002d00006863sv*sd*bc*sc*i*
alias:          pci:v00001002d00006862sv*sd*bc*sc*i*
alias:          pci:v00001002d00006861sv*sd*bc*sc*i*
alias:          pci:v00001002d00006860sv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000694Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000699Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006997sv*sd*bc*sc*i*
alias:          pci:v00001002d00006995sv*sd*bc*sc*i*
alias:          pci:v00001002d00006987sv*sd*bc*sc*i*
alias:          pci:v00001002d00006986sv*sd*bc*sc*i*
alias:          pci:v00001002d00006985sv*sd*bc*sc*i*
alias:          pci:v00001002d00006981sv*sd*bc*sc*i*
alias:          pci:v00001002d00006980sv*sd*bc*sc*i*
alias:          pci:v00001002d00006FDFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CCsv*sd*bc*sc*i*
alias:          pci:v00001002d000067CAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067C9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067DFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067D0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C7sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C4sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C2sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067C0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E7sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067FFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067EFsv*sd*bc*sc*i*
alias:          pci:v00001002d000067EBsv*sd*bc*sc*i*
alias:          pci:v00001002d000067E8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E3sv*sd*bc*sc*i*
alias:          pci:v00001002d000067E0sv*sd*bc*sc*i*
alias:          pci:v00001002d000098E4sv*sd*bc*sc*i*
alias:          pci:v00001002d00009877sv*sd*bc*sc*i*
alias:          pci:v00001002d00009876sv*sd*bc*sc*i*
alias:          pci:v00001002d00009875sv*sd*bc*sc*i*
alias:          pci:v00001002d00009874sv*sd*bc*sc*i*
alias:          pci:v00001002d00009870sv*sd*bc*sc*i*
alias:          pci:v00001002d0000730Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00007300sv*sd*bc*sc*i*
alias:          pci:v00001002d00006939sv*sd*bc*sc*i*
alias:          pci:v00001002d00006938sv*sd*bc*sc*i*
alias:          pci:v00001002d00006930sv*sd*bc*sc*i*
alias:          pci:v00001002d0000692Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000692Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00006929sv*sd*bc*sc*i*
alias:          pci:v00001002d00006928sv*sd*bc*sc*i*
alias:          pci:v00001002d00006921sv*sd*bc*sc*i*
alias:          pci:v00001002d00006920sv*sd*bc*sc*i*
alias:          pci:v00001002d00006907sv*sd*bc*sc*i*
alias:          pci:v00001002d00006903sv*sd*bc*sc*i*
alias:          pci:v00001002d00006902sv*sd*bc*sc*i*
alias:          pci:v00001002d00006901sv*sd*bc*sc*i*
alias:          pci:v00001002d00006900sv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000985Asv*sd*bc*sc*i*
alias:          pci:v00001002d00009859sv*sd*bc*sc*i*
alias:          pci:v00001002d00009858sv*sd*bc*sc*i*
alias:          pci:v00001002d00009857sv*sd*bc*sc*i*
alias:          pci:v00001002d00009856sv*sd*bc*sc*i*
alias:          pci:v00001002d00009855sv*sd*bc*sc*i*
alias:          pci:v00001002d00009854sv*sd*bc*sc*i*
alias:          pci:v00001002d00009853sv*sd*bc*sc*i*
alias:          pci:v00001002d00009852sv*sd*bc*sc*i*
alias:          pci:v00001002d00009851sv*sd*bc*sc*i*
alias:          pci:v00001002d00009850sv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000983Asv*sd*bc*sc*i*
alias:          pci:v00001002d00009839sv*sd*bc*sc*i*
alias:          pci:v00001002d00009838sv*sd*bc*sc*i*
alias:          pci:v00001002d00009837sv*sd*bc*sc*i*
alias:          pci:v00001002d00009836sv*sd*bc*sc*i*
alias:          pci:v00001002d00009835sv*sd*bc*sc*i*
alias:          pci:v00001002d00009834sv*sd*bc*sc*i*
alias:          pci:v00001002d00009833sv*sd*bc*sc*i*
alias:          pci:v00001002d00009832sv*sd*bc*sc*i*
alias:          pci:v00001002d00009831sv*sd*bc*sc*i*
alias:          pci:v00001002d00009830sv*sd*bc*sc*i*
alias:          pci:v00001002d000067BEsv*sd*bc*sc*i*
alias:          pci:v00001002d000067BAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067B9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067B0sv*sd*bc*sc*i*
alias:          pci:v00001002d000067AAsv*sd*bc*sc*i*
alias:          pci:v00001002d000067A9sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A8sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A2sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A1sv*sd*bc*sc*i*
alias:          pci:v00001002d000067A0sv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000665Csv*sd*bc*sc*i*
alias:          pci:v00001002d00006658sv*sd*bc*sc*i*
alias:          pci:v00001002d00006651sv*sd*bc*sc*i*
alias:          pci:v00001002d00006650sv*sd*bc*sc*i*
alias:          pci:v00001002d00006649sv*sd*bc*sc*i*
alias:          pci:v00001002d00006647sv*sd*bc*sc*i*
alias:          pci:v00001002d00006646sv*sd*bc*sc*i*
alias:          pci:v00001002d00006641sv*sd*bc*sc*i*
alias:          pci:v00001002d00006640sv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000131Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00001318sv*sd*bc*sc*i*
alias:          pci:v00001002d00001317sv*sd*bc*sc*i*
alias:          pci:v00001002d00001316sv*sd*bc*sc*i*
alias:          pci:v00001002d00001315sv*sd*bc*sc*i*
alias:          pci:v00001002d00001313sv*sd*bc*sc*i*
alias:          pci:v00001002d00001312sv*sd*bc*sc*i*
alias:          pci:v00001002d00001311sv*sd*bc*sc*i*
alias:          pci:v00001002d00001310sv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000130Asv*sd*bc*sc*i*
alias:          pci:v00001002d00001309sv*sd*bc*sc*i*
alias:          pci:v00001002d00001307sv*sd*bc*sc*i*
alias:          pci:v00001002d00001306sv*sd*bc*sc*i*
alias:          pci:v00001002d00001305sv*sd*bc*sc*i*
alias:          pci:v00001002d00001304sv*sd*bc*sc*i*
alias:          pci:v00001002d0000666Fsv*sd*bc*sc*i*
alias:          pci:v00001002d00006667sv*sd*bc*sc*i*
alias:          pci:v00001002d00006665sv*sd*bc*sc*i*
alias:          pci:v00001002d00006664sv*sd*bc*sc*i*
alias:          pci:v00001002d00006663sv*sd*bc*sc*i*
alias:          pci:v00001002d00006660sv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000683Bsv*sd*bc*sc*i*
alias:          pci:v00001002d00006839sv*sd*bc*sc*i*
alias:          pci:v00001002d00006838sv*sd*bc*sc*i*
alias:          pci:v00001002d00006837sv*sd*bc*sc*i*
alias:          pci:v00001002d00006835sv*sd*bc*sc*i*
alias:          pci:v00001002d00006831sv*sd*bc*sc*i*
alias:          pci:v00001002d00006830sv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Dsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Csv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000682Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006829sv*sd*bc*sc*i*
alias:          pci:v00001002d00006828sv*sd*bc*sc*i*
alias:          pci:v00001002d00006827sv*sd*bc*sc*i*
alias:          pci:v00001002d00006826sv*sd*bc*sc*i*
alias:          pci:v00001002d00006825sv*sd*bc*sc*i*
alias:          pci:v00001002d00006824sv*sd*bc*sc*i*
alias:          pci:v00001002d00006823sv*sd*bc*sc*i*
alias:          pci:v00001002d00006822sv*sd*bc*sc*i*
alias:          pci:v00001002d00006821sv*sd*bc*sc*i*
alias:          pci:v00001002d00006820sv*sd*bc*sc*i*
alias:          pci:v00001002d00006631sv*sd*bc*sc*i*
alias:          pci:v00001002d00006623sv*sd*bc*sc*i*
alias:          pci:v00001002d00006621sv*sd*bc*sc*i*
alias:          pci:v00001002d00006620sv*sd*bc*sc*i*
alias:          pci:v00001002d00006617sv*sd*bc*sc*i*
alias:          pci:v00001002d00006613sv*sd*bc*sc*i*
alias:          pci:v00001002d00006611sv*sd*bc*sc*i*
alias:          pci:v00001002d00006610sv*sd*bc*sc*i*
alias:          pci:v00001002d00006608sv*sd*bc*sc*i*
alias:          pci:v00001002d00006607sv*sd*bc*sc*i*
alias:          pci:v00001002d00006606sv*sd*bc*sc*i*
alias:          pci:v00001002d00006605sv*sd*bc*sc*i*
alias:          pci:v00001002d00006604sv*sd*bc*sc*i*
alias:          pci:v00001002d00006603sv*sd*bc*sc*i*
alias:          pci:v00001002d00006602sv*sd*bc*sc*i*
alias:          pci:v00001002d00006601sv*sd*bc*sc*i*
alias:          pci:v00001002d00006600sv*sd*bc*sc*i*
alias:          pci:v00001002d00006819sv*sd*bc*sc*i*
alias:          pci:v00001002d00006818sv*sd*bc*sc*i*
alias:          pci:v00001002d00006817sv*sd*bc*sc*i*
alias:          pci:v00001002d00006816sv*sd*bc*sc*i*
alias:          pci:v00001002d00006811sv*sd*bc*sc*i*
alias:          pci:v00001002d00006810sv*sd*bc*sc*i*
alias:          pci:v00001002d00006809sv*sd*bc*sc*i*
alias:          pci:v00001002d00006808sv*sd*bc*sc*i*
alias:          pci:v00001002d00006806sv*sd*bc*sc*i*
alias:          pci:v00001002d00006802sv*sd*bc*sc*i*
alias:          pci:v00001002d00006801sv*sd*bc*sc*i*
alias:          pci:v00001002d00006800sv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Fsv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Esv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Bsv*sd*bc*sc*i*
alias:          pci:v00001002d0000679Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006799sv*sd*bc*sc*i*
alias:          pci:v00001002d00006798sv*sd*bc*sc*i*
alias:          pci:v00001002d00006792sv*sd*bc*sc*i*
alias:          pci:v00001002d00006791sv*sd*bc*sc*i*
alias:          pci:v00001002d00006790sv*sd*bc*sc*i*
alias:          pci:v00001002d0000678Asv*sd*bc*sc*i*
alias:          pci:v00001002d00006788sv*sd*bc*sc*i*
alias:          pci:v00001002d00006784sv*sd*bc*sc*i*
alias:          pci:v00001002d00006780sv*sd*bc*sc*i*
depends:        gpu-sched,ttm,drm_display_helper,drm_buddy,amdxcp,cec,drm_suballoc_helper,drm_exec,video,drm_panel_backlight_quirks,drm_ttm_helper,i2c-algo-bit
intree:         Y
name:           amdgpu
retpoline:      Y
vermagic:       6.15.4-arch2-1 SMP preempt mod_unload
sig_id:         PKCS#7
signer:         Build time autogenerated kernel key
sig_key:        3D:E9:4F:8C:44:0E:C1:0E:E4:C4:7C:BA:FF:95:12:C4:DC:F4:AE:46
sig_hashalgo:   sha512
signature:      30:65:02:31:00:F4:33:EC:11:19:CF:0D:43:38:31:DC:0D:BC:C0:B8:
		E4:F1:A6:EC:AF:87:76:BD:0F:72:A9:08:16:B8:38:02:2B:13:B4:AD:
		E2:4E:82:36:00:F4:C6:0B:19:94:48:88:ED:02:30:08:ED:A7:5B:61:
		AE:75:07:81:89:D4:0F:B1:EA:BC:CB:74:ED:54:14:4A:77:0C:40:54:
		4B:70:D4:9D:AD:7B:C4:9B:20:CC:83:EE:64:31:67:6A:21:84:86:4F:
		DC:38:28
parm:           vramlimit:Restrict VRAM for testing, in megabytes (int)
parm:           vis_vramlimit:Restrict visible VRAM for testing, in megabytes (int)
parm:           gartsize:Size of kernel GART to setup in megabytes (32, 64, etc., -1=auto) (uint)
parm:           gttsize:Size of the GTT userspace domain in megabytes (-1 = auto) (int)
parm:           moverate:Maximum buffer migration rate in MB/s. (32, 64, etc., -1=auto, 0=1=disabled) (int)
parm:           audio:Audio enable (-1 = auto, 0 = disable, 1 = enable) (int)
parm:           disp_priority:Display Priority (0 = auto, 1 = normal, 2 = high) (int)
parm:           hw_i2c:hw i2c engine enable (0 = disable) (int)
parm:           pcie_gen2:PCIE Gen2 mode (-1 = auto, 0 = disable, 1 = enable) (int)
parm:           msi:MSI support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           svm_default_granularity:SVM's default granularity in log(2^Pages), default 9 = 2^9 = 2 MiB (uint)
parm:           lockup_timeout:GPU lockup timeout in ms (default: for bare metal 10000 for non-compute jobs and 60000 for compute jobs; for passthrough or sriov, 10000 for all jobs. 0: keep default value. negative: infinity timeout), format: for bare metal [Non-Compute] or [GFX,Compute,SDMA,Video]; for passthrough or sriov [all jobs] or [GFX,Compute,SDMA,Video]. (string)
parm:           dpm:DPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           fw_load_type:firmware loading type (3 = rlc backdoor autoload if supported, 2 = smu load if supported, 1 = psp load, 0 = force direct if supported, -1 = auto) (int)
parm:           aspm:ASPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           runpm:PX runtime pm (2 = force enable with BAMACO, 1 = force enable with BACO, 0 = disable, -1 = auto, -2 = auto with displays) (int)
parm:           ip_block_mask:IP Block Mask (all blocks enabled (default)) (uint)
parm:           bapm:BAPM support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           deep_color:Deep Color support (1 = enable, 0 = disable (default)) (int)
parm:           vm_size:VM address space size in gigabytes (default 64GB) (int)
parm:           vm_fragment_size:VM fragment size in bits (4, 5, etc. 4 = 64K (default), Max 9 = 2M) (int)
parm:           vm_block_size:VM page table size in bits (default depending on vm_size) (int)
parm:           vm_fault_stop:Stop on VM fault (0 = never (default), 1 = print first, 2 = always) (int)
parm:           vm_update_mode:VM update using CPU (0 = never (default except for large BAR(LB)), 1 = Graphics only, 2 = Compute only (default for LB), 3 = Both (int)
parm:           exp_hw_support:experimental hw support (1 = enable, 0 = disable (default)) (int)
parm:           dc:Display Core driver (1 = enable, 0 = disable, -1 = auto (default)) (int)
parm:           sched_jobs:the max number of jobs supported in the sw queue (default 32) (int)
parm:           sched_hw_submission:the max number of HW submissions (default 2) (int)
parm:           ppfeaturemask:all power features enabled (default)) (hexint)
parm:           forcelongtraining:force memory long training (uint)
parm:           pcie_gen_cap:PCIE Gen Caps (0: autodetect (default)) (uint)
parm:           pcie_lane_cap:PCIE Lane Caps (0: autodetect (default)) (uint)
parm:           cg_mask:Clockgating flags mask (0 = disable clock gating) (ullong)
parm:           pg_mask:Powergating flags mask (0 = disable power gating) (uint)
parm:           sdma_phase_quantum:SDMA context switch phase quantum (x 1K GPU clock cycles, 0 = no change (default 32)) (uint)
parm:           disable_cu:Disable CUs (se.sh.cu,...) (charp)
parm:           virtual_display:Enable virtual display feature (the virtual_display will be set like xxxx:xx:xx.x,x;xxxx:xx:xx.x,x) (charp)
parm:           lbpw:Load Balancing Per Watt (LBPW) support (1 = enable, 0 = disable, -1 = auto) (int)
parm:           compute_multipipe:Force compute queues to be spread across pipes (1 = enable, 0 = disable, -1 = auto) (int)
parm:           gpu_recovery:Enable GPU recovery mechanism, (1 = enable, 0 = disable, -1 = auto) (int)
parm:           emu_mode:Emulation mode, (1 = enable, 0 = disable) (int)
parm:           ras_enable:Enable RAS features on the GPU (0 = disable, 1 = enable, -1 = auto (default)) (int)
parm:           ras_mask:Mask of RAS features to enable (default 0xffffffff), only valid when ras_enable == 1 (uint)
parm:           timeout_fatal_disable:disable watchdog timeout fatal error (false = default) (bool)
parm:           timeout_period:watchdog timeout period (0 = timeout disabled, 1 ~ 0x23 = timeout maxcycles = (1 << period) (uint)
parm:           si_support:SI support (1 = enabled, 0 = disabled (default)) (int)
parm:           cik_support:CIK support (1 = enabled, 0 = disabled (default)) (int)
parm:           smu_memory_pool_size:reserve gtt for smu debug usage, 0 = disable,0x1 = 256Mbyte, 0x2 = 512Mbyte, 0x4 = 1 Gbyte, 0x8 = 2GByte (uint)
parm:           async_gfx_ring:Asynchronous GFX rings that could be configured with either different priorities (HP3D ring and LP3D ring), or equal priorities (0 = disabled, 1 = enabled (default)) (int)
parm:           mcbp:Enable Mid-command buffer preemption (0 = disabled, 1 = enabled), -1 = auto (default) (int)
parm:           discovery:Allow driver to discover hardware IPs from IP Discovery table at the top of VRAM (int)
parm:           mes:Enable Micro Engine Scheduler (0 = disabled (default), 1 = enabled) (int)
parm:           mes_log_enable:Enable Micro Engine Scheduler log (0 = disabled (default), 1 = enabled) (int)
parm:           mes_kiq:Enable Micro Engine Scheduler KIQ (0 = disabled (default), 1 = enabled) (int)
parm:           uni_mes:Enable Unified Micro Engine Scheduler (0 = disabled, 1 = enabled(default) (int)
parm:           noretry:Disable retry faults (0 = retry enabled, 1 = retry disabled, -1 auto (default)) (int)
parm:           force_asic_type:A non negative value used to specify the asic type for all supported GPUs (int)
parm:           use_xgmi_p2p:Enable XGMI P2P interface (0 = disable; 1 = enable (default)) (int)
parm:           sched_policy:Scheduling policy (0 = HWS (Default), 1 = HWS without over-subscription, 2 = Non-HWS (Used for debugging only) (int)
parm:           hws_max_conc_proc:Max # processes HWS can execute concurrently when sched_policy=0 (0 = no concurrency, #VMIDs for KFD = Maximum(default)) (int)
parm:           cwsr_enable:CWSR enable (0 = Off, 1 = On (Default)) (int)
parm:           max_num_of_queues_per_device:Maximum number of supported queues per device (1 = Minimum, 4096 = default) (int)
parm:           send_sigterm:Send sigterm to HSA process on unhandled exception (0 = disable, 1 = enable) (int)
parm:           halt_if_hws_hang:Halt if HWS hang is detected (0 = off (default), 1 = on) (int)
parm:           hws_gws_support:Assume MEC2 FW supports GWS barriers (false = rely on FW version check (Default), true = force supported) (bool)
parm:           queue_preemption_timeout_ms:queue preemption timeout in ms (1 = Minimum, 9000 = default) (int)
parm:           debug_evictions:enable eviction debug messages (false = default) (bool)
parm:           no_system_mem_limit:disable system memory limit (false = default) (bool)
parm:           no_queue_eviction_on_vm_fault:No queue eviction on VM fault (0 = queue eviction, 1 = no queue eviction) (int)
parm:           mtype_local:MTYPE for local memory (0 = MTYPE_RW (default), 1 = MTYPE_NC, 2 = MTYPE_CC) (int)
parm:           dcfeaturemask:all stable DC features enabled (default)) (uint)
parm:           dcdebugmask:all debug options disabled (default)) (uint)
parm:           visualconfirm:Visual confirm (0 = off (default), 1 = MPO, 5 = PSR) (uint)
parm:           abmlevel:ABM level (0 = off, 1-4 = backlight reduction level, -1 auto (default)) (int)
parm:           backlight:Backlight control (0 = pwm, 1 = aux, -1 auto (default)) (bint)
parm:           damageclips:Damage clips support (0 = disable, 1 = enable, -1 auto (default)) (int)
parm:           tmz:Enable TMZ feature (-1 = auto (default), 0 = off, 1 = on) (int)
parm:           freesync_video:Enable freesync modesetting optimization feature (0 = off (default), 1 = on) (uint)
parm:           reset_method:GPU reset method (-1 = auto (default), 0 = legacy, 1 = mode0, 2 = mode1, 3 = mode2, 4 = baco/bamaco) (int)
parm:           bad_page_threshold:Bad page threshold(-1 = ignore threshold (default value), 0 = disable bad page retirement, -2 = threshold determined by a formula, 0 < threshold < max records, user-defined threshold) (int)
parm:           num_kcq:number of kernel compute queue user want to setup (8 if set to greater than 8 or less than 0, only affect gfx 8+) (int)
parm:           vcnfw_log:Enable vcnfw log(0 = disable (default value), 1 = enable) (int)
parm:           sg_display:S/G Display (-1 = auto (default), 0 = disable) (int)
parm:           umsch_mm:Enable Multi Media User Mode Scheduler (0 = disabled (default), 1 = enabled) (int)
parm:           umsch_mm_fwlog:Enable umschfw log(0 = disable (default value), 1 = enable) (int)
parm:           smu_pptable_id:specify pptable id to be used (-1 = auto(default) value, 0 = use pptable from vbios, > 0 = soft pptable id) (int)
parm:           user_partt_mode:specify partition mode to be used (-2 = AMDGPU_AUTO_COMPUTE_PARTITION_MODE(default value) 						0 = AMDGPU_SPX_PARTITION_MODE, 						1 = AMDGPU_DPX_PARTITION_MODE, 						2 = AMDGPU_TPX_PARTITION_MODE, 			3 = AMDGPU_QPX_PARTITION_MODE, 						4 = AMDGPU_CPX_PARTITION_MODE) (uint)
parm:           enforce_isolation:enforce process isolation between graphics and compute . enforce_isolation = on (bool)
parm:           modeset:Override nomodeset (1 = enable, -1 = auto) (int)
parm:           seamless:Seamless boot (-1 = auto (default), 0 = disable, 1 = enable) (int)
parm:           debug_mask:debug options for amdgpu, disabled by default (uint)
parm:           agp:AGP (-1 = auto (default), 0 = disable, 1 = enable) (int)
parm:           wbrf:Enable Wifi RFI interference mitigation (0 = disabled, 1 = enabled, -1 = auto(default) (int)
```

amd-smi looks pretty much the same as yours

```
amd-smi
usage: amd-smi [-h]  ...

AMD System Management Interface | Version: 25.4.2+unknown | ROCm version: 6.4.1 |
Platform: Linux Baremetal
```

It's starting to look like a packaging bug. Do you have any idea who is supposed to call that `rocprofiler_set_api_table` procedure? Can you get the callstack from a debugger or something like that?

### huanrwan-amd · 2025-07-10

> It's starting to look like a packaging bug. Do you have any idea who is supposed to call that rocprofiler_set_api_table procedure? Can you get the callstack from a debugger or something like that?

OK, I notice you are using Arch Linux, while I am with Ubuntu. You could be right. It can be a packaging issue. rocprofiler_set_api_table() is for api registrations and called by runtimes, such as hip, hsa, etc. Here shows the stack from hsa side: 
```
#0  rocprofiler_set_api_table (name=0x7fffe6f58e5d "hsa", lib_version=71901, lib_instance=0, tables=0x7fffffffb7b0, 
    num_tables=1)
    at /home/rocm22/code/tool/github/git-hub-rocprofiler-sdk/source/lib/rocprofiler-sdk/registration.cpp:782
#1  0x00007ffff18bf769 in rocprofiler_register_library_api_table () from /opt/rocm-6.4.1/lib/librocprofiler-register.so.0
#2  0x00007fffe6e9c5e8 in ?? () from /opt/rocm-6.4.1/lib/libhsa-runtime64.so.1
#3  0x00007fffe6e9e058 in ?? () from /opt/rocm-6.4.1/lib/libhsa-runtime64.so.1
#4  0x00007fffe6e9e24c in ?? () from /opt/rocm-6.4.1/lib/libhsa-runtime64.so.1
#5  0x00007fffe6e677ee in ?? () from /opt/rocm-6.4.1/lib/libhsa-runtime64.so.1
#6  0x00007ffff1d82155 in ?? () from /opt/rocm-6.4.1/lib/libamdhip64.so.6
#7  0x00007ffff1d378f5 in ?? () from /opt/rocm-6.4.1/lib/libamdhip64.so.6
#8  0x00007ffff1d71476 in ?? () from /opt/rocm-6.4.1/lib/libamdhip64.so.6
#9  0x00007ffff1a4f216 in ?? () from /opt/rocm-6.4.1/lib/libamdhip64.so.6
#10 0x00007ffff1299ee8 in __pthread_once_slow (once_control=0x7ffff34fee58, init_routine=0x7ffff16dad50 <__once_proxy>)
    at ./nptl/pthread_once.c:116
#11 0x00007ffff1a75096 in ?? () from /opt/rocm-6.4.1/lib/libamdhip64.so.6
#12 0x00007ffff6e38341 in rocprofiler::hip::hip_api_impl<1ul, 102ul>::exec<hipError_t (*&)(int*), int*> (
    _func=@0x7ffff7468b78: 0x7ffff1a74f50)
    at /home/rocm22/code/tool/github/git-hub-rocprofiler-sdk/source/lib/rocprofiler-sdk/hip/hip.cpp:169
#13 0x00007ffff6e38894 in rocprofiler::hip::hip_api_impl<1ul, 102ul>::functor<hipError_t, int*> ()
    at /home/rocm22/code/tool/github/git-hub-rocprofiler-sdk/source/lib/rocprofiler-sdk/hip/hip.cpp:262
#14 0x00007ffff445003d in _rocblas_handle::_rocblas_handle() () from /opt/rocm-6.4.1/lib/librocblas.so.4
#15 0x00007ffff44528b4 in rocblas_create_handle () from /opt/rocm-6.4.1/lib/librocblas.so.4
#16 0x0000000000203c93 in Kernel0ROCBLAS::init() ()
#17 0x0000000000206073 in main ()

```

### DelusionalLogic · 2025-07-11

I think I got something.

My hypothesis is that the arch package [hsa-rocr](https://gitlab.archlinux.org/archlinux/packaging/packages/hsa-rocr/-/tree/main?ref_type=heads), which contains `libhsa-runtime64.so` on arch, is built without `rocprofiler-register` (packaged separately on arch) installed, and therefore doesn't include the hooks that rocprofiler expects to find.

Running `ldd` indeed shows that `libhsa-runtime64.so` does not load `rocprofiler-register`

```
$ ldd /opt/rocm/lib/libhsa-runtime64.so
	linux-vdso.so.1 (0x00007f6194f7b000)
	libelf.so.1 => /usr/lib/libelf.so.1 (0x00007f6194b92000)
	libdrm.so.2 => /usr/lib/libdrm.so.2 (0x00007f6194f5c000)
	libdrm_amdgpu.so.1 => /usr/lib/libdrm_amdgpu.so.1 (0x00007f6194b85000)
	libnuma.so.1 => /usr/lib/libnuma.so.1 (0x00007f6194b77000)
	libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x00007f6194800000)
	libm.so.6 => /usr/lib/libm.so.6 (0x00007f6194708000)
	libc.so.6 => /usr/lib/libc.so.6 (0x00007f6194518000)
	/usr/lib64/ld-linux-x86-64.so.2 (0x00007f6194f7d000)
	libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f6194b48000)
	libz.so.1 => /usr/lib/libz.so.1 (0x00007f6194b2f000)
	libzstd.so.1 => /usr/lib/libzstd.so.1 (0x00007f6194433000)
```

If I install the `rocprofiler-register` package on my own machine and rebuild `hsa-rocr` i get a version that does load this library.

```
$ git clone git@gitlab.archlinux.org:archlinux/packaging/packages/hsa-rocr.git
$ cd hsa-rocr
$ makepkg
$ ldd pkg/hsa-rocr/opt/rocm/lib/libhsa-runtime64.so
	linux-vdso.so.1 (0x00007f9b0b29e000)
	libelf.so.1 => /usr/lib/libelf.so.1 (0x00007f9b0b228000)
	librocprofiler-register.so.0 => /opt/rocm/lib/librocprofiler-register.so.0 (0x00007f9b0b1fc000)
	libdrm.so.2 => /usr/lib/libdrm.so.2 (0x00007f9b0b1e5000)
	libdrm_amdgpu.so.1 => /usr/lib/libdrm_amdgpu.so.1 (0x00007f9b0b1d8000)
	libnuma.so.1 => /usr/lib/libnuma.so.1 (0x00007f9b0b1ca000)
	libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x00007f9b0aa00000)
	libm.so.6 => /usr/lib/libm.so.6 (0x00007f9b0ad08000)
	libc.so.6 => /usr/lib/libc.so.6 (0x00007f9b0a810000)
	/usr/lib64/ld-linux-x86-64.so.2 (0x00007f9b0b2a0000)
	libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f9b0acdb000)
	libz.so.1 => /usr/lib/libz.so.1 (0x00007f9b0b1af000)
	libzstd.so.1 => /usr/lib/libzstd.so.1 (0x00007f9b0a72b000)
	libfmt.so.11 => /usr/lib/libfmt.so.11 (0x00007f9b0acb9000)
	libglog.so.2 => /usr/lib/libglog.so.2 (0x00007f9b0a6d6000)
	libgflags.so.2.2 => /usr/lib/libgflags.so.2.2 (0x00007f9b0a6a8000)
```

Installing that package seems to allow rocprofiler to generate an hsa trace

```
$ rocprofiler-sdk/build/bin/rocprofv3 --output-format csv --log-level info  --hsa-trace -- ./sgemm
$ tree delusionalStation
delusionalStation
├── 21439_agent_info.csv
└── 21439_hsa_api_trace.csv
```

This all seems a little messy. rocprofiler-sdk basically requires that rocprofiler-register was installed when the rocm runtime libraries were built. However, it does seem to work as designed. I'll talk to the arch maintainer to hear if he'd be willing to include rocprofiler-register as a dependency of the runtime packages.

### huanrwan-amd · 2025-07-11

@DelusionalLogic Yes, you are right. rocprofiler-sdk depends on rocprofiler-register for API registration and runtimes need this library, we assume this library is automatically loaded. Same as you had on your machine and in the trace posted above:
```
ldd /opt/rocm/lib/libhsa-runtime64.so
.....
        librocprofiler-register.so.0 => /opt/rocm/lib/librocprofiler-register.so.0 (0x000071a9cb57d000)
.....
```
Let us know the update on Arch Linux side. Thank you.

### DelusionalLogic · 2025-07-11

I think there's a feature request here too. It would be nice if the profiler warned you if you ask for a trace type it can't find a runtime providing. In this case that would mean it could detect that nobody called `rocprofiler_set_api_table("hsa", ...)` and warn the user trying to capture with `--hsa-trace` that they might need to check their runtime libraries.

I'll keep you updated on the outcome of the discussion with the arch packager :)

### tpkessler · 2025-07-13

Hi all! Arch package maintainer for the ROCm stack here. The issue is fixed for Arch Linux now.

### DelusionalLogic · 2025-07-13

Hey! Thanks @tpkessler. Did you see the message I sent on the mailing list or did you just stumble on this?

I'll test it out tomorrow to check that it resolves my problem so that we can close this issue.

### DelusionalLogic · 2025-07-14

I just tested it out and now I'm getting some HSA trace output with the mainline arch packages, so that's very good :)

@tpkessler I noticed that your commit message includes a link to the mailing list, that question was a little pointless had I done my due diligence. I think ROCm includes more packages that also feature optional `rocprofiler-register` integration. From just searching GitHub[1] it looks like rccl[2], clr[3] [4], rocDecode[5], and rocJPEG[6]

All of the packages that build these projects (I've linked the ones I could find in the gitlab) would have to depend on rocprofiler-register to get the experience upstream intended.

[1]: https://github.com/search?q=org%3Arocm+rocprofiler-register.h&type=code
[2]: https://gitlab.archlinux.org/archlinux/packaging/packages/rccl
[3]: https://gitlab.archlinux.org/archlinux/packaging/packages/rocm-opencl-runtime
[4]: https://gitlab.archlinux.org/archlinux/packaging/packages/hip-runtime
[5]: https://gitlab.archlinux.org/archlinux/packaging/packages/rocdecode
[6]: https://gitlab.archlinux.org/archlinux/packaging/packages/rocjpeg

### ppanchad-amd · 2025-07-18

@DelusionalLogic Can we go ahead and close this ticket now? Thanks!

### DelusionalLogic · 2025-07-22

I would appreciate a link if you have some documentation about which rocm subprojects require being built with rocprofiler-register installed. If you don't have that at hand I understand, that's probably what "TheRoc" is trying to solve.

Other than that, I don't think there's anything else you need to do. I'm ok with you closing it :)

Thanks for the help :)

### huanrwan-amd · 2025-07-23

Hi @DelusionalLogic ,  [(https://github.com/ROCm/rocprofiler-register)](url) is not customer facing. You may search through the repo for the dependencies. 
We will close the issue for now. 
