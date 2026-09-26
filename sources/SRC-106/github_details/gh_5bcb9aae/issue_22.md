# [Issue #22] [Issue]: Power info and energy counter APIs always return the same info

source: https://github.com/ROCm/amdsmi/issues/22
state: closed | updated: 2024-05-21T16:45:58Z
labels: 

## 正文

### Problem Description

# What I'm doing

I'm trying to measure the power and energy consumption of four MI100 accelerators on the node. It has multiple versions of ROCm installed (e.g., `/opt/rocm-5.7.1`, `/opt/rocm-6.0.2`), and I'm running the Python bindings of amdsmi like this:

```
$ cd /opt/rocm-6.0.2/share/amd_smi  # or /opt/rocm-5.7.1/share/amd_smi
$ python
>>> import amdsmi
>>> amdsmi
<module 'amdsmi' from '/opt/rocm-6.0.2/share/amd_smi/amdsmi/__init__.py'>
```

To utilize the GPU, I wrote a simple script that does matrix multiplication repetitively using PyTorch `2.2.2+rocm5.7`.
It runs for about 15 seconds on one GPU (and much longer if I disable GPUs).

To look at power and energy, I'm running the following in the Python interpreter:
```python
import amdsmi

amdsmi.amdsmi_init()
handles = amdsmi.amdsmi_get_processor_handles()
while True:
    for i in range(4):
        print(f"{i}: {amdsmi.amdsmi_get_power_info(handles[i])}")
# or
while True:
    for i in range(4):
        print(f"{i}: {amdsmi.amdsmi_get_energy_count(handles[i])}")
```

At the same time, I have `watch` up on another tmux pane, which is spawning `amd-smi` continuously. Notice that it's using amdsmi distributed as part of ROCm 6.0.2:

```sh
$ which amd-smi
/opt/rocm-6.0.2/bin/amd-smi

$ watch -n0.1 amd-smi metric -pE
GPU: 0
POWER:
    CURRENT_POWER: 33 W
    CURRENT_GFX_VOLTAGE: N/A
    CURRENT_SOC_VOLTAGE: N/A
    CURRENT_MEM_VOLTAGE: N/A
    POWER_LIMIT: 290 W
    POWER_MANAGEMENT: ENABLED
    THROTTLE_STATUS: UNTHROTTLED
ENERGY:
    TOTAL_ENERGY_CONSUMPTION: 131.426 J

GPU: 1
POWER:
    CURRENT_POWER: 34 W
    CURRENT_GFX_VOLTAGE: N/A
    CURRENT_SOC_VOLTAGE: N/A
    CURRENT_MEM_VOLTAGE: N/A
    POWER_LIMIT: 290 W
    POWER_MANAGEMENT: ENABLED
    THROTTLE_STATUS: UNTHROTTLED
ENERGY:
    TOTAL_ENERGY_CONSUMPTION: 131.426 J

GPU: 2
POWER:
    CURRENT_POWER: 34 W
    CURRENT_GFX_VOLTAGE: N/A
    CURRENT_SOC_VOLTAGE: N/A
    CURRENT_MEM_VOLTAGE: N/A
    POWER_LIMIT: 290 W
    POWER_MANAGEMENT: ENABLED
    THROTTLE_STATUS: UNTHROTTLED
ENERGY:
    TOTAL_ENERGY_CONSUMPTION: 131.426 J

GPU: 3
POWER:
    CURRENT_POWER: 34 W
    CURRENT_GFX_VOLTAGE: N/A
    CURRENT_SOC_VOLTAGE: N/A
    CURRENT_MEM_VOLTAGE: N/A
    POWER_LIMIT: 290 W
    POWER_MANAGEMENT: ENABLED
    THROTTLE_STATUS: UNTHROTTLED
ENERGY:
    TOTAL_ENERGY_CONSUMPTION: 131.426 J
```

# Problems

## ROCm 6.0.2

### Power API

Through the Python interpreter, the return value of the power API **never changes**:
```
{'current_socket_power': 34, 'average_socket_power': 34, 'gfx_voltage': 65535, 'soc_voltage': 65535, 'mem_voltage': 65535, 'power_limit': 290}
```
It's the exact same return value regardless of how many time I call it (in the `while` loop).
However, when I look at the `watch -n0.1 amd-smi metric -pE` monitor at the same time, I can see that the power (`CURRENT_POWER`) it reports fluctuates up and down slightly (34 W, 33 W, 35 W, 34 W, ...).
It feel as though the return value of `amdsmi_get_power_info` is cached somewhere inside the process and it never gets updated, whereas `watch` spawns a new `amd-smi` process every time, loading in updated values.

### Energy API

Through the Python interpreter, the return value of the energy API **never changes**:
```
{'power': 8589935, 'counter_resolution': 15.300000190734863, 'timestamp': 4951525529249129}
```
It's the exact same return value regardless of how many time I call it (in the `while` loop).
This time, even the numbers shown in `watch -n0.1 amd-smi metric -pE` never change!

Side note: I suppose users should multiply `power` and `counter_resolution` to get micro-Joules. I think this API is quite unintuitive.

## ROCm 5.7.1

### Power API

