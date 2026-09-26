# [Issue #3421] [BUG] 4.6.1: @cute.kernel / @cute.jit decorators leak caller call stack into reference cycles - regression vs 4.4.2

source: https://github.com/NVIDIA/cutlass/issues/3421
state: closed | updated: 2026-09-17T09:13:51Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

### Summary

In `nvidia-cutlass-dsl` 4.6.1, the `@cute.kernel` and `@cute.jit` decorators
retain the caller's Python frame object in a reference cycle, so it is freed
only by the cyclic GC, not by refcounting.

A retained frame keeps its `f_back` chain alive, so the decorators pin the
entire call stack that existed at decoration time, including all locals in
every frame of that chain. Any object that is a live local anywhere on the
stack when a `@cute.kernel` function is defined -- not compiled, not launched,
merely decorated -- stays alive until the next `gc.collect()`.

When kernel modules are imported lazily inside a function that holds large
CUDA tensors as locals, those tensors remain allocated until GC runs.
Applications that run with `gc.disable()` (common in CUDA-Graphs training
loops to avoid pauses) leak GPU memory. In a large workload this manifested
as multiple GiB of dead CUDA tensors held alive by dozens of retained
`CuTeDSL.kernel` frames plus importlib frames chaining back into the training
loop.

This is a regression vs 4.4.2.

### Environment

- Bad: `nvidia-cutlass-dsl==4.6.1` (code lives in `nvidia-cutlass-dsl-libs-core==4.6.1`)
- Good: `nvidia-cutlass-dsl==4.4.2`
- Python 3.12.9, Linux (pure CPython lifetime bug, architecture-independent)
- PyTorch with CUDA optional -- bug reproduces without GPU via weakref
- No GPU required to reproduce; CUDA tensor phase just makes impact concrete

### Reproduction - self-contained script

Decoration alone is sufficient. No `cute.compile`, no kernel launch, and no
GPU are required. Save the following as `repro.py` and run `python repro.py`.
Exit code 1 means bug reproduced, 0 means clean.

