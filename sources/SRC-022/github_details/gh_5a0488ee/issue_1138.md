# [Issue #1138] [Issue]: How to lower the resources that need to complile rccl 6.0.2 ?

source: https://github.com/ROCm/rccl/issues/1138
state: closed | updated: 2024-04-29T18:56:33Z
labels: 

## 正文

### Problem Description

How I can lower the resources need to compile the project ?

Start configure with:

```
CXX=/opt/rocm/bin/hipcc cmake \
    -DAMDGPU_TARGETS="gfx1100" \
    -DHIP_CLANG_INCLUDE_PATH=/opt/rocm/llvm/include \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS=OFF \
    -DGTEST_LIBRARY=/usr/lib64 \
    -DGTEST_INCLUDE_DIR=/usr/include \
    -DGTEST_MAIN_LIBRARY=/usr/lib64 \
    -DCPACK_GENERATOR=TGZ \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_PARALLEL_LEVEL=8 \
    -DLLVM_PARALLEL_LINK_JOBS=8 \
    -G Ninja \
    ..
```

-- Checking for ROCm support for GPU targets:
-- Compiling for gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack-;gfx90a:xnack+;gfx940;gfx941;gfx942;gfx1030;gfx1100;gfx1101;gfx1102
-- Setting ROCM_PATH based on hipcc location to /opt/rocm
-- HIP compiler:     clang
-- HIP runtime:      rocclr
-- hipcc executable: /opt/rocm/bin/hipcc
-- hipcc version:    6.0.32831
-- ROCm version: 6.0.2
-- Indirect function call enabled
-- HSA runtime: /opt/rocm/include
-- Found rocm_smi at /opt/rocm/include
-- Kernarg preloading to SGPR enabled
......
-- Generating /mnt/ubuntufs/test/rocm-build/build/rccl/hipify/src/collectives/device/msccl_kernel_SumPostDiv_uint64_t.cpp
-- HIP_UNCACHED_MEMORY enabled
-- Building shared RCCL library
-- rocm-cmake: Set license file to /mnt/ubuntufs/test/rocm-git/rccl/LICENSE.txt.
-- Configuring done (0.4s)
-- Generating done (0.0s)
-- Build files have been written to: /mnt/ubuntufs/test/rocm-build/build/rccl
....

After that the process stuck on linking library:

-- Generating /mnt/ubuntufs/test/rocm-build/build/rccl/hipify/src/collectives/device/msccl_kernel_SumPostDiv_uint64_t.cpp
-- HIP_UNCACHED_MEMORY enabled
-- Building shared RCCL library
-- rocm-cmake: Set license file to /mnt/ubuntufs/test/rocm-git/rccl/LICENSE.txt.
-- Configuring done (0.7s)
-- Generating done (0.0s)
-- Build files have been written to: /mnt/ubuntufs/test/rocm-build/build/rccl
[1/291] Updating git_version.cpp if necessary
-- Updating git_version.cpp
[289/291] Linking CXX shared library librccl.so.1.0.60002

and after a while (few hours)  and 30 load average the system killed the process because no more memory and swap memory with reason:

akeFiles/rccl.dir/hipify/src/collectives/device/msccl_kernel_SumPostDiv_int8_t.cpp.o CMakeFiles/rccl.dir/hipify/src/collectives/device/msccl_kernel_SumPostDiv_uint8_t.cpp.o CMakeFiles/rccl.dir/hipify/src/collectives/device/msccl_kernel_SumPostDiv_int32_t.cpp.o CMakeFiles/rccl.dir/hipify/src/collectives/device/msccl_kernel_SumPostDiv_uint32_t.cpp.o CMakeFiles/rccl.dir/hipify/src/collectives/device/msccl_kernel_SumPostDiv_int64_t.cpp.o CMakeFiles/rccl.dir/hipify/src/collectives/device/msccl_kernel_SumPostDiv_uint64_t.cpp.o CMakeFiles/rccl.dir/git_version.cpp.o -L/opt/rocm/lib64 -Wl,-rpath,/opt/rocm/lib64:  -fgpu-rdc  -ldl  /opt/rocm/lib64/librocm_smi64.so.1.0  /opt/rocm/lib64/libamdhip64.so.6.0.32831  --hip-link  --offload-arch=gfx803  --offload-arch=gfx900:xnack-  --offload-arch=gfx906:xnack-  --offload-arch=gfx908:xnack-  --offload-arch=gfx90a:xnack-  --offload-arch=gfx90a:xnack+  --offload-arch=gfx940  --offload-arch=gfx941  --offload-arch=gfx942  --offload-arch=gfx1030  --offload-arch=gfx1100  --offload-arch=gfx1101  --offload-arch=gfx1102  /opt/rocm/llvm/lib/clang/17.0.0/lib/linux/libclang_rt.builtins-x86_64.a  -lpthread  -lrt  -ldl && :
clang: warning: argument unused during compilation: '-mllvm --amdgpu-kernarg-preload-count=16' [-Wunused-command-line-argument]
clang: error: unable to execute command: Killed
clang: error: unable to execute command: Killed
clang: error: unable to execute command: Killed
clang: error: amdgcn-link command failed due to signal (use -v to see invocation)
clang: error: amdgcn-link command failed due to signal (use -v to see invocation)
clang: error: amdgcn-link command failed due to signal (use -v to see invocation)
clang version 17.0.0
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
clang: warning: treating 'c' input as 'c++' when in C++ mode, this behavior is deprecated [-Wdeprecated]
clang: warning: treating 'c' input as 'c++' when in C++ mode, this behavior is deprecated [-Wdeprecated]
clang: warning: treating 'c' input as 'c++' when in C++ mode, this behavior is deprecated [-Wdeprecated]
clang: note: diagnostic msg: Error generating preprocessed source(s).
Elapsed time (seconds): 8919.17
ninja: build stopped: subcommand failed.

free -m
               total        used        free      shared  buff/cache   available
Mem:           32013       31805         207           0          94         208
Swap:          12072       12072           0



OS:
NAME=Slackware
VERSION="15.0"
CPU: 
model name	: AMD Ryzen 7 3800X 8-Core Processor
GPU:
  Name:                    AMD Ryzen 7 3800X 8-Core Processor 
  Marketing Name:          AMD Ryzen 7 3800X 8-Core Processor 
  Name:                    gfx1100                            
  Marketing Name:          AMD Radeon RX 7900 XTX             
      Name:                    amdgcn-amd-amdhsa--gfx1100 


Any suggestion how to build it ?



### Operating System

Slackware 15.0 x86_64

### CPU

AMD Ryzen 7 3800X 8-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.0.0

### ROCm Component

rccl

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 3800X 8-Core Processor 
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 3800X 8-Core Processor 
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
  Max Clock Freq. (MHz):   4560                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32782004(0x1f436b4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32782004(0x1f436b4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32782004(0x1f436b4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-6e99eccb20090e4e               
  Marketing Name:          AMD Radeon RX 7900 XTX             
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
    L2:                      6144(0x1800) KB                    
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2482                               
  BDFID:                   3072                               
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
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
  Packet Processor uCode:: 550                                
  SDMA engine uCode::      19                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1100         
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

### Additional Information

_No response_

## 评论 (2)

### wenkaidu · 2024-04-11

Can you try simple build command, ./install.sh -l, and attach output?

### RandUser123sa · 2024-04-26

The problem is resolved. The compilation process take 32 GB ram memory and 15 GB swap space which was over and that was the issue. I increase the swap space to 100 GB and everything was done for few minutes. I can't publish the output because I delete the project a long time ago.
