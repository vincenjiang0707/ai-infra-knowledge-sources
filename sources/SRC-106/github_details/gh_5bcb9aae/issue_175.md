# [Issue #175] [Issue]: amd-smi USED_VRAM does not reflect real-time memory allocations/deallocations

source: https://github.com/ROCm/amdsmi/issues/175
state: closed | updated: 2026-02-27T17:11:41Z
labels: status: assessed

## 正文

### Problem Description

`amd-smi metric --mem` reports `USED_VRAM` that does not update when memory is allocated or freed. The value remains constant regardless of GPU memory operations. In contrast, `hipMemGetInfo()` correctly reports real-time memory usage.

### Impact
- torch.cuda.device_memory_used() returns inaccurate data on ROCm, which relies on `amdsmi_get_gpu_vram_usage()`.
- Any other memory monitoring tools using amd-smi to track real-time GPU memory usage.


### Operating System

Linux (kernel 6.8.0)

### CPU

AMD EPYC 9575F 64-Core Processor

### GPU

AMD Instinct MI355X (gfx950)

### ROCm Version

7.0.0

### ROCm Component

amdsmi

### Steps to Reproduce

```
import subprocess
import torch

def get_amd_smi_vram_mb():
    result = subprocess.run(['amd-smi', 'metric', '--gpu', '0', '--mem'], 
                          capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'USED_VRAM' in line and 'VISIBLE' not in line:
            return int(line.split(':')[1].strip().replace(' MB', ''))
    return -1

def get_hip_mem_used_mb():
    free, total = torch.cuda.mem_get_info(0)
    return (total - free) // (1024 * 1024)

# Initial state
amd_initial = get_amd_smi_vram_mb()
hip_initial = get_hip_mem_used_mb()
print(f"Initial:  amd-smi={amd_initial} MB, hipMemGetInfo={hip_initial} MB")

# Allocate 2GB
tensor = torch.zeros(2_000_000_000, dtype=torch.uint8, device='cuda:0')
torch.cuda.synchronize()
amd_after = get_amd_smi_vram_mb()
hip_after = get_hip_mem_used_mb()
print(f"After 2GB alloc: amd-smi={amd_after} MB (Δ={amd_after-amd_initial}), hipMemGetInfo={hip_after} MB (Δ={hip_after-hip_initial})")

# Free
del tensor
torch.cuda.empty_cache()
amd_free = get_amd_smi_vram_mb()
hip_free = get_hip_mem_used_mb()
print(f"After free: amd-smi={amd_free} MB, hipMemGetInfo={hip_free} MB")
```

### Expected Output
- Initial:  amd-smi=300 MB, hipMemGetInfo=634 MB
- After 2GB alloc: amd-smi=2348 MB (Δ=2048), hipMemGetInfo=2692 MB (Δ=2058)
- After free: amd-smi=300 MB, hipMemGetInfo=784 MB
### Actual Output
- Initial:  amd-smi=283 MB, hipMemGetInfo=634 MB
- After 2GB alloc: amd-smi=284 MB (Δ=1), hipMemGetInfo=2692 MB (Δ=2058)
- After free: amd-smi=284 MB, hipMemGetInfo=784 MB

amd-smi shows Δ=1 MB while hipMemGetInfo correctly shows Δ=2058 MB

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (12)

### darren-amd · 2026-01-28

Hi @zyzshishui,

Thanks for the detailed report and reproducer. Just gave this a quick try on latest ROCm (7.2) and was unable to reproduce the issue (the delta was ~2GB as expected). Could you please update your ROCm version by following the instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#quick-start-installation-guide) and let me know if the issue persists, thanks!

### zyzshishui · 2026-01-28

