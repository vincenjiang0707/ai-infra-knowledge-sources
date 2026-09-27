# [Issue #3469] [BUG] [CuTeDSL] cute.coalesce doesn't do anything on dynamic shapes

source: https://github.com/NVIDIA/cutlass/issues/3469
state: open | updated: 2026-09-26T06:24:10Z
labels: bug, ? - Needs Triage, inactive-30d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
A mode with a dynamic shape doesn't get coalesced into previous modes, even though the stride is static and the previous modes are fully static too (and that's all that's needed to check whether the modes can be coalesced).

**Steps/Code to reproduce bug**
```py
import torch
import cutlass.cute as cute
from cutlass.cute.runtime import from_dlpack


@cute.jit
def repro(tensor: cute.Tensor):
    layout = cute.make_layout(
        (16, tensor.shape[1] // 128),
        stride=(8, 128),
    )
    expected = cute.make_layout(
        (16 * (tensor.shape[1] // 128),),
        stride=(8,),
    )

    print("input:    ", layout)
    print("coalesced:", cute.coalesce(layout))
    print("expected: ", expected)


tensor = from_dlpack(torch.empty((4096, 8192), device="cuda"))
tensor = tensor.mark_compact_shape_dynamic(mode=1)
repro(tensor)
```

Output:
```text
input:     (16,?):(8,128)
coalesced: (16,?):(8,128)
expected:  (?{div=16}):(8)
```

**Environment details (please complete the following information):**
Version 4.7.0 of CuTeDSL

## 评论 (12)

### ccecka · 2026-08-17

This is intended behavior, otherwise information could be lost.

For instance, consider the shape `(16,?)` -- we know that the size of this shape is divisible by `16`.
Compare that to the shape `(?,)` -- we can't say anything about it's divisibility.

That divisibility could be used downstream for vectorization or validation purposes, but it is not recoverable from the `(?,)` shape.

Additionally, indexing each layout with an integer coordinate (i.e. treating both layouts as as array) should result in identical instruction sequences and performance characteristics because of the static evaluations.

### lw · 2026-08-18

I'm not an expert, but I thought that dynamic integers can carry divisibility information (e.g., `cute.sym_int32(divisibility=128)`, or `cute.assume(x, 128)`). Therefore I'd imagine that this dynamic coalesce can be done correctly and safely if we let the result be `(?{div=16}):(8)`. I updated the repro slightly to reflect that. WDYT?

### ccecka · 2026-08-18

It can, and it would be a valid solution to track that information in the new "dynamic" value rather than the existing extra mode. Until that is guaranteed though and that divisibility information can be properly taken advantage of in all subsequent operations, there is no cost to simply not coalescing the modes instead. The two representations -- `(16,?):(8,128)` and `?{div=16}:8` -- are completely isomorphic and I have no reason to prefer one over the other (except that one is a normal layout of static/dynamic integers and the other has a "special dynamic" value in it that potentially needs special care).

If you do find a concrete cost in evaluating or using `(16,?):(8,128)` vs `?:8` (or even `?{div=16}:8`), then that's the bug worth paying attention to. In all, `coalesce` is intended to be a "simplify" (for readability and human inspection) that does not change any actual concrete behavior or interactions with other operations.

### lw · 2026-08-18

The concrete situation where this came up, and posed a problem, was when preparing a TMA copy atom, as I needed some modes to be merged in order to get below the limit of 5 dimensions imposed by the hardware. In my situation the strides were scaled bases but I later realized that this occurred also with integer strides.

### ccecka · 2026-08-19

We have ways to account for that within TMA Builders -- constructing maps from each TMA Box mode to GMEM Tensor mode(s). A TMA Box is statically shaped, so once the box is determined, tiled out of GMEM, and reordered appropriately, then you can look for modes to coalesce.

### Pranshu-Bahadur · 2026-08-19

> It can, and it would be a valid solution to track that information in the new "dynamic" value rather than the existing extra mode. Until that is guaranteed though and that divisibility information can be properly taken advantage of in all subsequent operations, there is no cost to simply not coalescing the modes instead. The two representations -- `(16,?):(8,128)` and `?{div=16}:8` -- are completely isomorphic and I have no reason to prefer one over the other (except that one is a normal layout of static/dynamic integers and the other has a "special dynamic" value in it that potentially needs special care).
> 
> If you do find a concrete cost in evaluating or using `(16,?):(8,128)` vs `?:8` (or even `?{div=16}:8`), then that's the bug worth paying attention to. In all, `coalesce` is intended to be a "simplify" (for readability and human inspection) that does not change any actual concrete behavior or interactions with other operations.

