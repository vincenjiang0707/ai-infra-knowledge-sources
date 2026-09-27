# [Issue #62] For profiling metrics, dcgmi reports an error message: The third-party Profiling module returned an unrecoverable error

source: https://github.com/NVIDIA/DCGM/issues/62
state: open | updated: 2025-01-17T20:22:42Z
labels: 

## 正文

The problem is that dcgmi can not query profiling metrics. 
- Tesla V100 GPU. DCGM version: 3.1.3

- nvidia-smi :

Tue Jan 10 16:00:42 2023       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 510.47.03    Driver Version: 510.47.03    CUDA Version: 11.6     |

-dcgmi modules -l
It shows Profiling module is loaded.
+===========+====================+==================================================+
| Module ID | Name               | State                                            |
+-----------+--------------------+--------------------------------------------------+
| 0         | Core               | Loaded                                           |
| 1         | NvSwitch           | Loaded                                           |
| 2         | VGPU               | Not loaded                                       |
| 3         | Introspection      | Not loaded                                       |
| 4         | Health             | Not loaded                                       |
| 5         | Policy             | Not loaded                                       |
| 6         | Config             | Not loaded                                       |
| 7         | Diag               | Not loaded                                       |
| 8         | Profiling          | Loaded                                           |                             |

- dcgmi query profiling metrics: SM occupancy 
>dcgmi dmon -e 1002,1003
>Error setting watches. **Result: The third-party Profiling module returned an unrecoverable error**

- nv-hostengine debug log:


>2023-01-09 17:34:34.533 DEBUG [933520:933752] [[Profiling]] AddMetricToConfig was successful for deviceIndex 0. metricName sm__warps_active.avg.pct_of_peak_sustained_elapsed [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmLopConfig.cpp:905] [DcgmLopConfig::AddMetricToConfig]
>2023-01-09 17:34:34.533 DEBUG [933520:933752] [[Profiling]] CreateConfigAndPrefixImages was successful for deviceIndex 0. imageSize 172 [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmLopConfig.cpp:348] [DcgmLopConfig::CreateConfigAndPrefixImages]
>2023-01-09 17:34:34.533 DEBUG [933520:933752] [[Profiling]] counterDataImageSize 15316 [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmLopConfig.cpp:237] [DcgmLopConfig::InitializeWithMetrics]
>2023-01-09 17:34:34.533 DEBUG [933520:933752] [[Profiling]] InitializeCounterData was successful for deviceIndex 0 [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmLopConfig.cpp:96] [DcgmLopConfig::InitializeCounterData]
>2023-01-09 17:34:34.533 DEBUG [933520:933752] [[Profiling]] InitializeWithMetrics was successful for deviceIndex 0. 2 metrics [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmLopConfig.cpp:249] [DcgmLopConfig::InitializeWithMetrics]
>2023-01-09 17:34:34.533 DEBUG [933520:933752] [[Profiling]] Successfully added 1 metric groups. [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmLopGpu.cpp:166] [DcgmLopGpu::InitializeWithMetrics]
>2023-01-09 17:34:34.533 DEBUG [933520:933752] [[Profiling]] Enabling metrics for gpuId 0 [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:2588] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::ReconfigureLopGpu]
>**2023-01-09 17:34:34.535 ERROR [933520:933752] [[Profiling]] [PerfWorks] Got status 1 from NVPW_DCGM_PeriodicSampler_BeginSession() on deviceIndex 0 [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmLopGpu.cpp:351] [DcgmLopGpu::BeginSession]
>2023-01-09 17:34:34.535 ERROR [933520:933752] [[Profiling]] EnableMetrics returned -37 The third-party Profiling module returned an unrecoverable error [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:2591] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::ReconfigureLopGpu]
>2023-01-09 17:34:34.535 ERROR [933520:933752] [[Profiling]] Unable to reconfigure LOP metric watches for GpuId {0} [/workspaces/dcgm-rel_dcgm_3_1-postmerge/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:2680] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::ChangeWatchState]**


## 评论 (10)

### FindHao · 2023-01-17

I've seen this before. It is usually caused by other running profilers, such as ncu nvprof or another DCGM instance in embedded mode. 

### solrex · 2023-12-12

> I've seen this before. It is usually caused by other running profilers, such as ncu nvprof or another DCGM instance in embedded mode.

