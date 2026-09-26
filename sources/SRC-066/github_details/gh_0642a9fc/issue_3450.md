# [Issue #3450] [BUG] tvm-ffi fails with non-zero storage offset

source: https://github.com/NVIDIA/cutlass/issues/3450
state: closed | updated: 2026-09-01T07:04:06Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
DLPack allows for a storage offset in a tensor, which is now used by torch. cuteDSL hardcodes check for offset == 0, which raises when it isn't true.

**Steps/Code to reproduce bug**

```
"""Minimal repro: a CuteDSL kernel compiled with --enable-tvm-ffi rejects any tensor
  whose DLPack byte_offset is nonzero, i.e. any PyTorch view with storage_offset != 0.

  Root cause: the tvm-ffi argument-validation codegen emits an unconditional
  `byte_offset == 0` check. Present identically in nvidia-cutlass-dsl 4.5.2 and 4.7.0:
      cutlass/base_dsl/tvm_ffi_builder/tvm_ffi_builder.py
          lambda: self.equal(byte_offset, self.i64(0)),
          ..., ", expected byte_offset=0"

  This only became reachable from PyTorch after pytorch/pytorch#182924 (Aug 2026), which
  made DLPack export set `data = storage_base` and `byte_offset = storage_offset*itemsize`
  for ALL devices. Before that torch folded the offset into `data` and always sent
  byte_offset = 0, so the check was vacuously satisfied.

  Note the wrap itself is fine: from_dlpack correctly folds byte_offset into the cute
  tensor's pointer (printed below). Only the compiled entry point's validation rejects it.

  Run:  python cutedsl_byte_offset_repro.py
  """

  import cuda.bindings.driver as cuda

  import cutlass
  import cutlass.cute as cute

  import torch


  N = 1024
  V = 4  # 4 x fp32 = 128 bits, so a 4-element offset keeps 16-byte alignment


  @cute.kernel
  def _fill_kernel(mDst: cute.Tensor, val: cutlass.Float32):
      tidx, _, _ = cute.arch.thread_idx()
      bidx, _, _ = cute.arch.block_idx()
      row = bidx * 256 + tidx
      if row < cute.size(mDst, mode=[0]):
          for j in cutlass.range_constexpr(V):
              mDst[row, j] = val


  @cute.jit
  def _fill(mDst: cute.Tensor, val: cutlass.Float32, stream):
      nrow = cute.size(mDst, mode=[0])
      grid = (nrow + 255) // 256
      _fill_kernel(mDst, val).launch(grid=[grid, 1, 1], block=[256, 1, 1], stream=stream)


  def wrap(t, enable_tvm_ffi):
      ct = cute.runtime.from_dlpack(
          t.reshape(-1, V), assumed_align=16, enable_tvm_ffi=enable_tvm_ffi
      )
      ct.element_type = cutlass.Float32
      return ct


  def main():
      torch.cuda.init()
      dev = torch.cuda.current_device()
      stream = cuda.CUstream(torch._C._cuda_getCurrentRawStream(dev))

      base = torch.zeros(N + V, device="cuda", dtype=torch.float32)
      at_zero = base[:N]  # storage_offset == 0
      at_offset = base[V : V + N]  # storage_offset == 4 -> byte_offset == 16

      for t, name in ((at_zero, "at_zero"), (at_offset, "at_offset")):
          print(
              f"{name:10s} contiguous={t.is_contiguous()} "
              f"storage_offset={t.storage_offset():2d} "
              f"byte_offset={t.storage_offset() * t.element_size():3d} "
              f"16B-aligned={t.data_ptr() % 16 == 0}"
          )

      for enable_tvm_ffi in (True, False):
          tag = "--enable-tvm-ffi" if enable_tvm_ffi else "default convention"
          print(f"\n=== compiled with {tag} ===")
          opts = "--enable-tvm-ffi" if enable_tvm_ffi else None
          seed = wrap(at_zero, enable_tvm_ffi)
          print(f"  wrapped at_zero   -> {seed}")
          compiled = cute.compile(_fill, seed, cutlass.Float32(0.0), stream, options=opts)
          for t, name, want in ((at_zero, "at_zero", 1.0), (at_offset, "at_offset", 2.0)):
              ct = wrap(t, enable_tvm_ffi)
              if name == "at_offset":
                  print(f"  wrapped at_offset -> {ct}   (pointer already offset by 16B)")
              try:
                  compiled(ct, cutlass.Float32(want), stream)
                  torch.cuda.synchronize()
                  ok = bool((t == want).all())
                  print(f"  call {name:10s}: OK (all values == {want}: {ok})")
              except Exception as e:  # noqa: BLE001
                  print(f"  call {name:10s}: {type(e).__name__}: {str(e)[:150]}")


  if __name__ == "__main__":
      main()
```
**Expected behavior**

Should not raise when compiled with tvm-ffi

```  at_zero    contiguous=True storage_offset= 0 byte_offset=  0 16B-aligned=True
  at_offset  contiguous=True storage_offset= 4 byte_offset= 16 16B-aligned=True

  === compiled with --enable-tvm-ffi ===
    wrapped at_zero   -> Tensor<0x00007ff6c9000000@gmem o (256,4):(4,1)>
    call at_zero   : OK (all values == 1.0: True)
    wrapped at_offset -> Tensor<0x00007ff6c9000010@gmem o (256,4):(4,1)>   (pointer already offset by 16B)
    call at_offset : ValueError: Mismatched Tensor on argument #0 when calling: `_fill(mDst: Tensor([256, 4], float32), val: float32, stream: Stream)`,
  expected byte_offset=0

  === compiled with default convention ===
    wrapped at_zero   -> Tensor<0x00007ff6c9000000@gmem o (256,4):(4,1)>
    call at_zero   : OK (all values == 1.0: True)
    wrapped at_offset -> Tensor<0x00007ff6c9000010@gmem o (256,4):(4,1)>   (pointer already offset by 16B)
    call at_offset : OK (all values == 2.0: True)
```

**Environment details (please complete the following information):**
 - Bare metal
 - cuteDSL 4.5.2, 4.7.0


## 评论 (1)

### brandon-yujie-sun · 2026-08-27

@slayton58 this is fixed in both 4.6.3 and 4.7.1
