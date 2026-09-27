# [Issue #64] Question about DCGM fields

source: https://github.com/NVIDIA/DCGM/issues/64
state: closed | updated: 2025-03-27T00:06:21Z
labels: 

## 正文

I was going through the different dcgm [fields](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-field-ids.html) and had the following questions:

**Question-1:** What is the difference between the below fields
[DCGM_FI_DEV_GPU_UTIL](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_DEV_GPU_UTIL) vs [DCGM_FI_PROF_GR_ENGINE_ACTIVE](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_PROF_GR_ENGINE_ACTIVE)
[DCGM_FI_DEV_MEM_COPY_UTIL](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_DEV_MEM_COPY_UTIL) vs [DCGM_FI_PROF_DRAM_ACTIVE](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_PROF_DRAM_ACTIVE)

**Question-2:**
I am looking to track the following metrics for my AI workloads:
1. GPU utilization over time - Idea here is to understand if the task is utilizing the GPU efficiently or is it just wasting GPU resources
2. Memory utilization over time - Idea here is to know if there is scope to increase the batchsize of the AI workload
3. How effectively is my task utilizing the GPU parallelization capabilities? Some stat to understand if there is further scope to parallelize the computation, something like % core utilization and total cores. (Perhaps [DCGM_FI_PROF_SM_ACTIVE](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_PROF_SM_ACTIVE)?)
4. Can I increase my computation batch size? This I believe should come from some memory utilization stat.

