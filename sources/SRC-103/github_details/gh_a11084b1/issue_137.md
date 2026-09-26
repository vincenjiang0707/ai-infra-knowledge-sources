# [Issue #137] [Issue]: rocprofv3 kernel trace does not write into file

source: https://github.com/ROCm/rocprofiler-sdk/issues/137
state: closed | updated: 2025-09-15T15:57:42Z
labels: 

## 正文

### Problem Description

I was using rocprofv3 to profile vllm server and trying to get csv and perfetto trace format output. I got: `E20250904 21:02:16.242980 139963295913728 output_stream.cpp:105] Opened result file: test_run/mem_cu_results.pftrace`. But the trace did not write into the files.

I have a python script that starts vllm server and automatically trigger vllm benchmarks. Here's the command I used:
```
rocprofv3 --kernel-trace --pmc GPU_UTIL,MfmaUtil,BANDWIDTH_EA --output-format csv pftrace \
  -o mem_cu -d test_run \
  -- python3 ./sweep_chunk_size.py 
```

## What I expected:
rocprofv3 runs without error and I get both .csv and .pftrace format traces.

## What happened:
I got `E20250904 21:02:16.230164 139963295913728 output_stream.cpp:105] Opened result file: test_run/mem_cu_agent_info.csv` and `E20250904 21:02:16.242980 139963295913728 output_stream.cpp:105] Opened result file: test_run/mem_cu_results.pftrace` in the shell output. But the 2 output files generated under test_run dir (mem_cu_agent_info.csv and mem_cu_results.pftrace) do not contains any kernel trace output.

## Environment
Docker built from vllm official repo, tag/v0.10.0,

### Operating System

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### CPU

Intel(R) Xeon(R) Platinum 8480+ 

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

