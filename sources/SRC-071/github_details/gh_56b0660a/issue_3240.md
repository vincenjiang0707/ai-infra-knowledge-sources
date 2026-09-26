# [Issue #3240] [BUG][CuTeDSL][FP4/FP8] DeepSeek V4 act quant: FP4 conversion/store broken against CUTLASS DSL 4.7, FP8 store rejected by libNVVM

source: https://github.com/tile-ai/tilelang/issues/3240
state: open | updated: 2026-09-17T10:46:17Z
labels: 

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I searched the issue tracker for an existing dedicated report.

### What version of TileLang are you using?

Current `main` at `e688a439a8f79d69497d02c4fad7c75fada954ad`.

### System information

- GPU: NVIDIA L20 (sm_89)
- CUDA / nvcc: 12.8.61 (`/usr/local/cuda-12.8`)
- PyTorch: 2.10.0+cu128
- TileLang: editable build of `main` (`0.1.14+cuda.gite688a439`)
- CuTeDSL / CUTLASS DSL: `nvidia-cutlass-dsl==4.7.0` with `nvidia-cutlass-dsl-libs-cu12==4.7.0`

### How the CuTeDSL backend is really selected

`examples/conftest.py` xfails `deepseek_v4/test_tilelang_example_deepseek_v4.py::test_example_act_quant`
when `TILELANG_TARGET=cutedsl`, and `.github/workflows/ci.yml` runs the examples with
`TILELANG_TARGET: cutedsl`. But nothing in the library reads `TILELANG_TARGET` — only
`examples/conftest.py` and two example tests do. Verified on current `main`:

```text
$ TILELANG_TARGET=cutedsl python -c "...compile a trivial kernel, print adapter/target..."
TILELANG_TARGET= cutedsl
adapter: TVMFFIKernelAdapter
target: {"kind":"cuda", ..., "arch":"sm_89"}
```

So that env var only toggles the xfail markers; the examples still run on the default
backend. The backend is actually selected with `TILELANG_DEFAULT_TARGET=cutedsl`
(or `tilelang.compile(..., target="cutedsl")`). Worth fixing in its own right, because it
makes the CuTeDSL CI job and every "reproduce under CuTeDSL" recipe a no-op.

### Problem description

With the backend actually selected, the DeepSeek V4 activation-quantization example fails
in two independent ways: the FP4 conversion/store helpers call MLIR ops that no longer
exist in CUTLASS DSL 4.7, and the FP8 store path is rejected by libNVVM.

```text
$ TILELANG_DEFAULT_TARGET=cutedsl python -c "import act_quant; act_quant.test_fp8_act_quant(M=64,N=256,block_size=128)"
CompilerDiagnosticError: error: NVVM backend compilation failed
  error: libNVVM failed while compiling generated device IR.
  note: target architecture: sm_89
  raw: NVVM_ERROR_COMPILATION, libNVVM extra log: NVVM backend compilation failed

$ TILELANG_DEFAULT_TARGET=cutedsl python -c "import act_quant; act_quant.test_fp4_act_quant(M=64,N=256,block_size=32)"
AttributeError: module 'cutlass._mlir.dialects.vector' has no attribute 'extractelement'
  at tilelang/contrib/cutedsl/utils.py:256 in _float32_to_f4e2m1_tensor
```

`test_round_trip_error` fails with the same libNVVM error because it calls the FP8 path first.

### Root causes found so far

**1. FP4 conversion helpers use removed MLIR ops.**
`tilelang/contrib/cutedsl/utils.py` calls `vector.extractelement` / `vector.insertelement`
in `_f4e2m1_to_float32_tensor` and `_float32_to_f4e2m1_tensor`. CUTLASS DSL 4.7 ships
`vector.extract` / `vector.insert` (with explicit dynamic/static position lists) instead:

```text
$ python -c "from cutlass._mlir.dialects import vector; print([n for n in dir(vector) if 'extract' in n or 'insert' in n])"
['ExtractOp', 'ExtractStridedSliceOp', 'InsertOp', 'InsertStridedSliceOp', 'extract', 'extract_strided_slice', 'insert', 'insert_strided_slice']
```

Porting the four call sites (`vector.extract(v, [], [idx])`, `vector.insert(v, dst, [], [idx])`)
makes the FP4 kernel compile and run.

**2. The CuTeDSL adapter materializes sub-byte outputs unpacked.**
`CuTeDSLKernelAdapter._convert_torch_func` allocates outputs as
`torch.empty(*param_shapes[i], dtype=param_dtypes[i])` using the *logical* TIR shape. For
`float4_e2m1fn` (4-bit) the torch storage dtype `float4_e2m1fn_x2` packs two elements per
byte, so the last dimension must be divided by the packing factor — which is what the CUDA
adapters already do (see the `stride_scale` note in `tilelang/jit/adapter/tvm_ffi.py`).
Without it, `fp4_act_quant` returns a `(M, N)` tensor instead of `(M, N/2)`:

```text
AssertionError: Shape mismatch: torch.Size([64, 256]) vs torch.Size([64, 128])
```

