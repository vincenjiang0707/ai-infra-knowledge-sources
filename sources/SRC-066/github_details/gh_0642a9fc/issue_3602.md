# [Issue #3602] [BUG] CuTe DSL: FloatNV8E5M3FNU.to(Float32) returns inf for the entire top exponent binade (codes 248-254)

source: https://github.com/NVIDIA/cutlass/issues/3602
state: open | updated: 2026-09-13T02:46:39Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
Converting a `FloatNV8E5M3FNU` (UE5M3) value to `Float32` returns `inf` for
every code in the top exponent field (`E=31`, codes `248`–`254`), instead of
the finite values `65536.0` … `114688.0`.

UE5M3 is a *finite-only* format: unsigned, 5-bit exponent (bias 15), 3-bit
mantissa, **no infinity encoding**, `0xFF` is the only NaN, and `0xFE` is the
maximum finite value `114688.0`. The decode appears to apply IEEE
`inf`/`NaN` semantics to the top exponent field, which is correct for
`Float8E5M2` but not for this format.

Two things narrow it down:

1. **Encoding is unaffected**, so the round trip is asymmetric —
   `114688.0` → code `254` (correct) → `inf` (wrong).
2. **`Float8E4M3FN` decodes correctly.** That format has the same shape of
   problem — finite-only, NaN living in the top exponent field — and all 256
   of its codes decode exactly. So this looks like an inconsistency in the
   UE5M3 path rather than a deliberate convention.

Sweeping all 256 codes of every 8-bit narrow float the DSL exposes:

| Type | Mismatching codes / 256 |
|---|---|
| **`FloatNV8E5M3FNU`** | **7** (codes 248–254) |
| `Float8E4M3FN` | 0 |
| `Float8E5M2` | 0 (`E=31` genuinely *is* inf/NaN there) |
| `Float8E8M0FNU` | 0 |

**Steps/Code to reproduce bug**
1. Save the script below.
2. Run `python repro.py` on any supported GPU.
3. Observe that codes 248–254 decode to `inf`, while the analogous
   `Float8E4M3FN` codes decode exactly.

```python
import torch
import cutlass
import cutlass.cute as cute
from cutlass.cute.runtime import from_dlpack


@cute.kernel
def decode_kernel(gCodes: cute.Tensor, gUE5M3: cute.Tensor, gE4M3: cute.Tensor):
    t, _, _ = cute.arch.thread_idx()
    if t < 256:
        gUE5M3[t] = gCodes[t].bitcast(cutlass.FloatNV8E5M3FNU).to(cutlass.Float32)
        gE4M3[t] = gCodes[t].bitcast(cutlass.Float8E4M3FN).to(cutlass.Float32)


@cute.jit
def run(a: cute.Tensor, b: cute.Tensor, c: cute.Tensor):
    decode_kernel(a, b, c).launch(grid=[1, 1, 1], block=[256, 1, 1])


# UE5M3: bias 15, 3 mantissa bits, no inf, 0xFF is the only NaN
def expected(code):
    E, M = code >> 3, code & 7
    return 2.0**-14 * (M / 8) if E == 0 else 2.0 ** (E - 15) * (1 + M / 8)


codes = torch.arange(256, dtype=torch.uint8, device="cuda")
ue5m3 = torch.zeros(256, dtype=torch.float32, device="cuda")
e4m3 = torch.zeros(256, dtype=torch.float32, device="cuda")
run(from_dlpack(codes), from_dlpack(ue5m3), from_dlpack(e4m3))
torch.cuda.synchronize()

print(f"{'code':>6} {'expected':>12} {'got':>8}")
for c in range(248, 255):
    print(f"{c:>6} {expected(c):>12.1f} {float(ue5m3[c]):>8}")

print("\nnon-finite codes outside the NaN encoding:")
print("  FloatNV8E5M3FNU ->", [c for c in range(255) if not torch.isfinite(ue5m3[c])])
print("  Float8E4M3FN    ->",
      [c for c in range(256) if (c & 0x7F) != 0x7F and not torch.isfinite(e4m3[c])])
```

**Observed error:**

```
  code     expected      got
   248      65536.0      inf
   249      73728.0      inf
   250      81920.0      inf
   251      90112.0      inf
   252      98304.0      inf
   253     106496.0      inf
   254     114688.0      inf

non-finite codes outside the NaN encoding:
  FloatNV8E5M3FNU -> [248, 249, 250, 251, 252, 253, 254]
  Float8E4M3FN    -> []
```

**Expected behavior**
Codes 248–254 should decode to the finite values 65536.0, 73728.0, 81920.0,
90112.0, 98304.0, 106496.0 and 114688.0 respectively. Only `0xFF` should
produce NaN, and no UE5M3 code should ever produce an infinity.

**Environment details (please complete the following information):**
- GPU: Blackwell+, CUDA 13.4
- CUDA: 13.4 (V13.4.59)
- `nvidia-cutlass-dsl`: 4.8.0.dev0
- Python: 3.12.3
- PyTorch: 2.14.0a0
- OS: Linux 6.17.0 aarch64

**Additional context**
Workaround, in case it helps anyone else — decode by explicit bit
construction instead of `.to()`:

```python
def decode_ue5m3(code):          # code: Uint8
    c = code.to(cutlass.Uint32)
    E = c >> cutlass.Uint32(3)
    M = c & cutlass.Uint32(7)
    # normal: 2^(E-15) * (1 + M/8); fp32 exponent field is (E-15)+127
    bits = ((E + cutlass.Uint32(112)) << cutlass.Uint32(23)) | (M << cutlass.Uint32(20))
    normal = bits.bitcast(cutlass.Float32)
    sub = M.to(cutlass.Float32) * cutlass.Float32(2.0**-17)   # E == 0
    is_norm = (E != cutlass.Uint32(0)).to(cutlass.Float32)
    return normal * is_norm + sub * (cutlass.Float32(1.0) - is_norm)
```

We have not checked whether the 4-bit and 6-bit finite-only types
(`Float4E2M1FN`, `Float6E2M3FN`, `Float6E3M2FN`) have the same issue in their
top binade; they are harder to sweep because they cannot be bitcast from a
`Uint8` directly. Might be worth checking alongside a fix.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3617.
