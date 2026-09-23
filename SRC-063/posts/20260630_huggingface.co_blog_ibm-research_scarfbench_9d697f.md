# ScarfBench: Benchmarking AI Agents for Enterprise Java Framework Migration

source: https://huggingface.co/blog/ibm-research/scarfbench
published: Tue, 30 Jun 2026 18:32:50 GMT

Updated • 409 • 19

#
[
](https://huggingface.co#scarfbench-benchmarking-ai-agents-for-enterprise-java-framework-migration)
ScarfBench: Benchmarking AI Agents for Enterprise Java Framework Migration

[Enterprise Article](https://huggingface.co/blog)

Recent advances in coding agents have sparked excitement around AI-assisted modernization. But an important question remains:

**Can AI agents reliably modernize real-world enterprise applications?**

Existing software engineering benchmarks have demonstrated impressive progress in bug fixing and code generation, but framework migration presents a fundamentally different challenge. Success requires not only translating code, but also preserving behavior, adapting build systems, and navigating runtime dependencies.

To address this gap, we introduce **ScarfBench (Self-Contained Application Refactoring Benchmark)**, an open benchmark for evaluating AI agents on cross-framework migration tasks in Enterprise Java.

ScarfBench focuses on migrations across three major Java ecosystems:

- Spring
- Jakarta EE
- Quarkus

Unlike traditional benchmarks that compare generated code against reference implementations, ScarfBench evaluates whether migrated applications actually build, deploy, and preserve behavior.

##
[
](https://huggingface.co#why-migration-is-hard)
Why Migration Is Hard

Framework migration is much more than replacing annotations.

A simple repository migration can require changes across dependency injection, persistence configuration, queries, and framework descriptors. Small mistakes in any of these pieces can prevent successful deployment.

**Figure: Spring → Jakarta Migration Example**

Framework migration requires translating framework semantics, not just source code.

##
[
](https://huggingface.co#introducing-scarfbench)
Introducing ScarfBench

[ScarfBench](https://huggingface.co/spaces/ibm-research/ScarfBench) provides a systematic way to evaluate AI agents on enterprise Java framework migration tasks.

Applications are required to:

- Build successfully.
- Deploy correctly.
- Pass behavioral validation.

This provides a much more realistic measure of modernization quality.

## Benchmark at a Glance

ScarfBench includes both focused migration tasks and whole-application migrations.

**Figure: ScarfBench Construction Pipeline**

Starting from a JSR-based enterprise Java taxonomy, expert migrations create verified implementations across Spring, Jakarta EE, and Quarkus.

##
[
](https://huggingface.co#how-do-frontier-agents-perform)
How Do Frontier Agents Perform?

We evaluated several state-of-the-art coding agents on ScarfBench.

Despite strong performance on traditional software engineering benchmarks, framework migration remains difficult. Success rates vary considerably across framework pairs and whole-application migrations remain particularly challenging.

**Figure: Current Leaderboard**

[scarfbench.info/leaderboard](https://scarfbench.info/leaderboard)

**Figure: Compile → Deploy → Test Progression**

Compile success consistently exceeds deploy success, which in turn exceeds behavioral success. Build success alone significantly overestimates migration quality.

**Figure: Migration Outcomes by Target Framework**

Migration difficulty depends strongly on the target framework, with Jakarta EE proving particularly challenging.

##
[
](https://huggingface.co#what-we-learned-about-ai-agents-for-java-modernization)
What We Learned About AI Agents for Java Modernization

Beyond measuring success rates, ScarfBench helps us understand how agents behave during modernization.

###
[
](https://huggingface.co#can-agents-reliably-tell-when-a-migration-is-complete)
Can Agents Reliably Tell When a Migration Is Complete?

A migrated application is only useful if it actually builds and runs.

We therefore compared agent-reported outcomes against independent build verification.

####
[
](https://huggingface.co#finding-agents-are-overconfident)
Finding: Agents Are Overconfident

Claude Code reported successful builds for 29 out of 30 whole applications.

Only 22 of those applications actually built successfully.

Meanwhile, the single application classified as failed by the agent ultimately built correctly.

This suggests that agent self-assessment should not be treated as a reliable signal of migration completion.

Independent build and test validation remains essential.

###
[
](https://huggingface.co#how-do-agents-navigate-application-dependencies)
How Do Agents Navigate Application Dependencies?

Framework migrations rarely affect a single file or layer.

Changes in configuration, services, databases, and web components often cascade across the application.

####
[
](https://huggingface.co#finding-migration-is-iterative-rather-than-linear)
Finding: Migration Is Iterative Rather Than Linear

The most frequently visited layers were:

- Configuration
- Web
- Database
- Service

Common transitions included:

- Configuration ↔ Web
- Service ↔ Database

This suggests that migration is an iterative dependency-resolution process rather than a simple source-to-source transformation.

###
[
](https://huggingface.co#where-do-agents-spend-most-of-their-effort)
Where Do Agents Spend Most of Their Effort?

We used layer revisit frequency as a proxy for migration effort. Layers that required repeated visits typically involved debugging, dependency resolution, or framework adaptation.

####
[
](https://huggingface.co#finding-configuration-dominates-migration-effort)
Finding: Configuration Dominates Migration Effort

Rather than proceeding linearly, agents repeatedly returned to configuration-related artifacts while resolving framework differences and dependency issues.

###
[
](https://huggingface.co#what-challenges-are-not-about-code-transformation)
What Challenges Are Not About Code Transformation?

Not every migration issue originates from source code.

####
[
](https://huggingface.co#finding-environment-and-tooling-matter)
Finding: Environment and Tooling Matter

Agents frequently struggled with environmental issues, including:

- Docker cache inconsistencies
- Port connectivity problems
- Maven wrapper and build tooling issues

These operational concerns often delayed validation even when the source-code migration itself was largely complete.

**Figure: Failure Mode Distribution**

Modernization failures span build systems, deployment environments, dependency injection, databases, endpoints, assertions, and infrastructure.

##
[
](https://huggingface.co#key-takeaway)
Key Takeaway

The biggest challenge in framework modernization is not translating Java code.

It is managing the web of dependencies across configuration, infrastructure, and runtime environments.

While frontier agents can automate substantial portions of the migration process, reliable validation and architectural reasoning remain critical for achieving successful outcomes.

ScarfBench helps expose these challenges and provides a standardized way to measure progress toward truly autonomous application modernization.

##
[
](https://huggingface.co#explore-scarfbench)
Explore ScarfBench

ScarfBench is designed as an open resource for researchers and practitioners.

Resources include:

- Benchmark dataset
- Evaluation infrastructure
- Public leaderboard
- Documentation
- Open-source code

Researchers can compare agent architectures and techniques. Practitioners can use ScarfBench to evaluate modernization solutions before deploying them in production environments.

###
[
](https://huggingface.co#website)
Website

###
[
](https://huggingface.co#dataset)
Dataset

[https://huggingface.co/datasets/ibm-research/ScarfBench](https://huggingface.co/datasets/ibm-research/ScarfBench)

###
[
](https://huggingface.co#space)
Space

[https://huggingface.co/spaces/ibm-research/ScarfBench](https://huggingface.co/spaces/ibm-research/ScarfBench)

###
[
](https://huggingface.co#github-repository)
GitHub Repository

[https://github.com/scarfbench/scarfbench](https://github.com/scarfbench/scarfbench)

###
[
](https://huggingface.co#leaderboard)
Leaderboard

[https://scarfbench.info/leaderboard](https://scarfbench.info/leaderboard)

###
[
](https://huggingface.co#paper)
Paper

[https://arxiv.org/abs/2605.06754](https://arxiv.org/abs/2605.06754)

Framework migration remains one of the largest unsolved problems in AI-assisted software engineering. We hope ScarfBench helps the community measure progress and accelerate the next generation of AI-assisted application modernization.

We invite researchers, practitioners, and framework communities to evaluate their agents, contribute new migration scenarios and help advance the state of the art.