# [Issue #303] DCGM profiling metrics report 0 after Xid 31 while GPU remains active; nv-hostengine GetSamples -37

source: https://github.com/NVIDIA/DCGM/issues/303
state: open | updated: 2026-06-17T18:40:53Z
labels: 

## 正文

## Summary

We observed a case where, after a GPU Xid 31 MMU fault, DCGM profiling metrics for the affected GPU were exported as `0` even though the GPU remained capable of running new workloads and standard utilization telemetry still reported high GPU utilization.

The main symptom is a divergence between:

- `DCGM_FI_DEV_GPU_UTIL = 100`
- `DCGM_FI_PROF_GR_ENGINE_ACTIVE = 0`

for the same GPU, while a healthy peer GPU under the same workload reports both high GPU utilization and near-fully-active profiling metrics.

`nv-hostengine` logs show the failure originates in the DCGM profiling / PerfWorks sampling path:

```text
[Profiling] [PerfWorks] Decoded zero samples after 48 attempt(s) to decode counters
[Profiling] Got error from GetSamples: -37 The third-party Profiling module returned an unrecoverable error
````

Restarting DCGM resolves the issue temporarily.

## Environment

### Host

```text
Host: phx8-2fa
OS: Debian GNU/Linux 12 (bookworm)
Kernel: Linux 6.18.30-1
Architecture: x86_64
```

### NVIDIA driver / CUDA

```text
NVIDIA-SMI: 590.48.01
Driver Version: 590.48.01
CUDA Version reported by nvidia-smi: 13.1
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64 590.48.01
```

### GPUs

The node has 4x Quadro RTX 5000 GPUs:

```text
GPU 0: Quadro RTX 5000
UUID: GPU-9d3de631-3422-9bc2-c43e-5e9106c621f4
PCI Bus ID: 00000000:3B:00.0
VBIOS: 90.04.87.00.03

GPU 1: Quadro RTX 5000
UUID: GPU-d8a1127b-afb2-7a36-9c90-37d0bb7e0a90
PCI Bus ID: 00000000:5E:00.0
VBIOS: 90.04.87.00.03

GPU 2: Quadro RTX 5000
UUID: GPU-a76358a7-c820-d3dc-ad4e-2ff0d26935b2
PCI Bus ID: 00000000:86:00.0
VBIOS: 90.04.87.00.03

GPU 3: Quadro RTX 5000
UUID: GPU-893e8405-030d-31eb-a44e-982d4d646a22
PCI Bus ID: 00000000:AF:00.0
VBIOS: 90.04.87.00.03
```

The affected GPU is:

```text
GPU index: 3
UUID: GPU-893e8405-030d-31eb-a44e-982d4d646a22
PCI Bus ID: 00000000:AF:00.0
```

### MIG

MIG is not applicable on this node/GPU model:

```text
mig.mode.current: [N/A]
mig.mode.pending: [N/A]
```

### DCGM / nv-hostengine / exporter

```text
dcgmi version: 4.4.2
nv-hostengine version: 4.4.2
nv-hostengine Build ID: 15378
nv-hostengine Build Date: 2025-11-12
nv-hostengine Build Type: RelWithDebInfo
nv-hostengine Commit ID: 354202804259a367f548cc92998629e311841f4c
nv-hostengine Branch Name: v4.4.2
```

dcgm-exporter image:

```text
nvcr.io/nvidia/k8s/dcgm-exporter:4.4.2-4.7.0-ubuntu22.04
```

Exporter scrape interval:

```text
1 minute
```

This scrape interval makes a high-frequency polling explanation unlikely.

## Deployment / topology

There are two dcgm-exporter-related containers running on the affected node:

```text
dcgm-exporter
dcgm-exporter-physical
```

Both have `dcgmi 4.4.2` available.

`crictl` showed both containers using the same image ID:

```text
IMAGE: f8693602cfb82
```

The failure appears to happen upstream of dcgm-exporter because `nv-hostengine` itself logs the profiling / PerfWorks / `GetSamples` error before the metric is exposed as `0`.

## DCGM discovery output

`dcgmi discovery -l` sees all 4 GPUs correctly and maps the affected GPU as GPU ID 3:

```text
4 GPUs found.

