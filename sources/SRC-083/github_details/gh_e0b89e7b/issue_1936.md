# [Issue #1936] [sm_87] Multi-shape Linear4bit sequence reboots Jetson Orin Nano Super (system reboot, not OOM)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1936
state: open | updated: 2026-05-11T18:41:41Z
labels: aarch64, CUDA

## 正文

### System Info

 - Hardware: Jetson Orin Nano Super 8 GB (sm_87, Ampere, 1024 CUDA cores)
  - OS: JetPack 6.2 (L4T R36.4) / Ubuntu 22.04
  - CUDA: 12.6
  - Python: 3.10.12
  - PyTorch: 2.5.1 (source-rebuilt for Jetson with USE_DISTRIBUTED=1 USE_GLOO=1; reports as 2.5.0a0+gita8d6afb)
  - bitsandbytes: 0.46.1, source-built at SHA 4bca84499ad194d6c37e77dfcf99201b81dc6981 with `cmake -DCOMPUTE_BACKEND=cuda -DCOMPUTE_CAPABILITY=87 -S .`
  - Power mode: MAXN_SUPER (`nvpmodel -m 2`)

### Reproduction

### Summary

  On Jetson Orin Nano Super (sm_87), running a sequence of three `bnb.nn.Linear4bit` construct + forward cycles at large output dimensions in a single Python process **reboots the entire system** — kernel-level reboot, not Python crash, not Linux OOM-killer, not `cudaMalloc` ENOMEM. It fires reliably; I've reproduced it twice on separate fresh boots, and the same shapes pass cleanly when each is isolated in its own process.

  The fault appears to be **accumulated state across multiple bnb-NF4 cycles** in the same process — most likely allocator fragmentation, bnb scratch-buffer accumulation, or driver bookkeeping at sm_87.

  ### Reproducer

  Standalone gist: https://gist.github.com/neil-the-nowledgeable/a5ade63cbd2143d0628c96c8f840c87e

  ```python
  # WARNING: reboots the Jetson on every attempt I've tried.
  # Run via ssh from a separate machine; close any unsaved work first.
  import torch
  import bitsandbytes as bnb

  shapes = [
      (4096, 32768),    # Linear A — large intermediate-class
      (4096, 128256),   # Linear B — Llama-3.1-8B-class lm_head
      (3584, 152064),   # Linear C — Qwen2.5-7B-class lm_head
  ]

  for in_f, out_f in shapes:
      print(f"Constructing Linear4bit({in_f}, {out_f})...", flush=True)
      layer = bnb.nn.Linear4bit(
          in_f, out_f, bias=False,
          quant_type="nf4",
          compute_dtype=torch.bfloat16,
          quant_storage=torch.bfloat16,
      ).to("cuda")
      x = torch.randn(1, in_f, dtype=torch.bfloat16, device="cuda")
      with torch.no_grad():
          y = layer(x)
          torch.cuda.synchronize()
      print(f"  forward OK; peak_mb={torch.cuda.max_memory_allocated()/1e6:.1f}",
            flush=True)
  ```

  ### Observed

  - Shapes A and B complete forward cleanly (peak memory printed, sync returns).
  - During or shortly after Linear C's forward, the Jetson reboots. dmesg / journalctl from the prior boot show no kernel oops, no OOM-killer event, no NVIDIA driver fault 
  - the system simply restarts. ssh sessions die; the Jetson is back up ~60 s later.
  - Reproduces every time so far (twice on fresh boots, identical shape sequence).

  ### Bracket — what works vs what doesn't

  | Test | Result |
  |---|---|
  | Linear C alone in fresh process: `Linear4bit(3584, 152064)` construct + forward | **PASS** (fwd ~30 ms, peak ~2530 MB) |
  | Linears A, B, C in *separate* processes, sequentially | PASS each |
  | Linears A → B → C in **same** Python process (above) | **REBOOT** |

  The single-shape PASS for `(3584, 152064)` is what made me revise an earlier framing — I'd initially thought it was a single-shape geometry fault. It isn't; the bug requires multi-shape sequencing.

  ### Workload context

  This is the limiting factor for running 7B-class QLoRA training on Jetson Orin Nano Super on the bnb path. The multi-shape sequence reboot above is one of three\*
  distinct bnb-NF4 sm_87 fault regimes I've observed at the broader 7B-class workload boundary. The 1B–4B class is solid on this build; Mistral-7B-v0.3 specifically (32 K vocab, intermediate=14336, 32 layers) also dodges all three regimes at single-Jetson + no-FSDP and trains cleanly to 15,610 stable steps at 5044 ± 1 MB peak.

  \* The other two regimes — both reproducible, separate bugs, scope-creep for this issue but flagged for awareness:
  - **Stacked-context fault**: Llama-3.1-8B real-model forward (no FSDP at all) hangs Python at the bnb forward call. Each individual Linear in the model passes synthetically; the fault requires the full 32-decoder-layer + lm_head graph context to fire.
  - **FSDP2-multilayer-aggravated**: per-decoder `fully_shard()` wrap of any 7B-class model with `intermediate_size ≥ 14336` hangs forward.

  ### Cross-reference

  This is the kernel-fault caveat referenced in #1218 (prebuilt aarch64+CUDA wheel request).

  ### Offer

  I'm happy to run instrumented variants of the repro on my Jetson — per-shape `cudaDeviceSynchronize`, allocator stats between shapes, `compute-sanitizer` if it fits in memory, etc. — and share JSON outputs. Let me know what would be most helpful.


