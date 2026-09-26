source: https://github.com/resources/insights/agentic-engineering-system?locale=en-US

# GitHub's Agentic Engineering System

Code generation is getting easier, but delivering customer value requires more than just volume. It requires a system.

AI agents can help teams ship faster, but shipping faster does not automatically deliver more value. Without a foundation of strong governance, shared knowledge, and clear feedback loops, agents can increase confusion, rework, and risk.

GitHub's Agentic Engineering System (AES) is a framework for building that foundation, so your teams are set up to deliver customer value from day one. It describes:

Governance, shared knowledge, and customer value as three "stocks" that shape system health over time

Define, deliver, and detect as three "activities" that move work through the system

Director, performer, and assessor as three "modes" that describe how people and agents contribute


**Use this framework to:**

Evaluate your readiness to scale agent use

Decide which work can be delegated, and which needs more human oversight

Improve the quality of information available to people and agents


The diagram above shows how work moves through an engineering system with agents (a software component that can work asynchronously and (semi)-autonomously). The three activities form a continuous loop; the three modes describe how people participate; and over time, the three stocks accumulate and shape whether each cycle improves the next.

A simple way to tell whether agent adoption is working: as agent use expands, escaped defect rates should stay flat or fall, and the quality of shared knowledge should improve alongside delivery speed. When both happen, the system is getting faster without getting weaker. If they diverge, something in the operating model needs attention.

AES is tool-agnostic. The stocks, activities, and modes apply to any organization adopting agents in software engineering, regardless of vendor. This document uses examples from the GitHub ecosystem because it's the environment we know best, but the same concepts can be mapped to other toolchains. The framework is relevant at both the organizational and team level, though teams are often constrained by the conditions set at the organizational level. Implementation guidance related to this playbook is available in [GitHub Well-Architected](https://learn.github.com/well-architected/governance/recommendations/agentic-engineering-system-on-github).

AES also assumes a set of operating-environment conditions: reliable and secure infrastructure, appropriately skilled humans, a culture that supports responsible agent participation, and sufficient data and content access. These are preconditions for the framework to behave as described and are covered under readiness and preconditions in the adoption and readiness FAQ. If they are absent, agent adoption will struggle regardless of how well governance, shared knowledge, and participation modes are designed.