Hey @ccecka! Please correct me if I am wrong, but this is because there is no integer divide over a Shape right?

@lw If it helps, you could try using a 1D formulation with your own indexing formula (in a way you can choose to view the physical GMEM layouts however you like), once you have a concrete formula maybe you wont need to abstract it away? (ND->1D, think of how swizzles are laid out). 

Thank you again, sorry I'm immersed in the CuTe papers and seeing how the formulation raises questions in practise was super insightful!

### lw · 2026-08-20

@ccecka Thanks for the tips on TMA, I was able to reformulate this in a different way which sidesteps the issue above.

However, this has led me to a new instance of the same limitation with coalescing a dynamic layout. This time, I need to "flatten" (in PyTorch parlance) a layout so that it becomes 1-d as otherwise it cannot be used as a lhs for cute.composition. cute.coalesce should be the right tool for it, except that for dynamic layouts it returns a 2-d output instead of the expected 1-d one. Here's a self-contained repro:
```py
import torch
import cutlass.cute as cute
from cutlass.cute.runtime import from_dlpack


@cute.jit
def repro(tensor: cute.Tensor):
    expected = cute.make_layout((cute.size(tensor)))
    actual = cute.coalesce(tensor.layout)

    print(f"{expected=}")
    print(f"{actual=}")

    print(f"{cute.composition(expected, cute.make_layout((256, 192)))=}")
    print(f"{cute.composition(actual, cute.make_layout((256, 192)))=}")


tensor = from_dlpack(torch.empty((256, 192), device="cuda").t())
# Comment this out to make the repro pass
tensor = tensor.mark_compact_shape_dynamic(mode=1)
repro(tensor)
```
With dynamic inputs it prints:
```text
expected=?{div=192}:1
actual=(192,?):(1,192)
cute.composition(expected, cute.make_layout((256, 192)))=(256,192):(1,256)
loc("print(f\22{cute.composition(actual, cute.make_layout((256, 192)))=}\22)"("/home/lcw/repro_coalesce.py":15:13)): error: unable to compute the following composition: '!cute.layout<"(192,?):(1,192)">' o '!cute.layout<"(256,192):(1,256)">'
```
With static inputs it prints:
```text
expected=49152:1
actual=49152:1
cute.composition(expected, cute.make_layout((256, 192)))=(256,192):(1,256)
cute.composition(actual, cute.make_layout((256, 192)))=(256,192):(1,256)
```

### ccecka · 2026-08-20

> so that it becomes 1-d as otherwise it cannot be used as a lhs for cute.composition

Why can't it be used as a LHS for cute.composition?

### lw · 2026-08-21

Have you looked at my previous repro? I put the error message in the logs. It's:
```
error: unable to compute the following composition: '!cute.layout<"(192,?):(1,192)">' o '!cute.layout<"(256,192):(1,256)">'
```

### ccecka · 2026-08-21

I see, interesting point. I agree that is an instance of a false divisibility condition and I can see why you would want the weaker version of coalesce... I'll keep this in mind.

As a quick work-around, you could always do a two-step to statically tile the `?` mode first:
```
composition(Layout((192,?), (1,192)), (192,256))                  =>  (192,256):(1,192)
composition(Layout(Layout((192,256), (1,192)), Layout((256,192))) =>  (256,192):(1,256)
or
composition(Layout((192,?), (1,192)), 192*265)   =>  49152:1
composition(Layout(49152, 1), Layout((256,192))) =>  (256,192):(1,256)
```

### ccecka · 2026-08-27

As an update, I agree with the analysis in this thread and this behavior is now (conditionally) supported in PyCuTe:
https://github.com/NVlabs/CuTe/commit/eb530435472d9b7af53ee3e8883d4e504a963ea5
where the merge condition now only checks for determinism/purity, which fails for an opaque handle (e.g. `? * 4 -> ?`).

Very interesting, thank you.

### github-actions[bot] · 2026-09-26

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.
