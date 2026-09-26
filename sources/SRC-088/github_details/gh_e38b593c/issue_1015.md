# [Issue #1015] [RFC]: Add a staged layer-selection pathway for drafter training

source: https://github.com/vllm-project/speculators/issues/1015
state: open | updated: 2026-08-23T08:52:15Z
labels: RFC

## 正文

### Motivation

Choosing *which* target hidden-state layers to feed a drafter is a decision that
today is effectively a guess. In our Gemma-4-31B sweep the aux hidden-state layer
id (or set of ids) had a meaningful effect on acceptance length — the best single
layer beat the worst by a clear margin, and deep layers tended to beat shallow
ones — yet we have no principled, cheap procedure for finding a good selection.
We don't yet have enough evidence to claim how this ranks against other training
decisions in general, but it is clearly a knob worth choosing deliberately rather
than by default. Doing a full-data training run per candidate to find out does not
scale: an exhaustive layer search at full data cost is prohibitive.

<img width="1080" height="690" alt="Image" src="https://github.com/user-attachments/assets/99a9e46f-b93a-4d5a-b7d6-0c9aec117929" />

*Acceptance length as a function of the aux hidden-state layer id, at both data
scales. The choice of layer moves acceptance length substantially, and the shape
of the curve is the same at small and large data — deep layers win at both.*

The key empirical observation motivating this RFC: **a drafter's performance
under a small amount of training data is highly correlated with its performance
under a large amount of data.** If cheap runs rank candidates the same way
expensive runs do, we can prune the search space cheaply and only spend
full-data compute on the finalists.

We measured this directly on Gemma-4-31B (`google/gemma-4-31B-it`), DFlash
drafter, 1 epoch on ShareGPT, evaluated by drafts-weighted mean acceptance
length across 9 held-out subsets, comparing **n=4096** (small) vs **n=65536**
(16× larger) training samples per config.

**Single aux layer, sweep of layers 0,4,…,56 (n=15 configs):**

| Metric | Value |
|---|---|
| Spearman ρ (rank corr, 4096 vs 65536) | **0.914** (p=1.9e-06) |
| Kendall τ | **0.790** (p=4.9e-06) |
| Top-1 preserved across scales | 1 of 1 (layer 56 at both) |
| Top-2 preserved across scales | 2 of 2 (52, 56) |
| Top-3 preserved across scales | 3 of 3 (48, 52, 56) |

<img width="1020" height="780" alt="Image" src="https://github.com/user-attachments/assets/3f10253b-1651-4a2e-8e5a-bc7d3c82b05b" />

*Each point is one single-layer selection; x = acceptance length trained on 4096
samples, y = trained on 65536 samples (16× more data). The cheap-run score
reliably predicts the expensive-run score.*

**Five random aux layers, configs sampled by depth category (n=12 configs):**

