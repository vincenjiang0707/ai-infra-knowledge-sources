# [Issue #3672] [FEA][CuTeDSL] Let make_tiled_tma_atom set the TMA L2 promotion

source: https://github.com/NVIDIA/cutlass/issues/3672
state: open | updated: 2026-09-24T20:39:51Z
labels: CuTe DSL

## 正文

### Which component requires the feature?

CuTe DSL

### Feature Request

**Is your feature request related to a problem? Please describe.**

`cpasync.make_tiled_tma_atom` takes no L2 promotion and its atom type has no such field (`non_exec_tiled_tma_load<arch, dtype, copy_bits, tma_gbasis, tma_format>`); every H100 descriptor tested encodes 128 B.

The driver's `cuTensorMapEncodeTiled` accepts `CU_TENSOR_MAP_L2_PROMOTION_L2_256B`, the setting suggested in #1139 for a memory-bound FP8 GEMM and encoded explicitly by DeepGEMM. A DSL kernel streaming its weight operand from DRAM cannot get that behaviour through `make_tiled_tma_atom` today.

**Describe the solution you'd like**

Add `l2_promotion=` (default 128 B) to `make_tiled_tma_atom`, carried in the atom type next to `tma_format` so the lowering encodes it; `cutlass.experimental.cuda.TensorMapL2Promotion` could be the enum.

**Describe alternatives you've considered**

Two workarounds, neither carried by the atom:

(a) Our kernel copies the atom's descriptor to a per-CTA global-memory slot, ORs 0x06 into byte 10, fences, and passes the slot as a generic-space `tma_desc_ptr=` (#3671). Read back on H100, the slots match the atom's descriptor except byte 10, and clearing their swizzle field changes the output, so the loads use them; but this rests on an undocumented byte layout and is not portable.

