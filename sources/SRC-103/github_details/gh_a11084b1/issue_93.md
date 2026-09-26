# [Issue #93] [Issue]: rocprov3 invalid pointer on free when profiling python script

source: https://github.com/ROCm/rocprofiler-sdk/issues/93
state: closed | updated: 2025-08-07T18:30:34Z
labels: Under Investigation

## 正文

### Problem Description

When trying to run rocprofv3 to profile a python script, the profiler seems to hit an invalid pointer on a free() operation causing the profiler to exit. The exact error is below and the full logs are attached.

```sh
I20250731 08:32:42.633829 139852384890432 hsa.cpp:637] updating table entry for hsa_ext_image_get_capability_with_layout
I20250731 08:32:42.633831 139852384890432 hsa.cpp:637] updating table entry for hsa_ext_image_data_get_info_with_layout
I20250731 08:32:42.633833 139852384890432 hsa.cpp:637] updating table entry for hsa_ext_image_create_with_layout
I20250731 08:32:42.633837 139852384890432 scratch_memory.cpp:319] copying table entry for hsa_amd_tool_scratch_event_alloc_start
I20250731 08:32:42.633840 139852384890432 scratch_memory.cpp:319] copying table entry for hsa_amd_tool_scratch_event_alloc_end
I20250731 08:32:42.633845 139852384890432 scratch_memory.cpp:319] copying table entry for hsa_amd_tool_scratch_event_free_start
I20250731 08:32:42.633851 139852384890432 scratch_memory.cpp:319] copying table entry for hsa_amd_tool_scratch_event_free_end
I20250731 08:32:42.633854 139852384890432 scratch_memory.cpp:319] copying table entry for hsa_amd_tool_scratch_event_async_reclaim_start
I20250731 08:32:42.633861 139852384890432 scratch_memory.cpp:319] copying table entry for hsa_amd_tool_scratch_event_async_reclaim_end
I20250731 08:32:42.633864 139852384890432 scratch_memory.cpp:583] updating table entry for hsa_amd_tool_scratch_event_alloc_start
I20250731 08:32:42.633867 139852384890432 scratch_memory.cpp:583] updating table entry for hsa_amd_tool_scratch_event_alloc_end
I20250731 08:32:42.633869 139852384890432 scratch_memory.cpp:583] updating table entry for hsa_amd_tool_scratch_event_free_start
I20250731 08:32:42.633871 139852384890432 scratch_memory.cpp:583] updating table entry for hsa_amd_tool_scratch_event_free_end
I20250731 08:32:42.633874 139852384890432 scratch_memory.cpp:583] updating table entry for hsa_amd_tool_scratch_event_async_reclaim_start
I20250731 08:32:42.633876 139852384890432 scratch_memory.cpp:583] updating table entry for hsa_amd_tool_scratch_event_async_reclaim_end
I20250731 08:32:42.633879 139852384890432 runtime_initialization.cpp:123] HSA runtime has been initialized
free(): invalid pointer
W20250731 08:32:42.634097 139852384890432 tool.cpp:1902] rocprofv3_error_signal_handler caught signal 6...
I20250731 08:32:42.634121 139852384890432 tool.cpp:1183] invoked: finalize_rocprofv3
I20250731 08:32:42.634123 139852384890432 tool.cpp:1186] finalizing rocprofv3: caller='rocprofv3_error_signal_handler'...
I20250731 08:32:42.634126 139852384890432 registration.cpp:576] invoke_client_finalizer(client_id=240812945)
I20250731 08:32:42.634129 139852384890432 hsa.cpp:844] hsa reference count: 1
I20250731 08:32:42.634140 139852384890432 tool.cpp:274] flushing buffers...
I20250731 08:32:42.634146 139852384890432 tool.cpp:279] flushing buffer 2220
I20250731 08:32:42.634208 139852361102912 tool.cpp:763] Executing buffered tracing callback for 16 headers
I20250731 08:32:42.634918 139852384890432 tool.cpp:279] flushing buffer 2221
I20250731 08:32:42.634963 139852352710208 buffer.cpp:211] buffer at 2221 is empty...
I20250731 08:32:42.635002 139852384890432 tool.cpp:279] flushing buffer 2216
I20250731 08:32:42.635049 139852344317504 buffer.cpp:211] buffer at 2216 is empty...
```

