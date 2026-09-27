# [Issue #558] [Bug]: --list-metrics is missleading

source: https://github.com/ROCm/rocprofiler-compute/issues/558
state: closed | updated: 2025-08-06T18:23:07Z
labels: bug, triage, Under Investigation

## 正文

### Describe the bug

--list-metrics gfx908
lists metrics as available that are not in fact possible on the selected ISA

For  `rocprof-compute analyze -p workloads/occupancy/MI100 --list-metrics gfx908` we get:

```
0 -> Top Stats
1 -> System Info
2 -> System Speed-of-Light
	2.1 -> Speed-of-Light
		2.1.0 -> VALU FLOPs
		2.1.1 -> VALU IOPs
		2.1.2 -> MFMA FLOPs (BF16)
		2.1.3 -> MFMA FLOPs (F16)
		2.1.4 -> MFMA FLOPs (F32)
		2.1.5 -> MFMA FLOPs (F64)
		2.1.6 -> MFMA IOPs (Int8)
		2.1.7 -> Active CUs
		2.1.8 -> SALU Utilization
		2.1.9 -> VALU Utilization
		2.1.10 -> MFMA Utilization
		2.1.11 -> VMEM Utilization
		2.1.12 -> Branch Utilization
		2.1.13 -> VALU Active Threads
		2.1.14 -> IPC
		2.1.15 -> Wavefront Occupancy
		2.1.16 -> Theoretical LDS Bandwidth
		2.1.17 -> LDS Bank Conflicts/Access
		2.1.18 -> vL1D Cache Hit Rate
		2.1.19 -> vL1D Cache BW
		2.1.20 -> L2 Cache Hit Rate
		2.1.21 -> L2 Cache BW
		2.1.22 -> L2-Fabric Read BW
		2.1.23 -> L2-Fabric Write BW
		2.1.24 -> L2-Fabric Read Latency
		2.1.25 -> L2-Fabric Write Latency
		2.1.26 -> sL1D Cache Hit Rate
		2.1.27 -> sL1D Cache BW
		2.1.28 -> L1I Hit Rate
		2.1.29 -> L1I BW
		2.1.30 -> L1I Fetch Latency
3 -> Memory Chart
...
```

Clearly this is wrong, there is no way 2.1.0 -> VALU FLOPs will ever give a usefull value on gfx908 as it lacks a formular:
https://github.com/ROCm/rocprofiler-compute/blob/bceddb094316a304334f0940c962eee85f011ef3/src/rocprof_compute_soc/analysis_configs/gfx908/0200_system-speed-of-light.yaml#L24

Further i find it very bad UX that rocprofiler-compute analyze simply prints an empty field for 'None', instead the field should be filled with "Unsupported" or "N/A (HW)" or something to that effect.

### Linux Distribution

Any

### ROCm Compute Profiler Version

Git at 3396ba39064afe5946a9ccf37fb9130ad0bc0cfd

### GPU

MI100

### ROCm Version

6.3.2

### Reproducer

run: rocprof-compute analyze -p workloads/occupancy/MI100 --list-metrics gfx908

### Expected behavior

metrics not supported should not be offered.

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/44

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
