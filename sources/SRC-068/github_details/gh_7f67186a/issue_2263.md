# [Issue #2263] [Question] Numerics of e2e

source: https://github.com/Dao-AILab/flash-attention/issues/2263
state: closed | updated: 2026-07-28T18:32:19Z
labels: 

## 正文

Hi. Potentially a very noob question: Is there a way to verify if the exp2 emulation is bitwise equivalent? i.e., is it 100% safe to use?

I saw in https://github.com/Dao-AILab/flash-attention/issues/2081#issuecomment-3864743891 that it should be safe for BF16 outputs. But I ran a small repro, and the BF16 outputs can be off by **1 ULP**. Potentially I messed up some fma. 


```
import torch
import cutlass
import cutlass.cute as cute
from cutlass import Float32, Int32
from cutlass._mlir.dialects import llvm
from cutlass.cute.runtime import from_dlpack
from cutlass.cutlass_dsl import dsl_user_op, T
from typing import Tuple


# ---------------------------------------------------------------------------
# Exact copies from flash_attn/cute/utils.py
# ---------------------------------------------------------------------------

@dsl_user_op
@cute.jit
def evaluate_polynomial(
    x: Float32, poly: Tuple[Float32, ...], *, loc=None, ip=None
) -> Float32:
    deg = len(poly) - 1
    out = poly[deg]
    for i in cutlass.range_constexpr(deg - 1, -1, -1):
        out = out * x + poly[i]
    return out


@dsl_user_op
def add_round_down(
    x: float | Float32, y: float | Float32, *, loc=None, ip=None
) -> Float32:
    return cutlass.Float32(
        llvm.inline_asm(
            T.f32(),
            [Float32(x).ir_value(loc=loc, ip=ip), Float32(y).ir_value(loc=loc, ip=ip)],
            "add.rm.ftz.f32 $0, $1, $2;",
            "=f,f,f",
            has_side_effects=False,
            is_align_stack=False,
            asm_dialect=llvm.AsmDialect.AD_ATT,
        )
    )


@dsl_user_op
def combine_int_frac_ex2(
    x_rounded: Float32, frac_ex2: Float32, *, loc=None, ip=None
) -> Float32:
    return cutlass.Float32(
        llvm.inline_asm(
            T.f32(),
            [
                Float32(x_rounded).ir_value(loc=loc, ip=ip),
                Float32(frac_ex2).ir_value(loc=loc, ip=ip),
            ],
            "{\n\t"
            ".reg .s32 x_rounded_i, frac_ex_i, x_rounded_e, out_i;\n\t"
            "mov.b32 x_rounded_i, $1;\n\t"
            "mov.b32 frac_ex_i, $2;\n\t"
            "shl.b32 x_rounded_e, x_rounded_i, 23;\n\t"
            "add.s32 out_i, x_rounded_e, frac_ex_i;\n\t"
            "mov.b32 $0, out_i;\n\t"
            "}\n",
            "=f,f,f",
            has_side_effects=False,
            is_align_stack=False,
            asm_dialect=llvm.AsmDialect.AD_ATT,
        )
    )


@dsl_user_op
def ex2_emulation(x: Float32, *, loc=None, ip=None) -> Float32:
    # We assume x <= 127.0
    poly_ex2_deg3 = (
        1.0,
        0.695146143436431884765625,
        0.227564394474029541015625,
        0.077119089663028717041015625,
    )
    fp32_round_int = float(2**23 + 2**22)
    x_clamped = cute.arch.fmax(x, -127.0)
    # We want to round down here, so that the fractional part is in [0, 1)
    x_rounded = add_round_down(x_clamped, fp32_round_int, loc=loc, ip=ip)
    # The integer floor of x is now in the last 8 bits of x_rounded
    # We assume the next 2 ops round to nearest even. The rounding mode is important.
    x_rounded_back = x_rounded - fp32_round_int
    x_frac = x_clamped - x_rounded_back
    x_frac_ex2 = evaluate_polynomial(x_frac, poly_ex2_deg3, loc=loc, ip=ip)
    return combine_int_frac_ex2(x_rounded, x_frac_ex2, loc=loc, ip=ip)


# ---------------------------------------------------------------------------
# Kernel
# ---------------------------------------------------------------------------

class Exp2CompareKernel:
    @cute.kernel
    def run(self, inp: cute.Tensor, hw: cute.Tensor, emu: cute.Tensor, n: Int32):
        i = cute.arch.block_idx()[0] * 128 + cute.arch.thread_idx()[0]
        if i < n:
            x = inp[i]
            hw[i] = cute.arch.exp2(x)
            emu[i] = ex2_emulation(x)

    @cute.jit
    def __call__(self, inp: cute.Tensor, hw: cute.Tensor, emu: cute.Tensor, n: Int32):
        self.run(inp, hw, emu, n).launch(
            grid=(cute.ceil_div(n, 128), 1, 1), block=[128, 1, 1])


# ---------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------

def test_range(kern, name, inp):
    n = inp.numel()
    hw, emu = torch.empty_like(inp), torch.empty_like(inp)
    kern(from_dlpack(inp), from_dlpack(hw), from_dlpack(emu), n)
    torch.cuda.synchronize()

    hw_bf16 = hw.to(torch.bfloat16)
    emu_bf16 = emu.to(torch.bfloat16)
    hw_b = hw_bf16.view(torch.int16)
    emu_b = emu_bf16.view(torch.int16)
    mismatches = hw_b != emu_b
    mm = mismatches.sum().item()

    fp32_hw_b = hw.view(torch.int32)
    fp32_emu_b = emu.view(torch.int32)
    fp32_ulp = (fp32_hw_b.long() - fp32_emu_b.long()).abs().max().item()

    print(f"  {name} (n={n}):")
    print(f"    FP32 max ULP: {fp32_ulp}")
    print(f"    BF16: {mm}/{n} mismatch ({100*mm/n:.2f}%)", end="")
    if mm > 0:
        ulp = (hw_b[mismatches].long() - emu_b[mismatches].long()).abs()
        print(f", all off by {ulp.max().item()} BF16 ULP")
        idxs = mismatches.nonzero(as_tuple=True)[0][:5]
        for idx in idxs:
            i = idx.item()
            print(f"      x={inp[i].item():>12.6f}  "
                  f"hw_f32=0x{fp32_hw_b[i].item():08X} -> bf16=0x{hw_b[i].item() & 0xFFFF:04X}  "
                  f"emu_f32=0x{fp32_emu_b[i].item():08X} -> bf16=0x{emu_b[i].item() & 0xFFFF:04X}")
    else:
        print(" (bitwise identical)")


if __name__ == "__main__":
    gpu = torch.cuda.get_device_name(0)
    cc = torch.cuda.get_device_capability(0)
    print(f"GPU: {gpu} (SM {cc[0]}{cc[1]})")
    print()
    print("ex2_emulation (degree-3 poly) vs hardware ex2.approx, output at BF16")
    print("=" * 72)

    kern = Exp2CompareKernel()
    test_range(kern, "[-20, 0)", torch.empty(1_000_000, device="cuda").uniform_(-20.0, 0.0))
    test_range(kern, "[-10, 0)", torch.empty(1_000_000, device="cuda").uniform_(-10.0, 0.0))
    test_range(kern, "[-1, 0)", torch.empty(1_000_000, device="cuda").uniform_(-1.0, 0.0))
    test_range(kern, "[0, 1)", torch.empty(1_000_000, device="cuda").uniform_(0.0, 1.0))
    test_range(kern, "integers", torch.arange(-20, 1, device="cuda", dtype=torch.float32))
```

