# [Issue #2021] Target-wide `-mavx512*` puts EVEX in the scalar dequant fallbacks; source builds SIGILL on non-AVX-512 x86_64

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2021
state: open | updated: 2026-07-28T19:34:40Z
labels: Linux, Build, x64 CPU

## 正文

The AVX-512 build flags are scoped two different ways:

- **Enablement is target-wide:** `CMakeLists.txt:375` gates on whether the *compiler* accepts `-mavx512f`,
  true on any modern GCC regardless of the machine, then applies `-mavx512f -mavx512bw -mavx512dq
  -mavx512vl` to the whole `bitsandbytes` target.
- **Suppression is per-function:** the `#pragma GCC target("avx2,fma,no-avx512f")` region from #1901
  covers the scalar quantize functions that PR added, and nothing else.

GCC can then auto-vectorize any ungated function in those TUs with EVEX instructions. That includes the
paths which exist because the CPU has no AVX-512. `dequantizeBlockwise8bitCpu` has no AVX-512 branch at
all, and `dequantizeBlockwise4bitCpu`'s scalar fallback is the branch reached when `has_avx512f()` returns
false. Both get compiled with AVX-512 anyway, so a from-source build on a machine without it dies the
first time one of them runs.

Runtime detection reports correctly here (`has_avx512bf16()` → `0`, `backends.cpu.ops._has_avx512` →
`False`). It cannot guard a function that was never an AVX-512 path to begin with.

## Repro

Xeon W-1250 (Comet Lake, no AVX-512) / `g++ (Debian) 14.2.0` / torch 2.13.0+cpu / Python 3.10.20, built
with `RUNNER_OS=Linux RUNNER_ARCH=X64 bash .github/scripts/build-cpu.sh`:

```python
import torch, bitsandbytes as bnb

A = torch.randn(64, 64, dtype=torch.float16, requires_grad=True)
B = torch.randn(96, 64, dtype=torch.float16)
torch.nn.init.xavier_uniform_(B)
bias = torch.randn(96, dtype=torch.float16, requires_grad=True)

B2, qs = bnb.functional.quantize_4bit(B, compress_statistics=True, quant_type="fp4")
out = bnb.matmul_4bit(A, B2, qs, bias=bias)
# Illegal instruction (exit 132)
```

`compress_statistics=True` is crucial; it routes the nested absmax through the 8-bit blockwise
dequant. Same crash from the suite via
`tests/test_autograd.py::test_matmul_4bit[quant_type=fp4-compress_statistics=T-fp16-has_bias=T-transpose_B=T-req_grad=TFT-dim4=96-dim3=64-dim2=64-cpu]`.

Under gdb:

```
Program received signal SIGILL, Illegal instruction.
=> _Z26dequantizeBlockwise8bitCpuIfEvPfPhPKfPT_xx._omp_fn.0+415:
       vinsertf32x4 $0x1,%xmm1,%ymm3,%ymm3
#0  dequantizeBlockwise8bitCpu<float>(...) [clone ._omp_fn.0]
#1  GOMP_parallel ()
#2  cdequantize_blockwise_cpu_fp32 ()      # ctypes, from backends/cpu/ops.py:101
```

`vinsertf32x4` is AVX-512F, but the operands here are ymm/xmm. No `zmm`, no `{%k}` mask. So
`-mprefer-vector-width=256` doesn't prevent it, and a disassembly grep for `%zmm`/`{%k}` misses it
outright; that pattern scored the faulting function as clean on my first pass. The reliable check counts
instructions whose encoding starts with the EVEX prefix `0x62`:
`objdump -d libbitsandbytes_cpu.so | grep -c $'\t62 '`.

Measured that way, the shipped configuration emits 1264 EVEX instructions inside the intentional gated
kernels (`gemv_4bit_inference`, `tinygemm_kernel_nn`) and 130 outside them, spread across
`dequantizeBlockwise8bitCpu<float,bf16_t>._omp_fn.0`,
`dequantizeBlockwise4bitCpu<float,fp16_t,bf16_t>._omp_fn.0`, and the `cdequantize_blockwise_cpu_*`
wrappers. Forcing `HAS_AVX512F_FLAG` off takes both counts to zero and the repro passes.

## Repairs that don't work

- Extending #1901's `push_options` region upward over the dequantize kernels. No change: still 130, still
  SIGILL. These are templates, and their explicit instantiations at `cpu_ops.cpp:922–950` sit outside the
  region, so codegen happens there under the target-wide options. That probably also limits the existing
  Zen3 mitigation wherever a guarded template is instantiated outside its region.
