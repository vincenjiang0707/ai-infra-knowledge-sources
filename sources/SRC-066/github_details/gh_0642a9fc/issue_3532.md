# [Issue #3532] rank_2k_universal and symm_universal Arguments constructors discard batch_stride_B

source: https://github.com/NVIDIA/cutlass/issues/3532
state: open | updated: 2026-09-02T06:12:52Z
labels: CUTLASS C++

## 正文

### Description

The `Arguments` constructors of two kernels discard their `batch_stride_B` parameter and store 0 instead:

```cpp
// include/cutlass/gemm/kernel/rank_2k_universal.h:176
batch_stride_A(batch_stride_A), batch_stride_B(0),

// include/cutlass/gemm/kernel/symm_universal.h:173
batch_stride_A(batch_stride_A), batch_stride_B(0),
```

`trmm_universal.h:158` stores its parameter (`batch_stride_B(batch_stride_B)`), which makes the intent clear; these are copy-paste typos. Confirmed by constructing `Arguments` for both kernels in a host program and printing the stored field: passing 200 stores 0.

Consequences:

1. `Params` construction copies `args.batch_stride_B`, so downstream code always sees stride 0.
2. Both kernels' `transposed_problem()` does `std::swap(args.batch_stride_A, args.batch_stride_B)` on an `Arguments` built by that constructor (`rank_2k_universal.h:189`), so after the swap the *stored* `batch_stride_A` becomes the dead 0 too: for the transposed path both batch strides are wrong, not just B's.

Additional observation while tracing this: neither kernel body ever reads `params.batch_stride_A` or `params.batch_stride_B` (unlike `gemm_universal.h`, which advances both pointers per batch), so batched operation through these kernels keeps A and B fixed across batches regardless of the arguments. The typo is provable on its own; the unused-stride observation may deserve separate attention.

### Suggested fix

Store the parameter in both places:

```cpp
batch_stride_A(batch_stride_A), batch_stride_B(batch_stride_B),
```


## 评论 (3)

### Samyra312007 · 2026-09-02

Respected Maintainer and Author, I would like to understand about this issue end to end and work on it. Is it open for contributors?

### VaggelisGian · 2026-09-02

Thanks for the interest. This one is already claimed: a fix (storing the batch_stride_B parameter instead of 0 in both Arguments constructors) is prepared and queued to be published as a PR. I will link it here once it is up.

### Samyra312007 · 2026-09-02

Thanks for the response. I will look for some other issues to work on.
