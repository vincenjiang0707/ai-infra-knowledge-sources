# [Issue #3263] [BUG] NVRTC wrapper omits host-computed scalar kernel arguments

source: https://github.com/tile-ai/tilelang/issues/3263
state: open | updated: 2026-09-21T16:09:32Z
labels: 

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

`0.1.14+cuda.git6ba187e2` (source checkout).

Initially reproduced at `eab74a4a`; the affected wrapper is unchanged in `6ba187e2`.

### System information

- Installation: source build with CUDA enabled, CMake/Ninja.
- OS: Windows x64 (`win32`).
- Python: 3.12.13, 64-bit.
- PyTorch: `2.11.0+cu130`.
- NVRTC: 13.0.

### Problem description

The NVRTC wrapper can omit scalar kernel arguments computed on the host after host/device splitting.

For valid host IR such as:

```python
p = n * 3 + 1
q = p * 2 + 5
T.call_packed("main_kernel", A, B, p, q, 128)
```

the device signature is `main_kernel(A, B, p, q)`, but the generated NVRTC dispatcher contains only:

```python
arg_values = A.data_ptr(), B.data_ptr()
arg_types = ctypes.c_void_p, ctypes.c_void_p
```

`SplitHostDevice` correctly captures the prepared values. The wrapper subsequently matches CUDA parameter names against the original function's arguments, where `p` and `q` do not exist. The existing TVM-FFI path executes the same host preparation correctly.

This may have gone unnoticed because ordinary compilation inlines this example's arithmetic into the kernel before `SplitHostDevice`: `A[i] + p + q` becomes `A[i] + 9 * n + 8`, leaving only the original scalar parameter `n` to forward. This happens before the NVRTC adapter; writing the bindings outside `T.Kernel` does not prevent it.

The reproducer preserves the host bindings to exercise the adapter boundary. It does not demonstrate a failure through the default compilation pipeline. Launch-time hoisting such as #3261 could expose this gap if the computed values remain on the host and become additional kernel arguments.


### Reproducible example code

Requires a CUDA-enabled TileLang source build. This inspects generated source without launching the incomplete argument list.

```python
import tilelang as tl
import tilelang.language as T
from tilelang import tvm
from tilelang.backend.module import create_backend_context
from tilelang.engine.lower import device_codegen_without_compile, get_device_call, get_host_call
from tilelang.jit.adapter.nvrtc.wrapper import TLNVRTCSourceWrapper


@T.prim_func
def main(A: T.Tensor((128,), "int32"), B: T.Tensor((128,), "int32"), n: T.int32):
    p = T.bind(n * 3 + 1)
    q = T.bind(p * 2 + 5)
    with T.Kernel(1, threads=128):
        i = T.get_thread_binding()
        B[i] = A[i] + p + q


ctx = create_backend_context({"kind": "cuda", "arch": "sm_80"}, "c", "nvrtc")
original = tvm.IRModule({"main": main})
# Preserve host bindings to exercise the adapter boundary.
mod = tvm.transform.Sequential(
    [
        tvm.tirx.transform.BindTarget(ctx.target),
        tl.transform.MaterializeKernelLaunch(),
        tl.transform.LowerOpaqueBlock(),
        tl.transform.AnnotateDeviceRegions(),
        tl.transform.SplitHostDevice(),
        tvm.tirx.transform.AnnotateEntryFunc(),
        tl.transform.MakePackedAPI(),
        tl.transform.LowerDeviceKernelLaunch(),
    ]
)(original)
host = tvm.tirx.transform.Filter(get_host_call())(mod)
device = tvm.tirx.transform.Filter(get_device_call())(mod)
source = device_codegen_without_compile(device, ctx).inspect_source()
wrapper = TLNVRTCSourceWrapper(original, source, ctx.target, device_mod=device, host_mod=host)
print(source)
print(wrapper.host_func)
```


### Traceback

No traceback is produced by the source-generation reproducer. The malformed dispatcher is inspected, not executed with an incomplete CUDA argument list.

### Expected behavior

Resolve launch operands from the actual host call, preserve the required scalar bindings and their execution scope, and marshal every device argument in signature order. Unsupported host computations should produce an explicit diagnostic rather than an incomplete CUDA argument list.


### Additional context

The existing TVM-FFI path and a separate IR-driven NVRTC prototype passed changing-input and guarded-launch checks on the same host/device program.

This differs from #2755/#2756, which concerned forwarding original scalar parameters and dynamic strides. The missing values here are introduced by host preparation and are not original function parameters. Related preparation work is discussed in #3261.


## 评论 (3)

### sepcnt · 2026-09-21

Heavy ctypes conversion would also degrades optimization effects in https://github.com/tile-ai/tilelang/issues/3261.

### LeiWang1999 · 2026-09-21

Following the review of #3264, the preferred long-term solution is to have NVRTC use the existing TVM-FFI host execution path. We closed that PR with the rationale here: https://github.com/tile-ai/tilelang/pull/3264#issuecomment-5763558608. This issue remains valid and should stay open to track the replacement.

NVRTC should be the device compiler choice, while host preparation and execution should go through the shared host lowering/codegen and runtime:

- Device IR -> CUDA source -> NVRTC -> cubin/PTX -> CUDA runtime module.
- Host IR -> existing host codegen -> TVM-FFI executable, importing that CUDA module.

This makes host-prepared scalar arguments a natural consequence of executing the host program. Bindings, dtype conversions, conditions, loops, and supported host helper calls can use the same implementation as the existing TVM-FFI path. We would avoid having to reconstruct these semantics individually in a Python launcher whenever a compiler transformation introduces new host preparation. The integration needs to reuse host codegen as well as the FFI calling interface.

The existing CUDA build already accepts compiled device bytes through a callback and packages them as a runtime module. During review, a process-local experiment replaced that callback with NVRTC compilation, retained `execution_backend="tvm_ffi"`, and explicitly disallowed NVCC compilation. It compiled and executed successfully on the GPU, including a float32 host-condition case that the Python launcher evaluated incorrectly. This is a feasibility check; the combined path still needs a supported configuration and full integration coverage.

This direction also addresses the concern above about repeatedly expressing host arithmetic and conversions through Python/ctypes. Any launch-latency benefit should be measured alongside host compilation costs.

The follow-up should preserve the host-binding reproducer and useful regression cases from #3264, and cover compiler options, cache keys, stream/device behavior, TMA and other launch metadata, and export/load behavior. Host toolchain requirements need to be explicit, especially on Windows: NVRTC compiles device code, and the C host codegen path still needs a host C/C++ compiler. LLVM support or a deliberately restricted fallback can be evaluated where appropriate.


### sepcnt · 2026-09-21

@LeiWang1999 Thanks for your review. #3264 was initially intended to experiment with the launch-invariant lowering proposed in [[#3261](https://github.com/tile-ai/tilelang/issues/3261)](https://github.com/tile-ai/tilelang/issues/3261). The ablation results show that the existing CPython + NVRTC path becomes especially inefficient as the number of parameters increases. I’m still looking into this.
