source: https://github.com/vllm-project/guidellm/releases?page=2

# Releases: vllm-project/guidellm

## Release list

## v0.5.1

## Overview

GuideLLM v0.5.1 fixes multiple issues introduced in v0.4.0. We recommend all user that rely on constraints other then `--max-requests`

update immediately due to some bugs in incomplete request accounting.

To get started, install with:

`pip install guidellm[recommended]==0.5.1`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.1`

## What's Fixed

- Incomplete requests now record the number of tokens received up to cancellation. This restores pre-v0.4.0 behavior.
- Audio benchmarking now works for vLLM
`>v0.7.3`

.

## Compatibility Notes

**Python**: 3.10–3.13**OS**: Linux, MacOS

## Changelog

### Bug fixes

- bug fix - html rendering when multiple percentiles are the same by
[@sjmonson](https://github.com/sjmonson)in[#515](https://github.com/vllm-project/guidellm/pull/515) - Fix Transcription / Translation endpoint usage by
[@sjmonson](https://github.com/sjmonson)in[#524](https://github.com/vllm-project/guidellm/pull/524) - Record output_tokens for incomplete requests by
[@sjmonson](https://github.com/sjmonson)in[#519](https://github.com/vllm-project/guidellm/pull/519)

### Documentation

- Fix outputs documentation with correct parameter syntax by
[@maryamtahhan](https://github.com/maryamtahhan)in[#508](https://github.com/vllm-project/guidellm/pull/508)

### CI, Workflows & Packaging

- memory ut case by
[@tukwila](https://github.com/tukwila)in[#506](https://github.com/vllm-project/guidellm/pull/506) - update db_file ut case by
[@tukwila](https://github.com/tukwila)in[#507](https://github.com/vllm-project/guidellm/pull/507) - Rerun e2e tests in CI due to flakyness by
[@sjmonson](https://github.com/sjmonson)in[#503](https://github.com/vllm-project/guidellm/pull/503) - Update settings.py by
[@DaltheCow](https://github.com/DaltheCow)in[#512](https://github.com/vllm-project/guidellm/pull/512) - Container Build Caching by
[@sjmonson](https://github.com/sjmonson)in[#509](https://github.com/vllm-project/guidellm/pull/509) - UT for src/guidellm/data/deserializers/huggingface.py by
[@tukwila](https://github.com/tukwila)in[#500](https://github.com/vllm-project/guidellm/pull/500) - mock audio translations/transcriptions functions by
[@tukwila](https://github.com/tukwila)in[#521](https://github.com/vllm-project/guidellm/pull/521)

## New Contributors

[@maryamtahhan](https://github.com/maryamtahhan)made their first contribution in[#508](https://github.com/vllm-project/guidellm/pull/508)

**Full Changelog**: `v0.5.0...v0.5.1`

## GuideLLM v0.5.0

## Overview

GuideLLM v0.5.0 is a small release adding request throttling when server is over-saturated. The release re-introduces features for dataset preprocessing and fixes various issues introduced in v0.4.0.

To get started, install with:

`pip install guidellm[recommended]==0.5.0`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.0`

## Breaking Changes

**Throughput Mode**: Throughput mode previously assumed a fixed rate.*Migration*: Throughput mode now requires manually specifying`--rate`

if used outside of sweep mode.


## What's New

**Comprehensive Preprocessing Guide**: Major documentation update covering preprocessing configs, strategies for handling short prompts, advanced column mapping, and reproducibility controls.**Over-Saturation Detection**: Automatic benchmark stopping when LLM servers are overloaded with a fine-tunable saturation detection and in-depth docs.

## What's Changed

**Dataset Preprocessing Command**: Re-enable`guidellm preprocess dataset`

command for custom prompt/output token sizing, column mapping, batch preprocessing, prompt strategies, and huggingface uploads.**Benchmark CLI**: Added`--detect-saturation`

and`--over-saturation`

