# [Issue #567] [RFC]: Add random anchor for p-eagle first position

source: https://github.com/vllm-project/speculators/issues/567
state: closed | updated: 2026-07-02T14:14:01Z
labels: RFC

## 正文

### Motivation.

Peagle uses COD sampling, which predicts the next token for every possible starting token in a sample. Then also predicts the token after that for some percent of the tokens (e.g. 70%). And then predicts the 3rd token for 70% of the selected 70%, etc.

So our attention mask shape is: $(\text{sequence len} * 2.73)^2$, where $2.73 = \sum_{n=0}^4{0.7^n}$ and 4 is number of speculative tokens. What we're proposing is using `num_anchors` as starting points for peagle training because a good chunk of the original sequence length will have loss mask 0. That would give us attention masks of size: $(\text{num anchors} \times 2.73) \times (\text{num anchors} \times 1.73 + \text{sequence len})$ This would be smaller and potentially helps us train with longer sequence length.

### Proposed Change.

Add the `max_anchors` parameter to the P-Eagle config that caps the number of COD chain starting points. When set, `generate_cod_sample_indices` randomly selects `max_anchors` positions from the loss_mask=1 indices at depth 0 instead of using all positions. The attention mask construction reuses the existing
  `select_anchors` method to identify these starting points, then builds an asymmetric mask where queries are the COD-sampled tokens $(\text{max anchors} × 2.73)$ and keys/values include the full original sequence plus the deeper COD tokens $(\text{max anchors} × 1.73 + \text{sequence len})$. This shrinks the attention mask from
 $(\text{sequence len} × 2.73)^2$ to $(\text{num anchors} \times 2.73) \times (\text{num anchors} \times 1.73 + \text{sequence len})$, enabling training with longer sequence lengths under the same memory budget.

### Any Other Things.

_No response_

## 评论 (8)

### orestis-z · 2026-06-05

Thanks for the RFC. Here is my proposal:

1. Reuse the D-Flash Pattern: Adapt D-Flash's existing max_anchors and select_anchors logic (`dflash/utils.py`, `dflash/config.py`) for the depth-0 subsampling to keep the codebase DRY.

2. Asymmetric Mask via Verifier KV: Your proposed mask shape includes `+ seq_len` in the KV dimension. This is a _larger architectural shift_ than just subsampling depth-0, but it’s the right way to achieve that mask shape efficiently. To avoid heavy draft-model forward passes for the unselected tokens, we should mirror D-Flash's cross-attention setup:
    - KV Strategy: Sampled draft tokens act as Queries, while the full sequence's verifier hidden states (projected via the draft model's linear layers) supply the Keys/Values.
    - Depth > 0 Attention: Deeper-depth queries should attend to the full original sequence, not just their anchor chain. The memory footprint is already paid for by the verifier KV, and the richer context is necessary to maintain high acceptance rates.

What are your thoughts?


### shanjiaz · 2026-06-07

@orestis-z Thanks for looking into this! I think the plan would probably work and you're right this is going to require more than just subsampling depth-0 but I'm hesitant to convert p-eagle to just dflash+COD sampling. Did some experiments, looks like for qwen3-8b at least, we can train up to 7 draft tokens without hitting out of memory issue. Maybe we experiment with more aggressive drop samling rate? What do you think?

### orestis-z · 2026-06-08

@shanjiaz That makes total sense. I understand that this would essentially convert peagle to dflash+COD sampling.
I think an ablation study on drop sampling rates is a great idea.

Alternatively, we could also experiment with a symmetric `max_anchors` approach which would preserve the self-attention mechanism. The tradeoff here would be that we would have to sample `max_anchors` from a contiguous block (rather than randomly across the whole document, which would destroy local context).

If you agree, I believe both avenues could be worth exploring. I can start with your suggestion (reduced drop sampling rates).

What do you think?

### shanjiaz · 2026-06-08

@orestis-z I agree. I think a contiguous block of `max_anchors` make sense! Since we're already limiting based on loss mask, this should be relatively straightforward. Let me know how it goes!

### orestis-z · 2026-06-09

Ran an ablation on the two approaches discussed above. Setup: Qwen3-8B, 2000-sample subset, 1 epoch, A100 80GB.

**VRAM profiling** (single-batch memory measurement with random inputs):

| Config | seq_len=4096 | seq_len=8192 |
|--------|-------------|-------------|
| Baseline (no cap) | 48.6 GB | OOM |
| max_anchors=256, window=1024 | 13.8 GB | 13.8 GB |
| max_anchors=512, window=2048 | 13.8 GB | 13.8 GB |
| max_anchors=1024, window=4096 | 16.8 GB | 16.8 GB |

`max_anchors` makes VRAM independent of sequence length — baseline OOMs at 8K, all capped configs fit comfortably.

**Training ablation** (validation metrics):

