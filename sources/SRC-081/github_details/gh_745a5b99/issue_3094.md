# [Issue #3094] Small Model REAP Ablation Metrics

source: https://github.com/vllm-project/llm-compressor/issues/3094
state: open | updated: 2026-08-25T20:02:29Z
labels: documentation, RFC, keep-open

## 正文

# REAP Baseline Benchmarking - MoE Models Across Sizes and Architectures

Baseline: [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash) (bf16, 47L, 64 routed experts, top-4) and [moonshotai/Moonlight-16B-A3B-Instruct](https://huggingface.co/moonshotai/Moonlight-16B-A3B-Instruct) (bf16, 27L, 64 routed experts, top-6)

Hardware: 1xH100
Serving: vLLM, TP=1, max-model-len=4096 (lm-eval `--model vllm`; offline `LLM.generate` for throughput). `out tok/s` is whole-generation (prefill+decode) wall-clock from a single batched `generate` (128 prompts x 256 tokens, `ignore_eos`), n=1 
Recipe: `REAPPruningModifier(sparsity=0.25 / 0.50)`, prune-only (no quantization stage), sequential pipeline, `moe_calibrate_all_experts=False`, bf16, saved with `save_compressed=True`

## Summary

- I've found that REAP-25 is essentially free lunch around the board on GLM-4.7-Flash: 98-100% quality recovery on all tasks, +20-22% offline generation throughput, 27% smaller weights.
- Safe sparsity appears to be contingent on expert redundancy, not necessarily model size: at equal 64-expert counts, GLM-4.7-Flash retains 92.7% gsm8k at 50% sparsity vs Moonlight-16B's 19.5%. (128-expert Qwen3-30B-A3B retains 99.8% per [`examples/reap_expert_pruning/README.md`](https://github.com/vllm-project/llm-compressor/blob/main/examples/reap_expert_pruning/qwen38_example.py)
- Calibration dataset holds more weight in pruning: perfectblend vs ultrachat moves gsm8k recovery +17.0pp (512 samples) / +14.6pp (1024 samples); doubling samples adds only +1.4-3.7pp (percentage points) (2x2 below).
- Degradation is task-asymmetric: generative reasoning (gsm8k) collapses first; loglikelihood tasks (hellaswag, arc) hold >= 75% everywhere.

## GLM-4.7-Flash (gsm8k strict / arc_challenge acc_norm / hellaswag acc_norm)

| Variant | gsm8k | arc_c | hellaswag | Avg recovery | out tok/s | weights |
|---|---|---|---|---|---|---|
| Baseline (64e) | 0.8355 | 0.5751 | 0.8023 | - | 5495 | 55.9 GiB |
| REAP-25 UC (48e) | 0.8279 | 0.5751 | 0.7931 | **0.9931** | 6704 (+22.0%) | 42.9 GiB |
| REAP-25 PB (48e) | 0.8218 | 0.5538 | 0.7862 | 0.9755 | 6600 (+20.1%) | 42.9 GiB |
| REAP-50 UC (32e) | 0.5914 | 0.5282 | 0.7393 | 0.8492 | 8096 (+47.3%) | 30.0 GiB |
| REAP-50 PB (32e) | 0.7748 | 0.4437 | 0.6341 | 0.8298 | 8271 (+50.5%) | 30.0 GiB |

## Moonlight-16B-A3B-Instruct (UC calibration)

| Variant | gsm8k | arc_c | hellaswag | Avg recovery | out tok/s | weights |
|---|---|---|---|---|---|---|
| Baseline (64e) | 0.7498 | 0.5828 | 0.7882 | - | 10516 | 29.8 GiB |
| REAP-25 UC (48e) | 0.6308 | 0.5555 | 0.7854 | 0.9303 | 11618 (+10.5%) | 23.1 GiB |
| REAP-50 UC (32e) | 0.1463 | 0.4386 | 0.7413 | 0.6294 | 13819 (+31.4%) | 16.4 GiB |

Consistent with `examples/reap_expert_pruning/README.md` for this model (79.8% / 17.0% gsm8k recovery at 25%/50%).

## Calibration: dataset vs sample count (GLM, REAP-50, gsm8k strict)

| | 512 samples | 1024 samples | count effect |
|---|---|---|---|
| ultrachat_200k | 0.5914 | 0.6285 | +3.7pp |
| open-perfectblend | 0.7612 | 0.7748 | +1.4pp |
| **dataset effect** | **+17.0pp** | **+14.6pp** | |

Dataset choice also trades task types: PB preserves reasoning (gsm8k +15-17pp) but regresses arc/hellaswag by 8.4pp / 10.5pp vs UC at REAP-50. Match calibration data to the deployment target (PB for reasoning, per the RedHatAI cards).

## Cross-architecture gsm8k recovery

| | GLM-4.7-Flash (64e) | Moonlight-16B (64e) | Qwen3-30B-A3B (128e, README) |
|---|---|---|---|
| REAP-25 | 99.1% | 84.2% | 98.9% |
| REAP-50 | 92.7% (PB) | 19.5% | 99.8% |

## Recipes

[gist here](https://gist.github.com/soyr-redhat/287a37158f4f5dbef56e7642dfab7e4a)


## 评论 (1)

### soyr-redhat · 2026-08-25

# Reasoning evals: MATH-500 + GPQA Diamond (CoT, zeroshot)

Follow-up pass on the same checkpoints. Tasks: `minerva_math500` (math_verify metric reported; exact_match is extraction-limited) and `gpqa_diamond_cot_zeroshot` (flexible-extract reported; strict-match is format-limited for these models).

Setup notes:
- GPQA ran on a mirror task pointing at `nmayorga7/gpqa_diamond` (the official `Idavidrein/gpqa` is gated; identical 198-question diamond content and schema).
- `--gen_kwargs max_gen_toks=4096` is required for reasoning tasks on these models: lm-eval's 256-token generation default truncates CoT and produced garbage scores (GPQA 0.11 for the GLM baseline before the fix; 0.3939 after).
- `max_model_len=8192`, otherwise identical harness (vLLM backend, batch auto, TP=1).

## GLM-4.7-Flash

| Variant | GPQA (flex) | recovery | MATH-500 (verify) | recovery |
|---|---|---|---|---|
| Baseline (64e) | 0.3939 | - | 0.7360 | - |
| REAP-25 UC (48e) | 0.3384 | 85.9% | 0.6380 | 86.7% |
| REAP-25 PB (48e) | 0.3333 | 84.6% | 0.6920 | **94.0%** |
| REAP-50 UC (32e) | 0.1111 | 28.2% | 0.4340 | 59.0% |
| REAP-50 PB (32e) | 0.1465 | 37.2% | 0.5660 | **76.9%** |

## Moonlight-16B-A3B-Instruct (UC)

| Variant | MATH-500 (verify) | recovery |
|---|---|---|
| Baseline (64e) | 0.4940 | - |
| REAP-25 UC (48e) | 0.1840 | 37.2% |
| REAP-50 UC (32e) | 0.0500 | 10.1% |

GPQA omitted for Moonlight: the baseline scores 0.2020 (below the 25% random floor), so the task carries no signal for this model family; REAP-25/50 "recovering" to 110%/90% of baseline confirms it is noise here.

## Takeaways

1. **Recovery is difficulty-dependent.** On GLM at REAP-25, recovery slopes from 99-100% (hellaswag/arc) -> 99% (gsm8k) -> 87-94% (MATH-500) -> 85% (GPQA). "REAP-25 is a free lunch" holds for standard workloads; frontier-difficulty reasoning is where pruning cost shows first.
2. **PB-for-reasoning replicates on a second task family.** At REAP-25, MATH-500 recovery is 94.0% (PB) vs 86.7% (UC); at REAP-50, 76.9% vs 59.0%. Same direction as gsm8k (+15-17pp), strengthening the calibration-dataset finding.
3. **GPQA is the most sensitive task run so far**: at REAP-50, GLM drops to 28-37% recovery regardless of calibration - an order of magnitude worse than loglikelihood tasks at the same sparsity.
4. Moonlight math degradation tracks its gsm8k fragility (37% / 10% at 25%/50%), reinforcing that 64-expert DeepSeek-arch redundancy is low compared to GLM-4.7's 64 experts.