### Expected behavior

The shape sequence should either:

  1. Complete cleanly and print "Sequence complete" — same outcome as running each shape in its own process.
  2. Raise a Python-level error (e.g., CUDA OOM) that surfaces through normal exception handling.

  Rebooting the Jetson is unexpected and not recoverable in-process. There's no Python traceback, no kernel oops, no driver fault log — the system just restarts, which makes it both hard to diagnose and dangerous for any long-running training process that hits the sequence.


## 评论 (6)

### matthewdouglas · 2026-05-04

Thanks for the report @neil-the-nowledgeable. This may be a little tricky and involve some back-and-forth as I don't have access to this hardware, but I'd like to try to help if I can.

The first thing I'd like to know is if this same issue persists on v0.49.2.

The next question is, does it reproduce at an input batch size > 1?

Can you try it in a lower power mode?




### neil-the-nowledgeable · 2026-05-05

 **EDITED 2026-05-05**: 0.49.2 does NOT fix the reboot — see follow-up comment

Hi Matthew,

Thanks for the quick triage. I ran the three asks plus an axis-bisection matrix on a second physical Jetson (same JetPack 6.2 / CUDA 12.6 / sm_87, bnb 0.46.1 source-built from the same SHA `4bca844…`). **Headline: bnb 0.49.2 already fixes the reboot at MAXN_SUPER.** Detail below.

### TL;DR

| Cell | Test 01 baseline (ABC, NF4, bf16/bf16, double_quant, no hygiene, batch=1) |
|---|---|
| **bnb 0.46.1 + nvpmodel mode 2 (MAXN_SUPER)** | **REBOOT** (N=4 across two physical Jetsons) |
| bnb 0.46.1 + nvpmodel mode 1 (25W stock) | PASS |
| bnb 0.46.1 + nvpmodel mode 0 (15W) | PASS |
| **bnb 0.49.2 + nvpmodel mode 2 (MAXN_SUPER)** | **PASS** ← fixed |

Whatever changed between v0.46.1 and v0.49.2 closes the most-severe regime — happy to `git bisect` if you want the responsible commit identified.

### Direct answers to your three asks

**Q: does it persist on v0.49.2?**
**No** — the reboot is gone. Source-built 0.49.2 with the same `cmake -DCOMPUTE_BACKEND=cuda -DCOMPUTE_CAPABILITY=87` flags as 0.46.1, installed via `pip install --target /tmp/bnb-0.49.2-site` and `PYTHONPATH`-shadowed over the venv's 0.46.1. Verified shadow import (`bnb.__file__ == /tmp/bnb-0.49.2-build/bitsandbytes/__init__.py`, `bnb.__version__ == 0.49.2`) before running. Test 01 baseline at MAXN_SUPER passed cleanly: shape A 3.4ms / B 9.3ms / C 83ms forward, all_pass=True, no reboot.

**Q: does it reproduce at batch > 1?**
Different fault mode at batch>1: **SIGKILL (rc=137), not system reboot.** At batch=2 and batch=8, peak memory after shape B is ~3501 MB (vs ~2507 MB at batch=1 — extra activations). The OOM-killer fires during shape C, killing the python process, but **the box stays alive**. This is consistent across all three power modes and across both bnb 0.46.1 and 0.49.2 — it's a memory-pressure phenomenon, not the bnb-code bug. Worth knowing as a separate observation but probably not the same upstream issue.

