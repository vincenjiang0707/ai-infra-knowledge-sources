# [Issue #3673] [BUG] Order-dependent wrong rmem values on Windows SM120 with CuTe DSL 4.8 CUDA12 stack; CUDA13 control passes

source: https://github.com/NVIDIA/cutlass/issues/3673
state: open | updated: 2026-09-24T22:21:19Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**

A standalone CuTe DSL reproducer produces deterministic incorrect packed values on an RTX 5090 (SM120) under the tested Windows CUDA12 stack.

The same source and input produce correct results when:

- the four-element rmem tensor is replaced with independent scalar values;
- the same Windows RTX 5090 is tested with the CUDA13 stack; or
- the reproducer is run on the Linux SM121 control system.

Reversing the evaluation order also moves the corruption from the first component to the second component.

This behavior appears consistent with an SSA/liveness/code-generation issue, but I have not identified the exact failing compiler stage.

I am not claiming that this is specifically a register allocator, NVVM, or SM120 hardware bug.


**Steps/Code to reproduce bug**

The attached `repro.py` is standalone.

It does not require DS41RT, SparkInfer, a model, model weights, or an external fixture.

Run:

```text
python repro.py --variant rmem --output out-rmem
python repro.py --variant scalar --output out-scalar
python repro.py --variant reverse --output out-reverse
python repro.py --variant snapshot --output out-snapshot
```

Each variant tests 16 split positions with 3 repeats per position.

The script exits successfully after collecting results even when a numerical mismatch is found. Use the `passed` value in `report.json` or stdout to determine correctness.

Windows RTX 5090 / SM120 results:

| Stack | Compiler pipeline | rmem | scalar | reverse | snapshot |
|---|---|---:|---:|---:|---:|
| Torch 2.11.0+cu128, CuTe CUDA12.9 backend | legacy | FAIL | PASS | FAIL | PASS |
| Torch 2.11.0+cu128, CuTe CUDA12.9 backend | extension | FAIL | PASS | FAIL | PASS |
| Torch 2.11.0+cu130, CuTe CUDA13.4 backend | legacy | PASS | PASS | PASS | PASS |

Linux GB10 / SM121 / CuTe DSL 4.8.0 / CUDA13.2 passes all four variants.

With the normal rmem variant:

```text
part0 -> part1
corruption: part0 side
```

With reversed evaluation order:

```text
part1 -> part0
corruption: part1 side
```

Replacing the rmem tensor with four independent `Uint32` scalar variables removes the failure.

Adding snapshot stores also suppresses the failure.


**Expected behavior**

For the `rmem` variant at split 0, output index 0:

```text
Expected:          0x3f803f82
Windows CUDA12:    0x3c003c45
Windows CUDA13:    0x3f803f82
Windows scalar:    0x3f803f82
Linux control:     0x3f803f82
```

The CUDA12 result is deterministic across all 3 repeats.

CUDA12 rmem mismatch counts across split 0..15:

```text
[28, 28, 28, 28, 28, 28, 28, 28, 28, 24, 20, 16, 12, 8, 4, 0]
```

Reverse-order mismatch counts:

```text
[31, 27, 23, 19, 15, 11, 7, 3, 0, 0, 0, 0, 0, 0, 0, 0]
```


**Environment details (please complete the following information):**

- Environment location: Bare-metal

Failing CUDA12 stack:

```text
OS: Windows 11 x86-64
GPU: NVIDIA GeForce RTX 5090
Compute capability: SM120
Driver: 591.86
Python: 3.13.5
PyTorch: 2.11.0+cu128
torch CUDA: 12.8
nvidia-cutlass-dsl: 4.8.0
cuda-bindings: 12.9.8

CuTe native module:
_cutlass_ir.cu12.cp313-win_amd64.pyd

CuTe runtime:
cu12/lib/cute_dsl_runtime.dll
```

Passing CUDA13 stack:

```text
OS: Windows 11 x86-64
GPU: NVIDIA GeForce RTX 5090
Compute capability: SM120
Driver: 591.86
Python: 3.13.5
PyTorch: 2.11.0+cu130
torch CUDA: 13.0
nvidia-cutlass-dsl: 4.8.0
cuda-bindings: 13.2.0

CuTe backend reports CUDA 13.4

CuTe native module:
_cutlass_ir.cu13.cp313-win_amd64.pyd

CuTe runtime:
cu13/lib/cute_dsl_runtime.dll
```

The system `CUDA_PATH` remains pointed at the existing CUDA 12.8 toolkit in both cases. The loaded CuTe native module/runtime was checked explicitly, so the CUDA13 result is not inferred from `CUDA_PATH`.

The CUDA12 -> CUDA13 comparison changes several components of the CUDA package stack together. Therefore this comparison does not establish which individual component or compiler pass is responsible.

Linux control:

```text
OS: Linux aarch64
GPU: NVIDIA GB10
Compute capability: SM121
Driver: 580.142
CUDA: 13.2
CuTe DSL: 4.8.0
PyTorch: 2.12.0a0 NVIDIA build
cuda-bindings: 13.2.0
```


