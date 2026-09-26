source: https://github.com/vllm-project/guidellm/tree/v0.6.0

**GuideLLM** is a platform for evaluating how language models perform under real workloads and configurations. It simulates end-to-end interactions with OpenAI-compatible and vLLM-native servers, generates workload patterns that reflect production usage, and produces detailed reports that help teams understand system behavior, resource needs, and operational limits. GuideLLM supports real and synthetic datasets, multimodal inputs, and flexible execution profiles, giving engineering and ML teams a consistent framework for assessing model behavior, tuning deployments, and planning capacity as their systems evolve.

GuideLLM gives teams a clear picture of performance, efficiency, and reliability when deploying LLMs in production-like environments.

**Captures complete latency and token-level statistics for SLO-driven evaluation**, including full distributions for TTFT, ITL, and end-to-end behavior.**Generates realistic, configurable traffic patterns**across synchronous, concurrent, and rate-based modes, including reproducible sweeps to identify safe operating ranges.**Supports both real and synthetic multimodal datasets**, enabling controlled experiments and production-style evaluations in one framework.**Produces standardized, exportable reports for dashboards, analysis, and regression tracking**, ensuring consistency across teams and workflows.**Delivers high-throughput, extensible benchmarking**with multiprocessing, threading, async execution, and a flexible CLI/API for customization or quickstarts.

Many tools benchmark endpoints, not models, and miss the details that matter for LLMs. GuideLLM focuses exclusively on LLM-specific workloads, measuring TTFT, ITL, output distributions, and dataset-driven variation. It fits into everyday engineering tasks by using standard Python interfaces and HuggingFace datasets instead of custom formats or research-only pipelines. It is also built for performance, supporting high-rate load generation and accurate scheduling far beyond simple scripts or example benchmarks. The table below highlights how this approach compares to other options.

| Tool | CLI | API | High Perf | Full Metrics | Data Modalities | Data Sources | Profiles | Backends | Endpoints | Output Types |
|---|---|---|---|---|---|---|---|---|---|---|
| GuideLLM | ✅ | ✅ | ✅ | ✅ | Text, Image, Audio, Video | HuggingFace, Files, Synthetic, Custom | Synchronous, Concurrent, Throughput, Constant, Poisson, Sweep | OpenAI-compatible | /completions, /chat/completions, /audio/translation, /audio/transcription | console, json, csv, html |
|