> Hi [@zyzshishui](https://github.com/zyzshishui),
> 
> Thanks for the detailed report and reproducer. Just gave this a quick try on latest ROCm (7.2) and was unable to reproduce the issue (the delta was ~2GB as expected). Could you please update your ROCm version by following the instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#quick-start-installation-guide) and let me know if the issue persists, thanks!

Hi, thanks for your reply. I'm already using the latest version of ROCM and the issue still exist.

<img width="844" height="328" alt="Image" src="https://github.com/user-attachments/assets/94a5c326-e658-4829-a79c-d76e661e281f" />

<img width="1021" height="1015" alt="Image" src="https://github.com/user-attachments/assets/24275e95-be41-4586-bb54-7d0e59dbbb1b" />

### darren-amd · 2026-01-28

Hi @zyzshishui,

You appear to be on ROCm 7.0, the latest ROCm version is 7.2. Would you mind upgrading by following the instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#quick-start-installation-guide)? You may want to uninstall the older version by following the instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager/package-manager-ubuntu.html#uninstalling).  I'm also using the latest torch wheels available [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html#use-a-wheels-package). Please let me know if you run into any issues, thanks!

### zyzshishui · 2026-01-28

Still same
<img width="887" height="173" alt="Image" src="https://github.com/user-attachments/assets/f4cbe4a6-b84e-4ed5-a33b-63b3f0c47822" />

### zyzshishui · 2026-01-28

Try this minimum reproduction:
```
>>> import torch
>>> torch.cuda.device_memory_used(0)
296747008
>>> x =  torch.randn(1000000, 500, device='cuda:0')
>>> torch.cuda.device_memory_used(0)
297795584
>>> torch.cuda.device_memory_used(3)
2449473536
>>> del x
>>> torch.cuda.device_memory_used(3)
2449473536
```
There are 2 issues:
1. Need to specify `device_memory_used(3)` for quering gpu0.
2. There is a lag — even though I `del x`, the memory occupation is still large.

### darren-amd · 2026-01-29

Hi @zyzshishui,

Thanks for confirming, I gave this a try on an MI350 system and was able to reproduce what you are facing. The ID being used by torch (`cuda:0`) is the hip device ID and does not directly map to the device ID for amd-smi (`amd-smi metric --gpu 0`). You can run `amd-smi` to see the correct mapping, for example:


<img width="649" height="479" alt="Image" src="https://github.com/user-attachments/assets/496aa670-ecff-4442-82a5-4339ac452dab" />


For example, in the above `cuda:0` would be device 3 in amd-smi (similar to what you're seeing). For the second question, after deletion via `del x` I believe torch still holds onto the memory, you'd need to run something like `torch.cuda.empty_cache()` for it to be fully freed.

### zyzshishui · 2026-01-29

> Hi [@zyzshishui](https://github.com/zyzshishui),
> 
> Thanks for confirming, I gave this a try on an MI350 system and was able to reproduce what you are facing. The ID being used by torch (`cuda:0`) is the hip device ID and does not directly map to the device ID for amd-smi (`amd-smi metric --gpu 0`). You can run `amd-smi` to see the correct mapping, for example:
> 
> <img alt="Image" width="649" height="479" src="https://private-user-images.githubusercontent.com/180982888/542411354-496aa670-ecff-4442-82a5-4339ac452dab.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njk3MjI4MjcsIm5iZiI6MTc2OTcyMjUyNywicGF0aCI6Ii8xODA5ODI4ODgvNTQyNDExMzU0LTQ5NmFhNjcwLWVjZmYtNDQ0Mi04MmE1LTQzMzlhYzQ1MmRhYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTI5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEyOVQyMTM1MjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YzhhN2MzY2RiNzk0ZjFhNjRkNGI5MzZhYjExZTMyOTVlMmQ1ZjA3YjFmNWYxY2E0MDc1OGU1Njk2MmIxNmY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.15yuXzQjq_vJP2GLvDuuZMVfHDDdZ4yfWjq95ikit9I">
> For example, in the above `cuda:0` would be device 3 in amd-smi (similar to what you're seeing). For the second question, after deletion via `del x` I believe torch still holds onto the memory, you'd need to run something like `torch.cuda.empty_cache()` for it to be fully freed.

After I run `torch.cuda.empty_cache()`, the result is the same.
I know that the mapping is not direct, but this is not supposed to be visible to the user, isn't it? That makes `torch.cuda.device_memory_used()` incorrect.

### darren-amd · 2026-01-29

Just to confirm, after allocating on device `cuda:0`, when you run `torch.cuda.device_memory_used(3)` on the mapped HIP ID -> amd-smi ID (0 -> 3 in the above screenshot), the VRAM is unchanged?

Could you try running:
```
import subprocess
import torch

def get_amd_smi_vram_mb(gpu_id):
    result = subprocess.run(['amd-smi', 'metric', '--gpu', str(gpu_id), '--mem'], 
                          capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'USED_VRAM' in line and 'VISIBLE' not in line:
            return int(line.split(':')[1].strip().replace(' MB', ''))
    return -1

def get_hip_mem_used_mb(gpu_id):
    free, total = torch.cuda.mem_get_info(gpu_id)
    return (total - free) // (1024 * 1024)

def print_all_gpu_memory(label):
    print(f"\n{label}:")
    num_gpus = torch.cuda.device_count()
    for gpu_id in range(num_gpus):
        amd_mem = get_amd_smi_vram_mb(gpu_id)
        hip_mem = get_hip_mem_used_mb(gpu_id)
        print(f"  GPU {gpu_id}: amd-smi={amd_mem} MB, hipMemGetInfo={hip_mem} MB")

# Initial state
print_all_gpu_memory("Initial")

# Allocate 2GB on GPU 0
tensor = torch.zeros(2_000_000_000, dtype=torch.uint8, device='cuda:0')
torch.cuda.synchronize()
print_all_gpu_memory("After 2GB alloc on GPU 0")

# Free
del tensor
torch.cuda.empty_cache()
print_all_gpu_memory("After free")
```

And provide me the output as well as the output of `amd-smi`? 

### zyzshishui · 2026-01-29

> Just to confirm, after allocating on device `cuda:0`, when you run `torch.cuda.device_memory_used(3)` on the mapped HIP ID -> amd-smi ID (0 -> 3 in the above screenshot), the VRAM is unchanged?
> 
> Could you try running:
> 
> ```
> import subprocess
> import torch
> 
> def get_amd_smi_vram_mb(gpu_id):
>     result = subprocess.run(['amd-smi', 'metric', '--gpu', str(gpu_id), '--mem'], 
>                           capture_output=True, text=True)
>     for line in result.stdout.split('\n'):
>         if 'USED_VRAM' in line and 'VISIBLE' not in line:
>             return int(line.split(':')[1].strip().replace(' MB', ''))
>     return -1
> 
> def get_hip_mem_used_mb(gpu_id):
>     free, total = torch.cuda.mem_get_info(gpu_id)
>     return (total - free) // (1024 * 1024)
> 
> def print_all_gpu_memory(label):
>     print(f"\n{label}:")
>     num_gpus = torch.cuda.device_count()
>     for gpu_id in range(num_gpus):
>         amd_mem = get_amd_smi_vram_mb(gpu_id)
>         hip_mem = get_hip_mem_used_mb(gpu_id)
>         print(f"  GPU {gpu_id}: amd-smi={amd_mem} MB, hipMemGetInfo={hip_mem} MB")
> 
> # Initial state
> print_all_gpu_memory("Initial")
> 
> # Allocate 2GB on GPU 0
> tensor = torch.zeros(2_000_000_000, dtype=torch.uint8, device='cuda:0')
> torch.cuda.synchronize()
> print_all_gpu_memory("After 2GB alloc on GPU 0")
> 
> # Free
> del tensor
> torch.cuda.empty_cache()
> print_all_gpu_memory("After free")
> ```
> 
> And provide me the output as well as the output of `amd-smi`?

The lag issue is solved after empty cache, thanks.

The results you asked are below. My point is, it's inacceptable that `torch.zeros(2_000_000_000, dtype=torch.uint8, device='cuda:0')` and `torch.cuda.device_memory_used(0)` are not mapped to the same gpu, this behavior is also different form the result on nvidia.
```
Initial:
  GPU 0: amd-smi=283 MB, hipMemGetInfo=634 MB
  GPU 1: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 2: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 3: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 4: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 5: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 6: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 7: amd-smi=284 MB, hipMemGetInfo=634 MB

After 2GB alloc on GPU 0:
  GPU 0: amd-smi=284 MB, hipMemGetInfo=2692 MB
  GPU 1: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 2: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 3: amd-smi=2334 MB, hipMemGetInfo=634 MB
  GPU 4: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 5: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 6: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 7: amd-smi=284 MB, hipMemGetInfo=634 MB

After free:
  GPU 0: amd-smi=284 MB, hipMemGetInfo=784 MB
  GPU 1: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 2: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 3: amd-smi=426 MB, hipMemGetInfo=634 MB
  GPU 4: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 5: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 6: amd-smi=284 MB, hipMemGetInfo=634 MB
  GPU 7: amd-smi=284 MB, hipMemGetInfo=634 MB
```

<img width="740" height="841" alt="Image" src="https://github.com/user-attachments/assets/ebcbe52a-199f-4260-99be-a99eff721e11" />

### darren-amd · 2026-02-26

Hi @zyzshishui,

I'm glad to hear that it is working on your end!

I agree that it can be unintuitive. The root cause is that amd-smi and HIP use different enumeration schemes. amd-smi enumerates by BDF, whereas HIP enumerates by UUID. I've discussed with the team and we aren't intending to change this behavior as they serve different purposes (BDF is useful for partitions). I'd recommend building a mapping between the two, where you can correlate HIP device IDs <-> amd-smi device IDs.

### zyzshishui · 2026-02-26

> Hi [@zyzshishui](https://github.com/zyzshishui),
> 
> I'm glad to hear that it is working on your end!
> 
> I agree that it can be unintuitive. The root cause is that amd-smi and HIP use different enumeration schemes. amd-smi enumerates by BDF, whereas HIP enumerates by UUID. I've discussed with the team and we aren't intending to change this behavior as they serve different purposes (BDF is useful for partitions). I'd recommend building a mapping between the two, where you can correlate HIP device IDs <-> amd-smi device IDs.

I understand that you don't want to change this. Then I think you'd better change relevant implementation for torch rocm's api? Otherwise it would confuse users

### darren-amd · 2026-02-27

Hi @zyzshishui,

Thanks for the suggestion, I relayed this to the team and since [the specs](https://docs.pytorch.org/docs/stable/generated/torch.cuda.device_memory_used.html) state that this call is routed through nvidia-smi/amd-smi, we would like to keep in line with this. I'd recommend that you use [`torch.cuda.memory.mem_get_info`](https://docs.pytorch.org/docs/stable/generated/torch.cuda.memory.mem_get_info.html) as you have been doing.
