# [Issue #3635] [BUG] CuTe DSL 4.7.1 TVM-FFI AOT objects reference symbols missing from `libcuda_dialect_runtime_static.a`

source: https://github.com/NVIDIA/cutlass/issues/3635
state: closed | updated: 2026-09-22T15:07:59Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**

CuTe DSL 4.7.1 generates TVM-FFI-enabled AOT object files that reference the following runtime symbols:

```text
CuteDSLRT_TVMFFISetRaisedCudaError
CuteDSLRT_TVMFFISetRaisedCudaLaunchError
```

However, these symbols are not provided by the packaged `libcuda_dialect_runtime_static.a`.

They are only exported by `libcute_dsl_runtime.so`.
As a result, an AOT object generated with TVM-FFI enabled can no longer be linked using the static CUDA dialect runtime that worked for previous CuTe DSL versions.

This appears to be either:

1. a missing-object packaging issue in `libcuda_dialect_runtime_static.a`, or
2. an undocumented breaking change requiring TVM-FFI C++ AOT users to switch from
   `libcuda_dialect_runtime_static.a` to the shared
     `libcute_dsl_runtime.so`.

**Steps/Code to reproduce bug**

Install CuTe DSL 4.7.1 with CUDA 13 support:

```bash
$ pip3 install "nvidia-cutlass-dsl[cu13]==4.7.1"
```
```bash
LIBDIR="$(python -m cutlass.cute.export.aot_config --libdir)"
```

The required symbol is absent from the static CUDA dialect runtime:

```bash
$  nm -g --defined-only "${LIBDIR}/libcuda_dialect_runtime_static.a" | grep CuteDSLRT_TVMFFISetRaisedCuda
```

=> no output

The symbol is present in the shared CuTe DSL runtime:

```bash
nm -D --defined-only "${LIBDIR}/libcute_dsl_runtime.so" | grep CuteDSLRT_TVMFFISetRaisedCuda
```

=>

```text
00000000001aec00 T CuteDSLRT_TVMFFISetRaisedCudaError
00000000001aec70 T CuteDSLRT_TVMFFISetRaisedCudaLaunchError
```

Linking the generated object with only `libcuda_dialect_runtime_static.a` therefore fails:

```text
undefined reference to `CuteDSLRT_TVMFFISetRaisedCudaError'
```

**Expected behavior**

Should be able to compile with static library link? Or is it an intended breaking change?

**Environment details (please complete the following information):**

nvidia-cutlass-dsl: 4.7.1
nvidia-cutlass-dsl-libs-cu13: 4.7.1
apache-tvm-ffi: 0.1.13.post3

**Additional context**
Add any other context about the problem here.


## 评论 (3)

### brandon-yujie-sun · 2026-09-17

Thanks for reporting this, will take a look

### brandon-yujie-sun · 2026-09-22

Update - We got a fix and will include that in the upcoming release.

### ktaebum · 2026-09-22

@brandon-yujie-sun Thanks a lot! Will close the issue.
