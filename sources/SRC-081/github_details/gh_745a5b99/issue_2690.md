# [Issue #2690] [RFC] HIGGS Integration into llm-compressor

source: https://github.com/vllm-project/llm-compressor/issues/2690
state: open | updated: 2026-08-25T18:17:14Z
labels: enhancement, RFC, keep-open

## 正文

# [RFC] Native HIGGS-style mixed-precision allocation pipeline in `llm-compressor` (NVFP4 / FP8_Dynamic / FP16)

## Background

We implemented a practical HIGGS-style workflow externally around `llm-compressor` and `vLLM`, inspired by the paper *Pushing the Limits of Large Language Model Quantization via the Linearity Theorem*.

Today, the workflow is split into three custom scripts:

1. `create_quantized_layers.py`  
   - Runs `llmcompressor.oneshot(...)` to export per-layer/group weights for multiple precisions (currently `FP16`, `FP8_Dynamic`, `NVFP4`).
2. `HIGGS.py`  
   - Builds an error DB from exported layer banks, estimates sensitivity coefficients (`alpha`) with heuristic/noise/hybrid modes, and solves an LP bit allocation problem under a target average bit budget.
3. `create_mixed_precision_models.py`  
   - Reads per-layer assignments and runs one final mixed quantization pass to generate the final compressed checkpoint.

This has been exercised across model families including:
- `meta-llama/Llama-3.2-{1B,3B}-Instruct`
- `meta-llama/Llama-3.1-8B-Instruct`
- `Qwen/Qwen3-8B`
- `Qwen/Qwen3-30B-A3B`
- `Qwen/Qwen3-30B-A3B-Instruct-2507`

## What we have today (working, but external)

- A reproducible optimization-first pipeline for mixed precision allocation.
- Architecture-aware grouping (e.g., `q/k/v -> qkv`, `gate/up -> gate_up`) to avoid incoherent per-subprojection assignment.
- Error modeling from measured relative Frobenius distortion per candidate precision.
- Alpha modes:
  - `heuristic` (cheap)
  - `noise` (loss-perturbation probing)
  - `hybrid`
- LP solve with constraints:
  - one precision choice per layer/group
  - weighted bit budget target
  - optional anti-degenerate mixedness behavior
- Final checkpoint generation via one-shot quantization using chosen assignments.
- Evaluation utilities (KL/perplexity) with `vLLM` prompt logprobs.

## Problem / pain points

The current setup requires substantial glue code and multiple passes around `oneshot`:

- custom artifact export + parsing (`.pth` banks, metadata, layer size JSON)
- custom grouping/expansion conventions duplicated outside compressor internals
- external optimization script and solver dependencies
- custom config handoff into final quantization pass
- hard to standardize and maintain as first-class `llm-compressor` UX

In short: the approach works, but orchestration is outside `llm-compressor`, so users must reimplement pipeline logic to reproduce HIGGS-like dynamic allocation.

## Proposal

Add first-class HIGGS-style mixed-precision allocation support in `llm-compressor` so users can run this as a native pipeline/modifier flow.

### Proposed capabilities

1. **Candidate precision scoring pass**
   - Native way to collect per-layer/group distortion for multiple candidate quant schemes.
   - Reuse existing quantization infrastructure instead of external layer-bank scripts.

2. **Layer/group abstraction**
   - First-class grouping policy for transformer projections (e.g. `qkv`, `gate_up`) and singletons (`o_proj`, `down_proj`), with extensibility for architectures.

3. **Sensitivity (`alpha`) estimation plugins**
   - Built-in modes equivalent to current prototype:
     - `heuristic`
     - `noise`
     - `hybrid`
   - Noise mode should integrate cleanly with sequential/offload-friendly pipelines.

4. **Global allocator**
   - Built-in LP/MIP allocator over candidate precisions under weighted bit budget.
   - Output should include assignment map + summary stats + feasibility diagnostics.

5. **Materialization stage**
   - Apply assignment map directly to produce one final compressed checkpoint.
   - Integrate with current `QuantizationModifier` / config groups and serialization conventions.

6. **Artifacts and reporting**
   - Optional persisted artifacts for:
     - per-layer error tables
     - alpha tables
     - allocator stats
     - final assignment JSON

## Sketch of desired user experience

Something close to:

```yaml
HIGGSMixedPrecisionModifier:
  targets: ["Linear"]
  candidate_schemes: ["NVFP4", "FP8_DYNAMIC", "FP16"]
  target_avg_bits: [5.0, 5.5, 6.0, 6.5, 7.0]
  grouping:
    policy: "transformer_default"  # qkv, gate_up, o_proj, down_proj
  alpha:
    method: "hybrid"               # heuristic | noise | hybrid
    calibration_dataset: "HuggingFaceH4/ultrachat_200k"
    calibration_split: "train_sft"
    calibration_samples: 32
  optimizer:
    solver: "scip"
    force_mixed: true
  output:
    save_assignment: true
    save_stats: true
```

Or equivalent CLI flags under a dedicated pipeline entrypoint.

## Scope / non-goals (for initial RFC)

**In scope**
- Weight precision allocation over a defined candidate set (`NVFP4` / `FP8_Dynamic` / `FP16`)
- Group-aware assignment and budget-constrained optimization
- Exporting reproducible assignment/stats artifacts

