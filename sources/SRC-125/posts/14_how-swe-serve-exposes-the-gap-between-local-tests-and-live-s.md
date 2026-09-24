# how-swe-serve-exposes-the-gap-between-local-tests-and-live-serving

source: https://developer.nvidia.com/blog/how-swe-serve-exposes-the-gap-between-local-tests-and-live-serving/

An AI coding agent’s patch can pass tests yet fail when the server loads a real model and handles requests. Evaluating changes to inference-serving software therefore requires checking the full serving path, including whether the system returns correct results through its public interface.

Developed with input from the SGLang team, SWE-Serve evaluates this gap with 53 tasks derived from merged changes to SGLang, an open-source system for serving large language models. Across 19 tasks with live-serving checks, the same patches passed 69.4% of the time when those checks were excluded, but only 45.9% with the complete verifier. About one in three patches that passed the other checks failed live-serving tests.

Quick links: [Read the paper](https://arxiv.org/abs/2609.26777) | [Explore the leaderboard](https://research.nvidia.com/benchmarks/swe-serve) | [Run SWE-Serve on GitHub](https://github.com/NVIDIA/swe-serve)

## What SWE-Serve tests

Existing repository-level benchmarks evaluate coding agents across general software-engineering tasks, while inference benchmarks often concentrate on kernel generation or performance optimization. SWE-Serve instead tests repository-scale changes across the inference-serving stack, including model enablement, decoding, caching, scheduling, serving APIs, and runtime performance.

To evaluate this broader engineering work, SWE-Serve turns 83 merged SGLang pull requests into 53 executable tasks across six inference-engineering families.

| Engineering family | Tasks |
|---|---|
| Speculative and advanced decoding | 14 |
| Model and backend enablement | 12 |
| Kernels, quantization, and performance | 8 |
| Serving APIs and runtime correctness | 8 |
| Caching and runtime state | 7 |
| Distributed execution and scheduling | 4 |

*Table 1. Distribution of SWE-Serve’s 53 tasks across six inference-engineering families*

Twelve tasks run on CPU, while 41 use a single NVIDIA H100. This first release doesn’t evaluate other inference engines, multi-GPU execution, or multi-node serving.

Thirty-seven tasks come from a single upstream pull request. The other 16 combine two to six related changes. In total, the benchmark draws on 83 merged SGLang pull requests. The SGLang team, a launch partner for SWE-Serve, contributed ideas for identifying challenging tasks, suggested particularly demanding pull requests, and helped shape our approach to verifying correctness.

Each task gives the agent an instruction and a containerized SGLang checkout from before the target change. The agent’s patch passes if it satisfies the task’s hidden verifier on the declared hardware. It is never compared with the reference implementation.

These are substantial changes. The median reference solution modifies 553 lines across seven files. A typical verifier has seven tests for the new behavior and 10 regression tests. Nineteen tasks start a real server, and three enforce a calibrated performance gate on an H100.

## What one task looks like

One task asks the agent to add serving support for dense and mixture-of-experts (MoE) Qwen3.5 models. Starting from a revision without Qwen3.5 support, the agent must make both the 0.8B dense model and the 35B-A3B MoE model load and serve through the normal SGLang interfaces on one H100.

Its verifier checks model registration, configuration and weight loading, image and video inputs, OpenAI-compatible requests, native batched generation, log probabilities, and execution through the MoE model’s routed experts.

## What live serving tests catch

Some failures only appear once a real server starts. The SGLang team contributed ideas for end-to-end verification, including recommendations for specific model-serving tests. SWE-Serve includes 19 tasks that load the required model and test the agent’s patch through a live serving interface.

Across these tasks, the same 627 patches pass 45.9% of the time under the complete verifier. When the live serving tests are excluded, that rate rises to 69.4%. In other words, 147 patches changed from fail to pass when the live serving tests were excluded.

The 19 tasks contain 276 live serving tests. Of those, 242 are sourced or adapted from SGLang. The remaining 34 cover behavior introduced by the corresponding merged changes when no suitable upstream test was available.

The Gemma 4 MoE task makes the result concrete. Sixteen of 33 patches passed every other check but failed at least one live serving test. Those tests cover model loading, expert routing, text and image serving, and batched generation with correct ordering and log probabilities.

A SWE-Serve pass has a narrow meaning: the patch satisfies the benchmark verifier. SWE-Serve’s tests are not SGLang’s upstream review process. They don’t establish that an agent patch or benchmark reference solution is deployable, ready to merge, or endorsed by SGLang maintainers.

## Where agents score lower

We divided the request-to-output path into four runtime domains: request handling and I/O, scheduling and request lifecycle, model execution, and KV-cache and runtime-resource management.

Across the best setting for each of the 11 models, the 26 tasks confined to one runtime domain have a 69.0% pass rate. The 27 tasks spanning more than one runtime domain have a 47.7% pass rate, a difference of 21.3 percentage points. Every model setting shows the same direction of difference.

## Performance varies widely across models

Model performance varies substantially. Across each model’s best tested configuration, mean `pass@1`

ranges from 34.6% to 75.5%. No model scores highest in every task category, and configurations with similar overall scores can have very different costs and runtimes.

We evaluated 11 models and 31 model-effort configurations with `mini-swe-agent`

, a minimal software-engineering agent that uses only Bash, under closed-book conditions. We tested the two Claude and three GPT-5.6 models at five effort levels; the other six models ran at one setting each.

Each configuration ran the complete 53-task benchmark three times. Each agent session was capped at 210 minutes and 350 steps. A task counts as solved only when the agent’s patch passes the complete verifier on the task’s declared hardware. The table reports the highest-scoring effort setting for each model.

| Model | Reasoning setting | `pass@1` (mean ± SD, 3 runs) | Mean cost/task | Mean wall time |
|---|---|---|---|---|
| Claude Opus 5 | max | 75% ± 3% | $17.40 | 57.5 min |
| GPT-5.6 Sol | max | 75% ± 6% | $12.26 | 29.5 min |
| Claude Sonnet 5 | xhigh | 64% ± 3% | $6.61 | 40.6 min |
| Kimi K3 | max | 64% ± 5% | $7.24 | 99.9 min |
| GPT-5.6 Luna | max | 64% ± 4% | $0.95 | 28.9 min |
| GPT-5.6 Terra | max | 64% ± 4% | $5.06 | 25.5 min |
| DeepSeek V4 Flash (0731) | max | 55% ± 4% | $0.69 | 36.4 min |
| GLM-5.2 | max | 48% ± 2% | $2.10 | 34.0 min |
| Gemini 3.6 Flash | high | 48% ± 6% | $4.84 | 37.3 min |
| Laguna S 2.1 | max | 46% ± 5% | $0.33 | 56.9 min |
| Inkling S | xhigh | 35% ± 3% | $0.44 | 17.6 min |

*Table 2. Best-scoring reasoning setting for each model across three runs of all 53 SWE-Serve tasks. Pass@1 shows mean ± standard deviation; cost and wall time are means per task. API-model costs use recorded token usage and frozen prices; downloadable-model costs use hosted-rate estimates*

Native harnesses didn’t improve the two leaders: GPT-5.6 Sol scored 73.6% in Codex and Claude Opus 5 scored 69.8% in Claude Code, versus 75.5% each with `mini-swe-agent`

.

Cost doesn’t map cleanly to performance. Among the four models tied at 64%, mean cost ranges from $0.95 to $7.24 per task, while mean wall time ranges from 25.5 to 99.9 minutes.

No model leads all six engineering families, and models with the same overall score can have different strengths. The top score shows that many SWE-Serve tasks are within reach of current agents; the spread shows that performance is far from uniform.

## How we validate the benchmark

We screened 786 potential task sources, built 156 executable candidates, and admitted 53.

Every admitted task was tested on its declared hardware. The unmodified repository had to fail the tests for the new behavior while continuing to pass regression tests. A reference patch had to pass the complete verifier. We also challenged the verifiers with agent-created patches, repairing, narrowing, or excluding tasks when we found a concrete problem.

Reported evaluations are closed-book. We block the public web and upstream source repositories, while allowing Hugging Face access for model weights, because an open-network pilot showed models retrieving task-specific upstream code. We audited all 1,749 trials behind the leaderboard; 196 prohibited retrieval attempts were blocked, and none succeeded. The paper describes the full qualification and evaluation-integrity process.

## Run SWE-Serve

SWE-Serve includes the task environments, verifiers, and baseline configurations. It makes the gap between passing local checks and working through the full serving path measurable.

**Explore the SWE-Serve leaderboard, then run SWE-Serve on GitHub to evaluate your coding agent on SGLang inference-engineering tasks.**

## Start the discussion at forums.developer.nvidia.com
