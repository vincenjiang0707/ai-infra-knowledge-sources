# Changelog (aggregated from releases.body)

> releases: 11

## v0.1.0 (2025-08-08)

## Overview

This first public release publishes the complete initial codebase for Speculators — a unified library for building, evaluating, converting, and serving speculative decoding algorithms for LLMs. It delivers the core framework, CI/CD and developer workflow, model/config implementations (EAGLE v1/HASS/EAGLE‑3), converter CLIs from external research repos, a Hugging Face–compatible model format with vLLM serving support, and prototype training code.

## What’s New (Highlights)

- Unified, extensible framework for speculator models (build, evaluate, convert, store)
- Hugging Face–compatible speculator format with serving support landed in vLLM
- Models/configs for EAGLE v1 (HASS-style), HASS, and EAGLE‑3 (multi-layer types)
- Checkpoint converter CLIs (Eagle, Eagle‑3) from external research repositories
- Prototype training code and scripts (EAGLE‑1-style drafter, HASS) + requirements
- Production readiness: CI/CD, tests, style, docs, examples, and benchmarks

## Use Cases Enabled

- Register and configure new speculator algorithms via a standardized configuration and registry system
- Convert external checkpoints (EAGLE/EAGLE‑3/HASS variants) into the Speculators format with CLI tools
- Serve Speculators models directly in vLLM for low‑latency inference
- Evaluate and benchmark speculators (e.g., with GuideLLM), including quantized verifier swaps
- Prototype‑train drafters using provided research code and scripts

## Getting Started

- Install (Python 3.9–3.13 on Linux or macOS):
  ```bash
  pip install git+https://github.com/neuralmagic/speculators.git
  ```
- Serve with vLLM (requires v1 API):
  ```bash
  VLLM_USE_V1=1 vllm serve RedHatAI/Qwen3-8B-speculator.eagle3
  ```
- Explore examples and research: `examples/`, `research/eagle3/`, `research/hass/`

## Compatibility Notes

