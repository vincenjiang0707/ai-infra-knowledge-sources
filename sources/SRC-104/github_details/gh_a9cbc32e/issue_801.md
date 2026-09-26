# [Issue #801] [Bug]: Empty rocprof results

source: https://github.com/ROCm/rocprofiler-compute/issues/801
state: closed | updated: 2025-07-25T08:31:19Z
labels: bug, triage

## 正文

### Describe the bug

When I use omniperf to generate rooflines, it launches rocprof. the resulting MI200/pmc_perf_*.csv files contains empty values in the columns.

If I launch the rocprof command that omniperf launched my self, for instance:
`rocprof -i ./workloads/roof0/MI200/perfmon/pmc_perf_0.txt --timestamp on -o ./workloads/roof0/MI200/pmc_perf_0.csv "./tests/demo_dummy_integration"`

I get results.

### Linux Distribution

rhel 8.10

### ROCm Compute Profiler Version

6.2.1 - 6.4.0

### GPU

mi250x

### ROCm Version

6.2.1 - 6.4.0

### Cluster name (if applicable)

Frontier

### Reproducer

-

### Expected behavior

_No response_

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (6)

### etiennemlb · 2025-07-09

The code definitely works on GPU, I can see it using rocm smi, could it be that there is a conflict with the libraries ?

```
libtree -p tests/demo_dummy_integration
tests/demo_dummy_integration
├── /opt/rocm-6.2.1/lib/libamdhip64.so.6 [LD_LIBRARY_PATH]
│   ├── /opt/rocm-6.2.1/lib/librocprofiler-register.so.0 [LD_LIBRARY_PATH]
│   │   └── /lib64/libpthread.so.0 [default path]
│   ├── /opt/rocm-6.2.1/lib/libamd_comgr.so.2 [LD_LIBRARY_PATH]
│   │   ├── /lib64/libpthread.so.0 [default path]
│   │   ├── /lib64/libzstd.so.1 [default path]
│   │   ├── /lib64/libz.so.1 [default path]
│   │   ├── /lib64/libtinfo.so.6 [default path]
│   │   └── /lib64/librt.so.1 [default path]
│   │       └── /lib64/libpthread.so.0 [default path]
│   ├── /opt/rocm-6.2.1/lib/libhsa-runtime64.so.1 [LD_LIBRARY_PATH]
│   │   ├── /opt/rocm-6.2.1/lib/librocprofiler-register.so.0 [LD_LIBRARY_PATH]
│   │   ├── /opt/amdgpu/lib64/libdrm_amdgpu.so.1 [ld.so.conf]
│   │   │   ├── /opt/amdgpu/lib64/libdrm.so.2 [ld.so.conf]
│   │   │   └── /lib64/libpthread.so.0 [default path]
│   │   ├── /opt/amdgpu/lib64/libdrm.so.2 [ld.so.conf]
│   │   ├── /lib64/libelf.so.1 [default path]
│   │   │   ├── /lib64/libz.so.1 [default path]
│   │   │   ├── /lib64/libbz2.so.1 [default path]
│   │   │   ├── /lib64/liblzma.so.5 [default path]
│   │   │   │   └── /lib64/libpthread.so.0 [default path]
│   │   │   └── /lib64/libzstd.so.1 [default path]
│   │   ├── /lib64/librt.so.1 [default path]
│   │   ├── /lib64/libpthread.so.0 [default path]
│   │   └── /lib64/libnuma.so.1 [default path]
│   ├── /lib64/libpthread.so.0 [default path]
│   ├── /lib64/librt.so.1 [default path]
│   └── /lib64/libnuma.so.1 [default path]
├── /lib64/libpthread.so.0 [default path]
└── /lib64/libomp.so [default path]
    ├── /lib64/libpthread.so.0 [default path]
    └── /lib64/librt.so.1 [default path]
```

### etiennemlb · 2025-07-10

Using rocprofv3 and rocm 6.4.0 fixies the issue. 

Any idea as to why rocprof would not work ?

### harkgill-amd · 2025-07-11

Hi @etiennemlb, there have been major changes since ROCm 6.2.1, many of which could have resolved the issue that you're seeing. Omniperf with ROCm 6.2.1 also supports rocprofv2. Could you please give that a try to see if it works on your end with
```
ROCPROF=rocprofv2 omniperf ...

### etiennemlb · 2025-07-12

I tried using rocprof v3 and it works fine. but it seemed to me that using rocprof (v1) worked previously. I observe that on mi300a rocprof v1 works but not on mi250x. there must be something wrong with my environment, I was wondering if you could guide me as to what could produce this issue.

To remind you, using rocprof v1, the counter values are always zero, but the other csv rows are populated as expected. using rocprof 3, all columns are populated.

On 11 July 2025 16:00:02 UTC, harkgill-amd ***@***.***> wrote:
>harkgill-amd left a comment (ROCm/rocprofiler-compute#801)
>
>Hi @etiennemlb, there have been major changes since ROCm 6.2.1, many of which could have resolved the issue that you're seeing. Omniperf with ROCm 6.2.1 also supports rocprofv2. Could you please give that a try to see if it works on your end with
>```
>ROCPROF=rocprofv2 omniperf ...
>


### tcgu-amd · 2025-07-24

Hi @etiennemlb, thanks for reaching out! Can you run with rocprofv1 with the `export AQLPROFILE_READ_API=0` env var and see if this resolves the issue? If that still doesn't work, please provide a reproducer workload so we can further investigate. Thanks! 

### etiennemlb · 2025-07-25

I run on a cluster, a node must have gone wrong, I can't figure out why, but I'm not able to reproduce my issue.
i'll close and if I encounter this issue again, I'll reopen.