```python
#!/usr/bin/env python3
"""Reproducer: nvidia-cutlass-dsl 4.6.1 @cute.kernel / @cute.jit retain the
caller's Python frame chain in reference cycles.

In 4.6.1, BaseDSL.jit / BaseDSL.kernel (base_dsl/dsl.py, ~lines 896-909) and
CuTeDSL.kernel (cutlass_dsl/cutlass.py) do:

    cur_frame = inspect.currentframe()
    frame = cur_frame.f_back

Binding the classmethod's own frame object to one of its locals (cur_frame)
creates a frame -> f_locals -> frame reference cycle, so the frame is never
freed by reference counting -- only by the cyclic garbage collector. A retained
frame pins its entire f_back call-stack chain and every local variable in
every frame of that chain. Consequently, ANY object that is a live local
anywhere on the call stack at kernel-definition time -- e.g. a multi-GiB
torch.cuda tensor, when a kernel module is imported lazily inside a model's
forward() -- stays allocated until the next gc.collect(). Applications that
run gc.disable() (common for CUDA-graph training loops) leak unboundedly.

4.4.2 used frame = inspect.currentframe().f_back (no local naming the
current frame), which does not form the cycle: everything is freed promptly by
reference counting. Same script on 4.4.2 shows no retention.

Decoration alone triggers the bug -- no cute.compile, no kernel launch, and
no GPU are required (the CUDA-tensor phase is skipped if CUDA is unavailable;
the weakref phase demonstrates the same retention CPU-only).

Usage:
    python repro.py

Exit status: 1 if retention is detected (bug present), 0 if clean.
"""

import gc
import os
import sys
import types
import weakref

# Disable cyclic GC up front so the demonstration is not racy: with GC enabled
# an automatic collection could free the cycle at any allocation. Real
# applications that hit this bug run gc.disable() deliberately.
gc.disable()

import cutlass
import cutlass.cute as cute

# dont need CUDA to repro
try:
    import torch

    HAS_CUDA = torch.cuda.is_available()
except Exception:
    torch = None
    HAS_CUDA = False

TENSOR_BYTES = 1 << 30  # 1 GiB


def define_trivial_kernels():
    """Define (decorate) a trivial device kernel and host jit function.

    Decoration is the only ingredient needed: the returned wrappers are
    deliberately dropped, nothing is compiled, and nothing is launched. Any
    retention observed afterwards comes from the decorator machinery itself.
    """

    @cute.kernel
    def device_noop():
        pass

    @cute.jit
    def host_noop():
        pass


class Sentinel:
    pass


def probe_cuda_tensor():
    """Allocate a 1 GiB CUDA tensor as a frame local, then define kernels.

    The tensor is never passed to (or touched by) any kernel; it merely lives
    in this frame's locals while decoration happens one call level below.
    """
    big = torch.empty(TENSOR_BYTES // 4, dtype=torch.float32, device="cuda")
    define_trivial_kernels()
    return None  # big dies with this frame -- unless the frame is pinned


def probe_weakref_sentinel():
    """CPU-only variant: a sentinel object as a frame local at decoration."""
    sentinel = Sentinel()
    ref = weakref.ref(sentinel)
    define_trivial_kernels()
    return ref  # sentinel dies with this frame -- unless the frame is pinned


def collect_retained_frame_evidence():
    """Run gc with DEBUG_SAVEALL and report which frames sat in cycles."""
    define_trivial_kernels()  # fresh decoration so the cycle (if any) exists
    gc.set_debug(gc.DEBUG_SAVEALL)
    gc.collect()
    frames = [o for o in gc.garbage if isinstance(o, types.FrameType)]
    this_file = os.path.abspath(__file__)
    relevant = []
    for f in frames:
        fn = f.f_code.co_filename
        if "cutlass" in fn or os.path.abspath(fn) == this_file:
            short = fn.split("site-packages" + os.sep)[-1]
            if os.path.abspath(fn) == this_file:
                short = os.path.basename(fn)
            relevant.append(f"{f.f_code.co_qualname} @ {short}:{f.f_lineno}")
    # Restore normal GC state and actually free the saved garbage.
    gc.set_debug(0)
    gc.garbage.clear()
    del frames
    gc.collect()
    return relevant


def main():
    print(f"python  : {sys.version.split()[0]}")
    print(f"cutlass : {cutlass.__version__}")
    if torch is not None:
        dev = torch.cuda.get_device_name(0) if HAS_CUDA else "no CUDA device"
        print(f"torch   : {torch.__version__} ({dev})")
    else:
        print("torch   : not installed (CUDA phase will be skipped)")
    print()

    leaked = False

    # ---- Phase 1: CUDA tensor pinned across decoration (primary) ----------
    if HAS_CUDA:
        print("[1] CUDA tensor retention through @cute.kernel decoration")
        base = torch.cuda.memory_allocated()
        probe_cuda_tensor()
        pre_gc = torch.cuda.memory_allocated() - base
        gc.collect()
        post_gc = torch.cuda.memory_allocated() - base
        print(f"    tensor size                          : {TENSOR_BYTES} bytes")
        print(f"    allocated after probe returned, pre-gc : {pre_gc} bytes")
        print(f"    allocated after gc.collect()           : {post_gc} bytes")
        if pre_gc >= TENSOR_BYTES:
            print("    RESULT: LEAKED -- tensor pinned by decorator frame cycle "
                  "until gc.collect()")
            leaked = True
        else:
            print("    RESULT: ok -- tensor freed by refcounting, no gc needed")
        print()
    else:
        print("[1] CUDA phase skipped (no usable CUDA device); "
              "phase [2] shows the same defect CPU-only")
        print()

    # ---- Phase 2: weakref sentinel (works without a GPU) -------------------
    print("[2] weakref sentinel retention (no GPU required)")
    ref = probe_weakref_sentinel()
    alive_pre = ref() is not None
    gc.collect()
    alive_post = ref() is not None
    print(f"    sentinel alive after probe returned, pre-gc : {alive_pre}")
    print(f"    sentinel alive after gc.collect()           : {alive_post}")
    if alive_pre:
        print("    RESULT: LEAKED -- sentinel pinned by decorator frame cycle "
              "until gc.collect()")
        leaked = True
    else:
        print("    RESULT: ok -- sentinel freed by refcounting, no gc needed")
    print()

    # ---- Phase 3: which frames sat in reference cycles ---------------------
    print("[3] retained-frame evidence (gc.DEBUG_SAVEALL on a fresh decoration)")
    evidence = collect_retained_frame_evidence()
    decorator_frames = [e for e in evidence
                        if ".kernel @" in e or ".jit @" in e]
    print(f"    cutlass/repro frames found in cyclic garbage: {len(evidence)}")
    for e in evidence:
        print(f"      {e}")
    if decorator_frames:
        print("    RESULT: decorator frames (CuTeDSL.kernel / BaseDSL.jit) are "
              "retained in reference cycles")
        leaked = True
    else:
        print("    RESULT: no decorator frames retained in cycles")
    print()

    if leaked:
        print("VERDICT: BUG REPRODUCED -- @cute.kernel/@cute.jit decoration "
              "retained caller frames (and their locals) until gc.collect()")
        return 1
    print("VERDICT: clean -- no retention through decorator frames")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

The script does three phases:

1. Allocates a 1 GiB CUDA tensor as a function local, defines trivial
   `@cute.kernel`/`@cute.jit` one call level below, returns, and compares
   `torch.cuda.memory_allocated()` before and after `gc.collect()` (skipped if
   no CUDA).

2. Repeats with a `weakref.ref` sentinel (no GPU needed).

3. Re-runs decoration and collects with `gc.set_debug(gc.DEBUG_SAVEALL)`,
   printing qualified names of frame objects found in cyclic garbage.

### Observed output

#### 4.6.1 (bug)

```
python  : 3.12.9
cutlass : 4.6.1
torch   : 2.12.0a0 (NVIDIA GB200)

