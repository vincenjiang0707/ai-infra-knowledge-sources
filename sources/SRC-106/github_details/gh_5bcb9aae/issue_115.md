# [Issue #115] [Issue]: Energy counter goes backward in some conditions (Rust interface)

source: https://github.com/ROCm/amdsmi/issues/115
state: closed | updated: 2026-01-12T15:01:42Z
labels: Under Investigation, status: assessed

## 正文

### Problem Description

Rust code (a whole tokio-based app has been omitted):
```rs
if let Ok((energy, resolution, amd_t)) = amdsmi_get_energy_count(handle) {
    log::debug!("amdsmi_get_energy_count({handle:p}) returned (energy={energy}, res={resolution}, t={amd_t}); energy*res={}", (energy*resolution as u64));
}
```

Output:
```rs
[2025-08-29T10:24:30Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cf110) returned (energy=4750896266, res=15.3, t=1712024507665); energy*res=71263443990
[2025-08-29T10:24:30Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cedd0) returned (energy=4975767868, res=15.3, t=1712024418738); energy*res=74636518020
[2025-08-29T10:24:30Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b59c610) returned (energy=4734149698, res=15.3, t=1712027255611); energy*res=71012245470
[2025-08-29T10:24:30Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cef70) returned (energy=4801658003, res=15.3, t=1712027134583); energy*res=72024870045
[2025-08-29T10:24:31Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cf110) returned (energy=4736943791, res=15.3, t=1713024458751); energy*res=71054156865
[2025-08-29T10:24:31Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cef70) returned (energy=4736943791, res=15.3, t=1713024458751); energy*res=71054156865
[2025-08-29T10:24:31Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b59c610) returned (energy=4804490929, res=15.3, t=1713026508503); energy*res=72067363935
[2025-08-29T10:24:31Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cedd0) returned (energy=4753708700, res=15.3, t=1713026706714); energy*res=71305630500
[2025-08-29T10:24:32Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cef70) returned (energy=4981660158, res=15.3, t=1714024488057); energy*res=74724902370
[2025-08-29T10:24:32Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cf110) returned (energy=4981660158, res=15.3, t=1714024488057); energy*res=74724902370
[2025-08-29T10:24:32Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cedd0) returned (energy=4807326799, res=15.3, t=1714026534077); energy*res=72109901985
[2025-08-29T10:24:32Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b59c610) returned (energy=4807326799, res=15.3, t=1714026534077); energy*res=72109901985
[2025-08-29T10:24:33Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cef70) returned (energy=4984605886, res=15.3, t=1715024523769); energy*res=74769088290
[2025-08-29T10:24:33Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cf110) returned (energy=4742547811, res=15.3, t=1715024442851); energy*res=71138217165
[2025-08-29T10:24:33Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cedd0) returned (energy=4810162706, res=15.3, t=1715026581741); energy*res=72152440590
[2025-08-29T10:24:33Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b59c610) returned (energy=4810162706, res=15.3, t=1715026581741); energy*res=72152440590
[2025-08-29T10:24:34Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b59c610) returned (energy=4987552062, res=15.3, t=1716024553825); energy*res=74813280930
[2025-08-29T10:24:34Z DEBUG plugin_amd_gpu::amd::probe] amdsmi_get_energy_count(0x56254b5cf110) returned (energy=4812992425, res=15.3, t=1716024437876); energy*res=72194886375

```

Compiler with commit `8e454950ef9713b4316ccea5dcf06983ad5ea822` (because the current main does not compile anymore).
Either something is wrong with the Rust interface, or with the underlying lib.

Even weirder: as reported by @victoryeagle77, using `valgrind` on the Rust binary makes the problem disappear… 

### Operating System

Debian 11.11

### CPU

Intel Xeon Platinum 8568Y+ (Emerald Rapids), x86_64, 2 CPUs/node, 48 cores/CPU

### GPU

4x AMD Instinct MI210 (64 GiB)

### ROCm Version

3.0.0+94441cb

