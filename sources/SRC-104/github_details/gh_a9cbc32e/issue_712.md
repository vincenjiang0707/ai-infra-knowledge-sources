# [Issue #712] [Bug]: Inaccurate analysis results using rocprof-compute with rocprofv1/v2 on MI300X (e.g., incorrect peak TFLOPs, HBM bandwidth, active CUs)

source: https://github.com/ROCm/rocprofiler-compute/issues/712
state: closed | updated: 2025-07-25T16:10:07Z
labels: bug, triage, Under Investigation

## 正文

### Describe the bug

Multiple inaccurate or misleading metrics are observed when analyzing results from `rocprofv1` or `rocprofv2` on MI300X:

1. **Peak FP16/BF16 TFLOPs is overestimated by 2x**  
   - Source: [`0200_system-speed-of-light.yaml`](https://github.com/ROCm/rocprofiler-compute/blob/a50e44ec251db408b10822d97194e7dc17d54804/src/rocprof_compute_soc/analysis_configs/gfx942/0200_system-speed-of-light.yaml#L62C13-L62C62)  
   - Formula used: `peak: ((($max_sclk * $cu_per_gpu) * 4096) / 1000)`  
   - **Issue**: MI300X's actual FP16 throughput is 2048 per CU per cycle (not 4096); this leads to inflated peak values and misleading utilization percentages.
   - This issue has been previously reported for **gfx941** as well:
https://github.com/ROCm/rocprofiler-compute/issues/700

2. **HBM and L2 Cache Bandwidth peaks are incorrect**  
   - `L2-Fabric Read BW` and `L2-Fabric Write BW` are marked with peak values like **665.6 GB/s**, which appears to be the per-XCD HBM bandwidth.
   - However, runtime-measured values (e.g., **2021.97 GB/s**) are for the **entire chip** (8 XCDs), resulting in incorrect utilization ratios like **303%**, which is nonsensical.

3. **Active CUs are misreported**  
   - For a large GEMM kernel (e.g., MNK=16384), active CU count is shown as **44**, but MI300X has **304 total CUs**.
   - Even if the tool reports per-XCD CU usage, it should max out at **304/8 = 38**, making the reported value even more confusing.


### Linux Distribution

Ubuntu 22.04.5 LTS

### ROCm Compute Profiler Version

3.1.0

### GPU

AMD MI300X

### ROCm Version

rocm-6.2.2

### Cluster name (if applicable)

a 8X MI300 node

### Reproducer

Run any HIP-compiled kernel or HIP-based library workload using `rocprofv1` or `rocprofv2` as the backend. Examples:

- Profiling a HIP-based library workload (e.g., PyTorch with rocBLAS, using rocprofv1):

    ```bash
    ROCPROF=rocprofv1 rocprof-compute profile -n workload_v1 --device 0 --verbose -- /path/to/python3 your_script.py
    rocprof-compute analyze -p ./workloads/workload_v1/MI300
    rocprof-compute analyze -p ./workloads/workload_v1/MI300 --gui
    ```

- Profiling a custom HIP kernel compiled with `hipcc` (using rocprofv1 or rocprofv2):

    ```bash
    ROCPROF=rocprofv2 rocprof-compute profile -n kernel_v2 --device 0 -- ./your_hip_executable
    rocprof-compute analyze -p ./workloads/kernel_v2/MI300
    rocprof-compute analyze -p ./workloads/kernel_v2/MI300 --gui
    ```

### Expected behavior

Both theoretical peak values and runtime-measured metrics should accurately reflect the architecture of MI300X.

- Peak values (e.g., FP16/BF16 TFLOPs, L2/fabric bandwidth, etc.) should be correctly computed based on MI300X hardware specifications.
- Runtime metrics (e.g., active compute units, achieved bandwidth) should be correctly collected and reported.
- All reported values should clearly indicate whether they are per-XCD or per-chip to avoid confusion, especially on multi-XCD architectures like MI300X.

### Relevant log output

```shell

```

### Screenshots

1. **Active CU Reporting Error**

   In the screenshot from a large GEMM workload (M=N=K=16384), the analyzer reports only **44 active CUs**, 
   while MI300X has **304 total CUs**. This number is inconsistent with expected utilization for such a large workload.
![Image](https://github.com/user-attachments/assets/947ced91-dfaa-4561-84df-4ea3f29e0d26)

2. **Incorrect Peak and Runtime Bandwidth/Compute Metrics**

   Another screenshot highlights multiple modeling and runtime reporting issues:
   - FP16/BF16 peak throughput is shown as **2× the correct value**
   - `L2-Fabric Read BW`, `L2-Fabric Write BW`, and `L2 Cache BW` all show **wrong peak values**
   - Utilization percentages exceed 100% (e.g., 606.48%) due to mismatch between per-XCD peak assumptions and full-chip measured throughput

![Image](https://github.com/user-attachments/assets/865b5890-258a-4f01-94e7-b31ae65d6fb8)

### Additional Context

_No response_

## 评论 (5)

### ppanchad-amd · 2025-05-26

Hi @Hamerlate. Internal ticket has been created to investigate this issue. Thanks!

### feizheng10 · 2025-05-26

Do you have chance to try it with rocprofv3?

### Hamerlate · 2025-05-26

> Do you have chance to try it with rocprofv3?

Yeah, I’ve tried rocprofv3. Still running into some issues though. Here’s the other issue I opened: https://github.com/ROCm/rocprofiler-compute/issues/711

### Hamerlate · 2025-05-27

By the way, the combination of ROCm 6.4.1 and rocprofv3 still exhibits similar issues.

### ppanchad-amd · 2025-07-25

Hi @Hamerlate 

- Speed of light numbers are correct in latest build

- Bandwidth numbers are correct in latest build

- "Active CUs" metric is correct in the sense that the calculation produces the correct value, but is poorly named and will be updated/removed in future releases.

Closing ticket.  Feel free to comment or reopen ticket if you still need assistance. Thanks!
