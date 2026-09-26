# [Issue #2992] [BUG][Fuzzer][ice-on-valid-code] Public builtin T.sync_global() aborts CUDA codegen with an internal LOG(FATAL)

source: https://github.com/tile-ai/tilelang/issues/2992
state: open | updated: 2026-08-27T17:00:31Z
labels: 

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported.

### What version of TileLang are you using?

0.1.13

### System information

```
3.13.13 linux
tilelang 0.1.13
torch 2.13.0+cu130
cuda 13.0
gpu NVIDIA L40S (sm_89)
```
Installed via pip into an isolated venv.

### Problem description

`T.sync_global()` is a public language builtin — exported through `tilelang.language` in `__all__` and carrying the docstring *"Synchronize all threads in the entire grid."* Any valid kernel that calls it aborts compilation during CUDA device codegen with an internal fatal error:

```
tvm.error.InternalError: Global storage sync is no longer supported
```

The frontend lowers `T.sync_global()` to a `"global"`-scope `tvm_storage_sync`, and the `"global"` branch of TileLang's CUDA `PrintStorageSync` is now a bare `LOG(FATAL)` — the global-barrier codegen that once backed it was removed, but the public builtin was left in place. So the backend unconditionally kills any program that reaches this API. This is a compiler abort on a valid, exported API call, not a Python-level error the user can catch at trace time.

The documented sibling `T.sync_grid()` compiles and runs correctly (control below), so grid-wide synchronization *is* available — just not through `sync_global`.

### Reproducible example code

```python
import tilelang, tilelang.language as T, torch

N = 32

@T.prim_func
def main(A: T.Tensor((N,), "float32"), B: T.Tensor((N,), "float32")):
    with T.Kernel(1, threads=N) as bx:
        for i in T.Parallel(N):
            B[i] = A[i]
        T.sync_global()          # public builtin, exported in __all__

k = tilelang.compile(main, out_idx=[1])   # aborts here
a = torch.arange(N, dtype=torch.float32, device="cuda")
print(k(a).cpu())
```

Output (0.1.13, L40S sm_89):
```
tx ty tz 1 32 1
...
  File "<unknown>", line 0, in tvm::codegen::CodeGenTileLangCUDA::PrintStorageSync(...)
  File "<unknown>", line 0, in tvm::runtime::detail::LogFatal::~LogFatal()
tvm.error.InternalError: Global storage sync is no longer supported
```

<details>
<summary>Control: identical kernel with <code>T.sync_grid()</code> compiles + runs correctly</summary>

```python
import tilelang, tilelang.language as T, torch
N = 32
@T.prim_func
def main(A: T.Tensor((N,), "float32"), B: T.Tensor((N,), "float32")):
    with T.Kernel(1, threads=N) as bx:
        for i in T.Parallel(N):
            B[i] = A[i]
        T.sync_grid()            # documented sibling
k = tilelang.compile(main, out_idx=[1])
a = torch.arange(N, dtype=torch.float32, device="cuda")
assert torch.allclose(k(a).cpu(), a.cpu())   # passes
# emitted CUDA contains: cooperative_groups::this_grid().sync();
```
Removing the sync call entirely also compiles and runs correctly, so only the `T.sync_global()` call triggers the abort.
</details>

### Traceback

```
tx ty tz 1 32 1
2026-... [TileLang:tilelang.jit.kernel:INFO] TileLang begins to compile kernel `main` with `out_idx=[1]`
  File ".../tilelang/backend/device_codegen.py", line 22, in build
    return tvm.ffi.get_global_func(global_func_name)(mod, target)
  File "<unknown>", line 0, in tvm::codegen::BuildTileLangCUDA(tvm::IRModule, tvm::Target)
  File "<unknown>", line 0, in tvm::codegen::CodeGenTileLangCUDA::AddFunction(...)
  File "<unknown>", line 0, in tvm::codegen::CodeGenTileLangCUDA::PrintStorageSync(tvm::tirx::CallNode const*)
  File "<unknown>", line 0, in tvm::runtime::detail::LogFatal::~LogFatal()
tvm.error.InternalError: Global storage sync is no longer supported
```

### Expected behavior

A public, exported builtin should not abort the compiler with an internal `LOG(FATAL)` on a valid kernel. Since `T.sync_grid()` already provides working grid-wide synchronization (it compiles to `cooperative_groups::this_grid().sync();`) and the codegen message states global storage sync is intentionally gone, the evidence suggests one of: route `sync_global()` to the same lowering as `sync_grid()`; or, if it is meant to be retired, remove it from the public API / have it raise a normal `NotImplementedError` at trace time (pointing users at `sync_grid()`) rather than reaching the backend fatal. Which is appropriate depends on whether `sync_global` is intended to stay — a call for the maintainers.

### Additional context

**Root cause.** `T.sync_global()` lowers to a `"global"`-scope `tvm_storage_sync`, and TileLang's CUDA codegen handles that scope with an unconditional `LOG(FATAL)` while the builtin is still public and exported. `PrintStorageSync` handles `"warp"`, `"shared"`/`"shared.dyn"`, and `"cluster"` normally (verified in source at `codegen_cuda.cc#L1509-L1542`: `warp`→`__syncwarp`, `shared`→`__syncthreads`, `cluster`→`tl::cluster_sync()`); only `"global"` is a dead fatal, and nothing else in codegen ever emits the `"global"` scope, so the branch is reachable only through `sync_global`. Class = a public API wired to a removed/dead backend branch (the sibling storage-sync scopes all lower correctly; only this one aborts).

