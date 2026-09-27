# [Issue #5115] [Bug] AddressManager accepts size 0, breaks free list / ZeroDivisionError

source: https://github.com/LMCache/LMCache/issues/5115
state: closed | updated: 2026-09-23T19:19:10Z
labels: 

## 正文

Hey team, 

I found `AddressManager.allocate()` and `batched_allocate()` say size should be > 0 but don't check it. On dev (68b7e5f):

```python
from lmcache.v1.memory_management import AddressManager

am = AddressManager(1 << 20)
a = am.allocate(4096)
z = am.allocate(0)
b = am.allocate(4096)
am.free(*z); am.free(*b); am.free(*a)
print([(x.start, x.size) for x in am._explicit_list])
# [(0, 4096), (4096, 4096), (8192, 1040384)]  <- never coalesced
am.allocate(1 << 20)
# RuntimeError: no memory is available (everything is free)

AddressManager(1 << 20).batched_allocate(0, 3)
# ZeroDivisionError (block.size // aligned_size)
```

The ZeroDivisionError also gets past `TensorMemoryAllocator.batched_allocate`, which only catches RuntimeError.

I hit this through `SegmentTokenDatabase`: a leading/trailing/double separator gives an empty range (e.g. `(4, 4)`), and `LMCacheEngine.store()` allocates 0 bytes for it.

Fix I'd suggest: raise RuntimeError for size <= 0 in both (same as #5061 did for batch_size) and add tests in `tests/v1/test_address_manager.py`. Happy to send a PR.


## 评论 (2)

### chrisyifanjin · 2026-09-14

some more context. i found this while playing with random tests for the allocator, and i think it'd be nice to have them in the repo. a few bugs here were found by hand so far (this one, [#5005](https://github.com/LMCache/LMCache/issues/5005), [#3834](https://github.com/LMCache/LMCache/issues/3834)).

the idea is pretty simple. do a bunch of random allocate/free calls with a fixed seed, remember what's allocated in a dict, and after each call check that nothing overlaps, free blocks next to each other got merged, and the sizes add up. at the end free everything and make sure you get one big block back. if it fails it prints the seed so you can rerun it.

no new deps, just cpu. i'd start with [`AddressManager`](https://github.com/LMCache/LMCache/blob/5001a52cd9ec315f4a7ce1cc7ca9e02cde1f7fb0/lmcache/v1/memory_management.py#L1286) and [`TensorMemoryAllocator`](https://github.com/LMCache/LMCache/blob/5001a52cd9ec315f4a7ce1cc7ca9e02cde1f7fb0/lmcache/v1/memory_allocators/tensor_memory_allocator.py#L23), and add two thread tests: several threads doing allocate/free at once, and the same thing while [`sbrk`](https://github.com/LMCache/LMCache/blob/5001a52cd9ec315f4a7ce1cc7ca9e02cde1f7fb0/lmcache/v1/memory_management.py#L1543) grows the heap. both pass on dev today, they're more to catch it if someone removes a lock later.

also when i tried calling [`check_consistency()`](https://github.com/LMCache/LMCache/blob/5001a52cd9ec315f4a7ce1cc7ca9e02cde1f7fb0/lmcache/v1/memory_management.py#L1579) while other threads were writing, it sometimes returned false or threw `IndexError`, and the size check in [`memcheck`](https://github.com/LMCache/LMCache/blob/5001a52cd9ec315f4a7ce1cc7ca9e02cde1f7fb0/lmcache/v1/memory_allocators/tensor_memory_allocator.py#L289) failed while `sbrk` was running. looks like [#3833](https://github.com/LMCache/LMCache/pull/3833) already fixes this by adding the lock, so +1 for that PR.

if this sounds ok i can write it up as an RFC after the size 0 fix.


### LiRunGuo · 2026-09-15

/claim
