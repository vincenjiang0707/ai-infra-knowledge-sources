# [Issue #2872] [RFC] Agent skill for hardware-aware quantization + example generation

source: https://github.com/vllm-project/llm-compressor/issues/2872
state: closed | updated: 2026-09-09T02:11:43Z
labels: RFC

## 正文

**Is your feature request related to a problem? Please describe.**

Two recurring friction points when adopting LLM Compressor:

1. **"Which scheme should I use on my GPU?"** Picking between FP8 / NVFP4 / W4A16
   / INT8 / MXFP4 means knowing what your hardware can actually accelerate
   (FP4 → Blackwell, FP8 → Ada/Hopper+, INT8 → Turing+) and whether the model
   even fits VRAM for calibration *and* serving.
2. **Writing the first example.** Each new model/scheme means copying an
   `examples/*.py`, swapping model/recipe/scheme/ignore, and remembering current
   API details (e.g. AWQ now lives in `modifiers.transform.awq` paired with a
   `QuantizationModifier`).

**Describe the solution you'd like**

An optional **agent skill** (`SKILL.md` + small helper scripts) that:

- detects the local GPU (or a `--target` GPU) and recommends a scheme;
- estimates VRAM fit from HF metadata (no download);
- **generates a flat `examples/`-style script** for the chosen model/scheme —
  templates copied from the canonical examples, current APIs only — and can
  optionally run it;
- ships `verify_apis.py` to confirm every import/scheme it uses exists in the
  installed `llmcompressor` / `compressed-tensors`.

It **mirrors verified examples and delegates to real APIs** rather than
reimplementing library logic, so its output is itself a mergeable example. It is
also safe by construction: no telemetry, network limited to the HF reads any
example does, read-only hardware/verify steps, and it only writes the file you
name (no shell, no remote exec).

**Questions before a PR:**

1. Do you want an agent skill of this kind in the repo at all?
2. Placement — a new top-level `skills/`, the existing `.claude/skills/`, or
   `docs/`?
3. Is an optional NVIDIA Model Optimizer comparison welcome, or better left out
   to avoid an out-of-tree dependency?

**Describe alternatives you've considered**

- Keep the skill local and only contribute the **generated `examples/*.py`** it
  produces.
- Place it under `.claude/skills/` next to the existing `style.md` / `test.md`.

**Additional context**

A working version is up as a draft PR for reference (linked below). It is
API-correct against `main` and `ruff` / `ruff format`-clean; on an RTX 5090 the
generated FP8/NVFP4/AWQ scripts run end-to-end and produce vLLM-servable
compressed-tensors checkpoints. Happy to adjust placement and scope to your
preference.


## 评论 (5)

### 2imi9 · 2026-06-29

Reference draft PR with a working implementation: https://github.com/vllm-project/llm-compressor/pull/2873

### dsikka · 2026-06-29

Hey - I actually started a set of skills to help with initial model creation: https://github.com/vllm-project/llm-compressor/pull/2851
This should act as the source of truth in coming up with writing an example. This needs some additional testing but I plan to land this in the coming weeks.

### 2imi9 · 2026-06-30

Thanks @dsikka — makes sense, I'll treat #2851 as the source of truth for example generation and close #2873 to avoid duplicating it.

Two things #2851 doesn't cover yet that I'm happy to add as a small follow-up if useful:

- **detect → recommend + fit**: a helper that reads the local (or `--target`) GPU's compute capability and auto-picks the scheme — your per-scheme skills already have the hardware notes, this just automates choosing between them (Blackwell→NVFP4, Ada/Hopper→FP8, Ampere→W4A16…) — plus a quick "will it fit?" VRAM estimate from HF safetensors metadata before downloading.
- **testing**: I have a Blackwell RTX 5090 + working env, so I'm glad to run #2851's generated scripts end-to-end (FP8/NVFP4/INT8/MXFP4) and report any breakage, since you mentioned it needs more testing.

Otherwise I'll happily just use #2851 — thanks for the heads-up!


### 2imi9 · 2026-06-30

Followed your template and drafted four skills for the formats #2851 doesn't cover yet — kv-cache, attention, w4a8 (W4AFP8), and autoround — in https://github.com/vllm-project/llm-compressor/pull/2878. Same `examples/.claude/skills/` structure, independent directories, and all four smoke-tested end-to-end on a 5090. Happy to fold these into #2851 instead if you'd prefer a single PR.

### dsikka · 2026-09-09

Closing as completed by https://github.com/vllm-project/llm-compressor/tree/main/examples/.claude/skills
