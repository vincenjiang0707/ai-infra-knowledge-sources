source: https://docs.nvidia.com/dynamo/zh-CN/dev/agent-skills/optimization
lastmod: 2026-09-23T23:30:39.914Z

# Performance Optimization Skills

The evidence-driven loop that benchmarks a confirmed baseline and challenges it with candidates.

These skills form the optimization workflow: capture a workload contract, benchmark a confirmed
baseline, then challenge it with one candidate at a time until the Service Level Objectives (SLOs)
are met or the budget runs out. The loop also uses
[ deploy-dynamo-recipe](https://github.com/ai-dynamo/dynamo/tree/main/.agents/skills/deploy-dynamo-recipe),
listed on the

[Deployment and Operations](https://docs.nvidia.com/dynamo/dev/agent-skills/deployment)page, to deploy the confirmed baseline and each approved candidate.

A prompt that reaches them: “Optimize this deployment for output tokens per second per user under a 200 ms time-to-first-token SLO. Budget 8 GPU-hours and stop after three failed deployments.”

See the
[optimization loop](https://github.com/ai-dynamo/dynamo/blob/main/agent-docs/guides/optimization/optimize-loop.md)
for the full sequence and the
[evidence rules](https://github.com/ai-dynamo/dynamo/tree/main/agent-docs/rules) for benchmark
validity requirements.