Could you please advice what fields I should look into for the above stats? Note that I require the same set of metrics both on **tesla T4** and **A100 (MIG)** cards. (Asking as [issue#58](https://github.com/NVIDIA/DCGM/issues/58#issuecomment-1334504185) seems to mentions that the above mentioned \*\_DEV_\* fields do not work for MIGs) 

Also dcgm [documentation](https://docs.nvidia.com/datacenter/dcgm/3.0/user-guide/feature-overview.html#multiplexing-of-profiling-counters) says not all fields can be queried in parallel. Does this apply only for the \*\_PROF_\* fields or even the \*\_DEV_\* fields? More specifically I wanted to know if the *DCGM_FI_DEV_GPU_UTIL* can be allotted to any [group](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-profiling.html?highlight=getsupportedmetricgroups#_CPPv432dcgmProfGetSupportedMetricGroups12dcgmHandle_tP25dcgmProfGetMetricGroups_t) or does it need to be part of its own group?

## 评论 (10)

### bstollenvidia · 2023-01-23

DCGM_FI_DEV_GPU_UTIL is roughly equal to DCGM_FI_PROF_GR_ENGINE_ACTIVE. DCGM_FI_PROF_GR_ENGINE_ACTIVE is higher precision and works on MIG. 

[DCGM_FI_DEV_MEM_COPY_UTIL](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_DEV_MEM_COPY_UTIL) is utilization of the copy engine of the GPU. I would shy away from it as it may not capture all memory bandwidth. Sometimes cuda mem copies use cuda kernels rather than the copy engine, which would not be picked up by this metric. Also, this metric does not work on MIG. 

[DCGM_FI_PROF_DRAM_ACTIVE](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_PROF_DRAM_ACTIVE) is dram bandwidth vs theoretical maximum. This metric is accurate and captures all transfers to and from the GPU's DRAM. 

"memory utilization" is ambiguous. Do you mean bandwidth or allocation? For bandwidth, use DCGM_FI_PROF_DRAM_ACTIVE. For allocation, use DCGM_FI_DEV_FB_USED,DCGM_FI_DEV_FB_FREE, DCGM_FI_DEV_FB_TOTAL.

> Also dcgm [documentation](https://docs.nvidia.com/datacenter/dcgm/3.0/user-guide/feature-overview.html#multiplexing-of-profiling-counters) says not all fields can be queried in parallel.

This is no longer true. We will remove this from our documentation. 

> More specifically I wanted to know if the DCGM_FI_DEV_GPU_UTIL can be allotted to any [group](https://docs.nvidia.com/datacenter/dcgm/3.0/dcgm-api/dcgm-api-profiling.html?highlight=getsupportedmetricgroups#_CPPv432dcgmProfGetSupportedMetricGroups12dcgmHandle_tP25dcgmProfGetMetricGroups_t) or does it need to be part of its own group?

DCGM_FI_DEV_GPU_UTIL can be in any group. The same is true for any other fieldIds. 

### starry91 · 2023-01-24

Thanks @bstollenvidia! Could you please help me with the following questions as well?
1. Is `PROF_SM_OCCUPANCY` the right field to understand the SM effective usage? i.e, are all the cores in an SM being utilized? (I do understand this could be limited by SM shared/L1 memory, registers)
2. Is `PROF_SM_ACTIVE*PROF_SM_OCCUPANCY*Total_cores` indicative of the cores used (rough estimate)?
3. Is there a way I can get `DCGM_FI_DEV_FB_USED`, `DCGM_FI_DEV_FB_FREE`, `DCGM_FI_DEV_FB_TOTAL` for MIGs as well? Is this something being planned for future releases? The documentation says only the \*\_PROF_* fields are available for MIGs.
4. w.r.t `PROF_SM_OCCUPANCY` Say a GPU has 128 cores/SM, does that mean its `maximum number of concurrent warps`  is `128/32 = 4`?


### bstollenvidia · 2023-01-24

Think of them as 3 dimensions of utilization:
PROF_GR_ENGINE_ACTIVE - Is any kernel running on any SM?
PROF_SM_ACTIVE - What ratio of SMs are active?
PROF_SM_OCCUPANCY - How many warps are running vs theoretical max (2048 per SM). 

Rough estimate of SMs used would be PROF_SM_ACTIVE * numSMs.

> w.r.t PROF_SM_OCCUPANCY Say a GPU has 128 cores/SM, does that mean its maximum number of concurrent warps is 128/32 = 4?

There aren't cores per SM. I would read up on the cuda programming model here:
https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/
or here:
https://en.wikipedia.org/wiki/Thread_block_(CUDA_programming)

The FB metrics are available at the MIG level. See https://github.com/NVIDIA/DCGM/blob/661d939e808591f0accb4acce7bc317e99da26e7/dcgmlib/src/DcgmCacheManager.cpp#L10585

Make sure you're using our latest release (DCGM 3.1.3) from here https://developer.nvidia.com/dcgm#Downloads

### starry91 · 2023-02-07

@bstollenvidia The image in https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/ does mention SM has multiple cores. Am I understanding it in a wrong way?
![image](https://user-images.githubusercontent.com/29708560/217235470-d4b6cf03-0c71-4b7e-ac03-a8badcaee1c3.png)

[Another](https://www.researchgate.net/figure/Typical-NVIDIA-GPU-architecture-The-GPU-is-comprised-of-a-set-of-Streaming_fig6_283559088) reference which gives out the same meaning.


### starry91 · 2023-02-07

> PROF_GR_ENGINE_ACTIVE - Is any kernel running on any SM?

@bstollenvidia Does this mean this can only have a discreet set of values, either 0 or 1? 0 if nothing is running, 1 if GPU is being used in any way(Even if 1 core or device memory is being used).
Also, is the value inclusive of memory utilization as well, i.e, it would be 1 even if the compute core is not being used but data is being transferred to the device memory?

### starry91 · 2023-02-20

@bstollenvidia Could you please look into the questions posted in the above 2 comments?

### bstollenvidia · 2023-02-21

SMs don't have independent cores. They can do cuda threads in parallel but every thread is doing exactly the same instruction per cycle. They re-run kernels for any branches taken. 

> Does this mean this can only have a discreet set of values, either 0 or 1? 0 if nothing is running, 1 if GPU is being used in any way(Even if 1 core or device memory is being used).

No. The values are from 0 - 1. Could be 0.522922 or something. 

> Also, is the value inclusive of memory utilization as well, i.e, it would be 1 even if the compute core is not being used but data is being transferred to the device memory?

Yes. Waiting on memory transfers = busy. Technically, the SM is busy but blocked on a dram transfer. 

### starry91 · 2023-02-22

> No. The values are from 0 - 1. Could be 0.522922 or something.

@bstollenvidia Could you please elaborate in what case we will see a fractional number? And also how to interpret it?

### bstollenvidia · 2023-02-27

> Could you please elaborate in what case we will see a fractional number? 

In all cases. I would suggest trying out the dcgmproftester12 tool that's installed with DCGM to understand how workloads relate to profiling metrics. 
See docs here: CUDA Test Generator (dcgmproftester)[¶](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html#cuda-test-generator-dcgmproftester)

> And also how to interpret it?

You can think of it as a percentage but instead of between 0 and 100 it's between 0 and 1.0. You can multiply this by 100 if you want percentage. 

### kev-iotairx · 2025-03-27

@bstollenvidia could you clarify whether `DCGM_FI_PROF_DRAM_ACTIVE` metric includes `L1` and `L2` cache i.e on-chip memory or only HBM memory connected to the GPU Die? We are trying to distinguish between data transfer between HBM and L2. 