# outputs
```
GPU: NVIDIA GB200 (SM 100)

ex2_emulation (degree-3 poly) vs hardware ex2.approx, output at BF16
========================================================================
  [-20, 0) (n=1000000):
    FP32 max ULP: 1428
    BF16: 10060/1000000 mismatch (1.01%), all off by 1 BF16 ULP
      x=  -10.221991  hw_f32=0x3A5B7D5C -> bf16=0x3A5B  emu_f32=0x3A5B8197 -> bf16=0x3A5C
      x=  -12.691620  hw_f32=0x391E8128 -> bf16=0x391F  emu_f32=0x391E7FB1 -> bf16=0x391E
      x=  -12.472450  hw_f32=0x39388261 -> bf16=0x3939  emu_f32=0x39387F25 -> bf16=0x3938
      x=   -5.655628  hw_f32=0x3CA2822F -> bf16=0x3CA3  emu_f32=0x3CA27FD0 -> bf16=0x3CA2
      x=  -18.084177  hw_f32=0x36717D95 -> bf16=0x3671  emu_f32=0x3671807E -> bf16=0x3672
  [-10, 0) (n=1000000):
    FP32 max ULP: 1428
    BF16: 9892/1000000 mismatch (0.99%), all off by 1 BF16 ULP
      x=   -5.785695  hw_f32=0x3C947FA3 -> bf16=0x3C94  emu_f32=0x3C9480E8 -> bf16=0x3C95
      x=   -4.114324  hw_f32=0x3D6C7F28 -> bf16=0x3D6C  emu_f32=0x3D6C8360 -> bf16=0x3D6D
      x=   -7.132768  hw_f32=0x3BE97E0E -> bf16=0x3BE9  emu_f32=0x3BE982BA -> bf16=0x3BEA
      x=   -8.411281  hw_f32=0x3B408029 -> bf16=0x3B41  emu_f32=0x3B407E45 -> bf16=0x3B40
      x=   -1.776008  hw_f32=0x3E957FBE -> bf16=0x3E95  emu_f32=0x3E9580BD -> bf16=0x3E96
  [-1, 0) (n=1000000):
    FP32 max ULP: 1429
    BF16: 10052/1000000 mismatch (1.01%), all off by 1 BF16 ULP
      x=   -0.603303  hw_f32=0x3F2882C1 -> bf16=0x3F29  emu_f32=0x3F287F68 -> bf16=0x3F28
      x=   -0.221923  hw_f32=0x3F5B7FFC -> bf16=0x3F5B  emu_f32=0x3F5B8436 -> bf16=0x3F5C
      x=   -0.248459  hw_f32=0x3F577FE0 -> bf16=0x3F57  emu_f32=0x3F578369 -> bf16=0x3F58
      x=   -0.189529  hw_f32=0x3F607BFA -> bf16=0x3F60  emu_f32=0x3F6080C6 -> bf16=0x3F61
      x=   -0.536379  hw_f32=0x3F308304 -> bf16=0x3F31  emu_f32=0x3F307F3D -> bf16=0x3F30
  [0, 1) (n=1000000):
    FP32 max ULP: 1429
    BF16: 10148/1000000 mismatch (1.01%), all off by 1 BF16 ULP
      x=    0.791107  hw_f32=0x3FDD7DCF -> bf16=0x3FDD  emu_f32=0x3FDD824E -> bf16=0x3FDE
      x=    0.103163  hw_f32=0x3F897CF8 -> bf16=0x3F89  emu_f32=0x3F89800D -> bf16=0x3F8A
      x=    0.060684  hw_f32=0x3F857FB7 -> bf16=0x3F85  emu_f32=0x3F858251 -> bf16=0x3F86
      x=    0.134344  hw_f32=0x3F8C7DF3 -> bf16=0x3F8C  emu_f32=0x3F8C80DF -> bf16=0x3F8D
      x=    0.784531  hw_f32=0x3FDC7BF4 -> bf16=0x3FDC  emu_f32=0x3FDC8052 -> bf16=0x3FDD
  integers (n=21):
    FP32 max ULP: 0
    BF16: 0/21 mismatch (0.00%) (bitwise identical)
```