**Additional context**

- A simple `Uint32` load-only helper does not reproduce the problem.
- Restoring half2 unpack and BF16 packing makes the failure reproducible again on the CUDA12 stack.
- FP4 decoding is not required.
- MMA is not required.
- Multiple tiles are not required.
- `vote_ballot_sync` is not required.
- One warp is sufficient.
- The generated kernel source is identical across the compared Windows CUDA12/CUDA13 runs.
- CUDA12 legacy and extension compiler pipelines both reproduce the failure.
- CUDA13 legacy passes both with and without the host-side compiler-routing observer.

This reproducer demonstrates a standalone CuTe DSL numerical correctness failure with the tested Windows CUDA12 stack.

It does not establish whether the root cause is in CuTe DSL lowering, shared MLIR/LLVM lowering, the CUDA12 NVVM/backend, the CuTe CUDA12 native library/runtime, or another interaction within the tested CUDA12 stack.

I have not tested Linux SM120, the CUDA13 extension compiler pipeline, or a main-branch-built CuTe DSL package.

The latest published CUTLASS/CuTe DSL package I found at the time of testing is 4.8.0.

I also checked related CUTLASS issues involving rmem/SSA/code-generation problems, but I did not find an existing report matching this deterministic order-dependent behavior.

Source attribution: the in-file helper/kernel template was adapted from SparkInfer commit `4b0954148523b5a2e93813f963d483ffd350b9c9`, specifically `b12x/_lib/intrinsics.py` and `b12x/attention/dsa_indexer/_v41_overlay.py`. Copyright (c) 2025 by the b12x authors. Those portions are licensed under Apache-2.0.

