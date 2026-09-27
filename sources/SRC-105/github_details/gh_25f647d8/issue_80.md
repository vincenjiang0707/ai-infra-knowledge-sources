# [Issue #80] DCGM_FI_DEV_GPU_UTIL with MIG devices

source: https://github.com/NVIDIA/DCGM/issues/80
state: closed | updated: 2025-10-15T10:53:04Z
labels: 

## 正文

Hi. I understand that the `DCGM_FI_DEV_GPU_UTIL` metric is currently not available for MIG devices. Are there any plans to support it?

I think the `DCGM_FI_DEV_GPU_UTIL` metric is really important for efficiently running a large number of GPUs on the platform. 
As an alternative, I'm using the `DCGM_FI_PROF_GR_ENGINE_ACTIVE` metric, but it's somewhat inconvenient that I can't see the exact utilization. 

Thank you.

## 评论 (5)

### nikkon-dev · 2023-05-08

@devnjw,

Currently, there are no plans to support DCGM_FI_DEV_GPU_UTIL for MIG instances. This metric is outdated and has several limitations. However, the new hardware now supports the same method as DCGM_FI_PROF_* metrics. Starting from the Hopper architecture, the NVML API can provide similar metrics directly. You can find more information at [link](https://docs.nvidia.com/deploy/nvml-api/group__GPM.html#group__GPM).

> that I can't see the exact utilization
Could you provide more details about this? Typically, the DCGM_FI_PROF_* metrics offer more precise data.

### devnjw · 2023-05-08

I understood that `DCGM_FI_DEV_GPU_UTIL` is exactly the utilization between 0 and 100, and `DCGM_FI_PROF_GR_ENGINE_ACTIVE` only indicates if the GPU is being used, but I could be wrong.

One question, is it possible for `DCGM_FI_DEV_GPU_UTIL` to go up but not `DCGM_FI_PROF_GR_ENGINE_ACTIVE` as shown in the graph below?
(I am using GPU for machine learning).

<img width="1565" alt="image" src="https://user-images.githubusercontent.com/48133047/236717164-c329c6aa-674d-4d8a-8ece-62095fbc9510.png">

Thank you!

### starry91 · 2023-05-16

@devnjw [https://github.com/NVIDIA/DCGM/issues/64#issuecomment-1400811885](https://github.com/NVIDIA/DCGM/issues/64#issuecomment-1400811885) would have answers for your question. _[Asked be me previously]_

Also, following is the definition of GPU utilization: (From `nvidia-smi --help-query-gpu`
```
"utilization.gpu"
Percent of time over the past sample period during which one or more kernels was executing on the GPU.
The sample period may be between 1 second and 1/6 second depending on the product.
```

### nikkon-dev · 2023-05-16

@starry91,

Both `DCGM_FI_DEV_GPU_UTIL` and `nvidia-smi utilization.gpu` measure GPU utilization from the driver's point of view. The `DCGM_FI_PROF_*` metrics provide more precise utilization values per specific GPU subsystems, as they use special hardware.

`DCGM_FI_PROF_GR_ENGINE_ACTIVE` measures the percentage of time when the graphical engine was active. Essentially, it shows when the GPU pipeline scheduler did any work at all. If you only use one thread on one SM, but for the whole monitoring interval, the GR_ENGINE_ACTIVE will show 1.0 (which is 100% as it goes from 0.0 to 1.0).

For a more precise high-level picture of your system state, consider using the `DCGM_FI_PROF_SM_OCCUPANCY` or `DCGM_FI_PROF_SM_ACTIVE` metrics.

It is possible to see `nvidia-smi utilization.cpu` at 100% but `DCGM_FI_PROF_GR_ENGINE_ACTIVE` at 0%. Such a situation can be simulated easily using the `dcgmproftester12 -t 1009 —no-dcgm-validation` command, which utilizes PCI bandwidth but none of the SMs do any job (thus the GrActive remains at 0%).

### kmosunoff · 2025-10-15

> It is possible to see `nvidia-smi utilization.cpu` at 100% but `DCGM_FI_PROF_GR_ENGINE_ACTIVE` at 0%.

@nikkon-dev Hi! Did you mean nvidia-smi utilization.gpu (not cpu)?
Also, are H2D/D2H data transfers the only difference between DCGM_FI_DEV_GPU_UTIL (including them) and DCGM_FI_PROF_GR_ENGINE_ACTIVE (excluding them)?
