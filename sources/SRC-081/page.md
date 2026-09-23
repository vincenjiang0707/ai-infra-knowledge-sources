# GPTQModel

source: https://github.com/vllm-project/llm-compressor/releases

# Releases: vllm-project/llm-compressor

## Release list

## v0.14.0


# LLM-Compressor v0.14.0

## Key Highlights ✨

-
**GPTQ Performance Improvements**[#3128](https://github.com/vllm-project/llm-compressor/pull/3128)- GPTQ now ships a Triton-based quantization kernel, approximately
**15× faster end-to-end**than the previous implementation. - Layers that share the same shape can now be batched, achieving approximately
**30× faster end-to-end performance**on some MoE workloads. - Hessian offloading has been removed.
- The remaining eager path was independently sped up by
**1.5–2×**.

- GPTQ now ships a Triton-based quantization kernel, approximately
-
**Expanded MSE/iMatrix Observers**[#2950](https://github.com/vllm-project/llm-compressor/pull/2950),[#3076](https://github.com/vllm-project/llm-compressor/pull/3076)- Added functionality to expand the grid search for iMatrix and MSE observers.
- Enables identification of better local scales for NVFP4.
- The expanded search space is a superset of the Fourosix-style quantization strategy.

-
**MSE Observer Performance Improvements**[#2991](https://github.com/vllm-project/llm-compressor/pull/2991)- Added a new Triton kernel for grid search, improving observation time by approximately
**10×**. - Reaches bitwise parity with the eager path under full evaluation.

- Added a new Triton kernel for grid search, improving observation time by approximately
-
**REAP DDP + e-Score Correction**[#3045](https://github.com/vllm-project/llm-compressor/pull/3045),[#3101](https://github.com/vllm-project/llm-compressor/pull/3101)- REAP expert pruning now supports distributed DDP runs.
- Added optional e-score correction bias.
- Added a new HY3 example.

-
**Model-Free PTQ Improvements**[#2976](https://github.com/vllm-project/llm-compressor/pull/2976),[#3053](https://github.com/vllm-project/llm-compressor/pull/3053),[#2935](https://github.com/vllm-project/llm-compressor/pull/2935),[#3158](https://github.com/vllm-project/llm-compressor/pull/3158)- Replaced static round-robin GPU assignment with a dynamic, memory-aware scheduler.
- Added mixed-precision and KV-cache quantization support.
- Unified the entry point into a single
`ModelFreePtqConverter`

class. - Added profiler-based memory estimates.

-
**Expanded MoE Machinery**[#3080](https://github.com/vllm-project/llm-compressor/pull/3080),[#3017](https://github.com/vllm-project/llm-compressor/pull/3017),[#3173](https://github.com/vllm-project/llm-compressor/pull/3173),[#3100](https://github.com/vllm-project/llm-compressor/pull/3100)- Added
`patch_moe_mappings()`

for overriding 2D load mappings per checkpoint. - Added
`repack_moe()`

for restoring native fused 3D expert modules after linearization. - Added fast loading for
`nemotron_h`

(Nemotron 3 Ultra). - Added GPT-OSS expert linearization.

- Added

## GPTQ

The GPTQ modifier received its largest performance upgrade since launch in ** #3128**:

**New Triton GPTQ kernel:**Approximately**15× faster**than the previous eager implementation.**Layer batching:**Layers sharing the same shape can be quantized together, achieving approximately**1.67× higher throughput per batch**and up to**30× end-to-end speedups**on MoE workloads with many shared shapes.**Simplified Hessian handling:**Removed Hessian offloading.**Faster eager path:**Independently improved by approximately**1.5–2×**.**Hessian loop optimization:**Hoisted loop invariants out of the per-column quantization loop ([#3097](https://github.com/vllm-project/llm-compressor/pull/3097)).**RTN fallback reporting:**Added an end-of-run summary for modules that fall back to RTN ([#3098](https://github.com/vllm-project/llm-compressor/pull/3098)).**A100 FP8 support:**Fixed GPTQ FP8 handling with a supported Triton FP8 cast ([#3181](https://github.com/vllm-project/llm-compressor/pull/3181)).

## Observers

### NVFP4 and MSE/iMatrix

**Expanded grid search:**MSE and iMatrix observers now support an expansion factor, making their search space a superset of the Fourosix strategy ([#2950](https://github.com/vllm-project/llm-compressor/pull/2950)).**NVFP4 quality:**The new expanded MSE observer outperforms GPTQ for NVFP4 on average across internal perplexity benchmarks.**Triton MSE grid search:**Added a Triton kernel for scale grid search with buffered per-qparam patience and adaptive 512-value tiling ([#2991](https://github.com/vllm-project/llm-compressor/pull/2991)).**Bitwise parity:**The Triton MSE implementation reaches bitwise parity with the eager path under full evaluation.**Format coverage:**Supports INT, FP4, FP8, and FP16/BF16 with E8M0 scales.**Triton error buffer:**Added`triton_error_buffer`

to enable approximate congruence between eager and Triton patience behavior.**Observer resolution:**Quantization-argument resolution and observer defaulting moved from`compressed-tensors`

into LLM-Compressor ([#3091](https://github.com/vllm-project/llm-compressor/pull/3091)).**Validation:**`MovingAverageMSEObserver`

now validates`expand >= 1.0`

([#3095](https://github.com/vllm-project/llm-compressor/pull/3095)).

## Model-Free PTQ

**Dynamic GPU scheduling:**Replaced static round-robin assignment with a capacity-first, memory-aware scheduler that queries available GPU memory before each job and tracks reservations ([#2976](https://github.com/vllm-project/llm-compressor/pull/2976)).**Reliable fallback:**Insufficient capacity now triggers an explicit fallback instead of silently dropping work.**Mixed precision:**Added mixed-precision quantization support ([#3053](https://github.com/vllm-project/llm-compressor/pull/3053)).**KV-cache quantization:**Added KV-cache quantization support.**Unified API:**Consolidated model-free PTQ into`ModelFreePtqConverter`

([#2935](https://github.com/vllm-project/llm-compressor/pull/2935)).**Memory estimation:**Added profiler-based memory estimates ([#3158](https://github.com/vllm-project/llm-compressor/pull/3158)).

## REAP

**Distributed support:**REAP expert pruning now supports DDP.- Saliency statistics are reduced across ranks.
- Statistics are computed on rank 0.
- Results are broadcast back to workers (
[#3045](https://github.com/vllm-project/llm-compressor/pull/3045)).

**e-Score correction:**Added an optional e-score correction bias ([#3101](https://github.com/vllm-project/llm-compressor/pull/3101)).**New example:**Added an HY3 REAP example.

## MoE

Expanded MoE support includes:

`patch_moe_mappings()`

— Override 2D load mappings on a per-checkpoint basis through a load context ([#3080](https://github.com/vllm-project/llm-compressor/pull/3080)).`repack_moe()`

— Restore native fused 3D expert modules so`save_pretrained()`

writes Hugging Face-native keys ([#3017](https://github.com/vllm-project/llm-compressor/pull/3017)).**Nemotron 3 Ultra:**Added fast-loading support and 2D conversion mappings for`nemotron_h`

([#3173](https://github.com/vllm-project/llm-compressor/pull/3173)).**GPT-OSS:**Added expert linearization support ([#3100](https://github.com/vllm-project/llm-compressor/pull/3100)).**Performance:**Experts are no longer onloaded when checking`FusedExpertsProtocol`

([#3039](https://github.com/vllm-project/llm-compressor/pull/3039)).**Cleanup:**Removed`GraniteMoeLinearExperts`

([#2885](https://github.com/vllm-project/llm-compressor/pull/2885)).

## New Model Support

**GLM 5.3 / GLM 5.3 Flash**([#3164](https://github.com/vllm-project/llm-compressor/pull/3164))**Kimi-K3****Qwen3.8****Muse Glimmer**— Added AWQ mappings ([#3124](https://github.com/vllm-project/llm-compressor/pull/3124))**Cohere2MoE**— Added AWQ and SmoothQuant support ([#2938](https://github.com/vllm-project/llm-compressor/pull/2938))**DeepSeekV2**— Added AWQ support ([#2938](https://github.com/vllm-project/llm-compressor/pull/2938))**Nanbeige**— Added AWQ/SmoothQuant mappings ([#3073](https://github.com/vllm-project/llm-compressor/pull/3073))**Glm4MoeLite**— Added AWQ/SmoothQuant mappings ([#3072](https://github.com/vllm-project/llm-compressor/pull/3072))**OlmoForCausalLM v1/v2**- Added AWQ/SmoothQuant mappings using the Exaone4-style mapping.
[#2802](https://github.com/vllm-project/llm-compressor/pull/2802)


## New Examples

**MR-GPTQ:**QuIP + GPTQ + NVFP4A16 ([#2751](https://github.com/vllm-project/llm-compressor/pull/2751))**FP8 Attention + AutoRound:**Qwen3 dense and MoE ([#3092](https://github.com/vllm-project/llm-compressor/pull/3092))**Mixed W2A16 / W4A16 MoE**([#2940](https://github.com/vllm-project/llm-compressor/pull/2940))**GLM-5.2 MXFP4 × MXFP8**([#3048](https://github.com/vllm-project/llm-compressor/pull/3048))**DeepSeek V4 MXFP4–MXFP8**([#2897](https://github.com/vllm-project/llm-compressor/pull/2897))**GLM-5.3 MXFP4**([#3163](https://github.com/vllm-project/llm-compressor/pull/3163))**Llama 3.3 70B MXFP8 + FP8 Attention**([#3160](https://github.com/vllm-project/llm-compressor/pull/3160))**Qwen3 MoE**([#2946](https://github.com/vllm-project/llm-compressor/pull/2946))**Agent skills**- Added a shared quantization skill for AWQ, SmoothQuant, GPTQ, and
`QuantizationModifier`

. - Added FP8/NVFP4 skill updates.
- Added prebaked-dataset selection.
[#2971](https://github.com/vllm-project/llm-compressor/pull/2971)

- Added a shared quantization skill for AWQ, SmoothQuant, GPTQ, and

## Performance

**GPTQ:**New Triton kernel and layer batching ([#3128](https://github.com/vllm-project/llm-compressor/pull/3128)).**Subgraph tracing:**O(1) node-membership lookups ([#2992](https://github.com/vllm-project/llm-compressor/pull/2992),[#2999](https://github.com/vllm-project/llm-compressor/pull/2999)).**AutoRound VRAM:**Calibration inputs can be offloaded to CPU for large`N`

([#3055](https://github.com/vllm-project/llm-compressor/pull/3055)).**AutoRound memory:**Prevented`input_capture_hook`

from accumulating GPU memory during optimization ([#3024](https://github.com/vllm-project/llm-compressor/pull/3024)).

## Bug Fixes

- Upfront model decompression for Kimi-K3 (
[#3184](https://github.com/vllm-project/llm-compressor/pull/3184)) - Distributed hang caused by incorrectly shaped
`weight_global_scale`

writeback ([#3185](https://github.com/vllm-project/llm-compressor/pull/3185)) - GPTQ FP8 handling on A100 (
[#3181](https://github.com/vllm-project/llm-compressor/pull/3181)) - Prevent recursion into container modules in
`observe/update_qparams`

([#2990](https://github.com/vllm-project/llm-compressor/pull/2990)) - Dtype serialization (
[#3152](https://github.com/vllm-project/llm-compressor/pull/3152)) `polynomial_decay`

pruning scheduler for even exponents ([#3096](https://github.com/vllm-project/llm-compressor/pull/3096))- Global scale shape (
[#3191](https://github.com/vllm-project/llm-compressor/pull/3191)) - Qwen2.5-VL AWQ mapping for vision towers (
[#3169](https://github.com/vllm-project/llm-compressor/pull/3169)) - Python 3.14 compatibility issues in
`Recipe.dict()`

and dataset split help text ([#2778](https://github.com/vllm-project/llm-compressor/issues/2778),[#2871](https://github.com/vllm-project/llm-compressor/pull/2871),[#3140](https://github.com/vllm-project/llm-compressor/pull/3140)) `collect_env`

crash on Apple Silicon/MPS ([#3068](https://github.com/vllm-project/llm-compressor/pull/3068))- Decorated forwards without
`functools.wraps`

in`autowrap_forward`

([#3058](https://github.com/vllm-project/llm-compressor/pull/3058)) `llmcompressor.trace`

boolean flags now toggle correctly ([#3070](https://github.com/vllm-project/llm-compressor/pull/3070))- Runtime issues in recipe validation, AutoRound, and AWQ (
[#2973](https://github.com/vllm-project/llm-compressor/pull/2973)) - Weightless modules in distributed greedy bin packing (
[#3113](https://github.com/vllm-project/llm-compressor/pull/3113))

## Refactoring & Breaking Changes

- Removed deprecated GPTQ Group/Dynamic Activation Ordering (
[#3038](https://github.com/vllm-project/llm-compressor/pull/3038)). - Removed
`GraniteMoeLinearExperts`

([#2885](https://github.com/vllm-project/llm-compressor/pull/2885)). - Moved observer resolution/defaulting into LLM-Compressor (
[#3091](https://github.com/vllm-project/llm-compressor/pull/3091)). - Unified model-free PTQ under
`ModelFreePtqConverter`

([#2935](https://github.com/vllm-project/llm-compressor/pull/2935)). `TensorProfiler`

is now imported from`compressed-tensors`

([#3203](https://github.com/vllm-project/llm-compressor/pull/3203)).`exec_jobs_dynamic`

was ported to`compressed-tensors`

([#3075](https://github.com/vllm-project/llm-compressor/pull/3075)).

## Datasets & Miscellaneous

- Added the
`perfectblend`

prebaked dataset and`ultrachat`

alias ([#3060](https://github.com/vllm-project/llm-compressor/pull/3060)). - Replaced example datasets with prebaked
`perfectblend`

/`flickr30k`

datasets ([#3062](https://github.com/vllm-project/llm-compressor/pull/3062)). - Changed the default for
`pad_to_max_length`

([#3180](https://github.com/vllm-project/llm-compressor/pull/3180)). - Added
`resave_config`

to preserve the original model configuration on save ([#3147](https://github.com/vllm-project/llm-compressor/pull/3147)). - Sequential onloading now supports frozen dataclasses (
[#2016](https://github.com/vllm-project/llm-compressor/pull/2016)). - Modernized type hints across logger, datasets, and observers (
[#2960](https://github.com/vllm-project/llm-compressor/pull/2960)).

## Dependencies & Infrastructure

Bumped to`compressed-tensors`

:**0.19.0**([#3213](https://github.com/vllm-project/llm-compressor/pull/3213)).Minimum version raised to`accelerate`

:**>=1.15.0**for full-disk offloading ([#3176](https://github.com/vllm-project/llm-compressor/pull/3176)).**Transformers:**Updated the supported version range ([#3122](https://github.com/vllm-project/llm-compressor/pull/3122)).**Pre-commit:**Added hooks mirroring`make quality`

([#3120](https://github.com/vllm-project/llm-compressor/pull/3120)).

## Full Changelog

- Revise README for new Muse-Glimmer-30B checkpoints by
[@dsikka](https://github.com/dsikka)in[#3019](https://github.com/vllm-project/llm-compressor/pull/3019) - Update review rules by
[@dsikka](https://github.com/dsikka)in[#3026](https://github.com/vllm-project/llm-compressor/pull/3026) - load_quantizable_moe with new transformers version by
[@Roderick-Wu](https://github.com/Roderick-Wu)in[#3016](https://github.com/vllm-project/llm-compressor/pull/3016) - [transformers] Update tests to use new compressed-tensors api, pin transformers by
[@kylesayrs](https://github.com/kylesayrs)in[#3021](https://github.com/vllm-project/llm-compressor/pull/3021) - [MTP] Update to work with Qwen 3.8 by
[@dsikka](https://github.com/dsikka)in[#3033](https://github.com/vllm-project/llm-compressor/pull/3033) - [Performance] [MoE] Don't onload weights when checking FusedExpertsProtocol by
[@kylesayrs](https://github.com/kylesayrs)in[#3039](https://github.com/vllm-project/llm-compressor/pull/3039)

...

[Read more](https://github.com/vllm-project/llm-compressor/releases/tag/0.14.0)

## v0.13.0


# Key Highlights

**REAP Expert Pruning**—[#2864](https://github.com/vllm-project/llm-compressor/pull/2864): New modifier for structurally pruning Mixture-of-Experts (MoE) models by removing individual experts based on calibration-based saliency scores. Based on the[REAP the Experts paper](https://arxiv.org/pdf/2510.13999).**Arbitrary Bit-Width Quantization (Humming)**—[ct#732](https://github.com/vllm-project/compressed-tensors/pull/732),[ct#785](https://github.com/vllm-project/compressed-tensors/pull/785): Dense packing for non-power-of-2 bit widths (3, 5, 6, 7) with no wasted bits, plus 16 new WxAy presets covering W2–W8 weights with A4, A8, or A16 activations.**Observer Fusion and Deletion**—[#2865](https://github.com/vllm-project/llm-compressor/pull/2865): Refactored observer lifecycle and significantly reduced memory usage for large models due to observer statistics persisting after calibration.**Expanded MoE Architecture Support**—[#2847](https://github.com/vllm-project/llm-compressor/pull/2847): Extended MoE linearization to support a broader range of architectures, including Transformers v5.13.0 models.**Improved XPU Compatibility**—[#2776](https://github.com/vllm-project/llm-compressor/pull/2776),[#2884](https://github.com/vllm-project/llm-compressor/pull/2884): Migrated`torch.cuda`

calls to`torch.accelerator`

for Intel XPU support.**AutoRound Sub-Bit Quantization**—[#2895](https://github.com/vllm-project/llm-compressor/pull/2895): Added sub-bit quantization, including W2A16 attention / W4A16 MLP mixed precision.**Pre-Quantized Model Support**—[#2909](https://github.com/vllm-project/llm-compressor/pull/2909):`oneshot`

now provides experimental support for pre-quantized models, provided the targeted layers have not been previously quantized.

## REAP Expert Pruning

**REAP (Router-weighted Expert Activation Pruning)** structurally compresses MoE models by permanently removing individual experts based on saliency scores computed during calibration. The algorithm is introduced in the [REAP the Experts: Why Pruning Prevails for One-Shot MoE Compression](https://arxiv.org/pdf/2510.13999) paper.

REAP can be combined with quantization modifiers. For example, users can prune low-saliency experts first and then quantize the remaining model to **FP8** or **NVFP4**.

## Arbitrary Bit-Width Quantization (Humming)

### Dense Packing for Non-Standard Bit Widths

The `pack_quantized`

compressor in `compressed-tensors`

now uses dense cross-element packing ([ct#732](https://github.com/vllm-project/compressed-tensors/pull/732)). Previously, 3-, 5-, 6-, and 7-bit formats used padded packing that wasted bits.

The new implementation:

- Packs 32 consecutive
`intB`

elements into exactly`num_bits`

`int32`

words. - Uses no wasted bits and splits elements across
`int32`

boundaries when needed. - Supports activation quantization in addition to weight-only schemes.

### Expanded WxAy Quantization Presets

A new `_int_wnam()`

helper generates valid integer WxAy combinations ([ct#785](https://github.com/vllm-project/compressed-tensors/pull/785)), adding **16 presets** covering W2–W8 weights with A4, A8, or A16 activations, including W3A8, W5A16, and W6A8.

All presets use **group-128 symmetric weights** and **token-wise dynamic symmetric activations** and are supported in vLLM as of [vllm#46390](https://github.com/vllm-project/vllm/pull/46390).

W2–W7 weight-only (A16) schemes were also added as standalone presets ([ct#760](https://github.com/vllm-project/compressed-tensors/pull/760)), extending the previous W4A16 and W8A16 presets.

## Observer Fusion and Deletion

Observer lifecycle management was refactored to fix a memory leak where statistics persisted after calibration ([#2865](https://github.com/vllm-project/llm-compressor/pull/2865)):

- A dedicated
`fusion_handler`

manages fused observer groups. - Statistics are deleted only after the full fusion group completes.
- Weight observers skip redundant observation when statistics already exist, reducing recomputation for AWQ/GPTQ workflows.

## Expanded MoE Support

MoE linearization now supports a broader range of architectures, including models introduced in Transformers v5.13.0 ([#2847](https://github.com/vllm-project/llm-compressor/pull/2847)). Import patterns were also refactored for backwards compatibility.

**Cohere2MoE SpinQuant** support was added ([#2867](https://github.com/vllm-project/llm-compressor/pull/2867)), including special handling for its parallel transformer block where one `input_layernorm`

feeds attention, MLP, and the router.

## Lifecycle Improvements

### Calibration Events

Calibration events are now first-class lifecycle hooks ([#2783](https://github.com/vllm-project/llm-compressor/pull/2783), [#2784](https://github.com/vllm-project/llm-compressor/pull/2784)):

- Added
`on_calibration_start`

,`on_sequential_epoch_end`

, and`on_calibration_end`

. - Calibration start/end logic is handled by the
`Modifier`

base class. - Renamed
`calibration_epoch_start/end`

to`calibration_start/end`

.

### Calibration Requirement Check

Each modifier now declares `requires_calibration_data()`

([#2947](https://github.com/vllm-project/llm-compressor/pull/2947)), replacing the hardcoded pipeline registry list. GPTQ, AutoRound, SparseGPT, Wanda, SmoothQuant, AWQ, and REAP explicitly require calibration.

### Pipeline Device Movement

Device movement logic has been removed from pipelines ([#2846](https://github.com/vllm-project/llm-compressor/pull/2846)). `load_offloaded_model`

now handles distributed dispatch and disk offloading, simplifying pipeline logic.

## Distributed Improvements

**Module Parallel Calibration**—[#2785](https://github.com/vllm-project/llm-compressor/pull/2785): Weight calibration can run in parallel across distributed workers.**Suspend Distributed Timeout**—[#2868](https://github.com/vllm-project/llm-compressor/pull/2868): Supports saving very large or disk-offloaded models taking more than 10 minutes.**AutoRound DDP**—[#2844](https://github.com/vllm-project/llm-compressor/pull/2844),[#2934](https://github.com/vllm-project/llm-compressor/pull/2934): Added Qwen MoE DDP example and fixed rank-local device placement.**DDP Smoke Tests**—[#2769](https://github.com/vllm-project/llm-compressor/pull/2769): Added comprehensive DDP tests with subsequent stability fixes in[#2840](https://github.com/vllm-project/llm-compressor/pull/2840),[#2857](https://github.com/vllm-project/llm-compressor/pull/2857),[#2863](https://github.com/vllm-project/llm-compressor/pull/2863), and[#2943](https://github.com/vllm-project/llm-compressor/pull/2943).

## Performance

—`torch.compile`

for MSE Observer[#2384](https://github.com/vllm-project/llm-compressor/pull/2384): Added chunked execution support for`torch.compile`

, with significant speedups for activation quantization. Pass`enable_compile=True`

to`oneshot`

to enable.—`IntermediatesCache`

`pin_memory`

Fix[#2813](https://github.com/vllm-project/llm-compressor/pull/2813): Fixed a CUDA OOM issue with nested dispatchers.**Reduced Default Save Shard Size**—[#2927](https://github.com/vllm-project/llm-compressor/pull/2927): Reduced the default shard size to**20 GB**for improved network transfer performance.

## XPU Compatibility

All main-path `torch.cuda`

calls have been migrated to `torch.accelerator`

([#2884](https://github.com/vllm-project/llm-compressor/pull/2884)). A `torch.cuda`

linter was added to CI ([#2776](https://github.com/vllm-project/llm-compressor/pull/2776)), along with XPU Docker and testing infrastructure ([#2945](https://github.com/vllm-project/llm-compressor/pull/2945)).

## New Model Support

**DeepSeek V4 Pro**—[#2858](https://github.com/vllm-project/llm-compressor/pull/2858), with automatic MTP weight copying ([#2951](https://github.com/vllm-project/llm-compressor/pull/2951)).**GLM 5.2**—[#2869](https://github.com/vllm-project/llm-compressor/pull/2869)**GLM 4.6**—[#2343](https://github.com/vllm-project/llm-compressor/pull/2343)**HunyuanMoE V3**—[#2928](https://github.com/vllm-project/llm-compressor/pull/2928)**Gemma 4**—[#2816](https://github.com/vllm-project/llm-compressor/pull/2816)**Mellum2**—[#2832](https://github.com/vllm-project/llm-compressor/pull/2832)**Cohere2MoE SpinQuant + NVFP4**—[#2867](https://github.com/vllm-project/llm-compressor/pull/2867)**Input Embedding Quantization example**—[#2830](https://github.com/vllm-project/llm-compressor/pull/2830)**New AWQ/SmoothQuant mappings**for Step3p5 ([#2770](https://github.com/vllm-project/llm-compressor/pull/2770)), Granite ([#2797](https://github.com/vllm-project/llm-compressor/pull/2797)), Nanbeige ([#2966](https://github.com/vllm-project/llm-compressor/pull/2966)), and Qwen3.5 MoE ([#2718](https://github.com/vllm-project/llm-compressor/pull/2718),[#2727](https://github.com/vllm-project/llm-compressor/pull/2727)).

## Breaking Changes

- Removed sparsity-preserving logic from GPTQ —
[#2860](https://github.com/vllm-project/llm-compressor/pull/2860) - Removed
`IMatrixGatherer`

; functionality consolidated into observers —[#2920](https://github.com/vllm-project/llm-compressor/pull/2920) - Deprecated
`GPTQ actorder=group`

—[#2893](https://github.com/vllm-project/llm-compressor/pull/2893) - Deprecated
`reindex_fused_weights`

—[#2737](https://github.com/vllm-project/llm-compressor/pull/2737) - QuIP now defaults to input (
`v`

) rotations only —[#2815](https://github.com/vllm-project/llm-compressor/pull/2815)

## New Contributors

[@KKothuri](https://github.com/KKothuri)made their first contribution in[#2830](https://github.com/vllm-project/llm-compressor/pull/2830)[@EdalatiAli](https://github.com/EdalatiAli)made the...

[Read more](https://github.com/vllm-project/llm-compressor/releases/tag/0.13.0)

## v0.12.0.1

## v0.10.0.3

## What's Changed

- [Deprecation] Remove Sparse24 e2e tests from release-0.10.0 by
[@deepak-kumar-neu](https://github.com/deepak-kumar-neu)in[#2720](https://github.com/vllm-project/llm-compressor/pull/2720) - [release-0.10.0] bump up pillow and requests upper bound by
[@dhuangnm](https://github.com/dhuangnm)in[#2959](https://github.com/vllm-project/llm-compressor/pull/2959)

**Full Changelog**: `0.10.0.2...0.10.0.3`

## v0.9.0.4

## v0.7.1.4

## v0.7.1.3

## v0.12.0


# LLM Compressor v0.12.0 Release Notes

This release upgrades to Transformers v5 with improved MoE support, streamlines the dataset interface, and adds multi-GPU acceleration for model-free PTQ. Major highlights include comprehensive Transformers v5 integration with refactored MoE linearization, a simplified dataset split API that removes legacy multi-stage logic, multi-GPU distribution for model-free PTQ workflows, and expanded model coverage with Nemotron Ultra FP8 examples.

This release contains changes to example scripts with backwards compatibility with previous examples and scripts. Please read [Transformers v5](https://github.com#transformers-v5) for more information.

## Key Highlights ✨

- Transformers v5 Upgrade (
[#2647](https://github.com/vllm-project/llm-compressor/pull/2647)): Full integration with Transformers v5, including refactored MoE linearization with`load_context`

for efficient loading, updated model structure handling, and improved tied embeddings support. Maintains LM eval performance across the transition. Note:**LLM Compressor no longer supports installation with**.`transformers<5.0.0`

- Simplified Dataset Interface (
[#2551](https://github.com/vllm-project/llm-compressor/issues/2551)): Removed legacy multi-split logic, replacing`splits={"calibration": "train[:100]"}`

with cleaner`split="train[:100]"`

API. Legacy argument usage is deprecated and will be removed in a future release. - Multi-GPU Model-Free PTQ (
[#2773](https://github.com/vllm-project/llm-compressor/pull/2773)): Added support to distribute model-free PTQ jobs across multiple GPUs for significant parallelization and speedup for quantization workflows. - Nemotron Ultra Support (
[#2803](https://github.com/vllm-project/llm-compressor/pull/2803)): Added FP8 quantization example for Nemotron Ultra models in the model-free PTQ examples.

# Transformers v5

## Examples and Model Loading

-
Example regexes and recipes have been updated to reflect new model structures introduced by Transformers v5

-
Examples which utilize disk offloading or mixture-of-experts (MoE) calibration now load models with

`load_context`

provided by`llmcompressor.utils`

. This context is a catch-all context and should be used in all scripts for efficient model loading.

```
- from compressed_tensors.offload import load_offloaded_model
- from llmcompressor.modeling.moe.linearize import load_quantizable_moe
-
- with load_offloaded_model(), load_quantizable_moe():
- model = AutoModelForCausalLM.from_pretrained(model_id)
+ from llmcompressor.utils import load_context
+
+ with load_context():
+ model = AutoModelForCausalLM.from_pretrained(model_id)
```

`dtype`

now defaults to`"auto"`

, so this explicit argument has been removed to reduce verbosity

```
- model = AutoModelForCausalLM.from_pretrained(model_id, dtype=”auto”)
+ model = AutoModelForCausalLM.from_pretrained(model_id)
```

`from_pretrained`

no longer supports`use_auth_token`

. This argument has been removed from`oneshot`


## Expanded and Refactored MoE Support

Applying quantization to Mixture-of-Experts (MoE) models requires explicit linearization and class overriding in order to efficiently calibrate experts. This logic has been implemented by LLM Compressor through two pathways:

`llmcompressor.modeling.moe.linearize::linearize_moe`

which replaces experts modules with linearized and calibration-friendly classes AFTER weights have already been loaded

`llmcompressor.modeling.moe.linearize::load_quantizable_moe`

which replaces experts modules with linearized and calibration-friendly classes BEFORE weights have been loaded. This context is more efficient and reduces runtime during model loading.

Both of these pathways are called as needed by `llmcompressor.utils::load_context`

. These implementations are capable of automatically handling >90% of all model definitions provided by `transformers`

. For unconventional or custom model definitions, see [Adding MoE Calibration Support for a New Model](https://docs.vllm.ai/projects/llm-compressor/en/latest/developer-tutorials/add-moe-support)

## Multi-GPU Model-Free PTQ

Model-free PTQ now supports distributing quantization jobs across multiple GPUs when available. This feature automatically detects available GPUs and parallelizes the quantization workflow, significantly reducing processing time for large models.

## Simplified Dataset Interface

The dataset split interface has been refactored to remove legacy multi-stage logic that previously supported separate datasets for training, oneshot, and eval in a single command. Since training and eval tasks are no longer supported in the same command, the API has been simplified.

Old interface:

```
oneshot(
model,
dataset="ultrachat",
splits={"calibration": "train_sft[:100]"}
)
```

New interface:

```
oneshot(
model,
dataset="ultrachat",
split="train_sft[:100]"
)
```

The new API is backwards compatible and will issue warnings when using the old dictionary-based splits argument.

## Nemotron 3 Ultra Examples

This release adds model-free PTQ examples for NVIDIA's Nemotron-3-Ultra-550B model.

Pre-quantized FP8 checkpoints are available on HuggingFace:

[NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-dynamic](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-dynamic)[NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-block](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-block)- See the model-free
[PTQ examples](https://github.com/vllm-project/llm-compressor/tree/main/examples/model_free_ptq)for usage details.

## Breaking Changes

- The minimum transformers version has been bumped up to v5.9

## New Contributors

[@JINO-ROHIT](https://github.com/JINO-ROHIT)made their first contribution in[#2773](https://github.com/vllm-project/llm-compressor/pull/2773)[@u7k4rs6](https://github.com/u7k4rs6)made their first contribution in[#2779](https://github.com/vllm-project/llm-compressor/pull/2779)[@soyr-redhat](https://github.com/soyr-redhat)made their first contribution in[#2794](https://github.com/vllm-project/llm-compressor/pull/2794)[@arpitkh101](https://github.com/arpitkh101)made their first contribution in[#2589](https://github.com/vllm-project/llm-compressor/pull/2589)[@Priya95715](https://github.com/Priya95715)made their first contribution in[#2768](https://github.com/vllm-project/llm-compressor/pull/2768)

**Full Changelog**: `0.11.0...0.12.0`

## v0.11.0


# LLM Compressor v0.11.0

This release focuses on distributed computing enhancements, quantization lifecycle improvements, and expanded model support. Major highlights include DDP support for AWQ and SmoothQuant with significant speedups (up to 3.2x), a comprehensive refactor of the Compressed Tensors API, and observer/lifecycle refactors that simplify quantization workflows. New model support includes Qwen 3.5/3.6, Gemma 4, Kimi K2.6, and experimental DeepSeek-V4 support along with quantized checkpoints.

Note: LLM Compressor v0.11.0 removes support for Sparse24 quantization formats and sparse model compression. This decision was made based upon lack of community interest and maintainability concerns. Support for sparse compression may be re-introduced as part of a future release. For Sparse24 compression support, please use LLM Compressor v0.10.0.2.


## Key Highlights ✨

**DDP Performance**: AWQ and SmoothQuant now support DDP with 2.9-3.2x speedups and up to 51% memory reduction per GPU (with 4 GPUs).**Compressed Tensors Refactor**: Simplified API with clear entrypoints, removed sparsity support, streamlined compressor architecture**Quantization Lifecycle**: Unified calibration timing (now at epoch end), decoupled observation from qparam calculation**Extended Quantization Support**: GPTQ actorder now works across all weight strategies, AWQ refactored for NVFP4 compatibility**Converter Entrypoint**: New tool and framework for converting from AutoAWQ and ModelOpt NVFP4 to Compressed-Tensors, as well as decompressing Compressed-Tensors checkpoints**Large Model Support**: DDP+GPTQ+disk offloading fixes for models like Qwen3-VL-235B-A22B

## DDP and Lifecycle Updates

-
**AWQ DDP Support**: Added DDP (Distributed Data Parallel) functionality for AWQ resulting in significant speedups and reduced GPU memory usage:Model Single-GPU Time DDP Time (4 GPUs) Speedup Single-GPU Memory DDP Memory Memory Reduction Llama-3-8B 7.02 min 2.40 min 2.9x 10.20 GB 4.99 GB 51% Llama-3-8B (masked) 8.13 min 2.67 min 3.0x 10.14 GB 4.98 GB 51% Qwen3-30B-A3B 459.65 min 143.90 min 3.2x 4.13 GB 3.36 GB 19% Accuracy metrics remain comparable between DDP and single-GPU approaches.

-
**SmoothQuant DDP Support**: Added DDP support for SmoothQuant resulting in significant speedups:GPUs Total Time Peak GPU Mem Speedup 1 GPU 94.1 min 8.93 GB 1.00x 2 GPU 58.7 min 7.06 GB 1.60x 4 GPU 28.7 min 7.06 GB 3.28x

Special thanks to [@dzhengAP](https://github.com/dzhengAP) for their excellent contributions to the SmoothQuantModifier!

-
**Observer Refactor**: Decoupled observation from quantization parameter calculation, allowing natural separation of responsibilities where`observer.forward()`

records statistics about observed tensors while`get_qparams()`

performs qparam calculation. This simplifies design and expands the types of observers supported. Key changes:- Observers now have
`update_statistics_from_observed()`

for forward pass and`get_qparams()`

for parameter calculation - Global scale logic now entirely contained in observers (observers have references to fused weight observers for global_scale calculation)
- Removed module references from observers, simplified observer utilities
- Fixed imatrix observer synchronization in DDP and imatrix+global_scale bug
- Consolidated synchronization logic with new
`activation_statistics`

concept for activation observers and one weight observer

- Observers now have
-
**DDP Support for Activation Quantization**: Added DDP support for quantization schemes with activation quantization. Extended QuantizationModifier to support distributed activation calibration via PR[#2391](https://github.com/vllm-project/llm-compressor/pull/2391)(merged Mar 27, 2026).**Implementation**: At`SEQUENTIAL_EPOCH_END`

and`CALIBRATION_EPOCH_END`

, activation observer min/max values are all-reduced across ranks. Scale/zero-point are then recomputed from the global statistics so all ranks have identical quantization parameters.**Key Changes**:- Added
`synchronize()`

,`recompute_qparams()`

,`recompute_global_scale()`

to Observer base class - Added
`sync_activation_observers()`

to QuantizationMixin (shared by QuantizationModifier and GPTQModifier) - Batch all async
`dist.all_reduce`

operations and wait once, matching GPTQ DDP pattern

- Added
-
**DDP+GPTQ+Disk Offloading for Large Models**: Added fixes and features to enable DDP+GPTQ+disk offloading to work for very large models (e.g., Qwen3-VL-235B-A22B). Key improvements include:- Reduced shared memory overload and mmap issues for big models with DDP + CPU/disk offloading
- Fixed MoE calibration context to use same offloading as original module (previously reverted to CPU offloading causing issues)
- Only store original modules when needed to avoid mmap issues
- Added synchronization steps during model saving to prevent thread timeout issues
- Added sync points for MoE calibration context to handle NCCL timeout when different threads take varying time on large models
- Fixed NVFP4 DDP support on A100 (NCCL broadcast workaround for FP8)
- Reduced memory requirements of
`moe_calibration_context`

by removing retained module references after replacement

-
**Distributed Model Compression**: Accelerate the model compression step (bit packing) by assigning modules across ranks and compressing them in parallel, greatly reducing runtime for large models, scaling linearly with the number of GPUs available. -
**Quantization Lifecycle Refactor**: Altered quantization lifecycle so weight and activation calibration both now happen on epoch end (previously weight calibration happened at start for QuantizationModifier but end for other modifiers). Benefits include simpler code, faster runtime due to reduced on/offloading during quantization, and quantization now disabled across the board during calibration (previously modifier-dependent). -
**Microscale Calibration Refactor**: Refactored microscale formats which require fused`global_scale`

calculation. Rather than treating global scale as a generic qparam in the observer with additional post-modifications, the observer is now entirely responsible for`global_scale`

. Observers are now fused (made aware of other observers with which they share a global_scale) so they can calculate a joint global_scale. Note: this requires that all fused observers have generated statistics through their forward method. This massively simplifies global_scale handling while maintaining accuracy.

## New Model Support

-
**Qwen 3.5 and Qwen 3.6**: Calibration support has been added as part of this release with instructions summarized in the documentation for[Qwen3.5](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/qwen3.5/)and[Qwen3.6](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/qwen3.6/). Several quantized checkpoints have also been released, including: -
**Gemma 4**: Calibration support has been added with details listed in the documentation for[Gemma 4](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/gemma4/). Several quantized checkpoints have also been released, including: -
**Kimi K2.6**: This model was originally released in W4A16 packed quantized format. Decompression support has been enabled through the converters entrypoint and calibration support has also been added with details listed in the documentation for[Kimi K2.6](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/kimi-k26/). Quantized checkpoints have also been released: -
**DeepSeek-V4**: Support for quantization of DeepSeekV4 Flash and Pro models. These features are currently available via experimental branches, but are planned for integration as part of the next release of LLM Compressor. More details can be found[here](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/deepseek-v4/). Sample checkpoint:

## Converter Entrypoint (Compressed-Tensors)

-
**Model Format Conversion**: Addedentrypoint to enable decompression and conversion of models from various packed quantized formats to Compressed-Tensors format. Currently supports:`Converter`

- AutoAWQ to CT conversion
- Compressed-Tensors Decompression
- ModelOpt NVFP4 to CT Conversion
- FP8 Block Decompression (popularized by DeepSeek)

More details:

[https://docs.vllm.ai/projects/llm-compressor/en/latest/guides/entrypoints/convert/](https://docs.vllm.ai/projects/llm-compressor/en/latest/guides/entrypoints/convert/)

## Compressed Tensors

- ...

[Read more](https://github.com/vllm-project/llm-compressor/releases/tag/0.11.0)