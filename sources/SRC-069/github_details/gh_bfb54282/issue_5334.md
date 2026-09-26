# [Issue #5334] [Bug] Blackwell GDN chunked: TMEM stage released while tcgen05.ld is still in flight (cg1_shared_acc, gated_delta_net_chunked.py:4528 and :4569)

source: https://github.com/flashinfer-ai/flashinfer/issues/5334
state: open | updated: 2026-09-18T23:44:37Z
labels: needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and did not find a solution or an existing report.

## Summary

In the Blackwell GDN chunked kernel, two consumer releases of the `cg1_shared_acc` TMEM accumulator stage signal the producer that the stage is free **without waiting for the `tcgen05.ld` that is still reading it**. The producer's next `tcgen05.mma` into that stage can therefore overwrite it mid-read, so the consumer's registers receive a mix of the intended chunk's values and the next chunk's.

Compute group 0 performs the structurally identical handoff correctly by calling `cute.arch.fence_view_async_tmem_load()` before releasing. The two compute-group-1 sites omit it.

Present in `main` @ `d7bfcab6091da2e1d98c1b26b46d8e613389c2e1`, and in `v0.6.18.post1` (byte-identical regions; same line numbers).

`flashinfer/gdn_kernels/blackwell/gated_delta_net_chunked.py`:

| Line | Handle | TMEM read | Load fence before release? |
|---|---|---|---|
| `4528` | `ks_handle` (`tTR_tCtKS`) | `cute.copy(tiled_ks_t2r, …)` at `4521` | **no** |
| `4569` | `nv_handle` (`tTR_tCtShared`) | `cute.copy(tiled_shared_t2r, …)` at `4561` | **no** |
| `3082` | `kk0_handle` | `3076` | yes, at `3081` |
| `3110` | `kk1_handle` | `3104` | yes, at `3109` |

`nv_handle`'s release is unconditional in that function, so it is on every chunk of this path, not a rare branch.

## Why this needs machine code to see

`cute.arch.fence_view_async_tmem_load()` lowers to a bare `NOP`. `ptxas` attaches the actual ordering to the *following* `SYNCS.ARRIVE` as a wait-mask bit. So the ordering is invisible in the source, invisible in PTX operands, and invisible in SASS mnemonics — it exists only in the instruction control bits.

Compiled for `sm_103a` (CUDA 13.3.29, `nvdisasm -c -g -hex`), correct handoff in compute group 0:

```
/*3250*/  LDTM.16dp32bit_t16_t31.x16 R4, tmem[UR4+0x130]   ; wr_bar=1
/*3270*/  NOP                                              ; <- fence_view_async_tmem_load()
/*3280*/  SYNCS.ARRIVE.TRANS64.A1T0 RZ, [UR7+0x160], RZ    ; wait=000010  <- waits on bar 1
```

Defective handoff, compute group 1 (`ks_handle`):

```
/*8850*/  LDTM.16dp256bit.x8 R4, tmem[UR4+0x100180]        ; wr_bar=1
/*8860*/  FMUL2 R50, R40.F32x2.HI_LO, R70.F32x2.HI_LO
/*8870*/  SYNCS.ARRIVE.TRANS64.A1T0 RZ, [UR7+0x178], RZ    ; wait=000000  <- waits on nothing
```

Same pattern at `0x96b0` for `nv_handle`. Both release the same empty mbarrier (`UR7+0x178`). `LDTM` is asynchronous and its scoreboard is the only completion mechanism, so at `0x8870` the producer is told the buffer is free while a read of it is outstanding.

Specialization audited (the vLLM Qwen3-Next first-prefill path): `use_initial_state=True`, `store_final_state=True`, no state-index indirection, no checkpoints, persistent, 16 QK heads / 48 V heads, head dim 128, 148 SMs. Non-CP branch (confirmed via `should_use_cp_host`, which returns `False` for batch 1–16 at that geometry).

## Two lookalike sites that are NOT defective

`qs_handle` (`4554`) and `o_qs_handle` (`4618`) also lack a load fence and **are correct**: an intervening register consumer already waits on the `LDTM` scoreboard, so the load has provably completed. Please don't "fix" those — a source-level fence audit is unsound in both directions here. Only the control bits decide.

## Proposed fix

Two lines, applying the compute-group-0 idiom:

```diff
@@ -4525,6 +4525,7 @@
             )
             for k in cutlass.range(cute.size(tTR_rKS), vectorize=True):
                 tTR_rKS[k] = tTR_rKS[k] * tGrCumprod[k]
+            cute.arch.fence_view_async_tmem_load()
             ks_handle.release()
             for k in cutlass.range(cute.size(tTR_rKS), vectorize=True):
                 tRT_rV[k] = tRT_rV[k] - tTR_rKS[k].to(self.io_dtype)
@@ -4566,6 +4567,7 @@
             tTR_rNv_inp[None, sub, 0].store(
                 tTR_rNv[None, sub, 0].load().to(self.io_dtype)
             )
+        cute.arch.fence_view_async_tmem_load()
         nv_handle.release()
```

Recompiled under identical conditions, checking every release that has an `LDTM` scoreboard live at that point:

| Variant | Releases with in-flight `LDTM` | Unordered |
|---|---|---|
| baseline | 4 | **2** (`0x8870`, `0x96b0`) |
| + fix | 4 | **0** |
| revert | 4 | **2** (same two) |

In the fixed build both releases carry wait mask `000010` on precisely the scoreboard set by the corresponding `LDTM`, with `LDTM` count (32) and `SYNCS.ARRIVE` count (30) unchanged and the two already-correct group-0 releases untouched.

## Reproduction status — please read before triaging

**I could not reproduce a wrong result at runtime, and I am not claiming I did.**