cc @v0i0 

## 评论 (7)

### tridao · 2026-02-19

It's certainly not bitwise equivalent, that's not our goal (and we don't know the details of how ex2 instruction works in hardware). Can you compare both ex2 and ex2_emulation vs a reference output in fp64?

For ex2 can you use `cute.arch.exp2(x, fastmath=True)` instead? That corresponds to the `ex2` instruction in ptx.

### henrylhtsang · 2026-02-19

> It's certainly not bitwise equivalent, that's not our goal (and we don't know the details of how ex2 instruction works in hardware). Can you compare both ex2 and ex2_emulation vs a reference output in fp64?
> 
> For ex2 can you use `cute.arch.exp2(x, fastmath=True)` instead? That corresponds to the `ex2` instruction in ptx.

Thanks for the reply! Comparing to fp64 reference, it seems that:
* hardware impl `cute.math.exp2(x, fastmath=True)` is off on < 0.001% of cases 
* ex2_emulation is wrong on ~1% of the cases. But when wrong, it is off by at most 1 BF16 ULP.

### tridao · 2026-02-28

The ~1% BF16 ULP mismatch rate sounds nontrivial but the actual numerical error is small. Here's a comparison of BF16 output error against the true FP64 2^x reference, measured on 4M random inputs in [0, 1):

| Method             | Max abs err | Max rel err | Mean rel err | BF16 mismatch vs hw |
|-------------------|------------:|------------:|-------------:|--------------------:|
| Ideal (FP64→BF16) | 3.906e-3    | —           | —            | —                   |
| hw ex2.approx     | 3.906e-3    | 3.891e-3    | 1.409e-3     |                    |
| deg3 (original)   | 4.064e-3    | 3.902e-3    | 1.410e-3     | 1.008%     |
| deg3 (tuned)      | 4.230e-3    | 3.903e-3    | 1.410e-3     | 0.878%     |
| deg4              | 3.912e-3    | 3.892e-3    | 1.409e-3     | 0.033%      |

The dominant error is BF16 quantization itself (~3.9e-3). The degree-3 polynomial adds only ~0.16e-3 on top of that. The "1% mismatch" means 1% of values land close enough to a BF16 rounding boundary that the polynomial's FP32 error nudges them to the adjacent BF16 value — but adjacent BF16 values differ by only 1 part in 128, so the actual error is negligible. The max/mean relative errors are virtually identical across all methods.

We also searched for better degree-3 coefficients (tuned to minimize BF16 mismatches against hardware on GPU, preserving exact FMA rounding behavior). This reduces mismatches from 1.008% to 0.878% with no extra compute:
  1.0, 0.6953951120376587, 0.22727741301059723, 0.07698985189199448

For cases where bitwise agreement with hardware matters, we have a degree-4 polynomial that gets it down to 0.03% at the cost of one extra FMA:
  1 + x * (0.693042695522308349609375 + x * (0.2412912547588348388671875 + x * (5.2225358784198760986328125e-2 + x * 1.3434938155114650726318359375e-2)))

We might try deg4 to see how much perf drop. 

### tridao · 2026-02-28

Did some quick test, going from deg 3 -> deg 4 causes 1-2% perf drop. Maybe it's ok

### tridao · 2026-03-03

I've added degree 5 as well, perf drop is not too bad (1-2%). Degree 5 matches the accuracy of `ex2.approx` for fp32. I still think if you're gonna quantize the output to bf16, degree 3 is sufficient (since the error from quantization is much larger than the error from emulation).
But if you're very concerned, you can use degree 5, or disable ex2 emulation.

### henrylhtsang · 2026-03-05

Thanks a lot of the reply. Good to close.

Though personally I am more concerned with changing the numerics (which can happen if we disable e2e, or tune the e2e configs), then the numerics degradation (if any) from using e2e.

### tridao · 2026-03-05

Feel free to disable e2e. There's a bit of perf hit but it's not as severe as before. We've made improvements in the kernel so e2e isnt' as essential as before.
