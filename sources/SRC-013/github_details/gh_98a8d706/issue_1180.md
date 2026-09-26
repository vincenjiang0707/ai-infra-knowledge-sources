# [Issue #1180] Guided llm-d install missions in KubeStellar Console

source: https://github.com/llm-d/llm-d/issues/1180
state: open | updated: 2026-09-25T01:19:32Z
labels: lifecycle/rotten

## 正文

We built guided install missions for llm-d inside [KubeStellar Console](https://console.kubestellar.io?utm_source=github&utm_medium=issue&utm_campaign=cncf_outreach&utm_term=llm-d), a standalone Kubernetes dashboard (unrelated to legacy kubestellar/kubestellar, kubeflex, or OCM — zero shared code).

→ **[Browse the llm-d mission catalog](https://console.kubestellar.io/missions?tag=llm-d&utm_source=github&utm_medium=issue&utm_campaign=cncf_outreach&utm_term=llm-d)**

### What the missions do

The Console ships nine specialized install missions covering llm-d's well-lit paths — single-node, disaggregated prefill/decode, tensor parallelism, and the companion Inference Scheduler. Each mission runs against your live cluster via kubeconfig, checks prerequisites, applies the corresponding manifests or Helm chart, validates pod readiness and CRD registration, and ships a rollback path.

### Why we're reaching out

llm-d is part of the Console's broader local-LLM strategy, which covers Ollama (dev), llama.cpp (minimal), LocalAI (CPU-first), vLLM (GPU throughput), Red Hat AI Inference Server (OpenShift enterprise), LM Studio (workstation GUI), and Open WebUI (frontend). llm-d slots in as the \"multi-node inference scheduling\" option for operators running GPU clusters at scale. See the [Local LLM Strategy](https://docs.kubestellar.io/console/local-llm-strategy?utm_source=github&utm_medium=issue&utm_campaign=cncf_outreach&utm_term=llm-d) docs page for the full decision matrix.

Separately, the Console's [workload-variant-autoscaler nightly E2E harness](https://github.com/llm-d/llm-d-infra?utm_source=github&utm_medium=issue&utm_campaign=cncf_outreach&utm_term=llm-d) is already wired into llm-d-infra and has been running since 2026-03. This issue is about the install-mission surface, which is a separate touchpoint.

### Install

Local (connects to your current kubeconfig context):
```bash
curl -sSL https://raw.githubusercontent.com/kubestellar/console/main/start.sh | bash
```

Deploy into a cluster:
```bash
curl -sSL https://raw.githubusercontent.com/kubestellar/console/main/deploy.sh | bash
```

---

Mission definitions are open source — PRs welcome at [fixes/llm-d/](https://github.com/kubestellar/console-kb/tree/master/fixes/llm-d?utm_source=github&utm_medium=issue&utm_campaign=cncf_outreach&utm_term=llm-d). Feel free to close if not relevant.

## 评论 (1)

### github-actions[bot] · 2026-09-10

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
