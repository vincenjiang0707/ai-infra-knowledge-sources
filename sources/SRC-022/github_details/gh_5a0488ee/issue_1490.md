# [Issue #1490] [Issue]: low performance all_gather_perf

source: https://github.com/ROCm/rccl/issues/1490
state: closed | updated: 2025-05-13T06:41:36Z
labels: Under Investigation

## 正文

### Problem Description

I use the aws ofi rccl pluggin ith libfabric 1.23 on a cray SS11.

I run on 4 nodes, each with 4 mi250x. See cpu/gpu details.

I use slurm:
```
srun --nodes=4 --ntasks-per-node=8 --cpus-per-task=8 --threads-per-core=1 --label \
    -- all_gather_perf -b 64K -e 4G -f 2 -g 1
```
There is no cgroup getting in DMA's way.

All gather performance seems low until 16777216.
```
 0: #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
 0: #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
 0:        65536           512     float    none      -1    107.5    0.61    0.59      0    105.6    0.62    0.60      0
 0:       131072          1024     float    none      -1    210.0    0.62    0.60      0    202.6    0.65    0.63      0
 0:       262144          2048     float    none      -1    211.1    1.24    1.20      0    200.9    1.30    1.26      0
 0:       524288          4096     float    none      -1    692.3    0.76    0.73      0    678.9    0.77    0.75      0
 0:      1048576          8192     float    none      -1   1456.6    0.72    0.70      0   1304.0    0.80    0.78      0
 0:      2097152         16384     float    none      -1    70248    0.03    0.03      0    73593    0.03    0.03      0
 0:      4194304         32768     float    none      -1    71951    0.06    0.06      0    59139    0.07    0.07      0
 0:      8388608         65536     float    none      -1    72576    0.12    0.11      0    25554    0.33    0.32      0
 0:     16777216        131072     float    none      -1   1071.2   15.66   15.17      0   1057.5   15.86   15.37      0
 0:     33554432        262144     float    none      -1   1223.2   27.43   26.58      0   1223.3   27.43   26.57      0
 0:     67108864        524288     float    none      -1   1273.4   52.70   51.05      0   1268.6   52.90   51.25      0
 0:    134217728       1048576     float    none      -1   1457.6   92.08   89.20      0   1453.4   92.34   89.46      0
 0:    268435456       2097152     float    none      -1   2864.2   93.72   90.79      0   2853.3   94.08   91.14      0
 0:    536870912       4194304     float    none      -1   5695.6   94.26   91.32      0   5674.5   94.61   91.65      0
 0:   1073741824       8388608     float    none      -1    11366   94.47   91.52      0    11319   94.86   91.90      0
 0:   2147483648      16777216     float    none      -1    22549   95.24   92.26      0    22498   95.45   92.47      0
 0:   4294967296      33554432     float    none      -1    44904   95.65   92.66      0    44867   95.73   92.74      0
 0: # Errors with asterisks indicate errors that have exceeded the maximum threshold.
 0: # Out of bounds values : 0 OK
 0: # Avg bus bandwidth    : 37.9868
```

