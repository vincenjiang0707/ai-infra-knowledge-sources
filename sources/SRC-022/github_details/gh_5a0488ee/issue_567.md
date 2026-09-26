# [Issue #567] Missing roc:: namespace in rccl-config.cmake

source: https://github.com/ROCm/rccl/issues/567
state: closed | updated: 2023-04-05T23:12:42Z
labels: 

## 正文

 Hello, this is a bug report concerning RCCL packaged as a part of ROCm framework, as of 5.1.1. The file `rccl-config.cmake` should be changed as show below:

```diff
--- rccl-config.cmake.old  2022-06-21 20:35:34.815053058 +0000
+++ rccl-config.cmake  2022-06-21 18:58:15.774500081 +0000
@@ -91,14 +91,14 @@
 
 include(${rccl_TARGET_FILE})
 
-set(rccl_LIBRARIES rccl)
+set(rccl_LIBRARIES roc::rccl)
 
-set(rccl_LIBRARY rccl)
+set(rccl_LIBRARY roc::rccl)
 
-set(RCCL_LIBRARIES rccl)
+set(RCCL_LIBRARIES roc::rccl)
 
-set(RCCL_LIBRARY rccl)
+set(RCCL_LIBRARY roc::rccl)
 
-set(rccl_LIBRARIES rccl)
+set(rccl_LIBRARIES roc::rccl)
 
-set(rccl_LIBRARY rccl)
+set(rccl_LIBRARY roc::rccl)
```

Background. The missing namespace is necessary, in order to pick up targets defined in `rccl-targets-noconfig.cmake`. Without the namespace, CMake simply issues `-lrccl` to the linker command, which will fail. For example, PyTorch fails like this:

```
/opt/rh/devtoolset-7/root/usr/libexec/gcc/x86_64-redhat-linux/7/ld: cannot find -lrccl
```

In other libraries the namespace is present, for example in rocblas. So, this patch simply aligns RCCL CMake config with the other ROCm libraries.

The file `rccl-config.cmake` is not present in this repository, please help me to report it where it belongs to.

## 评论 (6)

### dmikushin · 2022-06-22

PyTorch tries to workaround this bug by helping to find RCCL manually, with a TODO note:

```
  # TODO: rccl_LIBRARIES should return fullpath to the library file,
  # however currently it's just the lib name
  find_library(PYTORCH_RCCL_LIBRARIES ${rccl_LIBRARIES} HINTS ${RCCL_PATH}/lib)
```

MIOpen is the only one library that like RCCL requires the same handling:

```
  # TODO: miopen_LIBRARIES should return fullpath to the library file,
  # however currently it's just the lib name
  find_library(PYTORCH_MIOPEN_LIBRARIES ${miopen_LIBRARIES} HINTS ${MIOPEN_PATH}/lib)
```

### pfultz2 · 2022-06-22

This issue is that it lists the target as `rccl` instead of `roc::rccl` in `rocm_export_targets`: 

https://github.com/ROCmSoftwarePlatform/rccl/blob/develop/CMakeLists.txt#L351

### dmikushin · 2022-06-22

Someone made a point that end users should just link against the ROCm, and then it correctly brings the whole collection of libraries into the link command. That indeed works. On the other hand, the issue happens when the user is trying to link just against RCCL_LIBRARY.

### doctorcolinsmith · 2022-08-18

@pfultz2 Can this issue be closed?  Looks like the fix was completed.

### dmikushin · 2022-08-19

@doctorcolinsmith , the fix was unfortunately reverted, and we still wait for it to be re-applied again, see https://github.com/ROCmSoftwarePlatform/rccl/pull/576

### gilbertlee-amd · 2023-04-05

This should be fixed with current RCCL.  Please re-open if this is not the case.
