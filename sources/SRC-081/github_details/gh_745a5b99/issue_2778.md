# [Issue #2778] [Bug]: Python 3.14 incompatibility via pydantic eval_type_backport on Recipe.dict()

source: https://github.com/vllm-project/llm-compressor/issues/2778
state: closed | updated: 2026-08-31T15:45:24Z
labels: 

## 正文

## Summary

Importing `llmcompressor` on Python 3.14 raises `TypeError: 'function' object is not subscriptable` at class-creation time in `recipe.py`, making the package completely unusable on Python 3.14.

## Reproduction

**Environment:**
- Python 3.14.4
- pydantic 2.13.4 (latest stable)
- llm-compressor at `8dc48513` (current `main`)

```bash
pytest tests/sparsity/test_module.py -v
```

The failure occurs at import, before any test runs. Trimmed traceback (verified on clean `upstream/main` checkout with no local changes):

```
ERROR tests/sparsity/test_module.py
src/llmcompressor/recipe/recipe.py:27: in <module>
    class Recipe(BaseModel):
        [pydantic model construction]
        ...
    evaluated = typing._eval_type(...)
    value = forward_ref.evaluate(...)
    return eval(code, globals=globals, locals=locals)
TypeError: 'function' object is not subscriptable
Unable to evaluate type annotation 'dict[str, Any]'.
```

## Root cause

`Recipe` (in `recipe.py:27`) defines both an `args: dict[str, Any]` field and a `def dict(self, ...)` method. On Python 3.14, annotations are evaluated lazily (PEP 649 semantics), so when Pydantic's `eval_type_backport` resolves `dict[str, Any]` it looks up `dict` in the class namespace — where it finds the method instead of the builtin — and raises `TypeError`.

This is a known interaction between Python 3.14 and pydantic ≤ 2.13.x. Relevant upstream history:
- **pydantic/pydantic#13036** — same error triggered by a `type` method shadowing the builtin on Python 3.14+
- **pydantic/pydantic#13097** — root-cause analysis: `dict` (or any builtin) method shadowing breaks `eval_type_backport` annotation evaluation
- **pydantic/pydantic#13070** — the refactor that introduced the regression (`safe_get_annotations` switched from `__dict__` to `getattr`)
- **pydantic/pydantic#13133** — the fix: removes `eval_type_backport()` entirely; merged into pydantic `main`, shipping with **pydantic v2.14.0** (currently only in `v2.14.0a1` — no stable release yet)

Since pydantic is a transitive dependency here (not pinned in `setup.py`), there is no released pydantic version that resolves the issue today.

## Proposed fix

Add a temporary `<3.14` cap to `python_requires` in `setup.py` as a holding pattern until pydantic 2.14.0 stable ships:

```python
# TODO: remove <3.14 cap once pydantic >= 2.14.0 is released (see pydantic/pydantic#13133)
python_requires=">=3.10,<3.14",
```

`setup.py` already declares `python_requires=">=3.10"` with no upper bound, so this is a one-line change. Happy to open that PR if it's the preferred direction.

## Longer-term note

`Recipe.dict()` (`recipe.py:232`) is a deprecated Pydantic API — `model_dump()` is the current equivalent. Removing or renaming that method would eliminate the builtin shadow and fix the Python 3.14 failure without a version cap and without waiting on pydantic 2.14.0 stable. Leaving the call on whether to pursue that to the maintainers.

## 评论 (1)

### kylesayrs · 2026-06-08

Thank you for the insightful analysis! Are there any other options that you are aware of for resolving this conflict?
