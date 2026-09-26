# [Issue #1649] [Issue]: incorrect location of rocm_version.h

source: https://github.com/ROCm/rccl/issues/1649
state: closed | updated: 2025-05-22T20:53:41Z
labels: Under Investigation

## 正文

### Problem Description

On Fedora and OpenSUSE, the location of rocm_version.h is independent  of the version of rocm and is found 

 > dnf provides */rocm_version.h

rocm-core-devel-6.3.3-1.fc43.x86_64 : Libraries and headers for rocm-core
Repo         : rawhide
Matched From : 
Filename     : /usr/include/rocm_version.h

In the RCCL cmake infra there is logic hard coded to the version assuming the path here

https://github.com/ROCm/rccl/blob/develop/src/include/hip_rocm_version_info.h#L40

where as the path is really found here

https://github.com/ROCm/rccl/blob/develop/src/include/hip_rocm_version_info.h#L47

Locating files should use a generic mechanism like find_file()


### Operating System

Fedora, OpenSUSE

### CPU

ALL

### GPU

ALL

### ROCm Version

ROCm 6.4.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (2)

### ppanchad-amd · 2025-04-21

Hi @trixirt. Internal ticket has been created to fix this issue. Thanks!

### ppanchad-amd · 2025-05-12

Hi @trixirt. 

Per our support matrix https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html Open SUSE and Fedora is not in our OS support list.

Users are welcome to modify our code to get it to compile for their desired OS. 
