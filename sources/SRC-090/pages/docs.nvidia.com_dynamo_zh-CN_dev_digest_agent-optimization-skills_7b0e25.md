source: https://docs.nvidia.com/dynamo/zh-CN/dev/digest/agent-optimization-skills
lastmod: 2026-09-23T23:30:39.914Z

# Dynamo Agent Optimization Skills

A skillpack that turns coding agents into disciplined performance engineers — August 2026

*(Written by a human, ironically)*

Frontier coding agents are incredibly capable, but we’ve noticed they need some help when it comes to optimizing Dynamo deployments. Today we’ve merged a “skillpack” into the Dynamo repo. It helps your coding agent optimize deployments using the same techniques NVIDIA experts use. These are repo-native instruction files, requiring no installation or explicit invocation. If you point your agent at the Dynamo repo and tell it to optimize any deployment, these skills will activate.

These skills shore up agent knowledge and behavior in three key areas:

**Objective function**- With this skillpack, your coding agent will work with you to clarify optimization objectives and turn those into a disciplined benchmarking script (default is[AIPerf](https://github.com/ai-dynamo/aiperf), our open-source benchmarking tool). This shores up the foundation of any optimization exercise.**Experimental discipline**- These skills ensure that your agent tracks experiments systematically, isolates variables to test, and passes adversarial review before consuming valuable GPU time. Absent skills, even frontier agents tend to struggle with running a clean lab.**Domain knowledge**- What optimization levers are there in Dynamo and which should be tried first? How do we layer cluster-level optimizations atop engine-level tuning? Agents don’t know this natively, so we’ve added skills to help guide them efficiently and make sure the optimization process moves the biggest levers first.

Our Solutions Architects have been field testing these skills in real customer scenarios and we’ve been very happy with the results. Compared to “unskilled” coding agents with the Dynamo repo, our skill-infused agents reached 15% to 77% better throughput in our internal A/B tests (same model, same GPUs, same goal per pair; one Claude Code pair and one Codex pair, measured with AIPerf). And our teams love the way that optimization work can proceed while they sleep! Below is the hill climb that one agent performed while we slept.

To get started, just clone [Dynamo](https://github.com/ai-dynamo/dynamo), point your coding agent at the repo, and tell it to optimize your deployment. The [Agent Skills docs page](https://docs.nvidia.com/dynamo/dev/agent-skills/overview) has the full skill inventory plus practical notes on GPU budgets and unattended runs. We’ll be adding new skills all of the time, so agents will get smarter as Dynamo evolves.