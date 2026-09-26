# [Issue #17] [Issue]:  AMDSMI_STATUS_NOT_SUPPORTED - Feature not supported

source: https://github.com/ROCm/amdsmi/issues/17
state: closed | updated: 2025-06-05T20:21:27Z
labels: Under Investigation, Feature Request

## 正文

### Problem Description

When I try to use rocm-smi or amd-smi to set fan speed, I find that only 6700XT successfully but 7900XTX failed.
And rocm-smi command returns this:

![image](https://github.com/ROCm/amdsmi/assets/69568351/f26aaeda-a3f7-4278-b779-3497ddfa8d7b)

It cannot display the marketing name of 7900XTX

OS:
NAME="Ubuntu"
VERSION="22.04.4 LTS (Jammy Jellyfish)"

CPU: 
model name      : Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz

GPU:
  Name:                    Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz
  Marketing Name:          Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz
  Name:                    gfx1100                            
  Marketing Name:                                             
      Name:                    amdgcn-amd-amdhsa--gfx1100         
  Name:                    gfx1100                            
  Marketing Name:          AMD Radeon RX 6700 XT              
      Name:                    amdgcn-amd-amdhsa--gfx1030

(base) loong@ubuntu-server-220403:~/Codes/CV$ sudo amd-smi set -g 0 -f 80%

            ******WARNING******

            Operating your AMD GPU outside of official AMD specifications or outside of
            factory settings, including but not limited to the conducting of overclocking,
            over-volting or under-volting (including use of this interface software,
            even if such software has been directly or indirectly provided by AMD or otherwise
            affiliated in any way with AMD), may cause damage to your AMD GPU, system components
            and/or result in system failure, as well as cause other problems.
            DAMAGES CAUSED BY USE OF YOUR AMD GPU OUTSIDE OF OFFICIAL AMD SPECIFICATIONS OR
            OUTSIDE OF FACTORY SETTINGS ARE NOT COVERED UNDER ANY AMD PRODUCT WARRANTY AND
            MAY NOT BE COVERED BY YOUR BOARD OR SYSTEM MANUFACTURER'S WARRANTY.
            Please use this utility with caution.
            
Do you accept these terms? [y/n] y
amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
        2 | AMDSMI_STATUS_NOT_SUPPORTED - Feature not supported

The above exception was the direct cause of the following exception:

ValueError: Unable to set fan speed 204 on GPU ID: 0 BDF:0000:03:00.0
(base) loong@ubuntu-server-220403:~/Codes/CV$ sudo amd-smi set -g 1 -f 80%

            ******WARNING******

            Operating your AMD GPU outside of official AMD specifications or outside of
            factory settings, including but not limited to the conducting of overclocking,
            over-volting or under-volting (including use of this interface software,
            even if such software has been directly or indirectly provided by AMD or otherwise
            affiliated in any way with AMD), may cause damage to your AMD GPU, system components
            and/or result in system failure, as well as cause other problems.
            DAMAGES CAUSED BY USE OF YOUR AMD GPU OUTSIDE OF OFFICIAL AMD SPECIFICATIONS OR
            OUTSIDE OF FACTORY SETTINGS ARE NOT COVERED UNDER ANY AMD PRODUCT WARRANTY AND
            MAY NOT BE COVERED BY YOUR BOARD OR SYSTEM MANUFACTURER'S WARRANTY.
            Please use this utility with caution.
            
Do you accept these terms? [y/n] y
GPU: 1
FAN: Successfully set fan speed 204

### Operating System

Ubuntu 22.04.4 LTS (Jammy Jellyfish)

### CPU

Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.0.0

### ROCm Component

amdsmi, rocm_smi_lib

### Steps to Reproduce

(base) loong@ubuntu-server-220403:~/Codes/CV$ sudo amd-smi set -g 0 -f 80%

            ******WARNING******

            Operating your AMD GPU outside of official AMD specifications or outside of
            factory settings, including but not limited to the conducting of overclocking,
            over-volting or under-volting (including use of this interface software,
            even if such software has been directly or indirectly provided by AMD or otherwise
            affiliated in any way with AMD), may cause damage to your AMD GPU, system components
            and/or result in system failure, as well as cause other problems.
            DAMAGES CAUSED BY USE OF YOUR AMD GPU OUTSIDE OF OFFICIAL AMD SPECIFICATIONS OR
            OUTSIDE OF FACTORY SETTINGS ARE NOT COVERED UNDER ANY AMD PRODUCT WARRANTY AND
            MAY NOT BE COVERED BY YOUR BOARD OR SYSTEM MANUFACTURER'S WARRANTY.
            Please use this utility with caution.
            
Do you accept these terms? [y/n] y
amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
        2 | AMDSMI_STATUS_NOT_SUPPORTED - Feature not supported

The above exception was the direct cause of the following exception:

ValueError: Unable to set fan speed 204 on GPU ID: 0 BDF:0000:03:00.0
(base) loong@ubuntu-server-220403:~/Codes/CV$ sudo amd-smi set -g 1 -f 80%

            ******WARNING******

            Operating your AMD GPU outside of official AMD specifications or outside of
            factory settings, including but not limited to the conducting of overclocking,
            over-volting or under-volting (including use of this interface software,
            even if such software has been directly or indirectly provided by AMD or otherwise
            affiliated in any way with AMD), may cause damage to your AMD GPU, system components
            and/or result in system failure, as well as cause other problems.
            DAMAGES CAUSED BY USE OF YOUR AMD GPU OUTSIDE OF OFFICIAL AMD SPECIFICATIONS OR
            OUTSIDE OF FACTORY SETTINGS ARE NOT COVERED UNDER ANY AMD PRODUCT WARRANTY AND
            MAY NOT BE COVERED BY YOUR BOARD OR SYSTEM MANUFACTURER'S WARRANTY.
            Please use this utility with caution.
            
Do you accept these terms? [y/n] y
GPU: 1
FAN: Successfully set fan speed 204

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
  Name:                    Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz
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
  Max Clock Freq. (MHz):   4700                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    65775456(0x3eba760) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65775456(0x3eba760) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65775456(0x3eba760) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-85631fd855c9cea1               
  Marketing Name:                                             
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
  BDFID:                   768                                
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
*******                  
Agent 3                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 6700 XT              
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
    L2:                      3072(0xc00) KB                     
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29663(0x73df)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2855                               
  BDFID:                   2304                               
  Internal Node ID:        2                                  
  Compute Unit:            40                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
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
  Packet Processor uCode:: 116                                
  SDMA engine uCode::      80                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    12566528(0xbfc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    12566528(0xbfc000) KB              
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

## 评论 (14)

### Looong01 · 2024-04-28

I try to reinstall all the Ubuntu system and amdgpu driver and ROCm. It still does NOT work.
```
$ sudo amd-smi set -f 100% -g 0

            ******WARNING******

            Operating your AMD GPU outside of official AMD specifications or outside of
            factory settings, including but not limited to the conducting of overclocking,
            over-volting or under-volting (including use of this interface software,
            even if such software has been directly or indirectly provided by AMD or otherwise
            affiliated in any way with AMD), may cause damage to your AMD GPU, system components
            and/or result in system failure, as well as cause other problems.
            DAMAGES CAUSED BY USE OF YOUR AMD GPU OUTSIDE OF OFFICIAL AMD SPECIFICATIONS OR
            OUTSIDE OF FACTORY SETTINGS ARE NOT COVERED UNDER ANY AMD PRODUCT WARRANTY AND
            MAY NOT BE COVERED BY YOUR BOARD OR SYSTEM MANUFACTURER'S WARRANTY.
            Please use this utility with caution.

Do you accept these terms? [y/n] y
amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
        2 | AMDSMI_STATUS_NOT_SUPPORTED - Feature not supported

The above exception was the direct cause of the following exception:

ValueError: Unable to set fan speed 255 on GPU ID: 0 BDF:0000:03:00.0
```
and
```
$ rocm-smi


==================================== ROCm System Management Interface ====================================
============================================== Concise Info ==============================================
Device  [Model : Revision]    Temp    Power  Partitions      SCLK  MCLK   Fan  Perf  PwrCap  VRAM%  GPU%
        Name (20 chars)       (Edge)  (Avg)  (Mem, Compute)
==========================================================================================================
0       [0x7901 : 0xc8]       30.0°C  10.0W  N/A, N/A        0Mhz  96Mhz  0%   auto  327.0W    0%   0%
        0x744c
==========================================================================================================
========================================== End of ROCm SMI Log ===========================================
```

### marifamd · 2024-05-01

@Looong01 I'm not seeing this issue on the version released with ROCm version 6.1.0, can you update to the latest ROCm and see if you can reproduce? Also can you run it with debug logging?
```shell
sudo amd-smi set -f 100% -g 0 --loglevel debug
``` 


### Looong01 · 2024-05-01

> @Looong01 I'm not seeing this issue on the version released with ROCm version 6.1.0, can you update to the latest ROCm and see if you can reproduce? Also can you run it with debug logging?
> 
> ```shell
> sudo amd-smi set -f 100% -g 0 --loglevel debug
> ```

```
$ sudo amd-smi set -f 100% -g 0 --loglevel debug

            ******WARNING******

            Operating your AMD GPU outside of official AMD specifications or outside of
            factory settings, including but not limited to the conducting of overclocking,
            over-volting or under-volting (including use of this interface software,
            even if such software has been directly or indirectly provided by AMD or otherwise
            affiliated in any way with AMD), may cause damage to your AMD GPU, system components
            and/or result in system failure, as well as cause other problems.
            DAMAGES CAUSED BY USE OF YOUR AMD GPU OUTSIDE OF OFFICIAL AMD SPECIFICATIONS OR
            OUTSIDE OF FACTORY SETTINGS ARE NOT COVERED UNDER ANY AMD PRODUCT WARRANTY AND
            MAY NOT BE COVERED BY YOUR BOARD OR SYSTEM MANUFACTURER'S WARRANTY.
            Please use this utility with caution.

Do you accept these terms? [y/n] y
Traceback (most recent call last):
  File "/opt/rocm-6.1.0/libexec/amdsmi_cli/amdsmi_commands.py", line 3190, in set_gpu
    amdsmi_interface.amdsmi_set_gpu_fan_speed(args.gpu, 0, args.fan)
  File "/usr/local/lib/python3.10/dist-packages/amdsmi/amdsmi_interface.py", line 2652, in amdsmi_set_gpu_fan_speed
    _check_res(
  File "/usr/local/lib/python3.10/dist-packages/amdsmi/amdsmi_interface.py", line 504, in _check_res
    raise AmdSmiLibraryException(ret_code)
amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
        2 | AMDSMI_STATUS_NOT_SUPPORTED - Feature not supported

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/bin/amd-smi", line 109, in <module>
    args.func(args)
  File "/opt/rocm-6.1.0/libexec/amdsmi_cli/amdsmi_commands.py", line 3413, in set_value
    self.set_gpu(args, multiple_devices, gpu, fan, perf_level,
  File "/opt/rocm-6.1.0/libexec/amdsmi_cli/amdsmi_commands.py", line 3194, in set_gpu
    raise ValueError(f"Unable to set fan speed {args.fan} on {gpu_string}") from e
ValueError: Unable to set fan speed 255 on GPU ID: 0 BDF:0000:03:00.0
```

### tcgu-amd · 2024-10-29

Hi @Looong01, sorry for the lack of response. Are you still experiencing the same issue on the latest version of ROCm and driver? Something seems to be wrong with the driver. I would try a couple of things:

1. Make sure that the Intel iGPU is disabled from the BIOS.
2. Try swapping the two GPU's slots and see if the issue still persists on the 7900XTX
3. Try leaving only the 7900XTX plugged in, try each slot on the motherboard. 
4. Check dmesg and paste any amdgpu logs here.

Thanks!

### tcgu-amd · 2024-11-11

This issue will be closed for now due to inactivity. Please feel free to reopen for follow up. Thanks!

### Looong01 · 2024-11-25

> Hi @Looong01, sorry for the lack of response. Are you still experiencing the same issue on the latest version of ROCm and driver? Something seems to be wrong with the driver. I would try a couple of things:
> 
> 1. Make sure that the Intel iGPU is disabled from the BIOS.
> 2. Try swapping the two GPU's slots and see if the issue still persists on the 7900XTX
> 3. Try leaving only the 7900XTX plugged in, try each slot on the motherboard.
> 4. Check dmesg and paste any amdgpu logs here.
> 
> Thanks!

Hii, I did 1, 2 and 3, but no one helps. So I paste the dmesg here:
```
[141478.624436] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:408c:4ec7:613c:0000:0000:7b48:bd0a DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=43 FLOWLBL=918171 PROTO=UDP SPT=43971 DPT=51413 LEN=112
[141845.987412] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=33164 DF PROTO=UDP SPT=40126 DPT=51413 LEN=100
[141937.039303] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=89.22.198.73 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=7422 PROTO=UDP SPT=45051 DPT=51413 LEN=112
[142129.047585] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=78.128.114.62 DST=192.168.3.19 LEN=40 TOS=0x00 PREC=0x00 TTL=243 ID=3393 PROTO=TCP SPT=41030 DPT=7890 WINDOW=1024 RES=0x00 SYN URGP=0
[142634.079697] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=47.9.115.154 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=36 ID=0 PROTO=UDP SPT=44099 DPT=51413 LEN=112
[142787.846020] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0e0a:09a7:72a0:d1e0:de32:b067:f709 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=987266 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[142808.346736] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=63514 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[142835.809408] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=9754 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[142862.820540] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=26426 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[142873.784876] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0861:4744:5200:8471:b340:9744:7519 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=81633 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[142922.758712] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=59469 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[143170.707489] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a00:1858:1047:853d:f201:67ab:2e56:7085 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=566293 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[143203.460741] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2600:6c5a:7004:0200:8d2c:312d:62ce:5240 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=107 FLOWLBL=823722 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[143229.232343] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=47.9.115.154 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=36 ID=0 PROTO=UDP SPT=44099 DPT=51413 LEN=112
[143266.625582] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0e11:300c:c400:a8e5:5aff:fe94:7e40 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=688117 PROTO=UDP SPT=55250 DPT=51413 LEN=112
[143439.121265] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:8086:0d0a:9a80:ffc6:bbdf:8b68:5121 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=53 FLOWLBL=308885 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[143690.636212] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=15450 DF PROTO=UDP SPT=40066 DPT=51413 LEN=100
[144198.015566] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=14638 DF PROTO=UDP SPT=40089 DPT=51413 LEN=100
[144300.817147] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2600:6c5a:7004:0200:8d2c:312d:62ce:5240 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=107 FLOWLBL=711852 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[144762.613526] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0e0a:0a4d:f780:265e:beff:fe23:f0cb DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=46 FLOWLBL=17280 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[145102.915306] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:056c:d7d8:6b00:acdf:4e30:06b3:7648 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=216717 PROTO=UDP SPT=45958 DPT=51413 LEN=112
[145153.067648] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=26311 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145173.934153] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2600:100e:a022:133d:4886:eaff:fea8:2684 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=926016 PROTO=UDP SPT=57008 DPT=51413 LEN=112
[145185.292736] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=8834 DF PROTO=UDP SPT=40089 DPT=51413 LEN=100
[145228.782492] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=61716 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145279.937697] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=25861 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145299.534928] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=36231 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145310.712334] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=42628 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145330.561372] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=56047 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145350.182335] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=63881 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145361.322592] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=700 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145381.193042] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=11740 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145400.807394] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=21970 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145411.903765] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=27228 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145431.921434] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=37851 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145451.851584] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=45205 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145471.753388] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=54602 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145482.458518] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=60552 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145492.733516] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=64535 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145530.601333] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=17947 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145557.234641] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=32034 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145577.540656] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=39363 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145635.031189] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=3392 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145692.538117] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=36140 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[145827.599141] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:6f38:c03e:f700:30a9:93f4:f722:2c0a DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=538825 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[145895.400210] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18167 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145910.244751] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18168 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145911.224877] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18169 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145911.228058] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18170 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145911.242707] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18171 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145911.242986] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18172 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145916.825682] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=155.93.168.203 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=42171 PROTO=UDP SPT=34626 DPT=51413 LEN=111
[145921.245295] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18173 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145922.246924] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18174 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145922.247647] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18175 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145922.247954] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=18176 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[145981.297786] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.252.60.130 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=113 ID=4966 PROTO=UDP SPT=3221 DPT=51413 LEN=112
[146004.634411] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a00:23a8:4bc4:5801:af2f:fb28:a73b:9c8d DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=225837 PROTO=UDP SPT=1180 DPT=51413 LEN=112
[146025.741899] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=59238 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[146956.462975] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:2f00:4302:5d00:08c9:62a6:6886:a2b8 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=788480 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[147195.053972] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2600:6c5a:7004:0200:8d2c:312d:62ce:5240 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=107 FLOWLBL=347634 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[147818.268256] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=24218 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[147821.341330] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=24219 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[147822.185903] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=24220 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[147824.315062] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:a31a:a2c0:1980:58ed:3ddd:7043:d8c6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=1046684 PROTO=UDP SPT=48812 DPT=51413 LEN=112
[147835.834683] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0e0a:0b1d:3e20:00f1:c4fa:6d6d:07a8 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=48 FLOWLBL=381873 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[148542.684157] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:13d8:41a2:1700:1539:3aa4:152b:0d2c DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=32 HOPLIMIT=46 FLOWLBL=866642 PROTO=UDP SPT=56815 DPT=51413 LEN=112
[148803.315454] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0e0a:05bb:7390:42b0:76ff:fea3:be27 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=97 TC=0 HOPLIMIT=49 FLOWLBL=249241 PROTO=UDP SPT=50000 DPT=51413 LEN=57
[149107.463754] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2800:0098:1628:042e:c08b:beb0:261b:7987 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=751827 PROTO=UDP SPT=41061 DPT=51413 LEN=112
[149175.468504] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=48649 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149196.119826] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=59763 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149225.687318] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=14453 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149236.808477] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=17618 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149256.472476] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=26358 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149276.468801] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=37745 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149287.434588] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=41841 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149296.332393] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2600:0380:6b3b:c19c:d74f:04de:26f7:b1c4 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=8 HOPLIMIT=237 FLOWLBL=872230 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[149307.497953] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=51890 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149312.664783] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:820c:8f0b:0381:0000:0000:0000:0a15 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=4 HOPLIMIT=56 FLOWLBL=712908 PROTO=UDP SPT=60001 DPT=51413 LEN=112
[149327.456098] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=63554 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149338.305526] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=5950 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149358.306003] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=17890 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149378.250821] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=30689 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149389.291166] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=35504 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149409.169642] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=44965 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149429.188250] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=58042 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149440.114674] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=63462 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149460.144588] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=11730 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149490.020842] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=23847 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149520.759049] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=36096 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149567.196870] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=57931 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[149693.633271] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=222.99.106.136 DST=192.168.3.19 LEN=143 TOS=0x00 PREC=0x00 TTL=114 ID=59079 PROTO=UDP SPT=7683 DPT=51413 LEN=123
[149900.135103] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:408c:4ec7:613c:0000:0000:7b48:bd0a DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=43 FLOWLBL=918171 PROTO=UDP SPT=43971 DPT=51413 LEN=112
[149987.971564] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:1308:1c1d:e800:a656:4d64:c4cc:e597 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=274247 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[150085.808801] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=18619 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150085.979663] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=18620 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150095.818030] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20928 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150095.818201] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20929 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150095.818422] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20930 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150095.818613] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20931 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150095.818805] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20934 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150095.818998] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20932 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150095.819400] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20935 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150095.819554] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20933 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150116.415724] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=21502 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150137.023467] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=24325 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150147.396731] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=25088 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150168.726871] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27482 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150190.255818] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=28615 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150212.489105] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=30308 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150233.516726] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=32188 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150251.902993] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=34366 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150273.869299] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=35701 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150286.041677] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=37509 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150315.076183] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=39005 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150337.627483] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=41027 DF PROTO=UDP SPT=52292 DPT=51413 LEN=111
[150964.259962] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2600:100e:a022:133d:4886:eaff:fea8:2684 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=926016 PROTO=UDP SPT=57008 DPT=51413 LEN=112
[151079.365002] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2600:100e:a022:133d:4886:eaff:fea8:2684 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=926016 PROTO=UDP SPT=57008 DPT=51413 LEN=112
[151110.879885] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a00:23c7:ae19:8d01:75c6:1886:7d31:1079 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=314443 PROTO=UDP SPT=62865 DPT=51413 LEN=112
[151627.859654] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=58.23.160.133 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=56 ID=56181 DF PROTO=UDP SPT=13348 DPT=51413 LEN=66
[151713.331760] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.24.52.223 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=112 ID=12714 PROTO=UDP SPT=51905 DPT=51413 LEN=111
[151719.311637] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=58.23.160.133 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=56 ID=4337 DF PROTO=UDP SPT=13348 DPT=51413 LEN=66
[151754.534124] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=58.23.160.133 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=56 ID=9822 DF PROTO=UDP SPT=13348 DPT=51413 LEN=66
[151765.336159] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.24.52.223 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=112 ID=12715 PROTO=UDP SPT=51905 DPT=51413 LEN=111
[151894.846867] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=200.111.153.195 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=109 ID=13545 PROTO=UDP SPT=10756 DPT=51413 LEN=131
[152009.079169] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=31.126.149.202 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=48476 DF PROTO=UDP SPT=44492 DPT=51413 LEN=112
[152266.503528] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0e68:5431:15f7:c803:8cfc:9395:f66f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=119 TC=0 HOPLIMIT=240 FLOWLBL=1038523 PROTO=UDP SPT=17768 DPT=51413 LEN=79
[152295.391101] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=47.9.115.154 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=36 ID=0 PROTO=UDP SPT=44099 DPT=51413 LEN=112
[152837.975417] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=26986 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[153220.160916] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8210:603c:b652:0000:0000:0000:0020 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=113 TC=192 HOPLIMIT=58 FLOWLBL=915025 PROTO=UDP SPT=54812 DPT=51413 LEN=73
[153845.254278] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=41478 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153856.002681] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=46239 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153866.466777] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=51034 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153876.911042] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=55908 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153887.214922] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=60664 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153897.572768] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=1844 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153908.006983] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=6020 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153918.659655] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=13780 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153919.007245] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=50 ID=13877 DF PROTO=UDP SPT=56035 DPT=51413 LEN=149
[153956.708745] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=32001 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153967.457317] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=37056 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153977.900536] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=43252 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153988.221624] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=48993 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[153998.591444] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=53336 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154008.906600] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=58962 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154019.283175] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=65152 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154029.716953] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=3286 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154037.215229] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=16207 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[154040.029393] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=10312 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154050.605053] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=14040 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154071.393712] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=23137 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154090.817692] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=37412 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154114.497066] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=48148 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154127.426047] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=5082 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[154157.095441] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=1833 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154165.689120] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2800:0200:f290:0918:1caa:2efa:6449:1e08 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=285089 PROTO=UDP SPT=53670 DPT=51413 LEN=112
[154167.722715] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=7175 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154188.927015] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=20832 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154222.230610] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=38181 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154277.205585] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0620:22f8:6500:f5fb:d751:a666:de87 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=0 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[154279.414092] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=1008 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154307.459392] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=14200 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154316.577238] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=10119 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[154334.354401] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=27807 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154363.512508] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=46228 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154378.025208] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=39502 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[154476.685474] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=28132 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[154479.951812] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=43215 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154495.250594] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=183.236.237.89 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=52 ID=38445 DF PROTO=UDP SPT=51413 DPT=51413 LEN=66
[154527.172284] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53258 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[154565.534890] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=183.236.237.89 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=52 ID=39408 DF PROTO=UDP SPT=51413 DPT=51413 LEN=66
[154567.687852] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=11362 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154662.367266] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=183.236.237.89 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=52 ID=45035 DF PROTO=UDP SPT=51413 DPT=51413 LEN=66
[154686.006298] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=10342 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[154818.511626] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2607:fea8:935a:52a0:0000:0000:0000:e772 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=132285 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[155605.131516] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:0305:5983:cf90:21ac:6a59:3f81:9a2f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=53 FLOWLBL=0 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[155661.155429] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:0305:5983:cf90:21ac:6a59:3f81:9a2f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=53 FLOWLBL=0 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[155666.502182] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:0305:5983:cf90:21ac:6a59:3f81:9a2f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=158 TC=0 HOPLIMIT=53 FLOWLBL=0 PROTO=UDP SPT=51413 DPT=51413 LEN=118
[155708.057602] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:0305:5983:cf90:21ac:6a59:3f81:9a2f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=158 TC=0 HOPLIMIT=53 FLOWLBL=0 PROTO=UDP SPT=51413 DPT=51413 LEN=118
[156702.031231] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50013 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156713.660928] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50014 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156713.663016] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50015 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156713.664384] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50016 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156713.665507] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50017 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156713.667309] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50018 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156713.667834] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50019 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156721.661200] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50020 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156726.660179] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50021 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156727.733776] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.24.116.223 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=28759 PROTO=UDP SPT=30744 DPT=51413 LEN=111
[156740.568341] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50022 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156755.095394] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50027 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156766.883418] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50030 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156782.080590] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=50033 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[156899.177032] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=79.124.56.102 DST=192.168.3.19 LEN=44 TOS=0x00 PREC=0x00 TTL=243 ID=20295 PROTO=TCP SPT=57597 DPT=7890 WINDOW=1025 RES=0x00 SYN URGP=0
[157490.691928] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a0e:041d:e05b:0000:c467:7aff:fe26:1ce8 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=80 HOPLIMIT=51 FLOWLBL=774430 PROTO=UDP SPT=55193 DPT=51413 LEN=112
[157536.852456] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=78.63.168.212 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=50 ID=40454 DF PROTO=UDP SPT=51767 DPT=51413 LEN=112
[157544.794714] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=55168 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[157588.584419] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=3488 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[157646.791018] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=30470 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[157692.885780] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=54099 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[157728.980320] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=10794 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[157809.690716] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=42165 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[157872.702225] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=8962 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[157898.404305] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=29449 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158051.394596] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=50910 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158148.882587] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=27499 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158149.254169] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2402:9d80:03e0:0ae8:8381:56a2:b6d8:87db DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=41 FLOWLBL=693027 PROTO=UDP SPT=48929 DPT=51413 LEN=112
[158201.595766] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:448a:6102:12f1:7c1b:3bff:fe3e:b9b5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=562341 PROTO=UDP SPT=52581 DPT=51413 LEN=112
[158301.614274] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=23713 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158373.613333] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.76.188.130 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=49703 DF PROTO=UDP SPT=6881 DPT=51413 LEN=112
[158418.437933] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=19868 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158429.114668] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=23918 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158512.927814] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:820c:8f0b:0381:0000:0000:0000:0a15 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=4 HOPLIMIT=56 FLOWLBL=712908 PROTO=UDP SPT=60001 DPT=51413 LEN=112
[158529.505522] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=9131 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158582.001936] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=42260 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158689.244684] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=27424 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158695.882124] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=183.98.204.247 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=115 ID=58369 PROTO=UDP SPT=28108 DPT=51413 LEN=111
[158790.196552] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=9271 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158824.517301] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=23558 DF PROTO=UDP SPT=40126 DPT=51413 LEN=100
[158830.812192] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=35982 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158898.210724] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53824 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[158978.752983] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=35655 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[159117.316713] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53251 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[159136.695027] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=517 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[159159.042840] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=9332 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[159176.883674] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=17950 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[159392.344757] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=78.63.168.212 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=50 ID=51515 DF PROTO=UDP SPT=51767 DPT=51413 LEN=112
[159461.530953] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0df7:2380:c9b2:f83a:2bff:fe3a:3de6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=758178 PROTO=UDP SPT=55074 DPT=51413 LEN=112
[159566.601463] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0df7:2380:c9b2:f83a:2bff:fe3a:3de6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=758178 PROTO=UDP SPT=55074 DPT=51413 LEN=112
[159609.857243] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0e68:5431:15f7:c803:8cfc:9395:f66f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=174 TC=0 HOPLIMIT=240 FLOWLBL=33325 PROTO=UDP SPT=17768 DPT=51413 LEN=134
[159808.830680] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=189.4.72.195 DST=192.168.3.19 LEN=327 TOS=0x00 PREC=0x00 TTL=47 ID=17180 DF PROTO=UDP SPT=16360 DPT=51413 LEN=307
[159913.769497] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.76.188.130 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=27058 DF PROTO=UDP SPT=6881 DPT=51413 LEN=112
[160203.220710] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=222.99.106.136 DST=192.168.3.19 LEN=143 TOS=0x00 PREC=0x00 TTL=114 ID=31208 PROTO=UDP SPT=7683 DPT=51413 LEN=123
[160686.879577] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.153.179.154 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=45 ID=15281 PROTO=UDP SPT=25611 DPT=51413 LEN=112
[160809.892776] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=89.134.6.73 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=44389 PROTO=UDP SPT=57205 DPT=51413 LEN=112
[160853.266646] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:22b8:4016:4b00:df59:982f:caa6:54e8 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=82675 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[161379.492204] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=50 ID=38525 DF PROTO=UDP SPT=56035 DPT=51413 LEN=149
[161406.207843] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=48592 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[161486.495754] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=21978 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[161517.155868] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=28979 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[161528.596915] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=34971 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[161716.497262] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=119 TOS=0x00 PREC=0x00 TTL=55 ID=46679 DF PROTO=UDP SPT=40070 DPT=51413 LEN=99
[162074.928111] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=73.233.32.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=110 ID=46 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[162173.157395] perf: interrupt took too long (3961 > 3947), lowering kernel.perf_event_max_sample_rate to 50250
[162256.395606] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2806:103e:0021:79a6:90df:253a:7546:60b2 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=51 FLOWLBL=0 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[163418.481089] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.76.188.130 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=33747 DF PROTO=UDP SPT=6881 DPT=51413 LEN=112
[163945.620508] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=21903 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164082.148082] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=5325 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164121.430609] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=20421 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164160.875314] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=39220 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164180.883344] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=52062 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164200.884008] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=61966 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164220.884226] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=3537 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164240.884587] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=16341 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164260.884579] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=27117 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164271.561363] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=35117 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164292.059256] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=47283 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164323.140423] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=61198 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164334.681503] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=1462 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164358.142883] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=6757 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164359.203721] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=9908 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164368.899650] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=10053 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164377.917844] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=16754 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164380.063048] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=16072 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164399.908894] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=16914 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164411.042360] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=25176 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164419.849946] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=38496 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164421.907245] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=32955 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164440.543940] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=49755 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164441.374779] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=42074 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164452.886942] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=46778 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164461.348023] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=64107 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164463.563090] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=51928 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164481.312153] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=8501 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164492.845720] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=61686 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164507.630228] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=20808 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164524.482872] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=27156 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164555.248344] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=45875 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164566.533720] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=53751 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164588.170705] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=36281 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[164607.553744] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=15194 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[164676.787898] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.76.188.130 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=62431 DF PROTO=UDP SPT=6881 DPT=51413 LEN=112
[165599.039248] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=78.63.168.212 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=50 ID=10374 DF PROTO=UDP SPT=51767 DPT=51413 LEN=112
[166263.175380] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=85.198.105.92 DST=192.168.3.19 LEN=125 TOS=0x00 PREC=0x00 TTL=44 ID=27209 DF PROTO=UDP SPT=2817 DPT=51413 LEN=105
[166263.975314] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=197.206.178.8 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=47 ID=38269 DF PROTO=UDP SPT=42429 DPT=51413 LEN=112
[166450.480796] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=63954 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[166477.792532] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=11442 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[166562.752584] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=57743 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[166627.774722] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=23581 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[166654.334310] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=30075 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[166676.212566] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=42940 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[166696.613339] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=53910 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[167521.785049] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=210.68.238.72 DST=192.168.3.19 LEN=126 TOS=0x00 PREC=0x00 TTL=115 ID=15161 PROTO=UDP SPT=12743 DPT=51413 LEN=106
[167605.876704] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=64256 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[167672.244382] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=34931 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[167786.722574] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=200.111.153.195 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=109 ID=5241 PROTO=UDP SPT=10756 DPT=51413 LEN=131
[167843.586541] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=59003 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[167858.721041] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=200.111.153.195 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=109 ID=5242 PROTO=UDP SPT=10756 DPT=51413 LEN=79
[167880.817683] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=12467 DF PROTO=UDP SPT=40070 DPT=51413 LEN=100
[168254.582430] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2600:100e:a022:133d:4886:eaff:fea8:2684 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=926016 PROTO=UDP SPT=57008 DPT=51413 LEN=112
[168254.829536] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2800:0810:0539:05f7:c5db:8fd0:cc83:9a24 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=866711 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[168283.147094] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=35547 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[168417.274485] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=35512 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[168907.447304] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=181.238.50.8 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=47 ID=58404 DF PROTO=UDP SPT=2323 DPT=51413 LEN=112

```

### Looong01 · 2024-11-25

```
[168955.122318] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2405:4803:d575:8670:8d38:e9b3:30fa:51da DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=42 FLOWLBL=51682 PROTO=UDP SPT=44640 DPT=51413 LEN=112
[169036.256703] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0e11:300c:c400:a8e5:5aff:fe94:7e40 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=688117 PROTO=UDP SPT=55250 DPT=51413 LEN=112
[169120.228205] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=22004 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169524.586188] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=64205 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169560.899933] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=11180 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169581.479256] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=22783 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169627.280031] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=36913 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169630.133718] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=202.130.217.5 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=38 ID=16435 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[169647.762666] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=46714 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169682.068728] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.252.60.130 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=113 ID=42125 PROTO=UDP SPT=4441 DPT=51413 LEN=111
[169684.030881] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=56981 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169740.534121] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=30779 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169776.465329] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=47507 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169843.704544] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=29858 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169889.816527] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=56192 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169921.681118] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=59584 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[169988.135944] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=42217 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[170085.762988] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=28361 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[170133.005088] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=35806 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[170270.332692] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2800:0810:0539:05f7:c5db:8fd0:cc83:9a24 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=759022 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[170410.510433] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2800:0810:0539:05f7:c5db:8fd0:cc83:9a24 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=992155 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[170551.698421] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=169.61.68.78 DST=192.168.3.19 LEN=121 TOS=0x00 PREC=0x00 TTL=47 ID=31349 DF PROTO=UDP SPT=6881 DPT=51413 LEN=101
[170584.800616] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=67.193.73.38 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=54269 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[170958.895226] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:0341:1708:d800:b1ed:3a05:8462:dab2 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=52 FLOWLBL=0 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[171020.707985] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:0341:1708:d800:b1ed:3a05:8462:dab2 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=52 FLOWLBL=0 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[171069.595289] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:0341:1708:d800:b1ed:3a05:8462:dab2 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=52 FLOWLBL=0 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[171353.576971] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0e0a:0310:0350:3923:1a4d:1651:4fa1 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=836894 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[171433.764636] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.76.188.130 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=44928 DF PROTO=UDP SPT=6881 DPT=51413 LEN=112
[171591.093695] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:4900:1cdc:52ec:b858:b3f6:ea6b:7f3b DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=50 FLOWLBL=663671 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[172547.221708] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:a31a:a2c0:1980:58ed:3ddd:7043:d8c6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=1046684 PROTO=UDP SPT=48812 DPT=51413 LEN=112
[172912.358625] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19536 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172925.634426] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19538 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172925.637578] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19540 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172925.638922] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19543 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172965.287593] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19546 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172973.233520] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19548 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172976.689963] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19549 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172976.707502] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19550 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172983.238360] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19551 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172983.283228] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19552 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172984.167273] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19553 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172984.236815] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19554 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[172990.703320] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19555 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[173001.392831] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19558 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[173049.403688] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19560 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[173050.806125] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19561 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[173053.945827] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=19562 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[173440.800788] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=67.193.73.38 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=54273 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[173717.852444] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:1308:282c:b200:d790:0daf:0a6f:c4b5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=724207 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[174060.314383] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=10216 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[174105.526748] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=33735 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[174117.551453] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40874 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174117.551615] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40875 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174117.552026] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40876 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174117.552223] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40877 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174117.552420] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40878 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174117.552573] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40879 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174117.552781] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40880 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174117.552937] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40881 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174117.553242] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40882 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174139.209750] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=45387 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174149.228939] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=47632 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174170.151660] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=48775 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174190.734074] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=50775 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174209.473208] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=13614 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[174233.655833] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57936 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174254.284546] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=62363 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174274.752681] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=347 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174286.185969] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=1170 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174306.151192] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=4530 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174326.779778] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=6054 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174347.448386] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=8085 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174368.375720] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=9327 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174388.703615] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10378 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174409.929826] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=14904 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174430.089569] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=16415 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[174483.025325] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=14124 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[174500.035807] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=19042 DF PROTO=UDP SPT=40070 DPT=51413 LEN=100
[174529.753360] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=40235 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[174534.311574] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014c:3b62:0024:d492:16b9:847e:f6db DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=669064 PROTO=UDP SPT=43185 DPT=51413 LEN=112
[174578.842627] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=61244 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[174608.139756] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=6754 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[175050.283460] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47627 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[175061.824331] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=94.154.187.178 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=109 ID=24750 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[175160.507145] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47629 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[175275.064157] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.252.60.130 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=113 ID=889 PROTO=UDP SPT=4441 DPT=51413 LEN=111
[175462.243046] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47632 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[175463.785234] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47633 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[175463.787525] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47634 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[175463.788015] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47635 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[175463.789031] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47636 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[175463.790504] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47637 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[175775.415604] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=51 ID=9410 DF PROTO=UDP SPT=56188 DPT=51413 LEN=149
[175801.264214] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=21885 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[175826.690783] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=35488 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[175863.613091] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=50538 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[175900.312375] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=511 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[175948.014442] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=29270 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[175983.305411] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=47889 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[176025.186754] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2400:4050:a9a2:ea00:1418:f1ff:fe1f:1873 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=361878 PROTO=UDP SPT=42591 DPT=51413 LEN=112
[176029.634312] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=5143 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[176055.808437] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=18942 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[176091.789711] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=36300 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[176139.603871] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=314 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[176342.481234] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=51511 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[176597.550461] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:6f38:c03e:f700:30a9:93f4:f722:2c0a DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=69425 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[176667.655025] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:6f38:c03e:f700:30a9:93f4:f722:2c0a DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=522565 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[176697.794110] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=171.126.163.231 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=120 ID=8737 PROTO=UDP SPT=40632 DPT=51413 LEN=112
[177605.892174] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=185.224.128.17 DST=192.168.3.19 LEN=40 TOS=0x00 PREC=0x00 TTL=242 ID=54321 PROTO=TCP SPT=41620 DPT=7890 WINDOW=65535 RES=0x00 SYN URGP=0
[178001.162740] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0df7:2380:c9b2:f83a:2bff:fe3a:3de6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=758178 PROTO=UDP SPT=55074 DPT=51413 LEN=112
[178010.908018] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2601:0204:c300:4030:610e:b712:08fd:0c69 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=44 FLOWLBL=977787 PROTO=UDP SPT=41416 DPT=51413 LEN=112
[178150.832640] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=67.193.73.38 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=56132 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[178173.588874] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:4900:1cdc:52ec:b858:b3f6:ea6b:7f3b DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=50 FLOWLBL=817510 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[178467.211296] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=63562 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[178468.227389] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=63563 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[178468.229841] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=63564 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[178468.231211] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=63565 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[178468.231703] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=63566 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[178576.226896] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=63567 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[179103.220043] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=11420 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[179173.678480] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=27448 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[179225.851238] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=6680 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[179266.969803] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=62939 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[179336.015765] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014c:3b62:0024:d492:16b9:847e:f6db DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=669064 PROTO=UDP SPT=43185 DPT=51413 LEN=112
[179340.775858] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=31820 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[179408.650704] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=88 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[179421.587387] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=181.66.157.24 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=109 ID=24806 PROTO=UDP SPT=48709 DPT=51413 LEN=112
[179464.693958] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014c:3b62:0024:d492:16b9:847e:f6db DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=669064 PROTO=UDP SPT=43185 DPT=51413 LEN=112
[179550.329669] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8210:603c:b652:0000:0000:0000:0020 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=192 HOPLIMIT=58 FLOWLBL=260440 PROTO=UDP SPT=54812 DPT=51413 LEN=112
[180443.633845] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=50 ID=23613 DF PROTO=UDP SPT=56035 DPT=51413 LEN=149
[180450.789110] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10594 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180450.789387] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10595 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180450.789680] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10596 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180450.789955] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10597 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180450.790279] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10598 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180450.790476] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10599 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180450.790673] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10600 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180450.790869] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10601 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180450.791030] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10602 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180479.490645] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=48052 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[180493.002616] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=17802 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180515.178566] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20433 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180524.782510] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=20489 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180546.014884] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=24774 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180569.766033] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=29422 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180586.737376] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=31948 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180611.333448] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=34559 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180626.769565] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=35905 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180649.700576] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=37393 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180664.901601] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40845 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180697.589322] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=46105 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180718.916245] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=48294 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180738.659086] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51570 DF PROTO=UDP SPT=50582 DPT=51413 LEN=111
[180748.589495] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=58431 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[180778.687018] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=12933 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[180803.261164] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=33942 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[181199.384960] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:2f00:4302:5d00:08c9:62a6:6886:a2b8 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=788480 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[181206.256731] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=46646 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[181263.261878] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=46647 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[181286.614730] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=200.111.153.195 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=109 ID=3057 PROTO=UDP SPT=10756 DPT=51413 LEN=79
[181446.032862] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:833c:1026:8f01:35b3:3ba1:4eba:c4ba DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=337547 PROTO=UDP SPT=37221 DPT=51413 LEN=112
[181484.222143] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:833c:1026:8f01:35b3:3ba1:4eba:c4ba DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=337547 PROTO=UDP SPT=37221 DPT=51413 LEN=112
[181524.596889] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:4900:7251:af87:0000:0000:0e2f:4172 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=32 HOPLIMIT=241 FLOWLBL=268565 PROTO=UDP SPT=43884 DPT=51413 LEN=112
[181608.852331] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=51.81.7.219 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=108 ID=13039 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[181995.075357] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=155.93.168.203 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=62627 PROTO=UDP SPT=34626 DPT=51413 LEN=111
[182137.316700] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:75f4:8b00:2ede:fe64:3aff:feba:e958 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=0 PROTO=UDP SPT=46761 DPT=51413 LEN=112
[182158.608298] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:1c85:8e95:d9c3:34e6:c89f:68fd DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=243200 PROTO=UDP SPT=37819 DPT=51413 LEN=112
[182260.396296] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=23795 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[182269.407538] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=19216 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[182296.503161] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=40483 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[182357.414681] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=7052 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[182394.388182] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=25636 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[182399.544134] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=119 TOS=0x00 PREC=0x00 TTL=55 ID=15614 DF PROTO=UDP SPT=40066 DPT=51413 LEN=99
[182431.184292] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=45769 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[182467.614906] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=64742 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[182532.239389] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=46652 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[182534.507145] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=33560 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[182647.415968] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=46653 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[182739.983882] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2400:c600:462a:eb73:44ff:47a3:2ae7:2bee DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=485892 PROTO=UDP SPT=47344 DPT=51413 LEN=112
[182761.808083] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:1c85:8e95:d9c3:34e6:c89f:68fd DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=243200 PROTO=UDP SPT=37819 DPT=51413 LEN=112
[183200.864108] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=36550 DF PROTO=UDP SPT=40089 DPT=51413 LEN=100
[183468.573244] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=39.99.135.118 DST=192.168.3.19 LEN=44 TOS=0x00 PREC=0x00 TTL=242 ID=34997 PROTO=TCP SPT=25158 DPT=7890 WINDOW=1024 RES=0x00 SYN URGP=0
[184091.653163] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2602:fe45:0a03:ed70:1e12:b0ff:feda:cc0e DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=41 FLOWLBL=978359 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[184114.490002] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=114.228.87.28 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=52 ID=21734 DF PROTO=UDP SPT=56024 DPT=51413 LEN=114
[184362.202127] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=46659 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[184855.699939] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=17186 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[184875.714060] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=27732 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[185139.182059] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=46663 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[185392.283643] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=58955 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[185752.187767] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=46666 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[185959.961632] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2400:1a00:b1e0:5d99:fae6:1aff:fe31:7954 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=32 HOPLIMIT=47 FLOWLBL=0 PROTO=UDP SPT=45308 DPT=51413 LEN=112
[186090.126960] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.252.60.130 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=113 ID=61448 PROTO=UDP SPT=4441 DPT=51413 LEN=111
[186205.322277] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=2304 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[186226.073746] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=12056 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[186375.369056] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=19190 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[186416.217729] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=46273 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[186998.156936] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=46671 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[187128.151461] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=46672 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[187386.915654] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:03b1:c849:7910:9270:922c:bf2c:c684 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=52 FLOWLBL=950456 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[187465.703625] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:03b1:c849:7910:9270:922c:bf2c:c684 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=52 FLOWLBL=950456 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[187486.380693] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:03b1:c849:7910:9270:922c:bf2c:c684 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=53 FLOWLBL=950456 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[187643.489544] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42527 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.489866] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42528 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.490062] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42529 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.490359] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42530 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.490553] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42531 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.490788] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42532 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.491240] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42533 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.491385] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42534 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.491579] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42535 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187643.491709] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42536 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187674.402270] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=49960 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187695.398048] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=52044 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187710.888309] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=23251 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[187726.168380] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=58080 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187750.259788] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=62640 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187767.447078] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=1224 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187803.522197] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=3800 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187813.801762] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=3853 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187824.402127] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=4547 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187844.684651] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=8378 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187864.301206] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=12833 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187887.109136] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=15872 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187907.689770] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=18487 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187927.967489] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22994 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[187943.592539] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=23711 DF PROTO=UDP SPT=50592 DPT=51413 LEN=111
[188070.104155] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=14823 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188099.087619] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[188161.156347] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[188172.482821] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=61431 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188199.740379] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=222.99.106.136 DST=192.168.3.19 LEN=143 TOS=0x00 PREC=0x00 TTL=114 ID=43925 PROTO=UDP SPT=7683 DPT=51413 LEN=123
[188206.887571] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=79.110.62.223 DST=192.168.3.19 LEN=40 TOS=0x00 PREC=0x00 TTL=243 ID=48835 PROTO=TCP SPT=40205 DPT=7890 WINDOW=1024 RES=0x00 SYN URGP=0
[188209.466574] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=17451 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188267.178460] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=16910 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[188318.141174] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=46675 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[188350.209969] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=19655 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188390.672127] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=29374 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188398.304241] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=46030 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188412.407671] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=16912 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[188455.320696] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=13952 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188470.138207] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=46677 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[188492.195397] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=28056 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188501.581888] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=22362 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188608.991249] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=10345 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188640.170820] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=22941 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188752.530453] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=17481 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188826.452458] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=91.180.155.207 DST=192.168.3.19 LEN=132 TOS=0x04 PREC=0x00 TTL=50 ID=61602 DF PROTO=UDP SPT=6881 DPT=51413 LEN=112
[188848.515370] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=62794 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188870.170722] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=6465 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188888.522431] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=20155 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188907.569582] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=31608 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188910.200708] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=29578 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[188957.748794] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=60284 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[188988.972797] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=4992 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[189091.820098] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=51907 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[189148.654059] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=15805 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[189759.654811] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=52150 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[189788.736016] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=47.11.253.16 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=36 ID=17080 DF PROTO=UDP SPT=55365 DPT=51413 LEN=112
[189848.607324] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=47.11.253.16 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=36 ID=44902 DF PROTO=UDP SPT=55365 DPT=51413 LEN=112
[189873.121937] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=28027 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[190333.790904] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=102.17.17.233 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=10369 PROTO=UDP SPT=56636 DPT=51413 LEN=111
[190358.153494] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=64163 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190494.305730] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=6964 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190515.264089] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=16288 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190535.731605] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=26552 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190546.253216] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2800:0484:df7b:be00:32fc:ebff:fe4c:6ed6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=962145 PROTO=UDP SPT=48104 DPT=51413 LEN=112
[190565.276676] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=37564 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190586.441456] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=45000 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190723.812790] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=42801 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190794.554089] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=5595 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190826.486935] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0df7:2380:c9b2:f83a:2bff:fe3a:3de6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=758178 PROTO=UDP SPT=55074 DPT=51413 LEN=112
[190844.895492] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=23353 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[190931.694407] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=55390 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[190972.511334] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=30345 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191010.369884] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=1.80.148.248 DST=192.168.3.19 LEN=95 TOS=0x00 PREC=0x00 TTL=52 ID=23633 PROTO=UDP SPT=2675 DPT=51413 LEN=75
[191042.648591] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=2018 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191082.674467] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=22833 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191103.026660] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=39875 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191165.105824] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=8593 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191291.906297] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=2951 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191343.879021] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014c:3b62:0024:d492:16b9:847e:f6db DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=669064 PROTO=UDP SPT=43185 DPT=51413 LEN=112
[191362.354901] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=41737 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191379.964735] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2806:105e:0006:8196:f042:06ff:fef8:ac15 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=946905 PROTO=UDP SPT=53997 DPT=51413 LEN=112
[191381.428386] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=50658 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191412.507972] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=62109 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191549.048727] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=10497 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191570.197648] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=16155 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191610.527962] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=33715 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191661.160803] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=56172 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191756.595598] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=171.4.219.207 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=107 ID=10456 PROTO=UDP SPT=47438 DPT=51413 LEN=111
[191773.922651] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=67.224.128.158 DST=192.168.3.19 LEN=93 TOS=0x00 PREC=0x00 TTL=45 ID=50769 DF PROTO=UDP SPT=47722 DPT=51413 LEN=73
[191828.426463] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=27533 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191848.560765] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=40098 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191849.847352] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=17726 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191849.847656] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=17727 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191849.848000] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=17728 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191859.339070] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=43256 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[191881.053259] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22939 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191881.053428] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22940 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191881.053768] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22941 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191897.040625] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=45406 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[191901.909111] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=25963 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191903.334565] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=26160 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191903.334685] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=26161 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[191917.426877] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=57870 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114

```

### Looong01 · 2024-11-25

```
[191963.692838] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=13681 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[191966.863512] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a03:4000:001e:05d5:a825:deff:fead:e431 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=97 TC=0 HOPLIMIT=49 FLOWLBL=34828 PROTO=UDP SPT=51413 DPT=51413 LEN=57
[192004.535584] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=34773 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[192016.657503] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=4042 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192041.602965] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=56179 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[192097.061977] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=49079 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192097.932907] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=21208 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[192118.287669] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=58601 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192118.826658] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=32565 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[192123.481610] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=4887 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[192147.158308] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=7559 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192150.574448] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56997 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[192150.574941] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56998 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[192176.839145] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=25897 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192290.516279] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=7848 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[192318.331751] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=43239 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192322.585326] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8214:821c:cfe0:56f6:c5ff:fe18:b37f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=55 FLOWLBL=430588 PROTO=UDP SPT=5793 DPT=51413 LEN=112
[192329.435024] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=49916 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192376.855158] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:8a0c:9847:1880:185e:0c6e:215c:6a16 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=51 FLOWLBL=983811 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[192400.360988] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=26600 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192469.539403] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=52582 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192526.756642] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=8788 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192608.344800] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=47678 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192628.431507] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=54712 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192688.520792] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=19709 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192765.831038] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53971 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192795.975043] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=5146 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[192826.346987] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=19822 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[193002.531754] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=171.4.219.207 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=107 ID=39818 PROTO=UDP SPT=47438 DPT=51413 LEN=111
[193052.373622] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27321 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.373908] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27322 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.374036] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27323 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.374715] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27324 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.374949] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27325 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.375102] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27326 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.375310] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27327 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.375462] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27328 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.375637] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27329 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193052.375793] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=27330 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193083.747285] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=30795 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193093.560548] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=32197 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193114.283640] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=35158 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193135.076213] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=39068 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193155.695774] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=41157 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193176.198010] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=44227 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193196.890058] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=46716 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193217.549008] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=48676 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193238.392625] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51327 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193255.631574] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=52676 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193273.073785] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=54769 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193293.863603] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57489 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193313.303552] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=61262 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193334.980370] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=61362 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193352.751848] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=61829 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193375.273129] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=64846 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[193395.391956] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=50 ID=16543 DF PROTO=UDP SPT=56035 DPT=51413 LEN=149
[193429.201740] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:0fe0:c437:9100:0ce7:23c9:8bc8:8388 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=226447 PROTO=UDP SPT=1668 DPT=51413 LEN=112
[193431.163399] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=30508 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[193493.335017] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=57313 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[193551.868144] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=26327 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[193583.334086] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=39228 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[193624.147043] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2806:0265:3498:8462:a112:67f2:20b9:825a DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=173743 PROTO=UDP SPT=51506 DPT=51413 LEN=112
[193719.839071] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=42268 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[193740.035405] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53148 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[193780.295946] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=5300 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[193800.992192] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=22085 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[194046.550195] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=53540 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[194165.188962] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:40f0:102d:2577:6e57:edc1:2efe:3b8c DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=234 FLOWLBL=778881 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[194175.176542] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.252.60.130 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=113 ID=6652 PROTO=UDP SPT=4441 DPT=51413 LEN=111
[194201.816155] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=53541 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[194223.335042] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=56775 DF PROTO=UDP SPT=40126 DPT=51413 LEN=100
[194223.789460] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0df7:2380:c9b2:f83a:2bff:fe3a:3de6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=758178 PROTO=UDP SPT=55074 DPT=51413 LEN=112
[194401.146647] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:2f00:4302:5d00:08c9:62a6:6886:a2b8 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=788480 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[194490.864279] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:40f0:102d:2577:6e57:edc1:2efe:3b8c DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=233 FLOWLBL=636585 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[194858.401439] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=39184 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[194894.254138] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=197.95.53.77 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=44 ID=31806 PROTO=UDP SPT=5939 DPT=51413 LEN=112
[194994.403623] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=197.95.53.77 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=44 ID=31807 PROTO=UDP SPT=5939 DPT=51413 LEN=112
[195045.174701] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:0fe0:c437:9100:a98b:bb51:e23c:5c25 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=373143 PROTO=UDP SPT=1664 DPT=51413 LEN=112
[195106.916953] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:0fe0:c437:9100:a98b:bb51:e23c:5c25 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=153136 PROTO=UDP SPT=1664 DPT=51413 LEN=112
[195179.539529] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0df7:2380:c9b2:f83a:2bff:fe3a:3de6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=758178 PROTO=UDP SPT=55074 DPT=51413 LEN=112
[195687.550281] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:00e8:018d:4300:84c9:ed5d:4a4c:a949 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=42 FLOWLBL=0 PROTO=UDP SPT=51857 DPT=51413 LEN=112
[195712.310586] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:1c85:8e95:d9c3:34e6:c89f:68fd DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=243200 PROTO=UDP SPT=37819 DPT=51413 LEN=112
[195803.113931] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[195826.752609] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[195932.973095] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[196392.991466] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=14795 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[196498.846891] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47959 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[196498.851359] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47960 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[196657.685355] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22334 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.685682] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22335 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.686009] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22336 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.686133] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22337 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.686380] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22338 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.686579] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22339 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.686906] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22340 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.687108] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22341 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.687195] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22342 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196657.687366] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=22343 DF PROTO=UDP SPT=50206 DPT=51413 LEN=111
[196967.584488] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:8a0c:9847:1880:185e:0c6e:215c:6a16 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=51 FLOWLBL=712345 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[197045.426418] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240f:0037:fcbe:0001:e910:e07f:d0bc:50a7 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=52 FLOWLBL=0 PROTO=UDP SPT=10862 DPT=51413 LEN=112
[197097.026833] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49300 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197097.030980] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49301 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197097.032587] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49302 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197097.531584] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49303 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197098.039582] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49304 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197098.041449] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49305 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197098.546578] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49306 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197098.548640] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49307 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197098.549523] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49308 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197098.550016] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49309 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197116.521650] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:8a0c:9847:1880:185e:0c6e:215c:6a16 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=51 FLOWLBL=712345 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[197216.993501] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=49311 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197348.400695] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014c:3b62:0024:d492:16b9:847e:f6db DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=669064 PROTO=UDP SPT=43185 DPT=51413 LEN=112
[197649.256640] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=118.130.109.108 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=44 ID=0 DF PROTO=UDP SPT=51413 DPT=51413 LEN=66
[197687.743257] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=118.130.109.108 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=44 ID=0 DF PROTO=UDP SPT=51413 DPT=51413 LEN=66
[197698.906440] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6435 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197699.920809] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6436 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197699.922670] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6437 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197699.923555] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6438 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197700.936753] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6439 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197700.939596] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6440 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197700.941104] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6441 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197700.942153] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6442 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197700.943562] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6443 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197717.850930] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=6444 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[197771.698952] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2400:1a00:b020:d611:cf93:1e89:4bc9:1d86 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=117480 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[197819.265532] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=118.130.109.108 DST=192.168.3.19 LEN=86 TOS=0x00 PREC=0x00 TTL=44 ID=0 DF PROTO=UDP SPT=51413 DPT=51413 LEN=66
[197855.982592] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=14801 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[197957.035638] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2400:1a00:b020:d611:cf93:1e89:4bc9:1d86 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=570620 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[198120.253686] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=80.66.83.47 DST=192.168.3.19 LEN=44 TOS=0x00 PREC=0x00 TTL=243 ID=32886 PROTO=TCP SPT=40740 DPT=7890 WINDOW=1025 RES=0x00 SYN URGP=0
[198261.324742] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2603:c021:8012:4c00:9607:749b:705e:9960 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=113 TC=4 HOPLIMIT=52 FLOWLBL=944966 PROTO=UDP SPT=2269 DPT=51413 LEN=73
[198458.476248] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=67.193.73.38 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=4563 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[198647.538630] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8210:603c:b652:0000:0000:0000:0020 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=113 TC=192 HOPLIMIT=58 FLOWLBL=631954 PROTO=UDP SPT=54812 DPT=51413 LEN=73
[198660.659398] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a00:1370:817c:1750:3cfe:97f5:909d:26c0 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=878208 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[198789.215032] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a00:1370:817c:1750:3cfe:97f5:909d:26c0 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=140476 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[198921.505722] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=50 ID=25054 DF PROTO=UDP SPT=56035 DPT=51413 LEN=149
[198947.908560] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=40058 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[198988.756000] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=60741 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[199028.436637] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=12781 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[199109.349118] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=52100 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[199227.208376] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=50715 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[199266.751628] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=4941 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[199297.635678] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=26867 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[199730.599200] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=7012 DF PROTO=UDP SPT=40126 DPT=51413 LEN=100
[199787.930185] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=28159 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[199807.940005] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=28706 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[199814.789192] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=43615 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[199835.127606] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=51299 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[199882.217566] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=12251 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[199918.972255] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=31851 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[199945.997695] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=46229 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[199972.771132] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.25.243.154 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=114 ID=27678 PROTO=UDP SPT=9115 DPT=51413 LEN=112
[199974.221952] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=59714 DF PROTO=UDP SPT=52374 DPT=51413 LEN=111
[199974.222277] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=59715 DF PROTO=UDP SPT=52374 DPT=51413 LEN=111
[199974.222430] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=59716 DF PROTO=UDP SPT=52374 DPT=51413 LEN=111
[199982.635628] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=61364 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[199985.368587] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=62234 DF PROTO=UDP SPT=52374 DPT=51413 LEN=111
[200004.923092] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=28708 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[200015.870501] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=3060 DF PROTO=UDP SPT=52374 DPT=51413 LEN=111
[200019.428627] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=15086 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[200031.441110] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2403:3800:3289:7540:dcfc:adff:fe37:6350 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=902881 PROTO=UDP SPT=39932 DPT=51413 LEN=112
[200051.939911] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=28709 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[200057.029985] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=29315 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[200102.983598] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=50653 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[200151.470991] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2403:3800:3289:7540:dcfc:adff:fe37:6350 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=902881 PROTO=UDP SPT=39932 DPT=51413 LEN=112
[200160.637680] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=14336 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[200206.736319] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=28370 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[200215.937633] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:6f38:403e:f700:c97b:8e07:0696:0957 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=324959 PROTO=UDP SPT=54672 DPT=51413 LEN=112
[200263.763887] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=471 DF PROTO=UDP SPT=40126 DPT=51413 LEN=100
[200921.758376] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:cb19:8e83:5500:1aad:cfce:533b:40d8 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=246 FLOWLBL=786066 PROTO=UDP SPT=49966 DPT=51413 LEN=112
[201235.977471] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0569:504c:6e00:0cb8:3927:f874:25bd DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=51 FLOWLBL=655360 PROTO=UDP SPT=6882 DPT=51413 LEN=112
[201238.497592] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[201243.305902] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=27.59.125.16 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=47 ID=34408 DF PROTO=UDP SPT=61635 DPT=51413 LEN=112
[201323.559274] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=213.130.93.24 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=112 ID=61695 PROTO=UDP SPT=48364 DPT=51413 LEN=111
[202132.453822] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:ab88:3796:0900:0000:0000:0000:8b41 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=549015 PROTO=UDP SPT=8128 DPT=51413 LEN=112
[202390.744075] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=26261 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202410.746483] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=38383 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202416.670960] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=40260 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[202446.691353] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=52340 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[202536.946610] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=30121 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202583.251019] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=58505 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202625.572467] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=20796 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[202677.093429] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=48274 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[202685.475164] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=43710 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202727.512345] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=6399 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[202760.495005] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=13329 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202818.984192] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=40322 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202859.084512] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=62362 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202910.875486] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=28715 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[202954.017163] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=50060 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[202980.848016] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=64857 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[203000.995271] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=5510 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[203105.227077] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:448a:50e0:5a5d:146f:feff:feae:57aa DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=44 FLOWLBL=789163 PROTO=UDP SPT=37673 DPT=51413 LEN=112
[203174.122870] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:ab88:3796:0900:0000:0000:0000:8b41 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=421656 PROTO=UDP SPT=8128 DPT=51413 LEN=112
[203375.965454] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2806:109f:000e:66eb:50d4:8b02:5d32:26ad DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=316805 PROTO=UDP SPT=46030 DPT=51413 LEN=112
[203394.504757] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=37.215.65.12 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=108 ID=40225 PROTO=UDP SPT=21822 DPT=51413 LEN=111
[203412.216621] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2806:109f:000e:66eb:50d4:8b02:5d32:26ad DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=316805 PROTO=UDP SPT=46030 DPT=51413 LEN=112
[203436.599134] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=189.14.50.8 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=106 ID=6450 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[203927.526785] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=78.128.114.58 DST=192.168.3.19 LEN=40 TOS=0x00 PREC=0x00 TTL=243 ID=33380 PROTO=TCP SPT=48545 DPT=7890 WINDOW=1024 RES=0x00 SYN URGP=0
[203949.337927] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a04:cec2:0007:47b8:4074:a6e0:ed4b:fe3f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=199740 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[203975.342271] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2601:0084:8b00:79d0:1515:3cc3:6682:3257 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=396364 PROTO=UDP SPT=50699 DPT=51413 LEN=112
[204207.840700] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=26450 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[204238.600674] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=42315 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[204266.419245] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=54369 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[204317.169227] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=9494 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[204361.855473] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=113 ID=39322 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[204435.575820] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=189.14.50.8 DST=192.168.3.19 LEN=93 TOS=0x00 PREC=0x00 TTL=106 ID=6451 PROTO=UDP SPT=6881 DPT=51413 LEN=73
[204490.683758] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=189.14.50.8 DST=192.168.3.19 LEN=93 TOS=0x00 PREC=0x00 TTL=106 ID=6452 PROTO=UDP SPT=6881 DPT=51413 LEN=73
[204612.620440] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=25320 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[204672.727183] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=60026 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[204751.160418] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a04:cec2:0007:47b8:4074:a6e0:ed4b:fe3f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=588295 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[204772.225402] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=102.17.17.233 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=10382 PROTO=UDP SPT=56636 DPT=51413 LEN=111
[204872.264897] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=51.81.7.219 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=108 ID=13054 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[204928.952324] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=7018 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205107.253954] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=16224 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205156.859165] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=41072 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205177.155927] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=55407 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205328.991104] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13316 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205343.907635] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13317 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205343.908008] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13318 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205343.909664] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13319 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205343.953547] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13320 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205353.036653] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=89.151.129.12 DST=192.168.3.19 LEN=93 TOS=0x00 PREC=0x00 TTL=111 ID=65380 PROTO=UDP SPT=30864 DPT=51413 LEN=73
[205354.908330] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13321 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205354.909172] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13322 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205354.910054] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13323 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205354.910698] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13324 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205354.911790] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13325 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205371.601897] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13329 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205390.655301] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13334 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205411.825071] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13341 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205457.825161] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13342 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205468.904672] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13343 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205479.685698] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13344 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205492.626554] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=11133 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205517.030414] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=13345 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[205613.020379] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=14315 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205702.757446] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=44390 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205722.043508] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=47973 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205773.567597] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a04:cec2:0007:47b8:4074:a6e0:ed4b:fe3f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=161407 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[205793.831065] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=16500 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[205883.837604] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a04:cec2:0007:47b8:4074:a6e0:ed4b:fe3f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=44 FLOWLBL=989976 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[205923.114400] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=27902 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206024.098929] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=16831 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206119.319457] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=77.29.153.66 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=47 ID=56337 DF PROTO=UDP SPT=37395 DPT=51413 LEN=112
[206132.222376] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=23625 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206142.482128] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=31410 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206221.741489] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=51375 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[206254.831579] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=24541 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206402.351264] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=34865 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206566.304492] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=43448 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206662.426477] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=26920 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206713.418633] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=52927 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206714.224955] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=102.17.17.233 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=10384 PROTO=UDP SPT=56636 DPT=51413 LEN=111
[206744.650176] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=448 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[206847.920608] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=27.59.125.16 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=47 ID=50727 DF PROTO=UDP SPT=61635 DPT=51413 LEN=112
[206930.516232] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2806:109f:000e:66eb:50d4:8b02:5d32:26ad DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=300713 PROTO=UDP SPT=40042 DPT=51413 LEN=112
[207130.125645] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22393 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207144.012222] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22394 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207144.012427] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22395 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207144.719738] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22396 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207144.757486] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22397 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207154.930561] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22398 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207154.931573] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22399 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207154.932593] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22400 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207154.933471] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22401 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207155.927403] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22402 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207155.957247] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22403 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207172.231034] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22408 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207197.706833] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22415 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207212.703701] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22417 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207258.686795] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22418 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207274.645248] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22419 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207280.589119] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22420 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207311.910367] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=22421 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[207856.855276] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:4900:1c22:4a78:001c:70ff:feed:22b0 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=32 HOPLIMIT=50 FLOWLBL=318684 PROTO=UDP SPT=50997 DPT=51413 LEN=112
[207992.471249] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:de00:0001:0006:0000:0000:0000:8ae5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=51 FLOWLBL=1007506 PROTO=UDP SPT=57210 DPT=51413 LEN=75
[208107.326538] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2601:0084:8b00:79d0:1515:3cc3:6682:3257 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=953084 PROTO=UDP SPT=50699 DPT=51413 LEN=112
[208136.793088] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=39337 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[208202.156168] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a00:1370:817c:1750:4d4f:9a0b:d745:bb24 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=890470 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[208350.221491] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=15268 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[208462.466431] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=60921 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[208531.536774] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=25100 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[208531.540144] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=25101 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[208531.542137] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=25102 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[208531.542729] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=25103 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[208532.551543] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=25104 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[208554.781562] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=5.76.124.130 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=113 ID=11439 PROTO=UDP SPT=6882 DPT=51413 LEN=112
[208673.711155] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=30708 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[208693.841646] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=41568 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[208714.504403] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=49782 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[208774.477725] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=13716 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[208815.252986] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=34200 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[208876.136957] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:75f4:8b00:2ede:1405:d1f2:19e9:5978 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=0 PROTO=UDP SPT=48022 DPT=51413 LEN=112
[208932.067105] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2602:fe45:0a03:ed70:1e12:b0ff:feda:cc0e DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=41 FLOWLBL=978359 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[209023.686083] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2400:4050:a9a2:ea00:1418:f1ff:fe1f:1873 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=361878 PROTO=UDP SPT=42591 DPT=51413 LEN=112
[209241.530940] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=55917 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[209425.771897] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=14793 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[210271.853018] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[210357.758382] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=14798 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[210362.712567] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[210436.882021] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[210487.688822] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=73.245.145.45 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=22673 PROTO=UDP SPT=22010 DPT=51413 LEN=112
```

### Looong01 · 2024-11-25

```
[210562.765172] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=73.245.145.45 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=22674 PROTO=UDP SPT=22010 DPT=51413 LEN=112
[210995.168554] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=27.59.125.16 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=47 ID=15377 DF PROTO=UDP SPT=61635 DPT=51413 LEN=112
[211349.023767] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.24.116.223 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=62562 PROTO=UDP SPT=30744 DPT=51413 LEN=111
[211398.034698] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.24.116.223 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=62563 PROTO=UDP SPT=30744 DPT=51413 LEN=111
[212553.040644] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.24.116.223 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=111 ID=21148 PROTO=UDP SPT=30744 DPT=51413 LEN=111
[212627.289098] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=28813 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[212697.246703] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=222.99.106.136 DST=192.168.3.19 LEN=143 TOS=0x00 PREC=0x00 TTL=114 ID=18373 PROTO=UDP SPT=7683 DPT=51413 LEN=123
[213342.763021] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=213.130.93.24 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=112 ID=21159 PROTO=UDP SPT=48364 DPT=51413 LEN=111
[213543.883447] audit: type=1400 audit(1732545899.625:48): apparmor="DENIED" operation="open" profile="ubuntu_pro_esm_cache" name="/opt/rocm-6.2.3/lib/" pid=2392832 comm="python3" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
[213543.883451] audit: type=1400 audit(1732545899.625:49): apparmor="DENIED" operation="open" profile="ubuntu_pro_apt_news" name="/opt/rocm-6.2.3/lib/" pid=2392831 comm="python3" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
[213933.686451] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=34762 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[213942.695061] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=42090 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[214114.728354] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:03a2:5214:46e0:3175:6bf8:4c3c:cd0d DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=151 TC=0 HOPLIMIT=52 FLOWLBL=0 PROTO=UDP SPT=15000 DPT=51413 LEN=111
[214188.465397] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:03a2:5214:46e0:3175:6bf8:4c3c:cd0d DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=52 FLOWLBL=0 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[214201.485970] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=42092 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[214226.708383] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:03a2:5214:46e0:3175:6bf8:4c3c:cd0d DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=52 FLOWLBL=0 PROTO=UDP SPT=15000 DPT=51413 LEN=75
[214343.498155] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=26586 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[214384.197045] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=54174 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[214559.859159] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=201.119.129.12 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=15757 DF PROTO=UDP SPT=37939 DPT=51413 LEN=112
[214609.221815] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:de00:0001:0006:0000:0000:0000:8ae5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=51 FLOWLBL=190275 PROTO=UDP SPT=57210 DPT=51413 LEN=75
[214647.461582] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=37.215.65.12 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=108 ID=40236 PROTO=UDP SPT=21822 DPT=51413 LEN=111
[214671.784880] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:de00:0001:0006:0000:0000:0000:8ae5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=51 FLOWLBL=825089 PROTO=UDP SPT=57210 DPT=51413 LEN=75
[214778.692654] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:de00:0001:0006:0000:0000:0000:8ae5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=115 TC=0 HOPLIMIT=51 FLOWLBL=437579 PROTO=UDP SPT=57210 DPT=51413 LEN=75
[214822.637253] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2003:00ee:bf43:c000:f597:8e8e:3247:e1d9 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=244 FLOWLBL=373529 PROTO=UDP SPT=44411 DPT=51413 LEN=112
[214872.668556] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2003:00ee:bf43:c000:f597:8e8e:3247:e1d9 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=244 FLOWLBL=373529 PROTO=UDP SPT=44411 DPT=51413 LEN=112
[214977.922202] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=67.193.73.38 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=48613 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[214999.666645] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=42095 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[215223.956227] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=36476 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[215296.791762] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=2328 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[215393.587871] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=38.96.255.76 DST=192.168.3.19 LEN=125 TOS=0x00 PREC=0x00 TTL=53 ID=54521 DF PROTO=UDP SPT=10022 DPT=51413 LEN=105
[215586.041449] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=222.155.46.253 DST=192.168.3.19 LEN=126 TOS=0x00 PREC=0x00 TTL=111 ID=61607 PROTO=UDP SPT=20934 DPT=51413 LEN=106
[215922.612823] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=48275 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[215936.656116] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=42098 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[215968.650277] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=42099 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[216206.753663] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=222.99.106.136 DST=192.168.3.19 LEN=143 TOS=0x00 PREC=0x00 TTL=114 ID=8063 PROTO=UDP SPT=7683 DPT=51413 LEN=123
[216298.489777] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2003:00ee:bf43:c000:f597:8e8e:3247:e1d9 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=244 FLOWLBL=373529 PROTO=UDP SPT=44411 DPT=51413 LEN=112
[216609.353233] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:820c:8f0b:0381:0000:0000:0000:0a15 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=4 HOPLIMIT=56 FLOWLBL=712908 PROTO=UDP SPT=60001 DPT=51413 LEN=112
[216643.565840] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=47017 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[216747.853495] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=37871 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[216857.573348] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=39.99.135.118 DST=192.168.3.19 LEN=44 TOS=0x00 PREC=0x00 TTL=242 ID=39882 PROTO=TCP SPT=27128 DPT=7890 WINDOW=1024 RES=0x00 SYN URGP=0
[216887.622256] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2806:02f0:8561:fc94:592e:6f8e:0c12:7d20 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=50 FLOWLBL=379645 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[217196.469750] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2401:4900:6587:ec9f:f7bb:eb78:28a0:ce45 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=128 HOPLIMIT=47 FLOWLBL=209119 PROTO=UDP SPT=48195 DPT=51413 LEN=112
[217606.527754] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=179.107.253.16 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=6 DF PROTO=UDP SPT=52113 DPT=51413 LEN=112
[217612.753448] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=179.107.253.16 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=310 DF PROTO=UDP SPT=52113 DPT=51413 LEN=112
[217961.270443] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=3221 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[217981.592467] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=11727 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[218118.625232] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=24209 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[218148.305775] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=38446 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[218218.950933] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=11400 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[218978.461619] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.228.200.195 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=62601 PROTO=UDP SPT=25446 DPT=51413 LEN=112
[219194.221820] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=222.155.46.253 DST=192.168.3.19 LEN=126 TOS=0x00 PREC=0x00 TTL=111 ID=62304 PROTO=UDP SPT=20934 DPT=51413 LEN=106
[219621.127536] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=214 DF PROTO=UDP SPT=52448 DPT=51413 LEN=111
[219655.450278] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=1408 DF PROTO=UDP SPT=52448 DPT=51413 LEN=111
[219697.026176] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2800:0b20:111b:2e5d:c14b:cb67:7555:65e8 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=45 FLOWLBL=165588 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[219801.018502] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=31123 DF PROTO=UDP SPT=52448 DPT=51413 LEN=111

[219801.056770] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=31131 DF PROTO=UDP SPT=52448 DPT=51413 LEN=111

[219842.443780] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=40301 DF PROTO=UDP SPT=52448 DPT=51413 LEN=111

[220010.052533] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=78.85.39.95 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=112 ID=7624 PROTO=UDP SPT=38914 DPT=51413 LEN=112
[220548.904291] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=9015 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[220760.551358] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=83.97.7.219 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=113 ID=3796 PROTO=UDP SPT=4686 DPT=51413 LEN=111
[220902.083765] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=27769 DF PROTO=UDP SPT=40126 DPT=51413 LEN=100
[221727.552479] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=83.97.7.219 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=113 ID=26618 PROTO=UDP SPT=4686 DPT=51413 LEN=111
[221755.534702] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=83.97.7.219 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=113 ID=26619 PROTO=UDP SPT=4686 DPT=51413 LEN=111
[222107.641959] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.215.236.52 DST=192.168.3.19 LEN=44 TOS=0x00 PREC=0x00 TTL=242 ID=55683 PROTO=TCP SPT=43373 DPT=7890 WINDOW=1025 RES=0x00 SYN URGP=0
[222823.168823] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=8730 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[222847.452578] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a00:1370:818e:5169:7b29:48b2:e033:de85 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=238 FLOWLBL=81285 PROTO=UDP SPT=23942 DPT=51413 LEN=112
[222932.276693] systemd-rc-local-generator[2433353]: /etc/rc.local is not marked executable, skipping.
[222933.349514] loop6: detected capacity change from 0 to 183096
[222933.506892] systemd-rc-local-generator[2433412]: /etc/rc.local is not marked executable, skipping.
[222933.944333] audit: type=1400 audit(1732555289.642:50): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/snap/snapd/21759/usr/lib/snapd/snap-confine" pid=2433456 comm="apparmor_parser"
[222933.944337] audit: type=1400 audit(1732555289.642:51): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/snap/snapd/21759/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=2433456 comm="apparmor_parser"
[222934.110911] audit: type=1400 audit(1732555289.810:52): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.lxd.benchmark" pid=2433459 comm="apparmor_parser"
[222934.111888] audit: type=1400 audit(1732555289.810:53): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.lxd.activate" pid=2433458 comm="apparmor_parser"
[222934.112711] audit: type=1400 audit(1732555289.810:54): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.lxd.buginfo" pid=2433460 comm="apparmor_parser"
[222934.113169] audit: type=1400 audit(1732555289.810:55): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.lxd.check-kernel" pid=2433461 comm="apparmor_parser"
[222934.163242] audit: type=1400 audit(1732555289.862:56): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.lxd.hook.configure" pid=2433463 comm="apparmor_parser"
[222934.176425] audit: type=1400 audit(1732555289.874:57): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.lxd.daemon" pid=2433462 comm="apparmor_parser"
[222934.240105] audit: type=1400 audit(1732555289.938:58): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.lxd.hook.install" pid=2433471 comm="apparmor_parser"
[222934.270458] audit: type=1400 audit(1732555289.970:59): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.lxd.hook.remove" pid=2433472 comm="apparmor_parser"
[222934.534737] systemd-rc-local-generator[2433499]: /etc/rc.local is not marked executable, skipping.
[222934.794754] systemd-rc-local-generator[2433533]: /etc/rc.local is not marked executable, skipping.
[222935.320428] systemd-rc-local-generator[2433630]: /etc/rc.local is not marked executable, skipping.
[222986.835865] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=36720 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[223048.208580] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=40785 DF PROTO=UDP SPT=40126 DPT=51413 LEN=100
[223053.724180] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=3451 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[223135.519990] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=46825 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[223917.345314] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:408c:271f:234d:0000:0000:0e95:58ad DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=43 FLOWLBL=422643 PROTO=UDP SPT=42494 DPT=51413 LEN=112
[224449.560817] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=12913 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[224937.310596] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:0d59:b902:0f00:997e:768c:9937:aa5d DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=316087 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[225138.388734] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=57301 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[225632.045516] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a01:0e11:300c:c400:a8e5:5aff:fe94:7e40 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=688117 PROTO=UDP SPT=55250 DPT=51413 LEN=112
[225723.541041] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=49411 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[225769.309838] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=109.228.200.195 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=111 ID=16309 PROTO=UDP SPT=25446 DPT=51413 LEN=112
[225774.933092] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=14989 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[226645.624756] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:1424:6171:1400:c4de:1c08:9267:4261 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=614033 PROTO=UDP SPT=46843 DPT=51413 LEN=112
[226660.628462] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:1424:6171:1400:c4de:1c08:9267:4261 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=614033 PROTO=UDP SPT=46843 DPT=51413 LEN=112
[226760.547232] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=179.107.253.16 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=49 ID=12463 DF PROTO=UDP SPT=52113 DPT=51413 LEN=112
[226828.540288] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=57305 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[226860.949925] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=65037 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[226860.968705] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[226912.995300] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=62884 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[226941.900554] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[226984.241371] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=26958 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[226986.551997] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=57306 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[226992.297711] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[227132.034340] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=30436 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[227163.972705] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=48475 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[227301.645621] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=57691 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[227326.409435] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56445 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227326.409896] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56446 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227326.410111] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56447 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227326.410307] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56448 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227326.410504] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56449 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227326.410898] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56450 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227326.411094] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=56451 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227337.629985] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=58587 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227337.630198] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=58588 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227337.630427] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=58589 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227348.302813] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=60767 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227368.370533] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=62906 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227388.932432] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=420 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[227409.826361] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=1943 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[227417.969485] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:a03f:64e3:4200:b534:a8bc:02ba:6932 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=265860 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[227430.302547] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=5627 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[227451.687272] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=9103 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[227472.694818] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=10974 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227493.120698] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=13179 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227507.740118] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=14654 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227526.505492] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=18027 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227547.180390] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=19319 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227568.880206] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=21460 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227589.505940] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=23943 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227611.151362] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=26337 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227631.787612] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=28652 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227647.745760] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=30415 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227668.713572] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=33321 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227689.098186] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=35962 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227706.925168] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=182.118.46.36 DST=192.168.3.19 LEN=120 TOS=0x00 PREC=0x00 TTL=55 ID=36759 DF PROTO=UDP SPT=40126 DPT=51413 LEN=100
[227735.283980] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=42465 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227748.206090] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=43325 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227767.020229] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=44356 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227787.813638] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=46184 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227809.043164] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=49590 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227830.248305] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=52929 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227851.135432] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57090 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227868.784454] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=58908 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227892.032554] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=61451 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227906.744602] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=63196 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[227927.553741] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=400 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[227947.877611] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=3472 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[227968.677777] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=6286 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[227986.533791] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=7288 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[228008.047549] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=9366 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[228041.090343] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=16171 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228068.872983] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=21101 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228082.353115] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=23148 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228099.085640] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=24078 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228174.720224] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:820c:8f0b:0381:0000:0000:0000:0a15 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=4 HOPLIMIT=56 FLOWLBL=712908 PROTO=UDP SPT=60001 DPT=51413 LEN=112
[228239.259591] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51174 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228239.259632] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51175 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228239.259648] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51176 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228239.259716] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51177 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228239.259722] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51178 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228239.259853] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51179 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228239.504563] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51183 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228248.356822] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=51900 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[228290.822519] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=25421 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[228310.880541] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=223.111.104.4 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=51 ID=32679 DF PROTO=UDP SPT=56188 DPT=51413 LEN=114
[228314.557809] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=858 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[228620.263032] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=50 ID=35891 DF PROTO=UDP SPT=56035 DPT=51413 LEN=149
[228676.782962] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=4219 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[228708.471307] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=15736 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[228750.594050] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=38999 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[228791.019365] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=52479 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[228897.146128] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a04:cec2:0007:47b8:4074:a6e0:ed4b:fe3f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=46 FLOWLBL=894722 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[228901.385269] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=41547 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[228931.844701] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=56487 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[228973.072411] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=11174 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229112.437545] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=1996 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229278.562421] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=34080 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229319.410604] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=55593 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229402.187161] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=25618 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229517.925861] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=18011 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229545.586055] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:78b3:6001:b590:0789:b345:e8e3 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=41 FLOWLBL=24047 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[229548.453024] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=39853 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229578.830495] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=58310 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229596.399844] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a0a:f640:1800:16d4:0000:0000:0000:005f DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=239 FLOWLBL=844650 PROTO=UDP SPT=43509 DPT=51413 LEN=112
[229630.776534] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:78b3:6001:b590:0789:b345:e8e3 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=42 FLOWLBL=257180 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[229631.170278] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=24506 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229705.580183] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=50990 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229766.819352] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=14974 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229828.597200] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53394 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[229901.089228] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=95.90.186.85 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=46 ID=46342 DF PROTO=UDP SPT=25208 DPT=51413 LEN=112
[229938.446540] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=40053 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230109.052629] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53721 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230162.514785] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=14952 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230293.063670] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2409:408c:271f:234d:0000:0000:0e95:58ad DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=40 HOPLIMIT=43 FLOWLBL=422643 PROTO=UDP SPT=42494 DPT=51413 LEN=112
[230313.081490] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=28692 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230353.933411] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=48874 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230501.335871] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=63775 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230583.097847] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=45751 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230644.079591] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=1889 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[230673.155284] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=45.244.72.195 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=46 ID=38641 DF PROTO=UDP SPT=53658 DPT=51413 LEN=112
[230695.661401] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=7734 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111
[230746.081233] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=1423 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230796.213623] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=30895 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230816.663000] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=41018 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230876.809845] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=8332 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[230985.991091] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=4085 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[231005.329779] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2001:0569:504c:6e00:0cb8:3927:f874:25bd DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=51 FLOWLBL=655360 PROTO=UDP SPT=6882 DPT=51413 LEN=112
[231211.636351] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=151 TOS=0x00 PREC=0x00 TTL=112 ID=52750 PROTO=UDP SPT=33330 DPT=51413 LEN=131
[231348.290426] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=50 ID=56433 DF PROTO=UDP SPT=56035 DPT=51413 LEN=149
[231416.285525] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=21548 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[231465.653169] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=52502 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[231486.393121] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=2096 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[231517.534081] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=11810 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[231636.138144] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=20051 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[231676.251568] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53286 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[231829.814638] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=222.155.46.253 DST=192.168.3.19 LEN=126 TOS=0x00 PREC=0x00 TTL=111 ID=32639 PROTO=UDP SPT=20934 DPT=51413 LEN=106
[232026.927437] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=169 TOS=0x00 PREC=0x00 TTL=50 ID=20239 DF PROTO=UDP SPT=56035 DPT=51413 LEN=149
[232095.837258] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=43979 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[232125.386413] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53348 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[232285.862030] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:78b3:6001:b590:0789:b345:e8e3 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=42 FLOWLBL=656180 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[232558.370692] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=240e:0346:2148:f700:023a:6eff:fe73:3fb5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=52 FLOWLBL=986292 PROTO=UDP SPT=34567 DPT=51413 LEN=112
[232709.373883] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=179.186.122.85 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=46 ID=60456 PROTO=UDP SPT=52885 DPT=51413 LEN=112
[232800.729397] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57463 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.729645] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57464 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.729841] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57465 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.730038] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57466 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.730432] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57467 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.730630] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57468 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.730794] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57469 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.730988] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57470 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.731118] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57471 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[232800.731281] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=180.162.215.115 DST=192.168.3.19 LEN=131 TOS=0x00 PREC=0x00 TTL=52 ID=57472 DF PROTO=UDP SPT=49738 DPT=51413 LEN=111

[233113.328705] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[233142.505254] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2803:cc50:753f:1700:c2d3:c0ff:fe9b:ede7 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=43 FLOWLBL=0 PROTO=UDP SPT=53787 DPT=51413 LEN=112
[233151.368182] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2408:8248:5e11:a1b0:b2d5:9dff:fee5:31c5 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=106 TC=0 HOPLIMIT=56 FLOWLBL=943546 PROTO=UDP SPT=51413 DPT=51413 LEN=66
[233161.061758] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2602:fe45:0a03:ed70:1e12:b0ff:feda:cc0e DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=42 FLOWLBL=978359 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[233628.852402] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=63741 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[233691.798136] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=197.215.193.12 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=43 ID=14604 DF PROTO=UDP SPT=56332 DPT=51413 LEN=112
[234530.009276] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=53437 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[234550.345077] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=63605 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[234661.935070] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=42239 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[234780.201001] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=47256 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[234811.333984] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=57143 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[234901.757666] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=27815 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[235001.634797] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=9443 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[235082.754520] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=50801 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[235206.632661] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:78b3:6001:b590:0789:b345:e8e3 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=41 FLOWLBL=783714 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[235614.267960] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=94.156.167.76 DST=192.168.3.19 LEN=44 TOS=0x00 PREC=0x00 TTL=243 ID=51774 PROTO=TCP SPT=56892 DPT=7890 WINDOW=1025 RES=0x00 SYN URGP=0
[236079.479849] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8215 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236083.246863] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8216 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236095.460563] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8217 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236109.185799] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8218 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236109.186020] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8219 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236110.163867] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8220 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236110.164447] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8221 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236115.323053] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8222 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236116.210684] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8223 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236118.196186] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8224 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236122.313082] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8225 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236122.313494] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=178.209.255.219 DST=192.168.3.19 LEN=146 TOS=0x00 PREC=0x00 TTL=109 ID=8226 PROTO=UDP SPT=49001 DPT=51413 LEN=126
[236235.643349] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:a31a:a2c0:1980:58ed:3ddd:7043:d8c6 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=47 FLOWLBL=1046684 PROTO=UDP SPT=48812 DPT=51413 LEN=112
[236739.958504] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=64740 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[236747.901832] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47610 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236747.945305] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47611 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236747.947379] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47612 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236748.454057] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47613 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236748.958800] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47614 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236748.961612] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47615 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236748.962100] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47616 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236762.127694] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47617 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236762.130343] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47618 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236763.146105] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47619 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236822.121575] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=28236 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[236822.150638] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=125.137.96.150 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=115 ID=47623 PROTO=UDP SPT=7705 DPT=51413 LEN=112
[236929.728419] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=1906 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[236960.051368] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:78b3:6001:b590:0789:b345:e8e3 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=42 FLOWLBL=948536 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[236970.070242] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:014d:78b3:6001:b590:0789:b345:e8e3 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=42 FLOWLBL=948536 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[236992.162525] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=33142 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237041.328821] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=55976 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237119.976394] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=23295 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237130.258461] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=27060 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237211.871415] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=8337 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237232.381802] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=20217 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237311.740818] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=997 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237314.136848] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:a03f:64e3:4200:b534:a8bc:02ba:6932 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=879505 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[237339.169190] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a02:a03f:64e3:4200:b534:a8bc:02ba:6932 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=48 FLOWLBL=879505 PROTO=UDP SPT=6881 DPT=51413 LEN=112
[237351.684704] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2a06:c701:9b43:6b00:8cf6:a7ff:fe0d:0a76 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=50 FLOWLBL=294873 PROTO=UDP SPT=52504 DPT=51413 LEN=112
[237392.853488] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=50629 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237481.398079] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=34664 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237570.211071] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=28091 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237790.170499] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=4346 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237798.809164] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:86:dd SRC=2804:1660:402d:9500:c8d8:39ff:feea:4314 DST=2408:8210:2421:6950:5452:84c8:a48c:0003 LEN=152 TC=0 HOPLIMIT=49 FLOWLBL=0 PROTO=UDP SPT=54150 DPT=51413 LEN=112
[237822.234898] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=15694 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237843.267714] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=23431 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[237907.068338] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=171.126.163.231 DST=192.168.3.19 LEN=93 TOS=0x00 PREC=0x00 TTL=120 ID=13086 PROTO=UDP SPT=40632 DPT=51413 LEN=73
[237971.650936] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=29055 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[238032.657260] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=3371 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[238172.254120] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=3716 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[238190.238560] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=46.61.80.184 DST=192.168.3.19 LEN=99 TOS=0x00 PREC=0x00 TTL=112 ID=48103 PROTO=UDP SPT=33330 DPT=51413 LEN=79
[238201.268628] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=18810 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[238244.355342] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=45983 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[238380.073389] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=48409 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[238400.629200] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=55725 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[238471.388838] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=91.83.73.81 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=48 ID=39756 DF PROTO=UDP SPT=37047 DPT=51413 LEN=112
```

### Looong01 · 2024-11-25

```
[238520.005878] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=57524 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
[238557.926051] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=181.132.8.195 DST=192.168.3.19 LEN=132 TOS=0x00 PREC=0x00 TTL=45 ID=50324 DF PROTO=UDP SPT=46627 DPT=51413 LEN=112
[238571.115295] [UFW BLOCK] IN=enp8s0 OUT= MAC=a8:5e:45:b6:d7:21:54:52:84:c8:a4:8c:08:00 SRC=61.147.218.201 DST=192.168.3.19 LEN=134 TOS=0x00 PREC=0x00 TTL=50 ID=24865 DF PROTO=UDP SPT=56035 DPT=51413 LEN=114
```

### Looong01 · 2024-11-25

It seems that there is no amdgpu info.

### Looong01 · 2024-11-25

> This issue will be closed for now due to inactivity. Please feel free to reopen for follow up. Thanks!

Pls reopen this.🙏

```
$ sudo amd-smi set -f 100% -g 0 --loglevel debug

            ******WARNING******

            Operating your AMD GPU outside of official AMD specifications or outside of
            factory settings, including but not limited to the conducting of overclocking,
            over-volting or under-volting (including use of this interface software,
            even if such software has been directly or indirectly provided by AMD or otherwise
            affiliated in any way with AMD), may cause damage to your AMD GPU, system components
            and/or result in system failure, as well as cause other problems.
            DAMAGES CAUSED BY USE OF YOUR AMD GPU OUTSIDE OF OFFICIAL AMD SPECIFICATIONS OR
            OUTSIDE OF FACTORY SETTINGS ARE NOT COVERED UNDER ANY AMD PRODUCT WARRANTY AND
            MAY NOT BE COVERED BY YOUR BOARD OR SYSTEM MANUFACTURER'S WARRANTY.
            Please use this utility with caution.

Do you accept these terms? [y/n] y
Traceback (most recent call last):
  File "/opt/rocm-6.2.3/libexec/amdsmi_cli/amdsmi_commands.py", line 3487, in set_gpu
    amdsmi_interface.amdsmi_set_gpu_fan_speed(args.gpu, 0, args.fan)
  File "/usr/local/lib/python3.10/dist-packages/amdsmi/amdsmi_interface.py", line 2772, in amdsmi_set_gpu_fan_speed
    _check_res(
  File "/usr/local/lib/python3.10/dist-packages/amdsmi/amdsmi_interface.py", line 545, in _check_res
    raise AmdSmiLibraryException(ret_code)
amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
        2 | AMDSMI_STATUS_NOT_SUPPORTED - Feature not supported

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/bin/amd-smi", line 133, in <module>
    args.func(args)
  File "/opt/rocm-6.2.3/libexec/amdsmi_cli/amdsmi_commands.py", line 3735, in set_value
    self.set_gpu(args, multiple_devices, gpu, fan, perf_level,
  File "/opt/rocm-6.2.3/libexec/amdsmi_cli/amdsmi_commands.py", line 3491, in set_gpu
    raise ValueError(f"Unable to set fan speed {args.fan} on {gpu_string}") from e
ValueError: Unable to set fan speed 255 on GPU ID: 0 BDF:0000:03:00.0
```

### tcgu-amd · 2024-11-26

> > This issue will be closed for now due to inactivity. Please feel free to reopen for follow up. Thanks!
> 
> Pls reopen this.🙏

Hi @Looong01, thanks for reaching out again. After some investigation, it seems that manual fan speed control is not currently supported on Navi 31 unfortunately. There is a related issue [here](https://github.com/ROCm/ROCK-Kernel-Driver/issues/162). Since this is a missing feature, I will keep this post open and label it as feature request. We will try our best to post you on the status of the issue (it is still being investigated). However, please do feel free to follow up on this post to ping us as well. Thanks! :)

### tcgu-amd · 2025-02-28

Hi @Looong01, currently, it is possible to enable fan control through the overdrive interface. Here are the instructions

https://github.com/ROCm/ROCK-Kernel-Driver/issues/162#issuecomment-2690986760.

Thanks! 
