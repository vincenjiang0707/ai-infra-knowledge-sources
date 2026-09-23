# Changelog (aggregated from releases.body)

> releases: 18

## v0.1.0 (2024-09-04)

## What's Changed

Initial release of GuideLLM with version 0.1.0! This core release adds the basic structure, infrastructure, and code for benchmarking LLM deployments across several different use cases utilizing a CLI interface and terminal output. Further improvements are coming soon!

* Support added for general OpenAI backends and any text-input-based model served through those
* Support added for emulated, transformers, and file-based datasets
* Support added for general file storage of the full benchmark/evaluation that was run
* Full support for different benchmark types including sweeps, synchronous, throughput, constant, and poison enabled through new scheduler and executor interfaces built on top of Python's asyncio

## New Contributors
* @DaltheCow made their first contribution in https://github.com/neuralmagic/guidellm/pull/4
* @markurtz made their first contribution in https://github.com/neuralmagic/guidellm/pull/3
* @rgreenberg1 made their first contribution in https://github.com/neuralmagic/guidellm/pull/21
* @jennyyangyi-magic made their first contribution in https://github.com/neuralmagic/guidellm/pull/35

**Full Changelog**: https://github.com/neuralmagic/guidellm/commits/v0.1.0

## v0.2.0 (2025-04-18)

## Summary

- **Minimal Execution Overheads**
    - Refactor enabling async multi-process/threaded design with just 0.16% overhead in synchronous and 99.9% accuracy for constant requests
- **Robust Accuracy + Monitoring**
    - Built-in timings and diagnostics added to validate performance and catch regressions
- **Flexible Benchmarking Profiles**
    - Prebuilt support for synchronous, concurrent (added), throughput, constant rate, poisson rate, and sweep modes
- **Unified Input/Output Formats**
    - JSON, YAML, CSV, and console output now standardized
- **Multi-Use Data Loaders**
    - Native support for HuggingFace datasets, file-based data, and synthetic samples with fixes for previous flows and expanded support
- **Pluggable Backends via OpenAI-Compatible APIs**
    - Redeisgned to work out of the box with OpenAI style HTTP servers, easily expandable to other interfaces and servers. Fixed issues related to improper token lengths and more

## What's Changed
* Add summary metrics to saved json file by @anmarques in https://github.com/neuralmagic/guidellm/pull/46
* ADD TGI docs by @philschmid in https://github.com/neuralmagic/guidellm/pull/43
* Add missing vllm docs link by @eldarkurtic in https://github.com/neuralmagic/guidellm/pull/50
* Change default "role" from "system" to "user" by @philschmid in https://github.com/neuralmagic/guidellm/pull/53
* FIX TGI example by @philschmid in https://github.com/neuralmagic/guidellm/pull/51
* Revert Summary Metrics and Expand Test Coverage to Stabilize Nightly/Main CI by @markurtz in https://github.com/neuralmagic/guidellm/pull/58
* [Dataset]: Iterate through benchmark dataset once by @parfeniukink in https://github.com/neuralmagic/guidellm/pull/48
* Replace busy wait in async loop with a Semaphore by @sjmonson in https://github.com/neuralmagic/guidellm/pull/80
* Add backend_kwargs to generate_benchmark_report by @jackcook in https://github.com/neuralmagic/guidellm/pull/78
* Drop request count check from throughput sweep profile by @sjmonson in https://github.com/neuralmagic/guidellm/pull/89
* Rework Backend to Native HTTP Requests and Enhance API Compatibility & Performance by @markurtz in https://github.com/neuralmagic/guidellm/pull/91
* Multi Process Scheduler Implementation, Benchmarker, and Report Generation Refactor by @markurtz in https://github.com/neuralmagic/guidellm/pull/96
* Update the README by @sjmonson in https://github.com/neuralmagic/guidellm/pull/112
* Fix units for Req Latency in output to seconds by @smalleni in https://github.com/neuralmagic/guidellm/pull/113
* Fix/non integer rates by @thameem-abbas in https://github.com/neuralmagic/guidellm/pull/116
* Output support expansion, code hygiene, and tests by @markurtz in https://github.com/neuralmagic/guidellm/pull/117
* Bump min python to 3.9 by @sjmonson in https://github.com/neuralmagic/guidellm/pull/121
* v0.2.0 Version Update and Docs Expansions by @markurtz in https://github.com/neuralmagic/guidellm/pull/118
* Fix issue if async task count does not evenly divide accross process pool by @sjmonson in https://github.com/neuralmagic/guidellm/pull/120
* Readme grammar updates and cleanup by @markurtz in https://github.com/neuralmagic/guidellm/pull/124
* Update CICD flows to enable automated releases and match the feature set laid out in #56 by @markurtz in https://github.com/neuralmagic/guidellm/pull/125
* CI/CD Build Fixes for Release by @markurtz in https://github.com/neuralmagic/guidellm/pull/126

## New Contributors
* @anmarques made their first contribution in https://github.com/neuralmagic/guidellm/pull/46
* @philschmid made their first contribution in https://github.com/neuralmagic/guidellm/pull/43
* @eldarkurtic made their first contribution in https://github.com/neuralmagic/guidellm/pull/50
* @sjmonson made their first contribution in https://github.com/neuralmagic/guidellm/pull/80
* @jackcook made their first contribution in https://github.com/neuralmagic/guidellm/pull/78
* @smalleni made their first contribution in https://github.com/neuralmagic/guidellm/pull/113
* @thameem-abbas made their first contribution in https://github.com/neuralmagic/guidellm/pull/116

**Full Changelog**: https://github.com/neuralmagic/guidellm/compare/v0.1.0...v0.2.0

## v0.2.1 (2025-04-29)

## Summary
* Bug fixes enabling HF datasets and local data files for benchmarking that were resulting in crashes due to improper calls into datasets load_dataset function
* Refactored CI/CD system based on the latest standards for releases

## What's Changed
* Update version on main to 0.3.0 to begin work on the next release by @markurtz in https://github.com/neuralmagic/guidellm/pull/127
* Fix python versions for display in README.md by @markurtz in https://github.com/neuralmagic/guidellm/pull/128
* Fix logging by @hhy3 in https://github.com/neuralmagic/guidellm/pull/129
* Data and request fixes for real data / chat_completions pathways by @markurtz in https://github.com/neuralmagic/guidellm/pull/131
* Fix argument error in nightly unit tests by @sjmonson in https://github.com/neuralmagic/guidellm/pull/132
* Add docs for data/datasets and how to configure them in GuideLLM by @markurtz in https://github.com/neuralmagic/guidellm/pull/137
* Refactor CI/CD system based on latest standardization for upstreams by @markurtz in https://github.com/neuralmagic/guidellm/pull/135

## New Contributors
* @hhy3 made their first contribution in https://github.com/neuralmagic/guidellm/pull/129

**Full Changelog**: https://github.com/neuralmagic/guidellm/compare/v0.2.0...v0.2.1

## v0.3.0 (2025-09-16)

# **GuideLLM v0.3.0**

## **Overview**

A major (non-semantic versioning sense) release introducing the GuideLLM web UI, containerized benchmarking, dataset preprocessing, and significant workflow improvements. This release transitions the project from the Neural Magic organization into the vLLM project ecosystem while expanding benchmarking capabilities and improving developer experience.

To get started, install with:

```bash
pip install guidellm==0.3.0
```

Or from source with:

```bash
pip install git+https://github.com/vllm-project/guidellm.git@v0.3.0
```

## **What's New**

- **GuideLLM Web UI**: Complete frontend interface with interactive charts and data visualization for benchmark results
- **Dataset Preprocessing**: New preprocess command to filter datasets by token distribution and save to local files or Hugging Face Hub
- **Containerized Benchmarking**: Docker support with configurable environment variables for streamlined deployment
- **Benchmark Scenarios**: Support for file-based benchmark configuration with Pydantic validation
- **HTML Report Generation**: Static HTML reports with embedded visualization data

## **What's Changed**

