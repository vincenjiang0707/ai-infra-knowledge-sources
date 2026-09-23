# Introducing Amazon SageMaker HyperPod Inference Gateway

source: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-inference-gateway/
published: Fri, 18 Sep 2026 13:08:34 +0000

[Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Introducing Amazon SageMaker HyperPod Inference Gateway

Eliminate GPU waste. Reduce first-token latency by up to 82%. Install one Kubernetes-native addon with zero application changes.

## The problem: Naive routing wastes your most expensive resource

Running large language models (LLMs) at scale on GPU clusters is expensive. The default Kubernetes load balancers are making it worse. Round-robin and least-connections algorithms have no visibility into what’s happening inside your GPUs: which pods have saturated KV caches, which are mid-way through long-context generations, or which already have the LoRA adapter your request needs loaded in memory.

*The result? Round-robin routing causes requests to pile up behind busy pods while idle capacity remains unused.* First-token latency spikes to 4+ seconds during traffic bursts. GPU utilization becomes uneven and unpredictable. You over-provision to compensate. This burns money on GPUs that aren’t doing useful work.

## The solution: SageMaker HyperPod Inference Gateway

Today, we’re excited to announce Amazon SageMaker HyperPod Inference Gateway. It is a Kubernetes-native, GPU-aware routing system that deploys as a single EKS managed addon on your existing HyperPod infrastructure. It uses real-time GPU signals to place every inference request on the best-suited pod, delivering lower latency with no changes to your model servers or client applications.

*“A chatbot user waiting 4.4 seconds for the first token now sees it in under 800 ms.”*

## How it works: Two-tier architecture

The Inference Gateway uses a two-tier design built entirely on Kubernetes-native primitives.

### Tier 1 — Per-cluster gateway (EKS managed addon)

The first tier installs directly on each HyperPod/EKS cluster as the amazon-sagemaker-hyperpod-inference addon. It consists of three core components, all built on the open-source Gateway API Inference Extension:

#### 1. Envoy Gateway

High-performance L7 proxy that terminates incoming HTTPS traffic and exposes a single private endpoint per cluster.

#### 2. Body-Based Router (BBR)

Inspects each incoming OpenAI-compatible request body, extracts the model field, and routes to the correct model pool. Supports multi-model routing: one gateway, many models.

#### 3. Endpoint Picker (EPP)

The intelligence layer. EPP consumes real-time Prometheus metrics from every model-serving pod and uses a weighted scoring algorithm to select the best-suited backend:

**KV cache utilization —**avoids pods whose key-value memory is nearly full.**Queue depth —**avoids pods with deep request backlogs.**LoRA adapter residency —**prefers pods that already have the requested adapter loaded.**Prefix cache hit rate —**prefers pods likely to serve from cached prompt prefixes.**Running requests —**balances active work across the fleet.

Each scorer carries a configurable weight, so you can tune routing behavior for your specific workload (latency-sensitive chat compared to throughput-optimized batch).

### Tier 2 — Global Inference Router (GIR) (coming soon)

The second tier adds fleet-wide coordination across multiple clusters and regions, with cross-cluster failover, global rate limiting, and cost-aware traffic shaping. Tier 2 builds on top of Tier 1. Each cluster’s per-cluster gateway continues to handle local intelligent routing.

## Getting started in 5 minutes

The Inference Gateway deploys with a single addon install and a declarative InferenceGatewayConfig custom resource. No sidecars, no service mesh, no application code changes.

### Step 1: Install the addon

### Step 2: Label your model pods

Add a label to your existing model server deployments so the gateway can discover them:

### Step 3: Apply the gateway configuration

Create a single InferenceGatewayConfig resource that defines your models and routing behavior:

### Step 4: Send inference requests

The gateway exposes a standard OpenAI-compatible endpoint. Your existing client code works unchanged:

That’s it. No SDK changes. No SigV4 signing for inference traffic. Standard HTTP with an OpenAI-compatible schema.

## Multi-model routing

Running multiple models on the same cluster? The Body-Based Router handles it natively. Define multiple schedulers in your config, and the gateway automatically routes each request to the correct model pool based on the model field in the request body.

One gateway. Multiple models. Zero routing logic in your application.

## LoRA adapter routing

Serving fine-tuned LoRA adapters on a shared base model? The Inference Gateway routes adapter requests to pods that already have the adapter loaded in GPU memory. This eliminates costly adapter swap latency.

The EPP’s LoRA Affinity Scorer identifies which pods have the requested adapter resident and routes accordingly. If no pod has it loaded, the request goes to the pod with the most available capacity to load it quickly.

## Graceful failure and self-healing

The gateway degrades gracefully at every level:

Failure Scope |
Behavior |
Recovery |
Pod failure |
EPP excludes pods with stale metrics. Routes to healthy pods | Automatic when metrics resume |
Pool exhaustion |
Returns HTTP 429 with Retry-After header | Autoscaling adds capacity |
Cluster failure |
GIR detects stale heartbeat, redirects traffic within 35s | Gradual ramp-up on reintroduction |
Regional failure |
Cross-region routing activates automatically | Higher latency, no availability impact |

## Built-in observability

The gateway emits metrics at every layer, all surfaced through your existing monitoring stack:

**Pod level —**KV cache utilization, queue depth, running requests, adapter residency (Prometheus).**Pool level —**Request totals, duration histograms, token counts (Prometheus/Grafana).**Cluster level —**Average KV cache, error rate, P99 latency (Amazon CloudWatch).**Fleet level —**Routing decisions, failover events, rate limit hits (CloudWatch).

## Benchmarking

How much performance are you leaving on the table with default Kubernetes routing? To find out, we benchmarked four models ranging from 8B to 235B parameters, deployed on p5.48xlarge (H100) and g5 (A10G) instances. All traffic was routed through internal Application Load Balancers, matching the exact path a production request travels. A dedicated client node group generated controlled load while model servers ran in isolation on a separate server node group, ensuring zero resource contention under high concurrency. Every result that follows uses the gateway’s default routing configuration, with no tuning required.

GPU-aware routing delivers the biggest gains exactly where round-robin struggles most. We tested three real-world scenarios across four models (8B to 235B parameters).

### Mixed GPU generations

In production, GPU fleets are rarely uniform. When a smaller-memory instance saturates under traffic that its larger peers handle comfortably, round-robin keeps sending requests to overloaded pods. The Inference Gateway detects this imbalance in real time.

### Bursty traffic

Bursty demand is the norm for most LLM workloads. A single replica cycles between overloaded and idle, creating latency spikes that round-robin cannot smooth out. The gateway absorbs these bursts by steering requests toward pods with available capacity.

### Shared prompt prefixes

Workloads like multi-turn conversations and document Q&A share a common prompt prefix across requests. The gateway’s Prefix Cache Hit Rate scorer routes these requests to pods that already have the prefix cached, avoiding redundant computation.

The pattern across all three scenarios is consistent: the more your fleet diverges from uniform, the more you gain. On a fully uniform fleet under steady traffic, replicas hold near-identical utilization, and the gateway performs on par with round-robin. This makes intelligent routing most valuable for the conditions production traffic actually creates: mixed hardware, bursty demand, and shared prompt prefixes. You can turn it on without hand-tuning anything first.

### Summary of performance improvements

All figures are measured against a Kubernetes round-robin baseline on the same model replicas, using the gateway’s default routing configuration.

Workload Condition |
TTFT P95 |
TTFT P99 |
Throughput |
| Mixed GPU generations (Llama-3.1-8B) | –97% | –97% | +8% |
| Mixed GPU generations (Qwen3-32B) | –98% | –97% | +50% |
| Bursty traffic (Llama-3.1-70B) | –94% | –98% | +12% |
| Bursty traffic (Qwen3-235B) | Comparable | –89% | Comparable |
| Shared prompt prefix (Llama-3.1-8B) | –26% | –43% | Comparable |
| Uniform fleet, steady traffic (Qwen3-235B) | Comparable | Comparable | Comparable |

*“Comparable” means the difference fell within run-to-run variance.*

## Why Kubernetes-native matters

The Inference Gateway is not a separate platform you deploy alongside Kubernetes. It is Kubernetes:

**Gateway API conformant —**built on the official Kubernetes Gateway API and its Inference Extension.**Declarative config —**one CRD (InferenceGatewayConfig) defines your entire routing topology.**No lock-in —**works with any OpenAI-compatible model server (vLLM, SGLang, TGI, and so on).**Existing tooling —**kubectl, GitOps, Helm, ArgoCD — all work as expected.**EKS addon lifecycle —**install, upgrade, and rollback through the aws eks CLI or console.

## Availability

SageMaker HyperPod Inference Gateway (Tier 1, per-cluster routing) is available today in regions where inference add-on is available.

## What’s next

**Tier 2: Global Inference Router (GIR) —**Cross-cluster and cross-region intelligent routing with a centralized fleet gateway, global rate limiting, and cost-tier-aware traffic shaping.**Canary traffic splitting —**Route a percentage of traffic to new model versions using InferenceModelRewrite CRDs.**Flow control and priority bands —**Classify requests as Critical, Standard, or Sheddable with per-band admission control.

Ready to stop wasting GPU capacity on naive routing? Install the Inference Gateway addon and start seeing first-token latency improvements in minutes rather than weeks.