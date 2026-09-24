# how-to-evaluate-ai-agents-from-tool-calls-to-task-completion

source: https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/

When you ship an [AI agent](https://www.nvidia.com/en-us/glossary/ai-agents/), the key question is whether it can execute a chain of work across dozens of sequential tool calls against a live environment, and recover when a step fails. Scoring whether the model *sounds* right tells you almost nothing about whether the work *finished*.

That gap is why agent evaluation has had to evolve from scoring a single function call to scoring an entire task, with tool calling as the connective tissue underneath. This post traces that arc and explains why nearly every serious agent benchmark now rests on tool use.

## Why isn’t standard LLM benchmarking enough?

The original harnesses were built for static tasks. The first model-agnostic, open-source harness decoupled the model from the evaluation protocol.

Agents broke this assumption. Operating across multi-step tasks, an agent calls tools, handles errors, and observes results over many steps, making a single output string insufficient. The [ Berkeley Function-Calling Leaderboard (BFCL)](https://gorilla.cs.berkeley.edu/leaderboard.html) emerged to evaluate function selection and argument accuracy across single- and multi-turn scenarios. However, BFCL only evaluates individual

*calls*—a valid

`issue_refund`

call still fails if underlying checks or updates were skipped. Call accuracy is necessary, but not sufficient.## From scoring calls to scoring the environment

Full agentic evaluation now requires a **full execution environment**: one that executes each tool call, tracks state across steps, and reads the world afterward to decide whether the work got done.

Two scoring layers sit on top of it:

**Step-level**(*process scoring*) asks was this call valid, relevant, and useful given the state at that point?**End-to-end**(E2E, or*outcome scoring*) ignores the path and checks only the final state: did the refund post, did the ticket route correctly?

Step-level tells you *where* the chain breaks, which is what you want when debugging or targeting fine-tuning effort; E2E collapses a failure on step one and a failure on step nine into the same “task failed.” E2E is what your users actually experience, which is why most production evals gate the release on it and keep step-level tracing underneath for debugging.

Those two scores are two readings of one object: the **trace**. A trace is the ordered log of a single attempt: the user message, each step, and the environment state when the attempt stops. Process scoring grades the rows. E2E scoring grades the final state.

## What a benchmark run measures

A tool-calling benchmark scores three things in order: **deciding** to use a tool, **selecting** the right one, and **populating** its arguments. A model that reaches for a tool when a direct answer would fail as surely as one that skips a tool it needed. Cost and latency ride on top, set by the call’s verbosity and runtime.

Every run rolls up through a fixed hierarchy: **Benchmark → Trial → Task → Turn → Step**:

- A
**trial**is one independent pass over the whole task set under a fixed configuration. - A
**task**is one independently scorable problem instance, identified by a task ID. - A
**turn**is one exchange boundary: a message in, the agent’s reply out, everything between belongs to that turn. - A
**step**is one atomic action inside a turn — a tool/command invocation, or a non-tool emission like a plan or the final message.

A step is *usually a tool call*, and every score above it rolls up from those steps. The metrics worth tracking collapse onto three axes: **accuracy**, **verbosity**, **cost** (see Table 1, below).

| Metric | Formula | Axis | Why it exists |
|---|---|---|---|
| Task success rate | `successful_tasks / tasks` | Accuracy | The release gate. Did the environment reach the goal state? |
| Consistency | `range of success rate across 3–5 trials` | Accuracy | A 90% / 74% split isn’t 84%. Report 82–88%, not a point estimate. |
| Tool-call precision | `correct_calls / calls_issued` | Accuracy | Hallucinated names and extra calls surface here, not in success rate. |
| Argument accuracy | `correct_args / calls_with_right_tool` | Accuracy | Separates “wrong API” from “right API, filled wrong.” |
| Steps per success | `steps / successful_tasks` | Verbosity | How long the trajectory runs when the task actually finishes. |
| Cost per success | `spend / successful_tasks` | Cost | The economic unit. Tokens and GPU-seconds only matter per successful task. |

*Table 1. Core evaluation metrics, grouped by axis (accuracy, verbosity, cost)*

The pairings matter: success rate without consistency is a point estimate on a stochastic system (a model that hits 90% then 74% is a worse bet than one holding 84%); tool-call precision without argument accuracy hides slot-filling failures.

Step count is often the axis that varies *most* across models on the same task — four steps versus fifteen — though on suites like Terminal-Bench 2.0 steps-per-turn varies too, so which axis moves most is benchmark-dependent. **Parallel tool calling** cuts step count and latency, but not call count: a one-step turn firing four tools still issued four calls. Roll up in order; don’t average steps and call it a benchmark score.

## How to read an evaluation

Two benchmarks can both claim to test tool calling and produce numbers that aren’t comparable. Three dimensions explain most of the gap:

**Task complexity**— single-turn with one tool, or multi-turn requiring planning, error recovery, and state management? A single-call benchmark won’t tell you whether a model collapses on step eight of fifteen.**Statefulness**— does the environment update on each action? Stateful benchmarks surface drift, context loss, and corrupted state that static ones miss.**Methodology**— executable verification (did the DB update, did tests pass) is the gold standard. Reference-based evaluation needs an annotated answer set someone must maintain. LLM-as-a-Judge fills the gap where no executable check exists, but treats its scores as provisional until validated against human ratings on a sample.

Contamination now extends beyond training data leaks to live variants: web-searching agents retrieving answer keys during evaluation, and datasets on Hugging Face quickly re-scraped into pretraining corpora. Private domain evals solve this by being unable to scrape.

Table 2, below, is a public trace from a real benchmark run using step-level and E2E scoring, where the suite rather than an artificial ticket provides the tools, user, and completion criteria.

- Suite:
[SWE-bench Verified](https://arxiv.org/abs/2310.06770)(real GitHub issues, executable test verification) - Task ID:
`pytest-dev__pytest-5262`

(trial .2, turns 0–4) - User / user-simulator opening: “Implement the necessary changes to the repository (
`/testbed`

) so that the requirements specified in the issue are satisfied” — the issue:`_pytest.capture.EncodedFile`

reports mode`rb+`

(binary) from its underlying buffer, but its`write()`

only accepts`str`

, so external code that checks`.mode`

(e.g.`youtube-dl`

) crashes when it writes`bytes`

. - Harness notes (tools exposed, max steps, parallel calling on/off): OpenHands agent harness; tools exposed:
`terminal`

,`file_editor`

,`task_tracker`

,`finish`

; parallel tool-calling off (one tool call per turn); repo state persists turn to turn (real filesystem + git, not a mock).

| Step | Turn | Call | Environment observation | Verdict | Why (valid / useful / redundant / recovered / policy) |
|---|---|---|---|---|---|
| 1 | 0 | `terminal(find /testbed -name "capture.py")` | Returns `/testbed/src/_pytest/capture.py` | valid | Locates the file named in the issue before editing anything |
| 2 | 1 | `file_editor(view, capture.py)` | Dumps the full file (400+ lines) | redundant | File is large; grepping for the class first would have been more targeted |
| 3 | 2 | `terminal(grep -n "EncodedFile" capture.py)` | Returns 422: `return EncodedFile(...)` / 425: `class EncodedFile(object):` | recovered | Corrects step 2’s inefficiency by narrowing straight to the relevant lines |
| 4 | 3–4 | `file_editor(view, view_range=[420,450]/[450,470])` | Shows `EncodedFile.__init__` /`__getattr__` , revealing it delegates `.mode` straight from the binary-mode buffer | valid | Pinpoints the exact root cause (unfiltered `__getattr__` delegation) that step 5+ fixes |

*Table 2. Extracted trace call on SWE-Bench verified evaluation*

- E2E check (DB state / tests / ticket): PASSED
- E2E score (0 or 1): 1
- Step-level score (passes / steps): 3/4
- Tool-call precision: 3/4
- Argument accuracy: 4/4

Looking at the results that were outputted, it is important to look at the last 5 bullets: **E2E check, E2E score, step level score, tool-call precision, and argument accuracy**. **E2E check** tells us that the related tests for the bug issues it sought to fix passed, meaning **E2E score** in this case is 1 (is_resolved: true). The next metric is the **step level** score that tells you how many of the steps the model took were actually needed. Looking at the score for the table above, step level is 3/4 due to one of the steps in this case being redundant – in particular step 2. In this case, it directly plays into the **tool-call precision** which also received a 3/4 due to the minor misstep. For this trace, our final metric **argument accuracy** saw that all arguments filled in correctly with no malformed arguments.

## Why benchmarks are converging on tool use

The line between “calling a tool” and “completing a task” no longer holds: most benchmarks measuring general capability now also measure tool use because models aren’t run without tools in any viable deployment. A benchmark that withholds tool access scores a capability nobody ships.

Not every benchmark makes the case. **HumanEval** runs generated Python against unit tests, providing executable verification, but no tool call and no environment to act on. **SWE-bench** is where the shift becomes clear: resolving a real GitHub issue means navigating a codebase, writing a patch, and passing the suite — file-read, search, and edit calls in sequence. The score measures the outcome, but the trajectory underneath consists entirely of tool calls. In many cases, then, the benchmarks you already run for general capability are already exercising tool use. That reframes the question that matters:

**Academic benchmarks measure a model’s capability ceiling in the abstract. Enterprise benchmarks answer the narrower, more useful question: can it do my job — your tasks, against your APIs, under your policies?** The closer a benchmark sits to production, the more its score should weigh in your decision.

## Analyzing [Nemotron 3.5 Lightning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/) through this lens

Read [NVIDIA Nemotron 3.5 Lightning’s](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4) published suite as task completion and time-to-done, not isolated call accuracy. [ Banking](https://artificialanalysis.ai/models/nemotron-3-5-lightning) scores completion across a multi-turn banking conversation — the refund trace at scale, not a single call.

**GDPval-AA v2**scores real agentic work from actual job outputs, judged pairwise by a panel of LLM judges with Elo anchored to a 1,000 human-expert baseline — the kind of human validation that keeps a judge score trustworthy. On

**PinchBench**, Nemotron 3.5 Lightning hits 86% accuracy while finishing 10,000 tasks 30% faster than Qwen3.6 35B at comparable accuracy — a model that finishes efficiently beats one scoring higher on isolated accuracy while burning more steps and

[tokens](https://blogs.nvidia.com/blog/ai-tokens-explained/).

Public scores are a great signal, but they shouldn’t be considered as a release gate. Adapting the model to your task and use-cases is as important as ever.

## Benchmarking your own workload

**Set a public floor.**Run a published agentic suite; record success rate and its range across 3–5 trials.**Build a domain eval**from your real tickets, traces, and APIs. Gate on environment state — a database row, a merged PR, a closed ticket — not a judge’s opinion of the final message.**Adapt**the model and harness to that distribution.**Re-measure**success rate, consistency, steps per success, and cost per success. Keep step-level traces for debugging.

Verify consequences in the environment, use judges for language, and use tool-call precision and argument accuracy to find where the chain breaks.

To reproduce the published numbers, Nemotron ships [reproducibility docs](https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md) covering the configs behind the [model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4#benchmarks) scores. Try it on [build.nvidia.com](https://build.nvidia.com), grab weights from [Hugging Face](https://huggingface.co/nvidia), or follow the [NIM guide](https://docs.nvidia.com/nim/large-language-models/latest/get-started/advanced/get-started-nemotron-3.5-lightning.html).

Tool calling in the realm of [LLM](https://www.nvidia.com/en-us/glossary/large-language-models/) benchmarking is the foundation that evaluations today rest on. Being able to build, read, and understand these evaluations is pertinent in making an informed decision for your use case.

## Going further

*Stay up to date on NVIDIA Nemotron by subscribing to NVIDIA news and following NVIDIA AI on LinkedIn, X, YouTube, and the Nemotron channel on Discord.*

*Access open Nemotron Models on Hugging Face and a collection of NIM microservices and Developer Examples on build.nvidia.com.*

## Start the discussion at forums.developer.nvidia.com
