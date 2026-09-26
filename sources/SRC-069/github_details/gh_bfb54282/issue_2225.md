# [Issue #2225] [API Usability] Support checks for all library components

source: https://github.com/flashinfer-ai/flashinfer/issues/2225
state: open | updated: 2026-09-19T17:50:50Z
labels: feature request, priority: should have (P1), testing

## 正文

Opening this as a tracker as we start applying our new Support Check decorator ([!1809](https://github.com/flashinfer-ai/flashinfer/pull/1809)) across the entire library.

([!2224](https://github.com/flashinfer-ai/flashinfer/pull/2224)) will be used to keep track for support checks in each operation:
- [ ] Attention
- [ ] MoE
- [ ] GEMM
- [ ] Communication 

## 评论 (1)

### 0z5a · 2026-09-19

Support checks for one communication API family are in #5345 (base `dc04f50c9aa3eabcdaa5feb0934edb3d85e9529a`), as the behaviour-test replacement for the placeholder in #2224.

Family: the unified AllReduce-fusion API in `flashinfer/comm/allreduce.py` — `create_allreduce_fusion_workspace` (`trtllm` / `mnnvl` / `auto`), `allreduce_fusion`, and `AllReduceFusionWorkspace.destroy`. `trtllm_ar.py` already deprecates its low-level create/run pair in favour of this one, and `allreduce.py` is where the only existing hard backend requirement and the auto heuristic live. The #2224 comm skeleton cannot be imported at this revision because two symbols it references no longer exist in `flashinfer/comm/__init__.py`.

The gap it closes: an explicit backend had **no** architecture validation. The workspace constructor allocated three IPC buffers plus a `cudaMalloc` and only then ran the JIT — which cannot build on SM89 — so the machine paid the allocation and had no handle to clean up. Now: capability metadata on the existing checks (with a `_mnnvl_workspace_check` mirroring the JIT arch families), a `_BACKEND_CHECKS` registry, the four query helpers in the existing `backend_requirement` shape (the no-choices case keeps raising `ValueError` rather than being reinterpreted), and two collective-free pre-rejection gates — unknown backend refused with no silent auto fallback, unsupported compute capability refused before any loader/allocator/workspace/collective work, and `auto` filtering its candidate list by capability. `run` and `destroy` are untouched.

```
python -m pytest -s -q tests/comm/test_comm_support_checks.py
# 12 passed, 3 skipped, 6 xfailed, 0 failed
```

The tests assert behaviour, not attribute presence: side-effect-free queries (loader, allocator, constructor, multicast, topology vote, `torch.cuda` and `torch.distributed` spies all armed to raise); SM89 rejection with the JIT loader, IPC allocator, both constructors and the topology vote proven empty; the SM90 dispatch half reaching the constructor with exact kwargs; three forwards on a `__new__`-built workspace with every probe raising, so exactly three launches occur; idempotent destroy after a policy refusal; and two spawned two-process rejection runs under a 120 s deadline with per-rank reasons. The five capability assertions also fail when the gate is deleted, so they are not vacuous.

Skipped/xfailed deliberately: real two-rank collective numerics and the Hopper-only positive path (no SM90 here and no CI lane runs this file), plus the tracker entries not converted yet, under `strict=True` so the ledger cannot silently pass. Still open from the tracker: rollback of a mid-allocation failure inside the deprecated allocator in `trtllm_ar.py` — that is an allocator restructure, so it stays with #2224. One behaviour change to flag: `create_allreduce_fusion_workspace(backend="auto", ...)` on SM89 now raises immediately instead of failing inside the JIT build after allocating; SM90/SM100/SM120 selection is unchanged.

