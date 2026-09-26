# [Issue #4157] [Bug] IMA in trtllm_bf16_moe autotune sweep at the 1-token tuning profile (B200/sm100f, BF16 dynB GEMM2)

source: https://github.com/flashinfer-ai/flashinfer/issues/4157
state: open | updated: 2026-09-22T08:58:39Z
labels: needs-triage

## 正文

**Environment:** 8×B200 (sm100f), vLLM 0.26.0, flashinfer-python 0.6.14
(flashinfer-cubin/jit-cache bundled), GLM-5.2 NVFP4 TP8, MTP speculative
decoding (`num_speculative_tokens=6`), `--moe-backend flashinfer_trtllm`.
The MTP drafter layer is the model's only BF16 MoE (hidden 6144,
intermediate/rank 256, 256 experts, top-8, DeepSeekV3 routing).

**Symptom:** engine warmup crashes with `cudaErrorIllegalAddress` during the
AutoTuner sweep for `flashinfer::trtllm_bf16_moe`. Reproduced on vLLM 0.24,
0.26.0, and nightly (2026-07-25).

**Findings** (via per-launch device-sync instrumentation compiled into
`trtllm_batched_gemm_runner.cu` / `trtllm_fused_moe_kernel_launcher.cu`):

1. The fault occurs at the **m=1 (1-token) tuning profile**. First faulting
   launch: `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s6_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f`
   (GEMM2), invoked as the default config in `choose_one`'s
   `do_preparation` run.
2. Inputs at the faulting launch are valid: `numNonExitingCtas=8`,
   `totalNumPaddedTokens=64`, CTA maps consistent for m=1 × top-8 × E=256,
   no pending CUDA error.
3. Per-tactic exclusion does not resolve it, for two reasons: (a) the fault
   is not unique to one cubin: with the named cubin removed from
   `mPassingConfigIndices`, the next BF16 dynB candidate faults at the same
   m=1 bucket; (b) even when the autotuner catches a candidate's failure
   during profiling, `cudaErrorIllegalAddress` is context-fatal, so the sweep
   cannot skip-and-continue past it, so any faulting candidate kills the
   engine regardless of exclusion lists. Hence the profile-level fix below.
4. Runtime m=1 execution with default/cached tactics is healthy (drafter
   draft steps run 1-token batches in production without issue; autotune-off
   serving is stable). The fault is specific to executing these candidates
   under the tuning sweep's conditions.
5. **Fix validated:** dropping only the m=1 profile from this op's tuning
   buckets, same principle as the existing correctness skip of clusterZ>1
   cubins in `trtllm_batched_gemm_runner.cu`, applied at the tuning-profile
   level. The bf16 sweep completes 20/20 remaining profiles and the engine
   serves. Interim options on released versions, both validated:
   - supported knob (coarse): `VLLM_FLASHINFER_AUTOTUNE_SKIP_OPS=trtllm_bf16_moe`
     skips the whole op's tuning;
   - surgical (matches this fix): a `sitecustomize` wrapper around
     `AutoTuner._generate_optimization_profiles` that filters the 1-token
     profile out of this op's tuning buckets (code below).

**Performance funnel** (greedy, temperature 0, 600 completion tokens, bs=1,
streamed decode rate excl. TTFT; GLM-5.2-NVFP4 TP8 on 8xB200, MTP=6):

| config | bf16 autotune state | decode tok/s |
|---|---|---|
| cutlass MoE backend (our crash fallback) | n/a | 208 |
| trtllm + `SKIP_OPS` workaround (bf16 op tuning skipped) | op skipped | 262 / 264 / 279 |
| trtllm + m=1 profile omitted (**this fix**) | 20/20 profiles tuned | 279 / 280 / 281 |

i.e. the fix recovers full trtllm autotune value (+35% single-stream decode
over the cutlass fallback) while eliminating the crash.

<details>
<summary>sitecustomize monkeypatch (as validated)</summary>

```python
"""sitecustomize.py: drop the m=1 tuning profile for trtllm_bf16_moe.

BF16 dynB candidates fault at the 1-token tuning bucket; runtime m=1 with
cached/default tactics is healthy, so only the sweep's m=1 profile is
removed. Enable with DROP_M1_BF16_MOE=1.
"""

import os
import sys


def _install():
    import flashinfer.autotuner as at

    orig_choose = at.AutoTuner.choose_one
    orig_gen = at.AutoTuner._generate_optimization_profiles

    def gen_no_m1(self, tuning_config, inputs):
        profiles = orig_gen(self, tuning_config, inputs)
        if getattr(self, "_drop_m1", False):
            kept = []
            dropped = 0
            for p in profiles:
                shapes = p.get_opt_shapes()
                m = None
                for s in shapes:
                    # Token-dim detection keys off the hidden_states-like
                    # tensor; 6144 is our model's hidden size -- adapt, or
                    # derive the token dim from
                    # tuning_config.dynamic_tensor_specs.
                    if s and len(s) >= 2 and s[1] in (6144,):
                        m = s[0]
                        break
                if m == 1:
                    dropped += 1
                else:
                    kept.append(p)
            if dropped:
                print(f"[m1shim] dropped {dropped} m=1 profile(s), "
                      f"kept {len(kept)}", file=sys.stderr)
            return kept or profiles
        return profiles

    def choose_one(self, custom_op, runners, tuning_config, inputs, **kwargs):
        self._drop_m1 = "bf16" in custom_op
        try:
            return orig_choose(self, custom_op, runners, tuning_config,
                               inputs, **kwargs)
        finally:
            self._drop_m1 = False

    at.AutoTuner._generate_optimization_profiles = gen_no_m1
    at.AutoTuner.choose_one = choose_one
    print("[m1shim] installed", file=sys.stderr)


try:
    if os.environ.get("DROP_M1_BF16_MOE") == "1":
        _install()
except Exception as e:  # noqa: BLE001
    print(f"[m1shim] install failed: {e}", file=sys.stderr)
```