- **Project Migration**: Transitioned from neuralmagic to vllm-project GitHub organization with updated links and branding
- **Improved Scheduling**: Unified RPS and concurrent scheduler paths for better multi-turn conversation support
- **Enhanced OpenAI Backend**: Added support for custom headers, SSL verification control, query parameters, and request body modifications
- **Development Workflow**: Streamlined CI/CD with unified test execution, pre-commit improvements, and artifact management
- **Synthetic Data Generator**: Added prefix caching controls and unique prompt generation

## **What's Fixed**

- **Metric Calculation**: Fixed double-counting issues in token calculations and concurrency change events
- **Event Loop Errors**: Resolved "Event loop Closed" errors in HTTP client connection pooling
- **Token Counting**: Fixed max token limits in synthetic data generator and first decode token counting
- **Display Issues**: Corrected metric units display and Firefox compatibility for web UI

## **Compatibility Notes**

- Python: 3.9–3.13
- OS: Linux and macOS
- Dependencies: Updated to latest Pydantic, locked Click to support Python 3.9
- **Breaking**: Removed several UI workflow components and husky pre-commit hooks
- **Breaking**: Updated project URLs from vllm-project to neuralmagic organization

## **New Contributors**

- @chewong made their first contribution in #168
- @dagrayvid made their first contribution in #173
- @TomerG711 made their first contribution in #162
- @wangchen615 made their first contribution in #123
- @kyolebu made their first contribution in #207
- @rymc made their first contribution in #223
- @jaredoconnell made their first contribution in #185
- @natoscott made their first contribution in #231
- @kdelee made their first contribution in #230
- @Harshith-umesh made their first contribution in #240
- @tjandy98 made their first contribution in #256
- @tukwila made their first contribution in #302

## **Changelog**

### Major Features

- #169: Implement complete GuideLLM UI with interactive charts and Redux state management
- #162: Add dataset preprocessing command with HuggingFace integration
- #123: Add containerized benchmarking support with Docker configuration
- #99: Add support for benchmark scenarios with Pydantic validation
- #218: Implement HTML output generation with embedded data

### Infrastructure & Workflows

- #233: Unify RPS and concurrent scheduler paths for improved performance
- #215: Complete UI build pipeline and GitHub Pages workflows
- #231: Migrate project from vllm-project to neuralmagic organization
- #190: Add container build jobs to all workflows

### Backend Improvements

- #230: Add CLI options for custom headers and SSL verification
- #146: Allow extra query parameters for OpenAI server requests
- #184: Add remove_from_body parameter to OpenAIHTTPBackend
- #183: Add prefix caching controls to synthetic dataset generator

### Bug Fixes & Quality

- #266: Fix metric accumulation errors at extreme concurrency changes
- #188: Fix "Event loop Closed" error in HTTP client pooling
- #173: Fix double counting of tokens and warmup percentage calculation
- #170: Fix max token limits in synthetic data generator

### Developer Experience

- #240: Add --version flag to guidellm CLI
- #185: Add option to re-display benchmark files
- #181: Improve pre-commit usability for local development
- #239: Various tooling fixes including dependency groups and pylock

## v0.3.1 (2025-10-10)

# GuideLLM v0.3.1

## Overview
Minor release focused on container build/tagging stability, UI polish and terminology alignment, improved OpenAI backend robustness/configurability, clearer JSON output, and new documentation (llama.cpp usage and a vLLM simulator walkthrough). Workflows now produce versioned artifacts and maintain latest/stable tags automatically.

To get started, install with:
```bash
pip install guidellm[recommended]==0.3.1
```
Or from source with:
```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.3.1
```


## What's New
- **Recommended Extras Group**: Install OpenAI tokenizer dependencies via `guidellm[recommended]` (tiktoken, blobfile)
- **llama.cpp Guide**: New docs covering llama-server, model aliasing, and metadata handling
- **vLLM Simulator Example**: Step-by-step “first benchmark” walkthrough with sample output images
- **Container Maintenance Workflow**: Scheduled cleanup of old PR images; auto-retag latest and stable

## What's Changed
- **UI Polish**: Clearer labels (e.g., “Time Per Request”, “Measured RPS (Mean)”) and slider text
- **Versioned Reports**: PROD/STAGING report URLs pinned to versioned UI builds
- **Container Build System**: New top-level Containerfile using Fedora Python minimal + PDM; build type via GUIDELLM_BUILD_TYPE
- **Metrics JSON Output**: UTF-8 encoding with pretty-printed, indented JSON
- **Endpoint Max Tokens Keys**: Output-token limit now governed per-endpoint via `GUIDELLM__OPENAI__MAX_OUTPUT_KEY`

## What's Fixed
- **Streaming Robustness**: Safely handle missing delta.content for chat streams
- **Endpoint Token Keys**: Configurable max output key per endpoint (max_tokens vs max_completion_tokens)
- **CI Stability**: Fixes to RC tagging, GH Pages publish paths, and workflow typos; disable dry-run for image cleanup

## Compatibility Notes
- **Python**: 3.9–3.13
- **OS**: Linux and MacOS
- **Dependencies**: Optional extras via `guidellm[recommended]`; currently includes packages for OpenAI's tokenizer but may expand in the future
- **Breaking**: Previously all endpoints used both `max_tokens` and `max_completion_tokens` to bound output; this caused issues with some servers
  - The key is now controlled per-endpoint (defaults to `max_tokens` for legacy `completions` and `max_completion_tokens` for `chat/completions`)

## New Contributors
- **@rgerganov**: made their first contribution in PR #318
- **@git-jxj**: made their first contribution in PR #316
- **@psydok**: made their first contribution in PR #372

## Changelog
- UI & Presentation
  - #386: Update TPOT to ITL across labels and code
  - #298: Update RPS slider label
  - #301: Fix GH Pages UI publish path (src/ui/out)
  - #317: Correct type hint to fix Pydantic serialization warning
- Backend
  - #399: Make `max_tokens`/`max_completion_tokens` key configurable per endpoint
  - #316: Handle missing content in streaming delta
- Containers & CI
  - #254: Overhaul container image and CI (new top-level Containerfile, PDM build)
  - #379: Container CI bugfix and disable dry-run on image cleaner
  - #310: Use versioned builds (and version-pinned report links)
  - #389: Fix container RC tag
  - #398: Fix container RC tag (Attempt 2)
  - #400: Fix failing CI
  - #401: Fix typo in CI
  - #301: Correct UI src path in workflows (publish_dir)
- Output & Tooling
  - #372: Pretty-print and UTF-8 encode metrics JSON files
- Documentation
  - #318: Add documentation on how to use with llama.cpp
  - #328: Add “first benchmark testing example” (vLLM simulator)
- Packaging
  - #313: Add recommended extras group

Changelog link: https://github.com/vllm-project/guidellm/compare/v0.3.0...v0.3.1

## v0.4.0 (2025-11-21)

## **Overview**

This release marks a significant milestone with a **full architectural refactor** of the GuideLLM codebase to improve extensibility, performance, and maintainability. Key highlights include **multimodal benchmarking support** (vision and audio), a new **mock server** for testing, and comprehensive updates to output generation and statistics gathering. Additionally, the minimum supported Python version has been bumped to 3.10 to leverage modern language features.

To get started, install with:

```bash
pip install guidellm==0.4.0
```

Or from source with:

```bash
pip install git+https://github.com/vllm-project/guidellm.git@v0.4.0
```

## **What's New**

- **Multimodal Support**: Added comprehensive support for vision and audio workloads, including audio transcription and translation benchmarking.
- **Full Refactor**: Complete restructuring of core packages (`backends`, `scheduler`, `benchmark`, `data`) to support high-rate load generation and easier extensibility.
- **Mock Server**: Introduced a built-in mock server package to facilitate testing and development without requiring a live LLM backend.
- **E2E Testing**: Added a new End-to-End (E2E) testing workflow with a dedicated vLLM simulator.

## **What's Changed**

- **Python Requirement**: Minimum supported Python version bumped to **3.10** (previously 3.9).
- **CLI Arguments**:
    - Renamed `--rate-type` to `--profile` for clarity.
    - `--output-path` has been split into `--output-dir` and `--outputs`. E.g. `--output-dir /results --outputs benchmark.json,benchmark.csv`. `--output-path` will continue to work in this release, but will be deprecated in the future.
