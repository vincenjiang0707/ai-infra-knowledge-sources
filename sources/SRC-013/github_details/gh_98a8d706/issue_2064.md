# [Issue #2064] Your project is on StackMap — a curated map of the AI stack

source: https://github.com/llm-d/llm-d/issues/2064
state: open | updated: 2026-09-06T13:00:58Z
labels: 

## 正文

Hi — I curate **[StackMap](https://stackmap.shipwithai.xyz?utm_source=maintainer-outreach)**, a hand-curated knowledge graph of open-source AI/agent tools. Every entry is human-reviewed: a summary, an opinionated note on when to use it (and when not), and typed edges to what it pairs with or competes against — with the *why* written down.

**llm-d** earned a place on the map:
- Your page: https://stackmap.shipwithai.xyz/repos/llm-d/llm-d
- On the graph: https://stackmap.shipwithai.xyz/?focus=llm-d

How we mapped it:
- **built with `vllm`** — llm-d is explicitly the orchestration layer above model servers: vLLM does the on-accelerator inference, llm-d adds cluster-level routing, KV-cache management, disaggregation and autoscaling.
- **alternative to `ollama`** — Same job — serve open models on your own hardware — at opposite scales: Ollama is one command on one machine; llm-d is a CNCF stack for multi-node GPU fleets. Outgrow one, reach for the other.

If any of this misrepresents the project — an edge you'd dispute, a sharper "when NOT to use" — reply here and a human fixes it. And feel free to just close this issue; it's only a heads-up.

## 评论 (1)

### hoghweed · 2026-09-06

Small follow-up on the above, then I'll get out of your inbox.

Since that issue, every mapped repo has a badge. If you want the mapping visible in your README:

```markdown
[![On StackMap](https://img.shields.io/endpoint?url=https%3A%2F%2Fstackmap.shipwithai.xyz%2Fapi%2Fbadge%2Fllm-d.json)](https://stackmap.shipwithai.xyz/repos/llm-d/llm-d?utm_source=badge)
```

It renders as `StackMap | ↔ 7 typed links` and links to the llm-d page on the map — the count is how many human-reviewed relationships we've written for it.
The endpoint is static JSON, so it updates itself as the map changes. No script, no tracking, nothing for you to maintain.

Genuinely no obligation and no reply needed. If any of the mapping is still wrong, that's the reply I'd rather have.
