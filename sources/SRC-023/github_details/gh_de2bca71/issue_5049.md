# [Issue #5049] [Bug] fused MoE GPU-faults on GLM-5.3-Flash 288-expert/top-8 shape (gfx950, no tuned config)

source: https://github.com/ROCm/aiter/issues/5049
state: open | updated: 2026-08-28T23:03:47Z
labels: 

## 正文

### Problem

On **gfx950 (MI350X, 8× TP8)**, AITER's fused MoE GPU-faults on GLM-5.3-Flash's expert shape (288 experts, top-8). It is reached during vLLM's memory profiling and kills every rank:

```
[aiter] run_1stage = True, xbf16 = False, ksplit = 0 q_type = QuantType.per_1x128 block_m = 32 use_nt = True, estimated_m_per_expert = 1
[aiter] [fused_moe] using 1stage default for ('gfx950', 256, 64, 4096, 256, 288, 8,
        'ActivationType.Silu', 'torch.bfloat16', 'torch.float8_e4m3fn',
        'torch.float8_e4m3fn', 'QuantType.per_1x128', True, False)
Memory access fault by GPU node-2 (Agent handle: 0x2381c400) on address 0x79eaf1a00000. Reason: Unknown.
```

The `using 1stage default` line is the interesting part: there is no tuned config for this shape, and the default path does not survive it. Setting `VLLM_ROCM_USE_AITER_MOE=0` (Triton MoE) gets past it, and the model then serves correctly.

### Environment

