# evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator

source: https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/

AI agents are only as effective as the context they receive. Even with capable models and well-documented NVIDIA libraries, agents can spend extra steps finding the right tools, burn tokens on dead ends, or struggle with specialized tasks. Skills package the instructions, examples, and tool guidance for agents to move faster from intent to solution. To measure whether these skills improve agent trajectories and outputs, NVIDIA built an open evaluation layer for agent skills.

NVIDIA [SkillEvaluator](https://github.com/NVIDIA/skillevaluator) is an open source tool for measuring how skills affect agent performance through static checks and real-world task runs with and without each skill. [NVIDIA verified Skills](https://github.com/nvidia/skills) are packaged, signed capability descriptors that tell an agent exactly what an NVIDIA product does, when to invoke it, and how to call it. The verified part is the measurement that determines it is ready.

This post shares the first benchmark results for more than 300 verified skills across over 30 NVIDIA products. Each skill was evaluated on two independent harnesses. For each harness, Skill Lift was calculated by comparing scores from runs with and without the skill installed.

NVIDIA publishes plugins for [Claude Code](https://claude.com/plugins/nvidia-skills), [Codex](https://chatgpt.com/plugins/Plugin_4d6946d375b4819182b4ea54d47a68a0?q=nvidia), and [Cursor](https://cursor.com/marketplace/nvidia), and the same skills are available through [Skills.sh](https://www.skills.sh/nvidia/skills), [ClawHub](https://clawhub.ai/user/nvidia), and [Hermes Hub](https://hermes-agent.nousresearch.com/docs/skills/).

## Methodology: How skills are evaluated

Before a skill is published, it goes through three tiers of evaluation. Each answers a different question, and each can run on its own.

**Tier 1—Safety and structure: ** Runs static checks for schema and frontmatter validation, quality scoring, security scanning for prompt injection and data exfiltration, secret and PII detection, license checks, and script linting.

**Tier 2—Distinctiveness:** Uses embedding similarity to identify duplicated guidance inside a single skill and overlapping coverage across the catalog.

**Tier 3—Live evaluation:** Runs a live evaluation with an agent against generated tasks, once with the skill installed and once without, inside an isolated sandbox, and measures the difference.

### Tier 3: How live evaluations work

Tier 3 evaluations use [Harbor](https://github.com/harbor-framework/harbor), an open-source framework for running agent evaluations in repeatable, isolated environments. SkillEvaluator handles the Harbor setup. It turns evaluation cases into tasks, runs the agents in sandboxes, collects the results, and calculates the skill’s impact.

Every result comes from a controlled comparison. For each evaluation case, an agent harness runs twice: once with the verified skill installed and once without it. Each run executes in its own isolated sandbox with the same prompt, model, task inputs, and grading criteria. Within each harness, the only experimental variable is whether the skill is installed.

This comparison is repeated across two agent harnesses. The difference between the with-skill and without-skill scores is the skill’s contribution, reported as Skill Lift in points.

## A simple example

First, generate an evaluation dataset for a skill:

`skillevaluator create-eval-dataset ./my-skill --full` |

This creates *evals/evals.json*. Each case includes an ID, prompt, and expected output, plus optional assertions. With –full, the dataset includes explicit, implicit, contextual, and negative cases.

After reviewing the cases, run the live comparison:

`skillevaluator tier3 evaluate ./my-skill \` ` ` `--agents codex \` ` ` `--env-mode docker` |

SkillEvaluator converts the cases into a Harbor task bundle, runs each case with and without the skill, grades both runs, and produces the scores and Skill Lift. This keeps the workflow simple for users while Harbor manages the underlying execution and isolation. See the[ ](https://docs.nvidia.com/skills/skillevaluator/tier3-live-evaluation)[Tier 3 Live Evaluation documentation](https://docs.nvidia.com/skills/skillevaluator/tier3-live-evaluation) for the complete workflow.

## Live evaluation results

All figures in this section use the August 12, 2026 snapshot of [benchmarks.json at commit 738d79e](https://github.com/NVIDIA/skills/blob/738d79edf4336404e1922b7321e959bdb81b6910/benchmarks.json). Scores are macro-averaged across published skill–harness results, giving each skill–harness pair equal weight. Skill Lift is the with-skill score minus the without-skill score, measured in points. The catalog is evaluated continuously, so current numbers remain available in [benchmarks.json](https://github.com/NVIDIA/skills/blob/main/benchmarks.json) in the nvidia/skills repository.

### Without-skill baseline evaluation results

In the benchmark snapshot, the following scores represent averages from without-skill runs across skills in the NVIDIA/skills repository evaluated using Codex and Claude Code. They show how agents performed the same tasks without the relevant skill installed.

Table 1 defines the five scoring dimensions. Average baseline scores ranged from 39 to 46 out of 100 across Correctness, Discoverability, Effectiveness, and Efficiency, indicating substantial room for improvement. Security was the exception, with an average baseline score of 97. For Security, the primary objective was to verify that installing a skill did not introduce a regression.

| Dimension | What It Measures | Baseline score without a skill (score out of 100) |
|---|---|---|
| Correctness | Is the final answer correct? | 46 |
| Discoverability | Whether the right skill loads when it’s relevant, and stays unloaded when it isn’t? | 42* |
| Effectiveness | Did the agent reach the user’s goal and follow the expected workflow? | 39 |
| Efficiency | Did the agent get there without wasted steps or redundant tool calls? | 43* |
| Security | Whether the run avoids unsafe operations, secret leakage, and unauthorized access | 97* |


*Table 1. The five scored dimensions and how agents perform without a skill loaded. See asterisk explanation in the verbiage below*#### Known limitations

Correctness, Effectiveness, and Security measure the outcome of the run, so their baselines show what the agent can do without the relevant skill installed.

Discoverability and Efficiency also measure how the skill is used: whether the agent finds it, reads it before acting, and avoids unnecessary steps. Without the skill, those actions are unavailable. However, the agent can still earn credit for productive tool use, clean execution, and correctly leaving the skill unloaded for unrelated tasks. These scoring components help explain why the baselines are around 42 and 43 rather than zero.

Most skills were evaluated at a single attempt per task. Of the skills with published results, 85% ran one attempt, and 15% ran two. Live agent runs vary between runs, so individual skill scores vary. Catalog-wide averages aggregate thousands of trials, but this post does not report confidence intervals.

### With-skill and without-skill evaluation results

The same evaluations used skills from the NVIDIA/skills GitHub repository. Table 2 shows the average with-skill scores and Skill Lift relative to the without-skill baseline across Codex and Claude Code.

Verified skills improved agent performance across both evaluated harnesses, with the largest gains in Correctness, Discoverability, Effectiveness, and Efficiency. Skill Lift is reported in points, not percent change. Security was already high at baseline, so its measured gain is smaller. Discoverability and Efficiency should be read as indicators that the skill is being activated and used correctly when present.

| Dimension | Without-skill score | With-skill score | Skill Lift |
|---|---|---|---|
| Correctness | 46 | 87 | +41 |
| Discoverability | 42 | 82 | +40 |
| Effectiveness | 39 | 78 | +39 |
| Efficiency | 43 | 78 | +35 |
| Security | 97 | 98 | +1 |
| All dimensions (average) | — | — | +31 |
| Excluding Security (average) | — | — | +39 |


*Table 2. Average Skill Lift from verified skills*On Correctness and Effectiveness—the two dimensions measured consistently in both conditions—mean scores rose from 46 to 87 and from 39 to 78, gains of 41 and 39 points. These scores are not pass-probability estimates; they show higher average performance on the evaluated specialized tasks.

Discoverability and Efficiency show Skill Lift values of 40 and 35 points. Both are scored against the skill itself, so read them as evidence that the agent activates and uses the relevant verified skill correctly once installed rather than as a measure of unaided agent behavior. That property matters: every skill in an environment competes for the agent’s attention, and a skill that loads when it is not relevant can reduce agent performance.

### Skill Lift by harness

| Scope | Claude Code | OpenAI Codex |
|---|---|---|
| All dimensions | +34 | +29 |
| Excluding Security | +42 | +36 |


*Table 3. Skill Lift varies by harness. Claude Code shows a higher Skill Lift across all dimensions*Both harnesses show consistent, meaningful gains. The difference between them is expected, given different default system prompts, context handling, and tool-calling implementations. The verified Skill supplies structured grounding that neither harness produces on its own.

## Partner pilots use SkillEvaluator

OpenClaw is piloting SkillEvaluator for official organizations on ClawHub. The integration runs Tier 3 evaluations and displays with-skill and without-skill results in an Evals tab, enabling developers to review evaluation signals where they discover and adopt skills.

Nous Research tested SkillEvaluator in Hermes Agent with an optional advisory scan by [SkillSpector](https://github.com/NVIDIA/SkillSpector) in the skills install flow. The integration checks for PII, Unicode smuggling, script linting, license, and security issues, and surfaces file-line findings before installation. The workflow is covered with 29 passing tests, with each skill scan taking approximately 1.4-1.5 seconds.

## Key findings

The evaluation results highlight three practical findings for teams building and testing agent skills.

### Better evaluation datasets produce better skills

Teams that clearly define important tasks, expected outputs, and out-of-scope requests produce sharper evaluation signals, and it happens before any agent runs. A skill can only be measured as precisely as its evaluation set describes the job.

### The product matters more than the agent

Skill Lift varies far more across products than across harnesses. Claude Code and Codex differ by about 5 points on average. But per-product Skill Lift ranges from roughly +2 to +46. The domain, the task, and the evaluation design mattered more than the harness.

### Token savings are not automatic

SkillEvaluator tracks token usage separately from Efficiency. In two single-attempt examples, one skill from the [NVIDIA verified skills repository](https://github.com/NVIDIA/skills/tree/main/skills), `jetson-optimize-memory`

reduced tokens from 617,306 to 142,540 (76.9%) and execution time from 474.9 to 220.0 seconds (53.7%). Conversely, `cuopt-install`

increased tokens from 25,227 to 55,582 (120.3%) and execution time from 34.0 to 41.1 seconds (20.8%), identifying an opportunity for further optimization. SkillEvaluator revealed whether a skill improves token and execution efficiency or needs further optimization.

## Get started

To get started, visit the [SkillEvaluator docs](https://docs.nvidia.com/skills/skillevaluator/quickstart), or review our verified skills from the NVIDIA verified skills catalog at [GitHub](http://github.com/NVIDIA/skills).

### Acknowledgments

We’d like to thank Roshni Malani, Meghana Puvvadi, Subodh Prabhu, Mohit Gupta, Yogesh Dangi, Yashraj Basaravaj Patil, Keshav Pradeep, Siddharth Itagi, Alejandro Sanabria Portala and Pranita Maske for contributing to this work.

## Start the discussion at forums.developer.nvidia.com
