# [Issue #2560] Discussion: First-class image warmup workflow for AIBrix model workloads

source: https://github.com/vllm-project/aibrix/issues/2560
state: open | updated: 2026-09-25T03:43:27Z
labels: area/disaggregated, area/orchestration

## 正文

## Proposal

Add a first-class `ModelWarmup` workflow for AIBrix model workloads.

The initial scope is intentionally small: preload large inference/runtime images onto nodes before rollout or scale-out. This addresses cases where traffic arrives while a newly-created Pod is still waiting for the container runtime to pull and unpack images.

This issue is for design discussion. The API and controller behavior are not finalized.

## Business value

Image pulling is a major source of cold-start latency for model-serving workloads. It is especially visible during:

- autoscaler scale-out, when a new replica lands on a node without the required image cache;
- StormService or RoleSet rolling updates, when the new revision is not yet ready but traffic is already increasing;
- manual capacity preparation, where operators want to warm nodes before exposing them to serving traffic.

A first-class workflow should make image warmup observable through Kubernetes status and provide a verify-before-rollout/scale workflow.

## Proposed MVP

Introduce a standalone `ModelWarmup` CRD under `model.aibrix.ai/v1alpha1`.

```yaml
apiVersion: model.aibrix.ai/v1alpha1
kind: ModelWarmup
metadata:
  name: qwen-image-warmup
spec:
  targets:
  - nodes:
      names:
      - gpu-node-a
      - gpu-node-b
  - nodeSelector:
      matchLabels:
        resource-pool.aibrix.ai/name: latency-pool
  - workload:
      ref:
        apiVersion: orchestration.aibrix.ai/v1alpha1
        kind: StormService
        name: qwen
      subTarget:
        roleName: prefill

  imagePreload:
    images:
    - registry.example.com/vllm@sha256:...
    - registry.example.com/aibrix-runtime@sha256:...
    pullSecrets:
    - name: registry-secret

  policies:
    parallelism: 8
    globalTimeoutSeconds: 1800
    retryLimit: 2
    ttlSecondsAfterFinished: 3600
```

## Target selection

All of the following target sources should be supported:

1. **Explicit nodes**: a list of node names.
2. **Node labels, capabilities, or resource pools**: a Kubernetes `LabelSelector`, for example an AIBrix resource-pool label. This mode should discover matching nodes added later for autoscaler scale-out.
3. **AIBrix workloads**: resolve nodes from `StormService`, `RoleSet`, `Deployment`, `ModelClaim`, or `ModelAdapter` Pods, with role-level filtering such as `prefill` or `decode` where applicable.

Multiple target entries are allowed. The controller should take the union of all resolved targets and deduplicate by node name. This allows operators to combine a resource pool, a workload's current nodes, and explicitly reserved nodes.

A workload reference describes the current workload placement. It does not by itself guarantee coverage of future scale-out nodes; use a node selector/resource-pool target for that purpose.

## Execution model

The controller should:

1. Resolve all target sources.
2. Union and deduplicate target nodes.
3. Calculate a deterministic revision from the target and image configuration.
4. Create one node-pinned warmup Job per target node and revision.
5. Run one short-lived regular container per unique image so image pulls can proceed independently.
6. Update per-node and aggregate status from Job completion.
7. Reconcile newly matching nodes, failed Jobs, stale targets, retries, and TTL cleanup.

Warmup Jobs should use `nodeName` or required node affinity, support the target node's taints and architecture, use configured pull secrets, and avoid requesting GPU resources for image-only warmup. Image entrypoints should be overridden so an inference server does not start accidentally.

A Job is preferred over a bare Pod because it provides retry and completion semantics and can recreate a deleted warmup Pod.

## Suggested status

```yaml
status:
  phase: Pending|Running|Succeeded|Failed|Degraded
  observedRevision: ...
  desiredNodes: 2
  activeNodes: 1
  succeededNodes: 1
  failedNodes: 0
  startTime: ...
  completionTime: ...
  targets:
  - nodeName: gpu-node-a
    source: NodeSelector
    phase: Succeeded
    jobName: qwen-image-warmup-gpu-node-a
    reason: ImagePreloadSucceeded
    message: ...
  conditions: []
```

Image references should preferably be immutable digests, or the controller should record the resolved digest. A changed image list or target configuration must create a new revision and invalidate the previous result.

## MVP boundaries

