# [Issue #3351] [BUG] __c_pointers__() causes monotonic RSS growth due to uncached ctypes allocations in kernel launch hot path

source: https://github.com/NVIDIA/cutlass/issues/3351
state: open | updated: 2026-09-06T06:22:50Z
labels: bug, ? - Needs Triage, inactive-30d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**

`__c_pointers__()` on CUTLASS DSL scalar types (`Int32`, `Float32`, etc.) creates fresh `ctypes` objects on every kernel invocation. In ML training loops with frequent kernel launches, these short-lived allocations interleave with long-lived framework objects, causing memory fragmentation and monotonic process RSS growth that eventually leads to OOM.

This occurs regardless of the Python memory allocator (`pymalloc`, `glibc malloc`, or `jemalloc`).

The root cause is in `IntegerMeta.__new__` (and similar for Float types):

```python
def _c_pointers(self):
    c_value = getattr(ctypes, f"c_int{width}")(self.value)  # object 1
    return [ctypes.cast(ctypes.pointer(c_value),             # objects 2+3
                        ctypes.c_void_p)]
```

Each call creates 3 ctypes objects that are immediately discarded. In a training loop with multiple kernel calls per step, this produces hundreds to thousands of short-lived objects per step that fragment the heap.

**Observed in production:** ~0.3 GB/step RSS growth in large model training, leading to OOM within hundreds of steps.

**Steps/Code to reproduce bug**

```python
"""
Requires: pip install nvidia-cutlass-dsl
Run with: python repro.py
Also reproducible with: PYTHONMALLOC=malloc python repro.py
"""
import os, gc, sys

def get_rss_mb():
    with open(f"/proc/{os.getpid()}/status") as f:
        for line in f:
            if line.startswith("VmRSS:"):
                return int(line.split()[1]) / 1024
    return 0

from cutlass.base_dsl.typing import Int32, Int64, Float32, Float64

SCALAR_ARGS = [
    (Int32, [64, 128, 192, 256, 512, 1024, 2048, 4096]),
    (Int64, [2048, 4096, 8192, 16384]),
    (Float32, [0.088388, 0.125, 0.0625, 1.0]),
    (Float64, [1.0, 0.5, 0.001]),
]
long_lived_pool = []

def simulate_kernel_call():
    for cls, values in SCALAR_ARGS:
        for v in values:
            cls(v).__c_pointers__()  # 3 ctypes objects created and discarded

def simulate_framework_allocs(step):
    # Varied-size long-lived objects that pin arenas
    long_lived_pool.append({f"k{step}": bytearray(37 + step % 73)})
    long_lived_pool.append(tuple(range(10 + step % 20)))
    long_lived_pool.append([None] * (5 + step % 15))
    if step % 7 == 0:
        long_lived_pool.append(bytearray(200 + step % 300))

gc.disable()
rss_start = get_rss_mb()

for step in range(1, 100001):
    for _ in range(8):  # 8 kernel calls per step
        simulate_kernel_call()
    simulate_framework_allocs(step)

    if step % 10000 == 0:
        rss = get_rss_mb()
        print(f"Step {step:>6}: RSS = {rss:.0f} MB (growth: {rss - rss_start:.0f} MB)")

print(f"\nTotal RSS growth: {get_rss_mb() - rss_start:.0f} MB")
```

**Without fix (current behavior):**
```
Step  10000: RSS = 1573 MB (growth: 946 MB)
Step  50000: RSS = 5357 MB (growth: 4729 MB)
Step 100000: RSS = 10082 MB (growth: 9455 MB)
```

**With caching applied:**
```
Step  10000: RSS = 633 MB (growth: 8 MB)
Step  50000: RSS = 662 MB (growth: 36 MB)
Step 100000: RSS = 703 MB (growth: 78 MB)
```

The ~78 MB growth with caching corresponds to the actual long-lived payload (~59 MB). Without caching, RSS grows **120x** beyond actual data.

**Expected behavior**

`__c_pointers__()` should cache results for immutable scalar values, avoiding repeated ctypes object creation. Suggested fix:

```python
# Integer types (in IntegerMeta.__new__):
_cptr_cache = {}

def _c_pointers(self):
    key = self.value
    cached = _cptr_cache.get(key)
    if cached is not None:
        return cached
    c_value = getattr(ctypes, f"c_int{width}")(self.value)
    result = [ctypes.cast(ctypes.pointer(c_value), ctypes.c_void_p)]
    _cptr_cache[key] = result
    return result

# Same pattern for Float32, Float64, Float16, BFloat16, TFloat32
```

**Environment details:**
- Python 3.12
- nvidia-cutlass-dsl (CUDA 12.9+)
- Linux x86_64
- Reproducible with both default pymalloc and `PYTHONMALLOC=malloc`

## 评论 (9)

### a123pal · 2026-06-26

Hey, I think I have a fix for this. Mind if I put up a PR?

### Difers · 2026-06-26

> Hey, I think I have a fix for this. Mind if I put up a PR?

@a123pal Thanks for offering to put up a PR. I actually have a local fix that I've verified resolves the issue on my side as well. Would you be willing to take a look at my changes? #3352 





### a123pal · 2026-06-26

@Difers One thing I noticed in the Integer path is the cache write looks unreachable. The early return fires before `_cptr_cache[key] = result`, so the dict never actually gets populated. The Float64 fix looks solid though. Let me know if I'm missing something!

### Difers · 2026-06-26

> [@Difers](https://github.com/Difers) One thing I noticed in the Integer path is the cache write looks unreachable. The early return fires before `_cptr_cache[key] = result`, so the dict never actually gets populated. The Float64 fix looks solid though. Let me know if I'm missing something!

@a123pal The early return only happens on cache hit; on cache miss it builds `result`, writes `_cptr_cache[key] = result`, then returns it. So the cache should be populated.Could you share the exact line you’re looking at so I can make sure I’m not missing something?

### a123pal · 2026-06-26

@Difers You're right, I misread the diff. The fix looks good, sorry about that!

### anakinxc · 2026-07-06

Will take care of this

### github-actions[bot] · 2026-08-05

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### brandon-yujie-sun · 2026-08-07

@Difers this is fixed in 4.6.2 and 4.7

### github-actions[bot] · 2026-09-06

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.
