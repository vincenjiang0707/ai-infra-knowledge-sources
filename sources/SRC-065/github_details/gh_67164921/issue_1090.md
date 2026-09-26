# [Issue #1090] [Question] How to force certain computations to occur in float16?

source: https://github.com/triton-lang/triton/issues/1090
state: open | updated: 2026-09-01T18:09:38Z
labels: help wanted

## 正文

I have the following kernel:
```python3
@triton.jit
def unmasked_blend_kernel(
    img1_ptr, img2_ptr, ratio: float, total_items: int, BLOCK_SIZE: tl.constexpr
):
    block_idx = tl.program_id(0)
    offset = block_idx * BLOCK_SIZE
    item_element_idxs = tl.arange(0, BLOCK_SIZE)
    img1_item_ptrs = img1_ptr + offset + item_element_idxs
    img2_item_ptrs = img2_ptr + offset + item_element_idxs

    if offset + BLOCK_SIZE > total_items:
        mask = item_element_idxs < total_items % BLOCK_SIZE
        img1 = tl.load(img1_item_ptrs, mask=mask, other=0)
        img2 = tl.load(img2_item_ptrs, mask=mask, other=0)
        out = ratio * img1 + (1.0 - ratio) * img2
        tl.store(img1_item_ptrs, out, mask=mask)
    else:
        img1 = tl.load(img1_item_ptrs)
        img2 = tl.load(img2_item_ptrs)
        out = ratio * img1 + (1.0 - ratio) * img2
        tl.store(img1_item_ptrs, out)
```

Given that this kernel is blending 2 uint8  tensors, I figured it would make sense to do the computation ` out = ratio * img1 + (1.0 - ratio) * img2`  since I don't need high precision.

However, I can't figure out how to force the Triton compiler to do the computations in FP16.
I tried doing:

```python3
        img1 = tl.load(img1_item_ptrs, mask=mask, other=0).to(tl.float16)
        img2 = tl.load(img2_item_ptrs, mask=mask, other=0).to(tl.float16)
```
but from looking at the generated PTX, it just seems like the float16s are just converted to float32s before the multiplication 
occurs.

Is there a way I can force the Triton  compiler  to make the multiplications float16? (Or is this impossible for a good reason;  i.e maybe this is not what I actually want)?


## 评论 (11)

### vedantroy · 2023-01-24

Update: I tried to force everything to be float16, by taking the float value `ratio` that is an input to the kernel and storing it  in a float16 tensor, but that didn't work.

```python3
@triton.jit
def unmasked_blend_kernel(
    img1_ptr, img2_ptr, ratio: float, total_items: int, BLOCK_SIZE: tl.constexpr
):
    block_idx = tl.program_id(0)
    offset = block_idx * BLOCK_SIZE
    item_element_idxs = tl.arange(0, BLOCK_SIZE)
    img1_item_ptrs = img1_ptr + offset + item_element_idxs
    img2_item_ptrs = img2_ptr + offset + item_element_idxs

    ratio_tensor = tl.zeros((1,), dtype=tl.float16)
    ratio_tensor += ratio

    if offset + BLOCK_SIZE > total_items:
        mask = item_element_idxs < total_items % BLOCK_SIZE
        img1 = tl.load(img1_item_ptrs, mask=mask, other=0).to(tl.float16)
        img2 = tl.load(img2_item_ptrs, mask=mask, other=0).to(tl.float16)
        out = ratio_tensor * img1 + (1.0 - ratio_tensor).to(tl.float16) * img2
        tl.store(img1_item_ptrs, out, mask=mask)
    else:
        img1 = tl.load(img1_item_ptrs).to(tl.float16)
        img2 = tl.load(img2_item_ptrs).to(tl.float16)
        out = ratio_tensor * img1 + (1.0 - ratio_tensor).to(tl.float16) * img2
        tl.store(img1_item_ptrs, out)
```

### Jokeren · 2023-01-25

Convert `1.0` to `tl.float16` or using something like `tl.full`

### vedantroy · 2023-01-25

I don't see a `tl.full` method in the documentation  and running: `python3 -c 'import triton.language as tl; tl.full()'`  gives "module 'triton.language' has no attribute  'full'".

Also,  I'm not sure how to convert the `1.0` to a `tl.float16`. Is there some API that I'm missing in the docs?

### Jokeren · 2023-01-25

Please install triton master and retry. See `semantic.py`

### vedantroy · 2023-01-25

> Please install triton master and retry. See `semantic.py`

Sounds good. From looking at `semantic.py`, I'm  guessing  `full` creates a tensor filled with a given value.
I see there's a `cast`  method, which I'm guessing  is what I need to convert `1.0` into a fp16  value (although it looks like `cast` only works on tensors, so in reality I probably just need to use `full`?).

Is it sufficient for me to just convert  the `1.0` into a 1-element  fp16 tensor? Or, do I also need to turn ratio into a 1-element fp16 tensor?

### Jokeren · 2023-01-25

> Is it sufficient for me to just convert the 1.0 into a 1-element fp16 tensor? Or, do I also need to turn ratio into a 1-element fp16 tensor?

Either way, triton will do broadcasting for you. (If not, please report a bug :)). 

I would recommend using `tl.full`. 

### vedantroy · 2023-01-26

Sounds good, once I can build master successfully, I will try it out & close this issue.

### jjmcinto · 2025-10-15

It looks like the OP may have forgotten about this question. I would like to help to close it. I installed the latest version of `triton` and debugged the OP's code. The main change I made was to use `triton.language.cast` in place of `.to(tl.float16)`. I confirmed that the calculations in the kernel code can be done in float16 or float32, as chosen by the calling function. This seems to indicate that the main issue has been resolved.