**Out of scope (initial)**
- New low-level quantization kernels
- Runtime scheduling/autotuning in serving stack
- Full automatic search over arbitrary precision families

## Why this should live in `llm-compressor`

- Uses existing compressor quantization primitives already validated in production paths.
- Converts a proven external workflow into reusable core functionality.
- Reduces user-side script maintenance and mismatch risk.
- Aligns with optimizer-first compression roadmap: quality-budget tradeoffs become explicit and reproducible.

## Requested feedback

1. Preferred integration point: new modifier vs dedicated pipeline stage vs hybrid.
2. Best place to host alpha estimation APIs (modifier-level, observer-level, pipeline utility).
3. Solver expectations and optional dependency policy for LP/MIP backends.
4. Recommended artifact format for assignment + diagnostics (JSON schema expectations).
5. Interest in upstreaming with an initial constrained scope (`NVFP4/FP8_Dynamic/FP16`) and expanding later.

## Acceptance criteria for an initial implementation

- User can run one command/recipe and obtain:
  - per-layer/group precision assignment satisfying target average bits
  - a final compressed checkpoint materialized from that assignment
  - saved stats/diagnostics for reproducibility
- Works on representative Llama/Qwen decoder-only transformer models.
- Produces stable assignment behavior across multiple target bit budgets and alpha modes.

## Repro context from current prototype
Reference implementation and scripts are available here: https://github.com/neuralmagic/HIGGS


## 评论 (5)

### rpathade · 2026-05-11

I’d be interested in taking a first pass at the initial implementation if that would be helpful. Happy to align on scope before starting.


### HDCharles · 2026-05-13

Things that we need to align on design wise:

Seems like the two expensive parts are generating N quantizations per layer and calculating sensitivity. 

1) generating N quantizations per layer shouldn't be too difficult, we don't apply quantization until the end so we'd need to record qparams for N configs which seems relatively straightforward by either instantiating multiple observers or by mutating the observer config once statistics are collected.

Also do we have to actually hold onto the quantized weights or just get the MSE?

2) calculating sensitivity seems harder. It seems like we can't do it locally and we need to carry the activations all the way through the model. At layer 1 we calculate N altered outputs for N configs. Then in layer two we calculate N more and also need to pipe through the first N. After L layers we have N*L activations we're carrying through to get the sensitivity. I don't think the pipeline has any way to add additional activations that we pipe through but maybe it can be added. @krishnateja95 is this what you were envisioning in your proposed capabilities 1?

other questions, thoughts:

About fusing the constrained layers. We've discussed this, we generally unfuse layers for the 
moe calibration context so I think we'll need to find a workaround if we want to use any existing infrastructure. Leaving them unfused but then adding constraints to the ILP doesn't seem hard but having to calculate one sensitivity per unfused layer seems unideal if this already is a slow process. If we're doing pt 1 above, this should be something we can handle despite the unfusion, i.e. adding noise to all fused layers at the same time to calculate a joint sensitivity for fused layers. Then our ILP can be the same as before.

can this technique compose with things like GPTQ? General transforms like AWQ/smoothquant could be applied ahead of time with a little adaptation but not sure how this would work with GPTQ in our current setup. Seems like it wouldn't be too hard to make it work with different observers though. I know we can do GPTQ after the fact, once we've decided on how we quantize each layer but it seems like taking the GPTQ error into account in the ILP could be valuable. Actually maybe not since GPTQ will likely have a higher MSE.

So it seems like there are a few ways we can do this

1) use some kind of data free pipeline to get MSEs -> use heuristic to get sensitivity -> solve ILP to generate config -> run oneshot with config with data (note this will ignore error from dynamic quant)
1a same but then run data free pipeline (maybe for nvfp4a16 or w4a16)
2) use sequential pipeline to get MSE, qparams and calculate sensitivity -> solve ILP -> finalize configs and qparams
2a) same but don't record qparams and instead finalize with one shot (GPTQ?)

I suspect we might want option 1/1a as a fast path regardless. That path should be largely dominated by the speed of the final one shot which would be a lot faster. Especially if we can do 1a, we can make something which will be super fast for people to play with.



### brian-dellabetta · 2026-05-14

> calculating sensitivity seems harder. It seems like we can't do it locally and we need to carry the activations all the way through the model.

I missed this point in the initial HIGGS presentation. Isn't the whole point of the linearity theorem that layer-wise error can be treated independent from the overall change in PPL? If yes, this becomes a much easier problem to solve with the independent pipeline, provided we restrict sequential_targets to be the decoder layer. We don't have to worry about carrying activations all the way through the model

From https://arxiv.org/pdf/2411.17525

<img width="665" height="533" alt="Image" src="https://github.com/user-attachments/assets/11342e27-5edd-4ca8-8cc1-52ee8ee44c03" />

### HDCharles · 2026-05-15

There's 2 terms, a_l and t_l, t_l is basically MSE or whatever is in equation 3. The other is the hard part, it's independent of how you quantize the layer. You can calculate it with a heuristic or by applying some noise to the later and seeing how that changes the output. This is what's hard to calculate.

### github-actions[bot] · 2026-08-18

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!