- `__attribute__((target("avx2,fma,no-avx512f")))` on the definitions. Also no change, byte for byte.
  `cpu_ops.h:324–332` declares both templates without the attribute, and adding it only at the definition
  doesn't take.
- Neither touches `cdequantize_blockwise_cpu_*`, which lives in `pythonInterface.cpp:766`, a second TU the
  same flags cover.

Annotation-based scoping would have to be applied across header declarations, definitions and both TUs,
then survive OpenMP outlining on top of that. The `._omp_fn.0` clones hold most of the leaked instructions.

## Suggested fix

Compile the AVX-512 kernels in their own translation unit with the `-mavx512*` flags, via
`set_source_files_properties(... COMPILE_OPTIONS ...)` or a small object library, and leave the rest at
`-mavx2`. That avoids depending on attributes propagating correctly through template instantiation and OMP
outlining. Failing that, a `-DBNB_ENABLE_AVX512=OFF` opt-out would give affected users a supported
source-build path; I verified that configuration builds clean, emits zero EVEX and passes.

The released wheel is not reproducibly affected. `bitsandbytes==0.50.0` passes this test on the same
machine, and I could not fault it across 84 `quantize_4bit`/`dequantize_4bit` combinations (bf16/fp32/fp16
× nf4/fp4 × blocksize 64–4096 × plain and nested). Its 8-bit dequant carries no EVEX. It does carry 20
ungated EVEX instructions in `dequantizeBlockwise4bitCpu<bf16_t/float>._omp_fn.0` which I could not reach,
so I claim no user impact there, but the shipped artifact's safety currently rests on the release
compiler's vectorization choices rather than on anything structural. This is also one machine; I have no
second non-AVX-512 host to confirm on.

CI being green is consistent with that. #1901 hit this on a non-AVX-512 runner back in March, and the
runners' compiler evidently doesn't vectorize these particular loops to EVEX. The exposure is
compiler-version-dependent rather than closed. A build-time assertion that no EVEX appears outside the
gated kernels would catch the class cheaply.

Found while running the CPU test matrix locally against post-0.50.0 `main`. Happy to send the PR for
either fix, though the file split touches enough of `cpu_ops.cpp` that I'd want your preference on layout
first. I have no AVX-512 hardware, so someone would need to check the gated kernels still build and
perform on that side.


## 评论 (4)

### pjordanandrsn · 2026-07-27

Second host, and a smaller repro that drops torch entirely.

i7-12700H (Alder Lake-P, AVX-512 fused off) on WSL2 Ubuntu, `g++ 15.2.0`, upstream `main` at b88ddac
built with the unmodified `build-cpu.sh`. Different microarchitecture and a newer compiler than the
Comet Lake / gcc 14.2 box above, same result: 1268 EVEX instructions in the gated kernels, 128 outside
them, including the same 4 in `dequantizeBlockwise8bitCpu<float>._omp_fn.0`.

The fault needs nothing above the C entry point. No torch, no bitsandbytes Python layer, just the
freshly built shared object:

```python
import ctypes, glob

lib = ctypes.CDLL(glob.glob("bitsandbytes/libbitsandbytes_cpu.so")[0])
f = lib.cdequantize_blockwise_cpu_fp32
f.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_ubyte),
              ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
              ctypes.c_longlong, ctypes.c_longlong]

n, bs = 4096, 64
code   = (ctypes.c_float * 256)(*[i / 255.0 for i in range(256)])
A      = (ctypes.c_ubyte * n)(*[i % 256 for i in range(n)])
absmax = (ctypes.c_float * (n // bs))(*[1.0] * (n // bs))
out    = (ctypes.c_float * n)()

f(code, A, absmax, out, ctypes.c_longlong(bs), ctypes.c_longlong(n))
# Illegal instruction (exit 132)
```

That retires the single-machine caveat in the original report. Two microarchitectures, two compiler
versions, and the smaller repro rules out torch and the dispatch layer as contributors.

gcc 15 emitting it as well is the part I'd weigh: the exposure widens as distro compilers move forward,
so a build that works on the release toolchain today isn't evidence the source tree is safe.

Still no AVX-512 hardware here, so I can't check the other side of a fix (that the gated kernels still
build and perform). That verification would need to come from someone with an Ice Lake, Sapphire Rapids
or Zen 4/5 machine.


### matthewdouglas · 2026-07-28

Hi @pjordanandrsn,

Thanks for the report. So I've definitely been aware of this as a possible issue, and as you note, we try to test on CPUs with AVX512 and without it in CI for this reason.

