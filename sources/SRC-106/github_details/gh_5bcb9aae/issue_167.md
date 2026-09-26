# [Issue #167] [Issue]: error: redefinition of 'struct drm_color_ctm_3x4'

source: https://github.com/ROCm/amdsmi/issues/167
state: closed | updated: 2026-02-26T22:32:52Z
labels: 

## 正文

### Problem Description

This is a build error on Tumbleweed

34.02 cd /amdsmi/build/src && /usr/bin/c++ -DENABLE_ESMI_LIB=1 -Damd_smi_EXPORTS -I/amdsmi/include -I/amdsmi/build/include -I/amdsmi/third_party/shared_mutex -I/amdsmi/include/amd_smi -I/amdsmi/esmi_ib_library/include -I/amdsmi/src -I/amdsmi/rocm_smi/include -I/amdsmi/common/shared_mutex -I/amdsmi/include/ras-decode -I/usr/include/libdrm -I/amdsmi/src/include -Wtrampolines -Wall -Wextra -fno-rtti -m64 -msse -msse2 -Wconversion -Wcast-align -Wformat=2 -fno-common -Wstrict-overflow -Woverloaded-virtual -Wreorder -Wno-write-strings -std=c++17 -fPIC -MD -MT src/CMakeFiles/amd_smi.dir/amd_smi/amd_smi.cc.o -MF CMakeFiles/amd_smi.dir/amd_smi/amd_smi.cc.o.d -o CMakeFiles/amd_smi.dir/amd_smi/amd_smi.cc.o -c /amdsmi/src/amd_smi/amd_smi.cc
34.40 In file included from /amdsmi/include/amd_smi/impl/amd_smi_drm.h:35,
34.40                  from /amdsmi/include/amd_smi/impl/amd_smi_system.h:31,
34.40                  from /amdsmi/src/amd_smi/amd_smi.cc:53:
34.40 /amdsmi/include/amd_smi/impl/amdgpu_drm.h:1629:8: error: redefinition of 'struct drm_color_ctm_3x4'
34.40  1629 | struct drm_color_ctm_3x4 {
34.40       |        ^~~~~~~~~~~~~~~~~
34.40 In file included from /usr/include/libdrm/drm.h:1082,
34.40                  from /amdsmi/rocm_smi/include/rocm_smi/kfd_ioctl.h:26,
34.40                  from /amdsmi/rocm_smi/include/rocm_smi/rocm_smi.h:37,
34.40                  from /amdsmi/include/amd_smi/impl/amd_smi_common.h:27,
34.40                  from /amdsmi/src/amd_smi/amd_smi.cc:51:
34.40 /usr/include/libdrm/drm_mode.h:850:8: note: previous definition of 'struct drm_color_ctm_3x4'
34.40   850 | struct drm_color_ctm_3x4 {
34.40       |        ^~~~~~~~~~~~~~~~~


### Operating System

OpenSUSE Tumbleweed

### CPU

ALL

### GPU

ALL

### ROCm Version

7.1

### ROCm Component

amdsmi

### Steps to Reproduce

build this container
https://github.com/trixirt/rocm-distro-containers/blob/main/opensuse/tumbleweed/amdsmi/upstream/Dockerfile

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### tpkessler · 2026-01-05

Hi all! I'm a package maintainer for Arch Linux and came across the same issue. The PR https://github.com/ROCm/amdsmi/pull/165 fixes the issue.

### superm1 · 2026-02-23

https://github.com/ROCm/rocm-systems/pull/2377 is what I have been trying to land to fix it.

### marifamd · 2026-02-26

Fixed in [#3517](https://github.com/ROCm/rocm-systems/pull/3517)
