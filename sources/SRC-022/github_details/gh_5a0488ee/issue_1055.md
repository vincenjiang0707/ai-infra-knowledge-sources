# [Issue #1055] [Issue]: Multi-GPU training of AMD 7900 XTX invalid device pointer

source: https://github.com/ROCm/rccl/issues/1055
state: closed | updated: 2024-02-05T23:22:17Z
labels: 

## 正文

### Problem Description

**OS:**
NAME="Ubuntu"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
**CPU:** 
Model name: AMD EPYC 7532 32-Core Processor
**GPU:**
  Name:                    AMD EPYC 7532 32-Core Processor    
  Marketing Name:          AMD EPYC 7532 32-Core Processor    
  Name:                    gfx1100                            
  Marketing Name:          Radeon RX 7900 XTX                 
      Name:                    amdgcn-amd-amdhsa--gfx1100         
  Name:                    gfx1100                            
  Marketing Name:          Radeon RX 7900 XTX                 
      Name:                    amdgcn-amd-amdhsa--gfx1100 


```
rocm-smi --showvbios
```
[Vbios version](https://www.techpowerup.com/vgabios/258435/258435)
GPU[0]: VBIOS version 113-31XFSHBS1-L02
GPU[1]: VBIOS version 113-31XFSHBS1-L02

* Tested Docker containers from rocm [Dockerhub](https://hub.docker.com/r/rocm/pytorch/tags) with the same error presented in the **Error** section:
```
rocm/pytorch:latest 
rocm/pytorch:rocm6.0_ubuntu20.04_py3.9_pytorch_2.1.1
rocm/pytorch:rocm5.7_ubuntu22.04_py3.10_pytorch_2.0.1
rocm/pytorch:rocm5.6_ubuntu20.04_py3.8_pytorch_1.12.1
```

* AMD_IOMMU and IOMMU configurations are based on the documentation as can be seen below (`cat /proc/cmdline`):
```
BOOT_IMAGE=/boot/vmlinuz-6.5.0-14-generic root=UUID=b03a4065-0eaf-4035-acf1-bf8a900ce7eb ro pcie_aspm=off amd_iommu=on iommu=pt pci=nommconf quiet splash vt.handoff=7
```
* IOMMU and ReBar are also set in the BIOS of AsRock Rack RomeD8-2T. 

* Added rccl-test and rocm_bandwidth_test results as attachments.

To reproduce the error one can use the [`pytorch_examples`](https://github.com/pytorch/examples/blob/main/distributed/ddp-tutorial-series/multigpu.py) repository. From `ddp-tutorial-series`, multigpu.py will result in the same error. An example of how to run:
```
python multigpu.py --batch_size 32 10 5
```
To get the NCCL info, I added the following line as depicted in the main() below:
```
...
def main(rank: int, world_size: int, save_every: int, total_epochs: int, batch_size: int):
    os.environ["NCCL_DEBUG"] = "INFO" ### ADDED TO SEE THE DETAILS IN THE ERROR BELOW.
    ddp_setup(rank, world_size)
    dataset, model, optimizer = load_train_objs()
    train_data = prepare_dataloader(dataset, batch_size)
    trainer = Trainer(model, train_data, optimizer, rank, save_every)
    trainer.train(total_epochs)
    destroy_process_group()
...
```
**Note:** The error in the code above is the same as the one below. However, you might notice parts relevant to PyTorch Lightning in the error below. Unfortunately, the codebase producing the output below is part of an ongoing project, so I cannot share that source code. Instead, I've shared a public code reference with which you can replicate the same error from the RCCL.

**Error:**
The issue is when I start training with DDP rccl throws an error as follows (extracted by enabling `NCCL_DEBUG` flag into the code as shown in def main() above):
```
9cce34ff6c6c:504930:504930 [0] NCCL INFO Bootstrap : Using eth0:172.17.0.2<0>
9cce34ff6c6c:504930:504930 [0] NCCL INFO NET/Plugin : Plugin load (librccl-net.so) returned 2 : librccl-net.so: cannot open shared object file: No such file or directory
9cce34ff6c6c:504930:504930 [0] NCCL INFO NET/Plugin : No plugin found, using internal implementation
9cce34ff6c6c:504930:504930 [0] NCCL INFO Kernel version: 6.5.0-14-generic
RCCL version 2.17.1+hip5.7 HEAD:cbbb3d8
/opt/conda/envs/py_3.10/lib/python3.10/site-packages/pytorch_lightning/strategies/ddp.py:428: UserWarning: Error handling mechanism for deadlock detection is uninitialized. Skipping check.
  rank_zero_warn("Error handling mechanism for deadlock detection is uninitialized. Skipping check.")
9cce34ff6c6c:505250:505250 [1] NCCL INFO Bootstrap : Using eth0:172.17.0.2<0>
9cce34ff6c6c:505250:505250 [1] NCCL INFO NET/Plugin : Plugin load (librccl-net.so) returned 2 : librccl-net.so: cannot open shared object file: No such file or directory
9cce34ff6c6c:505250:505250 [1] NCCL INFO NET/Plugin : No plugin found, using internal implementation
9cce34ff6c6c:505250:505250 [1] NCCL INFO Kernel version: 6.5.0-14-generic
9cce34ff6c6c:505250:505433 [1] NCCL INFO NET/IB : No device found.
9cce34ff6c6c:505250:505433 [1] NCCL INFO NET/Socket : Using [0]eth0:172.17.0.2<0>
9cce34ff6c6c:505250:505433 [1] NCCL INFO Using network Socket
9cce34ff6c6c:505250:505433 [1] NCCL INFO rocm_smi_lib: version 5.0.0.0
9cce34ff6c6c:505250:505433 [1] NCCL INFO Setting affinity for GPU 1 to ffffffff,ffffffff
9cce34ff6c6c:505250:505433 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0 comm 0x1725baa0 nRanks 02 busId 3000
9cce34ff6c6c:505250:505433 [1] NCCL INFO P2P Chunksize set to 131072
9cce34ff6c6c:505250:505433 [1] NCCL INFO Channel 00/0 : 1[3000] -> 0[83000] via P2P/IPC comm 0x1725baa0 nRanks 02
9cce34ff6c6c:505250:505433 [1] NCCL INFO Channel 01/0 : 1[3000] -> 0[83000] via P2P/IPC comm 0x1725baa0 nRanks 02

9cce34ff6c6c:505250:505433 [1] /mnt/ubuntu/software/rocm/rccl/build/hipify/src/transport/p2p.cc:228 NCCL WARN Cuda failure 'invalid device pointer'
9cce34ff6c6c:505250:505433 [1] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/transport/p2p.cc:342 -> 1
9cce34ff6c6c:505250:505433 [1] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/transport.cc:160 -> 1
9cce34ff6c6c:505250:505433 [1] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/init.cc:1270 -> 1
9cce34ff6c6c:505250:505433 [1] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/init.cc:1501 -> 1
9cce34ff6c6c:505250:505433 [1] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]
9cce34ff6c6c:505250:505250 [1] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/group.cc:439 -> 1
9cce34ff6c6c:505250:505250 [1] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/group.cc:118 -> 1
9cce34ff6c6c:505250:505438 [1] NCCL INFO [Service thread] Connection closed by localRank 1
9cce34ff6c6c:505250:505250 [1] NCCL INFO comm 0x1725baa0 rank 1 nranks 2 cudaDev 1 busId 3000 - Abort COMPLETE

9cce34ff6c6c:504930:505428 [0] NCCL INFO NET/IB : No device found.
9cce34ff6c6c:504930:505428 [0] NCCL INFO NET/Socket : Using [0]eth0:172.17.0.2<0>
9cce34ff6c6c:504930:505428 [0] NCCL INFO Using network Socket
9cce34ff6c6c:504930:505428 [0] NCCL INFO rocm_smi_lib: version 5.0.0.0
9cce34ff6c6c:504930:505428 [0] NCCL INFO Setting affinity for GPU 0 to ffffffff,ffffffff
9cce34ff6c6c:504930:505428 [0] NCCL INFO Channel 00/02 :    0   1
9cce34ff6c6c:504930:505428 [0] NCCL INFO Channel 01/02 :    0   1
9cce34ff6c6c:504930:505428 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1 comm 0x154b8e30 nRanks 02 busId 83000
9cce34ff6c6c:504930:505428 [0] NCCL INFO P2P Chunksize set to 131072
9cce34ff6c6c:504930:505428 [0] NCCL INFO Channel 00/0 : 0[83000] -> 1[3000] via P2P/IPC comm 0x154b8e30 nRanks 02
9cce34ff6c6c:504930:505428 [0] NCCL INFO Channel 01/0 : 0[83000] -> 1[3000] via P2P/IPC comm 0x154b8e30 nRanks 02

9cce34ff6c6c:504930:505428 [0] /mnt/ubuntu/software/rocm/rccl/build/hipify/src/transport/p2p.cc:228 NCCL WARN Cuda failure 'invalid device pointer'
9cce34ff6c6c:504930:505428 [0] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/transport/p2p.cc:342 -> 1
9cce34ff6c6c:504930:505428 [0] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/transport.cc:160 -> 1
9cce34ff6c6c:504930:505428 [0] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/init.cc:1270 -> 1
9cce34ff6c6c:504930:505428 [0] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/init.cc:1501 -> 1
9cce34ff6c6c:504930:505428 [0] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]
9cce34ff6c6c:504930:504930 [0] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/group.cc:439 -> 1
9cce34ff6c6c:504930:504930 [0] NCCL INFO /mnt/ubuntu/software/rocm/rccl/build/hipify/src/group.cc:118 -> 1
9cce34ff6c6c:504930:505437 [0] NCCL INFO [Service thread] Connection closed by localRank 0
9cce34ff6c6c:504930:504930 [0] NCCL INFO comm 0x154b8e30 rank 0 nranks 2 cudaDev 0 busId 83000 - Abort COMPLETE
```

- The model trains with a single 7900 XTX perfectly well. The same code works with 6 of MI25 perfectly well. In addition, the code works as multiple GPUs with other GPU brands without any problems.

- I tried to recompile RCCL to solve the problem since the error seems to be related p2p.cc. Same issue persists.

- I tried to use NCCL flags such as `NCCL_CUMEM_ENABLE`, `NCCL_P2P_DISABLE`, `NCCL_P2P_LEVEL` flags within the code. Once I disabled P2P the training ran for a few steps then it hung. Changing P2P_LEVEL doesn't affect anything. The same `invalid device pointer` persists.

[rccl_7900_XTX.log](https://github.com/ROCm/rccl/files/13991759/rccl_7900_XTX.log)
[rbt_7900xtx.log](https://github.com/ROCm/rccl/files/13991781/rbt_7900xtx.log)

### Operating System

Ubuntu 22.04.3 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 7532 32-Core Processor    

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 5.7.0

### ROCm Component

_No response_

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
  Name:                    AMD EPYC 7532 32-Core Processor    
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD EPYC 7532 32-Core Processor    
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
  Max Clock Freq. (MHz):   2400                               
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
      Size:                    263769796(0xfb8cec4) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    263769796(0xfb8cec4) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    263769796(0xfb8cec4) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-527051e212014d03               
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
  Max Clock Freq. (MHz):   2482                               
  BDFID:                   33536                              
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
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
  Packet Processor uCode:: 510                                
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
      Segment:                 GLOBAL; FLAGS:                     
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
  Uuid:                    GPU-b07772e9c1571ad2               
  Marketing Name:          Radeon RX 7900 XTX                 
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
    L2:                      6144(0x1800) KB                    
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2482                               
  BDFID:                   768                                
  Internal Node ID:        2                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
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
  Packet Processor uCode:: 510                                
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
      Segment:                 GLOBAL; FLAGS:                     
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

--no response

## 评论 (11)

### wenkaidu · 2024-01-21

Can you check if large bar (64-bit) has been enabled on the GPUs?
"lspci -vv" should show something like below:

	Region 0: Memory at 27800000000 (64-bit, prefetchable) [size=32G]


### bankh · 2024-01-21

Hi @wenkaidu,
Thank you for your prompt reply. I enabled reBar as mentioned in the message. Sorry, I didn't include `lspci` output in my earlier message.

```
sudo update-pciids # To update the appropriate name of 7900 XTX instead of 744c
```

I checked each card by using bus |device |function.
```
sudo lspci -s "03:00.0" -vv
```
**output:**
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 31 [Radeon RX 7900 XT/7900 XTX] (rev c8) (prog-if 00 [VGA controller])
	Subsystem: XFX Limited RX-79XMERCB9 [SPEEDSTER MERC 310 RX 7900 XTX]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 313
	IOMMU group: 77
	Region 0: Memory at 7f000000000 (64-bit, prefetchable) [size=32G]
	Region 2: Memory at 7f800000000 (64-bit, prefetchable) [size=256M]
	Region 4: I/O ports at 3000 [size=256]
	Region 5: Memory at f2000000 (32-bit, non-prefetchable) [size=1M]
	Expansion ROM at f2100000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
lspci: Unable to load libkmod resources: error -2


For the second card,
```
sudo lspci -s "83:00.0" -vv
```
83:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 31 [Radeon RX 7900 XT/7900 XTX] (rev c8) (prog-if 00 [VGA controller])
	Subsystem: XFX Limited RX-79XMERCB9 [SPEEDSTER MERC 310 RX 7900 XTX]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 312
	IOMMU group: 27
	Region 0: Memory at 47000000000 (64-bit, prefetchable) [size=32G]
	Region 2: Memory at 47800000000 (64-bit, prefetchable) [size=256M]
	Region 4: I/O ports at b000 [size=256]
	Region 5: Memory at c2000000 (32-bit, non-prefetchable) [size=1M]
	Expansion ROM at c2100000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
lspci: Unable to load libkmod resources: error -2

Thank you,

### wenkaidu · 2024-01-21

Can you try install ROCm 6.0? I have only tested gfx1100 on ROCm 6.0. Please confirm amdgpu verison by:
dkms status:
amdgpu/6.3.6-1697589.22.04, 5.19.0-42-generic, x86_64: installed
amdgpu/6.3.6-1697589.22.04, 6.5.0-14-generic, x86_64: installed


### bankh · 2024-01-21

@wenkaidu 
I see. `dkms` is not installed within the rocm's Pytorch docker container. I pulled 
`rocm/pytorch:rocm6.0_ubuntu20.04_py3.9_pytorch_2.1.1` from the DockerHub. When I `apt install dkms` and check `dkms status`, there is nothing as output. I will check how to get the output that you highlighted out of the docker container and will let you know about the result.


### wenkaidu · 2024-01-21

ROCm 6.0 GPU kernel driver and firmware, amdgpu-dkms and amdgpu-dkms-firmware, must be installed on bare metal machine. Updating ROCm in docker itself is not enough.

### bankh · 2024-01-21

Yes. As far as I remember Docker containers share the kernel of the host operating system. Since the kernel was not an issue with the other cards that I have been using, I neglected these installations. I will check the documentation and go through with the installation starting from the kernel driver/ firmware, amdgpu-dkms, and amdgpu-dkms-firmware on bare metal machine. 

### bankh · 2024-01-22

Installing amdgpu-dkms on the bare metal machine and rebooting the machine solved the issue of the `invalid pointer` of RCCL in Docker container. To avoid potential misunderstandings for the people who would read this issue later, I think `apt-get` installs the aforementioned dkms firmware while installing amdgpu-dkms. There was /firmware for each GPU architecture during the installation process. I have the same result as one of the outputs that @wenkaidu shared as shown below for the host (baremetal) machine.
```
$ dkms status
```
Output
```
amdgpu/6.3.6-1697589.22.04, 6.5.0-14-generic, x86_64: installed
```
However, now the GPUs hung at some point during the training of the dummy model (pls see at the end) and despite `rocmsmi --gpureset -d {device_no}` I had some issues with the GPUs. So, I have to restart the machine. 

After looking into the repositories one more time, I am not so clear about building and installing [ROCk-Kernel-Driver's ROCM 6.0 branch](https://github.com/ROCm/ROCK-Kernel-Driver/tree/roc-6.0.x) since its documentation of the building instruction is quite poor on its repository. A standard approach to building a Linux kernel that I know is
```
$ cp /boot/config-`uname -r` .config
```
Followed by (while keeping oldconfig)
```
$ make oldconfig
```
However, I suspect this approach might bring different issues for ROCk-Kernel-Driver. **If there is proper documentation that you can suggest and explains the details of this installation that would be great.** I am also aware that I am not alone in this documentation issue since the people have issues with the [building steps](https://www.youtube.com/watch?v=NPinFkavsrk) and what I see is they prefer to build around Linux Kernel instead of this ROCk-Kernel-Driver.

Now to reproduce, multigpu.py (pytorch/examples/distributed/ddp-tutorial-series)
```
python multigpu.py --batch_size 32 10 5
```
Output:
```
b1cc0f529b57:525:525 [0] NCCL INFO Bootstrap : Using eth0:172.17.0.3<0>
b1cc0f529b57:525:525 [0] NCCL INFO NET/Plugin : Plugin load (librccl-net.so) returned 2 : librccl-net.so: cannot open shared object file: No such file or directory
b1cc0f529b57:525:525 [0] NCCL INFO NET/Plugin : No plugin found, using internal implementation
b1cc0f529b57:525:525 [0] NCCL INFO Kernel version: 6.5.0-14-generic
b1cc0f529b57:525:525 [0] NCCL INFO ROCr version 1.1
b1cc0f529b57:525:525 [0] NCCL INFO Dmabuf feature disabled without NCCL_ENABLE_DMABUF_SUPPORT=1
RCCL version 2.18.3+hip6.0 HEAD:2f6d59e+
b1cc0f529b57:526:526 [1] NCCL INFO ROCr version 1.1
b1cc0f529b57:526:526 [1] NCCL INFO Dmabuf feature disabled without NCCL_ENABLE_DMABUF_SUPPORT=1
b1cc0f529b57:526:526 [1] NCCL INFO Bootstrap : Using eth0:172.17.0.3<0>
b1cc0f529b57:526:526 [1] NCCL INFO NET/Plugin : Plugin load (librccl-net.so) returned 2 : librccl-net.so: cannot open shared object file: No such file or directory
b1cc0f529b57:526:526 [1] NCCL INFO NET/Plugin : No plugin found, using internal implementation
b1cc0f529b57:526:526 [1] NCCL INFO Kernel version: 6.5.0-14-generic
b1cc0f529b57:526:680 [1] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
b1cc0f529b57:525:679 [0] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
b1cc0f529b57:525:679 [0] NCCL INFO NET/IB : No device found.
b1cc0f529b57:526:680 [1] NCCL INFO NET/IB : No device found.
b1cc0f529b57:525:679 [0] NCCL INFO NET/Socket : Using [0]eth0:172.17.0.3<0>
b1cc0f529b57:525:679 [0] NCCL INFO Using network Socket
b1cc0f529b57:526:680 [1] NCCL INFO NET/Socket : Using [0]eth0:172.17.0.3<0>
b1cc0f529b57:526:680 [1] NCCL INFO Using network Socket
b1cc0f529b57:525:679 [0] NCCL INFO comm 0x93544d0 rank 0 nranks 2 cudaDev 0 busId 83000 commId 0xddf7a5357adcc52d - Init START
b1cc0f529b57:526:680 [1] NCCL INFO comm 0x7e7ba40 rank 1 nranks 2 cudaDev 1 busId 3000 commId 0xddf7a5357adcc52d - Init START
b1cc0f529b57:526:680 [1] NCCL INFO rocm_smi_lib: version 6.0.0.0
b1cc0f529b57:525:679 [0] NCCL INFO rocm_smi_lib: version 6.0.0.0
b1cc0f529b57:526:680 [1] NCCL INFO Setting affinity for GPU 0 to ffffffff,ffffffff
b1cc0f529b57:525:679 [0] NCCL INFO Setting affinity for GPU 1 to ffffffff,ffffffff
b1cc0f529b57:525:679 [0] NCCL INFO Channel 00/02 :    0   1
b1cc0f529b57:525:679 [0] NCCL INFO Channel 01/02 :    0   1
b1cc0f529b57:526:680 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0 comm 0x7e7ba40 nRanks 02 busId 3000
b1cc0f529b57:525:679 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1 comm 0x93544d0 nRanks 02 busId 83000
b1cc0f529b57:526:680 [1] NCCL INFO P2P Chunksize set to 131072
b1cc0f529b57:525:679 [0] NCCL INFO P2P Chunksize set to 131072
b1cc0f529b57:525:679 [0] NCCL INFO Channel 00/0 : 0[83000] -> 1[3000] via P2P/IPC comm 0x93544d0 nRanks 02
b1cc0f529b57:526:680 [1] NCCL INFO Channel 00/0 : 1[3000] -> 0[83000] via P2P/IPC comm 0x7e7ba40 nRanks 02
b1cc0f529b57:525:679 [0] NCCL INFO Channel 01/0 : 0[83000] -> 1[3000] via P2P/IPC comm 0x93544d0 nRanks 02
b1cc0f529b57:526:680 [1] NCCL INFO Channel 01/0 : 1[3000] -> 0[83000] via P2P/IPC comm 0x7e7ba40 nRanks 02
b1cc0f529b57:525:679 [0] NCCL INFO Connected all rings comm 0x93544d0 nRanks 02 busId 83000
b1cc0f529b57:526:680 [1] NCCL INFO Connected all rings comm 0x7e7ba40 nRanks 02 busId 3000
b1cc0f529b57:525:679 [0] NCCL INFO Connected all trees
b1cc0f529b57:526:680 [1] NCCL INFO Connected all trees
b1cc0f529b57:526:680 [1] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 256 | 256
b1cc0f529b57:526:680 [1] NCCL INFO 2 coll channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
b1cc0f529b57:525:679 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 256 | 256
b1cc0f529b57:525:679 [0] NCCL INFO 2 coll channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
b1cc0f529b57:525:679 [0] NCCL INFO MSCCL: No external scheduler found, using internal implementation
b1cc0f529b57:526:680 [1] NCCL INFO MSCCL: No external scheduler found, using internal implementation
b1cc0f529b57:525:679 [0] NCCL INFO Using MSCCL files from /opt/rocm/lib/../share/rccl/msccl-algorithms
b1cc0f529b57:526:680 [1] NCCL INFO Using MSCCL files from /opt/rocm/lib/../share/rccl/msccl-algorithms
b1cc0f529b57:526:680 [1] NCCL INFO MSCCL: Initialization finished, localSize 400
b1cc0f529b57:525:679 [0] NCCL INFO MSCCL: Initialization finished, localSize 400
b1cc0f529b57:526:680 [1] NCCL INFO comm 0x7e7ba40 rank 1 nranks 2 cudaDev 1 busId 3000 commId 0xddf7a5357adcc52d localSize 0 used 20984624 bytes - Init COMPLETE
b1cc0f529b57:525:679 [0] NCCL INFO comm 0x93544d0 rank 0 nranks 2 cudaDev 0 busId 83000 commId 0xddf7a5357adcc52d localSize 0 used 20984624 bytes - Init COMPLETE
[GPU1] Epoch 0 | Batchsize: 32 | Steps: 32
[GPU0] Epoch 0 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 1 | Batchsize: 32 | Steps: 32
Epoch 0 | Training checkpoint saved at checkpoint.pt
[GPU0] Epoch 1 | Batchsize: 32 | Steps: 32
[GPU0] Epoch 2 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 2 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 3 | Batchsize: 32 | Steps: 32
[GPU0] Epoch 3 | Batchsize: 32 | Steps: 32
[GPU0] Epoch 4 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 4 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 5 | Batchsize: 32 | Steps: 32
[GPU0] Epoch 5 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 6 | Batchsize: 32 | Steps: 32
Epoch 5 | Training checkpoint saved at checkpoint.pt
[GPU0] Epoch 6 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 7 | Batchsize: 32 | Steps: 32
[GPU0] Epoch 7 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 8 | Batchsize: 32 | Steps: 32
[GPU0] Epoch 8 | Batchsize: 32 | Steps: 32
[GPU1] Epoch 9 | Batchsize: 32 | Steps: 32
[GPU0] Epoch 9 | Batchsize: 32 | Steps: 32
b1cc0f529b57:526:682 [1] NCCL INFO [Service thread] Connection closed by localRank 1
b1cc0f529b57:525:681 [0] NCCL INFO [Service thread] Connection closed by localRank 0
b1cc0f529b57:525:525 [0] NCCL INFO MSCCL: Teardown finished
b1cc0f529b57:525:525 [0] NCCL INFO comm 0x93544d0 rank 0 nranks 2 cudaDev 0 busId 83000 - Abort COMPLETE
b1cc0f529b57:526:526 [1] NCCL INFO MSCCL: Teardown finished
b1cc0f529b57:526:526 [1] NCCL INFO comm 0x7e7ba40 rank 1 nranks 2 cudaDev 1 busId 3000 - Abort COMPLETE
```

Thank you,

### wenkaidu · 2024-01-22

I don't have experience of building amdgpu kernel driver. But why is this needed? I would just follow the installation guide and install using package manager: https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html#package-man-ubuntu

Which PyTorch docker is used for this test? We can try reproducing from our side.

### bankh · 2024-01-22

I was following the suggestion from your earlier message that stated, 'ROCm 6.0 GPU kernel driver and firmware, amdgpu-dkms, and amdgpu-dkms-firmware, must be installed on a bare metal machine. Updating ROCm in Docker alone is not sufficient.'

I had the same question about why this is necessary. Since you mentioned specific individual packages, I decided to try installing them separately. The last two items (amdgpu-dkms and amdgpu-dkms-firmware) you highlighted were installed using instructions from the package manager, which I have already utilized. As mentioned, this approach resolved the invalid device pointer issue. The first item -- the kernel driver and firmware -- seems more complicated. I believe you were referring to the [ROCk-Kernel-Driver](https://github.com/ROCm/ROCK-Kernel-Driver/tree/rocm-6.0.0), and I am aware that there are people who have attempted its installation to properly configure their 7900XTX and failed a while back (May 2023).

The Docker image is pulled using docker pull rocm/pytorch:rocm6.0_ubuntu20.04_py3.9_pytorch_2.1.1, and I run it with the following command:
```
docker run -it \                           # Run in interactive mode and allocate a pseudo-TTY 
--name <my_container_name> \                # Set a name for the container for easy referencing
--cap-add=SYS_PTRACE \                    # Grant SYS_PTRACE capability (useful for debugging)
--security-opt seccomp=unconfined \       # Disable the seccomp security profile for additional syscalls
--device=/dev/kfd \                       # Pass the /dev/kfd device to the container (for AMD ROCm)
--device=/dev/dri \                       # Pass the /dev/dri device to the container (for graphics rendering)
--group-add $(getent group video | cut -d':' -f 3) \ # Add the container to the 'video' group (usually for graphics)
--ipc=host \                              # Use the host's IPC namespace for shared memory segments
-v /mnt/data_drive:/mnt/data_drive \      # Mount /mnt/data_drive from the host to the container
-v /home/ubuntu:/mnt/ubuntu \             # Mount /home/ubuntu from the host to /mnt/ubuntu in the container
-p 0.0.0.0:6006:6006 \                    # Publish port 6006 to make it accessible externally
-e DISPLAY=$DISPLAY \                     # Pass the DISPLAY variable for GUI applications
<image_name>                              # The Docker image to use
```
Lastly, on a slightly separate note, after installing rocm6.0 via the package manager, I also tried compiling PyTorch 1.12.1 and encountered a similar issue as [this one](https://github.com/pytorch/pytorch/issues/115725), which remains unresolved. [The documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/3rd-party/pytorch-install.html#) suggests using .whl files for PyTorch installation ([versions 2.2 and 2.3](https://download.pytorch.org/whl/nightly/rocm5.7/torch/)), but I don't think this is an appropriate solution for users, as it limits them to versions 2.2/2.3 and causes dependency issues (already tried). Therefore, running PyTorch via Docker seems like a viable solution for the 7900XTX, as I have been exploring.

Edit: Found the following whl source for earlier versions of PyTorch: https://repo.radeon.com/rocm/manylinux/rocm-rel-6.0/

### wenkaidu · 2024-01-22

I could reproduce the issues you reported. After consulting with release management, gfx11 multi-GPU support will be available with ROCm 6.1 release. Please wait for a few months, so we can get this properly supported.

### bankh · 2024-02-05

@wenkaidu,
I've resolved the issue. The challenge was complex, touching on both the graphics card and its firmware. After compiling the ROCk-Kernel-Driver and installing amdgpu-dkms, I used:
```
$ export HSA_OVERRIDE_GFX_VERSION=11.0.0
$ export GPU_MAX_HW_QUEUE=1
```
After the appropriate installations, running these commands in the same terminal session enabled me to execute the dummy example I previously shared. For those encountering similar issues, these commands might be beneficial for training the example `multigpu.py.` However, tackling the dummy example led to encountering further complications with our more sophisticated training setup. The root of these challenges ties back to the graphics card, its design, and firmware. We've resolved the GPU firmware issues through some bash scripts and have since been successfully training our current models. Moving forward, I’ll monitor future ROCm releases to see if they address the specific issue we’ve managed to work around. 

Your support has been immensely valuable. I appreciate it.
Many thanks,
