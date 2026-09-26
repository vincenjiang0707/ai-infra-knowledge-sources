source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/kubernetes-deployment/operate/disagg-communication
lastmod: 2026-09-23T23:30:39.914Z

# Disaggregated Inference Communication Guide

Best practices for prefill/decode worker communication on Kubernetes

This guide explains how prefill and decode workers communicate in Dynamo’s disaggregated inference architecture on Kubernetes. It answers the frequently asked question: **Why can’t prefill and decode workers use NVLink to communicate on the same node?**

## Summary

**NVLink cannot be used between Kubernetes pods**due to process isolation and GPU partitioning**RDMA (InfiniBand, RoCE, or AWS EFA) is required**for production disaggregated deployments**Without RDMA, expect 200-500x performance degradation**in Time To First Token (TTFT) — observed ~98s TTFT with TCP vs ~200-500ms with RDMA**UCX or libfabric**are the communication layers that NIXL uses to transfer KV cache between workers**Topology-aware KV transfer**can constrain or bias decode routing so KV transfers stay within a selected topology domain such as zone or rack. See[Topology-Aware KV Transfer](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/topology-aware-kv-transfer).

## Architecture Overview

### Communication Stack

### Component Responsibilities

## Why NVLink Cannot Be Used Between Pods

### The Fundamental Constraint

NVLink is a **direct GPU-to-GPU interconnect** that operates at the hardware level. It requires:

**Same process**- Both GPUs must be visible to a single process so`cudaDeviceEnablePeerAccess()`

can be called**Direct memory access**- Process must have permission to access both GPU memory regions**Peer-to-peer mapping**- CUDA runtime must establish memory mappings between GPUs

**Kubernetes pods violate all three requirements:**

### Technical Explanation

-
**Process Isolation**: Kubernetes pods run in separate Linux namespaces. Even on the same node, Pod A cannot directly access Pod B’s memory space. -
**GPU Partitioning**: The Kubernetes device plugin assigns specific GPUs to each pod via`CUDA_VISIBLE_DEVICES`

. Pod A’s GPU 0 and Pod B’s GPU 0 are physically different devices. -
**Process/Namespace Isolation**: Each pod runs in a separate process namespace. NVLink peer-to-peer transfers require both GPUs to be within the same process so`cudaDeviceEnablePeerAccess()`

can be called. -
**Memory Registration**: NVLink transfers use`cudaMemcpy`

with peer access enabled. This requires calling`cudaDeviceEnablePeerAccess()`

- impossible across process boundaries.

### Where NVLink DOES Work

NVLink works **within a pod** for parallelism strategies (TP, EP) where all GPUs are in the same process:

## Supported Communication Options

### Transport Comparison

### Same-Node Communication

When prefill and decode workers are on the **same physical node**:

**Options (best to worst):**

- InfiniBand RDMA with GPUDirect → GPU-to-GPU, bypasses CPU
- RoCE RDMA with GPUDirect → GPU-to-GPU, bypasses CPU
- Host-staged RDMA → GPU→CPU→RDMA→CPU→GPU
- TCP (fallback) → GPU→CPU→TCP→CPU→GPU

**Best Practice**: Use RDMA even for same-node communication. The overhead is minimal and it provides consistent behavior whether pods land on the same or different nodes.

### Cross-Node Communication

When prefill and decode workers are on **different nodes**:

**Requirements for optimal cross-node performance:**

- RDMA network fabric (InfiniBand, RoCE, or AWS EFA)
- GPUDirect RDMA enabled (GPU memory registered with NIC)
- Proper UCX or libfabric configuration

## UCX Configuration Reference

### Environment Variables

UCX behavior is controlled through environment variables. Set these on both prefill and decode worker pods.

#### Core Transport Selection

**Excluding transports**: Use `^`

prefix to exclude (e.g., `UCX_TLS=^mm`

excludes memory mapping).

**Note**: When specifying `UCX_TLS`

explicitly with GPU memory, you must include `cuda_copy`

or `cuda_ipc`

for UCX to recognize GPU buffers.

#### Rendezvous Protocol Settings

**Recommendation**: Use `get_zcopy`

with threshold `0`

for KV cache transfers (always large).


⚠️ AWS EFA Exception: Do NOT use`get_zcopy`

on AWS with Ubuntu 24.04 + Kernel ≥6.8. See[AWS EFA Configuration]for required settings.

#### Memory Registration

#### Debugging and Diagnostics

**Note**: UCX statistics (`UCX_STATS_DEST`

, `UCX_STATS_TRIGGER`

) require UCX compiled with `--enable-stats`

flag, which is not enabled in default builds.

### Complete Production Configuration

### InfiniBand Configuration

For clusters with InfiniBand RDMA (e.g., ConnectX NICs), use UCX with the `rc`

(Reliable Connection) transport. This is the standard path for on-premises and bare-metal Kubernetes clusters.

**RDMA Resources:**

Request one `rdma/ib`

device per GPU. The RDMA device plugin injects `/dev/infiniband/*`

devices automatically:

No pod annotations are needed. InfiniBand devices are injected by the device plugin.

**Security Context:**

