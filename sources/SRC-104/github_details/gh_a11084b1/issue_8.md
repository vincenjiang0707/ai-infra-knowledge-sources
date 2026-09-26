# [Issue #8] [Issue]: rocprofiler-sdk compilation from source

source: https://github.com/ROCm/rocprofiler-sdk/issues/8
state: closed | updated: 2024-12-17T17:03:35Z
labels: Under Investigation

## 正文

### Problem Description

With this issue, I wanted to share an experience with compiling the new `rocprofiler-sdk` from source.

I compiled `rocprofiler-sdk` in the docker image `rocm/dev-ubuntu-22.04:6.1.2`. The build succeeded after resolving the following issues that I encountered:

- The documentation in the `README.md` indicates that `rocprofv3` is "shipped with the ROCm stack". It appears that this may not be the case yet for the current publicly available versions of the ROCm stack. E.g., in the docker image `rocm/dev-ubuntu-22.04:6.1.2`, there does not appear to be a `rocprofv3` executable in `/opt/rocm/bin`.

- I followed the `Build and Installation` instructions from the `README.md` file. In these instructions, the link in the `git clone` command appears to contain an error. I reported this in #7.

- I used the source code from the `amd-mainline` branch. The build exited with an error. The reason seems to be that code in the file `rocprofiler-sdk/source/lib/rocprofiler-sdk/counters/tests/hsa_tables.cpp` seeks to set a member variable `hsa_amd_queue_get_info_fn` from a struct `AmdExtTable`. However, it seems that this variable is not yet a member variable of this struct in the currently latest public version of ROCm, and may only become one in a future release. Protecting this line with the preprocessor conditional `HSA_AMD_EXT_API_TABLE_STEP_VERSION >= 0x02` as in the `amd-staging` branch allowed the build to proceed. I do not know if this fix is sufficient; e.g., there are other occurrences of `hsa_amd_queue_get_info_fn` in the code, but they seemingly did not cause a build issue.

- I initially used the `libhsa-amd-aqlprofile64.so` that came with the docker image. The build exited with linking errors due to missing symbols related to the aqlprofile. I installed the latest `libhsa-amd-aqlprofile64.so` by installing the `.deb` package from the link indicated in the warning in the `README.md`. I did so by using the command `dpkg -i ...`. This deleted the existing aqlprofile libraries from the `/opt/rocm/lib` directory, and new libraries were installed in a new directory `/opt/rocm-6.2.0-14213`.  I made symlinks in `/opt/rocm/lib` to the new libraries in the new directory. This allowed the build to proceed and complete. I do not know if this is a good way of installing the aqlprofile, nor whether replacing the aqlprofile libraries shipped with the rocm image with these new versions may break anything in the existing rocm stack. 

This experience may lead to two thoughts:

- Unless I made mistakes, this experience suggests that the source code in the `amd-mainline` branch of `rocprofiler-sdk` cannot currently be compiled against currently publicly available versions of the ROCm stack, because it appears to depend on features from future releases. This leads to the question of whether there could/should be a branch in the repository that can be compiled against an existing publicly available version of the ROCm stack. This question may be related to the distinction between the "mainline" and "staging" branches.

- It would be helpful to provide not only a "warning" about the "aqlprofile", but also some guidance to guide users/developers to install in an appropriate way the `aqlprofile` library, as well as some guidance about the impact that the installation of an updated version may have. E.g., does it impact only rocprofiler, or does it risk breaking anything in the stack? 

The work on rocprofiler-sdk seems really great! I'm looking forward to explore more.





### Operating System

Ubuntu 22.04

### CPU

AMD Ryzen9 5950X

### GPU

AMD Radeon Pro VII

### ROCm Version

ROCm 6.1.0

### ROCm Component

rocprofiler

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (5)

### jrmadsen · 2024-07-18

rocprofiler-sdk is targeted to be publicly available as a beta release in ROCm 6.2. Building it against 6.1 is unfortunately a bit pointless since 6.1 doesn’t have some necessary changes in HIP to allow tracing the HIP runtime. 

### maartenarnst · 2024-07-23

Hi @jrmadsen. OK, thanks a lot for the clarification. We'll wait for ROCm 6.2 before exploring the new rocprofiler more. 

### lucbruni-amd · 2024-12-17

Hi @maartenarnst, thank you for creating this issue!

I can see that `rocprofv3` is included in `/opt/rocm/bin` for image `rocm/dev-ubuntu-22.04:6.3`, would using this image suffice for your work?

As for your compilation issues, if you are still looking to build from source:

1. I can see there is a PR [here](https://github.com/ROCm/rocprofiler-sdk/pull/23/files) for correcting the clone URL in `README.md`. It is already corrected in the detailed documentation [here](https://github.com/ROCm/rocprofiler-sdk/blob/amd-mainline/source/docs/install/installation.md).
2. To match my ROCm version I used the `rocm-6.3.x` branch, and using the steps from the detailed documentation above, I was able to complete the build without the two main issues you described. Does this answer your question regarding having a branch that may compile against publicly released ROCm?

Please let me know if you still have troubles with the latest releases. Thanks!

### maartenarnst · 2024-12-17

Hi @lucbruni-amd. Thanks for the follow-up! Indeed, `rocprofv3` is now available in the docker images, I think as of `ROCm` 6.2. We're using it this way no, and we don't compile from source anymore. Thanks for the follow-up! OK to close the issue. 

### lucbruni-amd · 2024-12-17

Thank you for your reply, and for your patience regarding this issue. Closing as resolved.
