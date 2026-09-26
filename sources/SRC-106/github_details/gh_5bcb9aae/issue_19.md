# [Issue #19] [Issue]: ROCm 6.1: ModuleNotFoundError: No module named 'yaml' 

source: https://github.com/ROCm/amdsmi/issues/19
state: closed | updated: 2025-01-28T22:46:49Z
labels: Under Investigation

## 正文

### Problem Description

installed rocm 6.1, getting this error

OS:
NAME="Ubuntu"
VERSION="22.04.4 LTS (Jammy Jellyfish)"
CPU: 
model name      : AMD Ryzen 9 3950X 16-Core Processor
GPU:
  Name:                    AMD Ryzen 9 3950X 16-Core Processor
  Marketing Name:          AMD Ryzen 9 3950X 16-Core Processor
  Name:                    gfx1100                            
  Marketing Name:          Radeon RX 7900 XTX                 
      Name:                    amdgcn-amd-amdhsa--gfx1100         


> amd-smi 
ModuleNotFoundError: No module named 'yaml'

### Operating System

22.04.4 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 9 3950X 16-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.0.0

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

^[[37mROCk module version 6.7.0 is loaded^[[0m
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.13
Runtime Ext Version:     1.4
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
  Name:                    AMD Ryzen 9 3950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 3950X 16-Core Processor
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
  Max Clock Freq. (MHz):   3500                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    131797452(0x7db11cc) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131797452(0x7db11cc) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131797452(0x7db11cc) KB            
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
  Uuid:                    GPU-fff29e921a701d68               
  Marketing Name:          Radeon RX 7900 XTX                 
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
  Max Clock Freq. (MHz):   2371                               
  BDFID:                   3328                               
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
  Packet Processor uCode:: 92                                 
  SDMA engine uCode::      20                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB             
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

## 评论 (9)

### marifamd · 2024-04-23

Hi @brettkoonce do you have PyYAML installed?

Install via ubuntu package manager:
```
sudo apt install python3-yaml
``` 
Or you could install via python
```
python3 -m pip install 'PyYAML>=5.1'
``` 

Do you have any logs of the initial install, I would be curious to see if/where the pip query to install PyYAML failed.

### brettkoonce · 2024-04-24

My install included the first package:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-yaml is already the newest version (5.4.1-1ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 34 not upgraded.

but the second command, eg 
    python3 -m pip install 'PyYAML>=5.1'
got things working, thanks!

Here is the installer I used:

https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html

### dmitrii-galantsev · 2024-04-26

@brettkoonce 

as a follow up.. does it simply work if you run as sudo? I'm expecting that it's different python environments. And the user one doesn't pick up `python3-yaml`.

Honestly this has been a headache for us.

### brettkoonce · 2024-04-26

@dmitrii-galantsev see https://github.com/google/jax/issues/20955 for a better description of how I am getting here!

### dmitrii-galantsev · 2024-06-04

@brettkoonce hey sorry for double ping, reposting what i posted under jax:

Hm! It's likely you have to install it manually because managing python packages is very tricky...

```bash
cd /opt/rocm/share/amd_smi
python3 -m pip install .
```

Reopening because we need to add this in the readme or something.

### cjao · 2024-12-31

Sorry to comment on old thread -- but can we also print the actual import error in the [second exception handler](https://github.com/ROCm/amdsmi/blob/amd-staging/amdsmi_cli/amdsmi_cli.py#L60)? Something as simple as
```
--- a/amdsmi_cli.py	2024-12-30 21:46:11.853894028 -0500
+++ b/amdsmi_cli.py	2024-12-30 21:46:26.892893965 -0500
@@ -59,6 +59,7 @@
         from amdsmi import amdsmi_interface
         from amdsmi import amdsmi_exception
     except ImportError as e:
+        print(f"Unhandled import error: {e}")
         print(f"Still couldn't import 'amdsmi related scripts'. Make sure it's installed in {additional_path}")
         sys.exit(1)
```

would clarify the error:
```
$ amd-smi --help

Unhandled import error: No module named 'yaml'
Still couldn't import 'amdsmi related scripts'. Make sure it's installed in /usr/bin/../libexec/amdsmi_cli
```

### da-phil · 2025-01-28

I'm using rocm-6.3.1 and  ran into the same issue on Ubuntu 24.04, although "python3-yaml" was already installed (version 6.0.1) which should fulfill the requirement of "PyYAML>=5.1".
However only when I installed the latest version (6.0.2) via pip, `amdsmi_cli` would work. So something is weird here.

I also like @cjao's suggestion of being more verbose in the import exception handling, which should make it easier to pinpoint possible error sources.

### marifamd · 2025-01-28

I added the verbose handling, it will be there in the 6.4 release. Also an FYI, we managed to drop YAML as a dependency in the upcoming 6.4 release.

### da-phil · 2025-01-28

Awesome, thank you!
