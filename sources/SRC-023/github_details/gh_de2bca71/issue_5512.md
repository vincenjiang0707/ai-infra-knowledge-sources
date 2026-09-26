# [Issue #5512] [ROCm] GLM-5.3-Flash kpool indexer: GPU memory-access fault at max_num_batched_tokens=16384 (crash-loops production MI350 pods)

source: https://github.com/ROCm/aiter/issues/5512
state: closed | updated: 2026-09-18T16:48:25Z
labels: 

## 正文

# [ROCm] GLM-5.3-Flash kpool indexer: GPU memory-access fault at `max_num_batched_tokens=16384` (crash-loops production MI350 pods)

## Summary

GLM-5.3-Flash (`zai-org/GLM-5.3-Flash`, fp8, TP8) on **MI350X (gfx950)** with the kpool
sparse indexer faults with **`Memory access fault`** on all GPUs simultaneously whenever
chunked prefill runs with `--max-num-batched-tokens 16384`. The fault is
**deterministic, shape-triggered, and version-independent across the tested matrix**.
Setting `--max-num-batched-tokens 8192` (the default for most deployments) makes it go
away completely.

We bisected this over two days with in-pod source-tree testing, kernel serialization,
and standalone kernel micro-tests. Details below.

## Environment

- HW: MI350X (gfx950), 8 GPUs, TP8, EP
- vLLM: tested at `e7edf17cea` (nightly image), `98ed0856f` (#53906 merge commit), and
  `724f07381` (the day-0 ROCm GLM-5.3-Flash support commit)
- aiter: image-pinned `e481cc2f6b`, `0.1.19.post2`, and current `main` (6566fb4) — all tested
- Model: `zai-org/GLM-5.3-Flash` (45 layers, kv_lora_rank=512, kpool indexer,
  `is_aiter_triton_fp4_bmm_enabled` (mx-fp4 kv_b_proj))

## Reproduction

```
vllm serve zai-org/GLM-5.3-Flash \
  --tensor-parallel-size 8 --max-model-len 524288 \
  --enable-expert-parallel --max-num-batched-tokens 16384 ...
```
Then drive a large cold prefill (the vLLM serve smoke-test recipe at
https://github.com/vllm-project/vllm/blob/main/docs/... works: prefill a ~48K-token
prompt, then continue decoding). At `num_computed_tokens` crossing ≈48000, every GPU
faults simultaneously:

```
Memory access fault by GPU node-4 (Agent handle: 0x26ff9f00) on address 0x7edbdee00000. Reason: Unknown.
Memory access fault by GPU node-2 ... (×8, one per rank)
```
Worker dies (SIGABRT, exit -6), the engine catches it, the process exits 0, K8s
restarts it, and the cycle repeats every few hours. In production this manifests as
crash-looping pods (8+ restarts) with in-flight requests failing 500.

With `--max-num-batched-tokens 8192`: **clean, zero faults, repro passes**.

## Fault-site identification (AMD_SERIALIZE_KERNEL=3)

Serializing kernels shows the fault window:

```
17:46:54 JIT: BuildPrefillChunkMetadataKernel
17:46:55 JIT: _cp_gather_indexer_quant_cache_gfx950_kernel
17:46:55 JIT: _gluon_fp8_mqa_logits_kernel
17:46:55 JIT: _batched_gemm_a16wfp4_kernel        ← launched immediately before fault
       8× Memory access fault (one per GPU)
```

So the fault is in the kpool-indexer prefill chain
(`_cp_gather → _gluon_fp8_mqa_logits → _batched_gemm_a16wfp4`), at the 16384-token
chunk shape.

## What we ruled out (standalone kernel tests, in-pod, gfx950)

- **Contiguous `fp8_mqa_logits`**: clean at 16384×48000 (2.9 GiB logits),
  16384×131072 (8 GiB), 48000×262144 (46.9 GiB) — the #5121 + #5216 int32 gates hold.
- **Paged `deepgemm_fp8_paged_mqa_logits`**: clean at the indexer geometry
  (H=32, D=128, ctx up to 262144, chunk 16384).
- **`batched_gemm_a16wfp4` standalone** at the server shape (16384×16×512,
  transpose_bm=True, prequant=True): clean.

This points at the **fused kpool-cache-write chain** (or an interaction between the
gather/quant/logits/bmm kernels at 16K-chunk shapes), not any single kernel.

## Why we think it's the 32-bit-offset family

Two closely-related bugs were recently fixed in aiter, both in the same
"MLA prefill cache path" family:

1. **#5475** — `gather_kv_b_proj` refused KV caches with byte span ≥ 2³¹ (three
   separate i32 edges), fixed by lifting the guard and localizing pointer arithmetic.
