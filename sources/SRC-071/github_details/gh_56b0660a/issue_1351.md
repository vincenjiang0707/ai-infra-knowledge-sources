# [Issue #1351] [BUG] illegal memory access when using topk_selector

source: https://github.com/tile-ai/tilelang/issues/1351
state: open | updated: 2026-09-25T07:28:13Z
labels: bug

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

0.1.6.post2+cuda.gitf0c721a4

### System information

3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] linux
0.1.6.post2+cuda.gitf0c721a4
2.9.1+cu128

### Problem description

When I use `tl_topk()`, if the input data values ​​are close (for example, only the last 10 bits are different), an illegal memory access will occur.

### Reproducible example code

Please using `examples/deepseek_v32/topk_selector.py`. And add the following code.

The Python snippets:

```python

# Returns float values that differ in the last 10 bits
def get_10bit_data(bs: int, seq_len: int) -> torch.Tensor:
    torch.manual_seed(42)

    top_22_bits_mask = 0xFFFFFC00
    last_10_bits_mask = 0x000003FF
    fixed_top_22_bits = 0x3F900000

    # Generate random bits for the last 10 bits
    random_bottom_bits = torch.randint(
        0, 2**10, (bs, seq_len), dtype=torch.int32, device="cuda"
    )

    # Combine: fixed top 22 bits with random last 10 bits
    score_bits = (fixed_top_22_bits & top_22_bits_mask) | (
        random_bottom_bits & last_10_bits_mask
    )

  # Convert back to float
  score = score_bits.view(torch.float32)
  return score


batch = 2
seq_len = 32 * 1024
topk = 2048
input = get_10bit_data(batch, seq_len).cuda()
starts = torch.zeros(batch, dtype=torch.int32).cuda()
ends = torch.ones(batch, dtype=torch.int32).cuda() * seq_len

indexes_ref = torch.topk(input, topk, dim=-1)[1] 
print(f"indexes_ref shape: {indexes_ref.shape}, indexes_ref: {indexes_ref}") # good

indexes = tl_topk(input, starts, ends, topk) 
print(f"indexes shape: {indexes.shape}, indexes: {indexes}") # illegal memory access

```




### Traceback

```pytb
Traceback (most recent call last):
  File "/workspace_new/tilelang/examples/deepseek_v32/topk_selector.py", line 284, in <module>
    test_topk_selector()
  File "/workspace_new/tilelang/examples/deepseek_v32/topk_selector.py", line 235, in test_topk_selector
    print(f"indexes shape: {indexes.shape}, indexes: {indexes}")
                                                     ^^^^^^^^^
  File "/workspace_new/tilelang/venv/lib/python3.12/site-packages/torch/_tensor.py", line 1109, in __format__
    return object.__format__(self, format_spec)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace_new/tilelang/venv/lib/python3.12/site-packages/torch/_tensor.py", line 568, in __repr__
    return torch._tensor_str._str(self, tensor_contents=tensor_contents)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace_new/tilelang/venv/lib/python3.12/site-packages/torch/_tensor_str.py", line 722, in _str
    return _str_intern(self, tensor_contents=tensor_contents)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace_new/tilelang/venv/lib/python3.12/site-packages/torch/_tensor_str.py", line 643, in _str_intern
    tensor_str = _tensor_str(self, indent)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace_new/tilelang/venv/lib/python3.12/site-packages/torch/_tensor_str.py", line 375, in _tensor_str
    formatter = _Formatter(get_summarized_data(self) if summarize else self)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace_new/tilelang/venv/lib/python3.12/site-packages/torch/_tensor_str.py", line 142, in __init__
    value_str = f"{value}"
                  ^^^^^^^
  File "/workspace_new/tilelang/venv/lib/python3.12/site-packages/torch/_tensor.py", line 1108, in __format__
    return self.detach().item().__format__(format_spec)
           ^^^^^^^^^^^^^^^^^^^^
torch.AcceleratorError: CUDA error: an illegal memory access was encountered
Search for `cudaErrorIllegalAddress' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.html for more information.
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```

### Expected behavior

_No response_

### Additional context

Please also pay attention to accuracy issues after the repair. Thank you.

## 评论 (5)

### LeiWang1999 · 2025-11-27

Thanks @yweng0828 for your report! We'll take a look.

### twoflypig · 2025-12-08

Any updates? 

### LudovicoYIN · 2025-12-16

Hi @LeiWang1999 ,

I dug into the illegal memory access. Root cause is in `examples/deepseek_v32/topk_selector.py`: the kernel stored all candidates of the threshold bucket into a fixed-size shared buffer (`s_input_idx`, assumed ≤4K). With near-identical values (only lowest bits differ), the threshold bucket explodes >4K, the shared buffer gets overflowed, and CUDA reports illegal address. The duplicated `pos` declaration was a symptom of the same fragile path.

I refactored the kernel to avoid shared-buffer staging entirely: each pass now scans input directly, filters by prefix, and writes outputs atomically, so no bounded shared storage is used. I also added a repro script and a pytest (`testing/python/issue/test_tilelang_issue_1351.py`) that uses the reported “last 10 bits differ” data; both now pass locally with matching values vs `torch.topk`.

Could you assign this issue to me? I’d like to submit the fix.


### LudovicoYIN · 2026-09-10

Hi @ZenAlexa, thanks for checking. I’m not working on this anymore.

### liuyun7345 · 2026-09-25

Thanks @LudovicoYIN for the earlier root-cause analysis in this thread — I arrived at the same conclusion independently, and your notes were a helpful cross-check.

I can reproduce the crash at 134ade7d816d0b73ed952fb07c97e47aaa617489 (RTX 4090D, CUDA 12.1): whenever the threshold bucket picked by the first radix pass holds more than 4096 candidates — e.g. FP32 scores sharing their low 10 mantissa bits as in the report, or even `torch.ones(...)` with a small enough topk — the atomic appends in `tl_topk_impl` write past the end of the fixed `T.alloc_shared([2, 4096])` buffer (`s_input_idx`), surfacing as `CUDA_ERROR_ILLEGAL_ADDRESS`.

Under `compute-sanitizer --tool memcheck` the original kernel trips `ERROR SUMMARY: 129 errors` on the 10-bit reproducer and the launch then fails with `CUDA_ERROR_LAUNCH_FAILED`; the patched kernel passes the full 13-case test matrix under the sanitizer with `ERROR SUMMARY: 0 errors`.

Fix (submitted in #3280): replace the fixed shared buffer with a `(batch, 2, seq_len)` global-memory workspace allocated in the `tl_topk` wrapper, so both radix buffers are bounded by `seq_len`. The public `tl_topk()` signature is unchanged.

Accuracy (cc @yweng0828's note above): a 13-case regression test — low-mantissa inputs (positive and negative), all-equal inputs at seq_len 4095/4096/4097/32768, boundary tie buckets, partial `[starts, ends)` ranges, and random inputs — checks the selected values against a masked `torch.topk` reference with `rtol=0, atol=0` (exact FP32 value match; ties may be broken in any order, as before).

Cost: kernel-only latency +7-10% across the shapes I measured (global-memory atomics instead of shared), plus one `torch.empty((batch, 2, seq_len), int32)` per call (e.g. 16 MB at batch=64, seq_len=32768). Seems a reasonable price for correctness; happy to revisit if maintainers prefer a no-workspace variant.

