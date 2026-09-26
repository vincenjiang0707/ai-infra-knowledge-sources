# [Issue #1749] [Issue]: tests needs to #include <iomanip>

source: https://github.com/ROCm/rccl/issues/1749
state: closed | updated: 2025-10-31T15:11:07Z
labels: 

## 正文

### Problem Description

configure with
  -DBUILD_TESTS=ON

Produces an error like

.../rccl-6.4.1-build/rccl-rocm-6.4.1/test/common/TestBed.cpp:607:16: error: no member named\
 'setfill' in namespace 'std'
  607 |     ss << std::setfill(' ') << std::setw(20) << ncclFuncNames[funcType] << " ";
      |           ~~~~~^


### Operating System

Fedora Rawhide

### CPU

ALL

### GPU

ALL

### ROCm Version

6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (5)

### nileshnegi · 2025-06-17

We already have this: https://github.com/ROCm/rccl/blob/develop/test/common/TestBed.hpp#L13
Which RCCL branch are you using?

### nileshnegi · 2025-06-17

Okay, this commit is not a part of the RCCL ROCm 6.4.x branch, as it landed in develop branch, after cutoff.
Can you please use the develop branch?

### trixirt · 2025-06-17

ROCm packaged in linux distros will be using the released tarballs.
Would it be possible to backport this change to the 6.4 branch in time for 6.4.2 ?


### nileshnegi · 2025-06-17

Unfortunately, we will not be able to get this fix in ROCm 6.4.2. It will be a part of RCCL in the next major ROCm release.

For now, there are 3 options:
* Use the RCCL develop branch
* Manually edit the `TestBed.hpp` file to include [this statement](https://github.com/ROCm/rccl/blob/develop/test/common/TestBed.hpp#L13)
* Rollback your `gtest` to 1.12

### nileshnegi · 2025-10-31

Closing ticket due to no activity.