There is no problem! Even when I'm running the exact same code, I can see that the power draw of one of the four GPUs maxing out:
```
0: {'average_socket_power': 292, 'gfx_voltage': 900, 'soc_voltage': 0, 'mem_voltage': 0, 'power_limit': 290}
1: {'average_socket_power': 33, 'gfx_voltage': 662, 'soc_voltage': 0, 'mem_voltage': 0, 'power_limit': 290}
2: {'average_socket_power': 34, 'gfx_voltage': 662, 'soc_voltage': 0, 'mem_voltage': 0, 'power_limit': 290}
3: {'average_socket_power': 33, 'gfx_voltage': 656, 'soc_voltage': 0, 'mem_voltage': 0, 'power_limit': 290}
0: {'average_socket_power': 283, 'gfx_voltage': 912, 'soc_voltage': 0, 'mem_voltage': 0, 'power_limit': 290}
1: {'average_socket_power': 32, 'gfx_voltage': 662, 'soc_voltage': 0, 'mem_voltage': 0, 'power_limit': 290}
2: {'average_socket_power': 34, 'gfx_voltage': 662, 'soc_voltage': 0, 'mem_voltage': 0, 'power_limit': 290}
3: {'average_socket_power': 32, 'gfx_voltage': 650, 'soc_voltage': 0, 'mem_voltage': 0, 'power_limit': 290}
```

### Energy API

Same problem as ROCm 6.0.2 (return value never changing).

---

### Operating System

Rocky Linux 9.1 (Blue Onyx)

### CPU

AMD EPYC 7V13 64-Core Processor

### GPU

AMD Instinct MI100

### ROCm Version

ROCm 6.0.2, ROCm 5.7.1

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support
<details>

<summary>Click to expand</summary>

```
$ /opt/rocm-6.0.2/bin/rocminfo --support
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
  Name:                    AMD EPYC 7V13 64-Core Processor    
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD EPYC 7V13 64-Core Processor    
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
  Max Clock Freq. (MHz):   2450                               
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
      Size:                    263439732(0xfb3c574) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    263439732(0xfb3c574) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    263439732(0xfb3c574) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    AMD EPYC 7V13 64-Core Processor    
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD EPYC 7V13 64-Core Processor    
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
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2450                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    264211508(0xfbf8c34) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    264211508(0xfbf8c34) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    264211508(0xfbf8c34) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 3                  
*******                  
  Name:                    gfx908                             
  Uuid:                    GPU-e39e9bc78ccf0280               
  Marketing Name:                                             
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
  BDFID:                   58112                              
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
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    33538048(0x1ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
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
Agent 4                  
*******                  
  Name:                    gfx908                             
  Uuid:                    GPU-eb011b86ac1d9194               
  Marketing Name:                                             
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
    L1:                      16(0x10) KB                        
    L2:                      8192(0x2000) KB                    
  Chip ID:                 29580(0x738c)                      
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1502                               
  BDFID:                   49920                              
  Internal Node ID:        3                                  
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
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    33538048(0x1ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
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
Agent 5                  
*******                  
  Name:                    gfx908                             
  Uuid:                    GPU-3754a9ce7d763d1f               
  Marketing Name:                                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    4                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      8192(0x2000) KB                    
  Chip ID:                 29580(0x738c)                      
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1502                               
  BDFID:                   41728                              
  Internal Node ID:        4                                  
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
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    33538048(0x1ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
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
Agent 6                  
*******                  
  Name:                    gfx908                             
  Uuid:                    GPU-420fb9c697764214               
  Marketing Name:                                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    5                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      8192(0x2000) KB                    
  Chip ID:                 29580(0x738c)                      
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1502                               
  BDFID:                   33536                              
  Internal Node ID:        5                                  
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
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    33538048(0x1ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
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

</details>

### Additional Information

_No response_

## 评论 (5)

### jaywonchung · 2024-05-20

@marifamd @dmitrii-galantsev
Is there something I can do to help make progress on this issue? Has this been reproduced from the maintainer's end?

### marifamd · 2024-05-21

@jaywonchung Sorry for the late response. I believe this was a bug with how we called our gpu_metrics struct and didn't force gpu_metrics to update unconditionally. This should be resolved in ROCm 6.1+ branches. This is the commit that resolved your issue: 78074d7d77298446b34856b361e86096031fb6b2

### marifamd · 2024-05-21

Sorry, hit the wrong comment button :). If you update to the 6.1 release you should see this resolved.

### jaywonchung · 2024-05-21

Hi @marifamd, thanks a lot for your response! Would that require a whole ROCm update to 6.1, or is there some possibility that it will still work if I just update the AMDSMI library to the version embedded inside the ROCm 6.1 branch?

It's just that it was slightly confusing which versioning to follow, since according to #21 ROCm, the AMDSMI library, and AMDSMI tools are versioned separately, but GitHub releases/tags seem to only exist for new ROCm versions.

Thanks.

### marifamd · 2024-05-21

Since we are packaged and aligned with ROCm releases **I would recommend updating to 6.1**, this ensures you are on a stable build that is synced with the amdgpu driver. The alternative would be building and installing and overwriting the current version within the ROCm version you installed currently, which is not worth the effort vs using the package managed ROCm release.

To clarify on the versioning, the AMD-SMI Library and AMD-SMI CLI are versioned separately from ROCm for good practice as they are separate projects that we track internally. For the end user we align to the ROCm release schedule.
