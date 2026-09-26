# [Issue #894] `pd.concat(..., copy=False)` in `src/utils/file_io.py` emits Pandas4Warning on pandas ≥3.0 — drop the deprecated `copy` keyword

source: https://github.com/ROCm/rocprofiler-compute/issues/894
state: closed | updated: 2026-08-25T01:17:11Z
labels: 

## 正文

## Summary

`src/utils/file_io.py` calls `pd.concat(..., copy=False)` in two places,
which is deprecated in pandas 3.0:

| File | Line |
|---|---|
| `src/utils/file_io.py` | 238 `final_df = pd.concat(dfs, keys=coll_levels, axis=1, join="inner", copy=False)` |
| `src/utils/file_io.py` | 317 `all = pd.concat([all, tmp_df[SE_idx]], axis=1, copy=False)` |

Verified on pandas 3.0.5:

```
>>> pd.concat([df1, df2], keys=["x", "y"], axis=1, join="inner", copy=False)
Pandas4Warning: The copy keyword is deprecated and will be removed in a
future version. Copy-on-Write is active in pandas since 3.0 which utilizes
a lazy copy mechanism that defers copies until necessary. Use .copy() to
make an eager copy if necessary.
```

`Pandas4Warning` is a `DeprecationWarning` subclass, so it is invisible
by default and does not fail CI — but it fires on every pmc raw-data
load and wave-occupancy collection under pandas ≥3.0, and the keyword
will be removed in a future version.

## Suggested fix: version-guarded branch

Guard the call on the pandas version — keep `copy=False` on pandas <3.0
(where it still skips copying intermediate data) and drop it on ≥3.0,
following the pattern used in NVIDIA/cuml#8142:

```python
if PANDAS_VERSION < Version("3.0"):
    final_df = pd.concat(dfs, keys=coll_levels, axis=1, join="inner", copy=False)
else:
    final_df = pd.concat(dfs, keys=coll_levels, axis=1, join="inner")
```

and the same shape at line 317.

with `PANDAS_VERSION = Version(pd.__version__)` at module level
(`packaging` is already a transitive dependency of pandas).

This is behaviour-preserving on every pandas version: the `copy`
keyword never affects the **result** of `concat`, only whether input
buffers are copied, and the branch keeps that behaviour exactly as it
was on each side of the boundary. Verified with runtime checks in
isolated venvs:

- pandas 2.3.3 takes the `copy=False` branch: identical results to
  today's code (`keys` MultiIndex / `join="inner"` and the `SE_idx`
  column append), no warning.
- pandas 3.0.5 takes the plain branch: no `Pandas4Warning` is emitted,
  results identical (the `copy` keyword is a documented no-op under
  Copy-on-Write).

## Installation does not bound pandas below 3.0

The project's pandas requirement has no upper bound below 3.0, so a
fresh install resolves pandas 3.x and the warning fires whenever these
code paths run.


## 评论 (1)

### xyf5432 · 2026-08-25

Following up on the maintainer's comment on PR #895: this repository is archived and development has moved to ROCm/rocm-systems (`projects/rocprofiler-compute`).

I checked the migrated tree: it pins `pandas==2.2.3` in `requirements.txt`, so pandas ≥3.0 can never resolve there — the deprecated `copy=False` keyword of `pd.concat` will not emit `Pandas4Warning` under that pin. The issue therefore does not apply to the migrated repository, and I am closing it.

Thanks for the work on this project!