- **Container**: Updated Docker container to include `ffmpeg` and other utilities for multimodal support.
- **Data Pipelines**: Reworked data pipelines to support complex multimodal datasets and better error propagation for HuggingFace loading.

## **What's Fixed**

- **Synthetic Data**: Fixed an issue where synthetic text datasets would lose randomness across benchmarks in the same session.
- **CSV Generation**: Resolved failures in CSV output generation during benchmarks.
- **Asyncio Stability**: Fixed various `asyncio` and timezone-related issues in tests and schedulers.
- **Type Safety**: Extensive type fixes and improvements across the codebase, particularly in the `scheduler` and `utils` packages.

## **Compatibility Notes**

- **Python**: 3.10 – 3.13
- **OS**: Linux and macOS
- **Dependencies**:
    - Added `torchcodec`
    - Removed `librosa`, `pydub`, `soundfile`
    - Development workflow now uses `pdm` and `tox-pdm`

## **New Contributors**

- @shijinye made their first contribution in PR #327
- @git-jxj made their first contribution in PR #435
- @AlonKellner-RedHat made their first contribution in PR #440

## **Changelog**

### Refactor & Core Architecture

- PR #351: Full refactor of GuideLLM
- PR #354: Scheduler package updates, rewrites, and tests expansion
- PR #355: Backend package updates, rewrites, and tests expansion
- PR #356: Benchmark package updates and rewrites
- PR #357: Mock server package creation
- PR #364: Core reintroduction of changes from main

### Multimodal & Data

- PR #384: Data pipelines rework and multimodal support
- PR #419: Split multimodal group into vision and audio
- PR #411: Replace librosa, pydub, and soundfile with torchcodec
- PR #412: Fixes for constant rate and audio flows
- PR #463: Ensure synthetic text datasets remain random across benchmarks

### Features & Enhancements

- PR #378: Complete CSV output
- PR #432: Better scenario from-file support
- PR #441: Support dashed arguments for benchmark args
- PR #433: Switch --rates CLI arg to handle a comma separated list of values
- PR #382: Advanced Prefix Cache Controls

### Infrastructure & Quality

- PR #397: Bump minimum python version to 3.10
- PR #440: Basic E2E tests
- PR #420: Adapt container for new optional requirements
- PR #415: Add tox command to update lock file
- PR #442: Updates and Fixes for benchmark outputs, schemas, and stats calculations

### Bug Fixes

- PR #435: Resolve CSV output generation failure in benchmarks
- PR #413: Propagate valid failures from HuggingFace datasets loading
- PR #405: Fixes for asyncio and timezone tests
- PR #376: Edge case errors
- PR #449: Fix failing settings tests

## v0.5.0 (2025-12-16)

## Overview

GuideLLM v0.5.0 is a small release adding request throttling when server is over-saturated. The release re-introduces features for dataset preprocessing and fixes various issues introduced in v0.4.0.

To get started, install with:

```bash
pip install guidellm[recommended]==0.5.0
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.0
```

## Breaking Changes

- **Throughput Mode**:  Throughput mode previously assumed a fixed rate.
  - *Migration*: Throughput mode now requires manually specifying `--rate` if used outside of sweep mode.

## What's New

- **Comprehensive Preprocessing Guide**: Major documentation update covering preprocessing configs, strategies for handling short prompts, advanced column mapping, and reproducibility controls.
- **Over-Saturation Detection**: Automatic benchmark stopping when LLM servers are overloaded with a fine-tunable saturation detection and in-depth docs.

## What's Changed

- **Dataset Preprocessing Command**: Re-enable `guidellm preprocess dataset` command for custom prompt/output token sizing, column mapping, batch preprocessing, prompt strategies, and huggingface uploads.
- **Benchmark CLI**: Added `--detect-saturation` and `--over-saturation` for robust specification of saturation constraints.

## What's Fixed

- **Assorted documentation fixes**: Documentation polish and outdated references removed.
- **Dataset handler**: Fixed edge case where finite length datasets would stall out when exhausted.
- **Connection limit**: Uncapped limits on number of connections per worker. Previously fixed at 100.

## Compatibility Notes

- **Python**: 3.10–3.13
- **OS**: Linux, MacOS

## Changelog

### Bug fixes

* Unmask StopIteration in DataLoader by @sjmonson in https://github.com/vllm-project/guidellm/pull/468
* fix encode_audio with dict input failure by @tukwila in https://github.com/vllm-project/guidellm/pull/480
* ut for audio and vision encode function by @tukwila in https://github.com/vllm-project/guidellm/pull/489
* Allow unlimited connections per-worker by @sjmonson in https://github.com/vllm-project/guidellm/pull/488

### New features

* Add over saturation constraint by @AlonKellner-RedHat in https://github.com/vllm-project/guidellm/pull/438
* Add more metadata to benchmark report by @sjmonson in https://github.com/vllm-project/guidellm/pull/497
* Add vllm id to the response by @toslali-ibm in https://github.com/vllm-project/guidellm/pull/455
* Indicate max_concurrency for throughput and disallow running standalone without --rate by @sjmonson in https://github.com/vllm-project/guidellm/pull/467
* Reenable and improve preprocess dataset by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/472

### CI, Workflows & Packaging

* Fix container version mismatch by moving build type ARG after FROM by @yankay in https://github.com/vllm-project/guidellm/pull/473
* update build versions in settings, workflow versioned build fix by @DaltheCow in https://github.com/vllm-project/guidellm/pull/465
* Fixes and Cleanup of CI by @sjmonson in https://github.com/vllm-project/guidellm/pull/469
* Fix test failures due to collecting 0 tests by @sjmonson in https://github.com/vllm-project/guidellm/pull/485
* Fix container overriding output-dir/outputs by @sjmonson in https://github.com/vllm-project/guidellm/pull/486
* Switch to uv in build, test, and CI by @sjmonson in https://github.com/vllm-project/guidellm/pull/494
* Bump some old dependency locks by @sjmonson in https://github.com/vllm-project/guidellm/pull/496
* UT for src/guidellm/data/deserializers/file.py by @tukwila in https://github.com/vllm-project/guidellm/pull/495

## New Contributors
* @toslali-ibm made their first contribution in https://github.com/vllm-project/guidellm/pull/455
* @yankay made their first contribution in https://github.com/vllm-project/guidellm/pull/473

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.4.0...v0.5.0

## v0.5.1 (2026-01-14)

## Overview

GuideLLM v0.5.1 fixes multiple issues introduced in v0.4.0. We recommend all user that rely on constraints other then `--max-requests` update immediately due to some bugs in incomplete request accounting.

To get started, install with:

```bash
pip install guidellm[recommended]==0.5.1
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.1
```

## What's Fixed

* Incomplete requests now record the number of tokens received up to cancellation. This restores pre-v0.4.0 behavior.
* Audio benchmarking now works for vLLM `>v0.7.3`.

## Compatibility Notes

- **Python**: 3.10–3.13
- **OS**: Linux, MacOS

## Changelog

### Bug fixes

* bug fix - html rendering when multiple percentiles are the same by @sjmonson in https://github.com/vllm-project/guidellm/pull/515
* Fix Transcription / Translation endpoint usage by @sjmonson in https://github.com/vllm-project/guidellm/pull/524
* Record output_tokens for incomplete requests by @sjmonson in https://github.com/vllm-project/guidellm/pull/519

### Documentation

* Fix outputs documentation with correct parameter syntax by @maryamtahhan in https://github.com/vllm-project/guidellm/pull/508

### CI, Workflows & Packaging

* memory ut case by @tukwila in https://github.com/vllm-project/guidellm/pull/506
* update db_file ut case by @tukwila in https://github.com/vllm-project/guidellm/pull/507
* Rerun e2e tests in CI due to flakyness by @sjmonson in https://github.com/vllm-project/guidellm/pull/503
* Update settings.py by @DaltheCow in https://github.com/vllm-project/guidellm/pull/512
* Container Build Caching by @sjmonson in https://github.com/vllm-project/guidellm/pull/509
* UT for src/guidellm/data/deserializers/huggingface.py by @tukwila in https://github.com/vllm-project/guidellm/pull/500
* mock audio translations/transcriptions functions by @tukwila in https://github.com/vllm-project/guidellm/pull/521

