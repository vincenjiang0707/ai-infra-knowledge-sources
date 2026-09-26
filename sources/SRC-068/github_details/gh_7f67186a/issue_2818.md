# [Issue #2818] Using `torch.library.wrap_triton` introduces measurable CPU overhead in `rotary`

source: https://github.com/Dao-AILab/flash-attention/issues/2818
state: open | updated: 2026-09-18T19:11:18Z
labels: 

## 正文

older releases such as 2.7.4 don't do this
```
AFFECTED PATTERN: flash-attn 2.8.3.post1 rotary uses bare wrap_triton
installed path:    89.97 us/call
direct bypass:     19.97 us/call
recoverable:       70.00 us/call (4.5x)
```
minimal repro:
```
#!/usr/bin/env python3
"""Minimal reproducer for eager torch.library.wrap_triton overhead."""

import statistics
import time
import inspect

import torch
import triton
import triton.language as tl


@triton.jit
def touch(x):
    tl.store(x, 0.0)


x = torch.empty(1, device="cuda")
raw = touch
wrapped = torch.library.wrap_triton(touch)  # Cache it: construction is not the issue.
grid = lambda meta: (1,)  # Match the callable-grid path used by FlashAttention.


def time_calls(fn, calls=1000, repeats=7):
    fn()  # Compile/warm up outside the measurement.
    torch.cuda.synchronize()
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        for _ in range(calls):
            fn()
        torch.cuda.synchronize()
        samples.append((time.perf_counter() - start) * 1e6 / calls)
    return statistics.median(samples)


raw_us = time_calls(lambda: raw[grid](x))
wrapped_us = time_calls(lambda: wrapped[grid](x))
print(f"raw:     {raw_us:8.2f} us/launch")
print(f"wrapped: {wrapped_us:8.2f} us/launch")
print(f"overhead:{wrapped_us - raw_us:8.2f} us/launch ({wrapped_us / raw_us:.1f}x)")


print("\nInstalled FlashAttention check:")
try:
    import flash_attn
    from flash_attn.ops.triton import rotary
except ImportError as error:
    print(f"SKIP: FlashAttention is not importable ({error})")
else:
    version = getattr(flash_attn, "__version__", "unknown")
    source = inspect.getsource(rotary.apply_rotary)
    if "torch.library.wrap_triton" not in source:
        print(f"UNAFFECTED: flash-attn {version} rotary does not use bare wrap_triton")
    else:
        print(f"AFFECTED PATTERN: flash-attn {version} rotary uses bare wrap_triton")
    q = torch.ones((1, 1, 1, 2), device="cuda")
    cos = torch.ones((1, 1), device="cuda")
    sin = torch.zeros((1, 1), device="cuda")
    call = lambda: rotary.apply_rotary(q, cos, sin, inplace=True)
    native_us = time_calls(call, calls=500, repeats=5)
    original_wrap_triton = torch.library.wrap_triton
    try:
        torch.library.wrap_triton = lambda kernel: kernel
        direct_us = time_calls(call, calls=500, repeats=5)
    finally:
        torch.library.wrap_triton = original_wrap_triton
    print(f"installed path: {native_us:8.2f} us/call")
    print(f"direct bypass:  {direct_us:8.2f} us/call")
    print(f"recoverable:    {native_us - direct_us:8.2f} us/call ({native_us / direct_us:.1f}x)")
```

## 评论 (1)

### devtyagi3909 · 2026-09-18

yeah this overhead is from the torch inductor dispatch adding python overhead on every call. if we just bypass `torch.library.wrap_triton` or only use it conditionally when running inside `torch.compile` (via `torch.compiler.is_compiling()`), we can recover the native triton dispatch speed. i can prototype the fix if you agree.