The low performance up to 8388608 bytes seems unexpected. The same node pool on all_reduce_perf gives:
```
 0: #                                                              out-of-place                       in-place
 0: #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
 0: #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
 0:        65536         16384     float     sum      -1    78.91    0.83    1.61      0    77.42    0.85    1.64      0
 0:       131072         32768     float     sum      -1    101.6    1.29    2.50      0    102.0    1.29    2.49      0
 0:       262144         65536     float     sum      -1    157.8    1.66    3.22      0    161.5    1.62    3.15      0
 0:       524288        131072     float     sum      -1    202.4    2.59    5.02      0    202.2    2.59    5.02      0
 0:      1048576        262144     float     sum      -1    289.5    3.62    7.02      0    289.1    3.63    7.03      0
 0:      2097152        524288     float     sum      -1    265.7    7.89   15.29      0    330.2    6.35   12.31      0
 0:      4194304       1048576     float     sum      -1    366.0   11.46   22.20      0    364.7   11.50   22.28      0
 0:      8388608       2097152     float     sum      -1   1184.5    7.08   13.72      0    912.9    9.19   17.80      0
 0:     16777216       4194304     float     sum      -1    760.7   22.05   42.73      0    820.6   20.45   39.61      0
 0:     33554432       8388608     float     sum      -1   1326.7   25.29   49.00      0   1290.3   26.01   50.39      0
 0:     67108864      16777216     float     sum      -1   2444.7   27.45   53.19      0   2457.6   27.31   52.91      0
 0:    134217728      33554432     float     sum      -1   3486.7   38.49   74.58      0   3876.5   34.62   67.08      0
 0:    268435456      67108864     float     sum      -1   6326.1   42.43   82.21      0   5652.8   47.49   92.01      0
 0:    536870912     134217728     float     sum      -1    11268   47.65   92.32      0    11273   47.62   92.27      0
 0:   1073741824     268435456     float     sum      -1    22500   47.72   92.46      0    22504   47.71   92.45      0
 0:   2147483648     536870912     float     sum      -1    44867   47.86   92.74      0    44876   47.85   92.72      0
 0:   4294967296    1073741824     float     sum      -1    89585   47.94   92.89      0    89596   47.94   92.88      0
 0: # Errors with asterisks indicate errors that have exceeded the maximum threshold.
 0: # Out of bounds values : 0 OK
 0: # Avg bus bandwidth    : 43.7269
```

### Operating System

NAME="Red Hat Enterprise Linux" VERSION="8.10 (Ootpa)"

### CPU

AMD EPYC 7A53 64-Core Processor

### GPU

  Name:                    AMD EPYC 7A53 64-Core Processor   Marketing Name:          AMD EPYC 7A53 64-Core Processor   Name:                    AMD EPYC 7A53 64-Core Processor   Marketing Name:          AMD EPYC 7A53 64-Core Processor   Name:                    AMD EPYC 7A53 64-Core Processor   Marketing Name:          AMD EPYC 7A53 64-Core Processor   Name:                    AMD EPYC 7A53 64-Core Processor   Marketing Name:          AMD EPYC 7A53 64-Core Processor   Name:                    gfx90a   Marketing Name:          AMD Instinct MI250X       Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-   Name:                    gfx90a   Marketing Name:          AMD Instinct MI250X       Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-   Name:                    gfx90a   Marketing Name:          AMD Instinct MI250X       Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-   Name:                    gfx90a   Marketing Name:          AMD Instinct MI250X       Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-   Name:                    gfx90a   Marketing Name:          AMD Instinct MI250X       Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-   Name:                    gfx90a   Marketing Name:          AMD Instinct MI250X       Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-   Name:                    gfx90a   Marketing Name:          AMD Instinct MI250X       Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-   Name:                    gfx90a   Marketing Name:          AMD Instinct MI250X       Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-

### ROCm Version

ROCm 6.2.1

### ROCm Component

rccl

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### ppanchad-amd · 2025-01-17

Hi @etiennemlb. Internal ticket has been created to investigate your issue. Thanks!

### huanrwan-amd · 2025-01-23

Hi @etiennemlb,

Thank you for posting the question. As you noticed, there are differences between the all_gather_perf and all_reduce_perf tests, especially for smaller data amounts. The main reason lies in the nature of these operations:

- Reduction Operation: This allows for the overlap of computation (e.g., “sum” in your log) and communication. As data is received from other processes, it can be immediately computed with local data, and the result can be sent to the next process. This pipelining effect can lead to more efficient use of the communication bus.
- Gather Operation: This involves collecting data from all processes and distributing the combined data to all processes. Each process ends up with a complete set of data from all other processes. This operation primarily involves data movement with minimal computation.

For both operations, it is also noted that the larger the data, the higher the efficiency. This is due to the overhead of initiating transfers being amortized over more data, leading to better utilization of the communication pipeline.

If you have further comments, please let us know.

### huanrwan-amd · 2025-05-13

Another flag can be used: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html#disable-numa-auto-balancing
"If the output is 1, you can disable NUMA auto-balancing by running the following command: sudo sysctl kernel.numa_balancing=0."