GPU ID: 0
Name: Quadro RTX 5000
PCI Bus ID: 00000000:3B:00.0
Device UUID: GPU-9d3de631-3422-9bc2-c43e-5e9106c621f4

GPU ID: 1
Name: Quadro RTX 5000
PCI Bus ID: 00000000:5E:00.0
Device UUID: GPU-d8a1127b-afb2-7a36-9c90-37d0bb7e0a90

GPU ID: 2
Name: Quadro RTX 5000
PCI Bus ID: 00000000:86:00.0
Device UUID: GPU-a76358a7-c820-d3dc-ad4e-2ff0d26935b2

GPU ID: 3
Name: Quadro RTX 5000
PCI Bus ID: 00000000:AF:00.0
Device UUID: GPU-893e8405-030d-31eb-a44e-982d4d646a22

0 NvSwitches found.
0 ConnectX found.
0 CPUs found.
```

## DCGM field groups

`dcgmi fieldgroup -l` shows exporter-created field groups that include profiling fields:

```text
ID: 20
Name: gpu-collector-fieldgroup-18271970685516159845
Field IDs:
1002, 1003, 1001, 1005, 1004, 155, 156, 150, 140,
251, 252, 250, 230, 100, 101, 203, 204, 206, 207,
1009, 1010, 1007, 253
```

and:

```text
ID: 39
Name: gpu-collector-fieldgroup-16377074464650574493
Field IDs:
1009, 1010
```

So the exporter/DCGM setup is actively collecting `DCGM_FI_PROF_*` fields.

## Timeline / reproduction

### 1. Before the fault

Before fault injection:

* `nv-hostengine` was running.
* dcgm-exporter was running.
* DCGM profiling metrics were reporting normally.
* Both standard telemetry and profiling metrics were being exported.

### 2. Fault injection

A controlled Python/CUDA workload intentionally performed an invalid GPU memory access. The kernel logged an Xid 13 graphics exception followed by an Xid 31 MMU fault.

Kernel log excerpt:

```text
Jun 10 03:09:55 phx8-2fa kernel: NVRM: GPU at PCI:0000:af:00: GPU-893e8405-030d-31eb-a44e-982d4d646a22
Jun 10 03:09:55 phx8-2fa kernel: NVRM: GPU Board Serial Number: 1322019051845
Jun 10 03:09:55 phx8-2fa kernel: NVRM: Xid (PCI:0000:af:00): 13, pid=108743, name=python, Graphics Exception: channel 0x0000000b, Class 0000c5c0, Offset 00000000, Data 00000000
Jun 10 03:09:55 phx8-2fa kernel: NVRM: Xid (PCI:0000:af:00): 31, pid=108743, name=python, channel 0x0000000b, intr 00000000. MMU Fault: ENGINE GRAPHICS GPC0 GPCCLIENT_T1_0 faulted @ 0x0_deadb000.
```

Important details:

```text
Xid 13 and Xid 31 occurred at the same timestamp.
Both came from process: python.
Both came from GPU channel: 0x0000000b.
The Xid 31 fault address was: 0x0_deadb000.
The affected GPU was PCI 0000:af:00 / UUID GPU-893e8405-030d-31eb-a44e-982d4d646a22.
```

### 3. DCGM profiling failure shortly after the Xid

About 21 seconds later, `nv-hostengine` logged:

```text
2026-06-10 03:10:16.478 ERROR [69:98] [[Profiling]] [PerfWorks] Decoded zero samples after 48 attempt(s) to decode counters [/builds/dcgm/dcgm/dcgm_private/modules/profiling/DcgmLopConfig.cpp:586] [DcgmLopConfig::GetSamples]

2026-06-10 03:10:16.478 ERROR [69:98] [[Profiling]] Got error from GetSamples: -37 The third-party Profiling module returned an unrecoverable error [/builds/dcgm/dcgm/dcgm_private/modules/profiling/DcgmModuleProfiling.cpp:1627] [DcgmNs::Modules::Profiling::DcgmModuleProfiling::ReadGpuMetrics]
```

This points to the DCGM profiling path:

```text
DcgmModuleProfiling::ReadGpuMetrics
  -> DcgmLopConfig::GetSamples
    -> PerfWorks counter/sample decoding
