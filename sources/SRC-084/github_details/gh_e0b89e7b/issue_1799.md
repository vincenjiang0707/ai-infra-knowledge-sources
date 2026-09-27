# [Issue #1799] Bug Report: ROCm 8.0 binary not found (latest ROCm is 7.1)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1799
state: closed | updated: 2026-03-06T01:11:22Z
labels: Waiting for Info, ROCm

## 正文

### System Info

* OS: ubuntu 25.10
* Python version: 3.13.7
* ROCm version: 7.1
* GPU: 780M aka gfx1103

### Reproduction

**Describe the bug**
When trying to import `bitsandbytes` on a ROCm system, it fails to load due to a missing binary:

```
bitsandbytes library load error: Configured ROCm binary not found at /home/jerry/Desktop/bitsandbytes/bitsandbytes/libbitsandbytes_rocm80.so
Traceback (most recent call last):
  File "/home/jerry/Desktop/bitsandbytes/bitsandbytes/cextension.py", line 313, in <module>
    lib = get_native_library()
  File "/home/jerry/Desktop/bitsandbytes/bitsandbytes/cextension.py", line 282, in get_native_library
    raise RuntimeError(f"Configured {BNB_BACKEND} binary not found at {cuda_binary_path}")
RuntimeError: Configured ROCm binary not found at /home/jerry/Desktop/bitsandbytes/bitsandbytes/libbitsandbytes_rocm80.so
```

It was built with the following commands:
```
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git
HIPCXX="$(rocm-sdk path --root)/llvm/bin/clang" HIP_PATH="$(rocm-sdk path --root)" HIP_PLATFORM=amd CMAKE_PREFIX_PATH="$(rocm-sdk path --root):$CMAKE_PREFIX_PATH" cmake -DCOMPUTE_BACKEND=hip -S . -DCMAKE_HIP_FLAGS:STRING="-I$(rocm-sdk path --root)/include" -DBNB_ROCM_ARCH=gfx1103
make
pip install .
```



### Expected behavior

**Expected behavior**
`bitsandbytes` should either:
* Detect the available ROCm version (e.g., 7.1) and load the proper binary, or
* Fall back gracefully with a clear message if no compatible ROCm build exists.


## 评论 (8)

### mikealanni · 2025-11-08

Same issue in Comfyui

### matthewdouglas · 2025-11-10

Hi, 
Can you share more about what version of PyTorch you have? The information from `python -m torch.utils.collect_env` would be useful in troubleshooting this.

If you have a torch+rocm71 build, and then built bitsandbytes from source with the ROCm 7.1 toolkit, I would have expected it to try to load `libbitsandbytes_rocm71.so`. 

It's possible maybe "7.1.0" got misinterpreted as "7.10", which could result in behavior like this.

### matthewdouglas · 2025-11-10

Quick follow-up. I do see there may be an upcoming ROCm 7.10 preview release. I assume that this is what you're using. Note that 7.10 != 7.1 for versioning purposes, and that 7.10 > 7.1.

PyTorch versions built with that can certainly cause an issue as we've only designed to handle minor CUDA/ROCm version numbers 0-9. My understanding is that 7.9+ is also just a preview release, so it's not going to be a high priority to address at the moment.

You could get by for now with renaming your built `libbitsandbytes_rocm710.so` to `libbitsandbytes_rocm80.so`. Alternatively, I would recommend using a ROCm toolkit and PyTorch build with ROCm <= 7.9.

### sstamenk · 2025-11-14

@matthewdouglas I ran into a similar issue when testing with some internal builds. From what I understand the issue seems to be due to the fact CMake generates a shared library file name using the version number obtained by calling `hipconfig --version` while the import logic uses `torch.version.hip` version number which is populated by PyTorch using versions from `/opt/rocm/include/hip/rocm_version.h`. Apparently these 2 version numbers can be different in certain cases.

For now, as you said, renaming the shared library seems to be a valid workaround.

@Jerry-zirui can you post the contents of the `/home/jerry/Desktop/bitsandbytes/bitsandbytes/` directory to see how your .so file is named and then run `hipconfig --version` to confirm the naming matches the version provided. Also run `python -c "import torch; print(torch.version.hip)"` to see if there is a mismatch between those 2 version numbers, thanks.

### harkgill-amd · 2025-11-19

This issue boils down to `torch.version.hip` using the values from `/include/rocm-core/rocm_version.h`. This likely worked in the past but with HIP and ROCm versioning diverging going forward, this causes failures as bitsandbytes produces a shared library with versioning pulled from `hipconfig --version` (HIP versioning) but checks for the existence of that library with `torch.version.hip` (ROCm versioning), as @sstamenk mentioned.

https://github.com/pytorch/pytorch/pull/168097 will resolve alot of the confusion here as `torch.version.hip` will be reserved for the specific HIP version and a new variable will be introduced - `torch.version.rocm` which is used to retrieve the specific ROCm version. From the bitsandbytes end, it'd make most sense to adhere to the ROCm versioning instead here https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/CMakeLists.txt#L217-L221. This'll fix the issue for now, but the torch.version.hip checks will need to be converted to torch.version.rocm whenever the aforementioned PR is merged.

### sstamenk · 2025-11-19

I tested adding the logic that PyTorch uses for detecting the ROCm version for the torch.version.hip variable in the case of both Linux and Windows here [LoadHIP.cmake#L90-L139](https://github.com/ROCm/pytorch/blob/release/2.9/cmake/public/LoadHIP.cmake#L90-L139) instead of the one currently used by Bitsandbytes [CMakeLists.txt#L217-L221](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/CMakeLists.txt#L217-L221) (`hipconfig --version`) and it did fix the naming during shared library generation. Im not sure if it is too bloated for Bitsandbytes. Maybe @matthewdouglas can provide some input.


### TimDettmers · 2026-02-21

Closing this issue. The root cause was identified in the discussion: the HIP and ROCm version numbers are diverging, causing a mismatch between the library name generated at build time (via `hipconfig --version`) and what bitsandbytes looks for at runtime (via `torch.version.hip`). This is being addressed upstream in PyTorch (pytorch/pytorch#168097) with the introduction of `torch.version.rocm`.

In the meantime, renaming the built `.so` file to match the expected name is a valid workaround (as @matthewdouglas noted). Once the upstream PyTorch fix lands, bitsandbytes can switch to using `torch.version.rocm` for more reliable version detection. If you're still hitting this after updating PyTorch, please reopen.

### sstamenk · 2026-03-06

This looks like the same issue as in #1890, the fix is quite trivial #1889 
It doesn't look mainly caused by the ROCm and HIP versions diverging but rather by incorrect concatenation in `get_cuda_version_string()` which returned 80 (7 * 10 + 10) for ROCm 7.10 instead of 710.
