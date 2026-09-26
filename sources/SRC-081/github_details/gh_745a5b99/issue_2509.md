# [Issue #2509] [Feature Request] QAT support: training-aware quantization for llm-compressor

source: https://github.com/vllm-project/llm-compressor/issues/2509
state: closed | updated: 2026-07-25T18:00:28Z
labels: enhancement, stale

## 正文

> **Note:** This issue serves as the design document for QAT support in llm-compressor. The goal is to align on approach before implementation begins. Feedback from maintainers is welcome before any code is written.

## Motivation

LLM Compressor currently supports PTQ via `oneshot()`, which recovers accuracy well for most schemes. However, for aggressive quantization targets (INT4 weights, INT8 activations, NVFP4) or small/sensitive models, PTQ accuracy
degradation can be significant. QAT — training the model with simulated quantization in the forward pass — is the standard solution.This issue proposes adding the training support in a minimal, well-designed form focused specifically on QAT. Here I propose two complementary approaches targeting different use cases.

---

## Part 1: `train()` API (SFT + QAT)

### Overview

A new `train()` entrypoint that mirrors `oneshot()` but wraps HuggingFace Trainer with fake quantization injected via the existing `QuantizationModifier`. llm-compressor owns only the fake-quant injection and finalization — everything
else (distributed training, FSDP, data loading, checkpointing) is delegated to Trainer.

### Proposed API
```python
from llmcompressor import train
from llmcompressor.modifiers.quantization import QuantizationModifier

recipe = QuantizationModifier(
    targets="Linear",
    scheme="W8A8",
    ignore=["lm_head"],
)

train(
    model="meta-llama/Llama-3.2-1B-Instruct",
    dataset="open_platypus",
    recipe=recipe,
    output_dir="Llama-3.2-1B-W8A8-QAT",
    num_train_epochs=1,
    learning_rate=2e-5,
    max_seq_length=512,
)
```

Output is saved in the same compressed-tensors format as `oneshot()`, directly loadable in vLLM.

### How it works

1. Model loaded in full precision (BF16/FP16)
2. `QuantizationModifier.initialize()` inserts fake quantization ops into the
   forward pass via `torch.ao.quantization.FakeQuantize`
3. HuggingFace Trainer runs the training loop; gradients flow through
   straight-through estimator (STE) past the quantization ops
4. After training, `QuantizationModifier.finalize()` converts fake quant ops
   to real compressed-tensors quantization
5. Model saved with `save_pretrained()` in compressed-tensors format

### `train()` vs `oneshot()`

| | `oneshot()` | `train()` |
|---|---|---|
| Forward passes | Calibration only (no grad) | Full training loop |
| Dataset size | ~512 calibration samples | Full training dataset |
| Modifier lifecycle | initialize → calibrate → finalize | initialize → train N epochs → finalize |
| Output format | PTQ compressed checkpoint | QAT compressed checkpoint |
| Accuracy recovery | Good for most schemes | Better for aggressive quant / small models |

### Implementation plan

- New `src/llmcompressor/entrypoints/train.py` mirroring `oneshot.py` structure
- Reuse `SessionManagerMixIn` already in `src/llmcompressor/transformers/finetune/`
- `QuantizationModifier` gains a `qat_mode: bool = False` flag switching from
  PTQ calibration to fake-quant insertion on `initialize()`
- Fake quantization via `torch.ao.quantization.FakeQuantize` (no new dependencies)
- ~200 lines of new code; reuses all existing infrastructure

### Scope boundary

- SFT-based QAT only — not pretraining from scratch
- No custom training loop — delegate entirely to HuggingFace Trainer
- No RL training loops — see Part 2

---

## Part 2: verl Integration (RL + QAT)

### Overview

verl is a distributed RL training framework used for RLHF, PPO, and reasoning model training. Integrating llm-compressor's quantization recipe lifecycle into verl's training loop enables QAT in large-scale RL settings — particularly useful for post-RLHF quantization where PTQ accuracy loss is most pronounced on instruction-following and reasoning tasks.

### Proposed API
```python
# verl training config with llm-compressor QAT recipe
from llmcompressor.modifiers.quantization import QuantizationModifier

trainer = RayPPOTrainer(
    ...
    compression_recipe=QuantizationModifier(
        targets="Linear",
        scheme="W8A8",
        ignore=["lm_head"],
    ),
)

trainer.fit()  # QAT runs inside verl's PPO/GRPO loop
```

### How it works

1. llm-compressor exposes a `CompressionSession` lifecycle hook interface
2. verl calls `initialize()` at training start to inject fake quant ops
3. verl's PPO/GRPO loop runs normally — fake quant is transparent to the
   RL objective
4. verl calls `finalize()` at training end to convert to real quantization
5. Checkpoint saved in compressed-tensors format

### Implementation plan

- llm-compressor exposes a standalone `QATLifecycleHook` interface that
  verl can call at `on_train_begin` / `on_train_end`
- verl adds optional `compression_recipe` argument to `RayPPOTrainer`
- Integration layer is thin — verl owns all distributed execution

### Scope boundary

- May need to require coordination with verl maintainers
- Higher complexity and longer timeline than Part 1
- Best implemented after Part 1 is proven

---

## Comparison

| | Part 1: `train()` | Part 2: verl |
|---|---|---|
| Use case | SFT + QAT | RL training + QAT |
| Complexity | Low (~200 lines) | High (cross-repo) |
| Dependencies | HuggingFace Trainer | verl + Ray |
| Timeline | Weeks | Months |
| Target user | General quantization | Large-scale RL workflows |

**Recommended sequencing:** Start with Part 1 as the minimal viable QAT path.
Part 2 follows once the core QAT infrastructure is proven and stable.

---

## Prior Art

- SparseML  (suggested by @kylesayrs)
- NVIDIA ModelOpt QAT — similar approach using `torch.ao.quantization`
- HuggingFace `optimum` QAT — wraps Trainer with fake quant hooks
- llm-compressor `trl_mixin` — existing `SessionManagerMixIn` integration
  with SFTTrainer, which Part 1 builds directly on top of

---

## Open Questions for Maintainers 
1. Should `train()` live in `llmcompressor.entrypoints.train` or reuse `oneshot` with a `mode="qat"` parameter?
2. Is `SessionManagerMixIn` the right integration point, or should we build a dedicated `QATTrainer` subclass?
3. Are there plans to bring back `DistillationModifier` that would affect. this design?
4. For Part 2, is there an existing relationship with verl maintainers, or would this be a cold outreach?

Happy to start implementing Part 1 once the design direction is confirmed.@kylesayrs 

## 评论 (0)