### ROCm Component

amdsmi

### Steps to Reproduce

1. install amdsmi version 8e454950ef9713b4316ccea5dcf06983ad5ea822 (manually)
2. for each device, run a loop with a code that calls `amdsmi_get_energy_count`
3. find that the energy counter decreases sometimes, which should not be possible since it's an "accumulator" according to the docs 😅 

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>See more</summary>

```
ROCk module version 6.10.5 is loaded
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
  Name:                    INTEL(R) XEON(R) PLATINUM 8568Y+   
  Uuid:                    CPU-XX                             
  Marketing Name:          INTEL(R) XEON(R) PLATINUM 8568Y+   
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
  Max Clock Freq. (MHz):   4000                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            96                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    263656996(0xfb71624) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    263656996(0xfb71624) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    263656996(0xfb71624) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    263656996(0xfb71624) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    INTEL(R) XEON(R) PLATINUM 8568Y+   
  Uuid:                    CPU-XX                             
  Marketing Name:          INTEL(R) XEON(R) PLATINUM 8568Y+   
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
  Max Clock Freq. (MHz):   4000                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    264169592(0xfbee878) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    264169592(0xfbee878) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    264169592(0xfbee878) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    264169592(0xfbee878) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 3                  
*******                  
  Name:                    gfx90a                             
  Uuid:                    GPU-0a03eb1960c2df8d               
  Marketing Name:          AMD Instinct MI210                 
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
  Chip ID:                 29711(0x740f)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   1700                               
  BDFID:                   16384                              
  Internal Node ID:        2                                  
  Compute Unit:            104                                
  SIMDs per CU:            4                                  
  Shader Engines:          8                                  
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
  Packet Processor uCode:: 92                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    67092480(0x3ffc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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
  Name:                    gfx90a                             
  Uuid:                    GPU-3f8909e1fbd7df71               
  Marketing Name:          AMD Instinct MI210                 
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
  Chip ID:                 29711(0x740f)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   1700                               
  BDFID:                   22528                              
  Internal Node ID:        3                                  
  Compute Unit:            104                                
  SIMDs per CU:            4                                  
  Shader Engines:          8                                  
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
  Packet Processor uCode:: 92                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    67092480(0x3ffc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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
  Name:                    gfx90a                             
  Uuid:                    GPU-f68d5df9da6a57fa               
  Marketing Name:          AMD Instinct MI210                 
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
  Chip ID:                 29711(0x740f)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   1700                               
  BDFID:                   50176                              
  Internal Node ID:        4                                  
  Compute Unit:            104                                
  SIMDs per CU:            4                                  
  Shader Engines:          8                                  
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
  Packet Processor uCode:: 92                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    67092480(0x3ffc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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
  Name:                    gfx90a                             
  Uuid:                    GPU-b07b8dcc44911021               
  Marketing Name:          AMD Instinct MI210                 
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
  Chip ID:                 29711(0x740f)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   1700                               
  BDFID:                   56320                              
  Internal Node ID:        5                                  
  Compute Unit:            104                                
  SIMDs per CU:            4                                  
  Shader Engines:          8                                  
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
  Packet Processor uCode:: 92                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    67092480(0x3ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    67092480(0x3ffc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
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

## 评论 (9)

### ppanchad-amd · 2025-09-02

Hi @TheElectronWill. Internal ticket has been created investigate this issue. Thanks!

### darren-amd · 2025-09-02

Hi @TheElectronWill,

Thanks for reporting the issue. I gave it a try on this commit: https://github.com/ROCm/amdsmi/commit/51a44bc0c456884f3f0c901cfa2aa3e0095a7d01 and was unable to reproduce the issue. I ran this on an MI210 as well and the energy level appears to be non-decreasing. Could you give it a try on the newer commit and see if the issue persists on your end? Thanks!

Here's the sample I ran:
```
// Copyright (C) 2024 Advanced Micro Devices. All rights reserved.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy of
// this software and associated documentation files (the "Software"), to deal in
// the Software without restriction, including without limitation the rights to
// use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
// the Software, and to permit persons to whom the Software is furnished to do so,
// subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
// FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
// COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
// IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
// CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
//

