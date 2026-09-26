# [Issue #51] [Issue]: Building from source with libdw/elfutils also installed from source

source: https://github.com/ROCm/rocprofiler-sdk/issues/51
state: closed | updated: 2025-06-24T07:14:07Z
labels: Under Investigation

## 正文

### Problem Description

`rocprofiler-sdk` fails to build when `libdw` is installed from source in a non-system path and passed via `libdw_INCLUDE_DIR` and `libdw_LIBRARY` on the CMake command line.

### Operating System

Rocky Linux 8.9

### CPU

AMD EPYC 7702 64-Core Processor

### GPU

AMD Instinct MI210

### ROCm Version

ROCm 6.2.0 + `amd-staging` branch of rocprofiler-sdk

### ROCm Component

_No response_

### Steps to Reproduce

Trying to follow the recipe in `README.md` to build `amd-staging` from source on a system with no systemwide `elfutils`, CMake complains that it can't find `libdw`. It also gripes that it can't find `libdrm` and `libdrm_amdgpu`, despite those being in `/opt/amdgpu/lib64`. So, I install elfutils from source to $HOME/sw.

My nominally-working CMake configure line is thus:

```
cmake  \
    -B rocprofiler-sdk-build \
    -D ROCPROFILER_BUILD_TESTS=ON \
    -D ROCPROFILER_BUILD_SAMPLES=ON \
    -D CMAKE_INSTALL_PREFIX=$HOME/rocprofiler-sdk \
    -Dlibdw_LIBRARY=$HOME/sw/elfutils/lib/libdw.so \
    -Dlibdw_INCLUDE_DIR=$HOME/sw/elfutils/include/ \
    -Ddrm_LIBRARY=/opt/amdgpu/lib64/libdrm.so \
    -Ddrm_amdgpu_LIBRARY=/opt/amdgpu/lib64/libdrm_amdgpu.so \
    rocprofiler-sdk-source/
```
There are plenty of places in the generated `CMakeFiles/` where my elfutils include/lib locations are present, so CMake clearly picked them up for *something*. Nevertheless, a build spews continual errors of the style:
```
In file included from /home/wwilliam/rocprofiler-sdk-source/source/lib/output/pc_sample_transform.hpp:27,
                 from /home/wwilliam/rocprofiler-sdk-source/source/lib/output/metadata.hpp:29,
                 from /home/wwilliam/rocprofiler-sdk-source/source/lib/output/output_config.hpp:26,
                 from /home/wwilliam/rocprofiler-sdk-source/source/lib/output/tmp_file_buffer.hpp:26,
                 from /home/wwilliam/rocprofiler-sdk-source/source/lib/output/generator.hpp:25,
                 from /home/wwilliam/rocprofiler-sdk-source/source/lib/output/generateStats.hpp:25,
                 from /home/wwilliam/rocprofiler-sdk-source/source/lib/output/generateCSV.hpp:25,
                 from /home/wwilliam/rocprofiler-sdk-source/source/lib/output/generateCSV.cpp:23:
/home/wwilliam/rocprofiler-sdk-source/source/include/rocprofiler-sdk/cxx/codeobj/code_printing.hpp:28:10: fatal error: elfutils/libdw.h: No such file or directory
 #include <elfutils/libdw.h>
          ^~~~~~~~~~~~~~~~~~
```
in a tremendous variety of places where `code_printing.hpp` is used. Something appears to be off with the usage of this header and appropriate inclusion of `libdw` as a dependency.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (10)

### ppanchad-amd · 2025-04-02

Hi @wrwilliams. Internal ticket has been created to investigate this issue. Thanks!

### zichguan-amd · 2025-04-21

Hi @wrwilliams, thanks for reporting this. The linking to `libdw` appears missing from several places, I suspect it's the same for `libdrm` and `libdrm_amdgpu`. I'm working on a fix right now and will update when a PR is ready.

### zichguan-amd · 2025-04-22

I'm not able to repro any error with `libdrm` and `libdrm_amdgpu`, specifying `-Ddrm_LIBRARY=/opt/amdgpu/lib64/libdrm.so` and   `-Ddrm_amdgpu_LIBRARY=/opt/amdgpu/lib64/libdrm_amdgpu.so` works as expected. Can you share any error logs related to it?

### zichguan-amd · 2025-04-28