| Metric | Value |
|---|---|
| Spearman ρ | **0.916** (p=2.8e-05) |
| Kendall τ | **0.758** (p=2.4e-04) |
| Top-1 preserved across scales | 0 of 1 (#-1 and #-2 swap order) |
| Top-2 preserved across scales | 2 of 2 (same 2 configs) |
| Top-3 preserved across scales | 2 of 3 |

<img width="1020" height="780" alt="Image" src="https://github.com/user-attachments/assets/c8c581c8-e8b4-4158-b5f5-f8a74ac50d07" />

*Same relationship holds for five-layer selections: small-data acceptance length tracks large-data acceptance length.*

The practical takeaway matters more than the aggregate correlation: **the top
*set* is preserved even when exact order within it is not.** For single layers,
the top-3 by small data are exactly the top-3 by large data (order included). For
five-layer configs, the top-2 by small data are exactly the top-2 by large data
as a set, but the #-1 and #-2 swap places — so small data does **not** reliably
pick the single winner there; it reliably picks a small shortlist that contains
it. This is precisely why the funnel carries a top-k (not top-1) from Stage 1
into Stage 2 to confirm, rather than trusting the cheap run's #-1 outright — while
still spending ~16× less per Stage 1 run.

### Proposed Change.

### Proposed Change

Add a **staged (funnel) layer-selection pathway** to speculators that turns
layer selection into an explicit, cheap-to-expensive search instead of a guess.
Three stages, each narrowing the candidate set while increasing the data spent
per candidate:

1. **Stage 1 — broad search, small data.** Train many candidate layer
   selections on a small sample budget (e.g. ~4k samples, 1 epoch). Rank by
   acceptance length. Cheap enough to cover a wide search.
2. **Stage 2 — confirm, medium/large data.** Re-train only the top-k candidates
   from Stage 1 on a larger sample budget (e.g. ~64k). This filters out the
   small handful of cases where small-data ranking jitters, at a fraction of the
   cost of running everything at this scale.
3. **Stage 3 — final run, full data.** Train the single winning selection on the
   full dataset with production hyperparameters.

<img width="960" height="561" alt="Image" src="https://github.com/user-attachments/assets/c46c5451-fa12-47db-9f67-f38a73b0ff5a" />


Concretely, this would add to speculators:

- A **selection-strategy config** describing the candidate space for Stage 1
  (e.g. `single-layer-sweep`, `random-k`, `depth-biased` with late/uniform/early
  weightings — the sampling scheme we used here) plus `k` per stage and the
  sample budget per stage.
- An **orchestration entry point** (script/CLI, e.g. `scripts/select_layers.py`)
  that runs the three stages: fan out Stage 1 trainings, rank by benchmarked
  acceptance length, carry the top-k into Stage 2, then emit the recommended
  selection (and optionally kick off Stage 3).
- A small **results/leaderboard artifact** (CSV/JSON) recording each candidate's
  selection, stage, sample budget, and acceptance length, so the funnel is
  auditable and re-rankable.
- Reuse of the existing `--target-layer-ids` training path and the benchmark
  harness — this is orchestration on top of what already exists, not a new
  training mode.

#### Enabling infrastructure: runtime layer swap (depends on #996)

Stage 1 runs *many* candidate layer selections back-to-back. Today each candidate
requires relaunching the vLLM extraction server with a different
`--target-layer-ids`, paying full model-load + startup cost per trial — which
dominates wall-clock when each training run is itself cheap (small data). To make
the sequential cheap experiments practical, we need to change *which* target
hidden layers are captured **at runtime, without restarting the engine**.

The draft PR **[vllm-project/speculators#996](https://github.com/vllm-project/speculators/pull/996)**
(*"dynamic hidden-states layer swap for extract_hidden_states"*) provides exactly
this. It adds an opt-in vLLM plugin that swaps the captured aux-layer *set* live
over HTTP (`POST /aux_hidden_state_layers`) with no recompile and no
`--enforce-eager`: it replaces the `torch.compile`-frozen `layer_idx in
aux_layers` membership test with a masked accumulate over `N` fixed buffers,
where the selection is a one-hot mask in a registered buffer, so a swap is an
in-place `mask.copy_(...)` read live by both the compiled graph and captured CUDA
graphs. This is the mechanism a Stage 1 orchestrator would drive: launch the
extraction server once, then iterate candidates by POSTing new layer sets between
trials.

One constraint shapes the search design: **#996 fixes the layer *count* at launch
(only the set is swappable).** So a single extraction server can sweep candidates
of a fixed size `k` (e.g. all single-layer, or all 5-layer configs); sweeping a
different `k` requires a fresh launch. This fits the funnel naturally — pick `k`,
sweep sets of that size cheaply, confirm, commit — and is called out as a
dependency/assumption for Stage 1 below.

### Any Other Things.

#### Part of a broader hyper-parameter optimization suite

Layer selection is the first concrete instance of a general pattern, and we
propose building it so the machinery generalizes. The same cheap-predicts-
expensive funnel — plus a shared candidate-config schema, staged orchestrator,
benchmark harness, and leaderboard artifact — likely applies to many knobs in speculators training.

#### Search within a fixed number of hidden states

One design rule falls out of the data: **rank selections only against others with
the same number of hidden states — do not pool across different counts.** The
correlation figures above each hold *within* a fixed count, but the absolute
acceptance-length scale shifts with the count, so a cross-count comparison is not
apples-to-apples.

<img width="1110" height="840" alt="Image" src="https://github.com/user-attachments/assets/ea74b8ef-fbd2-4758-9fbc-694ac225f39c" />

*Both populations plotted together with separate fits. The five-layer cloud sits
well above the single-layer cloud: at the same small-data acceptance length, a
five-layer selection reaches ~0.2 higher acceptance length at large data. The
extra hidden states add capacity, which shifts the whole curve — so a five-layer
config and a single-layer config with identical small-data scores are not
equivalent. The small-predicts-large property we rely on is a within-count statement.*

This is why the funnel picks a number of hidden states `k` and searches sets of
that size, and it dovetails with #996's fixed-count-per-launch constraint: a
single extraction server sweeps one `k`, exactly the unit the ranking is valid
over.

### Any Other Things

Evidence appendix (full per-config numbers) and caveats:

- **Data source.** Gemma-4-31B DFlash, ShareGPT, 1 epoch, drafts-weighted mean
  acceptance length over 9 subsets. Single-layer sweep = 15 configs complete;
  five-layer sweep = 12 of 15 planned configs complete at drafting time (will be
  refreshed to 15 before posting).
- **Coverage caveats.** The single-layer sweep uses stride 4 and lands only on
  sliding-window (local) layers — it does not probe the 10 global-attention
  layers. Each (config, sample-size) point is a single run (1 epoch, one seed),
  so run-to-run variance is unmeasured; this is exactly why Stage 2 confirmation
  exists in the proposal rather than trusting Stage 1 outright.
- **What "small data predicts large data" does and does not claim.** It reliably
  preserves the *top* of the ranking (what the funnel needs). It does not
  perfectly preserve mid-pack ordering — closely-scoring candidates reshuffle
  between scales — which is expected and handled by carrying a top-k (not top-1)
  into Stage 2.
- **Generality.** Demonstrated on DFlash / Gemma here; the same funnel should
  apply to EAGLE3 / P-EAGLE and other targets. 
- **Dependency on #996 and its limits.** The efficient Stage 1 loop assumes the
  runtime layer-swap plugin from
  [#996](https://github.com/vllm-project/speculators/pull/996). Its constraints
  carry into the search: (a) the aux-layer *count* is fixed per server launch, so
  each server sweeps one fixed `k`; (b) live swap without `--enforce-eager` covers
  models that capture via `EagleModelMixin._maybe_add_hidden_state` (Qwen2/Qwen3,
  Llama, generic dense/MoE) — models that inline the membership test (e.g.
  `deepseek_v2`, `qwen3_next`) still need `--enforce-eager`, or a modified version of #996; (c) the extraction
  connector stores no layer-set metadata, so the orchestrator must record its own
  `{trial → layer set}` mapping. If #996 does not land, Stage 1 still works by
  relaunching the server per candidate — just more slowly.

NB: I have more data for Qwen3-8B and Laguna-XS-2.1 with 1-layer and 2-layer that I will format and post below soon.

## 评论 (1)

### zihanlin-ai · 2026-08-22

A data point on the "cheap procedure" part. Context: DSpark-style drafter for a 92B MoE verifier (46 decoder layers) on Ascend NPU.

**Instead of re-extracting per candidate:** dump *all* layers once for a small slice, then select layers at training time by name.

- A 1% slice of the training prompts (14.3k rows, 13.4M tokens) was dumped with every decoder layer's mean hidden state plus the final pre-norm hidden, BF16, stored per row as a safetensors file with named keys `layer_000_mean … layer_045_mean`, `merged_pre_rms`, `token_ids`. ~224 MB/row, 3.2 TB total — a one-off, and the only extraction needed for the whole layer sweep.
- The training-side loader takes a feature map (which named keys → aux channels) and does selective per-key reads (`safe_open` + `get_tensor`), so a 3-tap configuration reads 4 keys out of 48 and the sweep over tap sets is purely a config change. No vLLM restart, no re-dump, no count-fixed-at-launch constraint (the difference from the runtime-swap approach in #996, which keeps the layer *count* fixed).

**Sweep on our target (same data/seed, 5 epochs, accept_len; seed band ≈0.14):**

| taps | accept_len |
|---|---|
| last layer only (45) | 2.25 |
| 44+45 | 2.14 |
| 43+44+45 | 2.44 |
| final pre-norm hidden only | 2.21 |
| 45 + final pre-norm | 2.18 |

Deep taps, three of them, ahead; "just take the final hidden" no better than a single deep layer; adding taps not monotone (44+45 < 45). Caveat: this axis also changes the projector input width / parameter count, so it is not a pure "which layer" comparison — a staged pathway should control for that (e.g. fixed total aux width).

Two suggestions for the RFC:

1. Make the all-layer dump a first-class artifact of stage 1 (even at 0.5–1%), with named layer keys rather than a positional `[seq, num_layers, hidden]` block, so later stages can add/remove taps without re-extracting. The 3.2 TB is the cost; it was still far cheaper than N full extractions.
2. Separate the ranking objective from the count: pick the *set* under a fixed aux width first, then sweep width, otherwise the sweep mostly measures projector capacity.

