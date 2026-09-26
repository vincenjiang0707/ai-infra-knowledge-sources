# [Issue #757] RFC: Ablation Study — Domino vs DSpark Performance Comparison

source: https://github.com/vllm-project/speculators/issues/757
state: open | updated: 2026-08-23T08:59:53Z
labels: RFC, training, dflash

## 正文

## Motivation

Both Domino (#685, [arXiv:2605.29707](https://arxiv.org/abs/2605.29707)) and DSpark add sequential/causal conditioning on top of the DFlash parallel draft backbone, but through fundamentally different mechanisms:

- **Domino**: GRU-based correction head producing additive logit deltas on suffix positions, with a dual-loss lambda curriculum that transitions from 100% backbone loss to 100% refined loss.
- **DSpark**: Low-rank factorized Markov logit-bias head (`W1 @ W2`, rank 256) + optional confidence head (per-position acceptance predictor trained with BCE).

Prior experiments have compared these methods, but never under identical conditions (same dataset, hyperparameters, verifier, and evaluation protocol). Weifan's DPace ablations (#736) and the v6 Domino experiments used different datasets and settings, making direct comparison unreliable. This RFC proposes a controlled ablation to resolve that.

Additionally, the v6 Domino experiments showed that the lambda curriculum improved the **backbone itself** by +9.1% MAL even when the GRU head was dropped at inference — meaning sequential conditioning during training can act as a regularizer that benefits the parallel backbone. Understanding whether DSpark's Markov head produces a similar backbone-strengthening effect is a key question.

**Inference support in vLLM:**
- **DSpark**: Fully supported in vLLM — `DSparkSpeculator` loads the Markov head and performs sequential left-to-right sampling with Markov bias at each step (`vllm/v1/worker/gpu/spec_decode/dspark/`).
- **Domino**: WIP/draft support in vLLM (vllm-project/vllm#48241), not yet merged. Pending testing with a training checkpoint.

**Note on parameter and compute overhead:** The Domino GRU head and DSpark Markov head add different amounts of parameters on top of the DFlash backbone. More importantly, they have different computational profiles: the GRU requires sequential state updates (inherently less parallelizable), while DSpark's factorized Markov bias is a single embedding lookup + matmul. Parameter counts and drafting latency will both be reported alongside quality metrics.

## Experimental Design

### Shared Configuration

```
--verifier-name-or-path  Qwen/Qwen3-8B
--num-layers             5
--target-layer-ids       1 9 17 25 34
--block-size             8
--max-anchors            3072
--draft-vocab-size       32000
--sliding-window         2048        # SWA default
--optimizer              muon        # Muon default
--lr 1e-4  --muon-lr 1e-3
--scheduler-type         cosine
--noise-std              0.0
--seed                   42
```

**Data:** 100K samples from Magpie+Ultrachat blend (same as the DPace ablations in #736 for direct comparability).

**Note on single seed:** All runs use seed 42. This means observed differences reflect point estimates, not statistically significant effects. Phase 2 (500K) provides a second data point at higher scale; multi-seed runs are deferred unless results are ambiguous.

### Phase 1: 100K Samples, 2 Epochs — Quick Signal

#### Core runs (must-do)

| Run | Type | Loss | Sequential Head | Inference | Key Extra Flags |
|-----|------|------|-----------------|-----------|-----------------| 
| A1 | **DFlash baseline** | CE | None | DFlash | — |
| A2 | **Domino** | CE | GRU | Domino (vllm-project/vllm#48241) | `--projector-type domino --domino-lambda-start 1.0 --domino-lambda-decay-ratio 1.0` |
| A3 | **DSpark (vanilla)** | CE | Low-rank Markov r=256 + confidence head | DSpark (Markov active) | `--speculator-type dspark --markov-head-type vanilla` |
| A4 | **DSpark (no confidence head)** | CE | Low-rank Markov r=256 only | DSpark (Markov active) | `--speculator-type dspark --no-enable-confidence-head` |
| A5 | **DSpark (confidence head only)** | CE | Confidence head only (no Markov) | DFlash | `--speculator-type dspark --markov-rank 0 --no-confidence-head-with-markov` |
| A6 | **DSpark as DFlash** | CE | Markov r=256 + confidence head (training only) | DFlash (Markov head dropped) | Same checkpoint as A3; eval as plain DFlash |

A5 isolates the confidence head's contribution without the Markov head (`--markov-rank 0`). If DSpark's gains are largely driven by the BCE-trained acceptance predictor rather than sequential logit corrections, A5 will show comparable quality to A3. The confidence head takes only `hidden_size` as input (no Markov embedding) when `--no-confidence-head-with-markov` is set.

A6 reuses A3's checkpoint but evaluates it as a plain DFlash model (ignoring the Markov head at inference). This gives a fair training-technique comparison: A1 vs A6 are both evaluated identically as DFlash, isolating the effect of Markov conditioning during training on the backbone itself. Meanwhile, A3 vs A6 isolates the Markov head's inference-time contribution.

**Lambda decay:** Domino uses a dual-loss curriculum `loss = (1-λ)*final_loss + λ*base_loss` where λ decays from 1→0. The current code uses absolute step counts (`--domino-lambda-decay-steps`), but for consistency across Phase 1 (100K) and Phase 2 (500K) we want ratio-based decay (like `--scheduler-warmup-ratio`). `--domino-lambda-decay-ratio 1.0` means λ reaches 0 at 100% of total training steps. **This requires a code change to the Domino branch** — the existing `lambda_base_decay_steps` will be supplemented with a `lambda_decay_ratio` option following the same pattern as `scheduler_warmup_ratio` in the trainer.

**Est.** ~20-25 hours on 8x H100 (2 GPUs for vLLM server, 6 for FSDP training). A6 reuses an existing checkpoint so adds no training time, only an extra eval pass.

#### Extension runs (lower priority, reference data exists at 1 epoch)

The DPace results in #736 already show DPace helps at 1 epoch on the same dataset (DFlash CE 2.485 -> DPace 2.617, DSpark CE 2.560 -> DPace 2.675). These runs confirm the effect at 2 epochs.

| Run | Type | Loss | Key Extra Flags |
|-----|------|------|-----------------| 
| A7 | DFlash + DPace | CE + DPace | `--per-position-loss-weight dpace --dpace-alpha 0.5` |
| A8 | DSpark + DPace | CE + DPace | `--speculator-type dspark --per-position-loss-weight dpace` |
| A9 | DSpark native | `{"ce":0.1,"tv":0.9}` | DSpark with its "native" compound loss |
| A10 | Domino native | KL (default) | `--projector-type domino --domino-lambda-start 1.0 --domino-lambda-decay-ratio 1.0 --loss-fn kl_div` |

A9 and A10 form a "best possible config" pair — each method with its empirically preferred loss — complementing the CE-controlled A1-A6 comparison.

#### Block size 16 follow-up

The Domino paper defaults to block_size=16. Larger blocks give the sequential heads (GRU / Markov) more positions to correct, which could disproportionately benefit Domino and DSpark over vanilla DFlash. After the core runs at block_size=8, re-run the top 2-3 methods at block_size=16 to measure the effect.

**Important:** If `--max-anchors` must be reduced for block_size=16 to fit in GPU memory, gradient accumulation steps must be adjusted to keep the effective token batch size (`max_anchors * block_size * grad_accum_steps`) identical to the A-series runs. Otherwise the comparison is confounded by different training dynamics, not just block size.

| Run | Type | Loss | Key Extra Flags |
|-----|------|------|-----------------| 
| B1 | DFlash baseline (bs=16) | CE | `--block-size 16` |
| B2 | Winner from A2-A4 (bs=16) | CE | `--block-size 16` + winner config |
| B3 | Runner-up from A2-A4 (bs=16) | CE | `--block-size 16` + runner-up config |

### Phase 2: 500K Samples, 5 Epochs — Confirmation

Run top 3-4 methods from Phase 1 at 500K scale with 5 epochs. `--domino-lambda-decay-ratio 1.0` scales automatically (ratio-based, no manual step adjustment needed).

### Evaluation Protocol

For each checkpoint:
1. Serve as speculative decoder via vLLM (using `DSparkSpeculator` for DSpark runs, `DFlashSpeculator` for DFlash runs, Domino inference path for A2)
2. Run `scripts/evaluate/evaluate.py` in **`sweep`** mode on all 9 `RedHatAI/speculator_benchmarks` subsets (sweep mode collects both acceptance rates and inference speed metrics)
3. Report per-subset and mean MAL (Mean Accepted Length)
4. Generate comparison plots via `scripts/evaluate/plot.py compare`

**Primary metric:** Mean MAL across all 9 subsets
**Tiebreaker:** Wall-clock output tokens/s — if two methods have similar MAL, the faster one wins. A +0.2 MAL gain that tanks ITL due to sequential head overhead (e.g., GRU state updates) is not a real improvement.
**Secondary metrics:**
- Inference speed: TTFT (time to first token), ITL (inter-token latency), output tokens/s — all collected by the `sweep` evaluation mode
- Drafting latency: per-draft-step latency (ms) to quantify the computational cost of each sequential head (GRU vs Markov vs none)
- Per-position acceptance rates
- Training-time EAL curves
- Training wall-clock time and peak GPU memory per run
- Parameter counts for each head configuration

## Open Questions for Discussion

### Q1: Loss function alignment

The core runs (A1-A6) all use CE for strict architectural isolation. Extension runs A9/A10 add a "best native config" comparison (compound CE+TV for DSpark, KL for Domino). Is this sufficient, or should we also cross the DPace dimension with native losses?

## References

- Domino paper: [arXiv:2605.29707](https://arxiv.org/abs/2605.29707)
- DPace paper: [arXiv:2605.18810](https://arxiv.org/abs/2605.18810)
- DFlare paper: [arXiv:2606.02091](https://arxiv.org/abs/2606.02091)
- Domino PRs: https://github.com/vllm-project/speculators/pull/773 + https://github.com/vllm-project/vllm/pull/48241
- DPace PR: #736


## 评论 (10)

### orestis-z · 2026-07-10

Blocking this until #711 is in

### orestis-z · 2026-07-21

## A1: DFlash Baseline — Eval Results

**Checkpoint**: [orestis-z/dflash-Qwen3-8B-ablation757-a1](https://huggingface.co/orestis-z/dflash-Qwen3-8B-ablation757-a1)
**Verifier**: Qwen/Qwen3-8B
**Data**: magpie + ultrachat 100k (seed 0)
**Epochs**: 2 (12,677 steps)

<details>
<summary>Training command</summary>

```
scripts/train.py --verifier-name-or-path Qwen/Qwen3-8B --speculator-type dflash \
    --data-path /data/fast/qwen3-8b-magpie-ultrachat-100k-seed0 \
    --vllm-endpoint http://localhost:8000/v1 \
    --save-path /data/fast/checkpoints/ablation_757/a1_dflash \
    --loss-fn ce --num-layers 5 --target-layer-ids 1 9 17 25 34 \
    --block-size 8 --max-anchors 3072 --draft-vocab-size 32000 \
    --sliding-window 2048 --optimizer muon --lr 1e-4 --muon-lr 1e-3 \
    --scheduler-type cosine --noise-std 0.0 --seed 42 --epochs 2 \
    --total-seq-len 8192 --on-missing generate --on-generate delete
```

Environment: 6x H100, world_size=6, speculators 0.7.0.dev109, vLLM 0.25.1, torch 2.11.0+cu130
</details>

### Acceptance Rates (speculator_benchmarks, throughput mode, max 200 requests/subset)

| Subset | MAL | Pos 0 | Pos 1 | Pos 2 | Pos 3 | Pos 4 | Pos 5 | Pos 6 |
|---|---|---|---|---|---|---|---|---|
| math_reasoning | **2.07** | 0.425 | 0.247 | 0.156 | 0.102 | 0.067 | 0.044 | 0.028 |
| HumanEval | 1.90 | 0.408 | 0.210 | 0.118 | 0.071 | 0.044 | 0.027 | 0.017 |
| question | 1.84 | 0.412 | 0.202 | 0.099 | 0.058 | 0.035 | 0.021 | 0.013 |
| writing | 1.83 | 0.404 | 0.191 | 0.105 | 0.060 | 0.035 | 0.022 | 0.013 |
| rag | 1.79 | 0.413 | 0.183 | 0.094 | 0.052 | 0.029 | 0.015 | 0.008 |
| qa | 1.78 | 0.401 | 0.180 | 0.092 | 0.052 | 0.030 | 0.016 | 0.009 |
| tool_call | 1.76 | 0.394 | 0.176 | 0.091 | 0.049 | 0.027 | 0.015 | 0.009 |
| translation | 1.68 | 0.383 | 0.158 | 0.076 | 0.035 | 0.018 | 0.009 | 0.004 |
| summarization | 1.62 | 0.372 | 0.137 | 0.062 | 0.029 | 0.013 | 0.006 | 0.003 |
| **Average** | **1.81** | **0.401** | **0.187** | **0.099** | **0.057** | **0.033** | **0.019** | **0.012** |

This is the DFlash baseline (parallel draft backbone, no Markov head, no confidence head). Other results (A2–A6) will follow once training completes.


### orestis-z · 2026-07-22

## A4: DSpark No-Confidence — Eval Results

**Checkpoint**: [orestis-z/dspark-Qwen3-8B-ablation757-a4](https://huggingface.co/orestis-z/dspark-Qwen3-8B-ablation757-a4)
**Verifier**: Qwen/Qwen3-8B
**Data**: magpie + ultrachat 100k (seed 0)
**Epochs**: 2 (12,700 steps)

<details>
<summary>Training command</summary>

```
scripts/train.py --verifier-name-or-path Qwen/Qwen3-8B --speculator-type dspark \
    --data-path /data/fast/qwen3-8b-magpie-ultrachat-100k-seed0 \
    --vllm-endpoint http://localhost:8000/v1 \
    --save-path /data/fast/checkpoints/ablation_757/a4_dspark_no_conf \
    --loss-fn ce --num-layers 5 --target-layer-ids 1 9 17 25 34 \
    --block-size 8 --max-anchors 3072 --draft-vocab-size 32000 \
    --sliding-window 2048 --optimizer muon --lr 1e-4 --muon-lr 1e-3 \
    --scheduler-type cosine --noise-std 0.0 --seed 42 --epochs 2 \
    --total-seq-len 8192 --markov-rank 256 --markov-head-type vanilla \
    --no-enable-confidence-head \
    --on-missing generate --on-generate delete \
    --logger trackio --num-workers 12 --draft-attn-impl sdpa \
    --run-name a4-dspark-no-confidence
```

Environment: 6x H100, world_size=6, speculators 0.7.0.dev116, vLLM 0.25.1, torch 2.11.0+cu130
</details>

<details>
<summary>Validation metrics (best checkpoint)</summary>

- **Loss**: 0.567
- **Accept length**: 3.91
- **Position accuracies**: 83.5% / 76.6% / 70.6% / 65.3% / 60.7% / 56.7% / 53.1% / 49.8%
</details>

### Acceptance Rates (speculator_benchmarks, throughput mode, max 200 requests/subset)

| Subset | MAL | Pos 0 | Pos 1 | Pos 2 | Pos 3 | Pos 4 | Pos 5 | Pos 6 |
|---|---|---|---|---|---|---|---|---|
| math_reasoning | **4.17** | 0.841 | 0.652 | 0.510 | 0.385 | 0.291 | 0.217 | 0.159 |
| HumanEval | **3.77** | 0.820 | 0.608 | 0.450 | 0.320 | 0.226 | 0.160 | 0.112 |
| question | **3.34** | 0.761 | 0.525 | 0.369 | 0.252 | 0.173 | 0.119 | 0.084 |
| writing | **3.30** | 0.758 | 0.518 | 0.360 | 0.246 | 0.167 | 0.115 | 0.080 |
| tool_call | **3.06** | 0.738 | 0.482 | 0.319 | 0.207 | 0.135 | 0.086 | 0.055 |
| qa | **3.01** | 0.712 | 0.466 | 0.307 | 0.202 | 0.134 | 0.088 | 0.061 |
| rag | **2.98** | 0.735 | 0.474 | 0.309 | 0.194 | 0.123 | 0.075 | 0.046 |
| translation | **2.63** | 0.679 | 0.411 | 0.247 | 0.134 | 0.076 | 0.044 | 0.027 |
| summarization | **2.55** | 0.682 | 0.388 | 0.223 | 0.119 | 0.068 | 0.038 | 0.024 |
| **Average** | **3.20** | **0.747** | **0.503** | **0.344** | **0.229** | **0.155** | **0.105** | **0.072** |

DSpark with Markov logit-bias head (rank 256, vanilla) but **no confidence head**. vs A1 DFlash baseline (avg MAL 1.81): **+77% improvement** in mean acceptance length.


### orestis-z · 2026-07-22

## A3: DSpark Vanilla — Eval Results

**Checkpoint**: [orestis-z/dspark-Qwen3-8B-ablation757-a3](https://huggingface.co/orestis-z/dspark-Qwen3-8B-ablation757-a3)
**Verifier**: Qwen/Qwen3-8B
**Data**: magpie + ultrachat 100k (seed 0)
**Epochs**: 2 (12,700 steps)

<details>
<summary>Training command</summary>

```
scripts/train.py --verifier-name-or-path Qwen/Qwen3-8B --speculator-type dspark \
    --data-path /data/fast/qwen3-8b-magpie-ultrachat-100k-seed0 \
    --vllm-endpoint http://localhost:8000/v1 \
    --save-path /data/fast/checkpoints/ablation_757/a3_dspark \
    --loss-fn ce --num-layers 5 --target-layer-ids 1 9 17 25 34 \
    --block-size 8 --max-anchors 3072 --draft-vocab-size 32000 \
    --sliding-window 2048 --optimizer muon --lr 1e-4 --muon-lr 1e-3 \
    --scheduler-type cosine --noise-std 0.0 --seed 42 --epochs 2 \
    --total-seq-len 8192 --markov-rank 256 --markov-head-type vanilla \
    --enable-confidence-head --confidence-head-with-markov \
    --on-missing generate --on-generate delete \
    --logger trackio --num-workers 12 --draft-attn-impl sdpa \
    --run-name a3-dspark-vanilla
```

Environment: 6x H100, world_size=6, speculators 0.7.0.dev116, vLLM 0.25.1, torch 2.11.0+cu130
</details>

<details>
<summary>Validation metrics (best checkpoint)</summary>

- **Loss**: 0.790
- **Accept length**: 3.94
- **Confidence loss**: 0.226, abs error: 0.169, pred mean: 0.601
- **Position accuracies**: 83.6% / 76.7% / 70.8% / 65.5% / 60.9% / 56.9% / 53.3% / 50.0%
</details>

### Acceptance Rates (speculator_benchmarks, throughput mode, max 200 requests/subset)

| Subset | MAL | Pos 0 | Pos 1 | Pos 2 | Pos 3 | Pos 4 | Pos 5 | Pos 6 |
|---|---|---|---|---|---|---|---|---|
| math_reasoning | **2.20** | 0.716 | 0.304 | 0.109 | 0.042 | 0.016 | 0.007 | 0.003 |
| HumanEval | **2.08** | 0.697 | 0.264 | 0.074 | 0.027 | 0.011 | 0.006 | 0.003 |
| writing | **1.95** | 0.637 | 0.225 | 0.060 | 0.020 | 0.007 | 0.003 | 0.001 |
| question | **1.95** | 0.640 | 0.223 | 0.059 | 0.020 | 0.007 | 0.002 | 0.001 |
| rag | **1.95** | 0.625 | 0.219 | 0.067 | 0.024 | 0.010 | 0.004 | 0.002 |
| tool_call | **1.94** | 0.620 | 0.216 | 0.063 | 0.023 | 0.009 | 0.004 | 0.002 |
| qa | **1.88** | 0.593 | 0.197 | 0.055 | 0.020 | 0.007 | 0.002 | 0.001 |
| summarization | **1.87** | 0.598 | 0.199 | 0.051 | 0.016 | 0.004 | 0.002 | 0.000 |
| translation | **1.84** | 0.584 | 0.177 | 0.051 | 0.017 | 0.007 | 0.003 | 0.001 |
| **Average** | **1.96** | **0.634** | **0.225** | **0.065** | **0.023** | **0.009** | **0.004** | **0.002** |

DSpark with Markov logit-bias head (rank 256, vanilla) **and** confidence head. +8% avg MAL vs A1 DFlash baseline (1.96 vs 1.81). Training validation metrics are nearly identical to A4 (accept_len 3.94 vs 3.91), but inference MAL is significantly lower (1.96 vs 3.20). Acceptance drops sharply beyond pos 0 compared to A4 (pos 1: 0.225 vs 0.503).


### orestis-z · 2026-07-22

## A6: DSpark-as-DFlash — Eval Results

**Checkpoint**: [orestis-z/dflash-Qwen3-8B-ablation757-a6](https://huggingface.co/orestis-z/dflash-Qwen3-8B-ablation757-a6)
**Verifier**: Qwen/Qwen3-8B
**Data**: magpie + ultrachat 100k (seed 0)
**Epochs**: 2 (12,700 steps) — trained as A3 DSpark, then stripped of Markov + confidence heads and served as DFlash

<details>
<summary>Training command (same as A3)</summary>

```
scripts/train.py --verifier-name-or-path Qwen/Qwen3-8B --speculator-type dspark \
    --data-path /data/fast/qwen3-8b-magpie-ultrachat-100k-seed0 \
    --vllm-endpoint http://localhost:8000/v1 \
    --save-path /data/fast/checkpoints/ablation_757/a3_dspark \
    --loss-fn ce --num-layers 5 --target-layer-ids 1 9 17 25 34 \
    --block-size 8 --max-anchors 3072 --draft-vocab-size 32000 \
    --sliding-window 2048 --optimizer muon --lr 1e-4 --muon-lr 1e-3 \
    --scheduler-type cosine --noise-std 0.0 --seed 42 --epochs 2 \
    --total-seq-len 8192 --markov-rank 256 --markov-head-type vanilla \
    --enable-confidence-head --confidence-head-with-markov \
    --on-missing generate --on-generate delete \
    --logger trackio --num-workers 12 --draft-attn-impl sdpa \
    --run-name a3-dspark-vanilla
```

Environment: 6x H100, world_size=6, speculators 0.7.0.dev116, vLLM 0.25.1, torch 2.11.0+cu130
</details>

<details>
<summary>Validation metrics (A3 best checkpoint, before stripping)</summary>

- **Loss**: 0.790
- **Accept length**: 3.94
- **Position accuracies**: 83.6% / 76.7% / 70.8% / 65.5% / 60.9% / 56.9% / 53.3% / 50.0%
- **Confidence loss**: 0.226
- **Confidence abs error**: 0.169
</details>

### Acceptance Rates (speculator_benchmarks, throughput mode, max 200 requests/subset)

| Subset | MAL | Pos 0 | Pos 1 | Pos 2 | Pos 3 | Pos 4 | Pos 5 | Pos 6 |
|---|---|---|---|---|---|---|---|---|
| math_reasoning | **2.20** | 0.715 | 0.301 | 0.109 | 0.042 | 0.017 | 0.008 | 0.004 |
| HumanEval | **2.07** | 0.697 | 0.261 | 0.073 | 0.026 | 0.010 | 0.004 | 0.002 |
| question | **1.96** | 0.641 | 0.225 | 0.062 | 0.020 | 0.007 | 0.003 | 0.001 |
| qa | **1.95** | 0.605 | 0.210 | 0.069 | 0.032 | 0.020 | 0.013 | 0.003 |
| writing | **1.95** | 0.638 | 0.222 | 0.060 | 0.020 | 0.007 | 0.003 | 0.001 |
| rag | **1.93** | 0.616 | 0.213 | 0.063 | 0.022 | 0.009 | 0.003 | 0.002 |
| tool_call | **1.92** | 0.613 | 0.209 | 0.061 | 0.021 | 0.007 | 0.003 | 0.001 |
| summarization | **1.89** | 0.611 | 0.205 | 0.054 | 0.016 | 0.004 | 0.001 | 0.000 |
| translation | **1.85** | 0.582 | 0.181 | 0.052 | 0.019 | 0.007 | 0.003 | 0.001 |
| **Average** | **1.97** | **0.636** | **0.225** | **0.067** | **0.024** | **0.010** | **0.005** | **0.002** |

A3 DSpark checkpoint with Markov + confidence head weights stripped, served as DFlash. vs A1 DFlash baseline (avg MAL 1.81): **+9% improvement** in mean acceptance length.

<details>
<summary>Required local vLLM patch (not yet upstream)</summary>

DFlash `sample_from_anchor` is not read from the speculators config. Two changes needed:

**1. `vllm/transformers_utils/configs/speculators/algos.py`** — pass `sample_from_anchor` into `dflash_config`:
```diff
     pre_trained_config["dflash_config"] = {
         "mask_token_id": config_dict["mask_token_id"],
         "target_layer_ids": [i - 1 for i in aux_layer_ids],
+        "sample_from_anchor": config_dict.get("sample_from_anchor", False),
     }
```

**2. `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`** — read from config instead of hardcoding `False`:
```diff
-        self.sample_from_anchor = False
+        dflash_cfg = getattr(self.draft_model_config.hf_config, "dflash_config", {}) or {}
+        self.sample_from_anchor = dflash_cfg.get("sample_from_anchor", False)
+        if self.sample_from_anchor:
+            self.num_query_per_req = self.num_speculative_steps
```
</details>


### orestis-z · 2026-07-22

## A5: DSpark Confidence-Only (served as DFlash) — Eval Results

**Checkpoint**: [orestis-z/dflash-Qwen3-8B-ablation757-a5](https://huggingface.co/orestis-z/dflash-Qwen3-8B-ablation757-a5)
**Verifier**: Qwen/Qwen3-8B
**Data**: magpie + ultrachat 100k (seed 0)
**Epochs**: 2 (12,700 steps)

<details>
<summary>Training command</summary>

```
scripts/train.py --verifier-name-or-path Qwen/Qwen3-8B --speculator-type dspark \
    --data-path /data/fast/qwen3-8b-magpie-ultrachat-100k-seed0 \
    --vllm-endpoint http://localhost:8000/v1 \
    --save-path /data/fast/checkpoints/ablation_757/a5_dspark_conf_only \
    --loss-fn ce --num-layers 5 --target-layer-ids 1 9 17 25 34 \
    --block-size 8 --max-anchors 3072 --draft-vocab-size 32000 \
    --sliding-window 2048 --optimizer muon --lr 1e-4 --muon-lr 1e-3 \
    --scheduler-type cosine --noise-std 0.0 --seed 42 --epochs 2 \
    --total-seq-len 8192 --markov-rank 0 \
    --enable-confidence-head --no-confidence-head-with-markov \
    --on-missing generate --on-generate delete \
    --logger trackio --num-workers 12 --draft-attn-impl sdpa \
    --run-name a5-dspark-confidence-only
```

Environment: 6x H100, world_size=6, speculators 0.7.0.dev116, vLLM 0.25.1, torch 2.11.0+cu130
</details>

<details>
<summary>Validation metrics (best checkpoint)</summary>

- **Loss**: 1.059
- **Accept length**: 3.48
- **Position accuracies**: 83.7% / 68.7% / 57.2% / 48.0% / 40.4% / 34.2% / 28.9% / 24.3%
- **Confidence loss**: 0.205
- **Confidence abs error**: 0.118
</details>

### Acceptance Rates (speculator_benchmarks, throughput mode, max 200 requests/subset)

| Subset | MAL | Pos 0 | Pos 1 | Pos 2 | Pos 3 | Pos 4 | Pos 5 | Pos 6 |
|---|---|---|---|---|---|---|---|---|
| math_reasoning | **3.34** | 0.834 | 0.554 | 0.362 | 0.237 | 0.157 | 0.101 | 0.062 |
| HumanEval | **3.10** | 0.817 | 0.523 | 0.320 | 0.192 | 0.116 | 0.068 | 0.038 |
| writing | **2.80** | 0.768 | 0.451 | 0.254 | 0.147 | 0.087 | 0.051 | 0.028 |
| question | **2.79** | 0.767 | 0.446 | 0.252 | 0.145 | 0.085 | 0.049 | 0.028 |
| rag | **2.69** | 0.742 | 0.421 | 0.232 | 0.133 | 0.081 | 0.046 | 0.025 |
| qa | **2.59** | 0.719 | 0.396 | 0.211 | 0.117 | 0.069 | 0.043 | 0.025 |
| tool_call | **2.59** | 0.741 | 0.407 | 0.210 | 0.111 | 0.060 | 0.033 | 0.016 |
| translation | **2.38** | 0.699 | 0.368 | 0.175 | 0.079 | 0.035 | 0.015 | 0.006 |
| summarization | **2.29** | 0.683 | 0.334 | 0.147 | 0.067 | 0.033 | 0.015 | 0.007 |
| **Average** | **2.73** | **0.752** | **0.433** | **0.240** | **0.136** | **0.080** | **0.047** | **0.026** |

Trained as DSpark with confidence head only (markov_rank=0, no Markov logit-bias head), Markov + confidence head weights stripped, served as DFlash. vs A1 DFlash baseline (avg MAL 1.81): **+51% improvement** in mean acceptance length.

<details>
<summary>Required local vLLM patch (not yet upstream)</summary>

DFlash `sample_from_anchor` is not read from the speculators config. Two changes needed:

**1. `vllm/transformers_utils/configs/speculators/algos.py`** — pass `sample_from_anchor` into `dflash_config`:
```diff
     pre_trained_config["dflash_config"] = {
         "mask_token_id": config_dict["mask_token_id"],
         "target_layer_ids": [i - 1 for i in aux_layer_ids],
+        "sample_from_anchor": config_dict.get("sample_from_anchor", False),
     }
```

**2. `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`** — read from config instead of hardcoding `False`:
```diff
-        self.sample_from_anchor = False
+        dflash_cfg = getattr(self.draft_model_config.hf_config, "dflash_config", {}) or {}
+        self.sample_from_anchor = dflash_cfg.get("sample_from_anchor", False)
+        if self.sample_from_anchor:
+            self.num_query_per_req = self.num_speculative_steps
```
</details>


### orestis-z · 2026-07-24

## A2: Domino (DFlash + GRU Causal Correction) — Eval Results

**Checkpoint**: [orestis-z/domino-Qwen3-8B-ablation757-a2](https://huggingface.co/orestis-z/domino-Qwen3-8B-ablation757-a2)
**Verifier**: Qwen/Qwen3-8B
**Data**: magpie + ultrachat 100k (seed 0)
**Epochs**: 2 (12,676 steps)

<details>
<summary>Training command</summary>

```
scripts/train.py --verifier-name-or-path Qwen/Qwen3-8B --speculator-type dflash \
    --data-path /data/fast/qwen3-8b-magpie-ultrachat-100k-seed0 \
    --vllm-endpoint http://localhost:8000/v1 \
    --save-path /data/fast/checkpoints/ablation_757/a2_domino \
    --loss-fn ce --num-layers 5 --target-layer-ids 1 9 17 25 34 \
    --block-size 8 --max-anchors 3072 --draft-vocab-size 32000 \
    --sliding-window 2048 --optimizer muon --lr 1e-4 --muon-lr 1e-3 \
    --scheduler-type cosine --noise-std 0.0 --seed 42 --epochs 2 \
    --total-seq-len 8192 \
    --projector-type domino \
    --domino-lambda-start 1.0 --domino-lambda-decay-ratio 1.0 \
    --on-missing generate --on-generate delete \
    --logger trackio --num-workers 0 --draft-attn-impl sdpa \
    --run-name a2-domino
```

Environment: 6x H100, world_size=6, speculators 0.7.0.dev130 (`v6-normalize-experiment`), vLLM 0.25.1, torch 2.11.0+cu130
</details>

<details>
<summary>Validation metrics (best checkpoint, epoch 1)</summary>

- **Loss**: 0.542 (base_loss: 0.914, final_loss: 0.542)
- **EAL**: 2.754
- **Position accuracies**: 82.8% / 75.6% / 70.8% / 67.0% / 63.8% / 61.0% / 58.5% / 56.2%
</details>

### Acceptance Rates (speculator_benchmarks, throughput mode, max 200 requests/subset)

| Subset | MAL | Pos 0 | Pos 1 | Pos 2 | Pos 3 | Pos 4 | Pos 5 | Pos 6 |
|---|---|---|---|---|---|---|---|---|
| math_reasoning | **3.91** | 0.829 | 0.626 | 0.471 | 0.357 | 0.269 | 0.203 | 0.151 |
| HumanEval | **3.57** | 0.804 | 0.583 | 0.417 | 0.295 | 0.211 | 0.149 | 0.106 |
| question | **3.17** | 0.750 | 0.501 | 0.337 | 0.231 | 0.160 | 0.110 | 0.077 |
| writing | **3.19** | 0.752 | 0.501 | 0.341 | 0.235 | 0.162 | 0.114 | 0.081 |
| tool_call | **2.88** | 0.727 | 0.461 | 0.287 | 0.181 | 0.113 | 0.072 | 0.045 |
| qa | **2.85** | 0.711 | 0.451 | 0.279 | 0.178 | 0.116 | 0.074 | 0.046 |
| rag | **2.82** | 0.719 | 0.448 | 0.276 | 0.171 | 0.104 | 0.065 | 0.041 |
| translation | **2.52** | 0.668 | 0.389 | 0.220 | 0.120 | 0.066 | 0.037 | 0.021 |
| summarization | **2.44** | 0.669 | 0.362 | 0.194 | 0.102 | 0.058 | 0.034 | 0.020 |
| **Average** | **3.04** | **0.737** | **0.480** | **0.314** | **0.208** | **0.140** | **0.095** | **0.065** |

Domino adds a GRU-based causal correction head on top of DFlash. During inference, a prefix GRU processes previously-drafted tokens to build causal state, then applies additive logit corrections to the parallel base drafts. vs A1 DFlash baseline (avg MAL 1.81): **+68% improvement** in mean acceptance length. vs A4 DSpark no-confidence (avg MAL 3.20): slightly lower (-5%), but Domino uses a different approach — a causal GRU correction head (25.2M params) instead of DSpark's parallel Markov logit-bias head (16.4M params).

<details>
<summary>Required local vLLM patch (not yet upstream)</summary>

Domino inference requires vLLM PR [#48241](https://github.com/vllm-project/vllm/pull/48241) (`orestis-z/vllm:domino-speculators-patches`). The PR adds:
- `DominoHead` class (GRU encoder + low-rank correction MLP) to `qwen3_dflash.py`
- Domino config field passthrough (`projector_type`, `gru_hidden_dim`, `emb_dim`, `shift_label`, `pure_draft_prefix_len`) in `algos.py`
- Domino draft generation dispatch (`_generate_domino_draft`, `_sample_domino_logits`) in `dflash/speculator.py`
</details>



### orestis-z · 2026-07-28

## A3b: DSpark Vanilla (detach fix) — Eval Results

**Checkpoint**: [orestis-z/dspark-Qwen3-8B-ablation757-a3b-v2](https://huggingface.co/orestis-z/dspark-Qwen3-8B-ablation757-a3b-v2)
**Verifier**: Qwen/Qwen3-8B
**Data**: magpie + ultrachat 100k (seed 0)
**Epochs**: 2 (12,700 steps)

Re-training of A3 with the confidence head detach fix (PR #848). The DSpark outputs are now detached before feeding into the confidence head, preventing gradient interference with the backbone.

<details>
<summary>Training command</summary>

```
scripts/train.py --verifier-name-or-path Qwen/Qwen3-8B --speculator-type dspark \
    --data-path /data/fast/qwen3-8b-magpie-ultrachat-100k-seed0 \
    --vllm-endpoint http://localhost:8000/v1 \
    --save-path /data/fast/checkpoints/ablation_757/a3b_v2_dspark_detach \
    --loss-fn ce --num-layers 5 --target-layer-ids 1 9 17 25 34 \
    --block-size 8 --max-anchors 3072 --draft-vocab-size 32000 \
    --sliding-window 2048 --optimizer muon --lr 1e-4 --muon-lr 1e-3 \
    --scheduler-type cosine --noise-std 0.0 --seed 42 --epochs 2 \
    --total-seq-len 8192 --markov-rank 256 --markov-head-type vanilla \
    --enable-confidence-head --confidence-head-with-markov \
    --on-missing generate --on-generate delete \
    --logger trackio --num-workers 2 --draft-attn-impl sdpa \
    --run-name a3b-v2-dspark-detach
```

Environment: 6x H100, world_size=6, speculators 0.7.0.dev129, vLLM 0.25.2, torch 2.11.0
</details>

<details>
<summary>Validation metrics (best checkpoint)</summary>

- **Loss**: 0.814
- **Accept length**: 3.91
- **Confidence loss**: 0.247, abs error: 0.201, pred mean: 0.600
- **Position accuracies**: 83.5% / 76.6% / 70.6% / 65.3% / 60.7% / 56.7% / 53.1% / 49.8%
</details>

### Acceptance Rates (speculator_benchmarks, throughput mode, max 200 requests/subset)

Evaluated on vLLM 0.25.2 (note: A1–A4 were evaluated on 0.25.1, so direct MAL comparison is not apples-to-apples — see note below).

| Subset | MAL | Pos 0 | Pos 1 | Pos 2 | Pos 3 | Pos 4 | Pos 5 | Pos 6 | Pos 7 |
|---|---|---|---|---|---|---|---|---|---|
| math_reasoning | **4.48** | 0.837 | 0.681 | 0.551 | 0.440 | 0.348 | 0.269 | 0.205 | 0.153 |
| HumanEval | **4.09** | 0.817 | 0.645 | 0.498 | 0.376 | 0.281 | 0.208 | 0.153 | 0.110 |
| writing | **3.54** | 0.765 | 0.554 | 0.400 | 0.286 | 0.206 | 0.149 | 0.108 | 0.077 |
| question | **3.51** | 0.757 | 0.552 | 0.395 | 0.284 | 0.203 | 0.144 | 0.103 | 0.072 |
| tool_call | **3.25** | 0.738 | 0.520 | 0.357 | 0.243 | 0.163 | 0.107 | 0.071 | 0.047 |
| qa | **3.23** | 0.721 | 0.504 | 0.347 | 0.242 | 0.167 | 0.116 | 0.081 | 0.054 |
| rag | **3.20** | 0.741 | 0.515 | 0.349 | 0.234 | 0.157 | 0.100 | 0.064 | 0.040 |
| translation | **2.94** | 0.694 | 0.468 | 0.307 | 0.191 | 0.122 | 0.077 | 0.049 | 0.030 |
| summarization | **2.73** | 0.685 | 0.427 | 0.265 | 0.158 | 0.093 | 0.055 | 0.033 | 0.017 |
| **Average** | **3.44** | **0.750** | **0.541** | **0.385** | **0.273** | **0.193** | **0.136** | **0.096** | **0.067** |

**A3b vs A4 (DSpark No-Confidence)**: Validation metrics are **identical** (accept_len 3.91, same position accuracies to full precision), confirming the detach fix correctly isolates the confidence head — backbone weights are equivalent to training without a confidence head. The inference MAL difference (3.44 vs A4's 3.20) is entirely from vLLM version differences (0.25.2 vs 0.25.1); A3b is consistently ~7% higher across all subsets.

**vs A1 baseline** (DFlash, avg MAL 1.81 on vLLM 0.25.1): A3b shows +90% avg MAL improvement, though part of this gap is attributable to the vLLM version difference. For a clean comparison, A1 should be re-evaluated on 0.25.2.

<details>
<summary>vLLM serving bug fix (dspark_bonus_anchor)</summary>

`vllm/transformers_utils/configs/speculators/algos.py` line 152 hardcoded `dspark_bonus_anchor = True` for all DSpark checkpoints. For checkpoints with `sample_from_anchor=True` (N-slot layout), this set `num_query_per_req=9` instead of 8, causing `_anchor_idx` to exceed `input_ids` buffer size (max anchor = 1023×9 = 9207 > 8192), triggering a CUDA index-out-of-bounds crash.

Fix:
```diff
- pre_trained_config["dspark_bonus_anchor"] = True
+ pre_trained_config["dspark_bonus_anchor"] = not config_dict.get(
+     "sample_from_anchor", False
+ )
```

This bug was introduced between vLLM 0.25.1 and 0.25.2 — A3's eval on 0.25.1 was unaffected because the field wasn't set at all (defaulting correctly to `False`).
</details>

### orestis-z · 2026-07-30

## Summary: Cross-version comparison (avg MAL, 9 subsets)

Re-evalauted on v0.25.1:

| Run | Type | v0.25.1 | v0.26.0 | Delta |
|---|---|---|---|---|
| A1 | DFlash baseline | 1.80 | 3.19 | +77% |
| A2 | Domino (GRU) | 3.54 | 3.54 | +0% |
| A3 | DSpark (Markov + conf) | 3.23 | 3.45 | +7% |
| A4 | DSpark (Markov, no conf) | 3.20 | 3.42 | +7% |
| A5 | DFlash + conf head only | 2.71 | 3.25 | +20% |
| A6 | A3 served as DFlash | 1.95 | 2.24 | +15% |
| A3b | DSpark (conf head detach) | — | 3.44 | — |

A2 evaluated with unmerged vLLM PR vllm-project/vllm#48241 applied to both versions. Results are identical across versions (weighted avg MAL 3.544 vs 3.536).

### Key findings

- **Domino is perfectly stable across vLLM versions** — A2 shows +0% between 0.25.1 and 0.26.0 (3.54 on both). The GRU correction head is not sensitive to vLLM internals.
- **DSpark is stable across vLLM versions** — A3/A4 show only +7% between 0.25.1 and 0.26.0. The Markov head's sequential sampling is less sensitive to vLLM internals.
- **DFlash has a large regression on v0.25.1** — A1 drops from 3.19 to 1.80 (pos_0 acceptance: 82% → 41%). Root cause is in vLLM's DFlash sampling path, not token count.
- **Confidence head detach (A3b ≈ A4)** — detaching gradients before the confidence head has no effect on DSpark Markov inference (3.44 vs 3.42).
- **Original A3 eval (MAL 1.96) was likely served as DFlash** — A3 (1.96) ≈ A6 (1.97), and DSpark crashes without patches on v0.25.1.

### zihanlin-ai · 2026-08-22

Data on the confidence-head question from a different setting.

Setup: DSpark-style drafter (3 draft layers, Markov rank 512, block 5, window 128) for a 92B MoE verifier on Ascend NPU, `confidence_head_alpha=1`, same data/seed across arms, 5 epochs, metric = validation expected accept_len. Seed band on this setup ≈0.14.

"Isolate the confidence head" split into two cuts, because they are different mechanisms:

- **detach** — `conf_feat.detach()`, so the head cannot change the drafter's gradient *direction*;
- **independent clipping** — the head's params are clipped against their own budget and excluded from the drafter's `clip_grad_norm_`, so the head cannot change the drafter's *step size*.

2×2 over those axes:

| | shared clip | independent clip |
|---|---|---|
| connected | 2.436 | 2.561 |
| detached | 2.540 | 2.814 |

Interaction ≈ +0.15; detach alone +0.10, clipping alone +0.12, both together +0.38. A CPU gradient check agrees with the table: the drafter's post-clip gradients are bitwise equal to the `alpha=0` run only with *both* cuts (shared clip norm 2.913 vs isolated 2.825 on the probe). A detach-only arm looks like a regression for exactly that reason — the head still shares the global clip budget.

Implications for #848 → #908:

1. If the intended semantics of the head is "read-only probe that does not touch the drafter's trajectory", `detach()` is necessary but not sufficient under a global `clip_grad_norm_`; #848 only did the first half, so A3b ≈ A3 does not settle whether isolation matters.
2. The effect is setup-dependent (≈0 on Qwen3-8B here, large on ours), which argues for a flag (`--confidence-head-detach` + independent clip) rather than a default either way, so the ablation can be run per model.

Early stopping in our runs used the validation loss including the confidence term and was not decomposed, so the table is "isolation vs not", not a claim about the best alpha.