Add `IPC_LOCK`

and `SYS_RESOURCE`

capabilities. `IPC_LOCK`

allows RDMA memory pinning, `SYS_RESOURCE`

allows memlock limit escalation:

**Environment Variables (worker containers):**


Note:`UCX_IB_ADDR_TYPE=eth`

is the most common missing setting when bringing up NIXL disagg on InfiniBand clusters. If NIXL init succeeds but transfers fail with`NIXL_ERR_REMOTE_DISCONNECT`

, this is likely the cause.

**Known Issue — Bonded IB devices:**

Some clusters expose bonded InfiniBand devices (e.g., `mlx5_bond_0`

) with LID=0. If UCX selects a bonded device, transfers may fail. Verify device LIDs and select a non-bonded device:

### AWS EFA Configuration

NIXL supports **libfabric** as the backend for AWS EFA deployments. This is the **recommended approach** for disaggregated inference on AWS, achieving ~9.6 GB/s KV transfer bandwidth. See the [AWS EFA with NIXL documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start-nixl.html) for complete setup instructions.

**Requirements:**

- EFA installer version
**1.47.0**or later - Libfabric (installed via EFA installer at
`/opt/amazon/efa`

) - GDRCopy for GPU Direct RDMA operations (GPU Operator v26.x installs this automatically)
- EFA-enabled container image (e.g.,
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.2.0-efa-amd64`

)

**Kernel Compatibility:**

GDRCopy v2.5.1 has a build failure on kernel 6.15+ due to a `vm_flags_set`

redefinition. Pin your Ubuntu EKS AMI to kernel 6.14 or earlier until GDRCopy v2.5.2 is available in GPU Operator.

**Pod Anti-Affinity (Required):**

EFA is designed for **cross-node** communication. Prefill and decode workers must be scheduled on **different nodes** to avoid EAGAIN errors during KV transfer.


Note: Anti-affinity only needs to be configured on one side (here, the decode worker). The Kubernetes scheduler enforces the constraint symmetrically—if decode cannot be placed with prefill, they will end up on different nodes regardless of which pod has the rule.

**EFA Resource Requests:**

Request EFA interfaces in your pod spec. The p5.48xlarge instance has **32 EFA interfaces** (32 network cards × 1 interface each) with 3200 Gbps total bandwidth. The number of interfaces to allocate per worker depends on your deployment:

Example with 4 EFA interfaces (validated configuration):


Note: NIXL/libfabric automatically stripes traffic across all allocated EFA interfaces. The 4-interface configuration achieved ~9.6 GB/s in testing, which is sufficient for Llama-3.1-8B KV cache transfers at ISL=8000. Increase the count if your workload requires higher bandwidth (e.g., larger models or higher TP).

**Environment Variables:**

**vLLM Configuration:**

**Verification:**

**Expected Log Output:**

## Deployment Configuration

### Kubernetes Resource Requirements

### Required Capabilities and Resources

### Infrastructure Prerequisites

-
**RDMA Device Plugin**: Exposes`rdma/ib`

or`vpc.amazonaws.com/efa`

resources to Kubernetes -
**RDMA Network**: One of:- InfiniBand or RoCE fabric
- AWS EFA (Elastic Fabric Adapter)

-
**GPUDirect RDMA**(optional but recommended):- NVIDIA driver with GPUDirect enabled
`nvidia-peermem`

kernel module loaded (InfiniBand/RoCE)- GDRCopy installed (AWS EFA with libfabric)


## Diagnostics and Performance Validation

### Pre-Deployment Validation

#### 1. Verify RDMA Availability

Expected output shows InfiniBand or RoCE devices:

#### 2. Check UCX Transport Capabilities

Look for GPU memory support:

**If you only see host**: GPUDirect RDMA is not working. KV transfers will use host staging.

#### 3. Test UCX Performance

**Expected bandwidth**:

- InfiniBand HDR: 20-25 GB/s per port
- RoCE 100GbE: 10-12 GB/s
- TCP fallback: 1-2 GB/s

### NIXL Benchmark Tool

Deploy the NIXL benchmark to validate end-to-end KV transfer performance:

This deploys a benchmark that measures actual GPU-to-GPU transfer rates through NIXL.

### Runtime Diagnostics

#### Verify NIXL Backend Initialization

**Good output**:

**Bad output** (RDMA not working):

#### Monitor Transfer Performance

Check Grafana dashboards for:

**NIXL transfer bandwidth**: Should show GB/s, not MB/s**KV cache transfer latency**: Should be under 500ms for typical workloads

**Red flags indicating RDMA issues**:

- Transfer bandwidth under 1 GB/s
- TTFT > 10 seconds
`Unsupported operation`

errors in logs

### Common Diagnostic Commands

## Performance Expectations

### KV Cache Transfer Overhead


Note: For AWS EFA deployments, use libfabric with GDRCopy to enable GPUDirect RDMA. UCX on AWS EFA does not support GPUDirect on kernel ≥6.8 and results in severely degraded performance. See[AWS EFA Configuration]for setup instructions.

### When Disaggregated Makes Sense

**Use disaggregated architecture when:**

- Input sequence length (ISL) ≥ 4000 tokens (14-22% throughput gain)
- You need independent scaling of prefill vs decode capacity
- Prefill and decode have different hardware requirements

**Use aggregated architecture when:**

- Low-latency TTFT is critical
- Input sequences under 2000 tokens (minimal disagg benefit)
- RDMA is not available

### Break-Even Analysis

The KV transfer overhead is amortized across output tokens. **Measured data from Llama-3.1-8B-Instruct** on AWS p5.48xlarge with NIXL+libfabric:

**Key Insight**: The KV transfer overhead via libfabric+EFA is only **~37ms**. Combined with 41% faster decode (ITL), disaggregated inference delivers **22% higher throughput** for prefill-bound workloads.

**Disagg advantage scales with input length (ISL)** (all at OSL=50, concurrency=10):

## Troubleshooting Guide

### Problem: TTFT is 10+ seconds

**Symptoms**: TTFT degrades from expected 200-500ms to 10+ seconds

**Root Cause**: RDMA not active, falling back to TCP

**Diagnosis**:

**Solutions**:

- Verify RDMA device plugin is installed
- Add
`rdma/ib`

resource requests to pod spec - Add
`IPC_LOCK`

capability - Set UCX environment variables

### Problem: “Unsupported operation” errors

**Symptoms**: Logs show `Unexpected UCX error: Unsupported operation`


**Root Cause**: UCX attempting GPU RDMA on hardware that doesn’t support it

**Solutions**:

- Check if GPUDirect RDMA is enabled:
`ucx_info -d | grep cuda`

- If not supported, set
`UCX_RNDV_THRESH=inf`

to disable GPU RDMA - Verify
`nvidia-peermem`

module is loaded

### Problem: AWS EFA not using GPU Direct

**Symptoms**: 3x performance degradation on AWS despite EFA configured

**Root Cause**: GPU Direct RDMA not functional on kernel ≥6.8 with EFA when using UCX

**Solution**: Use libfabric instead of UCX for AWS EFA deployments. Libfabric with GDRCopy provides efficient GPU Direct RDMA operations on AWS. See the [AWS EFA Configuration](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/disagg-communication#aws-efa-configuration) section for setup instructions.

**Alternative options** (if libfabric is not available):

- Use kernel before 6.8 (Ubuntu 22.04 with kernel 5.15)
- Accept host-staging performance penalty

### Problem: EFA EAGAIN errors (fi_read still retrying)

**Symptoms**: Decode worker logs show repeated EAGAIN errors:

**Root Cause**: Prefill and decode workers are scheduled on the **same node**. AWS EFA is designed for cross-node communication and does not function correctly for intra-node transfers.

**Diagnosis**:

If both prefill and decode workers show the same NODE, this is the problem.

**Solution**: Add pod anti-affinity rules to ensure workers are scheduled on different nodes:


Note: Use`nvidia.com/dynamo-component`

as the label key, not`app.kubernetes.io/component`

. The Dynamo operator uses this label to identify component types.

### Problem: NIXL_ERR_BACKEND at create_backend on InfiniBand

**Symptoms**: NIXL backend creation fails immediately with `NIXL_ERR_BACKEND`

. UCX logs show:

Or:

**Root Causes**:

-
**Bonded IB device with LID=0**: UCX selects`mlx5_bond_0`

by default, but bonded devices may have LID=0 (invalid for UD transport). Fix: set`UCX_NET_DEVICES`

to a non-bonded device with a valid LID. -
**UCX/OFED version mismatch**: The container’s UCX mlx5 library may be compiled against a different devx ABI than the host kernel driver. Any transport using IB (rc, cuda_ipc with IB) triggers the devx crash. -
**Missing RDMA device injection**: If`rdma/ib`

is not requested in the pod spec, no IB devices are injected into the container.

**Diagnosis**:

**Solutions**:

- Request
`rdma/ib`

resources (1 per GPU) in the pod spec - Set
`UCX_NET_DEVICES`

to a non-bonded device if`mlx5_bond_0`

has LID=0 - Ensure the container image’s UCX build matches the host OFED version

### Problem: Intermittent transfer failures

**Symptoms**: Sporadic `getXferStatus: backend 'UCX' returned error status`


**Diagnosis**:

**Common causes**:

- Network congestion or packet loss
- Mismatched UCX versions between pods
- RDMA resource exhaustion

## Quick Reference

### Minimum Viable RDMA Configuration

### Diagnostic Checklist

-
`rdma/ib`

resources visible:`kubectl get nodes -o jsonpath='{..allocatable.rdma/ib}'`

- NIXL initialized:
`kubectl logs <pod> | grep "Backend"`

- Transfer bandwidth > 1 GB/s (check Grafana metrics)

**For UCX deployments:**

- UCX sees RDMA devices:
`ucx_info -d | grep "Transport: rc"`

- UCX sees GPU memory:
`ucx_info -d | grep "memory types.*cuda"`


**For libfabric deployments (AWS EFA):**

- EFA devices available:
`fi_info -p efa`

- GDRCopy installed:
`ls /dev/gdrdrv`