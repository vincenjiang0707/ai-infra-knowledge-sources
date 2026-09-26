source: https://docs.nvidia.com/dynamo/zh-CN/v-0-8-1/components/planner/overview
lastmod: 2026-09-23T23:30:39.914Z

# Planner

The planner monitors the state of the system and adjusts workers to ensure that the system runs efficiently.

Currently, the planner can scale the number of vllm workers up and down based on the kv cache load and prefill queue size:

Key features include:

**SLA-based scaling**that uses predictive modeling and performance interpolation to proactively meet TTFT and ITL targets**Graceful scaling**that ensures no requests are dropped during scale-down operations

🚀 Quick Start

**New to SLA Planner?** Start with the [SLA Planner Quick Start Guide](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-planner-quick-start) for a complete, step-by-step workflow.

**Prerequisites**: SLA-based planner requires pre-deployment profiling (2-4 hours on real silicon or a few minutes using simulator) before deployment. The Quick Start guide includes everything you need.

## Feature Support Matrix

## Footnotes

-
Supported with some limitations.

[↩](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/overview#user-content-fnref-1)