Long-term my plan has been to move what I can to be compiled into separate TUs, same as what you're proposing here. This would allow removing those `#pragma GCC target` regions and enable shipping with AVX512 optimizations on Windows too. But it's a little bit of work and not the highest priority. It's also a large enough change that I'm not certain that I'm comfortable with taking an external PR for it just yet.

I did try building on GCC 15.2 (arch linux) myself prior to release and must have missed it in my quick check.

So right now, the scope appears limited to:
* Linux x86-64 only, CPU-only usage
* Only CPUs without AVX512 support
* Source build only, with GCC at least >= 12, but only confirmed for >= 14
* Use of 8bit blockwise quantization (i.e. nested absmax in 4bit, optimizers, or direct)

Given this, it is a reasonable workaround at the moment IMO for anyone impacted to just build without the avx512f related flags or consider using our prebuilt wheels.


### pjordanandrsn · 2026-07-28

Correction to my EVEX numbers—the leak is smaller than I reported, and your scope list holds.

I counted "outside the gated kernels" against an allowlist of `gemv_4bit_inference` and
`tinygemm_kernel_nn` only. That missed a third intentional region: the `#if defined(__AVX512F__)` /
`has_avx512f()` branch in `dequantizeBlockwise4bitCpu` (`cpu_ops.cpp:355-397`). 100 of the 128 belong
to it—`vpmovzxbd`/`vpermps`/`vmulps {1to16}` in `._omp_fn.0`, the `set_*_lut()` `vmovaps %zmm` in the
outer function, and the inlined copies in the `cdequantize_blockwise_cpu_{fp4,nf4}_*` wrappers.
Correctly guarded, and it holds up under test.

The actual leak is 28 instructions, all 8-bit:

```
24  dequantizeBlockwise8bitCpu<bf16_t>._omp_fn.0
 4  dequantizeBlockwise8bitCpu<float>._omp_fn.0
 0  dequantizeBlockwise8bitCpu<fp16_t>._omp_fn.0
```

Rebuilt `main` @ 48df490 with the unmodified `build-cpu.sh`, gcc 15.2.0, Alder Lake with AVX-512
fused off, then called every CPU dequant entry point directly over ctypes:

- `cdequantize_blockwise_cpu_fp32` / `_bf16`: SIGILL on all 38 shape×blocksize combinations, at 1 and
  12 OMP threads.
- `cdequantize_blockwise_cpu_fp16`: clean on all 38. No EVEX in that instantiation.
- All six `cdequantize_blockwise_cpu_{fp4,nf4}_{fp32,bf16,fp16}`: clean on 120 combinations each,
  blocksize 32-4096. The scalar fallback clone `._omp_fn.1` carries zero EVEX in all six
  instantiations, so there is nothing there to reach.

So your fourth bullet tightens by one line: 8-bit blockwise, `float` or `bf16_t` output. `fp16` is
unaffected, and 4-bit without nested absmax is unaffected—I had left that as "couldn't reach it",
which implied more doubt than the disassembly warrants.

Two notes on what is left:

The 4-bit branch is safe because gcc kept the LUT materialization under the runtime check, not
because anything makes it. Same class as the 8-bit case, just not firing today.

A build-time assertion is cheaper than I made it sound—three allowlisted regions, and the check is
`grep -c $'\t62 '` per symbol.

Not pushing the TU split; understood that the layout is yours to pick. If the
`-DBNB_ENABLE_AVX512=OFF` opt-out is worth having in the meantime I will send just that, otherwise
happy to leave it here. No rush.


### pjordanandrsn · 2026-07-28

Re-ran the audit on the Comet Lake box from the original report (Xeon W-1250, `g++ (Debian) 14.2.0`),
`main` @ 1f4007e:

```
1394 total = 1264 gemv/tinygemm + 98 guarded 4-bit + 32 leak
```

98 + 32 = 130, exactly the number I reported there—so both counts I published were the guarded 4-bit
branch and the real leak added together. Same two functions and the same dtypes as the other host:
`dequantizeBlockwise8bitCpu<bf16_t>._omp_fn.0` and `<float>._omp_fn.0`, `<fp16_t>` at zero. Only the
size of the bf16 clone moves with the compiler, 28 on gcc 14.2 against 24 on gcc 15.2.

Probes match too: 8-bit `fp32`/`bf16` SIGILL on all 38 shape×blocksize combinations, `fp16` clean,
all six 4-bit entry points clean on 60 each, scalar fallback clones at zero EVEX.

Both hosts in the report decompose the same way now.

