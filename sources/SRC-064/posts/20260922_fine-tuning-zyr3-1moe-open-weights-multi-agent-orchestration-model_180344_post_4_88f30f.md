# Looking for collaborators (dataset curation / fine-tuning) — ZYR3.1MoE, open-weights multi-agent orchestration model

source: https://discuss.huggingface.co/t/looking-for-collaborators-dataset-curation-fine-tuning-zyr3-1moe-open-weights-multi-agent-orchestration-model/180344#post_4
published: Tue, 22 Sep 2026 07:51:31 +0000

Hi, I’m the developer behind ZYR3.1 (zyr-AGENT/ZYR3.1MoE). It’s an open weights, merged, standalone model — 9B parameters, fully self-contained (no adapter/PEFT step needed), built on a Qwen base.

The design is a layered multi-agent orchestration stack: an ATP layer handles planning, task decomposition, and verification; an ACN layer carries messages between components; and MeO (Router/Reasoner/Synthesizer) decides which of 11 specialist agents — Planner, Researcher, Reasoner, Coder, Math, Critic, Fact Checker, Creative, Optimizer, Reviewer, and a Computer agent — get involved for a given task. Simple questions skip the orchestration entirely and go straight to the base model; only real work requests trigger the full plan → route → build → verify loop.

I’ve also been careful to separate trained behavior from real execution — there’s a demo trace showing the simulated “team chat” style the model produces, and a separate, genuinely externally-verified trace (real commands, real exit codes, real pass/fail) so people can see the difference rather than take marketing copy at face value.

I’m running this solo right now and looking for one or two collaborators who enjoy dataset curation, agent orchestration, or fine-tuning work — especially if you’ve worked on tool-use datasets, agent trajectories, or MoE merges. Happy to go deep on the architecture or the eval setup with anyone interested.

Model card: [zyr-AGENT/ZYR3.1MoE · Hugging Face](https://huggingface.co/zyr-AGENT/ZYR3.1MoE)