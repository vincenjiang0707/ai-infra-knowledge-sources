# [Issue #73] [Issue]: --list-avail crashes

source: https://github.com/ROCm/rocprofiler-sdk/issues/73
state: closed | updated: 2025-07-08T18:26:39Z
labels: Under Investigation

## 正文

### Problem Description

I was trying to do HSA tracing (to profile an OpenCL application going into production on a cluster to be), but neither rocprofv1 or v2 could read any of the counters on my 9070 XT. (All counter values are 0, always. Derived and basic both.) After that I tried rocprofilerv3 which can't even list the available counters, because it crashes. Most likely due to having an unsupported IGP in the system. The magic [env vars](https://rocm.docs.amd.com/projects/HIP/en/docs-develop/reference/env_variables.html#gpu-isolation-variables) to make devices vanish don't seem to have an effect, the warning about the unsupported device always shows up before the crash.

### Operating System

NAME="Ubuntu" VERSION="24.04.2 LTS (Noble Numbat)"

### CPU

AMD Ryzen 7 7800X3D 8-Core Processor

### GPU

AMD Radeon RX 9070 XT & gfx1036

### ROCm Version

ROCm 6.4.1

### ROCm Component

rocprofiler

### Steps to Reproduce

Install ROCm from AMD repo, 1st party builds of everything and issue `rocprofilerv3 --list-avail` on a system with gfx1036 and gfx1201.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module version 6.12.12 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.15
Runtime Ext Version:     1.7
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 7800X3D 8-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 7800X3D 8-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5050                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    130986240(0x7ceb100) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    130986240(0x7ceb100) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    130986240(0x7ceb100) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    130986240(0x7ceb100) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-3a68d8a11eb4a074               
  Marketing Name:          AMD Radeon RX 9070 XT              
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30032(0x7550)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2520                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 1012                               
  SDMA engine uCode::      838                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16695296(0xfec000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1201         
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx12-generic   
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*******                  
Agent 3                  
*******                  
  Name:                    gfx1036                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon Graphics                
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      256(0x100) KB                      
  Chip ID:                 5710(0x164e)                       
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2200                               
  BDFID:                   30208                              
  Internal Node ID:        2                                  
  Compute Unit:            2                                  
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       APU
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 22                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65493120(0x3e75880) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65493120(0x3e75880) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1036         
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx10-3-generic 
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***
```
### Additional Information

Specific invocation and stack trace:

```
mate@gputest1:~/Develop/dyniso-test$ /opt/rocm/bin/rocprofv3 --list-avail
W20250621 18:34:28.158455 126820973094720 metadata.cpp:210] rocprofiler_iterate_agent_supported_counters returned ROCPROFILER_STATUS_ERROR_AGENT_ARCH_NOT_SUPPORTED for agent 2 (gfx1036) :: Agent HW architecture is not supported, no counter metrics found.
[rocprofiler_iterate_agent_supported_counters( agent->id, iterate_agent_counters_callback, (void*) (&_counter_dim_info))][/longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/rocprofiler-sdk/source/libexec/rocprofiler-sdk/rocprofiler-avail/rocprofv3_avail.cpp:274] Iterate rocprofiler counters failed with error code 39: Agent HW architecture is not supported, no counter metrics found.
terminate called after throwing an instance of 'std::runtime_error'
  what():  [rocprofiler_iterate_agent_supported_counters( agent->id, iterate_agent_counters_callback, (void*) (&_counter_dim_info))][/longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/rocprofiler-sdk/source/libexec/rocprofiler-sdk/rocprofiler-avail/rocprofv3_avail.cpp:274] Iterate rocprofiler counters failure (Agent HW architecture is not supported, no counter metrics found.)
*** Aborted at 1750530868 (unix time) try "date -d @1750530868" if you are using GNU date ***
PC: @     0x7357ce69eb2c pthread_kill
*** SIGABRT (@0x3ea00031475) received by PID 201845 (TID 0x7357cf0d2740) from PID 201845; stack trace: ***
    @     0x7357ce6a1ed3 (unknown)
    @     0x7357ce53e060 (unknown)
    @     0x7357ce645330 (unknown)
    @     0x7357ce69eb2c pthread_kill
    @     0x7357ce64527e gsignal
    @     0x7357ce6288ff abort
    @     0x7357c4aa5ff5 (unknown)
    @     0x7357c4abb0da (unknown)
    @     0x7357c4aa5a55 std::terminate()
    @     0x7357c4abb391 __cxa_throw
    @     0x7357ce504691 (unknown)
    @     0x7357cea54378 rocprofiler_query_available_agents
    @     0x7357ce509145 avail_tool_init
    @     0x7357ce835b16 (unknown)
    @     0x7357ce8323ef (unknown)
    @     0x7357ce8350be ffi_call
    @     0x7357ce85211c (unknown)
    @     0x7357ce84d2af (unknown)
    @           0x548f85 _PyObject_MakeTpCall
    @           0x5d6b2f _PyEval_EvalFrameDefault
    @           0x5d500b PyEval_EvalCode
    @           0x6081e2 (unknown)
    @           0x6b5033 (unknown)
    @           0x6b4d9a _PyRun_SimpleFileObject
    @           0x6b4bcf _PyRun_AnyFileObject
    @           0x6bcc35 Py_RunMain
    @           0x6bc71d Py_BytesMain
    @     0x7357cf297222 (unknown)
    @     0x7357ce62a1ca (unknown)
    @     0x7357ce62a28b __libc_start_main
    @           0x6575a5 _start
Aborted (core dumped)
```

## 评论 (4)

### ppanchad-amd · 2025-06-26

Hi @MathiasMagnus. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-06-27

Hi @MathiasMagnus,

I gave this a try on a 9070 XT and was unable to reproduce the issue. I suspect that it is because you have integrated graphics on the system, which is currently not supported with ROCm. Please follow the steps to [Disable IGP](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html#disable-integrated-graphics-igp) and let me know if the issue persists, thanks!

### AngryLoki · 2025-06-28

Hi @MathiasMagnus , exactly this crash you are talking about was fixed in `amd-staging` branch, so it will be a part of future release.

But as correctly mentioned, iGPU causes various issues, for example, `rocprofv3-avail list` fails (workaround: `rocprofv3-avail --device 0 list`)

### darren-amd · 2025-07-08

I'm going to close this ticket since it appears to be solved. Please feel free to create another ticket if the issue persists, thanks!
