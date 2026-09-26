# [Issue #2325] [Issue]: After the rollback of `PciInfo` the `nvmlDeviceGetPciInfo_v3` is used with `v2` struct causing stack buffer overflow.

source: https://github.com/NVIDIA/nccl/issues/2325
state: closed | updated: 2026-09-16T22:04:27Z
labels: 

## 正文

### How is this issue impacting you?

Data corruption

### Share Your Debug Logs

_No response_

### Steps to Reproduce the Issue

1. To reproduce use any code that calls the `ncclNvmlDeviceGetPciInfo`.
2. Run the binary with the address sanitizer. 

### NCCL Version

2.30.7-1

### Your platform details

_No response_

### Error Message & Behavior

```
SanitizerError
AddressSanitizer: stack-buffer-overflow (/usr/lib/libcuda/libnvidia-ml.so.1+0x3b306) 
```

```
==1292==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7b0fac6a3454 at pc 0x558b5a4009a8 bp 0x7b0fad884930 sp 0x7b0fad8840e0
WRITE of size 17 at 0x7b0fac6a3454 thread T33 (tf_CreateNcclCo)
    #0 0x558b5a4009a7 in vsnprintf llvm/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_common_interceptors.inc:1799:1
    #1 0x558b5a402096 in snprintf llvm/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_common_interceptors.inc:1872:1
    #2 0x7b0fde03b306  (/usr/lib/libcuda/libnvidia-ml.so.1+0x3b306)
    #3 0x7b0fde045547 in nvmlDeviceGetPciInfo_v3 (/usr/lib/libcuda/libnvidia-ml.so.1+0x45547)
    #4 0x558b6aaa58b0 in ncclNvmlDeviceGetPciInfo(nvmlDevice_st*, nvmlPciInfo_st*) nccl/src/misc/nvmlwrap.cc:332
    #5 0x558b6aa6068f in ncclTopoSetAttrFromNvml(ncclXmlNode*, nvmlDevice_st*, char const*) nccl/src/graph/xml.cc:451
    #6 0x558b6aa61c34 in ncclTopoGetXmlFromSys(ncclXmlNode*, ncclXml*) nccl/src/graph/xml.cc:639
    #7 0x558b6aa65854 in ncclTopoFillGpu(ncclXml*, char const*, ncclXmlNode**) nccl/src/graph/xml.cc:1065
    #8 0x558b6aa528dc in ncclTopoGetSystem(ncclComm*, ncclTopoSystem**, char const*) nccl/src/graph/topo.cc:1813
    #9 0x558b6aa83fea in initTransportsRank(ncclComm*, ncclComm*, unsigned long*) nccl/src/init.cc:1141
    #10 0x558b6aa7a1e9 in ncclCommInitRankFunc(ncclAsyncJob*) nccl/src/init.cc:1921
    #11 0x558b6aa67e1c in ncclAsyncJobMain(void*) nccl/src/group.cc:77
    #12 0x558b6aa6e531 in asyncJobLaunch(ncclIntruQueue<ncclAsyncJob, &ncclAsyncJob::next>*, bool volatile*) nccl/src/group.cc:479
    #13 0x558b6aa6b19f in groupLaunch(ncclAsyncJob*, ncclSimInfo_v22200*) nccl/src/group.cc:630
    #14 0x558b6aa690a7 in ncclGroupEndInternal(ncclSimInfo_v22200*) nccl/src/group.cc:866
    #15 0x558b6aa727ca in ncclCommInitRankConfig nccl/src/init.cc:2679
```

## 评论 (4)

### xiaofanl-nvidia · 2026-08-09

++ @thomasgillis @nv-udeodhar please take a look at this. 

### tilo-nvda · 2026-09-15

Thanks @thearusable for the report, this is a known issue and has been fixed as part of this commit [https://github.com/NVIDIA/nccl/commit/f3e5e99f6ab624c5d0a38358dfebd3005544e594](url) .  The overflow you shared happens because NCCL's `nvmlPciInfo_t` had a stale busId buffer while the driver's NVML ABI actually writes a larger busId (32 bytes) at that offset. Could you retest with 2.31+ to confirm if the issue still appears?

### thearusable · 2026-09-15

Thanks @tilo-nvda, I just checked with 2.31.2-1, and it works without any issues.

### xiaofanl-nvidia · 2026-09-16

Thanks for trying. Closing. 
