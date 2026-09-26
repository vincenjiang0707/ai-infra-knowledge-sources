# [Issue #1377] [Issue]: Degraded IB performance

source: https://github.com/ROCm/rccl/issues/1377
state: closed | updated: 2024-11-13T18:16:07Z
labels: 

## 正文

### Problem Description

I'm running `all_reduce_perf` on two IB-enabled nodes, and seeing much lower-than-expected bandwidth over IB between these two nodes.

The two nodes have kernel `6.5.0-1025-azure`. On further debugging, the issue seems to stem from lack of GDRDMA enablement.
I'm using latest rccl `develop` (a680e329e62ac1fba9e7512e3da66623ceeee8ba) which already has commit (105ff1611fc0638266af65e7ff1ae32b7f77b853, PR #1328) and is supposed to enabled GDR on HWE 6.5 kernel.

When looking at `ncclIbGdrSupport()` in `src/transport/net_ib.cc`, I see:

```c
    if (strncmp("Hyper-V UEFI Release", strValue, 20) == 0) {
      int roMode = ncclParamIbPciRelaxedOrdering();
      NCCLCHECK(ncclTopoGetStrFromSys("/proc/sys/kernel", "numa_balancing", strValue));
      if (strcmp(strValue, "1") == 0 && roMode == 0)
        moduleLoaded = 0;
    } else if (moduleLoaded == 0) {
      // Check for `ib_register_peer_memory_client` symbol in `/proc/kallsyms`
      // if your system uses native OS ib_peer module
      char buf[256];
      FILE *fp = NULL;
```

It seems like, in my case, the else-if block is never exercised because I'm on Hyper-V UEFI release v4.1.

This seems like a bug because on this kernel `ib_register_peer_memory_client` seems to be available:
```
$ cat /proc/kallsyms  | grep ib_register_peer_memory_client
0000000000000000 b pfn_ib_register_peer_memory_client   [amdgpu]
0000000000000000 r __kstrtab_ib_register_peer_memory_client     [ib_uverbs]
0000000000000000 r __kstrtabns_ib_register_peer_memory_client   [ib_uverbs]
0000000000000000 r __ksymtab_ib_register_peer_memory_client     [ib_uverbs]
0000000000000000 r __crc_ib_register_peer_memory_client [ib_uverbs]
0000000000000000 r __export_symbol_ib_register_peer_memory_client       [ib_uverbs]
0000000000000000 t __pfx_ib_register_peer_memory_client [ib_uverbs]
0000000000000000 T ib_register_peer_memory_client       [ib_uverbs]
```


### Operating System

Ubuntu 22.04.5 LTS

### CPU

Intel(R) Xeon(R) Platinum 8480C

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.2.0

### ROCm Component

rccl

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (2)

### harkgill-amd · 2024-11-13

Hi @adk9, can this be closed now that https://github.com/ROCm/rccl/pull/1378 has been merged?

### adk9 · 2024-11-13

> Hi @adk9, can this be closed now that #1378 has been merged?

Yes, thank you!
