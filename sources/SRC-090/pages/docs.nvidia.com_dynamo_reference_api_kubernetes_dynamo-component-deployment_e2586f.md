source: https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment
lastmod: 2026-09-24T19:58:16.636Z

DynamoComponentDeployment (DCD) Reference


DynamoComponentDeployment (DCD) Reference

Field reference for the DynamoComponentDeployment custom resource — the single Dynamo component that a DynamoGraphDeployment reconciles into pods.

A `DynamoComponentDeployment`

(DCD) describes one component of a Dynamo inference graph — a frontend, a worker, a prefill or decode worker, a planner, or an EPP. The [operator](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/dynamo-operator) reconciles each DCD into a Kubernetes Deployment (or Grove workload) plus its Services, ConfigMaps, and pods.

A DCD is rarely authored on its own. Each entry in a `DynamoGraphDeployment`

`spec.components`

list is a `DynamoComponentDeploymentSharedSpec`

, the same shape documented here under [Shared component spec](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment#shared-component-spec). The operator creates one child DCD per component. Author a standalone DCD only when you want to manage a single component’s lifecycle independently; otherwise define components inside a DGD.

This page documents the `nvidia.com/v1beta1`

API — the served, current version.

This reference covers user-configurable spec fields. For operator-injected defaults (images, ports, probes, resources) and environment variables, see the [Dynamo Operator](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/dynamo-operator) guide.

## Minimal example

## Spec reference

The DCD spec is `backendFramework`

plus the [shared component spec](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment#shared-component-spec) inlined at the same level.

Inference backend framework for this component. Drives backend-specific defaults the operator injects into the `main`

container.

### Shared component spec

These fields are shared between a standalone DCD and each entry of a DGD `spec.components`

list. In a DGD, prefix them with `spec.components[*]`

.

Stable logical identifier for the component, unique within its parent DGD’s `spec.components`

list. Must match `^[A-Za-z0-9]([-A-Za-z0-9]*[A-Za-z0-9])?$`

, 1–63 characters. For a standalone DCD the defaulting webhook populates `name`

from `metadata.name`

, so you rarely set it explicitly. The name is decoupled from the underlying workload name so the operator can rename child workloads (for example, hash-suffixing worker DCDs during a rolling update) without losing the identity that labels, status maps, scaling adapters, planner RBAC, and EPP filters depend on.

Role of the component within the graph. Drives port mapping, frontend detection, planner RBAC, and the pod label `nvidia.com/dynamo-component-type`

. `prefill`

and `decode`

are first-class values for disaggregated serving and can be set directly. At most one component per graph may be `epp`

.

Desired number of pods for this component. Minimum `0`

. When `scalingAdapter`

is set, this field is owned by the [DynamoGraphDeploymentScalingAdapter](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/autoscaling) and should not be modified directly.

Pod template for the component’s pods. The operator injects its defaults (image, command, env, ports, probes, resources, volume mounts) into the container named `main`

, merging your overrides by name. If no `main`

container is present, the operator generates one. Every other container is treated as a user-managed sidecar and receives no injected defaults — sidecars must specify their own required fields such as `image`

. Replaces the ten separate per-component fields (`resources`

, `envs`

, `livenessProbe`

, and so on) that existed in `v1alpha1`

.

[core/v1.PodTemplateSpec](https://pkg.go.dev/k8s.io/api/core/v1#PodTemplateSpec)

Configures a multinode component. See [Multinode Deployments](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments).

Number of nodes to deploy. Minimum `2`

. Total GPUs used is `nodeCount × container GPU request`

.

Size of the tmpfs mounted at `/dev/shm`

. Omit to use the operator default (`8Gi`

); set a positive quantity for a custom size; set `"0"`

to disable the shared-memory volume entirely.

[resource.Quantity](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity)

Places the component in the global Dynamo namespace rather than the per-deployment namespace derived from the DGD name.

References a model served by this component. When set, a headless service is created for endpoint discovery.

Base model identifier, for example `llama-3-70b-instruct-v1`

.

Model revision or version.

Opts the component into a [DynamoGraphDeploymentScalingAdapter](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/autoscaling) (DGDSA). Set it — even as an empty object, `scalingAdapter: {}`

— to create a DGDSA that owns `replicas`

so external autoscalers (HPA, KEDA, Planner) can drive scaling through the Scale subresource. Omit the field to opt out.

Designates a container in `podTemplate.spec.containers`

as the frontend sidecar. The value must match a container `name`

in that list; the operator merges its frontend-sidecar defaults (Dynamo env vars, ports, health probes) into that container the same way it merges into `main`

. The validation webhook rejects values that match no container.

Configures a PVC-backed compilation cache. The operator handles backend-specific mount paths and environment variables, so you do not hand-wire them into `podTemplate`

.

Name of a user-created PVC, which must exist in the same namespace as the deployment.

Overrides the backend-specific default mount path. When empty, the operator selects a default appropriate for the backend framework.

EPP-specific configuration. Only valid when `type`

is `epp`

. Exactly one of `configMapRef`

or `config`

must be set. See the [Gateway API Routing Reference](https://docs.nvidia.com/dynamo/reference/components/gateway-api-routing).

References a user-provided ConfigMap key containing EPP configuration. Mutually exclusive with `config`

.

[core/v1.ConfigMapKeySelector](https://pkg.go.dev/k8s.io/api/core/v1#ConfigMapKeySelector)

EPP `EndpointPickerConfig`

supplied inline. The operator marshals it to YAML and creates the ConfigMap for you. Mutually exclusive with `configMapRef`

.

Component-level topology placement. See [Topology-Aware Scheduling](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/topology-aware-scheduling).

Topology domain to pack pods within. Must match a domain defined in the referenced `ClusterTopology`

. When the parent DGD also sets `spec.topologyConstraint.packDomain`

, this value must be narrower than or equal to it.

Opt-in preview features whose API shape may change in breaking ways between `v1beta1`

releases. Fields here are **not** covered by the normal `v1beta1`

deprecation policy — do not rely on them for production workloads.

See: [ExperimentalSpec](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment#experimentalspec)

## Status

The operator maintains observed state under `status`

.

Standard Kubernetes conditions. `Available`

reports whether the component is serving traffic; `DynamoComponentReady`

reports whether the underlying Dynamo component is ready.

[metav1.Condition](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Condition)

Most recent `metadata.generation`

the controller has reconciled. A component is up to date when this equals `metadata.generation`

.

Replica status for this component: desired, ready, and available counts. Shares the shape documented on the [DGD Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment#componentreplicastatus).

## Additional Types

Nested struct types referenced by the fields above, broken out here to keep the field lists shallow. Types prefixed `core/v1.`

, `metav1.`

, `resource.`

, or `runtime.`

are standard Kubernetes types and link to their Go package documentation instead of being expanded.

### ExperimentalSpec

Groups opt-in preview features for a component. Referenced by `experimental`

. Nested types (`GMSClientPodSpec`

, `ComponentCheckpointJobConfig`

, `DynamoCheckpointIdentity`

) are expanded inline under the field that references them.

These preview features can change or disappear between `v1beta1`

releases without a name-preserving graduation path. They are excluded from the `v1beta1`

deprecation policy — do not rely on them for production workloads.

Configures the GPU Memory Service (GMS). When set, GPU access for GMS clients is managed through Dynamic Resource Allocation (DRA), and the operator replaces the `main`

container’s GPU resources with a DRA `ResourceClaim`

.

Selects the GMS deployment topology.

Allowed values: IntraPod InterPodThe DRA `DeviceClass`

to request GPUs from.

Additional user-declared containers that should be wired as GMS clients in service pods. Checkpoint Job clients are declared under the checkpoint job’s `gmsClientContainers`

instead. In each rendered pod, only matching container names are wired; absent names are ignored. Each name must match `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`

, 1–63 characters.

Additional GMS client pods for inter-pod GMS. Reserved for future use and rejected until inter-pod client orchestration is wired.

Identifies this client pod. Must match `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`

, 1–63 characters.

Configures the pod to run as a GMS client.

[core/v1.PodTemplateSpec](https://pkg.go.dev/k8s.io/api/core/v1#PodTemplateSpec)

Configures active-passive GPU failover for a worker component. The `main`

container is cloned into two engine containers (active + standby) sharing GPUs via DRA, and the standby acquires the flock when the active engine fails. Requires `gpuMemoryService`

to be set, `failover.mode`

to match `gpuMemoryService.mode`

, and the `nvidia.com/dynamo-kube-discovery-mode: container`

annotation on the DGD.

Failover deployment topology. Must match the GMS `mode`

on the same component.

Number of shadow (standby) engine containers per rank. Reserved for future use; the operator currently creates exactly one shadow. Minimum `1`

, maximum `1`

.

Configures container-image snapshotting and restore for the component. Set `checkpoint.enabled: true`

to opt in; omit `checkpointRef`

for a DGD-managed automatic checkpoint, or set it to restore an existing [DynamoCheckpoint](https://docs.nvidia.com/dynamo/kubernetes/operations/cold-start-optimizations/dynamo-snapshot).

Whether checkpointing is enabled for this component. When `true`

, omit `checkpointRef`

for a DGD-managed automatic checkpoint, or set `checkpointRef`

to restore an existing checkpoint. Omit the `checkpoint`

block, or set `enabled: false`

, to disable checkpointing.

When normal worker replicas are started relative to automatic checkpoint readiness. `Immediate`

starts workers cold immediately, and later pods restore from the checkpoint once it is Ready. `WaitForCheckpoint`

keeps worker replicas at zero until the checkpoint is Ready, then starts them from it.

Whether a DGD-managed automatic checkpoint CR and artifact are deleted or retained when the owning DGD is deleted. Explicit `checkpointRef`

checkpoints are never owned or deleted by the DGD.

References an existing `DynamoCheckpoint`

CR by `metadata.name`

. When set, this component’s `identity`

is ignored and the referenced checkpoint is used directly.

The workload container to snapshot and restore. Must match `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`

, 1–63 characters.

Customizes the DGD-managed checkpoint Job.

Checkpoint Job containers that should receive GMS client wiring. Requires `gpuMemoryService`

on the component. Each name must match `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`

, 1–63 characters.

Customizes the checkpoint Job pod. The operator starts from the selected workload container and merges this template, so you can add helper containers such as `gms-saver`

.

[core/v1.PodTemplateSpec](https://pkg.go.dev/k8s.io/api/core/v1#PodTemplateSpec)

Deprecated: omit `mode`

. Use `enabled: true`

without `checkpointRef`

for a DGD-managed automatic checkpoint, or use `checkpointRef`

to restore a named checkpoint.

Deprecated: omit for DGD-managed checkpoints; no action is needed. Use `checkpointRef`

to restore an existing checkpoint. Legacy checkpoint identity duplicated from `v1alpha1`

; `DynamoCheckpoint`

itself remains `v1alpha1`

.

Model identifier, for example `meta-llama/Llama-3-70B`

.

Runtime framework.

Allowed values: vllm sglang trtllmDynamo platform version.

Tensor parallel configuration. Deprecated: checkpoint launch uses the pod template instead. Minimum `1`

.

Pipeline parallel configuration. Deprecated: checkpoint launch uses the pod template instead. Minimum `1`

.

Data type, for example `fp16`

, `bf16`

, or `fp8`

.

Maximum sequence length. Minimum `1`

.

Additional parameters that affect the checkpoint hash.