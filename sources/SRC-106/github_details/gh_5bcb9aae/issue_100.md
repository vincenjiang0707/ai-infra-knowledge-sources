# [Issue #100] Only 8 of 64 GPUs Are Fully Partitioned and Usable in Docker After CPX/NPS4

source: https://github.com/ROCm/amdsmi/issues/100
state: open | updated: 2025-06-25T16:05:10Z
labels: Under Investigation

## 正文

**Summary**
After setting compute partition to `CPX` and memory partition to `NPS4`, only 8 GPUs **(indices 0, 8, 16, 24, 32, 40, 48, 56)** show valid COMPUTE_PARTITION: CPX and MEMORY_PARTITION: NPS4. Also, these are the only devices attachable via Docker’s --device option.


**How to Reproduce**
Run
```
sudo amd-smi set --memory-partition NPS4
amd-smi static --partition
```

**Actual Behavior**
Only 8 GPUs (indices 0, 8, 16, 24, 32, 40, 48, 56)  show the correct partitions. The rest show:
```
COMPUTE_PARTITION: N/A
MEMORY_PARTITION: N/A
```
Actual Output: [logs.txt](https://github.com/user-attachments/files/20882234/logs.txt)


**Expected Behavior**
All 64 GPUs should show: 

```
COMPUTE_PARTITION: CPX
MEMORY_PARTITION: NPS4
```

**System Info**
Dell PowerEdge XE9680 (MI300X)
CPU: 2 x Intel Xeon Platinum 8462Y+: 32c @ 2.8 GHz
RAM: 2.0 TiB NVMe: 124 TB
GPUs: 8 x AMD MI300X

Kernel: Linux 5.15.0-142-generic
ROCm version: 6.4.1
AMDSMI Tool: 25.4.2+aca1101
AMDSMI Library: 25.4.0
amdgpu version: 6.12.12
VBIOS: AMD MI300X_HW_SRIOV_CVS_1VF (Version: 022.040.003.043.000001, Date: 2025/02/18)
OS: Ubuntu 22.04.5 LTS


## 评论 (6)

### maxweiss · 2025-06-24

ROCm 6.4.1 seems to have issues with MI300A and MI300X GPUs. I've created a similar issue in the ROCm repo: https://github.com/ROCm/ROCm/issues/4759. Older ROCm versions work fine.

### Bihan · 2025-06-24

Thank you @maxweiss. I will try with `ROCm 6.4.0`

### Bihan · 2025-06-24

@maxweiss You are right with ROCm 6.4.0 it shows all PARTITION with valid values, but only devices (indices 0, 8, 16, 24, 32, 40, 48, 56) are attachable via Docker’s --device option.

Eg: **index 0 detected, but index 1 not detected**
```
docker run -it --network=host --device=/dev/kfd \
  --device=/dev/dri/renderD128 \
  --device=/dev/dri/renderD129 \
  --group-add video --security-opt seccomp=unconfined -v $HOME:$HOME -w $HOME rocm/pytorch
root@ENC1-CLS01-SVR07:/home/hotaisle# rocm-smi


============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK    MCLK    Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)                                                  
==========================================================================================================================
0       2     0x74a1,   3771   47.0°C      154.0W    NPS4, CPX, 0        133Mhz  900Mhz  0%   auto  750.0W  0%     0%    
1       3     N/A,      62138  N/A         N/A       N/A, N/A, 1         N/A     N/A     0%   n/a   N/A     2%     N/A   
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================
```

**indices 0, 8 both detected**
```
docker run -it --network=host --device=/dev/kfd \
  --device=/dev/dri/renderD128 \
  --device=/dev/dri/renderD136 \
  --group-add video --security-opt seccomp=unconfined -v $HOME:$HOME -w $HOME rocm/pytorch
root@ENC1-CLS01-SVR07:/home/hotaisle# rocm-smi


============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK    MCLK    Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)                                                  
==========================================================================================================================
0       2     0x74a1,   3771   47.0°C      154.0W    NPS4, CPX, 0        139Mhz  900Mhz  0%   auto  750.0W  0%     0%    
1       10    0x74a1,   29729  41.0°C      157.0W    NPS4, CPX, 0        134Mhz  900Mhz  0%   auto  750.0W  0%     0%    
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================
```

### maxweiss · 2025-06-24

I think this is just a display error/bug. Does `rocminfo` show the two GPUs?

On our host, the rocm-smi output in the container looks similar to yours, but `rocminfo` and pytorch show the correct number of GPUs:
```
$ docker run -it --device=/dev/kfd   --device=/dev/dri/renderD128   --device=/dev/dri/renderD129 -v $HOME:$HOME -w $HOME rocm/pytorch
root@4a3d7aed53e0:/home/mweiss# rocm-smi


============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK   MCLK     Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)                                                  
==========================================================================================================================
0       1     0x74a0,   42268  32.0°C      120.0W    NPS1, CPX, 0        94Mhz  1300Mhz  0%   auto  550.0W  0%     0%    
1       2     N/A,      22813  N/A         N/A       N/A, N/A, 1         N/A    N/A      0%   n/a   N/A     0%     N/A   
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================

root@4a3d7aed53e0:/home/mweiss# python -c "import torch; print(torch.cuda.device_count())"
2
```

But maybe someone from the AMD/ROCm team knows more.

### Bihan · 2025-06-25

@maxweiss Once again Thank You. Yes this looks like just a display error. I ran vllm inference and it worked too.

I also tried with `ROCm 6.4.1` and it worked too. Looks like even with 6.4.1 it is just a display error.

### schung-amd · 2025-06-25

Yes, unfortunately at the moment `rocm-smi` does not accurately report metrics for partitions. I don't have a firm ETA on when this will be fixed, but hopefully this will work in ROCm 7.0.
