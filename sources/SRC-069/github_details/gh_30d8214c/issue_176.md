# [Issue #176] B200(sm=100a) FP8 accumulator bits

source: https://github.com/deepseek-ai/DeepGEMM/issues/176
state: open | updated: 2025-11-14T07:57:03Z
labels: 

## 正文

Recently we get the B200 and test the "tcgen05.mma.cta_group::1.kind::f8f6f4". We find the accumulator maintain 25bits mantissa, higher compared to H100 (13bit mantissa).
1. we want to confirm our findings of 25bits is reliable?
2. if more mantissa bits are reserved, does the deepgemm still calculate a group of 128 in tensor core and then move to accumulate in cuda core?
3. we also test the "tcgen05.mma.cta_group::1.kind::mxf4nvf4" and "tcgen05.mma.cta_group::1.kind::mxf4", but the number of mantissa bits in accumulator is not sure, 34,35,36,37bits  are tested.Do you ever conduct the test or have some reference? 

<img width="868" height="832" alt="Image" src="https://github.com/user-attachments/assets/53f60260-d782-4957-bba6-25ebc8124f42" />

Waiting for your reply and suggestion. Thank you a lot~

## 评论 (2)

### LyricZhao · 2025-08-28

I have a script to detect the bits:

```python
def create_low_precision_tensors(dtype: torch.dtype, modifier_a: Callable, modifier_b: Callable):
    # The layout should always be NT
    a_fp32 = torch.zeros((256, 256), dtype=torch.float, device='cuda')
    b_fp32 = torch.zeros((256, 256), dtype=torch.float, device='cuda')
    modifier_a(a_fp32), modifier_b(b_fp32)
    a_dtype = a_fp32.to(dtype)
    b_dtype = b_fp32.to(dtype)
    assert (a_fp32 - a_dtype.float()).abs().amax() == 0
    assert (b_fp32 - b_dtype.float()).abs().amax() == 0
    return a_dtype, b_dtype


def tensor_core_precision():
    # Test tensor core accumulation precision (mantissa)
    print('Tensor core accumulation mantissa bits:')
    for dtype in (torch.float, torch.bfloat16, torch.float8_e4m3fn):
        shift, num_bits = 10, None
        for i in range(shift, 27):
            half_shift = (shift // 2, shift - (shift // 2))
            half_i = ((i - shift) // 2, i - shift - (i - shift) // 2)
            a, b = create_low_precision_tensors(
                dtype,
                lambda mat: (mat[0, 0].fill_(2 ** (-half_shift[0])), mat[0, 1].fill_(2 ** half_i[0]), mat[0, 2].fill_(-(2 ** half_i[0]))),
                lambda mat: (mat[0, 0].fill_(2 ** (-half_shift[1])), mat[0, 1].fill_(2 ** half_i[1]), mat[0, 2].fill_(2 ** half_i[1]))
            )
            # You have to create a CPP wrapper of cuBLAS
            d = cublas_gemm_nt(a, b, use_fp32_output=True)
            assert d.dtype == torch.float
            if int(d[0, 0].item() * (2 ** shift)) == 0:
                assert i != shift, 'The first case should not fail'
                num_bits = i - 1
                break
        assert num_bits is not None
        print(f' > {dtype}: {num_bits} bits')
```

1. We don't have SM100 GPUs, but you can run my script on SM100 to double confirm it;
2. If so, we don't have to use CUDA cores to accumulate, see NVIDIA's SM100 PR (or the SM100 code currently);
3. Same as 1.

### wecheerhuang · 2025-11-14

I want to test the mantissa bit width of the FP4 and FP8 accumulators in a tensor core on GB10, but I don't know how to test it using PTX. Could you please tell me how you tested it?
