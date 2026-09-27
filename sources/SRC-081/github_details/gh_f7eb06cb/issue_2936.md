# [Issue #2936] [Windows] ExLlamaV2 GPTQ/AWQ JIT build silently fails at link: unresolved external symbol cublasHgemm (missing cublas.lib in extra_ldflags)

source: https://github.com/ModelCloud/GPTQModel/issues/2936
state: closed | updated: 2026-07-09T09:31:41Z
labels: 

## 正文

## Summary

On Windows, the ExLlamaV2 JIT extensions (both GPTQ and AWQ) always fail to build at the final
link step because `cublas.lib` is never passed to the MSVC linker. The failure is **silent**:
gptqmodel logs `torch.ops JIT compilation failed ... using fallback path` and quietly selects a
slower kernel, so users with a fully working MSVC + CUDA toolchain still never get ExLlamaV2.

The newer ExLlamaV3 extension already handles this correctly via `_extra_ldflags()` in
`gptqmodel/exllamav3/ext.py` — the ExLlamaV2 extension definitions in
`gptqmodel/utils/exllamav2.py` simply don't pass any `extra_ldflags`.

## Environment

- gptqmodel 7.1.0 (PyPI), transformers 5.12.1, torch 2.6.0+cu124
- Windows 11, Python 3.10.6
- MSVC 14.39.33519 (VS 2022 Community, C++ workload), Windows SDK 10.0.22621.0
- CUDA toolkit 12.4.131 (nvcc), GPU: RTX 3050 Ti Laptop (SM 8.6)

Confirmed still present on current `main` (`gptqmodel/utils/exllamav2.py` has no
`extra_ldflags` / `cublas` reference as of 2026-07-04).

## Reproduction

1. Windows machine with working `cl.exe` + `nvcc` on PATH (`torch.utils.cpp_extension.load_inline`
   with a trivial CUDA kernel compiles fine).
2. Load any AWQ or GPTQ checkpoint through transformers (e.g.
   `Qwen/Qwen2-VL-2B-Instruct-AWQ`), or anything that triggers the ExLlamaV2 extension build.
3. Compilation of all `.cu`/`.cpp` objects succeeds, then linking fails.

Running `ninja -v` manually inside the build dir shows the actual error (gptqmodel swallows it):

```
[1/1] link.exe ext_awq.o q_matrix_awq.cuda.o q_gemm_awq.cuda.o /nologo /DLL c10.lib c10_cuda.lib
      torch_cpu.lib torch_cuda.lib ... cudart.lib /out:gptqmodel_exllamav2_awq_ops.pyd
q_gemm_awq.cuda.o : error LNK2019: unresolved external symbol cublasHgemm referenced in function
      "void __cdecl gemm_half_q_half_cuda(struct cublasContext *, ...)"
gptqmodel_exllamav2_awq_ops.pyd : fatal error LNK1120: 1 unresolved externals
```

What the user sees instead is only:

```
INFO  ExLlamaV2 AWQ: torch.ops JIT compilation failed in 57s (estimated ~35s); using fallback path.
```

## Root cause

`q_gemm.cu` / `q_gemm_awq.cu` call `cublasHgemm`, but neither
`_EXLLAMAV2_GPTQ_TORCH_OPS_EXTENSION` nor `_EXLLAMAV2_AWQ_TORCH_OPS_EXTENSION` in
`gptqmodel/utils/exllamav2.py` set `extra_ldflags`, so on Windows the MSVC link line never
includes `cublas.lib`. On Linux this happens to work because of how the shared library resolves
symbols at load time; MSVC requires the import library at link time.

## Suggested fix

Mirror `_extra_ldflags()` from `gptqmodel/exllamav3/ext.py`:

```python
def _exllamav2_ldflags() -> list[str]:
    if sys.platform != "win32":
        return []
    flags = ["cublas.lib"]
    if sys.base_prefix != sys.prefix:  # venv: python .lib lives in the base install
        flags.append(f"/LIBPATH:{os.path.join(sys.base_prefix, 'libs')}")
    return flags
```

and pass `extra_ldflags=_exllamav2_ldflags` to both `TorchOpsJitExtension(...)` definitions.

Verified locally: with this one-line wiring both extensions build and load
(`ExLlamaV2 AWQ: torch.ops JIT extension ready in 61s`), and inference output is correct.

A secondary suggestion: when a JIT build fails, logging the last few lines of the ninja error
(or pointing at the build dir) would make this class of problem much easier to diagnose —
the current single INFO line hides a hard toolchain error behind "using fallback path".


## 评论 (1)

### Qubitium · 2026-07-04

@xXpeira12  https://github.com/ModelCloud/GPTQModel/issues/2937#issuecomment-4879752534 Feel free to submit a PR which include your linkage fixes. Thanks!
