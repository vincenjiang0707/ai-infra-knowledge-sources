# Amazon SageMaker Inference: 2026 year-to-date launches in review

source: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-inference-2026-year-to-date-launches-in-review/
published: Fri, 18 Sep 2026 20:52:14 +0000

[Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Amazon SageMaker Inference: 2026 year-to-date launches in review

Generative AI inference is uniquely hard: models are tens to hundreds of gigabytes, latency requirements are measured in tokens per second, cold starts can span multiple minutes as containers and weights transfer, GPU capacity is constrained, and traditional monitoring tools expose none of the token-level signals that matter in production.

Amazon SageMaker AI offers customers the ability to deploy AI models and consume them by the instance (instead of by the token), using two paths: managed endpoints for teams that want AWS to handle infrastructure and operations, and Amazon SageMaker HyperPod Inference for teams that need Kubernetes-native control over dedicated GPU clusters. Year-to-date in 2026, SageMaker AI delivered 13 new capabilities across these two paths and this post walks through these capabilities and benefits to enterprises, startups and public sector.

## Choose the deployment that fits your workload

The table below compares the two deployment paths across seven dimensions.

Dimension |
Endpoints |
HyperPod |
Infrastructure |
Fully managed by AWS | Managed Kubernetes stack |
Deploy target |
Console, SDK, CLI | kubectl, Terraform, Console, CLI, SDK |
Scaling |
Managed auto scaling with Amazon CloudWatch | Auto scaling with Karpenter, KEDA, CloudWatch |
Customization and Control |
Customizable at the container and model layers | More customizability with Node level access, frameworks and AMI. |
API protocol |
OpenAI compatible with SageMaker endpoint | HTTP, gRPC and custom load balancer capability |
Best for |
Fast and fully managed deployment with minimal ops overhead | Kubernetes-based, train-to-serve multi-cloud/hybrid-cloud deployments |
Corresponding Launches: |
||
Launches |
Inference recommendations, Capacity Aware Inference, OpenAI API, Container Caching, Observability, Async Inference Inline Payloads, Prefix-Aware Routing | Simplified Operator, Tiered KV Cache, Data Capture, Performance Features, Disaggregated Prefill and Decode for HyperPod Inference, Model Caching |

## SageMaker AI endpoints: From model to production in hours

Managed SageMaker Inference endpoints are the faster path for teams that want AWS to handle GPU provisioning, scaling, and operational monitoring. You bring the model and define the performance target. SageMaker handles the rest. The seven launches year-to-date in 2026 below address deployment, capacity, integration, scaling, observability, and async simplification.

### Inference recommendations and benchmarking (April 2026)

Blog: [Amazon SageMaker AI now supports optimized generative AI inference recommendations](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-now-supports-optimized-generative-ai-inference-recommendations/)

Choosing the right instance type, serving container, and optimization settings for a generative AI model typically takes two to three weeks of manual benchmarking against 1000+ combinations, requiring expertise most teams do not have in-house. Inference recommendations automate this end-to-end.

Customers specify a model and performance goal (cost, latency, or throughput). SageMaker then runs a three-step process:

**Narrow.**Filter the instance type space by analyzing model architecture, size, and memory requirements.**Optimize.**Apply goal-aligned techniques: EAGLE 3.0 speculative decoding for throughput, kernel tuning for latency, tensor parallelism based on model size.**Benchmark.**Run NVIDIA AIPerf on real GPU infrastructure with statistically rigorous multi-run confidence reporting.

The output is a SageMaker Model Package with deployment-ready configurations and validated metrics: time to first token (TTFT), inter-token latency (ITL), P50/P90/P99 latency percentiles, throughput, and cost projection. In a demonstrated example, throughput optimization on `GPT-OSS-20B`

delivered 2x tokens per second at the same request latency. There is no additional cost for generating recommendations. Customers with ML Reservations can benchmark on reserved capacity at no extra charge, and inference recommender can also be used to evaluate alternative instance types.

### Capacity-aware instance pools (May 2026)

Blog: [Capacity-aware inference: automatic instance fallback for SageMaker AI endpoints](https://aws.amazon.com/blogs/machine-learning/capacity-aware-inference-automatic-instance-fallback-for-sagemaker-ai-endpoints/)

When a SageMaker endpoint required a single instance type, a capacity shortage meant the endpoint failed before serving a single request. Instance pools address that single point of failure.

Customers define a prioritized list of up to five instance types. SageMaker automatically works through the list at endpoint creation, during scale-out, and during scale-in. At creation, SageMaker tries the first-choice type and falls back immediately if capacity is unavailable. During scale-out, the next available type in the priority list absorbs demand. During scale-in, fallback instances are removed first, so the fleet trends back toward preferred hardware as capacity opens up.

Per-instance-type CloudWatch metric dimensions enable weighted scaling policies for heterogeneous fleets. Each pool entry can reference a separate optimized model configuration (tensor parallelism on high-memory instances, speculative decoding on mid-tier, quantization on smaller fallbacks), and inference recommendations can generate these per-hardware configurations automatically. Supported for single-model, inference component, and async endpoints in all commercial AWS Regions.

### OpenAI-compatible APIs (May 2026)

Blog: [Announcing OpenAI-compatible API support for Amazon SageMaker AI endpoints](https://aws.amazon.com/blogs/machine-learning/announcing-openai-compatible-api-support-for-amazon-sagemaker-ai-endpoints/)

Applications built on the OpenAI SDK, LangChain, or Strands Agents previously required custom client adapters and authentication rewrites to work with SageMaker-hosted models. That migration cost was a real barrier.

SageMaker endpoints now expose an /openai/v1 path supporting Chat Completions with streaming. Migration requires changing only the endpoint URL. SDK calls, streaming logic, and prompt formatting remain identical. Authentication uses bearer tokens generated from existing AWS credentials, valid for up to 12 hours, removing SigV4 signing complexity.

Multi-model endpoints allow hosting multiple models, each callable through the same OpenAI SDK with independent resource allocation. For agentic workloads, AI agents can run entirely on customer-owned GPU infrastructure using the same OpenAI-compatible interface they were built on. Available in 14 AWS Regions, with support for vLLM and SGLang AWS Deep Learning Containers and custom containers implementing the /v1/chat/completions path.

### Container caching (June 2026)

Blog: [Introducing container caching in Amazon SageMaker AI for faster model scaling](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling/)

During inference auto scaling events, new instances responding to traffic spikes previously had to pull the full container image from Amazon Elastic Container Registry (Amazon ECR) before serving requests. For large serving containers exceeding 10 GB, that pull alone added several minutes of dead time to every scale-out event.

Container caching pre-pulls images automatically, so new instances launch with the container already available locally. Zero configuration, no code changes, no container modifications. It activates automatically on supported accelerator instance types. With Qwen3-8B on ml.g6.2xlarge using the LMI container (17.7 GB compressed), end-to-end startup latency dropped from 525 seconds to 258 seconds, a 51% reduction. Model download time also improved, from 168 seconds to 77 seconds, because the image is no longer competing for network bandwidth. Early access customers observed improvements ranging from 38% to 65%.

Container caching is the third layer in a three-part scaling optimization suite:

Layer |
Optimization |
Impact |
Detection |
Sub-minute CloudWatch metrics | Triggers scale-up 6x faster than standard 1-minute metrics |
Existing instances |
Instance-store data caching | Removes image pull and model download for instances already running |
New instances |
Container image caching | Avoids image pull time; 51% startup latency reduction demonstrated |

### Inference observability and CloudWatch Insights dashboard (June 2026)

Token-level latency, KV cache pressure, GPU memory trends, and inference component placement across Availability Zones are signals that scattered CloudWatch metrics could not surface together, forcing teams to correlate problems manually after users had already been affected.

SageMaker now emits 100+ detailed inference metrics via native OpenTelemetry, paired with a pre-built Insights dashboard in Amazon CloudWatch. Zero instrumentation required. New endpoints have observability enabled by default, with metrics flowing within two minutes of reaching InService status. The dashboard covers three areas:

**Performance.**Time to first token (TTFT), inter-token latency (ITL), throughput, model latency vs. system overhead, KV cache utilization, and queue depth.**Capacity.**GPU utilization, memory, temperature, and disk across the fleet, with honeycomb visualizations for at-a-glance instance health.**Reliability.**Availability Zone distribution with risk scoring, cold start anatomy (model download, GPU load, container start phases), and scaling event history.

A PromQL-compatible endpoint lets teams query SageMaker metrics directly from Amazon Managed Grafana or a PromQL-compatible tool via SigV4 authentication.

### Async inference inline payloads (June 2026)

Blog: [Amazon SageMaker AI async inference now supports inline request payloads](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-async-inference-now-supports-inline-request-payloads/)

Async inference previously required uploading every input payload to Amazon Simple Storage Service (Amazon S3) before invoking the endpoint, even for a simple JSON prompt of a few hundred bytes, adding architecture complexity and latency on every request.

The InvokeEndpointAsync API now accepts a Body parameter with payloads up to 128,000 bytes directly in the request, removing the S3 pre-staging step for the vast majority of async workloads. Key benefits: one fewer network round-trip per request, no input bucket provisioning or IAM s3:PutObject grants, immediate size and parameter validation, and avoidance of the S3 PUT charge per invocation. Fully backward compatible. Existing InputLocation workflows continue unchanged. Available in 31 AWS Regions.

### Prefix-aware routing

Resource: [Reduce LLM latency with prefix-aware routing on Amazon SageMaker Inference](https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/)

A new routing strategy that reduces LLM latency by directing requests with shared prompt prefixes to the same instance. In many LLM applications, a large portion of the prompt (system instructions, retrieved documents, conversation history) is repeated across requests. Normally, each instance recomputes these shared tokens from scratch, wasting GPU resources.

Prefix-aware routing solves this by using the beginning of each request as a fingerprint to consistently route similar prompts to the same instance, maximizing KV cache reuse. It includes built-in safeguards for overload protection and stable behavior during scaling events.

Benchmarks on Llama 3.1 70B across 7 instances showed significant gains: for long-context workloads (8,000-token prefixes), P90 TTFT dropped by 33–37%, P50 TTFT by 71–77%, and KV cache hit rates jumped from ~25% to 82%. Short-context workloads also improved, with P90 TTFT reduced by 24–37%. The routing overhead is minimal, adding only 1.3–1.9 milliseconds per request.

SageMaker now offers three routing strategies: RANDOM (default), LEAST_OUTSTANDING_REQUESTS, and the new PREFIX_AWARE. The feature is ideal for RAG applications, multi-turn conversations, templated bots, and code completion scenarios.

Enabling it requires only setting RoutingStrategy, PrefixLength, and ConcurrencyThreshold in the endpoint configuration. No changes to model containers or serving frameworks are needed. It also supports multi-tenant prefix isolation, inference components, and dynamic LoRA adapters. The feature is available today on SageMaker real-time inference endpoints.

## HyperPod Inference: Production-grade inference on your Kubernetes clusters

HyperPod Inference extends HyperPod’s cluster resilience into the serving layer for teams who need Kubernetes-native control. It is built for practitioners who want to own their GPU infrastructure while still getting AWS-managed reliability on top. The six launches year-to-date in 2026 below address deployment, latency, compliance, and compute specialization.

### Simplified Inference Operator on EKS (April 2026)

Blogs: [Unlock efficient model deployment: Simplified Inference Operator setup on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/architecture/unlock-efficient-model-deployment-simplified-inference-operator-setup-on-amazon-sagemaker-hyperpod/) | [Best practices to run inference on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/best-practices-to-run-inference-on-amazon-sagemaker-hyperpod/)

Deploying an LLM on Kubernetes typically requires writing and maintaining Deployments, Services, ConfigMaps, HorizontalPodAutoscaler configs, and health check wiring for each model. For teams managing dozens of models, that handcrafted infrastructure becomes an engineering burden in itself.

The Simplified Inference Operator is a native EKS add-on that installs in a single step through the AWS console, CLI, SDK, kubectl, or Terraform. Once installed, teams deploy models by submitting a single custom resource definition instead of a stack of low-level Kubernetes objects. Key capabilities include:

**Multi-instance type fallback.**Priority-ordered instance list. The operator tries each in sequence, so models reach serving status without manual intervention.**Built-in autoscaling.**Native integration with CloudWatch, Amazon Managed Service for Prometheus, and KEDA for event-driven scaling.**EKS add-on lifecycle.**AWS manages version upgrades, compatibility checks, and health monitoring as part of the cluster lifecycle.**JumpStart integration.**Deploy popular foundation models directly from SageMaker JumpStart through the same operator interface.

### Managed tiered KV cache and intelligent routing

Blog: [Managed tiered KV cache and intelligent routing for Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/managed-tiered-kv-cache-and-intelligent-routing-for-amazon-sagemaker-hyperpod/)

For long-context and multi-turn workloads, LLMs recompute key-value attention values for shared prefixes on every request. Without caching, that redundant computation accumulates directly as latency and GPU cost.

HyperPod Inference manages a two-tier KV cache. The L1 tier lives in CPU memory on each node for low-latency local reuse. The L2 tier uses Redis for cross-node sharing, so a cached prefix computed by one model pod can be reused by other pods in the fleet. Intelligent routing keeps the cache effective by directing requests to the right instances:

**Prefix-aware routing.**Routes requests with shared system prompts or document prefixes to instances most likely to have a cache hit.**KV-aware routing.**Use real-time cache state to route to instances with highest cache occupancy for the incoming request.**Round-robin.**Standard load distribution for workloads where cache reuse is not a priority.

Together, tiered caching and intelligent routing deliver up to 40% latency reduction for long-context and multi-turn workloads compared to a non-cached baseline.

### Data capture (May 2026)

Resources: [Amazon SageMaker HyperPod data capture for inference workloads (What’s New)](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-sagemaker-hyperpod-data-capture) | [Enhancing enterprise inference on HyperPod with data capture, Hugging Face, NVMe, and Route 53 integration](https://aws.amazon.com/blogs/machine-learning/enhancing-enterprise-inference-on-amazon-sagemaker-hyperpod-with-data-capture-hugging-face-nvme-and-route-53-integration/)

Regulated enterprises need tamper-evident logs of inference activity for compliance, drift monitoring, and offline evaluation dataset construction. Building that logging infrastructure across multiple request paths from scratch is non-trivial.

HyperPod Inference data capture provides three capture points enabled via the custom resource definition (CRD): the SageMaker endpoint (full request and response at the application boundary), the ALB (load balancer traffic for routing visibility and latency measurement), and the model pod (request and response at the container boundary for model-level debugging). Captured data flows to Amazon S3 with no custom sidecar containers or application instrumentation required. Teams can enable capture selectively at any of the three points to keep storage costs proportional to actual needs.

### Disaggregated prefill and decode (July 2026)

Resources: [Disaggregated prefill and decode for LLM inference on SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/disaggregated-prefill-and-decode-for-llm-inference-on-sagemaker-hyperpod/) | [Amazon SageMaker HyperPod now supports disaggregated prefill and decode (What’s New)](https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-sagemaker-hyperpod-dpd/)

When prefill and decode share the same GPU pool, a long prefill for a complex prompt blocks token generation for every concurrent user in the queue. Under mixed traffic, this makes per-token latency unpredictable in proportion to request complexity.

Disaggregated Prefill and Decode (DPD), shipped in Inference Operator v3.2, separates these phases onto distinct GPU pools. Prefill GPUs handle prompt processing. Once the KV cache for a request is ready, it transfers to the decode pool over EFA using GPU-Direct RDMA, a direct memory transfer that bypasses the CPU entirely. Decode GPUs then generate output tokens without interference from incoming prefill work. Each pool scales independently: if prefill throughput is the bottleneck, more prefill GPUs can be added without touching the decode fleet.

Validated on Llama 3.3 70B under mixed traffic, DPD produced measurably more consistent TTFT and ITL distributions compared to colocated prefill and decode. Operators specify separate instance pools for prefill and decode nodes in the custom resource definition. The Inference Operator manages EFA configuration and KV cache transfer automatically.

### Performance features with Hugging Face, NVMe, and Route 53 (July 2026)

Amazon SageMaker HyperPod introduces new capabilities that enhance deployment flexibility, performance, and security for enterprise generative AI inference. Hugging Face Hub Integration lets you deploy models directly without pre-staging weights to S3, with support for gated models, revision pinning, and token isolation across vLLM, TGI, and SGLang runtimes. Local NVMe Model Loading reduces cold-start latency by reading weights from node-local storage instead of pulling over the network—ideal for autoscaling and scale-from-zero scenarios. When NVMe isn’t available, automatic fallback to cloud storage facilitates reliability. Amazon Route 53 DNS Management automatically creates, updates, and cleans up DNS records for custom inference domains through simple CRD configuration. Custom Service Accounts with IRSA provide pod-level IAM permissions, giving infrastructure teams fine-grained control over security boundaries. Together, these features help teams deploy AI applications faster without compromising governance or operational visibility.

### Amazon SageMaker HyperPod with model caching

Resources: [Reduce inference cold starts on Amazon SageMaker HyperPod with model caching](https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching/)

When deploying large language models on Amazon SageMaker HyperPod, cold starts create significant delays as pods must download model weights from remote storage and pull container images from Amazon ECR before serving requests. This problem compounds during scale-out events when multiple pods start simultaneously.

SageMaker HyperPod now offers **model caching**, which addresses this through two complementary mechanisms. The **weights cache** pre-downloads model weights to local NVMe storage on each node, enabling reads at approximately 7 GB/s instead of waiting for remote downloads. The **image cache** pre-pulls inference container images onto nodes via a DaemonSet, saving 5 to 7 minutes per pod start. Both caches use preferred (not required) scheduling, so pods can still start on uncached nodes with a graceful fallback.

The feature is managed through two Custom Resource Definitions (CRDs): **ModelDataCacheConfig** for weights and **ModelImageCache** for container images. The operator handles the full lifecycle automatically, including cache invalidation when model sources change.

Enabling caching requires adding a modelCacheConfig section to your existing **InferenceEndpointConfig** or **JumpStartModel** resource, with toggles for weights and image caching independently. It supports most model sources including Amazon S3, Amazon FSx for Lustre, and Hugging Face Hub.

Benchmarks show **around 60% faster scale-out** for models ranging from 57 GB to 145 GB. Key limitations include per-node storage (each node maintains its own copy), NVMe capacity constraints, and the fact that source updates at the same path are not auto-detected. Cleanup is automatic when you delete the parent resource. The feature is now generally available in all supported HyperPod regions.

## The compound value: 13 launches across the inference stack

Our feature launches focus on reducing time-to-market, letting customers use state-of-the-art capabilities out of the box with strong price-performance. Each of these launches addresses a distinct friction point across the inference lifecycle, from first deployment decision to production operations:

**Inference Recommendations (April 2026).**Automates instance selection, optimization, and benchmarking. Cuts weeks of manual work to hours.**Capacity-Aware Instance Pools (May 2026).**Up to five instance types with automatic fallback at creation, scale-out, and scale-in. No manual retry cycles.**OpenAI-Compatible APIs (May 2026).**SageMaker endpoints become a drop-in backend for OpenAI SDK, LangChain, or Strands Agents applications.**Container Caching (June 2026).**51% startup latency reduction demonstrated. Zero configuration. Activates automatically on supported instances.**Inference Observability Dashboard (June 2026).**100+ metrics via OpenTelemetry in a pre-built CloudWatch dashboard covering performance, capacity, and reliability.**Async Inference Inline Payloads (June 2026).**128 KB inline body parameter avoids mandatory S3 pre-staging for async workloads. Available in 31 Regions.**Simplified Inference Operator on EKS (April 2026).**Single EKS add-on install. Full lifecycle management. Multi-instance fallback and built-in autoscaling via CloudWatch, Amazon Managed Service for Prometheus, and KEDA.**Managed Tiered KV Cache and Intelligent Routing.**L1 (CPU memory) and L2 (Redis) caching with prefix-aware and KV-aware routing. Up to 40% latency reduction.**Data Capture (May 2026).**Three capture points (endpoint, ALB, model pod) enabled via CRD. Compliance-ready logging to S3 with no custom infrastructure.**Disaggregated Prefill and Decode (July 2026).**Separate GPU pools for prefill and decode. KV cache transfer over EFA/GPU-Direct RDMA. Predictable ITL under concurrent load on Llama 3.3 70B.**Performance Features (July 2026)**: Enhancing enterprise inference on Amazon SageMaker HyperPod with data capture, Hugging Face, NVMe, and Route 53 integration.**Amazon SageMaker HyperPod with model caching**(Sep 2026): Pre-load model weights and container images on local NVMe to cut cold start times by up to 60% on SageMaker HyperPod.**Prefix-Aware Routing**(Sep 2026): Route repeated prompt prefixes to the same instance to maximize KV cache reuse, cut time-to-first-token by up to 77%, and boost throughput across your SageMaker fleet.

From deployment to scaling to operations, these launches cover every layer of the inference stack, across both managed endpoints and Kubernetes-native clusters. Competitive advantage in AI inference increasingly comes not from choosing the best model, but from operating the most efficient inference stack. Using the capabilities described in this post does not require a team of AI infrastructure experts or researchers. The AWS Experience-Based Acceleration program brings these capabilities to enterprises and startups to help them configure and optimize instance-based AI inference. It works by understanding your inference workloads, data modalities, SLAs, and cost targets, running benchmark evaluations, and configuring your inference stack to run AI inference at scale.

## What is next

Investment continues across both managed endpoints and HyperPod Inference in 2026. On the managed endpoint side, the focus is deeper in AWS AI landscape integration. On the HyperPod Inference side, the roadmap includes additional routing strategies, broader model serving framework support, and expanded multi-region networking capabilities. Documentation and getting-started guides for all capabilities covered here are available in the [Amazon SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html). Start deploying.

## References

[Optimized Generative AI Inference Recommendations](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-now-supports-optimized-generative-ai-inference-recommendations/)[Capacity-Aware Inference: Automatic Instance Fallback for SageMaker AI Endpoints](https://aws.amazon.com/blogs/machine-learning/capacity-aware-inference-automatic-instance-fallback-for-sagemaker-ai-endpoints/)[Announcing OpenAI-Compatible API Support for Amazon SageMaker AI Endpoints](https://aws.amazon.com/blogs/machine-learning/announcing-openai-compatible-api-support-for-amazon-sagemaker-ai-endpoints/)[Introducing Container Caching in Amazon SageMaker AI for Faster Model Scaling](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling/)[Monitor and Debug Generative AI Inference with SageMaker Detailed Metrics and Insights Dashboard on CloudWatch](https://aws.amazon.com/blogs/machine-learning/monitor-and-debug-generative-ai-inference-with-sagemaker-detailed-metrics-and-insights-dashboard-on-cloudwatch/)[Amazon SageMaker AI Async Inference Now Supports Inline Request Payloads](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-async-inference-now-supports-inline-request-payloads/)[Unlock Efficient Model Deployment: Simplified Inference Operator Setup on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/architecture/unlock-efficient-model-deployment-simplified-inference-operator-setup-on-amazon-sagemaker-hyperpod/)[Best Practices to Run Inference on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/best-practices-to-run-inference-on-amazon-sagemaker-hyperpod/)[Managed Tiered KV Cache and Intelligent Routing for Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/managed-tiered-kv-cache-and-intelligent-routing-for-amazon-sagemaker-hyperpod/)[Amazon SageMaker HyperPod Data Capture for Inference Workloads (What’s New)](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-sagemaker-hyperpod-data-capture)[Enhancing Enterprise Inference on Amazon SageMaker HyperPod with Data Capture, Hugging Face, NVMe, and Route 53 Integration](https://aws.amazon.com/blogs/machine-learning/enhancing-enterprise-inference-on-amazon-sagemaker-hyperpod-with-data-capture-hugging-face-nvme-and-route-53-integration/)[Disaggregated Prefill and Decode for LLM Inference on SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/disaggregated-prefill-and-decode-for-llm-inference-on-sagemaker-hyperpod/)[Amazon SageMaker HyperPod Now Supports Disaggregated Prefill and Decode (What’s New)](https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-sagemaker-hyperpod-dpd/)[Reduce inference cold starts on Amazon SageMaker HyperPod with model caching](https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching/)[Reduce LLM latency with prefix-aware routing on Amazon SageMaker Inference](https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/)