use amdsmi::*;

fn main() {
    // Initialize the AMD SMI library
    if let Err(e) = amdsmi_init(AmdsmiInitFlagsT::AmdsmiInitAmdGpus) {
        eprintln!("Failed to initialize AMD SMI: {}", e);
        return;
    }

    // Get socket handles
    let socket_handles = match amdsmi_get_socket_handles() {
        Ok(handles) => handles,
        Err(e) => {
            eprintln!("Failed to get socket handles: {}", e);
            amdsmi_shut_down().expect("Failed to shutdown AMD SMI");
            return;
        }
    };

    for socket_handle in socket_handles {
        // Get processor handles for each socket handle
        let processor_handles = match amdsmi_get_processor_handles(socket_handle) {
            Ok(handles) => handles,
            Err(e) => {
                eprintln!(
                    "Failed to get processor handles for socket {:?}: {}",
                    socket_handle, e
                );
                continue;
            }
        };

        for processor_handle in processor_handles {
                  println!("\n--- Fetching Energy Count 100 times ---");
            let mut last_energy: Option<u64> = None;

            for i in 0..100 {
                match amdsmi_get_energy_count(processor_handle) {
                    Ok((energy, resolution, timestamp)) => {
						let energy_diff = if let Some(prev_energy) = last_energy {
                            Some(energy.checked_sub(prev_energy).unwrap_or_else(|| {
                                u64::MAX - prev_energy + energy + 1
                            }))
                        } else {
                            None
                        };
                        print!("amdsmi_get_energy_count({processor_handle:p}) returned (energy={energy}, res={resolution}, t={timestamp}); energy*res={}", (energy*resolution as u64));
						match energy_diff {
                            Some(diff) => println!(" {} ", diff),
                            None => println!("N/A "),
                        }
						last_energy = Some(energy);
                    }
                    Err(e) => {
                        eprintln!("  Loop {}: Failed to get energy count: {}", i, e);
                    }
                }
            }
            println!("--- End of Energy Count Loop ---\n");

            println!();
        }
    }

    // Shutdown the AMD SMI library
    if let Err(e) = amdsmi_shut_down() {
        eprintln!("Failed to shutdown AMD SMI: {}", e);
    }
}
```

### victoryeagle77 · 2025-09-12

It is normal to not have any error with basic code like this, the problem appears when we use tokio task and synchronous/asynchronous mecanism (we try to make minimal code to give you, to reproduce the metrics collection problem).
PS: We don't know if this is generalized for all metrics, for which the problem is not visible because we don't need a counterDiff on them.

### victoryeagle77 · 2025-09-16

The following code isn't wonderful, but it reproduces the problem perfectly. We minimize the code to simplify the collection of metrics issues with the aim of showing you a sample of the problem we have while developing on our open source project Alumet, for which we are currently developing an AMD plugin to collect information related to GPUs here : https://github.com/alumet-dev/alumet/tree/develop/plugin-amd-gpu/plugins/amd-gpu

```rust
use amdsmi::*;
use std::{
    io,
    sync::atomic::{AtomicUsize, Ordering}
};
use tokio::{
    runtime::Runtime,
    time::{sleep, Duration},
    signal
};

struct ManagedDevice(AmdsmiProcessorHandle);

unsafe impl Send for ManagedDevice {}

impl ManagedDevice {
    fn as_ptr(&self) -> AmdsmiProcessorHandle {
        self.0
    }
}

fn build_normal_runtime(worker_threads: Option<usize>) -> io::Result<Runtime> {
    let mut builder = tokio::runtime::Builder::new_multi_thread();
    builder.enable_all().thread_name_fn(|| {
        static ATOMIC_ID: AtomicUsize = AtomicUsize::new(0);
        let id = ATOMIC_ID.fetch_add(1, Ordering::SeqCst);
        format!("normal-worker-{id}")
    });
    if let Some(n) = worker_threads {
        builder.worker_threads(n);
    }
    builder.build()
}

