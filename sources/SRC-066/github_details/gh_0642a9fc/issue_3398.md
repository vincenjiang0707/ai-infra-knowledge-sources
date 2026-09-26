# [Issue #3398] [Feature] cute.compile hardcodes no_cache=True, disabling the DSL's content-addressed compile cache

source: https://github.com/NVIDIA/cutlass/issues/3398
state: open | updated: 2026-09-03T01:29:33Z
labels: 

## 正文

### Summary

The explicit compile entry point in the CuTeDSL Python runtime unconditionally forces
`no_cache=True`, so the DSL's own content-addressed on-disk MLIR cache never engages for
`cute.compile`. Every process that compiles the same kernel re-runs the full MLIR build from
scratch, even though a byte-identical artifact already exists on disk.

### Where

`python/CuTeDSL/cutlass/base_dsl/compiler.py`, in `_compile()` (the shared path behind
`cute.compile`):

```python
# compiler.py:1318-1319
kwargs["compile_only"] = True
kwargs["no_cache"] = True
```

`no_cache` is set on **every** call, overriding anything the caller passed and bypassing the
cache machinery the DSL otherwise maintains. There is no argument or environment override that
reaches this line.

Observed on `nvidia-cutlass-dsl` 4.5.2; the same two lines are present on `main` (4.6).

### Impact

We serve an inference engine whose attention kernels are `@cute.jit` functions compiled via
explicit `cute.compile` at startup. Because `no_cache=True` is forced, each server process pays
the full MLIR compile on every boot:

- Cold boot (no cache possible): ~506 s to ready.
- With the DSL cache re-enabled externally (we wrap `generate_mlir` to clear the forced flag):
  warm boot ~58 s — **an ~8.7× boot-time reduction**, with the reloaded artifacts verified
  byte-identical (same on-disk files, unchanged mtimes, zero new writes).

So the cache the DSL already implements recovers almost all of the compile cost — it's just
switched off at this one call site. Working around it requires wrapping an internal method whose
signature is not a stable API, which is fragile across DSL releases.

### Requested change

Stop unconditionally forcing `no_cache=True` in `_compile()`. Any of these would resolve it:

1. Honor a caller-supplied `no_cache` (only default it when unset), or
2. Gate it on an environment variable (e.g. `CUTE_DSL_COMPILE_CACHE=1`), consistent with the
   existing `CUTE_DSL_*` option surface, or
3. Enable the content-addressed cache by default for the explicit `cute.compile` path — its key
   already includes traced IR + target arch + toolkit version, so stale replay is not possible.

Illustrative sketch:

```diff
-        kwargs["compile_only"] = True
-        kwargs["no_cache"] = True
+        kwargs["compile_only"] = True
+        kwargs.setdefault("no_cache", _env_default_no_cache())  # respect caller / CUTE_DSL_* env
```

### Reproduce

Compile any `@cute.jit` function via `cute.compile` twice, in two fresh processes, with a
persistent `CUTE_DSL` cache directory set. The second process still performs a full MLIR compile
rather than a cache hit, because `_compile()` forces `no_cache=True`. Happy to provide a
self-contained repro script.

---

cc @Junkai-Wu — you appear as the author on the CuTeDSL mirror drops (e.g. #3362); apologies if
this isn't your area — if so, could you help route it to whoever owns the DSL compiler path? Thanks.


## 评论 (3)

### aryanputta · 2026-07-22

Looking at this on current `main`, the `no_cache` assignment is not the only thing disabling the cache.

`cute.compile` sets both flags together (`base_dsl/compiler.py:1318-1319`):

```python
kwargs["compile_only"] = True
kwargs["no_cache"] = True
```

and `_setup_common` then re-derives it independently (`base_dsl/dsl.py:2611-2612`):

```python
if not no_cache and compile_only:
    no_cache = True
    self.print_warning("Cache is disabled as user wants to compile only.")
```

Since `cute.compile` always sets `compile_only=True`, removing the `compiler.py` override on its own will not re-enable the content-addressed cache. Every `cute.compile` still lands in that second branch.

On whether compile-only results are cacheable at all: `compile_only` appears to only bypass execution. `dsl.py:2333-2334` returns `jit_function` directly instead of calling `run_compiled_program`, and `get_module_hash` (`dsl.py:1655`) keys on the module bytecode plus the envar values plus the compile options, so two builds that produce identical IR would legitimately map to the same entry.

The one thing I cannot rule out by reading is the relaxed argument path. Under `compile_only`, host arguments may be type-only placeholders with no execution arguments (`dsl.py:1286-1298`), and the cached function carries `dynamic_args` / `dynamic_kwargs` alongside the IR module. If two builds can produce identical IR but different dynamic-argument records, then sharing a cache entry between a compile-only build and a normal execution build would be unsafe, which would explain the gate as a deliberate guard rather than an oversight.

So the question is whether the `compile_only` implies `no_cache` rule is a correctness guard or just conservative.

What I would do, depending on the answer:

- If it is conservative: stop `compiler.py` from clobbering a caller-supplied `no_cache`, drop the `compile_only` implication in `_setup_common`, and add a test that compiles the same kernel in two separate processes and asserts the second one hits the on-disk cache instead of rebuilding.
- If it is a real guard: leave the guard's intent intact but fold the compile-only distinction into the cache key so the two build modes cannot collide, which gets the caching benefit without the aliasing risk.

Could I work on this? Happy to take whichever direction you prefer.


### github-actions[bot] · 2026-08-21

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### Junkai-Wu · 2026-09-03

@brandon-yujie-sun to take a look.