```

## Observed behavior after the fault

After deleting the workload that triggered Xid 31, a new workload was created to keep all GPUs busy.

The affected GPU still reported normal basic utilization:

```text
DCGM_FI_DEV_GPU_UTIL{gpu="3",UUID="GPU-893e8405-030d-31eb-a44e-982d4d646a22",pci_bus_id="00000000:AF:00.0",device="nvidia3",modelName="Quadro RTX 5000",Hostname="phx8-2fa",container="gpu-workload",namespace="default",pod="gpu-busy-test-all-gpus"} 100
```

But the profiling metric for the same GPU reported zero:

```text
DCGM_FI_PROF_GR_ENGINE_ACTIVE{gpu="3",UUID="GPU-893e8405-030d-31eb-a44e-982d4d646a22",pci_bus_id="00000000:AF:00.0",device="nvidia3",modelName="Quadro RTX 5000",Hostname="phx8-2fa",container="gpu-workload",namespace="default",pod="gpu-busy-test-all-gpus"} 0.000000
```

A healthy peer GPU under the same busy workload reported expected profiling activity:

```text
DCGM_FI_DEV_GPU_UTIL{gpu="2",UUID="GPU-a76358a7-c820-d3dc-ad4e-2ff0d26935b2",pci_bus_id="00000000:86:00.0",device="nvidia2",modelName="Quadro RTX 5000",Hostname="phx8-2fa",container="gpu-workload",namespace="default",pod="gpu-busy-test-all-gpus"} 100

DCGM_FI_PROF_GR_ENGINE_ACTIVE{gpu="2",UUID="GPU-a76358a7-c820-d3dc-ad4e-2ff0d26935b2",pci_bus_id="00000000:86:00.0",device="nvidia2",modelName="Quadro RTX 5000",Hostname="phx8-2fa",container="gpu-workload",namespace="default",pod="gpu-busy-test-all-gpus"} 0.998893
```

## Expected behavior

After the faulting workload exits and the GPU is capable of running new workloads, DCGM profiling metrics should either:

1. recover and report valid profiling samples, or
2. clearly indicate that profiling metrics are invalid, unavailable, or stale.

A numeric `0` is misleading because it is indistinguishable from real engine inactivity to downstream consumers.

## Actual behavior

After Xid 31:

* The GPU continues to run new workloads.
* `DCGM_FI_DEV_GPU_UTIL` reports `100`.
* `DCGM_FI_PROF_GR_ENGINE_ACTIVE` reports `0`.
* `nv-hostengine` logs PerfWorks decode failures.
* `nv-hostengine` returns `GetSamples: -37`.
* dcgm-exporter continues exposing the profiling field as a numeric zero.
* Restarting DCGM resolves the issue temporarily.

## Restart behavior

Restarting DCGM resolved the issue temporarily and profiling metrics recovered.

This makes the stale/failed DCGM profiling-path hypothesis stronger, because basic GPU execution was not persistently broken and the GPU remained capable of running workloads.

## Why this does not look like actual GPU idleness

The affected GPU showed:

```text
DCGM_FI_DEV_GPU_UTIL = 100
DCGM_FI_PROF_GR_ENGINE_ACTIVE = 0
```

A healthy peer GPU under the same workload showed:

```text
DCGM_FI_DEV_GPU_UTIL = 100
DCGM_FI_PROF_GR_ENGINE_ACTIVE ~= 0.999
```

Therefore, the affected GPU was not idle. The zero value appears to represent an invalid/stale profiling sample rather than real engine inactivity.

## Why this does not look like a dcgm-exporter root cause

dcgm-exporter exported the bad-looking zero value, but `nv-hostengine` had already logged the lower-level profiling failure:

```text
[Profiling] [PerfWorks] Decoded zero samples after 48 attempt(s) to decode counters
[Profiling] Got error from GetSamples: -37
```

So the primary failure appears to be upstream of exporter, in DCGM's profiling module / PerfWorks sample read path.

Exporter behavior may still be worth reviewing because an invalid profiling sample appears to be exposed as a numeric `0`.

## Why this does not look like high-frequency polling

The exporter scrape interval is:

```text
1 minute
```

So this does not appear to be caused by polling above 10 Hz / below 100 ms.

## Current hypothesis

A GPU channel/MMU fault, represented by Xid 31, can leave DCGM's PerfWorks-backed profiling sampling path in a failed or stale state for the affected GPU.

Basic GPU telemetry continues to work, but profiling counters become unreadable or undecodable. In this state, `DCGM_FI_PROF_*` fields are exported as numeric zero, even while the GPU continues to run workloads.

Proposed causal chain:

```text
Fault-injection Python workload
  -> invalid GPU memory access
  -> Xid 13 graphics exception on channel 0x0000000b
  -> Xid 31 MMU fault on the same channel at 0x0_deadb000
  -> driver recovers or tears down the faulted GPU channel
  -> GPU remains usable for future CUDA workloads
  -> DCGM profiling backend attempts to read profiling samples
  -> PerfWorks decodes zero samples after 48 attempts
  -> DCGM profiling GetSamples returns -37 unrecoverable error
  -> dcgm-exporter continues exposing the watched profiling field
  -> profiling metric is exported as 0
  -> observed mismatch: GPU_UTIL = 100, PROF_GR_ENGINE_ACTIVE = 0
