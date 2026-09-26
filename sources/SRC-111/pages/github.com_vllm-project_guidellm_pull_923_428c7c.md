source: https://github.com/vllm-project/guidellm/pull/923

# feat: Add graph plotting support for benchmarks - #923

## Conversation

|
Hi |


**reviewed**

[chatgpt-codex-connector](https://github.com/apps/chatgpt-codex-connector)BotJul 10, 2026

###
**
**[chatgpt-codex-connector](https://github.com/apps/chatgpt-codex-connector)
Bot
left a comment

**left a comment**

[chatgpt-codex-connector](https://github.com/apps/chatgpt-codex-connector)Bot

There was a problem hiding this comment.

### 💡 Codex Review

Here are some automated review suggestions for this pull request.

**Reviewed commit:** `b2642c5101`


## ℹ️ About Codex in GitHub

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you

- Open a pull request for review
- Mark a draft as ready
- Comment "
[@codex](https://github.com/codex)review".

If Codex has suggestions, it will comment; otherwise it will react with 👍.

Codex can also answer questions or update the PR. Try commenting "[@codex](https://github.com/codex) address that feedback".

[src/guidellm/benchmark/outputs/plot.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-08d407d145e6a2b427bc057faef48794a37c3a294b840a97617b0816a7169d2b)Outdated


**previously requested changes**

[sjmonson](https://github.com/sjmonson)Jul 10, 2026

[src/guidellm/benchmark/outputs/plot.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-08d407d145e6a2b427bc057faef48794a37c3a294b840a97617b0816a7169d2b)Outdated

[src/guidellm/benchmark/outputs/plot.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-08d407d145e6a2b427bc057faef48794a37c3a294b840a97617b0816a7169d2b)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 10, 2026

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)Outdated

|
|


**suggested changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 14, 2026

###
**
**[SkiHatDuckie](https://github.com/SkiHatDuckie)
left a comment

**left a comment**

[SkiHatDuckie](https://github.com/SkiHatDuckie)

There was a problem hiding this comment.

Some things that I found:

[pyproject.toml](https://github.com/vllm-project/guidellm/pull/923/files#diff-50c86b7ed8ac2cf95bd48334961bf0530cdc77b5a56f852c5c61b89d735fd711)Outdated

[src/guidellm/extras/plot.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-0f42a7fc29fd9988c2c7a9f4ab0dffc725f0c37fc36b0c1a8f6cbc3828472f30)Outdated

[src/guidellm/benchmark/schemas/output.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-34cd0d877acc1654fe1d3c3004a186722c684b576f5e68f7e9d185a706e290de)Outdated

[src/guidellm/benchmark/outputs/plot.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-08d407d145e6a2b427bc057faef48794a37c3a294b840a97617b0816a7169d2b)Outdated

[src/guidellm/benchmark/outputs/plot.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-08d407d145e6a2b427bc057faef48794a37c3a294b840a97617b0816a7169d2b)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 14, 2026

[src/guidellm/benchmark/schemas/output.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-34cd0d877acc1654fe1d3c3004a186722c684b576f5e68f7e9d185a706e290de)Outdated

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)Outdated

[Prasannajaga](https://github.com/Prasannajaga)

[force-pushed](https://github.com/vllm-project/guidellm/compare/43e3603ae811ae944ff7b673113156ae11e4e1dc..a90a01bc1df1097dc679452dcfb1e94cb976f5ab)the feature/plot-graph branch from

[to](https://github.com/vllm-project/guidellm/commit/43e3603ae811ae944ff7b673113156ae11e4e1dc)

`43e3603`


`a90a01b`

[Compare](https://github.com/vllm-project/guidellm/compare/43e3603ae811ae944ff7b673113156ae11e4e1dc..a90a01bc1df1097dc679452dcfb1e94cb976f5ab)

July 15, 2026 05:40

|
|


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 15, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Almost there. I triggered the CI, and I expect at least one of your tests will fail. Also, you've been persistently failing the "DCO" check because GuideLLM is configured to require that all commits be *signed*. You can sign all your commits on your branch using the instructions in the DCO report at [https://github.com/vllm-project/guidellm/pull/923/checks?check_run_id=87277547589](https://github.com/vllm-project/guidellm/pull/923/checks?check_run_id=87277547589)

[tests/unit/benchmark/test_plot_output.py](https://github.com/vllm-project/guidellm/pull/923/files#diff-7e88319bcac5f4ffd3c1170fd565d6d61d73eb41e6857aca81b1833901db689d)Outdated

Signed-off-by: prasanna <prasannajaga9@gmail.com>

Signed-off-by: prasanna <prasannajaga9@gmail.com>

Signed-off-by: prasanna <prasannajaga9@gmail.com>

Signed-off-by: prasanna <prasannajaga9@gmail.com>

> moved lazy loading for matplot > updated doc string for now Signed-off-by: prasanna <prasannajaga9@gmail.com>

Signed-off-by: prasanna <prasannajaga9@gmail.com>

Signed-off-by: prasanna <prasannajaga9@gmail.com>

[Prasannajaga](https://github.com/Prasannajaga)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a90a01bc1df1097dc679452dcfb1e94cb976f5ab..7f3bc22a2ce687f1bdcb862dbaf1b294c2ca2acd)the feature/plot-graph branch from

[to](https://github.com/vllm-project/guidellm/commit/a90a01bc1df1097dc679452dcfb1e94cb976f5ab)

`a90a01b`


`7f3bc22`

[Compare](https://github.com/vllm-project/guidellm/compare/a90a01bc1df1097dc679452dcfb1e94cb976f5ab..7f3bc22a2ce687f1bdcb862dbaf1b294c2ca2acd)

July 15, 2026 13:00

- Removed redundant suffix validation check from GenerativeBenchmarkerPlot.finalize() - Removed redundant unit test test_finalize_raises_unsupported_suffix - Rely on PlotBenchmarkOutputArgs for output path validation Signed-off-by: prasanna <prasannajaga9@gmail.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 15, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 15, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me. I think this will benefit from [#927](https://github.com/vllm-project/guidellm/pull/927), which will also allow us to set the DPI value when using from-value with this design.

[jaredoconnell](https://github.com/jaredoconnell)dismissed

[sjmonson](https://github.com/sjmonson)’s

[stale review](https://github.com#pullrequestreview-4672544362)

July 15, 2026 17:07

Sam is on PTO and I believe his concerns have been addressed.

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

GuideLLM right now doesn't provide graph plotting benchmarks , users need a simple way to generate static, publication-quality image graphs of their benchmark runs for research papers, presentations, or automated reporting pipelines.

This PR details the design, dependency management, and implementation plan for adding static image-based benchmark data visualizations directly into GuideLLM using a new output formatter kind (

`--output kind=plot`

) by`matplotlib`

(running headless using the`'Agg'`

backend).## Changed Files & Scope:

## [MODIFY] output.py

`PlotBenchmarkOutputArgs`

model registered under`"plot"`

.`validate_plot_suffix`

field validator restricting suffixes to`ALLOWED_PLOT_SUFFIXES`

(`.png`

,`.jpg`

,`.jpeg`

,`.svg`

,`.pdf`

) and defaulting/coercing unsupported suffixes to`.png`

.## [NEW] plot.py

`GenerativeBenchmarkerPlot`

following the existing`GenerativeBenchmarkerOutput`

class interface abstraction.Latency (TTFT & E2E) vs. Request Rate (RPS)Generation Speed (TPOT & ITL) vs. Request Rate (RPS)Token Throughput vs. ConcurrencyLatency vs. Throughput (Knee Plot)Request Status Counts vs. ConcurrencyLatency Breakdown at Peak ThroughputThroughput Efficiency vs. ConcurrencyToken Throughput Mix vs. Request Rate (Stacked Area)## [MODIFY] entrypoints.py

`reimport_benchmarks_report`

to support custom filename stems. Handles single-format file path mappings directly, or builds sibling format outputs when multiple formats are requested.CLI Usage Examples:Unsupported Suffix Coercion: Automatically coerces unsupported formats (e.g.`.aaf`

) to`.png`

while preserving the custom stem:(Outputs to`./results/my_report.png`

)Supported Suffix Formats: Direct output in supported vector or image formats (e.g.`.svg`

):(Outputs to`./results/my_report.svg`

)## Alternatives Considered:

(Empty)## Visualization Layout Prototype:

Here is the graph image generated by real benchmark metrics:

## Test Plan

All code validation lint checks and MyPy static type checks successfully passed.

## 1. Automated Tests

We consolidated the test suite in

`tests/unit/benchmark/test_plot_output.py`

to cover:`test_from_args_creates_correct_instance`

: Verifies the parser resolves plot configuration arguments.`test_from_args_with_wrong_type_raises_value_error`

: Assures incorrect arguments raise a`ValueError`

.`test_path_validation_with_png`

: Asserts valid`.png`

suffix values are accepted unchanged.`test_path_validation_coerces_non_png`

: Asserts invalid extensions default to`.png`

.`test_path_validation_case_insensitive`

: Confirms uppercase suffixes like`.PNG`

are preserved.`test_invalid_args_raises_validation_error`

: Ensures invalid arg types fail fast with`ValidationError`

.`test_finalize_writes_valid_image`

: Ensures image generation writes binary contents to disk successfully.`test_finalize_resolves_directory_path`

: Confirms directory paths resolve to`benchmarks.png`

.`test_finalize_coerces_suffix_to_png`

: Checks suffix correction during finalization.`test_finalize_handles_empty_benchmarks_gracefully`

: Verifies empty runs safely generate placeholder plots.`test_finalize_with_partially_missing_metrics`

: Verifies default fallbacks when report distributions are`None`

.`test_reimport_benchmarks_report_custom_extension_plot`

: Confirms name stem preservation when re-importing custom suffixes.`test_reimport_benchmarks_report_multiple_sibling_file_path`

: Asserts name stems are preserved when exporting multiple sibling formats.Run the test suite using:

`$ uv run --with tox-uv tox -e tests -- tests/unit/benchmark/test_plot_output.py ======================= 13 passed, 3 warnings in 10.04s ========================`

## Related Issues

## Use of AI

## git log

commit

1d5287bAuthor: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 18:29:09 2026 +0530

commit

4fc6925Author: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 18:29:09 2026 +0530

commit

d7f843fAuthor: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 18:29:09 2026 +0530

commit

d0a987bAuthor: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 18:29:09 2026 +0530

commit

7471f75Author: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 18:29:09 2026 +0530

commit

aef66feAuthor: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 18:29:09 2026 +0530

commit

e08a4f7Author: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 18:29:09 2026 +0530

commit

7f3bc22Author: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 18:29:09 2026 +0530

commit

773abc4Author: prasanna prasannajaga9@gmail.com

Date: Wed Jul 15 19:01:44 2026 +0530

Signed-off-by: prasanna prasannajaga9@gmail.com