**Q: lower power mode?**
**Yes — drops the reboot entirely.** Reran the full matrix at mode 1 (25W stock JetPack default) and mode 0 (15W). Both prevent test 01 baseline from rebooting. **Per-shape timing comparison at shape C**:

- mode 2 (MAXN_SUPER): construct ~13s; baseline reboots before completing shape C forward
- mode 1 (25W): construct 18.2s, forward **190ms** → PASS
- mode 0 (15W): similar profile to mode 1 → PASS

For reference, on bnb 0.46.1 at MAXN_SUPER the *passing* variants (anything that breaks the recipe fingerprint) complete shape C forward in ~14–150ms — so mode 1's 190ms is roughly an order of magnitude slower than the typical MAXN_SUPER fast path.

**This is the diagnostic smoking gun:** the fault is timing/race-sensitive. Slower clocks give the dequant kernel + Tegra driver enough head room to complete the operation cleanly. Strong evidence the underlying bug in 0.46.1 is a race condition (allocator state, scratch buffer release, or bus arbitration) rather than a static logic error — and consistent with whatever 0.49.2 changed serializing the racing operations sufficiently to close the window even at full clock.

### Bisection matrix on bnb 0.46.1 — what triggers vs prevents the fault

While I had the harness up I ran 13 single-axis variations to isolate exactly what's load-bearing. Every test below is one knob change off the dangerous baseline (ABC, NF4, bf16/bf16, double_quant, no hygiene, batch=1). Each ran on the second Jetson at MAXN_SUPER on bnb 0.46.1; relevant results compressed:

| Knob change | Result |
|---|---|
| (none — baseline) | **REBOOT** |
| `--shape-order` ∈ {ACB, BAC, BCA, CAB, CBA} | **all 5 PASS** — only ABC (the unique strictly-monotonic-increasing-by-product order) reboots |
| `--repeat-same-shape C` (3× same shape) | PASS |
| `--shape-pair AB` / `AC` / `BC` (2 of 3) | all PASS |
| `--memory-hygiene` (`del + empty_cache + sync` between shapes) | PASS |
| `--hygiene-after-shapes A` (cleanup A↔B only) | PASS |
| `--hygiene-after-shapes B` (cleanup B↔C only) | PASS |
| `--quant-storage uint8` (bnb default; not bf16) | PASS |
| `--compute-dtype fp16` | PASS |
| `--quant-type fp4` | PASS |
| `--no-double-quant` | PASS |
| `--batch-size 2 / 8` | SIGKILL (above; not reboot) |

Some of these are at N=2 (mem_hygiene, uint8 storage, reverse_order CBA) from a deliberate corroboration pass; the rest at N=1 in this matrix. Reboot evidence on the unmodified baseline is at N=4 across two Jetsons.

**Two takeaways from the bisection**:

1. The fault requires **all of**: ABC monotonic-increase order + NF4 + bf16 storage + bf16 compute + double_quant + no hygiene + batch=1 + MAXN_SUPER. Changing any single one prevents it. The fault sits at a delicate intersection of conditions.
2. Hygiene at **either** A↔B *or* B↔C is sufficient (doesn't need both). Suggests the bnb-side fix path doesn't need to release scratch on every `Linear4bit.__del__` — even one cleanup point in the chain breaks accumulated state.

### Mitigation summary for users on bnb 0.46.1 (in case 0.49.2 isn't an option)

In rough order of "easiest to apply":

1. **Upgrade to bnb 0.49.2** (now confirmed to fix it).
2. Drop nvpmodel to mode 1 / 25W (~30% throughput cost; prevents the reboot at full bnb 0.46.1).
3. Use `bnb_4bit_quant_storage=torch.uint8` (the bnb default; FSDP-recipe users can't, but anyone else already does).
4. Add `del layer; torch.cuda.empty_cache()` between successive `Linear4bit` constructs of different shapes in the same process.

### What I haven't done but can run on request

- **`git bisect v0.46.1..v0.49.2`** with this reproducer as the test case to identify the fix commit. If you want it for the changelog or backport candidacy.
- **Realistic HF `from_pretrained` workload** to confirm the fault doesn't fire under normal model-load patterns (which exercise many copies of the same Linear shape — the safe `C-C-C` pattern from the bisection). My sense is no, but untested.
- **Power-mode behavior on bnb 0.49.2** (do mode 1 / mode 0 also pass on the new version, or did the fix specifically open MAXN_SUPER without changing the timing profile?). Probably the former; happy to verify.

Reproducer + per-test JSON results + run logs are yours, if they would be useful in the fix-commit conversation. The harness (`scripts/bnb_sm87_multishape_matrix.py`) takes all the bisection axes as flags, so further variations are cheap.

Glad to know 0.49.2 is the answer for users — and it's a much cleaner outcome than I was expecting. Thanks for the asks; they pointed straight at the most informative experiments.

### neil-the-nowledgeable · 2026-05-05

Whoops, it seems a correction to my last post is in order but also a sharper diagnostic has emerged from the continuing investigation.

### TL;DR — the prior post was wrong about 0.49.2 (sorry bout that)

When I went to identify the responsible commit via `git bisect`, I couldn't reliably reproduce the fault — and after digging into why, **bnb 0.49.2 also reboots at cold-start**. The "0.49.2 fixes the reboot at MAXN_SUPER" headline from my prior comment was based on N=1 *warm-state* test of 0.49.2, which I mistook for evidence of a version-level fix. It isn't. **The fault is state-dependent (cold-start), not version-dependent. 0.49.2 doesn't fix it.**

### The data

| Test condition | Samples | Reboots | Passes |
|---|---:|---:|---:|
| **Cold-start** (very first GPU op after fresh boot) | 9 | **7** | **2** |
| Warm-state (any subsequent test, regardless of binary or version) | 29+ | 0 | 29+ |

Cold-start sub-breakdown across binaries:

| Binary | `.so` SHA256 | Cold-start samples | Reboots | Passes |
|---|---|---:|---:|---:|
| bnb 0.46.1 venv (provisioned by my Jetson script 2026-04-24) | `120d638b…` | 3 | 2 | 1 |
| **bnb 0.49.2** (built today, persistent install) | `a7085b13…` | 1 | **1** | 0 |
| bnb 4bca844 fresh-build (built today, persistent install) | `306b8f7c…` | 1 | 0 | 1 |
| Historical (astro + rosie original #1936 matrix work) | 4 | 4 | 0 |

Cold-start reboot rate is roughly 7/9 ≈ 78% across all binaries we've tested. With N=1 cold-start sample for each non-venv binary, we can't claim version-level immunity — and we have direct refutation for 0.49.2.

### What this most-likely is

A timing race in cold-start initialization of the bnb-NF4 dequant kernel + Tegra driver. On a freshly-booted system, the CUDA driver, bnb runtime, and scratch buffer state are all cold; the race window in the multi-shape A→B→C sequence is wide enough to hit ~78% of the time. After any successful bnb-4bit op, state stabilizes and the window closes — **0/29+ reboots once warm**.

This explains:
- The recipe-axis bisection in the prior post (mem hygiene, uint8 storage, fp16 compute, fp4 quant, no double-quant, non-ABC ordering, lower power mode — all prevented the fault by either lengthening the operation, altering its allocator footprint, or doing one bnb-4bit op before C, all of which slip past or warm up the race window).
- Why "0.49.2 fixes it" looked true at first — every 0.49.2 test happened to land in warm-state context.
- The bisect's trivial convergence on `4bca844 Release v0.46.1` — the bisect wasn't finding a real source-level transition; it was just confirming our externally-provided "bad" marker.

### What's actually upstreamable

- **bnb-side fix candidate**: a small dummy bnb-4bit op (any shape) inside `Linear4bit`'s first construction or at module load — a warmup pass that closes the cold-start race window before user code hits it. Cheap, doesn't change steady-state behavior, broadly safe.
- **User-side mitigation** (works on any version, today): run any small bnb-4bit forward as warmup before 7B-class workloads after a fresh boot. Trivially cheap.
- **The mitigations from the prior post still hold** — they just work by warming the race window past, not by patching a specific source bug. Lower power mode, memory hygiene, uint8 storage, fp16 compute, alternative quant_type, non-ABC ordering: all still prevent the reboot. The mechanism for *why* they prevent it is "they shift timing past the cold-start window," not "they avoid a logic bug."

### What I'm still uncertain about

- N=1 cold-start sample for both 0.49.2 (rebooted) and fresh-build 4bca844 (passed) — small for a probabilistic claim. The 4bca844 pass is plausibly the ~22% lucky-pass case rather than evidence of build-level immunity.
- Whether the warmup-in-`Linear4bit` fix actually closes the window or just shifts it. Worth a small bnb-side experiment if you want to pursue.

### Apologies for the noise

The prior post oversold what was actually a state-dependent finding as a version-level fix. The bisect being inconclusive was the first clue something was off; testing 0.49.2 at cold-start (which I'd never actually done) closed the loop. Hopefully I reported this before the backport conversations could go too far — and happy to run any further targeted experiments on the cold-start hypothesis if useful.


### neil-the-nowledgeable · 2026-05-05

Quick followup: tested the warmup-pass hypothesis from my last comment. **3/3 passes at cold-start** with a single `Linear4bit(256, 256)` warmup forward inserted before the dangerous A→B→C sequence — against **7/9 reboots without warmup** at the same recipe and binary (cluster-venv bnb 0.46.1 at MAXN_SUPER, very first GPU op after fresh boot).

```python
# WARMUP — cheap, runs in ~3ms / 0.3 MB peak
warmup = bnb.nn.Linear4bit(256, 256, bias=False, quant_type="nf4",
                            compute_dtype=torch.bfloat16,
                            quant_storage=torch.bfloat16).to("cuda")
with torch.no_grad():
    _ = warmup(torch.randn(1, 256, dtype=torch.bfloat16, device="cuda"))
torch.cuda.synchronize()

# THEN the dangerous A → B → C sequence runs cleanly
```

N=3 is small but the contrast (78% → 0% reboot) is large enough that the mechanism looks robust. Notably, shape C's forward time varied 89→148→323 ms across the three warmup runs — the underlying timing variance is real, but the warmup-immunity holds across all of it.

If you want to narrow the bnb-side fix surface: a one-shape warmup at module load, or in `Linear4bit.__init__` on first cold context, seems to be enough. Happy to share the test script (`bnb_sm87_warmup_test.py`) or per-run JSON if useful.


### neil-the-nowledgeable · 2026-05-06

One more note about the cold-start warmup to real-model multi-layer load.

The 2026-05-05 verification was at the synthetic ABC reproducer (`Linear4bit(4096,32768)` → `Linear4bit(4096,128256)` → `Linear4bit(3584,152064)`). An open question I had was does the warmup primitive (a tiny `Linear4bit(256,256)` NF4 forward at process start) transfer to a real-model dynamic NF4 quantization sequence, where HF transformers wraps every linear in a model with `Linear4bit` during `from_pretrained()`?

I've only shown this to be the case one time on my Jetson Orin Nano Super 8 GB (sm_87, JP6.2, MAXN_SUPER, fresh cold boot, single run), but once seemed reasonable given the context. Details:

- Warmup ran clean (`Linear4bit(256,256)` NF4 + bf16 storage + bf16 compute_dtype; 1 sec wall, 0 reboots).
- Then `Mamba2ForCausalLM.from_pretrained(...)` over a 7.3B-param model completed cleanly in 181 s, peak GPU memory 4173 MB. This is several hundred `Linear4bit` constructions across a varied shape set: `in_proj`, `out_proj`, `x_proj`, and `dt_proj` per decoder block, plus `lm_head` and embeddings — varied input/output dimensions, non-monotonic ordering, mostly non-power-of-2.
- No reboot during construction. No SIGKILL. No anomalous memory growth.

So for this hardware + recipe + warmup, the cold-start race does NOT fire on a real-model multi-layer dynamic NF4 quantize sequence either. It's not strict transfer-by-proof (different shape distribution from the ABC reproducer; non-monotonic shape ordering; non-power-of-2 dimensions in some places) but it's a useful additional data point: the warmup mitigation isn't narrow to the specific A→B→C synthetic sequence — it survives the 200+ Linear4bit construction sequence of a real model under HF transformers' load path.

Counter-evidence from the same run (worth flagging because it confirms there's something else going on at sm_87 and Mamba shapes specifically): after the model was loaded successfully, `model.generate(..., max_new_tokens=50)` triggered a kernel-level reboot of the Tegra ~30s into forward. The log explicitly captured the warning *"The fast path is not available because on of (selective_state_update, causal_conv1d_fn, causal_conv1d_update) is None. Falling back to the naive implementation"* — i.e., the Mamba SSM optimized CUDA kernels weren't installed and the naive PyTorch fallback was running at forward time. This is a separate fault from the cold-start race, and the reboot signature is different: it's deep in the SSM scan / conv1d kernel path at generation time, not in `Linear4bit` construction. This seemed worth noting since at first look I confused it with a cold-start race recurrence; the persistent log (i.e., writing logs to a non-tmpfs path, since `/tmp` is wiped on reboot) made the distinction visible.

In short:

- Warmup mitigation: N=3 (synthetic ABC) + N=1 (real-model multi-layer NF4 load on Mamba2-7B) all clean.
- The remaining sm_87 + Mamba forward-path issue is unrelated to this issue. It's about HF transformers' naive `selective_state_update` fallback on Tegra, not about the bnb 4-bit quantize/dequant kernels.

"EDIT: I just got Mamba/SSM model running on my Jetson Orin Nano Super working via JAL cu128 torch + source-built kernels; will share recipe and other details soon, for those who are interested.


### neil-the-nowledgeable · 2026-05-11

Two additions I omitted from the original body:

### Cross-references to prior bnb FSDP work

- [PR #970](https://github.com/bitsandbytes-foundation/bitsandbytes/pull/970) (Answer.AI) — original FSDP-QLoRA enablement. Added `bnb_4bit_quant_storage=bf16` so FSDP can shard Params4bit as a float dtype. Its body explicitly notes: *"Currently QLoRA finetuning using FSDP's low memory via the sync_module_states option doesn't work. Enabling this will require a future PR."* **This issue is the forward-correctness regression that blocks that future PR for FSDP2**: even with bf16 quant_storage, packed-NF4 nibbles encoded as bf16 NaN patterns get canonicalized by FSDP2's swap path before bnb's matmul_4bit can decode them.
- [PR #1866](https://github.com/bitsandbytes-foundation/bitsandbytes/pull/1866) + [PR #1916](https://github.com/bitsandbytes-foundation/bitsandbytes/pull/1916) — added `@property` accessors on Linear4bit so state_dict traversal works under FSDP2. State_dict serialization is fine; this issue extends bnb's FSDP integration history with the runtime-forward correctness gap that those PRs didn't cover.

### What's actionable for bnb maintainers

This is primarily a **PyTorch FSDP2 / DTensor** issue (the parameter-swap mechanism that re-routes `self.weight` access during forward through a float-canonicalizing code path). With the byte-level evidence in hand, the fix target is sharp: likely `torch.distributed._composable.fsdp._fsdp_param.py` (around `init_dtype_attrs` or the parameter-storage setup that allocates the swap-target buffer). The fix would read the bf16 Tensor-subclass buffer via `.view(torch.uint8)` (byte-true) rather than through any code path that triggers IEEE 754 NaN canonicalization. Alternative: skip the canonicalization step for parameters whose owning Tensor subclass overrides `__torch_function__` (i.e., Params4bit explicitly opts out of float-semantic handling).

Three concrete options for bnb maintainers, in increasing order of bnb-side effort:

1. **Cross-link a PyTorch core issue.** I'm am happy to file the cross-link against FSDP2 / DTensor maintainers with this byte-level evidence if maintainers prefer that routing. The root cause is in PyTorch; bnb is the most-visible affected library because Params4bit is the most-used Tensor subclass with packed integer data in float storage.

2. **Document the cached-ref workaround in bnb's FSDP-QLoRA docs** as the current path for FSDP2 users (until upstream lands a fix). This is the same recipe the Answer.AI FSDP-QLoRA docs use for FSDP1; the FSDP2 section just needs the additional cached-ref step before training begins.

3. **Optionally ship a `bitsandbytes.fsdp2_utils.install_fsdp2_workaround(model)` helper.** ~50 LoC, gives users a one-line fix. Validated bit-identical to 13 decimals at WS=2 with real PEFT + 154 Linear4bits; cluster_tests step 6 at WS=4 multi-host training completes end-to-end with descending finite loss on all 4 ranks. Happy to submit a PR.

Reproducer scripts (configuration-invariance matrix, byte-level NaN forensic, per-Linear forward delta) available as gists or in a PR-companion repo on request.

