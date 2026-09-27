# [Issue #241] [Feature Request] Add Process Information Fields to DCGM Exporter for GPU Allocation Detection

source: https://github.com/NVIDIA/DCGM/issues/241
state: open | updated: 2026-04-06T15:54:19Z
labels: 

## 正文

## Problem
Currently, DCGM Exporter lacks direct process information fields that would allow accurate detection of GPU allocation status. This makes it difficult to distinguish between:
- GPUs allocated to Kubernetes pods
- GPUs used directly on nodes (outside of pod allocation)
- Truly idle GPUs

## Current Limitation
DCGM doesn't expose these fields

## Requested Features
Please add the following process-related fields to DCGM
1. DCGM_FI_DEV_PIDS
   - Description: List of compute process PIDs using the GPU
   - Use case: Detect active compute workloads

## Use Cases

### 1. Kubernetes GPU Management
- Detect when GPUs are used outside of pod allocation
- Accurate billing and resource accounting
- Prevent resource conflicts

### 2. Multi-tenant Environments
- Track actual GPU usage vs. allocated resources
- Identify resource waste and optimization opportunities
- Implement fair-share policies

### 3. Monitoring and Alerting
- Real-time GPU allocation status
- Process-level GPU usage tracking
- Automated resource management

## Current Workaround Limitations

We currently use indirect methods like memory usage and GPU utilization:
```yaml
DCGM_FI_DEV_FB_USED_PERCENT > 5% = allocated
DCGM_FI_DEV_GPU_UTIL > 1% = allocated

Problems with this approach:

False positives from background processes
Delayed detection of allocation changes
Cannot identify specific processes
Inaccurate in mixed workload scenarios

## 评论 (1)

### nccurry · 2026-04-06

Related issue [DCGM Exporter #521](https://github.com/NVIDIA/dcgm-exporter/issues/521)
