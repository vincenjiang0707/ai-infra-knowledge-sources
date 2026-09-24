# ml-operations-with-agent-skills

source: https://www.anyscale.com/blog/ml-operations-with-agent-skills

# Reimagining ML Operations with Agent Skills: a new maturity model for on-call

[Christian Stano](https://www.anyscale.com/blog?author=christian-stano)| May 21, 2026

Last month we released [ Anyscale Agent Skills ](https://www.anyscale.com/blog/announcing-anyscale-agent-skills-ray)- the most token-efficient skills for building Ray pipelines on the market, grounded in real human building & debugging experience. I’ve long believed ML teams have been underserved by coding agents. These tools (rightfully) leave the nuance to your harness & custom skills, a time investment most teams can’t fully commit to. This puts more complex frameworks like Ray at a disadvantage because of the sheer amount of surface area they cover. This is one of the many reasons we released Anyscale Agent Skills.

Most of what’s been written so far covers what Anyscale Agent Skills do and how they work. **This post is about something else: how these skills reshape the way leaders should approach ML Operations. **Have we created a fun new plugin or reached fully autonomous ML teams? The answer lies somewhere in the middle (for now).

In this post, I cover what I believe is the new on-call default for ML operations and a new maturity model for leaders to unlock AI-native operations in AI platforms and workloads.

## LinkA new on-call default

I categorize operations into three phases - day 0, day 1, and day 2. Each of these involves a different activity and core metric to optimize for across building Ray AI pipelines.

|
|
|
Day 0 - Build | Golden path templates, code examples, wiki pages, 101/102 level enablement. | Time to first PR - how fast can someone get started with a new pipeline? |
Day 1 - Deploy | Platform interfaces, smart defaults, local environment setup, Slack back and forth to resolve “why did my job fail”. | Failure rate - how many failures happen across the stack to deploy a successful production job? |
Day 2 - Operate | Page responses, runbook definition, escalations, dashboard & log deep dives. | MTTR and business metrics - how long does it take to resolve a failure and how does that impact my business metrics? |

When I ran AI platform teams, we always looked for ways to improve efficiency of on-call across all three of these categories, but it was constantly a tradeoff. Should we invest time into automating or improving the on-call activities at the expense of feature work? For most of my career, this was a tax requiring 20-30% of a team’s time every sprint. In the last 12 months, agentic coding tools and skills started to reduce this tax, but also created a new tradeoff - investment into skills infrastructure.

Anyscale Agent Skills represent a third evolution, one made possible by lowering the investment required for skills and agent harness infrastructure. We ship skills in three families. Workload skills write the Ray and Anyscale code — Ray Train loops, Ray Serve deployments, Ray Data pipelines, and LLM serving configs. Platform skills run that code on Anyscale, inspect it when something breaks, and fix it. Infrastructure skills help you deploy Anyscale itself on Kubernetes or VMs.

Here’s a sneak peek into what this next evolution looks like:

|
|
|
Day 0 - Build | Platform Ray expert writes golden path code templates. Migrations needed to move from non-Ray or unoptimized Ray to best practice Ray templates. | Workload skills generate the workload and configs using Ray best practices out of the box. ML team focuses on business logic and model choice. Platform team ensures these skills integrate cleanly with platform & repo builds. |
Day 1 - Deploy | Hand-tuned configs. Tribal knowledge. “Hey @platform, why is my job broken?” | Platform skills handle launch, validation, and compute selection. Platform team only gets involved as needed, not on every release. |
Day 2 - Operate | Pager. Logs. Slack thread. The Ray expert gets paged in. MTTR measured in days. |
|

The key takeaway: **Anyscale** **Agent Skills become the first responder across day 0, day 1, and day 2.** Instead of baking in capacity for the inevitable daily interrupts for on-call, platform teams can lean on Anyscale Agent Skills to set the right patterns, handle deployments and questions, and triage pageable issues before any human needs to be in the loop.

Having a unified runtime (Ray on Anyscale) is a key success factor behind this. Ray gives the agent a single, Python-native control plane for the entire AI workload across data, training, serving, and batch inference. Anyscale gives it a managed runtime with stable APIs, observability, and guardrails the agent can actually reason about. For example, on a stitched-together stack - Kubernetes plus Airflow plus a serving framework plus a separate batch inference framework - the agent’s surface area expands substantially. The agent has to translate a Ray actor failure into a Kubernetes pod event into an Airflow task state. Each translation and tool boundary is a place where the wrong thing gets inferred, context gets lost, and tokens get burned. The agent spends more time translating between systems than solving the problem. Ray gives agents a singular traction point, and Anyscale bottles that up into a token-efficient CLI and Skill call.

** Every platform leader using Anyscale and Ray should be evaluating this new paradigm for on-call operations.** Across our customers, we’re starting to see velocity improvements for both researchers and platform engineers because of the self-service this paradigm creates. Researchers can accomplish more across build, deploy, and operate which also frees platform engineers to reinvest their on-call time into long-horizon work. This is available today, requires minimal time investment to unlock, and will yield results from day 1.

This is great - so what’s next?

## LinkThe new maturity model for on-call in AI platforms

I propose a new maturity model for on-call in AI Platforms, measured in stages of autonomy and human-in-the-loop time. Each stage of this maturity model remains anchored in the core phases of on-call (day 0, day 1, and day 2) and can serve as the foundation for a roadmap toward autonomous on-call.

### LinkStage 1: The coffee break (where most teams are today)

Most teams using coding agents today follow the same pattern. Spin up three or four Claude Code sessions. Hand each one a task. Step away for coffee while the agents "cook." Come back, review, ship. This works for day 0 operations, but it also breaks something.

Your senior ICs are now running a team of agents instead of writing code. They're context-switching between four parallel threads, each producing work they have to verify. The mental model shifts from "I'm building this" to "I'm managing four junior engineers who don't remember anything between turns." That's a real cognitive load.

The short-term gain is real because you can ship more pipelines per IC-hour. However, the long-term cost is that your best builders stop building. They become reviewers and dispatchers. The thing they're best at, including deep technical judgment on hard problems, gets squeezed into the gaps between agent check-ins.

**What changes for engineers**: Anyscale Agent Skills change the shape of this immediately by raising the abstraction level of each agent session. When a workload skill knows how to scaffold a Ray training job correctly the first time, your IC isn't reviewing five attempts to get the actor config right. Instead, they're reviewing one attempt that's already grounded in best practice. Each agent session produces more usable output per check-in, meaning your ICs can supervise fewer threads more deeply or the same number of threads with less mental overhead.

**Where this works & limitations: **If your ICs are spending their day reviewing agent output on problems Ray already has opinions about like config tuning, resource sizing, retry logic, that's not leverage. That's just moving where the toil happens. Skills push the toil into the runtime where it belongs, so your ICs can spend their cycles on the parts of the problem that actually need a human.

**How to unlock this stage: **This is the easiest win to capture, and it's the one most teams are leaving on the table. You don't need to rebuild your on-call rotation or trust an agent overnight to start here. You just need to give your agents better starting context.

### LinkStage 2: Open loop first responder (where you should strive for this half)

Day 1 and Day 2 operations as most teams run it today is a tax on the wrong people. Forget the 2 AM page for a minute; the bigger cost is the daytime interruption. Every Slack ping that says “*hey, this is broken, can you take a look?”* is a moment when your senior engineer isn’t advancing the product or the platform. Multiply that by a team of ten over a quarter and you’ve lost weeks of forward progress to context-switching on issues that, in most cases, are solvable from the logs.

The shift Anyscale Agent Skills enable is simple: **the first responder to these issues shouldn’t be a human.** It should be an agent running an `/anyscale-platform-inspect`

skill followed by an `/anyscale-platform-ask`

and `/anyscale-platform-fix`

skill grounded in Ray best practices. The agent triages, pulls the relevant logs, checks the cluster state, identifies the failure mode, and either remediates within its scoped permissions or escalates with a complete report.

**What changes for engineers**: The page or message you get is no longer “*something’s broken, figure it out.*” It’s “*here’s what broke, here’s what the agent tried, here’s what it found, here’s what it needs you to decide*.” You walk into a triaged incident, not a blank one.

**You’re not eliminating on-call. You’re raising the bar for what gets a human involved.** Non-critical triage runs autonomously. Your engineers only see escalations with the genuinely novel, ambiguous, and impactful issues that actually need judgment. Everything else gets handled before it shows up in their feed.

**Where this works & limitations: **This works well for a defined class of issues such as known failure modes, observable symptoms, scoped remediation. The dependency mismatch on a new CUDA version. The misconfigured resource request. The data pipeline that OOM’d from a misconfigured batch size. Novel failures still need humans, but novel failures are a small fraction of actual on-call volume. The rest is pattern-matchable. Pattern-matching is exactly what these agents are good at, and with Anyscale Agent Skills, agents have all of the context to recognize and fix these issues.

**How to unlock this stage: **Combine Anyscale Agent Skills with your on-call alerting surface areas and existing automation pipelines. Slack is a great place to centralize this automation and meet your engineers where they already work. Combine an [ Anyscale Job Failure Notification](https://docs.anyscale.com/administration/resource-management/custom-notifications) with Anyscale Agent Skills packaged into your CI/CD system to kick off an Anyscale “triage” job with the metadata and access to inspect, triage the issue, and post back to Slack with a report. Reuse this workflow for questions from researchers and alerts in channels. Simple to create, and only needs a week of work to wire everything together because the hard, time-intensive part of debugging is already packaged into the Anyscale Agent Skill.

** Tips for success: **Add human-in-the-loop evaluation to this system. Researchers and platform engineers can grade responses, your system captures those grades, and your teams can use that data to further improve your automation and outcomes.

### LinkStage 3: Closed loop first responder & nocturnal engineer (where you should strive for next)

Once Stage 1 & Stage 2 create a successful pattern of decreased toil across Day 0, Day, 1, and Day 2, a different kind of work becomes possible across all phases of operations: continuously automated research, experimentation, and triage.

Imagine handing an agent a research objective on Friday afternoon. Not a task. An objective. “*Improve recall on the long-tail entity extraction benchmark by 3 points without regressing latency.*” Or: “*Find a more efficient fine-tuning configuration for the 13B model - same loss curve, lower cost.*” You go home. The agent runs in a bounded environment, uses Workload skills to generate variants, Platform skills to launch and validate them, Debug skills to triage failures, and iterates. Monday morning, you walk in to find a pull request. Three configurations tried. One that beats the baseline. The difference, the eval results, and the cost numbers sitting in your queue waiting for review.

**What changes for engineers: **That’s a different operating model. The unit of overnight work shifts from “a script ran” to “a hypothesis was tested.” Your morning standup isn’t about what’s on fire. It’s about which experiments came back, which ones produced something worth pursuing, and what to point the agent at next.

**You’re not automating busywork. You’re extending the experimentation loop past the eight-hour day.** Headcount stays the same. The number of hypotheses your team can test in a week multiplies. That’s the leverage.

**How to unlock this stage: **The building blocks ship in the box today: chained skill execution, scoped permissions, destructive command blocking, acknowledgment gates. The cost guardrails are available in Anyscale via quotas and budgets. With the additional harness work in Stage 1 & Stage 2, you now have an E2E pipeline, where all you need to do is rethink how you approach business problems and outcomes.

## LinkGetting tactical

To bootstrap this new on-call default, here are some tactical 30-60-90 tips to get started:

**First 30 days:** Pilot one team, one workload, one clear success criterion. Measure time to production with and without Anyscale Agent Skills. Compare the results because without a baseline, you’re flying blind on ROI.

**Success story from the field: **We built and optimized a batch embeddings pipeline from a new data source for a customer in 2 days using our Agent Skills.

**Next 90 days**: Move on-call triage to agent-first for a defined class of known failure modes. Measure percentage of on-call tasks in backlog vs product work for the platform. Validate that you are actually freeing engineering time.

**Continuously**: Define your guardrails for unattended work. Pick one research objective worth running overnight, and see what comes back the next morning. Overnight research only works if leadership trusts the blast radius is contained, so start writing the guardrails before you need them, not after.

## LinkMoving forward

This post introduces a new maturity model for ML Operations, shifting the on-call paradigm by making Anyscale Agent Skills the first responder across Day 0, Day 1, and Day 2. This change is not about automating busywork; it's about fundamentally freeing your senior platform engineers from constant toil and context-switching, allowing them to focus on high-leverage product and long-horizon research. The competitive advantage of AI-native operations is available today. **Leaders must begin evaluating and implementing their tactical roadmap to move from open-loop triage to fully autonomous ML platforms now**.

#### Table of contents

[A new on-call default](https://www.anyscale.com#a-new-on-call-default)[The new maturity model for on-call in AI platforms](https://www.anyscale.com#the-new-maturity-model-for-on-call-in-ai-platforms)[Stage 1: The coffee break (where most teams are today)](https://www.anyscale.com#stage-1:-the-coffee-break-(where-most-teams-are-today))[Stage 2: Open loop first responder (where you should strive for this half)](https://www.anyscale.com#stage-2:-open-loop-first-responder-(where-you-should-strive-for-this-half))[Stage 3: Closed loop first responder & nocturnal engineer (where you should strive for next)](https://www.anyscale.com#stage-3:-closed-loop-first-responder-&-nocturnal-engineer-(where-you-should-strive-for-next))[Getting tactical](https://www.anyscale.com#getting-tactical)[Moving forward](https://www.anyscale.com#moving-forward)
