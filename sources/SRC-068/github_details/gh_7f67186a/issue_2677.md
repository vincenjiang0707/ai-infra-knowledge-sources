# [Issue #2677] [Cute,Bwd,Sm100] Sparse MLA backward: two findings about dPsum stride divisibility and redundant elect

source: https://github.com/Dao-AILab/flash-attention/issues/2677
state: open | updated: 2026-07-02T06:10:22Z
labels: 

## 正文

Hey, flash-attention team:

While exercising the sparse-MLA backward (`flash_bwd_mla_sm100.py`, added in #2621 / commit `940cd96`) on SM100 with real tensors, we noticed two things in the stats (`ScaleP` / `dPsum`) bulk-copy path and found small changes that were helpful for us.

## Finding 1 — `dPsum` isn't given the same stride-divisibility assumption as its sibling stats tensors

The backward's input prep applies a 16-byte stride-divisibility assumption (`new_stride`) to the f32/bf16 inputs, including `mScaleP`, but `mdPsum` is left out of that list:
https://github.com/Dao-AILab/flash-attention/blob/940cd9680f3315f2f06b43ab5bea2c2cf2d96806/flash_attn/cute/flash_bwd_mla_sm100.py#L369-L379

As a result, `ScaleP`'s global→shared bulk copy can prove its source pointer is aligned and compiles, while the analogous `dPsum` copy cannot, and its compile-time pointer-alignment check fails on real tensors. I'm not sure if this is lan oversight rather than intentional. I find the FakeTensor path already declares `dPsum` divisible, which is why compile-only runs pass: https://github.com/Dao-AILab/flash-attention/blob/940cd9680f3315f2f06b43ab5bea2c2cf2d96806/flash_attn/cute/interface.py#L1152)

**Why the assumption looks valid for `dPsum`.** `ScaleP` and `dPsum` are similar per-`(batch, query, head)` f32 statistics (`ScaleP` carries an extra top-k-block axis), and both are laid out with `nheads` contiguous. So their non-contiguous strides are integer multiples of `nheads`, and the 16-byte-alignment assumption reduces to the same condition for both, which is already taken for `ScaleP` and holds for the MLA head counts in use. I think asserting it for `dPsum` doesn't introduce a new requirement; it just makes `dPsum` consistent with the other stats inputs.

**Suggested change:** include `mdPsum` in the `new_stride` list.

```python
-        mQv, mV, mdV, mdO, mP, mdS, mScaleP = [
+        mQv, mV, mdV, mdO, mP, mdS, mScaleP, mdPsum = [
             cute.make_tensor(mX.iterator, cute.make_layout(mX.shape, stride=new_stride(mX)))
             if mX is not None
             else None
-            for mX in (mQv, mV, mdV, mdO, mP, mdS, mScaleP)
+            for mX in (mQv, mV, mdV, mdO, mP, mdS, mScaleP, mdPsum)
         ]
```

---

## Finding 2 — the explicit `elect_one` around the bulk copy may be redundant

The stats bulk `cute.copy` is wrapped in an explicit `cute.arch.elect_one()`:
https://github.com/Dao-AILab/flash-attention/blob/940cd9680f3315f2f06b43ab5bea2c2cf2d96806/flash_attn/cute/flash_bwd_mla_sm100.py#L1490-L1494

A bulk copy is inherently issued by a single lane, and in the CuTe DSL programming model the framework will handle single-issuer election for this path. Electing a lane in the kernel on top of that is redundant and can deadlock when multiple elects are nested. As with `cute.gemm` using tcgen05 MMA atoms and `cute.copy` using asyn bulk tensor atoms, users shouldn't add their own elect in the kernel.

**Suggested change:** drop the explicit `elect_one` around this bulk copy.

```python
         if const_expr(bulk_copy):
-            with cute.arch.elect_one():
-                cute.copy(copy_atom, tXgX, tXsX, mbar_ptr=mbar_ptr)
+            cute.copy(copy_atom, tXgX, tXsX, mbar_ptr=mbar_ptr)
         else:
             cute.copy(copy_atom, tXgX, tXsX, tma_bar_ptr=mbar_ptr)
```

## What we saw with both changes
On SM100, the real-tensor sparse-MLA backward then compiles and runs end-to-end, with `dQ/dK/dV/dQv` matching the reference within bf16 tolerance and no stall.

These may not be the ideal changes for your desig. We're sharing the observations and what worked for us. Happy to discuss here and send a PR with the two changes if they look reasonable.


## 评论 (9)

### jayhshah · 2026-06-26

1. the `mdPsum` alignment omission was an oversight and it's harmless to add this, thanks for catching this. However, since we use cp async bulk (`CopyBulkG2SOp`) to copy in these tensors, we shouldn't need to stipulate 128 bit alignment just as in the main `flash_bwd_sm100.py` which has no alignment divisibility check on `mdPsum`. In any case the tests `test_flash_attn_mla_absorbed_varlen` pass for me on main as it stands.

2. We've always used `with cute.arch.elect_one()` around copy with `CopyBulkG2SOp`, like in the main `flash_bwd_sm100.py`: https://github.com/Dao-AILab/flash-attention/blob/82d6441eec5d4dfec120153db2c0145ae855a083/flash_attn/cute/flash_bwd_sm100.py#L1970

Removing this hangs the kernel, so I don't understand your report.

### tridao · 2026-06-26

`CopyBulkG2SOp` (i.e. cp.async.bulk) requires `elect_one` as that elect is not done internally in cute-dsl. In contrast to `CopyBulkTensorTileG2SOp` (i.e. cp.async.bulk.tensor) where internally in cute-dsl one thread is elected.

### dongxiao92 · 2026-06-26

> `CopyBulkG2SOp` (i.e. cp.async.bulk) requires `elect_one` as that elect is not done internally in cute-dsl. In contrast to `CopyBulkTensorTileG2SOp` (i.e. cp.async.bulk.tensor) where internally in cute-dsl one thread is elected.

Exactly. We missed that during the lowering of cute.copy for CopyBulkG2SOp and other a few non-tile bulk copy atoms. We tried to fix this bug in following cute-dsl release and noticed this nested elect case

### tridao · 2026-06-26

Cool, whenever that version is released we'll update and remove the `elect_one`

### dongxiao92 · 2026-06-26

> Cool, whenever that version is released we'll update and remove the `elect_one`

Thanks for the support. We'll also test the kernels and confirm the impacted code and expected changes with you before the release.

> However, since we use cp async bulk (CopyBulkG2SOp) to copy in these tensors, we shouldn't need to stipulate 128 bit alignment just as in the main flash_bwd_sm100.py which has no alignment divisibility check on mdPsum. In any case the tests test_flash_attn_mla_absorbed_varlen pass for me on main as it stands.

I hit a compilation error with new cute-dsl nightly packages. It's related to the failure of deducing the expected 16B alignment of sliced`mdPsum` in the `CopyBulkG2SOp`. In this case, I find attaching the `div=4 ` information could help the alignment deduction and propagate the correct alignment alongside.
I'm also working on locating the changes in cute-dsl side that trigger this issue.

### jayhshah · 2026-06-26

Yes, that makes sense and we should just add it for mdPsum in both the backward kernels and for mLSE in `flash_bwd_sm100.py`. Do you see the same problem for ordinary attention backward?

### dongxiao92 · 2026-06-26

> Yes, that makes sense and we should just add it for mdPsum in both the backward kernels and for mLSE in `flash_bwd_sm100.py`. Do you see the same problem for ordinary attention backward?

Havn't checked more kernels yet. I could check others after the current investigation for this one on cute-dsl side

### dongxiao92 · 2026-06-29

I have draft this PR(https://github.com/Dao-AILab/flash-attention/pull/2689) to remove the nest elect_one and do testing on that with new cute-dsl wheels. I believe it will cause funtional issues like deadlocks with current and old cute-dsl packages.
Kindly ask what's the recommended flow to land changes like this?

### dongxiao92 · 2026-07-02

Hey, cutlass-dsl 4.6 is live here:https://pypi.org/project/nvidia-cutlass-dsl/4.6.0/
The 2 PRs to fix the nest elect_one are unblocked. Please help to review, thanks!

- https://github.com/Dao-AILab/quack/pull/164
- https://github.com/Dao-AILab/flash-attention/pull/2689
