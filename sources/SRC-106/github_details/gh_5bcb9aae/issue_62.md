# [Issue #62] [Issue]: ERROR output in conda environment

source: https://github.com/ROCm/amdsmi/issues/62
state: closed | updated: 2024-11-20T15:39:39Z
labels: Under Investigation

## 正文

### Problem Description

(base) johnny@johnny-Ubuntu:~$   echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";
  echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;
  echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
OS:
NAME="Ubuntu"
VERSION="24.04.1 LTS (Noble Numbat)"
CPU: 
model name	: AMD Ryzen 9 7950X3D 16-Core Processor
GPU:
  Name:                    AMD Ryzen 9 7950X3D 16-Core Processor
  Marketing Name:          AMD Ryzen 9 7950X3D 16-Core Processor
  Name:                    gfx1100                            
  Marketing Name:          AMD Radeon PRO W7900 Dual Slot     
      Name:                    amdgcn-amd-amdhsa--gfx1100   

### Operating System

24.04.1 LTS (Noble Numbat)

### CPU

AMD Ryzen 9 7950X3D 16-Core Processor

### GPU

AMD Radeon PRO W7900 Dual Slot

### ROCm Version

ROCm 6.2.3

### ROCm Component

amdsmi

### Steps to Reproduce

amd-smi in conda environment
![image](https://github.com/user-attachments/assets/afb25ac8-fd5f-41f1-9788-d970a10769c3)
amd-smi in python SO
![image](https://github.com/user-attachments/assets/da8e8ff0-7019-4f0d-9615-ae2ebd8e6f98)


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

(base) johnny@johnny-Ubuntu:~$  /opt/rocm/bin/rocminfo --support
ROCk module version 6.8.5 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.14
Runtime Ext Version:     1.6
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
  Name:                    AMD Ryzen 9 7950X3D 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 7950X3D 16-Core Processor
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
  Max Clock Freq. (MHz):   5759                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32475788(0x1ef8a8c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32475788(0x1ef8a8c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32475788(0x1ef8a8c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-22e7a62c92d3e75e               
  Marketing Name:          AMD Radeon PRO W7900 Dual Slot     
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
  Chip ID:                 29770(0x744a)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1760                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
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
  Packet Processor uCode:: 342                                
  SDMA engine uCode::      21                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    47169536(0x2cfc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    47169536(0x2cfc000) KB             
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

## 评论 (5)

### ppanchad-amd · 2024-10-28

Hi @johnnynunez. Internal ticket has been created to investigate your issue. Thanks!

### dmitrii-galantsev · 2024-11-15

heads up - i never used conda before.

Got this to work INSIDE conda env:

```
sudo rm -rf /opt/rocm/share/amd_smi/{amdsmi.egg-info,build}
sudo chmod -R a+rw /opt/rocm/share/amd_smi/
python3 -m pip install /opt/rocm/share/amd_smi/
```

Issue is with this: https://github.com/ROCm/amdsmi/blob/afd06950c15fad2dde57b9c54c807629ef8d02cf/DEBIAN/postinst.in#L173

which runs with system python on install. And installs amdsmi into `/usr/local/lib/python3.*/dist-packages/`. Which conda of course doesn't use.

### dmitrii-galantsev · 2024-11-15

I thought `PYTHONPATH=/opt/rocm/share/amd_smi/` would make it work.. But nope! it does NOT!

`PYTHONPATH=/usr/local/lib/python3.10/dist-packages/` does work though.  
(note that python version should match your system's.

### dmitrii-galantsev · 2024-11-15

thanks to @ppanchad-amd for pinging me about this ticket until I looked into it! Lots of stuff going on and it's easy to miss public github issues :)

### johnnynunez · 2024-11-17

> heads up - i never used conda before.
> 
> Got this to work INSIDE conda env:
> 
> ```
> sudo rm -rf /opt/rocm/share/amd_smi/{amdsmi.egg-info,build}
> sudo chmod -R a+rw /opt/rocm/share/amd_smi/
> python3 -m pip install /opt/rocm/share/amd_smi/
> ```
> 
> Issue is with this:
> 
> https://github.com/ROCm/amdsmi/blob/afd06950c15fad2dde57b9c54c807629ef8d02cf/DEBIAN/postinst.in#L173
> 
> which runs with system python on install. And installs amdsmi into `/usr/local/lib/python3.*/dist-packages/`. Which conda of course doesn't use.

It is working! Thanks