## New Contributors
* @maryamtahhan made their first contribution in https://github.com/vllm-project/guidellm/pull/508

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.5.0...v0.5.1

## v0.5.2 (2026-01-16)

## Overview

GuideLLM v0.5.2 continues to fix bugs and reintroduce features dropped in v0.4.0.

To get started, install with:

```bash
pip install guidellm[recommended]==0.5.2
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.2
```

## What's Changed

* Support for passing an API key has been reintroduced. API keys can be set with the argument `--backend-kwargs '{"api_key": "KEY"}'`.
* Console output now uses the "total" requests category rather then just "successful". See #529 for more details.

## What's Fixed

* Fixed a deadlock that could occur on benchmark start which could significantly delay the first request send.
* Fixed formatting of image and video URLs. The previous version worked with vLLM but was not OpenAI-API compliant.

## Compatibility Notes

- **Python**: 3.10–3.13
- **OS**: Linux, MacOS

## Changelog

### Bug fixes

* Make image_url/video_url send dictionaries by @Vinno97 in https://github.com/vllm-project/guidellm/pull/525
* Fix strategy initialization deadlock by @sjmonson in https://github.com/vllm-project/guidellm/pull/528

### Features

* Use total requests for throughput calculation by @sjmonson in https://github.com/vllm-project/guidellm/pull/530
* Added option to log errors from backends by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/534
* OpenAI API-Key Support by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/535

### Documentation

* Fix some outdated docs examples by @sjmonson in https://github.com/vllm-project/guidellm/pull/531
* docs: update link for vllm simulator by @maryamtahhan in https://github.com/vllm-project/guidellm/pull/532

## New Contributors
* @Vinno97 made their first contribution in https://github.com/vllm-project/guidellm/pull/525

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.5.1...v0.5.2

## v0.5.3 (2026-01-23)

## Overview

GuideLLM v0.5.3 is a very small patch focused on enabling mistral3 model tokenizers.

To get started, install with:

```bash
pip install guidellm[recommended]==0.5.3
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.3
```

## What's Changed

* Constant rate-type benchmarks now support the `--rampup` feature which ramps up the give rate linearly.
* Added `mistral-common` as a optional dependency to enable loading mistral3 based tokenizers.
    * NOTE: Loading the mistral tokenizer also requires `transformers>=5.0.0`.

## Compatibility Notes

- **Python**: 3.10–3.13
- **OS**: Linux, MacOS

## Changelog

### Bug fixes

* Correct import for transformers internals by @sjmonson in https://github.com/vllm-project/guidellm/pull/540

### Features

* Add Mistral tokenizer as optional dependency by @sjmonson in https://github.com/vllm-project/guidellm/pull/541
* Added rampup to constant rate type by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/549

### Documentation

* Add documentation how to use with llama.cpp by @rgerganov in https://github.com/vllm-project/guidellm/pull/536

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.5.2...v0.5.3

## v0.5.4 (2026-03-12)

## Overview

GuideLLM v0.5.4 is a hotfix patch recommended to all GuideLLM users.

To get started, install with:

```bash
pip install guidellm[recommended]==0.5.4
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.4
```

## What's Fixed

* `--sample-requests` should now function correctly
* Bump `transformers` package in lockfile to support mistral model tokenizers
* Update HTML report to pull its template from `raw.githubusercontent.com` rather than `blog.vllm.ai`
    * **Critical:** This issue would cause crashes when the HTML report was enabled

## Compatibility Notes

- **Python**: 3.10–3.13
- **OS**: Linux, MacOS

## Changelog

### Bug fixes

* Fix the guidellm benchmark --sample-requests command line option by @sjmonson in https://github.com/vllm-project/guidellm/pull/591
* Bump transformers version in lock by @sjmonson in https://github.com/vllm-project/guidellm/pull/628
* Move html template source location to raw github by @sjmonson in https://github.com/vllm-project/guidellm/pull/629

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.5.3...v0.5.4

## v0.6.0 (2026-04-01)

## Overview

GuideLLM v0.6.0 is a feature release adding multi-turn, Responses API, GeoSpatial model support, and in-process vLLM Python backend along with bug fixes.

To get started, install with:

```bash
pip install guidellm[recommended]==0.6.0
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.6.0
```

## Compatibility Notes

- **Python**: 3.10–3.13
- **OS**: Linux, MacOS

## What's New:

* Added basic Responses API support: tool calling support will be added later
* Added multi-turn support for both datasets and synthetic data
* Added vLLM Python (in-process) backend
* Added TerraTorch GeoSpacial model support

## What's Fixed:

* Allow disabling vLLM-specific body options in HTTP backend
* Fix `--sample-requests` to limit sampling in output
* Fix HTML references in html report
* Fixed container image HOME permissions for OpenShift

## Change Log

### Features

* Instant ttft oversaturation by @ushaket in https://github.com/vllm-project/guidellm/pull/607
* vLLM Python Backend by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/596
* Multiturn Benchmarking by @sjmonson in https://github.com/vllm-project/guidellm/pull/590
* Add turn and conversation trackers to the request by @sjmonson in https://github.com/vllm-project/guidellm/pull/649
* Basic Responses API Support by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/655
* Add support for TerraTorch Geospatial models served via the vLLM /pooling endpoint by @mgazz in https://github.com/vllm-project/guidellm/pull/610

### Internal refactoring & cleanup

* Fix and improve the mock server by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/640
* Import utils from sub-submodules by @sjmonson in https://github.com/vllm-project/guidellm/pull/644
* Move request formatting to backend by @sjmonson in https://github.com/vllm-project/guidellm/pull/478
* Drop median from throughput metrics in console by @sjmonson in https://github.com/vllm-project/guidellm/pull/617
* Fix HTML on main and disable by default by @sjmonson in https://github.com/vllm-project/guidellm/pull/638
* Drop vLLM extras group by @sjmonson in https://github.com/vllm-project/guidellm/pull/635
* Improve environment variables warning and validation cleanup by @sjmonson in https://github.com/vllm-project/guidellm/pull/654
* Pass mp context to strategy by @sjmonson in https://github.com/vllm-project/guidellm/pull/651
* Cleanup __init__ by @sjmonson in https://github.com/vllm-project/guidellm/pull/647

### Fixes

* fix(cli): validate --output-path against --output-dir by @aiwantaozi in https://github.com/vllm-project/guidellm/pull/561
* Fix the guidellm benchmark --sample-requests command line option by @natoscott in https://github.com/vllm-project/guidellm/pull/591
* Drop various depricated settings and remove the default OpenAI request timeout by @sjmonson in https://github.com/vllm-project/guidellm/pull/589
* Fix /v1/chat/completions formatting by @sjmonson in https://github.com/vllm-project/guidellm/pull/595
* Containerfile: ensure that HOME can be used by any user ID by @kpouget in https://github.com/vllm-project/guidellm/pull/601
* Fix JSON serialization for binary request payloads via base64 bytes config by @ushaket in https://github.com/vllm-project/guidellm/pull/612
* Move html template source location to raw github by @sjmonson in https://github.com/vllm-project/guidellm/pull/629
* Fix file extension not being sent to output handler by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/639
* Check if deserialization path is vaild safely by @sjmonson in https://github.com/vllm-project/guidellm/pull/659
* Support removing keys from HTTP request bodies by @sjmonson in https://github.com/vllm-project/guidellm/pull/661
* Replace line iter with bytes to lines wrapper by @sjmonson in https://github.com/vllm-project/guidellm/pull/663
* Revert back to iterating over lines by @sjmonson in https://github.com/vllm-project/guidellm/pull/680

### CI environment

