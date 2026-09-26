# [Issue #1156] Training a draft on a Mamba-backbone verifier fails: KeyError: 'embed_tokens.weight'

source: https://github.com/vllm-project/speculators/issues/1156
state: closed | updated: 2026-09-23T21:12:53Z
labels: 

## 正文

### What happened
Building a draft against `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16` fails at verifier-weight load with `KeyError: 'embed_tokens.weight'`. I reproduced it end-to-end with eagle3 and dflash on a recent `main` checkout. It is independent of `--draft-config`, since the load happens in the model base.

### Root cause
`SpeculatorModelBase._load_verifier_weights` (`src/speculators/model.py`) requests `embed_tokens.weight` and resolves it via `_resolve_key` / `_WEIGHT_ALIASES` (`src/speculators/utils/loading.py`). HF-format Mamba-backbone checkpoints name the input embedding `backbone.embeddings.weight`: NemotronH (verified on the published Nano, Super and Ultra checkpoints) and Mamba / Mamba2 / FalconMamba (per their transformers `modeling_*.py`). None of the current candidates (`embed_tokens.weight`, `tok_embeddings.weight`, `llm.embed.weight`) is a suffix of that key, so `_resolve_key` returns `None` and the subsequent lookup raises.

All algorithms on current `main` (eagle3, peagle, mtp, dflash, dflash2, dspark) load the verifier embedding through this method, so all are affected.

Llama-style hybrids (Bamba, Jamba, Zamba2) use `model.embed_tokens.weight` and are unaffected. Original `mamba_ssm`-format exports (`backbone.embedding.weight`, singular) are out of scope; this concerns HF/transformers-format checkpoints.

### Repro
    from speculators.utils.loading import _resolve_key
    _resolve_key("embed_tokens.weight", {"backbone.embeddings.weight": "x", "lm_head.weight": "x"})  # -> None

Code references: `main` @ `ad36840`. transformers 5.16.1.

### Context
The README lists Nemotron 3 Super/Ultra DFlash speculators, and their model cards document a `scripts/train.py --speculator-type dflash ...` recipe. Their verifiers also expose the embedding only as `backbone.embeddings.weight` (checked via the safetensors indices), and no released version of speculators resolves that key, so the recipe as written would hit this same error.

### Question
Is there an intended path for Mamba-backbone verifiers that I've missed (a flag, example or config override)? If not, I'd propose adding `backbone.embeddings.weight` to `_WEIGHT_ALIASES["embed_tokens.weight"]`, following #989, #719 and #1038. I have a PR ready (one alias plus resolver unit tests) and can open it if that approach works for you.


## 评论 (2)

### fynnsu · 2026-09-22

Hi @ra-srivid, yes it'd be great if you could open a pr similar to #989 to introduce the needed weight alias. I'm not sure exactly what approach was used to train the existing Nemotron 3 super/ultra drafters, but mostly likely the loading was just temporarily patched to support it and the fix never landed upstream. 

### ra-srivid · 2026-09-23

Thanks @fynnsu! Opened #1158 following the #989 pattern: it adds `backbone.embeddings.weight` to the `embed_tokens.weight` aliases, plus resolver tests covering the new key, confirming standard `model.embed_tokens.weight` checkpoints still resolve to the primary candidate, and checking that unrelated *_embeddings.weight tensors don't match. Happy to adjust if you'd like it scoped differently.
