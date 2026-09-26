# [Issue #1609] [Proposal]: Integration with Envoy AI Gateway

source: https://github.com/ai-dynamo/dynamo/issues/1609
state: open | updated: 2026-09-22T06:01:25Z
labels: enhancement, dep:proposed, process

## 正文

This proposal is going to track the process to integrate with Envoy AI Gateway in the current architecture. Empower the traffic management with an unified AI Gateway, working well with the dynamo frontend.

### Summary 

Currently, we supported frontend as the access endpoint for exposing the inference workload, it is great to work with the router and optimize the TTFT based on the prefix-cache awareness routing and load metrics exposed from the inference pod.

In production scenario, we usually need an AI Gateway, which can work well with the Inference Router/Gateway as the AI Unified Gateway, solving problems like:

<img width="907" alt="Image" src="https://github.com/user-attachments/assets/8c5166c7-358b-4d6d-afed-de8032c7dbfc" />

This proposal is going to add integrations with Envoy Gateway as well as the Envoy AI Gateway.

<img width="1163" alt="Image" src="https://github.com/user-attachments/assets/e022d4b1-dea7-4386-b9e5-9da7f8880700" />


### Goals

1. provide a seamless integration for adopting the Envoy AI Gateway, working well with the frontend.
2. provide a long-term collaboration with Dynamo to work with the AI/LLM traffic management needs.

### Background

[EnvoyProxy](https://github.com/envoyproxy/envoy) is a CNCF graduation project, [Envoy Gateway](https://github.com/envoyproxy/gateway) is an official API Gateway implementation of EnvoyProxy, with a widely adopters in production, driven by community. 

 [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) is an open source project for using Envoy Gateway to handle request traffic from application clients to GenAI services, based on, focusing on the LLM era traffic management. Envoy AI Gateway is a vendor-neutral, community driven OSS.it is gathering the envoy gateway and envoyproxy experts, envoy team core maintainer to grow fast and is open to collaborate.

Keynote in KubeCon 2024 NA: [intro](https://www.youtube.com/watch?v=do1viOk8nok&ab_channel=CNCF%5BCloudNativeComputingFoundation%5D), 

Before this proposal, it is adopted by [KServe](https://kserve.github.io/website/latest/admin/ai-gateway_integration/) under the kubernetes WG Serving umbrella, as their unified AI Gateway, and based on Envoy Gateway`s extensibility, the vLLM [AIBrix](https://github.com/vllm-project/aibrix) adopts Envoy Gateway to use as their inference Gateway like the router in Dynamo, implemented routing strategies like prefix-cache aware, load aware and a tons of routing algorithms. And also working on the upgrade from Envoy Gateway to Envoy AI Gateway, as their unified AI Gateway. 

### Design

This integration will let Dynamo focus on routing algorithm, performance and inference optimization. And the global Envoy AI Gateway workes on the routing with different frontend, provide higher level traffic management, service government, advanced security AuthZ/AuthN, extensible ecosystem (MCP/Agent).

Here are some advantages for expanding the traffic management layer with Envoy AI gateway, including:

1. Hybrid Routing Strategy: proxying from the in-cluster inference GW and out-cluster LLM Provider, like: routing to a same model in cluster and fallback to the LLM Provider when in-cluster inference workload is down. Or traffic split between the in-cluster and out-cluster, to take on some of the traffic pressure, also like canary release of inference workload etc.
2. Advanced Upstream Authentication: support various authentication like API Key, AWS Bedrock, Azure Credentials, and short-lived, long-lived access credentials management.
3. Advanced Token-Based ratelimit: support input/output/total/CEL token cost limit.
4. Unified OpenAI API compatible: chat, completions, embeddings etc.
5. Integration with custom Backend: with Envoy AI Gateway extensibility, we can quickly support various of Custom Backend.
6. Advanced Scheduling Policies: AI Gateway provides advanced scheduling like priority based scheduling between Models, Load aware routing, semantic cache etc.
8. Content Safety: intergration with external security detection service to ensure content safety.
9. AI/LLM Observability: AI Gateway provides unified metrics to access LLM Workloads, metrics based HPA etc.
10. Multi-tenant Support: natively supported the cross-namespace traffic orchestrations.
11. MCP & Agent Gateway: MCP support to integrate with LLM/Agents.


#### Deploy Mode

Frontend is focusing on model level routing, traffic cannot schedule between different models, namespace etc, this is how typical deployed in Kubernetes:

<img width="1580" alt="Image" src="https://github.com/user-attachments/assets/888c051f-ad14-470d-a47e-98e99b073364" />

Withing Envoy AI Gateway, it looks like:

<img width="1584" alt="Image" src="https://github.com/user-attachments/assets/72fddbee-726c-4c48-91c3-aa98c78bfe34" />

And even supported hybrid mode like:

<img width="1333" alt="Image" src="https://github.com/user-attachments/assets/03bfe6fb-291e-40a6-8f5f-7595e108038e" />

Envoy AI Gateway can route to both in-cluster dynamo workload and to out-cluster model platform, typical scenario can be traffic split, pressure load balancing, fallback etc.

#### Resource Relation

This section describes the relation between AI Gateway and Dynamo Resources, in short, they work with each other by the K8S Service exposed by frontend,

**Routing between different dynamo workloads for different models**

<img width="943" alt="Image" src="https://github.com/user-attachments/assets/21add3c9-f3b6-42ba-96ec-e41a0600e99a" />

**Routing between dynamo workload and model provider for the same model**

<img width="918" alt="Image" src="https://github.com/user-attachments/assets/e5c72ae6-ff8c-487d-b492-ae373441e571" />

Looking forward to the collaboration, We`d love to have long-term collaboration on AI Gateway part.


### Use Case

Solution for Unified AI/LLM traffic management


## 评论 (2)

### tzulingk · 2026-06-29

**Triage (DGH rotation):** Classifying this as a **DEP / design proposal** (not a bug) — labeled `dep:proposed` and keeping it in DGH for the Dynamo Enhancement Proposals review process rather than the bug-triage flow.

@nnshah1 — routing to you as DEP review owner: please pull this into the Dynamo Enhancement Proposals project and assign a PiC. It's a community/partner proposal (Envoy AI Gateway integration, authored by @Xunzhuo, impl side assigned to @hutm), so it warrants the proposal review track.

### rmccorm4 · 2026-09-22

Hi @Xunzhuo, thanks for raising this. 

I wanted to follow up on this issue. What is the current state and what would be the ideal next steps to get some traction on this?