Hi @wrwilliams, fix for `libdw` has landed in staging 3580478426c3da4319bbf793cabf6f3878540bfa. I'll close the issue if you don't have anything to add about `libdrm`.

### wrwilliams · 2025-04-28

I had been expecting that the CMake search for the libdrm libs would check default install locations without prompting—separate issue and may well be WAI from your side.Will check the libdw fix out when I’m back in the office next week.—bwOn Apr 28, 2025, at 5:29 PM, zichguan-amd ***@***.***> wrote:﻿
zichguan-amd left a comment (ROCm/rocprofiler-sdk#51)
Hi @wrwilliams, fix for libdw has landed in staging 3580478. I'll close the issue if you don't have anything to add about libdrm.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you were mentioned.Message ID: ***@***.***>

### jrmadsen · 2025-05-01

@wrwilliams please try the latest amd-staging branch. This should have been fixed in https://github.com/ROCm/rocprofiler-sdk/commit/3580478426c3da4319bbf793cabf6f3878540bfa

### wrwilliams · 2025-05-05

> [@wrwilliams](https://github.com/wrwilliams) please try the latest amd-staging branch. This should have been fixed in [3580478](https://github.com/ROCm/rocprofiler-sdk/commit/3580478426c3da4319bbf793cabf6f3878540bfa)

Tough to tell, as I'm now hitting ABI break static asserts with both [HEAD](https://github.com/ROCm/rocprofiler-sdk/commit/65f60bbb96aac58bf455717fe946d277369cf334) and [3580478](https://github.com/ROCm/rocprofiler-sdk/commit/3580478426c3da4319bbf793cabf6f3878540bfa).

This is building against ROCm 6.3.0-195, installed from RPM on Rocky 8.9.

`make -k` doesn't hit the libdw issue in anything it's able to try to build, but that may not be saying much.

ABI breaks are reported for:
```
hipSetValidDevices
hipMemcpyAtoD
hipMemcpyDtoA
hipMemcpyAtoA
hipMemcpyAtoHAsync
hipMemcpyHtoAAsync
hipMemcpy2DArrayToArray
```

Am I missing an obvious CMake flag here? The correct version of ROCm is detected by CMake, and there doesn't appear to be any extra version lying around the system to confuse matters.

### zichguan-amd · 2025-05-06

There shouldn't be any ABI changes since ROCm 6.3.0, those apis haven't been changed since last year https://github.com/ROCm/hip/blame/amd-staging/include/hip/hip_runtime_api.h. 
I'm able to build on Ubuntu 22.04 ROCm 6.3.0 at both [HEAD](https://github.com/ROCm/rocprofiler-sdk/commit/65f60bbb96aac58bf455717fe946d277369cf334) and [3580478](https://github.com/ROCm/rocprofiler-sdk/commit/3580478426c3da4319bbf793cabf6f3878540bfa).
Can you verify what include files and libraries are being picked up? I've seen cases where there are incorrect hip headers in `/usr/include/` causing problems.

### wrwilliams · 2025-05-08

> There shouldn't be any ABI changes since ROCm 6.3.0, those apis haven't been changed since last year https://github.com/ROCm/hip/blame/amd-staging/include/hip/hip_runtime_api.h.
> I'm able to build on Ubuntu 22.04 ROCm 6.3.0 at both [HEAD](https://github.com/ROCm/rocprofiler-sdk/commit/65f60bbb96aac58bf455717fe946d277369cf334) and [3580478](https://github.com/ROCm/rocprofiler-sdk/commit/3580478426c3da4319bbf793cabf6f3878540bfa).
> Can you verify what include files and libraries are being picked up? I've seen cases where there are incorrect hip headers in /usr/include/ causing problems.


@bwelton suggested we move the ABI static asserts to a separate issue: [https://github.com/ROCm/rocprofiler-sdk/issues/62]. And we agreed on our call 7MAY25 that the asserts firing here makes no sense; there should neither be a real ABI break nor any system weirdness that we are legitimately guarding against. The multiple ROCm installs was my first instinct as well but I checked; there's only the one install on the system and everything is coming out of 6.3.0.

### wrwilliams · 2025-06-24

> [@wrwilliams](https://github.com/wrwilliams) please try the latest amd-staging branch. This should have been fixed in [3580478](https://github.com/ROCm/rocprofiler-sdk/commit/3580478426c3da4319bbf793cabf6f3878540bfa)

Have gotten clean builds from source against 6.4.x, marking this one fixed.