A preregistered stress run on a B300 SXM6 (capability 10.3, 148 SMs, CUDA 13, Torch 2.13.0+cu130) exercised the real `gdn_prefill.chunk_gated_delta_rule` non-CP path for 12,000 launches across `L=8` and `L=4096`, with per-chunk alternating input magnitudes so a corrupted read would land ~16x off. Oracles were bitwise self-consistency across identical launches and a cross-check against an independent Triton implementation. The baseline was **bitwise deterministic with zero mismatches** and matched the reference at bf16 resolution.

The hazard window is one `LDTM`'s in-flight latency against the producer's barrier observation plus `tcgen05.mma` issue — apparently narrow enough that the hardware wins reliably in a standalone launch on this card. That is timing, not correctness: the ordering edge the ISA requires is absent, and nothing guarantees it holds at other clocks, occupancy, architectures, or under concurrent work.

So this is a latent defect found by static analysis of generated code, which is why the regression test below is static too.

## Possible relation to #4704

#4704 reported GDN prefill on SM100 producing NaNs nondeterministically across processes, and @yurekami's analysis there named "an uninitialized-TMEM read via a wrong ACCUMULATE edge" as a remaining candidate after compilation was exonerated, but the specific edge was never located. #4704 was last reported as no longer reproducible on `main`.

This is a concrete, confirmed TMEM read/overwrite race that is **still present in `main`** and would produce exactly that signature: intermittent garbage propagating into `v - k·s` and the NV/decayV GEMM inputs, varying with timing rather than with input data, and "going away" when unrelated changes shift the timing without fixing the missing edge. I can't show it *is* the cause of #4704 — I never reproduced a bad output — but it seems worth connecting, and it argues #4704 shouldn't be closed as fixed.

## Suggested regression test (CPU only, no GPU needed)

A source-level grep for the fence is unsound here (see the `qs_handle`/`o_qs_handle` note). The property that actually matters is scoreboard liveness in generated code, and it can be checked without a Blackwell device: compile for `sm_103a` without executing, disassemble with `nvdisasm -c -g -hex`, and assert that no `SYNCS.ARRIVE` releasing a TMEM stage leaves an `LDTM` scoreboard live.

I have such a test (compile + disassemble + control-bit analysis, ~200 lines with the analyzer). Validated against both variants:

```
baseline  -> FAILED
  release at 0x8870 (source line 4528, mbarrier UR7+0x178, wait mask 000000)
    does not wait on scoreboard(s) [1] set by LDTM 0x8850 (source line 4521)
  release at 0x96b0 (source line 4569, mbarrier UR7+0x178, wait mask 000000)
    does not wait on scoreboard(s) [1] set by LDTM 0x9630 (source line 4561)
+ fix     -> PASSED
```

Happy to open a PR with the two-line fix and that test if you'd like it — let me know whether you want the test in-tree, since it shells out to `nvdisasm` and is the only test of its kind in the repo.

## Environment

Found while investigating an unrelated vLLM serving stall (the stall is *not* explained by this; the mechanism predicts corruption, not the device non-completion that was observed). FlashInfer `0.6.18.post1`, file byte-identical to upstream `v0.6.18.post1` (sha256 `faaf28508f419a255cc030678ef86e73f47153631cc9403176d058b6a0bd715b`). B300 SXM6 AC, driver 580.95.05, CUDA 13.3 toolchain, `nvdisasm` 13.3.29, Python 3.13, Torch 2.13.0+cu130.


## 评论 (2)

### jxmorris12 · 2026-09-18

Follow-up that removes the main caveat in the original report: the analysis above was on a kernel I compiled from a *reconstructed* specialization with fake global-memory descriptors. I've now run the same check on the real thing.

A CUDA core dump retained from the production incident that started this investigation contains 141 loaded module images (`.cudbg.relfimg.dev0.ctx0`). One of them is this kernel, compiled by the live serving process, with the mangled entry symbol matching my reconstruction exactly:

```
kernel_cutlass_kernel_flashinfergdn_kernelsblackwellgated_delta_net_chunked
  GatedDeltaNetChunkedKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_
  PermutationMNK____MMAAtom_ThrID10_ShapeMNK6_0
```

Disassembled (`nvdisasm -c -hex`, sm_103) and run through the same control-bit analysis. It has the identical defect:

| | reconstruction | **production binary** |
|---|---|---|
| `LDTM` / `SYNCS.ARRIVE` | 32 / 30 | **32 / 30** |
| releases with an in-flight `LDTM` | 4 | **4** |
| ordered | `UR7+0x160` (wait `000010`), `UR7+0x168` | `UR14+0x160` (wait `000010`), `UR14+0x168` |
| **unordered** | `UR7+0x178` x2, wait `000000` | **`UR14+0x178` x2, wait `000000`** |

Same mbarrier offsets (`0x160`, `0x168`, `0x178`), same counts, same verdicts — only the uniform register holding the barrier base differs. The production build has no line info, so source lines don't appear, but the correspondence is unambiguous.

So this is not an artifact of my compile harness or of fake descriptors: the two releases really do issue with wait mask `000000` while an `LDTM` scoreboard is live, in the exact binary a real deployment had resident.

To restate the limits, unchanged: I still never observed a wrong output from it, and I'm still not claiming it caused that incident — the incident was a host thread blocked on a device operation that never completed, whereas this race predicts corruption, not non-completion. The connection I'd draw is only to the #4704 NaN signature.


### dundysm · 2026-09-18

taking this. plan: mirror the cg0 idiom and add fence_view_async_tmem_load before the two cg1 releases (ks_handle ~4528, nv_handle ~4569) only; leave qs/o_qs alone. will open a pr shortly and note the production sass confirmation.