```

## Impact

This creates a dangerous observability state:

* GPU is actively running work.
* Standard utilization telemetry still shows activity.
* `DCGM_FI_PROF_*` metrics show zero.
* Dashboards may show false idle.
* Alerts based only on profiling counters may fail.
* Accounting, scheduling, or health checks based on profiling counters may make incorrect decisions.

This is especially important for users relying on fields such as:

```text
DCGM_FI_PROF_GR_ENGINE_ACTIVE
DCGM_FI_PROF_SM_ACTIVE
other DCGM_FI_PROF_* metrics
```

## Reproducer

The issue was reproduced with a pod running a Python/CUDA workload that intentionally performs an invalid memory access, followed by another workload that keeps GPUs busy.

The fault kernel writes to an invalid address:

```cuda
__global__ void fault_kernel(int mode) {
    if (blockIdx.x == 0 && threadIdx.x == 0) {
        if (mode == 0) {
            volatile unsigned int *ptr =
                reinterpret_cast<volatile unsigned int *>(0xDEADBEEF);
            *ptr = 0x12345678;
        } else {
            volatile unsigned int *ptr =
                reinterpret_cast<volatile unsigned int *>(0x0);
            *ptr = 0x12345678;
        }
    }
}

void launch_fault_kernel(int mode) {
    fault_kernel<<<1, 1>>>(mode);
    CUDA_CHECK(cudaDeviceSynchronize());
}
```

The repro used `nvcr.io/nvidia/pytorch:25.05-py3` and `CUDA_LAUNCH_BLOCKING=1`.

After the Xid was triggered, a separate pod kept GPUs busy using repeated matrix multiplication on CUDA devices.

## Additional notes

Older unrelated log messages existed for NvSwitch / NSCQ / NVSDM module loading, but those occurred days before the Xid/profiling failure and do not appear to be in the profiling module path.

The relevant failure is tightly coupled to:

```text
Xid 31 on the affected GPU
-> nv-hostengine Profiling / PerfWorks / GetSamples error
-> DCGM_FI_PROF_* exported as 0 for the affected GPU
```

## Questions

1. Is `GetSamples: -37` after Xid 31 expected to require a DCGM restart for profiling metrics to recover?
2. Should `DCGM_FI_PROF_*` fields be reported as invalid, blank, unavailable, or stale instead of numeric `0` when PerfWorks sample decoding fails?
3. Is there a supported way to reset or reinitialize the profiling collection path for only one affected GPU, without restarting all of DCGM?
4. Are there additional `nv-hostengine`, DCGM, PerfWorks, or driver-level debug logs that would help determine whether the stale state is owned by DCGM, PerfWorks, the NVIDIA driver profiling interface, or an interaction among them?
5. Is this a known limitation after GPU Xid/MMU faults, or should DCGM automatically recover profiling collection after the faulted channel is torn down?


## 评论 (1)

### amitaekbote · 2026-06-17

to add to this, are there any tools/test suites we could use to reproduce these kind of errors? 
