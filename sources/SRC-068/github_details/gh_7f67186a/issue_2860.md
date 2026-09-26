# [Issue #2860] [FA4][SM120] flash_attn_varlen_func / flash_attn_func illegal memory access at >=4 varlen segments under real-workload memory layouts (b26/b29, GeForce Blackwell)

source: https://github.com/Dao-AILab/flash-attention/issues/2860
state: open | updated: 2026-09-05T00:27:23Z
labels: 

## 正文

## Environment

- GPU: NVIDIA RTX 6000D 84 GB (sm_120, GeForce Blackwell), driver 595.84, CUDA 13.2
- flash-attn-4: 4.0.0b26 and 4.0.0b29 (both tested)
- nvidia-cutlass-dsl: 4.6.0.dev0 / 4.6.2 / 4.7.1 (all three tested)
- torch 2.13.0+cu129, torchvision 0.28.0, Python 3.12
- Workload: MiniMax-H3 hybrid-attention video model (VDN-MiniMax-H3) — bf16 packed
  varlen attention, H=56 heads, D=128, per-window varlen segments
  (q ~5040 rows/segment, kv ~17580 rows/segment), called once per DiT block per NFE.

## Summary

Two independent problems when running FA4 on SM120:

1. **`AuxData` cannot cross the CuTe-DSL JIT boundary** — the SM120 forward path
   (`FlashAttentionForwardSm120`) passes `AuxData(cute_aux_tensors, aux_scalars)` as
   positional arg #17, but the DSL has no adapter for this NamedTuple
   (`JitArgAdapterRegistry.default_dataclass_adapter` is never registered in a plain
   `flash_attn_func`/`flash_attn_varlen_func` install, and NamedTuples are not
   auto-adapted). Consequences differ by DSL version:
   - DSL 4.6.2: `CUDADialectError` (empty message) → clean failure, kernel never runs
   - DSL 4.6.0.dev0 / 4.7.1: only a `UserWarning` ("cannot be converted to a
     JitArgument ... implement the JitArgument protocol"), then the kernel is
     launched with a mangled argument → **illegal memory access**

   Workaround that makes the kernel compile and run (register a zero-width
   JitArgument adapter; our calls always have `tensors=None, scalars=None`, at which
   point the kernel body early-returns in `compute_fastdiv_mods`):

   ```python
   import flash_attn.cute.utils as fa_utils
   import cutlass  # canonical DSL import path
   from cutlass.base_dsl.runtime.jit_arg_adapters import JitArgAdapterRegistry

   class _ZeroWidthAux:
       def __init__(self, src): self._src = src
       def __getattr__(self, name): return getattr(self._src, name)
       def __get_mlir_types__(self): return []
       def __c_pointers__(self): return []
       def __new_from_mlir_values__(self, values): return self

   def _adapt(aux):
       if aux.tensors is None and aux.scalars is None:
           return _ZeroWidthAux(aux)
       raise NotImplementedError("non-empty AuxData")

   JitArgAdapterRegistry.register_jit_arg_adapter(fa_utils.AuxData)(_adapt)
   ```

   Suggested upstream fixes (either): register a default dataclass/NamedTuple
   adapter in `base_dsl` when `default_dataclass_adapter` is unset, or annotate/
   adapt `AuxData` in `interface.py` so `flash_attn_func`/`flash_attn_varlen_func`
   work out of the box on SM120.

2. **With (1) worked around, the SM120 kernel still hits an illegal memory access
   once the varlen batch has >= 4 segments under real-workload memory layouts.**
   Details below. This is the blocker: the kernel is ~7x faster than our fallback
   for small inputs, but cannot be used for real renders.

## Bug 2 details

Bisect over sequence length (same call, same shapes family, real model):

| frames (latent) | varlen segments W | result |
|---|---|---|
| 22 (5 latent, 1 window) | 1 | OK — **2.22 s/NFE** |
| 39 (2 windows) | 2 | OK |
| 56 (3 windows) | 3 | OK |
| 73 (4 windows) | 4 | **CRASH illegal memory access** |
| 90 / 107 / 124 / 345 | 5+ | CRASH |

Captured real call at 124 frames (first FA4 call of the render):
`q (35280, 56, 128) bf16, stride (7168, 128, 1) (contiguous); cu_seqlens_q`
= [0, 4032, 9072, 14112, 19152, 24292, 29232, 34272, 35280]; `max_seqlen_q=5040`,
`max_seqlen_k=17580`.

What rules things out:

- **Exact-tensor replay passes.** Saving the exact crashing q/k/v/cu_seqlens and
  replaying `flash_attn_varlen_func` standalone (same GPU, same env) does NOT
  crash — nor do uniform-shape synthetic tensors with the same cu_seqlens.
- **Synthetic W×S grid all green.** W in {1..16} × S in {1024..24576} at H=8 and
  H=56, varlen and batched-dense (`flash_attn_func` on `[W, S, H, D]` views): all OK.
- **Not the tile config.** Forcing `tile_mn=(128, 128)` on SM120 (default is
  (128, 64) for head_dim > 64) still crashes.
- **Not the call form.** Both `flash_attn_varlen_func` and batched
  `flash_attn_func` crash at >= 4 windows in the real workload.
- **Non-deterministic attribution.** With `CUDA_LAUNCH_BLOCKING=1` the fault
  surfaces at varying downstream ops (`torch.tensor(..., device=cuda)`, `F.linear`,
  block-mask construction); sometimes the run gets further before dying. This
  smells like an OOB *write* that corrupts neighbouring allocations, with the
  fault surfacing in whatever kernel touches the corrupted region next.

So: the failure needs the real process context (allocator layout + the surrounding
33B-model step), and reproduces deterministically-in-practice at >= 4 varlen
segments there, while isolated replays of the identical inputs pass. Happy to run
any instrumented build, or to provide dumps/traces — the full model is public
(OpenVDN/vdn-minimax-h3, MiniMax-H3 hybrid attention) so the workload is
reproducible end to end.

## compute-sanitizer memcheck findings (precise localization)

Running `compute-sanitizer --tool memcheck` on the crashing render localizes every
fault to the same tile:

```
Invalid __global__ read of size 16 bytes
    at kernel_cutlass_kernel_flash_attncuteflash_fwd_sm120FlashAttentionForwardSm120
       _object_at__tensorptrbf16gmemalign16oi64div8...+0x15c0
    by thread (0,0,0) in block (15680,0,0)
    Access to 0xe2120aec000 is out of bounds
    (15,143,501,315,325 bytes after the nearest allocation — i.e. a wild pointer,
     not a small over-read; all 15 printed faults are lanes 0..14 of the same warp
     in the same block, one 16-byte-per-lane vectorized load)
    host: _flash_attn_fwd (interface.py:1540) <- flash_attn_varlen_func
          <- window_softmax_decomposed
```

Interpretation: for this workload the varlen grid is over-provisioned
(`SingleTileVarlenScheduler.get_grid_shape` returns
`ceil((total_q + num_batch*(tile_m-1))/tile_m) * num_head` = 283*56 = 15840 blocks,
while the decoder only recognizes `per-segment-ceil` accounting = 280*56 = 15680
valid tiles). Blocks 15680..15839 decode to garbage coordinates, and the kernel
performs its vectorized K/V prefetch load *before* (or without) honoring
`is_valid`, dereferencing a pointer computed from the invalid decode. A plausible
source fix is to gate the tile prologue (pointer computation + first K/V
prefetch) on the scheduler's `is_valid` in the SM80/SM120 varlen path — or to
have the decoder clamp invalid tiles to a null buffer.

Note the crash requires >= 4 varlen segments in practice: with 1-3 segments the
same over-provisioned blocks' garbage reads land in mapped allocator memory and
silently pass, which is why small renders (22/39/56 frames) work.

## Practical workaround found (confirms the mechanism)

Padding the caller-side `cu_seqlens_q`/`cu_seqlens_k` tensors with one extra
entry duplicating the last cumulative count makes the over-provisioned tail
tiles' out-of-bounds `cu[batch_idx + 1]` reads land on the sentinel entry.
The sentinel yields `seqlen == 0` for the invalid batch, all loads/stores
predicate off, and the render completes stably at full size (345 frames,
H=56, D=128) with the decomposed dense-varlen path — no illegal access across
repeated runs. This confirms the faulting reads are the scheduler/decoder's
unbounded `cu` accesses for over-provisioned tiles. A robust upstream fix would
be to bound those reads (or size the cu allocation with tile-granular slack)
inside `_flash_attn_fwd`'s varlen setup rather than requiring callers to pad.

## Additional experiment: clamping invalid decode does NOT fix it

We also patched `SingleTileVarlenScheduler._decode_work_tile` to clamp invalid
tiles to the sentinel batch (`batch_idx = num_batch`, `block = head = 0`), so
`SeqlenInfoQK` sees `seqlen == 0` and every load/store is predicated off. Under
memcheck the faults persist at adjacent grid-tail blocks (15681, 15682, ...).
Together with the isolation-replay and synthetic-grid results, this points at
the generated code itself: the SM80-algorithm kernels compiled for the sm_120
target miscompute addresses for this shape family (H=56, D=128, large packed
varlen), independent of scheduler decode correctness. A full fix likely needs
the CuTe DSL / ptxas codegen owners to validate SM80-path SASS on an sm_120
target.

## Current status for us

We ship with the Triton flex fallback (fp8 + `_scaled_mm` works great on SM120),
so nothing is blocked — but getting the FA4 SM120 path solid would be a large
win (2.22 s/NFE vs 15+ s/NFE on the fallback for the same 124-frame workload).

## Tested against upstream main

The render also crashes with the flash_attn/cute Python sources synced to
main @ ce088ab9 (which includes #2705 "Preserve first-tile flag during scheduler
reconstruction", #2745 "Fix forward dynamic-shape correctness", #2671 "Fix CuTe
SM120 compile-time argument handling", and the SM100 varlen/block-sparse deadlock
fix #2761). The illegal access persists identically, so this is still present on
the latest main. Environment can be re-tested on demand against any fix branch.

## 评论 (1)

### VXeffect · 2026-09-05

## Follow-up: SASS-level localization, explicit SM120 block-sparse assert, and nondeterminism data

Additional data after further debugging, in case it helps narrowing the SM120 defect.

### 1. SASS-level faulting instruction

Under `compute-sanitizer --tool memcheck`, all 15 reported faults resolve to the
same warp executing a 128-bit vectorized global load inside the generated
`FlashAttentionForwardSm120` varlen kernel:

```
Invalid __global__ read of size 16 bytes
    at kernel_cutlass_kernel_flash_attncuteflash_fwd_sm120FlashAttentionForwardSm120
       _object_at__tensorptrbf16gmemalign16oi64div8...+0x15c0
    by thread (0,0,0) in block (15680,0,0)
    Access to 0xe2120aec000 is out of bounds
    (15,143,501,315,325 bytes after the nearest allocation — wild pointer)
```

Disassembling the generated cubin (`nvdisasm -c`, compiled target `sm_120a`),
offset 0x15c0 sits in the address-formation sequence feeding an async
global→shared K/V copy:

```
/*1580*/  @P2 LEA     R12, P0, R18, R124, 0x1 ;
/*15c0*/  @P2 LEA.HI.X R13, R18, R120, R7, 0x1, P0 ;   // high half of 64-bit address
/*15a0+/  @P5/@P6/@P0/@P2 LDGSTS.E.BYPASS.LTC128B.128 [R127+...], desc[UR14][Rn.64]
```

i.e. the 64-bit tile base pointer (R12:R13) for the `LDGSTS.128` K/V prefetch is
computed from coordinates that are garbage for over-provisioned grid-tail tiles.

### 2. FA4 explicitly asserts block sparsity unsupported on SM 12.0

`interface.py` (b29 and current main) contains:

```python
assert not use_block_sparsity, "Block sparsity not supported on SM 12.0"
```

so the Flex block-sparse path is cleanly refused on SM120 (our fallback then
uses the Triton kernel, which is stable). The **dense varlen** path used by the
decomposed window softmax has no such guard and is where the illegal access
originates.

### 3. Nondeterminism data (same env, repeated runs)

| frames | segments | runs | outcome |
|---|---|---|---|
| 22 | 1 | 2 | OK (2.22 s/NFE) |
| 39 | 2 | 1 | OK |
| 56 | 3 | 1 | OK |
| 73 / 90 / 107 / 124 | 4+ | 6 | crash (pre-workaround) |
| 124 | 8 segments (unequal: [4032, 5040×6, 1008]) | 3 | stable after our cu-padding workaround |
| 241 | 12 segments (unequal) | 1 | **crash even with cu-padding workaround** |
| 345 | 14 segments (unequal) | 2 | 1 OK + 1 crash across configurations |

So with the cu-padding workaround the 124-frame tier (3 windows? 8 unequal
segments) is stable across repeated runs, but the defect still fires
nondeterministically at larger segment counts / larger totals — consistent with
a layout-dependent OOB in the generated SM120 code rather than a pure
shape-deterministic bounds bug.

### 4. Practical status

We ship the Flex + Triton path (fp8 + `torch._scaled_mm` works fine on SM120),
so nothing is blocked. But the FA4 SM120 varlen kernel shows ~7x headroom
(2.22 s/NFE vs 15+ s/NFE on the fallback at identical shapes), so a fix would
be very welcome. Environment can be re-tested on demand against any fix branch
— full evidence archived (memcheck log, captured cu tensors, PTX, and the
`sm_120a` cubin of the faulting kernel).

