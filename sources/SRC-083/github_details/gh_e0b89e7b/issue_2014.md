# [Issue #2014] ROCm 8.4 binary not found (latest ROCm is 7.14)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2014
state: closed | updated: 2026-07-21T15:07:40Z
labels: ROCm

## 正文

### System Info

- OS: RHEL 9.6
- Python version: 3.12.9
- ROCm version: 7.14
- GPU: MI350P

### Reproduction

When trying to import bitsandbytes on a ROCm system, it fails to load due to a missing binary:
```
Installing collected packages: bitsandbytes
Successfully installed bitsandbytes-0.49.2
(app-root) /opt/app-root$ python -c 'import bitsandbytes'
bitsandbytes library load error: Configured ROCm binary not found at /opt/app-root/lib64/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm84.so
Traceback (most recent call last):
  File "/opt/app-root/lib64/python3.12/site-packages/bitsandbytes/cextension.py", line 320, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/bitsandbytes/cextension.py", line 288, in get_native_library
    raise RuntimeError(f"Configured {BNB_BACKEND} binary not found at {cuda_binary_path}")
RuntimeError: Configured ROCm binary not found at /opt/app-root/lib64/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm84.so
```
Build:
Hermatic build with network-isolation.

Similar case but different ROCm version (7.1)
https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1799 

### Expected behavior

bitsandbytes should either:

Detect the available ROCm version (e.g., 7.14) and load the proper binary, or
Fall back gracefully with a clear message if no compatible ROCm build exists.


## 评论 (2)

### aoguntayo · 2026-07-20

Looks like https://github.com/bitsandbytes-foundation/bitsandbytes/pull/1889 fixes the issue

### matthewdouglas · 2026-07-21

This is fixed in combination of #1889, #1980, and #2007. The latter adds ROCm 7.14 builds, while the prior two enable better detection and automatic fallback to load the 7.2 build in the absence of a newer build.

These changes will be released to PyPI in v0.50.0 quite soon. In the meantime, we have [wheels built from main](https://github.com/bitsandbytes-foundation/bitsandbytes/releases/tag/continuous-release_main) that are available.