Thanks bro! I encountered exactly the same error when running `dcgmi dmon -e 1011` on the host machine after I had started a `[DCGM-Exporter](https://github.com/NVIDIA/dcgm-exporter)` docker container. The command goes back to normal after stopping the `DCGM-Exporter` container.

### nikkon-dev · 2023-12-12

The DCP metrics (1001-1014) require a unique lock in the same hardware used by the Nvidia profiler. This means that two different processes cannot access the same metrics. The nv-hostengine, the dcgm-exporter that runs the embedded hostengine, and the profiler are mutually exclusive.
There are several ways to avoid locks:
1. The dcgmi provides pause/resume functionality that can be used to stop DCP metrics gathering temporarily. This would allow run profiler.'
2. The dcgm-exporter can connect to a standalone nv-hostengine instead of running the embedded one - the `-r` command line argument.

### lynchyo · 2024-02-21

> The DCP metrics (1001-1014) require a unique lock in the same hardware used by the Nvidia profiler. This means that two different processes cannot access the same metrics. The nv-hostengine, the dcgm-exporter that runs the embedded hostengine, and the profiler are mutually exclusive. There are several ways to avoid locks:
> 
> 1. The dcgmi provides pause/resume functionality that can be used to stop DCP metrics gathering temporarily. This would allow run profiler.'
> 2. The dcgm-exporter can connect to a standalone nv-hostengine instead of running the embedded one - the `-r` command line argument.

If these two hostengines one is in a node，another is in the vm which is virtualized on this node，does this case works？ Thanks.

### nikkon-dev · 2024-02-21

@lynchyo,
It is only possible to support this if the GPU is in passthrough mode (meaning that the host does not see or use it). The limitation is due to hardware, not the driver/dcgm/profiling software.

### lynchyo · 2024-02-22

> @lynchyo, It is only possible to support this if the GPU is in passthrough mode (meaning that the host does not see or use it). The limitation is due to hardware, not the driver/dcgm/profiling software.

Get it, thank you very much.

### wxia6256 · 2025-01-17

> The DCP metrics (1001-1014) require a unique lock in the same hardware used by the Nvidia profiler. This means that two different processes cannot access the same metrics. The nv-hostengine, the dcgm-exporter that runs the embedded hostengine, and the profiler are mutually exclusive. There are several ways to avoid locks:
> 
> 1. The dcgmi provides pause/resume functionality that can be used to stop DCP metrics gathering temporarily. This would allow run profiler.'
> 2. The dcgm-exporter can connect to a standalone nv-hostengine instead of running the embedded one - the `-r` command line argument.

@nikkon-dev 
1. Are these locks the same ones that cause DCGM and NSIGHT conflicts?
2. You mentioned that the locks are mutually exclusive between the host-engine, DCGM-embedded and the 'profiler'. Does NSIGHT use the 'profiler' lock? If so, why does DCGM and NSIGHT conflict?
3. What happens when I query NVML_GPM metrics using NVML's `nvmlGpmMetricsGet` on two samples? Does it also use one of the locks from the above? Would NVML conflict with DCGM or NSIGHT?

### nikkon-dev · 2025-01-17

@wxia6256 ,

1. Yes. That is the same lock.
2. There is no "profiler" lock. The limiting resource is the perfmon subsystem on the GPU. Any software that wants to get profiling data (NSIGHT, DCGM) has to own the permon subsystem exclusively.
3. GPM utilizes a completely different GPU subsystem due to the locking issues between DCGM and NSIGHT. It does not rely on the perfmon subsystem and enables simultaneous metric collection and profiling. GPM can only be implemented on Hopper and newer architectures, as it requires hardware that older GPUs do not have.

### wxia6256 · 2025-01-17

@nikkon-dev  thanks for explaining. I was just trying get answers and found this interesting [line of DCGM code](https://github.com/NVIDIA/DCGM/blob/ddd6dcf4cb512ab94dacf58ba9ee0229c9a27982/dcgmlib/src/DcgmCacheManager.cpp#L11293) ( which I just realized you wrote :D ).

Does this mean that GPM-supported hardware (Hopper+ ?) won't ever cause lock issues on DCGM because it uses GPM instead of DCP?
 

### nikkon-dev · 2025-01-17

> Does this mean that GPM-supported hardware (Hopper+ ?) won't ever cause lock issues on DCGM because it uses GPM instead of DCP?

Yes. On GPM-supported platforms, the profiling module is not even loaded in DCGM, and metrics are collected directly via NVML GPM API.
