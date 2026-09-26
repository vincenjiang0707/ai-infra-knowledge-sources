# [Issue #3506] CuTeDSL: staged bool() with no arguments crashes the preprocessor with a raw IndexError

source: https://github.com/NVIDIA/cutlass/issues/3506
state: closed | updated: 2026-09-22T06:39:51Z
labels: bug, CuTe DSL

## 正文

### Description

`visit_Call` in `cutlass/base_dsl/ast_preprocessor.py` (~line 1971-1987) rewrites a staged `bool(...)` call into the DSL's `bool_cast` redirector using `args=[node.args[0]]` without checking that an argument is present. A jit body containing `z = bool()` therefore dies with a raw `IndexError: list index out of range` from inside the preprocessor instead of a proper diagnostic, while the one-argument case goes through `bool_cast` and produces a clean `DSLUserCodeError` when the argument is not convertible.

Verified against `nvidia-cutlass-dsl==4.7.0`; the repo source has the same unguarded `node.args[0]`.

```python
@cute.jit
def f() -> cutlass.Boolean:
    z = bool()
    return cutlass.Boolean(z)
```

Actual: `IndexError: list index out of range` (no location info, no suggestion).
Expected: a DSL diagnostic, e.g. `DSLUserCodeError` explaining that `bool()` requires exactly one argument.

### Suggested fix

Guard the rewrite: if `len(node.args) != 1 or node.keywords`, leave the call alone (or raise a proper `DSLUserCodeError` naming the file/function), so the failure carries a normal Python error message instead of an internal IndexError.


## 评论 (2)

### brandon-yujie-sun · 2026-09-01

Thanks for reporting the issue. We got a fix, and will include it in next release.

### brandon-yujie-sun · 2026-09-22

@VaggelisGian this is fixed in 4.8. Let us know if you still see issues.
