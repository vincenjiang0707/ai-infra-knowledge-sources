# [Issue #1658] [Autoscaling] Add a guide to show WVA ability to balance between two different InferencePools

source: https://github.com/llm-d/llm-d/issues/1658
state: open | updated: 2026-09-19T01:17:00Z
labels: help wanted, lifecycle/rotten

## 正文

For more context, see https://llm-d.slack.com/archives/C08T899332A/p1780347920986139

## 评论 (4)

### ManishSharma1609 · 2026-06-04

Hi @ahg-g , I'd like to work on this! 
From the linked discussion, it seems the main gap is documenting how WVA works across multiple InferencePools and providing a concrete example of that setup. I'm planning to clarify the per-pool vs. per-cluster/namespace behavior in the existing WVA docs and add a guide with manifests demonstrating a multi-InferencePool configuration.

### ahg-g · 2026-06-04

Thanks @ManishSharma1609, when do you think you can provide that?

/assign @ManishSharma1609 

### ManishSharma1609 · 2026-06-05

Hi @ahg-g, just opened PR #1696. Happy to incorporate any feedback!

### github-actions[bot] · 2026-09-04

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
