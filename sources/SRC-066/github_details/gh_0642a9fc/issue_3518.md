# [Issue #3518] SubbyteReference breaks its offset invariant for negative offsets (constructor and operator+=)

source: https://github.com/NVIDIA/cutlass/issues/3518
state: open | updated: 2026-09-01T21:32:40Z
labels: CUTLASS C++

## 正文

### Description

`SubbyteReference` (both the primary template and the `StorageVec` partial specialization in include/cutlass/subbyte_reference.h) mishandles **negative** offsets: the constructor and `operator+=` with a negative argument use truncating division without normalizing, leaving the object in a state that violates its own invariant.

Verified by execution on a minimal host build (Storage = uint8_t, Element = int4b_t):

```
control  -= (+3)  : storage_delta=-2 off=1   get=-3   correct
case B   += (-3)  : storage_delta=-1 off=-1            (invariant requires off in [0, 1])
FAIL: += negative breaks offset_ invariant
case C   ctor(ptr, -3): storage_delta=-1 off=-1        same broken state
```

Correct state for element -3 is one storage unit further back (`storage_delta == -2`, `offset_ == 1`). Instead `offset_ < 0`, and any subsequent `get()`/`set()` shifts by a negative bit count (undefined behavior) or reads the wrong nibble. The mirrored `operator-=` with a positive argument is correct - its borrow logic compensates - which is why only the negative-input paths were affected.

Reachability: `TensorRef::operator-(coord)` and negative `add_pointer_offset` feed this constructor through `ReferenceFactory` for sub-byte tensors. Nothing in-tree navigates sub-byte tensors backward across vector boundaries today, so this is latent public-API breakage.

### Suggested fix

Normalize negative deltas exactly like the positive path does: fold the current `offset_` in first, then use floor-style division/borrow so that the postcondition `0 <= offset_ < kElementsPerVector` always holds.


## 评论 (1)

### apjones-proton · 2026-09-01

BTW the PR  also fixes the case of negative offsets passed to operator-= .
