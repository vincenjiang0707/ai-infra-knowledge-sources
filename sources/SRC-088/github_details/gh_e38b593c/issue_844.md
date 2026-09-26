# [Issue #844] [RFC]: Investigate whether HF-native MTP support can simplify our MTP finetune + stitch pathway

source: https://github.com/vllm-project/speculators/issues/844
state: open | updated: 2026-09-01T12:36:26Z
labels: good first issue, RFC

## 正文

## Motivation

HuggingFace just merged native Multi-Token Prediction (MTP) support into `transformers`
([PR #46229](https://github.com/huggingface/transformers/pull/46229)). 

It adds an in-library MTP layer (`MtpLayer` / `MtpLayerStack`), lets a model declare MTP through its config
(`num_mtp_layers`), automatically finds and loads MTP weights from a checkpoint, and provides
both an inference path and a training path.

Today our MTP finetuning is built from three custom pieces that we maintain ourselves, and
each one grows every time a new model ships with native MTP:

1. **Convert / extract** (`src/speculators/convert/mtp/converter.py`) — pulls the MTP weights
   out of the checkpoint, renames every weight through hand-written lookup tables, and packs
   MoE expert weights together.
2. **Finetune** (`src/speculators/models/mtp/core.py`, `.../model_definitions.py`) — we
   re-implement the MTP layer once per model family (`qwen3`, `qwen3_next`, `qwen3_5`,
   `qwen3_5_moe`), and run our own training loop with FastMTP per-step loss weighting.
3. **Stitch** (`scripts/stitch_mtp.py`) — the exact reverse of step 1: rename every weight
   back, unpack the MoE experts, and merge the finetuned weights into the original checkpoint
   so vLLM can serve it. This is our most fragile piece — any mismatch with step 1 silently
   corrupts weights.

Now that HuggingFace defines the MTP layer for us, we may be able to delete some of this. The
biggest potential win is removing the **stitch** step entirely: if we can load the native
weights, finetune them, and save them back in the same native format, there is nothing to
rename or merge back. That is worth checking before we add the next model family to the
current pathway.

This RFC is a request to investigate and report back, it is not a
proposal to migrate yet. The goal is a clear recommendation.

## Proposed Change

Run a short investigation (read HuggingFace's merged code, then finetune one Qwen MTP model
through a HuggingFace-native path and compare token-acceptance against our current pathway).
Write up the answers and recommend one of three directions:

- **Adopt fully** — HuggingFace's layer works for our models, round-trips weights correctly,
  and supports our loss weighting. We delete the per-model layer code, the rename tables, and
  the stitch script.
- **Adopt partially** — use HuggingFace's layer (delete our per-model subclasses) but keep our
  own training loop and/or stitch step where HuggingFace falls short.
- **Not yet** — too early (unreleased, missing model coverage, or a training-quality gap).
  Record what would need to change for us to revisit.

The investigation should answer these questions, grouped by the pathway stage each affects.

**The MTP layer itself**
- Does HuggingFace's `MtpLayer` behave the same as ours — two inputs (verifier hidden states
  plus ground-truth token embeddings), separate norms, concatenate, project down to the hidden
  size, run a decoder layer, and feed each step's output into the next step?
- Which model families does HuggingFace's layer cover today? Does it handle the mixed
  linear/full-attention models we support (`qwen3_next`, `qwen3_5_moe`), including picking the
  correct attention layer index?

**Training quality (highest risk)**
- Does HuggingFace support per-step loss weighting, or only a single overall loss coefficient
  (`mtp_loss_coef`)? Our acceptance rate depends on FastMTP exponential-decay step weights
  (roughly `[0.51, 0.31, 0.18]`). If HuggingFace only offers one coefficient, using its
  trainer as-is would likely lower quality unless we can plug our weighting in.
- Can we keep our online-training setup, where hidden states are streamed from a live vLLM
  server during training, or does HuggingFace's path assume a full local forward pass?

**Weight loading and saving (this is what could kill the stitch step)**
- What weight layout does HuggingFace save? Does it match the original native layout that vLLM
  already reads, so a saved checkpoint serves without any stitching?
- If so, can we delete the rename tables and `stitch_mtp.py` outright — or does HuggingFace
  introduce its own conversion map we'd end up maintaining instead?
- Does HuggingFace handle MoE expert packing for us, removing our pack/unpack code?

**Coverage and compatibility (possible blockers)**
- HuggingFace's PR states DeepSeek v4 is **not** supported yet (its layer naming differs). We
  need to confirm which of our target models HuggingFace's layer actually covers, and whether
  gaps would force us to keep the current pathway for some models.
- Which released `transformers` version includes this? It is merged, but we need a released
  version, and adopting it raises our minimum `transformers` requirement.
- Does a checkpoint saved through the HuggingFace path still serve on vLLM with
  `{"method":"mtp","num_speculative_tokens":N}` exactly as today?

## Any Other Things

- **Scope.** In scope: reading the merged HuggingFace code and a throwaway experiment on one
  Qwen model to check acceptance parity. Out of scope: HuggingFace's own inference/generation
  path (we deploy on vLLM, not HuggingFace `generate`) and any actual migration, this RFC
  produces a recommendation, not a code change.
- **Deliverable.** A short findings write-up answering the questions above, one
  acceptance-rate comparison (HuggingFace-native finetune vs. our current pathway), and a
  recommendation (adopt fully / partially / not yet) with the concrete list of files we would
  delete or keep.

### References
- HuggingFace PR: https://github.com/huggingface/transformers/pull/46229
- Our MTP docs: `docs/user_guide/algorithms/mtp.md`,
  `docs/user_guide/tutorials/train_mtp_online.md`
- Converter: `src/speculators/convert/mtp/converter.py`
- Model: `src/speculators/models/mtp/core.py`, `.../model_definitions.py`
- Stitch: `scripts/stitch_mtp.py`
- FastMTP (our training recipe): https://arxiv.org/abs/2509.18362


## 评论 (4)

### rahul-tuli · 2026-07-26

> Hi @rahul-tuli, I'd like to work on this if it's still available.
> 
> I'd start with a small Qwen model and compare the HF-native path with the current flow, mainly checking whether we can remove stitching without breaking weight round-tripping or hurting token acceptance, and whether the FastMTP loss weights can be kept.
> 
> Could you assign me the issue if that sounds right?

Sounds good, this issue has been assigned to you!

### fus3r · 2026-07-26

Thks for assigning it! I’ll get started with the small Qwen comparison and I'll report back with my initial findings

### fus3r · 2026-07-26

Quick update: I checked this against Transformers 5.14.1.

`MtpLayer` itself looks reusable. After mapping the weights, it gives exactly the same outputs as the current Speculators layer for Qwen3, Qwen3-Next, Qwen3.5, and Qwen3.5-MoE.

The full HF path is blocked for Qwen at the moment. Qwen3.5 doesn't expose the config fields `get_mtp_config()` expects, and none of its 15 native `mtp.*` keys map to the released `MtpModel` layout. `save_pretrained()` doesn't write the native layout back either. The training forward also fails with labels and has no per-step FastMTP weights. With one physical MTP layer it produces one draft depth, while Speculators trains three by reusing that layer.

So I can't run a real acceptance comparison between the released HF path and the current one without patching HF first. Would you rather I test the narrower partial-adoption option (HF `MtpLayer` inside the current training and stitch flow), or write this up as "not yet" with the upstream changes needed to revisit it?

huggingface/transformers#45638 helps with the dense Qwen3.5 config, but it's still open and explicitly leaves training out of scope.


### rahul-tuli · 2026-09-01

I think for now "not yet" feels like the right way to go about this, we will make updates ones we have proper upstream support. Thanks for the investigation @fus3r really appreciate it
