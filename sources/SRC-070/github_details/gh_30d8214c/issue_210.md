# [Issue #210] [Feature] Support Bias

source: https://github.com/deepseek-ai/DeepGEMM/issues/210
state: open | updated: 2025-10-20T03:20:33Z
labels: 

## 正文

I was wondering if deepgemm can support bias computation. I think bias term is widely existing in linear layers.

Without bias support, we need to write dedicated kernels to perform sum operator. Compared with fused operator, extra time is needed to read and write the matrix. 

## 评论 (5)

### scuchenxiang · 2025-10-19

hi, @LyricZhao , I was wondering if deepgemm can support C = A*B+C in gemm， like the impl in wgemm.

### LyricZhao · 2025-10-20

> I was wondering if deepgemm can support C = A*B+C in gemm

Yes, we can do `D = C + A @ B`. But C should have the same shape with the output matrix (D). And inplace version is the fastest (C's ptr == D's ptr).

### LyricZhao · 2025-10-20

For bias support, we don't have some plans, as we don't have such demand internally. Adding support may cost extra maintainence efforts. Maybe later.

### scuchenxiang · 2025-10-20

> > I was wondering if deepgemm can support C = A*B+C in gemm
> 
> Yes, we can do `D = C + A @ B`. But C should have the same shape with the output matrix (D). And inplace version is the fastest (C's ptr == D's ptr).

Hi, @LyricZhao , I was also wondering is this feature likely to be released?

### LyricZhao · 2025-10-20

`D = C + A @ B` is already included in main.