```
rocprofv3 --kernel-trace --pmc GPU_UTIL,MfmaUtil,BANDWIDTH_EA --output-format csv pftrace \
  -o mem_cu -d test_run \
  -- python3 ./sweep_chunk_size.py 
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support
```
ROCk module version 6.10.5 is loaded
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
  Name:                    Intel(R) Xeon(R) Platinum 8480+    
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Platinum 8480+    
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
    L1:                      49152(0xc000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            112                                
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    1056515700(0x3ef92674) KB          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    1056515700(0x3ef92674) KB          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    1056515700(0x3ef92674) KB          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    1056515700(0x3ef92674) KB          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    Intel(R) Xeon(R) Platinum 8480+    
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Platinum 8480+    
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      49152(0xc000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            112                                
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    1056875292(0x3efea31c) KB          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    1056875292(0x3efea31c) KB          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    1056875292(0x3efea31c) KB          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    1056875292(0x3efea31c) KB          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 3                  
*******                  
  Name:                    gfx942                             
  Uuid:                    GPU-7f8b77e5fb46a39f               
  Marketing Name:          AMD Instinct MI300X                
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
    L1:                      32(0x20) KB                        
    L2:                      4096(0x1000) KB                    
    L3:                      262144(0x40000) KB                 
  Chip ID:                 29857(0x74a1)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2100                               
  BDFID:                   4352                               
  Internal Node ID:        2                                  
  Compute Unit:            304                                
  SIMDs per CU:            4                                  
  Shader Engines:          32                                 
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    2048(0x800)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 166                                
  SDMA engine uCode::      22                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    201310208(0xbffc000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    201310208(0xbffc000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
      Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-
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
Agent 4                  
*******                  
  Name:                    gfx942                             
  Uuid:                    GPU-8a94f70b8b1f8ef3               
  Marketing Name:          AMD Instinct MI300X                
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    3                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      4096(0x1000) KB                    
    L3:                      262144(0x40000) KB                 
  Chip ID:                 29857(0x74a1)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2100                               
  BDFID:                   12032                              
  Internal Node ID:        3                                  
  Compute Unit:            304                                
  SIMDs per CU:            4                                  
  Shader Engines:          32                                 
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    2048(0x800)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 166                                
  SDMA engine uCode::      22                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    201310208(0xbffc000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    201310208(0xbffc000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
      Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-
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
shell output:

<img width="841" height="611" alt="Image" src="https://github.com/user-attachments/assets/dd06ce3b-7e35-4641-807c-e1eb60ee896a" />

2 output files I got:
test_run/mem_cu_agent_info.csv
```
"Node_Id","Logical_Node_Id","Agent_Type","Cpu_Cores_Count","Simd_Count","Cpu_Core_Id_Base","Simd_Id_Base","Max_Waves_Per_Simd","Lds_Size_In_Kb","Gds_Size_In_Kb","Num_Gws","Wave_Front_Size","Num_Xcc","Cu_Count","Array_Count","Num_Shader_Banks","Simd_Arrays_Per_Engine","Cu_Per_Simd_Array","Simd_Per_Cu","Max_Slots_Scratch_Cu","Gfx_Target_Version","Vendor_Id","Device_Id","Location_Id","Domain","Drm_Render_Minor","Num_Sdma_Engines","Num_Sdma_Xgmi_Engines","Num_Sdma_Queues_Per_Engine","Num_Cp_Queues","Max_Engine_Clk_Ccompute","Max_Engine_Clk_Fcompute","Sdma_Fw_Version","Fw_Version","Capability","Cu_Per_Engine","Max_Waves_Per_Cu","Family_Id","Workgroup_Max_Size","Grid_Max_Size","Local_Mem_Size","Hive_Id","Gpu_Id","Workgroup_Max_Dim_X","Workgroup_Max_Dim_Y","Workgroup_Max_Dim_Z","Grid_Max_Dim_X","Grid_Max_Dim_Y","Grid_Max_Dim_Z","Name","Vendor_Name","Product_Name","Model_Name"
0,0,"CPU",112,0,0,0,0,0,0,0,0,1,112,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3800,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,"Intel(R) Xeon(R) Platinum 8480+","CPU","Intel(R) Xeon(R) Platinum 8480+",""
1,1,"CPU",112,0,128,0,0,0,0,0,0,1,112,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3800,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,"Intel(R) Xeon(R) Platinum 8480+","CPU","Intel(R) Xeon(R) Platinum 8480+",""
2,2,"GPU",0,1216,0,2147487744,8,64,0,64,64,8,304,32,32,1,10,4,32,90402,4098,29857,4352,0,128,2,14,8,24,3800,2100,22,166,746037888,9,32,141,1024,4294967295,0,11786967012253712646,32700,1024,1024,1024,4294967295,4294967295,4294967295,"gfx942","AMD","AMD Instinct MI300X","ip discovery"
3,3,"GPU",0,1216,0,2147487784,8,64,0,64,64,8,304,32,32,1,10,4,32,90402,4098,29857,12032,0,136,2,14,8,24,3800,2100,22,166,746037888,9,32,141,1024,4294967295,0,11786967012253712646,3884,1024,1024,1024,4294967295,4294967295,4294967295,"gfx942","AMD","AMD Instinct MI300X","ip discovery"
```

test_run/mem_cu_results.pftrace
Does not contain any kernel trace.

<img width="850" height="603" alt="Image" src="https://github.com/user-attachments/assets/87d1b25f-4cdd-4b68-bb51-f4ad3697b19a" />

## 评论 (8)

### ppanchad-amd · 2025-09-05

Hi @ahz-r3v. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-09-09

Hi @ahz-r3v,

Thanks for reporting the issue, could you please give me more details on the workload you are running (the contents of `sweep_chunk_size.py`) so that I can try reproducing the issue on my end? Could you also give it a try inside of our vLLM docker container [here](https://hub.docker.com/layers/rocm/vllm-dev/nightly/images/sha256-2c298bab13c6cf86b56e5f530eae1149f4269351ec03e9a49b94960d9e02d893). It looks like the data is being captured inside of the csv file but not being propagated to the perfetto output for some reason.

### ahz-r3v · 2025-09-11

[sweep_chunk_size (2).py](https://github.com/user-attachments/files/22267254/sweep_chunk_size.2.py)

Hi @darren-amd, I've tried the image you provided, and unfortunately it shows the same problem.
Attached is the script I used:

### darren-amd · 2025-09-11

Hi @ahz-r3v,

Thanks for providing the file, it looks like because rocprofv3 is being attached to the python script rather than the vLLM workload, it isn't picking up the kernel traces. I'd recommend running the vllm server with rocprofv3 instead, something like:
```
cmd = [
        "rocprofv3 --kernel-trace --pmc GPU_UTIL,MfmaUtil,BANDWIDTH_EA --output-format csv pftrace", " -- ", "vllm", "serve", MODEL_NAME,
        "--port", str(port),
        "--tensor-parallel-size", str(2),
        "--max-num-batched-tokens", str(chunk_size),
        "--gpu-memory-utilization", str(gpu_utilization),
        "--enforce-eager",
    ] + extra_args
```

Please give that a try and let me know if you run into any issues, thanks!


### ahz-r3v · 2025-09-12

Thank you for your advice @darren-amd, I updated this part like this:
```
    cmd = [
        "rocprofv3", "--kernel-trace", "--pmc", "MfmaUtil", "--output-format", "csv", "pftrace", 
        "-o", "mem_cu", "-d", "test_run_2", "--",
        "vllm", "serve", MODEL_NAME,
        "--port", str(port),
        "--tensor-parallel-size", str(tp_size),
        "--max-num-batched-tokens", str(chunk_size),
        "--gpu-memory-utilization", str(gpu_utilization),
        "--enforce-eager",
    ] + extra_args
```
but the behavior remains the same, the trace has no kernel events.

> Hi [@ahz-r3v](https://github.com/ahz-r3v),
> 
> Thanks for providing the file, it looks like because rocprofv3 is being attached to the python script rather than the vLLM workload, it isn't picking up the kernel traces. I'd recommend running the vllm server with rocprofv3 instead, something like:
> 
> ```
> cmd = [
>         "rocprofv3 --kernel-trace --pmc GPU_UTIL,MfmaUtil,BANDWIDTH_EA --output-format csv pftrace", " -- ", "vllm", "serve", MODEL_NAME,
>         "--port", str(port),
>         "--tensor-parallel-size", str(2),
>         "--max-num-batched-tokens", str(chunk_size),
>         "--gpu-memory-utilization", str(gpu_utilization),
>         "--enforce-eager",
>     ] + extra_args
> ```
> 
> Please give that a try and let me know if you run into any issues, thanks!



### darren-amd · 2025-09-12

Hi @ahz-r3v,

Thanks for getting back to me, I gave this a try on my end and was able to get it working with rocprofv3 built from source, without the modifications I mentioned above. You can build rocprof-sdk as follows:
```
git clone https://github.com/ROCm/rocm-systems.git
cd rocm-systems/projects
cmake                                         \
      -B rocprofiler-sdk-build                \
      -D ROCPROFILER_BUILD_TESTS=OFF           \
      -D ROCPROFILER_BUILD_SAMPLES=OFF         \
      -D CMAKE_INSTALL_PREFIX=/opt/rocm       \
       rocprofiler-sdk
cmake --build rocprofiler-sdk-build --target all --parallel 75
cmake --build rocprofiler-sdk-build --target install --parallel 75
```
Afterwards, I ran: `rocprofv3 --kernel-trace --output-format csv pftrace -- python3 sweep_chunk_size.py`. Please give that a try and let me know if you run into any issues, thanks!


### ahz-r3v · 2025-09-13

> Hi [@ahz-r3v](https://github.com/ahz-r3v),
> 
> Thanks for getting back to me, I gave this a try on my end and was able to get it working with rocprofv3 built from source, without the modifications I mentioned above. You can build rocprof-sdk as follows:
> 
> ```
> git clone https://github.com/ROCm/rocm-systems.git
> cd rocm-systems/projects
> cmake                                         \
>       -B rocprofiler-sdk-build                \
>       -D ROCPROFILER_BUILD_TESTS=OFF           \
>       -D ROCPROFILER_BUILD_SAMPLES=OFF         \
>       -D CMAKE_INSTALL_PREFIX=/opt/rocm       \
>        rocprofiler-sdk
> cmake --build rocprofiler-sdk-build --target all --parallel 75
> cmake --build rocprofiler-sdk-build --target install --parallel 75
> ```
> 
> Afterwards, I ran: `rocprofv3 --kernel-trace --output-format csv pftrace -- python3 sweep_chunk_size.py`. Please give that a try and let me know if you run into any issues, thanks!

Hi @darren-amd, this works for me! I can get the trace correctly now, thanks for your help!

### darren-amd · 2025-09-15

Awesome, glad to help! I'm going to close this ticket off now.