- Frontend: [`tilelang/language/builtin.py#L1182-L1188`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/builtin.py#L1182-L1188)
- Public export (`__all__`): [`tilelang/language/common.py#L273`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/common.py#L273)
- Backend fatal: [`src/cuda/codegen/codegen_cuda.cc#L1541-L1542`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L1541-L1542)
  ```cpp
  } else if (sync == "global") {
    LOG(FATAL) << "Global storage sync is no longer supported";
  }
  ```

<details>
<summary>Two secondary frontend defects in <code>sync_global</code> (latent today because codegen aborts first)</summary>

Both are in the builtin body and only matter if the `LOG(FATAL)` is ever lifted, but they are worth cleaning up with the fix:

1. **Leftover debug `print`** ([`builtin.py#L1186`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/builtin.py#L1186)): `print(tx, ty, tz, ex, ey, ez)` fires on every call — verified this session, it prints `tx ty tz 1 32 1` to stdout during tracing.
2. **`tx == 0 and ty == 0 and tz == 0` uses Python `and` over `PrimExpr`s** ([`builtin.py#L1187`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/language/builtin.py#L1187)). Python `and` over comparison-proxy expressions is unsafe: on 0.1.13, calling `bool()` on `tx == 0` raises `ValueError: Cannot use and / or / not operator to Expr, hint: use tvm.tirx.all / tvm.tirx.any` (verified this session in a traced kernel), so this line is fragile — it should use `tirx.all(tx == 0, ty == 0, tz == 0)` rather than Python `and`. (I could not deterministically reproduce a *silent* collapse to just `tx == 0` on 0.1.13; the `and`-over-`Expr` idiom is simply the wrong construct.)
</details>

<details>
<summary>Generalization tested this session (v0.1.13, L40S) — adjacent storage-sync scopes</summary>

The "adjacent cells" for this defect are the other storage-sync scopes and the sibling grid-sync API:

| API / scope | observed |
|---|---|
| `T.sync_global()` → `"global"` scope | crash: `InternalError: Global storage sync is no longer supported` (+ leftover `tx ty tz 1 32 1` print) |
| `T.sync_grid()` (documented sibling) | COMPILE_OK, emits `cooperative_groups::this_grid().sync();`, numerically matches input |
| no sync call | COMPILE_OK |
| `"warp"`/`"shared"`/`"cluster"` scopes (source-verified in `PrintStorageSync`) | handled normally (`__syncwarp`/`__syncthreads`/`tl::cluster_sync()`) |

Only the `"global"` scope — reachable solely through the public `sync_global` builtin — is a dead `LOG(FATAL)`. Distinct root from the frontend `__pos__` gap and the missing half-precision math lowering; kept as its own specific report.
</details>

**Impact.** The trigger is narrow (a single call to the public `sync_global` builtin — no exotic ingredient — and no example/test exercises it, so CI stays green) but the API is exported in `__all__` and documented "synchronize all threads in the entire grid." When it fires the failure is an internal `LOG(FATAL)` at CUDA codegen: it aborts compile, produces no wrong data, and blocks that one kernel from building. It cannot reach production as a silent miscompile, but any user who reaches for grid-wide sync and picks `sync_global` (rather than `sync_grid`) hits an uncatchable backend abort on first compile instead of a working lowering or a clean trace-time diagnostic.

**Suggested fix.** Either route `sync_global()` through the same lowering as `sync_grid()` (in `builtin.py`, emitting the `cooperative_groups::this_grid().sync()` path), or, if the builtin is retired, drop it from `__all__` and have the frontend raise `NotImplementedError` at trace time pointing at `sync_grid()` — instead of letting the call reach the backend `LOG(FATAL)`. The two secondary frontend defects noted above should be cleaned up alongside either choice.

**Provenance.** `sync_global` and the `"global"` codegen branch were introduced in [#2166](https://github.com/tile-ai/tilelang/pull/2166) (merged 2026-05-12, `431c85f1`). The `LOG(FATAL) << "Global storage sync is no longer supported"` line was set in [#2216](https://github.com/tile-ai/tilelang/pull/2216) *"[TIR][IR] Update to use tirx"* (merged 2026-05-20, `b939fa01`) — that refactor replaced the branch's prior body with the fatal but left the public `sync_global` builtin in place. Present in every release after #2216; not a recent regression.

**Dedup.** I searched the live tracker this session (open and closed issues and PRs, plus the local filed ledger): zero issues for `sync_global`, `"Global storage sync"`, or `barrier_expect`. The only PR hits are false positives (#811 changed only the `sync_global` docstring; #741 merged the ThreadPartialSync/ThreadStorageSync passes with `def sync_global()` unchanged context; #1421 adds a `"global"` branch in a different backend with a different message). Not in `bugs/FILED_ISSUES.md` / `bug_catalog_ext.json`.

**Reach.** The trigger is a single call to a public, exported builtin — no exotic ingredient. At `v0.1.13` `sync_global` appears in exactly two places, its definition and its `__all__` re-export; `grep -rn sync_global` finds zero uses in `examples/`, `testing/`, `benchmark/`, or `docs/`, which is why no test exercises it and CI stays green — but the symbol is public, so any user who reaches for grid-wide sync and picks `sync_global` (rather than `sync_grid`) hits the abort on the first compile.

## 评论 (1)

### rishabhsinha17 · 2026-08-27

Before opening a PR for this: which direction do you prefer? Option A: lower `sync_global()` to the same `cooperative_groups::this_grid().sync()` path as `sync_grid()` (change in `tilelang/language/builtin.py:1182`, after which the dead `"global"` branch at `src/cuda/codegen/codegen_cuda.cc:1591-1592` can be dropped). Option B: retire it cleanly, i.e. remove it from `__all__` and raise a trace-time error at `builtin.py:1182` pointing users to `T.sync_grid()`, so the call never reaches the backend `LOG(FATAL)`. Happy to implement either; both are small.