[1] CUDA tensor retention through @cute.kernel decoration
    tensor size                          : 1073741824 bytes
    allocated after probe returned, pre-gc : 1073741824 bytes
    allocated after gc.collect()           : 0 bytes
    RESULT: LEAKED -- tensor pinned by decorator frame cycle until gc.collect()

[2] weakref sentinel retention (no GPU required)
    sentinel alive after probe returned, pre-gc : True
    sentinel alive after gc.collect()           : False
    RESULT: LEAKED -- sentinel pinned by decorator frame cycle until gc.collect()

[3] retained-frame evidence (gc.DEBUG_SAVEALL on a fresh decoration)
    cutlass/repro frames found in cyclic garbage: 2
      CuTeDSL.kernel @ nvidia_cutlass_dsl/dsl_packages/cutlass/cutlass_dsl/cutlass.py:1599
      define_trivial_kernels @ repro.py:73
    RESULT: decorator frames (CuTeDSL.kernel / BaseDSL.jit) are retained in reference cycles

VERDICT: BUG REPRODUCED -- @cute.kernel/@cute.jit decoration retained caller frames (and their locals) until gc.collect()
```

Phase 3 lists the frames retained by that phase's fresh decoration: the
`CuTeDSL.kernel` classmethod frame -- the cycle itself -- plus the user frame
in which the kernels were defined, pinned via `f_back`. A collection run
immediately after `import cutlass` additionally shows retained
`BaseDSL.jit @ cutlass/base_dsl/dsl.py:899` frames and multiple cutlass
`<module>` import frames.

#### 4.4.2 (clean)

```
python  : 3.12.9
cutlass : 4.4.2
torch   : 2.12.0a0 (NVIDIA GB200)

[1] CUDA tensor retention through @cute.kernel decoration
    tensor size                          : 1073741824 bytes
    allocated after probe returned, pre-gc : 0 bytes
    allocated after gc.collect()           : 0 bytes
    RESULT: ok -- tensor freed by refcounting, no gc needed

[2] weakref sentinel retention (no GPU required)
    sentinel alive after probe returned, pre-gc : False
    sentinel alive after gc.collect()           : False
    RESULT: ok -- sentinel freed by refcounting, no gc needed

[3] retained-frame evidence (gc.DEBUG_SAVEALL on a fresh decoration)
    cutlass/repro frames found in cyclic garbage: 0
    RESULT: no decorator frames retained in cycles

