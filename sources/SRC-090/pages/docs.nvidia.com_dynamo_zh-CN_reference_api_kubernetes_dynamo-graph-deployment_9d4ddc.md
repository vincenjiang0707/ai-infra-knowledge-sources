source: https://docs.nvidia.com/dynamo/zh-CN/reference/api/kubernetes/dynamo-graph-deployment
lastmod: 2026-09-23T23:30:39.914Z

DynamoGraphDeployment (DGD) Reference


DynamoGraphDeployment (DGD) Reference

Field reference for the DynamoGraphDeployment custom resource — the canonical, live description of a Dynamo inference graph.

A `DynamoGraphDeployment`

(DGD) is the canonical description of a running Dynamo inference graph. You list the components that make up the graph — frontend, workers, prefill and decode workers, planner, EPP — and the [operator](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/dynamo-operator) reconciles them into [ DynamoComponentDeployment](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment) resources, pods, and Services.

A DGD is the resource that persists and serves traffic. Author one directly when you have a known-good configuration or a tuned [recipe](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/recipes); generate one from intent with a [ DynamoGraphDeploymentRequest](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request) (DGDR).

This page documents the `nvidia.com/v1beta1`

API — the served, current version.

Each entry in `spec.components`

is a `DynamoComponentDeploymentSharedSpec`

— the same fields documented on the [DCD Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment#shared-component-spec). This page covers the **graph-level** fields; per-component fields live there.

## Minimal example

## Spec reference

Components deployed as part of this graph. Each entry carries its own stable logical `name`

(unique within the list, case-insensitively). Component types are repeatable except `type: epp`

, which may appear at most once. Maximum 25 components. For the full per-component field set, see [DCD Reference — Shared component spec](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment#shared-component-spec).

Backend framework for the graph. Sets backend-specific defaults the operator injects into each component’s `main`

container.

Environment variables prepended to every component’s environment. A component-specific `env`

entry with the same name takes precedence and may reference values from this list.

[core/v1.EnvVar](https://pkg.go.dev/k8s.io/api/core/v1#EnvVar)

Annotations propagated to all child resources (scaling adapters, DCDs, Deployments, and pod templates). Component-level `podTemplate`

values take precedence on conflict.

Labels propagated to all child resources. Same precedence rules as `annotations`

.

Name of the `PriorityClass`

to use for Grove `PodCliqueSet`

s. Requires the Grove pathway. See [Grove](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/grove).

Restart policy for the graph. Change `restart.id`

to trigger a restart.

Arbitrary string; any change to it initiates a restart of the graph according to the configured strategy.

How components are restarted.

Whether components restart one at a time or all at once.

Allowed values: Sequential ParallelComplete ordered set of component names for a sequential restart. Omit to use the controller’s default order. Must not be set for parallel restarts.

Deployment-level topology constraint. Components without their own `topologyConstraint`

inherit this value. See [Topology-Aware Scheduling](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/topology-aware-scheduling).

Name of the `ClusterTopology`

resource defining the topology hierarchy for this deployment.

Default topology domain to pack pods within. Optional at this level; omit when only components carry constraints.

Graph-level opt-in preview features whose API shape may change in breaking ways between `v1beta1`

releases. Component-level experimental features live under `spec.components[*].experimental`

instead — see [DCD Reference — ExperimentalSpec](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-component-deployment#experimentalspec).

Topology-aware routing for KV-cache transfers between prefill and decode workers. Set exactly one of `labelKey`

or `clusterTopologyName`

. See [Topology-Aware KV Transfer](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/topology-aware-kv-transfer).

References a Grove `ClusterTopology`

CR. The operator reads the CR’s topology levels and projects them through Dynamo-owned pod labels for worker topology metadata. Mutually exclusive with `labelKey`

.

A Kubernetes node label key (for example `topology.kubernetes.io/zone`

) whose value identifies the topology domain for each worker. The operator copies the node label onto worker pods so the runtime can publish it as worker metadata. Should correspond to the topology level named in `domain`

. Mutually exclusive with `clusterTopologyName`

.

Logical name for the topology level to enforce (for example `zone`

, `rack`

). The router uses this to match workers that share the same value for the label identified by `labelKey`

. Free-form string matching `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`

.

How the selected prefill worker’s topology is applied to decode routing. `required`

allows only decode workers in the same topology domain as the selected prefill worker; `preferred`

keeps all decode workers eligible but biases selection toward the same domain.

Required and used only when `enforcement`

is `preferred`

. Higher values create a stronger same-domain routing preference but do not guarantee same-domain selection; the value is not a probability. `0`

disables the topology preference; `1`

is the strongest supported preference. Minimum `0`

, maximum `1`

.

## Status

The operator maintains observed state under `status`

.

High-level textual status of the graph deployment lifecycle.

Latest observed conditions, merged by type. Includes `Available`

and `DynamoComponentReady`

.

[metav1.Condition](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Condition)

Per-component replica status, keyed by component name.

Most recent `metadata.generation`

observed by the controller.

Status of a graph-level restart in progress.

The restart ID currently being processed. Matches `spec.restart.id`

.

Phase of the restart.

Allowed values: Pending Restarting Completed Failed SupersededNames of the components currently being restarted.

Per-component checkpoint status, keyed by component name. See [Snapshot and Restore](https://docs.nvidia.com/dynamo/kubernetes/operations/cold-start-optimizations/dynamo-snapshot).

Progress of operator-managed rolling updates. Currently supported only for single-node, non-Grove deployments. See [Rolling Update](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/rolling-update).

Current phase of the rolling update.

Allowed values: Pending InProgress Completed FailedWhen the rolling update began.

[metav1.Time](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Time)

When the rolling update completed, successfully or failed.

[metav1.Time](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Time)

Components that have completed the rolling update.

## Additional Types

Nested struct types referenced by the status fields above, broken out here to keep the field lists shallow. Types prefixed `core/v1.`

or `metav1.`

are standard Kubernetes types and link to their Go package documentation instead of being expanded.

### ComponentReplicaStatus

Replica information for a single component, keyed by component name in `status.components`

.

Underlying Kubernetes resource kind backing the component.

Allowed values: PodClique PodCliqueScalingGroup Deployment LeaderWorkerSetUnderlying Kubernetes resource names for this Dynamo component. During normal operation this contains a single name; during rolling updates it contains both the old and new resource names.

Total number of non-terminated replicas. Minimum `0`

.

Number of replicas at the current/desired revision. Minimum `0`

.

Number of ready replicas. Populated for `PodClique`

, `Deployment`

, and `LeaderWorkerSet`

; not available for `PodCliqueScalingGroup`

. Minimum `0`

.

Number of available replicas. Populated for `Deployment`

and `PodCliqueScalingGroup`

; not available for `PodClique`

or `LeaderWorkerSet`

. Minimum `0`

.

### ComponentCheckpointStatus

Checkpoint information for a single component, keyed by component name in `status.checkpoints`

.

Name of the associated `DynamoCheckpoint`

CR.

Artifact ID used by the snapshot protocol.

Computed hash of the checkpoint identity. Deprecated: automatic checkpoints use `checkpointID`

; this field is retained for older status consumers.

Whether the checkpoint artifact is ready for future pods to restore.