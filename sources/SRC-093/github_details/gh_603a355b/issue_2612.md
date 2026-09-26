# [Issue #2612] [Proposal] Make StormService the unified abstraction for distributed inference workloads

source: https://github.com/vllm-project/aibrix/issues/2612
state: open | updated: 2026-08-28T12:55:22Z
labels: 

## 正文

### 🚀 Feature Description and Motivation

Currently, AIBrix uses `StormService` as the inference workload abstraction, while distributed inference workloads may additionally require `RayClusterFleet` to provide the underlying distributed execution environment.

This separation provides a clear boundary between inference lifecycle management and distributed runtime management. However, it also exposes runtime implementation details to users who only want to deploy and operate LLM inference services.

For GenAI inference workloads, users typically think in terms of:

- Model to deploy
- Inference engine (vLLM/SGLang)
- Parallelism strategy (TP/PP/EP)
- GPU resources
- Replica count

They usually do not need to understand whether the underlying distributed execution is implemented through RayClusterFleet, Kubernetes primitives, or other runtime frameworks.

This proposal suggests making `StormService` the primary user-facing inference abstraction while allowing AIBrix to manage the lifecycle of underlying distributed runtime resources such as `RayClusterFleet`.

This proposal does **not** require removing `RayClusterFleet`. Instead, `RayClusterFleet` can remain an internal implementation resource managed by AIBrix controllers.

### Use Case

For large-scale LLM inference workloads, distributed execution is commonly required.

For example, deploying a model with:

- Model: DeepSeek/Qwen/Llama
- Engine: vLLM
- Tensor Parallel Size: TP=16
- Replicas: 2
- GPU requirement: 16 GPUs per replica

The user's intention is simply:

> Deploy a distributed inference service with TP=16.

However, the current workflow requires users to understand and manage multiple resources:

```
StormService
      +
RayClusterFleet
```

Users need to understand:

- When RayClusterFleet should be created
- How RayClusterFleet relates to StormService
- How lifecycle management is coordinated
- How failures and upgrades propagate between these resources

This becomes especially challenging for:

- Multi-node tensor parallel inference
- Pipeline parallel inference
- Expert parallel inference for MoE models
- Production LLM serving platforms

### Proposed Solution

Introduce a unified distributed inference abstraction inside `StormService`.

Example:

```yaml
apiVersion: serving.aibrix.io/v1alpha1
kind: StormService

spec:
  model:
    name: deepseek-model

  runtime:
    engine: vllm

  parallelism:
    tensorParallelSize: 16

  resources:
    gpu: 16

  replicas: 2
```

The `StormService` controller manages the underlying runtime resources:

```
StormService

      |
      |
      +---- RayClusterFleet

              |
              |
              +---- RayCluster

                      |
                      |
                      +---- Worker Pods
```

Advanced users may still access lower-level runtime resources if needed, but the default user experience should only require `StormService`.

---

## Benefits

### 1. Unified User Experience

Users can deploy both single-node and distributed inference workloads through the same abstraction.

Example:

Single node:

```
StormService
```

Multi-node:

```
StormService
      |
      +-- RayClusterFleet
```

---

### 2. Runtime Abstraction

`StormService` becomes independent from a specific distributed execution framework.

Future implementations could support:

```
StormService

    |
    +-- Ray backend

    |
    +-- Kubernetes native backend

    |
    +-- Other distributed runtime
```

---

### 3. Easier Platform Integration

Higher-level GenAI inference platforms can integrate with AIBrix through a single inference API without exposing runtime implementation details.

---

## Open Questions

- Should RayClusterFleet lifecycle management be fully handled by the StormService controller?
- Should direct RayClusterFleet creation remain supported for advanced users?
- Should this behavior be enabled by default or through an optional configuration?
- How should existing StormService + RayClusterFleet deployments migrate?

---

## Alternatives Considered

### Option 1: Keep current resource model

Pros:

- Clear separation between inference and runtime layers
- Reuses existing KubeRay abstractions

Cons:

- Requires users to understand multiple abstractions
- Exposes runtime implementation details
- Increases operational complexity for inference users

---

### Option 2: Introduce a new higher-level CRD

Example:

```
InferenceService

    |
    +-- StormService

    |
    +-- RayClusterFleet
```

Pros:

- Keeps existing resources unchanged

Cons:

- Adds another abstraction layer
- Increases API complexity

---

## Proposal Summary

The goal is not to remove `RayClusterFleet`, but to make `StormService` the unified inference-facing abstraction.

Similar to Kubernetes:

```
Deployment
    |
    +-- ReplicaSet
          |
          +-- Pod
```

Users should interact with the desired inference workload, while controllers manage the underlying execution resources.

