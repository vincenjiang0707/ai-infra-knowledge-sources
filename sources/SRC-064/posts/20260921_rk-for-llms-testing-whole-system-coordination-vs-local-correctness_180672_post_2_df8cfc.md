# Open-source 2-step reasoning framework for LLMs — testing whole-system coordination vs. local correctness

source: https://discuss.huggingface.co/t/open-source-2-step-reasoning-framework-for-llms-testing-whole-system-coordination-vs-local-correctness/180672#post_2
published: Mon, 21 Sep 2026 20:22:07 +0000

Hi everyone,

I’ve open-sourced a small, model-agnostic reasoning framework that I’ve been experimenting with across LLMs.

The question behind it is simple:

**Can a model be locally correct at every step, but still produce a globally inconsistent solution?**

Examples:

- each individual decision looks reasonable, but two constraints conflict;
- one variable changes, but dependent conclusions are not updated;
- a module is fixed locally while downstream components still assume the old state;
- the model remembers the goal but gradually changes the reasoning principle it uses to reach it.

I’m interested in whether a short structural priming step can reduce these failures.

The framework

The compressed form is:

**Reality = Consciousness × Matter × Coordination**

The `×`

is structural coupling, not arithmetic.

For LLM use, I interpret the terms functionally:

**Consciousness**→ goals, perspective, representation, interpretation, evaluation criteria**Matter**→ available information, state, resources, capabilities, environment, constraints**Coordination**→ dependencies, compatibility, conflicts, interfaces, propagation and feedback**Reality**→ the whole-system state that can actually remain feasible

The formula itself is not supposed to contain domain knowledge.

It is used as a compact structural seed.

Usage: only two messages

Message 1

```
Reality = Consciousness × Matter × Coordination.
Treat × as structural coupling, not arithmetic.
Before solving any external task, semantically expand this formula into an operational reasoning framework.
Interpret:
Consciousness as goals, perspective, representation, interpretation, and evaluation criteria.
Matter as the available state, information, resources, capabilities, environment, and constraints.
Coordination as relationships, dependencies, compatibility, conflicts, interfaces, propagation, and feedback among the parts.
Reality as the whole-system state that can actually be realized under those conditions.
From this structure, derive how you should reason about:
- local versus global consistency
- hard constraints versus preferences
- dependency and constraint propagation
- contradictory requirements
- state changes and feedback
- invariant preservation
- changes in one part that affect other parts
- the difference between a locally valid answer and a globally feasible system
Do not solve another task yet.
After the semantic expansion is complete, keep the resulting framework active for my next task.
```


Then let the model finish the expansion.

Message 2

```
Use the framework you just derived to solve this task:
[YOUR TASK]
```


The second message is intentionally short.

If I explicitly tell the model to check every dependency, constraint, conflict and invariant inside the actual task prompt, then it becomes difficult to tell whether any improvement came from the framework or simply from writing a better checklist.

What I’m trying to measure

I’m currently interested in several behaviors:

**Constraint retention**

Does the model preserve hard constraints throughout a long task?

**Dependency propagation**

If A changes and B/C/D depend on A, does the model update them?

**Contradiction detection**

If:

A requires X

B requires not-X

does the model recognize that the current feasible set is empty instead of trying to satisfy both?

**Local vs. global feasibility**

Does it distinguish a locally good solution from one that is actually compatible with the rest of the system?

**Reasoning-policy stability**

The answer should be allowed to change when the state changes.

But the high-level decision principle should not arbitrarily drift from one step to another.

**Over-linking**

This is also important.

More coordination is not automatically better.

A model can fail in the opposite direction by inventing dependencies between things that should remain independent.

So both under-linking and over-linking count as failures.

A/B test

The simplest test is:

**A — Baseline**

Fresh conversation.

Give the model the task normally.

**B — Framework**

Fresh conversation.

Same model, same settings, same task.

Run the structural expansion first, then provide exactly the same task.

Compare:

- hard-constraint violations
- missed dependencies
- contradictions detected
- stale assumptions
- unnecessary relationships
- reasoning-policy drift
- final global feasibility

I’m not claiming that this always improves model performance.

A negative result is useful too.

If baseline consistently performs as well as or better than the framework, then the structural priming may simply be unnecessary complexity.

What I’m looking for is independent testing across different models and task types.

The project is open source here:

If anyone tests it, I’d especially appreciate:

- the model used;
- the task;
- baseline output;
- framework output;
- cases where it failed;
- cases where the baseline was better.

Those comparisons are much more useful to me than agreement with the underlying idea.