VERDICT: clean -- no retention through decorator frames
```

### Expected vs Actual

Expected: after the function that defined kernels returns, its locals are
freed immediately by refcounting, no decorator frames remain in cyclic garbage,
and CUDA memory drops without needing `gc.collect()`.

Actual on 4.6.1: locals survive until next `gc.collect()`, decorator frames
are found in `gc.garbage` with `DEBUG_SAVEALL`, and CUDA allocation remains
pinned pre-GC.

### Root Cause

In 4.6.1 wheel, `cutlass/base_dsl/dsl.py` `BaseDSL.jit` (lines ~896-899) and
`BaseDSL.kernel` (~906-909) and `cutlass/cutlass_dsl/cutlass.py`
`CuTeDSL.kernel` (~1596-1601 and second override ~1946-1949):

```python
cur_frame = inspect.currentframe()
assert cur_frame is not None
frame = cur_frame.f_back
return BaseDSL.jit_runner(cls, "_kernel_helper", frame, *dargs, **dkwargs)
```

`cur_frame` is a local variable of the very frame it references, creating:

```
frame --f_locals--> {"cur_frame": frame, ...} --ref--> frame
```

So the frame survives its own return with non-zero refcount. When surrounding
user functions return, CPython transfers ownership of each interpreter frame
to the retained frame object and materializes its `f_back` chain, pinning the
entire stack present at decoration time and all locals.

4.4.2 avoids the cycle:

```python
frame = inspect.currentframe().f_back
return BaseDSL.jit_runner(cls, "_kernel_helper", frame, *dargs, **dkwargs)
```

A bare temporary is dropped immediately, so the decorator frame is freed by
refcount on return.

Additionally, `BaseDSL.jit_runner`'s inner `jit_runner_decorator` closes over
the `frame` argument only to compute
`func._decorator_location = BaseDSL.get_location_from_frame(frame)`. Keeping
a frame object alive inside a closure prolongs the risk.

Import-time side effect: `import cutlass` itself leaves several of its own
`<module>` import frames in cyclic garbage for the same reason, visible with
`gc.DEBUG_SAVEALL` (e.g. `cutlass/cute/runtime.py`, `cutlass/cute/testing.py`).

### Suggested Fix

Do not retain frame objects beyond decoration:
  
   extract source location eagerly and drop the frame before any
   closure is created. Instead of passing `frame` into `jit_runner` and closing
   over it, compute `DSLLocation` (filename/lineno) immediately:

   ```python
   cur = inspect.currentframe()
   caller = cur.f_back
   loc = BaseDSL.get_location_from_frame(caller)
   del cur, caller
   return BaseDSL.jit_runner(cls, "_kernel_helper", loc, ...)
   ```

   Then `jit_runner_decorator` uses the location value directly and never sees
   a frame. This guarantees no frame reference can outlive decoration even after
   future refactors.

Please add a regression test: with `gc.disable()`, decorate inside a
function holding a weakref-checked local, assert it is freed without
`gc.collect()`.

### Workaround for affected applications on 4.6.1

- Call `gc.collect()` after any lazy import or definition of `@cute.kernel`
  functions, or
- Keep cyclic GC enabled and accept collection pauses.

Both are undesirable in `gc.disable()` CUDA-Graphs training loops.

### Impact

Any application that defines or lazily imports `@cute.kernel`/`@cute.jit`
functions while large objects are live up-stack will pin those objects until
next GC. With `gc.disable()` this is an unbounded memory leak, observed as GPU memory leaks.


## 评论 (5)

### brandon-yujie-sun · 2026-08-27

@thakkarV hi Vijay, this is fixed in both 4.6.3 and 4.7.1

### zkyue · 2026-08-28

Following up on the note that this is fixed in 4.6.3 and 4.7.1: that matches what
I measure on the release wheels, but the fix does not appear to have reached
`main`, so the bug is still live for anyone tracking the 4.8 dev line.

## What I see on current `main`

At `ffa119a125` the pre-fix pattern is still present at five capture sites:

| file | function |
|---|---|
| `python/CuTeDSL/cutlass/base_dsl/dsl.py` | `BaseDSL.jit`, `BaseDSL.kernel` |
| `python/CuTeDSL/cutlass/cutlass_dsl/cutlass.py` | `CuTeDSL.kernel`, `CuteExperimentalDSL.kernel` |
| `python/CuTeDSL/cutlass/base_dsl/common.py` | `DSLOperationBuildError.__init__` |

This is not a new regression on the dev line — `7107b055`, the parent of the v4.8
dev update, already has the same named-local code, and the diff of that update
does not touch these sites. The fix landed on the release line instead: tag
`v4.7.1` is `cb424739`, whose parent `dcf215af` is the last commit it shares with
`main`. So `main` never received the forward-port rather than losing it.

`CuTeDSL.jit` (`cutlass.py:1781`) still uses the expression form and is fine, so
plain `@cute.jit` is unaffected. But `cutlass.cute.experimental.jit` resolves to
the inherited `BaseDSL.jit`, so the experimental JIT entry point *is* affected —
worth calling out, since it is easy to read "jit is safe" too broadly.

## Measured on the wheels

Decorating inside a frame that holds an 8 MiB local, `gc` disabled, 300
iterations, Python 3.12, RSS sampled from `/proc/self/status`:

| wheel | RSS growth per decoration | reclaimed by `gc.collect()` |
|---|---|---|
| 4.7.1 | 28.1 kB (flat) | 0 |
| 4.8.0.dev0 | 8200.3 kB | yes — confirms it is a cycle, not a true leak |
| 4.8.0.dev0 + `del` at the sites below | 29.9 kB (flat) | 0 |

Same shape for a decorate-then-`cute.compile` loop (30 iterations): 8234.4 kB/iter
on 4.8.0.dev0 versus 310.8 kB/iter on 4.7.1 and 306.8 kB/iter fixed — the ~310 kB
is version-independent compile-artifact growth.

CPU-only reproducer, no GPU required:

```python
import gc, weakref
import cutlass.cute as cute

