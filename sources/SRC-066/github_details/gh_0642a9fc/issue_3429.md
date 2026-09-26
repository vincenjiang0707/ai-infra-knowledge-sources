# [Issue #3429] [BUG] ICE when compiling kernel converting `Float32` to `Float8E4M3FN`

source: https://github.com/NVIDIA/cutlass/issues/3429
state: closed | updated: 2026-09-22T06:42:13Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
Trying to compile a kernel which converts a `float` to `Float8E4M3FN` causes an ICE. This only occurs when compiling the kernel directly, not when compiling a `@cute.jit` function that launches the kernel.

**Steps/Code to reproduce bug**

First, define `kernel` and `launch`:

```
import cutlass
from cutlass import cute

@cute.kernel
def kernel(x: cutlass.Float32):
    tidx, _, _ = cute.arch.thread_idx()
    if tidx == 0:
        x_fp8 = cutlass.Float8E4M3FN(x)
        cute.printf(x_fp8)

@cute.jit
def launch(x: float):
    print("Compiling launch()")
    cute.printf("Host side: launching kernel")
    kernel(x).launch(
        grid=(1,1,1),
        block=(32,1,1),
    )

cutlass.cuda.initialize_cuda_context()
```

#### Example 1
calling launch directly does not cause a problem:
```
[... first snippet ...]
launch(500.0)
```
Running the above shows:
```
Compiling launch()
Host side: launching kernel
448.000000
```
Where 448.0 is the maximum representable value in FP8E4M3FN, as expected.

#### Example 2
using `cute.compile` on `launch` does not cause a problem:
```
[... first snippet ...]
print("About to compile launch()")
compiled = cute.compile(launch, 0.0)
print("Compiled launch()")
compiled(500.0)
```
Running the above shows:
```
About to compile launch()
Compiling launch()
Compiled launch()
Host side: launching kernel
448.000000
```

#### Example 3
using `cute.compile` on `kernel` causes an Internal Compiler Error:
```
[... first snippet ...]
print("About to compile kernel()")
compiled = cute.compile(kernel, 0.0)
print("Compiled kernel()")
launch(500.0)
```
Running the above shows:
```
About to compile kernel()
MLIR Python Diagnostic handler raised exception: std::bad_cast
error: cannot be converted to LLVM IR: missing `LLVMTranslationDialectInterface` registratio

[Internal Error] The compiler hit a problem it could not trace back to your code.
This is a bug in the DSL, not a mistake in your kernel.

Detail: 🧊🧊🧊 ICE 🧊🧊🧊

Cause: Caused exception: Failure while creating the ExecutionEngine.

What to do:
  Please report this with the snippet above and your kernel.
  Re-run with CUTE_DSL_SHOW_STACKTRACE=1 to include the full technical detail.

============================================================================================
root@gb200-nvl4-ts2-93:/workspace# CUTE_DSL_SHOW_STACKTRACE=1 python3 test_fp8.py
About to compile kernel()
MLIR Python Diagnostic handler raised exception: std::bad_cast
error: cannot be converted to LLVM IR: missing `LLVMTranslationDialectInterface` registratio
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 1553, in compile_and_jit
    kernel = self.compiler_provider.compile_and_jit(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/compiler.py", line 215, in compile_and_jit
    return self.jit(module, opt_level, shared_libs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/compiler.py", line 184, in jit
    return self.execution_engine.ExecutionEngine(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Failure while creating the ExecutionEngine.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/workspace/test_fp8.py", line 27, in <module>
    compiled = cute.compile(kernel, 0.0)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/compiler.py", line 1250, in __call__
    return self._compile(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/compiler.py", line 1400, in _compile
    return func._dsl_object._func(func, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2680, in _func
    return self._func_impl(funcBody, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2693, in _func_impl
    result = self.generate_mlir(
             ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2301, in generate_mlir
    jit_function = self.compile_and_cache(
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/cutlass_dsl/cutlass.py", line 925, in compile_and_cache
    return super().compile_and_cache(  # type: ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2033, in compile_and_cache
    engine = self.compile_and_jit(
             ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 1585, in compile_and_jit
    raise DSLRuntimeError("🧊🧊🧊 ICE 🧊🧊🧊", cause=e)
cutlass.base_dsl.common.DSLRuntimeError:
[Internal Error] The compiler hit a problem it could not trace back to your code.
This is a bug in the DSL, not a mistake in your kernel.

Detail: 🧊🧊🧊 ICE 🧊🧊🧊

Cause: Caused exception: Failure while creating the ExecutionEngine.

What to do:
  Please report this with the snippet above and your kernel.
  Re-run with CUTE_DSL_SHOW_STACKTRACE=1 to include the full technical detail.

====================================================================================================
```

**Expected behavior**
I would expect 448.0 to be printed, just like in the other cases.

**Environment details (please complete the following information):**
 - Environment location: [Docker] 

**Additional context**
No additional context.


## 评论 (5)

### Shreya-gaur · 2026-08-10

This is a known bug which was fixed in CuTeDSL version 4.6.2 onwards(Listed in the release notes as "Fixed a vectorized fp32->f8 conversion issue"). If you upgrade your wheel, the issue should be resolved. If you cannot upgrade, the code should be changed as following to circumvent the issue:
```python
@cute.kernel
def kernel(x: cutlass.Float32):
    tidx, _, _ = cute.arch.thread_idx()
    if tidx == 0:
        # nvgpu.cvt_fptrunc (f32 -> f8) requires both operand and result to be
        # 32-bit-aligned 1-d vectors, so a direct scalar cast
        # `cutlass.Float8E4M3FN(x)` emits invalid IR. Route the value through a
        # vector<4xf32> (result vector<4xf8> = 32 bits), convert the whole vector,
        # then take element 0.
        x_vec = cute.full((4,), x, cutlass.Float32)
        fp8_vec = x_vec.to(cutlass.Float8E4M3FN)
        # Keep the round-trip vectorized too (scalar fp8 -> f32 hits the same
        # cvt_fpext scalar-operand bug). Convert back on the vector, then extract
        # a plain f32 scalar, which cute.printf can print.
        x_roundtrip = fp8_vec.to(cutlass.Float32)[0]
        cute.printf(x_roundtrip)
```