- 8× MI350X (gfx950), ROCm 7.2.3, Triton 3.7.1, TP=8
- `zai-org/GLM-5.3-Flash` (320B total / 18B active, 288 experts, top-8), native FP8 weights
- vLLM `glm-release` (vllm-project/vllm#53906 + the ROCm implementation in vllm-project/vllm#53943), `VLLM_ROCM_USE_AITER=1`
- `--tensor-parallel-size 8 --kv-cache-dtype bfloat16 --max-model-len 131072 --max-num-seqs 64 --gpu-memory-utilization 0.85`

### Why I am filing it separately

It looks independent of the sparse-MLA work in #4919 — it fires earlier, during profiling, well before the first attention decode, and disabling only the MoE clears it while leaving everything else in place.

Also worth noting: SGLang's own AMD recipe for this model (sgl-project/sglang#36608, merged today, GSM8K-verified on MI300X and MI355X) specifies `--moe-runner-backend triton` rather than AITER's fused MoE. So the Triton fallback appears to be the intended configuration for GLM-5.3 on ROCm today — but a GPU fault rather than a graceful "no tuned config, falling back" is still worth fixing, since it gives users no indication that the MoE backend is the problem.

I see #5006 (`fix glm5 regression`) and #5045 (`Retune GLM5.2 mxfp4 MoE`) landed recently; if either is expected to cover the 288/top-8 shape I am happy to re-test — 8× MI350X with the model staged, full boot in ~12 minutes.


## 评论 (9)

### stefanskiasan · 2026-08-27

**Important qualifier: this fault appears to be specific to the FP8 checkpoint. AMD's own MXFP4 recipes run AITER's fused MoE on the same GPU without trouble.**

sgl-project/sglang#36712, opened this afternoon by @andyluo7, adds GLM-5.3-Flash MXFP4 recipes validated *"on one 8x MI350X (gfx950) node"* — the same hardware I filed this from. Its configuration explicitly keeps **AITER MoE** enabled, alongside full decode graphs:

> preserve the validated BF16 KV + TileLang DSA, Triton linear-attention, **AITER MoE**, and full decode-graph settings

GSM8K there is 1,282/1,319 (TP4) and 1,281/1,319 (TP8+EP8), all `stop`, no faults.

So the shape alone is not the trigger. Both checkpoints are 288 routed experts / top-8; what differs is the weight format:

| | checkpoint | AITER fused MoE |
|---|---|---|
| this report | `zai-org/GLM-5.3-Flash` (native FP8, `QuantType.per_1x128`) | GPU-faults |
| sglang#36712 | `amd/GLM-5.3-Flash-Quark-MXFP4` | works, GSM8K-verified |

That matches the dispatch line I quoted originally, which selects on the FP8 tuple:

```
[aiter] [fused_moe] using 1stage default for ('gfx950', 256, 64, 4096, 256, 288, 8,
        'ActivationType.Silu', 'torch.bfloat16', 'torch.float8_e4m3fn',
        'torch.float8_e4m3fn', 'QuantType.per_1x128', True, False)
```

So please read this as: **no tuned config for the 288/top-8 shape in the FP8 (`per_1x128`) path, and the 1-stage default faults there rather than falling back**. The MXFP4 path is unaffected. Retitling or scoping accordingly is probably the right move; I would still argue a GPU fault is the wrong failure mode for a missing tuned config, since it gives no indication the MoE backend is at fault.

Worth noting for anyone landing here from the vLLM side: vLLM's published ROCm recipe (vllm-project/recipes#857) uses the FP8 checkpoint and specifies Triton MoE, which is consistent with this. If the intended answer for FP8 on gfx950 is "use Triton MoE", saying so in the dispatch — a warning and a fallback rather than a fault — would be enough.

Still happy to re-test: 8× MI350X, FP8 checkpoint staged, full boot in ~12 minutes. I have not pulled the MXFP4 checkpoint, so I cannot confirm the contrast on our node directly — that part is from sglang#36712's validation record, not my own measurement.


### andyluo7 · 2026-08-28

I prepared a narrow candidate fix for this shape:

- commit: https://github.com/andyluo7/aiter/commit/c12fffe61
- branch: https://github.com/andyluo7/aiter/tree/fix/glm53-fp8-fmoe-gfx950

It adds a gfx950/256-CU model tuning row for the GLM-5.3 FP8 FMoE shape and selects the existing non-vskip kernel:

```text
_ZN5aiter52fmoe_bf16_blockscaleFp8_g1u1_novs_silu_1tg_ps_32x256E
```

The row is specific to hidden=4096, inter=256, experts=288, topk=8, Silu, BF16 output, FP8 A/W, and `QuantType.per_1x128`. Because AITER rounds sub-32768 token counts to powers of two, the `token=64` row covers actual M=33..64.

Validation completed against current AITER main (`b0d56a038`) on one 8x MI350X/gfx950 host with a ROCm 7.2.3 container:

- production config merge/collision suite: 15 passed;
- dedicated FMoE `--run_config`: passed;
- actual M=33,48,63,64 with random, balanced, and concentrated-eight-expert routing: 12/12 completed;
- every case selected the non-vskip kernel;
- logits distance range: `6.72e-05` to `7.90e-05`;
- no NaNs, GPU faults, or residual KFD processes;
- M=32 and M=65 retain the existing default dispatch, confirming the intended bucket boundary.

On a separate gfx950 node, three-process M=64 timing gave 149.29 us median for vskip and 151.15 us for non-vskip (~1.25% operator cost). Full-model TP8 performance validation is still pending.

The current vskip kernel did not reproduce the fault on our available system, so this does not yet prove the original firmware-sensitive failure is resolved. Could you please retest commit `c12fffe61` on the original faulting MI350X/ROCm 7.2.3 system? A successful TP8 boot through memory profiling would be the decisive validation before opening the upstream PR.


### stefanskiasan · 2026-08-28

**Retested `c12fffe61` on the original faulting system. It fixes it — TP8 boots through memory profiling with AITER MoE enabled, and it is also 12–18 % faster than the Triton fallback.**

Same 8× MI350X (gfx950) node, ROCm 7.2.3, same container that produced the original fault. Only change: `VLLM_ROCM_USE_AITER_MOE=1` (was 0) plus your two CSVs mounted over `aiter/configs/model_configs/`.

**Boot:**

```
Selected kernel:  ..._novs_silu_1tg_ps_32x256
GPU KV cache size: 16,907,063 tokens
Memory access faults: 0
```

Server reaches `200 OK`, answers correctly ("Die Hauptstadt von Frankreich ist Paris.", 17×23 = 391, both `finish_reason: stop`). Before the fix, the identical configuration died during profiling on all 8 ranks right after `[aiter] [fused_moe] using 1stage default for ('gfx950', 256, 64, 4096, 256, 288, 8, ...)`.

**Throughput** — same benchmark, 8 fixed prompts, `temperature=0.0`, `max_tokens=1024`, BF16 KV, decode CUDA graphs on, `--max-model-len 131072 --max-num-seqs 256`, with ROCm/aiter#5060's GEMM CSV also mounted in both arms:

| N | Triton MoE | AITER MoE + this fix | |
|---:|---:|---:|---|
| 64 | 2,328 tok/s | **2,607 tok/s** | +12.0 % |
| 256 | 2,766 tok/s | **3,261 tok/s** | +17.9 % |

Zero faults across the whole sweep, all requests completed.

So the fix is worth more than closing the crash: the Triton fallback that the published recipes prescribe (`--moe-runner-backend triton` in sgl-project/sglang#36608, `VLLM_ROCM_USE_AITER_MOE=0` in vllm-project/recipes#857) is leaving ~18 % on the table at N=256 on this hardware. Worth revisiting those once this lands.

One observation, not a blocker: shapes outside the new row still take the default path, e.g.

```
using 1stage default for ('gfx950', 256, 128, 4096, 256, 288, 8, ...)
using 1stage default for ('gfx950', 256, 16384, 4096, 256, 288, 8, ...)
```

Neither faulted in our runs — token=16384 is the chunked-prefill batch and token=128 appears during warmup — so the M=33..64 bucket does look like the one that mattered. But if the underlying vskip issue is firmware-sensitive rather than shape-specific, those buckets are still on the default kernel and might surface elsewhere. Your call whether to widen the coverage or keep the fix narrow.

Happy to re-run anything before you open the upstream PR, including a longer soak or the other buckets — full boot here is ~12 minutes and the benchmark sweep another ~6.


### stefanskiasan · 2026-08-28

**Follow-up to my previous comment — please read before opening the PR. The boot fix holds, but the resulting kernel looks numerically degraded, and I should have checked that before calling it a win.**

After posting the throughput numbers I ran an output-quality check. Same container, same weights, same sampling (`temperature=0.0`), **only `VLLM_ROCM_USE_AITER_MOE` differs** — 0 selects the Triton fallback, 1 selects your fixed kernel with both CSVs mounted.

The probe is a single-tool function-calling request (`get_weather`, one required string parameter `city`) with a filler prefix of growing length, `tool_choice: "auto"`. A pass means vLLM's GLM tool parser emitted a structured `tool_calls` entry; a fail means it did not.

| Prompt tokens | AITER MoE (`=1`) | Triton (`=0`) |
|---:|:---|:---|
| 167 | pass | pass |
| 27,367 | **fail** | pass |
| 54,567 | **fail** | pass |
| 81,767 | **fail** | pass |
| 108,967 | fail | pass |
| 122,567 | **fail** | pass |

Repeated: Triton **34/36** across four full sweeps plus a two-tool variant; AITER **1/9**. The two Triton misses were the model asking a clarifying question ("for which city?") — ordinary behaviour. The AITER misses are not:

```
<tool_call>getWeather<arg_key>location</arg_key><arg_value>Hamburg</arg_value></tool_call>
<tool_call>get_weather/location=get
Ich rufe das Wetter für Hamburg ab.Ich rufe das Wetter für Hamburg ab.Ich rufe d…
```

The tool is named `get_weather` with parameter `city`. Under the AITER kernel the model invents `getWeather` / `location`, mangles the tag structure, and degenerates into repetition. vLLM's parser runs with `validate_tool_names=True`, so an invented name is dropped and the raw markup surfaces as content — which is why these show up as "fail" rather than as a wrong call.

Short prompts are unaffected: "Was ist die Hauptstadt von Frankreich?" and 17×23 both answer correctly under AITER. The degradation is length-dependent and hits structured output first, which is the usual signature of an accumulating numerical error rather than a formatting problem.

So the honest summary of my testing:

- ✅ `c12fffe61` **fixes the memory access fault.** TP8 boots through profiling, 0 faults across every run — that part I confirm without reservation.
- ✅ It is genuinely faster: +12 % at N=64, +18 % at N=256, +29 % at N=512 (3,915 vs 3,034 tok/s).
- ❌ But output quality regresses sharply beyond ~25k tokens, and I would not ship it in this state.

I don't know whether the fault is in the `novs` kernel itself or in the tuning rows steering these shapes to it, and I can't tell from outside which is more likely — you'll have a much better instinct for that than I do. If it helps, I'm happy to run whatever isolates it: a specific bucket forced on/off, a numerical diff of MoE outputs against the Triton path at a fixed input, or a bisect over the CSV rows. Boot is ~7 minutes here and the probe another ~4, so iterations are cheap on my side.

Sorry for the incomplete first report — the crash fix is real and I got ahead of myself on the rest.


### andyluo7 · 2026-08-28

Thanks for the follow-up. This disqualifies the `novs` candidate as an upstream fix; I will not open the PR with that kernel.

I prepared a second, deliberately separate retest branch:

- branch: https://github.com/andyluo7/aiter/tree/fix/glm53-fp8-fmoe-gfx950-vskip-nops
- tip: https://github.com/andyluo7/aiter/commit/610de6deb

It keeps `vskip`, which is the path that passed your long-context checks, but switches only the M=33..64 bucket from the faulting persistent kernel:

```text
..._vs_silu_1tg_ps_32x256
```

to the existing non-persistent kernel:

```text
..._vs_silu_1tg_32x256
```

Why this is the next useful isolation: your original crash names the persistent `vs ... ps` kernel, while the quality regression appears only after switching away from `vskip`. This candidate removes persistence without changing the vskip behavior.

I screened all four available 32x256 combinations on MI350X/gfx950 at actual M=33,48,63,64 with random, balanced, and concentrated-eight-expert routing (12 cases per kernel). The non-persistent vskip candidate completed all 12 without NaNs or faults. Its M=64 random-routing latency was 162.738 us versus 162.818 us for persistent vskip in the same screen; logits-distance values were comparable across the two. Postflight showed no KFD processes or kernel-fault messages.

That operator screen is only a filter, not proof of model quality—the short operator metrics also failed to expose the `novs` long-context regression. Could you please retest the branch tip on the original system with both decisive checks?

1. TP8 boot through memory profiling, confirming selection of `_vs_silu_1tg_32x256` and zero memory faults.
2. The same long-context tool-calling probe against Triton, especially >=27K prompt tokens.

If both pass, a short N=64/256/512 throughput rerun would establish whether it retains the AITER advantage. If it still faults, the next safe path is a tuned two-stage row or a regenerated/fixed 32x256 assembly kernel; I would not widen the `novs` row.


### stefanskiasan · 2026-08-28

**`610de6deb` passes both decisive checks on the original faulting system. Your isolation was right: the crash was the persistence, the quality regression was the loss of `vskip`.**

Same 8× MI350X (gfx950) node, ROCm 7.2.3, same container. Only change vs. the Triton arm: `VLLM_ROCM_USE_AITER_MOE=1` plus your two CSVs.

**1. Boot through memory profiling**

```
ready after 440 s
selected kernel:  ..._vs_silu_1tg_32x256      (non-persistent vskip, as intended)
Memory access faults: 0
```

**2. Long-context tool calling** — the check that killed the `novs` candidate (1/9 there). Single-tool `get_weather(city)`, `tool_choice: "auto"`, `temperature=0.0`, growing filler prefix; a pass means vLLM's GLM parser emitted a structured `tool_calls` entry:

| Prompt tokens | 167 | 27,367 | 54,567 | 81,767 | 108,967 | 122,567 |
|---|---|---|---|---|---|---|
| run 1 | pass | pass | pass | pass | pass | pass |
| run 2 | pass | pass | pass | pass | pass | pass |
| run 3 | pass | pass | pass | pass | pass | pass |
| run 4 | pass | pass | pass | pass | pass | pass |

Plus a two-tool variant (`read_file(path)` alongside `get_weather(city)`) at the same six lengths: 12/12.

**36/36 total, zero faults.** For reference in the same harness: Triton scored 34/36 (its two misses were the model asking "which city?" — ordinary behaviour), and the `novs` candidate scored 1/9.

**3. Throughput** — 8 fixed prompts, `temperature=0.0`, `max_tokens=1024`, BF16 KV, decode CUDA graphs on, `--max-model-len 131072 --max-num-seqs 256`, aiter#5060's GEMM CSV mounted in both arms:

| N | Triton | `novs` (rejected) | **`610de6deb`** | vs Triton |
|---:|---:|---:|---:|---:|
| 64 | 2,328 | 2,607 | **2,632** | +13.1 % |
| 256 | 2,766 | 3,261 | **3,428** | +23.9 % |
| 512 | 3,034 | 3,915 | **3,981** | +31.2 % |

So this candidate is both faster than `novs` and correct, which is a better outcome than I expected — I had assumed the quality cost bought the speed.

From my side this is ready for the upstream PR. Two notes for the description, neither blocking:

- The shapes outside the retuned bucket still take the default path (`using 1stage default for ('gfx950', 256, 128, ...)` and `(..., 16384, ...)`). Neither faulted in any run here, but if the underlying issue is persistence rather than this specific bucket, those are still on the persistent kernel.
- Worth revisiting the published recipes once this lands: sgl-project/sglang#36608 prescribes `--moe-runner-backend triton` and vllm-project/recipes#857 `VLLM_ROCM_USE_AITER_MOE=0`. On this hardware that guidance now costs ~31 % at N=512. I can post the numbers there once your PR has a link to point at.

Happy to re-run anything on request — full boot here is ~7 minutes, the quality sweep ~4, the throughput sweep ~6.


### stefanskiasan · 2026-08-28

**Correction to my validation above, before you open the PR: the 36/36 number is weaker evidence than I presented it as. The boot and throughput results stand unchanged.**

Overnight I found that GLM-5.3-Flash on this system does not produce reproducible output at `temperature=0` once prompts get long — same server process, same request, sent sequentially with nothing else in flight:

| Prompt tokens | distinct answers out of 4–5 runs |
|---:|---|
| 35 – 6,835 | 1 |
| 11,595 | 2 |
| 12,955 – 23,835 | 1 |
| 27,235 | 4 |
| 54,435 | 4 |
| 122,435 | 3 |

Short prompts are perfectly stable; long ones are not, and it is a probability that grows with length rather than a threshold. Details and the seven causes I ruled out are in vllm-project/vllm#53943.

**What that means for my report on this issue.** The tool-calling probe I used to compare candidates runs six prompt lengths, four of them past 25k. On a base that unstable, a single sweep is a sample, not a measurement:

- The **36/36** for `610de6deb` was four sweeps. Better than one, but all four ran within a few minutes on one server instance, so they share whatever state that instance happened to land in.
- The **1/9** for the `novs` candidate is the number I am now least comfortable with. It is what disqualified that kernel, and I reported it as decisive.
- Triton's **34/36** has the same weakness.

I do not think the `novs` conclusion is wrong — the failure mode there was qualitatively different from anything I have seen since (invented function names like `getWeather`, mangled tag structure, degeneration into repetition, at every length past 25k across nine sweeps, while short prompts stayed clean). That is not the signature of the run-to-run noise I have now characterised. But "I do not think it is wrong" is a weaker statement than what I wrote, and you are about to open a PR on it.

**What still stands without qualification**, because none of it depends on long-context output:

- `610de6deb` boots TP8 through memory profiling with **zero memory access faults**, selecting `..._vs_silu_1tg_32x256`. Reproduced across several boots.
- Throughput: **+13.1 % / +23.9 % / +31.2 %** at N=64/256/512 versus Triton (2,632 / 3,428 / 3,981 vs 2,328 / 2,766 / 3,034). Measured repeatedly, stable to within a few percent.
- Short-prompt correctness is unaffected and reproducible.

**Suggestion, entirely your call.** If the PR description quotes correctness numbers from my testing, I would keep them to "no faults, short-prompt output correct, long-context tool calling substantially better than the `novs` candidate" rather than a hard 36/36. If you want a stronger number I can run the probe across N independent boots and report the distribution instead of a single figure — that is roughly 15 minutes per boot here, so a 10-boot distribution is an afternoon. Say the word and I will run it.

Sorry to move the goalposts after the fact. I would rather hand you a softer number now than have it questioned after the PR is up.


### stefanskiasan · 2026-08-28

**Ran the multi-boot distribution I offered. It reverses my earlier correctness comparison: across four independent boots per arm, Triton scores higher than `610de6deb`, not lower. The throughput advantage is unchanged.**

Method: four independent server boots per arm, two sweeps of the six-length tool-calling probe per boot (`get_weather(city)`, `tool_choice: "auto"`, `temperature=0.0`, prompt lengths 167 / 27k / 55k / 82k / 109k / 123k tokens). A pass means vLLM's GLM parser emitted a structured `tool_calls` entry naming `get_weather`. Everything else held fixed, including the tuned GEMM CSVs.

| | correct | sweeps | min | max |
|---|---:|---:|---:|---:|
| `610de6deb` (AITER fMoE) | **33/42 = 78.6 %** | 7 | 4/6 | 6/6 |
| Triton fMoE | **45/48 = 93.8 %** | 8 | 4/6 | 6/6 |

Two-proportion z ≈ 2.1, p ≈ 0.03. Marginal, but the failures are not spread randomly — they concentrate at the same two lengths in both arms, and the AITER arm fails there about three times as often:

| failing length | `610de6deb` | Triton |
|---|---:|---:|
| 27k tokens | 6 | 2 |
| 55k tokens | 3 | 1 |
| all others | 0 | 0 |

**Why my earlier 36/36 vs 34/36 was misleading.** Both of those came from a single boot per arm. As I noted in my previous comment, this system is not run-to-run reproducible at long context, and 27k and 55k happen to be exactly the lengths where that instability bites hardest. A single sweep at those lengths is a coin flip weighted by whatever state the instance landed in; four boots make the underlying difference visible. I should have run the distribution before reporting a comparison at all.

**What this does not change:**

- The **crash fix is real**: TP8 boots through memory profiling with zero memory access faults, selecting `..._vs_silu_1tg_32x256`, reproduced across every boot in this study (four more, on top of the earlier ones).
- The **throughput advantage is real and stable**: +13.1 % / +23.9 % / +31.2 % at N=64/256/512 versus Triton.
- **Short-prompt correctness is unaffected** — position 1 of the probe passed in 15 of 15 sweeps across both arms.

**So the honest summary is a trade-off, not a win:** `610de6deb` buys roughly 31 % throughput at N=512 and costs roughly 15 percentage points of long-context tool-calling reliability on this hardware. Which side that favours depends on the workload — for batch throughput on short-to-medium prompts it looks clearly worth it; for a long-context agentic workload it does not.

I would rather hand you this than the 36/36. If it is useful I can extend to eight boots per arm to tighten the interval, or run the same study against the `novs` candidate so all three are on one scale — though I would expect `novs` to sit far below both, since its failure mode was qualitatively different (invented function names, mangled tags, repetition) rather than the occasional miss both of these show.

One question in case you have a view: the failures cluster at 27k and 55k in *both* arms, and those are also the lengths where I measured the worst run-to-run divergence (four distinct answers from five identical requests at 27k). If the fMoE kernel choice modulates something that is already marginal there rather than causing it outright, the right comparison might be against a batch-invariant build rather than against Triton. I have not been able to get `VLLM_BATCH_INVARIANT=1` to cover the ROCm sparse-MLA path yet.


### stefanskiasan · 2026-08-28

**Found it: the correctness gap was the CSV's bucket coverage, not the kernel. Extending the tuned rows from one bucket to four brings `610de6deb` to parity with Triton — at the same +31 % throughput. Numbers below.**

Your CSV carries a single tuned row, `token=64`. GLM-5.3-Flash also dispatches at token 128, 256, 512, 1024 and 16384; those miss the lookup and take `using 1stage default`. The failures I reported clustered at 27k and 55k prompt tokens — exactly where the larger buckets appear.

I copied your winning row (`..._vs_silu_1tg_32x256`, `block_m=32`, `ksplit=0`, err 0.0 %) verbatim to token 128, 256 and 512, changing nothing but the token field, and re-ran the same four-boot distribution study:

| | correct | sweeps |
|---|---:|---:|
| `610de6deb`, 1 bucket (as shipped) | 33/42 = **78.6 %** | 7 |
| `610de6deb`, 4 buckets | **45/48 = 93.8 %** | 8 |
| Triton fMoE | 45/48 = **93.8 %** | 8 |

**Exact parity with Triton, and `610de6deb` is still +13.1 % / +23.9 % / +31.2 % faster at N=64/256/512.** Zero memory access faults across all eight boots. So the trade-off I described in my previous comment does not exist once the buckets are covered — I withdraw that framing.

Two caveats, stated plainly:

1. **I hand-wrote those three rows rather than tuning them.** Your row is presumably the measured optimum for `token=64`; whether the same kernel and `block_m` are optimal at 512 is unknown to me. The correctness result says it is at least *sound* there, and throughput did not regress, but a real tuning pass might pick something better. I tried to run `gemm_moe_tune.py` for those buckets and could not get it to complete — it spins at ~600 % CPU with no compiler running and no output, for over 50 minutes, and produces no tuned file. If there is an invocation I am missing, I would happily run the proper tuning and send you the result; my call was `--untune_file <csv> --tune_file <csv> --all` against a 3-row untuned file in your format.

2. **The residual 6 % is my benchmark, not the model.** Forcing the call removes it entirely:

```
tool_choice=auto       4/6, 5/6
tool_choice=required   6/6, 6/6
```

The `auto` misses are the model responding "Notiz erhalten – die Protokollzeile ist in Ihrer Nachricht mehrfach…" — commenting on the fact that my filler is the same sentence repeated 3,600 times, instead of answering. That is reasonable behaviour on a pathological prompt, and it means my probe was measuring prompt quality as much as kernel quality at the long lengths. Worth knowing if you are reading my earlier numbers.

**Suggestion for the PR:** ship tuned rows for token 64, 128, 256 and 512 rather than 64 alone, and ideally 1024 and 16384 too — those still fall back here. If you can tune them properly on your side, that is clearly better than my copied rows; if it helps, the dispatch keys I see in the logs are `('gfx950', 256, <token>, 4096, 256, 288, 8, 'ActivationType.Silu', 'torch.bfloat16', 'torch.float8_e4m3fn', 'torch.float8_e4m3fn', 'QuantType.per_1x128', True, False)`.

Happy to re-run the distribution study against whatever CSV you produce.