2. **#5121** — `fp8_mqa_logits` gated buffer ops on **element** offsets rather than
   tensor bytes (fp32 logits tensors between 2 GiB and 8 GiB faulted at the
   `Sequence.h:275` "Begin must be less or equal to End" JIT abort); note
   **#5216** then forced buffer ops back on for gfx950 with the shifted-pointer
   re-basing.

Our fault has the same signature shape (fires only above a size threshold; chunk
8192 keeps every intermediate under the boundary, chunk 16384 crosses it). We have
**not** proven the exact overflowing offset — the serialized trace plus the matrix
above are the evidence — but the fault's shape-dependence (16384 vs 8192) and the
per-GPU simultaneity are consistent with the family.

At `num_computed_tokens` ≈ 262K (a real production trace), the same fault fires
mid-decode, which also fits: the kpool gather/logits intermediates at ctx > 256K
cross further 2³¹ byte thresholds (e.g. a `[M, 262144]` fp32 intermediate at
M ≥ 1024 is 1 GiB+, and page-table×stride products grow with context).

## Impact

- All GLM-5.3-Flash MI350 deployments with default `--max-num-batched-tokens`
  (= 16384 at `max_model_len ≥ 128K` in vLLM's chunked-prefill heuristic) crash-loop.
- Workaround: `--max-num-batched-tokens 8192`.

## Ask

1. Confirm/locate the overflowing access in the
   `BuildPrefillChunkMetadata → _cp_gather_indexer_quant_cache → _gluon_fp8_mqa_logits →
   _batched_gemm_a16wfp4` chain for chunk=16384.
2. If it's the i32-offset family, apply the #5121-style element-offset gates
   (or i64 re-basing) to the paged `pa_mqa_logits` and the kpool gather/bmm chain.
3. Consider a regression test at the 16384×~48K shape (analogous to
   `test_fp8_mqa_logits_logits_past_2gib` from #5121, which covers only the
   contiguous kernel today).

Happy to share the in-pod repro scripts (micro-tests + the serialized capture) and
the full bisect matrix.

— Mustafa Yıldırım (Character.AI), with the vLLM bisect details.


## 评论 (6)

### mustafayildirim · 2026-09-14

cc @jaredwen1234 (the GLM-5.3-Flash ROCm perf work in #55737/#55738 touches the same prefill paths) — flagging in case the 16K-chunk indexer chain overlaps your FlashKDA/masked-MHA testing.

### mustafayildirim · 2026-09-16

## Update: root cause isolated — fault requires CUDA-graph capture; eager mode is clean

Follow-up investigation on the same setup (MI350X / gfx950, TP8, GLM-5.3-Flash fp8, `max_num_batched_tokens=16384`). We've now isolated the trigger with a full differential test matrix.

### Cudagraph-mode differential (identical repro, identical aiter @ `2693202`)

| Cudagraph mode | Result on first 16K-chunk prefill |
|---|---|
| FULL | **Memory access fault ×8 (all ranks)** |
| PIECEWISE | **Memory access fault ×8** |
| FULL_AND_PIECEWISE (vLLM default) | **Memory access fault ×8** |
| `--enforce-eager` | **Clean — 0 faults across the full repro suite** |

The fault fires on the **first** 16K-token chunk prefill. The boot log shows all indexer-path kernels JIT-compiling *during inference* at that moment (boot warmup only covered decode shapes):

```
WARNING [jit_monitor.py] Triton kernel JIT compilation during inference: BuildPrefillChunkMetadataKernel.kernel
WARNING [jit_monitor.py] Triton kernel JIT compilation during inference: _cp_gather_indexer_quant_cache_gfx950_kernel
WARNING [jit_monitor.py] Triton kernel JIT compilation during inference: _gluon_fp8_mqa_logits_kernel
WARNING [jit_monitor.py] Triton kernel JIT compilation during inference: _expand_pools_and_append_tail_kernel
WARNING [jit_monitor.py] Triton kernel JIT compilation during inference: _batched_gemm_a16wfp4_kernel
Memory access fault by GPU node-4 (Agent handle: 0x59ba0110) on address 0x7f733a000000. Reason: Unknown.
```

i.e. **fresh triton JIT + vLLM's lazy piecewise/full capture of the 16384 bucket on gfx950 → fault**. In eager mode the same kernels JIT at the same moment and run clean.

### What we ruled out (in-server A/B via monkeypatch wrappers, each leg a full boot + repro)

| Suspect | Test | Verdict |
|---|---|---|
| `_gluon_fp8_mqa_logits` kernel | skipped in-server (correct-shape −inf logits returned) | fault persists → innocent |
| `_cp_gather_indexer_quant_cache_gfx950` | skipped in-server (zero-fill) | fault persists → innocent |
| `batched_gemm_a16wfp4` | skipped in-server | **fault gone — kernel required** |
| x / y / w / w_scales addresses | all cloned to fresh contiguous buffers in-server (528 clone-verified calls) | fault persists → addresses innocent |
| Kernel serialization | `AMD_SERIALIZE_KERNEL=3` on/off | no effect |
| M threshold | standalone M-sweep 4096→16000 with exact dumped tensors | clean at every M |
| Workspace-pool layout | pool-carved tensors, offset sweeps 0→2047 MB, stream interleave, cudagraph capture of the exact dumped call | all clean standalone |

Standalone replays (in-pod, same GPU, same aiter build) using the **exact tensors dumped from the faulting server call** — including real strides, real scale layout, `AMD_SERIALIZE_KERNEL=3`, plain `torch.cuda.CUDAGraph` capture, and even a fresh-JIT-variant first launch inside a capture — are all clean. The fault only reproduces under vLLM's graph-capture machinery (partitioner/lazy per-bucket capture), which we could not replicate standalone.

### Current mitigation

`--enforce-eager` (fully clean at `max_num_batched_tokens=16384`). Costs decode perf; we'd much prefer a capture-safe kernel or capture-time fix.

### Ask

Has anything been observed on the ROCm side with triton kernels being first-launched (fresh JIT) inside a lazily-captured CUDA graph on gfx950? The `_batched_gemm_a16wfp4` kernel (uses `tl.dot_scaled` / SMFM path, `matrix_instr_nonkdim=16`, `waves_per_eu=2`) is the one whose execution is required for the fault; the mqa/gather kernels are exonerated. Happy to share the dumped tensors and repro scripts.

Repro scripts + tensor dumps: available on request (in-pod pytest harness ~6s per leg).


### mustafayildirim · 2026-09-16

## Follow-up: prewarming is NOT sufficient to fix this (tested)

We tested the "extend warmup to cover the prefill shapes" direction end-to-end on the failing setup (MI350X TP8, aiter @ `2693202`, `max_num_batched_tokens=16384`, cudagraphs on):

**Experiment:** patched `GPUModelRunner.capture_model` (vllm `v1/worker/gpu/model_runner.py`) to run one **eager** `_dummy_run(max_num_tokens=16384)` before any cudagraph capture.

**Result:**
- The eager 16384-token dummy prefill completed cleanly on all 8 ranks at boot (JIT'd the fresh-prefill specializations of `_batched_gemm_a16wfp4`, `_cp_gather_indexer_quant_cache_gfx950`, `_gluon_fp8_mqa_logits` outside capture).
- The first real chunked prefill **still faulted** (8× Memory access fault) **and still JIT-compiled the same kernels during inference** — because the faulting call is a *chunked* prefill with a computed prefix (`batched_gemm_a16wfp4` at `M=16000`, i.e. chunk minus prefix), a **different triton specialization** than the fresh 16384-token prefill the dummy run exercised (different chunk metadata, cu_seqlens, kv lengths, gather layouts).

**Conclusion:** the triton JIT specialization space for the chunked-indexer path is effectively unbounded (depends on prefix length, chunk boundaries, kv layout), so a deterministic prewarm cannot cover it. "Extend warmup" is not a viable fix for this bug.

Additional data point from earlier in the investigation: during the faulting call, `BreakableCUDAGraphCapture.current()` is `None` (the bmm executes in an eager segment between captured pieces, not inside a capture) — yet the fault only occurs with cudagraphs enabled. This suggests an interaction between the eager bmm segment and the surrounding captured graph pieces on gfx950, which likely needs attention from those familiar with the breakable-cudagraph machinery.

Current proven workaround remains `--enforce-eager`.


### mustafayildirim · 2026-09-16

## The official MI350X recipe config hits the same fault

We verified the official serving recipe from recipes.vllm.ai (zai-org/GLM-5.3-Flash, MI350X, single-node TEP) against this bug.

**Recipe command** (docker `vllm/vllm-openai-rocm:nightly`, tested on our MI350X TP8 pod with vLLM `v0.28.1rc1.dev681+ge7edf17ce`, aiter `2693202`):

```
--enable-expert-parallel --tensor-parallel-size 8 --max-num-seqs 512 \
--attention-backend ROCM_AITER_MLA_SPARSE \
--tool-call-parser glm47 --enable-auto-tool-choice --reasoning-parser glm45
```

(no `--max-num-batched-tokens`, no `--enforce-eager` — exactly as published)

**Results:**
- Boot: clean, Ready. Note the engine derives **`max_num_batched_tokens=16384` by default** for this model — the recipe does not actually run at a smaller chunk size.
- First 20K-token prompt (chunked prefill, chunk 2 = M=16000 with prefix): **Memory access fault ×8 ranks — identical crash** to the configurations reported above.

**Why the recipe's validation likely missed this:** the published benchmark is `--random-input-len 8192` — no request ever produces a prefill chunk larger than 8192, and the fault requires a chunk that fills the 16384 budget (a chunk with a computed prefix, i.e. M between ~8192 and 16384 on a later chunk of a longer prompt). Single-chunk 16K prefills and all decode traffic are unaffected.

**Implication:** any user following the official MI350X recipe and serving prompts longer than ~16K tokens will crash-loop on the first long request, exactly as our production deployment did.

**Suggested interim documentation fix:** add `--max-num-batched-tokens 8192` to the MI350X recipe until the underlying capture/JIT fault is fixed (this caps all prefill chunks at 8192 and is verified stable), or note the limitation explicitly.


### mustafayildirim · 2026-09-16

## ROOT CAUSE FOUND + working fix: `VLLM_USE_BREAKABLE_CUDAGRAPH=0`

### Root cause

The fault is triggered by the **breakable cudagraph machinery** (`VLLM_USE_BREAKABLE_CUDAGRAPH=1`), not by the aiter kernels or any memory layout.

Differential (identical request repro, MI350X TP8):

| Config | First 16K-chunk prefill |
|---|---|
| breakable=1 (default in our env), cudagraph_mode FULL / PIECEWISE / FULL_AND_PIECEWISE | **fault ×8 ranks** |
| breakable=1, `--enforce-eager` | clean |
| **breakable=0, cudagraphs on (FULL_AND_PIECEWISE, 57 FULL graphs captured)** | **clean — 0 faults, repro ×2** |

### Working fix

```
VLLM_USE_BREAKABLE_CUDAGRAPH=0
```

- Validated on vLLM `0.29.1rc1.dev187+gaf1c01499` (nightly, 2026-09-16) with aiter `2693202`: full repro suite ×2 passes with zero faults, `max_num_batched_tokens=16384` honored, FULL+PIECEWISE cudagraphs active, decode graphs intact.
- On older builds without torch.compile support for this model (`0.28.1rc1.dev681+ge7edf17c`), breakable=0 cannot be used — the engine raises `piecewise CUDA graphs unavailable, model is not torch-compiled and breakable CUDA graph is off` (that build has no piecewise mechanism other than breakable graphs). The fix requires a torch.compile-enabled build.

### Mechanism notes for maintainers

- The faulting kernel (`aiter batched_gemm_a16wfp4` at M=16000, chunk 2 of a chunked prefill) executes with `BreakableCUDAGraphCapture.current() is None` — i.e. in an **eager segment between breakable-capture pieces** — yet faults only when the breakable machinery is active. Kernel serialization on/off, all tensor addresses (cloned in-server), M-threshold, and every standalone replay (including plain `torch.cuda.CUDAGraph` capture and fresh-JIT-in-capture) are clean. This points at the eager-segment-on-capture-stream execution pattern in `vllm/compilation/breakable_cudagraph.py` (ending a stream capture, launching a triton kernel on the capture stream, resuming capture) interacting badly with gfx950 — possibly the triton launch path doing module-load/scratch-alloc between capture end and resume.
- Triton JIT-during-inference still occurs with breakable=0 (7 warmup warnings at first prefill) and is harmless there — JIT alone is not the trigger.

### Repro summary

Serve GLM-5.3-Flash fp8 on 8×MI350X, TP8, `--max-num-batched-tokens 16384 --max-model-len 524288`, breakable cudagraph on (default), then send a prompt >16K tokens (chunk 2 of the chunked prefill, M=16000 with computed prefix). Memory access fault on all ranks, engine dies, pod crash-loops. Repro scripts and full bisect matrix in earlier comments.


### mustafayildirim · 2026-09-18

## Resolution — closing

The trigger attribution in my last update ("breakable cudagraph machinery") was the proximate trigger, not the root cause. The actual root cause was found and fixed upstream in vLLM:

**vllm-project/vllm#57317** — `KpoolTailSpec` incorrectly declared `uses_slot_mapping=True`, so the kpool indexer's one-block circular tail cache was written through slot-mapping indirection that doesn't match the kernel's pointer arithmetic. Breakable cudagraphs exposed it (they enable `'all'` custom ops → the AMD `sparse_attn_indexer_kpool` path runs); the fix adds `uses_slot_mapping = False` to `KpoolTailSpec`.

**Post-fix validation** (MI350X TP8, nightly `0bfc7a15d` + #57317, breakable cudagraph **ON** at 16384 chunk):
- Full mixed chunked-prefill/decode repro: clean
- Long-context ladder 32K → 400K + cached follow-ups: clean
- Tokenizer-exact max-depth prefill (524,212 tokens): OK, 26s
- Zero memory-access faults; engine healthy after the full suite

So the correct production posture once #57317 lands in a nightly is: **breakable cudagraphs ON** (drop the `VLLM_USE_BREAKABLE_CUDAGRAPH=0` workaround), which also restores PIECEWISE graph coverage for mixed batches.

Related fixes on the same path: vllm#57252 (topk hook, merged), vllm#57192 (jit-warmup, merged), vllm#57425 (AMD `SparseAttnIndexerKpool` forward_hip alias — boot crash with breakable on).

Closing as fixed upstream.
