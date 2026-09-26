# [Issue #70] The rocprofv3 launcher loads libraries by .so barename vs soname

source: https://github.com/ROCm/rocprofiler-sdk/issues/70
state: closed | updated: 2025-08-07T18:25:52Z
labels: Under Investigation

## 正文

In our new [ROCm Python Packages](https://github.com/ROCm/TheRock/blob/main/docs/packaging/python_packaging.md), the runtime libraries only contain shared libraries for the SONAME of each library (i.e. `librocprofiler-sdk.so.X` vs `librocprofiler-sdk.so`) because Python wheels do not support symlinks. Most other libraries in ROCm that do dynamic loading do so by SONAME, not barename. It would be great to update the `rocprofv3` launcher to do the same.

Without this, nightly wheels with people trying to use rocprofv3 get this:

```

((rocm-venv) ) rkayaith@SharkMi300X:~$ python -m pip install --find-links https://therock-nightly-python.s3.us-east-2.amazonaws.com/gfx94X-dcgpu/index.html   rocm-sdk[libraries,devel] --pre --upgrade
...
((rocm-venv) ) rkayaith@SharkMi300X:~$ ./rocm-venv/lib/python3.12/site-packages/_rocm_sdk_core/bin/rocprofv3
Fatal error: /home/rkayaith/rocm-venv/lib/python3.12/site-packages/_rocm_sdk_core/lib/rocprofiler-sdk/librocprofiler-sdk-tool.so does not exist
```


## 评论 (4)

### darren-amd · 2025-06-10

Hi @stellaraccident,

I have created a PR here: https://github.com/ROCm/rocprofiler-sdk/pull/71 to fix this issue, thanks for reporting!

### darren-amd · 2025-06-23

Hi @stellaraccident,

We have changed the behavior for loading in [this commit](https://github.com/ROCm/rocprofiler-sdk/commit/aeb1621c2bbcad5d659947c9bf11b86a87974e4e#diff-996e51bbe8dc3793c1de4268e0148c9156e93d196d16c3d8c4d45ca018a6996a), thanks for the report!

### stellaraccident · 2025-06-23

Thank you. @marbre let's pick this up when we can.

### systems-assistant[bot] · 2025-08-07

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/134