(b) Pass a second map from `create_tensor_map_tiled_from_view(..., l2_promotion=...)` as `tma_desc_ptr=`. In a 2-D, unswizzled, non-multicast test it loads correct data once `get_ptr()` is re-typed (#3670), but box, swizzle and mode order must match the atom's by hand.

CuTe C++ `make_tma_copy` hard-codes 128 B too, but C++ code can pass its own `cuTensorMapEncodeTiled` map.

**Additional context**

The repro dumps the atom's descriptor beside four driver-encoded maps that differ only in byte 10 bits [2:1]. Same output on nvidia-cutlass-dsl 4.7.1 and 4.8.0; `main` (0b55a2f) also exposes no `l2_promotion`. H100 80GB HBM3, driver 590.44.01, CUDA 13.2.

```python
import torch
import cutlass.cute as cute
try:
    from cutlass.tensor_utils import TensorMapManager, TensorMapUpdateMode  # 4.8
except ImportError:
    from cutlass.utils import TensorMapManager, TensorMapUpdateMode  # 4.7
from cutlass.cute.nvgpu import cpasync
from cutlass.cute.runtime import from_dlpack
from cuda.bindings import driver as drv

PROMO = ("NONE", "64B", "128B", "256B")


@cute.kernel
def dump_desc(tma_atom: cute.CopyAtom, out: cute.Tensor):
    tidx, _, _ = cute.arch.thread_idx()
    if tidx == 0:
        ptr = TensorMapManager(TensorMapUpdateMode.GMEM, 128).get_tensormap_ptr(out.iterator)
        cpasync.copy_tensormap(tma_atom, ptr)


@cute.jit
def atom_desc(x: cute.Tensor, out: cute.Tensor):
    smem_layout = cute.make_layout((64, 64), stride=(64, 1))
    tma_atom, _ = cpasync.make_tiled_tma_atom(cpasync.CopyBulkTensorTileG2SOp(), x, smem_layout, (64, 64))
    dump_desc(tma_atom, out).launch(grid=[1, 1, 1], block=[32, 1, 1])


def driver_desc(x, promo):
    U32, U64 = drv.cuuint32_t, drv.cuuint64_t
    err, m = drv.cuTensorMapEncodeTiled(
        drv.CUtensorMapDataType.CU_TENSOR_MAP_DATA_TYPE_FLOAT16, 2, x.data_ptr(),
        [U64(x.shape[1]), U64(x.shape[0])], [U64(x.stride(0) * x.element_size())],
        [U32(64), U32(64)], [U32(1), U32(1)],
        drv.CUtensorMapInterleave.CU_TENSOR_MAP_INTERLEAVE_NONE,
        drv.CUtensorMapSwizzle.CU_TENSOR_MAP_SWIZZLE_NONE, promo,
        drv.CUtensorMapFloatOOBfill.CU_TENSOR_MAP_FLOAT_OOB_FILL_NONE)
    assert err == drv.CUresult.CUDA_SUCCESS, err
    return b"".join(int(v).to_bytes(8, "little") for v in m.opaque)


x = torch.randn(256, 256, dtype=torch.float16, device="cuda")
for name in PROMO:
    d = driver_desc(x, getattr(drv.CUtensorMapL2promotion, f"CU_TENSOR_MAP_L2_PROMOTION_{'L2_' if name != 'NONE' else ''}{name}"))
    print(f"driver  L2_PROMOTION_{name:<4}  byte10=0x{d[10]:02x}  bits[2:1]={(d[10] >> 1) & 3}")

out = torch.zeros(16, dtype=torch.int64, device="cuda")
atom_desc(from_dlpack(x, assumed_align=16), from_dlpack(out, assumed_align=128))
torch.cuda.synchronize()
d = out.cpu().numpy().tobytes()
assert int.from_bytes(d[:8], "little") == x.data_ptr()  # the dumped map is the atom's map for x
print(f"make_tiled_tma_atom          byte10=0x{d[10]:02x}  bits[2:1]={(d[10] >> 1) & 3} -> {PROMO[(d[10] >> 1) & 3]}")
```

```text
driver  L2_PROMOTION_NONE  byte10=0x00  bits[2:1]=0
driver  L2_PROMOTION_64B   byte10=0x02  bits[2:1]=1
driver  L2_PROMOTION_128B  byte10=0x04  bits[2:1]=2
driver  L2_PROMOTION_256B  byte10=0x06  bits[2:1]=3
make_tiled_tma_atom          byte10=0x24  bits[2:1]=2 -> 128B
```


## 评论 (1)

### yunweili3 · 2026-09-24

Confirmed on B200 (`sm_100a`), CUDA 13.2, DSL 4.8.0: the atom's descriptor encodes byte 10 = `0x24` → bits[2:1] = 2 (128B), same as on H100.

**Why this can't be fixed in the Python layer:** `make_tiled_tma_atom` calls `cute_nvgpu.atom_make_non_exec_tiled_tma_load`, which only takes `num_multicast` and `tma_format`; the descriptor itself is encoded inside the compiler (`_cutlass_ir`). L2 promotion needs a new field on that op/atom type and in its lowering. It also can't be patched on device afterwards — PTX `tensormap.replace` has no L2-promotion field.

**Workaround (b) now works through `get_ptr()`:** with #3675, a map from `create_tensor_map_tiled_from_view(..., l2_promotion=TensorMapL2Promotion.l2_256b)` can be passed as `tma_desc_ptr=desc.get_ptr()` directly, without re-typing (verified: correct data, 2-D unswizzled non-multicast). Box, swizzle and mode order still have to match the atom by hand, so this remains a workaround.

**C++ note:** `make_tma_copy` hard-codes `CU_TENSOR_MAP_L2_PROMOTION_L2_128B` (`include/cute/atom/copy_traits_sm90_tma.hpp:1040`), while the im2col path already honours `TmaDescriptorAuxParams::l2promo_` (`copy_traits_sm90_im2col.hpp:451`). Giving the tiled path the same aux param would be a small, separate change.

Maintainers — would you accept a PR for that C++ change (tiled `make_tma_copy` taking an L2 promotion via `TmaDescriptorAuxParams`, default unchanged at 128B)? Happy to put it up if so.