for robust specification of saturation constraints.

## What's Fixed

**Assorted documentation fixes**: Documentation polish and outdated references removed.**Dataset handler**: Fixed edge case where finite length datasets would stall out when exhausted.**Connection limit**: Uncapped limits on number of connections per worker. Previously fixed at 100.

## Compatibility Notes

**Python**: 3.10–3.13**OS**: Linux, MacOS

## Changelog

### Bug fixes

- Unmask StopIteration in DataLoader by
[@sjmonson](https://github.com/sjmonson)in[#468](https://github.com/vllm-project/guidellm/pull/468) - fix encode_audio with dict input failure by
[@tukwila](https://github.com/tukwila)in[#480](https://github.com/vllm-project/guidellm/pull/480) - ut for audio and vision encode function by
[@tukwila](https://github.com/tukwila)in[#489](https://github.com/vllm-project/guidellm/pull/489) - Allow unlimited connections per-worker by
[@sjmonson](https://github.com/sjmonson)in[#488](https://github.com/vllm-project/guidellm/pull/488)

### New features

- Add over saturation constraint by
[@AlonKellner-RedHat](https://github.com/AlonKellner-RedHat)in[#438](https://github.com/vllm-project/guidellm/pull/438) - Add more metadata to benchmark report by
[@sjmonson](https://github.com/sjmonson)in[#497](https://github.com/vllm-project/guidellm/pull/497) - Add vllm id to the response by
[@toslali-ibm](https://github.com/toslali-ibm)in[#455](https://github.com/vllm-project/guidellm/pull/455) - Indicate max_concurrency for throughput and disallow running standalone without --rate by
[@sjmonson](https://github.com/sjmonson)in[#467](https://github.com/vllm-project/guidellm/pull/467) - Reenable and improve preprocess dataset by
[@jaredoconnell](https://github.com/jaredoconnell)in[#472](https://github.com/vllm-project/guidellm/pull/472)

### CI, Workflows & Packaging

- Fix container version mismatch by moving build type ARG after FROM by
[@yankay](https://github.com/yankay)in[#473](https://github.com/vllm-project/guidellm/pull/473) - update build versions in settings, workflow versioned build fix by
[@DaltheCow](https://github.com/DaltheCow)in[#465](https://github.com/vllm-project/guidellm/pull/465) - Fixes and Cleanup of CI by
[@sjmonson](https://github.com/sjmonson)in[#469](https://github.com/vllm-project/guidellm/pull/469) - Fix test failures due to collecting 0 tests by
[@sjmonson](https://github.com/sjmonson)in[#485](https://github.com/vllm-project/guidellm/pull/485) - Fix container overriding output-dir/outputs by
[@sjmonson](https://github.com/sjmonson)in[#486](https://github.com/vllm-project/guidellm/pull/486) - Switch to uv in build, test, and CI by
[@sjmonson](https://github.com/sjmonson)in[#494](https://github.com/vllm-project/guidellm/pull/494) - Bump some old dependency locks by
[@sjmonson](https://github.com/sjmonson)in[#496](https://github.com/vllm-project/guidellm/pull/496) - UT for src/guidellm/data/deserializers/file.py by
[@tukwila](https://github.com/tukwila)in[#495](https://github.com/vllm-project/guidellm/pull/495)

## New Contributors

[@toslali-ibm](https://github.com/toslali-ibm)made their first contribution in[#455](https://github.com/vllm-project/guidellm/pull/455)[@yankay](https://github.com/yankay)made their first contribution in[#473](https://github.com/vllm-project/guidellm/pull/473)

**Full Changelog**: `v0.4.0...v0.5.0`

## GuideLLM v0.4.0

**Overview**

This release marks a significant milestone with a **full architectural refactor** of the GuideLLM codebase to improve extensibility, performance, and maintainability. Key highlights include **multimodal benchmarking support** (vision and audio), a new **mock server** for testing, and comprehensive updates to output generation and statistics gathering. Additionally, the minimum supported Python version has been bumped to 3.10 to leverage modern language features.

To get started, install with:

`pip install guidellm==0.4.0`

Or from source with:

`pip install git+https://github.com/vllm-project/guidellm.git@v0.4.0`

**What's New**

**Multimodal Support**: Added comprehensive support for vision and audio workloads, including audio transcription and translation benchmarking.**Full Refactor**: Complete restructuring of core packages (`backends`

,`scheduler`

,`benchmark`

,`data`

) to support high-rate load generation and easier extensibility.**Mock Server**: Introduced a built-in mock server package to facilitate testing and development without requiring a live LLM backend.**E2E Testing**: Added a new End-to-End (E2E) testing workflow with a dedicated vLLM simulator.

**What's Changed**

**Python Requirement**: Minimum supported Python version bumped to**3.10**(previously 3.9).**CLI Arguments**:- Renamed
`--rate-type`

to`--profile`

for clarity. `--output-path`

has been split into`--output-dir`

and`--outputs`

. E.g.`--output-dir /results --outputs benchmark.json,benchmark.csv`

.`--output-path`

will continue to work in this release, but will be deprecated in the future.

- Renamed
**Container**: Updated Docker container to include`ffmpeg`

and other utilities for multimodal support.**Data Pipelines**: Reworked data pipelines to support complex multimodal datasets and better error propagation for HuggingFace loading.

**What's Fixed**

**Synthetic Data**: Fixed an issue where synthetic text datasets would lose randomness across benchmarks in the same session.**CSV Generation**: Resolved failures in CSV output generation during benchmarks.**Asyncio Stability**: Fixed various`asyncio`

and timezone-related issues in tests and schedulers.**Type Safety**: Extensive type fixes and improvements across the codebase, particularly in the`scheduler`

and`utils`

packages.

**Compatibility Notes**

**Python**: 3.10 – 3.13**OS**: Linux and macOS**Dependencies**:- Added
`torchcodec`

- Removed
`librosa`

,`pydub`

,`soundfile`

- Development workflow now uses
`pdm`

and`tox-pdm`


- Added

**New Contributors**

[@shijinye](https://github.com/shijinye)made their first contribution in PR[#327](https://github.com/vllm-project/guidellm/pull/327)[@git-jxj](https://github.com/git-jxj)made their first contribution in PR[#435](https://github.com/vllm-project/guidellm/pull/435)[@AlonKellner-RedHat](https://github.com/AlonKellner-RedHat)made their first contribution in PR[#440](https://github.com/vllm-project/guidellm/pull/440)

**Changelog**

### Refactor & Core Architecture

- PR
[#351](https://github.com/vllm-project/guidellm/pull/351): Full refactor of GuideLLM - PR
[#354](https://github.com/vllm-project/guidellm/pull/354): Scheduler package updates, rewrites, and tests expansion - PR
[#355](https://github.com/vllm-project/guidellm/pull/355): Backend package updates, rewrites, and tests expansion - PR
[#356](https://github.com/vllm-project/guidellm/pull/356): Benchmark package updates and rewrites - PR
[#357](https://github.com/vllm-project/guidellm/pull/357): Mock server package creation - PR
[#364](https://github.com/vllm-project/guidellm/pull/364): Core reintroduction of changes from main

### Multimodal & Data

- PR
[#384](https://github.com/vllm-project/guidellm/pull/384): Data pipelines rework and multimodal support - PR
[#419](https://github.com/vllm-project/guidellm/pull/419): Split multimodal group into vision and audio - PR
[#411](https://github.com/vllm-project/guidellm/pull/411): Replace librosa, pydub, and soundfile with torchcodec - PR
[#412](https://github.com/vllm-project/guidellm/pull/412): Fixes for constant rate and audio flows - PR
[#463](https://github.com/vllm-project/guidellm/pull/463): Ensure synthetic text datasets remain random across benchmarks

### Features & Enhancements

- PR
[#378](https://github.com/vllm-project/guidellm/pull/378): Complete CSV output - PR
[#432](https://github.com/vllm-project/guidellm/pull/432): Better scenario from-file support - PR
[#441](https://github.com/vllm-project/guidellm/pull/441): Support dashed arguments for benchmark args - PR
[#433](https://github.com/vllm-project/guidellm/pull/433): Switch --rates CLI arg to handle a comma separated list of values - PR
[#382](https://github.com/vllm-project/guidellm/pull/382): Advanced Prefix Cache Controls

### Infrastructure & Quality

- PR
[#397](https://github.com/vllm-project/guidellm/pull/397): Bump minimum python version to 3.10 - PR
[#440](https://github.com/vllm-project/guidellm/pull/440): Basic E2E tests - PR
[#420](https://github.com/vllm-project/guidellm/pull/420): Adapt container for new optional requirements - PR
[#415](https://github.com/vllm-project/guidellm/pull/415): Add tox command to update lock file - PR
[#442](https://github.com/vllm-project/guidellm/pull/442): Updates and Fixes for benchmark outputs, schemas, and stats calculations

### Bug Fixes

## GuideLLM v0.3.1

# GuideLLM v0.3.1

## Overview

Minor release focused on container build/tagging stability, UI polish and terminology alignment, improved OpenAI backend robustness/configurability, clearer JSON output, and new documentation (llama.cpp usage and a vLLM simulator walkthrough). Workflows now produce versioned artifacts and maintain latest/stable tags automatically.

To get started, install with:

`pip install guidellm[recommended]==0.3.1`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.3.1`

## What's New

**Recommended Extras Group**: Install OpenAI tokenizer dependencies via`guidellm[recommended]`

(tiktoken, blobfile)**llama.cpp Guide**: New docs covering llama-server, model aliasing, and metadata handling**vLLM Simulator Example**: Step-by-step “first benchmark” walkthrough with sample output images**Container Maintenance Workflow**: Scheduled cleanup of old PR images; auto-retag latest and stable

## What's Changed

**UI Polish**: Clearer labels (e.g., “Time Per Request”, “Measured RPS (Mean)”) and slider text**Versioned Reports**: PROD/STAGING report URLs pinned to versioned UI builds**Container Build System**: New top-level Containerfile using Fedora Python minimal + PDM; build type via GUIDELLM_BUILD_TYPE**Metrics JSON Output**: UTF-8 encoding with pretty-printed, indented JSON**Endpoint Max Tokens Keys**: Output-token limit now governed per-endpoint via`GUIDELLM__OPENAI__MAX_OUTPUT_KEY`


## What's Fixed

**Streaming Robustness**: Safely handle missing delta.content for chat streams**Endpoint Token Keys**: Configurable max output key per endpoint (max_tokens vs max_completion_tokens)**CI Stability**: Fixes to RC tagging, GH Pages publish paths, and workflow typos; disable dry-run for image cleanup

## Compatibility Notes

**Python**: 3.9–3.13**OS**: Linux and MacOS**Dependencies**: Optional extras via`guidellm[recommended]`

; currently includes packages for OpenAI's tokenizer but may expand in the future**Breaking**: Previously all endpoints used both`max_tokens`

and`max_completion_tokens`

to bound output; this caused issues with some servers- The key is now controlled per-endpoint (defaults to
`max_tokens`

for legacy`completions`

and`max_completion_tokens`

for`chat/completions`

)

- The key is now controlled per-endpoint (defaults to

## New Contributors

: made their first contribution in PR[@rgerganov](https://github.com/rgerganov)[#318](https://github.com/vllm-project/guidellm/pull/318): made their first contribution in PR[@git-jxj](https://github.com/git-jxj)[#316](https://github.com/vllm-project/guidellm/pull/316): made their first contribution in PR[@psydok](https://github.com/psydok)[#372](https://github.com/vllm-project/guidellm/pull/372)

## Changelog

- UI & Presentation
- Backend
- Containers & CI
[#254](https://github.com/vllm-project/guidellm/pull/254): Overhaul container image and CI (new top-level Containerfile, PDM build)[#379](https://github.com/vllm-project/guidellm/pull/379): Container CI bugfix and disable dry-run on image cleaner[#310](https://github.com/vllm-project/guidellm/pull/310): Use versioned builds (and version-pinned report links)[#389](https://github.com/vllm-project/guidellm/pull/389): Fix container RC tag[#398](https://github.com/vllm-project/guidellm/pull/398): Fix container RC tag (Attempt 2)[#400](https://github.com/vllm-project/guidellm/pull/400): Fix failing CI[#401](https://github.com/vllm-project/guidellm/pull/401): Fix typo in CI[#301](https://github.com/vllm-project/guidellm/pull/301): Correct UI src path in workflows (publish_dir)

- Output & Tooling
[#372](https://github.com/vllm-project/guidellm/pull/372): Pretty-print and UTF-8 encode metrics JSON files

- Documentation
- Packaging
[#313](https://github.com/vllm-project/guidellm/pull/313): Add recommended extras group


Changelog link: `v0.3.0...v0.3.1`

## GuideLLM v0.3.0

**GuideLLM v0.3.0**

**Overview**

A major (non-semantic versioning sense) release introducing the GuideLLM web UI, containerized benchmarking, dataset preprocessing, and significant workflow improvements. This release transitions the project from the Neural Magic organization into the vLLM project ecosystem while expanding benchmarking capabilities and improving developer experience.

To get started, install with:

`pip install guidellm==0.3.0`

Or from source with:

`pip install git+https://github.com/vllm-project/guidellm.git@v0.3.0`

**What's New**

**GuideLLM Web UI**: Complete frontend interface with interactive charts and data visualization for benchmark results**Dataset Preprocessing**: New preprocess command to filter datasets by token distribution and save to local files or Hugging Face Hub**Containerized Benchmarking**: Docker support with configurable environment variables for streamlined deployment**Benchmark Scenarios**: Support for file-based benchmark configuration with Pydantic validation**HTML Report Generation**: Static HTML reports with embedded visualization data

**What's Changed**

**Project Migration**: Transitioned from neuralmagic to vllm-project GitHub organization with updated links and branding**Improved Scheduling**: Unified RPS and concurrent scheduler paths for better multi-turn conversation support**Enhanced OpenAI Backend**: Added support for custom headers, SSL verification control, query parameters, and request body modifications**Development Workflow**: Streamlined CI/CD with unified test execution, pre-commit improvements, and artifact management**Synthetic Data Generator**: Added prefix caching controls and unique prompt generation

**What's Fixed**

**Metric Calculation**: Fixed double-counting issues in token calculations and concurrency change events**Event Loop Errors**: Resolved "Event loop Closed" errors in HTTP client connection pooling**Token Counting**: Fixed max token limits in synthetic data generator and first decode token counting**Display Issues**: Corrected metric units display and Firefox compatibility for web UI

**Compatibility Notes**

- Python: 3.9–3.13
- OS: Linux and macOS
- Dependencies: Updated to latest Pydantic, locked Click to support Python 3.9
**Breaking**: Removed several UI workflow components and husky pre-commit hooks**Breaking**: Updated project URLs from vllm-project to neuralmagic organization

**New Contributors**

[@chewong](https://github.com/chewong)made their first contribution in[#168](https://github.com/vllm-project/guidellm/pull/168)[@dagrayvid](https://github.com/dagrayvid)made their first contribution in[#173](https://github.com/vllm-project/guidellm/pull/173)[@TomerG711](https://github.com/TomerG711)made their first contribution in[#162](https://github.com/vllm-project/guidellm/pull/162)[@wangchen615](https://github.com/wangchen615)made their first contribution in[#123](https://github.com/vllm-project/guidellm/pull/123)[@kyolebu](https://github.com/kyolebu)made their first contribution in[#207](https://github.com/vllm-project/guidellm/pull/207)[@rymc](https://github.com/rymc)made their first contribution in[#223](https://github.com/vllm-project/guidellm/pull/223)[@jaredoconnell](https://github.com/jaredoconnell)made their first contribution in[#185](https://github.com/vllm-project/guidellm/pull/185)[@natoscott](https://github.com/natoscott)made their first contribution in[#231](https://github.com/vllm-project/guidellm/pull/231)[@kdelee](https://github.com/kdelee)made their first contribution in[#230](https://github.com/vllm-project/guidellm/pull/230)[@Harshith-umesh](https://github.com/Harshith-umesh)made their first contribution in[#240](https://github.com/vllm-project/guidellm/pull/240)[@tjandy98](https://github.com/tjandy98)made their first contribution in[#256](https://github.com/vllm-project/guidellm/pull/256)[@tukwila](https://github.com/tukwila)made their first contribution in[#302](https://github.com/vllm-project/guidellm/pull/302)

**Changelog**

### Major Features

[#169](https://github.com/vllm-project/guidellm/pull/169): Implement complete GuideLLM UI with interactive charts and Redux state management[#162](https://github.com/vllm-project/guidellm/pull/162): Add dataset preprocessing command with HuggingFace integration[#123](https://github.com/vllm-project/guidellm/pull/123): Add containerized benchmarking support with Docker configuration[#99](https://github.com/vllm-project/guidellm/pull/99): Add support for benchmark scenarios with Pydantic validation[#218](https://github.com/vllm-project/guidellm/pull/218): Implement HTML output generation with embedded data

### Infrastructure & Workflows

[#233](https://github.com/vllm-project/guidellm/pull/233): Unify RPS and concurrent scheduler paths for improved performance[#215](https://github.com/vllm-project/guidellm/pull/215): Complete UI build pipeline and GitHub Pages workflows[#231](https://github.com/vllm-project/guidellm/pull/231): Migrate project from vllm-project to neuralmagic organization[#190](https://github.com/vllm-project/guidellm/pull/190): Add container build jobs to all workflows

### Backend Improvements

[#230](https://github.com/vllm-project/guidellm/pull/230): Add CLI options for custom headers and SSL verification[#146](https://github.com/vllm-project/guidellm/pull/146): Allow extra query parameters for OpenAI server requests[#184](https://github.com/vllm-project/guidellm/pull/184): Add remove_from_body parameter to OpenAIHTTPBackend[#183](https://github.com/vllm-project/guidellm/pull/183): Add prefix caching controls to synthetic dataset generator

### Bug Fixes & Quality

[#266](https://github.com/vllm-project/guidellm/pull/266): Fix metric accumulation errors at extreme concurrency changes[#188](https://github.com/vllm-project/guidellm/pull/188): Fix "Event loop Closed" error in HTTP client pooling[#173](https://github.com/vllm-project/guidellm/pull/173): Fix double counting of tokens and warmup percentage calculation[#170](https://github.com/vllm-project/guidellm/pull/170): Fix max token limits in synthetic data generator

### Developer Experience

## GuideLLM v0.2.1

## Summary

- Bug fixes enabling HF datasets and local data files for benchmarking that were resulting in crashes due to improper calls into datasets load_dataset function
- Refactored CI/CD system based on the latest standards for releases

## What's Changed

- Update version on main to 0.3.0 to begin work on the next release by
[@markurtz](https://github.com/markurtz)in[#127](https://github.com/vllm-project/guidellm/pull/127) - Fix python versions for display in README.md by
[@markurtz](https://github.com/markurtz)in[#128](https://github.com/vllm-project/guidellm/pull/128) - Fix logging by
[@hhy3](https://github.com/hhy3)in[#129](https://github.com/vllm-project/guidellm/pull/129) - Data and request fixes for real data / chat_completions pathways by
[@markurtz](https://github.com/markurtz)in[#131](https://github.com/vllm-project/guidellm/pull/131) - Fix argument error in nightly unit tests by
[@sjmonson](https://github.com/sjmonson)in[#132](https://github.com/vllm-project/guidellm/pull/132) - Add docs for data/datasets and how to configure them in GuideLLM by
[@markurtz](https://github.com/markurtz)in[#137](https://github.com/vllm-project/guidellm/pull/137) - Refactor CI/CD system based on latest standardization for upstreams by
[@markurtz](https://github.com/markurtz)in[#135](https://github.com/vllm-project/guidellm/pull/135)

## New Contributors

**Full Changelog**: `v0.2.0...v0.2.1`

## GuideLLM v0.2.0

## Summary

**Minimal Execution Overheads**- Refactor enabling async multi-process/threaded design with just 0.16% overhead in synchronous and 99.9% accuracy for constant requests

**Robust Accuracy + Monitoring**- Built-in timings and diagnostics added to validate performance and catch regressions

**Flexible Benchmarking Profiles**- Prebuilt support for synchronous, concurrent (added), throughput, constant rate, poisson rate, and sweep modes

**Unified Input/Output Formats**- JSON, YAML, CSV, and console output now standardized

**Multi-Use Data Loaders**- Native support for HuggingFace datasets, file-based data, and synthetic samples with fixes for previous flows and expanded support

**Pluggable Backends via OpenAI-Compatible APIs**- Redeisgned to work out of the box with OpenAI style HTTP servers, easily expandable to other interfaces and servers. Fixed issues related to improper token lengths and more


## What's Changed

- Add summary metrics to saved json file by
[@anmarques](https://github.com/anmarques)in[#46](https://github.com/vllm-project/guidellm/pull/46) - ADD TGI docs by
[@philschmid](https://github.com/philschmid)in[#43](https://github.com/vllm-project/guidellm/pull/43) - Add missing vllm docs link by
[@eldarkurtic](https://github.com/eldarkurtic)in[#50](https://github.com/vllm-project/guidellm/pull/50) - Change default "role" from "system" to "user" by
[@philschmid](https://github.com/philschmid)in[#53](https://github.com/vllm-project/guidellm/pull/53) - FIX TGI example by
[@philschmid](https://github.com/philschmid)in[#51](https://github.com/vllm-project/guidellm/pull/51) - Revert Summary Metrics and Expand Test Coverage to Stabilize Nightly/Main CI by
[@markurtz](https://github.com/markurtz)in[#58](https://github.com/vllm-project/guidellm/pull/58) - [Dataset]: Iterate through benchmark dataset once by
[@parfeniukink](https://github.com/parfeniukink)in[#48](https://github.com/vllm-project/guidellm/pull/48) - Replace busy wait in async loop with a Semaphore by
[@sjmonson](https://github.com/sjmonson)in[#80](https://github.com/vllm-project/guidellm/pull/80) - Add backend_kwargs to generate_benchmark_report by
[@jackcook](https://github.com/jackcook)in[#78](https://github.com/vllm-project/guidellm/pull/78) - Drop request count check from throughput sweep profile by
[@sjmonson](https://github.com/sjmonson)in[#89](https://github.com/vllm-project/guidellm/pull/89) - Rework Backend to Native HTTP Requests and Enhance API Compatibility & Performance by
[@markurtz](https://github.com/markurtz)in[#91](https://github.com/vllm-project/guidellm/pull/91) - Multi Process Scheduler Implementation, Benchmarker, and Report Generation Refactor by
[@markurtz](https://github.com/markurtz)in[#96](https://github.com/vllm-project/guidellm/pull/96) - Update the README by
[@sjmonson](https://github.com/sjmonson)in[#112](https://github.com/vllm-project/guidellm/pull/112) - Fix units for Req Latency in output to seconds by
[@smalleni](https://github.com/smalleni)in[#113](https://github.com/vllm-project/guidellm/pull/113) - Fix/non integer rates by
[@thameem-abbas](https://github.com/thameem-abbas)in[#116](https://github.com/vllm-project/guidellm/pull/116) - Output support expansion, code hygiene, and tests by
[@markurtz](https://github.com/markurtz)in[#117](https://github.com/vllm-project/guidellm/pull/117) - Bump min python to 3.9 by
[@sjmonson](https://github.com/sjmonson)in[#121](https://github.com/vllm-project/guidellm/pull/121) - v0.2.0 Version Update and Docs Expansions by
[@markurtz](https://github.com/markurtz)in[#118](https://github.com/vllm-project/guidellm/pull/118) - Fix issue if async task count does not evenly divide accross process pool by
[@sjmonson](https://github.com/sjmonson)in[#120](https://github.com/vllm-project/guidellm/pull/120) - Readme grammar updates and cleanup by
[@markurtz](https://github.com/markurtz)in[#124](https://github.com/vllm-project/guidellm/pull/124) - Update CICD flows to enable automated releases and match the feature set laid out in
[#56](https://github.com/vllm-project/guidellm/issues/56)by[@markurtz](https://github.com/markurtz)in[#125](https://github.com/vllm-project/guidellm/pull/125) - CI/CD Build Fixes for Release by
[@markurtz](https://github.com/markurtz)in[#126](https://github.com/vllm-project/guidellm/pull/126)

## New Contributors

[@anmarques](https://github.com/anmarques)made their first contribution in[#46](https://github.com/vllm-project/guidellm/pull/46)[@philschmid](https://github.com/philschmid)made their first contribution in[#43](https://github.com/vllm-project/guidellm/pull/43)[@eldarkurtic](https://github.com/eldarkurtic)made their first contribution in[#50](https://github.com/vllm-project/guidellm/pull/50)[@sjmonson](https://github.com/sjmonson)made their first contribution in[#80](https://github.com/vllm-project/guidellm/pull/80)[@jackcook](https://github.com/jackcook)made their first contribution in[#78](https://github.com/vllm-project/guidellm/pull/78)[@smalleni](https://github.com/smalleni)made their first contribution in[#113](https://github.com/vllm-project/guidellm/pull/113)[@thameem-abbas](https://github.com/thameem-abbas)made their first contribution in[#116](https://github.com/vllm-project/guidellm/pull/116)

**Full Changelog**: `v0.1.0...v0.2.0`

## GuideLLM v0.1.0

## What's Changed

Initial release of GuideLLM with version 0.1.0! This core release adds the basic structure, infrastructure, and code for benchmarking LLM deployments across several different use cases utilizing a CLI interface and terminal output. Further improvements are coming soon!

- Support added for general OpenAI backends and any text-input-based model served through those
- Support added for emulated, transformers, and file-based datasets
- Support added for general file storage of the full benchmark/evaluation that was run
- Full support for different benchmark types including sweeps, synchronous, throughput, constant, and poison enabled through new scheduler and executor interfaces built on top of Python's asyncio

## New Contributors

[@DaltheCow](https://github.com/DaltheCow)made their first contribution in[#4](https://github.com/vllm-project/guidellm/pull/4)[@markurtz](https://github.com/markurtz)made their first contribution in[#3](https://github.com/vllm-project/guidellm/pull/3)[@rgreenberg1](https://github.com/rgreenberg1)made their first contribution in[#21](https://github.com/vllm-project/guidellm/pull/21)[@jennyyangyi-magic](https://github.com/jennyyangyi-magic)made their first contribution in[#35](https://github.com/vllm-project/guidellm/pull/35)

**Full Changelog**: [https://github.com/neuralmagic/guidellm/commits/v0.1.0](https://github.com/neuralmagic/guidellm/commits/v0.1.0)