* Fix multiple main CI failures by @sjmonson in https://github.com/vllm-project/guidellm/pull/578
* Replace exisiting issue templates with form versions by @sjmonson in https://github.com/vllm-project/guidellm/pull/586
* Add merge policies by @sjmonson in https://github.com/vllm-project/guidellm/pull/630
* Run format job in CI by @sjmonson in https://github.com/vllm-project/guidellm/pull/625
* Drop RC jobs and nightly PyPi publish by @sjmonson in https://github.com/vllm-project/guidellm/pull/632
* Mark requeue test as xfail due to uvloop bug by @sjmonson in https://github.com/vllm-project/guidellm/pull/652
* Lock all GitHub Actions to SHA by @dbutenhof in https://github.com/vllm-project/guidellm/pull/666
* Identify action versions by @dbutenhof in https://github.com/vllm-project/guidellm/pull/679
* Remove "uv" ecosystem from yaml by @dbutenhof in https://github.com/vllm-project/guidellm/pull/681

### Documentation

* Add multimodal benchmarking usage docs by @markurtz in https://github.com/vllm-project/guidellm/pull/568
* Add data parameter to benchmark command in README by @S1ro1 in https://github.com/vllm-project/guidellm/pull/616
* Add detail in benchmark profile documentation by @dbutenhof in https://github.com/vllm-project/guidellm/pull/619
* docs: add documentation for passing sampling parameters via --backend-kwargs by @cemigo114 in https://github.com/vllm-project/guidellm/pull/626
* docs: Fixing a broken link of docs/guides/outputs.md. by @theodor2311 in https://github.com/vllm-project/guidellm/pull/642

### Dependency updates

* Fixup pylock after dependabot PRs by @sjmonson in https://github.com/vllm-project/guidellm/pull/553
* Fix for Dependabot action by @sjmonson in https://github.com/vllm-project/guidellm/pull/554
* Drop pylock by @sjmonson in https://github.com/vllm-project/guidellm/pull/555
* Bump virtualenv from 20.35.4 to 20.36.1 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/544
* Bump urllib3 from 2.5.0 to 2.6.3 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/545
* Bump aiohttp from 3.13.2 to 3.13.3 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/547
* Bump protobuf from 6.33.1 to 6.33.5 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/580
* Bump pillow from 12.0.0 to 12.1.1 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/593
* Bump torchcodec (and torch) by @sjmonson in https://github.com/vllm-project/guidellm/pull/614
* Bump transformers version in lock by @sjmonson in https://github.com/vllm-project/guidellm/pull/628
* Bump orjson from 3.11.4 to 3.11.6 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/631
* Bump ujson from 5.11.0 to 5.12.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/643
* Require datasets 4.1.0 by @dbutenhof in https://github.com/vllm-project/guidellm/pull/650
* Bump requests from 2.32.5 to 2.33.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/657

## New Contributors
* @aiwantaozi made their first contribution in https://github.com/vllm-project/guidellm/pull/561
* @kpouget made their first contribution in https://github.com/vllm-project/guidellm/pull/601
* @ushaket made their first contribution in https://github.com/vllm-project/guidellm/pull/612
* @S1ro1 made their first contribution in https://github.com/vllm-project/guidellm/pull/616
* @dbutenhof made their first contribution in https://github.com/vllm-project/guidellm/pull/619
* @cemigo114 made their first contribution in https://github.com/vllm-project/guidellm/pull/626
* @theodor2311 made their first contribution in https://github.com/vllm-project/guidellm/pull/642
* @mgazz made their first contribution in https://github.com/vllm-project/guidellm/pull/610

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.5.3...v0.6.0

## v0.6.1 (2026-06-23)

## Overview

GuideLLM v0.6.1 is a hotfix patch to support RHAI 3.5 container build.

To get started, install with:

```bash
pip install guidellm[recommended]==0.6.1
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.6.1
```

## What's Fixed

- Bump torch version to 2.11
- Bump torchcodec version to 0.11

## Compatibility Notes

- **Python**: 3.10–3.13
- **OS**: Linux, MacOS

## What's Changed

* Upgrade 0.6 torch dependencies by @dbutenhof in https://github.com/vllm-project/guidellm/pull/837

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.6.0...v0.6.1

## v0.7.0 (2026-06-29)

## Overview

GuideLLM v0.7.0 improves how you configure and run benchmarks, adds production-realistic trace replay, and expands support for modern LLM workloads: reasoning models, tool calling, embeddings, and Mooncake traces.

To get started, install with:

```bash
pip install guidellm\[recommended\]==0.7.0
```

Or from source with:

```bash
pip install 'guidellm\[recommended\] @ git+[https://github.com/vllm-project/guidellm.git'@v0.7.0](https://github.com/vllm-project/guidellm.git'@v0.7.0)
```

## What's New

* Support for server-side conversation history in /v1/responses API
* Support for client and server side tool calling using /v1/chat/completions and /v1/responses APIs  
* Websocket backend (openai\_websocket) for realtime audio transcription  
* vLLM Python backend (vllm\_python) for running inference in the same process as GuideLLM using vLLM's python API (AsyncLLMEngine), without an HTTP server.  
* Synthetic tool calling support in chat/completions and responses APIs  
* Mooncake LLM trace replay  
  * Given a data file with timestamps and `prompt_tokens`/`output_tokens` synthetic data parameters, you can replay a recorded session. Mooncake provides KV cache replay using token cache block hash values which are used to compute tokens that replay a conversation with equivalent cache sensitivity, without recording or using the original data.  
* Support for testing OpenAI embeddings API  
* Support for building ARM64 container images

### Major CLI refactoring  
  * Constraints (`--max-requests`, `--max-duration`, `--max-errors`, etc.) are now treated as first class objects using the consistent syntax `--constraint kind=<name>,<OPTIONS>...`, such as `--constraint kind=max_requests,count=1000` or `--constraint kind=over_saturation,mode=enforce,moe_threshold=3.0`  
  * The `--data` handling was overloaded, often with no clear way to determine what sort of data was to be loaded – for example, a huggingface dataset vs a local file. Error messages are often unclear, because the engine searched through a list of possibilities with no way to know which was expected to succeed. Now “data” is clearly typed, like `--data kind=huggingface,source=<name>` or `--data kind=json_file,path=<path>`  
  * Specification of profiles and backends are now clearly typed, with clearly connected parameters, like `--backend kind=openai_http,target=<url>,streaming=true` and `--profile async ‘{“rate”:[10,20]}’`  
  * The syntax is designed to allow pre-loading layered “config” files like the previous `--scenario <file>`, also allowing overrides to the scenario/global values. This will enable the long-requested feature of being able to override constraints for each benchmark (“strategy”) scheduled under a profile. For example, `--profile kind=async,rate=10` schedules one asynchronous strategy with rate 10, but specifying multiple rates requires using inline JSON to specify a list. Instead, you can define the rates with `–profile kind=async --override profile.rate=10,20` you can run two rates.  


## CLI Migration Guide

