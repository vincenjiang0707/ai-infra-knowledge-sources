# [Issue #103] No healthy persistent workers available after baseline setup

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/103
state: closed | updated: 2025-10-28T05:24:49Z
labels: 

## 正文

I met the following error when running bench:
```
Failed to run workload 22298d10-a6b5-4f90-9130-11335cb6b6ec: No healthy persistent workers available after baseline setup
Persistent worker cuda:0 failed while running reference for def=gemm_n5120_k2048 wl=7b579664-05e4-4b3d-8a3c-9512309ed30a: [Errno 13] Permission denied: '/home/tianyoug/.cache'
Removing device cuda:0 after 3 failed attempts
Shutting down worker
Failed to run workload 7b579664-05e4-4b3d-8a3c-9512309ed30a: No healthy persistent workers available
Failed to run workload e23cf1f3-9437-4a46-8fce-f4e286db5178: No healthy persistent workers available
```

Do you know how to address this issue?

## 评论 (4)

### zanderjiang · 2025-10-27

Hi there, thank you for raising the issue. 

FlashInfer-Bench writes to your local cache to store temporary benchmarking data, it seems like you don't have permission to write to the local cache directory. 

This issue should resolve once you get permission.

### fortianyou · 2025-10-28

Hi @zanderjiang . I happened have not permission to write to the local cache directory. Is there a way to config the custom cache directory by myself? Or you could guide me how to fix it, I would love to do it.


### zanderjiang · 2025-10-28

Hi @fortianyou, yes, you can specify the directories via setting the FIB_DATASET_PATH and FIB_CACHE_PATH environment variables. 

### fortianyou · 2025-10-28

Thank you @zanderjiang . It's helpful.