The first implementation focuses on image preloading only. It should not yet include:

- model artifact/file download;
- engine startup or inference warmup;
- generic arbitrary commands or custom actions;
- automatic rollout blocking or autoscaler mutation;
- direct runtime sidecar RPC integration.

The status and API should remain extensible for later artifact, engine, and precheck stages. Existing StormService, RoleSet, ModelClaim, and PodAutoscaler behavior must remain unchanged unless warmup integration is explicitly enabled.

## Why keep warmup independent?

Warmup is useful before rollout, scale-out, and manual capacity preparation. A standalone resource provides reusable target selection, independent lifecycle and status, and a foundation for future integration with workload controllers without coupling the first implementation to a single workload type.

## Open questions

- Should the kind remain `ModelWarmup`, or should the image-only MVP use `ModelImageWarmup`?
- Should `StormService`, `RoleSet`, and `NodeSelector` be the initial supported target sources, with other workload kinds added later?
- Should failed Jobs be retained by default until TTL cleanup?
- Should the default failure behavior be fail-closed, degraded success, or require an explicit policy?


## 评论 (7)

### googs1025 · 2026-08-13

cc @Jeffwan 

This is just a discussion of a possible direction; it doesn't mean we'll start working on.

### googs1025 · 2026-09-12

## Possible follow-up stages and related tooling

The ImageReady workflow should remain the first implementation milestone. The same resource could later grow optional, independently observable stages without expanding the MVP:

- **ArtifactReady**: download model weights into a cache that is explicitly shared with the eventual serving Pod. This should build on AIBrix's existing `aibrix_download` flow, with checksum/version validation, disk-space checks, credentials, and download locking.
- **Precheck / diagnostics**: validate the node and Pod environment before allowing rollout or scale-out to proceed. This could cover GPU visibility, GPU topology, CPU/PCI information, RDMA connectivity, NIXL readiness, and P/D-specific prerequisites.


In particular, its preflight checks collect GPU topology and host information before vLLM starts, while its networking tests cover GPU topology, RDMA bandwidth/latency, NCCL/RCCL communication, and NIXL/UCX transfer paths. These capabilities may be reusable or provide a model for a future AIBrix precheck stage, especially for P/D disaggregation and NIXL/RDMA deployments.

A possible long-term flow is:

```text
ImageReady
  -> ArtifactReady
  -> PrecheckReady
```

These follow-up stages should not be required for the initial image-preload implementation, but the API/status design should leave room for them.


### googs1025 · 2026-09-12

cc @Jeffwan @varungup90 @scarlet25151 /PTAL 😄 

### varungup90 · 2026-09-12

## Design feedback

Strong proposal overall, and the MVP boundaries look right. Image pull is a real cold-start gap in AIBrix today, and treating it as a standalone, observable workflow is cleaner than bolting it onto StormService or PodAutoscaler first.

### What works well

**The problem is real.** Scale-out and StormService/RoleSet rollouts still pay kubelet pull/unpack cost with no first-class way to prepare nodes or verify readiness. ModelClaim warm pools, HistoricalNode preference, and `aibrix_download` help *process* and *weight* locality — not CRI image cache.

**A standalone CR is the right shape.** Warmup is useful before rollout, scale-out, and manual capacity prep. Coupling it to one workload type would either miss ModelAdapter/Deployment/ModelClaim cases or force invasive controller changes. That matches how ModelAdapter and ModelClaim already sit beside workloads.

**MVP scope is disciplined.** Image-only first, with no artifact download, engine warmup, or autoscaler mutation. Extending later to `ImageReady → ArtifactReady → PrecheckReady` is sensible; those stages are orthogonal and should stay independently observable.

**The execution model is practical.** Per-node Jobs, no GPU requests, overridden entrypoints, digests/revision invalidation, and unioned targets (nodes + selectors + workload refs) are the right primitives.

### Suggestions / open points

1. **Naming:** Prefer `ModelImageWarmup` for the image-only MVP (or keep `ModelWarmup` but make `imagePreload` the only stage in v1). `ModelWarmup` implies engine/artifact warmup that people will expect immediately.

2. **Don't over-index on workload refs in MVP.** Start with `nodeNames` + `nodeSelector` (resource pools). Workload-derived nodes only cover *current* placement; future scale-out still needs selectors. Support StormService/RoleSet next; ModelClaim/ModelAdapter can wait.