### janekb04 · 2026-08-11

Hi @Shreya-gaur, I am using `nvidia-cutlass-dsl` version `4.6.2`. `pip show nvidia-cutlass-dsl` gives:
```
Name: nvidia-cutlass-dsl
Version: 4.6.2
Summary: NVIDIA CUTLASS Python DSL
[...]
```
Unfortunately, the bug is still present and the workaround you suggested also causes an ICE.

The previous version,
```python
import cutlass
from cutlass import cute

@cute.kernel
def kernel(x: cutlass.Float32):
    tidx, _, _ = cute.arch.thread_idx()
    if tidx == 0:
        x_fp8 = cutlass.Float8E4M3FN(x)
        cute.printf(x_fp8)

@cute.jit
def launch(x: float):
    print("Compiling launch()")
    cute.printf("Host side: launching kernel")
    kernel(x).launch(
        grid=(1,1,1),
        block=(32,1,1),
    )

cutlass.cuda.initialize_cuda_context()

print("About to compile kernel()")
compiled = cute.compile(kernel, 0.0)
print("Compiled kernel()")
launch(500.0)
```
gives
```
About to compile kernel()
dler raised exception: std::bad_cast
error: cannot be converted to LLVM IR: missing `LLVMTranslationDialectInterface` registration for dialect for op: nvgpu.cvt_fptrunc
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 1647, in compile_and_jit
    kernel = self.compiler_provider.compile_and_jit(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/compiler.py", line 215, in compile_and_jit
    return self.jit(module, opt_level, shared_libs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/compiler.py", line 184, in jit
    return self.execution_engine.ExecutionEngine(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Failure while creating the ExecutionEngine.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/workspace/test.py", line 23, in <module>
    compiled = cute.compile(kernel, 0.0)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/compiler.py", line 1250, in __call__
    return self._compile(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/compiler.py", line 1396, in _compile
    return func._dsl_object._func(func, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2782, in _func
    return self._func_impl(funcBody, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2795, in _func_impl
    result = self.generate_mlir(
             ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2397, in generate_mlir
    jit_function = self.compile_and_cache(
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/cutlass_dsl/cutlass.py", line 884, in compile_and_cache
    return super().compile_and_cache(  # type: ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2127, in compile_and_cache
    engine = self.compile_and_jit(
             ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 1679, in compile_and_jit
    raise DSLRuntimeError("🧊🧊🧊 ICE 🧊🧊🧊", cause=e)
cutlass.base_dsl.common.DSLRuntimeError: 
^[[91m^[[1m[Internal Error] The compiler hit a problem it could not trace back to your code.^[[0m
This is a bug in the DSL, not a mistake in your kernel.

^[[94mDetail:^[[0m 🧊🧊🧊 ICE 🧊🧊🧊

^[[94mCause:^[[0m Caused exception: Failure while creating the ExecutionEngine.

^[[92mWhat to do:^[[0m
  ^[[92mPlease report this with the snippet above and your kernel.^[[0m
  ^[[92mRe-run with CUTE_DSL_SHOW_STACKTRACE=1 to include the full technical detail.^[[0m

====================================================================================================
```
The version with the workaround
```python
import cutlass
from cutlass import cute

@cute.kernel
def kernel(x: cutlass.Float32):
    tidx, _, _ = cute.arch.thread_idx()
    if tidx == 0:
        # nvgpu.cvt_fptrunc (f32 -> f8) requires both operand and result to be
        # 32-bit-aligned 1-d vectors, so a direct scalar cast
        # `cutlass.Float8E4M3FN(x)` emits invalid IR. Route the value through a
        # vector<4xf32> (result vector<4xf8> = 32 bits), convert the whole vector,
        # then take element 0.
        x_vec = cute.full((4,), x, cutlass.Float32)
        fp8_vec = x_vec.to(cutlass.Float8E4M3FN)
        # Keep the round-trip vectorized too (scalar fp8 -> f32 hits the same
        # cvt_fpext scalar-operand bug). Convert back on the vector, then extract
        # a plain f32 scalar, which cute.printf can print.
        x_roundtrip = fp8_vec.to(cutlass.Float32)[0]
        cute.printf(x_roundtrip)

@cute.jit
def launch(x: float):
    print("Compiling launch()")
    cute.printf("Host side: launching kernel")
    kernel(x).launch(
        grid=(1,1,1),
        block=(32,1,1),
    )

cutlass.cuda.initialize_cuda_context()

print("About to compile kernel()")
compiled = cute.compile(kernel, 0.0)
print("Compiled kernel()")
launch(500.0)
```
Gives the exact same output (except the error occurs at line 33 instead of 22).

### jackkosaian · 2026-08-14

@janekb04 , `cute.compile` cannot currently be called on a `@cute.kernel`-decorated function. The error message should ideally spell this out instead of giving an ICE.

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3619.

### brandon-yujie-sun · 2026-09-22

@janekb04 Like @jackkosaian mentioned, we now get an error message in 4.8 to fail the illegal case loudly for cute.compile.