[genai-bench](https://github.com/sgl-project/genai-bench)[llm-perf](https://github.com/ray-project/llmperf)[ollama-benchmark](https://github.com/aidatatools/ollama-benchmark)[vllm/benchmarks](https://github.com/vllm-project/vllm/tree/main/benchmarks)This section summarizes the newest capabilities available to users and outlines the current areas of development. It helps readers understand how the platform is evolving and what to expect next.

**Recent Additions**

- New refactored architecture enabling high-rate load generation at scale and a more extensible interface for additional backends, data pipelines, load generation schedules, benchmarking constraints, and output formats.
- Added multimodal benchmarking support for image, video, and audio workloads across chat completions, transcription, and translation APIs.
- Broader metrics collection, including richer statistics for visual, audio, and text inputs such as image sizes, audio lengths, video frame counts, and word-level data.

**Active Development**

- Generation of synthetic multimodal datasets for controlled experimentation across images, audio, and video.
- Extended prefixing options for testing system-prompt and user-prompt variations.
- Multi-turn conversation capabilities for benchmarking chat agents and dialogue systems.
- Speculative decoding specific views and outputs.

The Quick Start shows how to install GuideLLM, launch a server, and run your first benchmark in a few minutes.

Before installing, ensure you have the following prerequisites:

- OS: Linux or MacOS
- Python: 3.10 - 3.13

Install the latest GuideLLM release from PyPi using `pip`

:

`pip install guidellm[recommended]`

Or install from source:

`pip install git+https://github.com/vllm-project/guidellm.git`

Or run the latest container from [ghcr.io/vllm-project/guidellm](https://github.com/vllm-project/guidellm/pkgs/container/guidellm):

```
podman run \
--rm -it \
-v "./results:/results:rw" \
-e GUIDELLM_TARGET=http://localhost:8000 \
-e GUIDELLM_PROFILE=sweep \
-e GUIDELLM_MAX_SECONDS=30 \
-e GUIDELLM_DATA="prompt_tokens=256,output_tokens=128" \
ghcr.io/vllm-project/guidellm:latest
```

Start any OpenAI-compatible endpoint. For vLLM:

`vllm serve "neuralmagic/Meta-Llama-3.1-8B-Instruct-quantized.w4a16"`

Verify the server is running at `http://localhost:8000`

.

Run a sweep that identifies the maximum performance and maximum rates for the model:

```
guidellm benchmark \
--target "http://localhost:8000" \
--profile sweep \
--max-seconds 30 \
--data "prompt_tokens=256,output_tokens=128"
```

You will see progress updates and per-benchmark summaries during the run, as given below:

After the benchmark completes, GuideLLM saves all results into the output directory you specified (default: the current directory). You'll see a summary printed in the console along with a set of file locations (`.json,`

`.csv`

, `.html`

) that contain the full results of the run.

The following section, **Output Files and Reports**, explains what each file contains and how to use them for analysis, visualization, or automation.

After running the Quick Start benchmark, GuideLLM writes several output files to the directory you specified. Each one focuses on a different layer of analysis, ranging from a quick on-screen summary to fully structured data for dashboards and regression pipelines.

**Console Output**

The console provides a lightweight summary with high-level statistics for each benchmark in the run. It's useful for quick checks to confirm that the server responded correctly, the load sweep completed, and the system behaved as expected. Additionally, the output tables can be copied and pasted into spreadsheet software using `|`

as the delimiter. The sections will look similar to the following:

**benchmarks.json**

This file is the authoritative record of the entire benchmark session. It includes configuration, metadata, per-benchmark statistics, and sample request entries with individual request timings. Use it for debugging, deeper analysis, or loading into Python with `GenerativeBenchmarksReport`

.

Alternatively, a yaml version of this file can be generated for easier human readability with the same content as `benchmarks.json`

using the `--outputs yaml`

argument.

**benchmarks.csv**

This file provides a compact tabular view of each benchmark with the fields most commonly used for reporting—throughput, latency percentiles, token counts, and rate information. It opens cleanly in spreadsheets and BI tools and is well-suited for comparisons across runs.

**benchmarks.html**

The HTML report provides a visual summary of results, including charts of latency distributions, throughput behavior, and generation patterns. It's ideal for quick exploration or sharing with teammates without requiring them to parse JSON.

GuideLLM supports a wide range of LLM benchmarking workflows. The examples below show how to run typical scenarios and highlight the parameters that matter most. For a complete list of arguments, details, and options, run `guidellm benchmark run --help`


Simmulating different applications requires different traffic shapes. This example demonstrates rate-based load testing using a constant profile at 10 requests per second, running for 20 seconds with synthetic data of 128 prompt tokens and 256 output tokens.

```
guidellm benchmark \
--target http://localhost:8000 \
--profile constant \
--rate 10 \
--max-seconds 20 \
--data "prompt_tokens=128,output_tokens=256"
```

**Key parameters:**

`--profile`

: Defines the traffic pattern - options include`synchronous`

(sequential requests),`concurrent`

(parallel users),`throughput`

(maximum capacity),`constant`

(fixed requests/sec),`poisson`

(randomized requests/sec), or`sweep`

(automatic rate exploration)`--rate`

: The numeric rate value whose meaning depends on profile - for`sweep`

it's the number of benchmarks, for`concurrent`

it's simultaneous requests, for`constant`

/`poisson`

it's requests per second`--max-seconds`

: Maximum duration in seconds for each benchmark run (can also use`--max-requests`

to limit by request count instead)

GuideLLM supports HuggingFace datasets, local files, and synthetic data. This example loads the CNN DailyMail dataset from HuggingFace and maps the article column to prompts while using the summary token count column to determine output lengths.

```
guidellm benchmark run \
--target http://localhost:8000 \
--data "abisee/cnn_dailymail" \
--data-args '{"name": "3.0.0"}' \
--data-column-mapper '{"text_column":"article"}'
```

**Key parameters:**

`--data`

: Data source specification - accepts HuggingFace dataset IDs (prefix with`hf:`

), local file paths (`.json`

,`.csv`

,`.jsonl`

,`.txt`

), or synthetic data configs (JSON object or`key=value`

pairs like`prompt_tokens=256,output_tokens=128`

)`--data-args`

: Arguments for loading the dataset. Seefor valid options.`datasets.load_dataset`

`--data-column-mapper`

: JSON object of arguments for dataset creation - commonly used to specify column mappings like`text_column`

,`output_tokens_count_column`

, or HuggingFace dataset parameters`--data-samples`

: Number of samples to use from the dataset - use`-1`

(default) for all samples with dynamic generation, or specify a positive integer to limit sample count`--processor`

: Tokenizer or processor name used for generating synthetic data - if not provided and required for the dataset, automatically loads from the model; accepts HuggingFace model IDs or local paths

You can benchmark chat completions, text completions, or other supported request types. This example configures the benchmark to test chat completions API using a custom dataset file, with GuideLLM automatically formatting requests to match the chat completions schema.

```
guidellm benchmark \
--target http://localhost:8000 \
--request-type chat_completions \
--data path/to/data.json
```

**Key parameters:**

`--request-type`

: Specifies the API endpoint format - options include`chat_completions`

(chat API format),`completions`

(text completion format),`audio_transcription`

(audio transcription), and`audio_translation`

(audio translation).

Built-in scenarios bundle schedules, dataset settings, and request formatting to standardize common testing patterns. This example uses the pre-configured chat scenario which includes appropriate defaults for chat model evaluation, with any additional CLI arguments overriding the scenario's settings.

`guidellm benchmark --scenario chat --target http://localhost:8000`

**Key parameters:**

`--scenario`

: Built-in scenario name or path to a custom scenario configuration file - built-in options include pre-configured testing patterns for common use cases; CLI options passed alongside this will override the scenario's default settings

Warm-up, cooldown, and maximum limits help ensure stable, repeatable measurements. This example runs a concurrent benchmark with 16 parallel requests, using 10% warmup and cooldown periods to exclude initialization and shutdown effects, while limiting the test to stop if more than 5 errors occur.

```
guidellm benchmark \
--target http://localhost:8000 \
--profile concurrent \
--rate 16 \
--warmup 0.1 \
--cooldown 0.1 \
--max-errors 5 \
--data "prompt_tokens=256,output_tokens=128" \
--detect-saturation
```

**Key parameters:**

`--warmup`

: Warm-up specification - values between 0 and 1 represent a percentage of total requests/time, values ≥1 represent absolute request or time units.`--cooldown`

: Cool-down specification - same format as warmup, excludes final portion of benchmark from analysis to avoid shutdown effects`--max-seconds`

: Maximum duration in seconds for each benchmark before automatic termination`--max-requests`

: Maximum number of requests per benchmark before automatic termination`--max-errors`

: Maximum number of individual errors before stopping the benchmark entirely`--data`

: Data to use for benchmarking - synthetic data with 256 input and 128 output tokens`--detect-saturation`

: Enable over-saturation detection to automatically stop benchmarks when the model becomes over-saturated (see also`--over-saturation`

for more advanced control)

Developers interested in extending GuideLLM can use the project's established development workflow. Local setup, environment activation, and testing instructions are outlined in [DEVELOPING.md](https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md). This guide explains how to run the benchmark suite, validate changes, and work with the CLI or API during development. Contribution standards are documented in [CONTRIBUTING.md](https://github.com/vllm-project/guidellm/blob/main/CONTRIBUTING.md), including coding conventions, commit structure, and review guidelines. These standards help maintain stability as the platform evolves. The [CODE_OF_CONDUCT.md](https://github.com/vllm-project/guidellm/blob/main/CODE_OF_CONDUCT.md) outlines expectations for respectful and constructive participation across all project spaces. For contributors who want deeper reference material, the documentation covers installation, backends, datasets, metrics, output types, and architecture. Reviewing these topics is useful when adding new backends, request types, or data integrations. Release notes and changelogs are linked from the GitHub Releases page and provide historical context for ongoing work.

The complete documentation provides the details that do not fit in this README. It includes installation steps, backend configuration, dataset handling, metrics definitions, output formats, tutorials, and an architecture overview. These references help you explore the platform more deeply or integrate it into existing workflows.

Notable docs are given below:

- This guide provides step-by-step instructions for installing GuideLLM, including prerequisites and setup tips.**Installation Guide**- A comprehensive overview of supported backends and how to set them up for use with GuideLLM.**Backends Guide**- Information on supported datasets, including how to use them for benchmarking.**Data/Datasets Guide**- Detailed explanations of the metrics used in GuideLLM, including definitions and how to interpret them.**Metrics Guide**- Information on the different output formats supported by GuideLLM and how to use them.**Outputs Guide**- A detailed look at GuideLLM's design, components, and how they interact.**Architecture Overview**

GuideLLM is licensed under the [Apache License 2.0](https://github.com/vllm-project/guidellm/blob/main/LICENSE).

If you find GuideLLM helpful in your research or projects, please consider citing it:

```
@misc{guidellm2024,
title={GuideLLM: Scalable Inference and Optimization for Large Language Models},
author={Neural Magic, Inc.},
year={2024},
howpublished={\url{https://github.com/vllm-project/guidellm}},
}
```