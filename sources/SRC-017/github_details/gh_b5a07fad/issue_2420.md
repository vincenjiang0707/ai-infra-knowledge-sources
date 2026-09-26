# [Issue #2420] NVCC_GENCODE_LDMC_FP8 device-code gencode ignores the caller's NVCC_GENCODE target-arch list, breaking single-arch builds

source: https://github.com/NVIDIA/nccl/issues/2420
state: open | updated: 2026-09-21T17:01:48Z
labels: 

## 正文

## Bug: `NVCC_GENCODE_LDMC_FP8` device-code gencode ignores the caller's `NVCC_GENCODE` target-arch list, breaking single-arch builds

### Environment

- NCCL: 2.29.7-1 (`b91894b`), vendored under PyTorch's `third_party/nccl`
- CUDA Toolkit: 13.4 (also reproduces on 13.3 — the relevant gate is `>= 12.7`)
- Host: aarch64 (GB10 / NVIDIA DGX Spark, compute capability 12.1, `sm_121a`)
- Build invoked with `NVCC_GENCODE=-gencode=arch=compute_121a,code=sm_121a` only (a deliberate single-arch build; `torch_cuda_get_nvcc_gencode_flag()` in PyTorch's `cmake/External/nccl.cmake` correctly derives and passes this)

### Summary

`src/device/Makefile` computes `NVCC_GENCODE_LDMC_FP8` (the gencode used to compile the AllReduce/ReduceScatter `LDMC`-algorithm FP8 symmetric-memory kernels) purely from the CUDA toolkit version:

```makefile
ifeq ($(shell echo "$$((1000*$(CUDA_MAJOR) + 10*$(CUDA_MINOR) >= 12090))"),1)
	NVCC_GENCODE_LDMC_FP8 = -gencode=arch=compute_100f,code=sm_100f
else ifeq ($(shell echo "$$((1000*$(CUDA_MAJOR) + 10*$(CUDA_MINOR) >= 12070))"),1)
  NVCC_GENCODE_LDMC_FP8 = -gencode=arch=compute_100a,code=sm_100a
else
	NVCC_GENCODE_LDMC_FP8 =
endif
```

This is completely independent of the caller-supplied `NVCC_GENCODE` (the actual target-arch list). The result: **any build with CUDA >= 12.7 unconditionally embeds `sm_100f`/`sm_100a` (datacenter-Blackwell, NVSwitch-multicast-only) device code**, even when the build explicitly targets a single non-datacenter arch that can never use multicast hardware at all (GB10/`sm_121a` here — no NVSwitch).

Confirmed via direct evidence, not inference: swept every `.cu.o` built by the surrounding PyTorch build (570 files) for embedded `sm_100` cubins — zero matches anywhere *except* `obj/device/genobj/symmetric/*.o`. `cuobjdump --list-elf` on the final linked `libnccl.so`/`libtorch_cuda.so` shows both `sm_121a` (correctly, our only requested target) and `sm_100`/`sm_100f` (never requested) cubins side by side.

This breaks any downstream tooling that asserts a single-arch build actually is single-arch (our case: a CI/release gate that fails a build if it detects more than the one requested `-gencode` target embedded in the final library — which is exactly what caught this).

### Root cause

`symmetric/generate.py`'s kernel enumeration and `device/Makefile`'s gencode variable are two halves of one coupled contract that isn't kept in sync:

- `required_cuda()` in `generate.py` hardcodes `specific_sms = ["100a", "101a", "100f", "101f", "120a", "121a"]` for these FP8/LDMC kernels — a **runtime dispatch condition** list (which `NCCL_CUDA_ARCH_*_SPECIFIC` branch to take at runtime), used to emit an unconditional dispatch-table entry (and thus an `extern` symbol reference) for the kernel regardless of what's actually compiled.
- `kernel_gencode()` returns the single Makefile variable `$(NVCC_GENCODE_LDMC_FP8)` as the *only* compile-target gencode for every kernel needing it — gated purely on CUDA version, with no reference to the actual requested arch list at all.

So the generator always expects the kernel to exist (for the whole family, `121a` included, regardless of whether this build's `NVCC_GENCODE` actually asked for `121a`-specific device code here), while the Makefile variable that compiles it is independently gated on CUDA toolkit version only.

### What we tried

**Workaround attempted, does NOT work**: gate `NVCC_GENCODE_LDMC_FP8` on `NVCC_GENCODE` also containing `compute_100` (blank it out otherwise, matching the pattern PyTorch's own `cmake/Codegen.cmake`'s `_BUILD_FOR_ADDITIONAL_ARCHS` already uses for similar arch-gating elsewhere):

```makefile
ifneq ($(findstring compute_100,$(NVCC_GENCODE)),)
ifeq ($(shell echo "$$((1000*$(CUDA_MAJOR) + 10*$(CUDA_MINOR) >= 12090))"),1)
	NVCC_GENCODE_LDMC_FP8 = -gencode=arch=compute_100f,code=sm_100f
else ifeq ($(shell echo "$$((1000*$(CUDA_MAJOR) + 10*$(CUDA_MINOR) >= 12070))"),1)
  NVCC_GENCODE_LDMC_FP8 = -gencode=arch=compute_100a,code=sm_100a
else
	NVCC_GENCODE_LDMC_FP8 =
endif
else
	NVCC_GENCODE_LDMC_FP8 =
endif
```

This **compiles cleanly** (no build errors) but **breaks at runtime**: importing PyTorch (which dlopens `libtorch_cuda.so`, which links `libnccl_static.a`) fails with

```
ImportError: .../libtorch_cuda.so: undefined symbol: _Z54ncclSymkDevKernel_AllReduce_RSxLDMC_AGxSTMC_sum_f8e4m321ncclSymkDevWorkArgs4K
```

— because blanking the gencode drops the kernel's *device-code definition*, but `generate.py`'s dispatch table still holds a hard reference to it (since `121a` remains in `specific_sms` regardless of the Makefile-side change). A Makefile-only fix cannot work; the generator side has already committed to the kernel's symbol existing.

### Suggested fix direction — confirmed viable, not just theoretical

Have `NVCC_GENCODE_LDMC_FP8` compile for whatever `NVCC_GENCODE` the caller
actually requested, instead of (or in addition to) the fixed
`sm_100f`/`sm_100a` target. **Confirmed directly** (see minimal
reproduction below): the generated kernel source already has the correct
runtime-dispatch guard for `sm_121a` (`NCCL_CUDA_ARCH_SPECIFIC==1210` is
already one of the listed conditions in the generated `.cu` — see
`required_cuda()`'s `specific_sms` including `"121a"`), and compiling it
with `-gencode=arch=compute_121a,code=sm_121a` **succeeds cleanly** and
produces a real, correctly-defined kernel symbol (not a stub) targeting
only `sm_121a` — not a "multicast instructions are invalid on this arch"
compile failure as one might expect. The only thing standing between the
current behavior and a correct single-arch build is that
`device/Makefile` never actually tries this.

So a fix along these lines should work without needing to touch
`generate.py`'s enumeration/dispatch-table logic at all — just make
`NVCC_GENCODE_LDMC_FP8` reflect the caller's real `NVCC_GENCODE` instead
of a fixed CUDA-version-gated arch:

```makefile
NVCC_GENCODE_LDMC_FP8 = $(NVCC_GENCODE)
```

(or some intersection/subset of it, if there's a reason to exclude some
targets — we didn't find one; every arch in `specific_sms` that we could
test compiled cleanly).

### Reproduction (minimal — one codegen step + two `nvcc` invocations; no `make`, no full NCCL/PyTorch build)

Verified end-to-end on this environment (CUDA 13.4, GCC 14.2, aarch64).
`generate.py` writes generated files directly into the given target
directory (no `symmetric/` subdirectory of its own — that name in the
normal build's paths comes from the Makefile passing a directory already
named `symmetric` as its target):

```
cd nccl/src/device
./symmetric/generate.py /tmp/gensrc   # ~0.03s, no build system needed
```

Then, directly on the one generated file. `-I<BUILDDIR>/include` needs to
point at an `include/` tree already populated by one prior ordinary build
(`make -C .. src.build`, can be interrupted once it starts compiling) --
it resolves a transitive `#include "doca_gpunetio/..."` pulled in via
`nccl_device.h` that's unrelated to this bug but required to compile this
file in isolation at all:

```
# 1. As currently compiled (Makefile's fixed, CUDA-version-only gate):
nvcc -forward-unknown-to-host-compiler -I. -I.. -I<BUILDDIR>/include -I../include -I../include/plugin \
  -DCCCL_DISABLE_PDL -std=c++17 --expt-extended-lambda --expt-relaxed-constexpr \
  -gencode=arch=compute_100f,code=sm_100f \
  -c /tmp/gensrc/reduce_scatter_sum_f8e4m3_LDMC.cu -o test_100f.o
cuobjdump --list-elf test_100f.o
# ELF file 1: test_100f.1.sm_100.cubin   <- embedded regardless of target GPU

# 2. Compiled for the actual target arch instead (what a caller building
#    for GB10/sm_121a only actually wants and asked for via NVCC_GENCODE):
nvcc -forward-unknown-to-host-compiler -I. -I.. -I<BUILDDIR>/include -I../include -I../include/plugin \
  -DCCCL_DISABLE_PDL -std=c++17 --expt-extended-lambda --expt-relaxed-constexpr \
  -gencode=arch=compute_121a,code=sm_121a \
  -c /tmp/gensrc/reduce_scatter_sum_f8e4m3_LDMC.cu -o test_121a.o
cuobjdump --list-elf test_121a.o
# ELF file 1: test_121a.1.sm_121a.cubin  <- compiles cleanly, correct single arch
nm test_121a.o | grep ncclSymkDevKernel_ReduceScatter_LDMC_sum_f8e4m3
# 0000...d1c T _Z47ncclSymkDevKernel_ReduceScatter_LDMC_sum_f8e4m3...  <- real symbol, not a stub
```

Both compiles succeed with no warnings; only the embedded arch differs,
and only invocation 2 matches what the caller actually asked for via
`NVCC_GENCODE`.

(The undefined-symbol failure described above under "What we tried" only
shows up in the *linked, whole-library* context, where `generate.py`'s
dispatch table references every enumerated kernel unconditionally but
the Makefile never compiles a definition for any arch outside
`sm_100f`/`sm_100a` — reproducible via a full `NVCC_GENCODE=... make -C
src build` or a full PyTorch build with `TORCH_CUDA_ARCH_LIST=12.1a`, CUDA
>= 12.7, then `import torch`; omitted here since the two-`nvcc`-command
repro above isolates the actual root cause without needing either.)

---
Assisted-by: Claude


## 评论 (2)

### 0z5a · 2026-09-19

@zbrad I'd be happy to work on this if nobody is already handling it.

Rather than just suppressing NVCC_GENCODE_LDMC_FP8, I'd like to trace the full contract between the caller-supplied NVCC_GENCODE, symmetric/generate.py kernel enumeration, and the generated symbol references.

### besnardjb · 2026-09-21

@zbrad thanks for your detailed report, and @0z5a thank you for your proposed fix. We are looking into it on our side and will report promptly.