</details>

Possibly related to #3427 (kernel-family overlap:
`t128x8x128*schPd2x1x2x3*dynB` GEMM2, IMA on B200); different trigger and
serving stack.

PR with the m=1 profile exclusion: #4158.
Repro script, instrumentation patches, and full logs available on request.

*Disclosure: debugging and drafting were AI-assisted (Claude); findings
validated by a human on hardware.*


## 评论 (6)

### hiteshjain118 · 2026-07-26

PR with the m=1 profile exclusion: #4158 (draft). Full `tests/autotuner/` suite (core + CUDA integration) passes 240/240 on B200 with the change.

### janbernloehr · 2026-08-31

We evaluated the proposed #4158 change on B300/SM103 with the same fixed workload and software stack used for the reproduction.

The unmodified baseline failed 3/3 with 352 skipped tactics and an illegal-memory-access error during BF16 TRT-LLM MoE autotuning. The #4158 equivalent, setting tune_min_num_tokens=2, also failed 3/3 with 351 skipped tactics and the same fault chain. Removing the first tuning profile only shifted the progress index; it did not prevent the failure.

Thus #4158 is not a mitigation for this B300/SM103 failure. The issue remains open; the next useful data point is tactic-level logging for the failing bucket.

### XFDG · 2026-09-12

I retested the exact reported B200 geometry against current main d70a043f5edbd0ccb363784ffe7fe97608b2d9a3:

- NVIDIA B200 / SM100, CUDA 13.1, PyTorch 2.11.0a0+eb65b36914.nv26.02
- E=256, top_k=8, H=6144, I=256, BF16 shuffled weights
- exact m=1-only autotune (tune_max_num_tokens=1): 1/1 profile passed
- full sweep (tune_max_num_tokens=16384): 22/22 profiles passed
- m=1 was not filtered or skipped; the output was finite and both runs exited 0

I could not reproduce the old context-fatal IMA on current main. Since the original report was on 0.6.14 and the closed #4158 profile-level workaround was not general across SM103, I do not think resubmitting that workaround is appropriate. If this still reproduces on a current build, the most useful next artifact would be the exact failing tactic/cubin name and current package commit.

### janbernloehr · 2026-09-15

Thanks @XFDG! Confirmed on our end. The affected Blackwell BF16 TRT-LLM-Gen MoE workloads continued to reproduce the illegal-memory-access failure with FlashInfer 0.6.15–0.6.17, but stopped reproducing after upgrading to FlashInfer 0.6.18. With 0.6.18, the exercised configurations complete the full 22/22 autotune sweep successfully.

This points to #4319 (fix(moe): pad BF16 TRTLLM-Gen intermediates to 128 KiB) as the actual fix. It was merged on August 10 and is included in the 0.6.18 release. The previously proposed m=1 profile exclusion in #4158 was not a general mitigation—we confirmed that it merely moved the failure to the next profile on SM103.
Our current assessment is therefore:
- the original failure is no longer reproducible with FlashInfer 0.6.18/current main;
- #4319 fixed the underlying BF16 intermediate-buffer under-allocation;
- #4158 should remain closed because the profile-level workaround is unnecessary and incomplete.

From our side, it would be reasonable to close #4157 as fixed by #4319 / FlashInfer 0.6.18. If the failure recurs on a current release, we can reopen with the exact failing tactic and package commit.

### hiteshjain118 · 2026-09-20

@janbernloehr thanks for following up and mitigating the issue working with the team. I wasn't sure if anyone was going to work on this because my PR #4158 was closed after pattern matching, without any feedback and no response after repeatedly comments. It took me 1.5 day of human and machine time to narrow down traversing all the stack layers and propose a workaround, mitigating the hacks in the higher layers. 
 
I would love to contribute to flashinfer, but may be good to do a brief intro call first. Let me know if you'd be open to it. 

### janbernloehr · 2026-09-22

Thanks again for the detailed investigation. With #4319 shipped in FlashInfer 0.6.18, both current-main testing and our downstream release validation are green, and our related regressions are closed.
Could we close this issue as completed? If it recurs on a current release, we can reopen it with the failing tactic and package commit.
