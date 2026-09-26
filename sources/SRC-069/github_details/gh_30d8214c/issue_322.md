# [Issue #322] `get_paged_mqa_logits_metadata()` does not work with large batch size due to excessive static shared memory impl

source: https://github.com/deepseek-ai/DeepGEMM/issues/322
state: closed | updated: 2026-07-21T06:07:00Z
labels: 

## 正文

```python
import torch

from vllm.third_party.deep_gemm import get_paged_mqa_logits_metadata

batch_size = 8192
block_size = 64
num_sms = torch.cuda.get_device_properties(0).multi_processor_count

context_lens = torch.full((batch_size, 1), 4096, dtype=torch.int32, device="cuda")
indices = torch.arange(batch_size, dtype=torch.int32, device="cuda") // 2

get_paged_mqa_logits_metadata(
    context_lens,
    block_size,
    num_sms,
    indices=indices,
)
torch.cuda.synchronize()
```
```
NVCC compilation failed: ptxas error   : Entry function '_ZN9deep_gemm5sched30smxx_paged_mqa_logits_metadataILj8192ELj256ELj152ELb1EEEvjjbPKjS3_Pj' uses too much shared data (0x18004 bytes, 0xc000 max)

Traceback (most recent call last):
  File "/home/thien/debug.py", line 12, in <module>
    get_paged_mqa_logits_metadata(
RuntimeError: Assertion error (/workspace/.deps/deepgemm-src/csrc/apis/../jit_kernels/impls/../../jit/compiler.hpp:228): false and "NVCC compilation failed"
```

This is caused by static shared memory being linear with batch size

https://github.com/deepseek-ai/DeepGEMM/blob/891d57b4db1071624b5c8fa0d1e51cb317fa709f/deep_gemm/include/deep_gemm/scheduler/paged_mqa_logits.cuh#L19-L20

Would it possible to make it support large batch size instead? Either with dynamic shared memory or reimplement in a way that doesn't need that much shared memory.

The context is that I'm trying to use `fp8_fp4_paged_mqa_logits()` for prefill case, which requires calling this metadata preparation kernel. Thank you.

## 评论 (1)

### toffee-desuwa · 2026-05-30

@LyricZhao — I looked into [#322](https://github.com/deepseek-ai/DeepGEMM/issues/322) and I think I found the cause. Wanted to ask your preferred direction before anyone writes a fix.

The cause: In paged_mqa_logits.cuh, the kernel smxx_paged_mqa_logits_metadata declares three static __shared__ arrays, each sized by kAlignedBatchSize:

varlen_atom_token_start[kAlignedBatchSize] (line 19)
varlen_atom_context_len[kAlignedBatchSize] (line 20)
prefix_sum[kAlignedBatchSize] (line 57)
That is about 3 * 4 * kAlignedBatchSize bytes of static shared memory. When the batch size is large (roughly 4096+), this goes over the 48 KB static smem limit, so the kernel cannot launch. The host side in attention.hpp does not catch this: there is no batch-size check before launch, and the only smem accounting is for dynamic shared memory, which this kernel does not use. So it cannot detect a static smem overflow. This matches @gau-nernst's report: fine at small batch, breaks at large batch.

Three possible fixes (not sure which you prefer):

Option 1 — Move the three arrays to dynamic shared memory (extern __shared__), and pass the size through the launch config and the host check, so the existing accounting covers them.

Option 2 — Process the batch in fixed-size chunks, so static smem stays bounded no matter how large the batch is.

Option 3 — Keep it static but add a host-side DG_HOST_ASSERT on the batch-size limit. This is the smallest change: it turns a silent launch failure into a clear error, but it caps the supported batch instead of fixing it.

I'm happy to open a PR for whichever direction fits the codebase best. I just didn't want to decide the design myself on a core kernel. Thanks!