- Python: 3.9–3.13
- OS: Linux and macOS
- Transformers pinned to avoid mypy regressions (PR #73)
- vLLM v1 API required for serving (set `VLLM_USE_V1=1`)

---

## Full Changelog (v0.1.0)

First public release of Speculators. This release publishes the complete initial codebase and enables the first set of core use cases for speculative decoding with LLMs.

### Added

- Base configuration and registry system with tests: Speculator, Token Proposal, and Model Speculator configs; `EagleSpeculatorConfig` for EAGLE v1/HASS; config serialization/loading (PRs #26, #27, #28, #29, #34, #36)
- Eagle speculator model and support for multiple transformer layer types (PRs #37, #49)
- Eagle‑3 speculator model and Qwen support (PRs #50, #55)
- Checkpoint converter CLIs: Eagle and Eagle‑3; standardized converter interface (PRs #39, #53, #72)
- vLLM serving documentation and Qwen benchmark assets (PRs #77, #78, #82, #83)
- Examples directory and README for getting started (PR #81)
- Branding assets (icons, logos, user‑flow diagrams) (PR #87)

### Changed

- Standardized converter CLI UX and flags (PR #72)
- Documentation/readme formatting and content updates (PRs #70, #75, #83, #85)

### Fixed

- Missing embeddings in converted checkpoints/workflows (PR #65)
- CLI flags and `norm_before_residual` toggle (PRs #57, #58)
- Compatibility: pin `transformers` to resolve mypy/typing regressions (PR #73)

### CI/CD and Tooling

- GitHub Actions: migrated link checks to lychee and updated workflows (PRs #3, #45)
- PR comment behavior refinements (PR #47)

### Research and Training

- Training code for EAGLE‑1‑style drafter with multi‑step training (PR #35)
- HASS/EAGLE‑3 research updates, requirements, and DeepSpeed dependency (PRs #64, #67, #69)

### Documentation

- vLLM serving instructions, Qwen benchmark results, examples README, and research readmes (PRs #64, #70, #77, #78, #81, #83, #85)

### New Contributors

- @fynnsu made their first contribution in PR #47
- @shanjiaz made their first contribution in PR #53
- @MeganEFlynn made their first contribution in PR #55

Thanks also to continuing contributors: @markurtz, @rahul-tuli, @dsikka

### Links

- Compare changes: https://github.com/neuralmagic/speculators/compare/v0.0.1...v0.1.0


## v0.2.0 (2025-11-03)

# Speculators v0.2.0 Release Notes

### This Speculators v0.2.0 release introduces the following new features and enhancements:
- Support for Draft Models with Multiple Decoder Layers: Previously, only draft models with a single decoder layer were supported. The Eagle3 converter now sets the num_hidden_layers from the config instead of always assuming one layer.
- Added Support for eagle_aux_hidden_state_layer_ids Argument: This new argument allows users to toggle the layer IDs of the hidden state layers that are fetched during inference time. This enables support for converting Llama4 Maverick draft models to the Speculators format and running the converted model in vLLM.

### Updates and Deprecations:
- Python 3.9 Support Removed: Support for Python 3.9 has been removed and will no longer be provided. Python 3.10+ will be supported going forward.
- Default Number of Speculative Tokens Changed: The default number of speculative tokens has been changed from 5 to 3 for all Eagle and Eagle3 models.
- Override tie_weights() in Eagle3Speculator: This override prevents vocabulary corruption and supports Transformers 4.54.1.
- Updated head_dim Calculation in Eagle3 Converter: The head_dim value is now used from the config if provided; otherwise, it is calculated using the formula hidden_size // num_heads.
- Eagle3 Draft Models Retain Original Dtype: All Eagle3 draft models now keep their original dtype after being converted to the Speculators format. Previously, all converted draft models were cast to FP32.
- Extended Logic for target_vocab_size: The system defaults to using the "t2d" length, but if not available recursively search the verifier model's config file for vocab_size.
- Full End-to-End vLLM Smoke Testing: Extended and added full end-to-end vLLM smoke testing for both converted and unconverted models.

### Full Change Log
* Update README install commands now that Speculators is live on PyPi by @markurtz in https://github.com/vllm-project/speculators/pull/89
* override transformer tie_weights to prevent shape mismatch by @shanjiaz in https://github.com/vllm-project/speculators/pull/74
* [Testing][vLLM] Add vLLM Eagle3 Test Cases by @dsikka in https://github.com/vllm-project/speculators/pull/91
* Adding .readthedocs.yaml by @aireilly in https://github.com/vllm-project/speculators/pull/92
* [Tests][Eagle3] Extend vLLM test cases with conversion step by @dsikka in https://github.com/vllm-project/speculators/pull/93
* Model architectures by @anmarques in https://github.com/vllm-project/speculators/pull/90
* Fix type annotation override in SpeculatorModel.generate method by @rahul-tuli in https://github.com/vllm-project/speculators/pull/111
* Update mkdocs by @aireilly in https://github.com/vllm-project/speculators/pull/115
* Update README.md with badges by @dsikka in https://github.com/vllm-project/speculators/pull/108
* Update ReadME feature content by @dsikka in https://github.com/vllm-project/speculators/pull/109
* Fix broken links by @aireilly in https://github.com/vllm-project/speculators/pull/125
* Update README with new models and their links by @eldarkurtic in https://github.com/vllm-project/speculators/pull/135
* Fix for Eagle attention arch when head_dim is given in config.json by @eldarkurtic in https://github.com/vllm-project/speculators/pull/134
* Fix for draft models always being in fp32 datatype by @eldarkurtic in https://github.com/vllm-project/speculators/pull/136
* Fix install command for dev by @eldarkurtic in https://github.com/vllm-project/speculators/pull/137
* Fix 'test_download_with_cache_dir' by @dbarbuzzi in https://github.com/vllm-project/speculators/pull/141
* Update link checker so that it comments on existing issue by @fynnsu in https://github.com/vllm-project/speculators/pull/129
* Prevent forced casting to fp16 dtype by @eldarkurtic in https://github.com/vllm-project/speculators/pull/145
* Set default num of spec tokens to 3 by @eldarkurtic in https://github.com/vllm-project/speculators/pull/146
* Update speculator config & converter to support hidden states indexing by @shanjiaz in https://github.com/vllm-project/speculators/pull/142
* add num_hidden_layers by @shanjiaz in https://github.com/vllm-project/speculators/pull/147
* Update CI Testing by @dsikka in https://github.com/vllm-project/speculators/pull/150
* added loading util for specific layers by @shanjiaz in https://github.com/vllm-project/speculators/pull/144
* Remove PyPI publishing steps from nightly workflow by @dsikka in https://github.com/vllm-project/speculators/pull/151
* Refactor e2e tests to support external vLLM by @dbarbuzzi in https://github.com/vllm-project/speculators/pull/153
* Remove remaining python 3.9 usages by @fynnsu in https://github.com/vllm-project/speculators/pull/152
* Fix a typo in docs by @eldarkurtic in https://github.com/vllm-project/speculators/pull/107
* Added loading util tests by @shanjiaz in https://github.com/vllm-project/speculators/pull/155
* Extend E2E Tests for EAGLE3 Models by @rahul-tuli in https://github.com/vllm-project/speculators/pull/156
* Remove nightly in favour of testing repo by @dsikka in https://github.com/vllm-project/speculators/pull/159
* Remove nightly tests badge from README by @fynnsu in https://github.com/vllm-project/speculators/pull/163
* add back link-checks by @dhuangnm in https://github.com/vllm-project/speculators/pull/162
* Fix dev link checker workflow to comment directly on PRs by @markurtz in https://github.com/vllm-project/speculators/pull/164
* Only load Verifier model if attachment_mode is 'full' by @fynnsu in https://github.com/vllm-project/speculators/pull/154
* Fix EAGLE3 vLLM tests by disabling torch compile cache by @rahul-tuli in https://github.com/vllm-project/speculators/pull/166
* bump up version for last release by @dhuangnm in https://github.com/vllm-project/speculators/pull/167

## New Contributors
* @aireilly made their first contribution in https://github.com/vllm-project/speculators/pull/92
* @anmarques made their first contribution in https://github.com/vllm-project/speculators/pull/90
* @eldarkurtic made their first contribution in https://github.com/vllm-project/speculators/pull/135
* @dbarbuzzi made their first contribution in https://github.com/vllm-project/speculators/pull/141
* @dhuangnm made their first contribution in https://github.com/vllm-project/speculators/pull/162

**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.1.0...v0.2.0

## v0.3.0 (2025-12-10)

<img width="1538" height="884" alt="image (8) (1)" src="https://github.com/user-attachments/assets/ae488a12-b99d-4b60-8b86-c11c3e0f046c" />

# Speculators v0.3.0 Release Notes

This Speculators v0.3.0 release provides end-to-end training support for Eagle3 speculative decoding draft models.

Key new features include:
- Offline training data generation support using vLLM  
- Single- and multi-layer draft model training for MoE and non-MoE models  
- End-to-end scripts to generate data, train your draft model, and validate performance in vLLM  
- Examples highlighting training for Llama3, Qwen3, and gpt-oss  

## Offline Training Data Generation Support

Offline training data generation is now supported through a new hidden-states generator using vLLM. The generator provides support for MoE and non-MoE models. Vision-language support will be added in a future release.  
Generated data is saved as individual `data_{index}.pt` files. Each data point contains `input_ids`, `hidden_states`, and `loss_mask`. Along with the hidden states, a `token_freq.pt` file is also generated, containing information about token frequencies that is used to build the `target-to-draft` and `draft-to-target` vocabulary files required for training. Finally, a `data_config.json` is produced, containing metadata about the data generation process.

The hidden-states generator includes the following features:
- Multiprocess executor for efficient batch inference
- Tensor parallelism support
- Automatic KV-cache and memory management

The following scripts can be used to enable offline data generation:
- [data_generation_offline.py](https://github.com/vllm-project/speculators/blob/main/scripts/data_generation_offline.py): preprocesses data, saves token-frequency distribution, and generates hidden states  
- [build_vocab_mapping.py](https://github.com/vllm-project/speculators/blob/main/scripts/build_vocab_mapping.py): builds t2d and d2t tensors  

## Draft Model Training Support ✨

Full training support is now available for single- and multi-layer Eagle3 draft models for both Mixture of Experts (MoE) and non-MoE target models.

Training support includes:
- Updated Eagle3 draft model definitions with all features required for efficient Eagle3 model training  
- Added logic for Eagle3 algorithm's train-time-testing, now integrated into the `Eagle3DraftModel` [forward](https://docs.vllm.ai/projects/speculators/en/latest/reference/speculators/models/?h=forward#speculators.models.EagleSpeculator.forward) method. The `forward` method now supports dynamic step counts and computes per-step loss and accuracy.  
- New document-masking support enabling fast, memory-efficient Eagle3 draft model training. This approach exploits sparsity in train-time-test attention masks, providing faster performance and lower memory usage compared to a naive full attention matrix.  

The following script can be used for training:
- [train.py](https://github.com/vllm-project/speculators/blob/main/scripts/train.py)

## End-to-End Scripts and Examples

### New E2E script for data generation and training speculative draft models

A summary of the new scripts added to run each of the individual steps in the workflow is listed below:
1. [Generate training data offline](https://github.com/vllm-project/speculators/blob/main/scripts/data_generation_offline.py)  
2. [Build Vocab Mapping](https://github.com/vllm-project/speculators/blob/main/scripts/build_vocab_mapping.py)  
3. [Training](https://github.com/vllm-project/speculators/blob/main/scripts/train.py)  

A [new end-to-end script](https://github.com/vllm-project/speculators/blob/main/scripts/gen_and_train.py) has also been added that runs the full workflow mentioned above under a single configuration. The script provides a simplified interface for configuring a full training run that can be launched once. Internally, the script runs each step of the process and ensures data flows correctly from one step to the next. 

Training examples have been added for Llama3, Qwen3, and gpt-oss:
1. [llama3_8b_sharegpt_5k.py](https://github.com/vllm-project/speculators/blob/main/examples/data_generation_and_training/llama3_8b_sharegpt_5k.py)  
2. [gpt_oss_20b_ultrachat_5k.py](https://github.com/vllm-project/speculators/blob/main/examples/data_generation_and_training/gpt_oss_20b_ultrachat_5k.py)  
3. [qwen3_8b_sharegpt_ultrachat.py](https://github.com/vllm-project/speculators/blob/main/examples/data_generation_and_training/qwen3_8b_sharegpt_ultrachat.py)

## Testing and validation

### New vLLM benchmarking framework

A new automated evaluation framework that benchmarks Eagle3 speculator models using vLLM and GuideLLM has been added.  
Preconfigured evaluation configurations are available for the following models:

- Llama-3.1-8B  
- Llama-3.3-70B  
- gpt-oss-20B  
- Qwen3-8B  
- Qwen3-32B  

The framework can be reviewed in the [examples/evaluate/eval-guidellm](https://github.com/vllm-project/speculators/tree/main/examples/evaluate/eval-guidellm) folder.

To run an evaluation:

```cmd
./run_evaluation.sh -c configs/llama-3.1-8b-eagle3.env
```

This command automatically handles vLLM server startup, runs GuideLLM benchmarks, extracts acceptance-rate metrics from logs, and cleans up when complete.

The framework supports multiple dataset types, including HuggingFace datasets with colon syntax for specific files (e.g., org/dataset:file.jsonl), local files, and directories. It includes modular bash scripts following best practices, with proper error handling and process management, configurable sampling parameters (temperature, top_p, top_k), and outputs detailed metrics including weighted per-position acceptance rates and conditional acceptance probabilities.

Configuration precedence for the evaluation run is as follows and can be easily changed:

1. CLI arguments
2. Config file
3. Framework defaults

## Deprecations 

Previously supported training code under `research` has been removed. 

## New Contributors
* @SwekeR-463 made their first contribution in https://github.com/vllm-project/speculators/pull/212

**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.2.0...v0.3.0

## v0.4.0 (2026-03-04)

<img width="1794" height="1234" alt="Screenshot 2026-03-04 at 2 08 17 PM" src="https://github.com/user-attachments/assets/ca09d63f-6753-4a20-97ac-9b35fcda6448" />

# Speculators v0.4.0 Release Notes

This release expands the Speculators framework with enhanced algorithm flexibility, improved model support, and critical bug fixes. Key additions include response regeneration capabilities for on-policy training, extensible architecture supporting multiple speculative decoding algorithms beyond Eagle3, comprehensive Vision Language model integration, and updated infrastructure dependencies including PyTorch 2.10 and vLLM v0.16.0.

## Key Features

- **Response Regeneration Scripts**: New scripts enable on-policy training workflows by regenerating model responses for question-answer and chat-style datasets using vLLM
- **Extensible Algorithm Framework**: Training infrastructure generalized to support multiple speculative decoding algorithms beyond Eagle3 through registry-based architecture
- **Vision Language Model Support**: Complete training pipeline and speculative decoding support for Vision Language models, including MoE variants
- **PyTorch 2.10 Compatibility**: Framework updated to support PyTorch 2.10 for latest performance optimizations
- **Normalization Layer Fix**: Critical bug resolved, improving acceptance rates on gpt-oss-20b from 25% to 40%
- **Enhanced Evaluation Framework**: Configurable base models and speculative decoding parameters with explicit model separation

## Detailed Features

**Response Regeneration Scripts**

The update introduces response regeneration capabilities to facilitate on-policy training workflows. Draft model performance improves substantially when training on responses generated by the target model itself rather than pre-existing dataset responses. 

To enable this workflow, new scripts are available in the [response_regeneration](https://github.com/vllm-project/speculators/tree/main/scripts/response_regeneration) directory that regenerate model responses for question-answer and chat-style datasets using vLLM. Complete usage documentation and examples are provided in the accompanying README within the same directory.

**Extensible Algorithm Framework**

The training infrastructure has been generalized to support multiple speculative decoding algorithms beyond Eagle3. This architectural refactoring introduces a registry-based pattern using `@register` decorators, allowing algorithms to own their training logic through classmethods. The implementation adds a new `base_components.py` module providing shared transformer definitions for Llama and Qwen3 architectures, while removing algorithm-specific hardcoded values from core training utilities. Users can now specify `--speculator-type` as the main argument to `train.py`, with the training script dynamically looking up the corresponding model class in the registry. This design eliminates code duplication and enables new algorithms such as DFlash and FastMTP (both coming soon) to integrate without modifying core training infrastructure. Developer documentation is available [here](https://docs.vllm.ai/projects/speculators/en/latest/algorithms/add_new_algorithms/) with detailed implementation guidance.

**Vision Language Model Support**

Comprehensive support for Vision Language models has been integrated across the training pipeline. The framework now includes data generation capabilities, full training support for both standard and Mixture-of-Experts (MoE) architectures, and speculative decoding inference support in vLLM. Users can generate training data and train vision language models directly within Speculators, with MoE variants supported for production deployment with speculative decoding acceleration.

With this functionality, a [Qwen3-VL-235B-A22B-Instruct speculator was trained and released](https://huggingface.co/RedHatAI/Qwen3-VL-235B-A22B-Instruct-speculator.eagle3).

**PyTorch 2.10 Compatibility**

The framework has been updated to support PyTorch 2.10, enabling users to leverage the latest performance optimizations and enhanced training capabilities from this release.

**vLLM v0.16.0 Integration**

Data generation support has been updated to vLLM v0.16.0, ensuring compatibility with the latest vLLM features and performance improvements for hidden-state generation.

## Improvements and Fixes

**Normalization Layer Correction**

A critical bug in the Eagle3 model architecture has been resolved. The original research code applied a final layer normalization before the language model head, but vLLM-based data generation omitted this step, causing training targets to be computed incorrectly. This was particularly impactful on gpt-oss models. The fix introduces a `verifier_norm` layer in Eagle3DraftModel to apply normalization before the language model head, properly loading the final normalization weights from the verifier model. Results demonstrate substantial performance improvements, with acceptance rates for gpt-oss-20b on math reasoning tasks improving from 25% to 40% even when trained on a small 20k sample ultrachat dataset. The `data_format_version` parameter has been removed, and a new `embed_requires_grad` configuration option controls whether embedding layer weights update during training.

**Enhanced Evaluation Framework**

The evaluation framework has been restructured to support configurable base models and speculative decoding parameters. The command structure now uses separate `-b BASE_MODEL -s SPECULATOR_MODEL` flags instead of a single model parameter, with added `--num-spec-tokens` (default: 3) and `--method` (default: eagle3) parameters for flexible testing. All environment configuration files have been updated with explicit base/speculator model pairs. Users can now test different base models against the same speculator and easily adjust speculation depth to optimize speed/accuracy tradeoffs, while explicit model separation clarifies the architecture.

**Exact Sample Length Tracking**

The training data pipeline now implements exact sample length tracking. Previously, sequence lengths were estimated by comparing file sizes, which occasionally produced inaccurate results with approximately 10% failure rates for large datasets. The data generation script now collects sample lengths and stores exact sequence lengths in a `sample_lengths.json` file alongside generated data. The dataloader first attempts to load exact lengths from this file when available, falling back to the original file-size approximation method for backward compatibility with existing datasets.

**Full Verifier Vocabulary Support**

The `t2d` and `d2t` tensor parameters in Eagle3DraftModel are now optional, allowing training with either limited vocabulary mappings or the full verifier vocabulary. When vocabulary mapping paths are not provided, the training script loads the verifier configuration and uses its full vocabulary size.

## New Contributors
* @momo609 made their first contribution in https://github.com/vllm-project/speculators/pull/232
* @Vishnu-sai-teja made their first contribution in https://github.com/vllm-project/speculators/pull/262
* @gDINESH13 made their first contribution in https://github.com/vllm-project/speculators/pull/261
* @svlandeg made their first contribution in https://github.com/vllm-project/speculators/pull/289
* @guan404ming made their first contribution in https://github.com/vllm-project/speculators/pull/291
* @VincentG1234 made their first contribution in https://github.com/vllm-project/speculators/pull/317

**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.3.0...v0.4.0

## v0.4.0.1 (2026-03-26)

## What's Changed
* Minor update to allow hotfix for 0.4.0.1. by @dhuangnm in https://github.com/vllm-project/speculators/pull/357
* Fix conversion error by @shanjiaz in https://github.com/vllm-project/speculators/pull/359
* reconfigure run_vllm by @shanjiaz in https://github.com/vllm-project/speculators/pull/363


**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.4.0...v0.4.0.1

## v0.5.0 (2026-04-24)

<img width="2528" height="1684" alt="speculatorv0 5 0" src="https://github.com/user-attachments/assets/f2420575-76e9-46c5-9ef2-0911b811316b" />

# Speculators v0.5.0 Release Notes

This Speculators v0.5.0 release adds support for the DFlash algorithm, online training, and unifies all data generation — both online and offline — under vLLM's hidden states extraction system. Documentation has been expanded with end-to-end tutorials for all supported training workflows.

Key new features include:

*   DFlash algorithm training support
*   Full online training support
*   Both online and offline training now use vLLM's native hidden states extraction system
*   New tutorials for model serving, E2E online & offline Eagle 3 training, and E2E online DFlash training

## DFlash Training Support ✨

Speculators now supports training [DFlash](https://arxiv.org/abs/2602.06036) speculative decoding draft models. Unlike Eagle 3, which generates draft tokens autoregressively across multiple forward passes, DFlash uses a block diffusion approach to generate an entire block of draft tokens in a single forward pass. This parallel drafting reduces inter-token latency compared to Eagle 3.

Training support includes a new DFlash model definition, config, and associated training examples. The trainer has been updated to accept DFlash-specific arguments, and attention utilities are now shared across Eagle 3 and DFlash.

With this, a [Gemma 4 DFlash speculator](https://huggingface.co/RedHatAI/gemma-4-31B-it-speculator.dflash) was released, showing the following per-position acceptance rates:

| Dataset | Position 0 | Position 1 | Position 2 | Position 3 | Position 4 | Position 5 | Position 6 | Position 7 | Acceptance Length |
|---|---|---|---|---|---|---|---|---|---|
| HumanEval | 85.8% | 72.1% | 60.3% | 50.4% | 41.8% | 34.3% | 26.9% | 19.6% | 4.91 |
| Math Reasoning | 88.7% | 76.1% | 64.8% | 54.9% | 45.5% | 36.5% | 28.8% | 21.5% | 5.17 |

Gemma 4 DFlash achieves better inter-token latency than both Eagle 3 and a standalone FP8 quantized verifier. Combining DFlash with an FP8 quantized verifier yields even greater gains, as shown below:

<img width="2144" height="1334" alt="Screenshot 2026-04-19 at 4 31 20 PM (1)" src="https://github.com/user-attachments/assets/a396d18a-090a-460f-86b3-d8d246147eb8" />


## Hidden States Extraction System Integration

As of v0.5.0, both online and offline training in Speculators use vLLM's native hidden states extraction system. This is a significant unification: previously, offline data generation used a separate Speculators-managed system, and online training was not supported at all.

vLLM's [hidden states extraction system](https://vllm.ai/blog/extract-hidden-states), introduced in vLLM v0.18.0, provides a native way to extract intermediate model representations during inference. It routes hidden states through vLLM's existing speculative decoding pathway via a dummy draft model, storing them in a dedicated KV cache and exporting them via a custom KV Connector API. This design reuses vLLM's existing infrastructure — including tensor parallelism, prefix caching, and paged memory management — with minimal overhead on standard inference.

**Offline training** has been migrated to this system. It is more performant, better integrated with vLLM, and eliminates the risk of divergence between training and serving behavior that existed with the previous Speculators-managed data generation system.

**Online training** is now supported for the first time in this release. Speculators can train directly on live hidden states generated on-the-fly — eliminating the need to pre-cache training data entirely. This also enables hybrid training approaches combining online and offline data.

The online training workflow:

1.  [Response regeneration](https://github.com/vllm-project/speculators/tree/main/scripts/response_regeneration) — regenerate target model responses
2.  [prepare\_data.py](https://github.com/vllm-project/speculators/blob/main/scripts/prepare_data.py) — tokenize and format data
3.  [launch\_vllm.py](https://github.com/vllm-project/speculators/blob/main/scripts/launch_vllm.py) — launch the vLLM server
4.  [train.py](https://github.com/vllm-project/speculators/blob/main/scripts/train.py) — extract hidden states and train

## Documentation Updates

The [Speculators documentation](https://docs.vllm.ai/projects/speculators/en/latest/) has been refreshed to reflect the updated hidden states system and show up-to-date usage across all training flows.

New [tutorials](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/tutorials/) have been added covering the main usage workflows:

*   [Model serving](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/tutorials/serve_vllm/)
*   E2E [online](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/tutorials/train_eagle3_online/) & [offline](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/tutorials/train_eagle3_offline/) training with Eagle3 models
*   [E2E online training with DFlash models](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/tutorials/train_dflash_online/)

## Updated Examples

Training examples have been added for Eagle3 and DFlash:

*   [dflash\_qwen3\_8b\_sharegpt\_online\_5k.sh](https://github.com/vllm-project/speculators/blob/main/examples/train/dflash_qwen3_8b_sharegpt_online_5k.sh) — Online DFlash training with Qwen3-8B on ShareGPT
*   [eagle3_llama3_8b_ultrachat_offline_5k.sh](https://github.com/vllm-project/speculators/blob/main/examples/train/eagle3_llama3_8b_ultrachat_offline_5k.sh) — Offline Eagle3 training with Llama3-8B on UltraChat
*   [eagle3\_qwen3\_8b\_sharegpt\_online\_5k.sh](https://github.com/vllm-project/speculators/blob/main/examples/train/eagle3_qwen3_8b_sharegpt_online_5k.sh) — Online Eagle3 training with Qwen3-8B on ShareGPT

## Other Updates

*   Updated to support transformers v5.6
*   Updated to support torch 2.11

## Deprecations

The data generation system previously supported through Speculators v0.3.0 has been deprecated and removed as of v0.5.0. The old system required a vLLM dependency which has also been removed. All training flows are now supported through vLLM's hidden states extraction system.

## New Contributors
* @shubhra made their first contribution in https://github.com/vllm-project/speculators/pull/337
* @benchislett made their first contribution in https://github.com/vllm-project/speculators/pull/346
* @surojitiitg made their first contribution in https://github.com/vllm-project/speculators/pull/334

**Full Changelog**: [v0.4.0.1...v0.5.0](https://github.com/vllm-project/speculators/compare/v0.4.0.1...v0.5.0)

## v0.6.0 (2026-06-16)

<img width="2752" height="1536" alt="image (13)" src="https://github.com/user-attachments/assets/b237f595-5ce3-4f9c-a3ff-a64295429595" />
Speculators v0.6.0 release significantly expands Speculators' algorithm coverage and training capabilities. This release introduces P-EAGLE parallel eagle algorithm, Multi-Token Prediction (MTP) finetuning support, multi-modal dataset training, and a comprehensive performance benchmarking suite. Alongside these headline features, v0.6.0 delivers important improvements to DFlash including sliding window attention and a wide range of training infrastructure enhancements.

## Key features include:
- MTP finetuning support: Finetune native MTP heads  
- P-EAGLE algorithm support: Parallel multi-token prediction with Conditional Drop-token(COD) sampling
- DFlash sliding window attention: Reduced KV cache usage for long-context sequences
- Multi-modal dataset training: Train speculators on datasets containing images and other modalities
- GuideLLM-based performance benchmarking suite
- Multi-node offline data generation

# P-EAGLE Support 

Speculators v0.6.0 adds support for the P-EAGLE (Parallel EAGLE) algorithm, a new state-of-the-art approach for speculative
decoding. We have released a Qwen3-8B P-EAGLE model. This implementation extends our existing EAGLE3 foundation with sophisticated parallel pattern support and loss-mask aware sampling.

## Key Technical Components

The P-EAGLE implementation introduces several key components:

- Model Architecture: New P-EAGLE model and configuration classes that inherit from EAGLE3, providing a familiar API while enabling parallel speculative patterns.
- Loss-Mask Aware COD Sampling: Basic implementation of Context-Oriented Decoding (COD) sampling that respects loss masking for improved generation quality.
- Mask Embeddings: Integrated mask embeddings into the P-EAGLE model architecture for handling masked tokens during parallel speculation.
- Parallel Attention Patterns: Attention mask construction using flex attention to support parallel speculation patterns efficiently.
- Position-Based Loss Masking: Loss mask updates for masked tokens using position IDs, ensuring correct gradient flow during training.
- Cross-Entropy Loss Option: Added cross-entropy loss function as an alternative training objective in the training script for improved flexibility.
- vLLM Integration: P-EAGLE models now support simplified serving via vllm serve <peagle-speculators-model> with automatic configuration extraction from config.json.

This implementation enables users to leverage the latest advances in parallel speculative decoding while maintaining compatibility with the existing Speculators framework.

Acceptance rates matrix for the [Qwen3-8B P-EAGLE](https://huggingface.co/RedHatAI/Qwen3-8B-speculator.peagle) model:

| Dataset | Pos 0 | Pos 1 | Pos 2 | Pos 3 | Pos 4 | Pos 5 | Pos 6 | Avg. Length |
|---------|-------|-------|-------|-------|-------|-------|-------|-------------|
| HumanEval | 81.30% | 59.00% | 41.10% | 27.90% | 18.80% | 12.80% | 8.90% | 3.5 |
| math_reasoning | 83.30% | 63.50% | 47.00% | 34.30% | 24.40% | 17.20% | 11.80% | 3.82 |
| qa | 70.50% | 44.70% | 27.60% | 17.10% | 10.80% | 7.10% | 4.80% | 2.83 |
| question | 74.60% | 49.60% | 31.60% | 20.20% | 13.10% | 8.50% | 5.60% | 3.03 |
| rag | 73.60% | 48.40% | 29.80% | 18.40% | 11.30% | 6.90% | 4.10% | 2.93 |
| summarization | 68.00% | 39.00% | 21.00% | 10.80% | 5.40% | 2.60% | 1.20% | 2.48 |
| tool_call | 73.70% | 47.60% | 28.70% | 17.10% | 10.30% | 6.20% | 3.70% | 2.87 |
| translation | 73.80% | 47.70% | 28.70% | 17.30% | 10.40% | 6.50% | 4.10% | 2.89 |
| writing | 75.00% | 50.00% | 32.10% | 20.60% | 13.30% | 8.70% | 5.70% | 3.05 |

## Example Usage

See our P-EAGLE Qwen3-8B training [example](https://github.com/vllm-project/speculators/blob/main/examples/train/peagle_qwen3_8b_sharegpt_online_5k.sh) for a complete training script.

# MTP Algorithm Support

Speculators now supports finetuning MTP (Multi-Token Prediction) speculator heads. Unlike Eagle-3, DFlash, and P-EAGLE, which train draft models from scratch, MTP finetuning starts from a model's native MTP
head, extracting its pre-trained weights, finetuning on domain-specific data, and stitching the improved weights back into the original checkpoint for deployment.

Only the MTP layers are trained; `embed_tokens` and `lm_head` remain frozen and shared with the verifier. The approach follows the FastMTP method from Tencent, using exponential-decay loss weighting across
speculative steps.

Training support includes a new MTP model definition, config, converter, and weight stitcher. Native MTP weights are automatically extracted from the verifier during training initialization, so no separate
conversion step is needed. The trainer has been updated to accept MTP-specific arguments, and the full pipeline runs end-to-end in under 8 minutes for Qwen3.5-9B on 2× H200 GPUs.

## Finetuning Results

Finetuning Qwen3.5-9B on GSM8K with 3 speculative steps:

| Metric | Position 0 | Position 1 | Position 2 | Acceptance Length |
|--------|-----------|-----------|-----------|-------------------|
| Acceptance Rate | 89.36% | 72.34% | 61.70% | 3.23 |

On Qwen3-Next-80B-A3B, mean accepted tokens improved +22.5% (2.01 → 2.46) after 1 epoch on GSM8K.

After training, `stitch_mtp.py` merges the finetuned weights back into the verifier checkpoint for deployment with vLLM's native MTP speculative decoding.

## Resources

See the following resources to get started:

- **Algorithm overview**: https://docs.vllm.ai/projects/speculators/en/latest/user_guide/algorithms/mtp/
- **Online training tutorial**: https://docs.vllm.ai/projects/speculators/en/latest/user_guide/tutorials/train_mtp_online/
- **Example script**: https://github.com/vllm-project/speculators/blob/main/examples/train/mtp_qwen3_5_9b_gsm8k_online.sh

# DFlash Sliding Window Attention

Speculators v0.6.0 adds sliding window attention support for DFlash speculators, enabling more efficient long-context handling by reducing KV cache allocation compared to full attention.

The sliding window implementation introduces:

- **Configurable Window Size**: New CLI arguments (`--sliding-window`, `--sliding-window-indices`, `--sliding-window-non-causal`) allow per-layer attention configuration with a default window size of 2048
tokens (set to 0 for full attention).
- **Hybrid Attention Patterns**: Support for mixing sliding window and full attention layers within a single model, allowing fine-grained control over the attention-efficiency tradeoff at each layer.
- **Enhanced Masking**: Updated `create_anchor_block_mask_mod` to enforce sliding window visibility constraints with support for both causal and non-causal intra-block masking on sliding window layers.
- **Model Integration**: Extended `DFlashSpeculatorConfig` and `DFlashDraftModel` to handle sliding window parameters with per-layer mask selection during the forward pass.

This feature enables DFlash speculators to scale more efficiently to long-context scenarios while maintaining flexibility through the hybrid attention approach

# Asynchronous Writes Support

Speculators v0.6.0 adds support for asynchronous hidden states extraction, maintaining compatibility with vLLM's recent updates (#37374) to its hidden states writing system which landed in vLLM v0.22.0.

vLLM now writes hidden states to disk asynchronously and uses lock files to signal when hidden states files are ready for consumption. The Speculators extraction system has been updated to:

- **Lock File Handling**: Correctly detect and interpret lock files to determine hidden states availability.
- **Blocking Read Operations**: Wait for hidden states to be fully written before attempting to read, preventing incomplete or corrupted data from being processed.

This update ensures seamless integration with vLLM's asynchronous hidden states writing pipeline, enabling more efficient hidden states collection during training data preparation.

# Performance Benchmarking Suite

Speculators v0.6.0 adds a unified evaluation suite based on GuideLLM, replacing the previous evaluation pipeline with the tooling actively used by our research team. This new system provides comprehensive
performance analysis through two complementary measurement approaches.

## Key Features

The evaluation suite introduces:

- **Acceptance Metrics Monitoring**: Direct integration with the vLLM server's Prometheus endpoint to measure per-position acceptance rates in real time, providing granular insights into speculator
effectiveness at each decoding step.
- **End-to-End Performance Benchmarking**: GuideLLM-powered benchmarks across nine evaluation subsets with automatic output length estimation for each subset. The suite sweeps across request rates to
measure:
    - Latency
    - Throughput
    - Time to First Token (TTFT)
    - Inter-Token Latency (ITL)
- All metrics are captured at different load levels to provide a complete performance profile.
- **Visualization Tools**: New plotting utilities enable overlay comparisons of multiple model versions and pairwise speedup analysis with gradient colormaps for easy identification of performance
improvements.

This evaluation framework aligns the Speculators project with current research workflows and provides more actionable performance insights for both development and production deployments.

## Example Usage

See our [Qwen 3 8B DFlash HumanEval evaluation example](https://github.com/vllm-project/speculators/blob/main/examples/eval/qwen3_8b_dflash_humaneval.sh) and the complete [evaluation 
module](https://github.com/vllm-project/speculators/tree/main/speculators/eval) for more details.

# Training Infrastructure Improvements

- Multi-Node Offline Data Generation
- Async Hidden States Connector
- Graceful Shutdown on Interrupt
- Sub-Epoch Checkpointing
- Configurable Loss Function
- Dataset Support Enhancements


## New Contributors
* @DarkLight1337 made their first contribution in https://github.com/vllm-project/speculators/pull/495
* @Ryfernandes made their first contribution in https://github.com/vllm-project/speculators/pull/552
* @christinaexyou made their first contribution in https://github.com/vllm-project/speculators/pull/542
* @aman-source made their first contribution in https://github.com/vllm-project/speculators/pull/528
* @adelnobel made their first contribution in https://github.com/vllm-project/speculators/pull/561
* @SuperMarioYL made their first contribution in https://github.com/vllm-project/speculators/pull/562
* @coolthor made their first contribution in https://github.com/vllm-project/speculators/pull/527

**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.5.0...v0.6.0

## v0.7.0 (2026-07-30)

<img width="1536" height="1024" alt="spec_simple_v07" src="https://github.com/user-attachments/assets/ba302642-1ea6-45c6-bf8e-8b3d6234a3f4" />

Speculators v0.7.0 introduces the DSpark algorithm, a config-file-first training CLI, an expanded loss function library, DDP training with updated mixed precision, and broad improvements to training infrastructure and performance. This release also extends sliding window attention to Eagle3 and P-EAGLE, adds tool-call and multi-turn support to on-policy response regeneration, adds support for more loss functions, and makes Muon the default optimizer.

Note: For failures with this version and vLLM 0.27.0/0.27.1, consider using vLLM nightly or downgrading to v0.26.0

## Key Features:

- DSpark algorithm support: DFlash + Markov logit-bias head + per-position confidence head
- Config-file-first training CLI with typed YAML configuration
- Expanded loss library: D-PACE, TV, JSD, RKL, Negative Log-Acceptance, and Hybrid LK
- DDP as the default distributed backend with torch.autocast mixed precision
- Sliding window attention extended to Eagle3 and P-EAGLE
- Tool-call and multi-turn on-policy response regeneration
- Muon optimizer as the default
- NVIDIA SPEED-Bench evaluation support
- Mistral training support
- Partial MRoPE support for draft model training
- Multi-turn and tool call response regeneration


## DSpark Algorithm Support

Speculators v0.7.0 adds support for [DSpark](https://arxiv.org/abs/2607.05147), a new speculator type that extends DFlash with a low-rank Markov logit-bias head for intra-block token dependency, a per-position confidence head, and a TV-dominant training loss. Running DFlash with the heads disabled (--markov-rank 0) reproduces standard DFlash behavior.
Key Components

1. Markov Logit-Bias Head: Models sequential token dependencies within a draft block
```
--markov-head-type vanilla
--markov-head-type gated
--markov-head-type rnn
```
2. Per-Position Confidence Head: Predicts acceptance probability at each draft position.
Optionally incorporates the Markov embedding with:
```
--confidence-head-with-markov
```
3. Sample-from-Anchor: A new --sample-from-anchor mode where every block position, including slot, produces predictions. This matches the DSpark author’s implementation, while disabling this feature aligns with the DFlash implementation (and can be useful if finetuning a DSpark model from a DFlash checkpoint).

Example:
```
scripts/train.py \
    --speculator-type dspark \
    --markov-rank 256 \
    --markov-head-type vanilla \
    --enable-confidence-head \
    --verifier-name-or-path Qwen/Qwen3-8B \
    --data-path ./data \
    --save-path ./ckpt
```

With this, we released [RedHatAI/GLM-5.2-speculator.dspark](https://huggingface.co/RedHatAI/GLM-5.2-speculator.dspark) and [RedHatAI/gemma-4-31B-it-speculator.dspark](https://huggingface.co/RedHatAI/gemma-4-31B-it-speculator.dspark), they provide significant performance gains when compared to autoregressive drafting algorithms such as EAGLE-3.

<img width="1016" height="635" alt="Screenshot 2026-07-30 at 11 45 28 AM" src="https://github.com/user-attachments/assets/61d43bdb-a2f4-4d03-b1c6-8ebae2c13834" />

## Config-File-First Training CLI

The handwritten argparse interface in scripts/train.py has been replaced with a typed, layered configuration system built on pydantic-settings.

### Features

- ```--config PATH```
   -  Load a YAML configuration file.
    - Precedence: command-line flag > YAML > default.
- ```--dump-config```
   - Prints the fully resolved configuration as a round-trippable run.yaml and exits.
- Reproducibility
    - Every run writes run.yaml and train_command.txt alongside checkpoints.
- Grouped Help
   - Help is organized into General, Verifier, Draft, Data, Loss, Optimizer, Scheduler, Trainer, and algorithm-specific groups (DFlash, DSpark, P-EAGLE, MTP).

All existing flag-based training recipes continue to work unchanged.


## Expanded Loss Function Library

### D-PACE (Dynamic Position-Aware Cross-Entropy)
https://arxiv.org/abs/2605.18810

- Dynamically shifts per-position loss weights toward later positions as earlier positions stabilize.
- Achieves approximately 5% higher mean accepted length compared to fixed-decay cross-entropy.
- Enable with ```--per-position-loss-weight dpace.```

### Additional Losses

- Total Variation (TV) with a Triton-fused kernel for long-context efficiency
- Jensen-Shannon Divergence (JSD)
- Reverse KL (RKL)
- Negative Log-Acceptance (LK)
- Hybrid LK

### EAL Metric
Expected Accepted Length (EAL) is now available as a training evaluation metric.

### Composable Losses
```--loss-fn '{"ce": 0.1, "tv": 0.9}'```

## DDP Training + Updated AMP

The default distributed backend has changed from FSDP to DDP.

- ```--fsdp-shard``` remains available as an opt-in option.
- Master weights remain in FP32.
- torch.autocast manages reduced precision during forward and backward passes.
- Precision-sensitive layers are handled automatically. 

## Sliding Window Attention for Eagle3 and P-EAGLE

Sliding window attention now extends beyond DFlash to Eagle3 and P-EAGLE.

- Prevents sharp acceptance-rate drops on long-context requests.
- Default sliding window size is 2048 tokens.
- Enabled by default for all draft layers in DFlash and DSpark.
- ```--full-attention-indices allows selective overrides.```

## Tool-Call and Multi-Turn Response Regeneration

### Tool-Call Regeneration

- Tool-call tokens are regenerated on-policy.
- Cached tool results are spliced back positionally.

### Multi-Turn Regeneration

- Every user turn is regenerated using the newly generated conversation prefix.
- System prompts remain unchanged.
- Each assistant turn receives its own reasoning_content.

### New Dataset Presets

- Hermes function-calling dataset
- Open-PerfectBlend dataset

## Muon Optimizer as Default

Muon is now the default optimizer.
Validation shows improved performance over Adam for decoder-only (Qwen3-8B) and MoE models.

- Muon applies to 2D weight matrices.
- AdamW automatically handles norms, biases, embeddings, and lm_head.

## Training Infrastructure Improvements

- Sub-epoch checkpointing (--checkpoint-freq 0.5)
- Scheduler warmup ratio (--scheduler-warmup-ratio)
- prepare-data safety and correctness improvements (RFC #583)
- Step-level performance profiling
- Configurable train/validation split (--train-data-ratio)
- Restored --max-steps
- Batch validation metric reduction (one synchronization per epoch)
- Fused hidden-state dtype casting during collate copy
- MLflow metric handler
- Refactored hidden-state transfer with abstract backend
- On-policy (regenerated) data recommended as the default training strategy
- Dry run(--dryrun) produce a mock checkpoint with expected config.json and randomized weights, useful to test if the checkpoint runs correctly in vLLM

## DFlash Performance Improvements

- Sorted sampled anchors for contiguous FlexAttention blocks (~3× training speedup)
- Compiled create_block_mask to avoid dense mask materialization
- Compute verifier targets only at anchored positions
- Divergence losses computed in float32 during BF16 training for improved numerical stability
- Evaluation Improvements
- NVIDIA SPEED-Bench support in evaluate.py
- GuideLLM upgraded from 0.6.0 to 0.7.1
- Simple benchmarking script for quick acceptance-rate evaluation
- Other Notable Changes
- Mistral model training support
- Partial MRoPE support for draft model training
- Device-agnostic synchronization via torch.accelerator.synchronize()
- Default drafter architecture changed from Llama to Qwen3
- Reduced torch.compile graph breaks and recompilations
- Added CODEOWNERS and required reviewer approvals

## Bug Fixes

- fix(mtp): Pin static shapes for compiled MTP forward to prevent torch.compile crashes across PyTorch versions.
- fix(train): Fixed DSpark + FSDP2 + Muon crash.
- fix(train): Prevent double reduction of aliased metric tensors in distributed training.
- fix(train): Balance sampler sample counts and bound validation rank skew.
- fix(dspark): Correct position-0 decay weight and Markov bigram alignment for sample_from_anchor.
- fix(loss): Compute divergence losses in float32 under BF16 training.
- fix(eagle3): Always teacher-force TTT tokens.
- fix(regen): Stable --resume identity and request retries.
- fix: Apply --draft-attn-impl when loading with --from-pretrained.


## New Contributors
* @Sawyer117 made their first contribution in https://github.com/vllm-project/speculators/pull/589
* @menogrey made their first contribution in https://github.com/vllm-project/speculators/pull/600
* @olisicky made their first contribution in https://github.com/vllm-project/speculators/pull/300
* @deepak-kumar-neu made their first contribution in https://github.com/vllm-project/speculators/pull/608
* @qq1060 made their first contribution in https://github.com/vllm-project/speculators/pull/630
* @imargulis made their first contribution in https://github.com/vllm-project/speculators/pull/618
* @GIREESH7963 made their first contribution in https://github.com/vllm-project/speculators/pull/648
* @WindChimeRan made their first contribution in https://github.com/vllm-project/speculators/pull/627
* @mgoin made their first contribution in https://github.com/vllm-project/speculators/pull/677
* @KKothuri made their first contribution in https://github.com/vllm-project/speculators/pull/675
* @dmasloff made their first contribution in https://github.com/vllm-project/speculators/pull/709
* @omerap12 made their first contribution in https://github.com/vllm-project/speculators/pull/722
* @jessiewei7 made their first contribution in https://github.com/vllm-project/speculators/pull/743
* @weifanjiang made their first contribution in https://github.com/vllm-project/speculators/pull/736
* @PatchouliTIS made their first contribution in https://github.com/vllm-project/speculators/pull/733
* @weianlin05 made their first contribution in https://github.com/vllm-project/speculators/pull/759
* @Frozen7771 made their first contribution in https://github.com/vllm-project/speculators/pull/755
* @minziyu made their first contribution in https://github.com/vllm-project/speculators/pull/798
* @CarterDuan made their first contribution in https://github.com/vllm-project/speculators/pull/806
* @soyr-redhat made their first contribution in https://github.com/vllm-project/speculators/pull/766

**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.6.0...v0.7.0

## v0.6.0.1 (2026-08-12)

## What's Changed
* [Hotfix 0.6.0.1] fix NFS flock issue by @dhuangnm in https://github.com/vllm-project/speculators/pull/946


**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.6.0...v0.6.0.1

## v0.7.0.1 (2026-08-13)

## What's Changed
* [Hotfix 0.7.0.1] fix NFS flock issue by @dhuangnm in https://github.com/vllm-project/speculators/pull/947
* ci(quality): run Quality workflow on release-* branches by @dsikka in https://github.com/vllm-project/speculators/pull/950


**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.7.0...v0.7.0.1

## v0.8.0 (2026-09-03)

<img width="1536" height="1024" alt="spec_v08" src="https://github.com/user-attachments/assets/30d3dab4-5bbf-4af2-b86c-3d7ccceb542b" />

# Speculators v0.8.0

This release builds on the v0.7.0 DSpark/DFlash foundation with a unified `speculators` CLI, first-class Mooncake / hidden-state connectors (now published to PyPI), a fused Triton loss kernel for lower-memory training, experimental DFlash2 support, and broad hardening across the data-generation, preprocessing, and evaluation pipelines.

## Key Features

- Unified `speculators` CLI consolidating response regeneration, preprocessing, and online/offline training entry points.
- Mooncake hidden-state extraction backend and standalone `hs-connectors` package, now installable from PyPI.
- Memory-efficient training through a single fused Triton online-softmax loss kernel.
- Experimental DFlash2 training and checkpoint support.
- Laguna warm-start support with DFlash weight remapping.
- Reproducibility artifacts for evaluation runs, including `eval_command.txt` and vLLM launch metadata.
- More robust data pipelines, including NaN skipping, pre-tokenized dataset support, hidden-state validation, and recovery from generation failures.

## Unified Speculators CLI

A single `speculators` CLI now provides a consolidated interface for training and related workflows.

- Consolidated response regen, preprocessing, and training workflows.
- Migrated all training example scripts to the unified CLI.
- Migrated documentation to the unified CLI.
- Unstyled CLI output for more stable comparisons and snapshotting.

## DFlash2 Training

- DFlash defaults now use D-PACE, 5 layers, and CE loss.
- Added experimental DFlash2 training and checkpoint support. Note: you will need this commit in order to run the DFlash2 models in vLLM: https://github.com/vllm-project/vllm/pull/53797
- Added Laguna warm-start support:
  - Fused QKV weights are remapped for Laguna warm-start.
  - Laguna-style nested `rope_parameters` are flattened for compatibility.
- DSpark drafts now default to five layers.
- Reverted the confidence-head detach change.
- Verifier-owned weights are omitted from saved DFlash/DSpark checkpoints to reduce checkpoint size.
- DSpark's Markov lookup embedding is now initialized and optimized as a proper embedding.

## Multi-Node Training, Mooncake & `hs-connectors`

- Added a new Mooncake hidden-state extraction backend.
- Added the standalone `hs-connectors` package with:
  - Standard licensing and README.
  - Complete package metadata.
  - `mooncake-transfer-engine` dependency.
  - PyPI release support.
  - Nightly and release build support.
- Speculators now installs the matching `hs-connectors` package based on build type.
- Mooncake samples are validated with a checksummed manifest.
- Segment, buffer, and writer-thread sizing are configurable.
- Updated KV-cache extraction to follow the upstream restructure and use `extract_from_kv_cache`.
- Added Mooncake / `hs_connectors` documentation.

## Loss Functions

- Added a fused Triton online-softmax loss kernel used by all losses to reduce memory usage.
- Improved fused CE backward performance by stopping target-logit pinning.
- On Ascend NPU, fused-loss `BLOCK_SIZE` is capped at 4096.

## Data Generation, Preprocessing & Regen

- Support pre-tokenized datasets without requiring a chat template.
- Hardened hidden-state payload validation.
- Recover from hidden-state generation failures during training.
- `preprocess.py` now uses the vLLM render endpoint.
- Removed `--no-enable-chunked-prefill`.
- Unknown conversation roles are mapped to `assistant` during preprocessing.
- Regen now supports:
  - Local prompt files.
  - Sweep and sampling-parameter support.
  - Timing metrics for offline data generation.
- Log the number of broken records during data generation.
- Log the resolved training configuration to the metric backend.

## Evaluation, Benchmark & Provenance

- Added evaluation provenance artifacts:
  - `eval_command.txt`
  - vLLM launch metadata
- Benchmark now bounds the measured window and reports effective throughput.
- Updated evaluation requirements.

## Bug Fixes

- MTP: Default to SDPA attention instead of eager attention.
- Regen: Create parent directories for `--outfile` before opening.
- Locking: Use `O_RDWR` for `flock` compatibility on NFS.
- Data: Skip NaN hidden states instead of crashing training.
- Loading: Resolve LLM final norm for multimodal models.
- Training: Make cache cleanup accelerator-agnostic.
- Reject duplicate or negative `target_layer_ids`.
- Fail clearly when using tiny verifiers.
- Map unknown conversation roles to `assistant` during preprocessing.
- Suppress `httpx` logs during vLLM rendering.
- Trust remote code where required for model loading.
- Set the default maximum anchor to 512.

## Dependencies

- Updated `transformers` to `>=4.56.1,<5.17.0`, and subsequently to `5.0.0`.
- Updated `datasets` requirement to `>=4.0.0,<=5.0.1`.

## CI & Testing

- Migrated regression testing to nightly,
- Enabled per-commit smoke testing.
- Added pre-commit hooks mirroring `make quality`.

## Documentation

- Added DSpark algorithm documentation.
- Added loss-function documentation.
- Added P-EAGLE/DSpark training-argument pages.
- Added a multi-node Kimi-K3 DSpark training example.

## Full Changelog
* Add DSpark algorithm page by @guan404ming in https://github.com/vllm-project/speculators/pull/849
* Add timing metrics to offline data generation pipeline by @orestis-z in https://github.com/vllm-project/speculators/pull/804
* fix(regen): create parent dirs for --outfile before opening by @jialefu in https://github.com/vllm-project/speculators/pull/875
* Add loss functions page by @guan404ming in https://github.com/vllm-project/speculators/pull/858
* fix(mtp): default to SDPA attention instead of eager by @rahul-tuli in https://github.com/vllm-project/speculators/pull/881
* docs(tutorial): merge the four training tutorials into one by @WindChimeRan in https://github.com/vllm-project/speculators/pull/840
* Add 429 (Too many requests) to accepted return codes for link checks by @fynnsu in https://github.com/vllm-project/speculators/pull/891
* Add Mooncake hidden states extraction backend by @fynnsu in https://github.com/vllm-project/speculators/pull/836
* Document P-EAGLE and DSpark training arguments by @guan404ming in https://github.com/vllm-project/speculators/pull/857
* revert Detach dspark outputs before feeding them into the confidence head by @shanjiaz in https://github.com/vllm-project/speculators/pull/908
* fix(preprocessing): map unknown conversation roles to assistant by @orestis-z in https://github.com/vllm-project/speculators/pull/907
* fix(tests): fix weekly regression CI failures by @rahul-tuli in https://github.com/vllm-project/speculators/pull/909
* build(deps): update datasets requirement from <=5.0.0,>=4.0.0 to >=4.0.0,<=5.0.1 by @dependabot[bot] in https://github.com/vllm-project/speculators/pull/917
* [Data] Derive off-policy loss masks from vLLM render boundaries by @WindChimeRan in https://github.com/vllm-project/speculators/pull/794
* docs: fix supported models table structure by @cupkk in https://github.com/vllm-project/speculators/pull/925
* Revert "[Data] Derive off-policy loss masks from vLLM render boundaries" by @shanjiaz in https://github.com/vllm-project/speculators/pull/943
* ci(quality): run Quality workflow on release-* branches by @dsikka in https://github.com/vllm-project/speculators/pull/949
* fix(lock): use O_RDWR for flock compatibility on NFS by @fynnsu in https://github.com/vllm-project/speculators/pull/948
* removed no-enable-chunked-prefill by @shanjiaz in https://github.com/vllm-project/speculators/pull/976
* feat(train): default dflash to D-PACE, 5 layers, CE loss (RFC #979) by @shubhra in https://github.com/vllm-project/speculators/pull/980
* feat(dflash): remap fused QKV weights for Laguna warm-start by @orestis-z in https://github.com/vllm-project/speculators/pull/922
* feat: add Inkling weight aliases and training script by @orestis-z in https://github.com/vllm-project/speculators/pull/989
* update last release version by @dhuangnm in https://github.com/vllm-project/speculators/pull/990
* [Memory] Fuse every loss through one Triton online-softmax kernel by @WindChimeRan in https://github.com/vllm-project/speculators/pull/951
* fix(data): skip NaN hidden states instead of crashing training by @orestis-z in https://github.com/vllm-project/speculators/pull/994
* set default max anchor to 512 by @shanjiaz in https://github.com/vllm-project/speculators/pull/995
* fix(dflash): flatten Laguna-style nested rope_parameters by @orestis-z in https://github.com/vllm-project/speculators/pull/921
* update preprocess.py to use vllm render endpoint by @shanjiaz in https://github.com/vllm-project/speculators/pull/975
* cleanup(train): remove the deprecated --legacy-data path by @WindChimeRan in https://github.com/vllm-project/speculators/pull/914
* Update what's new and models list by @dsikka in https://github.com/vllm-project/speculators/pull/998
* [hs_connectors] Add a standard license and readme to enable initial pypi release by @dsikka in https://github.com/vllm-project/speculators/pull/997
* feat(eval): add eval_command.txt provenance artifact (RFC #880) by @orestis-z in https://github.com/vllm-project/speculators/pull/957
* [hs_connectors] Enhance pyproject.toml with description and keywords by @dsikka in https://github.com/vllm-project/speculators/pull/999
* test(mtp): xfail flaky weekly MTP online regression test by @rahul-tuli in https://github.com/vllm-project/speculators/pull/1003
* feat(launch_vllm): add vLLM provenance artifacts (RFC #880) by @orestis-z in https://github.com/vllm-project/speculators/pull/958
* build(deps): update transformers requirement from <5.15.0,>=4.56.1 to >=4.56.1,<5.16.0 by @dependabot[bot] in https://github.com/vllm-project/speculators/pull/1002
* trust remote code by @fynnsu in https://github.com/vllm-project/speculators/pull/963
* feat(data): accept pre-tokenized datasets without a chat template by @fynnsu in https://github.com/vllm-project/speculators/pull/964
* feat(train): log the resolved training config to the metric backend by @fynnsu in https://github.com/vllm-project/speculators/pull/965
* feat(data-generation): harden hidden-state payload validation by @fynnsu in https://github.com/vllm-project/speculators/pull/966
* [hs_connectors] Add mooncake-transfer-engine dependency by @dsikka in https://github.com/vllm-project/speculators/pull/1001
* feat(hs-connectors): validate Mooncake samples with a checksummed manifest by @fynnsu in https://github.com/vllm-project/speculators/pull/967
* feat(hs-connectors): expose Mooncake segment, buffer, and writer-thread sizing by @fynnsu in https://github.com/vllm-project/speculators/pull/968
* perf(losses): stop pinning target logits through the fused ce backward by @WindChimeRan in https://github.com/vllm-project/speculators/pull/1000
* revert: remove speculators import from launch_vllm.py by @rahul-tuli in https://github.com/vllm-project/speculators/pull/1008
* fix(pr-review): flag speculators imports in launch_vllm.py by @rahul-tuli in https://github.com/vllm-project/speculators/pull/1009
* [Testing] Migrate regression testing to nightly by @dsikka in https://github.com/vllm-project/speculators/pull/1004
* Support nightly/release build of hs-connectors and allow speculators to install corresponding package based on the build type by @dhuangnm in https://github.com/vllm-project/speculators/pull/1005
* fix(train): default DSpark drafts to five layers by @WindChimeRan in https://github.com/vllm-project/speculators/pull/1033
* fix(loading): resolve LLM final norm for multimodal models by @orestis-z in https://github.com/vllm-project/speculators/pull/1038
* Omit verifier-owned weights from saved DFlash/DSpark checkpoints by @qianlihuang in https://github.com/vllm-project/speculators/pull/962
* feat(losses): cap fused-loss BLOCK_SIZE at 4096 on Ascend NPU by @PHOEBEMOON0802 in https://github.com/vllm-project/speculators/pull/993
* fix(train): make cache cleanup accelerator-agnostic by @zihanlin-ai in https://github.com/vllm-project/speculators/pull/1025
* stablize eagle3 regression test by @shanjiaz in https://github.com/vllm-project/speculators/pull/1045
* Update eval requirements.txt by @orestis-z in https://github.com/vllm-project/speculators/pull/1042
* fix: reject duplicate or negative target_layer_ids, fail clearly on tiny verifiers by @zihanlin-ai in https://github.com/vllm-project/speculators/pull/1029
* Update transformers version to 5.0.0 by @dsikka in https://github.com/vllm-project/speculators/pull/1047
* Suppress httpx logs on vllm render by @fynnsu in https://github.com/vllm-project/speculators/pull/1040
* Add experimental DFlash2 training and checkpoint support by @mgoin in https://github.com/vllm-project/speculators/pull/1006
* feat(regen): support local prompt files by @WindChimeRan in https://github.com/vllm-project/speculators/pull/991
* ci: add pre-commit hooks mirroring make quality by @orestis-z in https://github.com/vllm-project/speculators/pull/1044
* [Testing] Enable per commit smoke testing by @dsikka in https://github.com/vllm-project/speculators/pull/1016
* [feat]: Log number of broken records by @pavelgein in https://github.com/vllm-project/speculators/pull/1035
* feat(train): recover from hidden-state generation failures by @fynnsu in https://github.com/vllm-project/speculators/pull/969
* No error to build from non-release tagged commit by @dhuangnm in https://github.com/vllm-project/speculators/pull/1039
* feat(benchmark): bound the measured window and report effective throughput by @fynnsu in https://github.com/vllm-project/speculators/pull/970
* fix(dspark): initialize and optimize the Markov lookup embedding as an embedding by @fynnsu in https://github.com/vllm-project/speculators/pull/971
* Regen improvements: sweep + sampling params by @shanjiaz in https://github.com/vllm-project/speculators/pull/1037
* docs(examples): add multi-node Kimi-K3 DSpark training example by @fynnsu in https://github.com/vllm-project/speculators/pull/972
* Add mooncake/hs_connectors docs by @fynnsu in https://github.com/vllm-project/speculators/pull/1046
* feat(cli): unified CLI surface by @rahul-tuli in https://github.com/vllm-project/speculators/pull/1024
* Update kv cache extraction following restructure by @fynnsu in https://github.com/vllm-project/speculators/pull/1068
* decrease gpu memory utilization for hidden sates vllm instance by @shanjiaz in https://github.com/vllm-project/speculators/pull/1069
* Add job checks for Unit, Integration, and Smoke tests by @fynnsu in https://github.com/vllm-project/speculators/pull/1070
* feat(examples): migrate train example scripts + docs to unified speculators CLI by @rahul-tuli in https://github.com/vllm-project/speculators/pull/1067
* Unstyle cli command output for more stable comparisons by @fynnsu in https://github.com/vllm-project/speculators/pull/1074
* Update hs_connector to use upstream extract_from_kv_cache by @fynnsu in https://github.com/vllm-project/speculators/pull/1072
* Move smoke tests into separate workflow by @fynnsu in https://github.com/vllm-project/speculators/pull/1073
* Update transformers version constraint in pyproject.toml by @dsikka in https://github.com/vllm-project/speculators/pull/1075
* perf(data): auto-size render endpoint concurrency for higher throughput by @WindChimeRan in https://github.com/vllm-project/speculators/pull/1013

## New Contributors
* @jialefu made their first contribution in https://github.com/vllm-project/speculators/pull/875
* @cupkk made their first contribution in https://github.com/vllm-project/speculators/pull/925
* @qianlihuang made their first contribution in https://github.com/vllm-project/speculators/pull/962
* @PHOEBEMOON0802 made their first contribution in https://github.com/vllm-project/speculators/pull/993
* @zihanlin-ai made their first contribution in https://github.com/vllm-project/speculators/pull/1025
* @pavelgein made their first contribution in https://github.com/vllm-project/speculators/pull/1035

**Full Changelog**: https://github.com/vllm-project/speculators/compare/v0.7.0...v0.8.0