[repro.py](https://github.com/user-attachments/files/32609246/repro.py)

## 评论 (1)

### yunweili3 · 2026-09-24

Reproduced on **Linux + B200 (`sm_100a`)** too, so this is not Windows-specific. The root cause is **ptxas 12.9**, not CuTe DSL:

- cu12 and cu13 generate identical MLIR and PTX; only `.version` differs. The cu12 cubin is built by ptxas **12.9.83**, the cu13 one by **13.4.59**.
- The same PTX fails with ptxas 12.9 at `-O1`/`-O2`/`-O3`, and passes at `-O0` and with ptxas 13.x.
- In the SASS, ptxas 12.9 loads a later value into the register that still holds `a[0]`/`a[2]`, which is why only the part-0 slots are corrupted.

**Minimal standalone PTX** (no DSL). `k(out, in, c)` with `c = 0`, `in[0] = 0x11`, `in[4] = 0x45`, 1 thread:

| ptxas | `out[0]` |
|---|---|
| 13.2 `-O3`, 12.9 `-O0` | `0x82` (correct) |
| 12.9.86 `-O1`/`-O2`/`-O3` | **`0x45`**, the raw `in[4]` byte |

```
ptxas -arch=sm_100a -O3 repro_3673.ptx -o k.cubin && python run_3673.py k.cubin
```

<details><summary>repro_3673.ptx (sm_100a)</summary>

```ptx
// Minimal repro for NVIDIA/cutlass#3673: ptxas 12.9 miscompile at -O1 and above.
// k(out, in, c) with c = 0, in[0] = 0x11, in[4] = 0x45: expected out[0] = 0x82 (low byte of a0).
//   ptxas 13.x -O3 / 12.9 -O0 : correct
//   ptxas 12.9.x -O1..-O3      : wrong (register holding a0 is reused for a later load)
.version 8.8
.target sm_100a
.address_size 64
.visible .entry k(.param .u64 pout, .param .u64 pin, .param .u32 pc)
{
	.reg .pred 	%p<3>;
	.reg .b32 	%r<39>;
	.reg .b64 	%rd<13>;
	ld.param.u64 	%rd1, [pout];
	ld.param.u64 	%rd2, [pin];
	ld.param.u32 	%r1, [pc];
	shl.b32 	%r2, %r1, 6;
	cvt.s64.s32 	%rd3, %r2;
	mov.b64 	%rd4, 0;
	cvt.u32.u64 	%r3, %rd3;
	mov.b64 	%rd5, 0;
	mov.b64 	%rd6, 0;
	setp.lt.s64 	%p1, %rd3, %rd4;
	@%p1 bra 	P0_ZERO;
	mov.b64 	%rd7, 0;
	mov.b64 	%rd8, 0;
	or.b64 	%rd9, %rd7, %rd8;
	add.s64 	%rd10, %rd2, %rd9;
	ld.global.b8 	%r4, [%rd10];
	or.b32 	%r5, %r4, 1006648320;
        {
            .reg .b16 lo, hi;
            mov.b32 {lo, hi}, %r5;
            cvt.f32.f16 %r6, lo;
            cvt.f32.f16 %r7, hi;
        }
	{ .reg .b16 t; cvt.rn.bf16.f32 t, %r6; cvt.u32.u16 %r8, t; }
	{ .reg .b16 t; cvt.rn.bf16.f32 t, %r7; cvt.u32.u16 %r9, t; }
	shl.b32 	%r10, %r9, 16;
	or.b32 	%r11, %r10, %r8;
	ld.global.b8 	%r12, [%rd10+4];
	or.b32 	%r13, %r12, 1006648320;
        {
            .reg .b16 lo, hi;
            mov.b32 {lo, hi}, %r13;
            cvt.f32.f16 %r14, lo;
            cvt.f32.f16 %r15, hi;
        }
	{ .reg .b16 t; cvt.rn.bf16.f32 t, %r14; cvt.u32.u16 %r16, t; }
	{ .reg .b16 t; cvt.rn.bf16.f32 t, %r15; cvt.u32.u16 %r17, t; }
	shl.b32 	%r18, %r17, 16;
	or.b32 	%r19, %r18, %r16;
	mov.b32 	%r20, 0;
	mov.b64 	%rd6, {%r19, %r20};
	mov.b64 	%rd5, {%r11, %r20};
	bra.uni 	P1;
P0_ZERO:
	mov.b64 	%rd6, 0;
	mov.b64 	%rd5, 0;
P1:
	setp.gt.s32 	%p2, %r3, 6;
	@%p2 bra 	DONE;
	mov.b64 	%rd11, %rd2;
	ld.global.b8 	%r21, [%rd11];
	or.b32 	%r22, %r21, 1006648320;
        {
            .reg .b16 lo, hi;
            mov.b32 {lo, hi}, %r22;
            cvt.f32.f16 %r23, lo;
            cvt.f32.f16 %r24, hi;
        }
	{ .reg .b16 t; cvt.rn.bf16.f32 t, %r23; cvt.u32.u16 %r25, t; }
	mov.b64 	{%r26, _}, %rd5;
	mov.b64 	%rd5, {%r26, %r25};
	ld.global.b8 	%r27, [%rd11+4];
	or.b32 	%r28, %r27, 1006648320;
        {
            .reg .b16 lo, hi;
            mov.b32 {lo, hi}, %r28;
            cvt.f32.f16 %r29, lo;
            cvt.f32.f16 %r30, hi;
        }
	{ .reg .b16 t; cvt.rn.bf16.f32 t, %r30; cvt.u32.u16 %r31, t; }
	shl.b32 	%r32, %r31, 16;
	mov.b64 	{%r33, _}, %rd6;
	mov.b64 	%rd6, {%r33, %r32};
DONE:
	mov.b64 	{%r34, %r35}, %rd5;
	mov.b64 	%rd12, %rd1;
	st.global.b8 	[%rd12], %r34;
	st.global.b8 	[%rd12+4], %r35;
	mov.b64 	{%r36, %r37}, %rd6;
	shr.u32 	%r38, %r37, 16;
	st.global.b8 	[%rd12+14], %r38;
	ret;
}
```
</details>

<details><summary>run_3673.py (cuda-python only)</summary>

```python
# usage: ptxas -arch=sm_100a -O3 repro_3673.ptx -o k.cubin && python run_3673.py k.cubin
import ctypes, sys
import numpy as np
from cuda.bindings import driver as cu

def ok(r):
    assert r[0] == cu.CUresult.CUDA_SUCCESS, r[0]
    return r[1] if len(r) == 2 else r[1:]

ok(cu.cuInit(0)); ok(cu.cuCtxSetCurrent(ok(cu.cuDevicePrimaryCtxRetain(ok(cu.cuDeviceGet(0))))))
fn = ok(cu.cuModuleGetFunction(ok(cu.cuModuleLoadData(open(sys.argv[1], "rb").read())), b"k"))
inp = np.zeros(64, np.uint8); inp[0], inp[4] = 0x11, 0x45
d_in, d_out = ok(cu.cuMemAlloc(64)), ok(cu.cuMemAlloc(16))
ok(cu.cuMemcpyHtoD(d_in, inp.ctypes.data, 64)); ok(cu.cuMemsetD8(d_out, 0, 16))
args = [ctypes.c_uint64(int(d_out)), ctypes.c_uint64(int(d_in)), ctypes.c_uint32(0)]
argv = (ctypes.c_void_p * 3)(*[ctypes.addressof(a) for a in args])
ok(cu.cuLaunchKernel(fn, 1, 1, 1, 1, 1, 1, 0, 0, argv, 0)); ok(cu.cuCtxSynchronize())
out = np.zeros(16, np.uint8); ok(cu.cuMemcpyDtoH(out.ctypes.data, d_out, 16))
print(f"out[0] = 0x{out[0]:02x}  (expected 0x82) ->", "OK" if out[0] == 0x82 else "WRONG")
```
</details>

For `sm_90a`, the 12.9 SASS shows the same register clobber (not run: no H100 here). On `sm_120a` this reduced kernel happens not to trigger, while the full repro does.

**Workarounds:** use the CUDA 13 build (`pip install "nvidia-cutlass-dsl[cu13]"`), or compile with `options="--ptxas-options=-O0"` (slower).