[rocprofv3-free-crash.txt](https://github.com/user-attachments/files/21526285/rocprofv3-free-crash.txt)

### Operating System

 22.04.5 LTS (Jammy Jellyfish)

### CPU

Intel(R) Xeon(R) Platinum 8470

### GPU

AMD Instinct MI300X VF  

### ROCm Version

ROCm 6.4.0

### ROCm Component

rocprofiler

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```sh
rocminfo --support
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
  Name:                    Intel(R) Xeon(R) Platinum 8470     
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Platinum 8470     
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
  Max Clock Freq. (MHz):   0                                  
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            13                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    230893520(0xdc327d0) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    230893520(0xdc327d0) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    230893520(0xdc327d0) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    230893520(0xdc327d0) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx942                             
  Uuid:                    GPU-25a594c05f2eb594               
  Marketing Name:          AMD Instinct MI300X VF             
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
    L2:                      4096(0x1000) KB                    
    L3:                      262144(0x40000) KB                 
  Chip ID:                 29877(0x74b5)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2100                               
  BDFID:                   1280                               
  Internal Node ID:        1                                  
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
  Packet Processor uCode:: 177                                
  SDMA engine uCode::      24                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    200998912(0xbfb0000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    200998912(0xbfb0000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    200998912(0xbfb0000) KB            
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

I've tried using the same profiler for various programs/executables:
- A compiled c++ program works fine
- Any python executable with AITER seems to fail
- Any python executable with PyTorch-rocm seems to fail

## 评论 (8)

### ppanchad-amd · 2025-07-31

Hi @jeremyfelder. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-07-31

Hi @jeremyfelder,

Could you please provide me with the minimum reproduceable example that you are running? Also, are you running rocprofv3 from staging or are you using the one bundled with 6.4? Thanks!

### jeremyfelder · 2025-08-01

@darren-amd I've created a gist here: https://gist.github.com/jeremyfelder/6235397a4f80f3750cad3cb29f439498

It contains three files that I ran and referenced in the Additional Information section above. Also a README with commands used to run these.

I tried using both the 6.4.0 and 6.4.2 versions, but have not tried the staging branch

### jeremyfelder · 2025-08-03

@darren-amd I tried the same files on a different machine (`Intel(R) Xeon(R) Platinum 8568Y+`) and got different errors. From the errors when running `rocprofv3` with a python script that uses torch, it seems like torch doesn't have access to the GPUs anymore.

Running `matmul_aiter.py`:

```sh
I20250803 12:48:29.405217 128917906982720 hsa.cpp:589] copying table entry for hsa_ext_sampler_create
I20250803 12:48:29.405220 128917906982720 hsa.cpp:589] copying table entry for hsa_ext_sampler_destroy
I20250803 12:48:29.405222 128917906982720 hsa.cpp:589] copying table entry for hsa_ext_image_get_capability_with_layout
I20250803 12:48:29.405224 128917906982720 hsa.cpp:589] copying table entry for hsa_ext_image_data_get_info_with_layout
I20250803 12:48:29.405226 128917906982720 hsa.cpp:589] copying table entry for hsa_ext_image_create_with_layout
I20250803 12:48:29.405229 128917906982720 runtime_initialization.cpp:123] HSA runtime has been initialized
Traceback (most recent call last):
  File "/root/matmul_aiter.py", line 10, in <module>
    matrix1 = torch.randn(100, 200, device=device, dtype=torch.bfloat16)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/ltx/lib/python3.12/site-packages/torch/cuda/__init__.py", line 372, in _lazy_init
    torch._C._cuda_init()