**3. The wrapper's FP8 dtype mapping disagrees with the codegen.**
`TLCuTeDSLSourceWrapper._TYPE_MAP` maps the TIR dtype string to `cutlass.Float8E4M3`, while
`src/cuda/codegen/codegen_cutedsl.cc` emits `Float8E4M3FN` ("Only Float8E4M3FN is supported
at the moment"). The TIR string for `float8_e4m3fn` is `float8_e4m3`, so the generated fake
tensors got `Float8E4M3` and every store tried `Float8E4M3FN.to(Float8E4M3)`:

```text
TypeError: Unsupported destination float type: Float8E4M3
  at cutlass/base_dsl/typing.py:1123 in Numeric.to
```

**Status after fixing 1–3** (local patch, no upstream PR yet):

| target | `test_fp8_act_quant` | `test_fp4_act_quant` | `test_round_trip_error` |
|---|---|---|---|
| `cuda` | pass | pass | pass |
| `cutedsl` | **libNVVM failure** | **pass** (`85/8192` bytes differ from FP4 tie-breaking) | **libNVVM failure** |

### Minimal reproducers

FP4 (fails before fix 1; passes after fixes 1–3 when written as a vectorized copy, which is
what the DeepSeek kernel does):

```python
import tilelang, tilelang.language as T
tilelang.disable_cache()

@T.prim_func
def k(A: T.Tensor((256,), "bfloat16"), B: T.Tensor((256,), "float4_e2m1fn")):
    with T.Kernel(1, threads=256):
        tx = T.get_thread_binding()
        B[tx] = T.cast(A[tx], "float4_e2m1fn")

tilelang.compile(k, target="cutedsl")
```

A *scalar* FP4 store is separately unsupported and reports
`ValueError: Sub-byte scalar dereference not supported for type Float4E2M1FN`; the DeepSeek
kernel avoids it by storing through `T.copy`, so that is not part of this report.

FP8 — this is the remaining blocker and it is not specific to the DeepSeek kernel:

```python
import torch, tilelang, tilelang.language as T
tilelang.disable_cache()

@T.prim_func
def k(A: T.Tensor((256,), "bfloat16"), B: T.Tensor((256,), "float8_e4m3fn")):
    with T.Kernel(1, threads=256):
        tx = T.get_thread_binding()
        B[tx] = T.cast(A[tx], "float8_e4m3fn")

kernel = tilelang.compile(k, target="cutedsl")     # source generation succeeds
a = torch.randn(256, dtype=torch.bfloat16, device="cuda")
b = torch.empty(256, dtype=torch.float8_e4m3fn, device="cuda")
kernel(a, b)   # CompilerDiagnosticError: NVVM backend compilation failed (sm_89)
```

The same kernel with `target="cuda"` runs and produces correct FP8 output. `T.copy`-based
vectorized FP8 stores, `64`/`256`-thread blocks and both `round_scale` settings all fail at
libNVVM. `libNVVM extra log` is empty, so the failure carries no further detail; compiling
the same source for `sm_90`/`sm_100` targets succeeds at the TileLang level (the cubin
build happens lazily at launch, which cannot run on this GPU, so arch attribution is not
proven).

### Expected behavior

The DeepSeek V4 activation-quantization example should compile and pass under the CuTeDSL
backend, and its entry should be removed from `CUTEDSL_KNOWN_FAILURES`.

### Proposed scope

1. Port the FP4 conversion helpers to the CUTLASS DSL 4.7 `vector.extract` / `vector.insert`
   API.
2. Pack sub-byte output shapes in `CuTeDSLKernelAdapter._convert_torch_func`.
3. Align `_TYPE_MAP["float8_e4m3"]` with the codegen's `Float8E4M3FN`.
4. Diagnose the remaining libNVVM failure for FP8 stores (needs a green FP8 path before the
   example can pass and the xfail can be dropped).
5. Add a focused CuTeDSL regression test for FP4/FP8 conversion/store lowering instead of
   relying on the whole DeepSeek example.
6. Separately: make `TILELANG_TARGET=cutedsl` actually select the backend, or update the CI
   job and the documented reproduction to use the variable the library reads.

### Related

- #1454 — CuTeDSL backend roadmap
- #2187 — added the CuTeDSL FP4 dtype mapping and documented the remaining limitation


## 评论 (1)

### 0z5a · 2026-09-17

The FP4 half of this is now up as #3241:

- `contrib/cutedsl/utils.py` ported to `vector.extract` / `vector.insert` (the helpers were calling the removed `vector.extractelement` / `vector.insertelement`),
- sub-byte outputs are now allocated with the packed last dimension in `CuTeDSLKernelAdapter`,
- `_TYPE_MAP["float8_e4m3"]` now agrees with the codegen's `Float8E4M3FN`.

With those, `test_fp4_act_quant(M=64, N=256, block_size=32)` passes under `target="cutedsl"` (85/8192 packed bytes differ from the reference only at FP4 rounding tie-breaks), and a focused FP4 regression test was added.

Still open, and not addressed by that PR: the FP8 store path fails inside libNVVM on sm_89 (`NVVM_ERROR_COMPILATION`, empty backend log) even for a minimal `bf16 -> float8_e4m3fn` elementwise store, so `test_example_act_quant` and `test_round_trip_error` cannot pass yet and the xfail entry stays. Also worth deciding separately: `TILELANG_TARGET=cutedsl` does not select this backend — only `examples/conftest.py` reads it, so the CI job and the documented reproduction run on the default backend.

