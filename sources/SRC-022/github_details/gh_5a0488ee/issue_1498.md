# [Issue #1498] [Issue]: duplicate symbol Definition

source: https://github.com/ROCm/rccl/issues/1498
state: closed | updated: 2025-02-04T12:08:44Z
labels: 

## 正文

### Problem Description

I am using the image: `rocm/dev-ubuntu-20.04:6.3.1-complete`. When executing `./install.sh -t --prefix=${RCCL_INSTALL_PREFIX}`, an error occurs.
Code is at the tag : `rocm-6.3.1`
```shell
ld.lld: error: duplicate symbol: ncclCommRegister
>>> defined at api_trace.cc
>>>            /tmp/api_trace-8e48f3.o:(ncclCommRegister)
>>> defined at nccl.cu
>>>            nccl.cu.o:(.text+0x6D80) in archive libmscclpp_nccl.a

ld.lld: error: duplicate symbol: ncclCommDeregister
>>> defined at api_trace.cc
>>>            /tmp/api_trace-8e48f3.o:(ncclCommDeregister)
>>> defined at nccl.cu
>>>            nccl.cu.o:(.text+0x6D90) in archive libmscclpp_nccl.a

ld.lld: error: duplicate symbol: ncclMemAlloc
>>> defined at api_trace.cc
>>>            /tmp/api_trace-8e48f3.o:(ncclMemAlloc)
>>> defined at nccl.cu
>>>            nccl.cu.o:(.text+0x6DA0) in archive libmscclpp_nccl.a

ld.lld: error: duplicate symbol: ncclMemFree
>>> defined at api_trace.cc
>>>            /tmp/api_trace-8e48f3.o:(ncclMemFree)
>>> defined at nccl.cu
>>>            nccl.cu.o:(.text+0x7390) in archive libmscclpp_nccl.a
```

### Operating System

Ubuntu 20.04

### CPU

Intel(R) Xeon(R) Platinum 8352Y CPU @ 2.20GHz

### GPU

MI210

### ROCm Version

ROCm 6.3.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### nileshnegi · 2025-01-22

This can be related to some recent commits in RCCL. Are you using the latest RCCL develop commit? Did you clone a fresh copy with this commit or use `git pull`?

If you used `git pull`, I would suggest `git submodule update --init --recursive`.

Also, you can try adding `-l --disable-mscclpp` to your install.sh command to build only for local GPU target and disable MSCCLPP as it is not supported on MI210.

### Qizhi697 · 2025-01-22

@nileshnegi 

- I am not using the latest commit from the `develop` branch, but rather the `tag`: `rocm-6.3.1`.
- After adding `-l` and eliminating the impact of MSCCLPP, the errors are gone. Thank you very much!
- You mentioned that `MSCCLPP` is not supported on `MI210`. Could you please let me know which `AMD GPUs` are currently supported by `MSCCLPP`? Is there a maintained list of GPUs supported by `MSCCLPP`?

### nileshnegi · 2025-01-28

Currently, we support MSCCLPP only on MI300 `gfx942` -- https://github.com/ROCm/rccl/blob/develop/CMakeLists.txt#L308