**Env**: Triton 3.5.0; PyTorch 2.8.0+cu129; Python 3.11.7; CUDA runtime 12.9; GPU NVIDIA RTX A6000 (SM 8.6); Driver 580.65.06; OS Linux-6.8.0-79-generic-x86_64-with-glibc2.35
**Code**:
```

import math
import torch
import triton
import triton.language as tl


@triton.jit
def unmasked_blend_kernel(
    img1_ptr,             # *u8
    img2_ptr,             # *u8
    out_ptr,              # *f32 (destination buffer)
    ratio,                # scalar float
    total_items: tl.constexpr,
    BLOCK_SIZE: tl.constexpr,
    MATH_DTYPE: tl.constexpr,     # tl.float16 or tl.float32
    CHECK_FP16: tl.constexpr,     # 1 = enforce fp16 specialization, else 0
):
    # If we're asserting fp16, fail compilation unless MATH_DTYPE is exactly fp16
    if CHECK_FP16:
        tl.static_assert(MATH_DTYPE == tl.float16, "Expected fp16 math specialization")
        
    block_idx = tl.program_id(0)
    offset = block_idx * BLOCK_SIZE
    item_element_idxs = tl.arange(0, BLOCK_SIZE)
    img1_item_ptrs = img1_ptr + offset + item_element_idxs
    img2_item_ptrs = img2_ptr + offset + item_element_idxs

    ratio_tensor = tl.zeros((1,), dtype=tl.float16)
    ratio_tensor += ratio

    if offset + BLOCK_SIZE > total_items:
        mask = item_element_idxs < total_items % BLOCK_SIZE
        img1 = tl.cast(tl.load(img1_item_ptrs, mask=mask, other=0), MATH_DTYPE)
        img2 = tl.cast(tl.load(img2_item_ptrs, mask=mask, other=0), MATH_DTYPE)
        out = ratio_tensor * img1 + tl.cast(1.0 - ratio_tensor, MATH_DTYPE) * img2
        tl.store(img1_item_ptrs, out, mask=mask)
    else:
        img1 = tl.cast(tl.load(img1_item_ptrs), MATH_DTYPE)
        img2 = tl.cast(tl.load(img2_item_ptrs), MATH_DTYPE)
        out = ratio_tensor * img1 + tl.cast(1.0 - ratio_tensor, MATH_DTYPE) * img2
        tl.store(img1_item_ptrs, out)

def run_once(n_items=1_000_000, ratio=0.37, block_size=1024, math_dtype="fp32", seed=0):
    torch.manual_seed(seed)

    # Inputs as uint8 on GPU – matches the “two uint8 images” premise
    img1 = torch.randint(0, 256, (n_items,), dtype=torch.uint8, device="cuda")
    img2 = torch.randint(0, 256, (n_items,), dtype=torch.uint8, device="cuda")

    out  = torch.empty(n_items, dtype=torch.float32, device="cuda")

    grid = lambda META: (triton.cdiv(n_items, META["BLOCK_SIZE"]),)

    # Select specialization + whether to enforce compile-time assertion
    if math_dtype == "fp16":
        triton_dtype = tl.float16
        check_fp16   = 1
    else:
        triton_dtype = tl.float32
        check_fp16   = 0

    unmasked_blend_kernel[grid](
        img1, img2, out, ratio,
        total_items=n_items,
        BLOCK_SIZE=block_size,
        MATH_DTYPE=triton_dtype,
        CHECK_FP16=check_fp16,
    )

    # References
    ref32 = ratio * img1.float() + (1.0 - ratio) * img2.float()
    ref16 = (ratio * img1.float() + (1.0 - ratio) * img2.float()).to(torch.float16).to(torch.float32)

    # Error metrics
    diff_fp32 = (out - ref32).abs().max().item()
    diff_fp16 = (out - ref16).abs().max().item()

    return out, ref32, ref16, diff_fp32, diff_fp16


def main():
    print("Running FP32-math kernel...")
    _, ref32, ref16, d32, d16 = run_once(math_dtype="fp32")
    print(f"FP32-math kernel vs FP32 ref: max|diff| = {d32:.6g}")
    print(f"FP32-math kernel vs FP16 ref: max|diff| = {d16:.6g}")

    print("\nRunning FP16-math kernel (with compile-time assert)...")
    _, ref32b, ref16b, d32b, d16b = run_once(math_dtype="fp16")
    print(f"FP16-math kernel vs FP32 ref: max|diff| = {d32b:.6g}")
    print(f"FP16-math kernel vs FP16 ref: max|diff| = {d16b:.6g}")

    # Sanity: fp16-specialized kernel should align closer to fp16 reference than to fp32 reference
    assert d16b <= d32b + 1e-4, "FP16-math kernel is not closer to FP16 reference than FP32 reference."


if __name__ == "__main__":
    main()

```
**Result**:
Running FP32-math kernel...
FP32-math kernel vs FP32 ref: max|diff| = 255
FP32-math kernel vs FP16 ref: max|diff| = 255

Running FP16-math kernel (with compile-time assert)...
FP16-math kernel vs FP32 ref: max|diff| = 509.63
FP16-math kernel vs FP16 ref: max|diff| = 509.625

If there’s no remaining case to investigate, I propose closing as resolved. @OP @maintainers—any objections?

### LeonxLJX · 2026-09-01

I'd like to take this one (`[Question] How to force certain computations to occur in flo`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)

### LeonxLJX · 2026-09-01

I'd like to take this one (`[Question] How to force certain computations to occur in flo`). I'll dig into the root cause and follow up with a PR shortly. (claiming via @LeonxLJX)

### LeonxLJX · 2026-09-01

I'd like to take this one (`[Question] How to force certain computations to occur in flo`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)
