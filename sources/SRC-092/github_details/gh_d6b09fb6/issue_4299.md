# [Issue #4299] [Bug]: Python `put`/`upsert`/`put_batch`/`upsert_batch` silently truncate non-byte buffers

source: https://github.com/kvcache-ai/Mooncake/issues/4299
state: open | updated: 2026-09-23T16:37:17Z
labels: bug

## 正文

### Bug Report

## Bug Report

**Environment:** main (`e88aacf2`), `mooncake-integration/store/store_py.cpp`. Not platform specific.

### What happens

`put`, `upsert`, `put_batch` and `upsert_batch` accept any object that supports the Python buffer protocol, but they use `buffer_info.size` as the byte length:

```cpp
// store_py.cpp:3129 (put); same in upsert:2865, put_batch:3178, upsert_batch:2921
std::span<const char>(static_cast<char *>(info.ptr), static_cast<size_t>(info.size))
```

In pybind11, `size` is the number of elements, not bytes. `itemsize` is the element size. So for anything other than a byte buffer, only part of the data is stored, and the call still returns `0`.

Strides are also ignored, so a non-contiguous view stores the wrong bytes.

`put_parts` and `upsert_parts` already guard against this (`if (info.ndim != 1 || info.itemsize != 1)` at lines 3150 and 2890). The four functions above do not.

### To reproduce

```python
import array
from mooncake.store import MooncakeDistributedStore

store = MooncakeDistributedStore()
# ... setup ...

value = array.array("f", [0.0] * 1024)   # 4096 bytes, itemsize 4
print(store.put("k", value))             # 0
print(store.get_size("k"))               # 1024, expected 4096
print(len(store.get("k")))               # 1024
```

A numpy `float32` array behaves the same way.

### Expected

Either store all `size * itemsize` bytes of a C-contiguous buffer, or reject non-byte / non-contiguous buffers with an error, the way `put_parts` does. Silent truncation with a success return code is the problem.

### Suggested fix

Use `info.size * info.itemsize` and check contiguity, or apply the same `ndim == 1 && itemsize == 1` check from `put_parts` to `put`, `upsert`, `put_batch` and `upsert_batch`. A small test with a typed buffer (`array.array("f", ...)`) would catch regressions.


### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (1)

### github-actions[bot] · 2026-09-23

Thanks for opening this issue, @yaojiejia!

| Field | Value |
|-------|-------|
| **Issue** | #4299 |
| **GitHub user ID** | `70050131` |
| **Reporter** | @yaojiejia |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