class Sentinel:
    pass

def decorate_with_local():
    sentinel = Sentinel()          # a local of the decoration-site frame
    ref = weakref.ref(sentinel)

    @cute.kernel
    def k():
        pass

    return k, ref

gc.disable()
k, ref = decorate_with_local()
alive_before = ref() is not None          # True on 4.8.0.dev0, False on 4.7.1
gc.collect()
freed_by_gc = ref() is None

print("caller frame pinned:", alive_before)
print("cycle:", alive_before and freed_by_gc)
```

Both prints matter. `freed_by_gc` on its own is also true on 4.7.1, where the
object was already gone by reference counting; it is the *pair* — alive before
collection, dead after — that identifies a cycle rather than a true leak.

## One more site, which predates all of this

`cutlass/experimental/primitives/gpu_ops.py`, `_get_smem_allocator`, binds the
captured frame to `caller` and never drops it, on every return path. That one is
*not* a 4.8 matter — it reproduces on 4.7.1 as well, and it is not covered by
#3423. A one-line `del caller` after `f_back` is taken fixes it, consistent with
`_mlir_helpers/op.py`, which already uses exactly that idiom.

## Suggestion

PR #3423 already carries the right fix for the five sites above and is still
open, so it looks like it just needs a rebase and CI rather than anything new —
please don't close it as stale on the strength of the release-line fix. I have
the `gpu_ops.py` one-liner and a broader regression test (direct *and* factory
decorator forms, plus `cute.experimental.jit` and a directly-bound
`BaseDSL.kernel`, which exercise the two base-class sites that #3423 patches but
does not test), and am happy to send them as a follow-up to #3423 or as a
separate small PR — whichever you prefer.


### anakinxc · 2026-08-28

Hi @zkyue 

Yes, 4.8.0.dev0 is a little bit behind, the non-dev version will carry the fix

### thakkarV · 2026-08-29

> @thakkarV hi Vijay, this is fixed in both 4.6.3 and 4.7.1

Did you add a regression test? 

### brandon-yujie-sun · 2026-09-01

@thakkarV Yes, we have improved the regression test for this.
