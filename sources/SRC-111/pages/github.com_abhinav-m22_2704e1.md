source: https://github.com/abhinav-m22

Software Engineer at Barclays. I own backend services that run in production, and I spend most of my free time contributing to open source LLM and agent infrastructure.

The part I care about starts before the code: sitting in design discussions, mapping how services talk to each other, and finding where a system will break long before it does. The interesting problem is never making something work once, it's keeping it fast and reliable when the load stops being polite.

I'd rather understand one system deeply than name drop ten.

Most of what I know about AI systems came from shipping into other people's codebases and getting reviewed by engineers who knew the domain better than I did.

[vllm-project/semantic-router](https://github.com/vllm-project/semantic-router)`Go`

`Rust`

`Envoy`

`Kubernetes`

Model routing for LLM inference, under the vLLM org alongside Red Hat, IBM Research, AMD and
Hugging Face. Contributing across the codebase.

[Archestra](https://github.com/archestra-ai/archestra)`TypeScript`

`MCP`

`RAG`

`LLM Integrations`

**25+ merged PRs**
Enterprise MCP security platform, $10M funded and running inside Fortune 50 companies.
Knowledge connectors for Google Drive, Slack, Salesforce and Linear into the retrieval
pipeline. Org wide admin audit log, agent export and clone, x.AI provider integration,
security hardening for sensitive knowledge sources.

[AgentMemory](https://github.com/rohitg00/agentmemory)`Python`

**3 merged PRs**
Memory layer for AI agents, 20k+ stars.

**Every merged PR across projects →**

**Barclays** · Software Engineer · 2025 to present

I own several production backend services end to end, from design review through deployment and on call.

**Resilient event driven flows.**Kafka producers and consumers plus Solace topic subscriptions. Most of the design work is deciding what happens when a downstream service is slow rather than down.**Memory and concurrency under load.**Fixed a service crashing with OOM in production: a million rows pulled into memory at once, a virtual thread spawned per entry, none ever shut down. Fixed by paging the reads and gating concurrency.**Transaction log friendly deletes.**A raw delete over millions of rows fills the database transaction log and can lock the database outright. Rewrote them as chunked Spring Batch jobs across SQL and MongoDB so commits stay small and failed runs resume.**Distributed cache coordination.**Kubernetes jobs refreshing in memory caches across hundreds of pods without a stampede.**Delivery.**GitLab CI/CD for multi module deploys, secrets management, automated environment provisioning.

**Earlier**

**Ridecell** · Backend Developer Intern · 2025
Refund and payment recovery workflows across 5000+ monthly transactions. Fixed Django and
Braintree integration failures, cutting error rates 35%.

**SellerSetu** · Software Developer Intern · 2024
Django REST and Go services with 75% faster endpoints. PostgreSQL to MongoDB migration for a
20% query improvement. Load balanced microservice split that cut database strain 30%.

**Barclays** · Technology Summer Intern · 2024
.NET Core status tracking tool and background worker parsing CI logs into JIRA.

```
Production Java · Spring Boot · Spring Batch · Kafka · Solace
Kubernetes · MongoDB · PostgreSQL
Also ship in Go · Python · TypeScript · Django REST · React
Platforms AWS · GCP · Docker · GitLab CI · Linux
```


```
Smart India Hackathon 2024 Winner, 1st place, software edition
Motia Backend Hackathon 2nd place, solo, of 4000+
Flipkart GRiD 5.0 Semi-finalist, top 0.5% of 400,000+
ETHIndia / ETHMumbai Sponsor prizes
```