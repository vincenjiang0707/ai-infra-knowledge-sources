# AIBrix

source: https://github.com/vllm-project/aibrix/releases

# Releases: vllm-project/aibrix

## Release list

## v0.7.0

AIBrix v0.7.0 is here! This release lands **242 merged PRs** over three months and pushes AIBrix toward a composable, self-service inference platform. The theme this cycle is **composability across the operational, workload, engine, and gateway layers**: a new web Console for self-service operations, a production OpenAI-compatible Batch API, first-class multi-engine support (vLLM, SGLang, **TensorRT-LLM**), a KV-cache-centric P/D disaggregation data plane, and a highly-available gateway with pluggable, blendable routing.

📖 Read the full release blog: [https://aibrix.github.io/posts/2026-06-16-v0.7.0-release/](https://aibrix.github.io/posts/2026-06-16-v0.7.0-release/)


⚠️ Maturity note: TheConsole,Batch API, andResource Manager / Cloud GPU executionare new or rebuilt in this cycle and are evolving quickly. Treat them as preview features for now — APIs and behavior may change in v0.8.0.

## 🚀 New Features Highlights

**AIBrix Management Console (Preview)**

**Web-based control plane**: A new React frontend + Go backend that lets users register models, deploy from reusable versioned templates, submit and track batch jobs, and download results — no`kubectl`

/YAML required. ([#2094](https://github.com/vllm-project/aibrix/pull/2094),[#2095](https://github.com/vllm-project/aibrix/pull/2095),[#2176](https://github.com/vllm-project/aibrix/pull/2176))**Model & template-centric UX**:`ModelDeploymentTemplate`

with model-centric workflows,`CreateModel`

API with HDFS path support, and provider-agnostic templates. ([#2141](https://github.com/vllm-project/aibrix/pull/2141),[#2144](https://github.com/vllm-project/aibrix/pull/2144),[#2175](https://github.com/vllm-project/aibrix/pull/2175),[#2214](https://github.com/vllm-project/aibrix/pull/2214))**Enterprise & auth**: OIDC login/callback with real user avatar rendering, MySQL backend, file proxy, and feature flags to gate Deployments/Playground. ([#2100](https://github.com/vllm-project/aibrix/pull/2100),[#2177](https://github.com/vllm-project/aibrix/pull/2177),[#2178](https://github.com/vllm-project/aibrix/pull/2178),[#2187](https://github.com/vllm-project/aibrix/pull/2187),[#2188](https://github.com/vllm-project/aibrix/pull/2188),[#2314](https://github.com/vllm-project/aibrix/pull/2314))**Batch experience in console**: job execution details, pagination, owner filtering, owner-only downloads, cursor-based listing, and an error-injection framework for resilience testing. ([#2244](https://github.com/vllm-project/aibrix/pull/2244),[#2268](https://github.com/vllm-project/aibrix/pull/2268),[#2272](https://github.com/vllm-project/aibrix/pull/2272),[#2274](https://github.com/vllm-project/aibrix/pull/2274),[#2317](https://github.com/vllm-project/aibrix/pull/2317),[#2336](https://github.com/vllm-project/aibrix/pull/2336))**Storage backends**: URI-based store factory with pure-Go SQLite driver and a hardened DB schema for self-hosted deployments. ([#2174](https://github.com/vllm-project/aibrix/pull/2174),[#2182](https://github.com/vllm-project/aibrix/pull/2182),[#2208](https://github.com/vllm-project/aibrix/pull/2208),[#2209](https://github.com/vllm-project/aibrix/pull/2209),[#2212](https://github.com/vllm-project/aibrix/pull/2212))

**OpenAI-Compatible Batch API (Rebuilt for Production)**

**Wire-compatible Batch API**: Self-hosted async batch processing for`/v1/chat/completions`

,`/v1/completions`

, and`/v1/embeddings`

, backed by a persistent metadata store and an async job state machine. ([#2136](https://github.com/vllm-project/aibrix/pull/2136),[#2147](https://github.com/vllm-project/aibrix/pull/2147),[#2185](https://github.com/vllm-project/aibrix/pull/2185),[#2203](https://github.com/vllm-project/aibrix/pull/2203))**Config-driven deployment**:`ModelDeploymentTemplate`

+`BatchProfile`

, inline template specs end-to-end, and the optional`aibrix.model_template`

extension to specify deployment. ([#2134](https://github.com/vllm-project/aibrix/pull/2134),[#2207](https://github.com/vllm-project/aibrix/pull/2207),[#2236](https://github.com/vllm-project/aibrix/pull/2236),[#2306](https://github.com/vllm-project/aibrix/pull/2306))**Execution engine rebuild**: Reworked around a`Runtime`

+`compute.provider`

model (retiring kopf/JobCache), with SSH-launch runtimes for cloud providers and a smart client with transport retry. ([#2257](https://github.com/vllm-project/aibrix/pull/2257),[#2261](https://github.com/vllm-project/aibrix/pull/2261),[#2267](https://github.com/vllm-project/aibrix/pull/2267),[#2339](https://github.com/vllm-project/aibrix/pull/2339))**Robust job lifecycle**: scheduling concurrency fixes, double-release prevention, job informer + pagination, and improved resilience across scheduler, console, and engine adapter. ([#2217](https://github.com/vllm-project/aibrix/pull/2217),[#2218](https://github.com/vllm-project/aibrix/pull/2218),[#2226](https://github.com/vllm-project/aibrix/pull/2226),[#2240](https://github.com/vllm-project/aibrix/pull/2240),[#2270](https://github.com/vllm-project/aibrix/pull/2270),[#2322](https://github.com/vllm-project/aibrix/pull/2322))**New API surface**: OpenAI**Responses API**support. ([#2312](https://github.com/vllm-project/aibrix/pull/2312))

**Resource Manager & Cloud GPU Execution (Preview)**

**Pluggable provider model**: Resource Manager interfaces with a GORM-backed store and k8s-backed provisioning. ([#2171](https://github.com/vllm-project/aibrix/pull/2171),[#2172](https://github.com/vllm-project/aibrix/pull/2172),[#2183](https://github.com/vllm-project/aibrix/pull/2183))**Cloud GPU providers**:**Lambda Cloud**and**RunPod**via a registry/provider pattern, enabling batch jobs to burst to cloud GPUs. ([#2248](https://github.com/vllm-project/aibrix/pull/2248))**Non-blocking planner**: policy-plugin planner with exponential backoff on provisioning failures and provider-agnostic core. ([#2239](https://github.com/vllm-project/aibrix/pull/2239),[#2280](https://github.com/vllm-project/aibrix/pull/2280),[#2319](https://github.com/vllm-project/aibrix/pull/2319))

**Multi-Engine Support (vLLM, SGLang, TensorRT-LLM)**

**TensorRT-LLM as a first-class engine**: tensor-rt inference engine support, TRT-LLM v1.1.0 metrics integration, and PD support for TRT-LLM 1.3.x. ([#2000](https://github.com/vllm-project/aibrix/pull/2000),[#2005](https://github.com/vllm-project/aibrix/pull/2005),[#2043](https://github.com/vllm-project/aibrix/pull/2043))**Engine-aware routing & metrics**: model validation and routing context carry engine information; per-engine metrics fixes for load- and KV-aware routing. ([#2022](https://github.com/vllm-project/aibrix/pull/2022),[#2118](https://github.com/vllm-project/aibrix/pull/2118))**Cross-engine PD validation**: PD disaggregation e2e tests across vLLM, SGLang, and TRT-LLM. ([#2080](https://github.com/vllm-project/aibrix/pull/2080))**vLLM-Omni / multimodal**: vLLM-Omni endpoints in mock + Dockerfile, multi-model per-service config, and v0.14.0 integration. ([#2036](https://github.com/vllm-project/aibrix/pull/2036),[#2037](https://github.com/vllm-project/aibrix/pull/2037),[#2056](https://github.com/vllm-project/aibrix/pull/2056),[#2129](https://github.com/vllm-project/aibrix/pull/2129))

**KV-Cache-Centric P/D Disaggregation**

**Unified KV data plane**: L2 KVCache zero-copy APIs and vLLM v0.14.0 integration over a single`aibrix_kvcache`

substrate (L1 DRAM + pluggable L2, PrisKV production backend). ([#2056](https://github.com/vllm-project/aibrix/pull/2056),[#2060](https://github.com/vllm-project/aibrix/pull/2060))**Connectors**:`AIBrixPDReuseConnector`

with prefix-cache support, per-pod KV connector type selection via pod labels, and Type2-inherits-Type1 connector refactor. ([#2092](https://github.com/vllm-project/aibrix/pull/2092),[#2125](https://github.com/vllm-project/aibrix/pull/2125),[#2238](https://github.com/vllm-project/aibrix/pull/2238))**Pluggable PD routing**: pluggable prefill score policies (least_request, prefix_cache), configurable decode scorers, decode pod load balancing, and a`KVTransferAgent`

abstraction (Mooncake stub). ([#2070](https://github.com/vllm-project/aibrix/pull/2070),[#2087](https://github.com/vllm-project/aibrix/pull/2087),[#2105](https://github.com/vllm-project/aibrix/pull/2105),[#2284](https://github.com/vllm-project/aibrix/pull/2284))**PD refactors & hardening**: split router into focused files, extracted`EngineHandler`

/`PodSelector`

and`PrefillExecutor`

, and fixed stale-handle/slot_mapping issues in connector type2. ([#2121](https://github.com/vllm-project/aibrix/pull/2121),[#2232](https://github.com/vllm-project/aibrix/pull/2232),[#2308](https://github.com/vllm-project/aibrix/pull/2308),[#2320](https://github.com/vllm-project/aibrix/pull/2320))

**Highly-Available Gateway with Composable Routing**

**Cross-replica state sync**: Redis-backed state sync for the in-memory gateway cache, aggregating running requests and prefix-cache state across gateway instances for consistent routing. ([#1989](https://github.com/vllm-project/aibrix/pull/1989),[#2159](https://github.com/vllm-project/aibrix/pull/2159))**Composable, blendable routing**: multi-strategy routing with normalized soft-scoring and weighting (e.g.`"least-request:2,throughput:1"`

), routing profiles, and a power-of-two router with request-tracker callbacks. ([#1944](https://github.com/vllm-project/aibrix/pull/1944),[#2024](https://github.com/vllm-project/aibrix/pull/2024),[#2124](https://github.com/vllm-project/aibrix/pull/2124))**Production hardening**: per-model RPS rate limiting, always-on prefix-cache metrics, HTTPRoute status caching to drop per-request API calls, GOMAXPROCS tuning, and graceful ext_proc shutdown. ([#2137](https://github.com/vllm-project/aibrix/pull/2137),[#2200](https://github.com/vllm-project/aibrix/pull/2200),[#2283](https://github.com/vllm-project/aibrix/pull/2283),[#2313](https://github.com/vllm-project/aibrix/pull/2313),[#2334](https://github.com/vllm-project/aibrix/pull/2334))

## 📊 Feature Enhancements

**Local mode**: Run gateway, router, and KV cache without Kubernetes, with Redis now optional and a local`/v1/models`

endpoint. ([#2039](https://github.com/vllm-project/aibrix/pull/2039),[#2055](https://github.com/vllm-project/aibrix/pull/2055),[#2058](https://github.com/vllm-project/aibrix/pull/2058))**Anthropic compatibility**: New`/v1/messages`

endpoint. ([#2115](https://github.com/vllm-project/aibrix/pull/2115))**OpenTelemetry tracing**: Optional end-to-end tracing with upstream`x-request-id`

preservation. ([#2157](https://github.com/vllm-project/aibrix/pull/2157),[#2255](https://github.com/vllm-project/aibrix/pull/2255),[#2271](https://github.com/vllm-project/aibrix/pull/2271))**Pluggable service discovery**: Unified`Provider`

interface (static / Consul / etcd) with refreshed static discovery. ([#2034](https://github.com/vllm-project/aibrix/pull/2034),[#2035](https://github.com/vllm-project/aibrix/pull/2035))**Autoscaling**: KV cache usage percentage added to APA, plus documented PodAutoscaler annotations. ([#2057](https://github.com/vllm-project/aibrix/pull/2057),[#2282](https://github.com/vllm-project/aibrix/pull/2282))**Chat app**: backend service, Dockerfile/compose/k8s manifests, image attachments, edit/retry persistence and UI cleanup. ([#1971](https://github.com/vllm-project/aibrix/pull/1971),[#1996](https://github.com/vllm-project/aibrix/pull/1996),[#2102](https://github.com/vllm-project/aibrix/pull/2102),[#2278](https://github.com/vllm-project/aibrix/pull/2278))**brixbench**: benchmark provisioning harness for release validation and regression testing, with PD routing scenarios and docs. ([#2165](https://github.com/vllm-project/aibrix/pull/2165),[#2273](https://github.com/vllm-project/aibrix/pull/2273),[#2298](https://github.com/vllm-project/aibrix/pull/2298),[#2352](https://github.com/vllm-project/aibrix/pull/2352))

## 📦 Installation & Tooling & CI

**Helm**: external Redis config with component-level password validation, controller-manager env support, router idleTimeout, and CRDs separated from operator manifests. ([#2201](https://github.com/vllm-project/aibrix/pull/2201),[#2216](https://github.com/vllm-project/aibrix/pull/2216),[#2222](https://github.com/vllm-project/aibrix/pull/2222),[#2230](https://github.com/vllm-project/aibrix/pull/2230),[#2234](https://github.com/vllm-project/aibrix/pull/2234))**CI**: build & preload AIBrix images into kind for chart-testing, multi-arch vllm-mock builds, reduced e2e workflow time, ruff bump/format, and CI action upgrades. ([#2059](https://github.com/vllm-project/aibrix/pull/2059),[#2081](https://github.com/vllm-project/aibrix/pull/2081),[#2093](https://github.com/vllm-project/aibrix/pull/2093),[#2219](https://github.com/vllm-project/aibrix/pull/2219),[#2259](https://github.com/vllm-project/aibrix/pull/2259),[#2349](https://github.com/vllm-project/aibrix/pull/2349))**Docs**: production gateway deployment guide, expanded routing/PD guides, vLLM semantic router integration, local-mode, console production setup, batch inference, and brixbench usage. ([#2189](https://github.com/vllm-project/aibrix/pull/2189),[#2192](https://github.com/vllm-project/aibrix/pull/2192),[#2193](https://github.com/vllm-project/aibrix/pull/2193),[#2337](https://github.com/vllm-project/aibrix/pull/2337),[#2347](https://github.com/vllm-project/aibrix/pull/2347),[#2348](https://github.com/vllm-project/aibrix/pull/2348))

## 🐞 Critical Bug Fixes

- Fix per-model metrics cross-talk on multi-model pods and drop duplicate metric-label sanitization. (
[#2228](https://github.com/vllm-project/aibrix/pull/2228),[#2331](https://github.com/vllm-project/aibrix/pull/2331)) - Fix session-affinity routing by preserving the
`x-session-id`

header and prevent nil-pointer panic in request tracking on context cancellation. ([#2122](https://github.com/vllm-project/aibrix/pull/2122),[#2338](https://github.com/vllm-project/aibrix/pull/2338)) - Fix several data races:
`TreeNode.lastAccess`

in prefix cache, SLO router fallback init, and shared`SyncPrefixHashTable`

instance. ([#2096](https://github.com/vllm-project/aibrix/pull/2096),[#2106](https://github.com/vllm-project/aibrix/pull/2106),[#2327](https://github.com/vllm-project/aibrix/pull/2327)) - Fix
`/v1/models`

returning 404 without a trailing slash and remove`min_tokens`

from PD prefill requests to avoid vLLM validation failure. ([#2194](https://github.com/vllm-project/aibrix/pull/2194),[#2237](https://github.com/vllm-project/aibrix/pull/2237)) - Prevent goroutine leaks in periodical sync loops and make the gRPC max message size configurable via env var. (
[#2077](https://github.com/vllm-project/aibrix/pull/2077),[#2364](https://github.com/vllm-project/aibrix/pull/2364)) - Clean up orphan resources when RoleSet
`podGroupSize`

changes. ([#2131](https://github.com/vllm-project/aibrix/pull/2131))

## New Contributors

[@jasonlee-1024](https://github.com/jasonlee-1024)made their first contribution in[#1990](https://github.com/vllm-project/aibrix/pull/1990)[@Lucas-Qian6](https://github.com/Lucas-Qian6)made their first contribution in[#1996](https://github.com/vllm-project/aibrix/pull/1996)[@xvchris](https://github.com/xvchris)made their first contribution in[#2007](https://github.com/vllm-project/aibrix/pull/2007)[@NJX-njx](https://github.com/NJX-njx)made their first contribution in[#1982](https://github.com/vllm-project/aibrix/pull/1982)[@DhyeyTr](https://github.com/DhyeyTr)made their first contribution in[#2057](https://github.com/vllm-project/aibrix/pull/2057)[@gabrnavarro](https://github.com/gabrnavarro)made their first contribution in[#2069](https://github.com/vllm-project/aibrix/pull/2069)[@tmchow](https://github.com/tmchow)made their first contribution in[#2076](https://github.com/vllm-project/aibrix/pull/2076)[@Peakpine](https://github.com/Peakpine)made their first contribution in[#2108](https://github.com/vllm-project/aibrix/pull/2108)[@naroam1](https://github.com/naroam1)made their first contribution in[#2119](https://github.com/vllm-project/aibrix/pull/2119)[@Yang1032](https://github.com/Yang1032)made their first contribution in[#2122](https://github.com/vllm-project/aibrix/pull/2122)[@DaveLi8086](https://github.com/DaveLi8086)made their first contribution in[#2153](https://github.com/vllm-project/aibrix/pull/2153)[@Genmin](https://github.com/Genmin)made their first contribution in[#2168](https://github.com/vllm-project/aibrix/pull/2168)[@ianliuy](https://github.com/ianliuy)made their first contribution in[#2118](https://github.com/vllm-project/aibrix/pull/2118)[@HeyZackWang](https://github.com/HeyZackWang)made their first contribution in[#2157](https://github.com/vllm-project/aibrix/pull/2157)[@zhutong196](https://github.com/zhutong196)made their first contribution in[#2194](https://github.com/vllm-project/aibrix/pull/2194)[@justinchen033](https://github.com/justinchen033)made their first contribution in[#2226](https://github.com/vllm-project/aibrix/pull/2226)[@Jing-ze](https://github.com/Jing-ze)made their first contribution in[#2228](https://github.com/vllm-project/aibrix/pull/2228)[@NelZyhh](https://github.com/NelZyhh)made their first contribution in[#2230](https://github.com/vllm-project/aibrix/pull/2230)[@ju](https://github.com/ju)...

[Read more](https://github.com/vllm-project/aibrix/releases/tag/v0.7.0)

## v0.6.0

# Release Notes

## 📌 Release Summary

- Improvements to
**gateway routing and traffic management**for LLM inference services. - Enhancements to
**distributed serving and orchestration**, enabling more flexible multi-node deployments. - Updates to
**batch request processing and OpenAI-compatible APIs**. - Better
**metrics and observability**support. - Various
**bug fixes, stability improvements, and CI/CD updates**.

Overall: This release focuses on improving routing, scalability, and operational stability for running vLLM-based LLM services in Kubernetes.

## 🚀 New Feature Highlights

**Expanded OpenAI-Compatible API Surface**

This release significantly expands the OpenAI-compatible API capabilities supported by AIBrix.

**Audio & Classification APIs**: Added support for OpenAI-style audio endpoints (/v1/audio/transcriptions, /v1/audio/translations) along with the new /v1/classify inference API. ([#1859](https://github.com/vllm-project/aibrix/pull/1859),[#1905](https://github.com/vllm-project/aibrix/pull/1905))**Image Generation Endpoint**: Introduced OpenAI-compatible generation APIs for images and videos (/v1/images/generations, /v1/video/generations), allowing multimodal generation workloads to run through the same gateway. ([#1867](https://github.com/vllm-project/aibrix/pull/1867))**Rerank Model Support**: Added support for rerank models via the /v1/rerank endpoint, enabling improved ranking and retrieval pipelines. ([#1837](https://github.com/vllm-project/aibrix/pull/1837))

These additions further strengthen AIBrix as a unified gateway for diverse AI workloads.

**Advanced Gateway & Routing Capabilities**

Major improvements were made to the gateway routing layer to enable smarter and more flexible inference traffic management.

**Session Affinity Routing**: Add plugin-based session affinity routing strategies for sticky workloads. ([#1751](https://github.com/vllm-project/aibrix/pull/1751),[#1823](https://github.com/vllm-project/aibrix/pull/1823))**Advanced Routing Filters**: Support external header filters for advanced routing scenarios. ([#1804](https://github.com/vllm-project/aibrix/pull/1804))**Custom HTTPRoute Paths**: Allow custom path configuration through annotations. ([#1841](https://github.com/vllm-project/aibrix/pull/1841))**Multi-Deployment Router Support**: Enable router configuration across multiple deployment targets. ([#1835](https://github.com/vllm-project/aibrix/pull/1835))**Least-Request Routing Strategy**: Introduce distributed DP API server routing using least-request algorithms. ([#1866](https://github.com/vllm-project/aibrix/pull/1866))

Together these improvements provide better flexibility when deploying large-scale inference workloads.

**Prefill/Decode (P/D) Disaggregation Improvements**

This release continues to expand support for Prefill/Decode disaggregated inference architectures.

**PD + KVCache Routing Compatibility**: Enable routing that supports both KVCache and P/D disaggregation within a single runtime image. ([#1781](https://github.com/vllm-project/aibrix/pull/1781))**Prefix Cache Optimizations**: Introduce asynchronous prefix cache updates and shared indexers across routing strategies. ([#1914](https://github.com/vllm-project/aibrix/pull/1914),[#1939](https://github.com/vllm-project/aibrix/pull/1939))**Combined Routing Strategy with P/D**: Enables intelligent routing across both PD-optimized pods (prefill/decode disaggregated) and combined pods (non-PD) within the same deployment, allowing mixed serving strategies and improved resource utilization. ([#1911](https://github.com/vllm-project/aibrix/pull/1911))

These changes improve the scalability and flexibility of large LLM inference clusters.

**StormService & Control Plane Enhancements**

The StormService controller received multiple upgrades to improve reliability and visibility.

**Role Revision Tracking**: Add per-role revision tracking to StormService for improved upgrade visibility. ([#1731](https://github.com/vllm-project/aibrix/pull/1731))**Role Status Aggregation**: Implement role-level status aggregation and improvements to reconcile logic. ([#1761](https://github.com/vllm-project/aibrix/pull/1761),[#1767](https://github.com/vllm-project/aibrix/pull/1767))**Periodic Reconciliation**: Introduce periodic reconciliation for ModelAdapter resources. ([#1824](https://github.com/vllm-project/aibrix/pull/1824))**Dynamic Discovery Provider Updates**: Enable discovery providers to dynamically update runtime state. ([#1908](https://github.com/vllm-project/aibrix/pull/1908))**Improved Scheduling Integration**: Enhance PodGroup and scheduling strategy handling. ([#1889](https://github.com/vllm-project/aibrix/pull/1889),[#1795](https://github.com/vllm-project/aibrix/pull/1795))

These changes strengthen the orchestration layer used for distributed inference deployments.

**LoRA & Model Adapter Lifecycle Management**

Model adapter and LoRA workflows are improved for reliability and runtime control.

**Dynamic LoRA Load/Unload for SGLang**: Support runtime loading and unloading of LoRA adapters. ([#1853](https://github.com/vllm-project/aibrix/pull/1853))**Artifact Preparation Improvements**: Delegate artifact preparation to LoRA downloader components. ([#1898](https://github.com/vllm-project/aibrix/pull/1898))**Improved Adapter Failure Handling**: Transition LoRA resources to`Failed`

state when pods are not recoverable. ([#1884](https://github.com/vllm-project/aibrix/pull/1884))

These updates improve multi-adapter inference reliability in production.

**KVCache Framework Improvements**

The AIBrix KVCache framework continues to evolve with new optimizations.

**Block-First KVCache Layout**: Introduce block-first KVCache layout support. ([#1947](https://github.com/vllm-project/aibrix/pull/1947))**CUDA Kernel Improvements**: Add padding token support in KVCache CUDA kernels. ([#1958](https://github.com/vllm-project/aibrix/pull/1958))**New KV Connector for PD Reuse**: Add`aibrix_pd_reuse_connector`

to support combined PD reuse workflows. ([#1852](https://github.com/vllm-project/aibrix/pull/1852))

These improvements further optimize memory efficiency and performance of KVCache-based inference.

## 📊 Observability & Metrics

Major improvements were introduced to monitoring and observability across gateway and runtime layers.

**Gateway Metrics Support**: Introduce metrics collection directly from the gateway layer. ([#1907](https://github.com/vllm-project/aibrix/pull/1907),[#1922](https://github.com/vllm-project/aibrix/pull/1922))**Inference Request Metrics**: Add granular metrics tracking inference request behavior. ([#1926](https://github.com/vllm-project/aibrix/pull/1926))**Prometheus Integration Enhancements**:**Routing & Cache Metrics Updates**: Improve routing and cache metrics definitions and naming. ([#1968](https://github.com/vllm-project/aibrix/pull/1968))

A new **SGLang gateway metrics dashboard** was also added. ([#1959](https://github.com/vllm-project/aibrix/pull/1959))

## 📦 Installation, Deployment & Platform Support

Deployment workflows and platform support continue to improve.

**Docker Compose Installation**: Simplify standalone installation with improved docker-compose configuration. ([#1871](https://github.com/vllm-project/aibrix/pull/1871),[#1878](https://github.com/vllm-project/aibrix/pull/1878))**Gateway Plugin Standalone Mode**: Allow gateway plugin to run without Kubernetes. ([#1873](https://github.com/vllm-project/aibrix/pull/1873))**Envoy Sidecar Support**: Add support for running Envoy as a sidecar alongside the gateway-plugin. ([#1931](https://github.com/vllm-project/aibrix/pull/1931))**Flexible Docker Builds**: Improve Docker builds to support multiple platforms and architectures. ([#1942](https://github.com/vllm-project/aibrix/pull/1942))**Custom Registry Support**: Support registry addresses containing port values. ([#1919](https://github.com/vllm-project/aibrix/pull/1919))

Additional samples were also added for **Ascend hardware deployments**. ([#1935](https://github.com/vllm-project/aibrix/pull/1935))

## 📚 Documentation Improvements

A large set of documentation updates and guides were added.

Highlights include:

- Envoy AI Gateway integration guide (
[#1733](https://github.com/vllm-project/aibrix/pull/1733)) - Session affinity routing documentation (
[#1823](https://github.com/vllm-project/aibrix/pull/1823)) - Prefill/Decode disaggregation examples (
[#1811](https://github.com/vllm-project/aibrix/pull/1811)) - LoRA adapter documentation updates (
[#1813](https://github.com/vllm-project/aibrix/pull/1813)) - AIBrix container images for vLLM/SGLang (
[#1792](https://github.com/vllm-project/aibrix/pull/1792)) - AWS Trainium2 / Neuron support documentation (
[#1894](https://github.com/vllm-project/aibrix/pull/1894)) - Prometheus gateway configuration documentation (
[#1954](https://github.com/vllm-project/aibrix/pull/1954))

Numerous README and documentation improvements were also included.

## 🐞 Critical Bug Fixes

A number of stability and correctness fixes were implemented across routing, metrics, and runtime systems.

Key fixes include:

- Resolve RDMA issues affecting SGLang and vLLM in P/D disaggregation setups. (
[#1783](https://github.com/vllm-project/aibrix/pull/1783)) - Fix Redis authentication handling in Helm charts. (
[#1806](https://github.com/vllm-project/aibrix/pull/1806)) - Prevent divide-by-zero errors in APA autoscaling logic. (
[#1879](https://github.com/vllm-project/aibrix/pull/1879)) - Fix envoy extension policy paths and gateway service configuration issues. (
[#1921](https://github.com/vllm-project/aibrix/pull/1921),[#1932](https://github.com/vllm-project/aibrix/pull/1932)) - Resolve inconsistent label cardinality panic when emitting metrics. (
[#1977](https://github.com/vllm-project/aibrix/pull/1977)) - Fix CGO build failures caused by mismatched builder/runtime environments. (
[#1925](https://github.com/vllm-project/aibrix/pull/1925))

Additional fixes improve controller stability, metrics correctness, and routing behavior.

## 🧪 Testing & Developer Experience

Testing coverage and development workflows were expanded.

- Add E2E tests for Batch API using OpenAI client. (
[#1743](https://github.com/vllm-project/aibrix/pull/1743)) - Improve client metrics testing. (
[#1727](https://github.com/vllm-project/aibrix/pull/1727)) - Add fake-client based PodGroup unit tests. (
[#1790](https://github.com/vllm-project/aibrix/pull/1790)) - Improve benchmark script dependencies and testing utilities. (
[#1909](https://github.com/vllm-project/aibrix/pull/1909))

## What's Changed

- [Misc] Added test for client metrics by
[@nurali-techie](https://github.com/nurali-techie)in[#1727](https://github.com/vllm-project/aibrix/pull/1727) - [Docs] v0.5.0 KVCache docs and samples by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1745](https://github.com/vllm-project/aibrix/pull/1745) - [Bug]: fix infinistore(rdma) exists/delete to avoid TCP interleaving by
[@sherlockkenan](https://github.com/sherlockkenan)in[#1748](https://github.com/vllm-project/aibrix/pull/1748) - [Chore] fix links in bug report template by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1750](https://github.com/vllm-project/aibrix/pull/1750) - [Test] Add E2E test for batch API using open AI client. by
[@zhangjyr](https://github.com/zhangjyr)in[#1743](https://github.com/vllm-project/aibrix/pull/1743) - fix(api): correct API comment of RayClusterReplicaSetStatus.Replicas by
[@zhixian82](https://github.com/zhixian82)in[#1754](https://github.com/vllm-project/aibrix/pull/1754) - docs(router): clarify parameter and return descriptions by
[@googs1025](https://github.com/googs1025)in[#1755](https://github.com/vllm-project/aibrix/pull/1755) - [Docs]: feature: envoy ai gateway integration by
[@googs1025](https://github.com/googs1025)in[#1733](https://github.com/vllm-project/aibrix/pull/1733) - [feat] Support per-role revision tracking in Stormservice by
[@Jeffwan](https://github.com/Jeffwan)in[#1731](https://github.com/vllm-project/aibrix/pull/1731) - [Docs] added v0.5.0 entry in README by
[@nurali-techie](https://github.com/nurali-techie)in[#1757](https://github.com/vllm-project/aibrix/pull/1757) - [Docs] seperate section for talks in README by
[@nurali-techie](https://github.com/nurali-techie)in[#1758](https://github.com/vllm-project/aibrix/pull/1758) - [Misc] upgrade sidecar webhook image from v0.4.0 to v0.5.0 by
[@nurali-techie](https://github.com/nurali-techie)in[#1762](https://github.com/vllm-project/aibrix/pull/1762) - [Feat] Implement role status aggregation for StormService by
[@Jeffwan](https://github.com/Jeffwan)in[#1761](https://github.com/vllm-project/aibrix/pull/1761) - [fix] Consider revision in role status aggregation by
[@Jeffwan](https://github.com/Jeffwan)in[#1767](https://github.com/vllm-project/aibrix/pull/1767) - [feat] Add affinity values for chart by
[@my-git9](https://github.com/my-git9)in[#1763](https://github.com/vllm-project/aibrix/pull/1763) - [Misc] fix sequence for dev-install-in-kind make target by
[@nurali-techie](https://github.com/nurali-techie)in htt...

[Read more](https://github.com/vllm-project/aibrix/releases/tag/v0.6.0)

## v0.5.0

## 🚀 New Features Highlights

**Batch API & Multimodal and other OpenAI compatible API Surface**

**Batch API Support**: Add OpenAI-style Batch API with simple LLM workers, Envoy/Gateway integration, JSONL & File List support, job pool sizing, and robust validation to safely offload large asynchronous workloads. ([#1298](https://github.com/vllm-project/aibrix/pull/1298),[#1617](https://github.com/vllm-project/aibrix/pull/1617),[#1671](https://github.com/vllm-project/aibrix/pull/1671),[#1698](https://github.com/vllm-project/aibrix/pull/1698),[#1700](https://github.com/vllm-project/aibrix/pull/1700),[#1701](https://github.com/vllm-project/aibrix/pull/1701))**Embeddings API and Moltimodal API**: Introduce OpenAI-compatible embeddings endpoint so online inference, search, and RAG traffic can share the same AIBrix control plane and routing. ([#1570](https://github.com/vllm-project/aibrix/pull/1570)) Support multimodality deployments and for image/video generation for other engines. ([#1678](https://github.com/vllm-project/aibrix/pull/1678),[#1679](https://github.com/vllm-project/aibrix/pull/1679),[#1603](https://github.com/vllm-project/aibrix/pull/1603),[#1584](https://github.com/vllm-project/aibrix/pull/1584))**Files API & Unified Storage**: Implement OpenAI Files API plus a pluggable storage layer (local, S3, TOS, Redis metadata) to standardize artifact and batch job management across backends. ([#1583](https://github.com/vllm-project/aibrix/pull/1583),[#1571](https://github.com/vllm-project/aibrix/pull/1571))

**AIBrix KVCache Offloading frameworks & Connectors:**

**High-Performance KVCache**: Adds GDR support, optimized collective communications, configurable max sequence length and batched tokens, multi-threading for higher concurrency, and block-hash based APIs plus external cache handles for flexible distributed deployments. ([#1411](https://github.com/vllm-project/aibrix/pull/1411),[#1446](https://github.com/vllm-project/aibrix/pull/1446),[#1453](https://github.com/vllm-project/aibrix/pull/1453),[#1451](https://github.com/vllm-project/aibrix/pull/1451),[#1627](https://github.com/vllm-project/aibrix/pull/1627),[#1628](https://github.com/vllm-project/aibrix/pull/1628),[#1545](https://github.com/vllm-project/aibrix/pull/1545),[#1531](https://github.com/vllm-project/aibrix/pull/1531),[#1542](https://github.com/vllm-project/aibrix/pull/1542))**Deep Engine Integrations**: Provide official AIBrix KVCache Dockerfiles and integration paths for vLLM and SGLang plus correctness fixes (head size, metrics, types) to make KV offloading a first-class option. ([#1641](https://github.com/vllm-project/aibrix/pull/1641),[#1696](https://github.com/vllm-project/aibrix/pull/1696),[#1705](https://github.com/vllm-project/aibrix/pull/1705),[#1473](https://github.com/vllm-project/aibrix/pull/1473),[#1450](https://github.com/vllm-project/aibrix/pull/1450),[#1689](https://github.com/vllm-project/aibrix/pull/1689))

**Production-Grade Prefill/Decode (P/D) Orchestration Support:**

**New StormService Primitives**: Add PodSet API, PodGroup support, FullRecreate strategy, role upgrade sequences, roleStatuses, and richer RoleSet/PodSet fields to model multi-pod workers, shard groups, and safer rollout/rollback for complex topologies. ([#1475](https://github.com/vllm-project/aibrix/pull/1475),[#1506](https://github.com/vllm-project/aibrix/pull/1506),[#1511](https://github.com/vllm-project/aibrix/pull/1511),[#1432](https://github.com/vllm-project/aibrix/pull/1432),[#1599](https://github.com/vllm-project/aibrix/pull/1599),[#1560](https://github.com/vllm-project/aibrix/pull/1560))**P/D-Aware & Topology-Aware Routing**: Prefer P/D workers in the same RoleSet in replication mode, score candidates by locality/load, and harden PD routing behavior for Nixl-based setups. ([#1409](https://github.com/vllm-project/aibrix/pull/1409),[#1634](https://github.com/vllm-project/aibrix/pull/1634),[#1429](https://github.com/vllm-project/aibrix/pull/1429),[#1601](https://github.com/vllm-project/aibrix/pull/1601),[#1703](https://github.com/vllm-project/aibrix/pull/1703),[#1693](https://github.com/vllm-project/aibrix/pull/1693))**Role-Level Autoscaling for StormService**: Introduced the "subTargetSelector" field in the PodAutoscaler API, allowing independent autoscaling of specific roles (e.g., prefill, decode) within a StormService resource, particularly in pooled mode. ([#1625](https://github.com/vllm-project/aibrix/pull/1625))

## 📊 Feature Enhancements

**Unified Runtime & Metadata**: Migrate metadata server from golang to Python for a simpler, lighter control path. Add liveness/readiness probes and shrink runtime image sizes. Improve downloader reliability and recursive object-store fetch support. ([#1391](https://github.com/vllm-project/aibrix/pull/1391),[#1639](https://github.com/vllm-project/aibrix/pull/1639),[#1548](https://github.com/vllm-project/aibrix/pull/1548),[#1702](https://github.com/vllm-project/aibrix/pull/1702),[#1571](https://github.com/vllm-project/aibrix/pull/1571))**LoRA & Model Adapter Reliability**: Support adapter scaling to desired replicas, refactor replica management, add wrappers, and enable LoRA downloading via the runtime to stabilize multi-adapter hosting.

([#1132](https://github.com/vllm-project/aibrix/pull/1132),[#1472](https://github.com/vllm-project/aibrix/pull/1472),[#1670](https://github.com/vllm-project/aibrix/pull/1670),[#1680](https://github.com/vllm-project/aibrix/pull/1680),[#1537](https://github.com/vllm-project/aibrix/pull/1537),[#1541](https://github.com/vllm-project/aibrix/pull/1541))**Autoscaling**: Unify and harden metrics fetching by adding retryable RestMetricsFetcher, shared client/aggregator and fixing race-condition for configuration updates ([#1466](https://github.com/vllm-project/aibrix/pull/1466),[#1487](https://github.com/vllm-project/aibrix/pull/1487),[#1620](https://github.com/vllm-project/aibrix/pull/1620),[#1621](https://github.com/vllm-project/aibrix/pull/1621),[#1709](https://github.com/vllm-project/aibrix/pull/1709)), Tune KPA defaults, support metric label selectors, and ensure PodAutoscaler emits events only when replica counts actually change. ([#1624](https://github.com/vllm-project/aibrix/pull/1624),[#1629](https://github.com/vllm-project/aibrix/pull/1629),[#1630](https://github.com/vllm-project/aibrix/pull/1630)) scaling history decision has been supported in the status spec ([#1618](https://github.com/vllm-project/aibrix/pull/1618))**AIBrixRuntime Injection**: Deployment & StormService webhooks and wrapper libraries to auto-inject the runtime sidecar, standardizing metrics, downloads, and admin controls across engines.

([#1403](https://github.com/vllm-project/aibrix/pull/1403),[#1457](https://github.com/vllm-project/aibrix/pull/1457),[#1543](https://github.com/vllm-project/aibrix/pull/1543),[#1681](https://github.com/vllm-project/aibrix/pull/1681),[#1561](https://github.com/vllm-project/aibrix/pull/1561))

## 📦 Installation & Tooling & CI

**Helm & Installation**: Strengthen the AIBrix Helm chart as the recommended deployment path by adding dedicated chart CI and fixes ([#1370](https://github.com/vllm-project/aibrix/pull/1370),[#1424](https://github.com/vllm-project/aibrix/pull/1424)), enriching Chart.yaml metadata ([#1414](https://github.com/vllm-project/aibrix/pull/1414)), introducing values.schema.json for input validation ([#1415](https://github.com/vllm-project/aibrix/pull/1415)), supporting imagePullSecrets configuration ([#1522](https://github.com/vllm-project/aibrix/pull/1522)), and resolving duplicate label issues for Flux Helm Controller compatibility ([#1615](https://github.com/vllm-project/aibrix/pull/1615)). Made KubeRay optional for AIBrix installations if you do not use RayclusterFleet API([#1724](https://github.com/vllm-project/aibrix/pull/1724))

## 🐞 Critical Bug Fixes

- Fixes StormService headless Service ownership and DNS behavior by setting proper ownerReferences and PublishNotReadyAddresses. (
[#1441](https://github.com/vllm-project/aibrix/pull/1441),[#1442](https://github.com/vllm-project/aibrix/pull/1442)) - Fixes incorrect naming for AIBRIX_MODEL_GPU_PROFILE_CACHING_FLAG to ensure configuration consistency. (
[#1427](https://github.com/vllm-project/aibrix/pull/1427)) - Fixes KVCache stability issues by preventing panic when watcher or metadata are not set in kvcache.spec. (
[#1526](https://github.com/vllm-project/aibrix/pull/1526)) - Fixes PodAutoscaler and metrics correctness by emitting events only on replica changes, aggregating resources across all containers, handling optional MetricSource fields, validating multiple PodAutoscalers targeting the same workload, and ensuring PodSet autoscaler collects metrics from rank0. (
[#1630](https://github.com/vllm-project/aibrix/pull/1630),[#1643](https://github.com/vllm-project/aibrix/pull/1643),[#1648](https://github.com/vllm-project/aibrix/pull/1648),[#1662](https://github.com/vllm-project/aibrix/pull/1662),[#1704](https://github.com/vllm-project/aibrix/pull/1704))

## New Contributors

[@JonathonShea](https://github.com/JonathonShea)made their first contribution in[#1427](https://github.com/vllm-project/aibrix/pull/1427)[@bigerous](https://github.com/bigerous)made their first contribution in[#1442](https://github.com/vllm-project/aibrix/pull/1442)[@jiangxiaobin96](https://github.com/jiangxiaobin96)made their first contribution in[#1431](https://github.com/vllm-project/aibrix/pull/1431)[@mayooot](https://github.com/mayooot)made their first contribution in[#1496](https://github.com/vllm-project/aibrix/pull/1496)[@zyfy29](https://github.com/zyfy29)made their first contribution in[#1505](https://github.com/vllm-project/aibrix/pull/1505)[@zhengkezhou1](https://github.com/zhengkezhou1)made their first contribution in[#1502](https://github.com/vllm-project/aibrix/pull/1502)[@tianzhiqiang3](https://github.com/tianzhiqiang3)made their first contribution in[#1566](https://github.com/vllm-project/aibrix/pull/1566)[@atakli](https://github.com/atakli)made their first contribution in[#1574](https://github.com/vllm-project/aibrix/pull/1574)[@jwjwjw3](https://github.com/jwjwjw3)made their first contribution in[#1573](https://github.com/vllm-project/aibrix/pull/1573)[@lx1036](https://github.com/lx1036)made their first contribution in[#1586](https://github.com/vllm-project/aibrix/pull/1586)[@chethanuk](https://github.com/chethanuk)made their first contribution in[#1558](https://github.com/vllm-project/aibrix/pull/1558)[@baozixiaoxixi](https://github.com/baozixiaoxixi)made their first contribution in[#1608](https://github.com/vllm-project/aibrix/pull/1608)[@TylerGillson](https://github.com/TylerGillson)made their first contribution in[#1615](https://github.com/vllm-project/aibrix/pull/1615)[@omrishiv](https://github.com/omrishiv)made their first contribution in[#1626](https://github.com/vllm-project/aibrix/pull/1626)[@lex1ng](https://github.com/lex1ng)made their first contribution in[#1658](https://github.com/vllm-project/aibrix/pull/1658)[@ChenTaoyu-SJTU](https://github.com/ChenTaoyu-SJTU)made their first contribution in[#1672](https://github.com/vllm-project/aibrix/pull/1672)[@zhenyu-02](https://github.com/zhenyu-02)made their first contribution in[#1682](https://github.com/vllm-project/aibrix/pull/1682)[@yapple](https://github.com/yapple)made their first contribution in[#1705](https://github.com/vllm-project/aibrix/pull/1705)[@xvoron](https://github.com/xvoron)made their first contribution in[#1708](https://github.com/vllm-project/aibrix/pull/1708)- @freedown19 made their first contribution in
[#1716](https://github.com/vllm-project/aibrix/pull/1716) [@Leafykn](https://github.com/Leafykn)made their first contribution in[#1718](https://github.com/vllm-project/aibrix/pull/1718)

## What's Changed

**Full Changelog**: `v0.4.0...v0.5.0`

- Update installation guidance for v0.4.0 by
[@Jeffwan](https://github.com/Jeffwan)in[#1406](https://github.com/vllm-project/aibrix/pull/1406) - [Bug] fix webhook config output when using make manifests by
[@googs1025](https://github.com/googs1025)in[#1412](https://github.com/vllm-project/aibrix/pull/1412) - Feat: Add AIBrix Helm chart CI by
[@omerap12](https://github.com/omerap12)in[#1370](https://github.com/vllm-project/aibrix/pull/1370) - [Feature] KVCache: support GDR by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1411](https://github.com/vllm-project/aibrix/pull/1411) - Select PD workers in same roleset by
[@varungup90](https://github.com/varungup90)in[#1409](https://github.com/vllm-project/aibrix/pull/1409) - [Bug] fix chart-ci by
[@omerap12](https://github.com/omerap12)in[#1424](https://github.com/vllm-project/aibrix/pull/1424) - [Misc]: Enhance Chart.yaml metadata with comprehensive information by
[@Jeffwan](https://github.com/Jeffwan)in[#1414](https://github.com/vllm-project/aibrix/pull/1414) - [feat]: Add values.schema.json for Helm chart input validation by
[@Jeffwan](https://github.com/Jeffwan)in[#1415](https://github.com/vllm-project/aibrix/pull/1415) - [Fix] Fix vLLM NIXL-based P/D samples by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1425](https://github.com/vllm-project/aibrix/pull/1425) - [Bug] Corrected naming convention for AIBRIX_MODEL_GPU_PROFILE_CACHING_FLAG by
[@JonathonShea](https://github.com/JonathonShea)in[#1427](https://github.com/vllm-project/aibrix/pull/1427) - Feat: add liveness & readiness probes to metadata service by
[@omerap12](https://github.com/omerap12)in[#1391](https://github.com/vllm-project/aibrix/pull/1391) - [Fix] Disable GGA in NIXL samples by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1436](https://github.com/vllm-project/aibrix/pull/1436) - doc: correct release date in README.md by
[@nurali-techie](https://github.com/nurali-techie)in[#1435](https://github.com/vllm-project/aibrix/pull/1435) - [Misc]: Remove v0.4.0 test files replaced by consolidated base templates by
[@Jeffwan](https://github.com/Jeffwan)in[#1428](https://github.com/vllm-project/aibrix/pull/1428) - feature: add stormservice webhook for inject aibrix runtime by
[@googs1025](https://github.com/googs1025)in[#1403](https://github.com/vllm-project/aibrix/pull/1403) - [Chore] KVCache: downgrade to cuda 12.1 by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1444](https://github.com/vllm-project/aibrix/pull/1444) - [misc] Update vLLM PD disaggregation image by
[@happyandslow](https://github.com/happyandslow)in[#1445](https://github.com/vllm-project/aibrix/pull/1445) - [Misc] remove unuseless event by
[@googs1025](https://github.com/googs1025)in[#1447](https://github.com/vllm-project/aibrix/pull/1447) - [Feature] KVCache: support max seq len by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1446](https://github.com/vllm-project/aibrix/pull/1446) - [Bug] stormservice's headless service not set ownerRef by
[@bigerous](https://github.com/bigerous)in[#1442](https://github.com/vllm-project/aibrix/pull/1442) - [Bug] stormservice's headless service need set PublishNotReadyAddresses by
[@bigerous](https://github.com/bigerous)in[#1441](https://github.com/vllm-project/aibrix/pull/1441) - [Bug] KVCache: fix metrics by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1450](https://github.com/vllm-project/aibrix/pull/1450) - [Improvement] KVCache: optimize coll communication by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1451](https://github.com/vllm-project/aibrix/pull/1451) - Fix P/D disaggregation router to follow Nixl kv_transfer_params by
[@Jeffwan](https://github.com/Jeffwan)in[#1429](https://github.com/vllm-project/aibrix/pull/1429) - [Misc] fix regression test manifests by
[@Jeffwan](https://github.com/Jeffwan)in[#1456](https://github.com/vllm-project/aibrix/pull/1456) - [Bug] KVCache: fix max seq len support by
[@DwyaneShi](https://github.com/DwyaneShi)in[https://githu](https://githu)...

[Read more](https://github.com/vllm-project/aibrix/releases/tag/v0.5.0)

## v0.4.1

Automatically generated release for tag v0.4.1.

## What's Changed

- [Misc] KVCache bugfixes cherry-picks for v0.4.1 by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1458](https://github.com/vllm-project/aibrix/pull/1458) - [Cherry-Pick] fix: align envoy pod template labels with controller selector by
[@omerap12](https://github.com/omerap12)in[#1462](https://github.com/vllm-project/aibrix/pull/1462) - Cherry picks
[#1409](https://github.com/vllm-project/aibrix/pull/1409)[#1412](https://github.com/vllm-project/aibrix/pull/1412)[#1425](https://github.com/vllm-project/aibrix/pull/1425)[#1436](https://github.com/vllm-project/aibrix/pull/1436)[#1429](https://github.com/vllm-project/aibrix/pull/1429)[#1427](https://github.com/vllm-project/aibrix/pull/1427)[#1442](https://github.com/vllm-project/aibrix/pull/1442)[#1441](https://github.com/vllm-project/aibrix/pull/1441)to release-0.4 branch by[@Jeffwan](https://github.com/Jeffwan)in[#1468](https://github.com/vllm-project/aibrix/pull/1468) - KVCache integration cherry picks by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1474](https://github.com/vllm-project/aibrix/pull/1474) - Cut release v0.4.1 against release-0.4 by
[@Jeffwan](https://github.com/Jeffwan)in[#1478](https://github.com/vllm-project/aibrix/pull/1478)

**Full Changelog**: `v0.4.0...v0.4.1`

## v0.4.0

## 🚀 New Features Highlights

**Prefill/Decode (P/D) Disaggregation Support**: Introduces StormService and RoleSet CRDs to enable fine-grained orchestration of P/D roles, along with routing to unlock disaggregated inference at scale. ([#1209](https://github.com/vllm-project/aibrix/pull/1209),[#1226](https://github.com/vllm-project/aibrix/pull/1226),[#1229](https://github.com/vllm-project/aibrix/pull/1229),[#1256](https://github.com/vllm-project/aibrix/pull/1256),[#1258](https://github.com/vllm-project/aibrix/pull/1258),[#1259](https://github.com/vllm-project/aibrix/pull/1259),[#1268](https://github.com/vllm-project/aibrix/pull/1268),[#1280](https://github.com/vllm-project/aibrix/pull/1280),[#1309](https://github.com/vllm-project/aibrix/pull/1309),[#1311](https://github.com/vllm-project/aibrix/pull/1311),[#1354](https://github.com/vllm-project/aibrix/pull/1354),[#1355](https://github.com/vllm-project/aibrix/pull/1355),[#1377](https://github.com/vllm-project/aibrix/pull/1377),[#1399](https://github.com/vllm-project/aibrix/pull/1399),[#1402](https://github.com/vllm-project/aibrix/pull/1402))**KVCache V1 Connector Optimizations**: Delivers a major refactor with v1 Connector integration, CUDA kernel separation from vllm downstream, compact memory layout, connector integration for PrisDB and InfiniStore(/w TCP), tunable block sizes, RDMA auto-detection support and few performance optimizations to boost throughput and deployment density. ([#1174](https://github.com/vllm-project/aibrix/pull/1174),[#1194](https://github.com/vllm-project/aibrix/pull/1194),[#1247](https://github.com/vllm-project/aibrix/pull/1247),[#1274](https://github.com/vllm-project/aibrix/pull/1274),[#1276](https://github.com/vllm-project/aibrix/pull/1276),[#1278](https://github.com/vllm-project/aibrix/pull/1278),[#1286](https://github.com/vllm-project/aibrix/pull/1286),[#1287](https://github.com/vllm-project/aibrix/pull/1287),[#1288](https://github.com/vllm-project/aibrix/pull/1288),[#1295](https://github.com/vllm-project/aibrix/pull/1295),[#1303](https://github.com/vllm-project/aibrix/pull/1303),[#1312](https://github.com/vllm-project/aibrix/pull/1312),[#1318](https://github.com/vllm-project/aibrix/pull/1318))**KV Event Synchronization**: Introduces remote tokenizer support to ensure tokenization consistency between client and server and implements a comprehensive KV cache event synchronization system that shares KV cache state between vLLM instances and aibrix gateway for improved prefix caching efficiency ([#1307](https://github.com/vllm-project/aibrix/pull/1307),[#1328](https://github.com/vllm-project/aibrix/pull/1328),[#1349](https://github.com/vllm-project/aibrix/pull/1349),[#1362](https://github.com/vllm-project/aibrix/pull/1362))**Multi-Engine Deployment Support**: Adds unified regression test suites and Helm values to support heterogeneous backends including vLLM, SGLang, and Dynamo, enabling flexible model deployment across engines. ([#1293](https://github.com/vllm-project/aibrix/pull/1293),[#1319](https://github.com/vllm-project/aibrix/pull/1319),[#1322](https://github.com/vllm-project/aibrix/pull/1322),[#1341](https://github.com/vllm-project/aibrix/pull/1341),[#1346](https://github.com/vllm-project/aibrix/pull/1346))

## 📊 Feature Enhancements

### 🌐 Gateway Enhancements

- SLO-aware router with profile support (
[#1192](https://github.com/vllm-project/aibrix/pull/1192),[#1305](https://github.com/vllm-project/aibrix/pull/1305),[#1368](https://github.com/vllm-project/aibrix/pull/1368)) - Adds custom inference port and metrics port support (
[#1140](https://github.com/vllm-project/aibrix/pull/1140),[#1313](https://github.com/vllm-project/aibrix/pull/1313)). - Make httproute timeout configurable and checks missing httproute before request start(
[#1212](https://github.com/vllm-project/aibrix/pull/1212),[#1344](https://github.com/vllm-project/aibrix/pull/1344)). - Adds metrics server support and adds ready-to-use sample dashboard (
[#1211](https://github.com/vllm-project/aibrix/pull/1211)).

### ☁️ Control Plane Improvements

- Enhance the CRD existence check and improve webhook support (
[#1170](https://github.com/vllm-project/aibrix/pull/1170),[#1187](https://github.com/vllm-project/aibrix/pull/1187)). - Ensure cache sync before starting controller reconcile and resync object on component restarts (
[#1146](https://github.com/vllm-project/aibrix/pull/1146),[#1219](https://github.com/vllm-project/aibrix/pull/1219)). - Use worker pool management for periodic metrics update (
[#1096](https://github.com/vllm-project/aibrix/pull/1096))

### 📦 Installation & Tooling & CI

- Adds Helm Chart support with helm standard labels and probes (
[#1323](https://github.com/vllm-project/aibrix/pull/1323),[#1331](https://github.com/vllm-project/aibrix/pull/1331),[#1343](https://github.com/vllm-project/aibrix/pull/1343)). - Supports multi-arch (AMD, ARM) Docker builds and refactors release pipelines (
[#1315](https://github.com/vllm-project/aibrix/pull/1315),[#1317](https://github.com/vllm-project/aibrix/pull/1317),[#1324](https://github.com/vllm-project/aibrix/pull/1324),[#1325](https://github.com/vllm-project/aibrix/pull/1325)). - Improves kind development workflow and supports port-forward via Makefile, support override IMAGE_TAG and disable docker push workflow in forked repo(
[#1210](https://github.com/vllm-project/aibrix/pull/1210),[#1274](https://github.com/vllm-project/aibrix/pull/1274),[#1301](https://github.com/vllm-project/aibrix/pull/1301)).

## 🐞 Bug Fixes

- Fixes incorrect request count, out-of-index errors, and race conditions in AIBrix router(
[#1246](https://github.com/vllm-project/aibrix/pull/1246),[#1262](https://github.com/vllm-project/aibrix/pull/1262),[#1305](https://github.com/vllm-project/aibrix/pull/1305)). - Fix Prefix cache chained hashing issue and optimize to O(N) via block-hash. (
[#1218](https://github.com/vllm-project/aibrix/pull/1218),[#1262](https://github.com/vllm-project/aibrix/pull/1262)) - Fixes completion body parsing and complex content bugs (
[#1145](https://github.com/vllm-project/aibrix/pull/1145),[#1160](https://github.com/vllm-project/aibrix/pull/1160)). - Fixes legacy autoscaling annotation misconfigurations (
[#1173](https://github.com/vllm-project/aibrix/pull/1173)). - Fixes image replacement issues in Kustomize (
[#1165](https://github.com/vllm-project/aibrix/pull/1165)). - Fixes e2e test flakiness with wait.PollUntilContextTimeout (
[#1214](https://github.com/vllm-project/aibrix/pull/1214)). - Add read lock for h.histogram (
[#1147](https://github.com/vllm-project/aibrix/pull/1147))

## 📚 Documentation Updates

- Adds v0.4.0 new features documentation including P/D disaggregation, multi-engine, KVCache Offloading and SLO routing documentation (
[#1279](https://github.com/vllm-project/aibrix/pull/1279),[#1285](https://github.com/vllm-project/aibrix/pull/1285),[#1341](https://github.com/vllm-project/aibrix/pull/1341),[#1356](https://github.com/vllm-project/aibrix/pull/1356),[#1368](https://github.com/vllm-project/aibrix/pull/1368)). - Fixes broken links, typos, and dashboard URLs (
[#1190](https://github.com/vllm-project/aibrix/pull/1190),[#1193](https://github.com/vllm-project/aibrix/pull/1193),[#1237](https://github.com/vllm-project/aibrix/pull/1237),[#1270](https://github.com/vllm-project/aibrix/pull/1270),[#1271](https://github.com/vllm-project/aibrix/pull/1271)). - Refactors component design docs into structured architecture folders (
[#1224](https://github.com/vllm-project/aibrix/pull/1224),[#1236](https://github.com/vllm-project/aibrix/pull/1236),[#1250](https://github.com/vllm-project/aibrix/pull/1250)). - Refactors local development and quickstart guides (
[#1193](https://github.com/vllm-project/aibrix/pull/1193),[#1339](https://github.com/vllm-project/aibrix/pull/1339),[#1172](https://github.com/vllm-project/aibrix/pull/1172)). - Improve installation commands and add more deployment examples (
[#1128](https://github.com/vllm-project/aibrix/pull/1128),[#1136](https://github.com/vllm-project/aibrix/pull/1136),[#1230](https://github.com/vllm-project/aibrix/pull/1230),[#1379](https://github.com/vllm-project/aibrix/pull/1379),[#1395](https://github.com/vllm-project/aibrix/pull/1395))

## New Contributors

[@dittops](https://github.com/dittops)made their first contribution in[#1128](https://github.com/vllm-project/aibrix/pull/1128)[@yyzxw](https://github.com/yyzxw)made their first contribution in[#1139](https://github.com/vllm-project/aibrix/pull/1139)[@firebook](https://github.com/firebook)made their first contribution in[#1145](https://github.com/vllm-project/aibrix/pull/1145)[@windsonsea](https://github.com/windsonsea)made their first contribution in[#1150](https://github.com/vllm-project/aibrix/pull/1150)[@emmanuel-ferdman](https://github.com/emmanuel-ferdman)made their first contribution in[#1161](https://github.com/vllm-project/aibrix/pull/1161)[@MondayCha](https://github.com/MondayCha)made their first contribution in[#1165](https://github.com/vllm-project/aibrix/pull/1165)[@learner0810](https://github.com/learner0810)made their first contribution in[#1170](https://github.com/vllm-project/aibrix/pull/1170)[@jiahuipaung](https://github.com/jiahuipaung)made their first contribution in[#1172](https://github.com/vllm-project/aibrix/pull/1172)[@didier-durand](https://github.com/didier-durand)made their first contribution in[#1190](https://github.com/vllm-project/aibrix/pull/1190)[@gcalmettes](https://github.com/gcalmettes)made their first contribution in[#1193](https://github.com/vllm-project/aibrix/pull/1193)[@justadogistaken](https://github.com/justadogistaken)made their first contribution in[#1218](https://github.com/vllm-project/aibrix/pull/1218)[@ModiCodeCraftsman](https://github.com/ModiCodeCraftsman)made their first contribution in[#1217](https://github.com/vllm-project/aibrix/pull/1217)[@haitwang-cloud](https://github.com/haitwang-cloud)made their first contribution in[#1230](https://github.com/vllm-project/aibrix/pull/1230)[@ae86zhizhi](https://github.com/ae86zhizhi)made their first contribution in[#1262](https://github.com/vllm-project/aibrix/pull/1262)[@nicole-lihui](https://github.com/nicole-lihui)made their first contribution in[#1270](https://github.com/vllm-project/aibrix/pull/1270)[@omerap12](https://github.com/omerap12)made their first contribution in[#1282](https://github.com/vllm-project/aibrix/pull/1282)- @li-rongzhi made their first contribution in
[#1285](https://github.com/vllm-project/aibrix/pull/1285) [@rudeigerc](https://github.com/rudeigerc)made their first contribution in[#1301](https://github.com/vllm-project/aibrix/pull/1301)[@Yaegaki1Erika](https://github.com/Yaegaki1Erika)made their first contribution in[#1313](https://github.com/vllm-project/aibrix/pull/1313)[@elizabetht](https://github.com/elizabetht)made their first contribution in[#1339](https://github.com/vllm-project/aibrix/pull/1339)[@autopear](https://github.com/autopear)made their first contribution in[#1362](https://github.com/vllm-project/aibrix/pull/1362)[@Epsilon314](https://github.com/Epsilon314)made their first contribution in[#1402](https://github.com/vllm-project/aibrix/pull/1402)

## What's Changed

**Full Changelog**: `v0.3.0...v0.4.0`

- [Docs] Update typo for installation command by
[@dittops](https://github.com/dittops)in[#1128](https://github.com/vllm-project/aibrix/pull/1128) - [Docs] fix: update example yaml ai runtime tag to v0.3.0 by
[@yyzxw](https://github.com/yyzxw)in[#1139](https://github.com/vllm-project/aibrix/pull/1139) - [Bug]: fix: README.md docs install error by
[@googs1025](https://github.com/googs1025)in[#1136](https://github.com/vllm-project/aibrix/pull/1136) - [Bug] fix: error when parse stop param in completion body by
[@firebook](https://github.com/firebook)in[#1145](https://github.com/vllm-project/aibrix/pull/1145) - Resync model adapters on gateway restart by
[@dittops](https://github.com/dittops)in[#1146](https://github.com/vllm-project/aibrix/pull/1146) - [Docs]add management user link by
[@yyzxw](https://github.com/yyzxw)in[#1141](https://github.com/vllm-project/aibrix/pull/1141) - [Bug] Add read lock for h.histogram by
[@runzhen](https://github.com/runzhen)in[#1147](https://github.com/vllm-project/aibrix/pull/1147) - [Doc] Improve samples/volcano-engine/README.md by
[@windsonsea](https://github.com/windsonsea)in[#1150](https://github.com/vllm-project/aibrix/pull/1150) - feature: use worker pool management for periodic metrics update by
[@googs1025](https://github.com/googs1025)in[#1096](https://github.com/vllm-project/aibrix/pull/1096) - [Misc] [gpu_optimizer] add namespace info for log by
[@googs1025](https://github.com/googs1025)in[#1149](https://github.com/vllm-project/aibrix/pull/1149) - Add support for custom inference engine port by
[@varungup90](https://github.com/varungup90)in[#1140](https://github.com/vllm-project/aibrix/pull/1140) - Modernize logger interface by
[@emmanuel-ferdman](https://github.com/emmanuel-ferdman)in[#1161](https://github.com/vllm-project/aibrix/pull/1161) - Add unit test code coverage by
[@varungup90](https://github.com/varungup90)in[#1156](https://github.com/vllm-project/aibrix/pull/1156) - feat: simplfy router interface by
[@Xunzhuo](https://github.com/Xunzhuo)in[#1163](https://github.com/vllm-project/aibrix/pull/1163) - [Bug] Fix image replacements in Kustomize files to support installation by
[@MondayCha](https://github.com/MondayCha)in[#1165](https://github.com/vllm-project/aibrix/pull/1165) - [Bug]: fix(aibrix kvcache): ObjectPool by
[@googs1025](https://github.com/googs1025)in[#1162](https://github.com/vllm-project/aibrix/pull/1162) - [Bug]: Fix legacy misconfigurations of autoscaling annotations. by
[@zhangjyr](https://github.com/zhangjyr)in[#1173](https://github.com/vllm-project/aibrix/pull/1173) - Enhance the CRD existence check by
[@learner0810](https://github.com/learner0810)in[#1170](https://github.com/vllm-project/aibrix/pull/1170) - [Misc]: add unit test for aibrix metrics collector by
[@googs1025](https://github.com/googs1025)in[#1153](https://github.com/vllm-project/aibrix/pull/1153) - [Docs] Add vllm-cpu local deployment guide to Quickstart by
[@jiahuipaung](https://github.com/jiahuipaung)in[#1172](https://github.com/vllm-project/aibrix/pull/1172) - fix: gateway benchmark info by
[@Xunzhuo](https://github.com/Xunzhuo)in[#1180](https://github.com/vllm-project/aibrix/pull/1180) - [Bug] fix: error when parse complex content in completion body by
[@firebook](https://github.com/firebook)in[#1160](https://github.com/vllm-project/aibrix/pull/1160) - Add race condition check in unit-test CI and add test-coverage cmd in Makefile by
[@varungup90](https://github.com/varungup90)in[#1169](https://github.com/vllm-project/aibrix/pull/1169) - Supporting Mooncake Traces in Workload Generator by
[@happyandslow](https://github.com/happyandslow)in[#1182](https://github.com/vllm-project/aibrix/pull/1182) - Recover Client Implementation by
[@happyandslow](https://github.com/happyandslow)in[#1191](https://github.com/vllm-project/aibrix/pull/1191) - Docs: fixing various text issues by
[@didier-durand](https://github.com/didier-durand)in[#1190](https://github.com/vllm-project/aibrix/pull/1190) - [Docs] update development instructions to new make commands by
[@gcalmettes](https://github.com/gcalmettes)in[#1193](https://github.com/vllm-project/aibrix/pull/1193) - feat: make preble configurable and rename by
[@Xunzhuo](https://github.com/Xunzhuo)in[#1189](https://github.com/vllm-project/aibrix/pull/1189) - [Misc] Add deepseek-r1 tp8 pp2 example by
[@Jeffwan](https://github.com/Jeffwan)in[#1195](https://github.com/vllm-project/aibrix/pull/1195) - [Misc] Update the latest news in README.md by
[@Jeffwan](https://github.com/Jeffwan)in[#1196](https://github.com/vllm-project/aibrix/pull/1196) - [Feature] Add RDMA auto-detection for kvcache by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1194](https://github.com/vllm-project/aibrix/pull/1194) - [Tooling]: port-forward support, Makefile changes for easier dev workflow in kind by
[@Venkat2811](https://github.com/Venkat2811)in[#1210](https://github.com/vllm-project/aibrix/pull/1210) - Multiple fixes and adding workload merging tool by
[@happyandslow](https://github.com/happyandslow)in[#1213](https://github.com/vllm-project/aibrix/pull/1213) - Add configurable httproute timeout by
[@varungup90](https://github.com/varungup90)in[#1212](https://github.com/vllm-project/aibrix/pull/1212) - [Bug] fix(e2e flaky): replace for-loop with wait.PollUntilContextTimeout in validateAllPodsAreReady by
[@googs1025](https://github.com/googs1025)in[#1214](https://github.com/vllm-project/aibrix/pull/1214) - [Misc] chore: use constant var for gpu_busy_ti...

[Read more](https://github.com/vllm-project/aibrix/releases/tag/v0.4.0)

## v0.3.0

Automatically generated release for tag v0.3.0.

## 🚀 New Features Highlights

**AIBrix KVCache Offloading Framework**: Introduces a pluggable multi-tier KVCache architecture with support for DRAM and remote backends, enabling efficient offloading of KV states to reduce GPU memory pressure and increase deployment density. ([#1057](https://github.com/vllm-project/aibrix/pull/1057),[#1061](https://github.com/vllm-project/aibrix/pull/1061),[#1062](https://github.com/vllm-project/aibrix/pull/1062),[#1063](https://github.com/vllm-project/aibrix/pull/1063),[#1064](https://github.com/vllm-project/aibrix/pull/1064),[#1068](https://github.com/vllm-project/aibrix/pull/1068),[#1069](https://github.com/vllm-project/aibrix/pull/1069),[#1080](https://github.com/vllm-project/aibrix/pull/1080),[#1107](https://github.com/vllm-project/aibrix/pull/1107))**New KVCache orchestration API**: Refactors the orchestration layer to support distributed hashing based caching solutions. ([#971](https://github.com/vllm-project/aibrix/pull/971),[#984](https://github.com/vllm-project/aibrix/pull/984),[#985](https://github.com/vllm-project/aibrix/pull/985),[#1037](https://github.com/vllm-project/aibrix/pull/1037),[#1055](https://github.com/vllm-project/aibrix/pull/1055),[#1071](https://github.com/vllm-project/aibrix/pull/1071),[#1114](https://github.com/vllm-project/aibrix/pull/1114))**Prefix Cache and Load aware Routing**: Uses hash token-based prefix matching and load awareness to reduce latency by increasing prefix cache hit rate and routing efficiency ([#838](https://github.com/vllm-project/aibrix/pull/838),[#774](https://github.com/vllm-project/aibrix/pull/774),[#933](https://github.com/vllm-project/aibrix/pull/933),[#1067](https://github.com/vllm-project/aibrix/pull/1067))**Preble Routing (ICLR’25)**: An implementation of Preble, it balances KV cache reuse and GPU load by comparing prefix lengths and computing prompt-aware cost scores for optimal routing. ([#678](https://github.com/vllm-project/aibrix/pull/678),[#719](https://github.com/vllm-project/aibrix/pull/719),[#730](https://github.com/vllm-project/aibrix/pull/730),[#1024](https://github.com/vllm-project/aibrix/pull/1024))**Fairness-oriented Routing (OSDI’24 VTC)**: Introduces the vtc-basic router with Windowed Adaptive Fairness Routing, which dynamically tracks token usage and ensures fair load distribution across pods. ([#964](https://github.com/vllm-project/aibrix/pull/964),[#1011](https://github.com/vllm-project/aibrix/pull/1011),[#1065](https://github.com/vllm-project/aibrix/pull/1065))

## 📊 Feature Enhancements

### Gateway Enhancements

- Support for OpenAI-compatible APIs, including streaming responses, usage reporting, asynchronous handling, and standardized error responses for seamless end-to-end integration. (
[#703](https://github.com/vllm-project/aibrix/pull/703),[#788](https://github.com/vllm-project/aibrix/pull/788),[#799](https://github.com/vllm-project/aibrix/pull/799)) - Introduced the /v1/models endpoint for compatibility with OpenAI-style API clients. (
[#802](https://github.com/vllm-project/aibrix/pull/802)) - Refactored gateway-plugins with an extensible ext-proc server architecture, laying the foundation for pluggable policies. (
[#810](https://github.com/vllm-project/aibrix/pull/810)) - Improved concurrency safety and routing stability through major cache and router redesigns (
[#878](https://github.com/vllm-project/aibrix/pull/878),[#884](https://github.com/vllm-project/aibrix/pull/884))

### Control Plane:

- Added Kubernetes webhook validation for CRDs, providing early error feedback during resource creation (
[#748](https://github.com/vllm-project/aibrix/pull/748),[#786](https://github.com/vllm-project/aibrix/pull/786)). - Improve RayClusterFleet to fully support Deepseek-r1/v3 models (
[#789](https://github.com/vllm-project/aibrix/pull/789),[#826](https://github.com/vllm-project/aibrix/pull/826),[#835](https://github.com/vllm-project/aibrix/pull/835),[#914](https://github.com/vllm-project/aibrix/pull/914),[#954](https://github.com/vllm-project/aibrix/pull/954)). - Add scale subresource in RayClusterFleet CRD and enable HPA support (
[#1082](https://github.com/vllm-project/aibrix/pull/1082),[#1109](https://github.com/vllm-project/aibrix/pull/1109))

### Installation Experiences:

- Introduced Terraform modules for GCP and Kubernetes deployment (
[#823](https://github.com/vllm-project/aibrix/pull/823)). - Added setup guides for Minikube on Lambda Cloud and AWS in the documentation (
[#1020](https://github.com/vllm-project/aibrix/pull/1020)). - Enabled standalone controller installation for simplified system bootstrapping.(
[#930](https://github.com/vllm-project/aibrix/pull/930),[#931](https://github.com/vllm-project/aibrix/pull/931)) - Streamlined upgrade workflows by introducing kubectl apply support. CRDs are now split and applied with --server-side, avoiding annotation size limits and enabling smooth incremental updates. (
[#793](https://github.com/vllm-project/aibrix/pull/793)) - Enabled container image publishing to Github Container Registry (GHCR) (
[#1041](https://github.com/vllm-project/aibrix/pull/1041)). - Support ARM container Images (
[#1090](https://github.com/vllm-project/aibrix/pull/1090))

### Observability & Stability:

- Shipped prebuilt Grafana dashboards covering control plane, gateway, and KV cache components for out-of-the-box observability. (
[#1048](https://github.com/vllm-project/aibrix/pull/1048)) - Tuned Envoy proxy memory and buffer configurations for better performance under high concurrency. (
[#825](https://github.com/vllm-project/aibrix/pull/825)) - Tuned Envoy proxy configurations for memory and buffer management under high concurrency (
[#967](https://github.com/vllm-project/aibrix/pull/967)). - Added graceful shutdown, liveness, and readiness probes to improve service resilience (
[#962](https://github.com/vllm-project/aibrix/pull/962)). - Delivered production-ready monitoring setups for all major system components (
[#1048](https://github.com/vllm-project/aibrix/pull/1048)).

## New Contributors

[@gaocegege](https://github.com/gaocegege)made their first contribution in[#731](https://github.com/vllm-project/aibrix/pull/731)[@eltociear](https://github.com/eltociear)made their first contribution in[#736](https://github.com/vllm-project/aibrix/pull/736)[@terrytangyuan](https://github.com/terrytangyuan)made their first contribution in[#746](https://github.com/vllm-project/aibrix/pull/746)[@jolfr](https://github.com/jolfr)made their first contribution in[#744](https://github.com/vllm-project/aibrix/pull/744)[@Abirdcfly](https://github.com/Abirdcfly)made their first contribution in[#763](https://github.com/vllm-project/aibrix/pull/763)[@pierDipi](https://github.com/pierDipi)made their first contribution in[#764](https://github.com/vllm-project/aibrix/pull/764)[@Xunzhuo](https://github.com/Xunzhuo)made their first contribution in[#810](https://github.com/vllm-project/aibrix/pull/810)[@zjd0112](https://github.com/zjd0112)made their first contribution in[#849](https://github.com/vllm-project/aibrix/pull/849)[@SongGuyang](https://github.com/SongGuyang)made their first contribution in[#850](https://github.com/vllm-project/aibrix/pull/850)[@vaaandark](https://github.com/vaaandark)made their first contribution in[#856](https://github.com/vllm-project/aibrix/pull/856)[@vie-serendipity](https://github.com/vie-serendipity)made their first contribution in[#860](https://github.com/vllm-project/aibrix/pull/860)[@nurali-techie](https://github.com/nurali-techie)made their first contribution in[#867](https://github.com/vllm-project/aibrix/pull/867)[@legendtkl](https://github.com/legendtkl)made their first contribution in[#870](https://github.com/vllm-project/aibrix/pull/870)[@ronaldosaheki](https://github.com/ronaldosaheki)made their first contribution in[#886](https://github.com/vllm-project/aibrix/pull/886)[@nadongjun](https://github.com/nadongjun)made their first contribution in[#890](https://github.com/vllm-project/aibrix/pull/890)[@cr7258](https://github.com/cr7258)made their first contribution in[#893](https://github.com/vllm-project/aibrix/pull/893)[@thomasjpfan](https://github.com/thomasjpfan)made their first contribution in[#883](https://github.com/vllm-project/aibrix/pull/883)[@runzhen](https://github.com/runzhen)made their first contribution in[#896](https://github.com/vllm-project/aibrix/pull/896)[@my-git9](https://github.com/my-git9)made their first contribution in[#895](https://github.com/vllm-project/aibrix/pull/895)[@googs1025](https://github.com/googs1025)made their first contribution in[#908](https://github.com/vllm-project/aibrix/pull/908)[@Iceber](https://github.com/Iceber)made their first contribution in[#926](https://github.com/vllm-project/aibrix/pull/926)[@ModiIntel](https://github.com/ModiIntel)made their first contribution in[#954](https://github.com/vllm-project/aibrix/pull/954)[@Venkat2811](https://github.com/Venkat2811)made their first contribution in[#964](https://github.com/vllm-project/aibrix/pull/964)[@SuperMohit](https://github.com/SuperMohit)made their first contribution in[#992](https://github.com/vllm-project/aibrix/pull/992)[@weapons97](https://github.com/weapons97)made their first contribution in[#990](https://github.com/vllm-project/aibrix/pull/990)[@zhixian82](https://github.com/zhixian82)made their first contribution in[#1082](https://github.com/vllm-project/aibrix/pull/1082)

## What's Changed

**Full Changelog**: `v0.2.0...v0.3.0`

- [Docs] fix format of the dist kv cache doc by
[@DwyaneShi](https://github.com/DwyaneShi)in[#714](https://github.com/vllm-project/aibrix/pull/714) - complete the 'make generate' command by
[@kerthcet](https://github.com/kerthcet)in[#711](https://github.com/vllm-project/aibrix/pull/711) - Update organization reference in code base by
[@Jeffwan](https://github.com/Jeffwan)in[#717](https://github.com/vllm-project/aibrix/pull/717) - [Misc] Update the documentation link by
[@Jeffwan](https://github.com/Jeffwan)in[#720](https://github.com/vllm-project/aibrix/pull/720) - Initial implementation of radix tree-based cache by
[@gangmuk](https://github.com/gangmuk)in[#678](https://github.com/vllm-project/aibrix/pull/678) - Add model adapter e2e tests by
[@varungup90](https://github.com/varungup90)in[#701](https://github.com/vllm-project/aibrix/pull/701) - Add vllm cpu alternative for local development by
[@varungup90](https://github.com/varungup90)in[#721](https://github.com/vllm-project/aibrix/pull/721) - Add white paper file by
[@Jeffwan](https://github.com/Jeffwan)in[#724](https://github.com/vllm-project/aibrix/pull/724) - Adding streaming client for AIbrix experiments by
[@happyandslow](https://github.com/happyandslow)in[#676](https://github.com/vllm-project/aibrix/pull/676) - [Docs] Update Readme with new links and blog post, and update white paper by
[@xieus](https://github.com/xieus)in[#725](https://github.com/vllm-project/aibrix/pull/725) - Recording failed requests in benchmark client by
[@gangmuk](https://github.com/gangmuk)in[#727](https://github.com/vllm-project/aibrix/pull/727) - Process response headers in gateway by
[@varungup90](https://github.com/varungup90)in[#703](https://github.com/vllm-project/aibrix/pull/703) - [misc] Fix white paper link by
[@Jeffwan](https://github.com/Jeffwan)in[#728](https://github.com/vllm-project/aibrix/pull/728) - Prefix and load aware routing with radix tree kv cache by
[@gangmuk](https://github.com/gangmuk)in[#719](https://github.com/vllm-project/aibrix/pull/719) - Fix slack link in README.md by
[@Jeffwan](https://github.com/Jeffwan)in[#729](https://github.com/vllm-project/aibrix/pull/729) - [readme] Fix wrong link by
[@gaocegege](https://github.com/gaocegege)in[#731](https://github.com/vllm-project/aibrix/pull/731) - [Misc] update scheduler.py by
[@eltociear](https://github.com/eltociear)in[#736](https://github.com/vllm-project/aibrix/pull/736) - Improve thread safety for TreeNode data structure and refactor related codes by
[@gangmuk](https://github.com/gangmuk)in[#730](https://github.com/vllm-project/aibrix/pull/730) - Fix CacheSpec api scheme by
[@kerthcet](https://github.com/kerthcet)in[#740](https://github.com/vllm-project/aibrix/pull/740) - docs: Fix link to license by
[@terrytangyuan](https://github.com/terrytangyuan)in[#746](https://github.com/vllm-project/aibrix/pull/746) - Use native codegen cmd generating client-go by
[@kerthcet](https://github.com/kerthcet)in[#741](https://github.com/vllm-project/aibrix/pull/741) - [Docs]: Fixed kubectl commands for install of components by
[@jolfr](https://github.com/jolfr)in[#744](https://github.com/vllm-project/aibrix/pull/744) - [fix] fixing bug in using AsyncOpenAI client (header setting, token counting, etc) by
[@gangmuk](https://github.com/gangmuk)in[#738](https://github.com/vllm-project/aibrix/pull/738) - Add webhook framework by
[@kerthcet](https://github.com/kerthcet)in[#748](https://github.com/vllm-project/aibrix/pull/748) - Use random seed for xxhash by
[@varungup90](https://github.com/varungup90)in[#752](https://github.com/vllm-project/aibrix/pull/752) - Create SECURITY.md to enable security policy by
[@xieus](https://github.com/xieus)in[#756](https://github.com/vllm-project/aibrix/pull/756) - [CI] Add integration test by
[@kerthcet](https://github.com/kerthcet)in[#759](https://github.com/vllm-project/aibrix/pull/759) - [Bug] fix: correct non-inherited context by
[@Abirdcfly](https://github.com/Abirdcfly)in[#763](https://github.com/vllm-project/aibrix/pull/763) - [Misc] Parametrize Makefile for mocked vLLM apps by
[@pierDipi](https://github.com/pierDipi)in[#764](https://github.com/vllm-project/aibrix/pull/764) - Support benchmarking script by using real application trace by
[@nwangfw](https://github.com/nwangfw)in[#737](https://github.com/vllm-project/aibrix/pull/737) - Maintaining common benchmarks utils in a separate dir by
[@gangmuk](https://github.com/gangmuk)in[#770](https://github.com/vllm-project/aibrix/pull/770) - Ignore worker pods for gateway routing by
[@varungup90](https://github.com/varungup90)in[#776](https://github.com/vllm-project/aibrix/pull/776) - Disable ENABLE_PROBES_INJECTION in correct way by
[@Jeffwan](https://github.com/Jeffwan)in[#779](https://github.com/vllm-project/aibrix/pull/779) - Make stream include usage as optional by
[@varungup90](https://github.com/varungup90)in[#788](https://github.com/vllm-project/aibrix/pull/788) - Append ray head label selector in PodAutoscaler by
[@Jeffwan](https://github.com/Jeffwan)in[#789](https://github.com/vllm-project/aibrix/pull/789) - Remove redundant install crds in makefile by
[@varungup90](https://github.com/varungup90)in[#792](https://github.com/vllm-project/aibrix/pull/792) - Update request message processing for /v1/completion input by
[@varungup90](https://github.com/varungup90)in[#794](https://github.com/vllm-project/aibrix/pull/794) - Added target...

[Read more](https://github.com/vllm-project/aibrix/releases/tag/v0.3.0)

## v0.3.0-rc.2

Automatically generated release for tag v0.3.0-rc.2.

## What's Changed

- [Bug] fix: condition nil panic in FindStatusCondition func by
[@googs1025](https://github.com/googs1025)in[#1078](https://github.com/vllm-project/aibrix/pull/1078) - Refactor request body processing and add multi-turn conversation support by
[@varungup90](https://github.com/varungup90)in[#1067](https://github.com/vllm-project/aibrix/pull/1067) - Upload arm build images with git.ref_name by
[@varungup90](https://github.com/varungup90)in[#1090](https://github.com/vllm-project/aibrix/pull/1090) - Update documentation and add openai sdk samples by
[@varungup90](https://github.com/varungup90)in[#1092](https://github.com/vllm-project/aibrix/pull/1092) - Rename preble based prefix routing strategy by
[@varungup90](https://github.com/varungup90)in[#1104](https://github.com/vllm-project/aibrix/pull/1104) - Add v0.3.0 ps performance regression test scenario by
[@Jeffwan](https://github.com/Jeffwan)in[#1099](https://github.com/vllm-project/aibrix/pull/1099) - Migrating benchmark entrypoints to python client by
[@happyandslow](https://github.com/happyandslow)in[#1066](https://github.com/vllm-project/aibrix/pull/1066) - [Misc] Add demo manifests for volcano engine by
[@Jeffwan](https://github.com/Jeffwan)in[#1105](https://github.com/vllm-project/aibrix/pull/1105) - [Integration] KVCache: update vLLM integration by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1107](https://github.com/vllm-project/aibrix/pull/1107) - [Bug]fix: add scale subresource to rayclusterfleet by
[@zhixian82](https://github.com/zhixian82)in[#1082](https://github.com/vllm-project/aibrix/pull/1082) - [Feature] KVCache: Suppport InfiniStore GID and enhance cluster mode by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1106](https://github.com/vllm-project/aibrix/pull/1106) - [Chore] fix: regenerate crd by
[@zhixian82](https://github.com/zhixian82)in[#1109](https://github.com/vllm-project/aibrix/pull/1109) - [Chore] KVCache: enhance format and dependencies by
[@DwyaneShi](https://github.com/DwyaneShi)in[#1108](https://github.com/vllm-project/aibrix/pull/1108) - Polish benchmark manifests and VE samples by
[@Jeffwan](https://github.com/Jeffwan)in[#1113](https://github.com/vllm-project/aibrix/pull/1113) - [API] Support customized template for cache by
[@Jeffwan](https://github.com/Jeffwan)in[#1114](https://github.com/vllm-project/aibrix/pull/1114) - Bump version to v0.3.0-rc.2 by
[@Jeffwan](https://github.com/Jeffwan)in[#1115](https://github.com/vllm-project/aibrix/pull/1115) - [Fix] Move pdb from patch to resources by
[@Jeffwan](https://github.com/Jeffwan)in[#1117](https://github.com/vllm-project/aibrix/pull/1117)

## New Contributors

[@zhixian82](https://github.com/zhixian82)made their first contribution in[#1082](https://github.com/vllm-project/aibrix/pull/1082)

**Full Changelog**: `v0.3.0-rc.1...v0.3.0-rc.2`

## v0.3.0-rc.1

## What's Changed

- [Docs] fix format of the dist kv cache doc by
[@DwyaneShi](https://github.com/DwyaneShi)in[#714](https://github.com/vllm-project/aibrix/pull/714) - complete the 'make generate' command by
[@kerthcet](https://github.com/kerthcet)in[#711](https://github.com/vllm-project/aibrix/pull/711) - Update organization reference in code base by
[@Jeffwan](https://github.com/Jeffwan)in[#717](https://github.com/vllm-project/aibrix/pull/717) - [Misc] Update the documentation link by
[@Jeffwan](https://github.com/Jeffwan)in[#720](https://github.com/vllm-project/aibrix/pull/720) - Initial implementation of radix tree-based cache by
[@gangmuk](https://github.com/gangmuk)in[#678](https://github.com/vllm-project/aibrix/pull/678) - Add model adapter e2e tests by
[@varungup90](https://github.com/varungup90)in[#701](https://github.com/vllm-project/aibrix/pull/701) - Add vllm cpu alternative for local development by
[@varungup90](https://github.com/varungup90)in[#721](https://github.com/vllm-project/aibrix/pull/721) - Add white paper file by
[@Jeffwan](https://github.com/Jeffwan)in[#724](https://github.com/vllm-project/aibrix/pull/724) - Adding streaming client for AIbrix experiments by
[@happyandslow](https://github.com/happyandslow)in[#676](https://github.com/vllm-project/aibrix/pull/676) - [Docs] Update Readme with new links and blog post, and update white paper by
[@xieus](https://github.com/xieus)in[#725](https://github.com/vllm-project/aibrix/pull/725) - Recording failed requests in benchmark client by
[@gangmuk](https://github.com/gangmuk)in[#727](https://github.com/vllm-project/aibrix/pull/727) - Process response headers in gateway by
[@varungup90](https://github.com/varungup90)in[#703](https://github.com/vllm-project/aibrix/pull/703) - [misc] Fix white paper link by
[@Jeffwan](https://github.com/Jeffwan)in[#728](https://github.com/vllm-project/aibrix/pull/728) - Prefix and load aware routing with radix tree kv cache by
[@gangmuk](https://github.com/gangmuk)in[#719](https://github.com/vllm-project/aibrix/pull/719) - Fix slack link in README.md by
[@Jeffwan](https://github.com/Jeffwan)in[#729](https://github.com/vllm-project/aibrix/pull/729) - [readme] Fix wrong link by
[@gaocegege](https://github.com/gaocegege)in[#731](https://github.com/vllm-project/aibrix/pull/731) - [Misc] update scheduler.py by
[@eltociear](https://github.com/eltociear)in[#736](https://github.com/vllm-project/aibrix/pull/736) - Improve thread safety for TreeNode data structure and refactor related codes by
[@gangmuk](https://github.com/gangmuk)in[#730](https://github.com/vllm-project/aibrix/pull/730) - Fix CacheSpec api scheme by
[@kerthcet](https://github.com/kerthcet)in[#740](https://github.com/vllm-project/aibrix/pull/740) - docs: Fix link to license by
[@terrytangyuan](https://github.com/terrytangyuan)in[#746](https://github.com/vllm-project/aibrix/pull/746) - Use native codegen cmd generating client-go by
[@kerthcet](https://github.com/kerthcet)in[#741](https://github.com/vllm-project/aibrix/pull/741) - [Docs]: Fixed kubectl commands for install of components by
[@jolfr](https://github.com/jolfr)in[#744](https://github.com/vllm-project/aibrix/pull/744) - [fix] fixing bug in using AsyncOpenAI client (header setting, token counting, etc) by
[@gangmuk](https://github.com/gangmuk)in[#738](https://github.com/vllm-project/aibrix/pull/738) - Add webhook framework by
[@kerthcet](https://github.com/kerthcet)in[#748](https://github.com/vllm-project/aibrix/pull/748) - Use random seed for xxhash by
[@varungup90](https://github.com/varungup90)in[#752](https://github.com/vllm-project/aibrix/pull/752) - Create SECURITY.md to enable security policy by
[@xieus](https://github.com/xieus)in[#756](https://github.com/vllm-project/aibrix/pull/756) - [CI] Add integration test by
[@kerthcet](https://github.com/kerthcet)in[#759](https://github.com/vllm-project/aibrix/pull/759) - [Bug] fix: correct non-inherited context by
[@Abirdcfly](https://github.com/Abirdcfly)in[#763](https://github.com/vllm-project/aibrix/pull/763) - [Misc] Parametrize Makefile for mocked vLLM apps by
[@pierDipi](https://github.com/pierDipi)in[#764](https://github.com/vllm-project/aibrix/pull/764) - Support benchmarking script by using real application trace by
[@nwangfw](https://github.com/nwangfw)in[#737](https://github.com/vllm-project/aibrix/pull/737) - Maintaining common benchmarks utils in a separate dir by
[@gangmuk](https://github.com/gangmuk)in[#770](https://github.com/vllm-project/aibrix/pull/770) - Ignore worker pods for gateway routing by
[@varungup90](https://github.com/varungup90)in[#776](https://github.com/vllm-project/aibrix/pull/776) - Disable ENABLE_PROBES_INJECTION in correct way by
[@Jeffwan](https://github.com/Jeffwan)in[#779](https://github.com/vllm-project/aibrix/pull/779) - Make stream include usage as optional by
[@varungup90](https://github.com/varungup90)in[#788](https://github.com/vllm-project/aibrix/pull/788) - Append ray head label selector in PodAutoscaler by
[@Jeffwan](https://github.com/Jeffwan)in[#789](https://github.com/vllm-project/aibrix/pull/789) - Remove redundant install crds in makefile by
[@varungup90](https://github.com/varungup90)in[#792](https://github.com/vllm-project/aibrix/pull/792) - Update request message processing for /v1/completion input by
[@varungup90](https://github.com/varungup90)in[#794](https://github.com/vllm-project/aibrix/pull/794) - Added target pod to client result and made clients consistent by
[@gangmuk](https://github.com/gangmuk)in[#799](https://github.com/vllm-project/aibrix/pull/799) - Enable CI tests for release branch by
[@Jeffwan](https://github.com/Jeffwan)in[#805](https://github.com/vllm-project/aibrix/pull/805) - Move modelAdapter runtime validation to webhook by
[@kerthcet](https://github.com/kerthcet)in[#786](https://github.com/vllm-project/aibrix/pull/786) - [Misc] Adding model field to each request by
[@happyandslow](https://github.com/happyandslow)in[#812](https://github.com/vllm-project/aibrix/pull/812) - [Refactor]: gateway-plugins ext-proc server codebase by
[@Xunzhuo](https://github.com/Xunzhuo)in[#810](https://github.com/vllm-project/aibrix/pull/810) - [CI]: update release tags pattern by
[@Xunzhuo](https://github.com/Xunzhuo)in[#815](https://github.com/vllm-project/aibrix/pull/815) - [Docs]: fix vllm mock app Unauthorized response by
[@Xunzhuo](https://github.com/Xunzhuo)in[#817](https://github.com/vllm-project/aibrix/pull/817) - Reconfigure workload generator for predefined synthetic patterns by
[@happyandslow](https://github.com/happyandslow)in[#771](https://github.com/vllm-project/aibrix/pull/771) - Workload generation scripts for prefix aware routing by
[@gangmuk](https://github.com/gangmuk)in[#820](https://github.com/vllm-project/aibrix/pull/820) - Fix the paths in lambda cloud doc by
[@gangmuk](https://github.com/gangmuk)in[#824](https://github.com/vllm-project/aibrix/pull/824) - [Bug] Added Startup Probe in Quickstart Model by
[@jolfr](https://github.com/jolfr)in[#773](https://github.com/vllm-project/aibrix/pull/773) - Add /v1/models endpoint to gateway by
[@varungup90](https://github.com/varungup90)in[#802](https://github.com/vllm-project/aibrix/pull/802) - Increase envoy proxy memory config and client connection buffersize by
[@varungup90](https://github.com/varungup90)in[#825](https://github.com/vllm-project/aibrix/pull/825) - Support to create default HttpRoute for RayClusterFleet by
[@Jeffwan](https://github.com/Jeffwan)in[#826](https://github.com/vllm-project/aibrix/pull/826) - [Misc] Fix CI issue on release branch and clean up logs by
[@Jeffwan](https://github.com/Jeffwan)in[#837](https://github.com/vllm-project/aibrix/pull/837) - Fix repeated initialization of gateway routers and add unit test for prefix cache by
[@varungup90](https://github.com/varungup90)in[#838](https://github.com/vllm-project/aibrix/pull/838) - Add deepseek-r1 671B deployment sample and docs by
[@Jeffwan](https://github.com/Jeffwan)in[#835](https://github.com/vllm-project/aibrix/pull/835) - Bump AIBrix version to v0.2.1 in manifests by
[@Jeffwan](https://github.com/Jeffwan)in[#839](https://github.com/vllm-project/aibrix/pull/839) - [Docs] Update Slack link by
[@gaocegege](https://github.com/gaocegege)in[#841](https://github.com/vllm-project/aibrix/pull/841) - [Docs] Remove repeated lines by
[@zjd0112](https://github.com/zjd0112)in[#849](https://github.com/vllm-project/aibrix/pull/849) - Bump AIBrix version to v0.2.1 for standalone distributed inference by
[@SongGuyang](https://github.com/SongGuyang)in[#850](https://github.com/vllm-project/aibrix/pull/850) - Support OpenAI api style /v1/models response by
[@Jeffwan](https://github.com/Jeffwan)in[#829](https://github.com/vllm-project/aibrix/pull/829) - [Misc] Resolve symlink ambiguity when generating codes by
[@vaaandark](https://github.com/vaaandark)in[#856](https://github.com/vllm-project/aibrix/pull/856) - Introduce RoutingContext in Route interface and clean up stale codes by
[@Jeffwan](https://github.com/Jeffwan)in[#855](https://github.com/vllm-project/aibrix/pull/855) - [Misc]: sync hpa status to podAutoScaler by
[@vie-serendipity](https://github.com/vie-serendipity)in[#860](https://github.com/vllm-project/aibrix/pull/860) - Generate workload based on prefix sharing synthetic data by
[@happyandslow](https://github.com/happyandslow)in[#840](https://github.com/vllm-project/aibrix/pull/840) - Fixing missing image link in
[#840](https://github.com/vllm-project/aibrix/pull/840)by[@happyandslow](https://github.com/happyandslow)in[#871](https://github.com/vllm-project/aibrix/pull/871) - Cite Melange paper in heterogeneous feature by
[@Jeffwan](https://github.com/Jeffwan)in[#872](https://github.com/vllm-project/aibrix/pull/872) - [Misc] support linux for vllm cpu local development by
[@nurali-techie](https://github.com/nurali-techie)in[#867](https://github.com/vllm-project/aibrix/pull/867) - Refactor make deploy to use apply instead of create by
[@varungup90](https://github.com/varungup90)in[#793](https://github.com/vllm-project/aibrix/pull/793) - Use string based tokenizer in prefix cache by
[@varungup90](https://github.com/varungup90)in[#774](https://github.com/vllm-project/aibrix/pull/774) - Add profiling support for gateway plugins and bug fix to close stream decoder by
[@varungup90](https://github.com/varungup90)in[#857](https://github.com/vllm-project/aibrix/pull/857) - Add flag to enable/disable GPU Optimizer tracing by
[@varungup90](https://github.com/varungup90)in[#875](https://github.com/vllm-project/aibrix/pull/875) - [Docs] fix typo in runtime feature page by
[@legendtkl](https://github.com/legendtkl)in[#870](https://github.com/vllm-project/aibrix/pull/870) - chore: clean-up mock yaml by
[@Xunzhuo](https://github.com/Xunzhuo)in[#877](https://github.com/vllm-project/aibrix/pull/877) - Fixing image link error in workload generator README.md by
[@happyandslow](https://github.com/happyandslow)in[#888](https://github.com/vllm-project/aibrix/pull/888) - Update Synthetic Load Prodefined Config for Geneerator by
[@happyandslow](https://github.com/happyandslow)in[#889](https://github.com/vllm-project/aibrix/pull/889) - [Misc] Fix plot_workload to pass dirname to makedirs by
[@ronaldosaheki](https://github.com/ronaldosaheki)in[#886](https://github.com/vllm-project/aibrix/pull/886) - [Misc] Fix client.py in case workload has model null and client has default_model by
[@ronaldosaheki](https://github.com/ronaldosaheki)in[#887](https://github.com/vllm-project/aibrix/pull/887) - [WIP] Adding input/output distribution argument to constant load generator by
[@happyandslow](https://github.com/happyandslow)in[#882](https://github.com/vllm-project/aibrix/pull/882) - [Docs] Fix broken contributing guidelines link in README by
[@nadongjun](https://github.com/nadongjun)in[#890](https://github.com/vllm-project/aibrix/pull/890) - [Bug] fix install script PATH environment variable by
[@cr7258](https://github.com/cr7258)in[#893](https://github.com/vllm-project/aibrix/pull/893) - [Docs] Link to dynamic lora from docs by
[@thomasjpfan](https://github.com/thomasjpfan)in[#883](https://github.com/vllm-project/aibrix/pull/883) - [API] Refactor: core cache design and impl by
[@Xunzhuo](https://github.com/Xunzhuo)in[#878](https://github.com/vllm-project/aibrix/pull/878) - Added antiaffinity in kvcache crd by
[@gangmuk](https://github.com/gangmuk)in[#865](https://github.com/vllm-project/aibrix/pull/865) - [Docs] Fix tpm and rpm typo in gateway-plugins.rst by
[@runzhen](https://github.com/runzhen)in[#896](https://github.com/vllm-project/aibrix/pull/896) - [Misc] Remove unused function in pkg/utils by
[@my-git9](https://github.com/my-git9)in[#895](https://github.com/vllm-project/aibrix/pull/895) - Remove model name from client and generator by
[@happyandslow](https://github.com/happyandslow)in[#894](https://github.com/vllm-project/aibrix/pull/894) - [Misc] Add PS benchmark manifests and scripts by
[@Jeffwan](https://github.com/Jeffwan)in[#899](https://github.com/vllm-project/aibrix/pull/899) - Add release overlays to update control plane config for production deployment by
[@varungup90](https://github.com/varungup90)in[https://github.com/vllm-project/aibri](https://github.com/vllm-project/aibri)...

[Read more](https://github.com/vllm-project/aibrix/releases/tag/v0.3.0-rc.1)

## v0.2.1

Automatically generated release for tag v0.2.1.

## What's Changed

- Cherry-pick Enable CI tests for release branch (
[#805](https://github.com/vllm-project/aibrix/pull/805)) by[@Jeffwan](https://github.com/Jeffwan)in[#808](https://github.com/vllm-project/aibrix/pull/808) - Cherry pick
[#776](https://github.com/vllm-project/aibrix/pull/776)[#779](https://github.com/vllm-project/aibrix/pull/779)[#788](https://github.com/vllm-project/aibrix/pull/788)[#789](https://github.com/vllm-project/aibrix/pull/789)[#794](https://github.com/vllm-project/aibrix/pull/794)to release branch by[@Jeffwan](https://github.com/Jeffwan)[@varungup90](https://github.com/varungup90)in[#809](https://github.com/vllm-project/aibrix/pull/809) - Cherry-pick
[#825](https://github.com/vllm-project/aibrix/pull/825)[#826](https://github.com/vllm-project/aibrix/pull/826)part of[#717](https://github.com/vllm-project/aibrix/pull/717)in release branch by[@varungup90](https://github.com/varungup90)[@Jeffwan](https://github.com/Jeffwan)in[#828](https://github.com/vllm-project/aibrix/pull/828) - Update version and tags to v0.2.1 by
[@Jeffwan](https://github.com/Jeffwan)in[#833](https://github.com/vllm-project/aibrix/pull/833)

**Full Changelog**: `v0.2.0...v0.2.1`

## v0.2.0

Automatically generated release for tag v0.2.0.

## 🚀 New Features Highlights

**Distributed KV Cache**: Implemented support for managing KV cache across multiple nodes, enhancing performance.**Cost-Driven Heterogenous Serving**: Improved scheduling and inference strategies for mixed GPU environments, optimizing cost and resource utilization. ([#371](https://github.com/vllm-project/aibrix/pull/371)[#430](https://github.com/vllm-project/aibrix/pull/430),[#509](https://github.com/vllm-project/aibrix/pull/509),[#598](https://github.com/vllm-project/aibrix/pull/598),[#554](https://github.com/vllm-project/aibrix/pull/554),[#598](https://github.com/vllm-project/aibrix/pull/598))**Optimizer Based Autoscaling**: Leverage offline profiles of inference server to calculate the number of replicas. ([#430](https://github.com/vllm-project/aibrix/pull/430),[#500](https://github.com/vllm-project/aibrix/pull/500),[#692](https://github.com/vllm-project/aibrix/pull/692),[#508](https://github.com/vllm-project/aibrix/pull/508))**Prefix Cache Aware Routing**: Added support for routing decisions based on prefix cache hits, improving inference efficiency. ([#641](https://github.com/vllm-project/aibrix/pull/641),[#657](https://github.com/vllm-project/aibrix/pull/657))

## 📊 Feature Enhancements

**LoRA Scheduling Enhancements**: Introduced multiple scheduling strategies, including bin packing, least latency, least throughput, and random. ([#544](https://github.com/vllm-project/aibrix/pull/544))**Prefix Cache Aware Routing**: Added support for routing decisions based on prefix cache hits, improving inference efficiency. ([#641](https://github.com/vllm-project/aibrix/pull/641))**Gateway Enhancements**: Improved request handling efficiency by enabling streaming in the Envoy gateway. ([#377](https://github.com/vllm-project/aibrix/pull/377)) Enhanced the handling of model registration and invalid cache scenarios. ([#542](https://github.com/vllm-project/aibrix/pull/542)), Introduced fallback strategies to ensure robust request allocation. ([#445](https://github.com/vllm-project/aibrix/pull/445)) Optimized cache store retrieval, reducing unnecessary overhead. ([#639](https://github.com/vllm-project/aibrix/pull/639)) Addressed missing Prometheus config preventing gateway startup. ([#441](https://github.com/vllm-project/aibrix/pull/441))**PodAutoscaler Scaling improvements**: Improved scaling logic to handle edge cases more efficiently. ([#508](https://github.com/vllm-project/aibrix/pull/508),[#515](https://github.com/vllm-project/aibrix/pull/515))

## 🛠Infrastructure & CI/CD Upgrades

- Parallelized Build Tasks: CI efficiency improvements by running builds in parallel. (
[#398](https://github.com/vllm-project/aibrix/pull/398)) - CrashLoopBackOff Detection in CI: Added monitoring for pod failures in testing workflows. (
[#444](https://github.com/vllm-project/aibrix/pull/444)) - Improved GitHub Actions Cost Efficiency: Optimized triggers and removed unnecessary nightly builds. (
[#411](https://github.com/vllm-project/aibrix/pull/411),[#422](https://github.com/vllm-project/aibrix/pull/422)) - Integration Tests for Core Components: Added integration tests for autoscalers, routing policies, and deployment configurations. (
[#616](https://github.com/vllm-project/aibrix/pull/616),[#620](https://github.com/vllm-project/aibrix/pull/620))

## What's Changed

- Add envoy gateway streaming support by
[@varungup90](https://github.com/varungup90)in[#377](https://github.com/vllm-project/aibrix/pull/377) - Add client traffic policy to increase per connection buffer size from 32kb to 256kb by
[@varungup90](https://github.com/varungup90)in[#395](https://github.com/vllm-project/aibrix/pull/395) - Misc: add support to metricsSources property of podautoscaler by
[@zhangjyr](https://github.com/zhangjyr)in[#371](https://github.com/vllm-project/aibrix/pull/371) - [Misc] Update runtime server startup command in v0.1.0 by
[@brosoul](https://github.com/brosoul)in[#396](https://github.com/vllm-project/aibrix/pull/396) - [CI] improve the ci efficiency by parallelizing the build tasks by
[@nwangfw](https://github.com/nwangfw)in[#398](https://github.com/vllm-project/aibrix/pull/398) - Fix the ticker interval by removing unnecessary ms by
[@Jeffwan](https://github.com/Jeffwan)in[#415](https://github.com/vllm-project/aibrix/pull/415) - [Misc] Disable specific endpoints logs by
[@Jeffwan](https://github.com/Jeffwan)in[#418](https://github.com/vllm-project/aibrix/pull/418) - [CI] Github Action trigger condition optimized for cost saving by
[@nwangfw](https://github.com/nwangfw)in[#411](https://github.com/vllm-project/aibrix/pull/411) - [Misc] Fix the mocked app role permission issue by
[@Jeffwan](https://github.com/Jeffwan)in[#416](https://github.com/vllm-project/aibrix/pull/416) - [CI] Nightly tag removed for release branch by
[@nwangfw](https://github.com/nwangfw)in[#422](https://github.com/vllm-project/aibrix/pull/422) - Enable setting PodAutoscaler configuration via YAML labels by
[@kr11](https://github.com/kr11)in[#409](https://github.com/vllm-project/aibrix/pull/409) - Update manifest to adopt v0.1.1 images by
[@Jeffwan](https://github.com/Jeffwan)in[#429](https://github.com/vllm-project/aibrix/pull/429) - [Bug]: duplicated http in rest metrics fetcher (
[#408](https://github.com/vllm-project/aibrix/issues/408)) by[@zhangjyr](https://github.com/zhangjyr)in[#421](https://github.com/vllm-project/aibrix/pull/421) - [MISC]: Improve Request Trace Granularity with Version Control by
[@zhangjyr](https://github.com/zhangjyr)in[#431](https://github.com/vllm-project/aibrix/pull/431) - Support histogram metrics from engine in cache by
[@Jeffwan](https://github.com/Jeffwan)in[#424](https://github.com/vllm-project/aibrix/pull/424) - Support fetching metrics from remote Prometheus server by
[@Jeffwan](https://github.com/Jeffwan)in[#433](https://github.com/vllm-project/aibrix/pull/433) - [CI] Add python wheel to release artifact by
[@Jeffwan](https://github.com/Jeffwan)in[#434](https://github.com/vllm-project/aibrix/pull/434) - Fix update cache pod issue and refactor updatePod handler by
[@Jeffwan](https://github.com/Jeffwan)in[#439](https://github.com/vllm-project/aibrix/pull/439) - Extract common metrics structure to types and utils by
[@Jeffwan](https://github.com/Jeffwan)in[#438](https://github.com/vllm-project/aibrix/pull/438) - Fix gateway startup issue due to missing prometheus config by
[@Jeffwan](https://github.com/Jeffwan)in[#441](https://github.com/vllm-project/aibrix/pull/441) - [feat]: GPU Optimizer and Simulator development app by
[@zhangjyr](https://github.com/zhangjyr)in[#430](https://github.com/vllm-project/aibrix/pull/430) - Add selectrandom fallback in routing and only scraping healthy pods by
[@Jeffwan](https://github.com/Jeffwan)in[#445](https://github.com/vllm-project/aibrix/pull/445) - AIBrix Workload Generator / Scenario Simulator by
[@happyandslow](https://github.com/happyandslow)in[#428](https://github.com/vllm-project/aibrix/pull/428) - CrashLoopBackOff status detection in CI by
[@nwangfw](https://github.com/nwangfw)in[#444](https://github.com/vllm-project/aibrix/pull/444) - Support installing individual controllers from giant controller-manager by
[@nwangfw](https://github.com/nwangfw)in[#442](https://github.com/vllm-project/aibrix/pull/442) - Refactor Scaler: Resolve Issues with Metric Parameter Updates in Multiple KPAs by
[@kr11](https://github.com/kr11)in[#437](https://github.com/vllm-project/aibrix/pull/437) - Support metrics multi labels for different models by
[@brosoul](https://github.com/brosoul)in[#450](https://github.com/vllm-project/aibrix/pull/450) - Add health check api interface for runtime by
[@Jeffwan](https://github.com/Jeffwan)in[#451](https://github.com/vllm-project/aibrix/pull/451) - Fix the service name override issue in rolebindings by
[@Jeffwan](https://github.com/Jeffwan)in[#453](https://github.com/vllm-project/aibrix/pull/453) - Reorganize docs/development and docs/tutorial structure by
[@Jeffwan](https://github.com/Jeffwan)in[#455](https://github.com/vllm-project/aibrix/pull/455) - Move tools to separate folders and update mocked app README.md by
[@Jeffwan](https://github.com/Jeffwan)in[#457](https://github.com/vllm-project/aibrix/pull/457) - Fix multi models metric result in PromQL by
[@brosoul](https://github.com/brosoul)in[#458](https://github.com/vllm-project/aibrix/pull/458) - Support Azure LLM trace in workload generator by
[@happyandslow](https://github.com/happyandslow)in[#462](https://github.com/vllm-project/aibrix/pull/462) - Fix autoscaler scalingstrategy switching logic by
[@nwangfw](https://github.com/nwangfw)in[#475](https://github.com/vllm-project/aibrix/pull/475) - Fix missing handle of PromQL scope is PodMetricScope by
[@brosoul](https://github.com/brosoul)in[#479](https://github.com/vllm-project/aibrix/pull/479) - [Misc] Consolidate app and simulator by
[@zhangjyr](https://github.com/zhangjyr)in[#477](https://github.com/vllm-project/aibrix/pull/477) - [Bug] Avoid including sensitive info in Dockerfile ENV by
[@zhangjyr](https://github.com/zhangjyr)in[#487](https://github.com/vllm-project/aibrix/pull/487) - Refactor generator to generate time-based traces by
[@happyandslow](https://github.com/happyandslow)in[#478](https://github.com/vllm-project/aibrix/pull/478) - [CI] Update deploy workload script in installation test by
[@nwangfw](https://github.com/nwangfw)in[#499](https://github.com/vllm-project/aibrix/pull/499) - [Bug] handle metricKey creation with MetricsSources by
[@nwangfw](https://github.com/nwangfw)in[#498](https://github.com/vllm-project/aibrix/pull/498) - Adding Client for Workload Generator Workload File by
[@happyandslow](https://github.com/happyandslow)in[#501](https://github.com/vllm-project/aibrix/pull/501) - [Feat] Integrate deployment configurations and fix autoscaler/gpu optimizer connectivity by
[@zhangjyr](https://github.com/zhangjyr)in[#500](https://github.com/vllm-project/aibrix/pull/500) - Fix some simulator format issue and add some TODOs by
[@Jeffwan](https://github.com/Jeffwan)in[#505](https://github.com/vllm-project/aibrix/pull/505) - [Bug] Fix the way how podautoscaler handle 0 pods. by
[@zhangjyr](https://github.com/zhangjyr)in[#508](https://github.com/vllm-project/aibrix/pull/508) - [Misc] Improve gpu optimizer debugging on podautoscaler. by
[@zhangjyr](https://github.com/zhangjyr)in[#509](https://github.com/vllm-project/aibrix/pull/509) - Optimize kustomize overlay for volcano engine deployment by
[@Jeffwan](https://github.com/Jeffwan)in[#512](https://github.com/vllm-project/aibrix/pull/512) - [perf] Refact tos downloader in Runtime by
[@brosoul](https://github.com/brosoul)in[#510](https://github.com/vllm-project/aibrix/pull/510) - Refactor metric source for customized protocol, port and path by
[@kr11](https://github.com/kr11)in[#511](https://github.com/vllm-project/aibrix/pull/511) - [Bug] Fixed the yaml of deployments in heterogenous GPU settings to make KPA scaling work as expected. by
[@zhangjyr](https://github.com/zhangjyr)in[#513](https://github.com/vllm-project/aibrix/pull/513) - [Misc] Heterogeneous GPU Optimizer Logging Clean Up by
[@nwangfw](https://github.com/nwangfw)in[#514](https://github.com/vllm-project/aibrix/pull/514) - Fix KPA bug, and an elaborate KPA test case by
[@kr11](https://github.com/kr11)in[#515](https://github.com/vllm-project/aibrix/pull/515) - Cut v0.2.0-rc.1 release by
[@Jeffwan](https://github.com/Jeffwan)in[#516](https://github.com/vllm-project/aibrix/pull/516) - [Bug] Accumulated bug fix on controller manager, mock app configuration, and gpu optimizer. by
[@zhangjyr](https://github.com/zhangjyr)in[#522](https://github.com/vllm-project/aibrix/pull/522) - [Misc] Reduced runtime's container image size by
[@nwangfw](https://github.com/nwangfw)in[#518](https://github.com/vllm-project/aibrix/pull/518) - clean memory scaler object when pa crd is deleted by
[@kr11](https://github.com/kr11)in[#520](https://github.com/vllm-project/aibrix/pull/520) - Configure autoscaler http client to skip certificate check by
[@Jeffwan](https://github.com/Jeffwan)in[#530](https://github.com/vllm-project/aibrix/pull/530) - [Doc] Update aibrix documentation by
[@Jeffwan](https://github.com/Jeffwan)in[#533](https://github.com/vllm-project/aibrix/pull/533) - Refactor the gateway-plugin and metadata service manifests by
[@Jeffwan](https://github.com/Jeffwan)in[#531](https://github.com/vllm-project/aibrix/pull/531) - Fix the GITHUB_WORKSPACE artifact sharing issue in release workflow by
[@Jeffwan](https://github.com/Jeffwan)in[#532](https://github.com/vllm-project/aibrix/pull/532) - [Misc] Polish the benchmark scripts by
[@Jeffwan](https://github.com/Jeffwan)in[#525](https://github.com/vllm-project/aibrix/pull/525) - Fix APA bugs in creation, add test and demo yaml by
[@kr11](https://github.com/kr11)in[#536](https://github.com/vllm-project/aibrix/pull/536) - Add VKE IPv4 Testing Cluster Config by
[@nwangfw](https://github.com/nwangfw)in[#537](https://github.com/vllm-project/aibrix/pull/537) - Support for request length internal trace by
[@happyandslow](https://github.com/happyandslow)in[#538](https://github.com/vllm-project/aibrix/pull/538) - [Feat] Add download status into runtime downloader by
[@brosoul](https://github.com/brosoul)in[#539](https://github.com/vllm-project/aibrix/pull/539) - [Feat] Add runtime model management api by
[@brosoul](https://github.com/brosoul)in[#540](https://github.com/vllm-project/aibrix/pull/540) - [gateway] handle the wrong model name and cache inconsistency case by
[@Jeffwan](https://github.com/Jeffwan)in[#542](https://github.com/vllm-project/aibrix/pull/542) - [Docs] fix: update the parameters instruction in readme by
[@scarlet25151](https://github.com/scarlet25151)in[#548](https://github.com/vllm-project/aibrix/pull/548) - add lora schedulers - bin pack, least latency, least throughput, random by
[@Aspirin96](https://github.com/Aspirin96)in[#544](https://github.com/vllm-project/aibrix/pull/544) - add request routers - least kv cache, least expected latency by
[@Aspirin96](https://github.com/Aspirin96)in[#543](https://github.com/vllm-project/aibrix/pull/543) - [Docs] heterogenous gpu docs added by ...

[Read more](https://github.com/vllm-project/aibrix/releases/tag/v0.2.0)