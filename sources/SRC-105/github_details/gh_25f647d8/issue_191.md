# [Issue #191] Running standalone DCGM on Kubernetes cluster along with DCGM in Triton

source: https://github.com/NVIDIA/DCGM/issues/191
state: closed | updated: 2025-01-19T22:31:39Z
labels: 

## 正文

Hello maintainters!

In [the release note of 24.08](https://docs.nvidia.com/deeplearning/triton-inference-server/release-notes/rel-24-08.html#rel-24-08), there is a known issue which is 

> Triton metrics might not work if the host machine is running a separate DCGM agent on bare-metal or in a container.

Also I found https://github.com/triton-inference-server/server/issues/3897#issuecomment-1035414009 which had said,

> Triton uses the library version of DCGM which is not allowed to co-exist with the container version of DCGM

I'm using Google Kubernetes Engine and followed [this page](https://cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nvidia-dcgm) to try running `nvidia-dcgm` and `nvidia-dcgm-exporter` pods (DaemonSet).
It turned out Triton metrics worked even with the separate DCGM in another pod.

Triton metrics 
`nv_gpu_utilization{gpu_uuid="GPU-c1eb1e78-d69a-c334-9ce5-2cec7c8399a1"} 0`

DCGM exporter metrics
`DCGM_FI_DEV_GPU_UTIL{gpu="0",UUID="GPU-c1eb1e78-d69a-c334-9ce5-2cec7c8399a1",device="nvidia0",modelName="Tesla T4",Hostname="gke-test-dcgm-default-pool-270c4b72-ct4k",container="triton-server",namespace="default",pod="triton-86c854b54b-84l8q"} 0`

Based on this observation, I have several questions.

- Does the issue where DCGM can't coexist still exist?
- If it still exists, is there a way to make sure Triton metrics are available even with a separate DCGM, without rebuilding Triton to disable DCGM? As we have some GPU workloads that are not using Triton, having a separate DCGM is necessary for the workloads.

## 评论 (7)

### nikkon-dev · 2024-09-17

@ysk24ok,

Could you clarify which hardware you’re using? Is that Hopper or older architecture?

### ysk24ok · 2024-09-18

@nikkon-dev Thank you for the reply. I tested using T4, so older than Hopper.

For reference:
- GKE: 1.30.3-gke.1639000
- NVIDIA driver: 560.35.03
- Triton Inference Server 24.08
- DCGM (Daemonset): 3.3.0

### nikkon-dev · 2024-09-21

@ysk24ok,

In previous architectures prior to Hopper, there is a hardware restriction on GPUs that prevents the simultaneous usage of multiple instances of the profiling system. As a result, it is not possible to run DCGM alongside other profiling tools such as Nsight compute profiler or another instance of DCGM. However, this limitation only applies to the DCGM_FI_PROF* set of metrics.

Your options could be:
- Rebuild Triton to disable DCGM
- Disable DCGM_FI_PROF* metrics in DCGM (and/or dcgm-exporter)
- Temporarily pause DCGM via `dcgmi pause` command

Regrettably, this type of limitation cannot be resolved through software alone. To address this issue, Hopper GPUs implement a dedicated hardware solution.

### ysk24ok · 2024-09-25

Thank you @nikkon-dev!

I tested again on GKE with T4 GPUs by deploying Triton as a standalone pod and dcgm / dcgm-exporter as DaemonSets.
Although T4's architecture is Turing which is older than Hopper (correct?) and there were several DCGM instances (Triton and DCGM daemonset), I confirmed DCGM_FI_PROF* metrics were available from DCGM exporter.

```
# HELP DCGM_FI_PROF_SM_ACTIVE The ratio of cycles an SM has at least 1 warp assigned
# TYPE DCGM_FI_PROF_SM_ACTIVE gauge
DCGM_FI_PROF_SM_ACTIVE{gpu="0",UUID="GPU-84412445-5790-0b3f-f714-da8aa3b2c0b0",device="nvidia0",modelName="Tesla T4",Hostname="gke-test-dcgm-default-pool-fed1e979-tt7p",container="triton-server",namespace="default",pod="triton-84d57987c9-kks4k"} 0.000000
DCGM_FI_PROF_SM_ACTIVE{gpu="1",UUID="GPU-4812b59b-1f1a-430f-d8a4-69d2ee8c18bb",device="nvidia1",modelName="Tesla T4",Hostname="gke-test-dcgm-default-pool-fed1e979-tt7p",container="",namespace="",pod=""} 0.000000
# HELP DCGM_FI_PROF_SM_OCCUPANCY The fraction of resident warps on a multiprocessor
# TYPE DCGM_FI_PROF_SM_OCCUPANCY gauge
DCGM_FI_PROF_SM_OCCUPANCY{gpu="0",UUID="GPU-84412445-5790-0b3f-f714-da8aa3b2c0b0",device="nvidia0",modelName="Tesla T4",Hostname="gke-test-dcgm-default-pool-fed1e979-tt7p",container="triton-server",namespace="default",pod="triton-84d57987c9-kks4k"} 0.000000
DCGM_FI_PROF_SM_OCCUPANCY{gpu="1",UUID="GPU-4812b59b-1f1a-430f-d8a4-69d2ee8c18bb",device="nvidia1",modelName="Tesla T4",Hostname="gke-test-dcgm-default-pool-fed1e979-tt7p",container="",namespace="",pod=""} 0.000000
# HELP DCGM_FI_PROF_PIPE_TENSOR_ACTIVE The ratio of cycles the tensor (HMMA) pipe is active (off the peak sustained elapsed cycles)
# TYPE DCGM_FI_PROF_PIPE_TENSOR_ACTIVE gauge
DCGM_FI_PROF_PIPE_TENSOR_ACTIVE{gpu="0",UUID="GPU-84412445-5790-0b3f-f714-da8aa3b2c0b0",device="nvidia0",modelName="Tesla T4",Hostname="gke-test-dcgm-default-pool-fed1e979-tt7p",container="triton-server",namespace="default",pod="triton-84d57987c9-kks4k"} 0.000000
DCGM_FI_PROF_PIPE_TENSOR_ACTIVE{gpu="1",UUID="GPU-4812b59b-1f1a-430f-d8a4-69d2ee8c18bb",device="nvidia1",modelName="Tesla T4",Hostname="gke-test-dcgm-default-pool-fed1e979-tt7p",container="",namespace="",pod=""} 0.000000
```

I didn't rebuild Triton to disable DCGM nor disable DCGM_FI_PROF* metrics in DCGM.

Do you have any idea? Is it because DCGM in Triton doesn't collect DCGM_FI_PROF* metrics? FYI, [here](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/metrics.html) are the list of the metrics available from Triton.

### ysk24ok · 2024-10-03

Hi @nikkon-dev, it'd be appreciated if could take a look at https://github.com/NVIDIA/DCGM/issues/191#issuecomment-2372734721 and give me a reply.

### ysk24ok · 2024-12-04

I digged into the Triton core code base (24.08) and found out that DCGM in Triton were not using `DCGM_FI_PROF_*` metrics.
https://github.com/triton-inference-server/core/blob/r24.08/src/metrics.cc#L915-L927
`dcgm_metadata.standalone_` seems to be always false? so `DCGM_FI_PROF_GR_ENGINE_ACTIVE` is not used.

Answering to my question in https://github.com/NVIDIA/DCGM/issues/191#issuecomment-2372734721, I guess `DCGM_FI_PROF_*` metrics were available from the standalone DCGM because DCGM embedded in Triton didn't use the metrics.

So to summarize:

- standalone DCGM can be used along with DCGM embedded in Triton as `DCGM_FI_PROF_*` is not used in Triton 24.08 but this might not hold for future versions of Triton.
- if Triton could use standalone DCGM instead of embedded one, we could just use the standalone one and avoid running multiple DCGM?

Closing the issue.


### nikkon-dev · 2024-12-28

> if Triton could use standalone DCGM instead of embedded one, we could just the standalone one and avoid running multiple DCGM?

That is correct. Only one DCGM instance is allowed to read the DCGM_FI_PROF_* metrics at a time. However, multiple clients can read those metrics from the same DCGM instance. In this scenario, both the DCGM exporter and Triton act as clients to a single nv-hostengine instance, allowing them to operate without interfering with one another.