| Config | Val Loss | Full Acc | Depth 0 | Depth 1 | Depth 2 | Depths 4-7 avg |
|--------|----------|----------|---------|---------|---------|----------------|
| Baseline (drop=0.7) | 4.578 | 0.212 | 0.425 | 0.193 | 0.124 | 0.073 |
| anchors=512, window=2048, drop=0.7 | 4.779 | 0.191 | 0.378 | 0.174 | 0.106 | 0.071 |
| drop=0.3 | **4.467** | **0.230** | **0.434** | 0.135 | 0.109 | **0.076** |
| anchors=512, window=2048, drop=0.3 | 4.625 | 0.215 | 0.408 | 0.120 | 0.097 | 0.069 |

### orestis-z · 2026-06-22

## Ablation Results: Drop Rate + Symmetric Windowed Attention at Scale

Experimental results from two rounds of ablation on Qwen3-8B with 6x H100 80GB.

**Drafter architecture**: PEagleDraftModel — 1 transformer layer (hidden=4096, intermediate=12288, 32 attn heads / 8 KV heads), 3 auxiliary verifier hidden state inputs (layers [2, 18, 33]), 8 draft depths, full 151K vocab, learnable embeddings.

---

### 1. Drop Rate Optimization

We screened four `down_sample_ratio` values at pilot scale (10K samples, 1 epoch, `seq_len=4096`), then validated the winner at 5x data and 2x epochs.

