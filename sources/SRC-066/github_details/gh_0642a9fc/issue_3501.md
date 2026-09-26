# [Issue #3501] CuTeDSL: print_warning_once re-warns when more than one distinct message is used (lru_cache maxsize=1)

source: https://github.com/NVIDIA/cutlass/issues/3501
state: open | updated: 2026-09-13T04:55:02Z
labels: CuTe DSL

## 正文

### Description

`BaseDSL.print_warning_once` (`cutlass/base_dsl/dsl.py` ~line 813) caches on `(self, message)` with `@lru_cache(maxsize=1)`:

```python
@lru_cache(maxsize=1)
def print_warning_once(self, message: str) -> None:
```

With more than one distinct message, every new message evicts the previous cache entry, so alternating messages re-warn forever instead of once each.

Repro against `nvidia-cutlass-dsl==4.7.0`:

```python
import warnings
from cutlass.base_dsl.dsl import BaseDSL

dsl = object.__new__(BaseDSL)
with warnings.catch_warnings(record=True) as rec:
    warnings.simplefilter("always")
    for msg in ["A", "B", "A", "B", "A"]:
        dsl.print_warning_once(msg)
print(len(rec))   # 5 warnings emitted; correct behavior is 2 (one per unique message)
```

Actual output: `5`.

### Suggested fix

Keep an instance-level `set` of already-emitted messages, or move the cache to a module-level function keyed on the message alone with unbounded size.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3629.
