# [Issue #21] [Issue]: CMake targets are not fully guarded against multiple inclusion

source: https://github.com/ROCm/rocprofiler-sdk/issues/21
state: closed | updated: 2025-01-15T18:55:24Z
labels: 

## 正文

### Problem Description

Only a subset of the CMake targets in rocprofiler-sdk and rocprofiler-sdk-roctx are guarded against multiple inclusions. The other ROCm packages do not have this issue.

Here is a simple reproducer (CMakeLists.txt):
```
project(foo)
set(CMAKE_MODULE_PATH ${ROCM_PATH}/lib/cmake/hip ${CMAKE_MODULE_PATH})
cmake_minimum_required(VERSION 3.26)
find_package(hiprtc)
find_package(hiprtc)
find_package(rocprofiler-sdk)
find_package(rocprofiler-sdk)
```

You will see that having *two* `find_package(hiprtc)` is OK, but having *two* `find_package(rocprofiler_sdk)` gives you this error:
```

CMake Error at /opt/rocm/lib/cmake/rocprofiler-sdk/rocprofiler-sdk-config.cmake:61 (add_library):
  add_library cannot create imported target
  "rocprofiler-sdk::rocprofiler-sdk" because another target with the same
  name already exists.
Call Stack (most recent call first):
  CMakeLists.txt:7 (find_package)


CMake Error at /opt/rocm/lib/cmake/rocprofiler-sdk/rocprofiler-sdk-config.cmake:124 (add_library):
  add_library cannot create imported target
  "rocprofiler-sdk::rocprofiler-sdk-external-nolink" because another target
  with the same name already exists.
Call Stack (most recent call first):
  CMakeLists.txt:7 (find_package)


CMake Error at /opt/rocm/lib/cmake/rocprofiler-sdk/rocprofiler-sdk-config.cmake:158 (add_executable):
  add_executable cannot create imported target "rocprofiler-sdk::rocprofv3"
  because another target with the same name already exists.
Call Stack (most recent call first):
  CMakeLists.txt:7 (find_package)
```

I believe the problem are these lines in rocprofiler-sdk-targets.cmake:
```
# Protect against multiple inclusion, which would fail when already imported targets are added once more.                                                                                                    
set(_cmake_targets_defined "")
set(_cmake_targets_not_defined "")
set(_cmake_expected_targets "")
foreach(_cmake_expected_target IN ITEMS rocprofiler-sdk::rocprofiler-headers rocprofiler-sdk::rocprofiler-shared-library)
  list(APPEND _cmake_expected_targets "${_cmake_expected_target}")
  if(TARGET "${_cmake_expected_target}")
    list(APPEND _cmake_targets_defined "${_cmake_expected_target}")
  else()
    list(APPEND _cmake_targets_not_defined "${_cmake_expected_target}")
  endif()
endforeach()
```

There are similar issues with the CMake module for rocprofiler-sdk-roctx. You can reproduce the issue by doing `find_package(find_package(rocprofiler-sdk-roctx)` twice in CMakeLists.txt

### Operating System

Ubuntu 22.04.4 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 7713 64-Core Processor

### GPU

AMD Instinct MI250

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### jrmadsen · 2024-09-28

Thanks for the ticket. This is easily fixed by adding an `include_guard(DIRECTORY)` to the top of the *-config.cmake files. I’ll get that taken care of. 

### naromero77amd · 2024-09-30

> Thanks for the ticket. This is easily fixed by adding an `include_guard(DIRECTORY)` to the top of the *-config.cmake files. I’ll get that taken care of.

Will the fixed CMake module make it into ROCm 6.2.3 (if there is such a thing) or will it go into ROCm 6.3? Do you want make to create an internal Jira for this?

### jrmadsen · 2025-01-15

This was resolved in https://github.com/ROCm/rocprofiler-sdk/commit/a92fa8f0712cca9db148eca048ae2cb0db4bdad9
