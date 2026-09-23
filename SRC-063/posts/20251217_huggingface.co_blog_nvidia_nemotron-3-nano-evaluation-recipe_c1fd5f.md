# The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator

source: https://huggingface.co/blog/nvidia/nemotron-3-nano-evaluation-recipe
published: Wed, 17 Dec 2025 13:22:18 GMT

Text Generation • 32B • Updated • 663k • 823

#
[
](https://huggingface.co#the-open-evaluation-standard-benchmarking-nvidia-nemotron-3-nano-with-nemo-evaluator)
The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator

[Enterprise + Article](https://huggingface.co/blog)

NVIDIA released [ Nemotron 3 Nano 30B
A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
with an explicitly open evaluation approach to make that distinction
clear. Alongside the model card, we are publishing the complete
evaluation recipe used to generate the results, built with the

[library, so anyone can rerun the evaluation pipeline, inspect the artifacts, and analyze the outcomes independently.](https://github.com/NVIDIA-NeMo/Evaluator/)

__NVIDIA NeMo Evaluator__We believe that open innovation is the foundation of AI progress. This level of transparency matters because most model evaluations omit critical details. Configs, prompts, harness versions, runtime settings, and logs are often missing or underspecified, and even small differences in these parameters can materially change results. Without a complete recipe, it’s nearly impossible to tell whether a model is genuinely more intelligent or simply optimized for a benchmark.

This blog shows developers exactly how to reproduce the evaluation
behind [ Nemotron 3 Nano 30B
A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
using fully open tools, configurations, and artifacts. You’ll learn how
the evaluation was run, why the methodology matters, and how to execute
the same end-to-end workflow using the NeMo Evaluator library so you can
verify results, compare models consistently, and build transparent
evaluation pipelines of your own.

##
[
](https://huggingface.co#building-a-consistent-and-transparent-evaluation-workflow-with-nemo-evaluator)
Building a consistent and transparent evaluation workflow with NeMo Evaluator

###
[
](https://huggingface.co#a-single-consistent-evaluation-system)
A single, consistent evaluation system

Developers and researchers need evaluation workflows they can rely on, not one-off scripts that behave differently from model to model. NeMo Evaluator provides a unified way to define benchmarks, prompts, configuration, and runtime behavior once, then reuse that methodology across models and releases. This avoids the common scenario where the evaluation setup quietly changes between runs, making comparisons over time difficult or misleading.

###
[
](https://huggingface.co#methodology-independent-of-inference-setup)
Methodology independent of inference setup

Model outputs can vary by inference backend and configuration, so evaluation tools should never be tied to a single inference solution. Locking an evaluation tool to one inference solution would limit its usefulness. NeMo Evaluator avoids this by separating the evaluation pipeline from the inference backend, allowing the same configuration to run against hosted endpoints, local deployments, or third-party providers. This separation enables meaningful comparisons even when you change infrastructure or inference engines.

###
[
](https://huggingface.co#built-to-scale-beyond-one-off-experiments)
Built to scale beyond one-off experiments

Many evaluation pipelines work once and then break down as the scope expands. NeMo Evaluator is designed to scale from quick, single-benchmark validation to full model card suites and repeated evaluations across multiple models. The launcher, artifact layout, and configuration model support ongoing workflows, not just isolated experiments, so teams can maintain consistent evaluation practices over time.

###
[
](https://huggingface.co#auditability-with-structured-artifacts-and-logs)
Auditability with structured artifacts and logs

Transparent evaluation requires more than final scores. Each evaluation run produces structured results and logs by default, making it easy to inspect how scores were computed, understand score calculations, debug unexpected behavior, and conduct deeper analysis. Each component of the evaluation is captured and reproducible.

###
[
](https://huggingface.co#a-shared-evaluation-standard)
A shared evaluation standard

By releasing [ Nemotron 3 Nano 30B
A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
with its

[, NVIDIA is providing a reference methodology that the community can run, inspect, and build upon. Using the same configuration and tools brings consistency to how benchmarks are selected, executed, and interpreted, enabling more reliable comparisons across models, providers, and releases.](https://github.com/NVIDIA-NeMo/Evaluator/blob/main/packages/nemo-evaluator-launcher/examples/nemotron/nano-v3-reproducibility.md)

__full evaluation recipe__##
[
](https://huggingface.co#open-evaluation-for-nemotron-3-nano)
Open evaluation for Nemotron 3 Nano

Open evaluation means publishing not just the final results, but the
full methodology behind them, so benchmarks are run consistently, and
results can be compared meaningfully over time. For [ Nemotron 3 Nano
30B
A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16),
this includes open‑source tooling, transparent configurations, and
reproducible artifacts that anyone can run end‑to‑end.

###
[
](https://huggingface.co#open-source-model-evaluation-tooling)
Open-source model evaluation tooling

[ NeMo
Evaluator](https://github.com/NVIDIA-NeMo/Evaluator/tree/main) is an
open-source library designed for robust, reproducible, and scalable
evaluation of generative models. Instead of introducing yet another
standalone benchmark runner, it acts as a unifying orchestration layer
that brings multiple evaluation harnesses under a single, consistent
interface.

Under this architecture, NeMo Evaluator integrates and coordinates
hundreds of benchmarks from many widely used evaluation harnesses,
including [ NeMo
Skills](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/eval-factory/containers/nemo_skills?version=25.11)
for Nemotron instruction-following, tool use, and agentic evaluations,
as well as the

[for base model and pre-training benchmarks, and many more (](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/eval-factory/containers/lm-evaluation-harness?version=latest)

__LM Evaluation Harness__[). Each harness retains its native logic, datasets, and scoring semantics, while NeMo Evaluator standardizes how they are configured, executed, and logged.](https://docs.nvidia.com/nemo/evaluator/latest/evaluation/benchmarks.html)

__full benchmark catalog__This provides two practical advantages: teams can run diverse benchmark categories using a single configuration without rewriting custom evaluation scripts, and results from different harnesses are stored and inspected in a consistent, predictable way, even when the underlying tasks differ. The same orchestration framework used internally by NVIDIA’s Nemotron research and model‑evaluation teams is now available to the community, enabling developers to run heterogeneous, multi‑harness evaluations through a shared, auditable workflow.

###
[
](https://huggingface.co#open-configurations)
Open configurations

We published the exact YAML configuration used for the [ Nemotron 3
Nano 30B A3B model
card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
evaluation with NeMo Evaluator. This includes:

- model inference and deployment settings
- benchmark and task selection
- benchmark-specific parameters such as sampling, repeats, and prompt templates
- runtime controls including parallelism, timeouts, and retries
- output paths and artifact layout

Using the same configuration means running the same evaluation methodology.

###
[
](https://huggingface.co#open-logs-and-artifacts)
Open logs and artifacts

Each evaluation run produces structured, inspectable outputs, including
per‑task `results.json`

files, execution logs for debugging and
auditability, and artifacts organized by task for easy comparison. This
structure makes it possible to understand not only the final scores, but
also how those scores were produced and to perform deeper analysis of
model behavior.

##
[
](https://huggingface.co#the-reproducibility-workflow)
The reproducibility workflow

Reproducing [ Nemotron 3 Nano 30B A3B model
card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
results follows a simple loop:

- Start from the released model checkpoint or hosted endpoint
- Use the
__published NeMo Evaluator config__ - Execute the evaluation with a single CLI command
- Inspect logs and artifacts, and compare results to the model card

The same workflow applies to any model you evaluate using NeMo
Evaluator. You can point the evaluation at a hosted endpoint or a local
deployment, including common inference providers such as
[ HuggingFace](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16),

[, and](https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b)

__build.nvidia.com__[. The key requirement is access to the model, either as weights you can serve or as an endpoint you can call. For this tutorial, we use the hosted endpoint on](https://openrouter.ai/chat?room=orc-1765809021-Ky770f22xVCIJI6lqlJJ)

__OpenRouter__[.](https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b)

__build.nvidia.com__##
[
](https://huggingface.co#reproducing-nemotron-3-nano-benchmark-results)
Reproducing Nemotron 3 Nano benchmark results

This tutorial reproduces the evaluation results for [ NVIDIA Nemotron
3 Nano 30B
A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
using NeMo Evaluator. The step-by-step tutorial, including the

[, is available on GitHub. Although we have focused this tutorial on the Nemotron 3 Nano 30B A3B, we also published](https://github.com/NVIDIA-NeMo/Evaluator/blob/fc304a0782c2a6ef4e2b94f27f51402352f86a98/packages/nemo-evaluator-launcher/examples/nemotron/nano-v3-reproducibility.md)

__published configs used for the model card evaluation__[.](https://github.com/NVIDIA-NeMo/Evaluator/blob/main/packages/nemo-evaluator-launcher/examples/nemotron/local_nvidia-nemotron-3-nano-30b-a3b-base.yaml)

__recipes for the base model evaluation__This walkthrough runs a comprehensive evaluation suite of the [ published configs used for the model card
evaluation](https://github.com/NVIDIA-NeMo/Evaluator/blob/fc304a0782c2a6ef4e2b94f27f51402352f86a98/packages/nemo-evaluator-launcher/examples/nemotron/nano-v3-reproducibility.md) for

[using the following benchmarks:](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)

__NVIDIA Nemotron 3 Nano 30B A3B__| Benchmark | Accuracy | Category | Description |
|---|---|---|---|
| BFCL v4 | 53.8 | Function Calling | Berkeley Function Calling Leaderboard v4 |
| LiveCodeBench (v6 2025-08–2025-05) | 68.3 | Coding | Real-world coding problems evaluation |
| MMLU-Pro | 78.3 | Knowledge | Multi-task language understanding (10-choice) |
| GPQA | 73.0 | Science | Graduate-level science questions |
| AIME 2025 | 89.1 | Mathematics | American Invitational Mathematics Exam |
| SciCode | 33.3 | Scientific Coding | Scientific programming challenges |
| IFBench | 71.5 | Instruction Following | Instruction following benchmark |
| HLE | 10.6 | Humanity's Last Exam | Expert-level questions across domains |

*For Model Card details, see the *

__NVIDIA Nemotron 3 Nano 30B A3B Model Card__. For a deep dive into the architecture, datasets, and benchmarks, read the full

__Nemotron 3 Nano Technical Report__.

###
[
](https://huggingface.co#1-install-nemo-evaluator-launcher)
1. Install NeMo Evaluator Launcher

`pip install nemo-evaluator-launcher`


###
[
](https://huggingface.co#2-set-required-environment-variables)
2. Set required environment variables

```
# NVIDIA endpoint access
export NGC_API_KEY="your-ngc-api-key"
# Hugging Face access
export HF_TOKEN="your-huggingface-token"
# Required only for judge-based benchmarks such as HLE
export JUDGE_API_KEY="your-judge-api-key"
```


*Optional but recommended for faster reruns:*
`export HF_HOME="/path/to/your/huggingface/cache"`


###
[
](https://huggingface.co#3-model-endpoint)
3. Model endpoint

The evaluation uses the NVIDIA API endpoint hosted on
[ build.nvidia.com](https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b):

```
target:
api_endpoint:
model_id: nvidia/nemotron-nano-3-30b-a3b
url: https://integrate.api.nvidia.com/v1/chat/completions
api_key_name: NGC_API_KEY
```


Evaluations can be run against common inference providers such as
[ HuggingFace](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16),

[, or](https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b)

__build.nvidia.com__[, or anywhere that the model has an available endpoint.](https://openrouter.ai/chat?room=orc-1765809021-Ky770f22xVCIJI6lqlJJ)

__OpenRouter__If you're hosting the model locally or using a different endpoint:

```
nemo-evaluator-launcher run \
--config local_nvidia_nemotron_3_nano_30b_a3b.yaml \
-o target.api_endpoint.url=http://localhost:8000/v1/chat/completions
```


###
[
](https://huggingface.co#4-run-the-full-evaluation-suite)
4. Run the full evaluation suite

Preview the run without executing using `--dry-run`

:

```
nemo-evaluator-launcher run \
--config local_nvidia_nemotron_3_nano_30b_a3b.yaml \
--dry-run
```


From the examples directory, run the evaluation using the YAML configuration provided:

```
nemo-evaluator-launcher run \
--config /path/to/examples/nemotron/local_nvidia_nemotron_3_nano_30b_a3b.yaml
```


Note that for quick testing, you can limit the number
of samples by setting `limit_samples`

:

```
nemo-evaluator-launcher run \
--config local_nvidia_nemotron_3_nano_30b_a3b.yaml \
-o evaluation.nemo_evaluator_config.config.params.limit_samples=10
```


###
[
](https://huggingface.co#5-running-an-individual-benchmark)
5. Running an individual benchmark

You can run specific benchmarks using the `-t`

flag (from the examples/nemotron
directory):

```
# Run only MMLU-Pro
nemo-evaluator-launcher run --config local_nvidia_nemotron_3_nano_30b_a3b.yaml -t ns_mmlu_pro
# Run only coding benchmarks
nemo-evaluator-launcher run --config local_nvidia_nemotron_3_nano_30b_a3b.yaml -t ns_livecodebench
# Run multiple specific benchmarks
nemo-evaluator-launcher run --config local_nvidia_nemotron_3_nano_30b_a3b.yaml -t ns_gpqa -t ns_aime2025
```


###
[
](https://huggingface.co#6-monitor-execution-and-inspect-results)
6. Monitor execution and inspect results

```
# Check status of a specific job
nemo-evaluator-launcher status
```


```
# Stream logs for a specific job
nemo-evaluator-launcher logs <job-id>
```


Results are written to the defined output directory:

```
results_nvidia_nemotron_3_nano_30b_a3b/
├── artifacts/
│ └── <task_name>/
│ └── results.json
└── logs/
└── stdout.log
```


##
[
](https://huggingface.co#interpreting-results)
Interpreting results

When reproducing evaluations, you may observe small differences in final scores across runs. This variance reflects the probabilistic nature of LLMs rather than an issue with the evaluation pipeline. Modern evaluation introduces several sources of non‑determinism: decoding settings, repeated trials, judge‑based scoring, parallel execution, and differences in serving infrastructure. All of which can lead to slight fluctuations.

The purpose of open evaluation is not to force bit-wise identical
outputs, but to deliver **methodological consistency** with clear
provenance of evaluation results. To ensure your evaluation aligns with
the reference standard, verify the following:

**Configuration**: use the published NeMo Evaluator YAML without modification, or document any changes explicitly**Benchmark selection**: run the intended tasks, task versions, and prompt templates**Inference target**: verify you are evaluating the intended model and endpoint, including chat template behavior and reasoning settings when relevant**Execution settings**: keep runtime parameters consistent, including repeats, parallelism, timeouts, and retry behavior**Outputs**: confirm artifacts and logs are complete and follow the expected structure for each task

When these elements are consistent, your results represent a valid reproduction of the methodology, even if individual runs differ slightly. NeMo Evaluator simplifies this process, tying benchmark definitions, prompts, runtime settings, and inference configuration into a single auditable workflow to minimize inconsistencies.

##
[
](https://huggingface.co#conclusion-a-more-transparent-standard-for-open-models)
Conclusion: A more transparent standard for open models

The evaluation recipe released alongside Nemotron 3 Nano represents a meaningful step toward a more transparent and reliable approach to open-model evaluation. We are moving away from evaluation as a collection of bespoke, "black box" scripts, and towards a defined system where benchmark selection, prompts, and execution semantics are encoded into a transparent workflow.

For developers and researchers, this transparency changes what it means to share results. A score is only as trustworthy as the methodology behind it and making that methodology public is what enables the community to verify claims, compare models fairly, and continue building on shared foundations. With open evaluation configurations, open artifacts, and open tooling, Nemotron 3 Nano demonstrates what that commitment to openness looks like in practice.

NeMo Evaluator supports this shift by providing a consistent
benchmarking methodology across models, releases, and inference
environments. The objective isn’t identical numbers on every run; it’s
confidence in an evaluation methodology that is explicit, inspectable,
and repeatable. And for organizations that need automated or large‑scale
evaluation pipelines, a separate microservice offering provides an
enterprise‑ready [ NeMo Evaluator
microservice](https://developer.nvidia.com/nemo-evaluator) built on
the same evaluation principles.

Use the published [ NeMo Evaluator
evaluation configuration](https://github.com/NVIDIA-NeMo/Evaluator/blob/main/packages/nemo-evaluator-launcher/examples/nemotron/nano-v3-reproducibility.md) for an end-to-end walkthrough of the evaluation recipe.

**Join the Community!**

[ NeMo
Evaluator](https://github.com/NVIDIA-NeMo/Evaluator/) is fully open
source, and community input is essential to shaping the future of open
evaluation. If there’s a benchmark you’d like us to support or an
improvement you want to propose, open an issue, or contribute directly
on GitHub. Your contributions help strengthen the ecosystem and advance
a shared, transparent standard for evaluating generative models.