AES draws in part on ideas from [System Dynamics](https://en.wikipedia.org/wiki/System_dynamics) and software delivery research, including [DORA](https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development). These sources help explain how system conditions shape outcomes over time, and why speed only creates value when it is paired with reliability, learning, and strong operational feedback loops.

## The stocks that make agent use reliable

### How to keep people and agents working effectively at speed

Governance and shared knowledge determine whether agent use is reliable. Customer value tells you whether that reliability is producing results that customers actually value. Together, these three stocks shape whether faster processes lead to better outcomes or just more output and risk.

The point is not just to have these stocks, but to keep improving them. In strong systems, each cycle leaves behind better governance, better shared knowledge, and clearer evidence of what customers value.

### Governance: What determines what can be delegated, and what still needs human oversight

Governance determines what people and agents are allowed to do, under what conditions, and with what oversight. It is what allows low-risk, well-bounded work to move quickly while ensuring higher-risk work gets the human attention it needs. While it may not impact customer value directly, it can make delivery more trustworthy.

When governance is strong, teams can delegate more work with confidence because the boundaries are clear and the controls match the risk. When it's weak, organizations usually end up in one of two bad states: over-restricting agents and losing potential speed gains, or under-restricting them and accumulating avoidable risk.

Good governance is less about creating a single gate and more about maintaining an operating layer that is evaluated continuously as work moves through the system: policy, permissions, reviews, automated checks, security requirements, deployment protections, and escalation paths. When that layer is current and well-calibrated, low-risk work can flow quickly and human attention can stay focused where judgment matters most. When it is vague, stale, or disconnected from real workflows, teams either work around it or are slowed down by it.

**Signals:**

Incidents or defects that point to missing controls or weak review boundaries

The share of low-risk work that still queues for manual review

How often automated policy checks pass versus require exceptions

How quickly incidents or near misses lead to governance updates

Whether approved tools and workflows are actually being used


### Shared knowledge: What people and agents need to do good work

Shared knowledge is the information people and agents rely on to do good work: code, decisions, documentation, telemetry, and customer feedback. It shapes how well work is defined, delivered, and improved over time. When shared knowledge is current, relevant, and easy to use, both people and agents are more likely to make good decisions and produce useful output.

When shared knowledge is strong, work is easier to scope, hand off, and complete with confidence because the right information is available in the right places. When it's weak, people and agents are more likely to rely on guesswork, outdated assumptions, or incomplete context. Humans can sometimes work around those gaps through experience or informal networks, while agents can only act on what they can access, which means weak shared knowledge often turns into fast, confident mistakes.

When knowledge is well maintained, decisions are documented, and important information is easy to find, so teams can delegate more effectively and spend less time correcting avoidable errors. When knowledge is stale, scattered, or overloaded with irrelevant detail, work slows down, review burden rises, and mistakes are more likely to add up.

**Signals:**

The freshness and quality of documentation, instruction files, and architecture records

How often agent or human work has to be re-scoped because key context was missing

Agent task success rates, especially where low success points to unclear or incomplete inputs

High token use, repeated retries, or tool-call churn on tasks that should be straightforward

How often important decisions or learnings are captured in places the broader system can use


### What a context window does and doesn't do

An agent's context window is not the same thing as organizational understanding. Even a powerful model can only act on the information it is given or allowed to retrieve, and large volumes of context do not guarantee that the right context is present, current, or well structured. In practice, better outcomes stem from giving agents the right information in a form they can use.

### Customer value: What tells you whether faster delivery is actually paying off

Customer value is the outcome these other two stocks exist to support. Governance and shared knowledge shape whether work can move quickly and reliably, while customer value tells you whether that work is solving real problems, improving the customer experience, and building trust over time. It is the clearest signal of whether agent adoption is creating better outcomes or just more activity.

When customer value is strong, faster delivery is translating into something customers actually notice: better experiences, more useful capabilities, fewer problems, or stronger trust in the product. When it's weak, teams may still be shipping quickly, but the work is not producing meaningful results. More output without more adoption, satisfaction, or reliability is a sign that something upstream is misaligned.

Good customer value depends on the system learning from real signals. Teams need to know not just what they shipped, but whether it worked, who it helped, and what should change next. When delivery is connected to usage, feedback, support patterns, and operational results, teams can correct course earlier and invest more confidently in what matters. When those signals are weak or ignored, it becomes easy to mistake motion for progress.

**Signals:**

Feature adoption and usage after release

Customer-reported defects and support volume trends

Satisfaction, retention, or trust indicators tied to delivery cycles

How often shipped work needs rollback or immediate follow-up fixes

Whether teams can clearly connect delivery work to customer outcomes


## How work moves, and how humans and agents contribute

The AES framework describes work in two ways. Activities illustrate how work moves through the lifecycle: define, deliver, and detect. Modes describe how people and agents participate in that work as directors, performers, and assessors.

These modes are not job titles or team boundaries. They are patterns of work that can shift depending on the situation. The same person or agent may move through multiple modes across the same activity, and the right mix of human and agent involvement depends on risk, governance, and shared knowledge.

### Activities: How work moves

The three activities describe the active work of the lifecycle: deciding what should happen, making a change, and observing what happened. They repeat many times across a product's life. What changes from one cycle to the next is not the activity itself, but the surrounding conditions: what governance allows, what shared knowledge is available, and whether a person or an agent is doing the work.

#### Define: Decide what should happen

Define is the decision about what should happen next. It could be writing a requirement, framing an issue, or deciding to act on an alert. In an agentic system, define matters more because cheaper delivery means poorly defined work can move into execution almost immediately.

Strong define depends on shared knowledge: customer insight, prior decisions, system constraints, and clear acceptance criteria. In strong systems, exploratory work is also more likely to turn into production outcomes, because the assumptions, constraints, and success criteria were defined clearly enough to build on. When they are weak, agents can produce well-structured but poorly grounded work very quickly.

**Signal:** The share of defined work that enters delivery without major re-scoping or rework.

#### Deliver: Make the change

Deliver is where work changes something in the world: shipping code, creating a prototype, updating documentation, changing infrastructure, or enabling a launch. In an agentic system, the key question is not whether agents can help deliver, but which kinds of delivery can safely move with less human involvement and which still require closer judgment.

Low-risk, well-bounded work can often flow through agent performers with strong automated checks and light human review. Higher-risk work, especially work involving trade-offs, customer impact, or difficult-to-reverse consequences, still needs deeper human direction and assessment.

**Signal:** Whether faster delivery is increasing customer value or just creating more in-flight work and review burden.

#### Detect: Observe what happened

Detect is how the system observes what happened: telemetry, incidents, support patterns, customer feedback, performance changes, and other real-world signals. Its job is not just to notice those signals, but to turn them into information the next cycle can use.

Agents can dramatically increase the volume and speed of detection. The challenge is no longer finding signals, but deciding which ones matter, when to escalate, and how to route them back into shared knowledge and governance. More detection without better interpretation creates noise, not insight.

**Signal:** Detection latency, signal coverage, and how often detected issues are structured and fed back into future work.

### Modes: How people and agents participate

Modes describe how people and agents participate in work. Director sets direction. Performer acts on that direction. Assessor evaluates the result. These aren't fixed roles: the same person or agent may hold different modes at different times depending on capability, risk, and what governance allows.

#### Director: Set direction

Director is the mode that sets intent, scope, and constraints. It decides what outcome matters, what trade-offs are acceptable, and what boundaries the work needs to stay within. In an agentic system, director becomes more important because faster execution makes weak direction more costly.

People are often best placed to hold the director mode when the work depends on judgment, organizational context, customer understanding, or competing priorities. Agents can support them by surfacing options, summarizing context, or turning rough goals into clearer plans, but they should not be mistaken for the source of intent.

**Anti-patterns:**

Delegating execution without clearly defining the objective

Treating agent-generated plans as if they reflect business intent on their own

Leaving trade-offs or escalation paths implicit


#### Performer: Carry out the work

Performer is the mode that carries out the work. It writes code, updates documentation, runs analysis, opens pull requests, executes remediation steps, or completes other bounded tasks. In an agentic system, agents can often hold this mode well when the task is clear, the context is strong, and the boundaries are well defined.

The question is not whether agents can perform work, but which work they can perform reliably. For low-risk, well-scoped tasks, agent performers can increase speed significantly. For work with higher ambiguity, broader consequences, or difficult-to-reverse outcomes, human involvement usually needs to increase alongside automation.

**Anti-patterns:**

Using agents on poorly scoped tasks and expecting reliable execution

Expanding delegation without improving governance or shared knowledge

Confusing task completion with successful outcomes


#### Assessor: Evaluate the result

Assessor is the mode that evaluates whether the work is correct, useful, safe, and complete enough to move forward. It reviews outputs against intent, standards, evidence, and real-world results. In an agentic system, assessor becomes more important, not less, because more generated work means more needs to be checked in the right way.

People are especially important in this mode when judgment, accountability, or customer impact is involved. Agents can support assessment by running tests, checking policy compliance, flagging anomalies, summarizing diffs, or comparing outputs against known patterns. But strong assessment depends on knowing what evidence matters and when a result should be questioned, not just whether a check passed.

**Anti-patterns:**

Treating green checks as a complete substitute for review

Reviewing agent output more lightly than comparable human work

Measuring speed without measuring error, rework, or downstream impact


### Participation modes grid

In successful organizations, activities and modes work together. Define, deliver, and detect describe the work itself. Director, performer, and assessor describe how people and agents take part in that work. The right mix depends on the task, the context available, and the risk involved.

Sometimes people hold all three modes. Sometimes agents take on more of the execution while people stay focused on direction and judgment. The goal is not maximum agent participation. It is the right participation for the work.

The matrix below is not a maturity ladder or a fixed operating model. It is a way to think through which forms of participation fit which kinds of work.

|
|
|
|
| PM raises an issue in GitHub Projects specifying a notification feature, assigns an agent to draft detailed requirements and acceptance criteria | Engineer writes a prompt instructing an agent to create a React prototype with specific component structure and test coverage | SRE configures an agent to collect latency and error rate metrics from Datadog (for the purpose of improving shared knowledge) |
| Agent reviews the backlog, weighs customer impact, technical debt, and team capacity, then proposes prioritized issues for the next sprint with written rationale. | Agent evaluates a failing deployment by correlating error signatures, change history, and dependency health, then chooses the least disruptive remediation within pre-authorized boundaries. | Agent investigates a latency shift by examining recent deployments and dependency graphs, then defines the observability changes it judges most informative within its pre-authorized scope. |
| Architect researches technical constraints and writes a feasibility assessment for the notification feature in response to the PM's issue | Engineer manually builds a payment integration requiring judgment about error handling and retry logic | SRE investigates a novel outage by correlating logs across three services and interviewing the on-call engineer |
| Agent drafts requirements and acceptance criteria by synthesizing customer feedback tickets, prior decisions, and technical constraints from shared knowledge | Agent writes code, generates tests, opens a pull request (which is assessed by a human), and deploys to staging | Agent pulls telemetry from Datadog, correlates it with recent deployments, and summarizes findings as a comment on the relevant GitHub issue |
| Tech lead reviews the drafted requirements, flags missing edge cases, and approves the issue for delivery | PM reviews the deployed prototype against the original issue description and acceptance criteria | SRE evaluates whether the agent's monitoring configuration is capturing the right signals at the right granularity and adjusts thresholds |
| Agent evaluates a drafted issue against architectural standards, decision records, and dependency risks, then approves with confidence notes or returns it with specific concerns. | Agent reviews a pull request by analyzing test results, complexity changes, and security findings, then approves, requests changes, or escalates based on residual risk. | Agent examines its detection outputs against historical baselines, identifies where coverage is thin or signal quality has degraded, and recommends targeted improvements. |

Use activities and modes together to decide where agent participation should expand, where people should stay more involved, and what conditions need to improve first. If a task is poorly defined, high risk, or weakly supported by shared knowledge, increasing automation will usually increase rework and risk. If the task is well bounded, the context is strong, and the assessment path is clear, agent participation can often expand safely.

**A note on agentic workflows**

Some teams use [orchestrator and worker agent](https://www.anthropic.com/research/building-effective-agents) patterns or [agentic workflows](https://github.github.com/gh-aw/), but these do not change the core framework. The same questions still apply: who is directing, who is performing, who is assessing, and what governance and shared knowledge make that participation reliable?

## See the framework in action

### New feature development: private preview to public preview to general availability

New feature development rarely moves through the lifecycle just once. It usually moves through multiple loops, with each cycle adding to shared knowledge and changing what the team does next.

A team may begin with shared knowledge such as customer insights, product strategy, prior decisions, system constraints, and existing code. That context is used to define an initial version of the work, often a narrow private preview designed to test a specific assumption. The team then delivers that preview to a small group of users and detects what happens: usage, feedback, support needs, defects, and unexpected behavior. Those signals feed back into shared knowledge.

The move from private preview to public preview is another loop. The team uses what it learned to define what needs to change before broader exposure, delivers those changes, and detects what happens at larger scale. By the time the feature reaches GA, the system has accumulated more shared knowledge about what users value, where the product struggles, and what needs to be true for a reliable launch.

### Ongoing maintenance and sustainment: signals to stability

A product in maintenance still moves through the lifecycle, but the cycle often starts with detect rather than a planned feature idea.

Signals such as usage patterns, incidents, support tickets, cost changes, and security alerts are continuously produced by the system. Through observability, customer feedback, operational reviews, and agent-supported analysis, those signals are detected and added to shared knowledge. The team uses that updated context to define the next piece of work, which might be a bug fix, reliability improvement, documentation update, or alert change.

The team then delivers the change, sometimes with agents doing part of the work under human review, and returns to detect to see whether the change had the intended effect. In this loop, customer value may not look like a new feature. It may show up as lower downtime, fewer support tickets, or more stable performance.

### Security incident: from detection to recovery

A security incident is another example of the lifecycle starting with detect and moving through the full cycle to restore stability and strengthen the system.

A vulnerability alert, unusual system behavior, or correlated monitoring signal may trigger the cycle. Those signals are detected, investigated, and added to shared knowledge: which systems are affected, what the blast radius is, and which assumptions failed. The team then defines the response, delivers the fix, and returns to detect to confirm that the issue is resolved and that no new problems have appeared.

In this kind of loop, agents may help identify affected systems, open pull requests, or summarize evidence, while humans remain closely involved in higher-risk actions such as secret rotation, policy changes, and final approval. The value delivered is not a new feature but the preservation of trust, reliability, and control.

## Assess where you are and decide what to do next

This section helps you assess how much work you can safely delegate to agents today, and what you need to strengthen before delegating more. The answer depends on two things: the health of your leading stocks—governance and shared knowledge—and the current range and depth of agent usage across your lifecycle.

Below you'll find our Stock-Adoption matrix. It helps teams locate their current posture, understand the risks of expanding too quickly or too slowly, and choose the next move that fits their system. You do not need to move the whole organization at once. Each process or task can shift on its own, so you can adopt one at a time and place each where it fits today.

Organizations may move from **Underdeveloped foundations** to **Healthy but underused**, and then toward a **Healthy agent-native system**. But many teams expand agent usage faster than their stocks can support and end up in a **Stretched agent-native system** instead.

To make the four quadrants concrete, the same small task is shown in each one. Only the surrounding conditions change.

**Shared task.** A backend engineer needs to add a `customer_tier`

field to the `GET /orders/{id}`

response. The field already exists in the system, so the change is small and read-only: expose the field, update the schema and documentation, and add a test.

**Healthy agent-native system.** Governance and shared knowledge are strong, and agent delegation is appropriately scoped. An agent picks up the task, uses current documentation and contract information, updates the API response, regenerates the spec, and opens a PR. Automated checks confirm the change is additive, and a human reviewer gives final approval. The work merges quickly because the surrounding system is reliable.

**What to do next:**Stay the course and expand to the next safe class of work.


**Healthy but underused.** The foundations are strong, but agent participation is still limited. A human engineer makes the same change using good documentation, reliable tests, and strong review controls. The work is safe and fast, but no agent is involved. The system could support more delegation than it is currently using.

**What to do next:**Expand agent participation in small, well-bounded tasks first.


**Underdeveloped foundations.** Governance and shared knowledge are too weak to support broader delegation reliably. A human engineer makes the change, but key context is hard to find: the spec is known to drift, downstream consumers are unclear, and the impact must be discovered manually. The engineer eventually finds a dependency that would have broken and coordinates a safer rollout. A human can absorb that discovery cost; an agent likely would not.

**What to do next:**Strengthen shared knowledge and governance before expanding agent use.


**Stretched agent-native system.** Agent usage has expanded faster than governance and shared knowledge. An agent makes the same change using stale or incomplete context. CI passes, a busy reviewer approves, and the PR merges quickly. The hidden dependency is only discovered later when a downstream job fails. The problem is not the agent alone; it is the weak system around it.

**What to do next:**Slow expansion, narrow agent scope, and repair the missing foundations.


The core lesson of the matrix is whether agent usage matches the strength of the foundations beneath it. **Healthy agent-native** and **Underdeveloped foundations** are aligned states: in one, strong governance and shared knowledge support broader delegation; in the other, weak foundations limit how much delegation is safe. **Healthy but underused** and **Stretched agent-native** are misaligned states: one could safely delegate more, while the other is already delegating too much for its current foundations.

**Risk appetite affects where an organization draws the line between "healthy enough" and "not yet."** Teams with higher tolerance for defect leakage may expand agent usage earlier. Teams with high consequences for failure will require stronger governance and shared knowledge before delegating the same work. The matrix shows direction, not a universal threshold.


## Explore other resources

## Frequently asked questions

## Applying the framework

### Why didn't our pilot scale?


Pilots often succeed because they happen under unusually favorable conditions: strong context, narrow scope, close human involvement, and temporary workarounds. They fail to scale when organizations copy the tool but not the surrounding conditions that made it work. The lesson from a pilot is not just that the agent was useful; it is what shared knowledge, governance, and participation patterns made the result reliable.

**Practical takeaway:** End every pilot with a structured handoff: what worked, what conditions made it work, and what another team would need to reproduce it.

### Where should we start with governance and data?


The right starting point is usually not an enterprise-wide data cleanup or a fully built governance model. It is one workflow where agent participation could add clear value. Map the information that workflow depends on, identify the governance conditions it needs, and close those gaps before expanding further.

**Practical takeaway:** Govern one workflow at a time, then accumulate what you learn.

### Why haven't our workflows changed?


In many organizations, AI tools are added without changing who is directing, performing, or assessing the work. When that happens, people still hold all three modes and agents remain ad hoc assistants. The workflow looks modern, but the operating model has not actually changed.

**Practical takeaway:** Use the activities × modes grid to identify where people are still acting as performers on work an agent could reliably take on.

### Why is review burden rising?


Rising review burden is often a sign that agent work is poorly scoped, weakly grounded, or too large to evaluate efficiently. This is usually a shared knowledge problem before it is a model problem. Better instructions, clearer acceptance criteria, smaller tasks, and more iterative use tend to improve output quality faster than simply switching models.

**Practical takeaway:** Reduce scope, improve context, and review smaller batches.

### How do we reduce shadow AI use?


Shadow AI use is usually a sign of unmet demand, not just noncompliance. Blanket bans rarely solve it. A better approach is to define which tools and data uses are allowed, where human oversight is required, and which actions are off-limits. Clear approved paths reduce the incentive to work around policy.

**Practical takeaway:** Replace blanket prohibition with clear, usable rules and approved alternatives.

## Readiness and preconditions

### What does the AES framework assume, but not model directly?


AES describes three stocks, three activities, and three modes. It does not attempt to model every condition an organization needs in place for those elements to work. It assumes a functioning operating environment underneath the framework: reliable and secure infrastructure, people who can work effectively with agents, a culture that supports responsible use, and access to the information and permissions needed to act. When those conditions are weak, results will diverge even if the framework itself is applied correctly.

### What if our infrastructure or vendors are too unstable to support this?


AES assumes the underlying environment is reliable enough for fast cycles to complete consistently and securely. If build systems are flaky, CI is slow, identity systems are unreliable, security practices are immature, or key vendors change behavior unexpectedly, teams will struggle no matter how well governance or shared knowledge are designed. In that situation, the problem is not the framework. It is the operating environment underneath it.

**Signal to watch:** Security incidents that reflect weak fundamentals, or cycle time dominated by waiting, retries, flaky jobs, or recurring vendor-driven rework.

### Do people need special skills to work effectively with agents?


Yes. The framework assumes people in director, performer, and assessor modes know how to instruct agents, evaluate their output, and intervene when needed. If teams can't scope work clearly, assess quality reliably, or recognize when to override an agent, outcomes will suffer.

**Signal to watch:** Rework, overrides, and review bottlenecks cluster around the same people or teams, or agent-authored work is reviewed too lightly relative to comparable human work.

### What kind of culture makes agent participation work?


AES works best in environments where agent participation is treated as a legitimate part of the work, not something to hide, over-celebrate, or distrust by default. Teams need to be able to use agents where they add value, keep people more involved where they do not, and report failures or near misses without penalty. If usage is politicized or treated as a status signal, the feedback loops the framework depends on become distorted.

**Signal to watch:** Agent use is hidden, exaggerated, or rewarded as an end in itself, while failures and near misses go unreported or are softened.

### What if agents can't access the information they need, or aren't allowed to use it?


AES assumes agents can reach the code, decisions, documentation, telemetry, and customer signals needed to make shared knowledge usable, and that legal, contractual, and regulatory constraints allow the intended actions. If agents only have access to partial, stale, or unusable information, or if the rules prevent them from acting where the workflow expects them to, the system will underperform regardless of model quality.

**Signal to watch:** Agents are given the task, but not the current and relevant information or permitted access needed to do it well.