async fn run_amd_source(processor_handle: ManagedDevice) {
    let bus_id = amdsmi_get_gpu_device_bdf(processor_handle.as_ptr()).expect("Failed to get bus ID: {e}");
    let mut last_energy = None;

    loop {
        if let Ok((energy, _res, timestamp)) = amdsmi_get_energy_count(processor_handle.as_ptr()) {
            let energy_diff = last_energy.map(|prev| {
                energy.checked_sub(prev).unwrap_or_else(|| u64::MAX - prev + energy + 1)
            });
            println!(
                "ptr = {:p}, bus={}, energy = {}, timestamp = {}, diff = {:?}",
                &processor_handle,
                bus_id,
                energy as f64 / 1e6,
                timestamp / 1_000_000,
                energy_diff
            );
            last_energy = Some(energy);
        }
        sleep(Duration::from_secs(1)).await;
    }
}

fn main() -> io::Result<()> {
    let rt = build_normal_runtime(Some(4))?;
    amdsmi_init(AmdsmiInitFlagsT::AmdsmiInitAmdGpus).expect("Failed to initialize AMD SMI");

    let mut processor_handles = Vec::new();
    for socket_handle in amdsmi_get_socket_handles().expect("Failed to get socket handles") {
        if let Ok(handles) = amdsmi_get_processor_handles(socket_handle) {
            for raw_handle in handles {
                if !raw_handle.is_null() {
                   processor_handles.push(ManagedDevice(raw_handle));
                }
            }
        }
    }

    rt.block_on(async {
        for processor_handle in processor_handles {
            tokio::spawn(run_amd_source(processor_handle));
        }
        signal::ctrl_c().await.expect("Failed to listen for ctrl-c");
    });

    amdsmi_shut_down().expect("Failed to shutdown AMD SMI");

    Ok(())
}
```

And the result is the following :

```text
ptr = 0x563a88890740, bus=0000:dc:00.0, energy = 160960.515936, timestamp = 57087189, diff = None
ptr = 0x563a888904c0, bus=0000:c4:00.0, energy = 160960.515936, timestamp = 57087189, diff = None
ptr = 0x563a88890040, bus=0000:40:00.0, energy = 160960.515936, timestamp = 57087189, diff = None
ptr = 0x563a888902c0, bus=0000:58:00.0, energy = 160960.515936, timestamp = 57087189, diff = None
ptr = 0x563a888902c0, bus=0000:58:00.0, energy = 160963.346769, timestamp = 57088190, diff = Some(2830833)
ptr = 0x563a888904c0, bus=0000:c4:00.0, energy = 161533.12197, timestamp = 57088191, diff = Some(572606034)
ptr = 0x563a88890740, bus=0000:dc:00.0, energy = 161533.12197, timestamp = 57088191, diff = Some(572606034)
ptr = 0x563a88890040, bus=0000:40:00.0, energy = 161533.12197, timestamp = 57088191, diff = Some(572606034)
ptr = 0x563a88890040, bus=0000:40:00.0, energy = 158582.354231, timestamp = 57089192, diff = Some(18446744070758783877)
ptr = 0x563a888904c0, bus=0000:c4:00.0, energy = 160966.181434, timestamp = 57089192, diff = Some(18446744073142611080)
ptr = 0x563a888902c0, bus=0000:58:00.0, energy = 160966.181434, timestamp = 57089192, diff = Some(2834665)
ptr = 0x563a88890740, bus=0000:dc:00.0, energy = 166082.20861, timestamp = 57089192, diff = Some(4549086640)
ptr = 0x563a88890040, bus=0000:40:00.0, energy = 161538.786465, timestamp = 57090192, diff = Some(2956432234)
ptr = 0x563a88890740, bus=0000:dc:00.0, energy = 166085.092836, timestamp = 57090194, diff = Some(2884226)
ptr = 0x563a888902c0, bus=0000:58:00.0, energy = 160969.016522, timestamp = 57090194, diff = Some(2835088)
ptr = 0x563a888904c0, bus=0000:c4:00.0, energy = 160969.016522, timestamp = 57090194, diff = Some(2835088)
ptr = 0x563a88890740, bus=0000:dc:00.0, energy = 161541.625744, timestamp = 57091195, diff = Some(18446744069166084524)
ptr = 0x563a88890040, bus=0000:40:00.0, energy = 161541.625744, timestamp = 57091195, diff = Some(2839279)
ptr = 0x563a888904c0, bus=0000:c4:00.0, energy = 160971.851184, timestamp = 57091196, diff = Some(2834662)
ptr = 0x563a888902c0, bus=0000:58:00.0, energy = 160971.851184, timestamp = 57091196, diff = Some(2834662)
ptr = 0x563a88890040, bus=0000:40:00.0, energy = 166090.861452, timestamp = 57092196, diff = Some(4549235708)
ptr = 0x563a88890740, bus=0000:dc:00.0, energy = 166090.861452, timestamp = 57092196, diff = Some(4549235708)
ptr = 0x563a888904c0, bus=0000:c4:00.0, energy = 160974.682439, timestamp = 57092197, diff = Some(2831255)
ptr = 0x563a888902c0, bus=0000:58:00.0, energy = 160974.682439, timestamp = 57092197, diff = Some(2831255)
ptr = 0x563a88890040, bus=0000:40:00.0, energy = 161547.292739, timestamp = 57093197, diff = Some(18446744069165982903)
ptr = 0x563a88890740, bus=0000:dc:00.0, energy = 166093.748865, timestamp = 57093198, diff = Some(2887413)
ptr = 0x563a888902c0, bus=0000:58:00.0, energy = 160977.516887, timestamp = 57093199, diff = Some(2834448)
ptr = 0x563a888904c0, bus=0000:c4:00.0, energy = 158593.419713, timestamp = 57093199, diff = Some(18446744071328288890)
```

And we can sometimes observe here, for the same device, a value lower than the next (which should not be the case), and naturally an overflow when we make the difference between them.

### victoryeagle77 · 2025-10-29

Hi I hope you're fine.
I was just wondering if you would have the time to show me the problem I described here, Or if you even had any ideas about it.

### victoryeagle77 · 2025-12-22

Hi I hope you're fine.
Since you changed something for the new **rocm** releases (v7.0.0 or 7.0.1 I don't know), The problem described above no longer occurs, thanks. I'd just like to know which packages now include this modification. For example, I tried running my program with the amd-smi-lib.x86_64 package from Red Hat 9.5, but I'm still having the problem. However, compiling from source resolves the issue.



### darren-amd · 2025-12-22

Hi @victoryeagle77,

Sorry for the delayed response. It looks like this commit: https://github.com/ROCm/rocm-systems/commit/62d3348c9e8b2a75fcfe3fede3dfb6b298812d56 addresses the issue with energy counters. This is included post ROCm 7, so installing the latest release for RHEL by following the [Installation Instructions](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#rocm-installation) would include the fix, thanks!

### TheElectronWill · 2025-12-29

Hello,
I don't think that https://github.com/ROCm/rocm-systems/commit/62d3348c9e8b2a75fcfe3fede3dfb6b298812d56 is related. Our issue occurred in a multi-threaded environment in Rust. IIUC, the above commit fixes something on the Python side, which we do not use. It also renames `power` to `energy_accumulator` in the C interface, but that does virtually nothing in our case :)

### darren-amd · 2025-12-30

Thanks, looks like I linked a PR from last year by mistake. I couldn't find the exact change that fixed the issue, but I can confirm on latest 7.1.1 that the issue is fixed. Thanks for the report!
