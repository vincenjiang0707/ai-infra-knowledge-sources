# [Issue #2289] [Issue]: nccl4py whls don't pin to a specific nccl version

source: https://github.com/NVIDIA/nccl/issues/2289
state: closed | updated: 2026-07-19T04:49:01Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

_No response_

### Steps to Reproduce the Issue

```
wget https://files.pythonhosted.org/packages/1d/43/1dbdadddb88e53c08875c7ede540f95ebb96d81bc8661281179a2d033d28/nccl4py-0.3.1-cp314-cp314t-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl
unzip nccl4py-0.3.1-cp314-cp314t-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl
rg nvidia-nccl-cu12 nccl4py-0.3.1.dist-info/METADATA
```

### NCCL Version

nccl4py==0.3.1

### Your platform details

_No response_

### Error Message & Behavior

nccl4py doesn't specify the nccl version in it's requirements so it's possible to have a different nccl version installed from what nccl4py was compiled/linked against.

In torch we specify the exact version but nccl4py doesn't which could cause issues since you may get a mismatched version installed.

```
tristanr@tristanr-fedora-PF5PDEHW ~/D/torch-2.14.0.dev20260714+cu130.dist-info> rg -i nccl
METADATA
129:Requires-Dist: nvidia-nccl-cu13==2.30.7; platform_system == "Linux"
```

vs

```
tristanr@tristanr-fedora-PF5PDEHW ~/D/nccl4py-0.3.1.dist-info> rg nvidia-nccl-cu13
METADATA
43:Requires-Dist: nvidia-nccl-cu13; extra == "cu13"
```

## 评论 (5)

### kwen2501 · 2026-07-15

Thanks for the report. The lack of an exact version pin is intentional — here's the rationale.

**Why there's no exact pin**

Unlike PyTorch, which bundles NCCL and pins to the exact version it ships, nccl4py is designed to work with a range of runtime NCCL versions. The bindings load all symbols lazily via `dlopen`/`dlsym` at first use rather than linking against `libnccl.so` at compile time. This means:

- A newer runtime NCCL (forward-compatible in API) works fine with an older nccl4py wheel.
- If a symbol is missing in the runtime library (e.g. because it's older than the build), nccl4py raises a clean `FunctionNotFoundError("function ncclFoo is not found")` rather than crashing with a segfault.

An exact pin would unnecessarily break users who upgrade NCCL independently of nccl4py.

### kwen2501 · 2026-07-15

That said, please let us know if there is anything we can improve, for example:
- better error messaging?
- adding a lower bound? 

It would be helpful if you could share how the lack of pinning impacts your workload. 
Thanks!
cc @xiakun-lu @xiaofanl-nvidia 

### fegin · 2026-07-15

In my case, I just installed `nccl4py` using `pip` and when running a test case, `nccl4py` complained that some symbol is not compatible. Unfortunately, I didn't preserve the error message, so I cannot confirm if it is `FunctionNotFoundError`. My fix was to pull the latest PyTorch and rebuild, my PyTorch was 2-3 weeks old. It may be rare, but if PyTorch's NCCL version was not compatible with `nccl4py`, which PyTorch's version is too old, then one needs to try either `USE_SYSTEM_NCCL=1` or force PyTorch to update the version or use old `nccl4py` release. @d4l3k, @kwen2501  is `USE_SYSTEM_NCCL=1` the recommended solution in such a case or raising a issue to PyTorch to update the version?

### xiakun-lu · 2026-07-15

To add to what @kwen2501  replied, nccl host API (the API in nccl.h) is forward and backward compatible, meaning nccl4py can work with older or newer libnccl.so. of course, for the symbols not existing in libnccl.so, nccl4py raises exception `FunctionNotFoundError`. 

In your case, you don't have to change the PyTorch behavior, you can change the libnccl.so used by nccl4py by setting `LD_PRELOAD`. nccl4py uses `cuda.pathfinder` to loaded libnccl.so, you can find the search order at https://nvidia.github.io/cuda-python/cuda-pathfinder/latest/generated/cuda.pathfinder.load_nvidia_dynamic_lib.html

### xiaofanl-nvidia · 2026-07-19

Closing this since this has been answered. Please reopen or open a new issue if I'm wrong. Thanks! 