RuntimeError: No HIP GPUs are available
I20250803 12:48:29.623491 128917906982720 tool.cpp:1998] rocprofv3: main function has returned with exit code: 1
I20250803 12:48:29.623521 128917906982720 tool.cpp:1183] invoked: finalize_rocprofv3
I20250803 12:48:29.623524 128917906982720 tool.cpp:1186] finalizing rocprofv3: caller='rocprofv3_main'...
I20250803 12:48:29.623527 128917906982720 registration.cpp:576] invoke_client_finalizer(client_id=3047967567)
I20250803 12:48:29.623536 128917906982720 hsa.cpp:844] hsa reference count: 1
I20250803 12:48:29.623550 128917906982720 tool.cpp:274] flushing buffers...
I20250803 12:48:29.623552 128917906982720 tool.cpp:279] flushing buffer 23016
```
---
Running `matmul_torch.py`:

```sh
I20250803 12:54:29.781079 131953165403968 hsa.cpp:589] copying table entry for hsa_ext_image_get_capability_with_layout
I20250803 12:54:29.781081 131953165403968 hsa.cpp:589] copying table entry for hsa_ext_image_data_get_info_with_layout
I20250803 12:54:29.781083 131953165403968 hsa.cpp:589] copying table entry for hsa_ext_image_create_with_layout
I20250803 12:54:29.781086 131953165403968 runtime_initialization.cpp:123] HSA runtime has been initialized
PyTorch with ROCm support is not available.
I20250803 12:54:29.901880 131953165403968 tool.cpp:1998] rocprofv3: main function has returned with exit code: 0
I20250803 12:54:29.901912 131953165403968 tool.cpp:1183] invoked: finalize_rocprofv3
I20250803 12:54:29.901914 131953165403968 tool.cpp:1186] finalizing rocprofv3: caller='rocprofv3_main'...
I20250803 12:54:29.901919 131953165403968 registration.cpp:576] invoke_client_finalizer(client_id=1231246112)
```
**`PyTorch with ROCm support is not available.` This print out is from the `matmul_torch.py` script.**

---

> [!NOTE]
> - Running these without the profiler, torch is able to find the GPU and the scripts complete as expected.
> - Rocm version used was the same 6.4.x
> - Rocprofv3 compiled from `amd-staging` branch produced the same results
> - User is a part of the `render` and `video` groups
> - The machine was a GPU droplet in AMD Developer Cloud


### darren-amd · 2025-08-05

Hi @jeremyfelder,

Thanks for the additional information. I gave this a try inside our latest Pytorch container with ROCm 6.4.2 and wasn't able to reproduce the issue with the latest aiter and triton versions. I suspect it may be related to the library versions you have installed. 

Could you please try our docker containers available [here](https://hub.docker.com/r/rocm/pytorch/tags), specifically `rocm/pytorch:rocm6.4.2_ubuntu24.04_py3.12_pytorch_release_2.6.0`. To update aiter and triton:

1. Install aiter with:
```
git clone --recursive https://github.com/ROCm/aiter.git
cd aiter
python3 setup.py develop
```
3. Update triton: `pip install --pre -U triton`

Please give that a try and let me know if the issue persists, thanks!

### jeremyfelder · 2025-08-06

@darren-amd Thanks for the quick response. I was able to get rocprofv3 working in the docker container you mentioned and also got it working outside of the docker container by not using the pytorch rocm version from the pytroch org and instead used the instructions from the [Radeon install guide](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-pytorch.html#install-pytorch-via-pip).

What is the difference between the wheels provided directly from amd and the wheel from pytorch org?

Also, i've noticed that the [log for writing to an output file successfully](https://github.com/ROCm/rocprofiler-sdk/blob/amd-staging/source/lib/output/output_stream.cpp#L111) is an Error level log. Not sure if that is meant to be like that, but thought I'd point it out. Threw me off for the first few times I looked at the logs.

Thanks for the help!

### darren-amd · 2025-08-06

@jeremyfelder, awesome to hear that its working for you now! The main difference is that we test the wheels we provide on ROCm, so there may be issues (such as the one you identified) when the nightly builds are updated. Is there anything else I can help you with?

### systems-assistant[bot] · 2025-08-07

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/143