Read on GitHub at [v0.7.0 Migration Guide](https://vllm-project.github.io/guidellm/0.7.0/guides/v0.7.0_migration_guide/) 

## What's Fixed

* Several fixes for the HTML report output rendering. (Future plans include making the HTML report format completely self-contained to eliminate many problems.)  
* Improved handling of audio file format – preserve original format if possible, and when transcoding is necessary default to WAV rather than MP3  
* Improved reporting of TTFT, especially when reasoning models first generate “non-output” thinking tokens  
* Several fixes in dataset column mapping, including fast failure when there are no mappable columns

## Known Limitations
- Tool call responses are currently added to the following user turn. The following release will separate them into dedicated response turns.

## Changelog

### Features
* Process tool call requests for chat completions API by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/687
* Apply tool calling stats to the responses API by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/692
* Support server-side conversation history on responses API by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/697
* feat: Add embeddings endpoint support (MVP) by @maryamtahhan in https://github.com/vllm-project/guidellm/pull/710
* [v0.7 CLI Refactor] Rework BackendArgs to be the authoritative config location  by @sjmonson in https://github.com/vllm-project/guidellm/pull/723
* [FEAT] Add replay from trace strategy by @VincentG1234 in https://github.com/vllm-project/guidellm/pull/620
* Multi-turn tool call chat completions conversations by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/712
* Add multi-arch (x86, arm) container image support by @maryamtahhan in https://github.com/vllm-project/guidellm/pull/720
* [v0.7 CLI Refactor] Rework Data Deserialization Config by @sjmonson in https://github.com/vllm-project/guidellm/pull/733
* Feat/multi turn tools responses by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/739
* [v0.7 CLI Refactor] Finish up data rework by @sjmonson in https://github.com/vllm-project/guidellm/pull/754
* CLI profile refactor by @dbutenhof in https://github.com/vllm-project/guidellm/pull/753
* Add lazy-loading for extras packages by @sjmonson in https://github.com/vllm-project/guidellm/pull/641
* Constraints refactor by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/786
* Add Mooncake trace format support by @SkiHatDuckie in https://github.com/vllm-project/guidellm/pull/777
* Infer audio encoding format from source instead of defaulting to MP3 by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/794
* [v0.7 CLI Refactor] New internal top-level args / CLI by @sjmonson in https://github.com/vllm-project/guidellm/pull/789
* Simplify constraint parameter names by @dbutenhof in https://github.com/vllm-project/guidellm/pull/799
* Realtime transcription endpoint by @ushaket in https://github.com/vllm-project/guidellm/pull/713
* Revert Pydantic Registry parameters back to single value fields by @sjmonson in https://github.com/vllm-project/guidellm/pull/826
* Restore startup logs and fix config environment variable support by @sjmonson in https://github.com/vllm-project/guidellm/pull/825
* Improve Pydantic commenting by @dbutenhof in https://github.com/vllm-project/guidellm/pull/818
* Rename "config" CLI command to "env" by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/849
* Added registry setup for metrics, with accompanying CLI option by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/863
* Add `--label` argument  by @sjmonson in https://github.com/vllm-project/guidellm/pull/846

### Internal refactoring and cleanup
* Add AGENTS.md by @sjmonson in https://github.com/vllm-project/guidellm/pull/714
* Refactor CSV tests by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/715
* Replace various key=value string parsers with a single utility by @sjmonson in https://github.com/vllm-project/guidellm/pull/569
* Refactor CLI into nested structure by @sjmonson in https://github.com/vllm-project/guidellm/pull/717
* Add instructions against common AI poor code quality habits by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/718
* Build ProfileArgs in BenchmarkGenerativeTextArgs by @dbutenhof in https://github.com/vllm-project/guidellm/pull/774
* [v0.7 CLI Refactor] Misc Cleanup by @sjmonson in https://github.com/vllm-project/guidellm/pull/788
* Disable reloading parent schemas by default by @sjmonson in https://github.com/vllm-project/guidellm/pull/805
* Switch BenchmarksArgs to BenchmarkScernario in output by @sjmonson in https://github.com/vllm-project/guidellm/pull/816
* Remove "rate" as an alias for profile parameters by @dbutenhof in https://github.com/vllm-project/guidellm/pull/836
* Conversation extraction script for debugging by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/848

### Bug fixes
* Add a health check for the worker processes by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/686
* Fix long import times due to processing all pydantic subclasses by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/689
* Fix custom column mapping by @sjmonson in https://github.com/vllm-project/guidellm/pull/711
* Fix CSV column misalignment across multiple benchmarks by @leehyeoklee in https://github.com/vllm-project/guidellm/pull/707
* Checks for no valid requests in processed dataset by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/709
* Fix TypeError when streaming delta has tool_calls=null by @rgerganov in https://github.com/vllm-project/guidellm/pull/752
* Fix blank HTML report by serving UI assets from GitHub Pages by @regrow1123 in https://github.com/vllm-project/guidellm/pull/744
* Fix TTFT measurement for reasoning-capable models by @soyr-redhat in https://github.com/vllm-project/guidellm/pull/742
* Make synthetic_text output_tokens optional and improve CLI errors by @rgerganov in https://github.com/vllm-project/guidellm/pull/759
* Time to first output token and related fixes by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/760
* Enable multiprocessing support for trace replay strategy by @VincentG1234 in https://github.com/vllm-project/guidellm/pull/745
* Fix unpicklable lambda collate_fn in TorchDataLoader for Python 3.14 by @rgerganov in https://github.com/vllm-project/guidellm/pull/782
* Fix report serialization for nested paths by @sjh9714 in https://github.com/vllm-project/guidellm/pull/783
* fix(data): fail fast when no mappable columns are found (#787) by @Anai-Guo in https://github.com/vllm-project/guidellm/pull/796
* fix(openai): surface streaming SSE error payloads as request failures (#743) by @Anai-Guo in https://github.com/vllm-project/guidellm/pull/795
* fix(openai): recognize reasoning_content key for TTFT calculation by @rgerganov in https://github.com/vllm-project/guidellm/pull/835
* Fix: Exclude computed fields during pydantic MP serialization by @SkiHatDuckie in https://github.com/vllm-project/guidellm/pull/845
* Fix `preprocess dataset` by @dbutenhof in https://github.com/vllm-project/guidellm/pull/842
* Fix: Add relative_timestamp column to output in Mooncake deserializer by @SkiHatDuckie in https://github.com/vllm-project/guidellm/pull/855
* Misc v0.7.0 Fixes by @sjmonson in https://github.com/vllm-project/guidellm/pull/843

### CI environment
* Drop UI CI jobs by @sjmonson in https://github.com/vllm-project/guidellm/pull/694
* Redrop nightly PyPi build by @sjmonson in https://github.com/vllm-project/guidellm/pull/695
* [GitHub Actions]: Bump actions/cache from 5.0.4 to 5.0.5 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/698
* [GitHub Actions]: Bump actions/upload-artifact from 7.0.0 to 7.0.1 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/699
* Rename tox envs by @sjmonson in https://github.com/vllm-project/guidellm/pull/701
* ci(mergify): upgrade configuration to current format by @mergify[bot] in https://github.com/vllm-project/guidellm/pull/685
* Made E2E test theoretically run better in CI by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/738
* Run a useful set of tox environments by default by @sjmonson in https://github.com/vllm-project/guidellm/pull/748
* Ensure system env vars don't taint tests by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/751
* feat: add automated docs deployment workflow by @1195343015 in https://github.com/vllm-project/guidellm/pull/747
* Add a rebase + merge based merge queue by @sjmonson in https://github.com/vllm-project/guidellm/pull/756
* fix mergify queue settings by @sjmonson in https://github.com/vllm-project/guidellm/pull/757
* fix: fix docs deploy trigger and minor doc issues by @1195343015 in https://github.com/vllm-project/guidellm/pull/758
* [GitHub Actions]: Bump docker/setup-qemu-action from 3.2.0 to 4.1.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/749
* Implement a Squash Commit PR Workflow by @sjmonson in https://github.com/vllm-project/guidellm/pull/763
* Fix update-description job by @sjmonson in https://github.com/vllm-project/guidellm/pull/766
* [GitHub Actions]: Bump docker/setup-buildx-action from 4.0.0 to 4.1.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/750
* [GitHub Actions]: Bump snok/container-retention-policy from 3.0.1 to 3.1.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/772
* [GitHub Actions]: Bump actions/checkout from 6.0.2 to 6.0.3 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/773
* Force linux LF line endings by @dbutenhof in https://github.com/vllm-project/guidellm/pull/798
* Add a HuggingFace cache step to tox-run by @sjmonson in https://github.com/vllm-project/guidellm/pull/806
* [GitHub Actions]: Bump actions/checkout from 6.0.3 to 7.0.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/815
* Update container build by @dbutenhof in https://github.com/vllm-project/guidellm/pull/819
* test: register `slow` pytest marker to silence PytestUnknownMarkWarning (#840) by @Anai-Guo in https://github.com/vllm-project/guidellm/pull/841
* Migrate docs build to nightly and fix error by @sjmonson in https://github.com/vllm-project/guidellm/pull/859
* [GitHub Actions]: Bump actions/setup-python from 6.2.0 to 6.3.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/858
* [GitHub Actions]: Bump actions/cache from 5.0.5 to 6.0.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/857

### Documentation
* Add documentation section regarding AI assistance by @dbutenhof in https://github.com/vllm-project/guidellm/pull/721
* Update README.md by @SkiHatDuckie in https://github.com/vllm-project/guidellm/pull/792
* Documentation refactoring by @dbutenhof in https://github.com/vllm-project/guidellm/pull/814
* Add troubleshooting guide by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/860
* Fix up doc linkages by @dbutenhof in https://github.com/vllm-project/guidellm/pull/870

### Dependency updates
* Bump aiohttp from 3.13.3 to 3.13.4 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/682
* Bump pillow from 12.1.1 to 12.2.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/693
* Bump python-dotenv from 1.2.1 to 1.2.2 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/702
* Bump lxml from 6.0.2 to 6.1.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/703
* Bump urllib3 from 2.6.3 to 2.7.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/727
* Bump ujson from 5.12.0 to 5.12.1 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/730
* Bump idna from 3.11 to 3.15 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/734
* Bump aiohttp from 3.13.4 to 3.14.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/771
* Bump pyarrow from 22.0.0 to 23.0.1 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/780
* Bump aiohttp from 3.14.0 to 3.14.1 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/801
* Bump ujson from 5.12.0 to 5.13.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/822
* Bump pydantic-settings from 2.12.0 to 2.14.2 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/823
* Bump msgpack from 1.1.2 to 1.2.1 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/824

## New Contributors
* @mergify[bot] made their first contribution in https://github.com/vllm-project/guidellm/pull/685
* @leehyeoklee made their first contribution in https://github.com/vllm-project/guidellm/pull/707
* @VincentG1234 made their first contribution in https://github.com/vllm-project/guidellm/pull/620
* @regrow1123 made their first contribution in https://github.com/vllm-project/guidellm/pull/744
* @1195343015 made their first contribution in https://github.com/vllm-project/guidellm/pull/747
* @soyr-redhat made their first contribution in https://github.com/vllm-project/guidellm/pull/742
* @sjh9714 made their first contribution in https://github.com/vllm-project/guidellm/pull/783
* @SkiHatDuckie made their first contribution in https://github.com/vllm-project/guidellm/pull/777
* @Anai-Guo made their first contribution in https://github.com/vllm-project/guidellm/pull/796

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.6.0...v0.7.0

## v0.7.1 (2026-07-02)

## Overview

GuideLLM v0.7.1 introduces some minor fixes for the v0.7.0 CLI changes plus finishing touches on tool-call and multi-turn.

To get started, install with:

```bash
pip install guidellm[recommended]==0.7.1
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.7.1
```

## What's Fixed

* When using a `--config` file, profile `rate`/`streams` parameters were not being passed to the benchmark. This is now fixed.
* The `--override` option now supports overriding sub-benchmark (per-strategy) constraints. For example, `--constraint kind=max_duration,seconds=30 --override constraint[0].seconds 10,20` will apply a 10 second constraint to the first strategy, and a 20 second constraint to the second strategy.
* Improved support for server tool calls. Turns can now be designated as turns where you expect the server to run a tool call, and turns where you do not expect the server to run a tool call.
* Improvements to realism of client-side tool calls. Client side tool calls now span 2 turns. The first turn is the client asking the server to request a tool call, and the second turn is the client sending the mocked tool call output to the server, and the server responding to that.
* Dataset requeue delay is now exposed in the dataset API as column `requeue_delay` (which can be remapped as usual). Requeue delay (sometimes called "think time") is the delay between the end of one turn and the start of the next turn. For synthetic text datasets, you can specify statistical delay spreads using:
  * `delay`: average requeue delay in seconds.
  * `delay_stdev`: standard deviation of requeue delay in seconds
  * `delay_min`: minimum requeue delay in seconds
  * `delay_max`: maximum requeue delay in seconds

## What's Changed
* Add auto queue rule + misc PR description fixes by @sjmonson in https://github.com/vllm-project/guidellm/pull/872
* Trace File Refactor by @SkiHatDuckie in https://github.com/vllm-project/guidellm/pull/829
* Loosen torchcodec requirement by @sjmonson in https://github.com/vllm-project/guidellm/pull/874
* Fix for being unable to specify "benchmarks" in a config by @sjmonson in https://github.com/vllm-project/guidellm/pull/875
* Fix tool call turn sequence and add improved support for server tool calls by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/839
* Support for per sub-benchmark constraints  by @sjmonson in https://github.com/vllm-project/guidellm/pull/877
* Update documentation for `--override` by @dbutenhof in https://github.com/vllm-project/guidellm/pull/880
* Expose requeue delay from datasets (#871 Cont.) by @SkiHatDuckie in https://github.com/vllm-project/guidellm/pull/876


**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.7.0...v0.7.1

## v0.7.2 (2026-07-23)

## Overview

GuideLLM v0.7.2 completes the v0.7.0 CLI transition, adds synthetic image and video data generation, adds support for generating graph images using `--output kind=plot,path=<file>`, and resolves some dependency vulnerabilities.

To get started, install with:

```bash
pip install guidellm[recommended]==0.7.2
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.7.2
```

## What's Fixed

* Fixed a bug where `console` output from `guidellm benchmark from-file` (now `guidellm export`) was crashing.
* Fixed a minor bug in the `safe_add` utility function.
* Fixed the HTML report format by locking the referenced assets to a published version.
* Fixed a crash in generating the CSV report format when using the backend `api_key` parameter.
* Fixed a redundant console refresh in the progress components.
* Restored the ability to configure a default directory for report outputs, with the GUIDELLM_DEFAULT_RESULTS_DIR environment variable.
* Improved the CLI help text for the benchmark command group.
* Updating our `transformers` dependency to 5.5.0 resolves a Critical and several High severity security vulnerabilities.

## What's Changed

* In 0.7.0 the `guidellm run` command was completely overhauled, but this introduced bugs and inconsistenies in the `guidellm benchmark from-file` (now `guidellm export`) and `guidellm preprocess dataset` commands. This release overhauls those commands to match the new `guidellm run` command. See the updated [v0.7.0 Migration Guide](https://vllm-project.github.io/guidellm/0.7.2/guides/v0.7.0_migration_guide) for more details.
* Added support for synthetic image and video data generation.
* Added support for generating graph images using `--output kind=plot,path=<file>`. The image type is inferred from the file extension, including SVG, PNG, and PDF.
* Added support for early exit from multi-strategy benchmarks when errors occur. (For example, when running a constant profile with multiple increasing rates, the benchmark will exit when the first rate fails rather than continuing to run higher rates which are likely to fail as well.). For example, `--constraint kind=max_errors,count=1,stopping_scope=all` will exit the benchmark when the first error occurs.
* With the addition of the "plot" output type, we've enhanced the `guidellm run` and `guidellm benchmark from-file` (now `guidellm export`) commands to allow generating multiple output files of the same kind. For example, `--output kind=plot,path=plots/plot.svg --output kind=plot,path=plots/plot.png` will generate two output files, one as SVG and one as PNG.
* Improved error messaging for command options using the new registry kind model: e.g., `--output` will now show the available kinds.
* Renamed the `guidellm benchmark from-file` command to `guidellm export` to better reflect its purpose.

## Changelog

### Features
* feat: synthetic image and video data generation for VLM benchmarking by @zakariaelh in https://github.com/vllm-project/guidellm/pull/732
* Feat/cross rate early exit by @ushaket in https://github.com/vllm-project/guidellm/pull/605
* feat: Add graph plotting support for benchmarks by @Prasannajaga in https://github.com/vllm-project/guidellm/pull/923
* Modernize benchmark from-file by @dbutenhof in https://github.com/vllm-project/guidellm/pull/927
* Handle repeated `--output` specifications consistently across run and from-file by @Pragadeesh122 in https://github.com/vllm-project/guidellm/pull/936
* Update `guidellm preprocess dataset` syntax to 0.7.x CLI style by @dbutenhof in https://github.com/vllm-project/guidellm/pull/943
* Added more useful error messages for kind inputs by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/949
* Renamed `guidellm benchmark from-file` to `guidellm export` by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/960

### Bug fixes
* Fix safe_add sign handling for the first value by @harivilasp in https://github.com/vllm-project/guidellm/pull/900
* Bump UI target to latest by @sjmonson in https://github.com/vllm-project/guidellm/pull/901
* Fix explicit fill-value overwrite detection in arg parser by @harivilasp in https://github.com/vllm-project/guidellm/pull/897
* Correct the CSV report format by @dbutenhof in https://github.com/vllm-project/guidellm/pull/912
* Disable redundant auto-refresh in console progress components by @whygyc in https://github.com/vllm-project/guidellm/pull/914
* Add a setting to configure the default working dir by @sjmonson in https://github.com/vllm-project/guidellm/pull/916
* Fix misleading CLI help text for benchmark command group by @bennyturns in https://github.com/vllm-project/guidellm/pull/938
### Documentation
* Cleanup docs/guides by @SkiHatDuckie in https://github.com/vllm-project/guidellm/pull/885
* docs(developing): add a proper Logging guide (#881) by @Anai-Guo in https://github.com/vllm-project/guidellm/pull/898
* Add example: benchmarking with local tokenizer and custom JSONL dataset by @miglis in https://github.com/vllm-project/guidellm/pull/915
### Internal refactoring and cleanup
* Minor logging cleanup by @dbutenhof in https://github.com/vllm-project/guidellm/pull/902
### CI environment
* Added integration tests for constraint overrides by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/887
* Allow TODO and HACK comments by @sjmonson in https://github.com/vllm-project/guidellm/pull/910
* Move tox runner setting back into tests env by @sjmonson in https://github.com/vllm-project/guidellm/pull/908
* Fix typo in pyproject.toml comment by @arijitroy003 in https://github.com/vllm-project/guidellm/pull/950
### Dependency updates
* [GitHub Actions]: Bump docker/setup-buildx-action from 4.1.0 to 4.2.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/882
* [GitHub Actions]: Bump actions/cache from 6.0.0 to 6.1.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/883
* [GitHub Actions]: Bump docker/setup-qemu-action from 4.1.0 to 4.2.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/884
* Bump development dependencies by @sjmonson in https://github.com/vllm-project/guidellm/pull/894
* Bump transformers from 5.3.0 to 5.5.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/928
* Bump pillow from 12.2.0 to 12.3.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/942
* Bump setuptools from 80.9.0 to 83.0.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/954
* [GitHub Actions]: Bump actions/setup-python from 6.3.0 to 7.0.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/957

## New Contributors
* @zakariaelh made their first contribution in https://github.com/vllm-project/guidellm/pull/732
* @harivilasp made their first contribution in https://github.com/vllm-project/guidellm/pull/900
* @whygyc made their first contribution in https://github.com/vllm-project/guidellm/pull/914
* @Prasannajaga made their first contribution in https://github.com/vllm-project/guidellm/pull/923
* @miglis made their first contribution in https://github.com/vllm-project/guidellm/pull/915
* @Pragadeesh122 made their first contribution in https://github.com/vllm-project/guidellm/pull/936
* @bennyturns made their first contribution in https://github.com/vllm-project/guidellm/pull/938
* @arijitroy003 made their first contribution in https://github.com/vllm-project/guidellm/pull/950

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.7.1...v0.7.2

## v0.7.3 (2026-07-31)

## Overview

GuideLLM v0.7.3 is a minor release to resolve a dependency vulnerability but adds a few minor improvements.

To get started, install with:

```bash
pip install guidellm[recommended]==0.7.3
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.7.3
```

## What's Fixed

* Our `transformers` dependency was locked by transitive dependencies to <5.0 in RHAI downstream, resulting in CRITICAL/HIGH CVEs. This release resolves the transitive dependency (through `huggingface_hub`) by updating to click 8.4.
* The `--output kind=plot` command is now documented, and has been updated to use `GUIDELLM_DEFAULT_RESULTS_DIR`.
* A minor improvement reports unusable LLM responses more gracefully.

## What's Changed

### Features
* bug(openai): support structured chat content metadata for OpenAI backend endpoint by @Prasannajaga in https://github.com/vllm-project/guidellm/pull/947

### Bug fixes
* Fix worker status for unusable terminal backend responses by @ushaket in https://github.com/vllm-project/guidellm/pull/615
* Make plot path behave like others by @dbutenhof in https://github.com/vllm-project/guidellm/pull/974

### Documentation
* docs: document the plot output kind by @Pragadeesh122 in https://github.com/vllm-project/guidellm/pull/971

### CI environment
* Add py.typed marker for PEP 561 compliance by @arijitroy003 in https://github.com/vllm-project/guidellm/pull/951
* Prevent .env files from tainting tests by @jaredoconnell in https://github.com/vllm-project/guidellm/pull/970

### Dependency updates
* [GitHub Actions]: Bump actions/checkout from 7.0.0 to 7.0.1 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/956
* Bump urllib3 from 2.6.3 to 2.7.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/962
* [GitHub Actions]: Bump redhat-actions/podman-login from 1.7 to 2.0 by @dependabot[bot] in https://github.com/vllm-project/guidellm/pull/977
* Update click to 8.4 by @dbutenhof in https://github.com/vllm-project/guidellm/pull/978

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.7.2...v0.7.3

## v0.7.4 (2026-09-16)

## Overview

GuideLLM v0.7.4 is a minor release which backports many bugfixes including a change to how token metrics interact with warmup/cooldown. This change will cause differences in which requests are sampled for latency metrics and will bound token event to only the tokens that occur outside warmup/cooldown.

To get started, install with:

```bash
pip install guidellm[recommended]==0.7.4
```

Or from source with:

```bash
pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.7.4
```

## What's Fixed

- Change to the methodology around tracking token latency and throughput events. See #1078 for full details of the problem.

## What's Changed

### Bug fixes

- Bound token events by when they occur in https://github.com/vllm-project/guidellm/pull/1079
- fix(openai): validate non-streaming tool calls before yielding in https://github.com/vllm-project/guidellm/pull/1099
- fix(openai): surface nested Responses streaming errors in https://github.com/vllm-project/guidellm/pull/1107
- fix(openai): accept SSE DONE markers without a space in https://github.com/vllm-project/guidellm/pull/1106
- fix: serialize audio translation filename in https://github.com/vllm-project/guidellm/pull/1096
- Pull pending requests into a worker only when a consumer is waiting in https://github.com/vllm-project/guidellm/pull/1042
- fix: use spawn multiprocessing context on macOS in https://github.com/vllm-project/guidellm/pull/1026
- Fix encoded audio sample frame metrics in https://github.com/vllm-project/guidellm/pull/987
- Fix non-streaming audio response parsing in https://github.com/vllm-project/guidellm/pull/981
- Fix multipart filenames for audio uploads in https://github.com/vllm-project/guidellm/pull/990

### CI environment

- [GitHub Actions]: Bump docker/setup-qemu-action from 4.2.0 to 4.3.0 in https://github.com/vllm-project/guidellm/pull/1129
- [GitHub Actions]: Bump redhat-actions/buildah-build from 3.0.2 to 3.1.0 in https://github.com/vllm-project/guidellm/pull/1062
- [GitHub Actions]: Bump redhat-actions/buildah-build from 2.13 to 3 in https://github.com/vllm-project/guidellm/pull/1036
- [GitHub Actions]: Bump redhat-actions/push-to-registry from 2.8 to 3 in https://github.com/vllm-project/guidellm/pull/1037
- fix: keep GHCR latest/stable as multi-arch manifests in https://github.com/vllm-project/guidellm/pull/1018

### Dependency updates

- build(deps): Bump transformers from 5.5.0 to 5.10.1 in https://github.com/vllm-project/guidellm/pull/1076
- Bump h2 from 4.3.0 to 4.4.1 in https://github.com/vllm-project/guidellm/pull/1011
- Bump aiohttp from 3.14.1 to 3.14.3 in https://github.com/vllm-project/guidellm/pull/995

**Full Changelog**: https://github.com/vllm-project/guidellm/compare/v0.7.3...v0.7.4



