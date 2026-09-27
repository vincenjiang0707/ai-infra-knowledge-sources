# [Issue #3834] Race condition in `TensorMemoryAllocator.memcheck()` causes false health failure during lazy expansion

source: https://github.com/LMCache/LMCache/issues/3834
state: closed | updated: 2026-09-22T02:22:55Z
labels: stale

## 正文

## Summary

`memcheck()` reads `AddressManager._size` twice through two separate unprotected calls while the `LazyMemoryAllocator` background thread can call `sbrk()` — which holds `_lock` — between those reads. The result is a false-positive inconsistency report that sets `is_healthy=False` and fails `test_l1_manager_status_shape`.

Introduced in commit `2ead3e31` (PR #2407) when `memcheck()` was changed from comparing against the fixed `buffer.numel()` to the dynamic `address_manager.get_heap_size()`.

## Root cause

```python
# memory_management.py — TensorMemoryAllocator.memcheck()
total_free_size = self.address_manager.get_free_size()   # read _size = 64 MB
# ← sbrk() can fire here, _size becomes 128 MB
if total_free_size + self.address_manager.total_allocated_size
        != self.address_manager.get_heap_size():          # read _size = 128 MB
    logger.error("Memory allocator size is inconsistent") # false positive
```

`sbrk()` is `@synchronized("_lock")`, but `get_free_size()` and `get_heap_size()` are not, so they race against it.

## Reproduction

The race window is narrow but does occur in CI — observed in [k3-unit-tests build 3831](https://buildkite.com/lmcache/k3-unit-tests/builds/3831/list?sid=019ef2c0-ee2a-4320-8494-2a2c288c6961&tab=output).

Two debug sleeps applied on top of `ec1156ea` make it fire on every run:

```diff
--- a/lmcache/v1/lazy_memory_allocator.py
+++ b/lmcache/v1/lazy_memory_allocator.py
@@ -248,6 +248,7 @@ class LazyMemoryAllocator(MemoryAllocatorInterface):
     def _commit_expansion(self, expand_size: int):
         """
         Call sbrk in the address manager to commit the expansion.
         """
+        import time; time.sleep(0.01)  # DEBUG: hold off sbrk until memcheck reads get_free_size()
         self._address_manager.sbrk(expand_size)
```

```diff
--- a/lmcache/v1/memory_management.py
+++ b/lmcache/v1/memory_management.py
@@ -1826,6 +1826,7 @@ class TensorMemoryAllocator(MemoryAllocatorInterface):
         # Check the real total free size
         total_free_size = self.address_manager.get_free_size()
+        import time; time.sleep(0.01)  # DEBUG: keep window open for sbrk to fire
         logger.info(" - Total free size: %f MB", total_free_size / 1048576)
```

```bash
pytest tests/v1/distributed/test_report_status.py::TestStorageManagerReportStatus::test_l1_manager_status_shape -v -s
```

Both sleeps are required. The first delays `sbrk()` so it has not yet run when `get_free_size()` reads `_size`; the second keeps the gap between the two reads open long enough for `sbrk()` to fire in between. Without either one, the race window collapses and the test passes consistently on a warm machine.

## Fix options

**Option 1 — Delete Check 1.**
`get_free_size()` is defined as `_size - total_allocated_size`, so the check reduces to `_size != _size`, which is a tautology in single-threaded use and only ever fires due to this race. `check_consistency()` (Check 2) already validates the same invariant by summing the explicit free list, so Check 1 is fully redundant and can simply be removed.

**Option 2 — Snapshot read under lock.**
Add a `@synchronized("_lock")` method to `AddressManager` that returns `(_size, total_allocated_size)` in a single critical section. Also mark `check_consistency()` as `@synchronized` for consistency.

```python
# AddressManager
@synchronized("_lock")
def size_snapshot(self) -> tuple[int, int]:
    return self._size, self.total_allocated_size

@synchronized("_lock")
def check_consistency(self) -> bool:
    ...

# TensorMemoryAllocator.memcheck()
heap_size, allocated_size = self.address_manager.size_snapshot()
total_free_size = heap_size - allocated_size
if total_free_size + allocated_size != heap_size:
    ...
```

Check 1 remains a tautology after this change, but the lock prevents future modifications to `get_free_size()` or the surrounding logic from accidentally re-introducing the race.

Open to either approach — going with Option 2 for now; let me know if you'd prefer Option 1.

## 评论 (2)

### github-actions[bot] · 2026-08-23

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### github-actions[bot] · 2026-09-22

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant!
