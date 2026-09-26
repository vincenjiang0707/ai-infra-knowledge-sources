# [Issue #3035] [BUG] AWQ calibration silently keeps only the last batch for variable-length inputs (starves MoE experts)

source: https://github.com/ModelCloud/GPTQModel/issues/3035
state: closed | updated: 2026-08-31T17:14:13Z
labels: 

## 正文

### Describe the bug

`AWQProcessor._layer_input_features()` silently discards all but the most recent calibration batch whenever cached per-module activations have variable sequence lengths.

The collapse logic concatenates cached batches only when every tensor shares the same trailing shape:

- equal shapes → `torch.cat(tensors, dim=0)` — all batches contribute;
- variable lengths (e.g. `[1, 423, H]` + `[1, 36, H]`) → `features[name] = tensors[-1]` — **only the last batch survives**, with no warning and no accounting.

Variable-length batches are the normal case for chat/instruction calibration corpora prepared without padding or packing, so in practice the AWQ scale search (per-channel `x_mean` and the ratio/loss evaluation) runs on a single calibration sample per module while the log still reports the full `nsamples`.

### Impact

For dense models this quietly weakens calibration. For fine-grained MoE models it is much worse: each routed expert only ever sees the tokens routed to it, so collapsing to one batch starves most experts entirely.

Real-world numbers from a 48-layer / 512-expert / top-10 MoE (Qwen3.8-Flash-Next) quantized with a 320-sample, 202,750-token variable-length corpus:

- before: every expert projection calibrated from the final batch only (a few hundred tokens for the whole layer);
- after aggregating all batches: `raw_tokens=202,750` per layer root, with per-expert retained-token accounting — and the resulting checkpoint's per-expert audit changed materially.

### Where

`gptqmodel/looper/awq_processor.py`, `_layer_input_features()` — the `else` branch keeping `tensors[-1]`, and the matching choice documented in `_concat_batch_metadata()`.

### Proposed fix

Since sequence-sensitive replay (attention masks / position ids) genuinely cannot span ragged batches, a safe fix is an **opt-in, model-declared aggregation policy** for pointwise modules (MLP/expert projections): pack ragged captures into deterministic bounded token rows (`[1, retained, hidden]`) so every batch contributes, keep legacy behavior for everything else, and record per-module `raw_tokens` / `retained_tokens` / `mode` stats so the remaining latest-batch fallback is at least visible.

PR with this implementation plus regression tests to follow shortly.


## 评论 (1)

### Qubitium · 2026-08-31

@Leonccaa Thanks you for the well-rounded report and PR fix. Checking it right now. Need some changes but the bug is real and bug fix is almost there. 
