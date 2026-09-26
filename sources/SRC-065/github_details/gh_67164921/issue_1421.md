# [Issue #1421] Use atomic_cas inside a loop

source: https://github.com/triton-lang/triton/issues/1421
state: open | updated: 2026-09-01T18:09:37Z
labels: help wanted

## 正文

Hi, I'm experimenting with a simple kernel that reduces a rank-3 tensor on its last dimension. The kernel uses atomics to sum across one tensor row (I know it's not efficient, this is just a simple reproducer). I'm using two versions of the atomics, the first using atomic_add, and the second using the lock-like mechanism with atomic_cas and atomic_xchg.

```
@triton.jit
def _sum_kernel(X, Locks, O, width: tl.constexpr, use_atomic_add: tl.constexpr):
  in_off = tl.program_id(0) * width
  out_off = tl.program_id(0)

  for w in range(0, width):
    x = tl.load(X + in_off + w)
    if use_atomic_add:
      tl.atomic_add(O + out_off, x)
    else:
      while tl.atomic_cas(Locks + out_off, 0, 1) == 1:
        pass
      tl.store(O + out_off, tl.load(O + out_off) + x)
      tl.atomic_xchg(Locks + out_off, 0)


def _sum_fn(a, use_atomic_add):
  b, h, w = a.shape
  locks = torch.zeros([b, h], dtype=torch.int32, device='cuda')
  out = torch.zeros([b, h], dtype=a.dtype, device='cuda')
  _sum_kernel[(b * h,)](a, locks, out, width=w, use_atomic_add=use_atomic_add)
  return out

if __name__ == "__main__":
  x = torch.empty((8, 64, 128), dtype=torch.float32, device="cuda").normal_()
  ref = torch.sum(x, axis=-1)
  rtol = 1e-03

  print(torch.allclose(ref, _sum_fn(x, True), rtol=rtol))
  print(torch.allclose(ref, _sum_fn(x, False), rtol=rtol))
```

Unfortunately for the second version I get
```

  File "/usr/local/home/giorgio/triton/python/triton/compiler.py", line 741, in visit_For
    assert for_op_region.size() == 1, "We use SCF, so the loop body should only have one block"
AssertionError: We use SCF, so the loop body should only have one block
```

Any help would be appreciated, thanks.

## 评论 (4)

### Jokeren · 2023-03-27

Can you try to rewrite `for w in range(0, width):` using a while loop?

### LeonxLJX · 2026-09-01

I'd like to take this one (`Use atomic_cas inside a loop`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)

### LeonxLJX · 2026-09-01

I'd like to take this one (`Use atomic_cas inside a loop`). I'll dig into the root cause and follow up with a PR shortly. (claiming via @LeonxLJX)

### LeonxLJX · 2026-09-01

I'd like to take this one (`Use atomic_cas inside a loop`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)
