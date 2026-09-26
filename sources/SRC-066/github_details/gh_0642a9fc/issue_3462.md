# [Issue #3462] [BUG] CuTe DSL 4.7.0: import-time CUTE_DSL_LIBS env write breaks Slurm jobs on other machines

source: https://github.com/NVIDIA/cutlass/issues/3462
state: closed | updated: 2026-09-01T07:05:09Z
labels: 

## 正文

**Component:** CuTe DSL
**Version:** nvidia-cutlass-dsl 4.7.0 (regression vs 4.5.3, which does not touch the environment)

## Bug

**This breaks Slurm-style clusters where the submitter's environment is forwarded to jobs on other machines** (Slurm `sbatch` defaults to `--export=ALL`). Two new behaviors in 4.7.0 combine:

**1. `import cutlass` mutates `os.environ`.** `_select_and_load_cutlass_ir_toolkit` (`cutlass/_mlir/_mlir_libs/__init__.py`) prepends the absolute path of the chosen `libcute_dsl_runtime.so` — inside the importing interpreter's site-packages — to `CUTE_DSL_LIBS`:

```console
$ python -c "import os, cutlass; print(os.environ.get('CUTE_DSL_LIBS'))"
/path/to/submitter/venv/site-packages/nvidia_cutlass_dsl/cu12/lib/libcute_dsl_runtime.so
```

A launcher that merely imports `cutlass` while preparing a job therefore ships a submitter-machine-local path to every worker.

**2. Workers hard-fail on the stale entry, despite having a valid runtime.** On the worker, `import cutlass` prepends its own (valid) path — but `get_shared_libs` (`cutlass/base_dsl/dsl.py`) raises on the first missing entry, so every `cute.compile` dies even though the first entry in the list is a good local runtime:

```console
$ CUTE_DSL_LIBS=/nonexistent/libcute_dsl_runtime.so python - <<'EOF'
import cutlass, cutlass.cute as cute
from cutlass import Int32

@cute.jit
def trivial(a: Int32):
    pass

cute.compile(trivial, Int32(0))
EOF
FileNotFoundError: [Errno 2] No such file or directory: '/nonexistent/libcute_dsl_runtime.so'
```

Reproduced on GB300 (aarch64, Python 3.13, split wheels `-libs-core`/`-libs-cu12` 4.7.0). Upgrading 4.5.3 → 4.7.0 took down two independent launch pipelines on our Slurm cluster in one night; the failing jobs never referenced `CUTE_DSL_LIBS` themselves.

## Expected behavior

- Importing a library shouldn't write machine-local absolute paths into the process environment — keep the chosen runtime path in module state instead.
- `get_shared_libs` should skip missing entries with a warning and fall back to auto-discovery (which resolves correctly here), raising only when *no* usable runtime is found — preserving the diagnostics intent of #3329 without turning an inherited stale entry into a hard crash.


## 评论 (3)

### anakinxc · 2026-08-15

Thanks for reporting, working on this.

### yentur · 2026-08-16

Opened #3466 with the `get_shared_libs` half of this: missing `CUTE_DSL_LIBS` entries are skipped with a warning and auto-discovery is retried, so an inherited stale path is no longer fatal when a valid runtime is present. The hard failure from #3329 still fires when nothing usable is found.

@anakinxc you said you were already working on this, so please just close mine if it duplicates your fix. I went ahead mainly because the repro and the regression test were already written.

I could not touch the other half. The import-time write is in `cutlass/_mlir/_mlir_libs/__init__.py`, which is not in this repository, so the submitter-local path is still exported to workers.

### brandon-yujie-sun · 2026-08-27

@sshleifer this is fixed in both 4.6.3 and 4.7.1
