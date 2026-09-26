# [Issue #2087] [BUG] NF4 Linear4bit wrong on gfx1100 (prebuilt ROCm 6.4 wheel); dequantize correct

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2087
state: open | updated: 2026-09-15T12:48:13Z
labels: 

## 正文

### System Info

- Radeon Pro W7800, gfx1100 (RDNA3); host ROCm 7.13; PyTorch 2.9.1+rocm6.4
- bitsandbytes 0.50.3.dev0 prebuilt wheel; loader uses libbitsandbytes_rocm64.so
- Linear4bit output is unrelated to the reference; quantize/dequantize is correct (~9% error). The fused 4-bit GEMM is wrong, not the quantizer.

### Reproduction

```python
import torch, bitsandbytes as bnb, bitsandbytes.functional as F
torch.manual_seed(0); dev="cuda"; dt=torch.bfloat16
x=torch.randn(8,512,dtype=dt,device=dev); w=torch.randn(256,512,dtype=dt,device=dev)
w4,qs=F.quantize_4bit(w,quant_type="nf4",compress_statistics=True)
print("dequant", ((F.dequantize_4bit(w4,qs)-w).abs().mean()/w.abs().mean()).item())   # ~0.09
q=bnb.nn.Linear4bit(512,256,bias=False,quant_type="nf4",compute_dtype=dt,device="meta")
q.weight=bnb.nn.Params4bit(w,quant_type="nf4",requires_grad=False); q=q.to(dev)
print("linear4bit", ((q(x)-x@w.t()).abs().mean()/(x@w.t()).abs().mean()).item())      # ~1.0
```

### Expected behavior

Expect both errors small (quantization-only, ~0.09); Linear4bit is ~1.0 instead.

Narrowing: prebuilt rocm64 wrong; same tree built with -DCOMPUTE_BACKEND=hip -DBNB_ROCM_ARCH=gfx1100 (ROCm 7.13, clang 23) correct (verified on a 27B NF4 model); gfx1100 is already in the release matrix.

Likely cause: RDNA3-only SIMT path in csrc/gemm_4bit_simt.cu (IS_RDNA3). Disassembly of the prebuilt gfx1100 code object shows a float↔int conversion around the int-typed __builtin_amdgcn_mov_dpp in the warp reduction (v_cvt_i32_f32_dpp truncating); clang 23 emits bit-preserving v_add_f32_dpp. Fix: explicit __float_as_uint/__uint_as_float bitcast there.

CI gap: no ROCm GPU correctness tests.

Workaround: source-build with -DBNB_ROCM_ARCH=gfx1100, or bypass the fused op via dequantize_4bit + F.linear.

Confirm the RDNA3 SIMT reduce path; I'll submit the bitcast fix + a regression test.




Note: this issue was made and written with help of Deepseek V4.1

## 评论 (1)

### liminfei-amd · 2026-09-15

I reproduced this on an RX 7900 GRE (gfx1100) with the supported ROCm 6.4.4
build. ROCm 6.4.4 is still included in the current bitsandbytes build matrix.

NF4 quantization and dequantization are working, but the fused `Linear4bit`
kernel has a `0.125295` relative L1 error compared with a matmul using the same
dequantized weight.

The issue is in the HIP DPP reduction: a `float` is passed directly to the
integer-typed `__builtin_amdgcn_mov_dpp`, so clang 19 emits numeric
float-to-integer and integer-to-float conversions around the DPP move.
Explicit `__float_as_uint` / `__uint_as_float` conversions generate the
expected `v_mov_b32_dpp`.

With that change, the error drops to `0.002051`, and the fused regression tests
pass for fp16, bf16, and fp32 on ROCm 6.4.4. The patched tests also pass with
ROCm 10 / clang 23. This is a compiler-independent correctness fix rather than
a version-specific workaround.

The fix and regression test are available in
https://github.com/bitsandbytes-foundation/bitsandbytes/pull/2089.

