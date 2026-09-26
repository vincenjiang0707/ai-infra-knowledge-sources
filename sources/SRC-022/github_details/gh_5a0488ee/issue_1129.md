# [Issue #1129] Distributed Data Parallel (DDP) Training on PyTorch with AMD GPUs (ROCm) and RCCL test hangs

source: https://github.com/ROCm/rccl/issues/1129
state: closed | updated: 2024-05-17T13:51:06Z
labels: 

## 正文

### Problem Description

I have a Ubuntu 22.04 machine with two AMD MI100 GPUs installed. When trying to run a PyTorch training script, using DDP and `backend="nccl"` (which under the hood should use `rccl`), the script hangs with the GPU use at 100%, without the expected GPU temperature buildup.

At first I thought it was related to my PyTorch installation, but when I tried the `all_reduce_perf` test of [`rccl-tests`](https://github.com/ROCm/rccl-tests) I observed the same behaviour: the script hangs with the GPU use at 100%, without the expected GPU temperature buildup.

Output of `all_reduce_perf`:
```
$ ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2
# nThread 1 nGpus 2 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version develop:3f7f785
# Using devices
#   Rank  0 Pid  21284 on deep-visionscaper3 device  0 [0000:2f:00.0] AMD Instinct MI100
#   Rank  1 Pid  21284 on deep-visionscaper3 device  1 [0000:03:00.0] AMD Instinct MI100
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)     
```
Nothing happens after this initial output.

Output of `rock-smi`:
```
$ rocm-smi --alldevices -f -P -t -u -g


============================ ROCm System Management Interface ============================
====================================== Temperature =======================================
GPU[0]		: Temperature (Sensor edge) (C): 63.0
GPU[0]		: Temperature (Sensor junction) (C): 76.0
GPU[0]		: Temperature (Sensor memory) (C): 61.0
GPU[1]		: Temperature (Sensor edge) (C): 58.0
GPU[1]		: Temperature (Sensor junction) (C): 70.0
GPU[1]		: Temperature (Sensor memory) (C): 56.0
==========================================================================================
=============================== Current clock frequencies ================================
GPU[0]		: sclk clock level: 15 (1502Mhz)
GPU[1]		: sclk clock level: 15 (1502Mhz)
==========================================================================================
=================================== Current Fan Metric ===================================
GPU[0]		: Not supported
GPU[1]		: Not supported
==========================================================================================
=================================== Power Consumption ====================================
GPU[0]		: Average Graphics Package Power (W): 114.0
GPU[1]		: Average Graphics Package Power (W): 107.0
==========================================================================================
=================================== % time GPU is busy ===================================
GPU[0]		: GPU use (%): 100
GPU[1]		: GPU use (%): 100
==========================================================================================
================================== End of ROCm SMI Log ===================================
```

The version of rccl I have installed:
```
$ apt list --installed | grep rccl

rccl-dev/jammy,now 2.18.3.60002-115~22.04 amd64 [installed,automatic]
rccl/jammy,now 2.18.3.60002-115~22.04 amd64 [installed,automatic]
```

**Am I missing anything in my installation?**

### Operating System

Ubuntu 22.04.4 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen Threadripper PRO 5975WX 32-Cores

### GPU

AMD Instinct MI100

### ROCm Version

ROCm 6.0.0

### ROCm Component

rccl

### Steps to Reproduce

Run ` ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2` of the `rccl-tests` repo, it should perform the `all_reduce` test without blocking.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
$ /opt/rocm/bin/rocminfo --support
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
  Name:                    AMD Ryzen Threadripper PRO 5975WX 32-Cores
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen Threadripper PRO 5975WX 32-Cores
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
  Max Clock Freq. (MHz):   3600                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            64                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    527960576(0x1f780a00) KB           
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    527960576(0x1f780a00) KB           
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    527960576(0x1f780a00) KB           
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx908                             
  Uuid:                    GPU-6fdb95cab945d4fe               
  Marketing Name:          AMD Instinct MI100                 
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
    L1:                      16(0x10) KB                        
    L2:                      8192(0x2000) KB                    
  Chip ID:                 29580(0x738c)                      
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1502                               
  BDFID:                   12032                              
  Internal Node ID:        1                                  
  Compute Unit:            120                                
  SIMDs per CU:            4                                  
  Shader Engines:          8                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 65                                 
  SDMA engine uCode::      18                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    33538048(0x1ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    33538048(0x1ffc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx908:sramecc+:xnack-
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
  Name:                    gfx908                             
  Uuid:                    GPU-c088ca837a22409d               
  Marketing Name:          AMD Instinct MI100                 
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
    L2:                      8192(0x2000) KB                    
  Chip ID:                 29580(0x738c)                      
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1502                               
  BDFID:                   768                                
  Internal Node ID:        2                                  
  Compute Unit:            120                                
  SIMDs per CU:            4                                  
  Shader Engines:          8                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 65                                 
  SDMA engine uCode::      18                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    33538048(0x1ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    33538048(0x1ffc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx908:sramecc+:xnack-
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

```
$ echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";
  echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;
  echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
OS:
NAME="Ubuntu"
VERSION="22.04.4 LTS (Jammy Jellyfish)"
CPU: 
model name	: AMD Ryzen Threadripper PRO 5975WX 32-Cores
GPU:
  Name:                    AMD Ryzen Threadripper PRO 5975WX 32-Cores
  Marketing Name:          AMD Ryzen Threadripper PRO 5975WX 32-Cores
  Name:                    gfx908                             
  Marketing Name:          AMD Instinct MI100                 
      Name:                    amdgcn-amd-amdhsa--gfx908:sramecc+:xnack-
  Name:                    gfx908                             
  Marketing Name:          AMD Instinct MI100                 
      Name:                    amdgcn-amd-amdhsa--gfx908:sramecc+:xnack-
```
```
$ apt show rocm-libs -a
Package: rocm-libs
Version: 6.0.2.60002-115~22.04
Priority: optional
Section: devel
Maintainer: ROCm Dev Support <rocm-dev.support@amd.com>
Installed-Size: 13.3 kB
Depends: hipblas (= 2.0.0.60002-115~22.04), hipblaslt (= 0.6.0.60002-115~22.04), hipfft (= 1.0.13.60002-115~22.04), hipsolver (= 2.0.0.60002-115~22.04), hipsparse (= 3.0.0.60002-115~22.04), hiptensor (= 1.1.0.60002-115~22.04), miopen-hip (= 3.00.0.60002-115~22.04), half (= 1.12.0.60002-115~22.04), rccl (= 2.18.3.60002-115~22.04), rocalution (= 3.0.3.60002-115~22.04), rocblas (= 4.0.0.60002-115~22.04), rocfft (= 1.0.25.60002-115~22.04), rocrand (= 3.0.0.60002-115~22.04), hiprand (= 2.10.16.60002-115~22.04), rocsolver (= 3.24.0.60002-115~22.04), rocsparse (= 3.0.2.60002-115~22.04), rocm-core (= 6.0.2.60002-115~22.04), composablekernel-dev (= 1.1.0.60002-115~22.04), hipblas-dev (= 2.0.0.60002-115~22.04), hipblaslt-dev (= 0.6.0.60002-115~22.04), hipcub-dev (= 3.0.0.60002-115~22.04), hipfft-dev (= 1.0.13.60002-115~22.04), hipsolver-dev (= 2.0.0.60002-115~22.04), hipsparse-dev (= 3.0.0.60002-115~22.04), hiptensor-dev (= 1.1.0.60002-115~22.04), miopen-hip-dev (= 3.00.0.60002-115~22.04), rccl-dev (= 2.18.3.60002-115~22.04), rocalution-dev (= 3.0.3.60002-115~22.04), rocblas-dev (= 4.0.0.60002-115~22.04), rocfft-dev (= 1.0.25.60002-115~22.04), rocprim-dev (= 3.0.0.60002-115~22.04), rocrand-dev (= 3.0.0.60002-115~22.04), hiprand-dev (= 2.10.16.60002-115~22.04), rocsolver-dev (= 3.24.0.60002-115~22.04), rocsparse-dev (= 3.0.2.60002-115~22.04), rocthrust-dev (= 3.0.0.60002-115~22.04), rocwmma-dev (= 1.3.0.60002-115~22.04)
Homepage: https://github.com/RadeonOpenCompute/ROCm
Download-Size: 1050 B
APT-Sources: https://repo.radeon.com/rocm/apt/6.0.2 jammy/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime software stack
```
```
$ apt show rccl -a
Package: rccl
Version: 2.18.3.60002-115~22.04
Priority: optional
Section: devel
Maintainer: RCCL Maintainer <rccl-maintainer@amd.com>
Installed-Size: 520 MB
Depends: hip-rocclr (>= 3.5.0), rocm-smi-lib (>= 4.0.0), rocm-core, libc6 (>= 2.34), libgcc-s1 (>= 3.0), libstdc++6 (>= 11)
Recommends: rccl-dev (>=2.18.3.60002)
Download-Size: 13.7 MB
APT-Manual-Installed: no
APT-Sources: https://repo.radeon.com/rocm/apt/6.0.2 jammy/main amd64 Packages
Description: ROCm Communication Collectives Library
 ROCm Communication Collectives Library
 Optimized primitives for collective multi-GPU communication
```

## 评论 (20)

### nileshnegi · 2024-04-01

Please re-run `all_reduce_perf` with `NCCL_DEBUG=VERSION` as: `NCCL_DEBUG=VERSION ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2` and share the output line stating `RCCL version`... I'd like to know the exact RCCL version and commit that is causing this hang.

Also, can you share the ROCm kernel version installed on your machine -- the output of `dkms status | grep amdgpu`?

### visionscaper · 2024-04-01

Hi @nileshnegi, thanks for looking in to this.

The RCCL version:
```
RCCL version 2.18.3+hip6.0 HEAD:2f6d59e+
```

The ROCm kernel version:
```
amdgpu/6.3.6-1718217.22.04, 5.15.0-101-generic, x86_64: installed
```
 

### visionscaper · 2024-04-01

HI @nileshnegi, I have additional info. I was looking at this issue from the PyTorch side and found that there was actually an issue with applying [`dist.barrier`](https://pytorch.org/docs/stable/distributed.html#torch.distributed.barrier) instead of DDP.  So, I searched online if other had this issue and came across [this post](https://discuss.pytorch.org/t/torch-distributed-barrier-doesnt-work-with-pytorch-2-0-and-backend-nccl/190232) that mentioned setting:
```
export NCCL_P2P_DISABLE=1
```
After setting this environment variable the test works!
```
$ ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2
# nThread 1 nGpus 2 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version develop:3f7f785
# Using devices
#   Rank  0 Pid  36660 on deep-visionscaper3 device  0 [0000:2f:00.0] AMD Instinct MI100
#   Rank  1 Pid  36660 on deep-visionscaper3 device  1 [0000:03:00.0] AMD Instinct MI100
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
           8             2     float     sum      -1    14.07    0.00    0.00      0    13.67    0.00    0.00      0
          16             4     float     sum      -1    14.51    0.00    0.00      0    14.79    0.00    0.00      0
          32             8     float     sum      -1    14.77    0.00    0.00      0    12.78    0.00    0.00      0
          64            16     float     sum      -1    13.09    0.00    0.00      0    13.23    0.00    0.00      0
         128            32     float     sum      -1    13.00    0.01    0.01      0    12.98    0.01    0.01      0
         256            64     float     sum      -1    13.17    0.02    0.02      0    13.23    0.02    0.02      0
         512           128     float     sum      -1    13.37    0.04    0.04      0    13.31    0.04    0.04      0
        1024           256     float     sum      -1    13.21    0.08    0.08      0    13.22    0.08    0.08      0
        2048           512     float     sum      -1    13.37    0.15    0.15      0    13.46    0.15    0.15      0
        4096          1024     float     sum      -1    14.57    0.28    0.28      0    14.43    0.28    0.28      0
        8192          2048     float     sum      -1    14.69    0.56    0.56      0    14.48    0.57    0.57      0
       16384          4096     float     sum      -1    26.79    0.61    0.61      0    27.56    0.59    0.59      0
       32768          8192     float     sum      -1    28.71    1.14    1.14      0    28.01    1.17    1.17      0
       65536         16384     float     sum      -1    27.36    2.40    2.40      0    27.24    2.41    2.41      0
      131072         32768     float     sum      -1    33.80    3.88    3.88      0    33.93    3.86    3.86      0
      262144         65536     float     sum      -1    47.68    5.50    5.50      0    46.88    5.59    5.59      0
      524288        131072     float     sum      -1    72.23    7.26    7.26      0    72.21    7.26    7.26      0
     1048576        262144     float     sum      -1    120.9    8.67    8.67      0    122.1    8.59    8.59      0
     2097152        524288     float     sum      -1    225.3    9.31    9.31      0    225.6    9.29    9.29      0
     4194304       1048576     float     sum      -1    431.5    9.72    9.72      0    432.8    9.69    9.69      0
     8388608       2097152     float     sum      -1    849.3    9.88    9.88      0    851.2    9.85    9.85      0
    16777216       4194304     float     sum      -1   1735.4    9.67    9.67      0   1735.0    9.67    9.67      0
    33554432       8388608     float     sum      -1   3417.2    9.82    9.82      0   3418.8    9.81    9.81      0
    67108864      16777216     float     sum      -1   6521.8   10.29   10.29      0   6582.1   10.20   10.20      0
   134217728      33554432     float     sum      -1    12192   11.01   11.01      0    12354   10.86   10.86      0
# Errors with asterisks indicate errors that have exceeded the maximum threshold.
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 4.00614 
```
The question is now, why do I need to set `NCCL_P2P_DISABLE=1`?

### visionscaper · 2024-04-01

Additional info 2:
I enabled NCCL P2P again and set `NCCL_DEBUG=INFO`:

```
freddy@deep-visionscaper3:~/workspace/rocm/rccl-tests$ export NCCL_DEBUG=INFO
freddy@deep-visionscaper3:~/workspace/rocm/rccl-tests$ export NCCL_P2P_DISABLE=0
freddy@deep-visionscaper3:~/workspace/rocm/rccl-tests$ ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2
# nThread 1 nGpus 2 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version develop:3f7f785
# Using devices
#   Rank  0 Pid  38629 on deep-visionscaper3 device  0 [0000:2f:00.0] AMD Instinct MI100
#   Rank  1 Pid  38629 on deep-visionscaper3 device  1 [0000:03:00.0] AMD Instinct MI100
deep-visionscaper3:38629:38629 [0] NCCL INFO Bootstrap : Using enp37s0f1:192.168.178.85<0>
deep-visionscaper3:38629:38629 [0] NCCL INFO NET/Plugin : Plugin load (librccl-net.so) returned 2 : librccl-net.so: cannot open shared object file: No such file or directory
deep-visionscaper3:38629:38629 [0] NCCL INFO NET/Plugin : No plugin found, using internal implementation
deep-visionscaper3:38629:38629 [0] NCCL INFO Kernel version: 5.15.0-101-generic

deep-visionscaper3:38629:38629 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:132 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
deep-visionscaper3:38629:38629 [1] NCCL INFO ROCr version 1.1
deep-visionscaper3:38629:38629 [1] NCCL INFO Dmabuf feature disabled without NCCL_ENABLE_DMABUF_SUPPORT=1
RCCL version 2.18.3+hip6.0 HEAD:2f6d59e+
deep-visionscaper3:38629:38635 [1] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
deep-visionscaper3:38629:38635 [1] NCCL INFO Failed to open libibverbs.so[.1]
deep-visionscaper3:38629:38635 [1] NCCL INFO NET/Socket : Using [0]enp37s0f1:192.168.178.85<0>
deep-visionscaper3:38629:38635 [1] NCCL INFO Using network Socket
deep-visionscaper3:38629:38634 [0] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
deep-visionscaper3:38629:38634 [0] NCCL INFO Using network Socket
deep-visionscaper3:38629:38635 [1] NCCL INFO comm 0x121b210 rank 1 nranks 2 cudaDev 1 busId 3000 commId 0xd5377226347d7d43 - Init START
deep-visionscaper3:38629:38634 [0] NCCL INFO comm 0x15cd470 rank 0 nranks 2 cudaDev 0 busId 2f000 commId 0xd5377226347d7d43 - Init START
deep-visionscaper3:38629:38634 [0] NCCL INFO rocm_smi_lib: version 6.0.0.0
deep-visionscaper3:38629:38635 [1] NCCL INFO rocm_smi_lib: version 6.0.0.0
deep-visionscaper3:38629:38634 [0] NCCL INFO Setting affinity for GPU 1 to ffffffff,ffffffff
deep-visionscaper3:38629:38635 [1] NCCL INFO Setting affinity for GPU 0 to ffffffff,ffffffff
deep-visionscaper3:38629:38635 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0 [2] -1/-1/-1->1->0 [3] -1/-1/-1->1->0 comm 0x121b210 nRanks 02 busId 3000
deep-visionscaper3:38629:38635 [1] NCCL INFO P2P Chunksize set to 131072
deep-visionscaper3:38629:38634 [0] NCCL INFO Channel 00/04 :    0   1
deep-visionscaper3:38629:38634 [0] NCCL INFO Channel 01/04 :    0   1
deep-visionscaper3:38629:38634 [0] NCCL INFO Channel 02/04 :    0   1
deep-visionscaper3:38629:38634 [0] NCCL INFO Channel 03/04 :    0   1
deep-visionscaper3:38629:38634 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1 [2] 1/-1/-1->0->-1 [3] 1/-1/-1->0->-1 comm 0x15cd470 nRanks 02 busId 2f000
deep-visionscaper3:38629:38634 [0] NCCL INFO P2P Chunksize set to 131072
```

This shows:
```
NCCL INFO NET/Plugin : Plugin load (librccl-net.so) returned 2 : librccl-net.so: cannot open shared object file: No such file or directory
```
I checked, but I don't have `librccl-net.so` on my machine:
```
$ sudo find / -type f -name *librccl*
/home/freddy/.virtualenvs/imagenet/lib/python3.10/site-packages/torch/lib/librccl.so
/home/freddy/.virtualenvs/mlpug/lib/python3.10/site-packages/torch/lib/librccl.so
/opt/rocm-6.0.2/lib/librccl.so.1.0.60002
```
How to install `librccl-net.so`, and why wasn't this installed with `rccl`? Or is this not the issue?

### gilbertlee-amd · 2024-04-01

librccl-net.so is an optional plugin for handling network transports that aren't natively supported (IB/sockets), such as libFabric.  It's not really an issue in this case.

This is likely due to trying to use P2P communication on machines with PCIe-connected GPUs.  Could you try the test again with HSA_FORCE_FINE_GRAIN_PCIE=1?


### wenkaidu · 2024-04-01

Can you check if you have large bar enabled in your system?
lspci -vv -d:738c

We expect 64-bit region 0, i.e.
Region 0: Memory at 3f800000000 (64-bit, prefetchable) [size=32G]

### visionscaper · 2024-04-01

> librccl-net.so is an optional plugin for handling network transports that aren't natively supported (IB/sockets), such as libFabric. It's not really an issue in this case.
> 
> This is likely due to trying to use P2P communication on machines with PCIe-connected GPUs. Could you try the test again with HSA_FORCE_FINE_GRAIN_PCIE=1?

Hi @gilbertlee-amd,  `HSA_FORCE_FINE_GRAIN_PCIE=1` doesn't work: the test is blocked.

### visionscaper · 2024-04-01





> Can you check if you have large bar enabled in your system? lspci -vv -d:738c
> 
> We expect 64-bit region 0, i.e. Region 0: Memory at 3f800000000 (64-bit, prefetchable) [size=32G]

Hi @wenkaidu, yes I think it is a 64-bit region:
```
$ lspci -vv -d:738c
03:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Arcturus GL-XL [Instinct MI100] (rev 01)
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Arcturus GL-XL [AMD Instinct MI100]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 555
	IOMMU group: 76
	Region 0: Memory at 11800000000 (64-bit, prefetchable) [size=32G]
	Region 2: Memory at 12000000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at 1000 [size=256]
	Region 5: Memory at f3d00000 (32-bit, non-prefetchable) [size=512K]
	Expansion ROM at f3d80000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

2f:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Arcturus GL-XL [Instinct MI100] (rev 01)
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Arcturus GL-XL [AMD Instinct MI100]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 553
	IOMMU group: 56
	Region 0: Memory at 10800000000 (64-bit, prefetchable) [size=32G]
	Region 2: Memory at 11000000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at 4000 [size=256]
	Region 5: Memory at f1000000 (32-bit, non-prefetchable) [size=512K]
	Expansion ROM at f1080000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
``` 

### wenkaidu · 2024-04-01

Can you try adding "iommu=pt" to remove this warning?
deep-visionscaper3:38629:38629 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:132 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!


### visionscaper · 2024-04-01

Hi @wenkaidu, in `/etc/default/grub`, I added `iommu=pt` to `GRUB_CMDLINE_LINUX_DEFAULT` and finished with `sudo update-grub`. After reboot, I can see that is added:
```
$ cat /proc/cmdline
BOOT_IMAGE=/vmlinuz-5.15.0-101-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro iommu=pt
```
Now, the RCCL test works!
```
$ ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2
# nThread 1 nGpus 2 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version develop:3f7f785
# Using devices
#   Rank  0 Pid   2303 on deep-visionscaper3 device  0 [0000:2f:00.0] AMD Instinct MI100
#   Rank  1 Pid   2303 on deep-visionscaper3 device  1 [0000:03:00.0] AMD Instinct MI100
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
           8             2     float     sum      -1    13.10    0.00    0.00      0    13.92    0.00    0.00      0
          16             4     float     sum      -1    13.46    0.00    0.00      0    13.64    0.00    0.00      0
          32             8     float     sum      -1    13.00    0.00    0.00      0    11.62    0.00    0.00      0
          64            16     float     sum      -1    12.11    0.01    0.01      0    12.17    0.01    0.01      0
         128            32     float     sum      -1    12.34    0.01    0.01      0    12.33    0.01    0.01      0
         256            64     float     sum      -1    12.07    0.02    0.02      0    12.14    0.02    0.02      0
         512           128     float     sum      -1    12.39    0.04    0.04      0    12.53    0.04    0.04      0
        1024           256     float     sum      -1    12.71    0.08    0.08      0    12.67    0.08    0.08      0
        2048           512     float     sum      -1    12.90    0.16    0.16      0    13.31    0.15    0.15      0
        4096          1024     float     sum      -1    13.21    0.31    0.31      0    13.53    0.30    0.30      0
        8192          2048     float     sum      -1    13.20    0.62    0.62      0    13.49    0.61    0.61      0
       16384          4096     float     sum      -1    25.15    0.65    0.65      0    24.78    0.66    0.66      0
       32768          8192     float     sum      -1    23.85    1.37    1.37      0    22.74    1.44    1.44      0
       65536         16384     float     sum      -1    22.78    2.88    2.88      0    23.14    2.83    2.83      0
      131072         32768     float     sum      -1    25.36    5.17    5.17      0    25.38    5.16    5.16      0
      262144         65536     float     sum      -1    31.88    8.22    8.22      0    31.49    8.32    8.32      0
      524288        131072     float     sum      -1    44.32   11.83   11.83      0    44.44   11.80   11.80      0
     1048576        262144     float     sum      -1    65.88   15.92   15.92      0    66.30   15.82   15.82      0
     2097152        524288     float     sum      -1    109.2   19.20   19.20      0    109.0   19.23   19.23      0
     4194304       1048576     float     sum      -1    198.9   21.09   21.09      0    198.7   21.11   21.11      0
     8388608       2097152     float     sum      -1    376.0   22.31   22.31      0    389.9   21.51   21.51      0
    16777216       4194304     float     sum      -1    736.6   22.78   22.78      0    743.3   22.57   22.57      0
    33554432       8388608     float     sum      -1   1458.0   23.01   23.01      0   1458.3   23.01   23.01      0
    67108864      16777216     float     sum      -1   2904.3   23.11   23.11      0   2911.0   23.05   23.05      0
   134217728      33554432     float     sum      -1   5749.8   23.34   23.34      0   5762.7   23.29   23.29      0
# Errors with asterisks indicate errors that have exceeded the maximum threshold.
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 8.06342 
#
```
Not sure if this is related but the bandwidth is also much higher (see previous results)...

I also checked my PyTorch training scripts, and it works now, without adding `NCCL_P2P_DISABLE=1`!

So, why does this work, what is the "pt" value and what does `"iommu=pt"` do?

### wenkaidu · 2024-04-01

I am glad to hear the issue has been fixed!
IOMMU needs to be disabled or put into "pass through" mode due to driver limitation. Please see: https://community.amd.com/t5/knowledge-base/iommu-advisory-for-multi-gpu-environments/ta-p/477468

### visionscaper · 2024-04-01

PS: Is this something that needs to be added to the ROCm documentation? Or is this something very specific to my system? Do others not need to add this kernel boot command line parameters?

### visionscaper · 2024-04-01

> I am glad to hear the issue has been fixed! IOMMU needs to be disabled or put into "pass through" mode due to driver limitation. Please see: https://community.amd.com/t5/knowledge-base/iommu-advisory-for-multi-gpu-environments/ta-p/477468

@wenkaidu, all, thanks for your help!

I see in the link above that `amd_iommu=on` also needs to be added, I don't have it right now, should I add it?

### wenkaidu · 2024-04-01

Yes, IOMMU setting is applicable to all systems. I agree this needs to be clearly called out in ROCm documentation.
amd_iommu=on is applicable only for systems with AMD CPUs. But I found it to be "optional" on systems with AMD CPUs.

### visionscaper · 2024-04-01

I have some more feedback about the documentation, maybe you can relay this?

This week I have been building this custom server, with AMD Ryzen Threadripper PRO 5975WX and two AMD MI100 GPUs (will be extended to 6x MI100 in the next week). I expected it to be harder to setup the AMD GPUs on Ubuntu 22.04 for training with PyTorch, so that's a good sign. However, I had the following issues related to documentation:

- The [quick start guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html) misses the part about [registering the repositories](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/native-install/ubuntu.html#registering-repositories) to install the kernel-driver and ROCm packages.

   I understand you want the quick install guide to be simple, but a remark that states that you might need to register the package repositories first could save users a lot of time.

- As a last step of the quick start guide, a link to what to add for a multi-gpu environments, as given in this thread, would also be helpful.

 - With respect to using ROCm with PyTorch, when installing the PyTorch pre-build wheels as given on the PyTorch site, the ROCm documentation should state that ROCm 6.0 is only available through PyTorch nightly, i.e.:
   ```
   pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.0
   ```
   When installing ROCm, through the quick install guide, currently ROCm 6.02 is installed, so the documentation should reflect that in the PyTorch installation section.
 

### wenkaidu · 2024-04-01

Thanks for the feedback. Will do!

### ghost · 2024-04-20

Can confirm this problem exists in ROCm 5.6.1 as well within a VM running Ubuntu 22.04.4.

### wenkaidu · 2024-04-22

@Trat8547 Can you please try ROCm 6.1 which has recently been released?

### ghost · 2024-05-17

> @Trat8547 Can you please try ROCm 6.1 which has recently been released?

Sorry for the late response. The 100% GPU stall issue still persists in both ROCm 6.1 and 6.1.1 with both 5.19 and 6.5. iommu=pt doesn't seem to have any effect and the GPU_MAX_HW_QUEUES=1 trick also doesn't help.

I'm running with xen virtualization with the following kernel parameter set: 

GRUB_CMDLINE_XEN_DEFAULT="iommu=1,pass-through"

Just to be thorough I've also set GRUB_CMDLINE_LINUX="iommu=pt" but this also doesn't fix the stall issue.

### wenkaidu · 2024-05-17

I think there should be no iommu setting for kernel running inside VM. Can you try removing that? Also what happens if testing under BM. Does it also hang?
