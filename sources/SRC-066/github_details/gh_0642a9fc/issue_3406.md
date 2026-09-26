# [Issue #3406] [CuTe DSL] setmaxregister_* can be silently dropped by ptxas (C7508) — nothing surfaces to Python; min_blocks_per_mp=1 prevents it

source: https://github.com/NVIDIA/cutlass/issues/3406
state: open | updated: 2026-09-13T03:17:53Z
labels: 

## 正文

---

**Describe the bug**

`cute.arch.setmaxregister_decrease/increase` emit `setmaxnreg` into the PTX.
When ptxas cannot determine the register count at kernel entry — which is the
common case for these kernels in our experience, though not universal — it
**ignores every `setmaxnreg` region** with only the build-time diagnostic:

```
ptxas info    : (C7508) Potential Performance Loss: 'setmaxnreg' ignored; unable to determine register count at entry.
```

The kernel compiles and runs correctly — but with a flat per-thread register
allocation instead of the requested warp-specialized budgets, and **nothing is
surfaced at the Python level**: no exception, no warning, no log line. The
C7508 text only exists inside the ptxas invocation, which is not surfaced by
default in the DSL workflow. Passing `min_blocks_per_mp=...` on the
`.launch(...)` (which emits `.minnctapersm` and pins down the entry register
count) reliably makes the requests take effect — in the reproducer below and
in every affected kernel we patched — but that interaction is not documented
on either API.

**Minimal repro** (nvidia-cutlass-dsl 4.6.1, CUDA 13.3, B200/sm_100a):

```python
<INSERT mini_c7508.py HERE>
```

Output on our machine:

```
variant A(default launch)     : PTX setmaxnreg sites=2  .minnctapersm=False  SASS USETMAXREG=0
    ptxas: ptxas info    : (C7508) Potential Performance Loss: 'setmaxnreg' ignored; unable to determine register count at entry.
    output correct: True
variant B(min_blocks_per_mp=1): PTX setmaxnreg sites=2  .minnctapersm=True  SASS USETMAXREG=2
    output correct: True
```

Variant A vs B is a one-argument difference in `.launch(...)`. In A the SASS
contains no `USETMAXREG` — the two `setmaxnreg` requests were dropped; in B
both are honored.

**How we hit it / impact**

We audited our production warp-specialized SM100 kernels
(attention-backward-style: producer warps shrink to a small budget, consumer
warpgroups grow) that had used `setmaxregister_*` for months. Of 11 kernel
instances that emitted `setmaxnreg` without `.minnctapersm`, **9 had the
requests silently dropped** (zero `USETMAXREG` in SASS); the other 2 were
honored anyway (ptxas evidently could bound the entry register count for
those), which makes the failure mode harder to notice — the same API pattern
works in one kernel and is a no-op in the next, with no visible difference at
the Python level. Adding `min_blocks_per_mp=1` at the launch (equivalently,
patching `.minnctapersm 1` into the dumped PTX) made `USETMAXREG` appear in
the SASS of every previously-dropped kernel. (Paired ABAB nsys A/B after the
fix: most kernels within ±2%; individual variants moved +3.8% / −4.1% — i.e.
the budgets were sometimes helping, sometimes actively mistuned, and we had
no way to know because the requests had never been in effect.)

The failure mode is nasty precisely because it is invisible: a
warp-specialized DSL kernel can ship with register budgeting that is a no-op,
and be validated and tuned against that wrong binary.

**Expected behavior**

Either of these would have caught it (in preference order):

1. **Make the diagnostic loud at the Python level.** The DSL drives the
   ptxas step; C7508 (and this one in particular, since it means a
   user-visible API had no effect) could be re-surfaced as a Python
   `warning`/log-error rather than swallowed build output. Alternatively (or
   additionally), a hard error / loud warning at trace time when
   `setmaxregister_*` is used and the launch does not specify
   `min_blocks_per_mp`.
2. **Consider auto-emitting `.minnctapersm` when `setmaxregister_*` is
   present and the launch omits `min_blocks_per_mp`.** We flag this as an
   option requiring maintainer judgment rather than a free win: a launch-bound
   directive is real compiler metadata (it can influence register allocation
   and spilling on its own), so silently injecting it trades one implicit
   behavior for another. The loud-diagnostic option has no such tradeoff.

A docs-only fix (documenting the interaction on `setmaxregister_*` and
`min_blocks_per_mp`) would be strictly better than today, but given the
silent-perf-loss failure mode we would argue for the loud diagnostic.

**Environment**: nvidia-cutlass-dsl 4.6.1, CUDA 13.3 (ptxas V13.3.33), B200
(sm_100a), Linux x86_64, Python 3.12.

**Offer**

We understand the authoritative fix for "unable to determine register count at
entry" lives inside ptxas, which is closed-source and out of reach from this
repo — that is why the request targets the DSL front end, which owns both the
launch metadata and the ptxas invocation and can therefore either supply
`.minnctapersm` or at least refuse to stay quiet. If option 1 (loud
warning/error) works for you, we are happy to send a PR:
trace-time detection of `setmaxregister_*` plus a loud warning/error when the
launch lacks `min_blocks_per_mp`. (Same DSL-meets-ptxas territory as #3389,
which we filed earlier.)

---

## 评论 (2)

### github-actions[bot] · 2026-08-23

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3618.