3. **Failure policy should be explicit.** Default to `Degraded` with per-node status, not fail-closed. Fail-closed only matters once something actually gates rollout/scale — and the MVP correctly does not.

4. **Image pull ≠ shared artifact cache.** Worth calling out clearly in the design. A successful image Job does not put weights on disk; a later `ArtifactReady` stage should reuse `aibrix_download` + hostPath/PVC locking, not the same Job container model.

5. **Watch node disk and GC.** Preloading multi-GB images across a pool can thrash containerd/kubelet GC and compete with serving pods. Cap concurrency, prefer digests, and consider node pressure signals before treating Succeeded as "safe forever."

6. **Keep integration opt-in.** Status consumers (operators, CI, later StormService/PodAutoscaler gates) should read conditions; don't mutate replica counts or block rollouts until there is a clear policy API.

### Verdict

Worth pursuing as a design track. The standalone CR + image-only MVP + extensible status aligns well with how AIBrix already separates orchestration from attachment workflows.

I'd greenlight design/prototyping on node + selector targets and Job-based preload, and defer workload refs, ArtifactReady, and prechecks until the status model proves useful in practice.

### googs1025 · 2026-09-16

Thanks for the detailed feedback — I agree with the overall direction, especially keeping the MVP focused on explicit node names and node selectors, using per-node Jobs, reporting partial failures as `Degraded`, and leaving workload-derived targets, artifact download, prechecks, and rollout/autoscaler gating for later iterations.

One point where I would prefer to keep the original proposal is the resource name. I think `ModelWarmup` is the better long-term API name. Although the v1alpha1 MVP only implements image preloading, the resource is intended to represent an extensible warmup workflow that may later contain independently observable stages such as:

```text
ImageReady
  -> ArtifactReady
  -> PrecheckReady
```

To avoid overpromising, the initial API should expose only `spec.imagePreload`, and the documentation should state clearly that artifact download and engine warmup are not supported yet. Future stages should have separate conditions and lifecycle status rather than being folded into a single ambiguous `Ready` state.

I also agree that image warmup status must be treated as a point-in-time observation rather than a permanent guarantee, since kubelet/container-runtime garbage collection may evict a previously pulled image. We should capture that explicitly in the status semantics and design the revision per warmup configuration so that a newly matched node can be reconciled without invalidating successful nodes unnecessarily.

So my preferred MVP is: keep the `ModelWarmup` kind, implement only `imagePreload`, start with node names and node selectors, keep integration opt-in, and defer the broader stages and workload references until the status and execution model have proven stable.

### googs1025 · 2026-09-20

will handle this feature in these week 

### googs1025 · 2026-09-25

A possible future extension is to introduce generic node-scoped warmup hooks.

The ModelWarmup MVP can remain focused on target resolution, image preloading, and status reporting. Hooks would provide an extensibility point for user-defined node actions without coupling AIBrix to a specific implementation such as GPU checks.

For example:

```yaml
spec:
  hooks:
  - name: gpu-health
    phase: BeforeWarmup
    target: Node
    failurePolicy: Block
    timeoutSeconds: 60
    retryLimit: 1
    executor:
      pod:
        image: registry.example.com/gpu-check:v1
        command:
        - /bin/check-gpu
        args:
        - --json
```

The lifecycle could be:

1. Resolve target nodes.
2. Execute BeforeWarmup hooks.
3. Run image warmup.
4. Execute AfterWarmup hooks.
5. Aggregate per-node status.

The first implementation could support a Pod-based executor. Future executors could include Jobs, HTTP integrations, or custom providers.

The hook contract can remain generic:

- exit code 0 means success;
- non-zero exit code, timeout, or Pod failure means failure;
- stdout may optionally contain structured JSON with reason, message, and arbitrary observations.

This would allow users to implement GPU health checks, driver checks, network or RDMA validation, cache preparation, external system integration, or post-warmup verification without adding workload-specific logic to the AIBrix controller.

A possible status shape would be:

```yaml
status:
  phase: Warming
  targets:
  - nodeName: node-a
    hooks:
    - name: gpu-health
      phase: Succeeded
      reason: NodeReady
      message: GPU check passed
      podName: warmup-hook-gpu-health-node-a
    imageWarmup:
      phase: Succeeded
```

This keeps the core workflow small while establishing a general Node-scoped Warmup Hooks extension point.
