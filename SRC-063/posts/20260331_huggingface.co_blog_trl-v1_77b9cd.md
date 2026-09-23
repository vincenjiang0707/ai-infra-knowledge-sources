# TRL v1.0: Post-Training Library Built to Move with the Field

source: https://huggingface.co/blog/trl-v1
published: Tue, 31 Mar 2026 00:00:00 GMT

Paper • 1707.06347 • Published • 12

#
[
](https://huggingface.co#trl-v10-post-training-library-built-to-move-with-the-field)
TRL v1.0: Post-Training Library Built to Move with the Field

[Update on GitHub](https://github.com/huggingface/blog/blob/main/trl-v1.md)

TRL now implements [more than 75 post-training methods](https://huggingface.co/docs/trl/en/paper_index). But coverage isn’t the goal by itself. What matters is making these methods easy to try, compare, and actually use in practice.
The design of the library wasn’t decided upfront. It is the result of years of iteration — the first commit goes back more than six years — and it has been shaped by everything the field threw at it: new algorithms, new models, shifting paradigms. Over time, this pressure forced the codebase toward a very specific design. Parts of it might look unusual at first, but like in many evolutionary codebases, they exist for a reason.

TRL is built for a field that doesn’t sit still. So the question is not how to design the perfect abstraction. It is how to make stable software in a domain that keeps invalidating its own assumptions. This is what we tried to solve in TRL v1.0, and this post explains how.

##
[
](https://huggingface.co#1-a-moving-target-post-training-as-a-shifting-field)
1. A moving target: post-training as a shifting field

Post-training has not evolved as a smooth refinement of one recipe. It has moved through successive centers of gravity, each changing not just the objective, but the shape of the stack.

PPO [[Schulman et al., (2017)](https://huggingface.co/papers/1707.06347); [Ziegler et al., (2019)](https://huggingface.co/papers/1909.08593)] made one architecture look canonical: a policy, a reference model, a learned reward model, sampled rollouts, and an RL loop.

Then DPO-style methods such as the original DPO [[Rafailov et al., (2023)](https://huggingface.co/papers/2305.18290)], ORPO [[Hong et al., (2024)](https://huggingface.co/papers/2403.07691)], and KTO [[Ethayarajh et al., (2024)](https://huggingface.co/papers/2402.01306)] cut through that stack: preference optimization could work without a separate reward model, value model, or any online RL. Components that had looked fundamental suddenly looked optional.

RLVR-style methods such as GRPO [[Shao et al., (2024)](https://huggingface.co/papers/2402.03300)] shifted the center again. On tasks like math, code, and tool use, rewards often come from verifiers or deterministic checks rather than learned reward models. Sampling and rollouts matter again, but the objects in the loop are no longer quite the ones PPO libraries were designed around.

The lesson is not just that methods change. The definition of the core keeps changing with them. Strong assumptions here have a short half-life. This is probably why no post-training library is really stable yet.

##
[
](https://huggingface.co#2-from-project-to-library-trl-has-a-chaos-adaptive-design)
2. From project to library: TRL has a chaos-adaptive design

So what does it mean to build a library for a field that won't sit still? The answer is counterintuitive: don't try to capture the essence of what's stable today. Instead, design around what could change. *Reward models* illustrate why: they looked essential in PPO, became optional in DPO, and came back as *verifiers* in RLVR methods — structures that could be deterministic functions rather than learned models. Any abstraction built around their original form would have been obsolete twice over by now. The library survives by recognizing that strong assumptions have a short life, and by making that changeability central to how the codebase is organized.

This is the environment in which TRL is downloaded 3 million times a month, and in which major downstream projects treat it as stable infrastructure. The field keeps shifting the ground, and at the same time, those users need things not to break.

###
[
](https://huggingface.co#a-shift-in-nature-from-code-to-contract)
A shift in nature: from code to contract

TRL didn’t make a deliberate decision to become a library. It found out it already was one. Projects like [Unsloth](https://github.com/unslothai/unsloth) and [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) — with thousands of users between them — had built directly on top of TRL’s trainers and APIs. A breaking change in TRL propagated instantly into their stacks. A renamed argument, a shifted default, a restructured output — any of these became someone else’s incident. The shift had already happened. v1.0 is the moment TRL acknowledged it explicitly.

###
[
](https://huggingface.co#stable-and-experimental-under-the-same-roof)
Stable and experimental, under the same roof

The unusual thing about TRL’s stability model is not what it guarantees, it is what it tolerates alongside those guarantees. Stable and experimental coexist within the same package, with explicitly different contracts. The stable core follows semantic versioning. The experimental layer makes no such promises — it is where new methods land while they are still being evaluated, and where the API can move fast to keep up with the field.

This isn’t a compromise. It’s a response to a specific constraint: the field produces new methods faster than any of them can earn stability. Refusing to add immature methods would make TRL irrelevant within months. Adding them all to stable would break every downstream project every time an algorithm turned out not to work as expected.

```
from trl import SFTTrainer # ⚖️ stable
from trl.experimental.orpo import ORPOTrainer # 🧪 experimental
```


Promotion from experimental to stable isn’t automatic. What matters is the ratio between maintenance cost and actual usage. Some methods earn their place because the community uses them heavily. Others become viable because we can make them cheap enough to maintain — and the design of the codebase is what makes that possible.

In practice, the **stable** surface includes trainers for SFT, DPO, Reward modeling, RLOO, and GRPO, along with their close variants. The **experimental** surface is broader and moves faster; for an up-to-date view, the best reference is the [TRL documentation](https://huggingface.co/docs/trl).

The breaking changes needed to reach v1.0 were distributed deliberately across the 0.x releases. Migration from the last 0.x version is minimal — see the [migration guide](https://github.com/huggingface/trl/blob/main/MIGRATION.md).

###
[
](https://huggingface.co#deliberately-limiting-abstractions)
Deliberately limiting abstractions

In a domain where patterns keep changing, the temptation is to build flexible abstractions that can accommodate anything. Our answer was the opposite: **limit abstractions to the strict minimum — while recognizing that this “minimum” is almost always overestimated**.

In practice, this translates into a very local approach to code:

- avoid generic class hierarchies
- favor explicit implementations
- accept, and even encourage, duplication

The goal is not to eliminate structure altogether — shared utilities still exist — but to avoid imposing abstractions where the domain itself is not yet stable. For instance, rather than defining a common base class for offline trainers, we prefer independent implementations when their future evolution is uncertain.

```
# ❌ No
class OfflineTrainer(Trainer):
def some_common_method(self): ...
class DPOTrainer(OfflineTrainer): ...
class KTOTrainer(OfflineTrainer): ...
# ✅ Better
class DPOTrainer(Trainer):
def some_common_method(self): ...
class KTOTrainer(Trainer):
def some_common_method(self): ...
```


Another example:

```
# ❌ No
# collator.py
class TRLCollator: ...
# dpo_trainer.py
class DPOTrainer:
def __init__(self, ...):
self.collator = TRLCollator(...)
# kto_trainer.py
class KTOTrainer:
def __init__(self, ...):
self.collator = TRLCollator(...)
# ✅ Better
# dpo_trainer.py
class DataCollatorForPreference: ...
class DPOTrainer:
def __init__(self, ...):
self.collator = DataCollatorForPreference(...)
# kto_trainer.py
class DataCollatorForUnpairedPreference: ...
class KTOTrainer:
def __init__(self, ...):
self.collator = DataCollatorForUnpairedPreference(...)
```


[Judges](https://github.com/huggingface/trl/blob/main/trl/experimental/judges/judges.py) are a good example of what happens when we don’t follow this principle. Early on, we introduced a `Judge`

abstraction to unify the various ways of evaluating model outputs. It looked reasonable at the time. In practice, it was never really used — the abstraction didn’t match how people actually approached evaluation, and it added indirection without adding value. It still lives in the repo, mostly as legacy. In hindsight, shipping the concrete implementations without the unifying abstraction would have served users better.

###
[
](https://huggingface.co#more-explicit-but-more-adaptable)
More explicit, but more adaptable

This approach favors explicit and modifiable usage over rigid frameworks: less magic, but more control. It comes with an obvious cost: code duplication. While often seen as an anti-pattern, in this context it has proven not only acceptable, but effective. Contrary to intuition, it remains manageable in practice with a small but consistent discipline: keeping deltas between implementations minimal and avoiding unnecessary divergence. Like in the [Transformers design philosophy](https://huggingface.co/blog/transformers-design-philosophy#3-machine-learning-is-evolving-at-a-neck-breaking-speed), we accept duplication and local explicitness by design. The motivations largely coincide, with some nuance in focus.

This is easier to see than to describe. Compare RLOO and GRPO: large parts of their implementation are duplicated almost line for line. That is not accidental, and it is not dead weight. These methods are close enough that keeping their code paths aligned makes them easier to read, easier to evolve, and cheaper to maintain.

##
[
](https://huggingface.co#3-where-trl-fits)
3. Where TRL fits

The goal of this comparison is not to argue that TRL should be judged as best on every axis. It should not. Some systems are built for maximum throughput (like [PipelineRL](https://github.com/ServiceNow/PipelineRL)), some are optimized for a narrower slice of the problem (like [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)), and some offer a more opinionated development experience in a specific environment (like [Tinker](https://github.com/thinking-machines-lab/tinker)). TRL occupies a different place in the ecosystem: it is a general-purpose post-training library that tries to keep the API and the code as simple as the domain allows, while combining broad method coverage, deep Hugging Face integration, a relatively low infrastructure burden, and an explicit stability contract.

Libraries like [Unsloth](https://github.com/unslothai/unsloth) and [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) are not included here because they build on top of TRL rather than sitting beside it in the comparison; in that sense, many of their users are also TRL users indirectly.

###
[
](https://huggingface.co#ecosystem)
Ecosystem

|
|---|

[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)

[veRL](https://github.com/volcengine/verl)

[PRIME-RL](https://github.com/PrimeIntellect-ai/prime-rl)

[PipelineRL](https://github.com/ServiceNow/PipelineRL)

[OAT](https://github.com/sail-sg/oat)

[Tinker](https://github.com/thinking-machines-lab/tinker)

[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

[torchtune](https://github.com/meta-pytorch/torchtune)

`report_to`

)`report_to`

) + swanlab###
[
](https://huggingface.co#training-methods)
Training methods

|
|---|

[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)

[veRL](https://github.com/volcengine/verl)

[PRIME-RL](https://github.com/PrimeIntellect-ai/prime-rl)

[PipelineRL](https://github.com/ServiceNow/PipelineRL)

[OAT](https://github.com/sail-sg/oat)

[Tinker](https://github.com/thinking-machines-lab/tinker)

[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

[torchtune](https://github.com/meta-pytorch/torchtune)

`environment_factory`

in GRPO)`AgentInstance`

interface)`BaseInteraction`

interface)###
[
](https://huggingface.co#project-health)
Project health

|
|---|

[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)

[veRL](https://github.com/volcengine/verl)

[PRIME-RL](https://github.com/PrimeIntellect-ai/prime-rl)

[PipelineRL](https://github.com/ServiceNow/PipelineRL)

[OAT](https://github.com/sail-sg/oat)

[Tinker](https://github.com/thinking-machines-lab/tinker)

[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

[torchtune](https://github.com/meta-pytorch/torchtune)

Some rows are factual (`GitHub stars`

, `Last release`

, `Last commit`

), others are qualitative judgments (`Semver stability`

).

Taken together, these comparisons point to a clear role for TRL: a general-purpose library designed to keep breadth, simplicity, integration, and stability in the same place. Its full downstream footprint is hard to measure, since most deployments are private and reverse dependencies are largely invisible, but the available signals already show that TRL operates at a distinctly different scale.

##
[
](https://huggingface.co#4-whats-next)
4. What’s next

By now, the logic of v1.0 should be clear: it is not a claim that post-training has stabilized. On the contrary, it is an acknowledgment that the field will keep shifting, and that we're confident that the library has the right shape to absorb whatever comes next. The question is not what comes **after** v1.0, but what’s next **for** v1.0.

###
[
](https://huggingface.co#asynchronous-grpo)
Asynchronous GRPO

Today, GRPO in TRL is primarily used through a synchronous loop: generate rollouts, score them, then step the optimizer. That shape is simple and dependable, but it ties throughput to the slowest stage and leaves performance on the table at scale.

The fix is conceptually simple: generation and training don't need to be lock-stepped. We already have an [early asynchronous GRPO design](https://huggingface.co/docs/trl/main/en/async_grpo_trainer), and the next step is to harden it. The core idea is to decouple generation and training, letting generation run continuously on dedicated inference resources while training consumes a steady stream of scored trajectories, with buffering, backpressure, and clear policy-version accounting. This improves utilization and scales across GPUs and nodes. Other libraries already offer forms of asynchronous RL, but bringing it to TRL would make this style of training available through broader integrations, simpler APIs, and a much lower barrier to adoption.

###
[
](https://huggingface.co#graduating-methods-to-stable)
Graduating methods to stable

The next candidates include [KTO](https://huggingface.co/docs/trl/main/en/kto_trainer) and newer distillation trainers such as [SDFT](https://huggingface.co/docs/trl/main/en/sdft_trainer), [SDPO](https://huggingface.co/docs/trl/main/en/sdpo_trainer), and possibly [GOLD](https://huggingface.co/docs/trl/main/en/gold_trainer) or [GKD](https://huggingface.co/docs/trl/main/en/gkd_trainer). As discussed in Section 2, before moving them to stable, the goal is to minimize code differences across implementations and monitor sustained community interest relative to maintenance cost.

###
[
](https://huggingface.co#scaling)
Scaling

TRL supports large-scale training, including multi-node runs and larger models; the next step is to make this path significantly more robust and easier to operate in production. That includes stronger guarantees around distributed stability, clearer scaling defaults, and deeper support for Mixture-of-Experts (MoE), especially expert parallelism, where routing, load balancing, and memory behavior become critical.

###
[
](https://huggingface.co#making-training-legible-to-agents)
Making training legible to agents

Training is still too often driven by vibes. Loss curves go down, reward curves go up, a few samples look better than before, and people convince themselves the run is working. When it fails, they scroll through logs, compare runs by eye, and guess. That is already a weak interface for humans. For agents, it is worse: it is barely an interface at all.

One of the most important directions for TRL is to make training legible to software, not just to people. That means going beyond dashboards and raw metrics to produce explicit signals: is the policy improving, collapsing, over-optimizing the verifier, drifting off-distribution, or plateauing? The goal is for TRL to surface these patterns automatically, explain them clearly, and turn them into actions.

The plan is to embed heuristics directly into the training loop and emit structured, actionable warnings — the kind a beginner can act on immediately and an agent can parse:

```
[TRL] WARNING: VRAM utilization at 34%. Consider increasing per_device_train_batch_size from 4 to 16.
...
[TRL] WARNING: Group reward std is 0.01 (near zero). Advantage signal has collapsed. Consider revisiting your reward function to ensure it provides sufficient variance for learning.
...
[TRL] WARNING: Clip ratio outside [0.8, 1.2] for 43% of updates. Consider reducing the learning rate.
```


Not just logging what happened — reasoning about what it means and what to do next. Useful for beginners who need guardrails, and for agents that need a training stack they can actually automate.

##
[
](https://huggingface.co#5-conclusion)
5. Conclusion

Post-training doesn't converge. It shifts, and the next shift is already coming.

v1.0 is not a claim that things have settled. It's an acknowledgment that they haven't yet, and a commitment that the library can be relied on anyway. Six years of evolving alongside the field — and alongside the hundreds of contributors who made it possible — shaped a design we're confident is ready for what comes next, whatever that turns out to be. The community and the downstream projects had already assumed that stability — v1.0 makes it real.

```
pip install --upgrade trl
```


Migration from the last 0.x release is minimal, and the [migration guide](https://github.com/huggingface/trl/blob/main/MIGRATION.md) covers everything. If you're new, now is a good time to start.