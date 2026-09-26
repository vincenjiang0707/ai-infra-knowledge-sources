# [Issue #2094] [BUG] Tmem tiled copy with non power-of-2 size fails to compile

source: https://github.com/NVIDIA/cutlass/issues/2094
state: open | updated: 2026-09-13T03:17:16Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

```
using namespace cute;
auto tmem_layout = make_layout(make_shape(_128{}, _160{}), make_stride(Int<65536>{}, _1{}));
Tensor A = make_tensor(make_tmem_ptr<float>(0), tmem_layout);
auto load = make_tmem_copy(SM100_TMEM_LOAD_32dp32b1x{}, A);
```
This fails to compile, with shape_div error. This is because `make_tmem_copy` calls `make_cotile_copy`, which calls `left_inverse` on the data layout. In this case left_inverse gives shape `(65440, 1)` to make it divisible by 160, but that leads to layout mismatch.

Is there another way I should be constructing the tmem tiled copy with non power-of-2 size?

Cc @thakkarV 

## 评论 (8)

### ccecka · 2025-02-10

Hmmmm, this is a really interesting bug, thanks Tri.

The core issue seems to be in my lazy implementation of `left_inverse`, which is simply incorrect in that case.

Indeed, when I hack in the correct left-inverse layouts to `make_cotiled_copy`, a valid partitioner (the same partitioner) is returned that performs exactly as we would expect
```cpp
  {
  Layout tmem_layout = make_layout(make_shape(_128{}, _128{}), make_stride(Int<65536>{}, _1{}));
  Tensor A = make_tensor(make_tmem_ptr<float>(0), tmem_layout);
  TiledCopy load = make_tmem_copy(SM100_TMEM_LOAD_32dp32b1x{}, A);

  print(tmem_layout); print("\n");
  print(complement(tmem_layout)); print("\n");
  print(left_inverse(tmem_layout)); print("\n");
  print(load);
  print(load.get_slice(0).partition_S(A));  print("\n");
  }

  {
  Layout tmem_layout = make_layout(make_shape(_128{}, _160{}), make_stride(Int<65536>{}, _1{}));
  Tensor A = make_tensor(make_tmem_ptr<float>(0), tmem_layout);
  TiledCopy load = make_tmem_copy(SM100_TMEM_LOAD_32dp32b1x{}, A);

  print(tmem_layout); print("\n");
  print(complement(tmem_layout)); print("\n");
  print(left_inverse(tmem_layout)); print("\n");  // XXX Wrong
  print(load);
  print(load.get_slice(0).partition_S(A));   print("\n");
  }
```
prints
```
(_128,_128):(_65536,_1)
_512:_128
(_65536,_128):(_128,_1)
TiledCopy
  Tiler_MN:       ((_4,_32):(_32,_1),_1:_0)
  TiledLayout_TV: ((_32,_4),_32):((_0,_1),_4)
Copy_Atom
  ThrID:        _32:_1
  ValLayoutSrc: (_32,_32):(_0,_1)
  ValLayoutDst: (_32,_1):(_1,_1)
  ValLayoutRef: (_32,_32):(_0,_1)
  ValueType:    32b
tmem_[32b](0x0000.0000) o ((_32,_1),_1,_128):((_65536,_0),_0,_1)
(_128,_160):(_65536,_1)
_409:_160
_65440:_128
TiledCopy
  Tiler_MN:       ((_4,_32):(_32,_1),_1:_0)
  TiledLayout_TV: ((_32,_4),_32):((_0,_1),_4)
Copy_Atom
  ThrID:        _32:_1
  ValLayoutSrc: (_32,_32):(_0,_1)
  ValLayoutDst: (_32,_1):(_1,_1)
  ValLayoutRef: (_32,_32):(_0,_1)
  ValueType:    32b
tmem_[32b](0x0000.0000) o ((_32,_1),_1,_160):((_65536,_0),_0,_1)
```
Give me a little time to correct the implementation of `left_inverse` -- I'll put the patch here and get it merged asap.

### ccecka · 2025-02-10

In the meantime, this also suggests that an immediate workaround is to build the partitioner with a very similar TMEM tensor and then use it on your actual TMEM tensor.

### tridao · 2025-02-10

> In the meantime, this also suggests that an immediate workaround is to build the partitioner with a very similar TMEM tensor and then use it on your actual TMEM tensor.

Yup that's the workaround i'm using right now: creating a fake tmem tensor of size (128, 128) to get the tiled tmem_copy. 

### github-actions[bot] · 2025-03-12

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2025-06-10

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### ccecka · 2025-06-10

This should just work now. Let me know if there are any issues with the normal pattern.

### github-actions[bot] · 2025-09-08

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### XFDG · 2026-09-13

I compiled the original non-power-of-two TMEM tiled-copy pattern (shape 128x160, stride 65536x1, SM100_TMEM_LOAD_32dp32b1x) from current main (147295a3d4b75f3aeff247c25b8927cea9a7006a) for sm_100a with CUDA 13.1. It now compiles successfully, consistent with the maintainer's update that left_inverse was fixed. This issue appears resolved.
