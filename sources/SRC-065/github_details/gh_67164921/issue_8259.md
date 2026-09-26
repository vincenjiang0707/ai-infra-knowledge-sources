# [Issue #8259] tl.range pipeline causes kernel to produce incorrect output

source: https://github.com/triton-lang/triton/issues/8259
state: closed | updated: 2026-09-01T18:09:34Z
labels: help wanted

## 正文

### Describe the bug

Repro:
```python
import torch
import triton
import triton.language as tl

@triton.jit
def pipeline_kernel_fail(ptr, diff):
    for pid in tl.range(tl.program_id(0), 4096, loop_unroll_factor=1, num_stages=2):
        for offset in tl.range(0, 4096, 128, loop_unroll_factor=2, num_stages=2, flatten=True):
            idx0 = offset + tl.arange(0, 128)
            addr = ptr + pid * 4096 + idx0
            values = (idx0 + pid).to(tl.float32)
            tl.store(addr, values)
            loaded = tl.load(addr)
            tl.store(diff + pid * 4096 + idx0, loaded - values)

@triton.jit
def safe_kernel(ptr, diff):
    for pid in tl.range(tl.program_id(0), 4096, loop_unroll_factor=1, num_stages=1):
        for offset in tl.range(0, 4096, 128, loop_unroll_factor=2, num_stages=1, flatten=False):
            idx0 = offset + tl.arange(0, 128)
            addr = ptr + pid * 4096 + idx0
            values = (idx0 + pid).to(tl.float32)
            tl.store(addr, values)
            loaded = tl.load(addr)
            tl.store(diff + pid * 4096 + idx0, loaded - values)


def run(kernel, name):
    ptr = torch.zeros((4096 * 4096,), device='cuda', dtype=torch.float32)
    diff = torch.empty_like(ptr)
    kernel[(4096,)](ptr, diff)
    max_abs = diff.abs().max().item()
    nonzero = (diff != 0).sum().item()
    print(f"{name}: max diff={max_abs}, nonzero={nonzero}")
    print('  sample', diff[:10])


if __name__ == '__main__':
    run(pipeline_kernel_fail, 'pipeline')
    run(safe_kernel, 'safe')

"""
Output:

pipeline: max diff=4095.0, nonzero=4095
  sample tensor([ 0., -1., -2., -3., -4., -5., -6., -7., -8., -9.], device='cuda:0')
safe: max diff=0.0, nonzero=0
  sample tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], device='cuda:0')
"""
```
It seems setting `num_stages > 1` causes the `tl.store(addr, values)` and `loaded = tl.load(addr)` to be executed out of order, causing it to load from stale data. As a fix, can the Triton compiler be able to serialize these two operations?

In general, does Triton have guarantee that all runnable kernels produce correct output, or should users proactively check the kernel output is correct?

### Environment details

Triton: 3.5.0
GPU: H100

## 评论 (6)

### Jokeren · 2025-09-23

The reproducer itself has problems.

```
            tl.store(addr, values)
            loaded = tl.load(addr)
            tl.store(diff + pid * 4096 + idx0, loaded - values)
```

This is not guaranteed to be correct unless you sync *within* the CTA.

### oulgen · 2025-09-23

> tl.store(addr, values)
>             loaded = tl.load(addr)
>             tl.store(diff + pid * 4096 + idx0, loaded - values)

Are you suggesting adding a tl.debug_barrier? Is there a more official solution?

### lezcano · 2025-09-25

Yep, we don't do range analysis for global memory pointers, so in these cases you do need to add a `tl.debug_barrier` sadly

### Khushiyant · 2026-02-14

Yeah the lack of range analysis is what I figured too. What I noticed is that pipelining doesn't just reorder the ops, it actually changes the loop structure. Traced it at the warp level on 3.6.0 (latest, SM 120) and the safe version hits 80 branch events per kernel vs 64 for the pipelined one, with every warp diverging. 1023/1024 elements came back stale, max diff 4095.

### LeonxLJX · 2026-09-01

I'd like to take this one (`tl.range pipeline causes kernel to produce incorrect output`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)

### lezcano · 2026-09-01

there is nothing to fix here, the fix is as described at https://github.com/triton-lang/triton/issues/8259#issuecomment-3325488510
