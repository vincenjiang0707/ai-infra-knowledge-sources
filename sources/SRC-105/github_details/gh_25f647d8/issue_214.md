# [Issue #214] DCGM_FI_PROF_NVLINK_TX_BYTES Metric Disappears After Running for a Period of Time

source: https://github.com/NVIDIA/DCGM/issues/214
state: open | updated: 2025-02-20T18:58:31Z
labels: 

## 正文

Description:
We have observed an issue with DCGM where the DCGM_FI_PROF_NVLINK_TX_BYTES metric is initially available when DCGM starts but disappears after running for a period of time (ranging from 5 minutes to 1 hour). When this happens, the following error message is logged:

`ERROR [1:41] Got nvml st 4 from nvmlGpmSampleGet(). [/workspaces/dcgm-rel_dcgm_3_3-postmerge/dcgmlib/src/DcgmGpmManager.cpp:161] [DcgmGpmManagerEntity::MaybeFetchNewSample]
`

System Information:
OS Version: Rocky Linux 9.2 (Blue Onyx)
Kernel Version: 5.14.0-284.25.1.el9_2.x86_64
DCGM Version: test0-3.2.5-3.1.7-ubi8-diamond-r1
Driver Version: 550.90.07
Container Permissions: SYS_ADMIN
Findings:
Granting the container privileged mode (--privileged) eliminates the issue.
However, from a security perspective, granting privileged mode is not a recommended solution.
The issue does not appear immediately; the metric is available initially and disappears only after a period of GPU workload execution, which suggests that this may not be a simple permission-related issue.
Request for Assistance:
Could this be related to resource exhaustion, NVML state changes, or DCGM internal behavior when handling GPU telemetry over time?
Are there known cases where nvmlGpmSampleGet() returns st 4 in long-running workloads?
Are there recommended configurations or alternative permissions that allow stable collection of DCGM_FI_PROF_NVLINK_TX_BYTES without requiring privileged mode?
Any insights or debugging suggestions would be greatly appreciated. Thank you!

## 评论 (1)

### nikkon-dev · 2025-02-20

@Paladin1412,

This error comes from the underlying library and is very unexpected, especially if metrics work initially.

Could you collect the debug logs by setting the env variables for the process: `__NVML_DBG_LVL=DEBUG` and `__NVML_DBG_FILE=path_to_log_file`? The produced log file will be encrypted.