## 评论 (5)

### googs1025 · 2026-08-25

Thanks for the proposal. The direction sounds interesting, but the scope feels quite broad to me.

  `StormService` and `RayClusterFleet` currently seem to represent different layers: one for inference workload orchestration, and one for the underlying distributed runtime. I’m wondering why we need to merge these abstractions instead of keeping them separate and improving the integration between them.

  Maybe it would help to first clarify the concrete pain points in the current `StormService + RayClusterFleet` 

### lettycat · 2026-08-26

@googs1025 Thanks, that makes sense. After looking more closely at the current StormService implementation and documentation, I agree that merging the two abstractions may not be the right framing.

The more concrete pain point I see is actually that AIBrix now seems to provide two different ways to run distributed inference workloads, but the boundary between them is not very clear.

`StormService` already supports multi-pod workloads through `podGroupSize` and `PodSet`, and the installation documentation also mentions that KubeRay is optional and that StormService can be used for both single-node and multi-node inference.

At the same time, the current Multi-Node Inference documentation and the complete examples in the repository are still mainly based on `RayClusterFleet` / KubeRay.

So for a user who wants to deploy a multi-node vLLM workload, for example TP/PP across multiple nodes, it is not very clear when they should choose:

1. `StormService + PodSet`
2. `RayClusterFleet + KubeRay`

The concrete pain points I see are:

- The intended use cases and boundaries of these two abstractions are not clearly documented.
- The same inference intent, such as "run a vLLM model with TP/PP across multiple nodes", appears to have two different orchestration models.
- There is a complete RayClusterFleet-based multi-node example, but I could not find an equivalent end-to-end StormService + PodSet + vLLM multi-node example.
- From a user perspective, this makes it difficult to understand which abstraction is the recommended default for distributed inference.

So I think a narrower question may be:

> What is the intended relationship between StormService-based multi-node orchestration and RayClusterFleet-based distributed inference?

If they are intended to remain two parallel approaches, it may be useful to clearly document the selection criteria and provide equivalent examples for both.

If StormService is intended to become the primary inference workload abstraction, then perhaps the discussion could focus on whether integration with distributed runtimes such as RayClusterFleet should be improved, rather than merging the CRDs themselves.

Would this be closer to the intended architecture?

### googs1025 · 2026-08-28

I think what we need are more examples of using stormservice for multi-node inference. It would be great if you could help improve this.

### DsThakurRawat · 2026-08-28

on "we need more examples of using stormservice for multi-node inference", i went looking for what's actually there at `42ec3cf` first, and i think the gap is narrower and more fixable than it looks.

there is already a complete end-to-end StormService multi-node example: `samples/disaggregation/sglang/tp-1p1d.yaml`. it's `kind: StormService`, `podGroupSize: 2` on both the prefill and decode roles, and the containers run `--nnodes 2 --tp-size 2`, so it's genuinely TP across two nodes, not two pods on one. it's also the only sample in the whole repo that carries real multi-node engine flags, i grepped for `nnodes` across `samples/` and it's the single hit.

so @lettycat's read of the symptom is right but the cause is one step over: it isn't that no StormService multi-node example exists, it's that the one that does exist is filed under `samples/disaggregation/sglang/`, where you'd only find it if you were already looking for PD disaggregation rather than for multi-node TP.

the docs side is more clear-cut. `docs/source/features/multi-node-inference.rst` is 78 lines and contains zero occurrences of the string "StormService". it documents `RayClusterReplicaSet` and `RayClusterFleet` and says "most of the time, you only need to use RayClusterFleet". nothing in `docs/` references `tp-1p1d.yaml` at all. so a user following the multi-node page gets pointed at RayClusterFleet by omission, whatever the installation docs say about KubeRay being optional.

that suggests a cheaper first step than writing new examples: point the existing multi-node page at the example that's already in the tree, and say plainly when each abstraction applies. writing more samples doesn't help if the page a multi-node user actually lands on never mentions the abstraction you want them to use.

worth someone with more context than me confirming one thing before that gets written down though: whether `podGroupSize` + `PodSet` is considered ready to be the recommended path for plain multi-node TP, or whether the sglang sample works because it's specifically a PD-disaggregated topology. that answer decides whether the doc gains a section or a redirect.


### googs1025 · 2026-08-28

Thanks for checking the existing samples. I agree this makes the gap more concrete: the problem may not be that a StormService multi-node example is completely missing, but that the existing example is hard to discover from the multi-node inference docs.

  Once that boundary is clear, I think a good first improvement would be to update `docs/source/features/multi-node-inference.rst` to mention both paths, link the existing StormService sample, and explain when users should choose each abstraction.