![Drop rate ablation](https://raw.githubusercontent.com/orestis-z/speculators/631817ef9ae6c797cf6267db64b41a3dd01fb50c/docs/ablation/section1_drop_rate.png)

**Pilot findings** (top row): Lower drop rates monotonically improve loss and d0, but **d1 degrades sharply** (20.5% → 14.9%). This is the COD sparsity trap — at `drop=0.15`, only 15% of positions survive to depth 1, starving the model of training signal at deeper depths. The 2-depth EAT ($1 + d_0 + d_0 \times d_1$) peaks at `drop=0.50` (1.552) and `drop=0.30` (1.545), while `drop=0.15`'s d1 collapse drags it to last (1.537).

**Scale validation** (bottom row): At 50K samples / 2 epochs, `drop=0.50` achieves **3.1% lower val_loss** (3.413 vs 3.520) and **6.0% higher full_acc** (33.4% vs 31.5%). The depth tradeoff persists — `drop=0.70` retains a 1–2pp edge on d1–d4 — but `drop=0.50` wins on 2-depth EAT as well (1.808 vs 1.802), since the higher d0 absorbs the d1 gap.

**Conclusion**: `drop=0.50` is Pareto-optimal for this 1-layer drafter. The optimal ratio is architecture-dependent — a larger drafter with more capacity may benefit from higher ratios that provide denser signal at deeper depths.

---

### 2. Long-Context Windowed Attention

We tested whether extending to 8K with `max_anchors=512` + `max_context_window=2048` improves draft quality over the equivalent 4K configuration (both at `drop=0.50`, 50K samples, 2 epochs).

![Window penalty](https://raw.githubusercontent.com/orestis-z/speculators/631817ef9ae6c797cf6267db64b41a3dd01fb50c/docs/ablation/section2_window.png)

The windowed 8K config underperforms the 4K baseline with **2.7% higher val_loss** (3.505 vs 3.413) and **uniform degradation across all depths**. The largest penalty is at $d_0$ (−2.4pp), propagating through $d_1$– $d_4$ before tapering at the floor.

**Root cause**: While this comparison is slightly confounded (changing sequence length, data packing, and windowing simultaneously), the uniform degradation strongly points to an information bottleneck. `max_context_window=2048` restricts the draft head to seeing only 25% of the 8K sequence. Because the verifier's hidden states encode full-sequence context, the draft head's symmetric attention window cannot recover those long-range dependencies — creating a verifier-drafter alignment mismatch that degrades predictions even at the root depth.

**Conclusion**: Symmetric windowed attention is not viable for long-context P-EAGLE. If long-context training is pursued, an **asymmetric approach** (draft queries attend to the full verifier KV) would be necessary to avoid context blindness.

---

### Recommendations

- **Use `down_sample_ratio=0.50`** as the default for P-EAGLE training with this drafter architecture.
- **Abandon symmetric windowing** for long-context — pursue asymmetric cross-attention instead.
- **Truncate draft tree depth to ~5** — depths 5–7 converge at 7–9% across all 7 configurations tested (4 pilot + 3 macro), regardless of drop rate, sequence length, or training scale. This represents a hard representational ceiling for the 1-layer drafter. Eliminating d5–d7 would reduce draft-step latency by ~30% with <2% EAT loss.

### orestis-z · 2026-06-23

`0.70` is likely the correct default for multi-layer drafters used in research, but `0.50` is the sweet spot for lightweight 1-layer setups.

 Original Peagle paper used 4 layers and a drop rate of `0.8`.

### orestis-z · 2026-06-29

## Random Anchor Subsampling: 8K Without OOM

The previous 8K ablation showed a quality regression, but it changed three variables at once. We ran a set of fast 10K-sample / 1-epoch pilot runs to isolate the variables.

**TL;DR**: The 8K degradation was entirely caused by the symmetric window's context blindness. By combining `max_anchors=1024` (random tree subsampling) with standard full causal attention, we can natively fit 8K in VRAM without OOMing and without degrading $d_0$ quality. Streaming is not required for 8K.

Here is the breakdown of the data.

> **Note**: `val_loss` and `full_acc` are omitted below as `max_anchors` changes the loss denominator, making them incomparable across configs. $d_0$ accuracy is the clean metric, as depth 0 is always the full sequence.

---

### 1. Isolating `max_anchors` at 4K (`drop=0.50`)

First, we tested if capping anchors degrades quality at 4K.

| Config | d0 | d1 | d2 | d3 | d4 | d5 | d6 | d7 |
|---|---|---|---|---|---|---|---|---|
| Control (no cap) | 54.5% | 25.5% | 14.2% | 10.6% | 8.9% | 8.2% | 7.7% | 7.4% |
| 1024 anchors | 57.6% | 21.9% | 11.3% | 8.3% | 6.6% | 6.2% | 5.9% | 5.3% |
| 512 anchors | 57.9% | 18.3% | 9.3% | 7.4% | 6.8% | 5.4% | 7.8% | 0.0% |
| 256 anchors | 57.9% | 14.0% | 8.6% | 5.6% | 3.3% | 0.0% | 0.0% | 0.0% |

![max_anchors ablation](https://raw.githubusercontent.com/vllm-project/speculators/90ce78fae036df2ee6fe435d890a539f2a3fa0a2/docs/ablation/phase1_max_anchors_ablation.png)

**Finding**: `max_anchors` actually **improves** $d_0$ (+3.1pp). 1024 is the sweet spot; going down to 512 or 256 hits a deep-tree sparsity trap where $d_5$– $d_7$ collapse to zero.

---

### 2. Scaling to 8K (Standard Attention, `anchors=1024`, `drop=0.50`)

Next, we moved to 8K using standard full causal attention (no window, no streaming). Because 1024 anchors shrink the query dimension so aggressively, the dense $O(N^2)$ attention matrix physically fits in 80GB VRAM at 8K.

- **4K Baseline** ($d_0$): 57.6%
- **8K Run** ($d_0$): 59.2%

**Finding**: Context blindness is cured. The model actually **improves** at $d_0$ because it can leverage longer context without being artificially cut off by a symmetric window.

---

### 3. Optimizing the 8K Baseline (`drop` and `max_depth`)

Because 1024 anchors sample a sparser fraction of an 8K sequence, $d_1$– $d_3$ accuracies dipped slightly compared to 4K. We ran two quick ablations to optimize the tree:

- **Drop rate**: Boosting from `drop=0.50` to `drop=0.70` fully recovered the $d_1$ dip (18.3% → 20.8%) with no cost to $d_0$. Because the tree is capped at 1024, the drafter has the capacity for a denser signal.
- **Truncation**: Truncating training to `max_depth=5` yielded identical $d_0$– $d_4$ accuracy to depth 8. Depths 6–7 are dead weight for a 1-layer drafter.

---

### Separate Ablation: StreamingLLM & The 32K Wall

Since we had the FlexAttention streaming infrastructure ready, we also tested it to see if it's worth merging for future scale (16K/32K contexts).

| seq_len | Attention Type | d0 | d1 | Failure Mode |
|---|---|---|---|---|
| 8K | Standard | 59.2% | 17.4% | — |
| 8K | Streaming (sink=256, window=2048) | 59.4% | 18.3% | — |
| 32K | Standard | — | — | OOM |
| 32K | Streaming (sink=256, window=2048) | — | — | OOM |

![8K streaming comparison](https://raw.githubusercontent.com/vllm-project/speculators/90ce78fae036df2ee6fe435d890a539f2a3fa0a2/docs/ablation/phase2_8k_streaming.png)

**Streaming works perfectly**: It carries zero penalty to $d_0$ at 8K and successfully protects the system prompt.

**The 32K Plot Twist**: At 32K, both configurations OOM. The crash isn't the attention matrix — it's the **vocab projection**. For a 32K sequence and the 151K Qwen vocab, the logits tensor alone is massive: `32K × 151K × 2 bytes ≈ 9.4 GiB` per batch item, blowing up the VRAM during loss calculation.

---

### Experiment Setup

All runs: 10K samples, 1 epoch, batch size 1, lr 1e-4, KL loss, single GPU (H100 80GB).

| Param | Value |
|---|---|
| Verifier | Qwen/Qwen3-8B |
| Draft layers | 1 |
| Aux hidden state layers | [2, 18, 33] |
| `num_depths` | 8 (unless noted) |
| `down_sample_ratio` | 0.50 (unless noted) |
| `down_sample_ratio_min` | 0.20 |
| `draft_vocab_size` | 151936 |
| `mask_token_id` | 151665 |

---

### Related PRs

- #687 — Random anchor subsampling (`max_anchors`, standalone)
- #683 — StreamingLLM attention for P-EAGLE
- #590 — Superseded contiguous window approach


